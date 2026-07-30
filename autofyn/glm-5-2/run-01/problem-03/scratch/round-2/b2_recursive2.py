from fractions import Fraction
import numpy as np

def D_exact(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i) * s[i] for i in range(len(s)))

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

# n=2 B2: non-dom 3-piece, a_2 < 2/7. After pairing, rest' has 2 pieces.
# D(rest') = |diff| = max - min. rest' = {L-a2, a3}.
# Since L < 2*a2, L-a2 < a2. Since a3 <= a2, max = max(L-a2, a3).
# D(rest') = |(L-a2) - a3| = |L - a2 - a3| = |L - (1-L)| = |2L-1|.
# For 3 pieces sorted: L >= 1/3, so 2L-1 >= -1/3. But L >= a2 >= a3, L+a2+a3=1.
# L >= 1/3 => 2L >= 2/3, 2L-1 >= -1/3. Could be negative? L=1/3: 2L-1=-1/3<0.
# But D = |2L-1| = 1-2L when L < 1/2. For L < 1/2: D = 1-2L. Need 1-2L < 1/7 => L > 3/7.
# For L in [1/3, 3/7): D = 1-2L >= 1/7. PROBLEM!
print("=== n=2 B2: D(rest') = |2L-1|, need < 1/7 ===")
tgt2 = Fraction(1,7)
fails = 0
for L_num in range(34, 100):
    for a2_num in range(15, 50):
        L = Fraction(L_num, 100)
        a2 = Fraction(a2_num, 100)
        a3 = 1 - L - a2
        if a3 <= 0 or a3 > a2 or L < a2 or L >= 2*a2: continue
        if a2 >= Fraction(2,7): continue  # B2 only
        rest = [L-a2, a3]
        d = D_exact(rest)
        if d > tgt2:
            fails += 1
            if fails <= 5:
                print(f"  B2 FAIL n=2: L={float(L):.3f}, a2={float(a2):.3f}, a3={float(a3):.3f}, D(rest')={float(d):.6f}, |2L-1|={abs(2*L-1)}")
print(f"n=2 B2 unmarked rest' fails: {fails}")
# These are configs where pairing alone (1 mark) doesn't close, need the 2nd mark.
# But Xiang HAS the 2nd mark (n=2, 1 used for pairing, 1 left).

# For these failing configs, does the 2nd mark close it?
# rest' = {L-a2, a3}, 2 pieces, 1 mark. Split the larger into halves.
# rest' = (r1, r2), r1 >= r2. Split r1 into r1/2, r1/2. If r1/2 >= r2: D = r1/2 - r1/2 + r2 = r2.
#   Wait: (r1/2, r1/2, r2) sorted. If r1/2 >= r2: D = r1/2 - r1/2 + r2 = r2.
#   Need r2 <= 1/7. r2 = min(L-a2, a3) = min of rest.
# For the failing configs: r2 = a3 (since a3 <= a2 and L-a2 could be > or < a3).
print("\n  Checking if 2nd mark (halve larger of rest') closes failing configs:")
for L_num in range(34, 50):  # L < 1/2 range
    for a2_num in range(15, 50):
        L = Fraction(L_num, 100)
        a2 = Fraction(a2_num, 100)
        a3 = 1 - L - a2
        if a3 <= 0 or a3 > a2 or L < a2 or L >= 2*a2: continue
        if a2 >= Fraction(2,7): continue
        rest = sorted([L-a2, a3], reverse=True)
        r1, r2 = rest
        d_unmarked = r1 - r2
        if d_unmarked <= tgt2: continue  # already ok
        # Halve r1: split into r1/2, r1/2
        if r1/2 >= r2:
            d_after = r2  # (r1/2, r1/2, r2), D = r2
        else:
            # r1/2 < r2: sorted (r2, r1/2, r1/2), D = r2 - r1/2 + r1/2 = r2. SAME!
            d_after = r2
        # Actually: (r2, r1/2, r1/2) sorted if r2 > r1/2. D = r2 - r1/2 + r1/2 = r2.
        # (r1/2, r1/2, r2) sorted if r1/2 >= r2. D = r1/2 - r1/2 + r2 = r2.
        # Either way D = r2 after halving r1!
        if d_after > tgt2:
            print(f"    2-mark FAIL: L={float(L):.3f}, a2={float(a2):.3f}, a3={float(a3):.3f}, r2={float(r2):.4f} > 1/7")

# KEY: after pairing + halving the rest's larger piece, D = min(rest) = r2.
# Need r2 <= 1/7. r2 = min(L-a2, a3). 
# a3 = 1-L-a2. L-a2. min depends.
print("\n  KEY: after pairing+halving, D = r2 = min(L-a2, a3). Need r2 <= 1/7.")
print("  r2 = min(L-a2, 1-L-a2). For B2 (a2 < 2/7, L < 2*a2):")
maxr2 = Fraction(0)
for L_num in range(34, 100):
    for a2_num in range(15, 50):
        L = Fraction(L_num, 100)
        a2 = Fraction(a2_num, 100)
        a3 = 1 - L - a2
        if a3 <= 0 or a3 > a2 or L < a2 or L >= 2*a2: continue
        if a2 >= Fraction(2,7): continue
        r2 = min(L-a2, a3)
        if r2 > maxr2:
            maxr2 = r2
print(f"  max r2 in B2 = {maxr2} = {float(maxr2):.6f}, 1/7 = {float(tgt2):.6f}, ok={maxr2 <= tgt2}")
print("DONE")
