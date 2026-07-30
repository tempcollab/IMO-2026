## Goal

Solve problem `imo-2026-03` (IMO 2026 P3, combinatorics, difficulty 9, compute_and_prove, answer_type: expression).

Statement (short): stick of length 1; Liu Bang marks ≤n points, then Xiang Yu marks ≤n points (all distinct); cut at marks; players alternate claiming pieces, Liu Bang first, each maximizes own total length. Determine largest c = c(n) Liu Bang can guarantee.

- Metric: `results/imo-2026-03/current.md` `## Status` + approach ranking in `results/imo-2026-03/approaches/.ranking.json`.
- Eval: read those two files each round.
- Baseline (round 1): no workspace existed — Status unsolved, no approaches.
- Target: Status `solved` — explicit closed-form c(n), both directions proven (Liu Bang strategy achieving c AND Xiang Yu strategy capping at c), proof-reviewer APPROVE.
- Constraints: no web access; prose Markdown proofs; rigor rules in CLAUDE.md; one problem for the whole run.

## Goal Updates

- [2026-07-28 round 1] Initial user message: solve imo-2026-03, no web search/fetch/curl/wget, don't cheat.
- [2026-07-28 14:22] User: "do not use internet do not look up solutions" — reaffirmed; pass to all subagents.

## Eval History

- Round 1: Status partial. Conjectured c(n) = 2^n/(2^{n+1}−1). discrepancy-halving: lower bound Theorem L drafted; U(m) Cases 1, 2 (a₁>a₂), U(≤3) done; middle case open. tie-structure-variational: infra built, n=1 solved end-to-end. dyadic-recursion builder interrupted. IMPROVED.
- Round 2 (review of r1 builds + re-plan; builders never ran — round timed out): Lower bound c(n) ≥ 2^n/(2^{n+1}−1) PROVED and certified (`lemmas/ladder-resists.md`). 4 certified lemmas. Problem reduced to Claim U(m) middle case (a₁<2^{m−1}β, a₂<2^{m−2}β, m≥3) + a₁=a₂ tie sub-case. U(m) verified numerically m=3..5, 60 instances, 0 failures. dyadic-recursion-induction FOLDED (Elo-penalized, not deleted). Copy created: discrepancy-halving-bands. Elo: disc-halving 1547, bands 1501, dyadic 1480, tie-var 1472. Both reviewed slugs: CHANGES REQUESTED. IMPROVED (breakthrough on lower bound).
- Round 3: discrepancy-halving builder finished — claimed U(m) proved in full generality via Lemma B (balancing pigeonhole) + Lemma W (two-pile walk realizability), whole problem closed. bands + tie-var builders force-interrupted (stuck watchdog). No review ran. BREAKTHROUGH (pending verification).
- Round 4: proof-reviewer APPROVE. Status **solved**: c(n) = 2^n/(2^{n+1}−1). Lemma B re-derived from scratch; Lemma W independently re-implemented, 4,800 exact-arithmetic instances m=1..8 zero failures; lower bound re-attacked (Nelder–Mead, n=1..3 min Δ = u exactly); 3 lemma files certified (reduction-to-um, um-proof, um-easy-cases); record_outcome = verified-milestone. GOAL MET.

## Rules

- ALWAYS: pass "no internet, no looking up solutions" to every subagent prompt (user constraint, rounds 1+3).
- ALWAYS: keep numerics chunked with frequent prints; long unchunked computations killed a round-1 builder (round 1).
- NEVER: let builders re-prove certified lemmas — import `lemmas/greedy-claiming.md`, `threshold-identity.md`, `ladder-resists.md`, `tie-structure.md` (round 2).
- NEVER: retry recorded dead ends: parity-XOR top-rung induction; integrality of pinned replies; plain greedy match-or-bisect for U(m) (fails on (5,3,3,2)/13); C(m) slack invariant (round 2).
- ALWAYS: if adopting the tail-min strengthened invariant for U(m), re-prove ALL cases at the strengthened invariant (round 1).
- IF both twins bottom out on the same ladder-like stall (super-increasing/distinct-band) next round → shared-gap plateau: demand a genuinely foreign framing from the outliner (round 2 outline-reviewer warning).
- ALWAYS: check round N-1 reports at round start — a timed-out round leaves an unconsumed build set to execute directly (round 3).

## State

- Done: R1: workspace, 3 approaches, lower-bound draft. R2: lower bound certified, 4 shared lemmas, field ranked. R3: discrepancy-halving builder closed U(m) (Lemmas B + W). R4: proof-reviewer APPROVE — problem SOLVED, c(n) = 2^n/(2^{n+1}−1), current.md flipped to solved with Full proof, all lemmas certified.
- Broken: nothing.
- Next: nothing — run complete. end_session called round 4.
