"""
Majorization monotonicity test: is D*(L) = min_Xiang D(L) monotone in the
majorization (Lorenz) order on Liu configs, with the tower as maximal element?

Majorization: A majorizes B (A >=_maj B) iff for all k, sum of k largest of A
>= sum of k largest of B (totals equal). A more "spread/unequal".

Hypothesis (G1): D* is Schur-convex (non-decreasing in majorization), tower = max.
Counter-hypothesis: single piece (1,0,..) is the MOST majorizing, but D* small.

We test n=3 (Xiang 3 marks), m in {1,2,3,4}. Pad to 4 pieces with zeros for
majorization comparison. Compute D* and the majorization rank.
"""
import numpy as np
from xiang_optimizer import min_D

def majors(a, b):
    """a majorizes b? (both same total)"""
    sa = sorted(a, reverse=True)
    sb = sorted(b, reverse=True)
    n = max(len(sa), len(sb))
    sa = sa + [0.0]*(n-len(sa))
    sb = sb + [0.0]*(n-len(sb))
    ca = np.cumsum(sa); cb = np.cumsum(sb)
    return all(ca[i] >= cb[i] - 1e-9 for i in range(n))

Dn = {1:3, 2:7, 3:15, 4:31}
n = 3
target = 1/Dn[n]

# Configs spanning the majorization order at n=3 (4 slots, sum 1)
configs = {
    "single [1]":            [1.0],
    "near-single .9":        [0.9, 0.05, 0.03, 0.02],
    "more-spread .6,.25":   [0.6, 0.25, 0.1, 0.05],
    "tower T_3":             [8/15, 4/15, 2/15, 1/15],
    "perturbed-tower +":    [9/15, 4/15, 2/15, 0.0],
    "0.5,0.3,0.15,0.05":    [0.5, 0.3, 0.15, 0.05],
    "0.45,0.3,0.2,0.05":    [0.45, 0.3, 0.2, 0.05],
    "0.4,0.3,0.2,0.1":      [0.4, 0.3, 0.2, 0.1],
    "0.35,0.3,0.2,0.15":    [0.35, 0.3, 0.2, 0.15],
    "0.3,0.3,0.25,0.15":    [0.3, 0.3, 0.25, 0.15],
    "0.27,0.27,0.27,0.19":  [0.27, 0.27, 0.27, 0.19],
    "uniform .25":           [0.25, 0.25, 0.25, 0.25],
}

print(f"n={n}, target 1/D_n = {target:.6f}")
print(f"{'name':24s} {'D*':>10s} {'/target':>8s}  majorization-predecessors")
results = {}
for name, cfg in configs.items():
    d = min_D(cfg, n)
    results[name] = (cfg, d)
    # find what it majorizes / is majorized by, among the set
    preds = [q for q in configs if q != name and majors(configs[q], cfg)]
    succs = [q for q in configs if q != name and majors(cfg, configs[q])]
    print(f"{name:24s} {d:10.5f} {d/target:8.3f}  maj>={','.join(preds[:3]) or '-'}  <={','.join(succs[:3]) or '-'}")

print()
print("=== Monotonicity check: for every comparable pair A >=_maj B, is D*(A) >= D*(B)? ===")
violations = []
for na, (ca, da) in results.items():
    for nb, (cb, db) in results.items():
        if na != nb and majors(ca, cb):
            if da + 1e-9 < db:
                violations.append((na, nb, da, db))
if violations:
    print(f"MONOTONICITY VIOLATED: {len(violations)} violations")
    for na, nb, da, db in violations:
        print(f"  {na} >=_maj {nb} but D*({na})={da:.5f} < D*({nb})={db:.5f}")
else:
    print("Monotone on this sample (no violations).")
