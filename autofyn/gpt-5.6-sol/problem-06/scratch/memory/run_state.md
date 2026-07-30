## Goal
Solve `imo-2026-06` with a complete rigorous prose proof accepted by the proof-reviewer. Metric: `results/imo-2026-06/current.md` has `## Status\nsolved`, a complete `## Full proof`, and proof-reviewer verdict APPROVE. Eval: `python - <<'PY'\nfrom pathlib import Path\np=Path('results/imo-2026-06/current.md')\nprint(p.read_text() if p.exists() else 'MISSING')\nr=Path('results/imo-2026-06/approaches/.ranking.json')\nprint(r.read_text() if r.exists() else 'NO_RANKING')\nPY`. Baseline: pending evaluation. Target: solved / APPROVE. Constraints: no web search, web fetch, curl, wget, or external solution lookup; consult both local `knowledge_base.md` and crux corpus; one whole-problem attempt per slug; all proof rigor rules in `CLAUDE.md`.

## Goal Updates

## Eval History
- Round 1 baseline: `results/imo-2026-06/current.md` MISSING; `results/imo-2026-06/approaches/.ranking.json` NO_RANKING. Status unsolved/no workspace. [baseline]
- Round 1 Goal Progress: `imo-2026-06`: **partial**. Verified static gcd-polar enumeration, exact-support realization/self-duality, an ordered disjoint witness below \(\mu(H)\), and finite-control \(\Rightarrow\) global periodic indexing. Remaining load-bearing gap: prove a finite controlling prime set exists. The proposed finite-anchor construction additionally fails in its alleged negative direction because \(B_A\cap A=\varnothing\) does not imply \(B_A\cap(H\cap P)=\varnothing\). Round-1 outcome recorded as `partial`; verdict `CHANGES REQUESTED`. [IMPROVED]
- Round 2 Goal Progress: **APPROVE / solved**, correctness 10/10, completeness and rigor 10/10, progress 10/10. The candidate proves the original statement for every permitted initial value \(a_1>1\), producing positive integers \(T,L\) with \(a_{n+T}=a_n+L\) for every positive integer \(n\). The marked-prime descent, both terminal cases, finite controller, and final order-preserving periodic enumeration were independently re-derived and verified. [BREAKTHROUGH]

## Rules
- NEVER: use web search, web fetch, curl, wget, or external solution lookup (explicit user constraint, round 1).
- ALWAYS: consult both `knowledge_base.md` and the crux corpus before building proofs (project requirement, round 1).
- ALWAYS: keep rival approaches genuinely different in framing and route, with each slug targeting the whole problem (project requirement, round 1).
- ALWAYS: check whether a witness disjoint from a finite trace is actually disjoint from the full set after enlarging the controlling universe (reviewer found this exact invalid inference, round 1).
- NEVER: infer finite control from one chosen positive witness per negative trace without proving both membership directions (the one-stage anchor construction failed, round 1).
- ALWAYS: derive indexed periodicity via the translation bijection on the half-line and count a half-open initial block (this correctly handles every n from 1, round 1).
- ALWAYS: in marked-prime support descent, prove the mark survives both witness selection and minimization using linkedness each time (omitting the second linkedness use leaves a real gap, round 2).
- NEVER: treat Cantor-cube closedness or pointwise finite rank as uniform finite control without a proved isolation or clopen lemma (compactness alone does not provide uniformity, round 2).

## State
### Done
- Initialized the fixed run goal for `imo-2026-06` and installed required scientific packages.
- Round 1 certified static gcd-polar enumeration, exact-support self-duality, ordered disjoint witnesses, and finite-control-to-global-periodicity.
- Round 2 scouted bounded-radical, compactness, and direct-arithmetic framings and ranked the resulting field.
- Completed the `finite-support-maximal-linked` approach by a marked-prime strict radical descent, uniformly bounding every prime in every minimal positive support.
- Proved finite control in both directions and obtained global indexed periodicity for every positive index.
- Proof-reviewer independently verified the complete proof, recorded a `verified-milestone`, certified three new lemmas, and updated `results/imo-2026-06/current.md` to `solved` with verdict APPROVE.

### Broken
- None. The round-1 finite-control gap is closed. The rejected compactness and direct-arithmetic outlines remain nonviable but are not needed.

### Next
- Goal achieved; no further proof work is required.
