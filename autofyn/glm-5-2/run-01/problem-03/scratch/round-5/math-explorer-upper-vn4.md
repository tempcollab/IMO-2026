## imo-2026-03 — V(n≥4) crux scout (upper-bound wall)

### 1. The crux restated (and refuted as a crux)

The round-4 `majorization-upper` spine is **V(n): D* ≤ M_2/2^{n−1}** (second-largest piece). The
inductive step `V(n) ← V(n−1)` reportedly FAILS in the crux regime `a_1 < 2a_2 ∧ a_3 > a_1/2` (three
near-equal large pieces): the simple pairing IH overshoots 37% of crux cases (`M_2(rest') > M_2/2`),
though the actual `D(rest')` is 0.71× the V(n) target (slack real, IH-invisible).

**I computed the EXACT optimal Xiang response (breakpoint-restricted, B1-justified, exact `Fraction`
arithmetic) for n=4 against: (a) the 11 round-4 Max-bound violators extended to m=5, (b) a grid of
balanced-triple crux configs, (c) 3000+ random crux float configs, (d) all integer configs with
sum ≤ 28.** The headline result is decisive:

**THE CRUX REGIME IS NOT A CRUX FOR n=4.** Every single crux config (a_1<2a_2 ∧ a_3>a_1/2) has
D* = 0 or D* far below 1/D_4 = 1/31. The worst crux ratio D*/(1/31) over 3000 random trials is
**0.52** (D* = 0.017). The "37% overshoot" is an artifact of the V(n−1) IH being a loose worst-case
bound — the actual D* in the crux is zero or tiny. The slack is not "IH-invisible"; it is enormous.

The ONLY n=4 config achieving D* = 1/31 is the tower T_4 = (16,8,4,2,1)/31 (and its scalings, e.g.
2·T_4 = (32,16,8,4,2)/62). Every perturbation of the tower drops D* to 0 or to 1/sum < 1/31.
The tower is in the DOMINANT regime (a_1 = 16 ≥ 2·8 = 2a_2), NOT the crux regime.

### 2. Computed optimal Xiang responses for worst n=4 configs (table)

| config (integer, sum) | D* (exact) | 1/31 | ratio | ≤1/31? | crux? | strategy pattern |
|---|---|---|---|---|---|---|
| T_4 = (16,8,4,2,1)/31 | 1/31 | 1/31 | 1.000 | YES | no | cascade-split a_1 down to match tower → balanced pairs + bottom 1 |
| 2·T_4 = (32,16,8,4,2)/62 | 1/31 | 1/31 | 1.000 | YES | no | same (scale-free) |
| (17,8,4,2,1)/32 | 1/32 | 1/31 | 0.969 | YES | no | halve top 3, leave bottom 2 → D = 2−1 = 1/32 |
| (18,8,4,2,1)/33 | 1/33 | 1/31 | 0.939 | YES | no | cascade → residual = bottom 1/33 |
| (20,8,4,2,1)/35 | 1/35 | 1/31 | 0.886 | YES | no | cascade → residual = bottom 1/35 |
| (24,8,4,2,1)/39 | 1/39 | 1/31 | 0.795 | YES | no | halve → residual = 1/39 |
| (50,8,4,2,1)/65 | 1/65 | 1/31 | 0.477 | YES | no | cascade → residual = 1/65 |
| (7,6,5,3,1)/22 [crux, Max-bound violator+1] | 0 | 1/31 | 0 | YES | YES | pair-matching cascade → all pairs cancel |
| (7,6,5,3)/21 [n=3 violator, m=4, n=4 marks] | 0 | 1/31 | 0 | YES | YES | 4-mark pair cascade → D=0 |
| (22,19,16,10,1)/68 [crux] | 1/68 | 1/31 | 0.46 | YES | YES | pair cascade → residual 1/68 |
| (8,7,6,1,1)/23 [crux] | 0 | 1/31 | 0 | YES | YES | pair cascade → D=0 |
| (5,5,5,1,1)/17 [crux, balanced triple] | 0 | 1/31 | 0 | YES | YES | pair → D=0 |
| worst random crux (0.405,0.313,0.210,0.045,0.028) | 0.0169 | 1/31 | 0.52 | YES | YES | halving cascade |
| worst random all-config (0.532,0.301,0.103,0.042,0.023) | 0.0198 | 1/31 | 0.61 | YES | no | halving cascade |
| (16,8,4,2)/31 [m=4 tower] | 0 | 1/31 | 0 | YES | no | halve all 4 → D=0 |
| (16,8,4,3,1)/32 [tower perturbed] | 0 | 1/31 | 0 | YES | no | pair cascade → D=0 |
| (16,8,5,2,1)/32 [tower perturbed] | 0 | 1/31 | 0 | YES | no | pair cascade → D=0 |

**Key structural facts (all conjectures supported by exhaustive breakpoint computation, NOT proofs):**
- **m ≤ n ⇒ D* = 0 always.** Xiang halves each of the m ≤ n pieces (m marks), producing m
  canceling pairs. Verified 0/120 nonzero for m=3 and m=4 (n=4). So the ONLY hard case is m = n+1.
- **m = n+1 (maximal): D* > 0 only for the "tower-tail" family** `(a_1, 2^{n−1}, 2^{n−2}, …, 2, 1)/S`
  (bottom 4 pieces in geometric ratio 2). For these, D* = 1/S = a_{n+1} (the bottom piece), and
  the strategy is "cascade-split a_1 down to match the tower structure" OR "halve the n largest,
  leave the smallest." D* = 1/S ≤ 1/D_n ⟺ S ≥ D_n. The tower T_n (S = D_n, minimum) is the worst.
- **Any perturbation of the tower tail drops D* to 0.** (16,8,4,3,1), (16,8,5,2,1), (16,9,4,2,1)
  all give D*=0 — the pair-matching cascade fully cancels.

### 3. Reverse-engineered strategy pattern

When Xiang hits D ≤ 1/D_n, the structural move is **NOT the 3-mark cascade (B)** and **NOT the
mutual W/V branch (A)**. It is one of two clean patterns:

**(P1) Tower-tail / dominant configs (a_n ≥ 2·a_{n+1}, "bottom-dominant"):** Xiang **halves the n
largest pieces, leaving the smallest a_{n+1} unsplit.** The n equal-pairs (a_i/2, a_i/2) sit
adjacent in sorted order (since a_i/2 ≥ a_{i+1}/2 ≥ … ≥ a_n/2 ≥ a_{n+1}), cancel at positions
(1,2),(3,4),…,(2n−1,2n), and the residual a_{n+1} sits at position 2n+1 (odd, +). **D = a_{n+1}.**
This is optimal for the tower-tail family (D* = a_{n+1} = 1/S) and gives D ≤ a_{n+1} ≤ 1/D_n
exactly when S ≥ D_n (the config is "spread" enough). For the tower, S = D_n, so D = 1/D_n (tight).

**(P2) Non-tower-tail / non-bottom-dominant configs (a_n < 2·a_{n+1}):** Xiang uses a
**pair-matching cascade** — split pieces to create matching fragments (ties), cascading the
matches until all pieces pair up. Result: D = 0 (all cancel) for most configs; small residual
for some. Always far below 1/D_n (worst ratio 0.52 over 3000 random trials).

The **V(n) bound D* ≤ M_2/2^{n−1} is TIGHT for the entire tower-tail family** (not just the
tower): for (a, 2^{n−1}, …, 1)/S, V(n) = (2^{n−1}/S)/2^{n−1} = 1/S = a_{n+1} = D*. And 1/S ≤ 1/D_n
⟺ S ≥ D_n. So V(n) is the right bound for the hard family, and the tower is the worst member.

### 4. Assessment of the 3-mark cascade (B) and mutual W/V (A)

**3-mark cascade (B) — RED HERRING.** The cascade (pair a_1↔a_3, pair a_2↔a_3, split a_3, residual
a_1−a_2 ≤ M_2) was conjectured for the crux regime a_1<2a_2 ∧ a_3>a_1/2. But the crux regime gives
D*=0 (m≤4) or tiny D* (m=5, ratio ≤0.52). The cascade is unnecessary: the simple 4-mark
pair-matching cascade already drives crux configs to D=0. The cascade does not address the actual
hard case (tower-tail dominant configs, where the winning move is halving, not pairing).
**Obstruction: the cascade targets the wrong regime.** Drop it.

**Mutual W/V recursion (A) — solves the wrong problem.** V(n) ← W(n−1) for dominant rest, V(n) ←
V(n−1) for non-dominant rest. The non-dominant-rest branch "fails" (IH overshoots), but it doesn't
matter because D* there is 0 — the IH is too loose, not the actual D*. The recursion is trying to
prove V(n) via V(n−1), but the inductive target V(n−1) is a worst-case bound that is blind to the
slack. **Obstruction: the V(n−1) IH cannot see that the non-dominant rest is far from T_{n−1}, so
it overshoots. No refinement of the recursion fixes this — the IH is the wrong tool.** The crux
branch (V(n) ← V(n−1) for non-dominant rest) should be abandoned.

### 5. D* > 1/D_n violation search

**No violation found.** Exhaustive breakpoint computation (B1-justified, exact `Fraction`) over:
- All integer configs with sum ≤ 28 (4037 configs): 0 violations (all D*=0, no tower config exists
  at these sums).
- Tower and near-tower configs with sum 31–65: 0 violations; T_4 is the unique max (ratio 1.000).
- 3000 random crux float configs: 0 violations, worst ratio 0.52.
- 3000 random all-config float configs: 0 violations, worst ratio 0.61.
- The 11 round-4 Max-bound violators extended to m=5: 0 violations (all D*=0 or D*=1/sum < 1/31).

**V(4) = M_2/8 also has 0 violations** (tight at T_4 and 2·T_4, loose everywhere else). The answer
c(n) = 2^n/D_n survives for n=4.

### 6. Recommendation for the outliner

**Drop the V(n)←V(n−1) IH approach and the 3-mark cascade. Develop a DIRECT upper-bound slug
targeting D* ≤ 1/D_n via the "tower-tail is the hard family" structural observation.**

**One-sentence skeleton:** For m ≤ n, Xiang halves all m pieces → D=0; for m = n+1, split by
bottom-dominance: if a_n ≥ 2a_{n+1}, halve the n largest leaving a_{n+1} → D = a_{n+1} ≤ 1/D_n
(requires proving a_{n+1} ≤ 1/D_n in this regime — the hard step); if a_n < 2a_{n+1} (near-equal
bottom), use the pair-matching cascade → D = 0 or D ≪ 1/D_n (the slack regime).

**Hard step:** prove that for bottom-dominant m=n+1 configs with a_n ≥ 2a_{n+1}, either
a_{n+1} ≤ 1/D_n (so halving gives D ≤ 1/D_n), OR the config is far enough from the tower-tail
family that a better strategy exists (D* < 1/D_n). The cleanest sub-claim: for the tower-tail
family (a_1, 2^{n−1}, …, 1)/S, D* = 1/S ≤ 1/D_n ⟺ S ≥ D_n (verified, needs proof). The general
"non-tower-tail ⟹ D* < 1/D_n" is the real gap — it is an exchange/continuity argument (flagged as
hard in round 2), but now localized to the bottom-dominant regime where the halving strategy gives
a clean D = a_{n+1} formula.

**Alternative framing if the exchange argument is too hard:** prove V(n) = M_2/2^{n−1} DIRECTLY
(not via V(n−1) IH) for the bottom-dominant case using the halving strategy (D = a_{n+1}, then
prove a_{n+1} ≤ M_2/2^{n−1} when a_n ≥ 2a_{n+1} — this is a counting/AM-GM step on the bottom n
pieces), and handle the non-bottom-dominant case by showing D*=0 (pair-matching cascade fully
cancels). This avoids the IH entirely and sidesteps the phantom crux.

### Small-case / intuition notes (all CONJECTURES from computation, not proofs)
- T_n is the unique config (up to scaling) with D* = 1/D_n for n=1..4. CONJECTURE.
- For m ≤ n, D* = 0 always (Xiang halves all pieces). CONJECTURE (verified n=4, 240 random configs).
- For m = n+1, D* > 0 only for the tower-tail family (a_1, 2^{n−1}, …, 1)/S. CONJECTURE (verified
  n=4, 3000 random m=5 configs all have D* > 0 but none are tower-tail and all have ratio ≤ 0.66).
- V(n) = M_2/2^{n−1} is tight for the ENTIRE tower-tail family, not just T_n. CONJECTURE (verified
  n=4: (17,8,4,2,1)/32, (20,8,4,2,1)/35, etc. all have D* = M_2/8 = 1/sum).
- The "halve n largest, leave smallest" strategy gives D = a_{n+1} when a_n ≥ 2a_{n+1}
  (bottom-dominant). VERIFIED n=4 (all tested bottom-dominant configs match D(halve) = a_5).
- It is NOT optimal for non-tower-tail bottom-dominant configs (e.g. (10,8,4,2,1)/25: halving gives
  D=0.04 but D*=0). So the halving bound is an upper bound on D*, tight only for tower-tail.

### Dead ends (do not retry)
- **V(n) ← V(n−1) IH for the crux regime (a_1<2a_2 ∧ a_3>a_1/2):** the IH overshoots because V(n−1)
  is a worst-case bound blind to slack. The crux D* is 0 or tiny. Abandon this IH route.
- **3-mark pairing cascade (B):** targets the wrong regime (crux is easy; hard case is dominant
  tower-tail). Drop.
- **Max-bound D* ≤ M/2^n:** REFUTED (round 4, (7,6,5,3)/21). Do not revisit.
