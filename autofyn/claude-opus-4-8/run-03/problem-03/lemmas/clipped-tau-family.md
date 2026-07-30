# Lemma CLIP (clipped-`D` / τ-family identity) — CERTIFIED (round 10)

**Setting.** Let `S = F ⊔ B` be an admissible `a=0` refinement of `C_n = {2^0,…,2^n}`
(units of `u`): `F` = fragments of the top `2^n` (each `≤ L := 2^{n−1}`, `ΣF = 2^n`), `B` a
`≤(n−1)`-cut refinement of `C_{n−1}` (each piece `≤ L`, `ΣB = 2^n − 1`). Put
`g(t) = N_F(t) − N_B(t)` on `(0,L)`, `φ(c) = 1[c odd] − c`. For `τ ∈ [0,L]` define the clip
`S'_τ = {p − τ : p ∈ S, p > τ} = F'_τ ⊔ B'_τ`, `F'_τ = {f−τ : f∈F, f>τ}`,
`B'_τ = {b−τ : b∈B, b>τ}`, and `N_F(τ) = |F'_τ| = #{f∈F : f>τ}`.

**Statement (exact identities; no inequality is asserted).**
1. `μ{t ∈ (τ,L) : g(t) odd} = D(S'_τ)`.
2. `∫_τ^{L} φ(g(t)) dt = D(S'_τ) − (ΣF'_τ − ΣB'_τ)`.
3. (Order-statistic form, via certified Lemma OSR on `S'_τ`)
   `Σ_{F' at even rank} v' − Σ_{B' at odd rank} v' = (ΣF'_τ − ΣB'_τ) − D(S'_τ)`,
   hence `∫_τ^{L} φ(g) = ΣB'_τ − ΣF'_τ + D(S'_τ)` and the τ-family reserve inequality
   `Φ(τ) := ∫_τ^{L}φ(g) + 2τ|F'_τ| ≥ 0` is equivalent to
   `Σ_{F' even rank} v' − Σ_{B' odd rank} v' ≤ τ|F'_τ|`.

At `τ = 0`, `S'_0 = S`, `F'_0 = F`, `B'_0 = B`, so identity 2 reads
`∫_0^{L} φ(g) = D(S) − (ΣF − ΣB) = D(S) − 1` — i.e. **MID-core is exactly the `τ=0` face**
(`D(S) ≥ 1 ⟺ ∫_0^L φ(g) ≥ 0 ⟺ Σ_{F even rank}v ≤ Σ_{B odd rank}v`, the certified OSR form).

**Proof.**
1. For `s > 0`, `N_{S'_τ}(s) = #{p∈S : p−τ > s, p>τ} = #{p∈S : p > τ+s} = N_S(τ+s)`. Since every
   piece of `S` is `≤ L`, `N_S = N_F + N_B ≡ N_F − N_B = g (mod 2)` on `(0,L)`; hence
   `N_{S'_τ}(s) ≡ g(τ+s) (mod 2)`. By the certified measure identity (Lemma M),
   `D(S'_τ) = μ{s>0 : N_{S'_τ}(s) odd} = μ{s>0 : g(τ+s) odd} = μ{t∈(τ,L) : g(t) odd}`
   (`g` supported on `(0,L)`).
2. `∫_τ^{L} φ(g) = ∫_τ^{L} 1[g odd] − ∫_τ^{L} g`. The first term is
   `μ{t∈(τ,L):g odd} = D(S'_τ)` by part 1. For the second, by the layer-cake identity
   `∫_τ^{L} N_X = Σ_{x∈X, x>τ}(x−τ)` (valid as every piece is `≤ L`, so `N_X(L)=0`):
   `∫_τ^{L} g = ∫_τ^{L} N_F − ∫_τ^{L} N_B = Σ_{f>τ}(f−τ) − Σ_{b>τ}(b−τ) = ΣF'_τ − ΣB'_τ`.
   Subtracting gives identity 2.
3. Certified Lemma OSR applied to `S'_τ` (a finite multiset partitioned `F'_τ ⊔ B'_τ`):
   `D(S'_τ) − (ΣF'_τ − ΣB'_τ) = 2(Σ_{B' odd rank}v' − Σ_{F' even rank}v')`. Combined with
   identity 2 and `Φ(τ) = ∫_τ^{L}φ(g) + 2τ|F'_τ|`, rearranging yields the stated equivalence. ∎

**Verification.** Machine-checked exact (max error `7.1·10^{−15}` over 2000 random admissible
`a=0` refinements, `n=2..6`, random `τ∈[0,L]`). Reviewer-reproduced round 10.

**Scope / honesty.** These are *exact identities only*. The associated inequality
`Φ(τ) ≥ 0` (RESERVE-NONNEG) is **FALSE** (explicit `n=7` witness: `F={63.0119,62.8559,2.1322}`,
`B` a 12-piece refinement of `C_6` with `ΣB=127`; `D(S)=15.07 ≥ 1` yet `Φ(8.944) = −2.07 < 0`,
reviewer-reproduced). So Lemma CLIP does NOT prove MID-core; it is the cleanest exact restatement
of the residual, casting it as the τ=0 face of an order-statistic transport
`Σ_{F' even}v' ≤ Σ_{B' odd}v' + τ|F'|`. Self-contained on certified Lemmas M and OSR.
