# Lemma: mass-budget-breakpoint-inequality

**Status:** CERTIFIED (round 6, reviewer-certified).

**Statement.** At a breakpoint config of T_n (cascade type: all ≤ n marks split the top piece 2^n into fragments f_1, ..., f_r with r ≤ n+1, sum = 2^n; the below-top tower pieces {2^{n−1}, ..., 2, 1} are unsplit; breakpoint condition: every fragment value appears ≥ 2 times in the full config), let

- F = Σ (surviving non-dyadic fragment values in the spine, after `spine-pair-cancellation` S1),
- T = Σ (surviving tower values in the spine).

Then

$$T \geq 3F - 1. \qquad (\text{tower units: } 2^n = \text{top}, \; 2^{n+1}-1 = D_n).$$

**Proof.** The top mass 2^n is partitioned among fragments. Classify fragment values:

1. **Surviving non-dyadic** values w_1, ..., w_l (odd count c_{w_i} ≥ 3, since breakpoint forces ≥ 2 ties and non-dyadic values can only tie other top fragments — tower pieces are all powers of 2): each consumes c_{w_i}·w_i ≥ 3·w_i from the top budget. Total ≥ 3F.

2. **Non-surviving non-dyadic** values (even count ≥ 2): each consumes ≥ 0. Total ≥ 0.

3. **Dyadic** values 2^k appearing d_k times among top fragments: consume d_k·2^k.

Total: 2^n ≥ 3F + 0 + Σ_k d_k·2^k.

For each tower piece 2^k (k = 0, ..., n−1):
- If d_k is odd (≥ 1): 2^k is NOT in the spine (count 1 + d_k is even). It contributes d_k·2^k ≥ 2^k to the top budget.
- If d_k is even (≥ 0): 2^k IS in the spine (count 1 + d_k is odd). It contributes d_k·2^k ≥ 0.

So Σ_k d_k·2^k ≥ Σ_{d_k odd} 2^k = (2^n − 1) − T (the non-surviving tower mass; total tower mass below top = 2^n − 1, surviving = T).

Substituting: 2^n ≥ 3F + (2^n − 1) − T, giving 1 ≥ 3F − T, i.e., T ≥ 3F − 1. ∎

**Corollary 15a (block condition sufficiency).** At a breakpoint of T_n, IF the block condition holds on the spine (all surviving fragments at + positions) AND D = 1, THEN F = 0 (the spine is all-tower).

*Proof.* Block condition (all F at +) gives D = F − T. D = 1 gives F = T + 1. Lemma: T ≥ 3F − 1 = 3(T+1) − 1 = 3T + 2, so −2T ≥ 2, T ≤ −1. Since T ≥ 0 (nonneg mass), contradiction — unless F = 0. When F = 0, the block condition is vacuous and the spine is all-tower, D ≥ 1 by `even-group-spine-lower-bound` (geometric dominance). ∎

**Corollary 15b (continuity rules out "all F at −").** At a D = 1 breakpoint, the "all surviving fragments at −" block direction is impossible.

*Proof.* If the block condition holds with all fragments at − on an adjacent PL cell, the `mass-balance-lemma` gives D = 2S_+ − D_n ≤ 2(2^n − 1) − D_n = −1 on that cell (all top fragments at − ⟹ S_+ ≤ 2^n − 1 < 2^n). By PL continuity (§6, `pl-breakpoint-minimum`), D extends to the cell boundary; a cell with D ≤ −1 on its interior cannot have D = 1 at its boundary vertex. Contradiction. ∎

**Combining 15a + 15b:** At a D = 1 breakpoint, IF the block condition holds on any adjacent cell, it must be the "all F at +" direction (15b rules out −), which forces F = 0 (15a), making the spine dyadic, D ≥ 1 by §8. The block condition is SUFFICIENT for D = 1 at breakpoints.

**Honest caveat (the open step).** This constrains F but does NOT prove F = 0 without the block-condition hypothesis. The remaining open step is GAP-C(i)-balance-implies-block: prove the block condition (or F = 0) at D = 1 breakpoints directly. Any counterexample to D ≥ 1 must have F > 0 AND the block condition failing — a much more constrained scenario.

**Verified.** 0 violations across all T_3 cascade breakpoints (1/24 grid). Tightness: {7/3,7/3,7/3,1} gives T=6=3·(7/3)−1; {4/3,4/3,4/3,4} gives T=3=3·(4/3)−1. When F > 0, D > 1 always (minimum D = 5/3). ✓
