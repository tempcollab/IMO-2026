# split-rung-mutual-induction

## Status
partial (the outline's clean split-rung identity (I1′) is FALSE; the honest identity re-exposes the
certified odd-set-overlap wall. One genuinely new, verified sub-lemma banked: generalized red-peel
(I3′) for arbitrary blue.)

## Target
Full lower-bound Case B `D̃(π_0⊎F')≥1` for all `n` and every dyadic-cut `F'` (equivalently
`Δ_n(π_0,F')≥0`, `I_n≤0`), completing `c(n)=2^n/(2^{n+1}−1)`.

## Setting and notation (dyadic integer normalization)
`L_m={2^{m−1},…,2,1}`, `ΣL_m=2^m−1`, `θ:=2^{m−1}`. For a finite positive multiset `P`,
`N_P(t)=#{p∈P:p>t}`, `O_P={t>0:N_P(t) odd}`, and by certified **Lemma G**
`D̃(P)=λ(O_P)=Σ_j(−1)^{j−1}w_j` (descending sort, tie-invariant). For red `R` and blue `Z` put
`Δ_m(R,Z):=½(D̃(R⊎Z)−ΣR+ΣZ)`. When `Z` is a refinement of `L_m` (so `ΣZ=2^m−1`),
`Δ_n(π_0,F')≥0 ⟺ D̃(π_0⊎F')≥1` (since `Σπ_0=2^n`, `ΣF'=2^n−1`, direct from the definition of `Δ`).
The `k=0` slice `Z=L_m` is the certified base-slice engine `base-slice-star.md`.

## Approaches tried
- (R14) split-rung mutual induction with the outline's clean split-rung-peel identity (I1′) —
  **DEAD as a closer.** Two verified facts kill it:
  1. **The clean (I1′) form is FALSE.** The outline proposed
     `Δ_m(R,Z)=2^m−1−ΣR−Δ_{m−1}(R,Z')+D̃(ρ_1)` (a SIGN-FLIP of `Δ_{m−1}` plus a closed alternating-sum
     correction) for a split top rung `ρ_1={c_1≥…≥c_{j+1}}`, `Σρ_1=θ`, `Z=ρ_1⊎Z'`.
     Exact-`Fraction` sweep: this identity **fails 3931/4000** random split configs (`m∈{2,3}`).
     Simplest witness (`m=2`, `θ=2`, `j=1`): `R={1}`, `ρ_1={3/2,1/2}`, `Z'={1}=L_1`, so `Z={3/2,1/2,1}`.
     True `Δ_2(R,Z)=3/2`; the clean form predicts `2^2−1−1−Δ_1(R,{1})+D̃({3/2,1/2})=3−0+1... =3`.
     Off by `3/2`. The clean form silently assumed the sign-flip `∫_S 1[N_{R⊎Z'} odd]=D̃(R⊎Z')`,
     which holds ONLY when the flip set `S` covers the whole support (the single-rung case (I1)).
  2. **The honest identity re-exposes the certified overlap wall (the shared wall).** The exact
     relation, derived and verified below (§Derived identity, 0/4000), is
     `Δ_m(R,Z)=Δ_{m−1}(R,Z')+½θ+½D̃(ρ_1)−I_S`, with residual
     `I_S:=λ(O_{ρ_1}∩O_{R⊎Z'})`. By the CERTIFIED peel symmetric-difference identity (SD/PEEL,
     `peel-difference-bound.md` item (1)), `I_S` is exactly the odd-set OVERLAP term that item (1)
     leaves open — the "loaded dyadic-shape invariant on the overlap" the certified bundle names as
     the residual GAP-P1 wall. So the split-rung route, made rigorous, does not open new content: it
     restates the shared overlap wall.
  3. **The only clean scalar bound is too lossy.** `0≤I_S≤λ(S)=D̃(ρ_1)≤θ` gives the clean but weak
     `Δ_m(R,Z)≥Δ_{m−1}(R,Z')` (verified). Telescoped down all scales this yields only
     `Δ_m(R,Z)≥Δ_0(R,∅)=½(D̃(R)−ΣR)≤0` (since `D̃≤Σ` always) — vacuous. Discarding `I_S≥0` discards
     exactly the mass that carries the theorem. Keeping `R=π_0` fixed while peeling one blue scale
     doubles the relative red mass (`ΣR=2^m` against `L_{m−1}`), so the promised "bounded mass" is
     illusory — the same mass difficulty as the absorb route, plus a lost sign-flip.
- (prior rounds, imported context) base slice `b=0` PROVEN & certified (`base-slice-star.md`); every
  π_0-fixed / single-cut / WM-IH / (NEG) / scalar-b / measure route DEAD (run_state).

## Current best
The furthest rigorous progress this round is two exact tools plus a precise localization of the wall.

### Derived split-rung peel identity (exact, replaces the false (I1′))
Let `Z=ρ_1⊎Z'`, `ρ_1={c_1≥…≥c_{j+1}}`, `Σρ_1=θ`, `R` arbitrary. Then
```
   D̃(R⊎Z) = D̃(R⊎Z') + D̃(ρ_1) − 2·λ(O_{ρ_1} ∩ O_{R⊎Z'}),                                  (†)
   equivalently   Δ_m(R,Z) = Δ_{m−1}(R,Z') + ½θ + ½D̃(ρ_1) − I_S,   I_S:=λ(O_{ρ_1}∩O_{R⊎Z'}).
```
**Proof.** `(†)` is the certified SD/PEEL identity `D̃(A⊎B)=D̃(A)+D̃(B)−2λ(O_A∩O_B)`
(`peel-difference-bound.md` (1)) with `A=ρ_1`, `B=R⊎Z'`, together with the fact
`λ(O_{ρ_1})=D̃(ρ_1)=Σ_i(−1)^{i−1}c_i` (Lemma G; the flip set `S=O_{ρ_1}=⋃_{p odd}[c_{p+1},c_p)` has
measure the descending alternating sum — verified `lamS=D̃(ρ_1)`, 0/3000). Converting `(†)` through
`Δ_m(R,Z)=½(D̃(R⊎Z)−ΣR+θ+ΣZ')` and `Δ_{m−1}(R,Z')=½(D̃(R⊎Z')−ΣR+ΣZ')` gives the `Δ`-form. Both
lines verified exact-`Fraction` 0/4000. ∎

The residual `I_S=λ(O_{ρ_1}∩O_{R⊎Z'})` is the certified-open overlap term. **This is the wall.** No
scalar cap on `R` or `Z'` (the (P/Q/LB) style) controls it, because it depends on the fine
interleaving of `R⊎Z'` against the multi-interval set `O_{ρ_1}` — exactly the "whole sub-level
function" obstruction the multicut explorer identified, and precisely the object round-9 role-memory
flags as re-deriving `(△⋆)`.

### Generalized red-peel (I3′) — NEW, verified, PROMOTABLE
The certified red-peel (I3) generalizes from blue `= L_m` to ANY blue `Z` with all parts `≤θ`:
> **(I3′).** Let `Z` be any finite positive multiset with every part `≤θ`, `R` any finite positive
> multiset, and `y=max R` with `y>θ`. Then `D̃(R⊎Z)=y−D̃((R∖y)⊎Z)`, equivalently (when `ΣZ=2^m−1`)
> `Δ_m(R,Z)=2^m−1−Σ(R∖y)−Δ_m(R∖y,Z)`.

**Proof.** Put `P=R⊎Z`, `P'=(R∖y)⊎Z`, so `P=P'⊎{y}` and `N_P(t)=N_{P'}(t)+1[t<y]`. Since `y` is the
maximum of `R` and every blue part is `≤θ<y`, `y≥` every part of `P'`; hence `N_{P'}(t)=0` for `t≥y`,
so `D̃(P')=∫_{(0,y)}1[N_{P'} odd]` and `1[N_P odd]=0` on `(y,∞)`. On `(0,y)`, `N_P=N_{P'}+1`, so
`1[N_P odd]=1−1[N_{P'} odd]`. Therefore
`D̃(P)=∫_{(0,y)}(1−1[N_{P'} odd])=y−D̃(P')`. The `Δ`-form follows by
`Δ_m(R,Z)+Δ_m(R∖y,Z)=ΣZ−Σ(R∖y)` (add the two `Δ`-definitions and cancel `D̃`). ∎
Verified exact-`Fraction` **0/4000** (random `m∈{2,3,4}`, arbitrary blue with parts `≤θ`, one
`y>θ`). This strictly extends certified (I3), which assumed blue `=L_m`. It reduces ANY blue-`Z`
lower bound to the all-red-`≤θ` regime (peel each red `>θ` in turn), exactly as (I3) does for `L_m`.

### Where the wall stands
After (I3′) reduces to all red `≤θ`, the split top rung forces the residual `I_S`. `I_S` is the
certified odd-set overlap `λ(O_{ρ_1}∩O_{R⊎Z'})`; controlling it is `GAP-P1` verbatim. The split-rung
mutual induction therefore does **not** bypass the shared wall — it is a re-encoding of it. The genuine
open content remains: a loaded invariant on the overlap that is *not* a scalar summary of `R` or `Z`.

## Promotable lemmas
- **Generalized red-peel (I3′).** *Statement:* for any finite positive multiset `Z` with every part
  `≤θ:=2^{m−1}`, any finite positive `R` with `y=max R>θ`,
  `D̃(R⊎Z)=y−D̃((R∖y)⊎Z)`; equivalently for a refinement `Z` of `L_m`,
  `Δ_m(R,Z)=2^m−1−Σ(R∖y)−Δ_m(R∖y,Z)`. *Proved:* §Current best above (parity-flip on `(0,y)`,
  `N_{P'}=0` above `y`); verified exact-`Fraction` 0/4000. This is the arbitrary-blue extension of
  certified (I3); safe to import into any blue-`=F'` (P/Q/LB) induction.
- **Split-rung peel identity (†).** *Statement:* for `Z=ρ_1⊎Z'` with `ρ_1` any partition of the top
  rung `θ`, `D̃(R⊎Z)=D̃(R⊎Z')+D̃(ρ_1)−2λ(O_{ρ_1}∩O_{R⊎Z'})`, with `λ(O_{ρ_1})=D̃(ρ_1)=Σ_i(−1)^{i−1}c_i`.
  *Proved:* directly from certified SD/PEEL (`peel-difference-bound.md` (1)) + Lemma G; verified 0/4000.
  (This is a corollary of already-certified machinery, banked here for the record so no future round
  re-proposes the FALSE clean (I1′) form.)

## Spec concerns (for the orchestrator/outliner)
- The outline's load-bearing hypothesis — that the split-rung correction is a CLOSED alternating-sum
  term producing a sign-flipped `Δ_{m−1}` recursion — is **false** (fails 3931/4000; witness above).
  The true correction is the certified odd-set overlap `I_S=λ(O_{ρ_1}∩O_{R⊎Z'})`, which is `GAP-P1`
  itself. So this approach **RETHINK**: as posed it cannot close the b-lift; it re-encodes the shared
  overlap wall rather than opening new content. The "bounded red mass" selling point is illusory —
  keeping `R` fixed while peeling one blue scale doubles the relative red mass, and dropping `I_S≥0`
  telescopes to a vacuous bound.
- Constructive residue worth keeping: (I3′) is a real, verified extension of the certified peel
  machinery to arbitrary blue and should be certified for reuse by any surviving b-lift route.
- Per the diversity note in the outline review: with split-rung reducing to the overlap wall and the
  absorb route sharing the "handle the split top rung" difficulty, the field has now collapsed onto
  that one wall. Next round should seed one genuinely different b-lift framing that attacks the overlap
  term `λ(O_{π_0}∩O_{F'})` with a NON-scalar loaded invariant on `F'`'s cut-tree (the object every
  scalar route has failed on), not another peel of the top rung.
