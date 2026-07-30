import numpy as np

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

def best_xiang_D(config, n_marks, grid=14, memo=None):
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

n = 3
Dn = 15
tgt = 1.0/Dn
rng = np.random.default_rng(77)
ntrials = 250
opt_fail = 0; pair_fail = 0
for _ in range(ntrials):
    k = rng.integers(1, n+2)
    a = np.sort(rng.dirichlet(np.ones(k)))[::-1]
    L = a[0]; a2 = a[1] if k >= 2 else 0
    memo = {}
    d_opt = best_xiang_D(a, n, grid=14, memo=memo)
    if d_opt > tgt + 1e-7: opt_fail += 1
    if k >= 2 and L < 2*a2:
        cfg_pair = [a2, a2, L-a2] + list(a[2:])
        memo2 = {}
        d_pair = best_xiang_D(cfg_pair, n-1, grid=14, memo=memo2)
        if d_pair > tgt + 1e-7: pair_fail += 1
print(f"n=3: {ntrials} configs, opt_fail={opt_fail}, pair_fail={pair_fail}")
for cfg in [[0.52,0.26,0.13,0.09],[0.50,0.25,0.15,0.10]]:
    cfg = sorted(cfg, reverse=True)
    memo = {}
    d = best_xiang_D(cfg, n, grid=14, memo=memo)
    halved = [cfg[0]/2, cfg[0]/2] + cfg[1:]
    print(f"  reg2 cfg={[round(x,3) for x in cfg]}: optD={d:.6f} ({d/tgt:.3f}x), halveD={D_alt(halved):.6f}")
print("DONE")
