"""
Round 7 — vertex-enum-n3: FULL exhaustive exact-Fraction enumeration of ALL PL
vertices of the <=3-mark refinement space of T_3 = (8,4,2,1), total D_3 = 15.

GOAL: prove the n=3 LOWER bound D*(T_3) >= 1 (tower units) <==> c(3) >= 8/15.
(Upper bound c(3) <= 8/15 already certified: v3-upper-bound + n2-max-bound.)

=== COMPLETENESS ARGUMENT (the load-bearing hard step) ===

By pl-breakpoint-minimum (certified), the global minimum of D (the alternating sum
of the sorted refined multiset, in tower units) over ALL <=3-mark refinements of
T_3 is attained at a PL vertex (a breakpoint / tie configuration).

A PL vertex lives in a FIXED combinatorial type = a fixed grouping (partition of the
N pieces into 4 tower-groups G_8,G_4,G_2,G_1 summing 8,4,2,1) and a fixed sort order
of the N pieces. Within a fixed grouping, the refinement space is a product of 4
simplices (one per tower), of dimension (N-4) where N = number of pieces = 4 + (active
marks), N in {4,5,6,7}. D is LINEAR (affine) in the split positions on each type-cell.
A type-cell is a polytope; the min of an affine function on a polytope is at a VERTEX
of that polytope. The vertices of a type-cell's closure are where the sort-order
inequalities become tight = TIES (two adjacent-in-sort pieces become equal) or a split
degenerates (a piece -> 0 = fewer active marks = lower N).

A vertex therefore has >= (N-4) independent ties among the N pieces. N pieces with
>= N-4 independent ties collapse to <= N-(N-4) = 4 distinct value-groups. SO:

    (**) EVERY PL vertex of the <=3-mark refinement of T_3 has AT MOST 4 distinct
        piece values (and is an ISOLATED point: the ties + tower-sum equations pin
        all split positions).

A vertex with exactly d distinct values (d <= 4) is pinned by:
  - the d value-equalities (grouping the N pieces into d blocks of equal value), and
  - the 4 tower-sum equations (each tower-group sums to its tower value),
giving a linear system C v = rhs (4 equations in d unknowns), where C[t][b] =
number of pieces of tower t that lie in value-block b. The vertex is ISOLATED iff
this system has a UNIQUE solution (rank C = d). If rank C < d, the tie-structure
is a CONTINUOUS FAMILY (positive-dimensional); D is affine on it, so its min is at a
BOUNDARY of the family = a point with MORE ties (a coarser tie-structure, d-1, same
grouping, captured by the d-1 enumeration) or a degeneracy (piece -> 0, lower N,
captured by the lower-N enumeration).

CONSEQUENCE: enumerating, for every N in {4,5,6,7} and every d in {1,2,3,4}, every
4 x d nonneg-integer count matrix C (margins >= 1, total N), the UNIQUE positive
solution of C v = (8,4,2,1)^T, and recording D = alt_sum(sorted M), CAPTURES THE
GLOBAL MIN. Continuous families are skipped but their minima lie at captured
boundary vertices; degenerate (piece = 0) vertices are captured at their true
(lower) N. This is a FINITE, EXACT (Fraction) exhaustion of the PL-vertex set —
legitimate casework (KB "Casework / exhaustion"), NOT a continuum grid sample.

This is a SUPERSET of the vertex set in the sense that we also record rank=d
solutions whose values coincide pairwise (those are really coarser structures,
already recorded at lower d, and deduped by multiset M). Dedup by M is safe because
D depends ONLY on the multiset M.
"""
from fractions import Fraction as F
from collections import Counter

TOWER_VALUES = [F(8), F(4), F(2), F(1)]   # rows 0..3
D3 = F(15)

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum((F(-1) ** i) * s[i] for i in range(len(s)))

def is_pow2(x):
    if x <= 0:
        return False
    if isinstance(x, F):
        if x.denominator == 1:
            n = int(x)
            return n > 0 and (n & (n - 1)) == 0
        num, den = x.numerator, x.denominator
        return (num & (num - 1)) == 0 and (den & (den - 1)) == 0
    return False

# ---- Gaussian elimination over Fraction, on augmented matrix A (rows x (cols+1)) ----
def row_reduce(A):
    """A: list of lists (augmented, last col = rhs). Returns RREF.
    All entries coerced to Fraction for EXACT arithmetic (no floats)."""
    A = [[F(x) for x in row] for row in A]
    rows = len(A)
    cols = len(A[0]) - 1  # coefficient columns
    pivot_cols = []
    r = 0
    for c in range(cols):
        # find pivot in column c at row >= r
        piv = None
        for rr in range(r, rows):
            if A[rr][c] != 0:
                piv = rr
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        # normalize
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        # eliminate other rows
        for rr in range(rows):
            if rr != r and A[rr][c] != 0:
                f = A[rr][c]
                A[rr] = [a - f * b for a, b in zip(A[rr], A[r])]
        pivot_cols.append(c)
        r += 1
        if r == rows:
            break
    return A, pivot_cols

def solve_system(C, rhs):
    """C: 4 x d matrix (list of d-tuples, 4 rows). rhs: list of 4.
    Returns (status, v) where status in {'unique','underdet','inconsistent'},
    v = solution list (length d, all Fraction) if unique."""
    d = len(C[0])
    A = [[F(x) for x in C[t]] + [F(rhs[t])] for t in range(4)]
    R, pivots = row_reduce(A)
    rank_C = len(pivots)
    # consistency: any row [0 ... 0 | nonzero] => inconsistent
    consistent = True
    for row in R:
        if all(x == 0 for x in row[:-1]) and row[-1] != 0:
            consistent = False
            break
    if not consistent:
        return 'inconsistent', None
    if rank_C < d:
        return 'underdet', None  # continuous family
    # unique: read off solution (each pivot column -> rhs)
    v = [None] * d
    for i, pc in enumerate(pivots):
        # find the row with pivot at pc
        for row in R:
            if row[pc] == 1 and all(row[k] == 0 for k in range(d) if k != pc and k in pivots):
                v[pc] = F(row[-1])
                break
    # fill any free (shouldn't happen for unique)
    if any(x is None for x in v):
        return 'underdet', None
    return 'unique', v

# ---- enumerate 4 x d nonneg integer matrices with total N, all row sums >= 1, col sums >= 1 ----
def gen_matrices(d, N):
    """Yield 4 x d nonneg integer matrices (as list of 4 rows, each a list of d ints)
    with total sum N, every row sum >= 1, every column sum >= 1."""
    # generate compositions of g_0,g_1,g_2,g_3 (each >=1, sum N) and per-row compositions into d parts (>=0)
    # then filter col sums >= 1.
    # compositions of N into 4 positive parts:
    for g0 in range(1, N + 1):
        for g1 in range(1, N - g0 + 1):
            for g2 in range(1, N - g0 - g1 + 1):
                g3 = N - g0 - g1 - g2
                if g3 < 1:
                    continue
                gs = [g0, g1, g2, g3]
                # per-row: compositions of g_t into d nonneg parts
                row_opts = [list(compositions_nonneg(g, d)) for g in gs]
                for r0 in row_opts[0]:
                    for r1 in row_opts[1]:
                        for r2 in row_opts[2]:
                            for r3 in row_opts[3]:
                                C = [r0, r1, r2, r3]
                                # col sums >= 1
                                ok = True
                                for b in range(d):
                                    if r0[b] + r1[b] + r2[b] + r3[b] < 1:
                                        ok = False
                                        break
                                if ok:
                                    yield C

def compositions_nonneg(total, parts):
    """Yield tuples of length `parts` of nonneg ints summing to total."""
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions_nonneg(total - first, parts - 1):
            yield (first,) + rest

def main():
    vertices = []  # list of dicts: {N, d, C, M (tuple sorted desc), D, ...}
    seen_M = {}
    stats = {}
    for N in range(4, 8):
        for d in range(1, min(4, N) + 1):
            count = 0
            consistent = 0
            unique = 0
            for C in gen_matrices(d, N):
                count += 1
                status, v = solve_system(C, TOWER_VALUES)
                if status == 'inconsistent':
                    continue
                if status == 'underdet':
                    continue  # continuous family; min at boundary, captured elsewhere
                # unique
                unique += 1
                if any(x <= 0 for x in v):
                    continue
                # build M
                pieces = []
                for b in range(d):
                    pieces.extend([v[b]] * (C[0][b] + C[1][b] + C[2][b] + C[3][b]))
                if len(pieces) != N:
                    continue
                if sum(pieces) != D3:
                    continue  # hard validation
                M = tuple(sorted(pieces, reverse=True))
                D = alt_sum(pieces)
                # origin classification (ORIGIN-based, not value-type):
                # a piece is a "fragment" if its tower was split (row sum g_t >= 2);
                # else "tower piece" (unsplit). Track per-block origin majority for reporting.
                g = [sum(C[t]) for t in range(4)]
                key = M
                if key not in seen_M:
                    seen_M[key] = True
                    vertices.append({
                        'N': N, 'd': d, 'C': C, 'M': M, 'D': D,
                        'v': v, 'g': g,
                        'split_towers': [t for t in range(4) if g[t] >= 2],
                    })
            stats[(N, d)] = (count, unique)
    # ---- report ----
    print("=" * 72)
    print("FULL EXHAUSTIVE PL-VERTEX ENUMERATION of <=3-mark refinements of T_3")
    print("=" * 72)
    print(f"Towers: {TOWER_VALUES}, total D_3 = {D3}")
    print()
    print("Matrix-enumeration stats (4 x d count matrices, total N, margins >= 1):")
    print(f"{'N':>3} {'d':>3} {'#matrices':>10} {'#unique-soln':>13}")
    tot_mat = 0
    tot_uni = 0
    for (N, d), (cnt, uni) in sorted(stats.items()):
        print(f"{N:>3} {d:>3} {cnt:>10} {uni:>13}")
        tot_mat += cnt
        tot_uni += uni
    print(f"{'tot':>7} {tot_mat:>10} {tot_uni:>13}")
    print()
    print(f"Distinct PL-vertex multisets M recorded: {len(vertices)}")
    print(f"  with D < 1 : {sum(1 for v in vertices if v['D'] < 1)}")
    print(f"  with D = 1 : {sum(1 for v in vertices if v['D'] == 1)}")
    print(f"  with D > 1 : {sum(1 for v in vertices if v['D'] > 1)}")
    minD = min(v['D'] for v in vertices)
    maxD = max(v['D'] for v in vertices)
    print(f"  min D over all vertices: {minD}")
    print(f"  max D over all vertices: {maxD}")
    print()
    print("--- D value distribution ---")
    ddist = Counter(v['D'] for v in vertices)
    for Dval in sorted(ddist):
        print(f"  D = {Dval} : {ddist[Dval]} vertices")
    print()
    print("--- Vertices attaining the minimum D ---")
    for v in sorted([r for r in vertices if r['D'] == minD], key=lambda r: (r['N'], r['d'])):
        # classify origins
        # origin of each piece: tower t, fragment if g[t]>=2 else tower-piece
        origins = []
        for t in range(4):
            tag = 'F' if v['g'][t] >= 2 else 'T'
            for b in range(len(v['v'])):
                origins.extend([tag] * v['C'][t][b])
        F_mass = sum(p for p, o in zip(v['M'], origins) if o == 'F')
        T_mass = sum(p for p, o in zip(v['M'], origins) if o == 'T')
        print(f"  N={v['N']} d={v['d']} D={v['D']} M={list(v['M'])} v={list(v['v'])} "
              f"g={v['g']} split_towers={v['split_towers']} F_mass={F_mass} T_mass={T_mass}")
    print()
    # any D < 1 ? (would refute the candidate answer)
    viol = [r for r in vertices if r['D'] < 1]
    print("--- COUNTEREXAMPLES (D < 1) ---")
    if not viol:
        print("  NONE. min D = %s >= 1. Lower bound D*(T_3) >= 1 VERIFIED at every PL vertex." % minD)
    else:
        for r in viol:
            print(f"  COUNTEREXAMPLE: D={r['D']} M={list(r['M'])} N={r['N']} d={r['d']}")
    print()
    # Mark-distribution type breakdown
    print("--- Mark-distribution (split_towers) breakdown ---")
    from collections import defaultdict
    by_splits = defaultdict(list)
    for v in vertices:
        by_splits[tuple(v['split_towers'])].append(v)
    for st in sorted(by_splits):
        vs = by_splits[st]
        m = min(r['D'] for r in vs)
        print(f"  split_towers={st} ({len(st)} tower(s) split): {len(vs)} vertices, min D={m}")
    print()
    # Equality witness: the dyadic config
    print("--- Equality witness (D=1) ---")
    d1 = [v for v in vertices if v['D'] == 1]
    for v in d1:
        print(f"  M={list(v['M'])} N={v['N']} d={v['d']} (dyadic: all values powers of 2) "
              f"all_pow2={all(is_pow2(x) for x in v['M'])}")
    print()
    # sanity: does the dyadic balanced-pairs config appear?
    target = tuple(sorted([F(4), F(4), F(2), F(2), F(1), F(1), F(1)], reverse=True))
    print(f"Dyadic balanced-pairs config {list(target)} present: {target in seen_M}")
    if target in seen_M:
        Dt = alt_sum(list(target))
        print(f"  its D = {Dt} (expect 1)")

if __name__ == '__main__':
    main()
