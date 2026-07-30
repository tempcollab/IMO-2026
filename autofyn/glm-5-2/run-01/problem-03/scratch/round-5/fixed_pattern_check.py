"""
Round 5: Fixed pattern check — "dyadic" = tower piece value (2^k, k>=0, i.e. >= 1).
The previous run misclassified 1/8 = 2^{-3} as dyadic. In tower units, tower pieces
are 2^k for k = 0,...,n (all >= 1). Fragments < 1 are NOT tower values.

KEY FINDING from previous run:
  - "nd at - (block fail)" = 0 EVERYWHERE (all types, all n).
  - But 79/120 T_3 cascade had "nd at + but dy not all at -" — likely due to
    misclassifying small fragments (1/8, etc.) as dyadic.

With the fix, we expect: ALL D=1 configs have the generalized pattern
(non-tower-valued spine pieces at +, tower-valued pieces at -).
"""
from fractions import Fraction as F
from collections import Counter

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

def is_tower_val(x, n):
    """True iff x is a tower piece value: x = 2^k for some k in {0,...,n}."""
    if x <= 0: return False
    if isinstance(x, F):
        if x.denominator == 1:
            v = int(x)
            return v > 0 and (v & (v-1)) == 0 and v <= 2**n
        # Fraction like 1/8: not a tower value (tower values are integers)
        return False
    return False

def is_pow2_int(x):
    """True iff x is a positive integer power of 2."""
    if x <= 0: return False
    if isinstance(x, F):
        if x.denominator == 1:
            v = int(x)
            return v > 0 and (v & (v-1)) == 0
        return False
    return False

def spine(pieces):
    s = sorted(pieces, reverse=True)
    c = Counter(s)
    return sorted([v for v in sorted(c, reverse=True) for _ in range(c[v] % 2)], reverse=True)

def tower(n):
    return [F(2**(n-k)) for k in range(n+1)]

def check_generalized_pattern(n, cfg_fn, param_ranges, label):
    d1_count = 0
    sp_dyadic = 0  # spine all tower-valued
    sp_pattern = 0  # non-tower at +, tower at -
    sp_nd_at_minus = 0  # non-tower piece at - position (block fail)
    sp_nd_plus_dy_plus = 0  # non-tower at + but some tower also at +
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
        # Classify spine pieces: tower-valued (unsplit tower pieces) vs non-tower (fragments)
        is_tv = [is_tower_val(v, n) for v in sp]

        if all(is_tv):
            sp_dyadic += 1
            continue

        # Check: all non-tower pieces at + (even 0-based positions)?
        nd_pos = [i for i, tv in enumerate(is_tv) if not tv]
        dy_pos = [i for i, tv in enumerate(is_tv) if tv]

        all_nd_plus = all(i % 2 == 0 for i in nd_pos)
        all_dy_minus = all(i % 2 == 1 for i in dy_pos)

        if all_nd_plus and all_dy_minus:
            sp_pattern += 1
        elif all_nd_plus and not all_dy_minus:
            sp_nd_plus_dy_plus += 1
            if len(fail_examples) < 10:
                fail_examples.append((params, sp, nd_pos, dy_pos))
        else:
            sp_nd_at_minus += 1
            if len(fail_examples) < 10:
                fail_examples.append((params, sp, nd_pos, dy_pos))

    print(f"  {label} (T_{n}): D=1 = {d1_count}, spine all-tower = {sp_dyadic}, "
          f"pattern (frag +, tower -) = {sp_pattern}, "
          f"frag+ but tower not all- = {sp_nd_plus_dy_plus}, "
          f"frag at - (BLOCK FAIL) = {sp_nd_at_minus}")
    if fail_examples:
        print(f"  Non-pattern examples:")
        for params, sp, nd_pos, dy_pos in fail_examples[:5]:
            print(f"    params={params}")
            print(f"      spine={sp}")
            print(f"      nd_pos(+)={nd_pos} dy_pos={dy_pos}")
            for i, v in enumerate(sp):
                tv = is_tower_val(v, n)
                print(f"        pos {i} ({'+' if i%2==0 else '-'}): {v} {'tower' if tv else 'FRAG'}")
    return d1_count, sp_dyadic, sp_pattern, sp_nd_at_minus

# === Configs ===
def cfg_T3_cascade(q1, q2, q3):
    if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > q1/2 or q3 <= 0 or q3 > q2/2:
        return None
    return ([F(8)-q1, q1-q2, q2-q3, q3], [F(4), F(2), F(1)])

def cfg_T3_split_larger(q1, q2):
    if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > (8-q1)/2:
        return None
    return ([F(8)-q1-q2, q2, q1], [F(4), F(2), F(1)])

def cfg_T3_split_tower(q1, q2):
    if q1 <= 0 or q1 > 4 or q2 <= 0 or q2 > 2:
        return None
    return ([F(8)-q1, q1, F(4)-q2, q2], [F(2), F(1)])

def cfg_T4_cascade(q1, q2, q3):
    if q1 <= 0 or q1 > 8 or q2 <= 0 or q2 > q1/2 or q3 <= 0 or q3 > q2/2:
        return None
    return ([F(16)-q1, q1-q2, q2-q3, q3], [F(8), F(4), F(2), F(1)])

def cfg_T4_split_larger(q1, q2, q3):
    if q1 <= 0 or q1 > 8 or q2 <= 0 or q2 > (16-q1)/2 or q3 <= 0 or q3 > (16-q1-q2)/2:
        return None
    return ([F(16)-q1-q2-q3, q3, q2, q1], [F(8), F(4), F(2), F(1)])

def cfg_T4_split_tower2(q1, q2, q3):
    if q1 <= 0 or q1 > 8 or q2 <= 0 or q2 > 4 or q3 <= 0 or q3 > 2:
        return None
    return ([F(16)-q1, q1, F(8)-q2, q2, F(4)-q3, q3], [F(2), F(1)])

def cfg_T5_cascade(q1, q2, q3, q4):
    if q1 <= 0 or q1 > 16 or q2 <= 0 or q2 > q1/2 or q3 <= 0 or q3 > q2/2 or q4 <= 0 or q4 > q3/2:
        return None
    return ([F(32)-q1, q1-q2, q2-q3, q3-q4, q4], [F(16), F(8), F(4), F(2), F(1)])

# === Param ranges ===
N = 8
params_cascade3 = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, int(2*q1*N)+1):
        q2 = F(q2n, N)
        if q2 > q1/2: break
        for q3n in range(1, int(2*q2*N)+1):
            q3 = F(q3n, N)
            if q3 > q2/2: break
            params_cascade3.append((q1, q2, q3))

params_sl3 = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, int((8-q1)*N/2)+1):
        q2 = F(q2n, N)
        if q2 > (8-q1)/2: break
        params_sl3.append((q1, q2))

params_st3 = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    for q2n in range(1, 2*N+1):
        q2 = F(q2n, N)
        if q2 > 2: break
        params_st3.append((q1, q2))

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

# === Run ===
print("=" * 70)
print("GENERALIZED PATTERN CHECK (fixed: tower-valued = 2^k, k>=0)")
print("Pattern: all fragments (non-tower-valued) at + positions,")
print("         all tower-valued pieces at - positions, in the spine.")
print("If this holds for ALL D=1 configs, then sub-gap (ii) is vacuous")
print("and the obstruction is purely sub-gap (i): V-shape faces -> block condition.")
print("=" * 70)

print("\nT_3:")
check_generalized_pattern(3, lambda p: cfg_T3_cascade(*p), params_cascade3, "cascade")
check_generalized_pattern(3, lambda p: cfg_T3_split_larger(*p), params_sl3, "split-larger")
check_generalized_pattern(3, lambda p: cfg_T3_split_tower(*p), params_st3, "split-tower")

print("\nT_4:")
check_generalized_pattern(4, lambda p: cfg_T4_cascade(*p), params_cascade4, "cascade")
check_generalized_pattern(4, lambda p: cfg_T4_split_larger(*p), params_sl4, "split-larger")
check_generalized_pattern(4, lambda p: cfg_T4_split_tower2(*p), params_st4, "split-tower2")

print("\nT_5:")
check_generalized_pattern(5, lambda p: cfg_T5_cascade(*p), params_cascade5, "cascade")

# === Additional: check the mass balance at spine level ===
print("\n" + "=" * 70)
print("SPINE-LEVEL MASS BALANCE: for each D=1 config,")
print("  S_+(spine) = (total_spine + 1) / 2 ?")
print("(This is the condition D(spine) = 1.)")
print("=" * 70)

def check_spine_mass_balance(n, cfg_fn, param_ranges, label):
    d1_count = 0
    ok = 0
    fail = 0
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
        S_total = sum(sp)
        S_plus = sum(sp[i] for i in range(0, len(sp), 2))
        expected = F(S_total + 1, 2)
        if S_plus == expected:
            ok += 1
        else:
            fail += 1
            if fail <= 3:
                print(f"  FAIL: {label} sp={sp} S+={S_plus} expected={expected}")
    print(f"  {label} (T_{n}): D=1 = {d1_count}, spine mass balance OK = {ok}, FAIL = {fail}")

print("\nT_3:")
check_spine_mass_balance(3, lambda p: cfg_T3_cascade(*p), params_cascade3, "cascade")
check_spine_mass_balance(3, lambda p: cfg_T3_split_larger(*p), params_sl3, "split-larger")
check_spine_mass_balance(3, lambda p: cfg_T3_split_tower(*p), params_st3, "split-tower")

print("\nT_4:")
check_spine_mass_balance(4, lambda p: cfg_T4_cascade(*p), params_cascade4, "cascade")
check_spine_mass_balance(4, lambda p: cfg_T4_split_larger(*p), params_sl4, "split-larger")
check_spine_mass_balance(4, lambda p: cfg_T4_split_tower2(*p), params_st4, "split-tower2")

print("\nT_5:")
check_spine_mass_balance(5, lambda p: cfg_T5_cascade(*p), params_cascade5, "cascade")

# === Check: does every D=1 face contain a dyadic config? ===
print("\n" + "=" * 70)
print("DYADIC ENDPOINT CHECK: for each D=1 config, is there a dyadic config")
print("on the same face (same sort-order-with-ties pattern)?")
print("  Simplified: check if the type has D=1 dyadic configs,")
print("  and if D=1 configs form a connected set reaching the dyadic.")
print("=" * 70)

def check_face_dyadic(n, cfg_fn, param_ranges, label):
    """Check if D=1 configs are connected (grid BFS) to a dyadic D=1 config."""
    d1_set = set()
    d1_cfgs = []
    dyadic_d1 = []
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
        d1_set.add(params)
        d1_cfgs.append((params, all_pieces))
        if all(is_tower_val(v, n) for v in all_pieces):
            dyadic_d1.append(params)

    if not d1_set:
        print(f"  {label} (T_{n}): no D=1 configs")
        return
    if not dyadic_d1:
        print(f"  {label} (T_{n}): D=1 = {len(d1_set)}, NO dyadic D=1!")
        return

    # BFS from first dyadic point
    start = dyadic_d1[0]
    step = F(1, max(N, N4, N5))  # grid step
    visited = {start}
    dq = [start]
    while dq:
        c = dq.pop()
        for i in range(len(c)):
            for d in [step, -step]:
                nb = list(c)
                nb[i] += d
                nb = tuple(nb)
                if nb in d1_set and nb not in visited:
                    visited.add(nb)
                    dq.append(nb)

    outside = d1_set - visited
    print(f"  {label} (T_{n}): D=1 = {len(d1_set)}, dyadic D=1 = {len(dyadic_d1)}, "
          f"connected to dyadic = {len(visited)}, outside = {len(outside)}")
    if outside:
        for p in list(outside)[:3]:
            print(f"    outside: {p}")

print("\nT_3:")
check_face_dyadic(3, lambda p: cfg_T3_cascade(*p), params_cascade3, "cascade")
check_face_dyadic(3, lambda p: cfg_T3_split_larger(*p), params_sl3, "split-larger")
check_face_dyadic(3, lambda p: cfg_T3_split_tower(*p), params_st3, "split-tower")

print("\nT_4:")
check_face_dyadic(4, lambda p: cfg_T4_cascade(*p), params_cascade4, "cascade")
check_face_dyadic(4, lambda p: cfg_T4_split_larger(*p), params_sl4, "split-larger")
check_face_dyadic(4, lambda p: cfg_T4_split_tower2(*p), params_st4, "split-tower2")

print("\nT_5:")
check_face_dyadic(5, lambda p: cfg_T5_cascade(*p), params_cascade5, "cascade")
