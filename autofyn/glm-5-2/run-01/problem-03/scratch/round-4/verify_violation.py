"""
Verify the apparent Max-bound violation with EXACT Fraction arithmetic.
Config: [0.32765, 0.2863, 0.23565, 0.1504] (approx from dirichlet).
We need the exact rational. Let's reconstruct from the trace and also re-search
with Fraction-based optimizer to find a true rational violator if any.
"""
from fractions import Fraction as F

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] * (1 if i % 2 == 0 else -1) for i in range(len(s)))

def bp_splits(piece, all_pieces):
    cs = {piece / 2}
    for p in all_pieces:
        if 0 < p < piece:
            cs.add(p); cs.add(piece - p)
    return [(q, piece - q) for q in cs if 0 < q < piece]

def min_D_bp_exact(config, k):
    best = D_of(config)
    if k == 0: return best
    cfg_sorted = sorted(config, reverse=True)
    for i in range(len(cfg_sorted)):
        piece = cfg_sorted[i]
        rest = cfg_sorted[:i] + cfg_sorted[i+1:]
        for (q, r) in bp_splits(piece, cfg_sorted):
            new = rest + [q, r]
            d = min_D_bp_exact(new, k - 1)
            if d < best: best = d
    return best

# Reconstruct the violating config as a Fraction.
# The dirichlet output was [0.32765, 0.2863, 0.23565, 0.1504].
# Let's find the exact rational by limit_denominator.
vals = [0.32765, 0.2863, 0.23565, 0.1504]
# Actually these are rounded displays. Let's instead directly test the
# RATIO a1:a2:a3:a4 that the dirichlet produced.
# From the trace: split a1=0.32765 -> 0.04135+0.28630 (so a1-a2 = 0.04135).
# a2=0.28630, a3=0.23565, a4=0.15040.
# Let's use a grid of small denominators to find a clean rational violator.

# Strategy: test configs (p,q,r,s)/D for small integer p,q,r,s.
# crux: p<2q, r>p/2, p>=q>=r>=s, p+q+r+s=D.
# We want D*/(p/D / 8) > 1, i.e. D* * D / p > 1/8... no, D* <= p/(D*8).
# Actually bound is M/2^n = (p/D)/8. D* is computed on the normalized config.
# Let's just search integer partitions.

best_viol = F(0); best_cfg=None
viol_count = 0
# D from 8 to 40, 4-part partitions p>=q>=r>=s>=1, p+q+r+s=D
for D in range(8, 60):
    for p in range(D//4, D):  # p is largest, >= D/4
        if p < 1: continue
        for q in range(1, min(p, D-p)+1):
            if q > p: break
            rem = D - p - q
            if rem < 2: continue
            for r in range(1, min(q, rem)+1):
                s = rem - r
                if s < 1 or s > r: continue
                # crux: p < 2q and r > p/2
                if not (p < 2*q and 2*r > p): continue
                cfg = [F(p,D), F(q,D), F(r,D), F(s,D)]
                d = min_D_bp_exact(cfg, 3)
                bound = F(p, D) / 8
                if d > bound:
                    ratio = d / bound
                    if ratio > best_viol:
                        best_viol = ratio; best_cfg = (p,q,r,s,D)
                        viol_count += 1
                        if viol_count <= 20:
                            print(f"VIOL: ({p},{q},{r},{s})/{D} D*={float(d):.6f} M/8={float(bound):.6f} ratio={float(ratio):.5f}")
    if D % 10 == 0:
        print(f"  ... scanned D={D}, viol so far={viol_count}, best={float(best_viol):.5f}")

print()
print(f"Total violations found: {viol_count}")
print(f"Best violation ratio: {float(best_viol):.5f}")
if best_cfg:
    p,q,r,s,D = best_cfg
    print(f"Best violating config: ({p},{q},{r},{s})/{D}")
    cfg = [F(p,D), F(q,D), F(r,D), F(s,D)]
    d = min_D_bp_exact(cfg, 3)
    print(f"  D* = {d} = {float(d):.6f}")
    print(f"  M/8 = {F(p,D)/8} = {float(F(p,D)/8):.6f}")
    print(f"  target 1/15 = {float(F(1,15)):.6f}")
    print(f"  D* < 1/15? {d < F(1,15)}  (the actual upper bound)")
