# Lemma: Floor-half reduction of the top-scale peel (GAP-L Case B ⇔ a single scalar inequality)

Setting (P3, dyadic integer normalization): `F = ⊎_{j=0}^n π_j` is a simultaneous refinement of
the ladder `{1,…,2^n}` (Structure Lemma); top-scale peel `F = π_0 ⊎ F'`, `π_0` a partition of `2^n`,
`F'` a refinement of `{1,…,2^{n−1}}` with all parts `≤ θ := 2^{n−1}`, `ΣF' = 2^n−1`, `Σπ_0 = 2^n`.
`N_P(t)=#{p∈P: p>t}`, `O_P={t>0: N_P(t) odd}`, `D̃(P)=λ(O_P)` (certified Lemma G).
`M(t) := N_{π_0}(t) − N_{F'}(t)` on `(0,θ)`; `β := (y_1(π_0)−θ)^+`.

**(FLOOR) identity.**
```
   D̃(F) = 1 − 2 ∫_{(0,θ)} ⌊M(t)/2⌋ dt.
```

**Proof.** By the certified peel identity (`peel-difference-bound.md`), `D̃(F)=λ(O_{π_0}△O_{F'})`.
Split the axis at `θ`. Every part of `F'` is `≤θ`, so `O_{F'}⊆(0,θ]`; on `(θ,∞)`,
`O_{π_0}△O_{F'}=O_{π_0}∩(θ,∞)`. Since `Σπ_0=2^n=2θ`, at most one part of `π_0` exceeds `θ`, so
`N_{π_0}∈{0,1}` on `(θ,∞)` and `λ(O_{π_0}∩(θ,∞))=(y_1−θ)^+=β`. On `(0,θ)`,
`O_{π_0}△O_{F'}={t: N_{π_0}+N_{F'} odd}={t: M odd}` (parity of a sum = parity of a difference).
For every integer `m`, `1[m odd]=m−2⌊m/2⌋` (both equal `m mod 2`). Integrate over `(0,θ)`:
`λ{M odd}=∫M − 2∫⌊M/2⌋`. Now `∫_{(0,θ)}N_{F'}=ΣF'=2^n−1`, and `∫_{(0,θ)}N_{π_0}=Σπ_0−β=2^n−β`,
so `∫_{(0,θ)}M=(2^n−β)−(2^n−1)=1−β`. Hence `λ{M odd}=(1−β)−2∫⌊M/2⌋` and
`D̃(F)=β+λ{M odd}=1−2∫⌊M/2⌋`. ∎

**Consequence.** `D̃(F) ≥ 1  ⟺  I_n := ∫_{(0,θ)}⌊M/2⌋ ≤ 0`; the tie `D̃=1` is exactly `I_n=0`.
So the entire lower-bound Case B is equivalent to the single scalar inequality `I_n ≤ 0`.

**Layer form.** `⌊m/2⌋ = Σ_{k≥1}1[m≥2k] − Σ_{k≥1}1[m≤−(2k−1)]`, hence
`I_n = Σ_{k≥1}(λ{M≥2k} − λ{M≤−(2k−1)})` (even thresholds on the `+` side vs odd on the `−` side).

**Status.** Reviewer-verified (round 10): exact-`Fraction`, `0` mismatches of (FLOOR) over `3·10³`
feasible refinements `n≤5`; `I_n ≤ 0` (max `= 0`) over independent random feasible Case-B configs.
Self-contained from the certified peel identity + `1[m odd]=m−2⌊m/2⌋`. This is the cleanest known
restatement of GAP L; it supersedes the `(△⋆)` measure form. **Note:** proving `I_n ≤ 0` itself
remains OPEN (GAP-P1′) — this lemma is the reduction, not the closure.
