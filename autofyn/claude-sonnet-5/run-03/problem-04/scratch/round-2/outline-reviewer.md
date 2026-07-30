# Outline review — imo-2026-04, round 2

Population was empty entering this round; all three approaches below are newly registered
(`chip-double-force`, `budget-partition-dimension`, `three-distance-avoidance`).

## Adversarial check performed

I did not just read the outline — I implemented the master-formula cut and simulated the
*exact* claimed strategy (Lemma 1 Double-Forcing + Lemma 2 Chip-Reduction + the induction's
chip-down phase) end to end in Python for n = 3..11, 200 random starting triangles each.

Key finding: **a naive reading of the induction cycles forever.** If you re-search "which case
applies" fresh at every move (e.g. re-run the Lemma-1 case analysis from scratch after each move,
or re-pick "whichever vertex is currently ≥ θ" to chip), the strategy loops indefinitely — I
reproduced this failure mode concretely (e.g. n=3, θ=60°, triangle
(49.71, 83.93, 46.36) cycles through the same 3 states forever under naive greedy chipping, and a
naive re-invocation of Lemma 1's case search after producing the `(n-1)θ` vertex also just
regenerates the same triangle). This is because the master formula's `child2 = (c, s-x1, b+x1)`
always adds `x1` back onto the *same slot* `b`, and greedily re-choosing "any angle ≥ θ" or
re-running the general case search loses track of which vertex is the intended chip target and
which is the "shielded" angle — you can end up perpetually re-splitting the same vertex pair
without progress.

However, once I implemented the strategy with **explicit, persistent bookkeeping** — i.e. after
Lemma 1 produces the `(n-1)θ` vertex, fix that specific vertex as the chip target and fix one of
the other two as the untouched "shield" and the other as the "growing" angle, and repeat the
single deterministic `x1=θ` chip *always on that same designated vertex* until it reaches `2θ`,
then do the final double-split — the strategy succeeds on **all 200/200 random trials for every
n = 3..11 tested** (n=2's base case needed separate handling, consistent with the outline treating
it specially). So:

**The underlying mathematical mechanism (Lemma 1, Lemma 2, and the chip-down induction) is
correct and I have independently confirmed it end-to-end**, not just spot-checked the two lemmas
in isolation. This is much stronger evidence than the outliner's report indicates.

**But the write-up gap is real and non-cosmetic**: the outline's prose ("iterate Lemma 1's own
mechanism directly," "iterating this single deterministic chip move exactly k-2 more times") does
not state the invariant that must be tracked (which vertex is chip target vs. shield vs. growing,
held fixed across iterations) precisely enough — a builder following the prose literally, as I
first did, produces an infinite loop, not a proof. This must be fixed with an explicit loop
invariant / induction on the chip-target's value, not just narrative "iterate."

## Per-approach verdicts

### chip-double-force — CHANGES REQUESTED
- Master formula, Lemma 1, Lemma 2: sound, algebra checked by hand and matches numeric
  verification (both the outliner's 20-triangle spot check and my own 200-triangle end-to-end
  simulation per n).
- The strong induction on n covering "all angles ≥ θ" vs "not all ≥ θ" is exhaustive (these two
  cases are complementary and both handled) — no missing case.
- **Gap to close (real, not fatal):** the inductive step's chip-down phase must be rewritten with
  an explicit, unambiguous invariant: name the three roles (chip-target vertex, shield angle,
  growing angle) at the moment Lemma 1 hands off, state that they persist across the `k-2`
  subsequent forced chip moves (shield literally untouched, growing absorbs `+θ` each move, target
  decreases by `θ` each move), and only then invoke "repeat until target = 2θ." Without this the
  proof is not verifiable as written (I confirmed a literal reading loops).
- **Converse gap:** correctly and honestly flagged as open by the outline. The pure/impure
  linear-independence mechanism is not obviously wrong, but (i) survival under the "P-angle
  targeting" move type and (ii) survival at all depths (not just depth 1) are unproven — this is
  the load-bearing remaining lemma and must not be papered over with "by induction, it follows."
- Verdict: technique is right, forward direction essentially done pending the bookkeeping fix
  above; converse is the real remaining work. Not a RETHINK — the mechanism is verified sound.

### budget-partition-dimension — CHANGES REQUESTED, but largely redundant with chip-double-force
- Forward-direction novelty (general `p,q` split, O(log n) moves): unverified, and per
  CLAUDE.md's guidance not needed for the problem (only finiteness required) — do not let a
  builder sink time proving a stronger-than-needed generalization instead of closing an actual
  gap. This part contributes no proof-strength diversity to the field; it's an optimization that
  doesn't matter.
- Converse (codimension/proper-subvariety framing): the outliner's own file admits "the two
  converse sketches are not fully independent and may need to be merged" — this is the same
  underlying fact as chip-double-force's genericity argument, repackaged. It is not a genuinely
  different mechanism, so building both converse gaps in parallel this round risks duplicated
  effort hitting the identical wall (the CLAUDE.md "single-gap trap" — two slugs converging on one
  gap isn't real diversity). If pursued, it should target something chip-double-force's argument
  does NOT yet have: a completed inductive step "W_d proper ⟹ W_{d+1} proper" stated with an
  actual finite enumeration of the polynomial constraints at each depth (not vague Baire-category
  language) — this could become a genuinely independent, rigorous alternative if someone commits
  to finishing it properly, rather than a second half-attempt at the same idea.
- Verdict: keep in the population for diversity/insurance, but not a priority build this round
  given the overlap with chip-double-force's converse gap.

### three-distance-avoidance — CHANGES REQUESTED, weak/underdeveloped, do the validity check first
- Per the outliner's own instruction I checked this: the "G-primitivity dichotomy" (does
  180/θ = n ∈ ℤ, i.e. is θ a generator of G = θℤ+180ℤ) is **definitionally equivalent to the
  already-conjectured characterization itself** (q=1 in lowest terms of 180/θ = p/q iff n is an
  integer) — restating the target dichotomy in group-theoretic language is not new content and
  does not yet supply any proof mechanism connecting "θ non-primitive in G" to "Shan-Yu can
  survive forever." The file's own "Gap" section admits this ("EVERYTHING past step 2" is open),
  and honestly flags the core obstacle: triangle angles don't literally live on a circle mod L,
  so the three-distance theorem's precondition (a genuine modular/circle structure) is not yet
  established — without that, the theorem cannot be invoked. I found no numeric or structural
  contradiction with the conjecture (θ=50° being a losing case is consistent, but trivially so,
  since it's consistent with literally any correct characterization), so this is not yet a dead
  end, but it currently has zero actionable proof content beyond the (correct but unhelpful)
  observation that q≥2 ⟺ non-winning-θ.
- Verdict: keep registered as a genuinely different *tool* for future diversity insurance, but do
  not spend builder time on it this round — there is nothing concrete to build yet. A future round
  should only revive it if someone can articulate an actual circle/modular structure on the
  reachable angle-values (e.g. values of one tracked coordinate under repeated chip moves, taken
  mod some period tied to θ) — until then it is not ready.

## Diversity assessment (for the orchestrator)

The field currently has **one forward-direction mechanism** shared/imported by all three
approaches (chip-double-force's Lemma 1 + Lemma 2), which is fine since I've now verified it is
correct — no need for a second forward construction. But the **converse direction has only one
real mechanism in progress** (chip-double-force's pure/impure genericity argument); the other two
approaches' converse framings are either an admitted repackaging of the same fact
(budget-partition-dimension) or currently empty of mechanism (three-distance-avoidance). This is a
mild version of the single-gap trap: if the pure/impure invariant genuinely fails to survive some
move type, the whole field currently has no independent backup. Recommend that if
chip-double-force's converse stalls next round, the next outliner pass should seek a converse
approach that is a *genuinely different framing* (e.g. an explicit potential/monovariant argument,
or a direct adversary strategy for Shan-Yu stated as an explicit invariant rather than a generic
starting point) rather than another repackaging of "genericity."

## Directives for this round's builders

- **chip-double-force**: (1) Rewrite the inductive step's chip-down phase with an explicit,
  named invariant (chip-target / shield / growing roles, each tracked across moves) — I verified
  numerically that this exact bookkeeping succeeds (0 failures / 200 trials, n=3..11); a vaguer
  "iterate the move" write-up is not acceptable and I confirmed it can loop forever if
  under-specified. (2) Push the converse: extend the pure/impure invariant proof to (i) the
  "P-angle targeting" move type and (ii) all depths, not just depth 1 — this is the one lemma that
  must go from sketch to proof for Status to move past `partial`.
- **budget-partition-dimension**: do NOT invest in the general p,q forward lemma (unneeded,
  unverified, low value). Only work the converse, and only if it can be made a genuinely
  independent, complete proof (the W_d-codimension induction finished rigorously with an explicit
  finite constraint enumeration) rather than a second half-sketch of chip-double-force's
  genericity idea.

build set: chip-double-force, budget-partition-dimension
