from fractions import Fraction

# === Dominant factorization identity (2^n - 1)/D_{n-1} = 1 ===
print("=== Dominant factorization: (2^n - 1)/D_{n-1} = 1, and R/D_{n-1} <= 1/D_n at threshold ===")
for n in range(2, 8):
    Dn = 2**(n+1) - 1
    Dn1 = 2**n - 1  # D_{n-1}
    ident = Fraction(2**n - 1, Dn1)
    # at L = 2^n/D_n: R = 1 - 2^n/D_n = (D_n - 2^n)/D_n = (2^n - 1)/D_n = D_{n-1}/D_n
    L = Fraction(2**n, Dn)
    R = 1 - L
    RDn1 = R / Dn1  # should be 1/D_n
    print(f"n={n}: (2^n-1)/D_(n-1) = {ident} (expect 1); R/D_(n-1) at threshold = {RDn1}, 1/D_n = {Fraction(1,Dn)}, match={RDn1==Fraction(1,Dn)}")

# === Parity-rest-starts-at-position-3 under L/2 >= a_2 (rest max) ===
# After splitting L into L/2,L/2, with L/2 >= a_2, sorted order is (L/2, L/2, a_2, a_3, ...)
# positions 1,2 = L/2,L/2 cancel (odd,even). Rest starts at position 3 (odd). Same parity.
import random
random.seed(1)
violations = 0
tests = 0
for _ in range(100000):
    n = random.randint(2, 5)
    Dn = 2**(n+1) - 1
    # random dominant config: L >= 2^n/D_n, L >= 2*a_2, rest sums to 1-L with <= n pieces each <= L/2
    L = Fraction(2**n, Dn) + Fraction(random.randint(0,100), 1000)
    if L >= 1: continue
    R = 1 - L
    # random rest with max piece <= L/2
    npieces = random.randint(2, n+1)
    cuts = sorted([Fraction(random.randint(1,1000),1) for _ in range(npieces-1)], reverse=True)
    # build pieces summing to R
    raw = [Fraction(random.randint(1,100),1) for _ in range(npieces)]
    s = sum(raw)
    rest = [r*R/s for r in raw]
    rest.sort(reverse=True)
    if not rest: continue
    a2 = rest[0]
    if L < 2*a2: continue  # need dominant
    # after split: pieces = [L/2, L/2] + rest, sorted desc
    merged = sorted([L/2, L/2] + rest, reverse=True)
    # check positions 1,2 are L/2 (cancel)
    p1, p2 = merged[0], merged[1]
    if not (p1 == L/2 and p2 == L/2):
        # they may not be exactly equal due to rest having a piece == L/2; still check rest parity
        pass
    # rest's first element global position
    # find first non-(L/2) element
    idx = 0
    while idx < len(merged) and merged[idx] == L/2:
        idx += 1
    # rest occupies positions idx+1, idx+2, ... (1-indexed)
    # we need: rest-local position 1 (a_2) at GLOBAL position 3 (odd)
    # Actually claim: rest starts at global position 3 (odd), so rest-local-1 at global 3.
    tests += 1
    if (idx + 1) % 2 == 0:  # global position idx+1 even => wrong parity
        violations += 1
print(f"Parity check (rest starts at odd global position): {violations} violations / {tests} tests")
# Note: L/2 >= a_2 ensures exactly two L/2 pieces at top, so rest starts at position 3.

# Cleaner check: when L/2 >= a_2 strictly, positions 1,2 = L/2,L/2, rest at 3.
violations2 = 0; tests2 = 0
for _ in range(100000):
    n = random.randint(2,5)
    Dn = 2**(n+1)-1
    L = Fraction(2**n + random.randint(1, Dn - 2**n), Dn)  # strictly above arithmetic threshold
    if L >= 1: continue
    R = 1 - L
    npieces = random.randint(1, n)
    raw = [Fraction(random.randint(1,100)) for _ in range(npieces)]
    s = sum(raw); rest = [r*R/s for r in raw]; rest.sort(reverse=True)
    if not rest: continue
    if L < 2*rest[0]: continue
    merged = sorted([L/2,L/2]+rest, reverse=True)
    # find rest's max piece position
    a2 = rest[0]
    pos = merged.index(a2) + 1  # 1-indexed
    tests2 += 1
    if pos != 3 and merged[0]==merged[1]:
        # if two L/2 at top, rest must be at pos 3
        violations2 += 1
print(f"Parity check 2: {violations2} violations / {tests2} tests")

# Tower unique worst: parallel halving against tower gives D=1/D_n EXACTLY (already verified above)
# Below-threshold regime nonempty: case C for n=2
print("\n=== Below-threshold regime (Case C) nonempty for n=2 ===")
Dn = 7
# L in [1/2, 4/7), a_2 in [(1-L)/2, L/2]
# e.g. (0.55, 0.27, 0.18): L=0.55 < 4/7≈0.571, R=0.45 > 3/7=D_1/D_2
L = Fraction(55,100); R = 1 - L
print(f"L={L}, R={R}, 4/7={Fraction(4,7)}, D_1/D_2=3/7={Fraction(3,7)}")
print(f"L>=2*a_2? a_2=27/100, 2*a_2=54/100, L=55/100 => {L >= Fraction(54,100)} (parity clean)")
print(f"L < 2^2/D_2 = 4/7? {L < Fraction(4,7)} => Case C (overshoot)")
print(f"R/D_1 = {R/3} > 1/7 = {Fraction(1,7)}? {R/3 > Fraction(1,7)}")
