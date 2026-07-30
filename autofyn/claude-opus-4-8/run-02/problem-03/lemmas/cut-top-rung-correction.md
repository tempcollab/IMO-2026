# Lemma: exact cut-top-rung correction (C) and the uncut-top-rung Δ-reductions (A1),(A2),(A3)

Certified round 15 (from `ladder-length-deficient-induction`). Reviewer re-derived all four
identities from `D̃(P)=Σ_i(−1)^{i−1}w_i` (descending) and reproduced them with exact `Fraction`:
(C) 0 fails / 30000; (A1) 0, (A2) 0 / 15000; (A3) 0 / 15000.

Notation: `N_P(t)=#{p∈P:p>t}`, `O_P={t>0:N_P(t) odd}`, `D̃(P)=λ(O_P)=Σ_i(−1)^{i−1}w_i`.
`Δ(R,Z):=½(D̃(R⊎Z)−ΣR+ΣZ)`. `θ:=2^{m−1}`. `F'` a budgeted refinement of the ladder `L_m`
(rung `i` sums to `2^{m−i}`); `ρ₁` = top rung; `F''=F'∖ρ₁` (a budgeted refinement of `L_{m−1}`,
all parts `<θ`), `ΣF'=2^m−1`.

## Statements

**(C) Exact cut-top-rung correction.** Suppose the top rung is CUT: `r:=|ρ₁|≥2`, `Σρ₁=θ`, every
part of `ρ₁` is `<θ`; every red part is `≤θ`. Put `W:=R⊎F''` (so `O_W⊆(0,θ)`). Then
```
   D̃(R⊎F') = D̃(ρ₁) − D̃(W) + 2λ(E∩O_W),   E:={t∈(0,θ): N_{ρ₁}(t) even},
```
equivalently, via the certified SD identity, `Δ(R,F') = Δ(R,F'') + ½θ + ½D̃(ρ₁) − I_S`, where
`I_S := λ(O_{ρ₁}∩O_W)` is the certified GAP-P1 odd-set overlap term.

**(A1) uncut-top-rung reduction, all reds ≤ θ.** If `ρ₁={θ}` (uncut) and every red `≤θ`, then
`Δ(R,F') = (2^m−1−ΣR) − Δ(R,F'')`.

**(A2) uncut-top-rung reduction, one big red.** If `ρ₁={θ}` and exactly one red `y>θ` (rest `≤θ`),
then with `R₀=R∖y`, `Δ(R,F') = Δ(R₀,F'')`.

**(A3) big-red red-peel (any top rung).** If `y=maxR>θ` (hence exceeds every blue part), then with
`R₀=R∖y`, `Δ(R,F') = (2^m−1−ΣR₀) − Δ(R₀,F')`.

## Proofs

**(C).** Let `U:=R⊎{θ}⊎F''` be the uncut companion. On `(0,∞)`, `N_{R⊎F'}=N_W+N_{ρ₁}` and
`N_U=N_W+1[t<θ]`. On `(θ,∞)` both `N_{ρ₁}=0` and `1[t<θ]=0`, so the odd-indicators agree. On
`(0,θ)`, `1[t<θ]=1`, so `1[N_U odd]=1−1[N_W odd]`. Split `(0,θ)` by parity of `N_{ρ₁}`:
where `N_{ρ₁}` is odd, `1[N_{R⊎F'} odd]=1[N_W even]=1[N_U odd]` (no change); where `N_{ρ₁}` is even
(the set `E`), `1[N_{R⊎F'} odd]=1[N_W odd]`, so the integrand differs by `2·1[N_W odd]−1`.
Integrating, `D̃(R⊎F')−D̃(U)=2λ(E∩O_W)−λ(E)`. Since `O_{ρ₁}⊆(0,θ)` and `E=(0,θ)∖O_{ρ₁}`,
`λ(E)=θ−D̃(ρ₁)`; MAXPEEL gives `D̃(U)=θ−D̃(W)`. Hence
`D̃(R⊎F')=θ−D̃(W)+2λ(E∩O_W)−θ+D̃(ρ₁)=D̃(ρ₁)−D̃(W)+2λ(E∩O_W)`. The Δ-form is (SD) with `A=W`,
`B=ρ₁`, using `λ(O_W)=D̃(W)=λ(E∩O_W)+λ(O_{ρ₁}∩O_W)` (partition of `O_W` by parity of `N_{ρ₁}`). ∎

**(A1).** Every red `≤θ` and every `F''` part `<θ`, so `θ=max(R⊎F')`. MAXPEEL: `D̃(R⊎F')=θ−D̃(R⊎F'')`.
With `ΣF'=θ+ΣF''=2^m−1` and `ΣF''=2^{m−1}−1`, substitute into `Δ(R,F')` to get
`Δ(R,F')=(2^m−1−ΣR)−Δ(R,F'')`. ∎

**(A2).** `y>θ≥` every element of `R₀⊎F''⊎{θ}`, so `y` is rank 1, `θ` rank 2; they contribute
`y−θ` and the remaining ranks are those of `R₀⊎F''`, giving `D̃(R⊎F')=(y−θ)+D̃(R₀⊎F'')`. Direct
substitution yields `Δ(R,F')=Δ(R₀,F'')`. ∎

**(A3).** By the certified (I3′), `D̃(R⊎F')=y−D̃((R∖y)⊎F')`. Substituting into `Δ(R,F')` with
`ΣR=ΣR₀+y`, `ΣF'=2^m−1` gives `Δ(R,F')=(2^m−1−ΣR₀)−Δ(R₀,F')`. ∎

## Remark (scope / what this does NOT do)

(A1)–(A3) close every UNCUT-top-rung leaf of the budget-aware ladder-length induction
`(P̂_m)/(Q̂_m)/(L̂B_m)` (round 15). (C) is the exact peel of a CUT top rung; its residual is
`I_S=λ(O_{ρ₁}∩O_W)`, which is precisely the certified GAP-P1 overlap wall (`top-peel-general.md`).
(C) is a bookkeeping/accounting identity, NOT a closer: it carries the below-`p_r` tail flip
exactly, but bounding `I_S` (now with the global cut budget `Σa_i≤m` as an available hypothesis)
remains open. The (P̂_m)/(Q̂_m) STATEMENTS are true numerically (0 fails, m≤5) but are proved here
only for the uncut-top-rung induction step, so they are NOT certified as theorems.
