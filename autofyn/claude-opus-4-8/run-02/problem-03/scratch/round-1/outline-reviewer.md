# Outline review — imo-2026-03 (IMO 2026 P3), round 1

## Independent checks I ran (before judging)

- **Target value confirmed.** Grid brute-force of the full game (Liu ≤n marks, then Xiang
  ≤n marks, then greedy claiming) gives c(1)=2/3 (grids K=30,60) and c(2)=4/7 (grids
  K=28,42, both divisible by 7). Matches c(n)=2^n/(2^{n+1}−1). The whole field targets the
  right answer.
- **Shared Lemma G confirmed.** On 3000 random multisets (size 1–7), the true alternating
  minimax value equals the odd-rank sum b_1+b_3+… exactly (0 mismatches). The greedy-claim
  spine every approach imports is sound. This is the classical alternating-selection result;
  it will still need a written exchange/induction proof, but it is TRUE, so it is not a
  single-gap trap that sinks the field.
- **Discrepancy identity is algebra.** Liu=(1+D)/2 follows from Liu=odd-rank sum, Σb=1.
  And (1+u)/2 = 2^n/(2^{n+1}−1) with u=1/(2^{n+1}−1) checks out, so "D*=u" is a faithful
  restatement, not a new assumption.

Conclusion on the spine: **the shared base is solid**, and the three approaches genuinely
diverge on the true crux (the UPPER bound / non-myopic Xiang), attacking it by an adaptive
strategy vs. a one-cut recursion vs. a dual certificate. This is real framing diversity, not
one idea three times. Good field.

---

## dyadic-discrepancy — APPROVE

Most concrete and most honest. Spine verified above. Lower bound (dyadic 1:2:…:2^n, D≥u by
domination) is numerically tight and the domination mechanism (g_k=2^k u exceeds the sum
(2^k−1)u of all smaller pieces; n cuts can't cancel n+1 levels) is a real, stateable argument
— GAP L looks closable. The upper bound is correctly flagged as THE hard gap, and crucially
this approach **does not rely on the refuted "bisect n largest" rule** — it explicitly rules
it out and records the correct n=1 threshold strategy (bisect if p≤1/3 else pin the median).

Issues to close while building (do not block the build):
- **GAP U is the crux and is not yet a mechanism** — "design Xiang's cuts so the sorted
  multiset pairs up" is still a goal, not an argument. The builder must produce an actual
  adaptive rule generalizing the n=1 threshold, valid for ANY Liu partition (including
  partitions with ties and with <n+1 parts). This is where the round's real work is.
- **Lemma G optimality upper half** (no move beats greedy) with **ties** — handle carefully.

## induction-recursion — APPROVE

Legitimately different wall (size-reduction map, not endgame tier-counting). Recursion
T_n=2T_{n−1}/(2T_{n−1}+1) verified algebraically; the closed form solves it. Self-consistency
checks out: the top dyadic piece has size exactly 2^n u = c(n) > 1/2, so it dominates and Liu
claims it first, and the residual (2^n−1)u is exactly the scaled (n−1) dyadic instance. The
lower half (Liu prepends a dominating top piece) is plausible.

Issues to close (do not block the build, but the upper half is the risk):
- **Upper half decoupling is the load-bearing, under-justified step.** "Xiang spends one cut
  to neutralize Liu's largest piece so the rest is an (n−1)-instance" must be exact over ALL
  Xiang responses AND must handle the case where **Liu's partition has NO dominating piece**
  (e.g. several near-equal large pieces). There the "Liu claims the top piece first, then an
  (n−1)-subgame proceeds" story breaks because claims interleave across the two blocks — the
  residual is not cleanly an (n−1)-game. The builder must either prove Liu's optimum always
  presents a >1/2 piece (so a non-dominating partition is suboptimal for Liu) or bound the
  interleaved case directly. Flag this as the primary open gap for this slug.
- Confirm the recursion is between minimax *values* (both halves are inequalities on c(n)),
  and that Liu marking <n points cannot beat n marks.

## potential-certificate — CHANGES REQUESTED (kept for diversity, lowest-ranked)

Valuable as a third, genuinely different framing (dual witness, no adversary casework), and
the outliner honestly flags it "lives or dies on finding the right w." I am keeping it in the
build set for framing diversity, but with a hard structural caution and a mandatory gate,
because it has a real risk of being a plausible-looking dead end:

- **Separability objection (the likely fatal issue).** The outline pins the certificate to a
  *separable* potential Φ = Σ_pieces w(piece) and claims "odd-rank sum is monotone in Φ."
  The odd-rank sum is a **pairing/ordering functional** of the sorted multiset — two multisets
  with identical Σw(piece) can have different odd-rank sums — so a separable per-piece
  potential generically cannot control it. A working certificate here almost certainly must be
  **order-aware / non-separable** (weight depends on rank or on the sorted profile), which is a
  different and heavier object than the outline currently commits to.
- **Mandatory gate before writing any proof prose:** the builder must first *numerically*
  exhibit a single w (or order-aware Φ) that certifies BOTH bounds on n=1 AND n=2. If no such
  object exists (as the separability objection suggests for the separable form), degrade
  immediately to: use the certificate for the UPPER bound only and **import
  dyadic-discrepancy's lower bound**, or report the route as unviable. Do not spend the round
  writing a proof around an unverified w.

No approach secretly reuses the refuted "bisect n largest" universal strategy — I checked each.

---

## Ranking (Elo after this round)

1. dyadic-discrepancy — 1531 (most concrete, spine verified, lower bound near-closed, honest
   about the upper-bound crux; does not use the refuted rule)
2. induction-recursion — 1500 (sound standard technique; extra risk in the no-dominating-piece
   decoupling case)
3. potential-certificate — 1469 (distinct and useful for diversity, but separable-potential
   framing is structurally suspect; gated on an early numeric existence check)

## Field-level note for the orchestrator

The single true wall is the **upper bound (non-myopic Xiang)**; all three attack it differently
so they should not all die on it. If two of the three stall on GAP U in a later round, that is
the signal to seed a fourth framing far from these (e.g. a direct extremal/smoothing argument on
Liu's partition, or a fractional/LP relaxation of the cut game) rather than another variation.

build set: dyadic-discrepancy, induction-recursion, potential-certificate
