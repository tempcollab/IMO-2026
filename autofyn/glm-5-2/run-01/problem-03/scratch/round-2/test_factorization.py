from fractions import Fraction

# ---------------------------------------------------------------
# PART 2: Verify the arithmetic factorization of the dominant case.
# D_n = 2^{n+1} - 1.  D_{n-1} = 2^n - 1.
# Target: D <= 1/D_n.
# Rest total R = 1 - L.
# Dominant threshold: L >= 2*a_2  (the orchestrator's "L >= 2*a_2").
#   Also orchestrator mentions "L >= 2^n/D_n" as a possible threshold.
# These DIFFER. Let's work out which matters.
#
# The inductive argument:
#   - Split L into L/2, L/2 (requires L/2 >= a_2 to be "dominant").
#   - D(total) = D(rest), rest total = R = 1-L.
#   - By induction (n-1 game), Xiang forces D(rest_rescaled) <= 1/D_{n-1}
#     where rest is RESCALED to total 1.
#   - D is HOMOGENEOUS: scaling all pieces by c scales D by c.
#     So D(rest) = R * D(rest_rescaled) <= R * (1/D_{n-1}).
#   - For the bound D <= 1/D_n we need R/D_{n-1} <= 1/D_n,
#     i.e. R <= D_{n-1}/D_n = (2^n-1)/(2^{n+1}-1).
#   - Since R = 1 - L, this is L >= 1 - (2^n-1)/(2^{n+1}-1) = (2^{n+1}-1 - 2^n + 1)/(2^{n+1}-1)
#       = 2^n / (2^{n+1}-1) = 2^n/D_n.
# So the FACTORIZATION threshold is L >= 2^n/D_n (NOT L >= 2*a_2).
#
# The split-into-halves STAYS dominant (parity clean) requires L >= 2*a_2.
# So we have TWO conditions:
#   (A) L >= 2*a_2  (parity: halves occupy positions 1,2)
#   (B) L >= 2^n/D_n  (arithmetic: R small enough that induction closes)
# The dominant case = BOTH hold.
# ---------------------------------------------------------------

# Verify the equality (2^n - 1)/D_{n-1} = 1, i.e. D_{n-1} = 2^n - 1.
for n in range(2, 8):
    Dn = 2**(n+1) - 1
    Dn1 = 2**n - 1  # D_{n-1}
    assert Dn1 == (2**n - 1)
    # (2^n - 1)/D_{n-1} = 1 trivially since D_{n-1} = 2^n-1. YES.
    # And R/D_{n-1} with R = (2^n-1)/D_n gives (2^n-1)/(D_n * D_{n-1}) = 1/D_n. 
    R_max = Fraction(2**n - 1, Dn)  # R = 1 - 2^n/D_n
    bound = R_max / Dn1
    target = Fraction(1, Dn)
    print(f"n={n}: L_threshold=2^n/D_n={Fraction(2**n,Dn)}, R_max={R_max}, R/D_{{n-1}}={bound}, 1/D_n={target}, equal={bound==target}")

# Verify homogeneity of D.
def D_exact(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i) * s[i] for i in range(len(s)))

from fractions import Fraction as F
import random
random.seed(1)
hom_ok = True
for _ in range(1000):
    k = random.randint(2,5)
    a = [F(random.randint(1,9), random.randint(1,9)) for _ in range(k)]
    c = F(random.randint(1,5), random.randint(1,5))
    if D_exact([c*x for x in a]) != c * D_exact(a):
        hom_ok = False
        break
print("Homogeneity of D:", hom_ok)

print("PART 2 DONE")
