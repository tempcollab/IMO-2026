## Status
unsolved (NEW round 19 — UPPER wall, deep interior). Fresh far framing: attack the CERTIFIED
true target `min R(A) ≤ u_nL` (Reduction R-UV) directly via a DIVIDE-AND-CONQUER existence
argument over disjoint sub-profiles, NOT the caterpillar object `μ_{n+1}` that breakpoint-vertex
uses. This dissolves the explorer's false-completeness obstruction (the caterpillar min can
strictly exceed the tree min — irrelevant here, because the tree min is exactly what R-UV needs).

## Target
The whole IMO-2026-P3 upper bound: for every valley profile `A=(a₁≥…≥a_{n+1}>0)`, `Σ=L=1`,
`a₁<L/2` (deep sub-case `a₁ < L/2 − u_nL/2`, the only region still open — boundary layer closed by
certified WTC), Xiang forces `D ≤ u_nL`, where `u_n = 1/(2^{n+1}−1)`. Combined with the certified
lower bound this proves `c(n) = 2^n/(2^{n+1}−1)`.

## Technique (the spine — distinct route)
Divide-and-conquer / disjoint-block differencing on the reachable TREE-value set `R(A)`
(Lemma RL), telescoped by the exact dyadic recursion `1/u_n = 2·(1/u_{n-1}) + 1`.

**Why this is legal where MD2 density-pigeonhole was NOT.** MD2 (dead, R11) pigeonholed the
`2^{n+1}` caterpillar values into `[0,a₁]` and got two values within a gap `< a₁/2^{n+1}` — but a
GAP between two values of OVERLAPPING subsets is not itself reachable, so it died. The fix: if
`P, Q` are **disjoint** nonempty sub-multisets with tree values `x∈T(P)`, `y∈T(Q)`, then `|x−y|`
IS a genuine tree value on `P⊔Q` (root the tree at the difference of the two sub-trees). So a small
DISJOINT-pair discrepancy converts into a real reachable value. The whole game is producing two
disjoint blocks whose reachable windows overlap to within `u_nL`.

## Skeleton
1. **Reduce to the tree target.** By certified Reduction R-UV, the valley upper bound holds iff
   `min R(A) ≤ u_nL`, where `R(A)` = tree-realizable signed-difference values of nonempty
   sub-multisets (Lemma RL characterises it). Boundary layer `a₁ ≥ L/2 − u_nL/2` already closed by
   certified WTC; work in the deep interior `a₁ < L/2 − u_nL/2`. — by R-UV + WTC.
2. **Disjoint-difference primitive.** For disjoint nonempty `P,Q` and `x∈T(P), y∈T(Q)`,
   `|x−y| ∈ T(P⊔Q) ⊆ R(A)`. — by the tree constructor of Lemma RL (difference the two sub-trees).
3. **Scale grouping (ONE-REC engine).** Using certified ONE-REC, split the `n+1` pieces along a
   balanced binary tree of dyadic scales into two disjoint groups `G₁, G₂` at the top level whose
   masses straddle `L/2`; recurse inside each group. Each recursion level halves the target window
   and consumes one "scale of freedom," giving `n` levels. — by ONE-REC scale-truncation +
   induction.
4. **Window-overlap at each level (the exact heart).** At the top split, the deep condition
   `a₁ < L/2 − u_nL/2` guarantees NEITHER group is dominated by a single piece exceeding the other
   group's reachable window, so the two groups' reachable value-sets `T(G₁), T(G₂)` overlap within
   a window of width `w_1`. Recursion on 1/u gives `w_{k} = (w_{k-1} − u_{k}L)/2`-type contraction,
   telescoping to `w_n ≤ u_nL` via `1/u_n = 2/u_{n-1}+1`. — by induction on the split depth.
5. **Extract the witness.** Two disjoint blocks with tree values within `u_nL` ⇒ a nonempty tree
   value `≤ u_nL` ⇒ `min R(A) ≤ u_nL` ⇒ (R-UV) `D ≤ u_nL`. — by step 2.
6. **Lower bound + answer.** Certified lower machinery gives `D ≥ u_nL` on the dyadic input; equal
   ⇒ `c(n) = 2^n/(2^{n+1}−1)`, verified `n=0,1,2` by certified brute force. — by existing lemmas.

## Key lemmas (claim + mechanism)
- **Disjoint-difference legality** — `|x−y|` for disjoint-support sub-tree values is a tree value,
  because the differencing tree rooting `T(P)` against `T(Q)` uses each piece once (no overlap, so
  no piece is reused — the one constraint RL imposes).
- **Balanced-split existence (GAP)** — a disjoint split `G₁⊔G₂` of the pieces with masses within
  `[L/2 − a₁, L/2 + a₁]` of each other exists and both groups have reachable windows overlapping to
  `≤ u_nL`, BECAUSE the deep gap `L/2 − a₁ > u_nL/2` forbids any single piece from being larger than
  the complementary group's whole reachable span (so no "unmatched giant" blocks the overlap — the
  exact structural reason the anchored walk failed: it never split off the giant).
- **Dyadic telescope** — window width contracts by the map `w ↦ (w − u_kL)/2` down the `n` split
  levels and reaches exactly `u_nL` (no constant slack), because `1/u_n = 2/u_{n-1}+1` is the fixed
  point of that contraction (this is where VALLEY-TIGHT's no-margin requirement is met — the
  recursion is exact, not a bounded multiple).

## Open gaps
- Step 4 window-overlap induction (the exact heart) — the balanced-split-existence lemma and the
  window contraction. This is the whole difficulty; everything else is certified or routine.
- Step 3 confirm ONE-REC actually yields `n` independent split levels for an arbitrary deep profile
  (not only for scale-aligned profiles).

## Cases to cover
- Deep interior `a₁ < L/2 − u_nL/2` (only open region).
- Base `n=1` (verify window ≤ u_1L directly).
- Degenerate: repeated pieces / an exact even cancellation giving value 0 (only helps; 0 ≤ u_nL).

## Watch out for
- **VALLEY-TIGHT (no margin):** any version of step 4 that loses a constant factor (window ≤ C·u_nL,
  C>1) is DEAD on arrival — the tight family `A^{(n)}` drives the ratio → 1. The telescope must land
  EXACTLY at `u_nL`. Gate this first.
- **Not the dead greedy recursion (R9):** the split is a balanced EXISTENCE split, not a greedy
  largest-first fold; do not degenerate it into "pair a₁ with a₂ and recurse on the tail" (that is
  the dead `u_{n-1}(L−a₁)`-target recursion). The two groups must each carry ~half the mass.
- **R-UV realizability check:** confirm a GENERAL tree value (not just a caterpillar) is realizable
  by Xiang in ≤ n cuts — R-UV certifies this, but the builder must cite the exact clause (ESF-2 was
  stated for caterpillars; RL/R-UV extends it to trees). If only caterpillars are n-cut-realizable,
  the target reverts to `μ_{n+1}` and this approach must route through the bridge (see
  `tree-target-bridge`).

## MANDATORY exact-Fraction pre-build gate (run FIRST, n=4,5,6, no floats)
Script sketch (use `fractions.Fraction`, NEVER float; per explorer finding 4 compute `μ_{n+1}` via
the FGR **dist-recursion** `μ_i=min(μ_{i-1}, dist(a_i,R_{i-1}))`, NOT "min positive of the set"):
1. `treeVals(S)` memoized over index-subsets: `treeVals({i})={a_i}`;
   `treeVals(S)={|x−y| : ∅≠P⊊S, Q=S∖P, x∈treeVals(P), y∈treeVals(Q)}`. `minR = min_{∅≠S} min treeVals(S)`.
2. For the hard families — `A^{(n)}={2^n,…,4,3,2}/(2^{n+1}+1)`, its inward-sliver perturbations
   `a₁ = L/2 − u_n/K`, the R18 witness `{1/3,13/40,13/40,1/120,1/120}` and the `{30,25,20,15,10}/100`
   family — verify `minR ≤ u_nL` (target soundness) AND, for the D&C mechanism, that SOME balanced
   disjoint split `G₁⊔G₂` (masses within `2a₁` of each other) has `min_{x∈T(G₁),y∈T(G₂)}|x−y| ≤ u_nL`.
3. **KILL CRITERION:** if the best balanced-split difference / `u_n` GROWS with n on the hard family
   (covering-radius signature, like the 9 dead mechanisms), the D&C window does not contract to `u_n`
   — report and STOP, no prose. If it stays `≤ 1` (ideally `→` the true `minR/u_n`), the mechanism is
   green and the difficulty is purely the existence proof of the good split.
