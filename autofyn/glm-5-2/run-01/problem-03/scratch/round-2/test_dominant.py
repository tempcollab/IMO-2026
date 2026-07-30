import numpy as np
from itertools import product
from fractions import Fraction

def D_alt(pieces):
    """Alternating (signed) sum of sorted-descending multiset."""
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

def D_exact(pieces):
    """Exact alternating sum with Fractions."""
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i) * s[i] for i in range(len(s)))

# ---------------------------------------------------------------
# PART 1: Verify the dominant-case factorization claim.
# Claim: if L >= 2*a_2 (i.e. L/2 >= a_2 >= ... ), split L into L/2,L/2.
# Then the two halves occupy positions 1,2 (odd,even), cancel in D,
# rest fills positions 3,4,... with SAME parity (pos 3 odd = rest pos 1 odd).
# So D(total) = 0 + D(rest).
# Then induction: D(rest) <= R/D_{n-1} where R = 1-L, and dominant threshold
# L >= 2^n/D_n  =>  R <= (2^n-1)/D_n  => R/D_{n-1} = (2^n-1)/(D_n*D_{n-1}) = 1/D_n.
# ---------------------------------------------------------------

# First: the parity claim. After splitting L into L/2,L/2, the sorted order is:
#   [L/2, L/2, a_2, a_3, ...]   PROVIDED L/2 >= a_2, i.e. L >= 2*a_2.
# Positions: 1=L/2(odd,+), 2=L/2(even,-), 3=a_2(odd,+), 4=a_3(even,-), ...
# So D = (L/2 - L/2) + (a_2 - a_3 + ...) = D(rest) where rest=(a_2,a_3,...) in its OWN order.
# rest-local pos 1 = a_2 = global pos 3 (odd). SAME parity. CONFIRMED algebraically.

# Verify numerically: random Liu configs with L >= 2*a_2, split L into halves, check D==D(rest).
rng = np.random.default_rng(42)
mismatches = 0
for trial in range(200000):
    # random config: 3-5 pieces, sorted desc, sum 1
    k = rng.integers(3, 6)
    raw = rng.dirichlet(np.ones(k))
    a = np.sort(raw)[::-1]
    L = a[0]
    if not (L >= 2*a[1] if k >= 2 else True):
        continue
    # only test configs where L >= 2*a[2] (a_2), i.e. L/2 >= a_2
    if L < 2*a[1]:
        continue
    rest = a[1:]
    halves = [L/2, L/2]
    full = sorted(halves + list(rest), reverse=True)
    D_full = D_alt(full)
    D_rest = D_alt(rest)
    if abs(D_full - D_rest) > 1e-12:
        mismatches += 1
        if mismatches <= 3:
            print("MISMATCH:", a, D_full, D_rest)
print(f"Part1 parity claim: {mismatches} mismatches out of ~{200000} dominant configs")

# Edge: what if there's a TIE, L/2 == a_2? Then sorted order could interleave.
# Test: L/2 == a_2 exactly. The two halves and a_2 are all equal.
# sorted: [L/2, L/2, a_2(=L/2), a_3, ...]. positions 1,2,3 = L/2,L/2,a_2.
# D = L/2 - L/2 + a_2 - ... = a_2 - ... = a_2 + (-a_3 + a_4 ...)
# D(rest) where rest = (a_2, a_3, ...) = a_2 - a_3 + ...
# But global has a_2 at position 3 (odd,+), then a_3 at position 4 (even,-).
# So D_full = L/2 - L/2 + a_2 - a_3 + ... = D(rest). STILL HOLDS.
# The tie is harmless because both halves are equal (cancel) and a_2 takes position 3.
# Test a harder tie: L/2 == a_2, but also a_2 == a_3 (three-way at the top of rest).
L = Fraction(4,7)  # so L/2 = 2/7
rest = [Fraction(2,7), Fraction(2,7), Fraction(1,7)]  # a_2=a_3=2/7=L/2, a_4=1/7
# wait sum must be 1. L=4/7, rest sums to 5/7 != 1-4/7=3/7. Let me fix.
# Use sum 1: L=1/2, rest = [1/4,1/8,1/8] sum=1/2. L/2=1/4=a_2. dominant L=1/2 >= 2*1/4=1/2 yes (equality)
L = Fraction(1,2)
rest = [Fraction(1,4), Fraction(1,8), Fraction(1,8)]
halves = [L/2, L/2]
full = sorted(halves + rest, reverse=True)
print("Tie test L/2==a_2:", [str(x) for x in full], "D_full=", D_exact(full), "D_rest=", D_exact(rest))
# D_full should equal D_rest

print("PART 1 DONE")
