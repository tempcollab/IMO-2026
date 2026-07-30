# Build report — absorb-rescale-induction (R14)

**Status: partial.** The route as framed cannot close the b-lift, for a precise, verified reason.

## What I proved (rigorously, exact-Fraction verified)
1. **ABSORB identity (Lemma AB)** `Δ(R,Z)=θ+Δ(R⊎π_1,Z')`, exact, no hypothesis on `π_1`. Two-line
   same-multiset proof. 0 fails / 3000. Promotable.
2. **Refinement-blue max-peel (Lemma MAXPEEL / (I3)-gen)** `D̃(P)=max(P)−D̃(P∖max)`, hence for global
   max `y`: `Δ(R,Z)=y−ΣR+ΣZ−Δ(R∖y,Z)` against ANY blue (generalizes certified (I3) off the full
   ladder). 0 fails / 5000. Promotable.
3. **The exact equivalence chain** `Δ_n(π_0,F')≥0 ⟺ Δ_m(R̄,F'')≥−θ ⟺ D̃(π_0⊎F')≥1`, with all algebra
   shown (`Δ_m(R̄,F'')=½D̃(π_0⊎F')−2^m−½`).

## The wall (why it cannot close as framed) — KEY FINDING
ABSORB on this instance is a **bookkeeping tautology**: `R̄⊎F''=π_0⊎F'` as multisets, so
`D̃(R̄⊎F'')=D̃(π_0⊎F')` and the "reduced" statement `Δ_m(R̄,F'')≥−θ` is *literally the original
target*. Quantitatively (verified m=2..5):
- outline's **rescaled bound** ⇒ `Δ_m(R̄,F'')≥min(0,2^m−ΣR̄)=−2θ`,
- **trivial** `D̃≥0` ⇒ `Δ_m(R̄,F'')≥−θ−½`,
- **target** `−θ`.

So the rescaled engine (GAP-A1/GAP-A2 in the outline) is **strictly weaker than doing nothing** — it
loses `θ−½`. GAP-A2's count-cap accounting is therefore moot: closing it would still only yield `−2θ`.
The whole content is the **missing ½** (lift `D̃(π_0⊎F')` from `≥0` to `≥1`) at tripled mass against a
refinement — the same ½ the base slice injects via Lipschitz (I4), which does not reach a refined blue.

## Remaining gap (GAP-A) — and diversity concern for the orchestrator
Every reduction route either stays at scale `m` (peeling reds by MAXPEEL into the certified window) or,
to reduce scale `m→m−1`, must peel `F''`'s **split** top rung — which is exactly the split-rung-peel
identity `(I1′)`, the crux of the sibling approach `split-rung-mutual-induction`. **absorb-rescale has
no scale-reduction step independent of `(I1′)`; it reduces to the split-rung wall.**

**Spec concern (diversity collapse):** the two live b-lift approaches are NOT independent — absorb-
rescale's only closure runs through split-rung's `(I1′)`. If split-rung's `(I1′)` fails, both die
together (single-gap trap). Per CLAUDE.md's shared-gap rule, next round should seed ≥1 genuinely
different b-lift framing (the peel-scale hedge is already dead/banned). Candidate: attack the missing-½
directly as `D̃(π_0⊎F')≥1` via a refinement-aware Lipschitz/parity injection, not via the ladder
functional at all.

## Numerics
Target confirmed TRUE (not a false wall): worst `Δ_m(R̄,F'')+θ = 0` (attained, never <0) over 40000
exact configs at m=4 with `F''` a random refinement. All scripts: /tmp/absorb_check*.py.
