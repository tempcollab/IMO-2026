"""
Verify the CORRECTED LP-2 dual convention on genuinely-interleaved types,
and confirm the spine sign-pattern = dual-certificate equivalence.

Corrected dual (Conv-B):
  d_j   = (-1)^j - y_eq[b(j)]
  mountain m_k = -y_ub[k] >= 0  (k=0..m-2), sentinels m_{-1} = m_{m-1} = 0
  feasibility (INEQUALITY):  m_j - m_{j-1} <= d_j   for j=0..m-1
  objective:  Phi = sum_t y_eq[t] * 2^{n-t}
  strong duality:  max Phi (feasible) = min D (primal)
"""
import numpy as np
from scipy.optimize import linprog

def solve(n, b, tower_vals, title):
    m = len(b)
    c = np.array([(-1)**k for k in range(m)], dtype=float)
    bins = sorted(set(b))
    A_eq = np.zeros((len(bins), m)); b_eq = np.zeros(len(bins))
    for i, t in enumerate(bins):
        for k in range(m):
            if b[k] == t: A_eq[i, k] = 1.0
        b_eq[i] = float(tower_vals[t])
    A_ub = np.zeros((m-1, m)); b_ub = np.zeros(m-1)
    for k in range(m-1):
        A_ub[k, k] = -1.0; A_ub[k, k+1] = 1.0
    bounds = [(0, None)]*m
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method='highs')
    y_eq = res.eqlin.marginals; y_ub = res.ineqlin.marginals
    primal_min = res.fun
    dual_obj = float(b_eq @ y_eq)
    return dict(title=title, n=n, m=m, b=b, tower_vals=tower_vals,
                p=res.x, primal_min=primal_min, y_eq=y_eq, y_ub=y_ub,
                dual_obj=dual_obj, c=c, A_eq=A_eq, A_ub=A_ub, b_eq=b_eq)

def check_uniform_cert(R, y_eq_cert):
    """Check the corrected-conv inequality (star) for a GIVEN y_eq cert
    (with y_ub chosen optimally = the LP dual's y_ub is NOT used; instead
    we test whether ANY nonneg m satisfies m_j-m_{j-1} <= d_j).
    Feasibility of the inequality (star) is itself an LP: does there exist
    m_0..m_{m-2} >= 0 with m_j-m_{j-1} <= d_j (sentinels 0)?  We solve it
    as: minimize 0 subject to those constraints (feasibility LP)."""
    m = R['m']; b = R['b']
    d = np.array([(-1.)**k - y_eq_cert[b[k]] for k in range(m)])
    # variables m_0..m_{m-2}  (nvar = m-1)
    nvar = m-1
    # constraints:  m_j - m_{j-1} <= d_j   for j=0..m-1
    #   j=0:    m_0 - 0 <= d_0         -> m_0 <= d_0
    #   j=k(1..m-2): m_k - m_{k-1} <= d_k
    #   j=m-1:  0 - m_{m-2} <= d_{m-1}  -> -m_{m-2} <= d_{m-1}
    A = np.zeros((m, nvar)); rhs = np.zeros(m)
    for j in range(m):
        if j == 0:
            A[j, 0] = 1.0; rhs[j] = d[0]
        elif j < m-1:
            A[j, j] = 1.0; A[j, j-1] = -1.0; rhs[j] = d[j]
        else:
            A[j, m-2] = -1.0; rhs[j] = d[m-1]
    # feasibility: minimize 0 s.t. A m <= rhs, m >= 0
    feas = linprog(np.zeros(nvar), A_ub=A, b_ub=rhs,
                   bounds=[(0, None)]*nvar, method='highs')
    feasible = feas.success
    obj = float(sum(y_eq_cert[t]*R['tower_vals'][t] for t in y_eq_cert))
    return dict(d=d, feasible=feasible, obj=obj, m=feas.x if feasible else None)

def spine(p, b, tower_vals):
    """Greedy adjacent-equal pair cancellation (spine-pair-cancellation S1).
    Returns list of (value, original_position) of spine pieces (unpaired),
    with their ORIGINAL index in p (so we know sign (-1)^k)."""
    items = sorted([(float(p[k]), k) for k in range(len(p))], reverse=True)
    # cancel adjacent-equal pairs greedily
    spine_items = []
    i = 0
    while i < len(items):
        if i+1 < len(items) and abs(items[i][0]-items[i+1][0]) < 1e-9:
            i += 2  # cancel pair
        else:
            spine_items.append(items[i]); i += 1
    return spine_items

# ============ genuinely interleaved T_2 types ============
n = 2; TV = {0:4,1:2,2:1}

# Type I1: split 4->{2.5,1.5}(bin0), split 2->{1.2,0.8}(bin1), keep 1(bin2)
# sorted: 2.5(b0),1.5(b0),1.2(b1),1(b2),0.8(b1)  b=(0,0,1,2,1)
R1 = solve(n, (0,0,1,2,1), TV, "I1: bin0 interleaved at {0,1}")
print(f"\n### {R1['title']}")
print(f"  primal min D = {R1['primal_min']:.6f}  (scipy dual obj = {R1['dual_obj']:.6f})")
print(f"  optimal p = {np.round(R1['p'],6)}")
print(f"  scipy y_eq = {np.round(R1['y_eq'],6)}  y_ub = {np.round(R1['y_ub'],6)}")
sp = spine(R1['p'], R1['b'], TV)
print(f"  spine (value, orig idx): {[(round(v,4),k) for v,k in sp]}")
print(f"  spine D = {sum((-1)**k * v for v,k in sp):.6f}")
# uniform cert y_eq=(1,-1,-1)
cert = {0:1.0, 1:-1.0, 2:-1.0}
chk = check_uniform_cert(R1, cert)
print(f"  uniform cert y_eq=(1,-1,-1): feasible={chk['feasible']}, obj={chk['obj']:.4f}, d={np.round(chk['d'],4)}")

# Type I2: split 4->{3,1}(bin0, pos 0&2), split 1->{0.6,0.4}(bin2, pos 3&4), keep 2(bin1)
# sorted: 3(b0),2(b1),1(b0),0.6(b2),0.4(b2)  b=(0,1,0,2,2)  -- the round-4 example
R2 = solve(n, (0,1,0,2,2), TV, "I2 (round-4 demo): bin2 interleaved at {3,4}")
print(f"\n### {R2['title']}")
print(f"  primal min D = {R2['primal_min']:.6f}  (dual obj = {R2['dual_obj']:.6f})")
print(f"  optimal p = {np.round(R2['p'],6)}")
print(f"  scipy y_eq = {np.round(R2['y_eq'],6)}  y_ub = {np.round(R2['y_ub'],6)}")
sp = spine(R2['p'], R2['b'], TV)
print(f"  spine (value, orig idx): {[(round(v,4),k) for v,k in sp]}")
print(f"  spine D = {sum((-1)**k * v for v,k in sp):.6f}")
chk = check_uniform_cert(R2, cert)
print(f"  uniform cert y_eq=(1,-1,-1): feasible={chk['feasible']}, obj={chk['obj']:.4f}, d={np.round(chk['d'],4)}")

# Type I3: a 3-mark T_3 interleaved type whose minimizer has a non-dyadic spine.
# T_3=(8,4,2,1). Cascade: split 8->{5,3}(b0), split 4->{2.5,1.5}(b1), keep 2(b2), keep1(b3)
# sorted: 5(b0),3(b0),2.5(b1),2(b2),1.5(b1),1(b3)  b=(0,0,1,2,1,3) m=6 signs(+,-,+,-,+,-)
n=3; TV3={0:8,1:4,2:2,3:1}
R3 = solve(n, (0,0,1,2,1,3), TV3, "I3 T_3: bin0{0,1}+bin1{2,4} interleaved")
print(f"\n### {R3['title']}")
print(f"  primal min D = {R3['primal_min']:.6f}  (dual obj = {R3['dual_obj']:.6f})")
print(f"  optimal p = {np.round(R3['p'],6)}")
print(f"  scipy y_eq = {np.round(R3['y_eq'],6)}  y_ub = {np.round(R3['y_ub'],6)}")
sp = spine(R3['p'], R3['b'], TV3)
print(f"  spine (value, orig idx): {[(round(v,4),k) for v,k in sp]}")
print(f"  spine D = {sum((-1)**k * v for v,k in sp):.6f}")
cert3 = {0:1.0,1:-1.0,2:-1.0,3:-1.0}
chk = check_uniform_cert(R3, cert3)
print(f"  uniform cert y_eq=(1,-1,-1,-1): feasible={chk['feasible']}, obj={chk['obj']:.4f}, d={np.round(chk['d'],4)}")

# Type I4: T_3, interleaved producing non-dyadic spine minimizer.
# split 8->{4.5,3.5}(b0), split 2->{1.5,0.5}(b2), keep 4(b1), keep1(b3)
# sorted: 4.5(b0),4(b1),3.5(b0),1.5(b2),1(b3),0.5(b2) b=(0,1,0,2,3,2) m=6
R4 = solve(n, (0,1,0,2,3,2), TV3, "I4 T_3: bin0{0,2}+bin2{3,5} interleaved")
print(f"\n### {R4['title']}")
print(f"  primal min D = {R4['primal_min']:.6f}  (dual obj = {R4['dual_obj']:.6f})")
print(f"  optimal p = {np.round(R4['p'],6)}")
print(f"  scipy y_eq = {np.round(R4['y_eq'],6)}  y_ub = {np.round(R4['y_ub'],6)}")
sp = spine(R4['p'], R4['b'], TV3)
print(f"  spine (value, orig idx): {[(round(v,4),k) for v,k in sp]}")
print(f"  spine D = {sum((-1)**k * v for v,k in sp):.6f}")
chk = check_uniform_cert(R4, cert3)
print(f"  uniform cert y_eq=(1,-1,-1,-1): feasible={chk['feasible']}, obj={chk['obj']:.4f}, d={np.round(chk['d'],4)}")
# also test the spine-sign cert: y_eq = +1 for fragment-bins, -1 for tower-bins
# but "fragment" vs "tower" is determined at the SPINE, which is config-dependent.
# At the minimizer, identify spine bins and build the cert from them:
print("  --- spine-derived cert ---")
# tower bins = those whose spine piece equals a tower value
def is_tower_val(v, TV):
    return any(abs(v-tv)<1e-9 for tv in TV.values())
spine_bins = [R4['b'][k] for v,k in sp]
print(f"  spine bins (in spine order): {spine_bins}")
