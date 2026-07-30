"""
Fast float scan for Max-bound violators in the crux regime (m=4, n=3),
then EXACT Fraction verification of the candidates found.
"""
import numpy as np
from fractions import Fraction as F

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] * (1 if i % 2 == 0 else -1) for i in range(len(s)))

def bp_splits_f(piece, all_pieces):
    cs = {piece / 2.0}
    for p in all_pieces:
        if 0 < p < piece:
            cs.add(p); cs.add(piece - p)
    return [(q, piece - q) for q in cs if 0 < q < piece]

_MEMO = {}
def min_D_bp_f(config, k):
    key = (tuple(sorted(round(x,12) for x in sorted(config, reverse=True))), k)
    if key in _MEMO: return _MEMO[key]
    best = D_of(config)
    if k == 0:
        _MEMO[key] = best; return best
    cs = sorted(config, reverse=True)
    for i in range(len(cs)):
        piece = cs[i]; rest = cs[:i]+cs[i+1:]
        for (q,r) in bp_splits_f(piece, cs):
            d = min_D_bp_f(rest+[q,r], k-1)
            if d < best: best = d
    _MEMO[key] = best; return best

# integer partition scan (float)
viol_cfgs = []
for D in range(8, 80):
    for p in range(max(1,D//4), D):
        for q in range(max(1,(p+1)//2), min(p, D-p-1)+1):  # p<2q => q>p/2; p>=q
            rem = D-p-q
            if rem < 2: continue
            for r in range(max(1,(p)//2+1), min(q, rem)+1):  # r>p/2, r<=q
                s = rem - r
                if s < 1 or s > r: continue
                cfg = [p/D, q/D, r/D, s/D]
                _MEMO.clear()
                d = min_D_bp_f(cfg, 3)
                bound = (p/D)/8
                if d > bound + 1e-9:
                    viol_cfgs.append((p,q,r,s,D, d, bound, d/bound))
    if D % 20 == 0:
        print(f"scanned D={D}, viol so far={len(viol_cfgs)}")

viol_cfgs.sort(key=lambda x: -x[7])
print(f"\nTotal float violations: {len(viol_cfgs)}")
print("Top 15 float violators:")
for (p,q,r,s,D,d,b,ratio) in viol_cfgs[:15]:
    print(f"  ({p},{q},{r},{s})/{D} D*={d:.6f} M/8={b:.6f} ratio={ratio:.5f}")

# EXACT verify the top candidates
print("\nExact Fraction verification:")
def D_of_e(ps):
    s = sorted(ps, reverse=True)
    v = F(0)
    for i,x in enumerate(s): v += x*(1 if i%2==0 else -1)
    return v
def bp_splits_e(piece, allp):
    cs = {piece/2}
    for p in allp:
        if 0 < p < piece: cs.add(p); cs.add(piece-p)
    return [(q,piece-q) for q in cs if 0<q<piece]
def min_D_e(cfg, k):
    best = D_of_e(cfg)
    if k==0: return best
    cs = sorted(cfg, reverse=True)
    for i in range(len(cs)):
        piece=cs[i]; rest=cs[:i]+cs[i+1:]
        for (q,r) in bp_splits_e(piece, cs):
            d = min_D_e(rest+[q,r], k-1)
            if d<best: best=d
    return best

for (p,q,r,s,D,_,_,_) in viol_cfgs[:10]:
    cfg = [F(p,D),F(q,D),F(r,D),F(s,D)]
    d = min_D_e(cfg, 3)
    bound = F(p,D)/8
    target = F(1,15)
    print(f"  ({p},{q},{r},{s})/{D}: D*={d}={float(d):.8f} M/8={bound}={float(bound):.8f} "
          f"ratio={float(d/bound):.6f} viol={d>bound}  D*<1/15={d<target}")
