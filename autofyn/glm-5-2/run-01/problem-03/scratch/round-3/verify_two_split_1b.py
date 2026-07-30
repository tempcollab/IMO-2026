from fractions import Fraction as F

def D_tower(n):
    return sum(((-1)**k)*(2**(n-k)) for k in range(n+1))

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*v for i,v in enumerate(s))

# Sub-case 1b: q = 2^{n-1} (balanced first split), second cut = 2^m
# Fragments: 2^{n-1} (unsplit half), r = 2^{n-1}-2^m, 2^m. Plus T_{n-1}.
def two_split_1b_direct(n, m):
    r = 2**(n-1) - 2**m
    # T_{n-1} = (2^{n-1}, ..., 1) = [2**k for k in range(n)]
    pieces = [2**(n-1), r, 2**m] + [2**k for k in range(n)]
    return alt_sum(pieces)

def two_split_1b_formula(n, m):
    c = 3 + (-1)**(n+m-1)
    return (2**n + (-1)**n - c*2**m)//3

print("Sub-case 1b verification (fixed T_{n-1}):")
mm = 0
for n in range(3, 8):
    for m in range(n-1):
        direct = two_split_1b_direct(n, m)
        formula = two_split_1b_formula(n, m)
        if direct != formula:
            mm += 1
            print(f"  MISMATCH n={n} m={m}: direct={direct} formula={formula} r={2**(n-1)-2**m}")
print(f"  mismatches: {mm}")

# Verify D >= D(T_{n-2})
print("\nD >= D(T_{n-2}) check (1b):")
viol = 0
for n in range(3, 8):
    target = D_tower(n-2)
    for m in range(n-1):
        d = two_split_1b_direct(n, m)
        if d < target:
            viol += 1
            print(f"  VIOLATION n={n} m={m}: D={d} < target={target}")
print(f"  violations: {viol}")

# Case 2: balanced second split s = r = (2^n - q)/2
# Config: {q, s, r} with s=r, plus T_{n-1}. Two equal fragments cancel.
# Remaining: {q} ∪ T_{n-1}. If q = 2^a, D = D(T_{n-1} \ {2^a}).
def case2_direct(n, a):
    q = 2**a
    pieces = [q] + [2**k for k in range(n)]  # {2^a} ∪ T_{n-1}
    return alt_sum(pieces)

def case2_formula(n, a):
    return (2**n + (-1)**n + (-1)**(n+a)*2**a)//3

print("\nCase 2 verification:")
mm = 0
for n in range(3, 8):
    for a in range(n):
        d = case2_direct(n, a)
        f = case2_formula(n, a)
        if d != f:
            mm += 1
            print(f"  MISMATCH n={n} a={a}: direct={d} formula={f}")
print(f"  mismatches: {mm}")

# Case 4: all equal q=s=r=2^n/3. D = D({2^n/3} ∪ T_{n-1}).
# Claim D = D(T_{n-2}) + 2^{n-1}/3
from fractions import Fraction
def case4_direct(n):
    v = Fraction(2**n, 3)
    pieces = [v] + [Fraction(2**k) for k in range(n)]
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*v2 for i,v2 in enumerate(s))

def case4_formula(n):
    return Fraction(D_tower(n-2) + 2**(n-1), 3)

print("\nCase 4 verification:")
for n in range(2, 8):
    if 2**n % 3 != 0: 
        # only valid if 2^n divisible by 3 — never! 2^n not div by 3
        print(f"  n={n}: 2^n not divisible by 3, case 4 needs n such that...")
# Actually case 4 (q=s=r=2^n/3) requires q+s+r = 2^n with all equal, so each = 2^n/3.
# This is only integer if 3 | 2^n, which never happens. But as real numbers it's fine.
# Let's compute as Fraction.
for n in range(2, 8):
    d = case4_direct(n)
    f = case4_formula(n)
    print(f"  n={n}: direct={d} ({float(d):.4f}) formula={f} ({float(f):.4f}) D(T_(n-2))={D_tower(n-2)}")
