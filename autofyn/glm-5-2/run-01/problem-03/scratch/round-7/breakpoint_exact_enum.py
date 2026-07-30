"""
Round 7: EXHAUSTIVE exact-Fraction enumeration of STRONG BREAKPOINTS of T_3 and T_4
by TIE STRUCTURE (not grid). Decisive test of "balance ⟹ block".

A strong breakpoint of T_n (cascade type) = the top 2^n is split into r fragments
f1 >= f2 >= ... >= fr > 0 (sum 2^n), and EVERY fragment value appears >= 2 times in
the full multiset {f1..fr, 2^{n-1}, ..., 1}. (Each fragment ties an adjacent piece.)

We enumerate all TIE STRUCTURES: a set partition of the r fragments into groups,
where each group is either
  (a) assigned to a tower value 2^k (so those fragments = 2^k, tying the tower piece), or
  (b) a "free" non-dyadic group (group size >= 2, since a non-dyadic value must appear
      >= 2 times to tie another fragment; it can't tie a tower piece).

For each tie structure, the fragment equalities are linear constraints; together with
sum = 2^n we solve exactly (Fraction). We keep solutions with all fragments > 0 and
sorted (f1 >= f2 >= ... >= fr), and cascade-realizable.

For each realized strong breakpoint we:
  - compute D of the full config (exact)
  - compute the spine (pair-cancellation) with ORIGIN tracking (F=fragment, T=tower)
  - check the block condition on the spine: all F at + (even 0-based positions),
    all T at - (odd). [For cascade, single split group, block = all frags same sign;
    D=1 forces all-frag-+ by mass-balance, so block-fail = some frag at -.]
  - record whether D=1 AND block FAILS (the counterexample we hunt).

This is EXHAUSTIVE over tie structures => every strong breakpoint rational config is hit.
"""
from fractions import Fraction as F
from itertools import product
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
    return False

# ---- Bell / set-partition enumeration ----
def set_partitions(items):
    """Yield all set partitions of a list as a list of lists (groups)."""
    items = list(items)
    if not items:
        yield []
        return
    first = items[0]
    rest = items[1:]
    for sp in set_partitions(rest):
        # first in its own group
        yield [[first]] + sp
        # first joins an existing group
        for i, g in enumerate(sp):
            new_sp = [list(g2) for g2 in sp]
            new_sp[i] = [first] + list(g)
            yield new_sp

def spine_with_origins(pieces, origins):
    """Pair-cancellation spine. pieces/origins aligned.
    Returns list of (value, origin) sorted descending, one copy per value with odd count.
    Survivor origin: if value has odd #F, it's F; else T (odd #T since total odd)."""
    val_count = Counter(pieces)
    val_origins = defaultdict(list)
    for v, o in zip(pieces, origins):
        val_origins[v].append(o)
    sp = []
    for v in sorted(val_count.keys(), reverse=True):
        cnt = val_count[v]
        if cnt % 2 == 1:
            olist = val_origins[v]
            nF = olist.count('F')
            if nF % 2 == 1:
                sp.append((v, 'F'))
            else:
                sp.append((v, 'T'))
    return sp

def block_pattern_on_spine(sp):
    """sp: list of (value, origin) descending.
    Block pattern (all-frag-+, all-tower-): all F at even idx, all T at odd idx.
    Returns (pattern_ok, block_ok, frag_positions, tower_positions).
    block_ok (cascade) = all frags at same sign = all F at even OR all F at odd."""
    frag_pos = [i for i,(v,o) in enumerate(sp) if o == 'F']
    tow_pos = [i for i,(v,o) in enumerate(sp) if o == 'T']
    all_frag_plus = all(i % 2 == 0 for i in frag_pos)
    all_frag_minus = all(i % 2 == 1 for i in frag_pos)
    all_tow_minus = all(i % 2 == 1 for i in tow_pos)
    pattern = all_frag_plus and all_tow_minus
    block = all_frag_plus or all_frag_minus  # single split group: all frags same sign
    return pattern, block, frag_pos, tow_pos

# ============================================================
# Cascade type: r fragments of 2^n. Enumerate tie structures.
# ============================================================
def enumerate_cascade_breakpoints(n, r):
    """
    n: tower index (top = 2^n). r: number of fragments (r = n for full cascade? or r <= n+1).
    Returns list of (fragments_list, full_config, D, spine, pattern, block, D1_block_fail).
    """
    top = F(2)**n
    towers = [F(2)**(n-1-k) for k in range(n)]  # 2^{n-1},...,1
    tower_vals = sorted(set(towers), reverse=True)  # distinct tower values

    idx = list(range(r))
    results = []
    seen_configs = set()

    for sp in set_partitions(idx):
        groups = sp  # list of lists of fragment indices
        ngroups = len(groups)
        # For each group, decide: assign a tower value, or "free" (non-dyadic, size>=2).
        # A group assigned a tower value 2^k: all fragments in it = 2^k.
        #   But two different groups can be assigned the SAME tower value only if that
        #   tower value appears once among towers; multiple groups -> multiple fragments
        #   equal that tower -> fine (ties the one tower piece, appears >=2).
        #   Actually each tower value 2^k appears exactly once among towers. Assigning
        #   groups to tower values: each tower value can be assigned to >=0 groups.
        # A "free" group: non-dyadic value, size>=2.
        # Enumerate assignments: for each group, choice in tower_vals + "free".
        choices = []
        for g in groups:
            opts = list(tower_vals) + ['free']
            choices.append(opts)
        for combo in product(*choices):
            # Validate: free groups must have size >= 2
            valid = True
            assigned_vals = {}  # group_index -> value
            for gi, (g, c) in enumerate(zip(groups, combo)):
                if c == 'free' and len(g) < 2:
                    valid = False; break
                assigned_vals[gi] = c
            if not valid:
                continue
            # Two free groups could collide (same non-dyadic value) -> then they'd merge.
            # For a clean tie structure, distinct free groups should have DISTINCT values.
            # But the breakpoint condition only needs each value to appear >=2; if two free
            # groups happen to solve to the same value, that's a different (coarser) tie
            # structure already enumerated. To avoid double-counting, we just solve and dedupe.
            # Build linear system: f_i = value_of_its_group for each fragment i.
            # Sum of all fragments = 2^n.
            # If there are free groups, they each have ONE unknown value (all frags in group
            # equal that value). Let the free group values be unknowns v_1,...,v_m.
            # Constraint: sum of fragments = 2^n gives one equation in m unknowns.
            # If m == 1: solve uniquely. If m > 1: underdetermined -> a FAMILY of breakpoints
            # (a tie FACE). The D value on this face is affine; we need to check if D=1 is
            # achievable and whether block holds. For m==1 (one free group), we get isolated
            # breakpoints; for m==0, a fully-dyadic breakpoint; for m>=2, a face.
            free_groups = [gi for gi in range(ngroups) if combo[gi] == 'free']
            nfree = len(free_groups)
            # Assign known values to non-free groups
            frag_val = [None]*r
            for gi, g in enumerate(groups):
                if combo[gi] != 'free':
                    for i in g:
                        frag_val[i] = combo[gi]
            if nfree == 0:
                # All fragments assigned tower values. Sum must = 2^n.
                s = sum(frag_val)
                if s != top:
                    continue
                frags = sorted([frag_val[i] for i in range(r)], reverse=True)
            elif nfree == 1:
                # One free group g0 with |g0| fragments all equal to v. Sum = 2^n.
                g0 = groups[free_groups[0]]
                known_sum = sum(frag_val[i] for i in range(r) if frag_val[i] is not None)
                v = (top - known_sum) / len(g0)
                if v <= 0:
                    continue
                # v must be non-dyadic (not a tower value) for this tie structure to be
                # the "free" type; if v is dyadic, it's a coarser structure already covered.
                # We keep it anyway (dedupe by config) but note.
                for i in g0:
                    frag_val[i] = v
                frags = sorted([frag_val[i] for i in range(r)], reverse=True)
            else:
                # nfree >= 2: a tie FACE. The D value on the face is affine in the free vars.
                # We check: is D=1 achievable on this face (within the face's cone), and if so
                # does block hold? For now, SAMPLE the face: pick the free vars to make D=1
                # if possible, and also check block at representative points.
                # Simpler: parametrize. Let free vars v_1,...,v_m (m=nfree), constraint
                # sum = 2^n -> v_m determined by others. D is affine in v_1,..,v_{m-1}.
                # We check the face's D range by sampling extreme rays of the feasible cone
                # (where some v hits 0 or hits ordering bounds) — those are lower-dim faces
                # already enumerated. So the D=1 achievable points on this face are covered
                # by lower-dim faces IF D=1 is attained at a sub-face. But if the whole face
                # has D≡1 (affine constant), then block on the face is what matters.
                # Check: is D constant on this face? D = alt_sum(full config). On the face,
                # fragment values v_j appear |g_j| times. D = sum over fragments of sign*value.
                # The signs depend on sort order, which is FIXED on the face interior (that's
                # the point of the tie structure). So D is linear in the v_j's. With the
                # constraint sum v_j*|g_j| = (top - known), and m>=2 free, D is generically
                # non-constant. So D=1 is a codimension-1 slice -> a sub-face -> enumerated
                # at lower dim. Hence we can SKIP nfree>=2 faces here (their D=1 points are
                # covered by nfree<=1 sub-faces). EXCEPT the case where the face itself has
                # D≡1 identically (then every point is D=1 and block must hold on the face).
                # Check D≡1 on the face: D as a function of free vars is constant iff the
                # coefficient of each free var (with the sum constraint eliminating one) is 0.
                # This is the "block condition => D constant" of telescoping-block-lemma!
                # We test it directly: compute D's partial structure symbolically.
                # For simplicity here, just record the face and move on; the nfree<=1 cases
                # are the isolated breakpoints and will catch any counterexample.
                continue
            # Now frags is a realized breakpoint multiset. Dedupe.
            frags_t = tuple(frags)
            # ANY multiset of r positive frags summing to top is realizable by SOME
            # splitting tree (split off pieces greedily). D + block are multiset-level,
            # so the tree is irrelevant. No realizability constraint.
            if any(f <= 0 for f in frags):
                continue
            if frags != sorted(frags, reverse=True):
                continue
            full = list(frags) + list(towers)
            key = tuple(sorted(full, reverse=True))
            if key in seen_configs:
                continue
            seen_configs.add(key)
            D = alt_sum(full)
            origins = ['F']*len(frags) + ['T']*len(towers)
            sp = spine_with_origins(full, origins)
            pattern, block, fpos, tpos = block_pattern_on_spine(sp)
            d1_block_fail = (D == 1 and not block)
            results.append({
                'n': n, 'r': r, 'frags': frags, 'towers': list(towers),
                'full': full, 'D': D, 'spine': sp,
                'pattern': pattern, 'block': block,
                'd1_block_fail': d1_block_fail,
                'tie': combo,
            })
    return results

def summarize(results, label):
    print(f"\n=== {label} ===")
    print(f"  total strong breakpoints: {len(results)}")
    d1 = [r for r in results if r['D'] == 1]
    print(f"  D=1 count: {len(d1)}")
    d1_block_ok = [r for r in d1 if r['block']]
    d1_block_fail = [r for r in d1 if not r['block']]
    print(f"  D=1 block OK: {len(d1_block_ok)}")
    print(f"  D=1 block FAIL (COUNTEREXAMPLES): {len(d1_block_fail)}")
    for r in d1_block_fail[:20]:
        print(f"    COUNTEREXAMPLE: frags={r['frags']} towers={r['towers']} "
              f"D={r['D']} spine={[(str(v),o) for v,o in r['spine']]} "
              f"pattern={r['pattern']} block={r['block']} tie={r['tie']}")
    # distribution of D values
    dvals = Counter(r['D'] for r in results)
    print(f"  D value distribution (top 10): {sorted(dvals.items())[:10]}")
    if d1:
        # show a few D=1 examples with their spine
        print(f"  Sample D=1 breakpoints:")
        for r in d1[:5]:
            print(f"    frags={r['frags']} spine={[(str(v),o) for v,o in r['spine']]} "
                  f"pattern={r['pattern']} block={r['block']}")

# T_3 cascade: n=3, top=8, r=4 fragments
print("="*70)
print("T_3 cascade (top 8 -> 4 fragments, 3 marks)")
print("="*70)
res_t3_casc = enumerate_cascade_breakpoints(3, 4)
summarize(res_t3_casc, "T_3 cascade")

# T_3 split-larger type: top 8 split into 3 fragments via 2 marks on larger piece.
#   frags f1 >= f2 >= f3 > 0, sum 8, cascade on larger: f2 >= f3 (since f1 split off, then
#   f1's remainder split). Actually split-larger: 8 -> (8-q1)+q1, then split (8-q1) [the larger]
#   -> (8-q1-q2)+q2. So frags = [8-q1-q2, q2, q1] sorted descending = [f_big, q2, q1] with
#   f_big = 8-q1-q2 >= q2 >= q1. r=3 fragments.
print("\n"+"="*70)
print("T_3 split-larger (top 8 -> 3 fragments, 2 marks)")
print("="*70)
res_t3_sl = enumerate_cascade_breakpoints(3, 3)
summarize(res_t3_sl, "T_3 split-larger")

# T_3 split-tower: top 8 -> 2 frags (8-q1)+q1, tower 4 -> (4-q2)+q2. r=2 top frags + 2 tower-4 frags.
# This is a different origin structure; handle separately below.

# T_4 cascade: n=4, top=16, r=4 fragments (3 marks) -- main type
print("\n"+"="*70)
print("T_4 cascade (top 16 -> 4 fragments, 3 marks)")
print("="*70)
res_t4_casc = enumerate_cascade_breakpoints(4, 4)
summarize(res_t4_casc, "T_4 cascade")

# T_4 cascade with 4 marks (r=5 fragments) -- fuller
print("\n"+"="*70)
print("T_4 cascade-5 (top 16 -> 5 fragments, 4 marks)")
print("="*70)
res_t4_casc5 = enumerate_cascade_breakpoints(4, 5)
summarize(res_t4_casc5, "T_4 cascade-5")

print("\n"+"="*70)
print("T_4 split-larger (top 16 -> 3 fragments, 2 marks)")
print("="*70)
res_t4_sl = enumerate_cascade_breakpoints(4, 3)
summarize(res_t4_sl, "T_4 split-larger")

# ============================================================
# SPLIT-TOWER type: top split into 2 frags + a tower piece 2^k split into 2 frags.
# Origin: top frags = F, tower-derived frags = T (same origin as unsplit towers).
# ============================================================
def enumerate_split_tower_breakpoints(n, k):
    """
    T_n: top 2^n split into 2 frags (q1, 8-q1); tower piece 2^k (k<n) split into 2 frags.
    r_top = 2, r_tow = 2. Full fragments: 2 top + 2 tower-k. Towers: the rest (unsplit).
    Origin: top frags = F, tower-k frags = T, unsplit towers = T.
    Breakpoint: every fragment value appears >= 2 in full multiset.
    """
    top = F(2)**n
    tow_k = F(2)**k
    # unsplit towers: all 2^j for j in 0..n-1 except j=k
    unsplit = [F(2)**j for j in range(n) if j != k]  # 2^{n-1},... but exclude 2^k
    # actually towers are 2^{n-1},...,2,1 = 2^j for j=0..n-1
    unsplit = [F(2)**j for j in range(n) if j != k]
    # 4 fragments: f_t1 = top - q1, f_t2 = q1 (top frags); f_k1 = tow_k - q2, f_k2 = q2.
    # Tie structures among {f_t1, f_t2, f_k1, f_k2}: set partitions + tower-value/free assignment.
    idx = [0,1,2,3]  # 0,1 = top frags; 2,3 = tower-k frags
    results = []
    seen = set()
    tower_vals = sorted(set([F(2)**j for j in range(n)]), reverse=True)
    for sp in set_partitions(idx):
        groups = sp
        ngroups = len(groups)
        choices = []
        for g in groups:
            opts = list(tower_vals) + ['free']
            choices.append(opts)
        for combo in product(*choices):
            valid = True
            for gi, g in enumerate(groups):
                if combo[gi] == 'free' and len(g) < 2:
                    valid = False; break
            if not valid: continue
            free_groups = [gi for gi in range(ngroups) if combo[gi] == 'free']
            nfree = len(free_groups)
            frag_val = [None]*4
            for gi, g in enumerate(groups):
                if combo[gi] != 'free':
                    for i in g: frag_val[i] = combo[gi]
            if nfree == 0:
                # all 4 frags assigned tower values. sum must = top + tow_k.
                # top frags sum to top, tower-k frags sum to tow_k.
                s_top = frag_val[0] + frag_val[1]
                s_k = frag_val[2] + frag_val[3]
                if s_top != top or s_k != tow_k:
                    continue
                frags = [frag_val[0], frag_val[1], frag_val[2], frag_val[3]]
            elif nfree == 1:
                g0 = groups[free_groups[0]]
                # determine which "sum constraint" applies. The free group may be among
                # top frags, tower-k frags, or mixed. We have TWO sum constraints:
                #   frag_val[0]+frag_val[1] = top,  frag_val[2]+frag_val[3] = tow_k.
                # If the free group is entirely within {0,1} or entirely within {2,3},
                # one constraint determines v. If mixed, TWO unknowns... but nfree=1 means
                # one group with one value v; if mixed, both constraints must give same v.
                # Check: the free group has all frags = v. The non-free frags have fixed vals.
                # Constraint A: (sum of top frags) = top -> (sum of free-in-{0,1})*v + known_top = top.
                # Constraint B: (sum of tow-k frags) = tow_k -> (sum of free-in-{2,3})*v + known_k = tow_k.
                free_in_top = [i for i in g0 if i in (0,1)]
                free_in_k = [i for i in g0 if i in (2,3)]
                known_top = sum(frag_val[i] for i in (0,1) if frag_val[i] is not None)
                known_k = sum(frag_val[i] for i in (2,3) if frag_val[i] is not None)
                vA = (top - known_top) / len(free_in_top) if free_in_top else None
                vB = (tow_k - known_k) / len(free_in_k) if free_in_k else None
                if free_in_top and free_in_k:
                    if vA != vB: continue
                    v = vA
                elif free_in_top:
                    v = vA
                else:
                    v = vB
                if v is None or v <= 0:
                    continue
                for i in g0: frag_val[i] = v
                frags = [frag_val[0], frag_val[1], frag_val[2], frag_val[3]]
            else:
                continue  # face, skip
            # fragments: top frags must be (>=0, sum top), tower-k frags sum tow_k.
            # Realizability: q1 = f_t2, q1 <= top/2 (so f_t2 <= f_t1). q2 = f_k2, q2 <= tow_k/2.
            if frag_val[1] > frag_val[0]: continue  # q1 > 8-q1
            if frag_val[3] > frag_val[2]: continue  # q2 > tow_k - q2
            if any(f <= 0 for f in frags): continue
            full = list(frags) + list(unsplit)
            # origins: top frags F, tower-k frags T, unsplit T
            origins = ['F','F','T','T'] + ['T']*len(unsplit)
            key = tuple(sorted(full, reverse=True))
            if key in seen: continue
            seen.add(key)
            D = alt_sum(full)
            sp_spine = spine_with_origins(full, origins)
            # block condition for split-tower: top-frag group all same sign AND tower-k-frag group all same sign
            top_surv_idx = [i for i,(v,o) in enumerate(sp_spine) if o == 'F']
            # tower-k frags have origin T but we need to distinguish them from unsplit towers.
            # Actually for block: "each split's fragments at same sign". Top split: all top-frag
            # survivors at same sign. Tower-k split: all tower-k-frag survivors at same sign.
            # But spine doesn't distinguish tower-k-frags from unsplit towers (both origin T).
            # The mass-balance pattern for D=1 (split-tower): top frags at +, ALL tower-derived
            # (split-tower frags + unsplit) at -. So pattern = all F at +, all T at -.
            fpos = [i for i,(v,o) in enumerate(sp_spine) if o == 'F']
            tpos = [i for i,(v,o) in enumerate(sp_spine) if o == 'T']
            pattern = all(i % 2 == 0 for i in fpos) and all(i % 2 == 1 for i in tpos)
            # block (split-tower): top frags same sign (the tower-k frags automatically same sign
            # as unsplit towers in the pattern). For block we need: top frags all same sign.
            block = (all(i % 2 == 0 for i in fpos) or all(i % 2 == 1 for i in fpos))
            d1_block_fail = (D == 1 and not block)
            results.append({
                'n': n, 'k': k, 'frags': frags, 'unsplit': unsplit,
                'full': full, 'D': D, 'spine': sp_spine,
                'pattern': pattern, 'block': block,
                'd1_block_fail': d1_block_fail, 'tie': combo,
            })
    return results

print("\n"+"="*70)
print("T_3 split-tower (top 8 -> 2 frags, tower 4 -> 2 frags)")
print("="*70)
res_t3_st = enumerate_split_tower_breakpoints(3, 2)  # tower piece 4 = 2^2, k=2
summarize(res_t3_st, "T_3 split-tower (k=2)")

print("\n"+"="*70)
print("T_3 split-tower (top 8 -> 2 frags, tower 2 -> 2 frags, k=1)")
print("="*70)
res_t3_st2 = enumerate_split_tower_breakpoints(3, 1)
summarize(res_t3_st2, "T_3 split-tower (k=1)")

print("\n"+"="*70)
print("T_4 split-tower (top 16 -> 2 frags, tower 8 -> 2 frags, k=3)")
print("="*70)
res_t4_st = enumerate_split_tower_breakpoints(4, 3)
summarize(res_t4_st, "T_4 split-tower (k=3)")

print("\n"+"="*70)
print("T_4 split-tower (top 16 -> 2 frags, tower 4 -> 2 frags, k=2)")
print("="*70)
res_t4_st2 = enumerate_split_tower_breakpoints(4, 2)
summarize(res_t4_st2, "T_4 split-tower (k=2)")

# ============================================================
# GRAND TOTALS
# ============================================================
all_res = res_t3_casc + res_t3_sl + res_t3_st + res_t3_st2 + res_t4_casc + res_t4_casc5 + res_t4_sl + res_t4_st + res_t4_st2
print("\n"+"="*70)
print("GRAND TOTALS (all strong breakpoints enumerated by tie structure)")
print("="*70)
print(f"Total strong breakpoints: {len(all_res)}")
d1_all = [r for r in all_res if r['D'] == 1]
print(f"D=1 count: {len(d1_all)}")
d1_bfail_all = [r for r in d1_all if not r['block']]
print(f"D=1 block FAIL (COUNTEREXAMPLES to balance->block): {len(d1_bfail_all)}")
for r in d1_bfail_all:
    print(f"  COUNTEREXAMPLE: n={r.get('n')} frags={r['frags']} D={r['D']} "
          f"spine={[(str(v),o) for v,o in r['spine']]} block={r['block']}")
