# Build report — gen-func-transform (LOWER, GATED PROBE), Round 15

## Verdict: GATE = NO. Decisive refutation. Recommend RETHINK/dead-end (retire the recursion mechanism).

This was dispatched strictly as a decisive gate: does $Z_n(-1)=\int_0^L(-1)^{g}$ admit a clean
two-band recursion (via certified ONE-REC/TB) carrying a scalar IH toward $Z(-1)\le L-2$, or is it
a repackaging of the already-certified SPLIT cross-term / MID? I ran the gate FIRST in exact
`sympy`/`Fraction`, adversarially (not random), including the mandated witnesses. It is repackaging.

## What was established (all exact arithmetic)

1. **Identity (certified-MID repackaging, closes nothing):** $Z(-1)=L-2\mu\{g\text{ odd}\}$, so
   GAP MID-core ⟺ $Z(-1)\le L-2$. Confirmed exactly on all witnesses. Adds no new content.

2. **Exact two-band decomposition (holds always):**
   $Z_n(-1)=\text{TopBand}(F,F_B)+\int_0^{L/2}(-1)^{N_F(t)}(-1)^{g'(t)}dt$, with
   $g'=N_{F_B}-N_{B_B}$ the level-$(n-1)$ sub-integrand. Verified LHS=RHS at $n=3,4$ on
   $F=\{8,5,3\},\{6,6,4\},\{8,8\},\{4,3,1\}$.

3. **The obstruction:** the bottom band carries the weight $w=(-1)^{N_F}$ inside the sub-instance
   domain. Deviation from a clean recursion:
   $Z_n(-1)-[\text{TopBand}+Z_{n-1}(-1)]=-2\int_{O_F\cap(0,L/2)}(-1)^{g'}$ = exactly $-2\times$ the
   certified dead **SPLIT cross-term** $\mu(O_F\cap O_B)$. Verified exactly (deviation $=-2,-4,0,-2$
   respectively, each equal to $-2\int_{O_F}(-1)^{g'}$).

4. **Clean iff no small $F$-fragment:** the recursion $Z_n(-1)=\text{TopBand}+(-1)^{|F|}Z_{n-1}(-1)$
   holds iff $F$ has no fragment $<L/2$ (weight constant). That is essentially the closed $|F|=2$
   case; the OPEN residual $|F|\ge3$ with an interior fragment breaks it.

5. **Decisive collision (cut-budget-respecting, $n=4$, $\le3$ cuts):** fixed top-level data
   $F=\{8,5,3\}, F_B=\{4,4\}$ and fixed $Z_{n-1}(-1)=0$, three admissible $B_B$ give
   $Z_4(-1)\in\{-4,-2,0\}$. So $Z_n(-1)$ is NOT a function of $(F,F_B,Z_{n-1}(-1))$ — no scalar-IH
   recursion exists.

## Why it collapses (the explicit obstruction, for the run record)

Evaluating the transform at $z=-1$ does NOT linearize the cross-term; it re-introduces precisely
$\mu(O_F\cap O_B)$ — the object Lemma MID was constructed to eliminate. Bounding $Z_n(-1)$ from a
two-band split therefore requires controlling the detailed overlap of $O_F$ with the sub-instance's
odd-set, which is the still-open Gap-Interleaving exchange, NOT a scalar quantity. This is the same
"reframing, not reduction" fate as the vertex-polytope (R14) and LP-dual reframings. It confirms
both the R15 genfunc explorer's prediction and the outline-reviewer's independent prediction
(clean factorization needs $h=N_F-N_{F_B}$ trivial on the bottom band; generically false).

## Consequence for the field

**7th dead lower lever = the transform / generating-function object.** The LOWER wall's exhausted
families are now: scalar-reserve/potential (R10), structured transport/matching (R11),
prefix/termwise monovariant (R8), f-partition single-gap localisation (R12), vertex-polytope/LP-dual
(R14), merge/budget-domination (R15), and now Z-transform recursion (R15). No scalar transform of the
STATIC parity-measure can close MID-core — the difficulty is the $O_F$-vs-$O_B$ overlap and it is
irreducibly global.

Next round MUST attack the LOWER wall from an object that natively controls the $O_F\cap O_B$ overlap
— the shared Gap-Interleaving exchange lemma flagged by the recursion explorer (same DNA as the upper
$L^\star$/GAP-U wall, worth a unified attack), or a 2-scale self-similar recursion
$D(n)=\varphi(D(n-2))$. Do NOT re-seed any transform/generating-function/roots-of-unity recursion on
the static parity-measure.

## Spec concerns
None. The gate was run over the exact stated domain on structured + adversarial + budget-respecting
witnesses (per the R11/R14 rules on structured-family testing); the refutation is exact, not
sampled. No fake proof was shipped. Status set to `unsolved` in the approach file.
