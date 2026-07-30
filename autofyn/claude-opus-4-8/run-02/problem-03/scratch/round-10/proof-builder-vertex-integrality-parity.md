# Build report — vertex-integrality-parity — Round 10 — imo-2026-03

## Status: partial (GAP-IMR NOT closed; rigorous NEGATIVE established)

## Task
Close GAP-IMR via order-aware minimality smoothing: prove the global infimum of D̃ over the
continuum Φ_n is attained at an integer config, so the certified Parity Lemma finishes P3.

## Outcome
The smoothing mechanism does **not** close GAP-IMR. This round produced a precise rigorous
negative plus a new positive (GAP-IMR proved for n≤3), not a solve. Key results, all with exact
`Fraction`/exact vertex enumeration:

1. **GAP-IMR ⟺ Target (logical equivalence).** Once integer-min = 1 (already proved, Part 2) is
   used, GAP-IMR (`min_{Φ_n}D̃ = min over integer configs`) is equivalent to `μ = 1`, i.e. to the
   target `D̃≥1`. So GAP-IMR is a *reformulation*, not a difficulty-reducing sub-problem. This
   corrects the R9 approach-file "non-circularity" claim.

2. **Exact structure of the optimum.** Global continuum min = 1 for n=1,2,3 (LP over all order-cells
   of all cut vectors). Every min-value(=1) order-cell returns an INTEGER minimizer vertex:
   0/90 fractional at n=2, 0/1134 at n=3. So GAP-IMR is *proved for n≤3*.

3. **Odd fractional-block vertices exist but only off the optimum.** Exact vertex enumeration for
   n=2: 42 vertices carry an odd-size fractional tie-block (e.g. {4,2,1/3,1/3,1/3}, D̃=7/3;
   {4,3/2,1/2,1/2,1/2}, D̃=3). Every one has D̃>1. So odd fractional blocks are excluded only by
   minimality (= value 1 = target), not by cell geometry.

4. **The smoothing has no valid descent.** (a) For n≤3 there is no fractional minimizer, so the
   mechanism's non-trivial case is vacuous and cannot be exercised or validated. (b) At an isolated
   fractional vertex (the actual shape of the odd-frac vertices — e.g. the three 1/3's ARE the whole
   group, any feasible move splits the tie and strictly raises D̃), every feasible perturbation
   strictly increases D̃, so no D̃-non-increasing move exists to descend along. The mechanism cannot
   process the exact case it was designed for.

## What survives (rigorous)
- Parity Lemma (certified, imported) + reduction (GAP-IMR ⇒ target) — correct finishing device.
- Integer-min = 1 with explicit attaining family (verifies answer c(n)=2^n/(2^{n+1}−1) is tight).
- GAP-IMR proved for n≤3 (exact LP).

## Recommendation to orchestrator/outliner
- GAP-IMR is equivalent-difficulty to the target; the two GAP-IMR/mass-transfer slugs
  (vertex-integrality-parity, peel-integral-exchange) attack the full bound in disguise and the
  smoothing engine is insufficient. Do NOT open a fourth rounding variant.
- Fold the Parity Lemma in as the base/finishing device of `peel-scale-rank-induction` (the only
  route that proves the real-valued bound directly, no integrality detour) and concentrate effort
  there.
- Reserved far framing if peel stalls: 2-adic split N=N_++N_- (aimo-0917), or a global monovariant
  descent transporting every F to the canonical D̃=1 family {2^{n−1},…,3,2,1,1}.

## Promotable lemmas
- Parity Lemma — already certified (lemmas/parity-odd-total.md); imported, not re-promoted.
- GAP-IMR ⟺ Target (Part 4.1) — a reusable CAUTION (not a positive lemma) that "reduce to an integer
  minimizer" does not lower the difficulty of this lower bound.

## Spec concerns
None on the problem spec. One process note: the reduction framing recorded in R9 as "non-circular /
easier than the target" was over-claimed; corrected this round to "logically equivalent." Future
outlines should not treat GAP-IMR as a genuine reduction.
