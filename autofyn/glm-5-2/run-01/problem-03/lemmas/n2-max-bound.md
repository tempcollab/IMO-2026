# n = 2 Max-bound `D* ≤ max/4`

**Source:** `majorization-upper` Part III, round 4. Derived from the certified `n2-upper-bound-complete`.

## Statement

For every multiset `L = (a_1 ≥ a_2 ≥ ... ≥ a_m)` of positive reals summing to 1, with `m ≤ 3` (n = 2 game), Xiang has `≤ 2` marks with

$$D^{*}(L) \;\le\; \frac{\max(L)}{4} \;=\; \frac{a_1}{4}.$$

Moreover, equality holds iff `L` is the scaled tower `T_2 = (4, 2, 1)/7` (up to the `m < 3` edge cases where the bound is strict).

## Proof

Derived from the per-regime strategy of `n2-upper-bound-complete` (certified). The n = 2 proof partitions configs into four regimes by `(a_1, a_2)`; in each, the exhibited Xiang strategy gives `D ≤ a_1/4`. Let `M := a_1`.

**Regime A** (`a_1 ≥ 2a_2` AND `a_1 ≥ 4/7`): halve `a_1`. Rest `{a_2, a_3}` has total `R = 1 − a_1 ≤ 3/7`. The n = 1 bound (`n1-base-both-bounds`: for 2 pieces with 1 mark, `D* ≤ R/3`) gives `D(rest) ≤ R/3 ≤ 1/7 ≤ M/4` (since `M ≥ 4/7 ⟹ M/4 ≥ 1/7`).

**Regime C** (`a_1 ≥ 2a_2` AND `a_1 < 4/7`): halve `a_1`. Rest `{a_2, a_3}`, total `R > 3/7`. In regime C, `a_2 < 2a_3` always (the alternative `a_2 ≥ 2a_3` with `a_1 ≥ 2a_2` forces `a_1 ≥ 4/7`, contradicting the regime). The averaging bound `min(b_1 − b_2, 2b_2 − b_1) ≤ b_2/2` (min ≤ average) with `b_1 = a_2, b_2 = a_3` gives `D* ≤ a_3/2`. Since `a_3 ≤ a_2 ≤ a_1/2` (dominant), `a_3/2 ≤ a_1/4 = M/4`.

**Regime B1** (`a_1 < 2a_2` AND `a_2 ≥ 2/7`): pair `a_1 → {a_2, a_1 − a_2}`. Rest' `{a_1 − a_2, a_3}`, `b_1 = max(a_1−a_2, a_3), b_2 = min(a_1−a_2, a_3)`. If rest' dominant, `D* = 0 ≤ M/4`. If non-dominant, `D* ≤ b_2/2`. If `b_2 = a_1 − a_2 < a_1/2` (non-dominant `a_1 < 2a_2`), `D < M/4`. If `b_2 = a_3 ≤ a_1 − a_2 < a_1/2`, `D < M/4`.

**Regime B2** (`a_1 < 2a_2` AND `a_2 < 2/7`): pair `a_1`. Rest' `{a_1 − a_2, a_3}`. Here `b_1 < 2b_2` always (the alternative `b_1 ≥ 2b_2` forces `a_1 > 4/7`, contradicting `a_1 < 2a_2 < 4/7` — verified by the bound `a_2 + a_3 < 3/7` under the dominance hypothesis). `D* ≤ b_2/2 < M/4` as in B1.

**m ≤ 2**: halve/pair to get `D = 0 ≤ M/4`. Strict.

The four regimes are exhaustive and disjoint (split by `a_1 ≥ 2a_2` and `a_1 ≥ 4/7` / `a_2 ≥ 2/7` thresholds). ∎

**Equality.** Equality `D = M/4` in regime A requires `D = 1/7 = a_1/4`, i.e. `a_1 = 4/7`, and rest `{a_2, a_3}` attaining n = 1 equality `D = R/3`, i.e. `{a_2, a_3} = (2/7, 1/7)`. So `L = (4/7, 2/7, 1/7) = T_2`. Equality iff tower `T_2`.

## Verification

Exact-`Fraction` search over all 3-part configs with denominator `≤ 30`: 0 violations of `D* ≤ max/4`. ✓
