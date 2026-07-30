# Lemma: Positive-Layer Localization (GAP L, positive layers of I_n)

Setting (P3, dyadic integer normalization). Top-scale peel `F = π_0 ⊎ F'`, `θ := 2^{n−1}`,
`M(t) := N_{π_0}(t) − N_{F'}(t)` on `(0,θ)`. By the certified layer form (`floor-half-reduction.md`)
`I_n = ∫_{(0,θ)}⌊M/2⌋ = P − Q`, where
```
   P := Σ_{k≥1} λ_{(0,θ)}{M ≥ 2k} = ∫_{(0,θ)} max(⌊M/2⌋, 0),
   Q := Σ_{k≥1} λ_{(0,θ)}{M ≤ −(2k−1)} = ∫_{(0,θ)} max(−⌊M/2⌋, 0).
```
Let `y_1 ≥ y_2 ≥ … ≥ y_{a_0+1}` be the parts of `π_0` in nonincreasing order, `K_0 := ⌊(a_0+1)/2⌋`.

**(POS) bound.**
```
   P ≤ Σ_{k=1}^{K_0} y_{2k}.
```
In particular `a_0 = 0 ⇒ K_0 = 0 ⇒ P = 0` (re-derives Case A on the positive side), and a positive
layer of index `k` can be nonzero only when `π_0` has `≥ 2k` parts, i.e. `a_0 ≥ 2k−1`.

**Proof.** Fix `k ≥ 1`. Since `N_{F'} ≥ 0`, `{t∈(0,θ): M(t) ≥ 2k} ⊆ {t∈(0,θ): N_{π_0}(t) ≥ 2k}`.
`N_{π_0}(t) ≥ 2k` iff at least `2k` parts of `π_0` exceed `t`, iff `y_{2k} > t` (requires `π_0` to
have `≥ 2k` parts, else the set is empty). Two distinct parts each `≥ y_2` sum to `≤ Σπ_0 = 2^n = 2θ`,
so `y_2 ≤ θ`, hence `y_{2k} ≤ y_2 ≤ θ`, and `{N_{π_0} ≥ 2k} ∩ (0,θ) = (0, y_{2k})`, of measure
`y_{2k}`. Thus `λ_{(0,θ)}{M ≥ 2k} ≤ y_{2k}`, nonzero only for `2k ≤ a_0+1`, i.e. `k ≤ K_0`. Sum. ∎

**Verification (reviewer, exact `Fraction`).** `0` violations over `5000` random feasible peels per
`n = 2,3,4,5` (all budget splits), and the bound is TIGHT (`P = Σ_{k=1}^{K_0} y_{2k}` attained on a
substantial fraction of configs). Consistent with the builder's `0/20000`, `n=4`.

**Scope / what it does NOT give.** (POS) controls only the POSITIVE layers `P` — the `π_0` side.
Closing `I_n = P − Q ≤ 0` still requires a matching lower bound `Q ≥ P` on the negative layers,
which are governed by `N_{F'}` (`F'`'s recursive dyadic cut-tree). (POS) does not supply this; the
`Q ≥ P` bound is the shared open wall (GAP-P1′). This lemma is the clean FLOOR/layer form of the
banked round-6 even-rank deficit bound `E_A ≤ Σ y_{2j}`; it uses `π_0`'s exact ordered parts, not a
scalar summary.

Origin: `approaches/allocation-vertex-corner.md` (round 11). Self-contained from the certified
layer form (`floor-half-reduction.md`).
