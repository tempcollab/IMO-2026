# Outline Review — imo-2026-03, Round 9

Field: two isolated walls (LOWER MID-core aggregate compensation; UPPER Subset-KK). Outliner
nominates one vehicle per wall to build (parity-measure-potential, breakpoint-vertex) and holds
two mechanism-diverse reserves ranked-and-ready (ballot-matching, valley-differencing-construction).
This respects the single-gap-trap rule (exactly ONE lever per wall in the build set). I verified
no build-set pair shares a wall/inequality, and that both reserves are HELD, not built.

No new slugs to register (all nominees already in the population); outliner requested no branch/copy.

---

## parity-measure-potential — LOWER vehicle — CHANGES REQUESTED (advance, build)

Verdict: right technique class, honest gaps, load-bearing lemma named WITH a mechanism. Build it.

Why the technique is admissible (not a recorded dead end):
- Prefix/running-deficit monovariant is RIGOROUSLY DEAD (F1, ~27%) and the suffix companion is
  DEAD this round too (~89%). The skeleton does NOT reintroduce a one-pass sign — the reserve ρ_k
  is a genuinely 2-D/global object, exactly what the negatives demand. Compliant with the R8 rule.
- Per-dyadic-gap LOCAL compensation is REFUTED this round (20–75%). The skeleton explicitly
  concedes the local statement is false and repairs it with a cross-scale reserve ρ_k that carries
  banked credit down. This is the correct response to the refutation, not a repeat of it.
- Uses Lemma ONE (mandatory: the half-integer counterexample F={.5,.5,.5},B={.5} shows a
  structure-free ballot argument is false). Compliant.

Load-bearing lemma is identified with a stated mechanism (not a bare label):
- Reserve-monotonicity: ρ_{k+1} ≥ ρ_k − deficit_k with deficit_k ≤ ρ_k, mechanism = "Lemma ONE
  recursed caps F-fragments entering scale k at ≤1, bounding the one-step overshoot by banked
  credit." This is a concrete mechanism the builder must verify, not hand-wave.

Issues to close while building (do not block the build):
1. **"Lemma ONE recursed" is itself an unproven sub-lemma, not a certified import.** Certified
   Lemma ONE (top-scale-dichotomy) gives ≤1 piece > 2^{n-1} for a refinement of C_n — a SINGLE
   application. Step 2/step 3 use it "recursed down every dyadic sub-ladder," which requires that a
   truncated sub-ladder of an admissible refinement is itself an admissible refinement of a smaller
   C. That recursion must be stated and proved as its own lemma before ρ_k's per-scale ≤1 bound is
   legitimate. Flag it explicitly; do not treat as a certified reduction (step 1 mislabels it).
2. **Direction of the reserve.** A nonneg top-down reserve banks surplus from COARSER scales to pay
   FINER deficits — it handles "credit-up / debit-down" but NOT "debit-up / credit-down." The
   explorer's data (prefix fails 27%, i.e. some top-down running deficits DO occur) means the
   reserve must actually absorb those 27% bad prefixes. Builder must show ρ_k's banked credit is
   available BEFORE the deficit it pays (ordering), or the induction Φ_k≥0 breaks at the coarse
   scale before the fine credit arrives. This is the make-or-break; keep it honest.
3. Step 4 terminal absorption (ρ_0 vs S_m=|F|−|B|≤0, Fact F2) — the accounting must telescope to
   exactly D(S)−1≥0; confirm the base cases n=0,1 are the certified ones.

Cases: |F|=2 (certified), S_k≤1 / OSR-cap (certified); residual max_k S_k≥2, |F|≥3 only. Coverage OK.

## breakpoint-vertex — UPPER vehicle — CHANGES REQUESTED (advance, build)

Verdict: right technique (scale-recursion, explorer's "most promising" opening 1), honest gaps,
both load-bearing lemmas named WITH mechanisms. Build it.

Why admissible (avoids recorded dead ends):
- NOT a raw 2^{n+1} pigeonhole (Lemma RL forbids it — strict subset reachable). Compliant.
- Two-sided abs-flip kept (one-sided ESF-1 refuted by n=2 witness {9/20,7/25,27/100}). Compliant.
- NOT a single DELETE/MATCH + IH(n−1) (Lemma VS forbids it) — uses a two-step COMPOUND move
  (subset-peel Σ_T + residual-recurse). Compliant.

Arithmetic verified (band-landing crux): β_n = 2^{n-1}u_n EXACTLY for n=2..6, so the claimed band
width (≥2^{n-1}u_nL) equals the max step bound a₂<β_nL. The discrete IVT margin is therefore
exactly zero at the boundary a₂=β_nL — step < width holds STRICTLY only because the valley
inequality a₂<β_nL is strict. This makes the boundary/straddle edge case genuinely load-bearing,
which the outliner correctly flags as open gap (step 2). Good.

Issues to close while building:
1. **Band-landing rigor (step 2).** Discrete IVT gives a prefix sum in an interval of width = max
   step, but the argument needs (a) the target band POSITIONED so |a₁−Σ_T| lands one band lower,
   and (b) the straddle case where Σ_T crosses the band boundary. Both flagged — prove
   profile-independently, no spot-check (standing rule).
2. **Residual is a genuine (n−1)-scale IH instance (step 3) — the make-or-break.** Must show
   {r}∪(survivors∖T) satisfies the valley constraints at the next scale so the RATIO target u_nL
   telescopes (NOT an O(a₁) bound — aimo-0796 is off by 2^{n-1} and is at most a base-case block,
   per both the outliner and the upper explorer). This is the true crux; keep it honest, do not let
   an O(a) bound masquerade as the ratio bound.
3. Budget-legality (|T|−1 cuts + residual recurse = n) via ESF-2 tree-realizability — confirm the
   compound move never exceeds budget n at full budget.

Cases: full-budget valley only (U0 closes m≤n; a₁≥L/2 closed by whole-tail-peel). Coverage OK.

## Reserves — HELD (do NOT build this round)

- ballot-matching (LOWER reserve): revised to a SUFFIX-CUMULATIVE degree bound with long-range
  transport edges. This is a genuine re-plan responding to my R8 warning (a nearest-scale Hall
  condition collapses to the prefix-sum monovariant by LP duality). The suffix-summed double-count
  is at least formally distinct. Ranked-and-ready; activate next round ONLY if parity-measure stalls
  on ρ_k. Do NOT build alongside parity-measure (would be two levers on the LOWER wall).
- valley-differencing-construction (UPPER reserve): revised to a subtractive-Euclidean remainder
  monovariant + drop-one DELETE family, explicitly NOT the monotonicity claim I refuted in R8.
  Numeric drop-one-sufficiency probe mandated before commitment. Held; activate only if
  breakpoint-vertex stalls. Do NOT build alongside breakpoint-vertex.

## Diversity-of-thought note (for the orchestrator)

The field is healthy on diversity: each wall has a built vehicle (potential-induction / scale-
recursion) and a mechanism-DIFFERENT reserve (transport-certificate / explicit-construction). No
collapse to one framing. BUT both walls now depend on the SAME structural engine — "Lemma ONE
recursed down dyadic scales" (LOWER: caps per-scale F-excess; UPPER: the scale bands). If that
recursion turns out false/hard, BOTH walls stall together. Recommend next round's explorers stress-
test the Lemma-ONE recursion as a standalone claim (is a truncated sub-ladder of an admissible
refinement admissible?) — it is the field's single common dependency and is currently assumed, not
certified.

## Ranking (updated, stale cleared on all three last-built slugs)

parity-measure-potential 1730 (leader) · induction-peel 1587 · breakpoint-vertex 1578 ·
smoothing-majorization 1537 · valley-differencing 1514 · two-box-balancing 1502 · ballot-matching
1468 · merge-interleave 1445 · subset-sum-pigeonhole 1403 · lp-dual-weight 1400 · explicit-pairing
1336. Comparisons anchored to evidence: both advancing vehicles beat the dead-end/cold reserves;
breakpoint-vertex (advanced R8) beats induction-peel (dead-end lever R7) despite lower raw Elo.

build set: parity-measure-potential, breakpoint-vertex
