# Build report — peel-integral-exchange — Round 10 — imo-2026-03

## Outcome: partial (GAP-IMR still open; 2 new promotable lemmas delivered)

Target: GAP L (`D̃(F) ≥ 1` for all real feasible `F`) via GAP-IMR (integer minimizer) + Parity
Lemma. Assigned axis: use the certified peel SD/(DIFF) identity as a *cross-scale* integral-rounding
engine (distinct from the twin's within-group smoothing). Did NOT close GAP-IMR. Produced genuine,
verified progress that sharpens the wall to a finite lattice question.

## What was proved (new, rigorous, promotable)
1. **Lemma OB — Odd-Block Alternating-Value Formula.** `D̃(F) = Σ_p (−1)^{p−1} u_{(p)}`, the
   descending alternating sum over the *distinct values of odd multiplicity*; even tie-blocks
   contribute `0`. Proof via per-block `Σ_{t=0}^{r−1}(−1)^t = 𝟙[r odd]`. Verified `0` mismatches /
   `5·10^4` exact-`Fraction` multisets. This is a clean new form of the discrepancy and is the
   natural potential for a monovariant descent.
2. **Lemma V — Vertex Distinct-Value Bound.** `μ=min_{Φ_n}D̃` is attained at a cell-vertex; any such
   positive vertex has `K ≤ n+1` distinct part-values. Proof: LP active-constraint count
   `m ≤ (n+1)+(m−K)`. (Does NOT claim integrality — the refuted TU line is avoided.)
3. **Reduction R + GAP-IMR′.** Rigorously reduced GAP L to the finite statement *"some optimal
   cell-vertex is integer"* (then Parity Lemma ⇒ `μ≥1`). Non-circular (no reference to value `1`).
4. **Localization.** All vertex fractionality lives on **even** tie-blocks fed `≥2` parts by one
   scale (column entry `c_{jl}≥2`) — harmless to `D̃` (OB-int) but blocking in-place integralization.

## Where it stalls (the honest wall)
The cross-scale exchange requires a *non-increasing* integralization of an optimal vertex. Mass
**cannot** cross a scale boundary (each `Σπ_j = 2^{n−j}` is a hard equality), so the only cross-scale
lever is **budget reallocation** (merging parts of a small scale, freeing budget). But merging an
even fractional small-scale block can **increase** `D̃` — shown at `(4,2,½,½)`: `{½,½}→{1}` sends
`D̃ 2→3`. At a global minimizer that vertex is non-optimal, but I could not prove the required merges
are `D̃`-non-increasing *at an optimal vertex*. Also proved: the numerically-supported optimal-face
evenness Conjecture C is **insufficient alone** (evenness ⇏ `μ≥1` without integralization, since in
the continuum even blocks can carry fractional values summing to an odd total). So integrality — not
evenness — is irreducible; the Parity Lemma remains the only known `+1` injector.

## Numerics (exact Fraction)
- Global min `D̃ = 1` reproduced for `n=2,3,4` (local search); fractional value-1 minimizers exist
  (`n=2: {9/4,7/4,2,1}`), but they are non-vertices (`K=4>n+1`), consistent with Lemma V.
- `0` value-1 configs (after pushing to reduce distinct values) had an **odd** fractional block →
  supports Conjecture C.
- GAP-IMR′ holds `n≤3` (certified exact LP, twin §3.1); consistent with all `n≤5`.

## Divergence from the twin (kept the cross-scale axis load-bearing)
The twin attacks within-group same-value smoothing. This slug: (i) new global `D̃` form (Lemma OB),
(ii) vertex/lattice reduction (Lemma V, GAP-IMR′), (iii) the obstruction is diagnosed as a
*cross-scale* budget-reallocation problem (small scales resisting integer splits), NOT a within-group
one — exactly the half of §3.2 the twin cannot reach. The two approaches will not die together on the
within-group half.

## Spec concerns
- Both GAP-IMR slugs share the reduction target + Parity finisher (already flagged by the reviewer).
  This round narrows the shared wall to a FINITE lattice question (GAP-IMR′) — real progress, not a
  restatement. If both stall in R11, seed the reserved far framing (2-adic `aimo-0917`, or a
  Lemma-OB-driven monovariant descent to the canonical integer minimizer). No refuted line reused.
