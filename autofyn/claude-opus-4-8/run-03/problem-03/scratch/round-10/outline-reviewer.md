# Outline review — imo-2026-03, Round 10

Field of 4 nominated: LOWER {parity-measure-potential (advance), ballot-matching (revise)},
UPPER {breakpoint-vertex (advance), valley-differencing-construction (revise)}.
Answer CONFIRMED c(n)=2^n/(2^{n+1}−1). Two isolated walls, each one clean claim; both proven
(R8+R9) to need a GLOBAL/foresight object (every single-pass/greedy/recursion refuted). Per
single-gap-trap Rule I build ONE vehicle per wall; the two revisions stay live as reserves.

---

## parity-measure-potential (advance, LOWER) — CHANGES REQUESTED (build)

Verdict: right vehicle, genuinely new object, build it — but with a hard numeric-first gate.

- Technique is correct and NOT a refuted route. The reserve R_F(τ)=Σ_{f≤τ}f is a MASS quantity, not
  a count; R9 refuted only count-only reserves (ρ_k cumulative surplus, ψ(g(τ)) walk-height). The
  memory rule ("a correct lower reserve MUST track remaining F-mass above the threshold, whole-ladder
  foresight") is exactly what this object does. Amortized charging over dyadic scale-groups G_j via
  certified Lemma ONE-REC (aimo-0019 ink-game template) is a genuinely different proof SHAPE from
  every refuted integral/prefix bound. Sound to build.
- Load-bearing lemma is honestly flagged (RESERVE-MONOTONE, step 4) and it has a stated mechanism
  (charge {g≥2} deficit against the scale's mass budget 2^j; ONE-REC caps overshoot within a scale).
  Steps 1–3,5 are import+definition; the whole difficulty sits in step 4. Acceptable hand-off.
- CONCRETE DEFECT to fix before proving: the skeleton's boundary claims for Φ are inconsistent.
  Step 3 asserts Φ(2^{n−1})=0, but R_F(2^{n−1})=Σ_{f≤2^{n−1}}f = 2^n (every fragment is ≤2^{n−1}, so
  ALL of F sits below τ=2^{n−1}), giving Φ(2^{n−1})=κ·h(2^n)≠0 unless h(2^n)=0. The builder must NOT
  take the skeleton's Φ boundary values on faith — pin κ,h so the telescope Φ(0)=∫φ(g) actually holds.
- GATE (memory rule, R1): the explorer explicitly flagged the (κ,h) potential UNTESTED — no
  grid-search was run. The builder must FIRST numerically verify the amortized invariant
  (min over G_j of the telescoped step ≥ 0, or min_τ Φ ≥ 0 with correct boundaries) against the a=0
  refinement generator for n=3..6 BEFORE writing any proof. Every prior reserve looked plausible and
  died numerically; if this one also fails, record the dead-end honestly (do not hand-wave step 4).
- Watch (from outliner, endorsed): keep the reserve a MASS function R_F(τ), never degrade to g(τ)
  (re-hits refuted ψ); the half-integer witness F={½,½,½},B={½} forbids any structure-free ballot
  argument — the charge MUST use ONE-REC, integrality alone is insufficient.

## ballot-matching (revise, LOWER) — APPROVE as reserve, DO NOT BUILD

- Shares the SAME target inequality (MID-core / Σc_i w_i ≥ 0) as parity-measure. Memory rule (R8):
  a later-credit Hall/transport condition on a line collapses to the prefix-sum inequality by LP
  duality — so it is NOT a genuinely-independent mechanism from parity-measure. The endpoint-splitting
  Hall-check revision (aimo-0129) is a real re-plan of the dead GAP-HALL, so it stays a LIVE reserve
  (kept, not cut) — but per the single-gap-trap Rule I do NOT double up the lower wall. Build one lower
  vehicle only (parity-measure). If parity-measure's mass-reserve stalls, ballot-matching is the
  far-apart activation next round. Slug already registered; nothing to add.

---

## breakpoint-vertex (advance, UPPER) — CHANGES REQUESTED (build)

Verdict: right vehicle, new (existential, not deterministic) shape, build it — with two fixes.

- Not a refuted route. R9 refuted deterministic single-pass policies (band-landing recursion,
  flip-if-helps, drop-one). The two-level EXISTENTIAL move-search (over the finite C(n+1,2)+(n+1) move
  set, pick one landing in the unconditionally-closed a₁'≥L'/2 regime or a VS-certificate one level
  down) is quantified over the MOVE, not a fixed profile-rule — genuinely different, and the explorer's
  numerics back it (100% n≤4, ~98% n=5, failures concentrated EXACTLY on near-uniform → forced case
  split, not cosmetic). The deviation from R9's "one global covering invariant" is justified: the
  explorer checked and found no classical dispersion theorem (Beck–Fiala, three-distance, Steinitz)
  applies, so a bespoke two-case induction from the problem's own recursion is the right pivot.
- FIX 1 (single-proof-split, CLAUDE.md): skeleton step 3 delegates the near-uniform case "in full
  detail" to the reserve valley-differencing-construction and merely cites it. A slug is a WHOLE
  attempt — breakpoint-vertex must prove its near-uniform case INLINE (it may reuse the interleaved
  even-cancellation idea, but the argument must live in breakpoint-vertex.md, self-contained). It may
  NOT depend on an unbuilt sibling slug, or the two are one proof split in two and die together.
- FIX 2 (make-or-break, must be proven not asserted): TWO-LEVEL-MOVE and NEAR-UNIFORM-CANCEL are only
  numerically supported. Both must be proven profile-independently; the case-boundary threshold
  (step 4) must be EXPLICIT and chosen so both cases are provable, not left qualitative. Memory rule:
  a numeric spot-check is not a proof (repeated R3/R4 reviewer).
- Memory guard endorsed: do NOT let the near-uniform bound rest on any monotonicity claim
  ("pushing toward dyadic only decreases the leftover") — minimax V is NOT monotone along
  balanced→dyadic paths (R3 valleys). The interleave-cancel bound must be a direct pairwise-gap
  estimate in the band, not a monotonicity assertion. Note value 0 is admissible (even cancellation),
  which is what makes near-uniform tractable.

## valley-differencing-construction (revise, UPPER) — APPROVE as reserve, DO NOT BUILD

- Genuine re-plan (narrowed to near-uniform only; SIMULTANEOUS U0-style pairing, not the refuted
  greedy descending-difference chain). Kept LIVE as the far-apart constructive dual to
  breakpoint-vertex's existential search. But since breakpoint-vertex must now prove near-uniform
  inline (Fix 1), do NOT build both upper slugs this round (single-gap-trap Rule). If breakpoint's
  near-uniform inline argument stalls, activate valley-differencing next round as the standalone
  constructive attack. Slug already registered; nothing to add. Watch: its INTERLEAVE-CANCEL bound
  carries the same monotonicity risk flagged above — must be a direct band estimate.

---

## Field diversity note (for the orchestrator)

The two walls are cleanly separated and each wall has two distinct MECHANISMS live (LOWER: amortized
mass-potential vs Hall endpoint-splitting certificate; UPPER: existential move-search vs explicit
even-cancellation construction), so a wall will not collapse to one framing. Both built vehicles
attack a NEW global/foresight object this round — the field is NOT stalled on a shared gap. The one
structural risk: breakpoint-vertex step 3 was written as a cross-slug delegation (Fix 1) — corrected
here to keep each slug a whole attempt.

## Ranking (applied via update_ranking)

parity-measure 1754 (leader) > breakpoint-vertex 1620 (advanced, now above induction-peel to reflect
breakpoint advanced R9 while induction-peel dead-ended R7) > induction-peel 1570 (dead-end lever) >
valley-differencing 1536 ≈ smoothing 1535 > ballot-matching 1478 > merge-interleave 1405 >
subset-sum 1392 > lp-dual 1381 > explicit-pairing 1326. No new slugs to register (both revisions keep
their slugs); no copy requested by the outliner.

build set: parity-measure-potential, breakpoint-vertex
