import numpy as np
from fractions import Fraction

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

def recursive_strategy(config, n_marks):
    """At each level: if max >= 2*second -> halve max; else -> pair max with second.
    Returns D after applying this strategy with n_marks."""
    pieces = list(config)
    for _ in range(n_marks):
        s = sorted(pieces, reverse=True)
        if len(s) < 2:
            # only 1 piece: halve it
            pieces = [s[0]/2, s[0]/2]
            continue
        L, a2 = s[0], s[1]
        if L >= 2*a2:
            # halve L
            pieces = [L/2, L/2] + s[2:]
        else:
            # pair: split L into a2, L-a2
            pieces = [a2, L-a2] + s[1:]  # s[1:] includes a2 (orig) + rest
    return D_alt(pieces)

def best_xiang_D(config, n_marks, grid=18, memo=None):
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

# Test recursive strategy on n=2 and n=3
for n in [2, 3]:
    Dn = 2**(n+1)-1
    tgt = 1.0/Dn
    rng = np.random.default_rng(42)
    ntrials = 500 if n == 3 else 5000
    rec_fail = 0
    opt_fail = 0
    max_rec_ratio = 0
    for _ in range(ntrials):
        k = rng.integers(1, n+2)
        a = np.sort(rng.dirichlet(np.ones(k)))[::-1]
        d_rec = recursive_strategy(a, n)
        if d_rec > tgt + 1e-9:
            rec_fail += 1
            if d_rec/tgt > max_rec_ratio:
                max_rec_ratio = d_rec/tgt
        if n == 2:
            memo = {}
            d_opt = best_xiang_D(a, n, grid=40, memo=memo)
            if d_opt > tgt + 1e-7: opt_fail += 1
    print(f"n={n}: {ntrials} configs, recursive_strategy fails={rec_fail}, opt fails={opt_fail}, max rec ratio={max_rec_ratio:.3f}")

# Verify on tower configs
for n in [2, 3]:
    Dn = 2**(n+1)-1
    tower = [2**(n-i)/Dn for i in range(n+1)]
    d_rec = recursive_strategy(tower, n)
    print(f"Tower T{n}: recursive D = {d_rec:.6f}, target = {1.0/Dn:.6f}, ratio = {d_rec*Dn:.4f}")

print("DONE")
