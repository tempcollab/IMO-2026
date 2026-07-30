# Outline Review — imo-2026-03 (round 1)

## Shared verifications (done this round, all pass)
- **Answer c(n)=2^n/(2^{n+1}−1)** and reduction Liu=(1+D)/2, D:=odd-rank−even-rank sum: confirmed. c=(1+u)/2 with u=1/(2^{n+1}−1) is arithmetic-correct.
- **Identity D = measure{ t : N(t) odd }** (N(t)=#pieces>t): confirmed on 5000 random multisets (exact). This is real, not just conjectured.
- **Toggle calculus** (a cut of s into s_1≥s_2 gives +1 on [0,s_2), −1 on [s_1,s)): checked by hand, correct; |ΔD|≤2s_2.
- **Dyadic lower bound**: Liu playing u·(1,2,4) for n=2, best Xiang response drives D to exactly 1/7. Confirmed. n=1 minimax D≈1/3 at Liu≈(1/3,2/3). Constructions are sound.
- **Upper bound exists**: true Xiang minimax over random 3-piece Liu partitions (n=2) is ≈0.14 ≤ u=0.1429 (grid-limited). So SOME adaptive Xiang strategy forces D≤u — the hard direction is genuinely provable.

## Reduction Lemma R (shared by all three)
Greedy "take largest" is optimal on a pure multiset (no adjacency constraint on claiming), Liu gets odd ranks. Standard, sound. Mechanism (exchange/backward induction) is correctly stated. Acceptable as a shared gap to be certified once.

## Common structural risk — the single wall
All three share the SAME hard difficulty: the **adaptive Xiang upper bound for an ARBITRARY Liu partition**. Their lower bounds are also essentially one argument (dyadic + superincreasing ⇒ one uncancelled odd block ≥ u). The three "engines" differ in bookkeeping (recursion / measure covering / explicit pairing) but attack the same wall. This is acceptable diversity for round 1, but flag for the orchestrator: **if all three stall on the upper bound for 3+ rounds, next round must seed a genuinely different framing (e.g. a direct adversary-strategy / LP-duality / weight-function argument), not a fourth bookkeeping variant.**

## parity-measure-potential — APPROVE (rank 1)
Framing sound and strongest-supported: two of its four gaps (B0 identity, B1 toggle intervals) are already VERIFIED here, mechanical to write up. The measure identity gives the cleanest handle on both bounds. Gaps B2 (lower: superincreasing caps odd-measure cancellation at u) and B3 (upper: n adaptive toggles cover all but u of the odd set) are the real KEY gaps — genuinely open but attackable, and flagged honestly. Watch item (overlapping toggle windows must be counted net, not gross) is the correct hazard. Build this.

## induction-peel — APPROVE (rank 2)
Recursion D(n)=D(n−1)/(2+D(n−1)) is a legitimate distinct engine (the "verified numerically" note only checks the arithmetic identity 1/D(n)=2/D(n−1)+1, which is trivially true — the CONTENT is the game reduction, correctly flagged as GAP A2). Not circular. The real risk, which the builder must confront head-on: the two-stage minimax may NOT cleanly factor through a CLAIM(n−1) sub-game because Xiang's cuts on the top piece and on the tail interact through the GLOBAL descending sort — so "reduce to an (n−1) instance on the residual length" needs a rigorous argument that the top block contributes exactly one uncancelled odd block and nothing leaks across the peel. A2 is the load-bearing lemma and its mechanism ("+2 arises because…") is currently asserted, not proven — the builder must pin down the exact adaptive cut rule (the file's candidates: cut a_1 so smaller fragment = a_2, or so larger = a_1−a_2). Dead-end "bisect largest" correctly excluded (fails Liu=(0.6,0.4), n=1). Build this.

## explicit-pairing-strategy — CHANGES REQUESTED (rank 3) — NOT in build set this round
Framing (explicit strategies + combinatorial injection) is a legitimate route and not circular, BUT its selling point — the explicit "greedy-merge" Xiang strategy — is **refuted as written**. Testing the literal rule ("take two largest unpaired fragments; cut the larger so its top fragment equals the smaller") on random n=2 Liu partitions gives worst-case D ≈ 0.95, versus target u = 1/7 ≈ 0.14. The naive reading leaves a huge dominant top fragment. This is exactly the DEAD END the file itself warns about, which means the approach does not currently contain a working algorithm — GAP C2 is not "prove this algorithm works" but "find the algorithm at all," identical hard content to A2/B3 with the least infrastructure and a broken candidate. Keep it registered in the population, but it needs the outliner to supply a corrected adaptive strategy before it's worth a builder's time. Do not build this round; revisit once A/B expose the right adaptive cut rule (which C can then borrow).

## Ranking recorded
parity-measure-potential (1532) > induction-peel (1499) > explicit-pairing-strategy (1469).

build set: parity-measure-potential, induction-peel
