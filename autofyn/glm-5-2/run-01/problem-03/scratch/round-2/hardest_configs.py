import numpy as np

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

def best_xiang_D(config, n_marks, grid=50, memo=None):
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

n = 2
Dn = 2**(n+1)-1
tgt = 1.0/Dn

hardest = []
N = 80
for i in range(N):
    for j in range(i, N):
        a1 = (i+1) / (N+2)
        a2 = (j-i) / (N+2) if j > i else 1.0/(N+2)
        a3 = 1 - a1 - a2
        if a3 < 0.001 or a3 > a2 + 1e-9:
            continue
        cfg = sorted([a1, a2, a3], reverse=True)
        if abs(sum(cfg) - 1) > 1e-9: continue
        if cfg[0] < cfg[1] - 1e-9 or cfg[1] < cfg[2] - 1e-9: continue
        memo = {}
        d = best_xiang_D(cfg, n, grid=35, memo=memo)
        if d > tgt - 1e-6:
            hardest.append((d, cfg))

for a1 in np.linspace(0.5, 1.0, 50):
    cfg = [a1, 1-a1]
    memo = {}
    d = best_xiang_D(cfg, n, grid=35, memo=memo)
    if d > tgt - 1e-6:
        hardest.append((d, cfg))

memo = {}
d = best_xiang_D([1.0], n, grid=35, memo=memo)
if d > tgt - 1e-6:
    hardest.append((d, [1.0]))

hardest.sort(reverse=True)
print(f"n=2: {len(hardest)} configs with optimal D >= target ({tgt:.6f}):")
for d, cfg in hardest[:20]:
    if len(cfg) >= 2:
        regime = "DOMINANT" if cfg[0] >= 2*cfg[1] else "NON-DOMINANT"
    else:
        regime = "1-piece"
    print(f"  D={d:.6f} (tgt={tgt:.6f}, ratio={d/tgt:.3f}x) cfg={[round(x,4) for x in cfg]} [{regime}]")

print("\nPART 5 DONE")
