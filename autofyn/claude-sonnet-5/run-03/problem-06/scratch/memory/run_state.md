## Goal

Solve hard problem `imo-2026-06` (number theory, difficulty_rating 9) from problems.jsonl.

Statement: Let a_1, a_2, a_3, ... be an infinite sequence of positive integers greater than 1.
Suppose that for all positive integers n, a_{n+1} is the smallest positive integer greater than
a_n such that gcd(a_{n+1}, a_i) > 1 for every i=1,...,n. Prove that there exist positive integers
T and L such that a_{n+T} = a_n + L for every positive integer n (eventual periodicity of the
sequence, up to shift L, with period T).

Metric: proof-reviewer verdict on results/imo-2026-06/current.md `## Status`.
Eval command: read results/imo-2026-06/current.md `## Status` field (solved/partial/unsolved),
cross-checked against results/imo-2026-06/approaches/.ranking.json.
Baseline: unsolved (no work started, round 1).
Target: solved — Status: solved with a complete, gapless proof, proof-reviewer APPROVE.
Constraint: one problem for the whole run; never re-attempt if already solved; population of
rival approaches kept in results/imo-2026-06/approaches/.

## Goal Updates

## STATUS: SOLVED (round 6). Do not re-attempt.

`results/imo-2026-06/current.md` `## Status` = `solved`, with a complete `## Full proof` section,
proof-reviewer APPROVE (round 6, verified independently from scratch with extensive computational
corroboration, no gap found). If a future run touches this problem again, read current.md first —
this satisfies CLAUDE.md's "never re-attempt a solved problem" rule.

## Eval History

- Round 1: Status unsolved → partial. 3 approaches built: growth-bound-density (partial),
  core-signature-pigeonhole (partial — reduced to one open lemma "No-Escape"),
  monovariant-telescoping (RETHINK — |Q|<∞ proved FALSE). 5 lemmas certified. IMPROVED.
- Round 2: Status stays partial. 3 approaches: antichain-signature-closure (revise, collapses
  sufficiency+necessity into "Antichain Stabilization", partial), dilworth-antichain-bound (new
  "P-Confinement ⟹ theorem" reduction, PC provably implies Antichain Stabilization, partial),
  dense-signature-vanishing (crux aimo-0680 transplant REFUTED computationally, RETHINK). 3 new
  lemmas certified. IMPROVED (gap narrowed/unified, a1=2310 shows non-monotone antichain growth
  then Absorption collapse).
- Round 3: math-explorers (absorption-recurrence lens, fresh-framing lens) + proof-outliner ran;
  no outline-reviewer/builder/reviewer completed this round (session continued into round 4).
- Round 4: outline-reviewer ran. **Major result**: even-a_1 case fully solved
  (absorption-recurrence-even-case, certified lemmas/even-persistence.md) — a_n=a_1+2(n-1)
  unconditionally for 2|a_1. Entire remaining content narrowed to odd-a_1 case. Status stays
  partial overall.
- Round 5: 3 math-explorers + proof-outliner + outline-reviewer ran, build set emitted
  (leftover-witness-confinement, antichain-signature-closure, global-smooth-density-contradiction)
  and all 3 proof-builders completed — but session was interrupted (user stop) before the
  proof-reviewer step ran; current.md was not updated for round 5's builds until round 6.
- Round 6: (a) Ran the pending proof-reviewer over round 5's 3 builds: all CHANGES REQUESTED
  (partial) — genuine progress (2 new certified lemmas: antichain-stabilization-implies-theorem,
  growth-event-decomposition; citation-hygiene gap fully closed two independent ways) but all
  three independently converge onto ONE equivalent open combinatorial claim ("Step 6" / Antichain
  Stabilization / Type B finiteness / PC), a confirmed 5-round plateau on the same
  antichain-of-prime-sets object. (b) Per the plateau-breaking rule, dispatched 2 fresh
  math-explorers: one attacking Step 6/realizability directly, one scouting genuinely new
  non-antichain framings. Key find: imo-2026-06's recursion is literally crux aimo-0030 (IMO 2022
  P3, "Game of Numbers")'s "good numbers" construction; the official solution's purification +
  strong-downward-induction technique, applied GLOBALLY with threshold a_1, was untested (a prior
  LOCAL per-step transplant had been killed). (c) proof-outliner fielded 3 approaches:
  global-signature-purification (new, the global transplant), leftover-witness-confinement
  (revise, new Coincidence Lemma attempt), gcd-pigeonhole-omega-induction (new, aimo-0421
  transplant). (d) outline-reviewer approved all 3 as build set. (e) 3 proof-builders ran in
  parallel: global-signature-purification came back **Status: solved** — a complete, self-
  contained proof for ALL a_1≥2 (both parities), entirely independent of the antichain/PC/Step-6
  machinery; leftover-witness-confinement and gcd-pigeonhole-omega-induction each produced honest
  negative results (Coincidence Lemma refuted; Reduction Lemma found structurally obstructed).
  (f) proof-reviewer independently re-derived every step of global-signature-purification from
  scratch (Correspondence Lemma, Purification Lemma, Signature Determinacy Theorem, Periodic-
  Enumeration Lemma), ran extensive computational corroboration (a1∈{2..60}, 16553 random
  purification trials, direct periodicity checks for a1=9 (T=70,L=210) and a1=15
  (T=8008,L=30030)), found NO gap. **APPROVE. current.md Status set to solved, Full proof written
  in.** Lemmas certified: global-signature-purification.md, proper-subset-pigeonhole-dichotomy.md.
  BREAKTHROUGH — problem SOLVED after 6 rounds, via a fresh top-level framing that bypassed the
  entire antichain plateau rather than closing it.

## Rules

- ALWAYS test any "the active/relevant set is finite" premise computationally before a builder
  builds on it — caught S=primes(a_1) too coarse and |Q|<∞ false, round 1.
- ALWAYS phrase the central invariant as "does a large prime ever become the necessary/unique
  witness in a bounded window," never "does a large prime recur" — the latter is unavoidable and
  a dead end (round 1).
- The crux problem aimo-0030 (= aimo-0678, IMO 2022 P3 "Game of Numbers") is the DIRECT source of
  imo-2026-06's recursion ("good numbers" construction) — its official solution's purification +
  strong-downward-induction technique, applied GLOBALLY with threshold a_1 (not locally per-step,
  which fails), is what ultimately solved the problem in round 6. If this file is ever consulted
  again for a related problem, check this transplant first.
- aimo-0680 (IMO SL 2015 N4) transplant is REFUTED (bounded-difference-quotient pigeonhole,
  round 2) — do not reattempt.
- The naive O(log a_n)-per-step "witness-debt charging" argument is PROVEN not to work (budget is
  n-dependent) — do not reattempt that exact shape (round 2).
- A LOCAL per-step transplant of aimo-0030's purification technique was tried and killed (floor-
  mismatch reason) before round 6 — only the GLOBAL version (threshold fixed at a_1, not the
  current floor) works. If ever revisiting this proof family, preserve that distinction.
- Reusable certified lemmas in results/imo-2026-06/lemmas/ (12+ files) — see the directory;
  superseded by global-signature-purification.md's self-contained proof but kept as historical
  record of the antichain-family plateau (5 rounds) that was ultimately bypassed, not solved.
- The antichain-of-minimal-prime-sets framing (growth-bound-density, core-signature-pigeonhole,
  antichain-signature-closure, dilworth-antichain-bound, leftover-witness-confinement,
  global-smooth-density-contradiction) is a REAL, well-developed partial-progress family but never
  closed its own core claim (Antichain Stabilization/PC/Step 6) — the eventual solution came from
  an entirely different framing (good-number purification), confirming CLAUDE.md's plateau-
  breaking guidance: after 3+ rounds stuck on one shared gap, prioritize a genuinely different
  top-level framing over another technique variant on the same object.

## State

### Done
- Round 1: scaffolded results/imo-2026-06/, 3 explorers, outliner, outline-reviewer, 3 builders,
  1 reviewer. Reduced theorem to one open "No-Escape" lemma; 5 lemmas certified.
- Round 2: 2 explorers, outliner, outline-reviewer, 3 builders, 1 reviewer. Unified No-Escape into
  "Antichain Stabilization"/PC; 3 new lemmas certified; aimo-0680 transplant refuted.
- Round 3: 2 explorers + outliner ran (session continued to round 4 for outline-reviewer/build).
- Round 4: outline-reviewer + build/review completed. Even-a_1 case fully solved unconditionally
  (absorption-recurrence-even-case). Odd case isolated as sole remaining content.
- Round 5: 3 explorers, outliner, outline-reviewer, 3 builders all completed (build set:
  leftover-witness-confinement, antichain-signature-closure, global-smooth-density-contradiction);
  session interrupted (user stop) before proof-reviewer ran.
- Round 6: Ran the pending round-5 proof-reviewer (all 3 CHANGES REQUESTED/partial, 2 new certified
  lemmas, confirmed 5-round antichain plateau). Dispatched 2 fresh explorers per plateau-breaking
  rule → found the aimo-0030 global-purification transplant lead. proof-outliner fielded 3
  approaches → outline-reviewer approved build set of 3 → 3 proof-builders ran in parallel →
  global-signature-purification returned Status: solved. proof-reviewer independently verified
  from scratch with extensive computation, found no gap, APPROVED. current.md Status = solved,
  Full proof written in. **PROBLEM SOLVED.**

### Broken
(none — pure-math run, no build/eval infra)

### Next
- Problem imo-2026-06 is SOLVED. Per CLAUDE.md: "Never re-attempt a solved problem." If this run
  continues, there is no further work needed on imo-2026-06 — end_session should be called (goal
  achieved, all APPROVE). If a future run is scoped to a different problem, this file's Goal
  section should be replaced entirely for the new problem.
