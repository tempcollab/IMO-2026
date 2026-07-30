# Outline review — round 8, imo-2026-03

Source: `/tmp/round-8/proof-outliner.md`. Cross-checked against `current.md`,
`lemmas/parity-pair-anchor.md`, `lemmas/lemma-V-prime-free-coordinate.md`,
`lemmas/alternating-sum-toolkit.md`, `lemmas/partial-dom.md`, and
`universal-adversary-strategy.md`'s Claim PTBI section.

## recursive-embedding-induction — revise — APPROVE

Target: close Lemma PARITY-PAIR-ANCHOR/V'-GEN's two remaining sub-gaps (a)
partial-budget anchor-only ("M even") and (b) cross-piece tied free
coordinates, completing the tail-refined lower bound for `A_n`.

- Verified the outline's characterization of gap (a) against
  `lemmas/parity-pair-anchor.md` directly: the file's own "Remaining gap"
  section confirms the abstract parity statement is genuinely false
  (`c=(0,4)`, `n=2`) and that closure needs game-reachability, exactly as
  the outline states — not a mischaracterization.
- The new mechanism (Fact 1/2-style "no two distinct powers of 2 sum to a
  power of 2, so any anchor-exact split of an anchor value is realized by a
  binary subdivision tree") is a genuine, checkable number-theoretic fact,
  correctly stated: distinct powers of 2 never sum to a power of 2 (binary
  carry), while equal powers do (exact halving) — this is exactly the
  mechanism needed to justify "every reachable anchor-only configuration is
  a binary-tree leaf-multiset," not a hand-wave.
- Gap (b)'s mechanism (affine-in-each-tied-coordinate via the certified
  D-INSERT formula, then a local perturbation argument) is the same
  machinery that already closed Lemma FC (verified above in
  `lemma-V-prime-free-coordinate.md`, Step 4's convexity/endpoint-snap
  argument) — a legitimate, non-circular generalization pattern, not a new
  unverified black box.
- Watch-out (2) in the outline (extension-monotonicity is NOT assumed, and
  the file itself flags it only as an unproved "plausible lead," not
  invoked) is correctly self-policing — good discipline, keep it.
- Open gaps are honestly flagged as NOT yet proved (numeric evidence only,
  n≤4/n≤3) — no overclaiming.

No fatal issues. APPROVE.

## universal-adversary-strategy — revise — APPROVE

Target: prove Lemma BLOCK-RECURSE and close Claim PTBI (general upper bound
over arbitrary configs) via a fully recursive re-optimization of the
leftover residual, strictly generalizing certified PARTIAL-DOM/PARTIAL-DOM-
RESIDUAL.

- Cross-checked against `universal-adversary-strategy.md`'s existing Claim
  PTBI section (lines ~782-950): the file already documents that a naive
  scalar-IH induction fails algebraically and that a sharper,
  positionally-aware induction is needed — BLOCK-RECURSE is exactly that
  sharper mechanism (tracks the exact leftover multiset via the certified
  duplicated-block-cancels identity from Lemma PARTIAL-DOM, not just
  totals), consistent with the standing memory rule against pure
  scalar/aggregate-sums inductions.
- The "leftover always dominated, before and after further recursive
  refinement" mechanism is grounded in Lemma PARTIAL-DOM's own certified
  Step 1 (duplicated block's own alternating sum is 0, shifts the rest by
  an even amount) — a real mechanism, not asserted by fiat.
- Open gaps honestly flagged: BLOCK-RECURSE itself unproved (only numeric,
  m=3..9), the finite-candidate-menu inductive step unproved in closed
  form. The outline correctly warns the builder not to assume the leftover
  subproblem is solved non-recursively (a legitimate circularity risk it
  pre-empts rather than hides).
- Case coverage (odd/even m, base cases m=1,2, j=0 fallback to
  MULTI-HALVE/TAIL-SNIP/SANDWICH) is present and matches the file's own
  m=1,2 closure status.

No fatal issues. APPROVE.

## geometric-dominance-construction — advance — APPROVE

Target: same gap (b) (cross-piece tied free coordinates) as
recursive-embedding-induction, via direct slope computation on the
D-INSERT cell rather than tree-peeling induction.

- Per the standing round-5 memory rule ("two same-half rival approaches
  converge on the same crux sub-lemma via different mechanisms — approve
  both, flag coordination"), this is legitimate parallel exploration, not
  the single-gap trap: distinct mechanisms (explicit two-variable slope/
  sign case analysis vs. tree-peeling strong induction), both grounded in
  already-certified machinery (D-INSERT), with positive evidence the
  target lemma is true (n=2,3 exact-vertex data, large margin: D=3, 5/3 vs
  true min 1).
- The outline explicitly requires the two routes be reconciled if they
  disagree (line 213-216) — good, keeps this from silently producing two
  contradictory "proofs" of the same statement.
- This approach's overall target remains the whole lower-bound claim for
  `A_n` (not a fragment) — its unique remaining scope is exactly gap (b);
  Proposition K is already closed and correctly not re-attempted.

No fatal issues. APPROVE. Coordination note carried into the build set below.

## minimax-mixed-duality — retire (no build)

Correct call. Ranking shows `last_outcome: dead-end`, two consecutive
RETHINKs with the file's own honest self-assessment that the framing has
produced zero independent leverage and every construction collapses into
universal-adversary-strategy's mechanism. The round-8 explorer's candidate
new framing (Opening A / dynamic discount potential) was not numerically
gated before proposing it (explorer's own report: "I did not attempt this
proof"), and the outline gives a solid structural reason to expect it would
collapse to existing machinery (c(n) is not a pure geometric sequence in n,
so a fixed-rate telescoped bound can't reproduce it without re-deriving the
existing n-dependent recursion). Correctly not opened this round — avoids
forcing a low-quality diversity slot. Not registering a new slug for it.

## Diversity check

The three built approaches (recursive-embedding-induction,
universal-adversary-strategy, geometric-dominance-construction) now split
cleanly along the pre-established lower-bound/upper-bound structure (not a
single-gap trap, per the round-3 standing rule), and within the lower-bound
half, gap (b) is attacked by two genuinely different mechanisms per the
round-5 coordination rule. This is legitimate convergent narrowing near the
end of a long-running population, not field collapse: the remaining open
surface is now only 3 sharply-isolated technical gaps (lower-bound (a),
lower-bound (b), upper-bound PTBI), each with its own distinct required
argument, not one shared wall. No new diversity mandate needed this round.

## Ranking

Registered slugs are all pre-existing (no new slug to register this round —
recursive-embedding-induction, universal-adversary-strategy, and
geometric-dominance-construction all already in the population; no copy
requested by the outliner). Submitted 10 comparisons anchoring the newcomrs-
free field to last-round outcomes: the three live/approved slugs beat both
RETHINK'd approaches (minimax-mixed-duality, relaxed-adversary-transfer);
minimax-mixed-duality (real numeric output, 2nd RETHINK) still beats
majorization-smoothing (3rd confirmed structural dead end); relaxed-
adversary-transfer (clean rigorous negative result) beats
equalization-potential-bound (still-conditional, stagnant since round 1);
potential-averaging-bound (real feasibility-gate failure, not dead)
beats both majorization-smoothing and equalization-potential-bound but
loses to universal-adversary-strategy. Post-update Elo (best-first):
recursive-embedding-induction 1680, geometric-dominance-construction 1609,
universal-adversary-strategy 1551, relaxed-adversary-transfer 1497,
minimax-mixed-duality 1474, potential-averaging-bound 1453,
majorization-smoothing 1376, equalization-potential-bound 1360.

## Build-set coordination note (for the dispatched builders)

geometric-dominance-construction and recursive-embedding-induction are both
targeting gap (b) (cross-piece tied free coordinates) this round via
different mechanisms. Each builder should state its result independently;
if the two conclusions disagree, that must be flagged for reconciliation
before either is trusted (per the outline's own instruction) — do not let
one silently import the other's unverified claim this round.

build set: recursive-embedding-induction, universal-adversary-strategy, geometric-dominance-construction
