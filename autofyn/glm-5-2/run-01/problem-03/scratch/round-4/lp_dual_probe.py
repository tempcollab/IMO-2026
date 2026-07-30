#!/usr/bin/env python3
"""
4th-framing probe for imo-2026-03 lower bound (odd-count non-dyadic leftover wall).

Three sub-probes:
 (P1) LP / Farkas duality. For a fixed combinatorial type (bin assignment = which
      tower piece each fragment belongs to; sort order sigma), Xiang's min-D is an
      EXACT LP (any composition of a tower piece into r>0 parts is a valid split
      tree, so the bin-partition LP restricted to a type == the refinement LP).
      Solve primal (min D) + read dual. Is min D >= 1 (target)? Is there a UNIFORM
      dual certificate across types (the 4th framing's escape from sign-bookkeeping)?
 (P2) Alternative Liu config. Is the tower the UNIQUE config achieving
      min_X D = 1 (tower units) for n=3? If yes, lens-4 (different Liu config) is dead.
 (P3) Measure-transport: is there a simple convex functional of the N(t) profile
      that lower-bounds D and is minimized at the dyadic profile? Quick probe.

Tower units throughout. Target D >= 1.
"""
import numpy as np
from scipy.optimize import linprog
from itertools import product
from fractions import Fraction

# ============================================================
# Helper: alternating sum of a sorted-desc list
def Dval(pieces):
    p = sorted(pieces, reverse=True)
    return sum((-1)**i * p[i] for i in range(len(p)))

# ============================================================
# (P1) LP-dual probe.
# For a given refinement config, derive its TYPE = (bin assignment, sort order),
# build the exact LP, solve, extract dual.
#
# We build the LP in variables p_0..p_{m-1} (the pieces, in SORTED order).
# Type data:
#   - bin[j] = tower-piece index each sorted-piece belongs to (0..n, tower piece 2^n..1)
#   - sort order is just p_0 >= p_1 >= ... >= p_{m-1}
# Objective: minimize  D = sum_i (-1)^i p_i  ->  c = [(-1)^i]
# Constraints:
#   - bin-sum equalities: for each tower piece t with value V_t, sum of p_i (i in bin=t) == V_t
#   - sort: p_i >= p_{i+1}  ->  -p_i + p_{i+1} <= 0
#   - p_i >= 0
# We solve via scipy.linprog (minimize c.p s.t. A_ub p <= b_ub, A_eq p = b_eq, bounds).
#
# linprog dual: we read the marginal values (shadow prices) of the equality constraints
# (bin sums) -- these are the "Liu certificate weights" on tower pieces.
# ============================================================

def tower_vals(n):
    """tower pieces 2^n, 2^{n-1}, ..., 1 -> as values, index 0..n."""
    return [2**(n - k) for k in range(n + 1)]  # [2^n, ..., 1]

def build_and_solve_lp(n, pieces, bin_of_piece):
    """
    pieces: list of piece values (sorted desc) at a representative config.
    bin_of_piece: list, bin_of_piece[i] = tower-piece index (0..n) of sorted piece i.
    Build LP, solve, return (primal_opt, dual_eq_marginals, status).
    """
    m = len(pieces)
    V = tower_vals(n)
    c = np.array([(-1)**i for i in range(m)], dtype=float)  # minimize D
    # sort constraints: p_i >= p_{i+1}  ->  p_i - p_{i+1} >= 0  ->  -p_i + p_{i+1} <= 0
    A_ub = []
    b_ub = []
    for i in range(m - 1):
        row = np.zeros(m); row[i] = -1.0; row[i+1] = 1.0
        A_ub.append(row); b_ub.append(0.0)
    # bin-sum equalities
    A_eq = []
    b_eq = []
    for t in range(n + 1):
        row = np.zeros(m)
        for i in range(m):
            if bin_of_piece[i] == t:
                row[i] = 1.0
        # only add equality if this bin is nonempty
        if row.sum() > 0:
            A_eq.append(row); b_eq.append(float(V[t]))
    A_ub = np.array(A_ub) if A_ub else None
    b_ub = np.array(b_ub) if b_ub else None
    A_eq = np.array(A_eq) if A_eq else None
    b_eq = np.array(b_eq) if b_eq else None
    bounds = [(0, None)] * m
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    return res

def refine_with_bins(n, rng):
    """Random refinement of T_n; return (sorted pieces, bin_of_piece)."""
    pieces = tower_vals(n)  # each is a (value, bin)
    bins = list(range(n+1))
    # working list of (value, bin)
    work = [(tower_vals(n)[t], t) for t in range(n+1)]
    nmarks = int(rng.integers(0, n+1))
    for _ in range(nmarks):
        idx = int(rng.integers(0, len(work)))
        v, b = work[idx]
        frac = float(rng.uniform(0.05, 0.95))
        a = v*frac; bb = v - a
        work.pop(idx)
        work.append((a, b)); work.append((bb, b))
    work.sort(key=lambda x: -x[0])
    pieces = [v for v,_ in work]
    bin_of_piece = [b for _,b in work]
    return pieces, bin_of_piece

print("="*72)
print("(P1) LP-dual probe: exact LP per combinatorial type, min D + dual marginals")
print("="*72)
for n in [2, 3]:
    rng = np.random.default_rng(1000 + n)
    trials = 400 if n == 2 else 250
    min_primal = None
    worst_cfg = None
    n_odd = 0  # types where m is odd (the wall regime)
    odd_duals = []
    all_geq_1 = True
    for _ in range(trials):
        pieces, bins = refine_with_bins(n, rng)
        res = build_and_solve_lp(n, pieces, bins)
        if not res.success:
            continue
        opt = res.fun
        if min_primal is None or opt < min_primal:
            min_primal = opt
            worst_cfg = (pieces, bins)
        if opt < 1.0 - 1e-7:
            all_geq_1 = False
        m = len(pieces)
        if m % 2 == 1:
            n_odd += 1
            # equality marginals = shadow prices of bin-sum constraints
            # res.ineqlin/marginals exist in scipy>=1.7; res.eqlin.marginals for equalities
            try:
                marg = res.eqlin.marginals
                odd_duals.append((opt, list(marg), pieces, bins))
            except Exception:
                pass
    print(f"n={n}: trials={trials}, min LP primal (min D over each type cell) = {min_primal:.6f}")
    print(f"   all type-cells have min D >= 1 ? {all_geq_1}")
    print(f"   #odd-m types (the wall regime): {n_odd}")
    # show a few odd-type dual certificates
    odd_duals.sort(key=lambda x: x[0])
    for opt, marg, pieces, bins in odd_duals[:4]:
        # round marginals to see structure
        rm = [round(float(x),4) for x in marg]
        print(f"   odd-type: opt D={opt:.5f}  bin-sum marginals={rm}")
        print(f"      pieces~{[round(x,3) for x in pieces]}  bins={bins}")
    print()

# ============================================================
# (P1b) Direct probe on the KNOWN odd-count minimizer for T_3.
# Config {4.75,4,2,2,1,1,0.25}, D=1.
# Bins: tower 8 -> {4.75, 2, 1, 0.25} (sum 8); tower 4 -> {4}; 2->{2}; 1->{1}.
# ============================================================
print("-"*72)
print("(P1b) LP at the odd-count minimizer cell for T_3: {4.75,4,2,2,1,1,0.25}")
print("-"*72)
pieces = [4.75, 4, 2, 2, 1, 1, 0.25]
bins   = [0,    1, 0, 2, 0, 3, 0]   # 8-bin: 4.75,2,1,0.25 ; 4-bin:4 ; 2-bin:2 ; 1-bin:1
# sanity
V = tower_vals(3)
for t in range(4):
    s = sum(pieces[i] for i in range(len(pieces)) if bins[i]==t)
    assert abs(s - V[t]) < 1e-9, (t, s, V[t])
res = build_and_solve_lp(3, pieces, bins)
print(f"  primal min D over this type cell = {res.fun:.6f}  (target >=1; actual config D={Dval(pieces)})")
print(f"  bin-sum marginals (shadow prices) = {[round(float(x),4) for x in res.eqlin.marginals]}")
print(f"  -> a uniform dual would have the SAME marginals across all odd types.")

# ============================================================
# (P2) Alternative Liu config: is the tower UNIQUE for n=3?
# For a candidate Liu config (a_1>=...>=a_{n+1}, sum 1), compute min_X D (Xiang <=n marks)
# by grid search. Check if any non-tower config achieves min_X D = 1 (tower units).
# ============================================================
print("="*72)
print("(P2) Alternative Liu config: is tower T_3 unique best (min_X D = 1)?")
print("="*72)

def xiang_min_D_grid(n, liu_cfg, ngrid=30, seed=0):
    """Grid-search Xiang's <=n marks to minimize D (tower units). liu_cfg sum=D_n."""
    # naive: random + structured (halving) refinements
    rng = np.random.default_rng(seed)
    best = float('inf')
    # include parallel-halving strategy (split each piece in half, up to n marks)
    work = list(liu_cfg)
    # structured: greedily halve the largest piece, n times
    w = sorted(work, reverse=True)
    for _ in range(n):
        # halve the largest
        w2 = list(w)
        w2[0] = w2[0]/2
        w2.append(w2[0])
        w = sorted(w2, reverse=True)
        d = Dval(w)
        if d < best: best = d
    # random refinements
    for _ in range(ngrid*20):
        w = list(work)
        for _ in range(int(rng.integers(0, n+1))):
            idx = int(rng.integers(0, len(w)))
            v = w[idx]; f = float(rng.uniform(0.05,0.95))
            w.pop(idx); w.extend([v*f, v-v*f])
        w.sort(reverse=True)
        d = Dval(w)
        if d < best: best = d
    return best

n = 3
Dn = 2**(n+1)-1
tower = tower_vals(n)
print(f"  n={n}, D_n={Dn}. Tower T_{n}={tower}, min_X D (Xiang) ~ {xiang_min_D_grid(n, tower, 40, 0):.5f} (target=1)")
# try perturbed configs: scale tower pieces slightly, renormalize
best_alt = None
best_alt_cfg = None
rng = np.random.default_rng(7)
for trial in range(60):
    # perturb tower: random non-tower config with same #pieces summing to Dn
    raw = [float(x) * float(rng.uniform(0.5, 1.5)) for x in tower]
    s = sum(raw); raw = [x*Dn/s for x in raw]
    raw.sort(reverse=True)
    d = xiang_min_D_grid(n, raw, 30, trial)
    if best_alt is None or d > best_alt:
        best_alt = d; best_alt_cfg = raw
print(f"  best (max over Xiang-min) among 60 non-tower Liu configs: min_X D = {best_alt:.5f}")
print(f"  (if < 1, non-tower is WORSE for Liu -> tower unique best -> lens-4 DEAD for tight bound)")
print(f"  a strong non-tower cfg: {[round(x,3) for x in best_alt_cfg]}")
