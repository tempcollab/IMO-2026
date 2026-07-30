# Approach: ladder-length-deficient-induction (peel the top ladder rung; mutual induction on ladder length; b-lift = generalise blue from the uncut ladder L to an arbitrary budgeted dyadic refinement F')

## Spec concern (read first — a correction to the round-15 outline/reviewer)

The round-15 outline and reviewer both state the b-lift target as
`D̃(π₀ ⊎ F') ≥ 1` "for ANY dyadic refinement F' of the ladder L_n (ΣF'=2^n−1, all parts ≤ θ)."
**This statement, as written, is FALSE.** The claim needs, in addition to the rung-sum structure,
the GLOBAL cut-budget `Σ_{i} a_i ≤ n` (Xiang makes at most `n` marks total). Verified with exact
`Fraction`:

- **"Arbitrary F' with ΣF'=2^n−1, parts ≤ θ" fails.** `n=2`, `π₀={2,2}`, `F'={3/2,3/2}` (Σ=3=2²−1,
  parts ≤ θ=2): `D̃(π₀⊎F') = 0 < 1`. (1691 such counterexamples in 40000 random fractional trials.)
- **Rung-sum structure ALONE (unlimited cuts, no budget) fails.** `n=2`, rung 0 (=4) cut into 5
  parts, rung 2 (=1) cut into 4 parts (7 cuts total, `>n=2`): `D̃ = 0`.
- **Rung-sum structure AND budget `Σa_i ≤ n`: holds**, `min D̃ = 1`.

So the budget is load-bearing and **non-local**. Every generalised statement below carries the
budget explicitly.

## Status
partial — **Round-17 endpoint collapse, corrected (see §4.5).** The whole `(P̂_m)` induction is
reduced to the single slice `ΣR = 2^m` via two SOLID reductions: `(S1)` `ΣR ≤ 2^m−1` is TRIVIAL by
`D̃≥0` (subsuming the old Case I/IIa/IIb-1 work), and `(S2)` `2^m−1 < ΣR < 2^m` reduces to the
endpoint `ΣR = 2^m` by the certified Lipschitz `(I4)`. The all-or-nothing tooth-capture lever stays
REFUTED (`6481/8000`). **This round's fix:** the round-17 draft's `θ`-red-forcing split of the
endpoint is **RETRACTED** — its "no red `= θ ⟹` slack `D̃ ≥ 13/12`" claim is FALSE even on the
cut-top-rung endpoint (exact witness `R={3,3,2}`, `F'={2,2,2,1}`, `D̃ = 1`; `/tmp/r17_check.py`). The
endpoint is instead split by the **top rung of `F'`**: (S3-U big-red) closes by `(P̂_{m−1})`; the
pure-blue/`{θ,θ}` tail closes by the verified **anchor** `D̃(F') ≥ 1` (`≤ m−1` cuts), whose
cut-top-rung branch is exactly `(P̂_{m−1})` at endpoint (legitimate descent). **Two razor-tight
leaves remain OPEN:** (i) S3-U all-reds-`≤θ` → `(Q̂_{m−1})` endpoint; (ii) S3-C all-reds-`≤θ` → the
`(C)` overlap wall (`D̃ = 1` attained). Everything below the endpoint is SOLID. Whole GAP L: partial.

<details><summary>(round-16 status, retained)</summary>

partial — **Progress this round: the `ΣR ≤ θ` half of the cut-top-rung leaf is now CLOSED
completely and rigorously** (Case IIb, `ΣR ≤ θ`), via the previously-underused inheritance of the
FULL deficient lower bound `(L̂B_{m−1})` on `(R,F'')` (the file's earlier §4/§6 "only `(Q̂_{m−1})`
available" wording is corrected here). Together with the certified engine (all uncut-top-rung cases)
this leaves **exactly one wall**: the cut-top-rung leaf in the **oversized-red regime `ΣR > θ`**
(Case IIb with `ΣR > θ`, and its `(Q̂)`-mirror Case IIa). On that regime the correction `(C)` lands
on the certified GAP-P1 overlap `I_S = λ(O_{ρ₁}∩O_W)`, and — as verified below — the required bound
on `I_S` is **exactly equivalent to the target `D̃(R⊎F')≥1`** (it is razor-tight: the true minimum
of `Δ(R,F')` over oversized configs is `≈0.062 → 0`). So `I_S` is bounded here by a genuine
**per-tooth comb / parity-mismatch statement**, presented in §6 as the sole sharpened open gap, NOT
assumed as a lemma. Whole GAP L: partial.
</details>

## Approaches tried
- **(round 17, build) ENDPOINT COLLAPSE CORRECTED — retract the `θ`-red-forcing slack claim; split
  the endpoint by the top rung of `F'`** — PARTIAL. Banked `(S1)`,`(S2)`,`(anchor)` as SOLID (all
  `0` fails, exact `Fraction`), and **fixed the outline-reviewer's flagged flaw**: the round-17 claim
  "endpoint config with no red `= θ ⟹ D̃ ≥ 13/12`" is FALSE. The reviewer proposed restricting it to
  the cut-top-rung endpoint (claiming min `≈ 1.12`); **that too is FALSE** — exact witness
  `R = {3,3,2}` (`ΣR = 8 = 2^3`, all reds `< θ = 4`, no red `= θ`), `F' = {2,2,2,1}` (top rung
  `{2,2}` cut, budget `= 3 = m`) gives `D̃ = 1` exactly (`/tmp/r17_check.py`: `min D̃ = 1` over
  `4·10^5` cut-top-rung no-`θ` configs, `m = 3`). So the "no-`θ`-red" sub-case is razor-tight and the
  `θ`-red-peel + slack route is DEAD; retracted. Correct split: by the top rung `ρ₁` of `F'`.
  (a) **S3-U big-red red `> θ`:** `(A2) ⟹ (P̂_{m−1})` interior — CLOSED by descent.
  (b) **S3-U all reds `≤ θ`:** `(A1) ⟹ (Q̂_{m−1})` at endpoint `ΣR = 2^{(m−1)+1}` — OPEN (`(Q̂)`
     cut-top-rung branch).
  (c) **S3-C all reds `≤ θ`:** `(C)` overlap wall, razor-tight (`D̃ = 1` witness above) — OPEN.
  (d) **Anchor** `D̃(F') ≥ 1` (`≤ m−1` cuts): uncut top rung `= θ − D̃(F'') ≥ 1` (trivial); cut top
     rung `= (P̂_{m−1})` endpoint (strictly smaller, legitimate descent). Discharges the pure-blue
     endpoint and the `{θ,θ}` tail, but is NOT an independent endpoint closer (θ-forcing refuted).
  Net: the SOLID collapse (S1+S2+anchor-uncut) stands; the wall is now the honest pair of razor-tight
  endpoint leaves (b),(c) — no scalar/banned closer used, no overclaim.
- **(round 17) ENDPOINT COLLAPSE — the whole `(P̂_m)` reduces to the single slice `ΣR = 2^m`** —
  PARTIAL, major structural sharpening (all steps verified `0` fails, exact `Fraction`). See §4.5.
  Two SOLID new reductions dissolve almost the entire old wall, plus a refuted lever and a new
  promotable anchor:
  (a) **REFUTED — all-or-nothing tooth capture.** The round-17 "each tooth of `O_{ρ₁}` sits wholly
     inside a single band of `O_W`" finding is FALSE: `6481/8000` leaf configs have a `W`-part
     strictly inside a tooth (`/tmp/teeth_probe.py`). The rank/interleave form that survives is the
     full merged-order alternating sum `D̃(R⊎F')=Σ(−1)^{j−1}w_j`, i.e. the target itself
     (R8-banned merged-order object). So the per-tooth comb charge (all count-, all-or-nothing-, and
     magnitude-interleave forms) is DEAD; do not retry it.
  (b) **SOLID — `ΣR ≤ 2^m−1` is TRIVIAL.** `Δ(R,F')≥0 ⟺ D̃(R⊎F') ≥ ΣR−2^m+1`; for `ΣR ≤ 2^m−1`
     the RHS `≤ 0`, so `(NN)` `D̃≥0` closes it outright. This subsumes ALL of Case I, IIa and IIb-1
     for `ΣR ≤ 2^m−1` (the round-16 `(L̂B-inherit)`/`I_S≤D̃(ρ₁)` machinery for `ΣR≤θ` was
     unnecessary — `D̃≥0` already gives `Δ ≥ ½(2^m−1−ΣR) ≥ 0`). Verified `Δ<0` count `= 0`, min
     `Δ = 1/12 > 0` (`/tmp/sliver2.py`).
  (c) **SOLID — `2^m−1 < ΣR < 2^m` Lipschitz-reduces to the endpoint `ΣR = 2^m`.** Fill the reds up
     to `ΣR'=2^m` (feasible: `≥2` reds, each `≤θ`, capacity `(a₀+1)θ ≥ 2θ`), same count/budget. By
     `(I4)` (certified ½-injector), `D̃(R⊎F') ≥ D̃(R'⊎F') − (2^m−ΣR) ≥ 1 − (2^m−ΣR) = ΣR−2^m+1`,
     which is exactly `Δ(R,F')≥0`. Verified Lipschitz chain `0` violations (`/tmp/verify_chain.py`).
     The dual (IIa, one red `>θ`, `ΣR≤2^m`) is likewise trivial for `ΣR≤2^m−1` and fills to the
     same endpoint — removing the false-target `(A3)` mirror (`Δ(R₀,F')≤2^m−1−ΣR₀` is FALSE,
     `5096` violations, `/tmp/iia.py`).
  So **the entire b-lift = `(P̂_m)` at `ΣR = 2^m` exactly** (the b-lift instance `π₀`, `Σπ₀=2^n`).
  (d) **NEW promotable anchor (verified).** `D̃(F') ≥ 1` for any budgeted refinement `F'` of `L_m`
     with `≤ m−1` cuts (min `= 1`; FAILS at `m` cuts, min `= 0` — the spare budget unit is
     load-bearing) (`/tmp/anchor.py`). Uncut-top-rung sub-case is trivial: `D̃(F')=θ−D̃(F'')`,
     `D̃(F'')≤ΣF''=θ−1` (`0` violations, `/tmp/verify_chain.py`). ~~At the endpoint, tightness forces a
     red `= θ` (configs with no red `=θ` have `D̃ ≥ 13/12`)~~ **[RETRACTED in the round-17 build entry
     above: this slack claim is FALSE — witness `{3,3,2}⊎{2,2,2,1}`, `D̃=1`, no red `=θ`. The `θ`-red
     forcing route is dead; the anchor is used only for the pure-blue endpoint and `R={θ,θ}` tail.]**
- **(round 16) `(L̂B_{m−1})` inheritance + `ΣR≤θ` closure; TEETH residual sharpened** — PARTIAL,
  real advance. BANKED two sub-results: (a) `(L̂B_{m−1})` is admissible and exact on the leaf
  (because `a₁≥1` spends a budget unit, `a₀+b''≤m−1`), giving `Δ(R,F'')≥min(0,θ−ΣR)`; (b) the
  `ΣR≤θ` half of Case IIb closes in two lines via `(L̂B_{m−1})≥0` and `I_S≤D̃(ρ₁)≤p₁<θ`. Reduced the
  remaining wall to the oversized regime `ΣR>θ` and proved that the needed `I_S`-bound there is
  literally equivalent to the target (razor-tight, min `Δ→0`), so it must be closed by the per-tooth
  comb geometry — stated as a sharpened gap, not assumed. Verified 0 fails on all banked steps.
- **(round 15) budget-aware mutual induction `(P̂_m)/(Q̂_m)/(L̂B_m)`** — PARTIAL. Corrects the spec;
  generalises the certified engine; closes every uncut-top-rung case. Four reduction identities and
  `(P̂_m)/(Q̂_m)` verified `0` fails.
- **(round 13) base slice `(★)`** — SUCCESS, certified `lemmas/base-slice-star.md`. Retained.
- (prior rounds' history in `current.md`.)

## Current best
The b-lift `(P̂_m)` is rigorously reduced, via the budget-aware ladder-length mutual induction, to
the **single endpoint slice `ΣR = 2^m`** (SOLID: `(S1)` trivial band by `D̃≥0`, `(S2)` Lipschitz fill
to the endpoint by `(I4)`; §4.5). At the endpoint the split is by the **top rung of `F'`** (the
round-17 `θ`-red-forcing split is retracted — its slack premise is false, witness `{3,3,2}⊎{2,2,2,1}`
has `D̃ = 1`). Two of the four endpoint leaves CLOSE by induction descent: the big-red uncut-top-rung
leaf via `(P̂_{m−1})`, and the pure-blue / `R={θ,θ}` tail via the verified **anchor** `D̃(F') ≥ 1`
(`≤ m−1` cuts) whose cut-top-rung branch is exactly `(P̂_{m−1})` at endpoint. **Two razor-tight leaves
remain OPEN**, both on the measure-zero endpoint: (i) uncut top rung, all reds `≤ θ`, which by `(A1)`
is `(Q̂_{m−1})` at its own endpoint `ΣR = 2·2^{m−1}` (the `(Q̂)` cut-top-rung branch); (ii) cut top
rung, all reds `≤ θ`, where `(C)` gives `Δ(R,F') = Δ(R,F'') + ½θ + ½D̃(ρ₁) − I_S` and the required
`I_S ≤ Δ(R,F'') + ½θ + ½D̃(ρ₁)` is **equivalent to** the target (razor-tight, `D̃ = 1` attained). No
scalar `I_S`-ceiling, no merged-order/comb-capture, and no `θ`-forcing route can close either; these
are the sole open gaps.

## Proof

Throughout we use the **dyadic integer normalization** (certified Structure Lemma). For a finite
positive multiset `P`, `N_P(t) := #{p∈P: p>t}`, `O_P := {t>0: N_P(t) odd}`, and by the certified
**Lemma G** (`lemmas/greedy-claim.md`)
```
   D̃(P) = ∫_0^∞ 1[N_P(t) odd] dt = λ(O_P) = Σ_j (−1)^{j−1} w_j
```
(`w_1 ≥ w_2 ≥ …` the descending sort; tie-invariant). Two facts: **(NN)** `D̃ ≥ 0`; **(SD)**
(certified `peel-difference-bound.md`) for disjoint `A,B`, `D̃(A⊎B)=D̃(A)+D̃(B)−2λ(O_A∩O_B)`.

### 0. The exact b-lift target (with budget)

`L_m := {2^{m−1},…,2,1}` (uncut ladder, `ΣL_m=2^m−1`, top rung `θ:=2^{m−1}`). A **budgeted
refinement** of `L_m` is a multiset `F' = ⊎_{i=1}^{m} ρ_i` where each `ρ_i` is a finite positive
multiset with `Σρ_i = 2^{m−i}` (rung `i`); write `a_i := |ρ_i|−1 ≥ 0` (cuts in rung `i`) and
`b := Σ_{i=1}^m a_i` (total blue cuts). Every part of `F'` is `≤ θ`, and `ΣF' = 2^m − 1`.

For a red multiset `R` and any blue multiset `Z`, the **discrepancy functional** is
```
   Δ(R,Z) := ½( D̃(R⊎Z) − ΣR + ΣZ ).
```
When `Z = F'`, `ΣZ = 2^m − 1`, so `Δ(R,F') = ½(D̃(R⊎F') − ΣR + 2^m − 1)`.

**b-lift target.** For `π₀` (red, `Σπ₀ = 2^n`, `a₀ := |π₀|−1`) and `F'` a budgeted refinement of
`L_n` with `a₀ + Σ_{i=1}^n a_i ≤ n`, one has `D̃(π₀ ⊎ F') ≥ 1`, i.e. `Δ(π₀,F') ≥ 0`. Closing this
+ certified UB + Case A gives `c(n)=2^n/(2^{n+1}−1)`.

### 1. The budget-aware statements

For every integer `m ≥ 1`:

> **(P̂_m)** — *deficient lower bound.* Let `R` be red with `a₀:=|R|−1`, `ΣR ≤ 2^m`, and `F'` a
> budgeted refinement of `L_m` with `b:=Σa_i` blue cuts. If `a₀ + b ≤ m`, then `Δ(R,F') ≥ 0`.
>
> **(Q̂_m)** — *complementary upper bound.* Let `R` be red with `a₀:=|R|−1`, every part `≤ 2^m`,
> `ΣR ≤ 2^{m+1}`, and `F'` a budgeted refinement of `L_m` with `b` cuts. If `a₀ + b ≤ m+1`, then
> `Δ(R,F') ≤ 2^{m+1} − 1 − ΣR`.
>
> **(L̂B_m)** — *full deficient lower bound.* Let `R` (`a₀:=|R|−1`, parts `≤ 2^m`, `ΣR ≤ 2^{m+1}`)
> and `F'` budgeted refinement of `L_m`, `a₀ + b ≤ m`. Then `Δ(R,F') ≥ min(0, 2^m − ΣR)`.

When every blue rung is uncut (`b=0`, `F'=L_m`) these specialise **exactly** to the certified
`(P_m)/(Q_m)/(LB_m)`. The b-lift target is `(P̂_n)` at `ΣR = 2^n = 2^m`, `a₀ + b = n = m`.

All three are verified numerically (0 fails, `m ≤ 5`, exact `Fraction`; §7). We prove them by mutual
induction on `m`, and everything closes except the oversized-red cut-top-rung regime (§6).

### 2. Certified peel tools (imported) and the exact correction (C)

Import from `lemmas/`:

- **(I3′) arbitrary-blue red-peel** (`top-peel-general.md`): if `y = max R` exceeds every part of
  `Z` then `D̃(R⊎Z) = y − D̃((R∖y)⊎Z)`.
- **(I4) `D̃` is 1-Lipschitz** (`base-slice-star.md`): decreasing element values by total `ε`
  changes `D̃` by `≤ ε`. (The ½-injector.)
- **MAXPEEL** (`top-peel-general.md`): `D̃(P) = max(P) − D̃(P∖max)`.

Three level-measure reductions (certified in `lemmas/cut-top-rung-correction.md`):

**(A1) uncut-top-rung reduction (all reds ≤ θ).** If `ρ₁ = {θ}` and every red `≤ θ`, then with
`F'' := F'∖{θ}` (a budgeted refinement of `L_{m−1}`), `Δ(R,F') = (2^m − 1 − ΣR) − Δ(R,F'')`.

**(A2) uncut-top-rung reduction, one big red.** If `ρ₁={θ}` and exactly one red `y>θ` (rest `≤θ`),
then with `R₀:=R∖y`, `Δ(R,F') = Δ(R₀,F'')`.

**(A3) big-red red-peel (any top rung).** If `y = max R > θ`, then with `R₀ := R∖y`,
`Δ(R,F') = (2^m − 1 − ΣR₀) − Δ(R₀,F')`.

**(C) exact cut-top-rung correction (all reds ≤ θ).** Suppose `ρ₁` is CUT: `r := |ρ₁| ≥ 2`,
`Σρ₁ = θ`, every part `< θ`; every red `≤ θ`. Put `W := R⊎F''` (`F'' = F'∖ρ₁`, all parts `< θ`, so
`O_W ⊆ (0,θ)`). Then, with `E := {t∈(0,θ): N_{ρ₁}(t) even}`,
```
   D̃(R⊎F') = D̃(ρ₁) − D̃(W) + 2λ(E ∩ O_W),
```
equivalently `Δ(R,F') = Δ(R,F'') + ½θ + ½D̃(ρ₁) − I_S`, `I_S := λ(O_{ρ₁} ∩ O_W)`.

(All four proofs are in `lemmas/cut-top-rung-correction.md`; imported verbatim, not re-derived.)

### 3. Base case `m = 1`

`L_1 = {1}`, `θ=1`. A budgeted refinement `F'` of `L_1` is a partition of `1` into `a_1+1` parts.

- **(P̂_1)** (`a₀ + a_1 ≤ 1`, `ΣR ≤ 2`). Either `a_1 = 0` (`F'={1}=L_1`, certified `(P_1)`, `Δ≥0`)
  or `a₀ = 0` (`R={s}`, `0<s≤2`, `F'={p,1−p}`). For three numbers `{x≥y≥z≥0}`, `D̃ = x−y+z`. The
  three orderings of `{s,p,1−p}` give `Δ = 1−p`, `1−s`, `1−p` (as `s` largest/middle/smallest); each
  `≥0` because `p ≤ 1` always, and when `s` is not largest `s ≤ p ≤ 1`. Hence `Δ ≥ 0`. ✓
- **(Q̂_1)** (`a₀ + a_1 ≤ 2`, parts `≤ 2`, `ΣR ≤ 4`). With `P := R ⊎ F'`, `#P ≤ 4`, `ΣP = ΣR+1 ≤ 5`,
  parts `≤ 2`: `(3−ΣR)−Δ(R,F') = ½(6 − ΣP − D̃(P)) = (3 − w_1 − w_3) ≥ 0` because `w_1+w_3 ≤ 3`
  (else `w_1 ≥ w_2 ≥ w_3 > 1` with `#P=4` forces `ΣP>5`). ✓

### 4. Induction step `(P̂_m)` (`m ≥ 2`), assuming `(P̂_{m−1})`, `(Q̂_{m−1})`

`ΣR ≤ 2^m = 2θ` ⟹ at most one red `> θ`. Note first that, because `(P̂_{m−1})` is in hand, the FULL
deficient lower bound `(L̂B_{m−1})` is also available at scale `m−1` (it follows unconditionally from
`(P̂_{m−1})` via the certified Lipschitz collapse — proved in §5, `(L̂B_m)`-from-`(P̂_m)`, applied one
level down). This is the resource the round-15 file overlooked. Split on `ρ₁` and on `max R`.

**Case I — top rung uncut (`a₁=0`, `ρ₁={θ}`).**
- (Ia) some red `y>θ`: by **(A2)**, `Δ(R,F') = Δ(R₀,F'')`, `R₀=R∖y`, `ΣR₀ = ΣR−y < 2^{m−1}`,
  `a₀(R₀)=a₀−1`, `F''` a budgeted refinement of `L_{m−1}` with `b` cuts. Budget `(a₀−1)+b ≤ m−1`, so
  `(P̂_{m−1})` gives `Δ(R₀,F'') ≥ 0`, hence `Δ(R,F') ≥ 0`. ✓
- (Ib) all reds `≤ θ`: by **(A1)**, `Δ(R,F') ≥ 0 ⟺ Δ(R,F'') ≤ 2^m−1−ΣR`, exactly `(Q̂_{m−1})` for
  `R` against `F''` (hypotheses `a₀+b ≤ m=(m−1)+1`, parts `≤ θ`, `ΣR ≤ 2^m`). ✓

**Case II — top rung cut (`a₁≥1`).** The reds satisfy `ΣR ≤ 2^m`; every red `≤ θ` in (IIb), one red
`> θ` in (IIa).

**Lemma (L̂B-inherit).** *On the cut-top-rung leaf `(a₁≥1)`, with all reds `≤ θ`, one has*
```
   Δ(R,F'') ≥ min(0, θ − ΣR).
```
*Proof.* Apply `(L̂B_{m−1})` to the pair `(R, F'')`. Its hypotheses are met exactly:
(i) `F''` is a budgeted refinement of `L_{m−1}` (it is `F'∖ρ₁`); (ii) every red `≤ θ = 2^{m−1}` (case
hypothesis); (iii) `ΣR ≤ 2^m = 2^{(m−1)+1}` (the `(P̂_m)` hypothesis); (iv) the budget
`a₀ + b'' ≤ m−1`, where `b'' := Σ_{i≥2}a_i` is the number of cuts in `F''` — indeed the global budget
gives `a₀ + a₁ + b'' ≤ m`, and `a₁ ≥ 1` (the top rung is cut), so `a₀ + b'' ≤ m − a₁ ≤ m − 1`. Thus
`(L̂B_{m−1})` applies and yields `Δ(R,F'') ≥ min(0, 2^{m−1} − ΣR) = min(0, θ − ΣR)`. The spent cut
`a₁ ≥ 1` is exactly what frees the budget unit that makes `(L̂B_{m−1})` — not merely `(Q̂_{m−1})` —
admissible. ∎ *(Verified: `0` fails / `~70k` leaf configs, `m=2..5`; §7.)*

- **(IIa) some red `y > θ`.** By **(A3)**, `Δ(R,F') = (2^m−1−ΣR₀) − Δ(R₀,F')`, `R₀=R∖y`,
  `ΣR₀ = ΣR − y < 2^m − θ = θ`. This needs the UPPER bound `Δ(R₀,F') ≤ 2^m−1−ΣR₀` on a cut-top-rung
  config with `ΣR₀ < θ`. The available `(Q̂_m)` only gives `≤ 2^{m+1}−1−ΣR₀`, weaker by `2^m`; and by
  `(C)` for `R₀` the gap to the needed bound is a LOWER bound on `I_S₀ = λ(O_{ρ₁}∩O_{R₀⊎F''})`
  (the teeth must MEET `O_{R₀⊎F''}`). **(open — mirror of §6.)**

- **(IIb) all reds `≤ θ`.** By **(C)**, `Δ(R,F') = Δ(R,F'') + ½θ + ½D̃(ρ₁) − I_S`,
  `I_S = λ(O_{ρ₁} ∩ O_W)`, `W = R⊎F''`. Split on `ΣR`:

  **(IIb-1) `ΣR ≤ θ` — CLOSED.** By **(L̂B-inherit)**, `Δ(R,F'') ≥ min(0, θ−ΣR) = 0`. Hence
  ```
     Δ(R,F') ≥ ½θ + ½D̃(ρ₁) − I_S ≥ ½θ + ½D̃(ρ₁) − D̃(ρ₁) = ½( θ − D̃(ρ₁) ),
  ```
  using `I_S = λ(O_{ρ₁}∩O_W) ≤ λ(O_{ρ₁}) = D̃(ρ₁)`. Now `D̃(ρ₁) ≤ p₁` (the largest part): writing
  `ρ₁` descending `p₁ ≥ p₂ ≥ … ≥ p_r ≥ 0`, `D̃(ρ₁) = p₁ − (p₂−p₃) − (p₄−p₅) − ⋯ ≤ p₁`, each grouped
  term being `≥ 0`. Since `r ≥ 2` and `Σρ₁ = θ` with all parts positive, `p₁ < θ`. Therefore
  `θ − D̃(ρ₁) ≥ θ − p₁ > 0`, so `Δ(R,F') > 0`. (At `ΣR = θ` the floor is `min(0,0)=0`, so the same
  bound holds; the boundary is safe.) ✓ *(Verified: `0` fails on the `(b)`-chain over `119{,}119`
  configs `ΣR≤θ`, `m=2..5`; §7.)*

  **(IIb-2) `ΣR > θ` — OPEN (the TEETH residual).** Now `min(0,θ−ΣR) = θ−ΣR < 0`, the `(L̂B-inherit)`
  floor is negative, and combining it with the scalar ceiling `I_S ≤ D̃(ρ₁)` gives only
  `Δ(R,F') ≥ (θ−ΣR) + ½θ − ½D̃(ρ₁)`, which is inconclusive (see §6). This is the sole open leaf. ∎

So `(P̂_m)` is proved **for every case except the cut-top-rung, oversized-red leaf `ΣR > θ`** (IIb-2)
and its mirror (IIa).

### 4.5 Round-17 endpoint collapse (supersedes the §4/§6 case split on `ΣR`)

The round-16 split (IIb-1 `ΣR≤θ` vs IIb-2 `ΣR>θ`) is superseded by a cleaner, verified reduction.
Recall `Δ(R,F') ≥ 0 ⟺ D̃(R⊎F') ≥ ΣR − 2^m + 1` (since `ΣF' = 2^m−1`).

**(S1) `ΣR ≤ 2^m − 1`: TRIVIAL.** Then `ΣR − 2^m + 1 ≤ 0 ≤ D̃(R⊎F')` by `(NN)`. Closes *every*
case (I, IIa, IIb) with `ΣR ≤ 2^m−1` — no top-rung peel, no `(L̂B-inherit)`, no `I_S` bound.
*(Verified: `Δ<0` count `= 0`, min `Δ = 1/12`, `/tmp/sliver2.py`.)*

**(S2) `2^m−1 < ΣR < 2^m`: Lipschitz reduction to the endpoint.** Since `ΣR > 2^m−1 > θ` and each
red `≤ θ`, there are `≥ 2` reds with total slack `(a₀+1)θ − ΣR ≥ 2θ − ΣR = 2^m − ΣR =: ε ∈ (0,1)`.
Raise red values by total `ε` (greedy fill, each kept `≤ θ`) to `R'` with `ΣR' = 2^m`, same count
`a₀` and same budget. By `(I4)` (certified ½-injector, decrease `R'⊎F' ↦ R⊎F'` by total `ε`),
`D̃(R⊎F') ≥ D̃(R'⊎F') − ε ≥ 1 − ε = ΣR − 2^m + 1`, i.e. `Δ(R,F') ≥ 0`, **given the endpoint claim
`D̃(R'⊎F') ≥ 1`.** *(Verified: Lipschitz chain `0` violations, `/tmp/verify_chain.py`.)* The IIa
mirror (one red `> θ`, `ΣR ≤ 2^m`) fills identically to `ΣR = 2^m`; it needs **no** `(A3)`
upper-bound (whose reduced target `Δ(R₀,F') ≤ 2^m−1−ΣR₀` is FALSE, `/tmp/iia.py`).

**(S3) The endpoint `ΣR = 2^m` — the sole irreducible core (= the b-lift itself).** Prove
`D̃(R⊎F') ≥ 1` for `R` with `ΣR = 2^m`, parts `≤ 2^m`, `F'` a budgeted refinement of `L_m`, budget
`a₀ + b ≤ m`. At this slice `ΣR` is pinned to the integer `2^m` (maximal rigidity). Note first that,
since `ΣR = 2θ` and every red `≤ 2^m = 2θ`, **at most one red exceeds `θ`** (two reds `> θ` would
already sum to `> 2θ = ΣR`, contradicting the non-negativity of the remaining reds). We split on the
**top rung `ρ₁` of `F'`** (the correct split; the round-17 draft's `θ`-red-forcing split is
**retracted** — see the Correction below).

**(S3-U) top rung uncut (`a₁ = 0`, `ρ₁ = {θ}`).**
- *some red `y > θ`.* By **(A2)**, `Δ(R,F') = Δ(R₀,F'')`, `R₀ = R∖y`, `ΣR₀ = 2^m − y < 2^m − θ = θ`,
  `a₀(R₀) = a₀ − 1`, `F''` a budgeted refinement of `L_{m−1}` with `b` cuts; budget `(a₀−1)+b ≤ m−1`.
  Since `ΣR₀ < θ = 2^{m−1}`, `(P̂_{m−1})` gives `Δ(R₀,F'') ≥ 0`, hence `Δ(R,F') ≥ 0`. **CLOSED** by
  `(P̂_{m−1})` (a strictly smaller instance — legitimate induction descent). ✓
- *all reds `≤ θ`.* By **(A1)**, `Δ(R,F') = (2^m − 1 − ΣR) − Δ(R,F'') = −1 − Δ(R,F'')`, so
  `Δ(R,F') ≥ 0 ⟺ Δ(R,F'') ≤ −1`. This is exactly `(Q̂_{m−1})` for `(R,F'')` **at its own endpoint**
  `ΣR = 2^m = 2^{(m−1)+1}` (parts `≤ θ = 2^{m−1}`, budget `a₀+b ≤ m = (m−1)+1`): `(Q̂_{m−1})` gives
  `Δ(R,F'') ≤ 2^{(m−1)+1} − 1 − ΣR = 2^m − 1 − 2^m = −1`, exactly as needed. **This reduces to the
  `(Q̂_{m−1})` endpoint**, whose cut-top-rung sub-branch (top rung of `F''` cut, at the top of the
  range `ΣR = 2·2^{m−1}`) is **OPEN** (§5, the `(Q̂)` cut-top-rung `ΣR > 2^{m−1}` branch). — open.

**(S3-C) top rung cut (`a₁ ≥ 1`, every `F'` part `< θ`).**
- *some red `y > θ`.* By **(A3)**, `Δ(R,F') = (2^m − 1 − ΣR₀) − Δ(R₀,F')`, `R₀ = R∖y`,
  `ΣR₀ = 2^m − y < θ`, still a cut-top-rung config; this needs the **upper** bound
  `Δ(R₀,F') ≤ 2^m − 1 − ΣR₀`, i.e. `(Q̂_m)` on a cut-top-rung config — the `(Q̂)` cut-top-rung wall
  (§5). — open (mirror).
- *all reds `≤ θ`.* By **(C)**, `Δ(R,F') = Δ(R,F'') + ½θ + ½D̃(ρ₁) − I_S`, `I_S = λ(O_{ρ₁}∩O_W)`,
  `W = R⊎F''`. Here `ΣR = 2θ > θ`, so `(L̂B-inherit)` gives only `Δ(R,F'') ≥ min(0,θ−ΣR) = −θ`, and
  with the scalar ceiling `I_S ≤ D̃(ρ₁)` this yields `Δ(R,F') ≥ −½θ − ½D̃(ρ₁)`, **vacuous**. This is
  the razor-tight `(C)` overlap wall, and it **is** razor-tight: the exact witness `R = {3,3,2}`
  (`ΣR = 8 = 2^3`), `F' = {2,2,2,1}` (top rung `θ = 4` cut into `{2,2}`, budget `a₀+b = 2+1 = 3 = m`)
  has `D̃(R⊎F') = 1` exactly. — **open (the sole razor-tight core).**

**Correction (retracts the round-17 `θ`-red forcing).** The round-17 draft claimed the endpoint
splits as "some red `= θ` (peel via `(A3)`/anchor)" vs "no red `= θ` (**slack**, `D̃ ≥ 13/12`)". **The
slack claim is FALSE**, even on the cut-top-rung endpoint that the outline-reviewer proposed to
restrict it to. Exact witness (`m = 3`, `θ = 4`): `R = {3,3,2}` (`ΣR = 8 = 2^m`, all reds `< θ`, no
red `= θ`), `F' = {2,2,2,1}` (top rung `{2,2}` cut, budget `= 3 = m`) gives
`D̃({3,3,2}⊎{2,2,2,1}) = 3−3+2−2+2−2+1 = 1` exactly. *(Verified `/tmp/r17_check.py`: over `4·10^5`
random cut-top-rung endpoint configs with no red `= θ`, `min D̃ = 1` at `m = 3`.)* Hence the
"no-`θ`-red" sub-case is itself razor-tight; the `θ`-red-peel + slack route **cannot** close the
endpoint and is retracted. The correct split is by the top rung of `F'` as above.

**Anchor lemma (verified, promotable — NOT an independent endpoint closer).** *For any budgeted
refinement `F'` of `L_m` with `≤ m−1` cuts, `D̃(F') ≥ 1`.* **Proof.** Split on the top rung `ρ₁`.
If uncut (`ρ₁={θ}`), then `θ = max F'` and MAXPEEL gives `D̃(F') = θ − D̃(F'')` with
`D̃(F'') ≤ ΣF'' = θ − 1` (by `(NN)`-complement `D̃(P) ≤ ΣP`), so `D̃(F') ≥ 1`. If cut (`a₁ ≥ 1`), view
`ρ₁` as a red multiset `R̄` with `ΣR̄ = θ = 2^{m−1}` and `a₀(R̄) = a₁`; then `D̃(F') = D̃(R̄ ⊎ F'')`,
which is **exactly `(P̂_{m−1})` at its endpoint** `ΣR̄ = 2^{m−1}`, budget `a₁ + b'' ≤ m−1` (the
`≤ m−1`-cut hypothesis). So the anchor's cut-top-rung branch is a strictly smaller instance of the
endpoint claim — a legitimate induction descent (base `m = 1` proven, §3), **not circular**. ∎
*(Verified `0` fails / min `D̃ = 1` at `≤ m−1` cuts, and min drops to `0` at `m` cuts —
`/tmp/r17_verify.py`, `m ≤ 5`.)* The anchor discharges the pure-blue endpoint and the `R = {θ,θ}`
tail (two `θ`-red peels), but — because `θ`-red forcing is **refuted** — it does **not** reduce the
general endpoint; it is a self-consistent component of the induction that closes iff the whole
endpoint closes.

**Open (S3), honest.** The endpoint `ΣR = 2^m` splits into four leaves; two close by induction
descent (S3-U big-red → `(P̂_{m−1})`; the pure-blue/`{θ,θ}` tail → anchor `= (P̂_{m−1})` endpoint),
and **two remain open, both razor-tight, both on the measure-zero endpoint**:
(i) **S3-U, all reds `≤ θ`** → `(Q̂_{m−1})` at its endpoint (cut-top-rung `(Q̂)` branch open);
(ii) **S3-C, all reds `≤ θ`** → the `(C)` overlap wall `I_S ≤ Δ(R,F'')+½θ+½D̃(ρ₁)` (`D̃ = 1`
attained at `{3,3,2}⊎{2,2,2,1}`), which by §6 is literally equivalent to the target;
plus the big-red mirrors of both, which reduce to the `(Q̂)` cut-top-rung upper bound. None is a
scalar summary; none re-uses the refuted all-or-nothing capture; the `θ`-red-forcing route is
retracted. This is the sole remaining wall; verdict `partial`.

### 5. `(L̂B_m)` from `(P̂_m)`, and `(Q̂_m)` from `(L̂B_m)`

**(L̂B_m) from (P̂_m).** If `ΣR ≤ 2^m`, `(P̂_m)` gives `Δ(R,F') ≥ 0 = min(0,2^m−ΣR)`. If `ΣR > 2^m`,
set `ε := ΣR − 2^m`; shrink red values by total `ε` (discard any reaching `0`) to `R̂` with
`ΣR̂ = 2^m`, `a₀(R̂) ≤ a₀`, parts `≤ 2^m`; `(P̂_m)` gives `Δ(R̂,F') ≥ 0`. By **(I4)** applied to
`R⊎F' ↦ R̂⊎F'` (total decrease `ε`), `D̃(R⊎F') − D̃(R̂⊎F') ≥ −ε`, so
`Δ(R,F') − Δ(R̂,F') = ½[(D̃(R⊎F')−D̃(R̂⊎F')) − ε] ≥ −ε`, whence
`Δ(R,F') ≥ −ε = 2^m−ΣR = min(0,2^m−ΣR)`. ✓ *(the certified ½-injecting Lipschitz collapse; it
depends on the open leaves only through `(P̂_m)`, so introduces no new leaf. This is the derivation
used one level down in §4 to make `(L̂B_{m−1})` available.)*

**(Q̂_m) from (L̂B_m).** Let `y := max R` (`y=0` if `R=∅`).
- `y ≤ θ`, top rung uncut: by **(A1)**, `(Q̂_m) ⟺ Δ(R,F'') ≥ −2^m`; by `(NN)`,
  `Δ(R,F'') ≥ ½(−ΣR + 2^{m−1}−1) ≥ −2^m`. ✓
- `y ≤ θ`, top rung cut: by **(C)** need an upper bound; via `(L̂B-inherit)`/`(Q̂_{m−1})` and
  `I_S ≥ 0`, one gets `Δ(R,F') ≤ Δ(R,F'') + ½θ + ½D̃(ρ₁)`. If `ΣR ≤ 2^m`, `(Q̂_{m−1})` (admissible,
  `a₀+b''≤m−1≤m`) gives `Δ(R,F'') ≤ 2^m−1−ΣR`, hence
  `Δ(R,F') ≤ 2^m−1−ΣR + ½θ + ½D̃(ρ₁) ≤ 2^{m+1}−1−ΣR` (since `½θ+½D̃(ρ₁) < θ < 2θ = 2^m`). ✓ *(the
  `ΣR ≤ 2^m` cut-top-rung branch of `(Q̂_m)` closes via `I_S ≥ 0`.)* For `ΣR ∈ (2^m, 2^{m+1}]` this
  crude `I_S ≥ 0` step is the same oversized-regime overlap wall as §6; but the `(P̂_m)` induction
  only ever invokes `(Q̂_m)` at `ΣR < θ` (Case IIa peels one red `> θ`, leaving `ΣR₀ < θ`), so the
  `ΣR ≤ 2^m` branch suffices for `(P̂_m)`. **(The `ΣR > 2^m` cut-top-rung branch of `(Q̂_m)` is open —
  same wall, not needed by `(P̂_m)`.)**
- `y > θ`: by **(A3)**, `(Q̂_m) ⟺ Δ(R∖y,F') ≥ y − 2^m`. Apply `(L̂B_m)` to `R∖y`
  (`Σ(R∖y) < 2^{m+1}`, parts `≤ 2^m`, `a₀−1+b ≤ m`): `Δ(R∖y,F') ≥ min(0, 2^m − Σ(R∖y))`. If
  `Σ(R∖y) ≤ 2^m`, `0 ≥ y−2^m` (as `y ≤ 2^m`); else `2^m−Σ(R∖y) ≥ y−2^m ⟺ ΣR ≤ 2^{m+1}`, which
  holds. ✓ *(uniform red-peel; any number of reds `>θ`.)*

### 6. The open gaps (honest, sharpened) — superseded framing, retained for the `(C)` residual

**Note (round 17).** The `ΣR`-split of this section (Case IIb-1 `ΣR≤θ` vs IIb-2 `ΣR>θ`) is
**superseded by §4.5**: by `(S1)` everything with `ΣR ≤ 2^m − 1` is trivial, so the entire
"oversized-red `ΣR > θ`" residual below is trivial *except* at the endpoint `ΣR = 2^m`. What survives
is exactly the endpoint `(C)` overlap wall (§4.5 leaf S3-C, all reds `≤ θ`) and the `(Q̂)`
cut-top-rung endpoint (leaf S3-U, all reds `≤ θ`). The `(†)`/`(‡)` analysis below is the exact
algebraic form of that residual and is retained for reference; it is NOT assumed as a lemma (it is
equivalent to the target).

Collecting §3–§5: the budget-aware mutual induction `(P̂_m) ← {(P̂_{m−1}),(Q̂_{m−1})}`,
`(L̂B_m) ← (P̂_m)`, `(Q̂_m) ← (L̂B_m)` closes **every case except the cut-top-rung, oversized-red
leaf** — Case IIb-2 (`a₁≥1`, all reds `≤θ`, `ΣR > θ`) and its mirror Case IIa (`a₁≥1`, one red `y>θ`,
which forces `ΣR₀ < θ` but needs the `(Q̂)`-direction bound). When all blue rungs are uncut the whole
engine reduces to the certified `(P_m)/(Q_m)/(LB_m)`, recovering the base slice `(★)`.

**Exact form of the residual.** On IIb-2, by `(C)` the claim `Δ(R,F') ≥ 0` is
```
   (†)   I_S ≤ Δ(R,F'') + ½θ + ½D̃(ρ₁),      I_S = λ(O_{ρ₁} ∩ O_W),  W = R⊎F''.
```
**This is NOT a lemma we may assume.** Using the mass identity `D̃(W) = 2Δ(R,F'') + ΣR − (θ−1)` and
the even-complement identity `λ(E∩O_W) = D̃(W) − I_S` (`E = (0,θ)∖O_{ρ₁}`), `(†)` rearranges to the
purely geometric
```
   (‡)   λ(O_W ∩ O_{ρ₁}) − λ(O_W ∩ E) ≤ D̃(ρ₁) + 2θ − 1 − ΣR.
```
At the extremal `ΣR = 2θ` (the b-lift instance), the RHS is `D̃(ρ₁) − 1`, and moving the negative
term over, `(‡)` becomes
```
   λ(O_{ρ₁} ∩ E_W) + λ(E ∩ O_W) ≥ 1,     E_W := (0,θ)∖O_W,
```
i.e. `λ{t∈(0,θ): N_{ρ₁}(t), N_W(t) differ in parity} ≥ 1`, which is exactly `D̃(R⊎F') ≥ 1` (since
`N_{R⊎F'} = N_W + N_{ρ₁}` on `(0,θ)` and `D̃(R⊎F')` is the measure of the parity-mismatch set). So
`(†)`/`(‡)` are **literally equivalent to the target**; any purely scalar ceiling on `I_S`
(`I_S ≤ D̃(ρ₁)`, `I_S ≤ D̃(W)`, or `I_S ≤ min(·,·)`) telescopes to the vacuous R14 estimate and is
**banned/proved vacuous** (fails `62.4%` of oversized configs per the outline reviewer; and the true
`Δ(R,F')` bottoms at `≈0.062 → 0` over oversized configs — §7 — so the bound is razor-tight with no
scalar slack).

**The comb geometry (the concrete, non-scalar lever — the mechanism that must be proved).** Sort
`ρ₁` descending `p₁ > p₂ > ⋯ > p_r` (`r = a₁+1 ≥ 2`). Then
```
   O_{ρ₁} = (p₂,p₁) ∪ (p₄,p₃) ∪ ⋯   (+ (0,p_r) if r is odd),
```
a comb of exactly `⌈r/2⌉` disjoint **teeth**, and `D̃(ρ₁) = (p₁−p₂)+(p₃−p₄)+⋯`. (Verified: teeth
count `= ⌈r/2⌉` on all distinct-part configs; §7.) Thus `a₁ = r−1` controls the **tooth COUNT**, NOT
the tooth measure — indeed `D̃(ρ₁)` can be pushed to `θ⁻` for any `r` (one dominant part `θ−(r−1)ε`
plus `r−1` fragments `ε`), so no `a₁`-monotone shrinkage of `D̃(ρ₁)` or `I_S` may be assumed. Then
```
   I_S = Σ_{teeth} λ( tooth ∩ O_W ),
```
and `O_W` is itself a step-function odd set with `≤ |W| = a₀ + b'' + m ≤ 2m − a₁` boundary points
(budget-limited: `a₀ + b'' ≤ m − a₁`). The intended closure is a **per-tooth charge**: bound
`Σ_{teeth} λ(tooth ∩ O_W)` against `O_W`'s budget-limited breakpoints via the even-complement
identity, using that in the `ΣR > θ` regime the oversized red mass forces `O_W` to occupy the low
band where the teeth alternate — a pigeonhole / inclusion–exclusion across the `⌈r/2⌉` teeth versus
the `≤ 2m − a₁` breakpoints of `O_W`.

**What remains (exactly).** A rigorous per-tooth lower bound on the "saved" measure
`Σ_{teeth} λ(tooth ∩ E_W) + λ(E ∩ O_W) ≥ ΣR − 2θ + 1` (equivalently `(‡)`), derived from the comb
geometry of `O_{ρ₁}` and the budget-limited breakpoint count of `O_W` — NOT from any scalar summary
of `I_S`. The mirror (Case IIa / the `(Q̂)` cut-top-rung `ΣR>2^m` branch) needs the dual: a per-tooth
LOWER bound on `I_S` (teeth actually MEET `O_W`), which does not follow from the upper-bound argument
for free. **We have NOT closed either; we do NOT assume `(†)`.** This is the sole remaining wall; the
honest verdict is `partial`.

### 7. Numerical verification (exact `Fraction`)

**Round-17 build (this round), exact `Fraction`:**
- **`D̃` form.** `D̃(P) = Σ(−1)^{i−1}w_i` (descending) `= λ{t: N_P(t) odd}` cross-checked equal on
  `2000` random multisets (`/tmp/r17_verify.py`, `0` mismatch).
- **`(S1)` trivial band.** `Δ(R,F') ≥ 0` on `ΣR ≤ 2^m−1`: `0` fails over `40000` configs per
  `m ∈ {2,3,4,5}` (`/tmp/r17_s1s2.py`; `minΔ = 203/3200, 49/125, 2951/3200, 17713/8000`).
- **`(S2)` Lipschitz fill.** `D̃(R⊎F') ≥ D̃(R'⊎F') − ε` on `2^m−1 < ΣR < 2^m` with feasible fill to
  `ΣR' = 2^m` (each red `≤ θ`, count+budget preserved): `0` violations, `m ∈ {2..5}`
  (`/tmp/r17_s1s2.py`).
- **Anchor `D̃(F') ≥ 1` (`≤ m−1` cuts).** `min D̃ = 1`, `0` fails / `20000` per `m ∈ {2..5}`; at `m`
  cuts `min D̃` drops to `0` (`m=2,3`) — spare budget unit load-bearing (`/tmp/r17_verify.py`).
- **RETRACTION of the `θ`-red-forcing slack claim.** Cut-top-rung endpoint, all reds `≤ θ`, no red
  `= θ`: `min D̃ = 1` at `m = 3` (over `4·10^5` configs), with explicit witness `R = {3,3,2}`,
  `F' = {2,2,2,1}` (`D̃ = 1`) — so the sub-case is razor-tight, not slack (`/tmp/r17_check.py`,
  `/tmp/r17_witness.py`).
- **Endpoint target holds.** `D̃(R⊎F') ≥ 1` on the full endpoint `ΣR = 2^m` (both uncut- and
  cut-top-rung): `0` fails, `m ∈ {2,3,4}` (`/tmp/r17_endpoint.py`) — confirming the wall is genuine
  (target true) and razor-tight (`min = 1`).

Round-16 and earlier scripts `/tmp/tprobe.py`, `/tmp/tprobe2.py`, `/tmp/tprobe3.py`, `/tmp/probe4.py`,
exact rationals:

- **`(L̂B-inherit)` admissibility.** `Δ(R,F'') ≥ min(0,θ−ΣR)` on the cut-top-rung leaf: `0` fails /
  `~70{,}000` trials (`/tmp/probe4.py`, `fail_LB=0`) and `0` fails again in `/tmp/tprobe.py`
  (`fLB=0`, `m=2..5`).
- **`ΣR≤θ` closure (IIb-1).** `fail_final = 0` over `nA = 51{,}509` (`m=2`) … `43{,}665` (`m=5`)
  configs with `ΣR≤θ` (`/tmp/tprobe.py`); and the explicit bound chain `Δ(R,F') ≥ ½(θ−D̃(ρ₁)) ≥ 0`
  holds with `0` violations over `119{,}119` such configs (`/tmp/tprobe2.py`, `bad_b=0`), with
  `D̃(ρ₁) ≤ max part` never violated (`bad_Dmax=0`).
- **Comb structure.** `O_{ρ₁}` has exactly `⌈r/2⌉` teeth for `r` distinct positive parts
  (`/tmp/tcheck.py`; the only counted anomalies are degenerate cases where the random generator
  emitted a zero part, i.e. effectively fewer positive parts — the claim holds for every genuine
  `r`-part cut rung).
- **Residual (IIb-2) is real and razor-tight.** True `Δ(R,F') ≥ 0` always on oversized configs
  (`fail_final = 0`, `nB = 2{,}791..9{,}304`, `/tmp/tprobe.py`), yet the trivial route
  (`(L̂B-inherit)` floor + `I_S≤D̃(ρ₁)`) fails `~34%` (`946/2791` up to `3257/9304`); and the true
  minimum of `Δ(R,F')` over oversized configs is `31/500 = 0.062 → 0` (`/tmp/tprobe3.py`), so the
  bound `(†)` is tight and no scalar `I_S`-ceiling can close it.
- **Statements/identities.** `(P̂_m)`: `0`/`5·10⁴`; `(Q̂_m)`: `0`/`6·10⁴`; `(A1),(A2),(A3)`: `0`
  each; `(C)`: `0`/`2.2·10⁴` (round 15, certified). Base slice `(★)`: certified, `min D̃ = 1`.

## Promotable lemmas

0a. **(S1) trivial band.** For `R` (parts `≤ 2^m`) with `ΣR ≤ 2^m − 1` and `F'` any budgeted
   refinement of `L_m`, `Δ(R,F') ≥ 0`. *Proof:* `Δ(R,F') ≥ 0 ⟺ D̃(R⊎F') ≥ ΣR − 2^m + 1` (since
   `ΣF' = 2^m − 1`); the RHS is `≤ 0` on this band, and `D̃ ≥ 0` by `(NN)`. Proved in §4.5; verified
   `0` fails / `1.6·10^5`. No case split, no budget hypothesis needed. Certifiable stand-alone.

0b. **(S2) Lipschitz reduction to the endpoint.** For `R` (all reds `≤ θ`) with
   `2^m − 1 < ΣR < 2^m`, filling the reds to `ΣR' = 2^m` (feasible: `≥ 2` reds, capacity
   `(a₀+1)θ ≥ 2θ`, count+budget preserved) gives `Δ(R,F') ≥ 0` **provided** `D̃(R'⊎F') ≥ 1` at the
   endpoint. *Proof:* by `(I4)`, decreasing `R'⊎F' ↦ R⊎F'` by total `ε := 2^m − ΣR ∈ (0,1)` changes
   `D̃` by `≤ ε`, so `D̃(R⊎F') ≥ D̃(R'⊎F') − ε ≥ 1 − ε = ΣR − 2^m + 1`. Proved in §4.5; verified `0`
   Lipschitz violations. Certifiable stand-alone (a conditional reduction).

0c. **(Anchor) `D̃(F') ≥ 1` for a budgeted refinement of `L_m` with `≤ m−1` cuts.** *Proof:* uncut
   top rung ⟹ `D̃(F') = θ − D̃(F'') ≥ θ − ΣF'' = 1`; cut top rung ⟹ `D̃(ρ₁ ⊎ F'') = (P̂_{m−1})` at
   endpoint `ΣR = 2^{m−1}`, budget `a₁ + b'' ≤ m−1` (strictly smaller instance, legitimate descent;
   base `m = 1` proven). Proved in §4.5; verified `min D̃ = 1` at `≤ m−1` cuts, drops to `0` at `m`
   cuts (spare unit load-bearing). Certifiable stand-alone modulo `(P̂_{m−1})` at endpoint (the
   uncut-top-rung branch is unconditional).

1. **(L̂B-inherit) — full deficient lower bound inherited on the cut-top-rung leaf.** On Case II of
   `(P̂_m)` (top rung cut, `a₁ ≥ 1`), with all reds `≤ θ` and `ΣR ≤ 2^m`, the pair `(R,F'')`
   satisfies `Δ(R,F'') ≥ min(0, θ − ΣR)`. *Reason:* `a₁ ≥ 1` spends a budget unit, so
   `a₀ + b'' ≤ m − a₁ ≤ m − 1`, which — together with reds `≤ θ = 2^{m−1}` and `ΣR ≤ 2^m` — is
   exactly the hypothesis set of `(L̂B_{m−1})` (itself derived from `(P̂_{m−1})` via the certified
   Lipschitz collapse). Proved in §4; verified `0` fails / `~70k`. *(Corrects the round-15 file,
   which inherited only `(Q̂_{m−1})`.)*

2. **(ΣR≤θ cut-top-rung closure) — Case IIb-1.** On the cut-top-rung leaf with all reds `≤ θ` and
   `ΣR ≤ θ`, `Δ(R,F') ≥ ½(θ − D̃(ρ₁)) > 0`. *Proof:* `(L̂B-inherit)` gives `Δ(R,F'') ≥ 0`; then by
   `(C)`, `Δ(R,F') ≥ ½θ + ½D̃(ρ₁) − I_S ≥ ½θ − ½D̃(ρ₁)` (via `I_S ≤ D̃(ρ₁)`), and
   `D̃(ρ₁) ≤ p₁ < θ` (alternating sum `≤` largest part; largest part `< θ` since the rung is cut).
   Proved in §4 (IIb-1); verified `0` fails / `119{,}119`. Stand-alone, certifiable regardless of the
   residual.

3. **Exact cut-top-rung correction (C) + uncut reductions (A1),(A2),(A3)** — already certified
   (`lemmas/cut-top-rung-correction.md`); imported, not re-derived.
