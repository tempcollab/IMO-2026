from fractions import Fraction

def D_exact(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i) * s[i] for i in range(len(s)))

def best_xiang_D_exact(config, n_marks, num_grid=25, memo=None):
    config = tuple(sorted(config, reverse=True))
    if memo is None: memo = {}
    key = (config, n_marks)
    if key in memo: return memo[key]
    best = D_exact(list(config))
    if n_marks == 0:
        memo[key] = best; return best
    for i in range(len(config)):
        piece = config[i]
        others = list(config[:i]) + list(config[i+1:])
        for g in range(1, num_grid):
            p = Fraction(g, num_grid) * piece
            if p <= 0 or p >= piece: continue
            new = others + [p, piece - p]
            d = best_xiang_D_exact(new, n_marks - 1, num_grid, memo)
            if d < best: best = d
    memo[key] = best
    return best

# Verify pairing strategy: split L into (a_2, L-a_2), then optimal n-1 marks on rest.
# For non-dominant 3-piece configs with exact fractions.
n = 2
Dn = 2**(n+1)-1  # = 7
tgt = Fraction(1, 7)

# Test a range of non-dominant 3-piece configs with exact fractions
# Config: (L, a2, a3) with L + a2 + a3 = 1, L >= a2 >= a3, L < 2*a2.
# Parameterize by L and a2: a3 = 1 - L - a2.
test_configs = []
for L_num in range(35, 70):  # L from 0.35 to 0.70
    for a2_num in range(15, L_num+1):
        L = Fraction(L_num, 100)
        a2 = Fraction(a2_num, 100)
        a3 = 1 - L - a2
        if a3 <= 0 or a3 > a2: continue
        if L < a2: continue
        if L >= 2*a2: continue  # skip dominant
        test_configs.append((L, a2, a3))

print(f"Testing {len(test_configs)} non-dominant 3-piece configs (n=2)...")
pairing_fail = 0
optimal_fail = 0
worst_pair = Fraction(0)
worst_pair_cfg = None
for L, a2, a3 in test_configs:
    # Pairing: split L into (a2, L-a2). New config = {a2, a2, L-a2, a3}.
    cfg_pair = [a2, a2, L-a2, a3]
    # 1 mark used, 1 left. Optimal on rest.
    memo = {}
    d_pair = best_xiang_D_exact(cfg_pair, n-1, num_grid=50, memo=memo)
    if d_pair > worst_pair:
        worst_pair = d_pair
        worst_pair_cfg = (L, a2, a3)
    if d_pair > tgt:
        pairing_fail += 1
        if pairing_fail <= 5:
            print(f"  PAIRING FAIL: cfg=({float(L):.3f},{float(a2):.3f},{float(a3):.3f}), D_pair={float(d_pair):.6f}, tgt={float(tgt):.6f}")
    # Optimal
    memo2 = {}
    d_opt = best_xiang_D_exact([L, a2, a3], n, num_grid=50, memo=memo2)
    if d_opt > tgt:
        optimal_fail += 1

print(f"\nPairing(1mark)+optimal(1mark): {pairing_fail} fails out of {len(test_configs)}")
print(f"Full optimal (2 marks): {optimal_fail} fails")
print(f"Worst pairing D = {worst_pair} = {float(worst_pair):.6f} ({float(worst_pair/tgt):.4f}x tgt) at cfg={worst_pair_cfg}")
print(f"  Worst cfg floats: {tuple(float(x) for x in worst_pair_cfg)}")

print("\nPART 9 DONE")
