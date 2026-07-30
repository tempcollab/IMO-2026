## imo-2026-03

universal-adversary-strategy: revise
Target: Claim PTBI's Case C (`p_1 < Σ(A)/2`) for general `m≥4` — the ONLY
remaining gap for the whole problem (the entire lower bound and Case
A/B/m=3 of the upper bound are fully proven and certified; do not touch).
Technique: strong induction on piece-count `m` via an adaptive finite
move-menu (peel+halve / PARTIAL-DOM maximal-prefix match / budget-capped
nested TAIL-SNIP), building on certified Lemma PAIR-VALUE, Lemma
BLOCK-RECURSE, Lemma THRESHOLD-REDUCTION.
Skeleton (full detail written into
`results/imo-2026-03/approaches/universal-adversary-strategy.md`, section
"Round 12 plan — Candidate 5: budget-capped TAIL-SNIP recursion"):
  1. Formalize Candidate 5 exactly: `solve(A,budget)` = min of
     {peel+halve+recurse(same budget), PARTIAL-DOM-match+recurse(budget-1
     on leftover), TAIL-SNIP+recurse(budget-1) when |A| odd and budget>0},
     top-level entry `solve_full(A) := solve(A, budget=1)`.
  2. **MANDATORY GATE, run BEFORE any proof attempt**: adversarially
     stress-test Candidate 5 with `scipy.optimize.differential_evolution`
     (or an equivalent global optimizer) minimizing `target - value`
     over the Case-C simplex, for m=4..12+ — the same method that found
     the plain-menu's m=8 counterexample. Rationalize any near-zero
     margin to exact `Fraction` before trusting the sign. If budget=1
     fails, also test budget=2 before giving up on the mechanism.
  3a. IF the gate is passed: prove well-foundedness of the recursion
     (measure = lexicographic (|A|, budget), budget strictly decreases
     on every TAIL-SNIP use and is threaded — not reset — through every
     recursive call including the halve branch); prove each move's mark
     count telescopes to ≤ m-1 total (do not assume — verify explicitly,
     mirroring THRESHOLD-REDUCTION's existing telescoping); prove the
     new load-bearing claim, Lemma BUDGET-SUFFICES ("budget=1, or
     whatever constant the gate confirms, is always enough to beat
     c(m-1)Σ once Move 1+2 alone fail") — attempt via isolating why
     near-uniform witnesses need exactly one nested snip and whether
     that stacks boundedly; consider whether crux aimo-0063's
     Hall-deficient-set-deletion technique (iteratively remove a
     Hall-violating donor/target set and its neighborhood) is needed to
     make the general donor/subset-match step rigorous rather than ad
     hoc greedy-prefix.
  3b. IF the gate finds a counterexample: report it honestly (exact
     Fraction, m, A, target, value, margin) as CHANGES REQUESTED — do
     not force a patch without re-gating the patch.
Key lemmas (claim + mechanism):
  - Lemma PAIR-VALUE (certified) — matching-into-tied-pairs decomposition
    gives oddrank = Σ(matched) + oddrank(unmatched), unconditionally;
    algebraic backbone of every move's value formula.
  - Lemma BLOCK-RECURSE (certified) — PARTIAL-DOM maximal-prefix match is
    legal/correct at any recursion depth, any tail shape.
  - Lemma THRESHOLD-REDUCTION (certified) — c(k-1)=c(k)/(2(1-c(k))),
    supplies the target and the telescoping tool for the budget-indexed
    induction.
  - NEW Lemma BUDGET-SUFFICES (open, the actual mathematical content of
    Case C) — a small constant TAIL-SNIP budget threaded one level into
    PARTIAL-DOM's leftover always suffices; mechanism not yet known,
    only empirically supported (523 random trials, both hard witnesses,
    m=8 counterexample to the budget-0 menu closed exactly). This is
    what the builder must actually prove (after the gate), not just
    verify numerically again.
Open gaps: whole Case C for general m≥4 remains open pending the gate
result; if gate passes, Lemma BUDGET-SUFFICES's general proof is the gap.
Cases to cover: none beyond the induction's own case split (peel-wins /
partial-dom-wins / tail-snip-wins) — the induction itself must cover
every A in Case C, no separate enumeration needed.
Watch out for: (a) do not skip the mandatory gate — Candidate 3 (the
prior, un-capped menu) looked universal against 3600+ random trials and
2 hard witnesses before an optimizer found its one counterexample at
m=8; a modest random/witness sample is not sufficient evidence here.
(b) well-foundedness bug risk: an earlier unrestricted version (no
budget cap) was confirmed genuinely non-terminating (2M+ calls, no
termination on an m=9 instance) — the budget parameter must be threaded
through every recursive branch, not silently reset. (c) the winning fix
for m=8 is NOT non-contiguous subset matching — that was tested and
refuted by exhaustive 127-subset brute force; don't re-litigate it.

geometric-dominance-construction: no new work (per dispatch — lower
bound fully closed, no remaining target found this round; leave file
untouched, still live in the population as a certified cross-check).

recursive-embedding-induction: no new work (per dispatch — lower bound
fully closed, no remaining target found this round; leave file
untouched, still live in the population as the primary lower-bound
closure).

No new approach slug opened this round. Rationale (per
math-explorer-altframing's dedicated go/no-go check, 4th such check in
rounds 7/9/10/11 plus this round): every genuinely-new-framing candidate
tried in this run's history (concavity/smoothing on A, LP/mixed
duality, secondary-extremality statistic, ∞-mark relaxation) is a
*structurally* dead mechanism (convex kink, collapses into the same
casework, value-equivalent statistic, wrong-direction inequality
respectively) — not a stalled numeric search that a fresh framing would
unstick. The one new, not-yet-tried lever found this round
(Hall-deficient-set-deletion from crux aimo-0063) is a refinement
*within* the existing matching/adaptive-construction framing, correctly
folded into universal-adversary-strategy's Step 3a rather than spun out
as a competing slug — spinning it out would just be the same wall one
step later (CLAUDE.md's reframe-vs-bypass distinction). The field is not
collapsing to one line in an unhealthy sense: it's converging because
the lower bound is genuinely finished and only one precise gap remains
for the whole problem: this round's job is to sharpen that one gap's
attack, not manufacture artificial diversity where the terrain has
already ruled out the alternatives.

Build set: universal-adversary-strategy
