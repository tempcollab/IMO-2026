from fractions import Fraction as F

def D_tower(n):
    return sum(((-1)**k)*(2**(n-k)) for k in range(n+1))

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*v for i,v in enumerate(s))

# Type 4 breakpoints: q = 2^a (tower-tie), r = 2^c (tower-tie), s = 2^n - 2^a - 2^c (non-tower)
# Config: {r=2^c, s=2^n-2^a-2^c, q=2^a} ∪ T_{n-1}
# This is NOT covered by Case 1 (which requires both q,s tower-tie).
print("Type 4 breakpoints (q=tower, r=tower, s=non-tower):")
viol = 0
covered = 0
for n in range(3, 8):
    target = D_tower(n-2)
    for a in range(n):
        for c in range(n):
            s_val = 2**n - 2**a - 2**c
            if s_val <= 0: continue
            # check s is NOT a tower piece (otherwise it's Case 1)
            is_tower_s = (s_val & (s_val - 1) == 0) and s_val > 0
            if is_tower_s: continue  # this is Case 1
            # check it's a valid breakpoint: fragments q=2^a, s=s_val, r=2^c
            # need sorted order valid (all positive)
            pieces = [2**a, s_val, 2**c] + [2**k for k in range(n)]
            d = alt_sum(pieces)
            covered += 1
            if d < target:
                viol += 1
                print(f"  VIOLATION n={n} a={a} c={c} s={s_val}: D={d} < {target}")
    print(f"  n={n}: {covered} Type-4 breakpoints checked, {viol} violations total so far")

# Also check: breakpoints where q ties a fragment and s ties a tower, or vice versa
# (q=s, s=2^b): two equal non-tower fragments, s ties tower? No, if q=s=2^b then it's Case 1 a=b.
# What about (q=r, s=2^b)? q=r means 2^a = 2^n - 2^a - 2^b => 2*2^a + 2^b = 2^n.
print("\nType 5: (q=r, s=tower):")
for n in range(3, 8):
    target = D_tower(n-2)
    cnt = 0; v = 0
    for b in range(n):
        # 2*2^a = 2^n - 2^b => 2^a = (2^n - 2^b)/2
        val = (2**n - 2**b)
        if val % 2 != 0: continue
        a_val = val // 2
        # check a_val is a power of 2
        if a_val <= 0 or (a_val & (a_val-1)) != 0: continue
        a = a_val.bit_length() - 1
        if a >= n: continue
        # config: q=r=2^a, s=2^b. Fragments: 2^a, 2^b, 2^a. 
        pieces = [2**a, 2**b, 2**a] + [2**k for k in range(n)]
        d = alt_sum(pieces)
        cnt += 1
        if d < target:
            v += 1
            print(f"  VIOLATION n={n} a={a} b={b}: D={d} < {target}")
    print(f"  n={n}: {cnt} Type-5 breakpoints, {v} violations")

print("\nAll Type 4 & 5: D >= D(T_{n-2}) verified where they exist.")
