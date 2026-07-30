# V(3): second-largest-piece upper bound `D* ≤ M_2/4`

**Source:** `majorization-upper` Part IV, round 4. Uses the certified `n2-max-bound`.

## Statement

For every n = 3 Liu config `L = (a_1 ≥ a_2 ≥ a_3 ≥ ... ≥ a_m)`, `m ≤ 4`, summing to 1, Xiang has `≤ 3` marks with

$$D^{*}(L) \;\le\; \frac{M_2}{4} \;=\; \frac{a_2}{4}, \qquad M_2 := a_2 \text{ (second-largest piece)}.$$

## Proof

**Trivial case `m ≤ 3`.** If `m ≤ 3`, Xiang halves each piece once (`m ≤ 3` marks), producing `m` canceling pairs. `D = 0 ≤ M_2/4`. So assume `m = 4` (4 pieces, 3 marks).

**Case 1: Dominant (`a_1 ≥ 2a_2`).** Halve `a_1 → {a_1/2, a_1/2}`. Since `a_1/2 ≥ a_2 ≥ a_3 ≥ a_4`, the sorted order is `(a_1/2, a_1/2, a_2, a_3, a_4)`. The two halves at positions 1 (`+`) and 2 (`−`) cancel. The rest `(a_2, a_3, a_4)` starts at position 3 (odd, `+`), same parity as rest-local position 1, so `D(total) = D(rest)`. The rest has 3 pieces, max `a_2 = M_2`, and 2 marks remain. By `n2-max-bound` (applied scale-free to the rest, a 3-piece multiset with max `M'`): `D(rest, 2 marks) ≤ M'/4 = a_2/4 = M_2/4`. **Parity preserved**: subsequent fragments are `≤ a_2 ≤ a_1/2`, so the halves remain at positions 1, 2. **Mark budget**: `1 + 2 = 3`. ✓

**Case 2: Non-dominant (`a_1 < 2a_2`).** Pair `a_1 → {a_2, a_1 − a_2}`. Since `a_1 < 2a_2 ⟹ a_1 − a_2 < a_2`, and `a_3 ≤ a_2, a_4 ≤ a_2`, the two `a_2` copies are the largest pieces, at positions 1 (`+`) and 2 (`−`), canceling. The rest' `sort{a_1 − a_2, a_3, a_4}` starts at position 3 (`+`), so `D(total) = D(rest')`. The rest' has max `max(a_1 − a_2, a_3) ≤ a_2 = M_2` (both: `a_1 − a_2 < a_2` and `a_3 ≤ a_2`). By `n2-max-bound`: `D(rest', 2 marks) ≤ max(rest')/4 ≤ M_2/4`. **Parity preserved**: fragments `≤ max(rest') ≤ a_2`, so the two `a_2`'s remain at positions 1, 2. **Mark budget**: `1 + 2 = 3`. ✓

**Edge case `a_2 = a_3` (three `a_2` copies after pairing).** By tie-agnosticism (equal adjacent pieces contribute 0 regardless of order), two `a_2`'s can be placed at positions 1, 2 (canceling), the third entering the rest. The rest' multiset has max `≤ a_2 = M_2` regardless. `n2-max-bound` (stated for arbitrary sorted multisets, tie-agnostic) applies. ✓

**Exhaustion.** For `m = 4`, the cases `a_1 ≥ 2a_2` (dominant) and `a_1 < 2a_2` (non-dominant) are exhaustive and disjoint. For `m ≤ 3`, `D* = 0`. In every case, `D* ≤ M_2/4 = V(3)`. ∎

**Tightness.** At `T_3 = (8, 4, 2, 1)/15`: `M_2 = 4/15`, `V(3) = 1/15`, `D*(T_3) = 1/15` (by `parallel-halving-saturates-tower`). Equality.

## Verification

Exact-`Fraction` search over all 4-part integer configs `(p, q, r, s)/D` with `D ≤ 24`, `p ≥ q ≥ r ≥ s ≥ 1`: 0 violations of `D* ≤ M_2/4`; the tower `(8,4,2,1)/15` attains ratio `1.000`. ✓
