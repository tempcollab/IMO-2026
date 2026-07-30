## Goal

Solve problem `imo-2026-04` (Mulan's triangle game — for which θ, 0°<θ<180°, can Mulan force a triangle with an angle exactly θ in finitely many steps?). Note: this problem's `difficulty_level` in problems.jsonl is "medium" (rating 7), not one of the 39 "hard" problems CLAUDE.md normally targets — but the user explicitly named this problem_id, so per priority rules we attack it anyway, using the same population-of-approaches workflow.

Metric: `results/imo-2026-04/current.md` `## Status` field (unsolved → partial → solved), verified by proof-reviewer APPROVE.
Eval: read `results/imo-2026-04/current.md` and `results/imo-2026-04/approaches/.ranking.json` each round.
Baseline (round 2 start): workspace just created, no approaches yet. Status: unsolved.
Target: Status = solved, with a complete rigorous proof (characterization of all valid θ, both directions: Mulan wins ⟹ θ satisfies condition, and construction/strategy showing Mulan wins for all θ satisfying condition).
Constraint: full rigor rules in CLAUDE.md (no hand-waving, no skipped cases, name all invoked theorems).

## Goal Updates

## Eval History
- Round 2: current.md Status: unsolved → partial. Established rigorous bound {180°/n : n integer ≥2} ⊆ S ⊆ (0°,90°] (S = set of θ Mulan can force). Elo: dyadic-scaffold 1546, binary-word-invariant 1502, corrected-genericity-bound 1500 (dead-end), full-interval-hypothesis 1453 (dead-end). BREAKTHROUGH: found the "shift move" primitive (a↦a-θ) which strictly enlarges the forceable family beyond the earlier dyadic-only conjecture; refuted a false `solved` claim (corrected-genericity-bound wrongly claimed S={180/((2^k+1)2^j)} exactly, missing the shift move in its closure operator) via reviewer hand-verifying an exact 8-move witness for θ=180/7°.

## Rules
- ALWAYS have the proof-reviewer independently hand/computer-verify (e.g. with sympy Rational arithmetic) any explicit numbered move-sequence witness claimed by a builder, move-by-move against the raw problem statement — don't trust a builder's own verification table (round 2: this caught a false `solved` claim).
- ALWAYS suspect a "necessity/impossibility" argument that closes over only a named finite set of move primitives (e.g. "halve + reflect", "halve + cross-transfer") of silently omitting a real legal move outside that set — check the closure operator's generator list against the FULL legal move space (any point P on the perimeter), not just the primitives the paper named (round 2, twice: corrected-genericity-bound and full-interval-hypothesis both had this exact bug, both missing the "shift move").
- ALWAYS treat a "computational witness found via restricted search but not hand-verified" as unresolved, not as ground truth to build on or as a search artifact to dismiss — round 2 showed it can go either way (180/7° witness turned out to be genuine, verified only after explicit hand construction).

## State
### Done (round 2)
- Set up workspace fresh (round 1 report was empty/missing): created results/imo-2026-04/{approaches,lemmas}/, installed numpy/scipy/sympy, established goal + baseline (imo-2026-04 is labeled "medium" in problems.jsonl, not one of the 39 "hard" targets, but user explicitly named it so it's being attacked anyway).
- 3 parallel math-explorers scouted the game (angle-invariant structure, adversary/obstruction side, top-down characterization guess) — surfaced a direct conflict (is θ=60° forceable or not) that drove the round.
- proof-outliner resolved the explorer conflict (confirmed the "transfer move" lemma valid, θ=60° IS forceable, refuting an over-claimed genericity impossibility) and opened 4 rival approaches: dyadic-scaffold, corrected-genericity-bound, binary-word-invariant, full-interval-hypothesis.
- outline-reviewer ranked all 4, build set = all 4.
- 4 parallel proof-builders built out each approach; binary-word-invariant discovered a new "shift move" primitive giving a strictly larger forceable family {180/n : n≥2} than the dyadic family.
- proof-reviewer adjudicated a 3-way contradiction over θ=180/7° forceability by independently hand-verifying the witness sequence; confirmed it genuine; found the precise missing-generator bug in the two "impossible" proofs; certified 5 reusable lemmas to lemmas/; updated current.md to partial with the combined bound and a clear next-step plan.

### Broken
- (none — all 4 approaches got a clear, correct verdict this round)

### Next
- Exact upper bound on S still open. Two live paths per current.md: (a) repair corrected-genericity-bound's junk-coefficient closure by adding the shift generator (a↦a-θ) to C(V) and re-derive fixed points — plausible since the shift-doesn't-cancel-junk fact is already certified in lemmas/transfer-and-shift-moves.md; (b) search for a θ genuinely outside {180/n} that is nonetheless forceable, which would refute (a) instead. Next round's outliner should open/advance approaches attacking these two paths, likely reusing dyadic-scaffold's and binary-word-invariant's certified lemmas rather than re-deriving from scratch.
