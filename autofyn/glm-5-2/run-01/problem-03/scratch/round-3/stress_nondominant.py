"""
Stress-test D* <= M/2^n on ADVERSARIAL non-dominant configs where after
pairing, rest'-max = a_3 can exceed a_1/2 = M/2 (which would break the
simple induction). Also test whether an even sharper bound holds, and
probe the non-dominant induction path.
"""
import numpy as np
from m_over_2n_fast import min_D_bp, D_of
from xiang_optimizer import min_D

def bound_M(cfg, n):
    return max(cfg) / (2**n)

# Adversarial non-dominant: a_1 just under 2*a_2, a_3 close to a_2 (so a_3 > a_1/2)
n = 2
print(f"=== n={n}, target 1/D_n = {1/(2**(n+1)-1):.5f}, thresh M=2^n/D_n={2**n/(2**(n+1)-1):.5f} ===")
adversarial = [
    [0.40, 0.35, 0.25],
    [0.42, 0.30, 0.28],
    [0.45, 0.30, 0.25],
    [0.49, 0.27, 0.24],
    [0.50, 0.30, 0.20],
    [0.34, 0.33, 0.33],
    [0.40, 0.31, 0.29],
    [0.45, 0.28, 0.27],
    [0.48, 0.27, 0.25],
    [0.50, 0.26, 0.24],
]
for c in adversarial:
    c = sorted(c, reverse=True)
    d = min_D_bp(c, n)
    b = bound_M(c, n)
    flag = "VIOL" if d > b + 1e-9 else "ok"
    print(f"  cfg={[round(x,4) for x in c]} D*={d:.5f} M/2^n={b:.5f} {flag}")

# n=3 adversarial non-dominant, a_3 > a_1/2
n = 3
print(f"\n=== n={n}, target={1/(2**(n+1)-1):.5f}, thresh M={2**n/(2**(n+1)-1):.5f} ===")
adversarial3 = [
    [0.30, 0.25, 0.24, 0.21],
    [0.28, 0.26, 0.24, 0.22],
    [0.26, 0.25, 0.25, 0.24],
    [0.40, 0.25, 0.20, 0.15],
    [0.35, 0.30, 0.20, 0.15],
    [0.30, 0.28, 0.22, 0.20],
    [0.27, 0.26, 0.25, 0.22],
    [0.50, 0.20, 0.15, 0.15],
    [0.45, 0.25, 0.18, 0.12],
    [0.34, 0.34, 0.16, 0.16],
]
for c in adversarial3:
    c = sorted(c, reverse=True)
    d = min_D_bp(c, n)
    b = bound_M(c, n)
    flag = "VIOL" if d > b + 1e-9 else "ok"
    print(f"  cfg={[round(x,4) for x in c]} D*={d:.5f} M/2^n={b:.5f} {flag}")

# random heavy stress n=2
print("\n=== heavy random n=2 non-dominant (a_1<2 a_2) stress, 2000 cfgs ===")
np.random.seed(7)
viol=0; worst_r=0; worst_c=None
for _ in range(2000):
    raw = np.random.dirichlet([1]*3); c=sorted([float(x) for x in raw], reverse=True)
    if c[0] >= 2*c[1]: continue  # skip dominant
    d = min_D_bp(c, 2); b = bound_M(c, 2)
    if d > b + 1e-9:
        viol += 1
        if viol<=3: print(f"  VIOL {[round(x,4) for x in c]} D*={d:.5f} b={b:.5f}")
    if b>1e-12:
        r=d/b
        if r>worst_r: worst_r=r; worst_c=(c,d,b)
print(f"  violations={viol}, worst ratio={worst_r:.4f} at {[round(x,4) for x in worst_c[0]]} D*={worst_c[1]:.5f} b={worst_c[2]:.5f}")
