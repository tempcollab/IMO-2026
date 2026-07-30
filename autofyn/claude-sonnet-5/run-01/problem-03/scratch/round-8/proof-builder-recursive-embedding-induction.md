# Build report: recursive-embedding-induction (round 8)

## Task
Close the two remaining sub-gaps in the tail-refined lower bound for the
geometric configuration `A_n`: (a) partial-budget anchor-only strategies
(`M` even); (b) cross-piece tied free coordinates in Lemma V'-GEN.

## Result

**Gap (a): FULLY CLOSED**, and more strongly than requested (unconditional
for every mark budget, not just partial-budget `b<n`). New certified lemma
`lemmas/tree-bound-anchor.md` (Lemma TREE-BOUND), proved by reframing the
problem onto the actual binary-subdivision-tree reachability structure, per
the outline's instruction: since anchor values `t_i=2^{n-i}` are powers of
2 in a ratio-2 lattice, and no two *distinct* powers of 2 sum to a power of
2, every anchor-only split is forced to be an exact halving — so every
anchor-only strategy is exactly a choice of independent binary subdivision
trees for `P_1` (forced non-leaf root) and each `T_i` (leaf-or-split,
free). Proved a general "forest" sub-lemma (Sub-lemma ODD(m): for `(m,r)`
forests with odd top-level multiplicity `r`, `D≥τ_m`) by strong induction
on `m`, mirroring the certified Lemma PARITY-PAIR-GENERAL's Case A/B
mechanism but with the key new structural fact that every genuine tree
split produces children **in pairs**, so the remainder's top-level
multiplicity is *automatically* odd at every recursion level — this is
exactly the reachability information the abstract vector formalism lacked,
and it closes the induction with no extra hypothesis. Peeling `P_1`'s
forced root split reduces the whole problem to exactly the `(n,3)`-forest
case (`r=3`, always odd), giving Lemma TREE-BOUND for every `n≥1`.
Independently verified by exhaustive (not sampled) Python enumeration of
tree shapes — up to 175,760 distinct combinations at the largest case
checked — zero violations, matching the proof's prediction (`min D = t_n`)
exactly in every case tested (`m=1..4`, `r∈{1,3,5}`, and the full original
problem at `n=1..4`).

**Gap (b): genuine partial progress, NOT closed.** Attempted the outline's
perturbation/domination argument. Proved a new, general, certified-worthy
identity (**PAIR-CANCEL**: a genuine 2-way cross-tie's net contribution to
`D` is exactly `0`, regardless of the tied value — direct consequence of
the certified single-block alternating-sum fact). Also computed the exact
slope/kink structure via two applications of the certified Lemma D-INSERT,
finding a clean dichotomy: breaking the tie strictly decreases `D` when a
certain rank parity `ρ` is even, but strictly increases `D` (along the
natural symmetric perturbation) when `ρ` is odd. Identified precisely why
this does not close the case: if `x` is its piece's *sole* free coordinate
(everything else pinned at anchors), `x`'s value is not actually a free
continuous parameter — it's rigidly determined by the piece's own sum
constraint — so the two-variable perturbation isn't a genuinely feasible
move in the discrete game without a separate discrete-move argument (in
the spirit of gap (a)'s tree-peeling, or via bounding the PAIR-CANCEL
identity's `D(B'')` term, neither of which was completed this round). This
is honestly reported as open, not papered over.

## Status
`partial` (unchanged at the file level, since gap (b) — and the
out-of-scope general upper bound — remain), but the open surface has
shrunk: of the two sub-gaps this round targeted, one (gap a) is now a
complete, certified theorem, and the other (gap b) has substantial new
certified partial machinery (PAIR-CANCEL) plus a precisely-identified
remaining obstruction, rather than an unattempted plan.

## Files touched
- `results/imo-2026-03/approaches/recursive-embedding-induction.md` —
  updated Status header, added round-8 "Approaches tried" entry, new
  "Round 8" section with full detail on both gaps, updated "Full proof"
  placeholder text, and two new "Promotable lemmas" entries.
- `results/imo-2026-03/lemmas/tree-bound-anchor.md` — new file, full proof
  of Lemma TREE-BOUND (gap (a), fully closed).

## Recommendation for reviewer
Certify `lemmas/tree-bound-anchor.md` (Lemma TREE-BOUND) — it is complete
and independently verified. The PAIR-CANCEL identity (stated in the
approach file's "Round 8" and "Promotable lemmas" sections, not yet
spun out to its own lemma file since it doesn't close anything on its
own) could be certified as a small reusable fact if useful to whichever
approach next attacks gap (b) — reconcile against
`geometric-dominance-construction`'s parallel round-8 attempt on the same
gap (b), per the outline-reviewer's coordination note, before treating
either as settled.
