"""
Round 4 — focused crux investigation.
Key finding (preliminary): for m=3 crux (a1<2a2, a3>a1/2, 3 pieces),
n=3 marks drive D to 0. The crux is only hard for m>=4 (tail after top-3 cancel).
"""
import numpy as np
import sys

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] * (1 if i % 2 == 0 else -1) for i in range(len(s)))

def bp_splits(piece, all_pieces):
    cs = {piece / 2.0}
    for p in all_pieces:
        if 0 < p < piece:
            cs.add(p); cs.add(piece - p)
    return [(q, piece - q) for q in cs if 0 < q < piece]

_MEMO = {}
def min_D_bp(config, k):
    key = (tuple(sorted(round(x,12) for x in sorted(config, reverse=True))), k)
    if key in _MEMO: return _MEMO[key]
    best = D_of(config)
    if k == 0:
        _MEMO[key] = best; return best
    cfg_sorted = sorted(config, reverse=True)
    for i in range(len(cfg_sorted)):
        piece = cfg_sorted[i]
        rest = cfg_sorted[:i] + cfg_sorted[i+1:]
        for (q, r) in bp_splits(piece, cfg_sorted):
            new = rest + [q, r]
            d = min_D_bp(new, k - 1)
            if d < best: best = d
    _MEMO[key] = best; return best

def min_D_bp_trace(config, k):
    best = D_of(config); best_seq = []
    if k == 0: return best, best_seq
    cfg_sorted = sorted(config, reverse=True)
    for i in range(len(cfg_sorted)):
        piece = cfg_sorted[i]
        rest = cfg_sorted[:i] + cfg_sorted[i+1:]
        for (q, r) in bp_splits(piece, cfg_sorted):
            new = rest + [q, r]
            d, seq = min_D_bp_trace(new, k - 1)
            if d < best - 1e-12:
                best = d; best_seq = [(piece, q, r)] + seq
    return best, best_seq

# ===== m=3 crux n=3: confirm D*=0 =====
print("="*70)
print("m=3 crux n=3: confirm Xiang drives D to 0")
print("="*70)
_MEMO.clear()
for c in [[0.41,0.38,0.21],[0.4,0.35,0.25],[0.43,0.35,0.22]]:
    d,seq = min_D_bp_trace(list(c), 3)
    print(f'cfg={c} D*={d:.6f} moves={[(round(p,4),round(q,4),round(r,4)) for (p,q,r) in seq]}')

# ===== m=4 crux n=3: the real crux =====
print()
print("="*70)
print("m=4 crux n=3: a1<2a2, a3>a1/2, 4 pieces sum=1")
print("="*70)
n=3
_MEMO.clear()
rng = np.random.default_rng(123)
worst_r=0; worst_cfg=None; worst_d=None; worst_b=None; viol=0
all4=[]
trials=0
for _ in range(2000):
    for _ in range(50):
        raw = rng.dirichlet([1]*4)
        c = sorted(raw, reverse=True)
        if c[0] < 2*c[1] and c[2] > c[0]/2: break
    else: continue
    trials+=1
    d = min_D_bp(list(c), n)
    M=c[0]; b=M/8
    if d > b + 1e-7:
        viol+=1
        if viol<=5: print(f"  VIOL: D*={d:.6f} > M/8={b:.6f}, c={[round(x,5) for x in c]}")
    r = d/b if b>1e-12 else 0
    all4.append((r,c,d,b))
    if r > worst_r:
        worst_r=r; worst_cfg=list(c); worst_d=d; worst_b=b

print(f"n={n} m=4: {trials} configs, violations={viol}")
print(f"  worst ratio={worst_r:.5f} cfg={[round(x,5) for x in (worst_cfg or [])]}")
print(f"  D*={worst_d}  M/8={worst_b}")
all4.sort(reverse=True)
print(f"  top 8 worst:")
for r,c,d,b in all4[:8]:
    print(f"    ratio={r:.5f} cfg={[round(x,5) for x in c]} D*={d:.6f} M/8={b:.6f}")

# trace the worst
if worst_cfg:
    _MEMO.clear()
    d,seq = min_D_bp_trace(list(worst_cfg), 3)
    print(f"  worst trace: D*={d:.6f}")
    final = list(worst_cfg)
    for (p,q,r) in seq:
        idx = final.index(p); final = final[:idx]+final[idx+1:]+[q,r]
    sf = sorted(final, reverse=True)
    print(f"  final={sf} D={D_of(sf):.6f}")
    for (p,q,r) in seq:
        print(f"    split {p:.5f} -> {q:.5f}+{r:.5f}")
