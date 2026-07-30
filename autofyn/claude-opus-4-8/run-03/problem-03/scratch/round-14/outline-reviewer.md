# Outline review — imo-2026-03, Round 14

Answer CONFIRMED c(n)=2^n/(2^{n+1}−1), minimax D=u_n=1/(2^{n+1}−1). Both walls partial.
Field: ONE vehicle per wall + one constructive upper hedge (gated below). Reviewed against the
FIVE dead upper families (covering-radius ×2, density/COUNT, greedy recursion, bounded-depth
escape, mass-telescope/DSUM) and the FOUR+ dead lower families (scalar-reserve, structured
matching, prefix/termwise monovariant, f-partition single-gap localisation, canonical-ATT
characterization).

---

## LOWER — merge-interleave-pattern (revise): APPROVE (gate-bound)

Technique: LP-duality / same-group exchange-smoothing (Farkas certificate) on the CERTIFIED
interleave-word polytope P_T, target min_{vertex} L_T ≥ 1 for every type T. Whole-claim lower
bound (D(S)≥1 for every ≤n-cut admissible refinement of C_n). This is a genuine, end-to-end
attempt, not a fragment.

Soundness of the skeleton:
- The weak-duality logic is valid: if L_T(v)−1 ≡ Σ_j y_j(eq_j−rhs_j) + Σ_k z_k·slack_k with
  z_k ≥ 0, then on P_T (eq_j=rhs_j, slack_k≥0) we get L_T−1 = Σ z_k slack_k ≥ 0, hence L_T ≥ 1
  with NO vertex case-split. Correct Farkas certificate, not circular.
- Genuinely NEW lever, does NOT collapse to a dead family:
  - NOT the refuted ONE-REC facet-count — it repurposes the single-excursion FACT
    (superincreasing 2^j > Σ_{i<j}2^i prevents cross-group cascade) as a monotone-DIRECTION
    argument for the smoothing, not as a binding facet (R12 refutation was of the facet use only).
  - NOT the refuted canonical-ATT characterization — the outline explicitly requires the
    dual/smoothing to certify the non-canonical cross-group-pair tied family too (n=4 witness
    F={6,6,4}, sorted {6,6,4,4,3,3,2,2,1}, L_T=1; verified block structure = four even blocks +
    one odd singleton {1}, so ≤1 odd block there — consistent with GAP-ODDCOUNT).
- Corpus support is real: aimo-0146 (exchange-smoothing a linear functional over a sorted
  sequence under sum constraints, reduce to few extremal profiles) is a strong structural match;
  the single-vs-multi sum-constraint gap is exactly the open work, honestly flagged.

Load-bearing gap is honestly identified with mechanism: GAP-DUAL (the sparse Farkas identity
exists for every type, single order-inequality multiplier 2 + ±1 equality multipliers). Only 3
hand-built n=3 instances so far — this is the whole difficulty and it is NOT yet proven.

MANDATORY gate (binding precondition to prose — do NOT ship prose before it passes):
at n=5, across ALL types/words, machine-check (scipy HiGHS dual output
res.ineqlin.marginals / res.eqlin.marginals, then exact-rational re-verify) that
(i) the dual sparsity pattern holds (exactly one order-inequality with multiplier 2, plus
±1 equality multipliers), AND (ii) every box-free vertex has ≤ one odd-size block. Note the
R13 lower-vertex explorer only PARTIALLY covered n=5 box-free vertices (large-budget c_B≥2 types
skipped); the odd-block-count claim is UNVERIFIED at n=5 and must be checked, not assumed. If the
sparsity OR odd-block-count pattern breaks, REPORT the refutation — do NOT dress a fake smoothing
induction (the "−1 lost to a crude bound" failure mode). This is the same class of gate that
killed a bad recursion in each of R9–R13; it is the cheapest de-risk.

Cases both required: box-active vertices (TB / (n−1)-ladder branch of BLK) AND box-free vertices
(the dual/smoothing argument). Do not prove only the box-free branch.

## UPPER — breakpoint-vertex (revise): APPROVE with MANDATORY correction (gate-bound)

Technique: extremal-tie / smoothing minimax over the compact valley — Φ(A)=min_{∅≠T tree-realizable}
|Σ_{i∈T} ε_i a_i|, M* := max_{A∈valley} Φ(A), prove M* ≤ u_n L. This is the potential-free
extremal escalation called for since R12; it is a whole-valley maximization, NOT a forward
per-step bound, so it does NOT re-enter covering-radius / density / greedy / bounded-depth /
mass-telescope. Good.

DSUM correctly DROPPED: step 1 explicitly says do NOT cite or certify Lemma DSUM. Both explorers
confirm DSUM's per-step bound dist(a_i,R_{i−1}) ≤ a_1·2^{−(i−1)} is FALSE (exact rational
counterexample n=3), and even the aggregate has an unsound proof-sketch. Dispatch check satisfied —
DSUM must NOT be certified.

The tie/first-order argument (step 4) is a valid extremal principle (maximizer of a pointwise-min
forces multiple tied achievers or an active boundary). Sound in kind.

CONCRETE FLAW in the load-bearing step 5 (must be corrected before prose): the outline pins the
tied maximizer A* to the dyadic ladder a_i = 2^{n+1−i}/(2^{n+1}−1) with Φ = u_n L. But the dyadic
ladder is NOT in the valley — I checked arithmetically: a_1 = 2^n/(2^{n+1}−1) > L/2 for EVERY n
(0.571/0.533/0.516/0.508/0.504 at n=2..6), so the ladder lies in the a_1 ≥ L/2 region, which is
CLOSED separately by whole-tail-peel. The ladder is the tight point for the WHOLE upper bound
(across all A), not for the valley residual. Over the valley the bound holds with margin — the
recorded worst ratio is 0.75 (< 1), so M*_valley ≈ 0.75 u_n L is attained at an INTERIOR valley
point, NOT at the ladder and NOT at the a_1=L/2 boundary (where whole-tail-peel gives D=2a_1−L=0).
Hence step 5 as written ("balance conditions pin A* = dyadic ladder, Φ = u_n L") is doubly wrong:
wrong target (outside the domain) and wrong value (u_n vs ~0.75 u_n inside the valley).

Required correction (build with this, do not defer):
- Run the MANDATORY numeric gate FIRST, over the ACTUAL valley domain {a_1<L/2, a_2<β_nL} at
  n=3..6 over exact profiles: locate where Φ is maximized and confirm the tie (achieving-subset
  count ≥2) there. Expect an interior valley maximizer at ratio ≈0.75, NOT the ladder.
- The CLASSIFY step must then prove M*_valley ≤ u_n L by bounding Φ at ANY tied/boundary
  maximizer of the valley — do NOT force the ladder identification (the outline's own Watch-out
  says: "if a distinct tied maximizer exists off-ladder, CLASSIFY is false — report it, do not
  force the uniqueness"). If the classification cannot pin a clean extremal, report the stall;
  do NOT ship a proof asserting the ladder is the valley-maximizer.
GAP-TIE-FEASIBLE (exhibit the feasible ascent direction respecting Σa=L, ordering, both caps) is
correctly flagged as load-bearing.

This is the only live, non-dead-family upper lever available, so it is built this round — but its
step-5 closing mechanism is refuted-before-build and MUST be re-pointed as above.

## UPPER hedge — valley-differencing-construction: HOLD (do NOT build)

The outline itself flags the shared-gap risk and defers the decision to me. Verdict: HOLD.
1. Single-gap trap. Its step 2–3 ("guess T* optimal AT the dyadic ladder; perturb off-ladder can
   only DECREASE leftover") hinges on the SAME dyadic-ladder-as-tight-point premise as
   breakpoint-vertex's GAP-CLASSIFY — and inherits the SAME flaw: the ladder is outside the valley,
   so a T*-tree "optimal at the ladder" is optimized at a point not in the domain, and the
   robustness bound is anchored to the wrong profile. GAP-CONSTRUCT ≈ GAP-CLASSIFY; two upper
   vehicles sharing one wall = shared-gap collapse.
2. Its robustness step is a MONOTONICITY claim ("pushing toward dyadic only decreases leftover") —
   exactly the class refuted in R3 (minimax V is NOT monotone along balanced→dyadic paths;
   interior valleys) and which my standing rule says never to approve without a real telescoping
   induction on survivor count. Not repaired here.
Keep one vehicle per wall. valley-differencing-construction stays registered/live as a reserve; if
breakpoint-vertex's extremal lever stalls, revisit it next round only with a genuinely independent
telescoping proof that does NOT route through the maximizer characterization.

## Diversity note (for the orchestrator)

Both walls sit on cleaner certified residuals (GAP-EXTR / first-gap pigeonhole) but the two upper
vehicles collapse onto the same dyadic-ladder-tightness premise, and that premise is
domain-mismatched to the valley. The LOWER lever (LP-dual/smoothing) is the better-de-risked plan
this round (corpus-anchored, valid weak-duality logic, n=3 verified) — reflected in the ranking:
merge-interleave-pattern won its head-to-head against breakpoint-vertex this round. If BOTH gates
fail (n=5 dual-sparsity for LOWER; valley-maximizer≠ladder for UPPER), the UPPER wall in particular
needs a genuinely different framing that does NOT assume the ladder is the valley extremal — flag
to next round's outliner.

## Ranking (updated this round)

breakpoint-vertex 1757 (leader, but step-5 refuted-before-build), parity-measure-potential 1650
(family DEAD, do not rebuild), merge-interleave-pattern 1619 (rose — soundest plan this round),
valley-differencing 1507, smoothing-majorization 1506, induction-peel 1497, f-partition 1482,
ballot-matching 1425 (dead), explicit-pairing 1309 (dead). No new slug registered (both build
approaches already in the population); no copy (no branch requested).

build set: merge-interleave-pattern, breakpoint-vertex
