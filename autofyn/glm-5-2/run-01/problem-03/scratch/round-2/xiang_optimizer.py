import numpy as np
from fractions import Fraction
from itertools import product

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

# ---------------------------------------------------------------
# Xiang optimizer: given a Liu config (pieces summing to 1), find the min D
# achievable by Xiang with <= n marks (each mark splits one piece into 2).
# We use a recursive/DP approach over marks, with continuous optimization
# (for small configs, brute-force grid over split points).
# ---------------------------------------------------------------

def best_xiang_D(config, n_marks, grid=40, depth=0, memo=None):
    """Min D Xiang can force with n_marks, by trying splits on each piece."""
    config = tuple(sorted(config, reverse=True))
    if memo is None:
        memo = {}
    key = (config, n_marks)
    if key in memo:
        return memo[key]
    # Option 0: use no more marks
    best = D_alt(list(config))
    if n_marks == 0:
        memo[key] = best
        return best
    # Try splitting each piece
    for i in range(len(config)):
        piece = config[i]
        if piece < 1e-12:
            continue
        # split piece i into p + (piece - p), grid over p
        others = list(config[:i]) + list(config[i+1:])
        for g in range(1, grid):
            p = piece * g / grid
            if p < 1e-12 or p > piece - 1e-12:
                continue
            new = others + [p, piece - p]
            d = best_xiang_D(new, n_marks - 1, grid, depth+1, memo)
            if d < best:
                best = d
    memo[key] = best
    return best

# Test on worst non-dominant configs and the equality/dominant configs.
configs = {
    "(1/2,1/4,1/4)": [Fraction(1,2), Fraction(1,4), Fraction(1,4)],
    "(1/2,1/4,1/8,1/8)": [Fraction(1,2), Fraction(1,4), Fraction(1,8), Fraction(1,8)],
    "(0.5,0.26,0.24)": [0.5, 0.26, 0.24],  # strict non-dominant
    "(0.45,0.3,0.25)": [0.45, 0.3, 0.25],  # deep non-dominant
    "tower T2=(4,2,1)/7": [Fraction(4,7), Fraction(2,7), Fraction(1,7)],
    "(1/3,1/3,1/3)": [Fraction(1,3)]*3,  # all equal, non-dominant
    "(0.4,0.3,0.2,0.1)": [0.4,0.3,0.2,0.1],
}

print("=== Xiang's best (min D) with n marks ===")
for name, cfg in configs.items():
    # determine min n such that this is a valid config (pieces = marks+1, marks = len-1 or fewer)
    for n in [1, 2, 3]:
        Dn = 2**(n+1)-1
        tgt = 1.0/Dn
        # use float config
        cfgf = [float(x) for x in cfg]
        # the DP with fractions is exact but slow; use float for larger
        d = best_xiang_D(cfgf, n, grid=30)
        flag = "OK" if d <= tgt + 1e-9 else "OVER"
        print(f"  cfg={name}, n={n}: minD={d:.6f}, tgt=1/D_n={tgt:.6f} [{flag}]")
    print()
