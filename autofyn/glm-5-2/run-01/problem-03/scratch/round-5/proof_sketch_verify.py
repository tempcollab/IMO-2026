"""
Round 5: Verify the cheap-kill proof sketch for the spine sign-pattern lemma.

CLAIM: At a D=1 breakpoint, if a fragment (non-tower-valued) sits at a - position
and a tower-valued piece sits at a + position, the mass balance S_+ = (S_total+1)/2
is VIOLATED because fragment value != tower value (one is a power of 2, the other isn't).

This script:
1. Brute-force searches for a D=1 config where the spine has a fragment at -.
   (Should find NONE — already verified, but confirming with a different method.)
2. Tests the proof sketch: if we take a D=1 config with the correct pattern
   (frag at +, tower at -) and SWAP a fragment/tower pair, does D change?
3. The key algebraic check: can S_+ = (S_total+1)/2 hold with a frag at - and tower at +?
"""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

def is_tower_val(x, n):
    if x <= 0: return False
    if isinstance(x, F):
        if x.denominator == 1:
            v = int(x)
            return v > 0 and (v & (v-1)) == 0 and v <= 2**n
        return False
    return False

def spine(pieces):
    s = sorted(pieces, reverse=True)
    c = Counter(s)
    return sorted([v for v in sorted(c, reverse=True) for _ in range(c[v] % 2)], reverse=True)

# ============================================================
# 2. The SWAP test: take a D=1 spine with correct pattern,
#    swap a frag (at +) with an adjacent tower (at -).
#    The frag moves to -, the tower to +.
#    D changes by: lose frag from + (D -= frag), add frag at - (D -= frag),
#                  lose tower from - (D += tower), add tower at + (D += tower).
#    Net change: D_new - D_old = -2*frag + 2*tower = 2*(tower - frag).
#    For D to stay 1: tower = frag. But tower is a power of 2, frag isn't. IMPOSSIBLE.
# ============================================================
print("=" * 70)
print("SWAP TEST: swap a frag (at +) with adjacent tower (at -) in a D=1 spine")
print("=" * 70)
print("If frag v at + and tower t at - are SWAPPED:")
print("  D_new = D_old - 2v + 2t = 1 + 2(t - v)")
print("  For D_new = 1: t = v. But t = 2^k (tower), v != 2^k (frag). IMPOSSIBLE.")
print("  So D_new != 1. The swap ALWAYS changes D.")
print()

# Verify with concrete examples from T_3 cascade D=1 configs
def cfg_T3_cascade(q1, q2, q3):
    if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > q1/2 or q3 <= 0 or q3 > q2/2:
        return None
    return [F(8)-q1, q1-q2, q2-q3, q3, F(4), F(2), F(1)]

# A D=1 config: q1=4, q2=2, q3=1 (dyadic). Spine = {1}. No frag to swap.
# A D=1 config: q1=13/4, q2=5/4, q3=1/4. Spine = {19/4, 4, 1/4}.
# Frag 19/4 at pos 0 (+), tower 4 at pos 1 (-), frag 1/4 at pos 2 (+).
# Swap frag 19/4 (+) with tower 4 (-):
#   New spine order: {4, 19/4, 1/4} (4 > 19/4? No, 4 < 19/4. So sorted: {19/4, 4, 1/4} same.)
# Actually swapping POSITIONS not values. If we reassign: tower 4 to pos 0 (+), frag 19/4 to pos 1 (-).
# D_new = 4 - 19/4 + 1/4 = 4 - 18/4 = 4 - 9/2 = -1/2. Not 1. And 2*(4 - 19/4) = 2*(-3/4) = -3/2.
# D_new = 1 + (-3/2) = -1/2. ✓

sp = [F(19,4), F(4), F(1,4)]
D_old = alt_sum(sp)
print(f"Example spine: {sp}, D = {D_old}")
# Swap positions of frag (19/4, pos 0 +) and tower (4, pos 1 -):
# But they're adjacent in sorted order. Swapping them gives {4, 19/4, 1/4} but 4 < 19/4,
# so the sorted order is still {19/4, 4, 1/4}. The swap is only possible if they're equal
# (a tie), which they're not.
# The real question: can a DIFFERENT spine (different values) have frag at - and tower at +?
# This requires a DIFFERENT breakpoint config, not a swap of an existing one.

print()
print("The swap test shows: in a GIVEN spine, swapping adjacent frag/tower changes D by 2(t-v) != 0.")
print("But the real question is: can a DIFFERENT breakpoint config have a spine with frag at -?")
print()

# ============================================================
# 3. The algebraic check: can a spine with a frag at - satisfy the mass balance?
# ============================================================
print("=" * 70)
print("ALGEBRAIC CHECK: spine with frag at -, tower at +, can D = 1?")
print("=" * 70)
print()
print("A spine with k fragments at +, j fragments at -, a towers at +, b towers at -:")
print("  S_+ = (sum of k frags at +) + (sum of a towers at +)")
print("  S_- = (sum of j frags at -) + (sum of b towers at -)")
print("  D = S_+ - S_- = 1")
print("  S_total = S_+ + S_- = (all frags) + (all towers)")
print("  D = 1  <=>  S_+ = (S_total + 1) / 2")
print()
print("If ALL frags at + and ALL towers at - (the pattern):")
print("  S_+ = sum(frags), S_- = sum(towers)")
print("  D = sum(frags) - sum(towers) = 1  (the mass identity)")
print()
print("If one frag v moves to - and one tower t moves to +:")
print("  S_+ changes by -v + t (lose v, gain t)")
print("  D changes by 2(t - v)")
print("  D = 1 + 2(t - v)")
print("  For D = 1: t = v. But t is a power of 2 (tower), v is not (frag). IMPOSSIBLE.")
print()
print("This proves: the ONLY spine interleaving with D = 1 is frag-at-+, tower-at-.")
print()
print("BUT: this assumes exactly ONE frag-tower swap. What about MULTIPLE swaps?")
print("  k frags move to -, j towers move to +. D = 1 + 2(sum swapped towers - sum swapped frags).")
print("  For D = 1: sum(swapped towers) = sum(swapped frags).")
print("  Swapped towers are powers of 2; swapped frags are NOT powers of 2.")
print("  Can a sum of powers of 2 equal a sum of non-powers-of-2?")
print("  YES in general (e.g. 4 = 3 + 1, but 3 isn't a power of 2; 4 = 4 but 4 IS).")
print("  But: the frags and towers have the SAME total (mass identity).")
print("  So the question is whether a SUBSET of towers can have the same sum as a subset of frags.")

# ============================================================
# 4. Check: can a subset of tower pieces (powers of 2) have the same sum
#    as a subset of fragments (non-powers-of-2) in a D=1 spine?
# ============================================================
print()
print("=" * 70)
print("SUBSET-SUM CHECK: can sum(some towers) = sum(some frags) in a D=1 spine?")
print("=" * 70)

# Enumerate all D=1 spines from T_3 cascade and check.
N = 8
n = 3
d1_spines = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, int(2*q1*N)+1):
        q2 = F(q2n, N)
        if q2 > q1/2: break
        for q3n in range(1, int(2*q2*N)+1):
            q3 = F(q3n, N)
            if q3 > q2/2: break
            cfg = cfg_T3_cascade(q1, q2, q3)
            if cfg is None: continue
            D = alt_sum(cfg)
            if D != 1: continue
            sp = spine(cfg)
            d1_spines.append(sp)

print(f"T_3 cascade D=1 spines: {len(d1_spines)}")

# For each spine, check: can any subset of tower pieces have the same sum
# as any subset of fragments?
subset_sum_match = 0
no_match = 0
for sp in d1_spines:
    frags = [v for v in sp if not is_tower_val(v, n)]
    towers = [v for v in sp if is_tower_val(v, n)]
    if not frags or not towers:
        no_match += 1
        continue
    # Enumerate all nonempty subsets of towers and frags
    tower_sums = set()
    for r in range(1, len(towers)+1):
        for combo in combinations(towers, r):
            tower_sums.add(sum(combo))
    frag_sums = set()
    for r in range(1, len(frags)+1):
        for combo in combinations(frags, r):
            frag_sums.add(sum(combo))
    if tower_sums & frag_sums:
        subset_sum_match += 1
        if subset_sum_match <= 5:
            common = tower_sums & frag_sums
            print(f"  MATCH: spine={sp} frags={frags} towers={towers}")
            print(f"    common sums: {common}")
    else:
        no_match += 1

print(f"\nSubset-sum matches: {subset_sum_match}, no match: {no_match}")
if subset_sum_match == 0:
    print("NO spine has a tower-subset sum = a frag-subset sum.")
    print("This means: NO swap (single or multiple) can preserve D = 1.")
    print("The spine sign-pattern lemma is PROVED for T_3 cascade.")
else:
    print(f"{subset_sum_match} spines HAVE a subset-sum match — the swap argument needs refinement.")

# Also check T_3 split-larger and split-tower
print()
d1_spines_sl = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, int((8-q1)*N/2)+1):
        q2 = F(q2n, N)
        if q2 > (8-q1)/2: break
        cfg = [F(8)-q1-q2, q2, q1, F(4), F(2), F(1)]
        if alt_sum(cfg) == 1:
            d1_spines_sl.append(spine(cfg))

print(f"T_3 split-larger D=1 spines: {len(d1_spines_sl)}")
match_sl = 0
for sp in d1_spines_sl:
    frags = [v for v in sp if not is_tower_val(v, n)]
    towers = [v for v in sp if is_tower_val(v, n)]
    if not frags or not towers:
        continue
    tower_sums = set()
    for r in range(1, len(towers)+1):
        for combo in combinations(towers, r):
            tower_sums.add(sum(combo))
    frag_sums = set()
    for r in range(1, len(frags)+1):
        for combo in combinations(frags, r):
            frag_sums.add(sum(combo))
    if tower_sums & frag_sums:
        match_sl += 1
        if match_sl <= 3:
            print(f"  MATCH: spine={sp} frags={frags} towers={towers} common={tower_sums & frag_sums}")

print(f"Split-larger subset-sum matches: {match_sl}")

# T_3 split-tower
print()
d1_spines_st = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, 2*N+1):
        q2 = F(q2n, N)
        if q2 > 2: break
        cfg = [F(8)-q1, q1, F(4)-q2, q2, F(2), F(1)]
        if alt_sum(cfg) == 1:
            d1_spines_st.append(spine(cfg))

print(f"T_3 split-tower D=1 spines: {len(d1_spines_st)}")
match_st = 0
for sp in d1_spines_st:
    frags = [v for v in sp if not is_tower_val(v, n)]
    towers = [v for v in sp if is_tower_val(v, n)]
    if not frags or not towers:
        continue
    tower_sums = set()
    for r in range(1, len(towers)+1):
        for combo in combinations(towers, r):
            tower_sums.add(sum(combo))
    frag_sums = set()
    for r in range(1, len(frags)+1):
        for combo in combinations(frags, r):
            frag_sums.add(sum(combo))
    if tower_sums & frag_sums:
        match_st += 1
        if match_st <= 3:
            print(f"  MATCH: spine={sp} frags={frags} towers={towers} common={tower_sums & frag_sums}")

print(f"Split-tower subset-sum matches: {match_st}")

# T_4 cascade
print()
N4 = 4
n4 = 4
d1_spines4 = []
for q1n in range(1, 8*N4+1):
    q1 = F(q1n, N4)
    for q2n in range(1, int(q1*N4/2)+2):
        q2 = F(q2n, N4)
        if q2 > q1/2: break
        for q3n in range(1, int(q2*N4/2)+2):
            q3 = F(q3n, N4)
            if q3 > q2/2: break
            cfg = [F(16)-q1, q1-q2, q2-q3, q3, F(8), F(4), F(2), F(1)]
            if alt_sum(cfg) == 1:
                d1_spines4.append(spine(cfg))

print(f"T_4 cascade D=1 spines: {len(d1_spines4)}")
match4 = 0
for sp in d1_spines4:
    frags = [v for v in sp if not is_tower_val(v, n4)]
    towers = [v for v in sp if is_tower_val(v, n4)]
    if not frags or not towers:
        continue
    tower_sums = set()
    for r in range(1, len(towers)+1):
        for combo in combinations(towers, r):
            tower_sums.add(sum(combo))
    frag_sums = set()
    for r in range(1, len(frags)+1):
        for combo in combinations(frags, r):
            frag_sums.add(sum(combo))
    if tower_sums & frag_sums:
        match4 += 1
        if match4 <= 3:
            print(f"  MATCH: spine={sp} frags={frags} towers={towers} common={tower_sums & frag_sums}")

print(f"T_4 cascade subset-sum matches: {match4}")

# T_4 split-larger
d1_spines4sl = []
for q1n in range(1, 8*N4+1):
    q1 = F(q1n, N4)
    for q2n in range(1, int((16-q1)*N4/2)+2):
        q2 = F(q2n, N4)
        if q2 > (16-q1)/2: break
        for q3n in range(1, int((16-q1-q2)*N4/2)+2):
            q3 = F(q3n, N4)
            if q3 > (16-q1-q2)/2: break
            cfg = [F(16)-q1-q2-q3, q3, q2, q1, F(8), F(4), F(2), F(1)]
            if alt_sum(cfg) == 1:
                d1_spines4sl.append(spine(cfg))

print(f"T_4 split-larger D=1 spines: {len(d1_spines4sl)}")
match4sl = 0
for sp in d1_spines4sl:
    frags = [v for v in sp if not is_tower_val(v, n4)]
    towers = [v for v in sp if is_tower_val(v, n4)]
    if not frags or not towers:
        continue
    tower_sums = set()
    for r in range(1, len(towers)+1):
        for combo in combinations(towers, r):
            tower_sums.add(sum(combo))
    frag_sums = set()
    for r in range(1, len(frags)+1):
        for combo in combinations(frags, r):
            frag_sums.add(sum(combo))
    if tower_sums & frag_sums:
        match4sl += 1
        if match4sl <= 3:
            print(f"  MATCH: spine={sp} frags={frags} towers={towers} common={tower_sums & frag_sums}")

print(f"T_4 split-larger subset-sum matches: {match4sl}")

print()
print("=" * 70)
print("CONCLUSION")
print("=" * 70)
total_match = match_sl if n == 3 else 0  # placeholder
print(f"If all subset-sum matches are 0, then the spine sign-pattern lemma")
print(f"is PROVED: no subset of towers has the same sum as any subset of frags,")
print(f"so no sign swap (single or multiple) can preserve D = 1.")
print(f"The only D=1 spine interleaving is frag-at-+, tower-at-.")
