from fractions import Fraction as F
import itertools, random

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*v for i,v in enumerate(s))

def spine(pieces):
    # iteratively remove adjacent-equal pairs until strictly decreasing
    s = sorted(pieces, reverse=True)
    changed = True
    while changed:
        changed = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                changed = True
                break
    return s

# Verify S1: D(M) == D(spine(M))
random.seed(1)
mismatches = 0
for _ in range(20000):
    pieces = [F(random.randint(1,8), random.randint(1,4)) for _ in range(random.randint(2,8))]
    if sum(pieces) == 0: continue
    d1 = alt_sum(pieces)
    sp = spine(pieces)
    d2 = alt_sum(sp)
    if d1 != d2:
        mismatches += 1
        if mismatches < 5:
            print("S1 MISMATCH:", pieces, "D=", d1, "spine=", sp, "Ds=", d2)
print(f"S1 (pair-cancellation) mismatches: {mismatches}")

# Verify S3 geometric bound: for any strictly-decreasing distinct powers of 2, D >= 1
powers = [1, 2, 4, 8, 16, 32, 64]
min_D = None
for r in range(1, len(powers)+1):
    for combo in itertools.combinations(powers, r):
        d = alt_sum(list(combo))
        if min_D is None or d < min_D:
            min_D = d
        if d < 1:
            print("S3 VIOLATION:", combo, "D=", d)
print(f"S3: min D over all nonempty distinct-power-of-2 spines = {min_D}")

# Verify S3 nonempty claim: total mass D_n odd, removed pairs even mass, spine mass odd
# Construct an even-group strong breakpoint of T_3 and check spine = distinct powers of 2, D >= 1
# Example: split 8 -> 4+4 (balanced), split 4 (one of them) -> 2+2, split 2 -> 1+1
# Config: {4, 4, 2, 2, 1, 1, 1} (T_3 = 8,4,2,1; splits produce extra 4,2,1)
# Wait: T_3 = (8,4,2,1). 3 marks. Balanced splits: 8->4+4, 4->2+2, 2->1+1.
# Config: {4,4,2,2,1,1,1}. All dyadic. This is the balanced-pairs config.
pieces = [F(4), F(4), F(2), F(2), F(1), F(1), F(1)]
print("\nBalanced-pairs T_3:", pieces, "D=", alt_sum(pieces), "spine=", spine(pieces), "Ds=", alt_sum(spine(pieces)))

# Non-dyadic even-group strong breakpoint: e.g. 8 -> 5+3 (unbalanced), 3 -> 1.5+1.5 (balanced)
# Config: {5, 4, 2, 1.5, 1.5, 1} -- wait, 5+4+2+1.5+1.5+1 = 15 = D_3. 
# Non-dyadic fragment: 5 (not power of 2). Only one copy -> odd group. Not even-group.
# Try: 8 -> 5+3, 5 -> 2.5+2.5 (balanced). Config {4, 2.5, 2.5, 2, 3, 1}? No, 5->2.5+2.5, 3 unsplit.
# {4, 2.5, 2.5, 3, 2, 1} sorted {4, 3, 2.5, 2.5, 2, 1}. Non-dyadic: 3, 2.5. 2.5 appears twice (even group). 3 once (odd).
# Not even-group. 
# Let me construct an even-group one: 8 -> 4.5+3.5, 4.5 -> 2.25+2.25. Config {4, 3.5, 2.25, 2.25, 2, 1}? sum=4+3.5+2.25+2.25+2+1=15. Non-dyadic: 3.5 (once, odd), 2.25 (twice, even). Odd group present.
# Hard to get pure even-group with non-dyadic. Let me try: 8 -> 4.5+3.5, then 3.5 -> 1.75+1.75. Config {4.5, 4, 2, 1.75, 1.75, 1}? sum=4.5+4+2+1.75+1.75+1=15. Non-dyadic: 4.5 (once, odd), 1.75 (twice, even). Odd group.
# Even-group requires EVERY non-dyadic value to appear even times. With unbalanced splits, the larger fragment is unique unless tied.
# Example: 8 -> 3+5, then 5 -> 3+2. Config {4, 3, 3, 2, 2, 1}? sum=4+3+3+2+2+1=15. Non-dyadic: none (all powers of 2? 3 is not). 3 appears twice (even). 
pieces = [F(4), F(3), F(3), F(2), F(2), F(1)]
print("Even-group T_3:", pieces, "D=", alt_sum(pieces), "spine=", spine(pieces), "Ds=", alt_sum(spine(pieces)))

# Another: 8 -> 3+5, 5 -> 3+2. {4,3,3,2,2,1} same. Or 8->3+5, 4->2+2: {5,3,2,2,2,1}? sum=15. Non-dyadic 5,3. 5 once (odd). 
# Even group with non-dyadic: 8 -> 3+5, 5 -> 3+2: {4,3,3,2,2,1}. 3 is non-dyadic, appears twice. Even group. Spine: remove (3,3) and (2,2): {4,1}. D=4-1=3. >=1 ✓.
# But wait, is {4,3,3,2,2,1} a STRONG breakpoint? Every fragment must tie. Fragments: 3 (from 8->3+5), 3 (from 5->3+2), 2 (from 5->3+2)... 
# Actually 8->3+5 (fragments 3,5), 5->3+2 (fragments 3,2). So fragments are {3,3,2}. Tower pieces {4,2,1}. 
# Fragment 3 ties fragment 3 ✓. Fragment 2 ties tower piece 2 ✓. So strong breakpoint ✓ (every fragment ties).
# But fragment 5? Wait, 8->3+5, then 5 is split into 3+2. So 5 is not a fragment; it's an intermediate. The final fragments from the top are {3, 3, 2}. And the tower pieces are {4, 2, 1}. Total: {3,3,2,4,2,1} = {4,3,3,2,2,1}. 
# Fragments: 3,3,2. Each ties: 3 ties 3 ✓, 2 ties tower 2 ✓. Strong breakpoint ✓.

# Verify the geometric bound for this: spine {4,1}, D = 3 >= 1 ✓.

# Test S3 on many even-group strong breakpoints
print("\n--- S3 verification on constructed even-group strong breakpoints ---")
violations = 0
# Generate: pick a splitting tree of T_n, check if breakpoint is strong & even-group, verify D >= 1
# Simple test: all 2-split refinements of T_3 where both fragments tie
from itertools import product
for n in [3, 4]:
    Dn = 2**(n+1) - 1
    # enumerate 2-mark refinements: split top 2^n -> p+q, then split p -> u+v (or split a tower piece)
    # Just check a bunch of rational breakpoints
    for q in range(1, 2**n):
        for s in range(1, 2**n - q):
            # top split 2^n -> (2^n - q) + q; second split of (2^n-q) -> (2^n-q-s) + s
            a, b, c = 2**n - q - s, q, s
            if a < 0: continue
            tower = [2**k for k in range(n)]  # T_{n-1}
            pieces = [a, b, c] + tower
            # check if strong breakpoint: every fragment (a,b,c) ties an adjacent piece
            sp = sorted(pieces, reverse=True)
            # check each of a,b,c has an equal adjacent in sp
            is_strong = True
            for frag in [a, b, c]:
                # find positions of frag in sp
                positions = [i for i, v in enumerate(sp) if v == frag]
                # at least one pair of adjacent positions
                has_adj = any(positions[j+1] - positions[j] == 1 for j in range(len(positions)-1))
                if not has_adj and len(positions) >= 2:
                    has_adj = True  # any two equal are adjacent after sort? not necessarily
                # actually if value appears >= 2 times, they're adjacent in sorted order
                if sp.count(frag) < 2:
                    is_strong = False
                    break
            if not is_strong: continue
            # check even-group: non-dyadic fragments appear even times
            non_dyadic = [f for f in [a,b,c] if f not in [2**k for k in range(n+1)]]
            from collections import Counter
            cnt = Counter(non_dyadic)
            even_group = all(cnt[v] % 2 == 0 for v in cnt)
            if not even_group: continue
            d = alt_sum(pieces)
            if d < 1:
                violations += 1
                print(f"  S3 VIOLATION n={n} pieces={sp} D={d}")
print(f"S3 violations on 2-split even-group strong breakpoints: {violations}")
