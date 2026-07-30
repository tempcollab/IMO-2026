# Lemma: pl-breakpoint-minimum (B1)

**Statement.** Fix any Liu config `L = (a_1, …, a_m)` (sorted, summing to 1) and a budget of
`k` Xiang marks. The minimum of `D` (the alternating sum of the sorted refined multiset) over
all refinements of `L` using ≤ `k` marks (each mark splits one piece into two positive parts)
is attained at a **balanced/tie (breakpoint) refinement**: a refinement in which, for every
split, the resulting multiset has a tie — either the two fragments of some split are equal, or
some fragment ties an adjacent piece in the sorted order. Equivalently, the minimizer lies at a
**vertex** of the piecewise-linear structure of `D` in the split positions.

**Proof.** The space of ≤ `k`-mark refinements is compact (each split position lives in a closed
interval `[0, a_i]`; degenerate splits `q=0` or `q=a_i` encode "no mark" so the no-mark
refinements are included as boundary points). `D` is continuous in the split positions
(re-sorting is continuous; ties may change the labeling but not the value of the alternating
sum, since equal pieces contribute the same in either order). By Weierstrass, `D` attains its
minimum. Within a fixed **combinatorial type** (a fixed sorted order of all fragments), `D` is a
linear function of each split position `q` (the alternating sum is a fixed-signed linear
combination of the fragment lengths, each an affine function of `q`). A linear function on a
polytope attains its minimum at a vertex; the vertices of the type-polytope are exactly the
points where the sorted order changes, i.e. where a fragment ties an adjacent fragment — a
breakpoint. The global minimum (a minimum of finitely many PL pieces, one per type) is attained
at a breakpoint of some type. See `majorization-upper` Lemma B1; the specialization to Liu's
tower `T_n` is `tail-count` §6.

**Use (and caveat).** This CONSTRAINS where Xiang's optimum lives (to a discrete set of
breakpoint types); it does NOT by itself prove any bound. A type-by-type enumeration "every
type ≤ bound" WOULD be circular (the B3 trap of round 1); the lemma must be used as a
constraint reducing the case space, not as a substitute for the bound.

**Importable by:** `tail-count` (lower-bound reduction to breakpoint configs of `T_n`),
`majorization-upper` (justify that Xiang's optimal first move is a halving or matching-pair
split).
