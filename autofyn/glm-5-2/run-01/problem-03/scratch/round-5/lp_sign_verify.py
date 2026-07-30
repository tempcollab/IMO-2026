"""
Verify the EXACT sign convention of the LP-2 dual for the interleaved T_2 example.

Primal (per combinatorial type cell):
  min  D(p) = sum_k (-1)^k p_k
  s.t. A_eq p = b_eq      (bin-sum equalities)
       A_ub p <= b_ub=0   (sort order: -p_k + p_{k+1} <= 0, i.e. p_k >= p_{k+1})
       p >= 0

We solve with scipy.linprog (HiGHS) and READ the dual marginals (eqlin, ineqlin),
then reconstruct y_eq (free) and y_ub (<= 0 or >= 0? — let scipy tell us) and
verify against the candidate sign conventions.

Example (round-4 interleaved T_2 demo, claimed infeasible):
  n=2, T_2=(4,2,1), D_2=7.
  Refinement: split 4->{3,1} (bin 0), keep 2 (bin 1), split 1->{0.6,0.4} (bin 2).
  Sorted p=(3,2,1,0.6,0.4), m=5, b=(0,1,0,2,2).
  Signs (-1)^k = (+,-,+,-,+).
"""
import numpy as np
from scipy.optimize import linprog

def build_and_solve(n, b, tower_vals, title):
    m = len(b)
    c = np.array([(-1)**k for k in range(m)], dtype=float)  # minimize D
    # bin-sum equalities
    bins = sorted(set(b))
    A_eq = np.zeros((len(bins), m))
    b_eq = np.zeros(len(bins))
    for i, t in enumerate(bins):
        for k in range(m):
            if b[k] == t:
                A_eq[i, k] = 1.0
        b_eq[i] = float(tower_vals[t])  # tower_vals indexed by bin label t
    # sort order: p_k >= p_{k+1}  =>  -p_k + p_{k+1} <= 0  (row k, k=0..m-2)
    A_ub = np.zeros((m-1, m))
    for k in range(m-1):
        A_ub[k, k] = -1.0
        A_ub[k, k+1] = 1.0
    b_ub = np.zeros(m-1)
    bounds = [(0, None)]*m
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method='highs')
    print(f"\n=== {title} ===")
    print("primal min D =", res.fun)
    print("primal p =", np.round(res.x, 6))
    print("eqlin marginals (y_eq for each bin row):", np.round(res.eqlin.marginals, 6))
    print("ineqlin marginals (y_ub for each sort row):", np.round(res.ineqlin.marginals, 6))
    # Dual objective = b_eq . y_eq + b_ub . y_ub
    y_eq = res.eqlin.marginals
    y_ub = res.ineqlin.marginals
    dual_obj = b_eq @ y_eq + b_ub @ y_ub
    print("dual objective (b_eq.y_eq + b_ub.y_ub) =", round(dual_obj, 6))
    # Check stationarity: A_eq^T y_eq + A_ub^T y_ub  vs c  (which sign?)
    stat = A_eq.T @ y_eq + A_ub.T @ y_ub
    print("c                   =", c)
    print("A_eq^T y_eq+A_ub^T y_ub =", np.round(stat, 6))
    print("<= c ?", np.all(stat <= c + 1e-9))
    print(">= c ?", np.all(stat >= c - 1e-9))
    # Sign of y_ub
    print("y_ub <= 0 ?", np.all(y_ub <= 1e-9))
    print("y_ub >= 0 ?", np.all(y_ub >= -1e-9))
    return res, y_eq, y_ub, c, A_eq, A_ub, b_eq

# ---- Interleaved T_2 demo (claimed infeasible under round-4 wrong convention) ----
n = 2
tower_vals = {0: 4, 1: 2, 2: 1}  # value of bin label t
b = (0, 1, 0, 2, 2)
res, y_eq, y_ub, c, A_eq, A_ub, b_eq = build_and_solve(
    n, b, tower_vals, "Interleaved T_2: split 4->{3,1}, keep 2, split 1->{0.6,0.4}")

# ---- Reconstruct the mountain under BOTH candidate conventions and check nonneg ----
m = len(b)
# Convention A (round-4 WRONG): d_k = y_eq[b(k)] - (-1)^k ; prefix sums nonneg; y_ub>=0
# Convention B (CORRECT candidate): d_k = (-1)^k - y_eq[b(k)] ; prefix sums nonneg; y_ub<=0
print("\n--- mountain check ---")
for name, dfunc, expect_yub_sign in [
    ("Conv-A (old): d=y_eq-(-1)^k, m=prefix, y_ub>=0",
     lambda k: y_eq[b[k]] - (-1)**k, ">="),
    ("Conv-B (new): d=(-1)^k-y_eq, m=prefix, y_ub<=0",
     lambda k: (-1)**k - y_eq[b[k]], "<="),
]:
    d = [dfunc(k) for k in range(m)]
    pref = [0.0]*m
    s = 0.0
    for k in range(m):
        s += d[k]
        pref[k] = s
    print(f"\n{name}")
    print("  d =", np.round(d, 6))
    print("  prefix m =", np.round(pref, 6))
    print("  prefix all >= 0 ?", np.all(np.array(pref) >= -1e-9))
    print("  closes (m[-1]=0) ?", abs(pref[-1]) < 1e-9)

# ---- Now: a CLEAN type for sanity (should match LP-3 cert y_eq=parity, y_ub=0) ----
# Clean T_2: p=(4,2,1) unsplit, b=(0,1,2), m=3. signs (+,-,+). All clean.
tower_vals2 = {0: 4, 1: 2, 2: 1}
b2 = (0, 1, 2)
build_and_solve(n, b2, tower_vals2, "Clean T_2 unsplit (sanity: y_eq=parity, y_ub=0)")

# ---- Clean 2-split: split 4->{2.5,1.5}(bin0, positions 0,2 both +), keep 2(bin1,pos1 -), keep 1(bin2,pos3 -) ----
# p=(2.5,2,1.5,1), m=4, b=(0,1,0,2), signs (+,-,+,-). bin0 at {0,2} both +; bin1 at {1} -; bin2 at {3} -.
tower_vals3 = {0: 4, 1: 2, 2: 1}
b3 = (0, 1, 0, 2)
build_and_solve(n, b3, tower_vals3, "Clean 2-split T_2 (bin0 at +{0,2}, bins1,2 at -{1,3})")
