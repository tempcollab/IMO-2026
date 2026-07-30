from fractions import Fraction as F
import itertools

def D_tower(n):
    # D(T_n) = 2^n - 2^{n-1} + ... + (-1)^n
    return sum(((-1)**k)*(2**(n-k)) for k in range(n+1))

def alt_sum(pieces):
    # pieces sorted descending
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*v for i,v in enumerate(s))

# Verify D_tower matches (2^{n+1}+(-1)^n)/3
for n in range(8):
    val = D_tower(n)
    formula = (2**(n+1) + (-1)**n)//3
    assert val == formula, f"n={n}: {val} vs {formula}"
print("D_tower OK", [D_tower(n) for n in range(8)])

# Two-split lemma: both cuts on top's fragments.
# Config: {r, 2^b, 2^a} ∪ T_{n-1}, r = 2^n - 2^a - 2^b, r >= 2^{n-1} (Sub-case 1a)
# Claim: D = D(T_n) - (c_M*2^M + c_m*2^m)/3
# c_M = 3 + (-1)^{n+M}, c_m = 3 + (-1)^{n+m+1}
# M = max(a,b), m = min(a,b)

def two_split_1a_formula(n, a, b):
    M, m = max(a,b), min(a,b)
    cM = 3 + (-1)**(n+M)
    cm = 3 + (-1)**(n+m+1)
    return D_tower(n) - (cM*2**M + cm*2**m)//3

def two_split_1a_direct(n, a, b):
    assert a < n and b < n  # cuts at tower pieces below 2^{n-1}
    r = 2**n - 2**a - 2**b
    assert r >= 2**(n-1), f"r={r} < 2^(n-1)={2**(n-1)}"
    tower_rest = [2**k for k in range(n)]  # T_{n-1}: 2^{n-1},...,1
    pieces = [r, 2**b, 2**a] + tower_rest
    return alt_sum(pieces)

print("\nSub-case 1a verification:")
mismatches = 0
for n in range(3, 8):
    for a in range(n):
        for b in range(n):
            r = 2**n - 2**a - 2**b
            if r < 2**(n-1): continue
            if a == b: continue  # handled separately
            direct = two_split_1a_direct(n, a, b)
            formula = two_split_1a_formula(n, a, b)
            if direct != formula:
                mismatches += 1
                print(f"  MISMATCH n={n} a={a} b={b}: direct={direct} formula={formula}")
print(f"  1a mismatches: {mismatches}")

# Sub-case 1b: r < 2^{n-1}, forces M = n-1
# Claim: D = (2^n + (-1)^n - c*2^m)/3, c = 3 + (-1)^{n+m-1}
def two_split_1b_formula(n, m):
    c = 3 + (-1)**(n+m-1)
    return (2**n + (-1)**n - c*2**m)//3

def two_split_1b_direct(n, m):
    # one cut is 2^{n-1} (balanced), the other is 2^m
    # r = 2^{n-1} - 2^m, q = 2^{n-1}, s = 2^m (assume m < n-1)
    # Actually: r = 2^n - 2^{n-1} - 2^m = 2^{n-1} - 2^m
    r = 2**(n-1) - 2**m
    pieces = [r, 2**m, 2**(n-1)] + [2**k for k in range(n-1)]  # T_{n-1}
    return alt_sum(pieces)

print("\nSub-case 1b verification:")
mismatches = 0
for n in range(3, 8):
    for m in range(n-1):
        direct = two_split_1b_direct(n, m)
        formula = two_split_1b_formula(n, m)
        if direct != formula:
            mismatches += 1
            print(f"  MISMATCH n={n} m={m}: direct={direct} formula={formula}")
print(f"  1b mismatches: {mismatches}")

# Verify D >= D(T_{n-2})
print("\nD >= D(T_{n-2}) check:")
violations = 0
for n in range(3, 8):
    target = D_tower(n-2)
    # 1a
    for a in range(n):
        for b in range(n):
            if a == b: continue
            r = 2**n - 2**a - 2**b
            if r < 2**(n-1): continue
            d = two_split_1a_direct(n, a, b)
            if d < target:
                violations += 1
                print(f"  1a VIOLATION n={n} a={a} b={b}: D={d} < {target}")
    # 1b
    for m in range(n-1):
        d = two_split_1b_direct(n, m)
        if d < target:
            violations += 1
            print(f"  1b VIOLATION n={n} m={m}: D={d} < {target}")
print(f"  violations: {violations}")

# Now the a=b case (three copies of 2^a)
# Claim: D = D(T_n) - 2^{a+1}
def two_split_ab_equal_direct(n, a):
    # three fragments all 2^a? No: r = 2^n - 2*2^a, and q = s = 2^a
    # config: {r, 2^a, 2^a} ∪ T_{n-1}, r = 2^n - 2^{a+1}
    r = 2**n - 2**(a+1)
    pieces = [r, 2**a, 2**a] + [2**k for k in range(n)]
    return alt_sum(pieces)

def two_split_ab_equal_formula(n, a):
    return D_tower(n) - 2**(a+1)

print("\na=b case verification:")
mm = 0
for n in range(3, 8):
    for a in range(n):
        r = 2**n - 2**(a+1)
        if r < 2**a: continue  # need r >= 2^a (sorted)
        direct = two_split_ab_equal_direct(n, a)
        formula = two_split_ab_equal_formula(n, a)
        if direct != formula:
            mm += 1
            print(f"  MISMATCH n={n} a={a}: direct={direct} formula={formula}")
print(f"  mismatches: {mm}")

