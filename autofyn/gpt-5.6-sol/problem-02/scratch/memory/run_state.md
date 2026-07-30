## Goal
Solve `imo-2026-02` with a complete rigorous prose proof certified APPROVE by the proof-reviewer.
Metric: reviewer status and approach population progress. Eval: inspect `results/imo-2026-02/current.md` `## Status` and `results/imo-2026-02/approaches/.ranking.json`; terminal target is `Status: solved` with a proof-reviewer APPROVE and a complete `## Full proof` satisfying all CLAUDE.md rigor rules.
Baseline: no pre-existing workspace or certified proof; initial status unsolved with an empty approach population.
Target: solved / APPROVE.
Constraints: attack only `imo-2026-02`; consult both `knowledge_base.md` and the crux corpus; no web search/fetch/curl/wget or external solution lookup; one whole-problem attempt per approach slug; rank every round.

## Goal Updates
- Round 2 user reaffirmed the same target and constraints: solve `imo-2026-02`, follow CLAUDE.md, and do not use web search/fetch/curl/wget or cheat. No goal change.

## Eval History
- Round 1 baseline: no pre-existing `results/imo-2026-02` workspace; status unsolved; approach population empty.
- Round 1 IMPROVED — proof-reviewer Goal Progress: `imo-2026-02` remains `partial`. Canonical ranking snapshot: `{"trig-circle-factorization":{"elo":1516.0,"expanded":1,"last_outcome":"partial","stale":true},"vector-perpendicular-bisector":{"elo":1484.0,"expanded":1,"last_outcome":"partial","stale":true}}`.
- Round 1 certified milestones: `circle-value-determinant` and `circumcentre-linear-certificate` lemmas admitted. Current best reduces the goal to the explicit dot-cross identity recorded in `current.md`; deriving it from the three branched angle constraints remains open.
- Round 2 BREAKTHROUGH — proof-reviewer Goal Progress: `imo-2026-02` advanced from `partial` to `solved`. Two independent complete proofs received APPROVE. The vector proof closes the prior dot-cross gap via a fully verified two-residual coefficient identity; the synthetic proof closes the midpoint-web gap via explicit radical-axis equations with both tangent degeneracies handled. Certified lemmas added: `two-residual-vector-certificate` and `four-circle-midpoint-web`. Ranker outcomes for round 2: `vector-perpendicular-bisector = verified-milestone`; `four-circle-midpoint-web = verified-milestone`.

## Rules
- NEVER: use web search, web fetch, curl, wget, or external solution lookup (user constraint, round 1).
- ALWAYS: consult both `knowledge_base.md` and the crux corpus when developing approaches (project requirement, round 1).
- ALWAYS: keep rival slugs as complete end-to-end attempts with genuinely different framings (project requirement, round 1).
- ALWAYS: recompute every claimed triangle angle directly from the ray-order table before trusting or factoring its sine-law equations (a builder introduced a false common angle and invalid incidence system, round 1).
- ALWAYS: retain ordinary-angle branch and positivity data when translating the hypotheses into vector, dot-cross, or rotation-scale constraints (right-angle and orientation branches otherwise get lost, round 1).
- NEVER: treat an unpresented symbolic-ideal computation or numerical experiment as a proof certificate; provide a hand-checkable identity (both live approaches stalled there, round 1).
- ALWAYS: seek a genuinely concrete synthetic framing next round if the analytic cancellation remains unclosed (outline reviewer warned the selected field shares an analytic circle-equation backbone, round 1).
- ALWAYS: when a synthetic midpoint-web claim is the hard burden, replace an asserted spiral-similarity composition with explicit circle/radical-axis equations and handle tangent coincidence branches (this produced the independent solved proof, round 2).
- ALWAYS: materialize reviewer-owned `current.md` in the primary workspace and verify its status after isolated-agent review (worktree isolation initially left the canonical tracker stale, round 2).

## State
### Done
- Round 1 environment prepared with numpy, scipy, and sympy.
- Round 1 created and ranked rival outlines and certified two partial analytic reductions.
- Round 2 scouted synthetic, corrected-trigonometric, and vector routes; mandatory outline ranking selected the vector and midpoint-web approaches.
- Completed and adversarially certified two independent proofs: `vector-perpendicular-bisector` and `four-circle-midpoint-web` both received APPROVE / solved.
- Certified shared lemmas `two-residual-vector-certificate.md` and `four-circle-midpoint-web.md` in addition to the round-1 lemmas.
- Canonical `current.md` now records `solved` and contains the complete four-circle midpoint-web proof.

### Broken
- `trig-circle-factorization` remains partial and is unnecessary for terminal success; its corrected elimination certificate was not built.

### Next
- Goal achieved. End the session with the solved workspace and both independent certified proofs.
