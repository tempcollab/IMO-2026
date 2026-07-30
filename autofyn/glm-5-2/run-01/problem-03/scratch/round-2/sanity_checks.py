from fractions import Fraction
from itertools import product

def alt_sum(pieces):
    """Alternating sum of sorted-descending multiset."""
    s = sorted(pieces, reverse=True)
    D = Fraction(0)
    for i, x in enumerate(s):
        D += x if i % 2 == 0 else -x
    return D

def D_tower(m):
    """D(T_m) in tower units: T_m = (2^m,...,1), total = 2^{m+1}-1. Alternating sum."""
    pieces = [2**k for k in range(m, -1, -1)]  # 2^m, 2^{m-1},...,1
    return alt_sum(pieces)

# 1. Frontier recursion: D(T_m) = 2^m - D(T_{m-1}), D(T_0)=D(T_1)=1
print("=== Frontier recursion D(T_m) = 2^m - D(T_{m-1}) ===")
prev = {0: D_tower(0), 1: D_tower(1)}
print(f"D(T_0) = {prev[0]} (expect 1)")
print(f"D(T_1) = {prev[1]} (expect 1)")
for m in range(2, 8):
    Dm = D_tower(m)
    rec = 2**m - prev[m-1]
    print(f"D(T_{m}) = {Dm}, recursion 2^{m}-D(T_{m-1}) = {rec}, match={Dm==rec}")
    prev[m] = Dm

# 2. Parallel halving against tower T_n gives D = 1/D_n (tower units: D=1)
print("\n=== Parallel halving saturates tower: D=1 (tower units) ===")
for n in range(1, 6):
    # Split each of the n largest pieces 2^k -> 2^{k-1}+2^{k-1}
    pieces = []
    # tower T_n pieces: 2^n, 2^{n-1},...,2,1
    tower = [2**k for k in range(n, -1, -1)]
    # split each of the n largest (2^n,...,2^1) in half
    for k in range(n, 0, -1):
        pieces.append(2**(k-1))
        pieces.append(2**(k-1))
    pieces.append(1)  # the smallest piece unsplit
    D = alt_sum(pieces)
    print(f"n={n}: parallel-halving D (tower units) = {D}, expect 1, match={D==1}")

# 3. Tower is hardest: for n=2, every non-tower /7 config admits D=0 (odd-index=1/2)
# Check via grid search of Xiang's best response (min D over splits)
def xiang_best_D(pieces, n_marks, grid_points=None):
    """Brute force Xiang's best (min) D by trying splits greedily.
    pieces: list of Fraction (sum 1). n_marks: Xiang's budget.
    Returns min D achievable."""
    # We do a simple recursive: at each step, try splitting each piece at grid points
    # This is exponential but fine for small.
    best = [alt_sum(pieces)]  # no more marks
    def rec(cur, marks_left):
        # record
        best[0] = min(best[0], alt_sum(cur))
        if marks_left == 0:
            return
        for i in range(len(cur)):
            for q_frac in grid_points:
                L = cur[i]
                if L <= 0:
                    continue
                q = L * q_frac
                p = L - q
                if p <= 0 or q <= 0:
                    continue
                new = list(cur)
                new[i] = p
                new.append(q)
                rec(new, marks_left - 1)
    rec(list(pieces), n_marks)
    return best[0]

print("\n=== Tower is hardest (n=2): every non-tower /7 config admits D=0 ===")
D2 = 7
grid = [Fraction(1,k) for k in range(2,8)] + [Fraction(1,2)]
# enumerate /7 configs (3 or fewer pieces)
configs_3 = []
for a in range(1, D2-1):
    for b in range(a, D2-a+1):
        c = D2 - a - b
        if c < b: continue
        if c < 0: continue
        configs_3.append((Fraction(a,D2), Fraction(b,D2), Fraction(c,D2)))
configs_2 = []
for a in range(1, D2):
    b = D2 - a
    if b > a: continue
    configs_2.append((Fraction(a,D2), Fraction(b,D2)))

tower2 = (Fraction(4,7), Fraction(2,7), Fraction(1,7))
print(f"n=2 tower D (no marks) = {alt_sum(tower2)} (expect 1/7 = {Fraction(1,7)})")
best_tower = xiang_best_D(tower2, 2, grid)
print(f"n=2 tower Xiang-best D (2 marks) = {best_tower} (expect 1/7)")

# Check a few non-tower configs
nontowers = [(Fraction(5,7),Fraction(1,7),Fraction(1,7)),
             (Fraction(3,7),Fraction(3,7),Fraction(1,7)),
             (Fraction(3,7),Fraction(2,7),Fraction(2,7)),
             (Fraction(5,7),Fraction(2,7)),
             (Fraction(4,7),Fraction(3,7)),
             (Fraction(6,7),Fraction(1,7))]
for cfg in nontowers:
    bd = xiang_best_D(cfg, 2, grid)
    print(f"  non-tower {cfg}: Xiang-best D = {bd}, D=0? {bd==0}")

