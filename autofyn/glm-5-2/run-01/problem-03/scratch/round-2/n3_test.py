import numpy as np

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

def best_xiang_D(config, n_marks, grid=22, memo=None):
    config = tuple(sorted(config, reverse=True))
    if memo is None: memo = {}
    key = (config, n_marks)
    if key in memo: return memo[key]
    best = D_alt(list(config))
    if n_marks == 0:
        memo[key] = best; return best
    for i in range(len(config)):
        piece = config[i]
        if piece < 1e-12: continue
        others = list(config[:i]) + list(config[i+1:])
        for g in range(1, grid):
            p = piece * g / grid
            if p < 1e-12 or p > piece - 1e-12: continue
            new = others + [p, piece - p]
            d = best_xiang_D(new, n_marks - 1, grid, memo)
            if d < best: best = d
    memo[key] = best
    return best

# n=3, 4 pieces. Test: (1) does optimal always cap at 1/15?
# (2) does pairing (split L into a_2, L-a_2) + optimal 2 remaining marks always cap?
n = 3
Dn = 2**(n+1)-1  # = 15
tgt = 1.0/Dn  # = 1/15 ≈ 0.0667
L_thresh = 2.0**n / Dn  # = 8/15 ≈ 0.533
a2_thresh = 2.0**(n-1) / Dn  # = 4/15 ≈ 0.267

rng = np.random.default_rng(77)
ntrials = 800
opt_fail = 0
pair_fail = 0
pair_overshoot = 0  # pairing+induction overshoots but still ok
regime_stats = {}

for _ in range(ntrials):
    k = rng.integers(1, n+2)  # 1..4 pieces
    a = np.sort(rng.dirichlet(np.ones(k)))[::-1]
    L = a[0]
    a2 = a[1] if k >= 2 else 0
    memo = {}
    d_opt = best_xiang_D(a, n, grid=22, memo=memo)
    if d_opt > tgt + 1e-7:
        opt_fail += 1
    
    if k >= 2 and L < 2*a2:  # non-dominant
        # Pairing: split L into a_2, L-a_2
        cfg_pair = [a2, a2, L-a2] + list(a[2:])
        memo2 = {}
        d_pair = best_xiang_D(cfg_pair, n-1, grid=22, memo=memo2)
        if d_pair > tgt + 1e-7:
            pair_fail += 1
        # Check if induction bound overshoots: rest total R' = 1 - 2*a2
        R_prime = 1 - 2*a2
        Dn1 = 2**n - 1  # = 7
        ind_bound = R_prime / Dn1
        if ind_bound > tgt + 1e-9 and d_pair <= tgt + 1e-7:
            pair_overshoot += 1

print(f"n=3: {ntrials} random configs, optimal fails={opt_fail}, pairing fails={pair_fail}")
print(f"  pairing+induction overshoots but still ok: {pair_overshoot}")

# Test specific regime-2 configs (parity clean, R too big) for n=3
print("\n=== Regime 2 (parity clean, R too big) n=3 tests ===")
reg2_configs = [
    [0.52, 0.26, 0.13, 0.09],  # L=0.52 >= 2*0.26, L < 8/15=0.533
    [0.53, 0.26, 0.12, 0.09],
    [0.50, 0.25, 0.15, 0.10],
    [0.52, 0.26, 0.22, 0.00],  # boundary
]
for cfg in reg2_configs:
    cfg = sorted(cfg, reverse=True)
    L = cfg[0]; a2 = cfg[1]
    is_parity_clean = L >= 2*a2
    is_arith_ok = L >= L_thresh
    R = 1 - L
    memo = {}
    d = best_xiang_D(cfg, n, grid=22, memo=memo)
    # Halving: split L into L/2, L/2
    halved = [L/2, L/2] + cfg[1:]
    d_halve = D_alt(halved)
    print(f"  cfg={[round(x,3) for x in cfg]}: parity_clean={is_parity_clean}, arith_ok={is_arith_ok}, optD={d:.6f} ({d/tgt:.3f}x), halve_D={d_halve:.6f}, R/D2={R/7:.6f}")

print("\nDONE")
