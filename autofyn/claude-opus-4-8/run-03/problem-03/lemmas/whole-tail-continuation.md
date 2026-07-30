# Lemma WTC (whole-tail-continuation bound) — CERTIFIED (round 15)

**Statement (game-independent, unconditional).** For any reals
`a₁ ≥ a₂ ≥ … ≥ a_m > 0` (`m ≥ 1`) with sum `L`, the largest-first differencing
(descending-KK caterpillar) value
```
    K := descKK(a₁,…,a_m),   v₁ = a₁,   v_k = |v_{k−1} − a_k| (2≤k≤m),  K = v_m
```
satisfies
```
    K ≤ |2a₁ − L|.
```

**Proof (two-sided invariant, induction).** Put `P_k := a₂+…+a_k` (`P₁=0`), so
`P_m = L − a₁` and `a₁ − P_k = a₁ − (a₂+…+a_k)`. Claim the invariant, for `1≤k≤m`:
```
   (I_k)   a₁ − P_k  ≤  v_k  ≤  |a₁ − P_k| .
```
- Base `k=1`: `v₁ = a₁`, `P₁ = 0`, both sides `= a₁`. ✓
- Step: write `d := a₁ − P_{k−1}`, so `d ≤ v_{k−1} ≤ |d|`, and `a₁ − P_k = d − a_k`,
  `v_k = |v_{k−1} − a_k|`.
  - Lower: `v_k = |v_{k−1}−a_k| ≥ v_{k−1} − a_k ≥ d − a_k = a₁ − P_k` (uses `v_{k−1} ≥ d`). ✓
  - Upper, split on sign of `d`:
    - `d ≥ 0`: `|d|=d` forces `v_{k−1}=d`, so `v_k = |d−a_k| = |a₁−P_k|` (equality). ✓
    - `d < 0`: `0 ≤ v_{k−1} ≤ −d`, and `a₁−P_k = d−a_k < 0` so `|a₁−P_k| = a_k+(−d)`.
      For `t ∈ [0,−d]`, `|t−a_k|` is maximised at an endpoint:
      `a_k ≤ a_k+(−d)` and `|(−d)−a_k| ≤ (−d)+a_k` (triangle), both `= |a₁−P_k|`. ✓
- Take `k=m`: `K = v_m ≤ |a₁ − P_m| = |a₁ − (L−a₁)| = |2a₁ − L|`. ∎

**Certification (reviewer, round 15).** Re-derived the induction from scratch — every
step justified, no hand-waving. Verified independently: `K ≤ |2a₁−L|` holds with **0
violations over 200 000 exact-`Fraction` adversarial descending profiles** (`m=1..7`);
EQUALITY `K = |2a₁−L|` on the tight valley family `A^{(n)}={2^n,…,4,3,2}/(2^{n+1}+1)`
for `n=2..6`. The statement is exact/tight, not a margin bound.

**Use (upper wall, boundary layer).** With `Φ(A) := min_{∅≠T⊆{1,…,n+1}} descKK(T)`
(certified Reduction R-COV', sufficiency), the full profile is a nonempty subset, so
`Φ(A) ≤ K ≤ |2a₁−L|`. For any valley profile with `a₁ ≥ (L−u_nL)/2` (equivalently
`|2a₁−L| = L−2a₁ ≤ u_nL`, since `a₁ < L/2`), this gives `Φ(A) ≤ u_nL`, hence by
R-COV' (sufficiency) Xiang forces `D ≤ u_nL`. This closes the **boundary layer**
`(L−u_nL)/2 ≤ a₁ < L/2` of the valley EXACTLY (equality attained on `A^{(n)}`),
respecting VALLEY-TIGHT — it is the exact continuation of certified whole-tail-peel
(`a₁ ≥ L/2` ⇒ `D = 2a₁−L`, the `d ≥ 0` / equality branch of the invariant) across
`a₁ = L/2`. It does NOT touch the deep interior `a₁ < (L−u_nL)/2` (there
`|2a₁−L| > u_nL`, so the bound is vacuous — still open).
