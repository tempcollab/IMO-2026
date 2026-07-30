# Build report — even-rank-doublecount (imo-2026-03, round 8)

**Status: partial. Recommendation: RETHINK the genfn mechanism (cheap-kill refuted it), but PRESERVE
the new reformulation `(⊞)`.**

File written: `/home/agentuser/repo/results/imo-2026-03/approaches/even-rank-doublecount.md`

## Mandatory cheap-kill gate — ran FIRST, results

1. **Target confirmed & tight.** Exhaustive integer refinements: n=2 (7 configs) maxE=3=2^2−1;
   n=3 (62) maxE=7=2^3−1. Real-random 20000/each n=2..5: maxE = 3,7,15,30.74, **0 violations**,
   tight to n=4. Matches certified §9 and the outline-reviewer's brute check.
2. **Reformulation identity is EXACT.** `D̃(F)=∫⊕_j 1[N_j(t) odd] dt` verified 0/20000 mismatch
   (all n≤5, tol 1e-7). Fully proved (Lemma 2.2).
3. **Genfn closing mechanism FAILS the probe.** The scale-graded target `∫⊕s_j≥1` is non-additive.
   Prefix-budget-ok region {Σ_{j≤k}a_j≤k ∀k} has min D̃ = 4.04/8.08/9.00 for n=3/4/5 (huge slack);
   EVERY near-tight (D̃→1) config is front-loaded (budget on top scales). So no per-scale genfn
   defect bound closes it — the (♣)-not-pointwise obstruction reappears verbatim in the scale grading.

## What I proved (fully rigorous, game-free / no measure language)
- **`(⊞)` scale-parity XOR identity + even-rank level form** (Lemma 2.1–2.2): `E(F)=∫⌊N/2⌋`,
  `D̃(F)=∫⊕_j 1[N_j odd] = ½∫(1−∏_jσ_j)` (roots-of-unity form, σ_j=(−1)^{N_j}). Keeps every scale's
  parts separate (NOT a scalar summary of Z). Reusable — promotable to `lemmas/`.
- **Trivial half-bound** `E≤2^n−½` (D̃≥0), with `2^n−E = D̃/2` isolating the missing constant 1 as
  exactly the whole content.
- **Front-loaded/prefix-budget dichotomy**: sharpens the residual — prefix-ok slice is NOT the wall
  (margin ≥ 4,8,9); only the front-loaded slice is. Cleaner cut than the `maxc≥2` description.

## Honest gap
Target `∫⊕_j s_j ≥ 1` on the front-loaded core is unproved. The double-count reformulates it exactly
and secures the sign (D̃≥0) but not the constant 1 — it collapses to the field's shared non-additive
count-parity wall (scalar-summary, top-down reserve, budget-count, local injection all previously
refuted). The bivariate genfn does NOT recover the global bound.

## Routing recommendation
- The **genfn mechanism** for this slug is a RETHINK (cheap-kill gate refuted it, as anticipated by
  the outline-reviewer's "(♣) not pointwise" warning). Do not spend a second build forcing a
  scale-graded genfn identity.
- **Preserve/certify the `(⊞)` identity** — it is a clean, game-free, measure-free restatement that
  recasts the whole lower bound as a **parity-covering problem over n+1 interval-parity functions
  s_j with shared budget Σa_j≤n**. This could seed a genuinely different (covering/discrepancy)
  framing next round — distinct from both merged-order signed sum (A) and ordered-cut potential (B).
- Field signal: A (tiling) and C (this slug) both route through `E(F)≤2^n−1` and both stall on the
  same non-additive core; per the plateau rule, if B (cut-sequence-potential) also collapses to
  budget-count, escalate to a 4th framing that avoids BOTH the merged-order reduction and the static
  E-inequality (e.g. a covering argument directly on the s_j from `(⊞)`).
