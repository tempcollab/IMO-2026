import numpy as np
from fractions import Fraction

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

# ---------------------------------------------------------------
# PART 10: The KEY algebraic bound for the non-dominant case.
# After pairing (split L into a_2, L-a_2), rest' = {L-a_2, a_3, ..., a_m},
# total R' = 1 - 2*a_2. The induction closes iff R' <= D_{n-1}/D_n, i.e. a_2 >= 2^{n-1}/D_n.
#
# When a_2 < 2^{n-1}/D_n (Case B2), the induction overshoots. But there's a
# DIRECT bound on D(rest') using only 2-piece structure for small configs.
#
# KEY INSIGHT: In B2, ALL pieces satisfy a_i <= L < 2*a_2 < 2^n/D_n.
# So 2*L - 1 < 2*(2^n/D_n) - 1 = 2^{n+1}/D_n - 1 = 1/D_n.
# If we can show D(config) <= 2*L - 1 (the unmarked D, using 0 marks!),
# then B2 closes for FREE (mark nothing, D already < 1/D_n).
# But D <= 2L-1 is NOT always true (fails for equal pieces).
#
# Alternative: after pairing, D(rest') <= ?. The rest' has max piece <= a_2.
# For 2-piece rest': D = |diff| = |(L-a_2) - a_3| = |L - a_2 - a_3| = |L - (1-L)| = |2L-1|.
#   Since L >= 1/(n+1) >= 1/3 (for n>=2, 3 pieces): 2L-1 >= 0, so D(rest') = 2L-1.
#   And 2L-1 < 2*(2^n/D_n) - 1 = 1/D_n. CLOSES for n=2 (rest has 2 pieces).
#
# For 3-piece rest' (n=3, original 4 pieces): rest' = {L-a_2, a_3, a_4}.
#   D(rest') = ? Can be up to max(rest'). Need a bound.
# ---------------------------------------------------------------

# Verify: for n=2, non-dominant B2 (a_2 < 2/7), D(rest after pairing) = 2L-1 < 1/7.
print("=== n=2 B2 verification: D(rest') = 2L-1 < 1/7 ===")
n = 2; Dn = 7; tgt = Fraction(1,7)
# Grid of non-dominant 3-piece configs with a_2 < 2/7
ok = True
for L_num in range(34, 100):
    for a2_num in range(15, 50):
        L = Fraction(L_num, 100)
        a2 = Fraction(a2_num, 100)
        a3 = 1 - L - a2
        if a3 <= 0 or a3 > a2 or L < a2 or L >= 2*a2: continue
        if a2 >= Fraction(2,7): continue  # only B2
        # Pairing: rest' = {L-a2, a3}, total R' = 1-2*a2
        rest = [L-a2, a3]
        d_rest = D_exact2(rest)
        bound = 2*L - 1
        if d_rest > tgt:
            print(f"  FAIL: L={float(L):.3f}, a2={float(a2):.3f}, a3={float(a3):.3f}, D(rest')={float(d_rest):.6f}")
            ok = False
        if d_rest != bound:
            # D of 2 pieces (a,b) sorted desc = a - b
            r1, r2 = sorted(rest, reverse=True)
            if r1 - r2 != d_rest:
                print(f"  MISMATCH: {float(d_rest)} vs {float(r1-r2)}")
# Actually let me compute properly
def D_exact2(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i) * s[i] for i in range(len(s)))

for L_num in range(34, 100):
    for a2_num in range(15, 50):
        L = Fraction(L_num, 100)
        a2 = Fraction(a2_num, 100)
        a3 = 1 - L - a2
        if a3 <= 0 or a3 > a2 or L < a2 or L >= 2*a2: continue
        if a2 >= Fraction(2,7): continue
        rest = [L-a2, a3]
        d_rest = D_exact2(rest)
        if d_rest > tgt:
            print(f"  B2 FAIL n=2: L={float(L):.3f}, a2={float(a2):.3f}, D={float(d_rest):.6f}")
print("n=2 B2: all close (D(rest')=2L-1 < 1/7)" if ok else "FAILURES FOUND")

# For n=3, B2: after pairing, rest' has 3 pieces. Test if D(rest') <= 1/15 using 2 more marks.
print("\n=== n=3 B2: recursive pairing test ===")
n = 3; Dn3 = 15; tgt3 = 1.0/Dn3
# Generate B2 configs: 4 pieces, non-dominant, a_2 < 4/15
rng = np.random.default_rng(55)
b2_fail_unmarked = 0
b2_fail_2marks = 0
b2_count = 0
for _ in range(500):
    a = np.sort(rng.dirichlet(np.ones(4)))[::-1]
    L, a2 = a[0], a[1]
    if L >= 2*a2: continue  # dominant
    if a2 >= 4/15: continue  # B1, not B2
    b2_count += 1
    # After pairing: rest' = {L-a2, a3, a4}
    rest = sorted([L-a2, a[2], a[3]], reverse=True)
    d_unmarked = D_alt(rest)
    if d_unmarked > tgt3 + 1e-9:
        b2_fail_unmarked += 1
        # Check: is rest' non-dominant? (max < 2*second)
        if rest[0] < 2*rest[1]:
            # Can pair again! Split rest[0] into rest[1], rest[0]-rest[1]
            rest2 = sorted([rest[1], rest[0]-rest[1], rest[1], rest[2]], reverse=True)
            # Two rest[1]'s cancel. rest2' = {rest[0]-rest[1], rest[2]}, total = ...
            # Actually after 2 pairings, 2 marks used, 1 left. rest2'' has 2 pieces.
            d_after_2pair = D_alt([rest[0]-rest[1], rest[2]])
            if d_after_2pair > tgt3 + 1e-9:
                b2_fail_2marks += 1
                if b2_fail_2marks <= 3:
                    print(f"  2-pair FAIL: orig={np.round(a,4)}, rest'={np.round(rest,4)}, D_2pair={d_after_2pair:.6f}")
        else:
            # rest' is dominant. Halve rest[0].
            halved = sorted([rest[0]/2, rest[0]/2, rest[1], rest[2]], reverse=True)
            d_halve = D_alt([rest[0]/2, rest[0]/2] + [rest[1], rest[2]])
            if d_halve > tgt3 + 1e-9:
                b2_fail_2marks += 1
                if b2_fail_2marks <= 3:
                    print(f"  halve FAIL: orig={np.round(a,4)}, rest'={np.round(rest,4)}, D_halve={d_halve:.6f}")

print(f"n=3 B2: {b2_count} configs, unmarked D > tgt: {b2_fail_unmarked}, fail after 2 heuristic marks: {b2_fail_2marks}")
print("DONE")
