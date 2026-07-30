"""
Round 4: Max-bound crux regime investigation.
Focus: a_1 < 2*a_2 AND a_3 > a_1/2 (three near-equal large pieces), n=3,4,5.
Goals:
1. Find worst config (largest D*/(M/2^n) ratio) in the crux regime.
   Is the tower still the unique worst, or is there a crux-regime config
   that EXCEEDS M/2^n (which would falsify the Max-bound conjecture)?
2. Candidate two-variable IH forms f(M, M_2, n): regression / inspection.
3. Optimal Xiang move in the crux (pair a_1 w/ a_3? halve a_1? split a_2?).
"""
import numpy as np
from itertools import product
import sys

sys.setrecursionlimit(100000)

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] * (1 if i % 2 == 0 else -1) for i in range(len(s)))

def bp_splits(piece, all_pieces):
    """Breakpoint candidates: half + ties to each other piece (B1-justified)."""
    cs = {piece / 2.0}
    for p in all_pieces:
        if 0 < p < piece:
            cs.add(p)
            cs.add(piece - p)
    return [(q, piece - q) for q in cs if 0 < q < piece]

def min_D_bp(config, k):
    """Min D over <=k Xiang marks, breakpoint-only (B1-justified)."""
    best = D_of(config)
    if k == 0:
        return best
    key = (tuple(sorted(config, reverse=True)), k)
    if key in _MEMO:
        return _MEMO[key]
    for i in range(len(config)):
        piece = config[i]
        rest = config[:i] + config[i+1:]
        for (q, r) in bp_splits(piece, config):
            new = rest + [q, r]
            d = min_D_bp(new, k - 1)
            if d < best:
                best = d
    _MEMO[key] = best
    return best

_MEMO = {}

def min_D_bp_trace(config, k):
    """Min D with the move sequence traced."""
    best = D_of(config)
    best_seq = []
    if k == 0:
        return best, best_seq
    for i in range(len(config)):
        piece = config[i]
        rest = config[:i] + config[i+1:]
        for (q, r) in bp_splits(piece, config):
            new = rest + [q, r]
            d, seq = min_D_bp_trace(new, k - 1)
            if d < best - 1e-12:
                best = d
                best_seq = [(piece, q, r)] + seq
    return best, best_seq

# ----- 1. Crux-regime worst-case search -----
# Crux: a_1 < 2*a_2 AND a_3 > a_1/2. Normalized sum=1.
# For n=3: m can be 3,4 (m<=n+1=4). For n=4: m up to 5. For n=5: m up to 6.

def random_crux_config(m, rng):
    """Generate a random config in the crux regime: a1<2*a2, a3>a1/2, sorted desc, sum=1."""
    for _ in range(1000):
        raw = rng.dirichlet([1]*m)
        cfg = sorted(raw, reverse=True)
        if cfg[0] < 2*cfg[1] and m >= 3 and cfg[2] > cfg[0]/2:
            return cfg
    return None

def search_crux(n, n_trials, seed):
    rng = np.random.default_rng(seed)
    Dn = 2**(n+1) - 1
    target = 1.0/Dn
    worst_ratio = 0.0
    worst_cfg = None
    worst_d = None
    worst_bound = None
    violations = 0
    ratios = []
    for _ in range(n_trials):
        m = rng.integers(3, n+2)  # crux needs m>=3
        cfg = random_crux_config(m, rng)
        if cfg is None:
            continue
        d = min_D_bp(list(cfg), n)
        M = cfg[0]
        bound = M / (2**n)
        if d > bound + 1e-7:
            violations += 1
            if violations <= 10:
                print(f"  VIOL n={n}: D*={d:.6f} > M/2^n={bound:.6f}, cfg={[round(x,5) for x in cfg]}")
        r = d / bound if bound > 1e-12 else 0
        ratios.append(r)
        if r > worst_ratio:
            worst_ratio = r
            worst_cfg = list(cfg)
            worst_d = d
            worst_bound = bound
    print(f"n={n}: crux search {n_trials} trials, violations={violations}")
    print(f"  worst ratio D*/(M/2^n) = {worst_ratio:.5f}")
    print(f"  worst cfg = {[round(x,5) for x in worst_cfg]}")
    print(f"  D*={worst_d:.6f}  M/2^n={worst_bound:.6f}  target=1/D_n={target:.6f}")
    return worst_ratio, worst_cfg, worst_d, worst_bound, ratios

print("="*70)
print("CRUX REGIME WORST CASE SEARCH (a_1 < 2*a_2 AND a_3 > a_1/2)")
print("="*70)
for n in [3, 4, 5]:
    _MEMO.clear()
    search_crux(n, 2000 if n <= 4 else 400, seed=42+n)
    print()

# ----- 2. Grid search n=3 crux on a fine grid for m=3,4 -----
# m=3: (a1,a2,a3) sum=1, a1>=a2>=a3, a1<2*a2, a3>a1/2.
# This is a small triangle. Let's grid it finely.

def grid_crux_m3(n, grid):
    """Grid over m=3 crux region: a1>=a2>=a3>0, a1<2a2, a3>a1/2, sum=1."""
    Dn = 2**(n+1)-1
    target = 1.0/Dn
    worst_r = 0; worst_cfg=None; worst_d=None; worst_b=None; viol=0
    # parameterize a1, a2; a3 = 1-a1-a2
    for i in range(1, grid):
        a1 = i/grid
        for j in range(1, grid):
            a2 = j/grid
            a3 = 1.0 - a1 - a2
            if a3 <= 0: continue
            # sort
            c = sorted([a1,a2,a3], reverse=True)
            if not (c[0] < 2*c[1] and c[2] > c[0]/2): continue
            # also a1 must be the max
            d = min_D_bp(list(c), n)
            M = c[0]; b = M/2**n
            if d > b + 1e-7:
                viol += 1
                if viol <= 5:
                    print(f"  VIOL n={n} m=3: D*={d:.6f} > M/2^n={b:.6f}, c={[round(x,5) for x in c]}")
            r = d/b if b>1e-12 else 0
            if r > worst_r:
                worst_r = r; worst_cfg=c; worst_d=d; worst_b=b
    return worst_r, worst_cfg, worst_d, worst_b, viol

print("="*70)
print("GRID CRUX m=3 (fine grid)")
print("="*70)
for n in [3]:
    _MEMO.clear()
    r,cfg,d,b,v = grid_crux_m3(n, 80)
    print(f"n={n} m=3 grid-80: worst ratio={r:.5f} cfg={[round(x,5) for x in cfg]} D*={d:.6f} M/2^n={b:.6f} viol={v}")
    print()
