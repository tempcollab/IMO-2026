from fractions import Fraction
from itertools import product as iprod

def D_exact(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i) * s[i] for i in range(len(s)))

def best_xiang_D_exact(config, n_marks, num_grid=20, memo=None):
    """Exact Xiang optimizer using Fraction. Splits at rational grid points."""
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

# Verify tower T2 = (4/7, 2/7, 1/7), n=2: Xiang optimal D should be exactly 1/7.
tower2 = [Fraction(4,7), Fraction(2,7), Fraction(1,7)]
memo = {}
d = best_xiang_D_exact(tower2, 2, num_grid=50, memo=memo)
print(f"Tower T2, n=2: optimal D = {d} = {float(d):.6f}, target 1/7 = {1/7:.6f}, equal={d==Fraction(1,7)}")

# Tower T3 = (8/15,4/15,2/15,1/15), n=3: optimal D should be 1/15.
tower3 = [Fraction(8,15), Fraction(4,15), Fraction(2,15), Fraction(1,15)]
memo = {}
d3 = best_xiang_D_exact(tower3, 3, num_grid=30, memo=memo)
print(f"Tower T3, n=3: optimal D = {d3} = {float(d3):.6f}, target 1/15 = {1/15:.6f}, equal={d3==Fraction(1,15)}")

# Now: the THREE REGIMES for n=2, 3 pieces. Find the boundary configs and test.
# Regime 1 (FULL DOMINANT): L >= 2*a_2 AND L >= 4/7.
# Regime 2 (PARITY-CLEAN, R-TOO-BIG): L >= 2*a_2 AND L < 4/7.
# Regime 3 (NON-DOMINANT): L < 2*a_2.
# Test a config in regime 2: L=0.55, a_2=0.275 (=L/2 boundary), a_3=0.175. Actually need L>=2*a_2 strictly.
# L=0.55, a_2=0.27, a_3=0.18: L>=2*0.27=0.54 ✓, L=0.55<4/7≈0.571 ✓. Regime 2.
cfg2 = [Fraction(55,100), Fraction(27,100), Fraction(18,100)]
cfg2 = [Fraction(11,20), Fraction(27,100), Fraction(9,50)]
print(f"\nRegime 2 cfg={[float(x) for x in cfg2]}: L={float(cfg2[0]):.3f}, a2={float(cfg2[1]):.3f}, L>=2a2? {cfg2[0]>=2*cfg2[1]}, L<4/7? {cfg2[0]<Fraction(4,7)}")
memo = {}
d2 = best_xiang_D_exact(cfg2, 2, num_grid=40, memo=memo)
print(f"  Xiang optimal D = {float(d2):.6f}, target 1/7 = {1/7:.6f}, OK={d2<=Fraction(1,7)}")

# Test the halving strategy on this regime-2 config: split L into L/2,L/2.
L = cfg2[0]
halved = [L/2, L/2] + cfg2[1:]
print(f"  Halving D = {float(D_exact(halved)):.6f} (rest D = {float(D_exact(cfg2[1:])):.6f})")
# D(halved) should = D(rest) = D(cfg2[1:]) since L/2 >= a_2 (parity clean: L>=2*a_2 => L/2>=a_2)
# Then need induction: D(rest) <= R/D_1 = R/3 where R = 1-L.
R = 1 - L
print(f"  R = 1-L = {float(R):.4f}, R/D_1 = {float(R/3):.6f}, 1/D_n = {1/7:.6f}, overshoot = {float(R/3 - Fraction(1,7)):.6f}")

# Now test: does Xiang's optimal in regime 2 use halving + something, or a different first move?
# The key: halving gives D(rest), rest has 2 pieces (a_2, a_3) total R, with 1 mark left.
# Xiang can split a_2 or a_3 in rest. Let's see what's optimal.
print("\n=== Regime 2 analysis: after halving L, rest = (a_2, a_3), 1 mark left ===")
rest = sorted(cfg2[1:], reverse=True)
print(f"  rest = {[float(x) for x in rest]}, D(rest) = {float(D_exact(rest)):.6f}")
# Split a_2 into p, a_2-p:
for g in range(1, 20):
    p = Fraction(g, 20) * rest[0]
    if p <= 0 or p >= rest[0]: continue
    newrest = [p, rest[0]-p, rest[1]]
    print(f"    split a_2 at {float(p):.3f}: D = {float(D_exact(newrest)):.6f}")

print("PART 6 DONE")
