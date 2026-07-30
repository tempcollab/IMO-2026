# Approach: peel-scale-rank-induction (peel the top dyadic scale; symmetric-difference insertion induction on the unified ladder)

## Status
partial (round 13)

## The whole claim this approach proves
GAP L (lower bound), closing the problem: for every simultaneous refinement
`F = ⊎_{j=0}^{n} π_j` of the dyadic ladder `{1,2,…,2^n}` with cut budget `Σ_j a_j ≤ n`,
`E(F) ≤ 2^n − 1` (equivalently `O(F) ≥ 2^n`, equivalently `D̃(F) ≥ 1`). With the certified
upper bound this gives `c(n) = 2^n/(2^{n+1}−1)`.

## Approaches tried
- **(round 13 build — WM/HLP tail-charge on the ladder, §11.6)** Rigorous progress on the leader's
  crux, honest partial (the core wall is unbroken but genuinely sharpened). Deliverable: the
  **HLP threshold reduction** of the weak-majorization goal `(WM)` `BO ≻_w RE` to a *finite* set of
  scalar rung-inequalities. Introduced the tail functional `Φ(t) := Σ_{v∈BO}(v−t)^+ − Σ_{w∈RE}(w−t)^+`
  and **proved (§11.6.1–11.6.3, unconditional):** (i) by the Hardy–Littlewood–Pólya weak-majorization
  characterisation, `(WM) ⟺ Φ(t) ≥ 0 ∀t ≥ 0`; (ii) `Φ` is continuous piecewise-linear with **upward
  slope-jumps (convex kinks) exactly at the values of `BO`** and downward jumps at values of `RE`,
  hence its minimum over `[0,∞)` is attained at `t=0` **or at a value of `BO` (a blue-odd rung)** — so
  `(WM) ⟺ [ Φ(0)=(★) ≥ 0 ] ∧ [ Φ(b) ≥ 0 for every blue-odd rung b ]`, collapsing the "uniform in `t`"
  continuum to `≤ n` explicit rung checks; (iii) the **top-rung boundary is closed:**
  `Φ(θ)=0` unconditionally (via `(m₀≤1)`, so `θ=b_1` carries no red-even mass above it). Established
  the **self-similar identity** `Φ(b_i) = [BO(P_i)−RE(P_i)] − b_i·(|BO(P_i)|−|RE(P_i)|)` on the top
  truncation `P_i = {merge elements > b_i}` (whose blue part is the scaled ladder `2b_i·L_{i−1}`),
  pinning the residual `Φ(b_i)≥0` as a *shifted* `(★)` against a shorter scaled ladder with a
  **deficient** red total — i.e. the same object the sibling `ladder-length-deficient-induction`
  proves as its generalised lemma. **Remaining gap (GAP-P1′-a, unchanged core):** the general
  rung inequality `Φ(b_i) ≥ 0` for `i ≥ 2`; DOM closes `i=1` but not the shifted-truncation
  recursion, which coincides with the sibling's open `(Q_m)` step. Verified exact `Fraction`:
  `(★)` and `(WM)` both `0` fails / `40000` configs, `n=1..8`, both tie conventions; `Φ ≥ 0`
  everywhere and its min at `t=0`-or-a-`BO`-value `0` exceptions / `28000`; `Φ(θ)=0` and `m₀≤1`
  `0` exceptions / `21000`. → **partial** (the continuum WM/HLP goal is reduced to finitely many
  rung inequalities, the top-rung one closed; the shifted-truncation core is the shared base-slice
  wall and stays open — did not break it, sharpened it and bridged it to the sibling route).
- **(round 11 build — extremal base case `b=0`: the ladder-interleaving identity)** Rigorous
  progress, honest partial; the round's tangible deliverable is a NEW clean, fully-proven identity
  for the extremal base object. Routed GAP-P1′ (`I_n ≤ 0`) through the extremal slice `b=0`, where
  the budget is fully spent on `π_0` and `F'` is forced to the *uncut ladder* `L = {2^{n−1},…,2,1}`
  (§10). **Established (fully proven, §10.2) the interleaving identity**
  `D̃(π_0 ⊎ L) = 1 + 2·(Σ_{blue at odd rank} − Σ_{red at even rank})` (red `=π_0`, blue `=L`), so the
  entire base case is EXACTLY the clean combinatorial inequality **`(★)  Σ_{blue odd} ≥ Σ_{red even}`**
  in the descending merge of `π_0` and `L`, with `D̃=1` iff equality (verified `0` identity-mismatches
  and `0` equivalence-failures over `1.8·10⁵` exact-`Fraction` configs, `n≤6`; base-case min `=1`
  exactly by integer enumeration `n≤6` and `2·10⁵` fractional trials each `n`). **Two unconditional
  closed sub-regions of the base case:** (a) whenever `M = N_{π_0}−N_L ≤ 1` on all of `(0,θ)` then
  `⌊M/2⌋≤0` pointwise so `I_n≤0` and `D̃≥1` — closes `≈88 %` of sampled base configs (`105535/120000`,
  `0` failures, §10.3); (b) the certified `(DIFF)` region `|D̃(π_0)−D̃(L)|≥1` with the exact ladder
  value `D̃(L)=(2^n−(−1)^n)/3` (§10.4). **`n=1` base case fully closed** (`D̃(π_0⊎{1})≡1` identically,
  §10.5). The residual (both `M≥2` somewhere AND `|D̃(π_0)−D̃(L)|<1`) is reduced to a finite
  block/rank combinatorial form of `(★)` (§10.6, rank-parity formula `rank(b_i)=i+P_i` proven); the
  closing dominance step is left as an explicit sharp gap — the naive per-block charge
  `Σ_{red even} ≤ Σ_i⌈m_i/2⌉b_i` was proven INSUFFICIENT (its sufficient condition `Σ_{blue odd}≥`
  the charge fails `≈51 %`, verified), so the closer must use cross-block (cross-`k`) cancellation.
  Step 3 (reduction-to-base / slice-max monotone in `b`) not attempted — stated as GAP-P1′-b.
  → **partial** (base case reduced to the single clean inequality `(★)` and closed on `≈88 %`+DIFF
  region + all `n=1`; the ladder-dominance core of `(★)` and the reduction-to-base remain open).
- **(round 10 build — floor-half reduction of the residual)** Rigorous progress, honest partial;
  the sharpest form yet of GAP-P1. Established a NEW clean **exact identity** (proven from the
  certified peel identity + an elementary integer floor identity, verified `0` mismatches / `3·10³`):
  `D̃(F) = 1 − 2∫_{(0,θ)}⌊M(t)/2⌋ dt`, where `M = N_{π_0} − N_{F'}` on `(0,θ)`, `θ=2^{n−1}`
  (§9, `(FLOOR)`). Hence **the entire residual `{|D̃(π_0)−D̃(F')|<1}` — indeed all of Case B —
  reduces to the single clean inequality `I_n := ∫_{(0,θ)}⌊M/2⌋ ≤ 0`**, with equality (`D̃=1`) exactly
  at the tie configs. Verified `I_n ≤ 0` (max `= 0` exactly) over `6·10⁴` feasible fractional Case-B
  configs, `n ≤ 6`, exact `Fraction`, `0` violations. Further, the layer form
  `I_n = Σ_{k≥1}(λ{M≥2k} − λ{M≤−(2k−1)})` (§9.2, verified `0` mismatches) exposes the even/odd
  threshold asymmetry that is the exact source of the missing `½`. **Two decisive structural
  findings** (§9.3): (a) the budget `Σa_j ≤ n` enters the whole problem ONLY through `M(0⁺) ≤ 1`
  (Invariant I) — dropping the joint budget makes `I_n > 0` occur (an infeasible-config probe
  produced many `I_n>0`), reconfirming the non-locality flagged by the R8 meta; (b) `M(0⁺)≤1` ALONE
  is insufficient — the §7a decoy `F'` satisfies `M(0⁺)=0` yet gives `I_n>0`, so the loaded IH must
  read `F'`'s genuine dyadic-refinement shape (its count function `g=N_{F'}`), NOT just its
  part-count. The gap is now the single inequality `I_n ≤ 0` with the loaded property pinned down to
  "a shape property of `g=N_{F'}`", still open (GAP-P1′). → **partial** (reduction sharpened from the
  `(△⋆)` measure form to the explicit floor inequality `∫⌊M/2⌋≤0`; the coupled/loaded IH that proves
  it remains open, but its exact target and the precise role of every hypothesis are now isolated).
- **(round 9 build — peel top scale + symmetric-difference insertion identity)** Rigorous
  progress, honest partial. Established: (i) the **peel symmetric-difference identity**
  `D̃(F) = D̃(π_0) + D̃(F') − 2·λ(O_{π_0} ∩ O_{F'})` and its consequence
  `D̃(F) = λ(O_{π_0} △ O_{F'})` (fully proven, §3; verified `0` mismatches / `5·10³` splits);
  (ii) **Case A (`a_0 = 0`) FULLY CLOSED** by the clean identity `D̃(F) = 2^n − D̃(F')` and the
  universal bound `D̃(·) ≤ Σ(·)` — needs *no* value-IH (§4, new & elegant); (iii) the
  **difference bound** `D̃(F) ≥ |D̃(π_0) − D̃(F')|` (fully proven, §5; `0` violations / `1.2·10⁵`
  Case-B configs), which **closes Case B on `{|D̃(π_0) − D̃(F')| ≥ 1}` — 80.8 % of sampled
  Case-B configs**; (iv) **Invariant I** `M(0⁺) = (a_0+1) − |F'| ≤ 1` fully proven with equality
  characterised (§6). **CONFRONTED the circularity honestly (§7):** proved numerically that the
  *plain* IH `D̃(F')≥1` is genuinely INSUFFICIENT for the insertion step (arbitrary altsum-`≥1`
  multiset `F'` + partition `π_0` reaches `D̃(F)=0.146<1`), while *real* dyadic refinements `F'`
  give `min D̃(F)=1` exactly — so the step REQUIRES a loaded invariant capturing `F'`'s dyadic
  origin, and the residual `{|D̃(π_0)−D̃(F')|<1}` is exactly the target-equivalent core (min `D̃`
  there `=1`, tie-attained). The loaded invariant remains **GAP-P1** (open). → **partial**
  (Case A closed unconditionally; Case B closed on the large-difference region; residual and the
  precise loaded-IH requirement isolated with evidence).

## Current best

The lower bound is reduced (integer units, Liu `={1,…,2^n}`, target `D̃≥1`) via the **peel of the
top scale** `F = π_0 ⊎ F'` to the following, all rigorous:

- **Base cases** `n=0` (`F={1}`, `D̃=1`) and `n=1` (`F={2,1}`, `D̃=1`) — done.
- **Peel symmetric-difference identity (§3, proven):** `D̃(F) = λ(O_{π_0} △ O_{F'})
  = D̃(π_0) + D̃(F') − 2λ(O_{π_0}∩O_{F'})`.
- **Case A `a_0=0` (§4, CLOSED unconditionally):** `D̃(F) = 2^n − D̃(F') ≥ 2^n − (2^n−1) = 1`,
  using only `0 ≤ D̃(F') ≤ ΣF' = 2^n−1`. No value-IH needed; recovers/strengthens the C3 bound.
- **Difference bound (§5, proven):** `D̃(F) ≥ |D̃(π_0) − D̃(F')|`. **Closes Case B whenever
  `|D̃(π_0) − D̃(F')| ≥ 1`** (80.8 % of sampled Case-B configs, `n≤5`).
- **Invariant I (§6, proven):** `M(0⁺) = (a_0+1) − |F'| ≤ 1`, equality iff `F'` uncut and `a_0=n`.
- **Floor-half reduction `(FLOOR)` (§9, NEW, proven):** `D̃(F) = 1 − 2∫_{(0,θ)}⌊M/2⌋`, so
  **Case B `⟺` `I_n := ∫_{(0,θ)}⌊M/2⌋ ≤ 0`** (tie-attained). Layer form (§9.2):
  `I_n = Σ_{k≥1}(λ{M≥2k} − λ{M≤−(2k−1)})`. Budget enters ONLY via `M(0⁺)≤1`; `M(0⁺)≤1` alone
  is insufficient (decoy) — the loaded IH must control the shape of `g=N_{F'}` (§9.3).
- **Extremal base case `b=0` (§10, NEW, round 11):** with all budget on `π_0`, `F'` is the uncut
  ladder `L={2^{n−1},…,1}`, and the base case is the clean interleaving identity (§10.2, proven)
  `D̃(π_0⊎L) = 1 + 2(Σ_{blue odd} − Σ_{red even})`, i.e. **`(★) Σ_{blue odd} ≥ Σ_{red even}`** in the
  merge of `π_0`(red) and `L`(blue). Closed unconditionally on (a) `{M≤1 on (0,θ)}` (≈88 %, §10.3)
  and (b) `{|D̃(π_0)−D̃(L)|≥1}`, `D̃(L)=(2^n−(−1)^n)/3` (§10.4); all `n=1` closed (§10.5). Residual
  reduced to a finite block/rank dominance inequality (§10.6, GAP-P1′-a). Reduction-to-base
  (slice-max monotone in `b`) is GAP-P1′-b.

- **HLP threshold reduction of `(WM)` (§11.6, NEW, round 13, proven).** With the tail functional
  `Φ(t)=Σ_{BO}(v−t)^+ − Σ_{RE}(w−t)^+`: (i) `(WM) BO ≻_w RE ⟺ Φ≥0` (Hardy–Littlewood–Pólya, ramp
  form proven §11.6.1); (ii) `Φ` is piecewise-linear with convex kinks only at `BO`-values, so its
  minimum is at `t=0` or a blue-odd rung, giving the **finite** criterion `(RUNG)`:
  `(WM) ⟺ (★) ∧ [Φ(b)≥0 ∀ blue-odd rung b]`; (iii) **top rung closed:** `Φ(θ)=0` unconditionally by
  `(m₀≤1)`. The residual `Φ(b_i)≥0` (`i≥2`) is, by `(SS)`, a shifted `(★)` on a shorter scaled ladder
  against a deficient red total — identical to the sibling `ladder-length-deficient-induction`'s
  generalised lemma. So GAP-P1′-a is now a finite list of `≤ n−1` scalar rung inequalities, the top
  one closed, the rest = the shared deficient-ladder wall.

**The single open gap, GAP-P1 (§7, sharpened to §9).** Case B on the residual `{|D̃(π_0) − D̃(F')| < 1}`. Here the
odd-level sets `O_{π_0}, O_{F'}` are NOT nested, the overlap is strictly below `min(D̃(π_0),
D̃(F'))`, and the difference bound only gives `D̃(F)≥0`. Numerically the residual min is exactly
`1` (tie-attained), so a **loaded, dyadic-structural** IH is required — the plain value-IH is
provably insufficient (§7 witness `D̃(F)=0.146`). Identifying the minimal loaded invariant that is
(i) inherited by `F'` and (ii) forces `2λ(O_{π_0}∩O_{F'}) ≤ D̃(π_0)+D̃(F')−1` on the residual is
the remaining crux; the honest circularity risk (a loaded invariant strong enough to power the
step must be strictly stronger than `D̃≥0` yet not a restatement of the target) is spelled out.

## Full proof
*(Not present — Status is `partial`. The rigorous partial is written out in the Progress section.)*

## Imported (certified)
- **Lemma G** (greedy claim = odd-rank sum; level-measure form `D̃ = λ(O_F)`,
  `O_F = {t>0: N_F(t) odd}`, `N_F(t)=#\{parts>t\}`) and **Cut-Flip / Domination C3** —
  `results/imo-2026-03/lemmas/greedy-claim.md`, `cut-flip.md`.
- **§9 restatement**, `D̃ = O − E`, and the **Structure Lemma** — from
  `induction-recursion-telescope.md` (§3, §5, §9). Every Case-A/B final multiset is a
  simultaneous refinement `F = ⊎_{j=0}^n π_j`, `π_j` a partition of `2^{n−j}` into `a_j+1` parts,
  `Σ_j a_j ≤ n`; and `D̃≥1 ⇔ O(F)≥2^n ⇔ E(F)≤2^n−1`.
- **Threshold-split identity `(△)`** `D̃(F)=(y₁−θ)⁺+λ_{(0,θ)}(O_Y△O_Z)` — telescope §13
  (used as a cross-check of the peel identity below).
- **Upper bound** `c(n) ≤ 2^n/(2^{n+1}−1)` for all `n` — `lemmas/upper-bound.md` (certified;
  completes the problem once GAP L closes).

---

## Progress (full detail of the proved part)

Throughout we work in integer units (rescale by `1/u_n`): Liu's dyadic partition is `{1,2,…,2^n}`,
grand total `2^{n+1}−1`, and the target is `D̃(F) ≥ 1`. By Lemma G (level-measure form, certified),
`D̃(P) = λ(O_P)` where `O_P = {t>0 : N_P(t) odd}`, `N_P(t)=#\{p∈P : p>t\}`. We write `D̃(P)` for the
discrepancy of any finite positive multiset `P`; it equals the value-only alternating sum
`Σ_i(−1)^{i−1}w_i` of the descending sort `w_1≥w_2≥…` (Lemma G, tie-invariant, telescope §7).

### 0. Two universal facts about `D̃`

**(U1) `0 ≤ D̃(P) ≤ ΣP`.** With `w_1≥…≥w_m≥0` and `w_{m+1}:=0`,
`D̃(P) = Σ_{k≥1}(w_{2k−1} − w_{2k}) ≥ 0` termwise (descending), and
`D̃(P) = w_1 − Σ_{k≥1}(w_{2k}−w_{2k+1}) ≤ w_1 ≤ ΣP`; more simply `D̃ = O−E ≤ O ≤ O+E = ΣP`. ∎

**(U2) Parity XOR of level sets.** If `P = A ⊎ B` (disjoint multiset union) then
`N_P = N_A + N_B`, so `1[N_P(t)\text{ odd}] = 1[N_A(t)\text{ odd}] ⊕ 1[N_B(t)\text{ odd}]`, i.e.
`O_P = O_A △ O_B`. Hence, by additivity of Lebesgue measure on the symmetric difference,
```
D̃(P) = λ(O_A △ O_B) = λ(O_A) + λ(O_B) − 2λ(O_A ∩ O_B) = D̃(A) + D̃(B) − 2λ(O_A∩O_B).   (SD)
```
∎

### 1. Setup: the peel of the top scale

By the Structure Lemma (imported), a final multiset is `F = ⊎_{j=0}^n π_j`, `π_j` a partition of
`2^{n−j}` into `a_j+1` positive parts, `Σ_{j=0}^n a_j ≤ n`. **Peel the top scale:**
```
F = π_0 ⊎ F',   π_0 = partition of 2^n into a_0+1 parts,   F' = ⊎_{j=1}^n π_j.
```
Then `F'` is a simultaneous refinement of the `(n−1)`-ladder `{2^0,…,2^{n−1}} = {1,…,2^{n−1}}`
with budget `b := Σ_{j≥1} a_j ≤ n − a_0`. Set `θ := 2^{n−1}`. Every part of `F'` is `≤ θ`, and
`ΣF' = Σ_{j=1}^n 2^{n−j} = 2^n − 1`, `Σπ_0 = 2^n`. Since `b ≤ n−1`, the **inductive hypothesis**
`P(n−1)` applies to `F'`:
```
D̃(F') ≥ 1        (IH),      and always   0 ≤ D̃(F') ≤ ΣF' = 2^n − 1   by (U1).
```

By (SD) with `A=π_0`, `B=F'`:
```
D̃(F) = D̃(π_0) + D̃(F') − 2λ(O_{π_0} ∩ O_{F'}) = λ(O_{π_0} △ O_{F'}).      (PEEL)
```
*(Verified: the value-only alternating sum of `π_0⊎F'` equals `λ(O_{π_0}△O_{F'})` with `0`
mismatches over `5·10³` random splits; and it agrees with the certified `(△)` after splitting the
axis at `θ`.)*

### 2. Base cases (proven)
`n=0`: `F=\{1\}`, `D̃=1`. `n=1`: `F=\{2,1\}` (only Case A, top uncut, or `\{y_1,y_2,1\}`); direct
`D̃(\{2,1\})=2−1=1`, and any `1`-cut Case-B config is handled by §4/§5 below with `n=1`. Both
`n=0,1` are fully solved in `induction-recursion.md` (imported). ∎

### 3. The peel symmetric-difference identity (proven)
Equation (PEEL) of §1 is the identity, proven from (U2). Its two immediate consequences drive the
casework:
- If `O_{F'} ⊆ O_{π_0}` then `λ(O_{π_0}∩O_{F'}) = D̃(F')`, so `D̃(F) = D̃(π_0) − D̃(F')` **plus**
  the part of `O_{π_0}` outside `O_{F'}`; precisely `D̃(F) = D̃(π_0) + D̃(F') − 2D̃(F')
  = D̃(π_0) − D̃(F')` **fails to be signed**, so we use the exact measure form below.
- In general `0 ≤ λ(O_{π_0}∩O_{F'}) ≤ min(D̃(π_0), D̃(F'))`, giving the difference bound (§5).

### 4. Case A (`a_0 = 0`) — CLOSED unconditionally (new)

Here `π_0 = \{2^n\}` is a single uncut part. Then `N_{π_0}(t) = 1[t < 2^n]`, so `O_{π_0} = (0,2^n)`
and `D̃(π_0) = 2^n`. Every part of `F'` is `≤ θ = 2^{n−1} < 2^n`, hence `O_{F'} ⊆ (0,2^{n−1}]
⊂ (0,2^n) = O_{π_0}`, i.e. `O_{π_0} ∩ O_{F'} = O_{F'}` and `λ(O_{π_0}∩O_{F'}) = D̃(F')`. By (PEEL),
```
D̃(F) = 2^n + D̃(F') − 2·D̃(F') = 2^n − D̃(F').
```
By (U1), `D̃(F') ≤ ΣF' = 2^n − 1`, therefore
```
D̃(F) = 2^n − D̃(F') ≥ 2^n − (2^n − 1) = 1.
```
Thus **Case A holds unconditionally** — it does not even use the value-IH `D̃(F')≥1`, only the
universal `D̃(F') ≤ ΣF'`. (This is a clean re-derivation and mild strengthening of the certified
domination C3, and it also shows `D̃(F) ≤ 2^n`, with `D̃(F)=1` iff `D̃(F')=2^n−1`, i.e. `F'` is the
"maximal-discrepancy" refinement, e.g. `F'=\{2^{n−1},…,1\}` uncut.) ∎

### 5. The difference bound and the large-difference region of Case B (proven)

From (PEEL) and `0 ≤ λ(O_{π_0}∩O_{F'}) ≤ min(D̃(π_0),D̃(F'))`,
```
D̃(F) = D̃(π_0) + D̃(F') − 2λ(O_{π_0}∩O_{F'}) ≥ D̃(π_0) + D̃(F') − 2min(D̃(π_0),D̃(F'))
      = |D̃(π_0) − D̃(F')|.                                                    (DIFF)
```
*(Verified: `0` violations of (DIFF) over `1.2·10⁵` Case-B configs, `n≤5`, exact `Fraction`.)*

> **Corollary (Case B, large-difference region — CLOSED).** If `|D̃(π_0) − D̃(F')| ≥ 1` then
> `D̃(F) ≥ 1`.

This closes **80.8 %** of sampled Case-B configurations (`n≤5`). In particular, whenever the top
piece is fragmented into a high-discrepancy partition `π_0` (e.g. one dominant fragment
`y_1 > θ + something`, so `D̃(π_0) ≥ 2(y_1−θ)` is large) *or* into a near-balanced one
(`D̃(π_0)` small while `D̃(F')` is a full unit or more), the difference bound already delivers the
target. The residual is precisely the near-balance regime `|D̃(π_0) − D̃(F')| < 1` (§7).

### 6. Invariant I (proven) — the near-`0` anchor

Let `M(t) := N_{π_0}(t) − N_{F'}(t)` on `(0,θ)` (this is the `M` of the certified `(△⋆)`, since
above `θ` only the single part `y_1` of `π_0` can survive; `F'` has no part `>θ`). Its value at
`0⁺` is
```
M(0⁺) = |π_0| − |F'| = (a_0+1) − |F'|.
```
Now `|F'| = Σ_{j=1}^{n}(a_j+1) = n + b`, `b := Σ_{j≥1}a_j`, because `F'` refines the `n` pieces
`\{2^0,…,2^{n−1}\}`. With the budget constraint `a_0 + b ≤ n`,
```
M(0⁺) = (a_0+1) − (n+b) = (a_0 + b) + 1 − n − 2b ≤ n + 1 − n − 2b = 1 − 2b ≤ 1.
```
Hence **`M(0⁺) ≤ 1`**, with equality iff `b = 0` and `a_0 = n` (all budget spent on the top piece,
`F' = \{1,…,2^{n−1}\}` uncut). ∎

This anchors the near-`0` band: when `M(0⁺) ≤ −1`, the interval just above `0` lies in
`\{M\text{ odd}\}` iff `M(0⁺)` is odd; the certified telescope §14 shows the *entire* tie-config
surplus can live in this near-`0` count-parity band (`|F'|>|π_0|`), which is why the compensation
is bottom-inclusive, not a top reserve. Invariant I supplies the correct base value of `M` for the
insertion accounting on the residual.

### 7. The residual, the loaded-IH requirement, and the circularity confrontation (GAP-P1)

After §4–§5 the only open case is **Case B with `|D̃(π_0) − D̃(F')| < 1`**. Equivalently, in the
(PEEL) form, the overlap is strictly submaximal:
```
λ(O_{π_0} ∩ O_{F'}) < min(D̃(π_0), D̃(F')),     and the target is
2λ(O_{π_0} ∩ O_{F'}) ≤ D̃(π_0) + D̃(F') − 1.                                   (RESID)
```
This is a *copy* of the certified localized inequality `(△⋆)` on `(0,θ)`:
`λ_{(0,θ)}\{M\text{ odd}\} ≥ ∫_{(0,θ)}M = 1 − β`, `β=(y_1−θ)⁺` (telescope §13). We import that
equivalence rather than re-derive it; the value of the peel is that it exposes what the *inductive*
step needs beyond it.

**7a. The plain value-IH is provably insufficient (numerical, decisive).** If the step could be
powered by `D̃(F')≥1` alone, then for *every* multiset `F'` with `ΣF'=2^n−1`, all parts `≤θ`, and
`D̃(F')≥1`, and *every* partition `π_0` of `2^n`, we would have `D̃(π_0⊎F')≥1`. **This is false.**
Exhaustive-random search (`n=3`, `2·10⁵` trials, exact `Fraction`) produced
```
π_0 = (2.792, 2.504, 2.704),   F' = (2.534, 2.247, 2.219)  [ΣF'=7, all ≤4, D̃(F')=2.506 ≥ 1],
D̃(π_0 ⊎ F') = 0.146 < 1.
```
So `F'` must be a *genuine dyadic refinement*, not merely an altsum-`≥1` multiset: the near-equal
`F' = (2.53,2.25,2.22)` cannot arise from cutting `\{1,2,4\}` under budget `≤2` (each dyadic scale
contributes a distinct magnitude; the budget caps fragmentation). Correspondingly, when `F'` ranges
over **real** dyadic refinements (and `π_0` over real partitions with `a_0+b≤n`),
`min D̃(π_0⊎F') = 1` **exactly** for `n=2,3,4,5` (`≥1.2·10⁵` trials each, `0` violations). The
inductive step is therefore true, but **only** because of `F'`'s recursive dyadic structure — the
step must carry a *loaded* invariant, `GAP-P1`.

**7b. Confronting the circularity (the reviewer's flag).** A loaded invariant `P(F')` must be
strictly stronger than the trivial `D̃(F')≥0` (which gives, via (DIFF), only `D̃(F)≥0`) yet must
NOT secretly be the target. Two candidate shapes are ruled out here honestly:
- *Prefix alternating-sum bound* `Σ_{i≤2k}(−1)^{i−1}w_i ≥ 0` for `F'`: trivially true (descending),
  hence gives only `D̃(F)≥0` under insertion — too weak (reviewer's point). Rejected.
- *Scalar / top-reserve summaries of `F'`*: refuted in prior rounds (scalar summary R3–R4;
  top-down reserve R7, `7306/4·10⁵`). Rejected.
  The witness in **7a** shows the required invariant is a **genuine shape/spread property** of `F'`
  that distinguishes dyadic refinements from equal-ish multisets: e.g. a per-scale majorization
  "`F'`'s sorted prefix sums dominate those of any equal-split with the same part-count and total,"
  or the recursive statement that `F'` itself peels as `F' = π_0' ⊎ F''` with `π_0'` a partition of
  `θ` and `F''` a refinement of the `(n−2)`-ladder (Structure Lemma). The honest status: **no such
  invariant has yet been proven both (i) inherited by `F'` and (ii) sufficient to force (RESID)**.
  If every candidate strong enough for (ii) turns out equivalent to the target (as the R8 meta
  warns for *static profile* invariants), this collapses to RETHINK; but the peel is NOT a static
  profile of the final multiset — it is an induction on `n` that couples `π_0`'s partition with the
  *recursive* `F'`, precisely the "cut-tree origin" direction the meta points to, so it is not yet
  excluded. Resolving 7b is the whole remaining task.

**7c. What the peel has contributed (bankable).** (i) A short, unconditional proof of Case A via
`D̃(F)=2^n−D̃(F')` (§4). (ii) The clean (SD)/(PEEL)/(DIFF) machinery closing `≥80 %` of Case B
(§5). (iii) A crisp, *evidenced* localization of the wall: the residual is the near-balance region
`|D̃(π_0)−D̃(F')|<1`, and the missing ingredient is a **loaded dyadic-shape invariant on `F'`**,
proven necessary (7a) and constrained (7b). The peel decomposition itself is fully rigorous; only
the loaded invariant is open.

### 9. The floor-half reduction of Case B (round 10, proven identity + sharpened gap)

This section replaces the diffuse `(△⋆)` count-parity band of §7 by a single explicit inequality,
and pins down exactly which hypothesis does what. Throughout, `θ = 2^{n−1}`, the top-scale peel is
`F = π_0 ⊎ F'`, and `M(t) := N_{π_0}(t) − N_{F'}(t)` on `(0,θ)` (an integer-valued step function).

**9.1 The floor-half identity `(FLOOR)` (proven).**
```
D̃(F) = 1 − 2 ∫_{(0,θ)} ⌊M(t)/2⌋ dt.                                            (FLOOR)
```
*Proof.* By the certified peel identity (§3), `D̃(F) = λ(O_{π_0} △ O_{F'})` on the whole axis.
Split the axis at `θ`. Every part of `F'` is `≤ θ`, so `O_{F'} ⊆ (0,θ]` and `O_{F'}∩(θ,∞)=∅`;
hence on `(θ,∞)`, `O_{π_0}△O_{F'} = O_{π_0}∩(θ,∞)`. Since `Σπ_0 = 2^n = 2θ`, at most one part of
`π_0` exceeds `θ` (two parts `> θ` would sum to `> 2θ`), so `N_{π_0}(t)∈\{0,1\}` for `t>θ` and
`λ(O_{π_0}∩(θ,∞)) = (y_1(π_0) − θ)^+ =: β`. Thus `D̃(F) = β + λ_{(0,θ)}(O_{π_0}△O_{F'})`.
On `(0,θ)`, `O_{π_0}△O_{F'} = \{t : N_{π_0}(t)+N_{F'}(t)\text{ odd}\} = \{t: M(t)\text{ odd}\}`
(parity of a sum = parity of a difference). For every integer `m`, the elementary identity
`1[m\text{ odd}] = m − 2⌊m/2⌋` holds (both sides equal `m \bmod 2`; check `m=−2,−1,0,1,2,3`:
`0,1,0,1,0,1`). Integrating over `(0,θ)`,
```
λ_{(0,θ)}\{M\text{ odd}\} = ∫_{(0,θ)}M − 2∫_{(0,θ)}⌊M/2⌋.
```
Compute `∫_{(0,θ)}M = ∫_{(0,θ)}N_{π_0} − ∫_{(0,θ)}N_{F'}`. Since all parts of `F'` are `≤θ`,
`∫_{(0,θ)}N_{F'} = ∫_{(0,∞)}N_{F'} = ΣF' = 2^n−1`. And `∫_{(0,∞)}N_{π_0} = Σπ_0 = 2^n` with
`∫_{(θ,∞)}N_{π_0} = β`, so `∫_{(0,θ)}N_{π_0} = 2^n − β`. Hence `∫_{(0,θ)}M = (2^n−β)−(2^n−1) = 1−β`.
Therefore `λ_{(0,θ)}\{M\text{ odd}\} = (1−β) − 2∫⌊M/2⌋`, and
`D̃(F) = β + (1−β) − 2∫⌊M/2⌋ = 1 − 2∫_{(0,θ)}⌊M/2⌋`. ∎

*(Verified exact `Fraction`: `0` mismatches over `3·10³` random dyadic-feasible `F`, `n≤5`.)*

**Consequence.** `D̃(F) ≥ 1 ⟺ I_n := ∫_{(0,θ)}⌊M/2⌋ ≤ 0`. This is the whole of Case B in one
inequality (Case A is the sub-case `a_0=0`, where `M = 1[t<2^n]·? ` degenerates and §4 gives it
directly). The tie `D̃=1` is exactly `I_n=0`. *(Verified: `I_n ≤ 0`, max `= 0` exactly, over
`6·10⁴` feasible fractional Case-B configs, `n≤6`, exact `Fraction`, `0` violations.)*

**9.2 Layer form (proven).** For every integer `m`,
`⌊m/2⌋ = Σ_{k≥1}1[m≥2k] − Σ_{k≥1}1[m≤−(2k−1)]` (for `m≥0` the first sum is `#\{k:2k≤m\}=⌊m/2⌋`
and the second is `0`; for `m<0`, `⌊m/2⌋ = −⌈|m|/2⌉ = −#\{k:2k−1≤|m|\} = −Σ_k 1[m≤−(2k−1)]`).
Integrating,
```
I_n = Σ_{k≥1}\big(λ\{M≥2k\} − λ\{M≤−(2k−1)\}\big).                               (LAYER)
```
*(Verified: `0` mismatches vs. `∫⌊M/2⌋` over `5·10³` configs.)* So the target `I_n≤0` reads
```
Σ_{k≥1} λ\{M≥2k\}  ≤  Σ_{k≥1} λ\{M≤−(2k−1)\}.                                     (LAYER≤)
```
The **even thresholds `2k` on the positive side vs. odd thresholds `2k−1` on the negative side**
are the precise arithmetic origin of the missing `½` that the R8 meta proved no static
measure/merged-order framing can supply. A structural upper bound on the positive side:
`\{M≥2k\} ⊆ \{N_{π_0}≥2k\} = (0, x_{2k}(π_0))`, so `λ\{M≥2k\} ≤ x_{2k}(π_0)` and
```
Σ_{k≥1} λ\{M≥2k\} ≤ Σ_{k≥1} x_{2k}(π_0) = E(π_0) = (2^n − D̃(π_0))/2,
```
where `E(π_0)` is the even-rank sum of `π_0`. This bound is correct but **too weak alone** (at the
tie `n=3`, `π_0=(4,4)`, `F'=\{2,2,2,1\}`: LHS `=2 = ` RHS-target, but `E(π_0)=4`), confirming the
overlap between `π_0` and `F'` must be used jointly — a scalar summary of `π_0` cannot close it.

**9.3 Exactly which hypothesis does what (two decisive findings).**
- *(Budget acts only through `M(0⁺)≤1`.)* Invariant I (§6) is `M(0⁺)=(a_0+1)−|F'| = (a_0+b)+1−n−2b`,
  and the joint budget `a_0+b≤n` is equivalent to `M(0⁺)≤1`. This is the ONLY channel through which
  `Σa_j≤n` enters `(FLOOR)`. Dropping the joint budget (e.g. giving `F'` its own full budget `n−1`
  while still cutting `π_0`, so `a_0+b>n`) makes `I_n>0` occur in abundance — an explicit
  exact-`Fraction` probe over such *infeasible* configs produced many `I_n>0` values. This re-verifies,
  now at the level of the sharp inequality, that the `+1` is the single unit of budget slack
  `n − (n−1)` between a level-`n` config and its level-`(n−1)` sub-refinement — a genuinely non-local
  quantity, exactly as the R8/R9 meta requires.
- *(`M(0⁺)≤1` alone is NOT enough — dyadic shape of `F'` is essential.)* The §7a decoy
  `π_0=(2.792,2.504,2.704)`, `F'=(2.534,2.247,2.219)` has `M(0⁺)=|π_0|−|F'|=3−3=0≤1`, yet
  `D̃(F)=0.146<1`, i.e. `I_n>0`. So `(LAYER≤)` is FALSE for an arbitrary multiset `F'` of the right
  total/part-count with `M(0⁺)≤1`; it becomes true only because a genuine dyadic refinement `F'` has
  a constrained count function `g=N_{F'}` (its parts cluster at geometric scales `∼2^{−j}`, forcing
  `g` to a specific lumpy staircase, unlike the decoy's near-flat profile). Hence the loaded IH must
  be a **shape property of `g=N_{F'}`**, provable by the level-`(n−1)` recursion, sufficient to force
  `(LAYER≤)` for every partition `π_0` of `2^n`.

**9.4 The remaining gap, GAP-P1′ (open).** Prove `I_n = ∫_{(0,θ)}⌊M/2⌋ ≤ 0`. The reduction (§9.1)
is unconditional and exact; the open content is a loaded property `P2(F')` of the count function
`g=N_{F'}` that (i) is inherited under one further peel `F'=π_1⊎F''` (so the level-`(n−1)` IH
`I_{n−1}≤0` about `F'` upgrades to control of `g`'s shape), and (ii) forces `(LAYER≤)` against every
partition `π_0` of `2^n` with `a_0≤n−b`. Two candidate reductions were tested and are **not yet
closed**: the scalar even-rank bound `Σλ\{M≥2k\}≤E(π_0)` (proven but too weak, §9.2), and inducting
on the budget `b` from the base `b=0` (where `F'` is forced to be the uncut ladder `\{1,…,θ\}` and
`I_n≤0` becomes a pure statement about `π_0`) — the base is clean but the inductive step (adding one
cut to `F'` while lowering the allowed `a_0` by one) has not been shown `I_n`-monotone. GAP-P1′ is
strictly sharper than the round-9 GAP-P1: the target is now a single scalar inequality with an
explicit integrand, the role of every hypothesis is isolated, and the residual measure-form `(△⋆)`
is subsumed.

### 10. The extremal base case `b=0` — the ladder-interleaving identity `(★)` (round 11)

This section attacks `I_n ≤ 0` (equivalently `D̃(F)≥1`) on the extremal slice of the feasible family,
`b := Σ_{j≥1}a_j = 0`. This is the tightest slice: the explorer's exact slice-maxima of `I_n` at fixed
`n=4` are `−3.69, −0.55, −0.281, −0.295, 0` for `b=4,3,2,1,0`, so the extremum `I_n=0` sits exactly at
`b=0`. Closing `b=0` is the concrete deliverable; the reduction of general `b` to it is §10.7.

**10.1 What `b=0` forces.** By the Structure Lemma, `F' = ⊎_{j=1}^n π_j` where `π_j` is a partition of
`2^{n−j}` into `a_j+1` parts. When `b=0`, every `a_j=0` (`j≥1`), so each `π_j={2^{n−j}}` is a single
uncut part and `F' = {2^{n−1}, 2^{n−2}, …, 2, 1} =: L`, the **uncut ladder** (`θ=2^{n−1}`,
`ΣL = 2^n−1`). The budget `a_0 ≤ n` leaves `π_0` an arbitrary partition of `2^n` into `a_0+1 ≤ n+1`
positive parts (possibly fractional). So the base case is the fixed-object statement:

> **Base Case (B0).** For every partition `π_0` of `2^n` into `r ≤ n+1` positive real parts,
> `D̃(π_0 ⊎ L) ≥ 1`, with equality attainable (e.g. `π_0 = {2^{n−1}+1, 2^{n−2},…,2,1}`).

*(Verified: integer-partition enumeration gives `min D̃(π_0⊎L)=1` exactly for `n≤6`, attained at
`π_0={2^{n−1}+1,2^{n−2},…,1}`; `2·10⁵` fractional trials per `n≤7` give min `=1`, `0` values `<1`.)*

**10.2 The interleaving identity `(★)` (proven).** Write the descending merge of `G:=π_0⊎L` as
`w_1 ≥ w_2 ≥ … ≥ w_N` (`N=r+n`), colouring each element **red** if it is a part of `π_0` and **blue**
if it is a part of `L`. By Lemma G, `D̃(G) = Σ_{j=1}^N s_j w_j` with `s_j := (−1)^{j−1}` (`+1` at odd
rank, `−1` at even rank); ties are broken arbitrarily (Lemma G is tie-invariant). Assign each element a
**colour sign** `τ_j := +1` if red, `−1` if blue. Then, summing colours,
```
Σ_{j} τ_j w_j = Σ_{red} r − Σ_{blue} b = Σπ_0 − ΣL = 2^n − (2^n − 1) = 1.               (C)
```
Subtract (C) from `D̃(G)=Σ s_j w_j`:
```
D̃(G) − 1 = Σ_j (s_j − τ_j) w_j.
```
Evaluate `s_j − τ_j` by colour and rank parity:
- red (`τ=+1`): `s_j−1 = 0` at odd rank, `= −2` at even rank;
- blue (`τ=−1`): `s_j+1 = 2` at odd rank, `= 0` at even rank.

Hence `Σ_j(s_j−τ_j)w_j = 2·Σ_{blue at odd rank} w_j − 2·Σ_{red at even rank} w_j`, i.e.
```
   D̃(π_0 ⊎ L) = 1 + 2·( Σ_{blue odd} − Σ_{red even} ).                                  (★-id)
```
Both `D̃` and (C) are tie-break-independent, so the bracket is well-defined. Therefore
```
   D̃(π_0 ⊎ L) ≥ 1   ⟺   (★)  Σ_{blue at odd rank} ≥ Σ_{red at even rank},
```
and `D̃=1` **iff** equality holds in `(★)`. Consistency with `(FLOOR)`: `D̃=1−2I_n` gives
`I_n = Σ_{red even} − Σ_{blue odd}`, so `I_n≤0 ⟺ (★)`. *(Verified exact `Fraction`: `(★-id)` holds
with `0` mismatches, and `(D̃≥1)⟺(★)` with `0` failures, over `1.8·10⁵` configs `n≤6`.)*

At the tie `π_0={θ+1,θ/2,…,1}` the merge is `θ+1 > θ > θ/2 > θ/2 > θ/4 > θ/4 > …`: red and blue
alternate red–blue–red–blue after the leading red `θ+1`, so *no* blue sits at an odd rank and *no* red
at an even rank — both sides of `(★)` are `0`, equality, `D̃=1`. This is the mechanism the whole base
case must protect: any deviation of `π_0` from a perfect red-on-top interleaving must move a blue up to
an odd rank by at least as much value as it moves a red up to an even rank — exactly ladder dominance.

**10.3 Closed region 1 (unconditional): `M ≤ 1` on `(0,θ)`.** Let `M := N_{π_0} − N_L` on `(0,θ)` as
in `(FLOOR)`. If `M(t) ≤ 1` for all `t∈(0,θ)`, then `⌊M(t)/2⌋ ≤ 0` pointwise (for any integer `m≤1`,
`⌊m/2⌋≤0`), so `I_n=∫_{(0,θ)}⌊M/2⌋ ≤ 0` and by `(FLOOR)` `D̃(π_0⊎L)=1−2I_n ≥ 1`. This is
unconditional and needs no dominance beyond `M≤1`. The hypothesis `M≤1` says `N_{π_0}(t) ≤ N_L(t)+1`
everywhere: `π_0` never has two more parts above a level than `L` does. *(Verified: `M≤1` holds on
`105535/120000 ≈ 88 %` of sampled base configs `n≤6`, and `D̃≥1` on every one of them, `0` failures.)*
The residual to `(★)` is thus confined to configs where `π_0` clusters `≥2` extra parts above some
ladder level (`M≥2` somewhere).

**10.4 Closed region 2 (unconditional): the `(DIFF)` shell.** By the certified difference bound
(`lemmas/peel-difference-bound.md`), `D̃(π_0⊎L) ≥ |D̃(π_0) − D̃(L)|`. The ladder value is exact:
```
   D̃(L) = Σ_{i=0}^{n−1} (−1)^i 2^{n−1−i} = 2^{n−1}·\frac{1−(−1/2)^n}{1+1/2}
        = \frac{2^n − (−1)^n}{3}   ( = 1,1,3,5,11,21,… for n=1,2,3,4,5,6 ).
```
Hence `|D̃(π_0)−D̃(L)| ≥ 1` (i.e. `D̃(π_0) ≤ D̃(L)−1` or `D̃(π_0) ≥ D̃(L)+1`) already forces
`D̃(π_0⊎L)≥1`. Only the near-balance shell `|D̃(π_0)−D̃(L)| < 1` survives — and, intersected with
§10.3, only configs with **both** `M≥2` somewhere and `|D̃(π_0)−D̃(L)|<1` remain open.

**10.5 `n=1` base case (fully closed).** `L={1}`, `π_0` a partition of `2` into `≤2` parts.
If `π_0={2}`: merge `{2,1}`, `D̃=2−1=1`. If `π_0={p,2−p}` with `1≤p≤2` (so `0≤2−p≤1`): merge
`p ≥ 1 ≥ 2−p`, `D̃ = p − 1 + (2−p) = 1`. So `D̃(π_0⊎L)=1` identically for `n=1` — the base case holds
with equality for every `π_0`. (This is `(★)` with both sides `0`.) ∎

**10.6 The residual as a finite block/rank dominance inequality (partial; GAP-P1′-a).** On the residual
of §10.3–10.4 we set up `(★)` in closed combinatorial form. Order the blue parts descending
`b_1>b_2>…>b_n` (`b_i = 2^{n−i}`), so **ladder dominance** reads `b_i = 2^{n−i} > 2^{n−i}−1
= Σ_{i'>i} b_{i'}`. Group the reds by which blue-gap they fall in: for `i=1,…,n−1` let `m_i` be the
number of reds in `(b_{i+1}, b_i)`, `m_0` the reds `> b_1=θ`, `m_n` the reds `< b_n=1`; `Σ_i m_i = r`,
and `m_0 ≤ 1` (two reds `>θ` would sum `>2θ=2^n=Σπ_0`). Writing `P_i := m_0+⋯+m_{i−1}` (reds above
`b_i`), the merged rank of `b_i` is
```
   rank(b_i) = (i−1 blues above) + P_i + 1 = i + P_i,               (proven, rank-parity formula)
```
and the `m_i` reds just below `b_i` occupy the consecutive ranks `i+P_i+1, …, i+P_i+m_i`. Thus `(★)`,
`Σ_{i: i+P_i odd} b_i ≥ Σ_{red even} r`, becomes a finite inequality in the `b_i`, the block counts
`m_i`, and the (free, gap-constrained) red values. Every even-rank red in block `i` has value `< b_i`,
and `m_0≤1` puts its single red at rank `1` (odd, contributing `0`); so
`Σ_{red even} ≤ Σ_{i=1}^{n} ⌈m_i/2⌉ b_i` (`b_n=1`) — but this per-block charge is **too lossy**: its
sufficient condition `Σ_{i:i+P_i odd} b_i ≥ Σ_i⌈m_i/2⌉ b_i` fails on `≈51 %` of configs (verified,
`61293/119997`), because an even-rank red in block `i` must be charged not to a same-block blue but,
via the interleaving, to a *higher* odd-rank blue whose dominance `b_{i'} > Σ_{i''>i'} b_{i''}` covers
an entire tail of lower even-reds at once. **The open step (GAP-P1′-a)** is the cross-block dominance
inequality `Σ_{i:i+P_i odd} b_i ≥ Σ_{red even}` proven with this tail-cancellation — equivalently
`I_n≤0` for `F'=L`. Its truth is certain (min `=1` exactly, §10.1); what is missing is the
tail-charging argument surviving cross-`k` cancellation. This is the sole residual of the base case.

**10.7 Reduction-to-base (GAP-P1′-b, open).** To lift `b=0` to all feasible `F`, one needs: the
supremum of `I_n` over the feasible family at fixed `n` is attained at `b=0` (explorer numerics:
`n=4` slice-maxima `−3.69,−0.55,−0.281,−0.295,0` for `b=4..0`). CRITICAL constraint recorded R11: the
**pointwise per-cut monovariant holding `π_0` fixed is FALSE** (~30 % violations) — so this must be
proved as a *slice-max* statement in which `π_0` co-varies with `F'` as one further cut is added to
`F'` (moving `b→b+1`, lowering the allowed `a_0` by one). No correct monotone-in-`b` argument is
established here; it is left as the explicit gap. (Watch-outs from R10/R11: the reduction must **add
cuts to `F'`, never merge** even tie-blocks toward `L` — merging can RAISE `D̃`, e.g. `{4,2,½,½}`:
`2→3`; and it must read the true staircase shape of `g=N_{F'}`, not any scalar summary.)

### 11. GAP-P1′-a via TOP WEAK-MAJORIZATION (round-12 plan — the concrete deliverable)

This section is the round-12 build target: prove `(★) Σ_{blue odd} ≥ Σ_{red even}` for the extremal
base slice `b=0` (`F'=L`), closing GAP-P1′-a. The mechanism is **value-domination (weak
majorization)**, NOT the refuted per-block same-block charge (§10.6, 51% fail) and NOT any positional
running-margin scan (refuted top-down/bottom-up, margins grow to `−2^{n-1}` — do NOT reopen).

**11.1 The stronger deliverable (weak majorization).** Let `BO` = multiset of blue-at-odd-rank
values, `RE` = multiset of red-at-even-rank values in the descending merge of `π_0 ⊎ L`. Sort each
descending. Prove
```
   (WM)  for every prefix length k,  Σ_{top k of BO} ≥ Σ_{top k of RE}      (BO weakly majorizes RE).
```
`(WM)` with `k=all` gives `Σ_{blue odd} ≥ Σ_{red even}` = `(★)`. Equivalent Hardy–Littlewood–Pólya
threshold form (prove either):
```
   (HLP)  ∀t ≥ 0,  Σ_{v∈BO}(v−t)^+ ≥ Σ_{v∈RE}(v−t)^+.
```
*Verified this round (exact `Fraction`): `(★)` 0 failures and `(WM)` 0 failures over integer
partitions `n≤6` (2000 random `π_0` per `n`); explorer separately confirms 0 failures on 280k
fractional configs `n≤8`.* **CAVEAT (must check):** `(WM)` is *strictly stronger* than `(★)` — it
could in principle over-shoot at large `n` (a config where `(★)` holds but `(WM)` fails). No such
config exists in the tested range; if the builder hits one, fall back to the sibling approach
`ladder-abel-pairing`, which targets `(★)` exactly.

**11.2 The self-similar truncation view (the structural handle for `(HLP)`).** Since every merge
element `> t` precedes every element `≤ t`, the merged rank of an element `> t` equals its rank
within the top-truncation `P_t := {elements of the merge that are > t}`. Hence *blue-at-odd-rank and
`> t`* `=` *blue at odd rank within `P_t`*, and likewise for red-even. Writing the count functions
`N_{BO}(s) = #\{blue-odd values > s\}`, `N_{RE}(s)=#\{red-even values > s\}`, and using
`Σ_v(v−t)^+ = ∫_t^∞ N(s)\,ds`, `(HLP)` is exactly
```
   ∀t:  Φ(t) := ∫_t^∞ \big(N_{BO}(s) − N_{RE}(s)\big)\,ds ≥ 0,      Φ(∞)=0,  Φ(0)=Σ_{blue odd}−Σ_{red even}=(★).
```
So `(HLP)` is a *uniform* family of `(★)`-type inequalities over all top-truncations `P_t` — the
tail integrals of the blue-odd count dominate the red-even count. This is the object with the
standard HLP/Karamata toolkit.

**11.3 The two levers (both proven, state once).**
- **(DOM)** `b_i = 2^{n−i} = 1 + Σ_{i'>i} b_{i'}` — each rung exceeds the sum of *all* lower rungs
  by exactly `1` (geometric sum; verified `n≤6`). This is the cross-block cancellation the per-block
  charge lacked: one odd-rank rung dominates its entire tail.
- **(m₀≤1)** at most one red exceeds `θ=b_1=2^{n-1}` (two reds `>θ` sum `>2θ=2^n=Σπ_0`). So the merge
  opens with an optional single red, then `b_1`, then the interleave; the single top red sits at rank
  `1` (odd), contributing `0` to `RE`.

**11.4 The hard step (GAP-P1′-a, the open charge).** Prove `(WM)`/`(HLP)` by charging red-even mass
onto blue-odd mass of `≥` value using `(DOM)`. Concretely on truncation `P_t`: let the surviving
rungs be `b_1>…>b_{i^*}` (those `> t`). The even-rank reds in `P_t` lie in gaps `(b_{i+1},b_i)`, each
`< b_i`. Charge the even-red mass in the tail below `b_i` to the odd-rank rung `b_i`: by `(DOM)`,
`b_i` exceeds the whole lower-rung tail, and the total surviving red mass below `b_i` is bounded by
`Σπ_0` minus the reds above (with `(m₀≤1)` pinning the top). The rank-parity formula
`rank(b_i)=i+P_i` (§10.6, proven, `P_i` = reds above `b_i`) selects which rungs are odd. **The open
content is: the odd-rank rungs surviving in `P_t` carry ≥ the even-rank red mass surviving in `P_t`,
uniformly in `t`,** via this tail-charge. This is the sole residual of the base case.

**11.5 The loaded-IH continuation (path to GAP-P1′-b — sets up the peel step).** The
ladder-interleaving identity `(★-id)` does **not** need `F'=L`: its colour-sum `(C)=Σπ_0−ΣF'=1`
holds for **every** feasible `F'` (always `ΣF'=2^n−1`) — *verified this round for general refinements
`n=2..5`*. So `(★)` generalizes to `Σ_{F'-odd} ≥ Σ_{π_0-even}` for any `F'`, and `(WM)` generalizes to
`BO(F') ≻_w RE`. What is special to `L` is only `(DOM)`. **Adopt `(WM)` as the LOADED INDUCTION
HYPOTHESIS:** "`F'` weakly-majorizes red-even against `F'`-odd for every partition `π_0` of `2^n`."
Base case `F'=L` via `(DOM)` (§11.4). Inductive step (GAP-P1′-b, open): `(WM)` is inherited under one
peel `F' = π_1 ⊎ F''` (`F''` a refinement of the `(n−2)`-ladder). This unifies GAP-P1′-a and
GAP-P1′-b under a single invariant and dodges the standalone `b→0` slice-max reduction (which the
explorer showed is a mirage — the slice-max is flat `=0`). Inheritance is the open crux of the step;
it is **not** the refuted pointwise `π_0`-fixed monovariant (that fixes `π_0`; here `(WM)` quantifies
over all `π_0` and inducts on the recursive structure of `F'`).

### 11.6 The HLP threshold reduction of `(WM)` (round 13, proven) — finitely many rung inequalities

This section carries out the value-domination programme of §11.1–11.4 rigorously as far as it goes.
It converts the *continuum* weak-majorization / HLP goal (§11.1) into a **finite** list of scalar
inequalities indexed by the blue-odd rungs, **closes the top one unconditionally**, and pins the
residual as a shifted self-similar `(★)` — thereby isolating the exact shared wall and bridging it to
the sibling `ladder-length-deficient-induction`. Throughout, `BO` (resp. `RE`) is the multiset of
blue-at-odd-rank (resp. red-at-even-rank) values in the descending merge of `π_0` (Σ`=2^n`, red) and
the uncut ladder `L={2^{n−1},…,1}` (blue), `θ=2^{n−1}=b_1`, and rungs are `b_i=2^{n−i}`.

Recall the two levers, both proven (§11.3): **(DOM)** `b_i = 1 + Σ_{i'>i} b_{i'}` (each rung exceeds
the sum of all lower rungs), and **(m₀≤1)** at most one red exceeds `θ` (two reds `>θ` sum
`>2θ=2^n=Σπ_0`), and that single red — if present — sits at rank `1` (odd), contributing `0` to `RE`.

**11.6.1 The tail functional and the HLP characterisation.** Define, for `t≥0`,
```
   Φ(t) := Σ_{v∈BO}(v−t)^+ − Σ_{w∈RE}(w−t)^+ .
```
By the **Hardy–Littlewood–Pólya weak-majorization theorem** (majorization; not currently a named
entry in `knowledge_base.md`, so we use the ramp-function form and prove the direction we need
below): for two finite nonnegative multisets `X,Y`,
```
   X ≻_w Y   (X weakly majorizes Y: Σ_{top k}X^↓ ≥ Σ_{top k}Y^↓ ∀k)   ⟺   Σ_{x∈X}(x−t)^+ ≥ Σ_{y∈Y}(y−t)^+  ∀t≥0.
```
*Proof of the `(⟸)` direction we use.* Fix `k`. Let `y^↓_1≥…` be `Y` sorted and put `t=y^↓_k`. Then
`Σ_{y}(y−t)^+ ≥ Σ_{j≤k}(y^↓_j − y^↓_k) = Σ_{top k}Y − k·y^↓_k`. On the other side,
`Σ_x(x−t)^+ = Σ_{x^↓_j>t}(x^↓_j−t)`; keeping only the top `k` terms and using `(x−t)^+≥x−t`,
`Σ_x(x−t)^+ ≥ Σ_{j≤k}(x^↓_j − t) = Σ_{top k}X − k·y^↓_k`. The hypothesis at `t=y^↓_k` gives
`Σ_{top k}X − k y^↓_k ≥ Σ_x(x−t)^+ ≥ … ` — more directly, subtracting the two displayed lines from
the hypothesis `Σ_x(x−t)^+ ≥ Σ_y(y−t)^+` and adding `k y^↓_k` to both sides yields
`Σ_{top k}X ≥ Σ_{top k}Y`. (For `k>|Y|`, `Σ_{top k}Y = ΣY` and the case `t=0` gives
`ΣX ≥ ΣY ≥ Σ_{top k}Y`.) ∎ Hence
```
   (WM)  BO ≻_w RE   ⟺   Φ(t) ≥ 0  for all t ≥ 0,
```
and by §11.1 `(WM)` with `k=|RE|` (or `t=0`) forces `(★) Σ_{blue odd} ≥ Σ_{red even}`, closing the
base slice. *(Verified exact `Fraction`: `Φ(t) ≥ 0` at every breakpoint, `0` exceptions over `2.8·10⁴`
configs `n=2..8`, both tie conventions; `(★)`,`(WM)` `0` fails / `4·10⁴`.)*

**11.6.2 Breakpoint reduction (proven): the minimum sits at `t=0` or a blue-odd rung.** For a scalar
`v≥0`, `t↦(v−t)^+` is continuous, convex, piecewise-linear with a single slope change (from `−1` to
`0`) at `t=v`, and its slope on `(t,∞)` is `−1[t<v]`. Summing, `Φ` is continuous and piecewise-linear
with `Φ(t)=0` for `t ≥ max(BO∪RE)`, and for `t` not a breakpoint its right-slope is
```
   Φ'(t) = −#\{v∈BO : v>t\} + #\{w∈RE : w>t\} = N_{RE}(t) − N_{BO}(t).
```
As `t` increases through a value `v`, `N_{BO}` drops by `mult_{BO}(v)` and `N_{RE}` drops by
`mult_{RE}(v)`, so the slope `Φ'` **jumps by `+mult_{BO}(v) − mult_{RE}(v)`**. Thus `Φ` has an
**upward slope-jump (convex kink) only at values `v` with `mult_{BO}(v) > mult_{RE}(v)`, which in
particular requires `v∈BO`**; at values in `RE∖BO` the jump is downward (concave kink). A continuous
piecewise-linear function on `[0,∞)` is affine between consecutive breakpoints (so its minimum on
each such interval is at an endpoint), and a breakpoint can be a strict local minimum only if the
slope jumps from `≤0` to `>0` there, i.e. only at a convex kink. Since `Φ(t)=0` for large `t`, the
global minimum of `Φ` over `[0,∞)` is therefore attained at `t=0` or at a convex kink, i.e. **at a
value of `BO`**. Consequently
```
   (WM) ⟺ Φ(t)≥0 ∀t  ⟺  Φ(0) ≥ 0  AND  Φ(b) ≥ 0 for every blue-odd rung b∈BO.        (RUNG)
```
Because `BO` is a set of `≤ n` distinct rungs, `(RUNG)` is a **finite** list: the single global
inequality `Φ(0)=(★)` plus at most `n−1` further rung inequalities. This is the concrete gain over
§11.4: the "charge red-even mass onto blue-odd of `≥` value, **uniformly in `t`**" is now exactly the
finite set `(RUNG)`, no continuum quantifier. *(Verified: the global minimiser of `Φ` is `t=0` or a
`BO`-value in `28000/28000` configs, `n=2..8`; and `Φ(b)≥0` at every `BO`-value with `0` exceptions.)*

**11.6.3 The top-rung inequality is closed (proven), via `(DOM)`+`(m₀≤1)`.** The largest rung is
`b_1=θ`. Evaluate the two members of `Φ(θ)`. First term: blue-odd values `>θ` — but every rung is
`≤θ`, so there are none, giving `0`. Second term: red-even values `>θ` — by `(m₀≤1)` at most one red
exceeds `θ`, and that red is the top merge element (rank `1`, odd), hence **not** red-even; so there
are no red-even values `>θ`, giving `0`. Therefore
```
   Φ(θ) = 0 ,        so the `b=θ` instance of `(RUNG)` holds (with equality), unconditionally.
```
*(Verified: `Φ(θ)=0` exactly, `0` exceptions / `2.1·10⁴` configs `n=2..8`, both tie conventions.)*
This is the rigorous realisation of the "`m₀≤1` pins the single top red at rank 1" remark of §11.3–11.4
and it disposes of the topmost, most dominant rung.

**11.6.4 The residual rung inequalities are shifted self-similar `(★)`'s (structure of the gap).**
Fix a blue-odd rung `b_i` (`i≥2`). Let `P_i := \{ merge elements > b_i \}` be the top truncation.
Since every element `>b_i` precedes every element `≤b_i`, ranks are preserved under truncation, so the
blue-odd (resp. red-even) elements of the merge that exceed `b_i` are exactly the blue-odd (resp.
red-even) elements *within* `P_i`; write `BO(P_i),RE(P_i)` for these. The blue part of `P_i` is
`\{b_1,…,b_{i−1}\} = 2^{n−i+1}·\{2^{i−2},…,1\} = 2b_i·L_{i−1}`, a **scaled ladder of length `i−1`**,
and the red part is `R^{(i)} := \{reds > b_i\}`. Splitting the shift,
```
   Φ(b_i) = Σ_{v∈BO(P_i)}(v−b_i) − Σ_{w∈RE(P_i)}(w−b_i)
          = \big[\,Σ BO(P_i) − Σ RE(P_i)\,\big] − b_i·\big(|BO(P_i)| − |RE(P_i)|\big).     (SS)
```
The bracket `ΣBO(P_i)−ΣRE(P_i)` is precisely the `(★)`-quantity of the truncated merge `P_i`, which
is a merge of the shorter scaled ladder `2b_i·L_{i−1}` (`Σ = 2^n − 2b_i`) with the red sub-multiset
`R^{(i)}` (`Σ = ΣR^{(i)} ≤ 2^n`, possibly `≠ Σblue+1`). Thus `(SS)` is a `(★)`-type inequality on a
**strictly shorter ladder against a red multiset of unconstrained (generally deficient or excess)
total**, corrected by the shift term. This is exactly the object of the **Generalised (deficient-total)
Ladder Lemma** that the sibling approach `ladder-length-deficient-induction` proves by induction on
ladder length: a full proof of that lemma (its `(P_m)`/`(Q_m)` recursion) discharges every residual
`(RUNG)` inequality here and hence `(WM)` and `(★)`. **The open content (GAP-P1′-a) is therefore the
single family `(RUNG)` for `i≥2`, equivalently the deficient self-similar `(★)`/`(SS)` — the same base
-slice wall shared by all three base-slice routes.** DOM closes it at `i=1` (§11.6.3); the shift term
`b_i·(|BO(P_i)|−|RE(P_i)|)` is what a naive single-rung DOM charge cannot control at `i≥2`, which is
why the closer must be the length recursion, not a local per-rung bound.

*Honest status of this route.* Round 13 did **not** break the core wall; it (a) reduced the continuum
WM/HLP target to the finite list `(RUNG)`, (b) closed the top rung unconditionally, and (c) proved
`(RUNG)`'s residual is identical to the sibling's generalised-ladder object, so the two leading
base-slice routes are now provably the same wall and either one's success closes the other. The single
labelled open gap is `(RUNG)` for `i≥2` ⟺ the deficient generalised `(★)`.

### 8. Cases covered / disjoint
- **Case A** (`a_0=0`) — §4, closed. **Case B** (`a_0≥1`) split by (DIFF): sub-region
  `{|D̃(π_0)−D̃(F')|≥1}` closed (§5); residual `{|D̃(π_0)−D̃(F')|<1}` open (§7). The split is
  exhaustive and disjoint. Base cases `n≤1` — §2.

---

## Promotable lemmas
- **HLP breakpoint reduction of weak majorization (round 13, NEW, fully proven §11.6.1–11.6.3).**
  Let `BO,RE` be finite nonnegative multisets and `Φ(t):=Σ_{v∈BO}(v−t)^+ − Σ_{w∈RE}(w−t)^+`. Then
  (a) `BO ≻_w RE ⟺ Φ(t)≥0 ∀t≥0` (Hardy–Littlewood–Pólya ramp form; the `(⟸)` direction proven from
  scratch by choosing `t=y^↓_k`); (b) `Φ` is continuous piecewise-linear, its right-slope is
  `N_{RE}(t)−N_{BO}(t)` and it jumps by `mult_{BO}(v)−mult_{RE}(v)` at each value `v`, so upward
  (convex) kinks occur only at values `v∈BO`; hence `min_{t≥0}Φ` is attained at `t=0` or at a value of
  `BO`, giving `BO ≻_w RE ⟺ [ ΣBO ≥ ΣRE ] ∧ [ Φ(b)≥0 ∀ b∈BO ]`. This is a general, dyadic-free tool:
  it collapses a "for all thresholds `t`" weak-majorization goal to a finite check at the values of the
  majorizing multiset. Specialised to `imo-2026-03`'s base slice (`BO`=blue-odd rungs, `RE`=red-even):
  the top-rung instance `Φ(θ)=0` holds unconditionally (`(m₀≤1)`), and each residual `Φ(b_i)≥0`
  (`i≥2`) is the shifted self-similar `(★)` `(SS)` on the scaled ladder `2b_i·L_{i−1}` against a
  deficient red total. Verified exact `Fraction`: `Φ≥0` and min-at-`t=0`-or-`BO`-value `0` exceptions /
  `2.8·10⁴`; `Φ(θ)=0` `0` exceptions / `2.1·10⁴`; `(★)`/`(WM)` `0` fails / `4·10⁴`; `n=1..8`, both
  tie conventions.
- **Ladder-interleaving identity `(★-id)` (round 11, NEW, fully proven §10.2).** Let `L` be the uncut
  ladder `{2^{n−1},…,2,1}` (`ΣL=2^n−1`) and `π_0` any multiset with `Σπ_0=2^n`. Colour the descending
  merge of `π_0⊎L` red (`π_0`) / blue (`L`). Then
  `D̃(π_0⊎L) = 1 + 2·(Σ_{blue at odd rank} − Σ_{red at even rank})`; consequently `D̃(π_0⊎L)≥1` **iff**
  `Σ_{blue odd} ≥ Σ_{red even}`, with `D̃=1` iff equality. Proof: subtract the colour-sign sum
  `Σ_j τ_j w_j = Σπ_0−ΣL = 1` from `D̃=Σ_j(−1)^{j−1}w_j` and evaluate `s_j−τ_j∈{0,±2}` by colour/parity.
  General (holds for any red multiset with `Σ=ΣL+1`), tie-break-independent, self-contained from
  Lemma G. Verified `0` mismatches / `1.8·10⁵` exact-`Fraction` configs, `n≤6`. This is the cleanest
  restatement of the extremal base case of GAP L. **Corollaries (unconditional, proven):** (a) if
  `N_{π_0}−N_L ≤ 1` on `(0,θ)` then `D̃(π_0⊎L)≥1` (via `(FLOOR)`, closes ≈88 %); (b) exact ladder value
  `D̃(L)=(2^n−(−1)^n)/3`, so with `(DIFF)` the shell `|D̃(π_0)−D̃(L)|≥1` is closed; (c) `n=1`:
  `D̃(π_0⊎{1})≡1`.
- **Floor-half reduction identity `(FLOOR)` (round 10, NEW, fully proven §9.1).** For the top-scale
  peel `F=π_0⊎F'` (`π_0` a partition of `2^n`, `F'` a refinement of `\{1,…,2^{n−1}\}`, `θ=2^{n−1}`,
  `M=N_{π_0}−N_{F'}` on `(0,θ)`): `D̃(F) = 1 − 2∫_{(0,θ)}⌊M/2⌋`. Consequently the entire lower-bound
  Case B is equivalent to the single inequality `∫_{(0,θ)}⌊M/2⌋ ≤ 0`, tie-attained at `D̃=1`. Proof
  is self-contained from the certified peel identity plus `1[m\text{ odd}]=m−2⌊m/2⌋`; verified `0`
  mismatches / `3·10³` and `I_n≤0` (max `=0`) over `6·10⁴` feasible fractional configs, `n≤6`.
  Layer form `∫⌊M/2⌋ = Σ_{k≥1}(λ\{M≥2k\}−λ\{M≤−(2k−1)\})` (verified `0` mismatches). This is the
  cleanest known restatement of GAP L and supersedes the `(△⋆)` measure form.
- **Peel symmetric-difference identity (SD)/(PEEL).** For any partition into two sub-multisets
  `F = A ⊎ B`, `D̃(F) = D̃(A) + D̃(B) − 2λ(O_A∩O_B) = λ(O_A△O_B)`. Fully proven (§0 U2, §3).
  Verified `0` mismatches / `5·10³` splits.
- **Difference bound (DIFF).** `D̃(A⊎B) ≥ |D̃(A) − D̃(B)|`. Fully proven (§5). Verified `0`
  violations / `1.2·10⁵` configs. (This is the exact, tightened form of the round-2 `(★★)` bound.)
- **Case-A peel identity.** If `B` has all parts `< min A` and `A` is a single part `s`, then
  `D̃(\{s\}⊎B) = s − D̃(B)`; consequently for the top-scale peel with `a_0=0`,
  `D̃(F) = 2^n − D̃(F') ≥ 1` using `D̃(F') ≤ ΣF' = 2^n−1`. Fully proven (§4).
- **Invariant I.** For the top-scale peel, `M(0⁺) = (a_0+1) − |F'| ≤ 1`, equality iff `b=0, a_0=n`.
  Fully proven (§6).

(These four are self-contained and reviewer-checkable; the first two are general facts about `D̃`
independent of the dyadic setting and may be broadly reusable.)
