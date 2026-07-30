"""
Round 6, Mission A: CORRECTED sub-gap (i) check.

The round-5 spine_face_analysis.py "generalized pattern" check used
  dyadic (power of 2) vs non-dyadic
to classify spine pieces. But a FRAGMENT of the top piece can happen to be a
power of 2 (e.g. value 4, 2, 1, or 1/2, 1/4, ...). Such a fragment is
misclassified as a "tower piece" (dyadic), making the pattern check report
false failures.

The CORRECT check for the all-frag-+/all-tower- pattern (GAP-B(d)) classifies
by ORIGIN: is the piece a fragment of the top piece 2^n, or a piece derived
from a tower piece below 2^n (split or unsplit)?

This script:
  1. For each D=1 breakpoint config, tracks the origin of each piece.
  2. Computes the spine (after pair cancellation), tracking origins.
  3. Checks: in the spine, are ALL fragments at + positions and ALL tower
     pieces at - positions? (the all-frag-+/all-tower- pattern)
  4. If YES for all D=1 configs => sub-gap (i) VERIFIED (not proved).
  5. If any NO => counterexample to sub-gap (i).

We also check: is the block condition satisfied on the spine? (each split's
fragments at same sign). For cascade types, there's only one split (the top),
so the block condition = all fragments at same sign.
"""
from fractions import Fraction as F
from collections import Counter, defaultdict

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

def is_pow2(x):
    if x <= 0: return False
    if isinstance(x, F):
        if x.denominator == 1:
            n = int(x); return n > 0 and (n & (n-1)) == 0
        num, den = x.numerator, x.denominator
        return (num & (num-1)) == 0 and (den & (den-1)) == 0
    import math
    lg = math.log2(x) if x > 0 else -1
    return abs(lg - round(lg)) < 1e-9 and round(lg) >= -20

def tower(n):
    return [F(2)**(n-k) for k in range(n+1)]

def spine_with_origins(pieces, origins):
    """
    pieces: list of values.
    origins: list of same length, 'F' (fragment) or 'T' (tower).
    Returns spine as list of (value, origin), after pair cancellation.
    Pair cancellation: remove pairs of equal values (any origins).
    A piece survives if its value has odd count.
    For surviving pieces, origin = the origin of the surviving copy.
    (If multiple copies survive with different origins, pick the first.)
    """
    # Count by value
    val_count = Counter(pieces)
    # Build spine: for each value with odd count, keep one copy
    # We need to track origins. For each value, collect origins.
    val_origins = defaultdict(list)
    for v, o in zip(pieces, origins):
        val_origins[v].append(o)

    sp = []
    for v in sorted(val_origins.keys(), reverse=True):
        cnt = val_count[v]
        if cnt % 2 == 1:
            # One copy survives. Which origin?
            # If there are both F and T origins, the surviving one matters.
            # Actually, at a breakpoint with proper pairing, same-value pieces
            # pair off. The survivor's origin is the "odd one out."
            # Let's pick: if any F, pick F; else pick T. (Conservative.)
            origins_list = val_origins[v]
            # Count F vs T
            nF = origins_list.count('F')
            nT = origins_list.count('T')
            # The survivor: if nF is odd, it's F; if nT is odd, it's T.
            # (Since total is odd, exactly one of nF, nT is odd.)
            if nF % 2 == 1:
                sp.append((v, 'F'))
            else:
                sp.append((v, 'T'))
    return sp

def check_pattern_on_spine(sp):
    """
    sp: list of (value, origin), sorted descending.
    Check: all F at + positions (even 0-based), all T at - positions (odd).
    Returns (pattern_holds, block_condition_holds, details).
    """
    n = len(sp)
    frag_positions = [i for i, (v, o) in enumerate(sp) if o == 'F']
    tower_positions = [i for i, (v, o) in enumerate(sp) if o == 'T']

    all_frag_plus = all(i % 2 == 0 for i in frag_positions)
    all_tower_minus = all(i % 2 == 1 for i in tower_positions)

    pattern = all_frag_plus and all_tower_minus
    block = all_frag_plus  # for single-split (cascade), block = all frags same sign

    return pattern, block, (frag_positions, tower_positions)

def classify_all_d1(n, cfg_fn, param_ranges, label, origin_fn):
    """
    cfg_fn(params) -> (frags, towers) or None.
    origin_fn(params, frags, towers) -> list of origins for all_pieces
      (must align with frags + towers order).
    """
    d1_count = 0
    pattern_ok = 0
    pattern_fail = 0
    block_ok = 0
    block_fail = 0
    fail_examples = []

    for params in param_ranges:
        result = cfg_fn(params)
        if result is None:
            continue
        frags, towers = result
        all_pieces = list(frags) + list(towers)
        D = alt_sum(all_pieces)
        if D != 1:
            continue
        d1_count += 1

        origins = ['F'] * len(frags) + ['T'] * len(towers)
        sp = spine_with_origins(all_pieces, origins)

        pattern, block, details = check_pattern_on_spine(sp)

        if pattern:
            pattern_ok += 1
        else:
            pattern_fail += 1
            if len(fail_examples) < 10:
                fail_examples.append((params, all_pieces, sp, pattern, block, details))

        if block:
            block_ok += 1
        else:
            block_fail += 1

    print(f"  {label} (T_{n}): D=1 = {d1_count}, "
          f"pattern (all-F-+/all-T--) OK = {pattern_ok}, FAIL = {pattern_fail}, "
          f"block cond OK = {block_ok}, FAIL = {block_fail}")
    if fail_examples:
        print(f"  PATTERN FAIL examples:")
        for params, cfg, sp, pat, blk, det in fail_examples[:5]:
            sp_str = [(str(v), o) for v, o in sp]
            print(f"    params={params} spine={sp_str} pattern={pat} block={blk} det={det}")
    return d1_count, pattern_fail, block_fail

# ============================================================
# T_3 cascade: 8 -> (8-q1)+q1 -> (q1-q2)+q2 -> (q2-q3)+q3
# frags = [8-q1, q1-q2, q2-q3, q3], towers = [4, 2, 1]
# ============================================================
def cfg_T3_cascade(q1, q2, q3):
    if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > q1/2 or q3 <= 0 or q3 > q2/2:
        return None
    frags = [F(8)-q1, q1-q2, q2-q3, q3]
    towers = [F(4), F(2), F(1)]
    return (frags, towers)

N = 8
params_cascade = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, int(2*q1*N)+1):
        q2 = F(q2n, N)
        if q2 > q1/2: break
        for q3n in range(1, int(2*q2*N)+1):
            q3 = F(q3n, N)
            if q3 > q2/2: break
            params_cascade.append((q1, q2, q3))

print("=" * 70)
print("Mission A: CORRECTED sub-gap (i) check (origin-based classification)")
print("=" * 70)
print("\nT_3 cascade:")
classify_all_d1(3, lambda p: cfg_T3_cascade(*p), params_cascade, "cascade", None)

# T_3 split-larger: 8 -> (8-q1)+q1, split (8-q1) -> (8-q1-q2)+q2
def cfg_T3_split_larger(q1, q2):
    if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > (8-q1)/2:
        return None
    frags = [F(8)-q1-q2, q2, q1]
    towers = [F(4), F(2), F(1)]
    return (frags, towers)

params_sl = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, int((8-q1)*N/2)+1):
        q2 = F(q2n, N)
        if q2 > (8-q1)/2: break
        params_sl.append((q1, q2))

print("\nT_3 split-larger:")
classify_all_d1(3, lambda p: cfg_T3_split_larger(*p), params_sl, "split-larger", None)

# T_3 split-tower: 8 -> (8-q1)+q1, tower 4 -> (4-q2)+q2
# Here frags = top frags + tower-4 frags. towers = [2, 1]
# Origin: top frags = F, tower-4 frags = T (derived from tower), unsplit = T
def cfg_T3_split_tower(q1, q2):
    if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > 2:
        return None
    frags_top = [F(8)-q1, q1]
    frags_t4 = [F(4)-q2, q2]
    towers = [F(2), F(1)]
    # all "frags" in the return = frags_top + frags_t4
    # but origins: frags_top = F, frags_t4 = T, towers = T
    # We need to handle this differently.
    return (frags_top + frags_t4, towers)

# For split-tower, origins are mixed. Let's handle separately.
print("\nT_3 split-tower (origins: top-frag=F, tower-4-frag=T, unsplit=T):")
d1_st = 0; pat_ok_st = 0; pat_fail_st = 0; blk_ok_st = 0; blk_fail_st = 0
st_fail_examples = []
params_st = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, 2*N+1):
        q2 = F(q2n, N)
        if q2 > 2: break
        params_st.append((q1, q2))

for params in params_st:
    q1, q2 = params
    frags_top = [F(8)-q1, q1]
    frags_t4 = [F(4)-q2, q2]
    towers = [F(2), F(1)]
    all_pieces = frags_top + frags_t4 + towers
    origins = ['F', 'F', 'T', 'T', 'T', 'T']
    D = alt_sum(all_pieces)
    if D != 1:
        continue
    d1_st += 1
    sp = spine_with_origins(all_pieces, origins)
    pattern, block, details = check_pattern_on_spine(sp)
    if pattern: pat_ok_st += 1
    else:
        pat_fail_st += 1
        if len(st_fail_examples) < 5:
            st_fail_examples.append((params, all_pieces, sp, pattern, block, details))
    if block: blk_ok_st += 1
    else: blk_fail_st += 1

print(f"  split-tower (T_3): D=1 = {d1_st}, pattern OK = {pat_ok_st}, FAIL = {pat_fail_st}, "
      f"block OK = {blk_ok_st}, FAIL = {blk_fail_st}")
if st_fail_examples:
    print("  FAIL examples:")
    for params, cfg, sp, pat, blk, det in st_fail_examples:
        print(f"    params={params} spine={[(str(v),o) for v,o in sp]} pattern={pat} block={blk}")

# ============================================================
# T_4 cascade
# ============================================================
def cfg_T4_cascade(q1, q2, q3):
    if q1 <= 0 or q1 > 8 or q2 <= 0 or q2 > q1/2 or q3 <= 0 or q3 > q2/2:
        return None
    frags = [F(16)-q1, q1-q2, q2-q3, q3]
    towers = [F(8), F(4), F(2), F(1)]
    return (frags, towers)

N4 = 4
params_cascade4 = []
for q1n in range(1, 8*N4+1):
    q1 = F(q1n, N4)
    for q2n in range(1, int(q1*N4/2)+2):
        q2 = F(q2n, N4)
        if q2 > q1/2: break
        for q3n in range(1, int(q2*N4/2)+2):
            q3 = F(q3n, N4)
            if q3 > q2/2: break
            params_cascade4.append((q1, q2, q3))

print("\nT_4 cascade:")
classify_all_d1(4, lambda p: cfg_T4_cascade(*p), params_cascade4, "cascade", None)

# T_4 split-larger (3-step cascade on larger fragment)
def cfg_T4_split_larger(q1, q2, q3):
    if q1 <= 0 or q1 > 8 or q2 <= 0 or q2 > (16-q1)/2 or q3 <= 0 or q3 > (16-q1-q2)/2:
        return None
    frags = [F(16)-q1-q2-q3, q3, q2, q1]
    towers = [F(8), F(4), F(2), F(1)]
    return (frags, towers)

params_sl4 = []
for q1n in range(1, 8*N4+1):
    q1 = F(q1n, N4)
    for q2n in range(1, int((16-q1)*N4/2)+2):
        q2 = F(q2n, N4)
        if q2 > (16-q1)/2: break
        for q3n in range(1, int((16-q1-q2)*N4/2)+2):
            q3 = F(q3n, N4)
            if q3 > (16-q1-q2)/2: break
            params_sl4.append((q1, q2, q3))

print("\nT_4 split-larger:")
classify_all_d1(4, lambda p: cfg_T4_split_larger(*p), params_sl4, "split-larger", None)

# T_4 split-tower: 16->(16-q1)+q1, 8->(8-q2)+q2, 4->(4-q3)+q3
print("\nT_4 split-tower2 (origins: top-frag=F, rest=T):")
d1_st4 = 0; pat_ok4 = 0; pat_fail4 = 0; blk_ok4 = 0; blk_fail4 = 0
params_st4 = []
for q1n in range(1, 8*N4+1):
    q1 = F(q1n, N4)
    for q2n in range(1, 4*N4+1):
        q2 = F(q2n, N4)
        if q2 > 4: break
        for q3n in range(1, 2*N4+1):
            q3 = F(q3n, N4)
            if q3 > 2: break
            params_st4.append((q1, q2, q3))

for params in params_st4:
    q1, q2, q3 = params
    frags_top = [F(16)-q1, q1]
    frags_t8 = [F(8)-q2, q2]
    frags_t4 = [F(4)-q3, q3]
    towers = [F(2), F(1)]
    all_pieces = frags_top + frags_t8 + frags_t4 + towers
    origins = ['F', 'F', 'T', 'T', 'T', 'T', 'T', 'T']
    D = alt_sum(all_pieces)
    if D != 1:
        continue
    d1_st4 += 1
    sp = spine_with_origins(all_pieces, origins)
    pattern, block, details = check_pattern_on_spine(sp)
    if pattern: pat_ok4 += 1
    else: pat_fail4 += 1
    if block: blk_ok4 += 1
    else: blk_fail4 += 1

print(f"  split-tower2 (T_4): D=1 = {d1_st4}, pattern OK = {pat_ok4}, FAIL = {pat_fail4}, "
      f"block OK = {blk_ok4}, FAIL = {blk_fail4}")

# ============================================================
# T_5 cascade (coarse)
# ============================================================
def cfg_T5_cascade(q1, q2, q3, q4):
    if q1 <= 0 or q1 > 16 or q2 <= 0 or q2 > q1/2 or q3 <= 0 or q3 > q2/2 or q4 <= 0 or q4 > q3/2:
        return None
    frags = [F(32)-q1, q1-q2, q2-q3, q3-q4, q4]
    towers = [F(16), F(8), F(4), F(2), F(1)]
    return (frags, towers)

N5 = 2
params_cascade5 = []
for q1n in range(1, 16*N5+1):
    q1 = F(q1n, N5)
    for q2n in range(1, int(q1*N5/2)+2):
        q2 = F(q2n, N5)
        if q2 > q1/2: break
        for q3n in range(1, int(q2*N5/2)+2):
            q3 = F(q3n, N5)
            if q3 > q2/2: break
            for q4n in range(1, int(q3*N5/2)+2):
                q4 = F(q4n, N5)
                if q4 > q3/2: break
                params_cascade5.append((q1, q2, q3, q4))

print("\nT_5 cascade:")
classify_all_d1(5, lambda p: cfg_T5_cascade(*p), params_cascade5, "cascade", None)

print("\n" + "=" * 70)
print("SUMMARY: If pattern_fail = 0 and block_fail = 0 for all types,")
print("then sub-gap (i) is VERIFIED (origin-based): every D=1 breakpoint")
print("spine has the all-frag-+/all-tower- pattern (block condition holds).")
print("=" * 70)
