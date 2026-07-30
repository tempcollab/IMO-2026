# Lemma (Merged-order signed sum + Termwise Lattice Bound) — CERTIFIED round 4

Depends on: certified Lemma G / Level-Measure identity (`lemmas/greedy-claim.md`). Reviewer-verified
round 4 (identity + Lemma-T checked on 2·10⁴ random top/bottom splits, 0 violations of both the
signed-sum identity and `maxc≤1 ⇒ D≥sum(Y)−sum(Z)`).

## Reformulation (♣)/(♦)
Let `F = Y ⊎ Z` be a multiset split into two labelled sub-multisets. Set
`M(t) := N_Y(t) − N_Z(t)` where `N_P(t)=#{p∈P:p>t}`. Then:
- **(a)** `N_F = N_Y+N_Z ≡ N_Y−N_Z = M (mod 2)`, so `D(F) = λ{t : N_F odd} = ∫₀^∞ 1[M(t) odd] dt`.
- **(b)** `∫₀^∞ M dt = sum(Y) − sum(Z) =: Δ` (Fubini: `∫N_P = sum(P)`).
Merge `Y⊎Z` into a descending list `w₁≥…≥w_m` (`w_{m+1}=0`), label each part `T` (from `Y`) or `B`
(from `Z`), and let the prefix imbalance `c_i := #T − #B` among `w₁,…,w_i` (`c_0=0`). On
`(w_{i+1},w_i)`, `M = c_i`. Hence with `ψ(c) := 1[c odd] − c` and `Δw_i := w_i−w_{i+1} ≥ 0`,
`D(F) − Δ = Σ_i ψ(c_i) Δw_i`.  **(♦)**

## Termwise Lattice Lemma T
`ψ(c) ≥ 0 ⟺ c ≤ 1` (`ψ(1)=ψ(0)=0`; `ψ(c)≥−c≥0` for `c≤0`; `ψ(c)≤1−c<0` for `c≥2`). Therefore:
> If the merged descending order of `Y⊎Z` has `c_i ≤ 1` for **every** prefix `i`, then
> `D(Y⊎Z) ≥ sum(Y) − sum(Z)`.

**Proof.** Under `c_i≤1`, every `ψ(c_i)≥0`; each `Δw_i≥0`; so `D−Δ = Σψ(c_i)Δw_i ≥ 0`. ∎
Equality-robust: strict alternation `T,B,T,B,…` gives `c_i∈{0,1}`, all `ψ=0`, `D=Δ` exactly.

## Application to GAP L (lower bound, Case B)
In integer units `Y` = top-descendants (`sum 2^n`), `Z` = bottom-descendants (`sum 2^n−1`), so
`Δ = 1`. Lemma T closes Case B on the sub-region `maxc := max_i c_i ≤ 1`. The residual
`maxc ≥ 2` ("T-run" gets `≥2` ahead) is OPEN and provably needs `Z`'s recursive cut-tree
(Structure Lemma), not a scalar/count summary of `Z` (that is refuted).

## Guard
Lemma T is CONDITIONAL on `maxc ≤ 1`. The UNCONDITIONAL claim `D ≥ sum(Y)−sum(Z)` is FALSE and
must never be used; the conditional statement above is the certified one.
