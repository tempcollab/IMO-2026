# Lemma: Base-slice theorem (★) — extremal b=0 case of GAP L FULLY PROVEN

Setting (P3, dyadic integer normalization). `L_m := {2^{m−1},…,2,1}` (uncut ladder, `ΣL_m=2^m−1`,
`θ:=2^{m−1}`). For a finite positive multiset `P`, `D̃(P)=∫_0^∞ 1[N_P(t) odd] dt = Σ_j(−1)^{j−1}w_j`
(certified Lemma G, tie-invariant), `N_P(t)=#{p∈P:p>t}`.

**Ladder discrepancy functional.** For a red multiset `R` and blue ladder `L_m`,
`Δ_m(R) := ½( D̃(R⊎L_m) − ΣR + 2^m − 1 )`.

## Main result (CERTIFIED — reviewer re-derived + verified, round 13)

**Base-slice theorem (★).** For the uncut ladder `L_n` and ANY multiset `π_0` with `Σπ_0=2^n` and
`≤ n+1` parts (fractional allowed):
```
   D̃(π_0 ⊎ L_n) ≥ 1 ,     equivalently   Σ_{blue odd} ≥ Σ_{red even}   in the descending merge,
```
with equality iff the tie family `π_0 = {2^{n−1}+1, 2^{n−2},…,2,1}`. Via `(★-id)`
(`ladder-interleaving-identity.md`), `D̃(π_0⊎L_n) = 1 + 2Δ_n(π_0)`, so (★) ⟺ `Δ_n(π_0)≥0`.

This closes the `b=0` extremal base slice of GAP L, a wall open since round 3.

## Reusable sub-lemmas (all CERTIFIED)

**Lemma 0 (generalized ladder identity).** `Δ_m(R) = BO − RE` where `BO,RE` are the blue-odd-rank
and red-even-rank sums in the descending merge of `R` (red) and `L_m` (blue). Proof: subtract the
colour-sign sum `Σ_j τ_j w_j = ΣR − ΣL_m` from `D̃=Σ_j(−1)^{j−1}w_j`; `s_j−τ_j ∈ {0,±2}`.

**(I1) Rung-peel.** If every part of `R ≤ θ`: `D̃(R⊎L_m)=θ−D̃(R⊎L_{m−1})`, i.e.
`Δ_m(R)=2^m−1−ΣR−Δ_{m−1}(R)`.

**(I2) Branch-1 pair-removal.** If exactly one part `y>θ`, rest `≤θ`: `Δ_m(R)=Δ_{m−1}(R∖y)`.

**(I3) Red-peel.** If `y=max R>θ`: `D̃(R⊎L_m)=y−D̃((R∖y)⊎L_m)`, i.e.
`Δ_m(R)=2^m−1−Σ(R∖y)−Δ_m(R∖y)`.

**(I4) D̃ 1-Lipschitz.** Decreasing element values by total `ε` changes `D̃` by `≤ ε` (a single
decrease flips parity on an interval of measure `≤ δ`; triangle inequality). KEY: collapses any
*deficient*-total discrepancy bound to its *tight* case.

## Proof engine — mutual induction on ladder length `m`

Three statements, all `∀ m ≥ 1`:
- **(P_m)** — deficient LB: `#R ≤ m+1`, `ΣR ≤ 2^m` ⟹ `Δ_m(R) ≥ 0`.
- **(Q_m)** — complementary UB: `#R ≤ m+2`, parts `≤ 2^m`, `ΣR ≤ 2^{m+1}` ⟹
  `Δ_m(R) ≤ 2^{m+1}−1−ΣR`.
- **(LB_m)** — full deficient LB: `#R ≤ m+1`, parts `≤ 2^m`, `ΣR ≤ 2^{m+1}` ⟹
  `Δ_m(R) ≥ min(0, 2^m−ΣR)`.

Dependency (non-circular, grounded at `m=1`): `(P_m) ← {(P_{m−1}),(Q_{m−1})}`; `(LB_m) ← (P_m)`;
`(Q_m) ← (LB_m)`.

- **(P_m):** `ΣR≤2^m ⟹` ≤1 part `>θ`. Branch 1 (one `y>θ`): (I2) ⟹ `Δ_m(R)=Δ_{m−1}(R∖y)≥0` by
  `(P_{m−1})` (`#R∖y≤m`, `ΣR∖y<2^{m−1}`). Branch 2 (none `>θ`): (I1) ⟹ `Δ_m(R)≥0 ⟺
  Δ_{m−1}(R)≤2^m−1−ΣR`, which is exactly `(Q_{m−1})` (all its hyps hold).
- **(LB_m) from (P_m):** if `ΣR≤2^m`, direct from `(P_m)`. If `ΣR>2^m`, set `ε=ΣR−2^m`, shrink reds
  to total `2^m` (⟹ `R̂`, `(P_m)` gives `Δ_m(R̂)≥0`); by (I4)
  `Δ_m(R)−Δ_m(R̂)=½[(D̃-diff)−ε]≥−ε`, so `Δ_m(R)≥−ε=min(0,2^m−ΣR)`. **This Lipschitz collapse is
  the crux move — not circular, not hiding a ½.**
- **(Q_m) from (LB_m):** `y=max R`. If `y≤θ`: (I1)+`(NN)` D̃≥0 give `Δ_{m−1}(R)≥½(2^{m−1}−1−ΣR)≥−2^m`
  (uses `m≥1`). If `y>θ`: (I3) ⟹ conclusion ⟺ `Δ_m(R∖y)≥y−2^m`; `(LB_m)` on `R∖y` plus the part
  cap `y≤2^m` closes it. The uniform red-peel (I3) handles ANY number of reds `>θ` (the outline's
  "≤2 reds" undercount is irrelevant).
- **Base `m=1`:** `(P_1)`,`(Q_1)` proven directly by finite casework (`(Q_1) ⟺ w_1+w_3≤3`).

Take `m=n`, `R=π_0` (`ΣR=2^n≤2^n`, `#R≤n+1`): `(P_n)` gives `Δ_n(π_0)≥0`, i.e. (★). ∎

## Reviewer verification (round 13, exact `Fraction`, independent)
- Lemma 0 (`Δ=BO−RE`): 0 fails / 2·10⁴. (I1),(I2),(I3): 0 fails each (≈4·10⁴). (I4) Lipschitz:
  0 fails / 4·10⁴.
- `(P_m)`: 0 / 30k; `(Q_m)`: 0 / 41k; `(LB_m)`: 0 / 45k (m≤7, exact caps). Part-cap in `(Q_m)` is
  load-bearing (3230 fails when dropped).
- Target: `min D̃(π_0⊎L_n)=1` over all integer partitions of `2^n` into `≤n+1` parts, n=1..6, tie at
  `{2^{n−1}+1,…,1}` exactly.

## Status
FULLY PROVEN and certified (round 13). Closes GAP-P1′-a / the `b=0` extremal base slice. The
general-`b` lift (arbitrary dyadic-cut `F'` in place of `L`, GAP-P1′-b) is NOT covered by this lemma
and remains the sole open wall of GAP L.

Origin: `approaches/ladder-length-deficient-induction.md` (round 13). Self-contained from Lemma G +
`ladder-interleaving-identity.md`.
