"""
Fast breakpoint-only Xiang optimizer (B1-justified: global min is at a tie
refinement). Candidate splits for a piece = half + ties to every other piece.
No grid. Much faster. Verify D* <= M/2^n conjecture.
"""
import numpy as np
from fractions import Fraction as F

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] * (1 if i % 2 == 0 else -1) for i in range(len(s)))

def bp_splits(piece, all_pieces):
    """Breakpoint candidates only: half + ties to each other piece."""
    cs = {piece/2.0}
    for p in all_pieces:
        if 0 < p < piece:
            cs.add(p)
            cs.add(piece - p)
    return [(q, piece - q) for q in cs if 0 < q < piece]

def min_D_bp(config, k, depth=0):
    best = D_of(config)
    if k == 0:
        return best
    seen = set()
    for i in range(len(config)):
        piece = config[i]
        rest = config[:i] + config[i+1:]
        for (q, r) in bp_splits(piece, config):
            new = rest + [q, r]
            d = min_D_bp(new, k-1, depth+1)
            if d < best:
                best = d
    return best

def test_n(n, n_configs, seed=1):
    np.random.seed(seed)
    Dn = 2**(n+1) - 1
    target = 1.0/Dn
    worst_ratio = 0.0; worst = None; viol = 0
    for _ in range(n_configs):
        m = np.random.randint(1, n+2)
        raw = np.random.dirichlet([1]*m)
        cfg = sorted([float(x) for x in raw], reverse=True)
        d = min_D_bp(cfg, n)
        bound = max(cfg) / (2**n)
        if d > bound + 1e-9:
            viol += 1
            if viol <= 8:
                print(f"  VIOL n={n}: D*={d:.5f} > M/2^n={bound:.5f}, m={m}, cfg={[round(x,4) for x in cfg]}")
        if bound > 1e-12:
            r = d/bound
            if r > worst_ratio:
                worst_ratio = r; worst = (cfg, d, bound)
    print(f"n={n}: {n_configs} cfgs, {viol} violations, worst D*/(M/2^n)={worst_ratio:.4f}")
    if worst:
        print(f"   worst cfg={[round(x,4) for x in worst[0]]} D*={worst[1]:.5f} M/2^n={worst[2]:.5f}")
    # tower
    tow = [2**k for k in range(n+1)][::-1]; s=sum(tow); tow=[x/s for x in tow]
    dt = min_D_bp(tow, n)
    print(f"   tower T_{n}: D*={dt:.6f} M/2^n={max(tow)/2**n:.6f} target={target:.6f}")

if __name__ == "__main__":
    test_n(2, 500)
    test_n(3, 300)
    test_n(4, 60)
