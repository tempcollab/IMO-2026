import numpy as np
from fractions import Fraction

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

def best_xiang_D(config, n_marks, grid=40, memo=None):
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

# ---------------------------------------------------------------
# PART 8: Test candidate strategies for the non-dominant case (n=2, 3 pieces).
# Strategy A: HALVE L (split L into L/2, L/2). In non-dom, L/2 < a_2, so halves
#   interleave with rest. Not clean parity. But how bad is D after this + remaining marks?
# Strategy B: PAIR (split L into a_2, L-a_2). Creates pair (a_2,a_2). Clean parity for that pair.
# Strategy C: PAIR-with-a_3 (split L into a_3, L-a_3). Creates pair (a_3, a_3) IF a_3 is large enough.
# Strategy D: the true optimal (brute force).
# For each non-dominant config, compare D after each strategy (using remaining marks optimally).
# ---------------------------------------------------------------
n = 2
Dn = 2**(n+1)-1
tgt = 1.0/Dn
rng = np.random.default_rng(42)

results = {"A_halve": [], "B_pair_a2": [], "C_pair_a3": [], "D_optimal": []}
fail_strategies = {"A_halve": 0, "B_pair_a2": 0, "C_pair_a3": 0, "D_optimal": 0}

for _ in range(3000):
    a = np.sort(rng.dirichlet(np.ones(3)))[::-1]
    L, a2, a3 = a
    if L >= 2*a2: continue  # skip dominant
    
    # Strategy A: halve L
    cfgA = [L/2, L/2, a2, a3]
    memoA = {}
    dA = best_xiang_D(cfgA, n-1, grid=35, memo=memoA)  # 1 mark used for halving, 1 left
    results["A_halve"].append(dA)
    if dA > tgt + 1e-7: fail_strategies["A_halve"] += 1
    
    # Strategy B: pair with a_2 (split L into a_2, L-a_2)
    cfgB = [a2, L-a2, a2, a3]
    memoB = {}
    dB = best_xiang_D(cfgB, n-1, grid=35, memo=memoB)
    results["B_pair_a2"].append(dB)
    if dB > tgt + 1e-7: fail_strategies["B_pair_a2"] += 1
    
    # Strategy C: pair with a_3 (split L into a_3, L-a_3) — only if a_3 <= L/2
    if a3 <= L/2 and a3 > 0:
        cfgC = [L-a3, a3, a2, a3]  # sorted later
        memoC = {}
        dC = best_xiang_D(cfgC, n-1, grid=35, memo=memoC)
        results["C_pair_a3"].append(dC)
        if dC > tgt + 1e-7: fail_strategies["C_pair_a3"] += 1
    else:
        results["C_pair_a3"].append(None)
    
    # Strategy D: optimal
    memoD = {}
    dD = best_xiang_D(a, n, grid=40, memo=memoD)
    results["D_optimal"].append(dD)
    if dD > tgt + 1e-7: fail_strategies["D_optimal"] += 1

for s in ["A_halve", "B_pair_a2", "C_pair_a3", "D_optimal"]:
    vals = [v for v in results[s] if v is not None]
    if vals:
        print(f"{s}: n={len(vals)}, maxD={max(vals):.6f} ({max(vals)/tgt:.3f}x tgt), fails={fail_strategies[s]}")

print("\nPART 8 DONE")
