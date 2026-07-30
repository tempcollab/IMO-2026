# Outline Review — Round 6 — IMO 2026 P3 (`imo-2026-03`)

## Verification summary (computationally confirmed)

1. **Halving lemma (`halving-always-a-nplus1`):** VERIFIED 0/20000 exact-Fraction trials (n=2..6, strictly-decreasing m=n+1 configs). The parity/grouping proof is SOUND: each a_i/2 is pairwise distinct (strictly-decreasing ⟹), so each forms a size-2 (even) block contributing 0; a_{n+1} is the unique odd-multiplicity value (count 1+2k, k∈{0,1}); all even blocks above it ⟹ it starts at position 1+2·(#blocks above) = odd ⟹ contributes +a_{n+1}. This works WITHOUT bottom-dominance (the block-grouping argument handles any sorted order). **This is a real certifiable milestone.** It generalizes `bottom-dominant-halving` and drops its hypothesis. It closes a_{n+1}≤1/D_n for ALL n unconditionally.

2. **Tower unique-max:** VERIFIED n=2 (T_2 gives D*=1/7; non-tower (5,2,1)/8 gives D*=1/8 < 1/7). Consistent with the explorer's claim.

3. **FATAL FLAW in O1 (split-bottom + exact-pair-rest):** For the compressed config (5,3,2)/10 (n=2, a_3=1/5 > 1/7=1/D_2), I checked ALL x ∈ (0, 1/7] and ALL possible split targets/pairing patterns analytically. **Exact pairing into equal pairs is IMPOSSIBLE for every x and every split choice.** The obstruction is structural: the rest {0.5, 0.3, 0.2−x} has three distinct values; splitting any one into two parts to form two equal pairs requires x=0 or x<0 or x>1/7 in all 9 cases. Yet D*≤1/7 IS achievable for this config (best D=1/1750, via a non-exact-pairing strategy). **The O1 strategy's core claim — that some x≤1/D_n admits an exact pairing — is FALSE. The IVT argument (step 6) has no continuous function to apply IVT to: pairing feasibility is a discrete 0/1 indicator, not a PL function of x.** This kills O1 as a compressed-case strategy.

4. **Sub-gap (i) 0/523:** Confirmed consistent with round-5 findings (verification-not-proof). The superincreasing mechanism is INSUFFICIENT as stated: tower pieces are superincreasing (each 2^k > sum of smaller), but FRAGMENTS are arbitrary values (pieces of the top 2^n), NOT constrained by the superincreasing property. The "balance ⟹ block" argument only constrains tower-vs-tower subset-sums, not fragment-vs-tower balance. The stated mechanism does not yield the claim.

5. **Even-packing (O4) check:** For (5,3,2)/10, the best D=1/1750 gives even-sum E=(1−D)/2≈0.4997 ≥ 3/7≈0.4286 (target). The bound holds, but NOT via exact pairing — via near-equal piece distribution. This confirms O4 captures the actual mechanism better than O1.

---

## Per-approach review

### majorization-upper — CHANGES REQUESTED

**Sound parts:** The halving lemma milestone (steps 1–2) is SOUND and certifiable. It closes a_{n+1}≤1/D_n for ALL n unconditionally, generalizing `bottom-dominant-halving`. The builder should CERTIFY this lemma and fold the closure into the approach. This is the most concrete new progress this round.

**Fatally flawed part:** The O1 split-bottom + exact-pair-rest strategy (steps 3–7) for the compressed case (a_{n+1}>1/D_n) is FATAL. I proved exact pairing is IMPOSSIBLE for the compressed config (5,3,2)/10 (n=2) for ALL x∈(0,1/D_n] and ALL split choices — the obstruction is structural, not a gap to close. The "PL-pairing-feasibility function of x" (step 5) does not exist: pairing feasibility is a discrete 0/1 indicator, not a continuous PL function. IVT cannot apply. The outline's step 6 ("IVT on the PL-pairing-feasibility correspondence") is a category error — there is no continuous function to apply IVT to. The bounded-spread pigeonhole fallback is also unproved and does not rescue the exact-pairing target.

**What to change:** CERTIFY the halving lemma (`halving-always-a-nplus1`), close a_{n+1}≤1/D_n for all n. Do NOT pursue O1 (exact pairing) for the compressed case — it is provably impossible. Keep the compressed case (a_{n+1}>1/D_n) as an explicit GAP. The pair-matching cascade (round 5, Part VII) remains the conjectured strategy; the even-packing reframe (separate slug `even-packing-upper`) is the genuinely different alternative. The outline's claim that O1 bottoms on "subset-sum existence" is misleading — the subset-sum has NO solution in general; the real mechanism is near-equal piece distribution (captured by O4, not O1).

### even-packing-upper — CHANGES REQUESTED (NEW, register at 1500)

**Sound parts:** The algebraic reframe (D = 1 − 2E, maximize even-sum E) is correct (verified). The framing is GENUINELY DIFFERENT from O1: it attacks a packing/optimization quantity (max even-sum) rather than a discrete existence question (subset-sum/exact-pairing). This is the RIGHT direction for the compressed case — near-equal pieces distribute evenly across alternating positions at high density, and the bound holds (verified for (5,3,2)/10: E≈0.4997 ≥ 3/7).

**Load-bearing risk:** The "compression increases even-sum" exchange argument (step 4) is the open core and the main risk. The outline correctly warns against assuming Schur-convexity (D* is not Schur-convex). But the even-sum E is NOT a function of the Liu config alone — it depends on Xiang's marks (which determine the sort order and hence which positions are even). The "tower minimizes even-sum" claim is an extremal statement that needs a real exchange/smoothing proof, and it may fail for the same structural reason Schur-convexity failed (the tower is an isolated maximizer, not a smooth extremum). The greedy-packing-may-not-be-optimal concern is also valid.

**What to change:** Pursue the exchange argument but do NOT assume "compression increases even-sum" without proof. The builder should attempt a concrete exchange/smoothing argument (show that any deviation from the 2:1 geometric cascade shifts mass from odd to even slots) and be prepared for it to fail. If the exchange argument fails, the approach should fall back to a direct packing construction (exhibit explicit marks placing enough mass in even slots) rather than an extremal argument. The tower's isolated-maximum structure (D* drops to 0 under perturbation) means a pure continuity/monotonicity argument is unlikely to work — a breakpoint-structure argument is needed.

### tail-count — CHANGES REQUESTED

**Sound parts:** The PL+breakpoint reduction (step 1, certified) and mass-balance lemma (step 2, certified) are sound. The route-A framing (balance ⟹ block via superincreasing) is the only surviving non-circular lower-bound route.

**Insufficient mechanism:** The "balance ⟹ block" step (step 4) has a real gap. The superincreasing property (each 2^k > sum of all smaller 2^j) constrains TOWER pieces among themselves, but the balance equation (towers at +) = (fragments at −) involves FRAGMENT values, which are arbitrary pieces of the top 2^n — NOT tower pieces and NOT constrained by superincreasing. The outline's mechanism ("the superincreasing structure makes such an exact cover by smaller tower pieces IMPOSSIBLE") only works if the deficit is covered by tower pieces alone; but fragments can participate in the cover, and their values are arbitrary. The 0/523 verification supports the CLAIM but the stated MECHANISM does not yield it. The hard sub-case (fragments tied to tower pieces, sign-assignment ambiguity) is correctly identified but unresolved.

**What to change:** The builder needs a STRONGER mechanism than bare superincreasing. Options: (a) a Hall-type/matching argument on the tie graph (fragments tied to adjacent pieces form a bipartite structure); (b) a charging argument that assigns each fragment-at− to a strictly larger tower-piece-at+ with a deficit that the superincreasing property forbids; (c) a parity/modular argument on the fragment values. The 0/523 verification is strong evidence the claim is true — the mechanism needs to be found, not the claim re-verified.

### tower-induction — HOLD (not built this round, per outliner)

Confirmed: the outliner's HOLD is correct. G2-odd is the rival mechanism for the same lower wall; tail-count's route A is the more concretely-verifiable primary. The spine sign-pattern framing remains CIRCULAR (round 5) — do not retry.

---

## COPY decision

**None.** Confirmed. The two compressed-case routes (O1 in majorization-upper, O4 in even-packing-upper) are genuinely different framings (subset-sum existence vs packing-density exchange), not two ways to fill the same gap within one approach. Note: O1 is now FATAL (exact pairing impossible), so this is moot for O1 — but the two slugs remain separate because O4 attacks a different quantity.

---

## Shared-wall assessment

**majorization-upper (O1) and even-packing-upper (O4) both attack the compressed case, but they are NOT a single-gap trap — they are genuinely different framings.** O1 bottoms on subset-sum/multiset-equal-sums existence (can the rest be exactly paired?); O4 bottoms on a packing-density exchange (does compression increase the even-sum?). These are different mathematical objects. HOWEVER: O1's wall is not just "hard" — it is PROVABLY IMP passable (exact pairing does not exist for some compressed configs). So O1 is not a shared wall with O4; it is a DEAD END. O4's wall (the exchange argument) is the genuine open crux for the compressed case. The shared-wall concern is resolved: the two approaches do not die together on a single gap, because O1 is already dead (for a different reason — impossibility, not a shared gap).

**True-wall signal:** The fact that O1 (exact pairing) is impossible but the bound still holds (via near-equal distribution, captured by O4) suggests the TRUE wall for the compressed case is the exchange/packing argument (O4), not the subset-sum existence (O1/O2). The bounded-spread pigeonhole (folded as fallback in majorization-upper) also bottoms on the same subset-sum existence as O1 — so it is also likely dead. The genuine crux is O4's exchange argument or a direct packing construction.

---

## Registration

**even-packing-upper: REGISTER** at cold-start Elo 1500. The approach is approved (CHANGES REQUESTED on the exchange argument, but the framing is sound and genuinely different). It is the more promising direction for the compressed case now that O1 is fatally flawed.

---

## Ranking (head-to-head)

Anchoring to last outcomes: majorization-upper gained the halving lemma milestone (real certifiable progress on the priority upper wall) but its proposed O1 compressed strategy is fatally flawed. tail-count made NO new progress (superincreasing mechanism insufficient). even-packing-upper is new and genuinely different. The lower G1 remains a 5-framing true-hard-wall.

Key comparisons:
- majorization-upper > tail-count: majorization-upper gained a certifiable milestone (halving lemma, closes a_{n+1}≤1/D_n for all n) on the priority upper wall; tail-count made no new progress and the superincreasing mechanism is insufficient.
- majorization-upper > xor-overlap, lp-dual, gaps-leftover: certifiable milestone on the priority wall vs G1-equivalent gaps on the harder lower wall.
- tail-count > tower-induction, xor-overlap, lp-dual, gaps-leftover: accumulated 5-round progress on the lower wall.
- even-packing-upper < majorization-upper: new unproven exchange argument vs certifiable milestone.
- even-packing-upper < tail-count, tower-induction: new vs accumulated progress.
- even-packing-upper = xor-overlap: both at similar level (new upper with open exchange vs certified-but-G1-equivalent lower).
- even-packing-upper > lp-dual, gaps-leftover: genuinely different on priority wall vs G1-equivalent/stalled.

---

## Per-approach verdicts

- **majorization-upper: CHANGES REQUESTED** — halving lemma milestone sound (certify it, close a_{n+1}≤1/D_n); O1 split-bottom exact-pairing strategy FATAL (exact pairing impossible, verified for (5,3,2)/10); do NOT pursue O1.
- **even-packing-upper: CHANGES REQUESTED** — genuinely different framing (sound for the compressed case); exchange argument is the load-bearing risk (unproved, may fail like Schur-convexity); pursue with a concrete exchange or direct packing construction.
- **tail-count: CHANGES REQUESTED** — mass-balance + breakpoint sound; superincreasing mechanism insufficient for arbitrary fragments (only constrains tower pieces, not fragment values); needs a stronger mechanism (matching/charging/parity).
- **tower-induction: HOLD** — not built this round (per outliner); spine sign-pattern framing remains CIRCULAR.

## Updated ranking (Elo after update, best-first)

1. tail-count (~1730, stale cleared)
2. majorization-upper (~1565, up from 1544 — halving lemma milestone)
3. tower-induction (~1597)
4. even-packing-upper (~1500, new, cold-start)
5. xor-overlap (~1524)
6. lp-dual-certificate (~1486)
7. gaps-leftover (~1486)
8. self-similar (~1414)
9. d-potential (~1407)
10. balanced-configs (~1312, retired)

## Shared-wall assessment

O1 (majorization-upper) and O4 (even-packing-upper) are genuinely different framings (subset-sum existence vs packing-density exchange) — NOT a single-gap trap. However, O1 is now PROVABLY DEAD (exact pairing impossible for compressed configs), so the shared-wall concern is moot: O4's exchange argument is the genuine open crux for the compressed case. The bounded-spread pigeonhole (O1 fallback) also bottoms on subset-sum existence and is likely dead too. The true wall for the upper bound is now O4's exchange/packing argument.

## build set: majorization-upper, even-packing-upper, tail-count
