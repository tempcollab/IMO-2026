## Status
unsolved (new — round 12 skeleton; LOWER wall via majorization of the F-profile against the fixed
dyadic ladder B, plus a B-refinement monotonicity lemma)

## Approach: f-partition-majorization (framing K — compare the ordered F-value profile to the fixed superincreasing ladder B=C_{n-1} via a majorization/rearrangement inequality; control B-cuts by a separate monotonicity lemma)

Target (the whole claim): minimax `D=u_n`, hence `c(n)=2^n/(2^{n+1}−1)`, both bounds. Distinct
contribution: close the LOWER bound MID-core (`D(S)≥1` for `|F|≥3`) by a **majorization/exchange**
argument comparing `F`'s ordered profile to the *fixed* dyadic ladder `B`, treating the two sides
asymmetrically (F variable, B compared to its canonical form) — genuinely far from the reachable-word
LP-vertex route (merge-interleave-pattern) and from all three dead families (scalar-reserve,
transport/matching, termwise monovariant).

Imports (certified, no re-proof): R, M/T, P, PEEL, SPLIT, ONE, ONE-REC, TB, MID, CLIP, OSR.
Residual after import (MID): `S=F⊔B`, `|F|≥3`, all pieces `≤2^{n-1}`, `ΣF=2^n`, `B` a `≤(n−1)`-cut
refinement of `C_{n-1}` (`ΣB=2^n−1`); `g=N_F−N_B` on `(0,2^{n-1})`, `∫g=1`, `D(S)=μ{g odd}`; prove
`μ{g odd}≥1`. Equivalent CLIP `τ=0` face: `Σ_{F even rank}v ≤ Σ_{B odd rank}v`.

### Why the naive "B fixed WLOG" is NOT enough (explorer R12, recorded so it is not retried)
Fixing `B=C_{n-1}` (uncut) and running a pure majorization argument proves ONLY the `c_B=0` slice.
Numerically (R12 explorer, budget-respecting search, n=5): for a FIXED admissible `F`, spending a cut
on `B` STRICTLY lowers `D(F,B)` below the `B`-uncut value in **42.8%** of samples (by up to ~15%
relative) — so `c_B=0` is provably NOT a valid WLOG. The global minimiser does sit at `c_B=0`
(`|F|=n`, matching the certified `L2-telescope`), but that is only true at the JOINT optimum, not per
fixed `F`. Hence a complete proof needs a SECOND ingredient beyond majorization: a monotonicity lemma
bounding the effect of B-cuts. This is the honest structure of the approach.

### Skeleton
1. **Reduce (import).** Via R/M/TB/MID/OSR, the whole lower bound `LB(n)` is MID-core: `μ{g odd}≥1`
   for `|F|≥3`. (`|F|=2` and `0≤g≤1` already closed inside MID.)
2. **Ingredient MAJ — the `c_B=0` slice.** With `B=C_{n-1}` uncut (the fixed superincreasing ladder
   `{2^{n-1},…,2,1}`), view `D(S)=μ{g odd}` as a function of the ordered `F`-profile `f_1≥…≥f_{|F|}`
   (`Σf=2^n`, each `≤2^{n-1}`). Prove `D≥1` by a **majorization/rearrangement inequality**: the
   dyadic-ladder gaps are superincreasing, so as the `F`-fragments are inserted into the fixed ladder
   the odd-measure `Σ_{i odd}w_i` is minimised at the canonical one-fragment-per-gap insertion (value
   telescopes to exactly `1`), and any other `F`-profile majorises it, raising `D`. Uses ONE-REC to
   keep the ladder structure at every scale.
3. **Ingredient GAP B-MONO — cutting B never breaches the floor.** For every fixed admissible `F`,
   `min over admissible B-refinements of D(F,B) ≥ 1`. Mechanism (target): an **exchange/monotonicity
   step on B-cuts** — refining `B` by one cut changes `D` by a controlled amount governed by which
   dyadic gap the new B-fragment lands in; a single-scale exchange shows the minimising `B` is either
   uncut OR a canonical ladder-aligned cut, at which point ingredient MAJ (applied at that scale via
   ONE-REC recursion) gives `D≥1`. Numerically true on ALL samples to date (0 violations of `D≥1`).
4. **Combine.** `D(F,B) ≥ min_B D(F,B) ≥ 1` for every admissible `(F,B)` ⇒ MID-core ⇒ `LB(n)`.
5. Base cases `n≤2` by certified brute force (`min D=1`).

### Key lemmas (claim + mechanism)
- **MAJ (`c_B=0` slice):** with `B` the fixed dyadic ladder, `D=Σ_{i odd}w_i` over F-insertions is
  minimised by the canonical one-F-per-gap layout, value `Σt_k−Σg_k=(2^n−1)−(2^n−2)=1`; any other
  F-profile majorises it. *Because* the superincreasing ladder gaps make the odd-rank partial-sum
  functional Schur-appropriate — moving F-mass to a coarser gap can only add odd-measure (ONE-REC
  keeps ≤1 excursion per scale).
- **GAP B-MONO (make-or-break, genuinely new — unrefuted):** `∀` fixed admissible `F`,
  `min_B D(F,B) ≥ 1`. *Because* refining `B` by one cut perturbs `μ{g odd}` only within the single
  dyadic gap the new fragment enters (local support), so the min over B-refinements is attained at a
  single ladder-aligned configuration where MAJ applies; a B-cut can lower `D` toward `1` but the
  telescoping floor at the aligned configuration is exactly `1`.

### Cases to cover
- `c_B=0` slice (MAJ) and `c_B>0` general B-refinements (GAP B-MONO). Base `n≤2`.

### Watch out
- **c_B=0 is NOT WLOG** (explorer-proven, 42.8% of B-cuts lower D) — GAP B-MONO is MANDATORY, not
  cosmetic. Do NOT present the majorization slice as the whole proof.
- **Risk flag for the reviewer:** GAP B-MONO stated as `min_B D(F,B)≥1 ∀F` is close to MID-core
  restated (it quantifies over B for each fixed F). The DECOMPOSITION only has teeth if the
  exchange/monotonicity step genuinely reduces the B-search to ONE aligned configuration where MAJ
  closes it — that reduction is the real content and must be proved, not assumed. If the exchange
  step cannot localise the minimising B, this collapses back to full MID-core and should be retired.
- **No corpus majorization analogue** for this two-sided (F variable vs fixed ladder, each cuttable)
  structure — explorer scanned inequalities-SOS/convexity subtopics, found none. `aimo-0287`'s local
  adjacent-exchange (`δ` vs `Δ` casework) is a flavour hint for the exchange step ONLY, not a
  ready-made Karamata theorem. Report honestly; do not force a citation.
- Cheap-kill FIRST: exhaustive (not one-cut) adversarial B-refinement search per fixed F, n=4,5,
  confirming `min_B D(F,B)≥1` before committing prose — GAP B-MONO has only been spot-checked.

## Open gaps
- **MAJ:** the majorization inequality for the `c_B=0` slice (step 2).
- **GAP B-MONO:** the B-refinement monotonicity/exchange reducing the min-B search to one aligned
  configuration (step 3) — the genuinely new, unrefuted make-or-break.

## Approaches tried
- (round 12, new) registered as skeleton. Two-ingredient structure (MAJ + GAP B-MONO) isolated;
  c_B=0 explicitly recorded as NOT WLOG per explorer numerics. Far from the LP-vertex route
  (merge-interleave-pattern) and all three dead families.

## Current best
MID-core reframed as `min_B D(F,B) ≥ 1` per fixed `F`, split into the `c_B=0` majorization slice
(MAJ) and the B-cut monotonicity lemma (GAP B-MONO). Reduction imported; both ingredients open.
