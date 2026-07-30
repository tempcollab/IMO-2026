## imo-2026-03 — lens: per-rung-equality invariant (Σπ_j = 2^{n−j} per rung, not aggregate)

**Verdict up front: this lens does NOT open genuinely new terrain. It either (a) collapses to the
already-refuted additive/union framings (rules 39–41, R15) if attacked as a separate charge per
rung, or (b) IS the already-live (P̂/Q̂) ladder-length engine (leader, `ladder-length-deficient-
induction`) if attacked recursively/telescopically. I could not find a third, intermediate form
that is both non-additive-and-non-recursive and carries independent leverage. Recommend: do NOT
open a new slug on this lens; fold the observation below into strengthening the existing (P̂/Q̂)
engine's use of the budget, per the R15/R16 primary directive.**

### Where the per-rung equality already bites (traced through FLOOR/(POS))

- `Σπ_j = 2^{n−j}` for every rung, combined with "all of `F'`'s parts ≤ θ" (Structure Lemma),
  gives `∫_{(0,θ)} N_{π_j} = Σπ_j = 2^{n−j}` **exactly, for every rung independently** (each rung's
  parts are entirely inside the window `(0,θ)` for j≥1 since `2^{n−j} ≤ θ`). Summing over `j≥1`
  reproduces `∫_{(0,θ)}N_{F'} = 2^n − 1`, i.e. exactly the `∫M = 1−β` fact already used in the
  certified `floor-half-reduction.md`. **This is the AGGREGATE-LEVEL content of the per-rung
  equalities — already fully exploited.** The "extra" content the R15 cheap-kill detects
  (min D̃ → 0.386 without exact rung sums) must therefore live in the *distributional/shape* level:
  not just that each rung's mass integrates correctly, but *where within (0,θ)* that mass sits
  (governed recursively: rung j's own parts are further split with the SAME "≤ one part exceeds
  half the rung total" self-similar structure, since `Σπ_j = 2^{n−j}` forces at most one part of
  π_j to exceed `2^{n−j−1}` — exactly the β-argument used for π_0, recursively, one scale down).
- That recursive "at most one part exceeds half-of-own-rung-sum" fact, applied scale by scale, is
  **exactly what the certified peel identity / correction (C) and the (P̂/Q̂) mutual induction
  already use at every induction step** (going from ladder-length `m` to `m−1` consumes exactly
  `Σρ_i = 2^{m−i}`). So the "keyed on the exact rung-sum equality, not aggregate counts" mechanism
  the R15 meta pointed to is not a new object — it is the load-bearing hypothesis of the live
  leader engine, used recursively, not additively.

### Numerically confirmed (this round, exact `Fraction`, reproducing + tightening the R15 cheap-kill)

- Reproduced the R15 cheap-kill directly: generating feasible dyadic `F` with the exact per-rung
  sums `Σπ_j=2^{n−j}` enforced (n=4, 3000 trials, random cut counts respecting Σa_j≤n), `I_n :=
  ∫⌊M/2⌋` never exceeds ≈`−0.0096` (max observed, consistent with the certified tie `I_n=0`,
  `D̃=1`) — no violation.
- Separating witness (aggregate-only, NO individual rung-sum constraint, only total mass
  `2^{n+1}−1` split into `n+1..2n+2` arbitrary positive parts, same overall part-count regime as
  the feasible family): `D̃` (descending alternating sum) drops to `0.202` at `n=4` over 20000
  trials — well below the target `1`, confirming the R15 finding (they report `→0.386`; my quicker
  probe with a wider part-count window finds an even lower `0.202`, so the true infimum without
  per-rung equality may be lower still, i.e. potentially `→0` or negative with a fuller search).
  This is a genuine, reproducible separating witness: **per-rung equality is load-bearing; the
  aggregate total alone is not.**

### Attempted (and failed) to find a genuinely NEW mechanism

- Checked whether Q (the negative-layer integral, `Q := Σ_kλ{M≤−(2k−1)}`, the wall side per
  `positive-layer-localization.md`) could be lower-bounded by ANY **purely additive per-rung**
  quantity (a sum of terms each depending only on one `π_j`'s own shape, no cross-rung
  interaction). This is exactly the shape already cheap-killed in R15 (rule 39/41 in
  `/tmp/memory/math-explorer.md`): the trivial subadditive union bound on the overlap
  `λ(O_{π_0}∩O_{F'}) ≤ Σ_jλ(O_{π_0}∩O_{π_j})` holds but is too weak (fails to close `I_n≤0` on
  1125/3000 trials, deficit up to −7.6, n=4), and cross-rung `D̃` effects are strongly
  non-additive (joint vs sum-of-isolated gap up to 6.5). I did not find a variant escaping this;
  `Q` is a genuinely global count (`M` sums contributions from ALL rungs at once at each `t`), so
  no per-rung-local functional can certify it without cross terms — consistent with the R15
  negative.
- Checked whether a **linear/Abel-summation combination with rung-dependent but fixed
  coefficients** (e.g. `Σ_j c_j·a_j` or `Σ_j c_j·D̃(π_j)`, `c_j` depending only on `j`, not on the
  other rungs' shapes) could dominate `−I_n`. This is structurally the same "scalar-per-rung
  summary" family already refuted for the single scalar `b` (R11: exact ties `I_n=0` occur at
  `b=2,3`, so a single scalar has zero separating power) — a per-rung generalization inherits the
  same obstruction unless the coefficients are allowed to depend on the OTHER rungs' realized
  shapes, at which point it is no longer "local per rung" and becomes the recursive (P̂/Q̂)
  induction in disguise.

### Distinct openings surfaced (for the outliner, ranked by how far from the leader they are)

1. **(Weakest new content, likely re-encode)** A "rung-recursive telescoping charge" that walks
   scale by scale using `Σπ_j=2^{n−j}` exactly at each step — this is definitionally the certified
   `(P̂_m)/(Q̂_m)/(L̂B_m)` engine already advancing on the cut-top-rung leaf. Not a new slug; fold
   into the primary engine.
2. **(No leverage found)** Any additive/union per-rung charge for the overlap or the `Q` layer —
   REFUTED by R15's union-bound cheap-kill (rule 39/41) and reconfirmed structurally above (Q is
   an inherently cross-rung count).
3. **(Untried, genuinely different, worth a cheap probe next round if the leaf stalls again)** A
   **counting/pigeonhole argument on the *number of sign changes* of `M` across `(0,θ)`**, rather
   than its layer-integral. Since `M` changes by ±1 at each of the `(a_0+1) + Σ_{j≥1}(a_j+1)`
   breakpoints (a finite step function), and the per-rung equalities pin the total step count
   exactly (`Σ(a_j+1)` over `j=1..n` `= n+Σ_{j≥1}a_j`), a **discrete alternating-run-length /
   Sperner-type argument** on the *sequence* of ±1 steps (rather than the measure `∫⌊M/2⌋`) might
   supply the missing `+1` via a genuinely combinatorial (not measure-theoretic) parity count. I
   did NOT verify this has independent leverage — it is untested, offered only as a candidate
   third framing, since it is not measure/merged-order/sequential/genfn (R8 dead list) nor a
   direct clone of (P̂/Q̂). Flag as speculative, not vetted.

### Candidate technique(s)
- Confirmed: no new technique beyond what's already certified. The genuine content of "per-rung
  equality ≠ aggregate" is already fully captured by the (P̂/Q̂) engine's recursive peel steps and
  by `positive-layer-localization.md` (POS, for the π_0 side). Any NEW leverage must come from a
  combinatorial (discrete step-sequence) recast of `M`, not a measure recast — untested (see
  opening 3 above).

### Cheap-kill candidates
- Before building opening 3: cheap-kill it FIRST by checking numerically whether the discrete
  step-sequence of `M` (the sequence of ±1 jumps in breakpoint order) has any clean run-length or
  alternation invariant forcing `I_n≤0` on a handful of near-tight configs (the extremal ladder
  family + its neighbors) before committing a full slug.

### Knowledge-base entries to use
- None beyond what's already imported (`lemmas/floor-half-reduction.md`, `positive-layer-
  localization.md`, `cut-top-rung-correction.md`). No new `knowledge_base.md` entry surfaced by
  this lens.

### Analogous past problems (cruxes)
- None newly found. The closest corpus match remains the already-recorded `aimo-0117` (largest
  exceeds sum of rest, dyadic dominance — already used for the base-slice `(★)` proof) and
  `aimo-0388` (parity forces `|diff|≥1` on an alternating merged sum, already recorded as a
  baby-P3 template, round 12). Neither adds anything specific to the per-rung-equality question;
  I did not find a corpus problem whose crux is "exploit exact per-scale sum constraints as
  opposed to an aggregate budget" in a discrepancy game.

### Prior progress
- Whole problem: `partial`. b-lift reduced to the single cut-top-rung leaf (R15,
  `ladder-length-deficient-induction`), correction `(C)` certified. This lens does not advance
  that leaf directly; it confirms the leaf's existing machinery already IS the correct exploitation
  of per-rung equality.

### Dead ends (do not retry)
- Additive/union per-rung charge for the overlap or for `Q` (R15 rule 39/41, reconfirmed here
  structurally — `Q` is inherently cross-rung).
- Any per-rung scalar-coefficient linear combination with coefficients independent of other rungs'
  realized shapes (inherits the R11 scalar-`b` refutation, exact ties at `b=2,3`).
- Treating "per-rung equality" as a route distinct from the (P̂/Q̂) engine's own recursive peel —
  it is the same mechanism under a different name.

### Small-case / intuition notes (conjectural, numeric only)
- Reproduced (n=4, exact `Fraction`): with exact per-rung sums enforced, `max I_n ≈ −0.0096` over
  3000 trials (consistent with certified `I_n≤0`, tie at `0`). Without per-rung sums (aggregate
  total + budget only), `min D̃ ≈ 0.202` over 20000 trials at n=4 (below `1`, confirms/tightens the
  R15 finding of `0.386`) — strong conjectural confirmation that per-rung equality is load-bearing
  and cannot be relaxed to an aggregate statistic, but this was already established in R15; my
  contribution is a tighter witness and the structural argument for WHY it collapses onto (P̂/Q̂).
