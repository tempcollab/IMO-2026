## imo-2026-03

Answer (CONFIRMED, both walls): c(n)=2^n/(2^{n+1}−1), minimax D=u_n=1/(2^{n+1}−1).
Two walls remain open (both `partial`). Field this round: ONE vehicle per wall, kept FAR
APART by mechanism (LOWER = exchange-smoothing/LP-dual certificate on the CERTIFIED vertex
polytope; UPPER = extremal-tie minimax over the whole valley), plus ONE constructive
far-apart hedge on the upper wall (flagged for the reviewer to gate against the shared-gap
risk). f-partition-majorization stays HELD (mechanism not repaired; do NOT build).

Do NOT re-open (Rules, run_state.md): covering-radius (one/two-cap), density/COUNT,
greedy recursion, bounded-depth escape, mass-telescope discrepancy, scalar-reserve,
structured transport/matching, prefix/termwise monovariant, canonical-ATT-layout
characterization, f-partition single-gap localisation. All provably dead.

---

merge-interleave-pattern: revise  (LOWER wall — GAP-EXTR)
Target: For every n, every admissible refinement S of the ladder C_n with ≤ n cuts has
  D(S) ≥ 1 (⟺ minimax D = u_n, the lower half of c(n)=2^n/(2^{n+1}−1)). Whole-claim lower bound.
Technique: LP-duality / same-group exchange-smoothing (Farkas certificate) on the CERTIFIED
  interleave-word polytope P_T, replacing the refuted ONE-REC facet-count and the refuted
  canonical-ATT-layout characterization. Corpus spine: aimo-0146 (exchange-smoothing a linear
  functional over a sorted sequence under sum constraints, reduce to few extremal profiles,
  verify directly) — adapt to the MULTI-constraint (superincreasing dyadic) version.
Skeleton:
  1. Import certified VERT-LOW+BLK+ATT: MID-core ⟺ GAP-EXTR = "min_{vertex of P_T} L_T ≥ 1
     for every type T", where L_T(v)=Σ_odd v − Σ_even v is linear on P_T and P_T is cut out by
     (E) n+1 dyadic group-sum equalities, (O) the word's descending order chain, (C) the box
     0≤v_i≤2^{n-1}. — already certified, no re-proof.
  2. Promote the block-parity reduction to a stated lemma (Lemma ODD, near-proven, rests only
     on certified Lemma P): at any vertex the coordinates split into maximal equal-value blocks;
     every EVEN-size block is a set of Lemma-P cancelling pairs contributing 0 to L_T, so
     L_T = the alternating sum over the ODD-size blocks only. — by Lemma P (cancelling-pair).
  3. Same-group exchange move: within one dyadic group (one (E)-constraint, sum fixed), transfer
     one unit of value from a coordinate at an EVEN word-position to one at an ODD word-position.
     This changes L_T by exactly +2 per unit and keeps (E) satisfied; run it in REVERSE (odd→even)
     to DECREASE L_T until an (O) order-inequality or a (C) box face becomes binding. The
     terminal profile of this monotone smoothing is a vertex. — by linearity of L_T + the
     superincreasing property 2^j > Σ_{i<j}2^i (a lower group can never out-compete a higher one
     for value, so smoothing within a group does not cascade across groups — the single-excursion
     FACT underlying ONE-REC, reused as a MONOTONE-DIRECTION argument, NOT as a facet).
  4. LP-dual certificate (the closure): exhibit, for every type T, multipliers y_j ∈ {±1} on the
     (E)-equalities (sign = the word's net parity contribution of group j) and a SINGLE nonzero
     multiplier z=2 on ONE binding cross order-inequality ("B-piece ≥ F-fragment" or the reverse),
     such that the linear identity
        L_T(v) − 1 ≡ Σ_j y_j·(eq_j(v) − rhs_j) + z·(slack of that one order-ineq)
     holds for ALL v. Then L_T ≥ 1 on the whole P_T (weak LP duality), no vertex case-split.
  5. Terminal check: the smoothing of step 3 terminates at a FINITE set of block-structured
     profiles (even blocks cancel; the odd-block residual is pinned by the group sums to the
     dyadic residual = 1); verify L_T = 1 there directly, matching certified Lemma ATT. — direct
     computation on the finite terminal family, INCLUDING the non-canonical cross-group-pair
     family (see Watch out).
Key lemmas (claim + mechanism):
  - Lemma ODD (L_T = alternating sum over odd-size blocks) — because even blocks are Lemma-P
    cancelling pairs contributing 0; all content lives in the odd-multiplicity distinct values.
  - Smoothing monotonicity (each odd→even same-group transfer lowers L_T by 2/unit, feasibly) —
    because L_T is linear with ±1 coefficients by word-position and (E) is preserved; superincreasing
    group sums prevent cross-group cascade, so the move stays inside P_T until an (O)/(C) face binds.
  - Sparse dual (y_j=±1, single z=2) certifies L_T ≥ 1 for every type — because the observed
    Farkas multipliers are uniformly ±1/2-sparse (3 hand-built n=3 types + n=4 tight family), a
    small-integer certificate with NO κ-blowup (contrast the dead scalar-reserve family whose κ
    was unbounded in n).
Open gaps:
  - GAP-DUAL (load-bearing): prove the sparse Farkas identity of step 4 exists for EVERY type T,
    with the single binding order-inequality identified in CLOSED FORM from the word/block structure
    (which cross comparison, as a function of T). Equivalently, prove the step-3 smoothing terminates
    with L_T never dropping below 1. This is the whole difficulty; everything else is certified.
  - GAP-ODDCOUNT (sub-gap, cheap-killable first): bound the number of odd-size blocks a box-free
    vertex can have and pin the residual odd block(s) ≥ 1. Explorer's proposed collapse: if a
    box-free vertex has exactly ONE odd block (pinned to the smallest dyadic level = value 1),
    GAP-EXTR reduces to a single scalar bound. CHECK this odd-block count first (see cheap-kill).
Cases to cover: box-active vertices (a (C) face binds — handled by the TB split / (n−1)-ladder
  recurse branch of BLK, untouched by the n=4 refutation) AND box-free vertices (the smoothing/dual
  argument above). Both must be settled; do not prove only the box-free branch.
Watch out:
  - Do NOT assume the minimizing vertex is a canonical ATT one-fragment-per-scale layout — REFUTED
    at n=4 (explicit box-free vertex F={6,6,4}, B=C_3 with level-3 split {3,3,2}, sorted
    {6,6,4,4,3,3,2,2,1}, L_T = 1 via cross-group cancelling pairs, NOT ATT shape). The dual/smoothing
    argument MUST certify these non-canonical tied vertices too — a valid dual has to cover BOTH the
    ATT family and the cross-group-pair family at L=1 simultaneously (stronger, more informative test).
  - "No straddling" (a single fragment spanning two groups' ranges — TRUE, superincreasing) is much
    WEAKER than "no cross-group value coincidence" (FALSE per the n=4 witness). Do not conflate them.
  - MANDATORY cheap-kill BEFORE prose (fast, scipy HiGHS dual output res.ineqlin.marginals /
    res.eqlin.marginals, exact-rational re-check): at n=5 across ALL types/words, verify the dual
    sparsity pattern (exactly one order-inequality with multiplier 2, plus ±1 equality multipliers)
    holds and that every box-free vertex has ≤ one odd block. If the sparsity or odd-block-count
    pattern breaks at n=5, report the refutation — do NOT dress a fake smoothing induction (the
    outline-reviewer has repeatedly flagged the "−1 lost by a crude bound" failure mode).

---

breakpoint-vertex: revise  (UPPER wall — Prop UV / first-gap pigeonhole)
Target: For every n and every profile A (sum L, ≤ n+1 pieces), Xiang forces D ≤ u_n L (the upper
  half of c(n)). Reduced (certified R-UV/FGR/R-COV' sufficiency) to Prop UV:
  min_{∅≠T tree-realizable} descKK(T) ≤ u_n L for every full-budget balanced-valley profile.
Technique: extremal-tie / smoothing MINIMAX over the whole valley (potential-free LP-flavored
  extremal principle), attacking the entire valley at once — NOT a forward DP, NOT any of the five
  dead upper families. This is the escalation the run has called for since R12.
Skeleton:
  1. DROP Lemma DSUM. Its filed per-step bound dist(a_i,R_{i-1}) ≤ a_1·2^{-(i-1)} is FALSE (exact
     rational counterexample at n=3, i=3,4). The aggregate Σ dist ≤ a_1(2−2^{-n}) is only numerically
     supported and points the WRONG direction for any mass argument anyway. Do NOT let a builder cite
     or certify DSUM. The extremal-tie route below does not use it.
  2. Genericity reduction (disposes collisions cheaply): descKK values are continuous in A and the
     min over the finite nonempty (T,ε) family is continuous, so Prop UV is a closed condition; it
     suffices to prove it on the dense set of profiles with no exact reachable-value coincidence, then
     take limits. Collisions (some a_i equal, or a_i landing on a prior reachable value) give dist=0
     ≤ u_n in ONE step — strictly easier, NOT a separate hard regime. — by continuity/upper-semicont.
  3. Extremal reframe: set Φ(A) = min_{∅≠T tree-realizable} |Σ_{i∈T} ε_i a_i| and study
     M* := max_{A ∈ valley} Φ(A) over the compact valley polytope {a_1≥…≥a_{n+1}≥0, Σa_i=L,
     a_1<L/2, a_2<β_nL}. Prop UV ⟺ M* ≤ u_n L. — Φ is continuous, valley is compact, so M* is attained.
  4. Tie condition at a maximizer A*: if at A* the minimizing (T,ε) were UNIQUE, its value is a
     smooth linear function Σ ε_i a_i near A* with nonzero gradient ε; then there is a feasible
     direction (respecting Σa=L and the valley face) increasing that one signed sum, strictly raising
     Φ — contradicting maximality — UNLESS enough boundary constraints bind. Hence at A* either (a) a
     valley/order boundary constraint is active, or (b) ≥2 distinct tree-realizable signed sums are
     TIED at the min. — standard interior-extremum / first-order argument (extremal principle).
  5. Classify the tied extremal A*: the balance conditions (several signed sums equal in absolute
     value) + active boundaries pin A* to the dyadic ladder a_i = 2^{n+1-i}/(2^{n+1}−1) (conjectured
     UNIQUE tied point, consistent with the observed "tight only at dyadic, worst ratio 0.75 off it"
     signature). At the ladder, the descending cascade 2^n−2^{n-1}−…−1 telescopes to exactly 1, i.e.
     Φ = u_n L. Therefore M* = u_n L. — direct computation at the ladder + the tie-classification.
Key lemmas (claim + mechanism):
  - Tie-or-boundary at the maximizer — because a unique minimizing signed sum has nonzero gradient,
    so an interior maximizer with a unique achiever admits a feasible Φ-increasing perturbation
    (contradiction); maximality forces multiple tied achievers or an active valley face.
  - Dyadic ladder is the unique tied point with Φ = u_n L — because the ladder is the fixed point of
    the descending-difference cascade (each step halves the remainder to the next dyadic level),
    making many signed sums simultaneously equal to 1; off-ladder, the tie breaks and Φ drops (0.75).
Open gaps:
  - GAP-CLASSIFY (load-bearing): prove the tie + active-boundary conditions force A* = dyadic ladder
    (or a finite set all with Φ ≤ u_n L). This is the whole difficulty — the combinatorial
    identification of which signed sums tie and that they pin the ladder.
  - GAP-TIE-FEASIBLE: make step 4 rigorous — exhibit the feasible ascent direction explicitly given
    a unique achiever (must respect Σa=L, the ordering a_i≥a_{i+1}, and the two valley caps), i.e.
    show the active-constraint set at a genuine maximizer cannot pin A* while leaving a unique achiever.
Cases to cover: a_1 ≥ L/2 (CLOSED, whole-tail-peel, imported); m ≤ n (CLOSED, U0/DELETE, imported);
  the full-budget balanced valley (the extremal argument above). Enumerate no further sub-cases —
  the extremal reframe handles the whole valley at once.
Watch out:
  - MANDATORY numeric gate BEFORE prose: at n=3..6 over exact valley profiles, verify (i) Φ(A) is
    maximized ONLY at the dyadic ladder (no off-ladder tied maximizer), and (ii) at any near-maximizer
    the achieving-subset count is ≥2 (the tie). If a distinct tied maximizer exists off-ladder, the
    CLASSIFY step is false — report it, do not force the uniqueness.
  - Do NOT resurrect any forward reachable-set DP, covering radius, density count, greedy recursion,
    bounded-depth escape, or mass-telescope — all five dead. The extremal argument must stay a
    whole-valley maximization, never a per-step forward bound.
  - Tree-realizability (Lemma RL): only tree-realizable sign patterns count in Φ; the perturbation
    argument must respect that the achieving (T,ε) stays tree-realizable under small perturbation
    (it does — realizability is combinatorial, locally constant in A).

---

valley-differencing-construction: revise  (UPPER wall — far-apart CONSTRUCTIVE hedge)
Target: Same whole upper bound D ≤ u_n L, proved CONSTRUCTIVELY: exhibit an explicit ≤ n-cut Xiang
  response (a specific subset T and differencing-tree order) with leftover ρ ≤ u_n L.
Technique: dyadic-guided, NON-GREEDY explicit construction + robustness/stability off the dyadic
  ladder. Far from breakpoint-vertex by MECHANISM (build the witness vs prove its existence by
  contradiction). NOTE the shared-gap risk below — the reviewer should gate whether this is truly
  far enough to build alongside breakpoint-vertex, or held as a reserve.
Skeleton:
  1. Import certified R-UV/RL: suffices to build one nonnegative differencing tree on a nonempty
     subset T with value ≤ u_n L, budget |T|−1 MATCHes + (n+1−|T|) DELETEs ≤ n.
  2. Guess the subset T* and tree order that are optimal AT the dyadic ladder (there the descending
     cascade telescopes to exactly u_n L). This is a CLOSED-FORM recipe read off the sorted a_i, NOT
     a greedy running rule (plain greedy KK differencing REFUTED R9, overshoot ≤ 11.4×).
  3. Robustness: show that perturbing A off the ladder (within the valley) can only DECREASE the
     leftover of this fixed T*-tree relative to the tight dyadic value u_n L — a monotone/telescoping
     stability bound. — by explicit telescoping of the fixed cascade under the valley constraints.
Key lemmas (claim + mechanism):
  - Fixed dyadic-guided tree has leftover ≤ u_n L on the whole valley — because the cascade is tight
    (=u_n L) at the ladder and the valley caps a_1<L/2, a_2<β_nL bound each telescoped remainder below
    its dyadic value; the construction is fixed, so no greedy overshoot arises.
Open gaps:
  - GAP-CONSTRUCT (load-bearing): specify T* and the tree order in closed form from the sorted a_i,
    and prove the robustness/telescoping bound ρ(A) ≤ u_n L for every valley A. The R8/R9 greedy
    versions and the R10 near-uniform simultaneous-pairing narrowing are recorded dead — this must be
    a genuinely non-greedy, foresight-based recipe.
Cases to cover: full-budget balanced valley (a_1≥L/2 and m≤n imported closed).
Watch out:
  - SHARED-GAP RISK (flag to reviewer): the upper explorer notes this robustness argument is
    "essentially the extremal-tie opening in constructive form" — GAP-CONSTRUCT may coincide with
    breakpoint-vertex's GAP-CLASSIFY (both hinge on the dyadic ladder being the extremal/tight point).
    If the reviewer judges they share the wall, HOLD this and build only breakpoint-vertex (one vehicle
    per wall, single-gap trap). Build it only if the closed-form T* recipe gives a genuinely
    independent telescoping proof that does NOT route through the maximizer characterization.
  - Do NOT re-propose plain greedy KK differencing (R9 dead) or the near-uniform simultaneous-pairing
    (R10 narrowing, dead). Must be an explicit dyadic-guided subset with a proven stability bound.

---

HELD (not built this round): f-partition-majorization (GAP B-MONO localisation refuted R12, mechanism
  not repaired); parity-measure-potential (scalar-reserve family dead — do NOT rebuild); two-box-balancing.

Recommended build set (reviewer confirms): merge-interleave-pattern (LOWER), breakpoint-vertex (UPPER),
and valley-differencing-construction ONLY if the reviewer judges GAP-CONSTRUCT genuinely distinct from
GAP-CLASSIFY; otherwise hold it and keep the tight one-vehicle-per-wall field.
