# Build report — parity-measure-potential (LOWER wall), round 9

**Status: partial** (GAP MID-core remains open; genuine advance on the structural lemma + reserve
refutation).

## What I did (assigned: strengthened-IH scale reserve `ρ_k`, peel top gap via Lemma ONE recursed)

1. **Proved Lemma ONE-REC** (reviewer concern #1 — "Lemma ONE recursed is not certified"). The true
   form: a scale-truncation `B_{≤ℓ}=⊔_{j≤ℓ}G_j` of any refinement of `C_m` is itself a refinement of
   `C_ℓ` (partition-of-cuts identity), and each scale-group `G_j` has `≤1` fragment `> 2^{j−1}`
   (superincreasing). This reduces the field-wide "Lemma ONE recursed" to certified Lemma ONE + a
   triviality. Written as candidate `lemmas/recursed-dyadic-dichotomy.md`, proposed for certification.
   It is the single common structural dependency of BOTH walls, so certifying it de-risks both.

2. **Exact residual integrand.** MID-core `μ{g odd}≥1` `⟺` `∫_0^{2^{n−1}}φ(g)≥0` with
   `φ(c)=1[c odd]−c`, and `φ≥0 ⟺ c≤1`, `φ<0 ⟺ c≥2`. Negative mass sits exactly on `{g≥2}`
   (F leads by ≥2), positive on `{g≤0}` (B leads). Cleanest statement of the residual so far.

3. **Refuted the proposed reserve** (reviewer concern #2 — must absorb the ~27% bad top-down
   prefixes). The reserve `ρ_k` as "cumulative overshoot of local ∫g" is the top-down cumulative
   `∫_τ^{top}φ(g)`; numerically it reaches `−30.5` at `n=6` (negative in 6–8% of instances), the
   bottom-up version `−23`, and the deficit **grows with n** (so no additive constant repairs it).
   Also proved no reserve `ψ(g(τ))` depending only on the current walk height can work: the `{g=2}`
   band has unbounded measure per unit height. Conclusion: a correct reserve must be a whole-ladder
   object tracking *remaining F-mass above τ*, not a local surplus. This is exactly the reviewer's
   feared failure mode, made rigorous — the outliner's specific `ρ_k` mechanism is dead as stated.

4. **Ladder litmus (reviewer constraint #3) passed.** My argument invokes Lemma ONE-REC, which is
   unavailable for the `F={½,½,½},B={½}` witness (D=0), so it cannot certify that counterexample —
   confirming genuine use of the dyadic structure.

## Honest gap

GAP MID-core (`|F|≥3`, `max_k S_k≥2`, i.e. `∫φ(g)≥0` with `{g≥2}` present) is **not closed**. The
route's reserve, in the assigned "nonnegative cumulative-surplus" form, is refuted; the correct
reserve is a mass-tracking whole-ladder potential I did not construct/verify this round.

## Promotable lemmas
- **Lemma ONE-REC** (recursed dyadic dichotomy) — FULLY PROVED, candidate file written, propose
  certify. Shared by both walls.
- Reformulation `μ{g odd}−1=∫φ(g)`, `φ(c)=1[c odd]−c` — FULLY PROVED.
- NEGATIVE: nonnegative cumulative-surplus reserve does not exist (either direction); walk-height
  reserve `ψ(g(τ))` also fails — record to prune levers.

## Recommendation to orchestrator
The naive reserve is refuted. The two live LOWER options now are: (a) build the **ballot-matching**
reserve (suffix-cumulative Hall / long-range transport) next round — its long-range-edge design is
exactly the "whole-ladder, not local" object my refutation points to; or (b) re-plan parity-measure
with the mass-tracking reserve `ρ(τ)=2^n − (F-mass fully above τ)` coupled to the walk. Lemma ONE-REC
is now available to both. Recommend next round put the mass-tracking-reserve construction explicitly
in the outline (it is the specific object my R9.2 refutation identifies as the only viable shape).

## Spec concerns:
None. (The outliner's `ρ_k`-as-cumulative-overshoot is refuted, but that is a technical dead end I
recorded, not a spec ambiguity; the target claim `D(S)≥1 ⇔ c(n)=2^n/(2^{n+1}−1)` is correct and
unchanged.)
