from fractions import Fraction as F
import random, itertools

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*v for i,v in enumerate(s))

# Verify G1 (gaps+leftover identity)
def gaps_leftover(pieces):
    s = sorted(pieces, reverse=True)
    m = len(s)
    total = F(0)
    for k in range(m // 2):
        total += s[2*k] - s[2*k+1]
    if m % 2 == 1:
        total += s[-1]
    return total

random.seed(2)
mm = 0
for _ in range(20000):
    pieces = [F(random.randint(1,8), random.randint(1,4)) for _ in range(random.randint(2,9))]
    if sum(pieces) == 0: continue
    d = alt_sum(pieces)
    g = gaps_leftover(pieces)
    if d != g:
        mm += 1
        if mm < 5: print("G1 MISMATCH:", pieces, d, g)
print(f"G1 (gaps+leftover) mismatches: {mm}")

# Verify G2 (pairing bound): D >= p_m (m odd), D >= 0 (m even)
viol = 0
for _ in range(20000):
    pieces = sorted([F(random.randint(1,8), random.randint(1,4)) for _ in range(random.randint(2,9))], reverse=True)
    if sum(pieces) == 0: continue
    d = alt_sum(pieces)
    m = len(pieces)
    if m % 2 == 1:
        if d < pieces[-1]:
            viol += 1
    else:
        if d < 0:
            viol += 1
print(f"G2 (pairing bound) violations: {viol}")

# Verify Max-bound conjecture D* <= M/2^n for small n by brute-force optimization
# D*(L) = min over Xiang's <= n marks of D(refined). Hard to compute exactly; use breakpoint enumeration.
# For n=2, m=3 configs: enumerate Liu configs (a1 >= a2 >= a3, sum=1) on a grid, find Xiang's best 2-mark refinement.

def best_xiang_d(pieces, n_marks):
    # Xiang splits pieces (each split = pick a piece, split into two positive parts)
    # Minimize D over all refinements with <= n_marks
    # For exact: breakpoints are where fragments tie. Brute force over breakpoint configs.
    # Simplistic: try all "halving" and "pairing" and "tie to adjacent" splits recursively.
    # For verification, do a fine grid search over split positions.
    best = None
    # current state: list of pieces
    def recurse(current, marks_left):
        nonlocal best
        d = alt_sum(current)
        if best is None or d < best:
            best = d
        if marks_left == 0:
            return
        # try splitting each piece at various positions
        for i in range(len(current)):
            L = current[i]
            if L <= 0: continue
            # grid of split positions
            for q_num in range(1, 20):
                q = F(q_num, 20) * L
                if q <= 0 or q >= L: continue
                new = current[:i] + current[i+1:] + [L - q, q]
                recurse(new, marks_left - 1)
    recurse(list(pieces), n_marks)
    return best

# Test Max-bound for n=2 on random configs
random.seed(3)
viol = 0
worst_ratio = F(0)
for _ in range(200):
    # random 3-piece config
    a = F(random.randint(1,10), 10)
    b = F(random.randint(1,10), 10)
    if a + b >= 1: continue
    c = 1 - a - b
    if c <= 0: continue
    pieces = sorted([a, b, c], reverse=True)
    M = pieces[0]
    dstar = best_xiang_d(pieces, 2)
    bound = M / 4  # M/2^2
    if dstar > bound + F(1,1000):  # tolerance
        viol += 1
        print(f"  Max-bound VIOLATION n=2: pieces={pieces} D*={dstar} M/4={bound}")
    ratio = dstar / bound if bound > 0 else F(0)
    if ratio > worst_ratio:
        worst_ratio = ratio
print(f"Max-bound n=2: violations={viol}, worst ratio={float(worst_ratio):.4f} (tower should give 1.0)")

# Tower T_2 = (4,2,1)/7
tower = [F(4,7), F(2,7), F(1,7)]
dstar_tower = best_xiang_d(tower, 2)
print(f"Tower T_2: D*={dstar_tower} ({float(dstar_tower):.6f}), M/4={tower[0]/4} ({float(tower[0]/4):.6f})")
