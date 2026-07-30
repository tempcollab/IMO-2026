#!/usr/bin/env python3
"""
(P1c) Characterize the dual certificate for the 4th framing.

The LP dual of Xiang's min-D LP (per combinatorial type) has:
  - equality marginals y_eq[t] (one per tower-piece bin, value V_t = 2^{n-t})
  - sort-constraint duals y_ub[i] >= 0 (one per adjacent sort pair p_i >= p_{i+1})

Dual feasibility (stationarity) for piece at sorted position k in bin b(k):
   y_eq[b(k)] = (-1)^k + y_ub[k] - y_ub[k-1]      (y_ub[-1] = y_ub[m-1] = 0, y_ub >= 0)
Dual objective = sum_t y_eq[t] * V_t.

The empirical finding: y_eq = [1, -1, -1, ..., -1]  (objective = 2^n - (2^n-1) = 1)
is dual-feasible for MOST odd-count types; a few need [0,0,1,-1,...] fallbacks
(also objective 1).

This script: for each sampled odd-count type, CHECK whether the uniform
certificate y_eq[0]=+1, y_eq[t]=-1 (t>=1) admits y_ub >= 0 (a nonneg flow on the
position chain). Report the fraction where the SINGLE uniform cert works, vs
where a fallback is needed. This tells the outliner: 1 cert or a small family.
"""
import numpy as np
from scipy.optimize import linprog
from itertools import product

def tower_vals(n):
    return [2**(n-k) for k in range(n+1)]

def Dval(pieces):
    p = sorted(pieces, reverse=True)
    return sum((-1)**i * p[i] for i in range(len(p)))

def refine_with_bins(n, rng):
    work = [(tower_vals(n)[t], t) for t in range(n+1)]
    nmarks = int(rng.integers(0, n+1))
    for _ in range(nmarks):
        idx = int(rng.integers(0, len(work)))
        v, b = work[idx]
        frac = float(rng.uniform(0.05, 0.95))
        a = v*frac; bb = v - a
        work.pop(idx); work.append((a,b)); work.append((bb,b))
    work.sort(key=lambda x: -x[0])
    return [v for v,_ in work], [b for _,b in work]

def check_uniform_cert(n, pieces, bins):
    """
    Try y_eq = [1, -1, -1, ..., -1] (index by tower bin 0..n).
    Need y_ub >= 0 with y_eq[bin(k)] = (-1)^k + y_ub[k] - y_ub[k-1].
    => y_ub[k] - y_ub[k-1] = y_eq[bin(k)] - (-1)^k.
    Let d_k = y_eq[bin(k)] - (-1)^k. Then y_ub[k] = y_ub[k-1] + d_k, y_ub[-1]=0.
    So y_ub[k] = sum_{j=0}^{k} d_j. Feasible iff ALL prefix sums >= 0
    AND y_ub[m-1] = 0 (boundary). The boundary y_ub[m-1]=0 requires
    sum_{j=0}^{m-1} d_j = 0, i.e. sum_k (y_eq[bin(k)] - (-1)^k) = 0
    => sum_k y_eq[bin(k)] = sum_k (-1)^k.
    """
    m = len(pieces)
    y_eq = {t: (1 if t == 0 else -1) for t in range(n+1)}
    # prefix sums
    yub = []
    acc = 0.0
    feasible = True
    for k in range(m):
        b = bins[k]
        d = y_eq[b] - ((-1)**k)
        acc += d
        yub.append(acc)
        if acc < -1e-9:
            feasible = False
    # boundary: y_ub[m-1] must be 0
    boundary_ok = abs(yub[-1]) < 1e-9
    return feasible and boundary_ok, yub

def find_best_cert_objective(n, pieces, bins):
    """Solve the dual directly: maximize sum_t y_eq[t]*V_t s.t.
    y_eq[bin(k)] - y_ub[k] + y_ub[k-1] = (-1)^k, y_ub>=0, y_ub[-1]=y_ub[m-1]=0.
    Equivalently solve primal (min D) and read dual obj = primal obj."""
    m = len(pieces); V = tower_vals(n)
    c = np.array([(-1)**i for i in range(m)], dtype=float)
    A_ub = []; b_ub = []
    for i in range(m-1):
        row = np.zeros(m); row[i]=-1; row[i+1]=1; A_ub.append(row); b_ub.append(0.0)
    A_eq = []; b_eq = []
    for t in range(n+1):
        row = np.zeros(m)
        for i in range(m):
            if bins[i]==t: row[i]=1.0
        if row.sum()>0: A_eq.append(row); b_eq.append(float(V[t]))
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=[(0,None)]*m, method='highs')
    return res.fun, res.eqlin.marginals

print("="*72)
print("(P1c) Does the SINGLE uniform cert y_eq=[1,-1,-1,...,-1] cover all odd types?")
print("="*72)
for n in [2,3,4]:
    rng = np.random.default_rng(5000+n)
    trials = 600 if n<=3 else 300
    odd_total = 0; uniform_ok = 0; fallback = 0
    fallback_patterns = {}
    for _ in range(trials):
        pieces, bins = refine_with_bins(n, rng)
        if len(pieces) % 2 == 0: continue
        odd_total += 1
        ok, _ = check_uniform_cert(n, pieces, bins)
        if ok:
            uniform_ok += 1
        else:
            fallback += 1
            _, marg = find_best_cert_objective(n, pieces, bins)
            key = tuple(round(float(x),3) for x in marg)
            fallback_patterns[key] = fallback_patterns.get(key,0)+1
    print(f"n={n}: odd-type trials={odd_total}, uniform-cert feasible: {uniform_ok} "
          f"({100*uniform_ok/max(1,odd_total):.1f}%), fallback needed: {fallback}")
    # show the distinct fallback certificate patterns
    top = sorted(fallback_patterns.items(), key=lambda x:-x[1])[:6]
    for pat, cnt in top:
        # compute objective
        V = tower_vals(n)
        obj = sum(pat[t]*V[t] for t in range(len(pat)))
        print(f"   fallback cert y_eq={pat}  (objective={obj:.4f})  count={cnt}")
    print()

print("="*72)
print("(P1d) Sanity: the uniform cert boundary condition.")
print("  boundary y_ub[m-1]=0 requires sum_k y_eq[bin(k)] = sum_k (-1)^k.")
print("  For odd m: sum_k (-1)^k = +1. sum_k y_eq[bin(k)] = sum over pieces of")
print("  (1 if top-bin else -1) = (#top-bin pieces) - (#non-top pieces).")
print("  So boundary needs: (#top-bin pieces) - (m - #top-bin) = 1")
print("  => 2*(#top-bin pieces) = m+1 => #top-bin pieces = (m+1)/2.")
print("  (odd m: top-bin must hold exactly half the pieces, rounded up.)")
print("="*72)
