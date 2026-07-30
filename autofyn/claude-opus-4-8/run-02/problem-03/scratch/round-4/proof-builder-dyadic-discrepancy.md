# Proof-builder report — dyadic-discrepancy (IMO 2026 P3, imo-2026-03), Round 4

**Slug target:** upper bound `c(n) ≤ 2^n/(2^{n+1}−1)` (Xiang forces D ≤ u_n). GAP U.
**Assignment:** close GAP U Case (iii) balanced via disjunctive reserve-buffer invariant (aimo-0340).
**Status: partial.** Genuine new closure; the residual gap is sharpened but not fully closed.

## What I closed this round (rigorous, new)

**Pivot Lemma (§4.6, fully proven).** For any multiset ℓ_1≥…≥ℓ_m and any subset
S ⊆ {ℓ_2,…,ℓ_m} with sum(S) ≤ ℓ_1, Xiang using **exactly m−1 removal ops** — bisect every
piece not in S (deleted by the certified Invisible-Pair Lemma), then pin the pieces of S into
the pivot ℓ_1 one at a time in decreasing order — reaches effective total = ℓ_1 − sum(S) ≥ 0.
Pin-validity is clean: before subtracting s_i the pivot equals R_i = ℓ_1 − (s_1+…+s_{i−1}), and
R_i − s_i = ℓ_1 − (s_1+…+s_i) ≥ ℓ_1 − sum(S) ≥ 0, so every pin is legal (equality → free-delete).
Op-count = (m−1−|S|) + |S| = m−1 exactly.

**Case (iii-a) fully closed for all n.** Split Case (iii) {max(ℓ_1,2ℓ_2)<c(k)Σ} by ℓ_1 vs Σ/2.
When ℓ_1 ≥ Σ/2 (sub-case iii-a): the "others" sum to Σ−ℓ_1 ≤ ℓ_1, so S = all others is admissible;
Pivot Lemma gives residual = 2ℓ_1 − Σ. Since ℓ_1 < c(k)Σ and 2c(k)−1 = u_k, residual = 2ℓ_1 − Σ
< (2c(k)−1)Σ = u_k Σ. Hence D ≤ residual < u_k Σ. This closes the WHOLE slab Σ/2 ≤ ℓ_1 < c(k)Σ,
independent of ℓ_2, and is tight (residual → u_k Σ as ℓ_1 → c(k)Σ, the dyadic boundary).
Numerically verified with exact Fraction arithmetic: 0 violations, worst ratio →1⁻, k ≤ 7.

**Net effect on GAP U.** Cases (i) dominant, (ii) balanced-top (both already certified) + (iii-a)
new now settle EVERY configuration except the strictly-balanced sub-case ℓ_1 < Σ/2. GAP U is
reduced from "all of Case (iii)" to the single sub-case (iii-b).

## Remaining gap (precise)

**Sub-case (iii-b):** m = k+1 pieces, ℓ_1 < Σ/2 and ℓ_2 < c(k)Σ/2 (so also 2ℓ_2 < c(k)Σ). Need:
Xiang with ≤ k ops reaches effective total ≤ u_k Σ. Numerically TRUE with slack (worst residual
≈ 0.83 u_3, 0.72 u_4; solver exhaustive over all op-sequences, `/tmp/round-4/rt_search.py`), but
the slack → 0 at the (iii-a)/(iii-b) interface ℓ_1 ↑ Σ/2, so a sufficient bound must be sharp there.

Why the easy routes fail (both proved this round):
- Black-box single-move + RT(k−1) / max-total greedy: telescopes to 2/((k+1)(k+2)) > u_k, k≥3
  (round-3 obstruction, reconfirmed).
- Pivot-into-ℓ_1 subset-sum alone: on coarse instances the gap ℓ_1 − max{subset-sum ≤ ℓ_1} exceeds
  u_k Σ (e.g. k=3, (0.492,0.253,0.252,0.003): ρ_piv = 0.236 ≈ 3.5 u_3). The true optimum there
  DELETES the pivot ℓ_1 and cancels a near-equal pair (bisect ℓ_1, bisect ℓ_4, pin ℓ_2 into ℓ_3 →
  residual ℓ_2−ℓ_3). So (iii-b) needs an ADAPTIVE pivot (chosen after possibly deleting ℓ_1) and/or
  pin-created intermediate "coins" ℓ_i−ℓ_j as extra subset-sum denominations.
- Naive deterministic schedules (merge-top-two, pin-smallest-into-largest): ratios ≫ 1 for β<½.
- Even reducing to ONE piece (min |±signed sum|): ratio up to ~19 u_k — the optimum must ZERO OUT
  (bisect) some pieces, i.e. use coefficients in {0,±1}, not pure ±1.

The aimo-0340 disjunctive-reserve invariant was NOT successfully instantiated into a self-restoring
two-clause statement that closes (iii-b): a one-parameter potential ψ(k,β) does not close because the
pin recursion depends on ℓ_2,…,ℓ_m separately, not on β alone (verified: worst residual as a function
of β is jagged, and the recursion's new-config max depends on ℓ_2, ℓ_3 individually). I did not want
to overclaim a fake invariant.

## Recommended next step for this slug
(iii-b) route (α): prove that among {pivot-into-ℓ_1} ∪ {delete ℓ_1, then pivot-into-ℓ_2 with the
difference-coin ℓ_2−ℓ_3 available} at least one reaches ≤ u_k Σ, using the ℓ_1<Σ/2, ℓ_2<c(k)Σ/2
constraints. This is a finite-alternative subset-sum-with-differences claim; the solver confirms the
alternative always suffices — the open work is a clean proof of the subset-sum granularity bound in
the balanced regime.

## Promotable lemmas (for reviewer to certify)
- **Pivot Lemma** (§4.6): residual ℓ_1 − sum(S) in exactly m−1 ops, any admissible S. Unconditional,
  rests only on certified IP + generalized-pin. Reusable by dyadic-discrepancy-euclid.
- **Case (iii-a) closure**: Σ/2 ≤ ℓ_1 < c(n)Σ ⟹ residual 2ℓ_1−Σ < u_nΣ. Conditional on RT.

## Spec concerns
None. The reduction chain (RT ← removal-ops ← Invisible-Pair ← certified level-measure identity) is
intact; the Pivot Lemma is a specialization within it. The answer c(n)=2^n/(2^{n+1}−1) and the split
c(n)=(1+u_n)/2 are unchanged and consistent. Numerics used exact Fraction arithmetic (no float
round-off in the claims); all prose steps stand without the numerics. Gap honestly marked partial.
