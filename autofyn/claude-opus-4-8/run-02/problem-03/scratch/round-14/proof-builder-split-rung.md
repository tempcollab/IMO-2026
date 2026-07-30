# Build report — split-rung-mutual-induction (R14)

## Verdict
Status: **partial** (route does NOT close the b-lift; RETHINK-worthy). The outline's crux identity is
false; the honest identity re-encodes the certified shared overlap wall.

## What I proved
1. **Exact split-rung peel identity (†)** (replaces the outline's false (I1′)):
   `D̃(R⊎ρ_1⊎Z') = D̃(R⊎Z') + D̃(ρ_1) − 2·λ(O_{ρ_1}∩O_{R⊎Z'})`, with
   `λ(O_{ρ_1})=D̃(ρ_1)=Σ_i(−1)^{i−1}c_i`. It is a corollary of certified SD/PEEL
   (`peel-difference-bound.md` (1)) + Lemma G. Verified exact-`Fraction` 0/4000.
2. **Generalized red-peel (I3′)** — genuinely new, verified 0/4000: certified (I3) extends from
   blue `=L_m` to ANY blue `Z` with parts `≤θ` and `y=maxR>θ`: `D̃(R⊎Z)=y−D̃((R∖y)⊎Z)`. Full parity
   proof written. Promotable — reduces any blue-`=F'` bound to the all-red-`≤θ` regime.

## The gap (unclosed, and why it cannot close as posed)
- The outline's clean sign-flip form `Δ_m=2^m−1−ΣR−Δ_{m−1}(R,Z')+D̃(ρ_1)` is **FALSE**: fails
  3931/4000. Witness (`m=2`,`θ=2`,`j=1`): `R={1}`, `Z={3/2,1/2,1}` (`ρ_1={3/2,1/2}`, `Z'=L_1={1}`):
  true `Δ_2=3/2`, clean form gives `3`. The clean form silently assumed the full sign-flip
  `∫_S 1[N_{R⊎Z'} odd]=D̃(R⊎Z')`, valid only when `S=O_{ρ_1}` covers the whole support — i.e. only the
  single-rung (I1). Split rungs give `S` a strict multi-interval subset of `(0,θ)`.
- The true residual is `I_S=λ(O_{ρ_1}∩O_{R⊎Z'})`, the certified odd-set OVERLAP term that
  `peel-difference-bound.md` (1) itself leaves open (GAP-P1). So the route re-encodes the shared wall.
- Only clean scalar bound `0≤I_S≤λ(S)=D̃(ρ_1)` gives `Δ_m(R,Z)≥Δ_{m−1}(R,Z')`, which telescopes to
  the vacuous `Δ_m≥½(D̃(R)−ΣR)≤0`. "Bounded mass" is illusory: fixing `R` while peeling one blue scale
  doubles relative red mass — same difficulty as the absorb route, minus a sign-flip.

## Spec concerns
- **Outline flaw:** GAP-B1's mechanism is factually wrong (the correction is not a closed alternating
  sum; it is the overlap). This is a RETHINK for the slug — as posed it cannot close.
- **Field collapse:** split-rung reduces to `λ(O_{π_0}∩O_{F'})`; absorb shares the split-top-rung
  difficulty. Both bottom out on the SAME overlap wall. Per the shared-gap rule, next round needs one
  genuinely different framing attacking the overlap with a NON-scalar loaded invariant on `F'`'s
  cut-tree — not another top-rung peel.
- **Bank:** certify (I3′) (arbitrary-blue red-peel); it is verified and reusable.

## Files
- results/imo-2026-03/approaches/split-rung-mutual-induction.md (written; Status partial)
- No lemma file created (I3′ noted as Promotable for reviewer certification; (†) is a corollary of
  already-certified SD/PEEL).
