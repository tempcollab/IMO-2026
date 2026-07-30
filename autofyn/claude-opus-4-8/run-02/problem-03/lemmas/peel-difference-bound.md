# Lemma bundle: peel symmetric-difference identity, difference bound, Case-A closure, Invariant I

Notation: for a finite positive multiset `P`, `N_P(t)=#{p∈P: p>t}`, `O_P={t>0: N_P(t) odd}`,
and by the certified Lemma G (level-measure form) `D̃(P)=λ(O_P)=Σ_i(−1)^{i−1}w_i` (descending
sort). All statements below are for the P3 setting where `F=⊎_{j=0}^n π_j` is a simultaneous
refinement of the dyadic ladder `{1,…,2^n}` (Structure Lemma), and the top-scale peel is
`F = π_0 ⊎ F'`, `π_0` a partition of `2^n` into `a_0+1` parts, `F'` a refinement of
`{1,…,2^{n−1}}` with budget `b=Σ_{j≥1}a_j ≤ n−a_0`, `θ=2^{n−1}`.

**(1) Peel symmetric-difference identity (SD/PEEL).** For any split `F = A ⊎ B` of a finite
positive multiset, `N_F = N_A + N_B`, so `1[N_F(t) odd] = 1[N_A(t) odd] ⊕ 1[N_B(t) odd]`, i.e.
`O_F = O_A △ O_B`. Hence
`D̃(F) = λ(O_A △ O_B) = D̃(A) + D̃(B) − 2λ(O_A ∩ O_B)`.
*Proof:* additivity of `N` under disjoint union + inclusion–exclusion for `λ(A△B)`. ∎

**(2) Difference bound (DIFF).** `D̃(A ⊎ B) ≥ |D̃(A) − D̃(B)|`.
*Proof:* `0 ≤ λ(O_A ∩ O_B) ≤ min(λ(O_A),λ(O_B)) = min(D̃(A),D̃(B))`; substitute into (1). ∎
Consequence: if `|D̃(π_0) − D̃(F')| ≥ 1` then `D̃(F) ≥ 1` (closes the large-difference region
of Case B).

**(3) Case A (`a_0 = 0`) closed unconditionally.** With `π_0 = {2^n}` a single part,
`O_{π_0} = (0,2^n)` and `D̃(π_0)=2^n`; every part of `F'` is `≤ θ < 2^n`, so `O_{F'} ⊆ (0,θ)
⊆ O_{π_0}`, giving `λ(O_{π_0}∩O_{F'}) = D̃(F')`. By (1),
`D̃(F) = 2^n + D̃(F') − 2D̃(F') = 2^n − D̃(F')`.
Since `D̃(F') ≤ ΣF' = 2^n − 1` (universal bound `D̃ ≤ Σ`), `D̃(F) ≥ 2^n − (2^n−1) = 1`.
No value-IH is used, only `D̃ ≤ Σ`. ∎

**(4) Invariant I.** For the top-scale peel, `M(0⁺) := N_{π_0}(0⁺) − N_{F'}(0⁺)
= (a_0+1) − |F'|`, where `|F'| = Σ_{j=1}^n (a_j+1) = n + b`. With the budget `a_0 + b ≤ n`,
`M(0⁺) = (a_0+1) − (n+b) ≤ (n−b) + 1 − (n+b) = 1 − 2b ≤ 1`, equality iff `b=0` and `a_0=n`. ∎

**Verification (exact `Fraction`).** (1): `0` mismatches / `5·10³` random splits and `0` over
`5·10³` general `A,B`. (2): `0` violations / `1.2·10⁵` Case-B configs and over the same random
sample. (3): `D̃(F)=2^n−D̃(F')` reproduced. Integer/continuum feasible minimum `= 1`
(`n ≤ 5`), consistent.

**Scope / what it does NOT give.** (1)–(2) are general facts about `D̃`; (3) fully closes the
`a_0=0` branch of the P3 lower-bound induction; (4) is the correct near-0 anchor. They do NOT
close Case B on the residual `{|D̃(π_0) − D̃(F')| < 1}` (near-balance regime), which needs a
loaded dyadic-shape invariant on `F'` (open: GAP-P1); the plain value-IH `D̃(F')≥1` is provably
insufficient there (witness `π_0,F'` with `D̃(F')=2.506` yet `D̃(π_0⊎F')=0.146`).

Certified round 9 (proof-reviewer). Source approach: `peel-scale-rank-induction`.
