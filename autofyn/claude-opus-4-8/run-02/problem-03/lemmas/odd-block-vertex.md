# Lemmas OB and V: odd-block value formula for D̃, and the distinct-value bound at a minimizer

Setting: `D̃(F)=Σ_{i=1}^m(−1)^{i−1}w_i` for the descending sort `w_1≥…≥w_m` (certified Lemma G).
`Φ_n=⋃_a P_a` is the compact P3 feasible union, `P_a={x≥0: the a_j+1 coords of block j sum to
2^{n−j}}`, `Σ_j a_j ≤ n`, `m=Σ_j(a_j+1)=(n+1)+b`, `b=Σ_j a_j`.

## Lemma OB (odd-block alternating-value formula)

Let `F` have distinct values `u_1>⋯>u_K` with multiplicities `r_1,…,r_K`, first ranks
`s_l = 1+Σ_{l'<l} r_{l'}`. Then
```
   D̃(F) = Σ_{l=1}^K (−1)^{s_l−1} u_l · 𝟙[r_l odd].                     (OB1)
```
Listing the odd-multiplicity values descending as `u_{(1)}>⋯>u_{(q)}`,
```
   D̃(F) = Σ_{p=1}^q (−1)^{p−1} u_{(p)}   (even blocks contribute 0).    (OB2)
```
**Proof.** The block of value `u_l` occupies ranks `s_l,…,s_l+r_l−1`; its contribution is
`u_l(−1)^{s_l−1}Σ_{t=0}^{r_l−1}(−1)^t`, and `Σ_{t=0}^{r_l−1}(−1)^t = 𝟙[r_l odd]`. Summing gives
(OB1). For (OB2): `s_l−1=Σ_{l'<l}r_{l'} ≡ #{l'<l: r_{l'} odd} (mod 2)` (even multiplicities don't
change parity), so for the `p`-th odd value `(−1)^{s_l−1}=(−1)^{p−1}`. ∎
**Corollaries.** (OB-even) an even block contributes `0` and is freely re-splittable if the merged
order is preserved. (OB-int) if every odd-multiplicity value is an integer then `D̃(F)∈ℤ`.
**Status.** Reviewer-verified round 10: `0` mismatches vs Lemma G over `2·10⁴` random exact-`Fraction`
multisets.

## Lemma V (distinct-value bound at a minimizing vertex)

`μ := min_{Φ_n} D̃` is attained at a **vertex** `v^*` of some merged order-type cell
`Q_{a,σ}=P_a ∩ {x_{σ(1)}≥⋯≥x_{σ(m)}}`. At any such vertex with all coordinates positive, the number
`K` of distinct part-values satisfies `K ≤ n+1`.
**Proof.** On `Q_{a,σ}` the descending sort is fixed so `D̃` is linear; `μ=min_a min_σ min_{Q_{a,σ}}D̃`
is a finite family of LPs, each attained at a vertex. A vertex of an `m`-dim polytope is the unique
solution of `m` linearly independent active constraints. The available active constraints are the
`n+1` group-sum equalities and the adjacent ties `x_{σ(i)}=x_{σ(i+1)}` (there are `Σ_l(r_l−1)=m−K`
of them; `x≥0` inactive since all coords positive). Thus `m ≤ (n+1)+(m−K)`, i.e. `K ≤ n+1`. ∎
**Status.** Reviewer-verified round 10 (constraint-count argument checked; consistent with computed
vertices, e.g. `n=2` `(4,2,½,½)` has `K=3=n+1`).

**Scope note.** These are structural facts about `D̃`. Lemma V does **NOT** assert vertices are
integral (that TU claim was refuted R9). The reduction "some optimal cell-vertex is integer ⇒ target"
(GAP-IMR′) built on these lemmas is a valid but still-OPEN target — see the review; it shares the
integer-minimizer wall shown equivalent-difficulty to the target by `vertex-integrality-parity` R10.
