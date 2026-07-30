## Goal

Solve problem `imo-2026-04` (Mulan's Triangle Game, combinatorics, difficulty_rating 7, difficulty_level "medium" — user explicitly requested this specific problem by id, overriding the repo's default "hard only" filter).

Statement: Shan-Yu and Mulan play a game. Fix angle θ, 0°<θ<180°, known to both. Shan-Yu picks a triangle T. Repeat: if T has an angle exactly θ, Mulan wins immediately. Otherwise Mulan picks a point P on the perimeter of T (not a vertex), cuts from P to the opposite vertex, splitting T into two triangles; Shan-Yu discards one, the other becomes the new T. For which real θ can Mulan guarantee victory in finitely many steps, no matter how Shan-Yu plays?

Task type: compute_and_prove, answer_type: characterization. Need to determine the exact set of θ and prove both directions (Mulan wins for those θ; Shan-Yu can survive forever for other θ).

Eval: `results/imo-2026-04/current.md` `## Status` field, reviewed each round by proof-reviewer via APPROVE/CHANGES REQUESTED/RETHINK. Goal reached when Status = solved with proof-reviewer APPROVE and a `## Full proof` section present (upper/lower bound both proven, answer verified).

Baseline (round 1): no work done — run_state.md and results/ were empty at start of round 2. Baseline Status: unsolved (no approach files exist).

Target: Status = solved, APPROVE verdict from proof-reviewer.

Constraint: Follow CLAUDE.md workflow (math-explorer -> proof-outliner -> outline-reviewer -> proof-builder -> proof-reviewer) despite this being a "medium" problem, since it's the one the user specifically asked for this run.

## Goal Updates

- Round 2 (2026-07-28): User message explicitly requested "solve the problem imo-2026-04". This is a medium-difficulty problem, outside the repo's normal "hard only" scope, but taken as the fixed target for this entire run per user instruction priority.

## Eval History

- Round 2: 3 math-explorers dispatched (gametheory, extremal, verify). First two produced conflicting conjectures (θ∈(0°,90°] vs θ=90/2^k dyadic); third explorer built an exact minimax/backward-induction solver and found the correct conjecture: **Mulan wins iff θ=180°/n for integer n≥2**, refuting both priors with concrete counterexamples.
- Round 2: proof-outliner produced 3 approaches (chip-double-force, budget-partition-dimension, three-distance-avoidance). outline-reviewer ranked them (chip-double-force 1531 > budget-partition-dimension 1500 > three-distance-avoidance 1469 initial Elo) and set build set = {chip-double-force, budget-partition-dimension}.
- Round 2: proof-builder on chip-double-force produced a COMPLETE two-directional proof (forward: explicit M1/M2 two-move state machine with Target/Shield/Growing bookkeeping, induction on n; converse: residue-mod-θ "clean triangle" invariant, Lemma A + Lemma B with correct constant a₀:=θ/√2). proof-builder on budget-partition-dimension independently derived the same converse mechanism but with a buggy Lemma B constant (a₀:=√2·θ, invalid >180° for θ≳127.28°).
- Round 2: proof-reviewer independently re-derived and re-simulated everything (3600-trial forward re-check, 300,000-trial Lemma A re-check, all 0 failures/counterexamples) and issued **APPROVE** for chip-double-force (Status: solved, certified) and CHANGES REQUESTED for budget-partition-dimension (bug found and documented). BREAKTHROUGH — problem fully solved in a single round from a cold start.

## Rules

- ALWAYS treat imo-2026-04 as the fixed problem for this run — do not switch to a "hard" problem even though CLAUDE.md's default scope is hard-only; the user explicitly named this problem (round 2).
- ALWAYS `pip install numpy scipy sympy` at start of session if not present — not preinstalled in this container (round 2).
- ALWAYS have explorers verify each other's conjectures with an exact backward-induction/minimax search rather than trusting a single greedy-simulation counterexample search — round 2's first two explorers both had conjectures refuted by a third explorer who built a real minimax solver; greedy/heuristic simulations can miss winning strategies and falsely suggest "escape forever".
- ALWAYS have the proof-reviewer independently re-implement and re-run builders' verification scripts rather than trusting reported trial counts — round 2 found budget-partition-dimension's Lemma B had a real bug (invalid angle for θ≳127.28°) that its own 200,000-trial claim didn't catch, because the trials likely didn't sample that θ range.
- NEVER assume "medium" difficulty means low effort — imo-2026-04 (difficulty_rating 7) still required the full explorer/outline/build/review pipeline with 3 explorers and a conjecture-refutation cycle before solving.

## State

### Done
- Round 2: Set up environment (numpy/scipy/sympy), created results/imo-2026-04/{approaches,lemmas}/ dirs, ran full pipeline (3 explorers -> outliner -> outline-reviewer -> 2 parallel builders -> reviewer). Problem imo-2026-04 is now SOLVED and APPROVED: results/imo-2026-04/current.md Status=solved with full proof (answer: Mulan wins iff θ=180°/n for integer n≥2). Certified lemmas promoted to results/imo-2026-04/lemmas/.

### Broken
(none)

### Next
- Goal achieved. If the run continues, consider polishing/cross-checking the solved proof, or the outline-reviewer could still run once more for population hygiene, but the core goal (solve imo-2026-04) is complete — ready for end_session.
