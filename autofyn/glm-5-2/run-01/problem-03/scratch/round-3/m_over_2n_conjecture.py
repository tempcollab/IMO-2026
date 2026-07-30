"""
Test the conjecture D* <= M / 2^n, where M = max piece of the Liu config.
If true and tight (equality at the tower), this PROVES G1 in one stroke:
  tower has M = 2^n/D_n  ->  M/2^n = 1/D_n = D*(tower)  (equality)
  any config with M < 2^n/D_n  ->  D* <= M/2^n < 1/D_n  (strict, non-tower)
  any config with M > 2^n/D_n but non-tower  ->  need D* < 1/D_n still; M/2^n > 1/D_n there.
The bound M/2^n is only useful when M <= 2^n/D_n (below-threshold). For
M > 2^n/D_n we need the dominant factorization (regime A). So the conjecture
would close G2 (below-threshold C/B2), not the full G1 by itself -- but combined
with regime A (dominant factorization, certified conditional on IH), it closes
everything EXCEPT the exchange-monotonicity for M slightly above threshold but
non-tower. Actually if M > 2^n/D_n then regime A's halving factors D=D(rest)
with R <= D_{n-1}/D_n -> IH closes. So:
  - M >= 2^n/D_n AND a_1 >= 2 a_2: regime A (certified) -> D <= 1/D_n.
  - M < 2^n/D_n (below threshold): conjecture D* <= M/2^n < 1/D_n. NEW.
  - M >= 2^n/D_n AND a_1 < 2 a_2 (non-dominant, large top): regime B1 needs
    a_2 >= 2^{n-1}/D_n; if a_2 < 2^{n-1}/D_n it's B2 (below threshold for the
    rest). Conjecture applies to the rest after pairing? Need to think.

Test the raw conjecture D* <= M/2^n broadly first.
"""
import numpy as np
from xiang_optimizer import min_D

np.random.seed(1)

def M_over_2n(cfg, n):
    return max(cfg) / (2**n)

def test_n(n, n_configs=300):
    Dn = 2**(n+1) - 1
    target = 1/Dn
    thresh_M = 2**n / Dn  # = tower's max piece
    worst_ratio = 0.0
    worst_cfg = None
    violations = 0
    for _ in range(n_configs):
        # random config: m in 1..n+1 pieces, random Dirichlet, sorted desc
        m = np.random.randint(1, n+2)
        raw = np.random.dirichlet([1]*m)
        cfg = sorted([float(x) for x in raw], reverse=True)
        d = min_D(cfg, n)
        bound = M_over_2n(cfg, n)
        if d > bound + 1e-9:
            violations += 1
            if violations <= 5:
                print(f"  VIOLATION n={n}: D*={d:.5f} > M/2^n={bound:.5f}, cfg={[round(x,4) for x in cfg]}")
        r = d / bound if bound > 1e-12 else 0
        if r > worst_ratio:
            worst_ratio = r; worst_cfg = (cfg, d, bound)
    print(f"n={n}: {n_configs} configs, {violations} violations, worst D*/(M/2^n)={worst_ratio:.4f} at {worst_cfg}")
    # also test tower equality
    tower = sorted([2**k for k in range(n+1)], reverse=True)
    s = sum(tower)
    tower = [x/s for x in tower]
    dt = min_D(tower, n)
    print(f"  tower T_{n}: D*={dt:.6f}, M/2^n={M_over_2n(tower,n):.6f}, target={1/Dn:.6f}, ratio={dt/M_over_2n(tower,n):.4f}")

for n in [2, 3, 4]:
    test_n(n, 400)
