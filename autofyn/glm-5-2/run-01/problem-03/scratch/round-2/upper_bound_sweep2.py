import numpy as np

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

def best_xiang_D(config, n_marks, grid=30, memo=None):
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

# n=2 only (fast), thorough. n=3 with very small grid/sample.
for n, ntrials, grid_val in [(2, 8000, 45), (3, 600, 18)]:
    Dn = 2**(n+1)-1
    tgt = 1.0/Dn
    L_thresh = 2.0**n / Dn
    violations = 0
    max_ratio = 0
    hardest_cfg = None
    regime_max = {"1_full_dom": 0, "2_parity_R_big": 0, "3_nondom": 0}
    regime_count = {"1_full_dom": 0, "2_parity_R_big": 0, "3_nondom": 0}
    regime_hardest = {"1_full_dom": None, "2_parity_R_big": None, "3_nondom": None}
    rng = np.random.default_rng(123)
    for _ in range(ntrials):
        k = rng.integers(1, n+2)
        a = np.sort(rng.dirichlet(np.ones(k)))[::-1]
        L = a[0]
        a2 = a[1] if k >= 2 else 0
        memo = {}
        d = best_xiang_D(a, n, grid=grid_val, memo=memo)
        ratio = d / tgt
        if ratio > max_ratio:
            max_ratio = ratio; hardest_cfg = a.copy()
        if d > tgt + 1e-7:
            violations += 1
        if k == 1:
            reg = "1_full_dom"
        elif L >= 2*a2 and L >= L_thresh:
            reg = "1_full_dom"
        elif L >= 2*a2:
            reg = "2_parity_R_big"
        else:
            reg = "3_nondom"
        regime_count[reg] += 1
        if d > regime_max[reg]:
            regime_max[reg] = d; regime_hardest[reg] = a.copy()
    print(f"n={n}: {ntrials} configs, violations={violations}, max_ratio={max_ratio:.4f}, hardest={np.round(hardest_cfg,4)}")
    for reg in ["1_full_dom", "2_parity_R_big", "3_nondom"]:
        if regime_count[reg] > 0:
            print(f"  {reg}: n={regime_count[reg]}, maxD={regime_max[reg]:.6f} ({regime_max[reg]/tgt:.3f}x tgt), hardest={np.round(regime_hardest[reg],4)}")

print("DONE")
