"""
Round 5: Deeper analysis of the split-tower case and the GENERALIZED
mass-balance / block condition at the SPINE level.

KEY FINDING from mass_balance_enum.py:
  - Mass balance S_+ = 2^n holds for ALL D=1 configs (0 failures).
  - But the all-top-+/all-below-- SIGN PATTERN fails for split-tower D=1 configs.
  - Reason: split-tower has 2 top-frags + 4 below-tower pieces = 6 total,
    but only 3 + positions and 3 - positions. Need 4 below-tower at - (impossible: 4 > 3).

  So the all-top-+/all-below-- pattern is about the FULL config on a full-dimensional
  block-condition CELL. At a breakpoint (FACE), tied pairs cancel, and the effective
  structure is the SPINE.

  The split-tower D=1 face works because:
  - Top frags {4,4} are TIED -> cancel (contribute 0).
  - Spine = {4-q2, 2, q2, 1} with tower-4 frags {4-q2, q2} at +, unsplit {2,1} at -.
  - This is the GENERALIZED all-top-+/all-below-- at level k=2:
    largest split piece (4=2^2) frags at +, all below (2+1=3=2^2-1) at -.
    D = 4 - 3 = 1.

  The mass-balance argument works at ANY level k, not just k=n:
  D = 2^k - (2^k - 1) = 1 when piece 2^k is split (frags at +) and all below at -.

This script:
  1. Verifies the generalized mass-balance at the spine level.
  2. Checks whether EVERY D=1 breakpoint has a spine satisfying the generalized pattern.
  3. Enumerates D=1 breakpoints of T_4, T_5 and classifies by spine structure.
"""
from fractions import Fraction as F
from collections import Counter, defaultdict
import sys

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

def spine(pieces):
    s = sorted(pieces, reverse=True)
    c = Counter(s)
    return sorted([v for v in sorted(c, reverse=True) for _ in range(c[v] % 2)], reverse=True)

def tower(n):
    return [F(2)**(n-k) for k in range(n+1)]

# ============================================================
# 1. For every D=1 config, compute the spine and check:
#    (a) Is the spine dyadic? (all powers of 2)
#    (b) Does the spine satisfy the generalized all-top-+/all-below-- pattern?
#        i.e., the largest split-piece's fragments at +, all below at -.
#    (c) What is the spine's structure?
# ============================================================

def classify_spine(pieces, split_info):
    """
    pieces: full config (list of values).
    split_info: list of lists. Each sublist = indices (into pieces) of fragments
                of one split piece. The first sublist = top split fragments.

    Returns: (spine_pieces, is_dyadic_spine, has_generalized_pattern, pattern_level)
    """
    sp = spine(pieces)
    is_dyad = all(is_pow2(v) for v in sp)

    # For the generalized pattern: find the largest split piece whose fragments
    # survive in the spine. Check if all its fragments are at + and all smaller
    # pieces are at -.
    # This requires knowing which spine pieces belong to which split.
    # For simplicity, just report the spine structure.
    return (sp, is_dyad, None, None)

def generalized_pattern_check(sp, split_spine_groups):
    """
    sp: spine (sorted descending list of values).
    split_spine_groups: list of lists. Each sublist = indices (into sp) of
                         fragments of one split piece that survive in the spine.

    Check: does there exist a level k such that the largest split piece 2^k
    has all its spine-fragments at + positions, and all pieces below it at -?

    More generally: for each split group, check if its fragments are at same-sign
    positions in the spine. Then check the mass balance.
    """
    n = len(sp)
    # Check block condition on spine: each split group's fragments at same sign.
    # Since spine is strict (no ties), positions are 0,1,2,...,n-1.
    # Sign = + for even positions, - for odd.
    block_ok = True
    for group in split_spine_groups:
        signs = set(i % 2 for i in group)  # 0=+, 1=-
        if len(signs) > 1:
            block_ok = False
            break

    if not block_ok:
        return (False, False, "block fails on spine")

    # Block condition holds on spine. Check mass balance.
    # D = S_+ - S_- where S_+ = sum of pieces at + positions.
    S_plus = sum(sp[i] for i in range(0, n, 2))
    S_minus = sum(sp[i] for i in range(1, n, 2))
    S_total = S_plus + S_minus
    D = S_plus - S_minus

    # Check: is D = 1? (it should be, since we started with D=1 config)
    # The generalized pattern: the largest split piece's fragments at +,
    # all unsplit at -.
    # If block holds, each split group is at + or -. The mass balance determines D.

    return (True, D == 1, f"block OK, S+={S_plus}, S-={S_minus}, D={D}")

# ============================================================
# 2. Enumerate D=1 configs for various types and classify spines
# ============================================================

def enumerate_and_classify(n, cfg_fn, param_ranges, label, split_info_fn):
    """
    For each D=1 config, compute spine and classify.
    split_info_fn(params, all_pieces) -> list of lists of indices (split groups).
    """
    tow = tower(n)
    D_n = sum(tow)

    d1_count = 0
    spine_dyadic = 0
    spine_block_ok = 0
    spine_block_fail = 0
    spine_d1 = 0
    examples = []

    for params in param_ranges:
        result = cfg_fn(params)
        if result is None:
            continue
        if isinstance(result, tuple) and len(result) == 2:
            frags, towers = result
            all_pieces = list(frags) + list(towers)
        else:
            all_pieces = list(result)

        D = alt_sum(all_pieces)
        if D != 1:
            continue
        d1_count += 1

        sp = spine(all_pieces)
        is_dyad_sp = all(is_pow2(v) for v in sp)
        if is_dyad_sp:
            spine_dyadic += 1

        # Get split groups in terms of all_pieces indices
        split_groups = split_info_fn(params, all_pieces)
        # Map to spine indices: find which spine pieces correspond to which split group.
        # This is tricky because spine removes pairs. Let's just check the block condition
        # on the spine directly.

        # For each split group, find which of its pieces survive in the spine.
        # A piece survives if its value has odd count in the full config.
        # Actually, spine = pieces with odd count (one copy each).
        # Let's just check: in the spine, are the surviving split fragments
        # at same-sign positions?

        # Build a mapping: for each spine piece (by value), which split group does it belong to?
        # This requires tracking origins, which is complex. For now, just report spine structure.
        sp_D = alt_sum(sp)
        if sp_D == 1:
            spine_d1 += 1
        else:
            print(f"  SPINE D != 1: {label} params={params} cfg={all_pieces} spine={sp} D(sp)={sp_D}")

        if d1_count <= 5:
            examples.append({
                'params': params,
                'cfg': [round(float(x),3) for x in all_pieces],
                'spine': sp,
                'D_spine': sp_D,
                'spine_dyadic': is_dyad_sp,
            })

    print(f"  {label} (T_{n}): D=1 = {d1_count}, spine dyadic = {spine_dyadic}, "
          f"spine D=1 = {spine_d1}")
    for ex in examples:
        print(f"    cfg={ex['cfg']} spine={ex['spine']} D(sp)={float(ex['D_spine'])} dyad={ex['spine_dyadic']}")

    return d1_count, spine_dyadic

# T_3 cascade
def cfg_T3_cascade(q1, q2, q3):
    if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > q1/2 or q3 <= 0 or q3 > q2/2:
        return None
    frags = [F(8)-q1, q1-q2, q2-q3, q3]
    towers = [F(4), F(2), F(1)]
    return (frags, towers)

def split_info_cascade(params, all_pieces):
    # One split group: all fragments of the top piece (indices 0-3)
    return [list(range(4))]

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
print("1. T_3 cascade: spine classification")
print("=" * 70)
enumerate_and_classify(3, lambda p: cfg_T3_cascade(*p), params_cascade, "cascade",
                        split_info_cascade)

# T_3 split-larger
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

print("\n" + "=" * 70)
print("2. T_3 split-larger: spine classification")
print("=" * 70)
enumerate_and_classify(3, lambda p: cfg_T3_split_larger(*p), params_sl, "split-larger",
                        split_info_cascade)

# T_3 split-tower: 8 -> (8-q1)+q1, tower 4 -> (4-q2)+q2
def cfg_T3_split_tower(q1, q2):
    if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > 2:
        return None
    frags_top = [F(8)-q1, q1]
    frags_t4 = [F(4)-q2, q2]
    towers = [F(2), F(1)]
    return (frags_top + frags_t4, towers)

params_st = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, 2*N+1):
        q2 = F(q2n, N)
        if q2 > 2: break
        params_st.append((q1, q2))

print("\n" + "=" * 70)
print("3. T_3 split-tower: spine classification")
print("=" * 70)
enumerate_and_classify(3, lambda p: cfg_T3_split_tower(*p), params_st, "split-tower",
                        split_info_cascade)

# ============================================================
# 4. The KEY check: for every D=1 breakpoint, does the face contain
#    a dyadic endpoint?
# ============================================================
print("\n" + "=" * 70)
print("4. Does every D=1 face contain a dyadic endpoint?")
print("=" * 70)

def check_dyadic_in_face(n, cfg_fn, param_ranges, label, dyadic_params):
    """
    For each D=1 config, check if the config is on a face that contains a dyadic config.
    A face = set of configs with the same sort order (including ties).
    A dyadic config = all pieces are powers of 2.

    We check: is the config itself dyadic, OR is there a dyadic config
    reachable by moving along the same face (same ties)?
    """
    d1_count = 0
    d1_dyadic = 0
    d1_nondyadic = 0
    d1_nondyadic_face_has_dyadic = 0
    d1_nondyadic_face_no_dyadic = 0
    no_dyad_examples = []

    for params in param_ranges:
        result = cfg_fn(params)
        if result is None: continue
        if isinstance(result, tuple) and len(result) == 2:
            frags, towers = result
            all_pieces = list(frags) + list(towers)
        else:
            all_pieces = list(result)

        D = alt_sum(all_pieces)
        if D != 1: continue
        d1_count += 1

        is_dyad = all(is_pow2(v) for v in all_pieces)
        if is_dyad:
            d1_dyadic += 1
        else:
            d1_nondyadic += 1
            # Check: is there a dyadic config in the same face?
            # The face is defined by which pieces are tied. At a breakpoint,
            # some pieces tie. The face = set of configs with the same tie pattern.
            # For a grid check: is there a dyadic config with the same combinatorial type?
            # Simplified: check if any dyadic_params config has D=1 and shares the same
            # sort-order pattern (same group structure).

            # For now, just check: is there ANY dyadic config with D=1 in this type?
            # (This is a necessary condition, not sufficient.)
            # We'll check more carefully below.
            pass

    # Check: does the type have ANY dyadic D=1 config?
    has_any_dyadic_d1 = False
    for dp in dyadic_params:
        result = cfg_fn(dp)
        if result is None: continue
        if isinstance(result, tuple) and len(result) == 2:
            frags, towers = result
            all_pieces = list(frags) + list(towers)
        else:
            all_pieces = list(result)
        if all(is_pow2(v) for v in all_pieces) and alt_sum(all_pieces) == 1:
            has_any_dyadic_d1 = True
            break

    print(f"  {label} (T_{n}): D=1 = {d1_count}, dyadic = {d1_dyadic}, "
          f"non-dyadic = {d1_nondyadic}, type has dyadic D=1 = {has_any_dyadic_d1}")

# T_3 cascade: dyadic params (q1=4, q2=2, q3=1)
dyadic_cascade = [(F(4), F(2), F(1))]
check_dyadic_in_face(3, lambda p: cfg_T3_cascade(*p), params_cascade, "cascade", dyadic_cascade)

# T_3 split-larger: dyadic params (q1=4, q2=0) or (q1=2, q2=2) etc.
dyadic_sl = []
for q1 in [F(1), F(2), F(4)]:
    for q2 in [F(1), F(2)]:
        if q2 <= (8-q1)/2:
            dyadic_sl.append((q1, q2))
check_dyadic_in_face(3, lambda p: cfg_T3_split_larger(*p), params_sl, "split-larger", dyadic_sl)

# T_3 split-tower: dyadic params
dyadic_st = []
for q1 in [F(1), F(2), F(4)]:
    for q2 in [F(1), F(2)]:
        if q2 <= 2:
            dyadic_st.append((q1, q2))
check_dyadic_in_face(3, lambda p: cfg_T3_split_tower(*p), params_st, "split-tower", dyadic_st)

# ============================================================
# 5. For the split-tower type: trace D along faces to dyadic endpoints
# ============================================================
print("\n" + "=" * 70)
print("5. Split-tower: trace D=1 face connectivity to dyadic")
print("=" * 70)

# The split-tower face q1=4: config {4, 4, 4-q2, q2, 2, 1}
# D = 4 - 4 + (4-q2) - 2 + q2 - 1 = 1 for q2 in [1, 2] (when 4-q2 > 2 > q2 > 1)
# The dyadic endpoint is q2=2: {4, 4, 2, 2, 2, 1}, D=1.
print("  Face q1=4 (top balanced 8->4+4):")
for q2 in [F(1), F(5,4), F(3,2), F(7,4), F(2)]:
    cfg = cfg_T3_split_tower(F(4), q2)
    if cfg is None: continue
    all_p = list(cfg[0]) + list(cfg[1])
    D = alt_sum(all_p)
    sp = spine(all_p)
    print(f"    q2={q2} cfg={all_p} D={D} spine={sp} D(sp)={alt_sum(sp)} dyad={all(is_pow2(v) for v in all_p)}")

# Face q2=2 (tower-4 balanced): config {8-q1, q1, 2, 2, 2, 1}
print("\n  Face q2=2 (tower-4 balanced 4->2+2):")
for q1 in [F(1), F(3,2), F(2), F(3), F(4)]:
    cfg = cfg_T3_split_tower(q1, F(2))
    if cfg is None: continue
    all_p = list(cfg[0]) + list(cfg[1])
    D = alt_sum(all_p)
    sp = spine(all_p)
    print(f"    q1={q1} cfg={all_p} D={D} spine={sp} D(sp)={alt_sum(sp)} dyad={all(is_pow2(v) for v in all_p)}")

# ============================================================
# 6. The GENERALIZED mass-balance at spine level
# ============================================================
print("\n" + "=" * 70)
print("6. Generalized mass-balance at spine level")
print("=" * 70)
print("""
  At a breakpoint, tied pairs cancel. The spine = pieces with odd count.
  D(config) = D(spine) (by spine-pair-cancellation S1).

  On the spine, the block condition: each split's surviving fragments at same sign.
  If block holds, D(spine) = S_+ - S_- where S_+ = mass at + positions.

  The GENERALIZED GAP-B(d): if the spine's largest split piece V has all its
  fragments at +, and all pieces below V are at -, then
    D(spine) = V - (total below V) = V - (V - 1) = 1.
  (This uses: the pieces below V in the spine are {2^{k-1}, ..., 2, 1} for some k,
   summing to V - 1. This holds because the tower structure is preserved in the spine.)

  The mass-balance argument GENERALIZES: D(spine) = 1 on a block-condition spine
  iff the largest split piece is at + and all below at -.

  VERIFICATION: check that every D=1 breakpoint has a spine satisfying this.
""")

# Check all D=1 configs: does the spine satisfy the generalized pattern?
def check_generalized_pattern(n, cfg_fn, param_ranges, label):
    """
    For each D=1 config, compute spine and check:
    - Is the spine dyadic?
    - Does the spine satisfy the block condition + generalized pattern?
    """
    d1_count = 0
    sp_dyadic = 0
    sp_block_pattern = 0
    sp_block_fail = 0
    sp_block_ok_not_pattern = 0
    fail_examples = []

    for params in param_ranges:
        result = cfg_fn(params)
        if result is None: continue
        if isinstance(result, tuple) and len(result) == 2:
            frags, towers = result
            all_pieces = list(frags) + list(towers)
        else:
            all_pieces = list(result)

        D = alt_sum(all_pieces)
        if D != 1: continue
        d1_count += 1

        sp = spine(all_pieces)
        if all(is_pow2(v) for v in sp):
            sp_dyadic += 1
            continue

        # Check: in the spine, are all non-dyadic pieces at + positions?
        # (The generalized pattern: non-dyadic spine pieces at +, dyadic at -.)
        # Non-dyadic pieces in the spine are the surviving fragments.
        # Dyadic pieces are unsplit tower pieces.
        nd_positions = [i for i, v in enumerate(sp) if not is_pow2(v)]
        dy_positions = [i for i, v in enumerate(sp) if is_pow2(v)]

        # Check: all non-dyadic at even positions (+)?
        all_nd_plus = all(i % 2 == 0 for i in nd_positions)
        # Check: all dyadic at odd positions (-)?
        all_dy_minus = all(i % 2 == 1 for i in dy_positions)

        if all_nd_plus and all_dy_minus:
            sp_block_pattern += 1
        elif all_nd_plus and not all_dy_minus:
            sp_block_ok_not_pattern += 1
            if len(fail_examples) < 5:
                fail_examples.append((params, sp, nd_positions, dy_positions))
        else:
            sp_block_fail += 1
            if len(fail_examples) < 10:
                fail_examples.append((params, sp, nd_positions, dy_positions))

    print(f"  {label} (T_{n}): D=1 = {d1_count}, spine dyadic = {sp_dyadic}, "
          f"generalized pattern (nd at +, dy at -) = {sp_block_pattern}, "
          f"nd at + but dy not all at - = {sp_block_ok_not_pattern}, "
          f"nd at - (block fail) = {sp_block_fail}")
    if fail_examples:
        print(f"  Non-matching examples:")
        for params, sp, nd_pos, dy_pos in fail_examples[:5]:
            print(f"    params={params} spine={sp} nd_pos={nd_pos} dy_pos={dy_pos}")

    return d1_count, sp_dyadic, sp_block_pattern, sp_block_fail

print("\n  T_3 cascade:")
check_generalized_pattern(3, lambda p: cfg_T3_cascade(*p), params_cascade, "cascade")
print("\n  T_3 split-larger:")
check_generalized_pattern(3, lambda p: cfg_T3_split_larger(*p), params_sl, "split-larger")
print("\n  T_3 split-tower:")
check_generalized_pattern(3, lambda p: cfg_T3_split_tower(*p), params_st, "split-tower")

# T_4 cascade
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

print("\n  T_4 cascade:")
check_generalized_pattern(4, lambda p: cfg_T4_cascade(*p), params_cascade4, "cascade")

# T_4 split-larger
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

print("\n  T_4 split-larger:")
check_generalized_pattern(4, lambda p: cfg_T4_split_larger(*p), params_sl4, "split-larger")

# T_4 split-tower
def cfg_T4_split_tower2(q1, q2, q3):
    if q1 <= 0 or q1 > 8 or q2 <= 0 or q2 > 4 or q3 <= 0 or q3 > 2:
        return None
    frags_top = [F(16)-q1, q1]
    frags_t8 = [F(8)-q2, q2]
    frags_t4 = [F(4)-q3, q3]
    towers = [F(2), F(1)]
    return (frags_top + frags_t8 + frags_t4, towers)

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

print("\n  T_4 split-tower2:")
check_generalized_pattern(4, lambda p: cfg_T4_split_tower2(*p), params_st4, "split-tower2")

# T_5 cascade (coarse)
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

print("\n  T_5 cascade:")
check_generalized_pattern(5, lambda p: cfg_T5_cascade(*p), params_cascade5, "cascade")
