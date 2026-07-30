# Lemma TIE-NECESSARY (certified, round 6)

Source: `universal-adversary-strategy.md`, round 6 (skeleton proposed by the
round-6 `math-explorer-coordsplit` report; proved in full by the round-6
proof-builder). Depends only on the already-certified **Lemma D**
(`lemmas/interior-point-linear-obstruction.md`). Numerically sanity-checked
(not the load-bearing justification — the proof below is a complete,
self-contained argument): the "affine on a fixed order-type cell" claim was
checked against 3,892 exact-`Fraction` sample points across 36 distinct
order-type cells of a 2-parameter split (zero mismatches against an affine
fit), and a grid-search global minimum on a concrete 3-piece, 2-mark example
was confirmed to land exactly on a cell boundary (both a zero-length piece
*and* an exact tie simultaneously).

## Setup (Xiang Yu's response space, made precise)

Fix a Liu Bang configuration `A = (p_1 ≥ ... ≥ p_{m_0})` and a mark budget
`k ≤ n`. A **response** is described by:

- a *mark-allocation vector* `(c_1,...,c_{m_0})`, nonnegative integers with
  `Σc_i = k` (WLOG the full budget is used — a response using fewer than `k`
  marks is realized inside this same family by allowing one of the
  resulting sub-pieces to have length exactly `0`, which is already a
  degenerate boundary case, condition (a) below; so nothing is lost by
  requiring `Σc_i=k` on the nose and treating "spend fewer marks" as a
  boundary stratum of this larger space);
- for each `i` with `c_i ≥ 1`, a *cut-position vector*
  `0 ≤ y_{i,1} ≤ ... ≤ y_{i,c_i} ≤ p_i`, producing the `c_i+1` sub-pieces
  `y_{i,1}, y_{i,2}-y_{i,1}, ..., p_i - y_{i,c_i}` of `p_i` (each is a
  *linear* — homogeneous affine — function of the cut positions, with no
  constant term).

For a fixed allocation `(c_i)`, the cut-position vectors range over the
polytope `P_{(c_i)} := ∏_i {0≤y_{i,1}≤...≤y_{i,c_i}≤p_i}` (a product of
"chain simplices," one per piece with `c_i≥1`; total dimension `Σc_i = k`).
There are finitely many allocation vectors `(c_i)` with `Σc_i=k`
(a finite set of compositions of `k` into `m_0` nonnegative parts), so the
full response space is the finite union `⋃_{(c_i)} P_{(c_i)}`, a finite
union of compact polytopes, hence compact.

`oddrank(B)` (`B` = the resulting multiset of `m_0+k` sub-pieces, sorted
descending) depends on the response only through (i) which linear functions
of the cut positions the `m_0+k` resulting sub-pieces are, and (ii) their
relative sorted **order**. Fix a total preorder (with ties allowed) on the
`m_0+k` sub-piece labels; the set of cut-position vectors in `P_{(c_i)}`
realizing a *given strict* total order (no ties) is an open (relatively)
polyhedral region cut out from `P_{(c_i)}` by the finitely many strict
linear inequalities `(\text{piece }a) > (\text{piece }b)` for each pair
`a,b` adjacent in that order (all other pairwise comparisons are implied by
transitivity plus these); call its closure a **cell** `Q`. Since each
resulting piece length is linear in the cut positions, and `oddrank(B)` for
a *fixed* order is a fixed subset-sum (the sum of the pieces landing at odd
sorted rank under that order), `oddrank` restricted to a cell `Q` is a
**linear** (in particular affine) function of the cut-position parameters.

There are finitely many cells in total: finitely many allocation vectors,
and for each, finitely many strict total orders of a finite label set, so
finitely many cells (an order not realized by any point of `P_{(c_i)}`
simply contributes no cell). The response space is the finite union of the
closures of all these cells, and (since a strict order's realizing region is
open dense in its own cell, and every point of `P_{(c_i)}` has *some*
order, possibly with ties) these cell closures cover the whole response
space.

## Statement

Fix `A` and budget `k`, and consider the (compact) response space described
above with the (continuous, since piecewise-affine) function `oddrank(B)`
on it. Let `x*` be **any** global minimizer of `oddrank(B)` over this space
(one exists by compactness + continuity). Then `x*` can be chosen so that
either:

- **(a)** some resulting sub-piece has length exactly `0` (i.e. some
  `y_{i,\ell}=y_{i,\ell+1}$, or `y_{i,1}=0`, or `y_{i,c_i}=p_i` for some
  `i,\ell` — a "wasted" mark, equivalently a response realizable with
  strictly fewer than `c_i` cuts on piece `i`), **or**
- **(b)** two resulting sub-pieces that are *adjacent in sorted order*
  (i.e. consecutive ranks in the sorted list `B`) are exactly equal in
  value.

(Read: *some* global minimizer satisfies (a) or (b) — this is what
"necessary" means: Xiang Yu never needs to look past responses satisfying
(a) or (b) to find an optimum.)

## Proof

Let `x*` be a global minimizer, lying in some cell `Q` (a point may lie in
several cells' closures if it has ties; pick any one cell `Q` containing
`x*`). Two cases.

**Case 1: `x*` already lies on the (relative) boundary of `Q`.** A cell
`Q = P_{(c_i)} ∩ (\text{finitely many closed half-spaces "piece }a\ge
\text{piece }b\text{"})`. Every facet of `Q` is obtained by turning exactly
one of these finitely many defining inequalities into an equality. Each
defining inequality is of one of two kinds: (i) one of `P_{(c_i)}`'s own
chain-simplex inequalities `y_{i,1}\ge0`, `y_{i,\ell}\ge y_{i,\ell+1}`, or
`p_i\ge y_{i,c_i}` — tightening any of these to equality forces a
zero-length sub-piece of `p_i`, i.e. condition (a); or (ii) one of the
order-defining inequalities "piece `a` `\ge` piece `b`" for a pair `a,b`
adjacent in the cell's order — tightening this to equality makes pieces `a`
and `b` (which are sorted-adjacent by construction of the cell) exactly
tied, i.e. condition (b). So *every* boundary point of `Q` — in particular
`x*` itself, in this case — satisfies (a) or (b). Done.

**Case 2: `x*` lies in the relative interior of `Q`.** If `\dim Q = 0`
(`Q` is a single point), then "relative interior" means `Q=\{x^*\}$ itself
— so `x^*` IS the entirety of `Q`, and it suffices to apply exactly the
**same constraint-type dichotomy already used in Case 1**, directly to
`Q$'s own defining inequalities, rather than to assert which specific type
of inequality must be tight.

*(Correction, round 7: an earlier version of this paragraph claimed a
`\dim Q=0` cell must arise specifically from a collapsed chain-simplex
boundary, forcing condition (a) unconditionally. This is false: a
`0`-dimensional cell can equally arise from `k` independent **order-tie**
constraints alone (condition (b)), with no chain-simplex boundary
constraint active at all — e.g. two marks spent inside a single piece `p_1`
(a `2`-dimensional chain simplex `\{0\le y_1\le y_2\le p_1\}`), with the
first sub-piece `y_1` tied to (set exactly equal to) some fixed value `p_2`
and the third sub-piece `p_1-y_2` tied to a different fixed value `p_3`,
pins the `2`-dimensional simplex to the single point
`(y_1,y_2)=(p_2,\,p_1-p_3)$ using **two order-tie constraints alone** — no
chain-simplex inequality (`y_1\ge0`, `y_1\le y_2`, `y_2\le p_1`) is tight at
this point in general, so no sub-piece has length `0`, i.e. condition (a)
does **not** hold, yet `\dim Q=0` genuinely. The dichotomy below replaces
the incorrect unconditional claim.)*

Recall (from the setup) that `Q = P_{(c_i)} \cap (\text{finitely many
closed half-spaces})`, where each defining half-space is either (i) one of
`P_{(c_i)}`'s own chain-simplex inequalities (`y_{i,1}\ge0`,
`y_{i,\ell}\ge y_{i,\ell+1}`, `p_i\ge y_{i,c_i}`), or (ii) one of the
order-defining inequalities "piece `a`\ge`piece `b`" for a pair `a,b`
adjacent in `Q`'s order. A point has dimension `0` (is an extreme point of
`Q`) exactly when the tight inequalities among (i) and (ii), evaluated at
that point, span the full ambient dimension of `P_{(c_i)}` — in particular,
**since the ambient dimension is `\ge1$ whenever `Q` is nonempty and
`k\ge1`,** at least one defining inequality (of type (i) or (ii)) must be
tight at `x^*` (if none were tight, `x^*` would be an interior point of the
full-dimensional polytope `P_{(c_i)}` restricted only by inequalities that
are all slack, which is a positive-dimensional neighborhood, contradicting
`\dim Q=0`). Exactly as in Case 1: a tight inequality of type (i) forces a
zero-length sub-piece, i.e. condition (a); a tight inequality of type (ii)
forces two sorted-adjacent pieces to be exactly equal, i.e. condition (b).
Since at least one inequality (of either type) is tight at `x^*`, `x^*`
itself satisfies (a) or (b) directly — **exactly the disjunctive conclusion
needed, established here without any claim about which type must be tight**
(both types can occur simultaneously; only "at least one" is needed). So
this sub-case reduces to condition (a) or (b) directly, and we are done.

If `\dim Q \ge 1`: `oddrank` restricted to `Q` is affine (established
above), and `x*` minimizes it over the whole response space, in particular
over `Q \supseteq \{x*\}`, so `x*` minimizes `oddrank|_Q`. Apply **Lemma D**
(`lemmas/interior-point-linear-obstruction.md`) to the affine functional
`-oddrank|_Q` (negation turns "minimize `oddrank`" into "maximize
`-oddrank`"): since `-oddrank|_Q$ attains its maximum over the polytope `Q`
at the relative-interior point `x^*`, Lemma D gives that `-oddrank|_Q$ (hence
`oddrank|_Q`) is **constant** on all of `Q`. In particular, `oddrank` takes
the *same* minimal value at every point of `Q`, including every boundary
point of `Q` (nonempty, since `\dim Q\ge1`). Pick any boundary point `x'$ of
`Q`; by the argument in Case 1 (applied to `x'` instead of `x^*`), `x'$
satisfies (a) or (b), and `oddrank(x') = oddrank(x^*)` = the global minimum,
so `x'$ is itself a global minimizer satisfying (a) or (b). Replace `x^*`
by `x'$. Done. ∎

## Discussion

This converts Xiang Yu's continuous optimization (over cut positions) into
a **finite combinatorial search**: it suffices to consider, for each
allocation `(c_i)` with `Σc_i=k` (finitely many), responses built entirely
out of "chain ties" (each cut either lands exactly on an existing value —
tying two adjacent-rank pieces — or is degenerate/wasted). This does *not*
by itself determine *which* ties are optimal (that remains the open
"matching" question, see `universal-adversary-strategy.md`), but it rules
out, once and for all, any need to consider a genuine interior
(non-tied, non-degenerate) stationary point — confirmed in every numeric
instance tested this round (§ above; no genuine interior optimum was ever
found, only ties/degeneracies), consistent with what this proof establishes
unconditionally.

## Status
Certified (round 6; `\dim Q=0` sub-case of the proof corrected round 7).
Fully proved, not merely numerically supported — the numerics above are a
sanity check on the (easily-checked) affine-on-a-cell claim and one concrete
global-minimum example, not the proof itself, which rests entirely on the
already-certified Lemma D plus the finite polytope combinatorics above. The
round-6 write-up's `\dim Q=0` paragraph incorrectly asserted that a
`0`-dimensional cell must arise from a collapsed chain-simplex boundary
(unconditionally forcing condition (a)); round 7 replaces this with a
correct direct argument (at least one defining inequality, of either type,
must be tight at an extreme point, giving (a) or (b) directly) — the
lemma's *statement* was never affected (the disjunctive conclusion always
covered this case via condition (b)), only the proof of this one branch.
