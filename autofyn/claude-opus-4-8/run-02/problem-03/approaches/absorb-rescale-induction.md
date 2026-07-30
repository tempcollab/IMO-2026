# absorb-rescale-induction

## Status
partial

## Target
Full lower-bound Case B for all `n` and every dyadic-cut response `F'`:
`Δ_n(π_0,F')≥0` (equivalently `D̃(π_0⊎F')≥1`, `I_n≤0`), which with the certified UB, Case A, and the
certified base slice (★) completes `c(n)=2^n/(2^{n+1}−1)`.

## Technique
Strong induction on the SCALE `n`, applying the exact ABSORB identity ONCE per step to fold `F'`'s
(possibly split) top rung into the red side, then closing by a rescaled deficient bound. This round's
build was to close the `−θ` recovery (GAP-A1) and the count-cap budget (GAP-A2).

## Approaches tried
- **R14 (this round) — ABSORB-once + rescaled deficient bound.** Established every identity the route
  rests on RIGOROUSLY (ABSORB exact 0/3000; refinement-blue max-peel `(I3)-gen` exact 0/5000; the
  equivalence chain exact). **Outcome: the route as framed cannot close, for a precise, checkable
  reason (below), and its natural completion is NOT independent of the sibling split-rung identity.**
  Recorded as an honest partial + a diversity-collapse finding for the orchestrator. Two promotable
  identities extracted (ABSORB, refinement-blue max-peel).
- (Prior) `π_0`-fixed single/multi-cut descent, WM-IH inheritance, `(NEG) Q≥S_π`, scalar `b`-cutoff,
  measure/merged-order/sequential/genfn/GAP-IMR, naive ABSORB iteration — all DEAD (run_state Broken).

## Current best

### Notation and imported facts (all certified)
`L_m:={2^{m−1},…,2,1}`, `ΣL_m=2^m−1`, `θ:=2^{n−1}`, `m:=n−1`. `N_P(t)=#{p∈P:p>t}`. By certified
**Lemma G**, `D̃(P)=∫_0^∞1[N_P(t)\ odd]\,dt=Σ_j(−1)^{j−1}w_{(j)}` (`w` sorted descending, tie-invariant).
For a red multiset `A` and blue `B`, define `Δ(A,B):=½(D̃(A⊎B)−ΣA+ΣB)`; when `B=L_m` this is the
certified `Δ_m(A)` because `ΣL_m=2^m−1`. By `floor-half-reduction.md` and
`ladder-interleaving-identity.md`, Case B is exactly `Δ_n(π_0,F')≥0`, equivalently `D̃(π_0⊎F')≥1`.

Peel structure (certified dyadic **Structure Lemma**): `F=π_0⊎F'`, `Σπ_0=2^n`, `F'` a dyadic
refinement of `L_n` with `ΣF'=2^n−1`; write `F'=π_1⊎F''` where `π_1` = the parts of `F'` refining the
top rung (`Σπ_1=θ`, parts `≤θ`) and `F''` a refinement of `L_m` with `ΣF''=2^m−1=θ−1`.

### 1. ABSORB identity — PROVEN (promotable Lemma AB)
For any red `R`, any split `Z=π_1⊎Z'` with `θ:=Σπ_1`:
```
   Δ(R,Z) = θ + Δ(R⊎π_1, Z')            (ABSORB, exact, no hypothesis on π_1)
```
*Proof.* `R⊎Z=(R⊎π_1)⊎Z'` as multisets, so `D̃(R⊎Z)=D̃((R⊎π_1)⊎Z')`. Expand the RHS:
`Δ(R⊎π_1,Z')=½(D̃((R⊎π_1)⊎Z')−(ΣR+θ)+(ΣZ−θ))=½(D̃(R⊎Z)−ΣR+ΣZ)−θ=Δ(R,Z)−θ`. ∎
Verified 0 fails / 3000 exact `Fraction` (this round; matches reviewer 0/3000).

Applied here with `R=π_0`, `Z=F'`:
```
   Δ_n(π_0,F') = θ + Δ_m(R̄, F''),   R̄:=π_0⊎π_1,  ΣR̄=2^n+θ=3·2^m.
```
Hence the target `Δ_n(π_0,F')≥0` is **equivalent to** `Δ_m(R̄,F'')≥−θ`.

### 2. The `−θ` target is EXACTLY `D̃(π_0⊎F')≥1` — and ABSORB is a bookkeeping tautology (KEY FINDING)
Compute directly:
`Δ_m(R̄,F'')=½(D̃(R̄⊎F'')−ΣR̄+ΣF'')=½D̃(R̄⊎F'')−½·3·2^m+½(2^m−1)=½D̃(R̄⊎F'')−2^m−½`.
Therefore
```
   Δ_m(R̄,F'') ≥ −θ = −2^m   ⟺   ½D̃(R̄⊎F'')−2^m−½ ≥ −2^m   ⟺   D̃(R̄⊎F'') ≥ 1.
```
But `R̄⊎F''=π_0⊎π_1⊎F''=π_0⊎F'` as multisets, so `D̃(R̄⊎F'')=D̃(π_0⊎F')`. Thus the reduced
statement `Δ_m(R̄,F'')≥−θ` is **literally the original target** `D̃(π_0⊎F')≥1`.

**Consequence (why the outline's rescaled closer cannot work).** ABSORB is an exact identity, but on
this instance it is a *tautology*: it re-groups the same multiset, so `D̃` is unchanged and no bound is
advanced by ABSORB alone. Quantitatively:
- The **trivial** bound `D̃≥0` (measure) already gives `Δ_m(R̄,F'')≥−2^m−½=−θ−½`.
- The **rescaled deficient-bound** proposed in the outline gives `Δ_m(R̄,F'')≥min(0,2^m−ΣR̄)=2^m−3·2^m=−2·2^m=−2θ`,
  which is **weaker than the trivial bound** by `θ−½` (verified `m=2..5`: rescaled `−2θ`, trivial
  `−θ−½`, target `−θ`).

So the rescaled-engine framing (GAP-A1/GAP-A2) cannot close the `−θ` target — it is strictly weaker
than doing nothing. The **entire content** is the *missing ½*: lifting `D̃(π_0⊎F')` from its trivial
`≥0` to `≥1`, at tripled red mass `3·2^m` against a ladder-refinement `F''`. This is the same
missing-½ that the certified base slice injects via the Lipschitz collapse `(I4)` — but here against a
refined blue, where `(I4)` does not reach.

### 3. Refinement-blue max-peel — PROVEN (promotable Lemma MAXPEEL / `(I3)`-gen)
For ANY multiset `P`, `D̃(P)=max(P)−D̃(P∖max(P))` (the alternating sum peeled from the top). Hence if
`y=max R̄` is the **global** maximum of `R̄⊎F''` (guaranteed whenever `R̄` has a part `≥2^m`, since all
blue parts `≤2^{m−1}<2^m≤y`):
```
   Δ_m(R̄,F'') = y − ΣR̄ + (2^m−1) − Δ_m(R̄∖y, F'').
```
*Proof.* `D̃(R̄⊎F'')=y−D̃((R̄∖y)⊎F'')` by the top-peel; substitute into
`Δ_m(R̄,F'')=½(D̃(R̄⊎F'')−ΣR̄+ΣF'')` and re-collect against
`Δ_m(R̄∖y,F'')=½(D̃((R̄∖y)⊎F'')−(ΣR̄−y)+ΣF'')`. ∎ Verified 0 fails / 5000 exact (refinement blue).

This is the certified `(I3)` red-peel, generalized to a *refined* blue (it needs only `y` = global
max, no hypothesis on blue's shape). It lets us peel the (**at most one**, since `Σπ_0=2^{m+1}`) red
part exceeding `2^m`, and successively any red part exceeding the blue max, driving `ΣR̄` down into the
certified mass window `ΣR≤2^{m+1}` **without changing scale `m`**.

### 4. Where it stops — the residual gap (GAP-A), and the diversity finding
Peeling large reds by §3 keeps the scale at `m`. To *reduce* the scale `m→m−1` (the only way to reach
the induction base and shrink the object), one must peel the **top rung** of the blue object `F''`.
For a full ladder that is the certified rung-peel `(I1)`; but `F''`'s top rung is **split** into the
parts `π_1''⊆F''`, so peeling it is exactly the **split-rung-peel identity `(I1′)`** — the crux of the
sibling approach `split-rung-mutual-induction`. Pursued to its natural end, absorb-rescale has **no
scale-reduction step independent of `(I1′)`**.

**GAP-A (open):** prove `D̃(R̄⊎F'')≥1` for red `R̄` of mass `3·2^m` (parts `≤2^{m+1}`, count
`a_0+a_1+2`) against a ladder-refinement `F''` — equivalently inject the missing `½` at tripled mass
against a refined blue. Every reduction route (peel reds by §3, or peel the blue top rung) either stays
at scale `m` or invokes the split-rung-peel `(I1′)`. So this route reduces to the split-rung wall and
is **not** an independent line.

Numerics confirming the target is TRUE (so the wall is real, not a false target): over 40000 exact
`Fraction` configs at `m=4` (`R̄` mass `3·2^m`, `F''` a random refinement of `L_m`), the worst value
of `Δ_m(R̄,F'')+θ` was exactly `0` (attained), never negative — consistent with the certified fact
that `D̃(π_0⊎F')≥1` with equality at the tie family.

## Full proof
(Not present — Status is `partial`. The route is blocked at GAP-A, which coincides with the
split-rung-peel wall of the sibling approach; see §2–§4 for why the outline's rescaled closer is
strictly weaker than trivial and cannot close it.)

## Promotable lemmas
- **Lemma AB (ABSORB).** `Δ(R,Z)=θ+Δ(R⊎π_1,Z')` for any split `Z=π_1⊎Z'`, `θ=Σπ_1`, with
  `Δ(A,B)=½(D̃(A⊎B)−ΣA+ΣB)`. Exact, no hypothesis on `π_1`. Proved in §1 (same-multiset expansion);
  verified 0/3000 exact. One level more general than certified `(I1)` (which fixed `π_1={θ}` and
  required all red `≤θ`). *Caveat for future use:* on the b-lift instance it is a tautology (§2) — it
  advances no bound by itself; useful only as a bookkeeping bridge inside an induction that supplies
  independent content.
- **Lemma MAXPEEL (`(I3)`-gen, refinement blue).** For any multiset `P`, `D̃(P)=max(P)−D̃(P∖max(P))`;
  hence for red `R`, blue `Z` with `y=maxR≥maxZ` (global max), `Δ(R,Z)=y−ΣR+ΣZ−Δ(R∖y,Z)`. Proved in
  §3; verified 0/5000 exact against refined blue. Generalizes certified `(I3)` from `Z=L_m` to any
  blue; needs only `y` = global max.
