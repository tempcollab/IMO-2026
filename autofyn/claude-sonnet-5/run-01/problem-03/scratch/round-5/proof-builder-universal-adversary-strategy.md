# Build report — universal-adversary-strategy, round 5

Target this round (per dispatch): attempt the general-`n` upper bound for
arbitrary (non-geometric) Liu Bang configurations via a joint induction on
`(piece count, remaining mark budget)`, using the newly-found DOM boundary-
case budget-slack fact, and explicitly address the "near-tied top two"
case flagged by this round's explorer instead of skipping it.

## What was proved (all verified exactly, 0 mismatches, via `fractions.Fraction`)

1. **Lemma DOM-boundary-slack** — proved in full. When Lemma DOM's
   boundary case `p_1 = S` holds exactly, Xiang Yu can force
   `oddrank(B) = p_1` using only `k-1` marks instead of the generic `k`
   (splitting a piece into `j` parts always costs `j-1` marks; here the
   natural `k`-part split already sums exactly to `p_1`, so no residual
   `(k+1)`-th piece is needed). Verified by direct construction against
   2000 random boundary instances.

2. **Lemma SPLIT** (new, general) — a full generalization of the already-
   certified Lemma HALVE to splitting *any* single position `a_i` of a
   sorted list (not just the top `p_1`), whenever `a_i/2 \ge a_{i+1}`
   (no reordering). Gives an exact closed-form for the change in `oddrank`,
   with two cases by parity of `i`. Proved by the same rank-shift technique
   used in the certified Lemma HALVE proof; independently cross-checked by
   re-deriving Lemma HALVE exactly as the `i=1` special case. Verified
   exactly against 20,000 randomized trials, 0 mismatches.

3. **Lemma TAIL-SNIP** (corollary of Lemma SPLIT, `i=m`) — a genuinely new,
   **hypothesis-free** single-move identity: splitting the smallest piece
   always changes `oddrank` by exactly `∓a_m/2`, decreasing it iff the
   current piece-count `m` is odd. This is the first move in this
   approach's toolkit that needs no domination/ratio condition at all.

## The near-tied case: addressed directly, not skipped, and found to be sharper than previously known

The task instructed to treat the explorer's "near-tied top two, neither
DOM's nor HALVE's hypothesis fires, optimal move acts on a deeper tail
element" case as the sharpest remaining case and address it explicitly.
This was done: Lemma TAIL-SNIP (splitting the smallest/deepest element) is
exactly the natural formalization of the explorer's observed
"skip-to-the-tail" move. I tested it as a candidate general fix by
exact-`Fraction` search (3000 random configurations per `n=1..4`,
restricted to the region where neither DOM's nor HALVE's hypothesis
fires): **it fails**, with 773/3000 violations at `n=2` alone. Smallest
witness: `A=(4649/10000, 3042/10000, 2309/10000)`, giving TAIL-SNIP value
`11607/20000 = 0.58035 > c(2) = 4/7 ≈ 0.57143` (re-verified independently
in this report). A follow-up grid search over the full 2-mark budget on
this exact instance found the true optimum (`≈0.535 < c(2)`) requires
splitting **both** `p_1` and `p_2` simultaneously at jointly-optimized
non-half ratios — a strictly harder, coordinated multi-piece mechanism not
captured by any single-piece lemma (DOM, HALVE, or TAIL-SNIP) proved so
far.

This is a genuine sharpening of the open gap, not a resolution: the
near-tied case does not reduce to "split the deepest single element" as
the explorer's numeric example alone might have suggested — the true
obstruction is broader (coordinated multi-piece splitting), and this is
now documented with an exact witness for future rounds.

## Status

`partial`, unchanged at the top level (the upper bound over arbitrary
configurations is still open for general `n`), but with genuine new
content: three new fully-proved lemmas (DOM-boundary-slack, SPLIT,
TAIL-SNIP — all verified exactly), and a sharpened, honestly-reported
negative result narrowing exactly what mechanism the remaining gap needs
(coordinated ≥2-piece simultaneous splitting with non-half ratios, not any
single-piece rule). All positive claims and the counterexample were
independently re-verified with exact `Fraction` arithmetic in this report
before being written into the approach file — no computation was merely
asserted.

## File updated

`/home/agentuser/repo/results/imo-2026-03/approaches/universal-adversary-strategy.md`
— new "Approaches tried" entry, three new lemma sections (DOM-boundary-slack,
SPLIT, TAIL-SNIP) with full proofs, an updated "Dead ends" entry, and updated
"Full proof" / "Promotable lemmas" sections recommending all three new
lemmas for certification into `results/imo-2026-03/lemmas/`.
