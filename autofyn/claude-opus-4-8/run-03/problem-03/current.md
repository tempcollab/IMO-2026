## Status
partial

**R19 (reviewer-verified):** UPPER breakpoint-vertex — CHANGES REQUESTED, still live leader, CONSOLIDATION
round (no gap closed, none claimed). Officially RE-TARGETS the open deep-interior residual from the
caterpillar object μ_{n+1} to the certified true target `min 𝓡(A) ≤ u_nL` via certified Corollary R-UV
of Lemma RL (sufficiency: min 𝓡(A) ≤ u_nL ⟹ Xiang forces D ≤ u_nL; re-checked against the lemma file —
correctly the sufficient direction, converse R-COV' explicitly flagged uncertified/unused, no overclaim).
Re-target is SOUND: `min 𝓡(A) ≤ μ_{n+1}` always (caterpillars are one tree topology ⊆ all differencing
trees) — reviewer-verified numerically. The "completeness" identity μ_{n+1} = min 𝓡(A) is FALSE
(reviewer reproduced exact-Fraction: A=(17,16,11,8,4) μ=1/minR=0; (59,55,53,44,17) μ=2/minR=0;
(54,43,35,32,28) μ=3/minR=2), so any lever assuming that equality is unsound on arrival — hence the
re-target abandons μ_{n+1} for the weaker/equally-sufficient min 𝓡(A). Two R19 mechanisms recorded dead:
(ii) tree-min-divide-conquer (balanced FULL partition can't drop pieces → can't reach the anchor-EXCLUDING
tail minimiser; 9.30·u₄ on R18 witness, growing) and (iii) signed-tree-invariant band-restart (≡ descKK,
anchored at a₁; 9th dead anchored-walk relabeled). Deep interior `a₁<(L−u_nL)/2` OPEN; residual is now
`min 𝓡(A) ≤ u_nL`, a NON-anchored global (Steinitz/vector-balancing) existence claim over the
tree-realizable signed sums. Certified core (RL/R-UV, WTC boundary closure, R-COV', FGR, ESF-2) INTACT.
No lemma certified this round (nothing new proposed; R-UV already certified round 7). No APPROVE.

**R17 (reviewer-verified):** LOWER wall scale-origin-layercake — RETHINK, 10th dead lower lever
(scale-of-origin per-scale cap `Σ_i α_{i,j} ≤ Σ_i β_{i,j}` reproduced FALSE by the reviewer: loss-free
tagging but the local aggregate fails 13–48% with deficits growing 3/6/10 across n=4,5,6; (★) holds
0/all). UPPER breakpoint-vertex — CHANGES REQUESTED, still live leader: the R17 deep-interior
extremal/smoothing lever is refuted (G1 reviewer-verified: the deep interior AS DEFINED `a₁<L/2−u_n/2`
contains a `u_n/2`-wide near-boundary sliver where `Φ/u_n→1` — 0.881/0.938/0.968/0.984 at n=3..6 just
below the boundary — so NO uniform margin there, the outliner's 0.34–0.56 margin holds only in the
strictly-deeper `a₁≤L/2−u_n`; G2 smoothing move non-monotone; full-tree 2nd-moment 8th dead upper
mechanism). WTC boundary closure INTACT. Residual sharply localized to the near-boundary sliver +
single-target subset-sum density `Φ ≤ min_{S⊆tail}|a₁−Σ_S|` (a valid corollary of certified WTC, 0
fails / 832 profiles, but strictly loose 66% of the time — NOT certified as a new lemma; trivial
one-line consequence of WTC, no new proof content). No APPROVE this round.

## Approaches tried
- breakpoint-vertex (UPPER) — R15 CHANGES REQUESTED (partial, genuine advance; reviewer-verified).
  NEW certified game-independent Lemma WTC (`whole-tail-continuation`): for descending a₁≥…≥a_m>0
  summing to L, the largest-first differencing value K=descKK ≤ |2a₁−L| (two-sided invariant
  a₁−P_k ≤ v_k ≤ |a₁−P_k| by induction; reviewer re-derived from scratch, 0 fails/200k exact
  profiles, EQUALITY on A^{(n)}). CONSEQUENCE: since Φ(A)=min_{∅≠T}descKK(T) ≤ descKK(full) ≤
  |2a₁−L|, the boundary layer (L−u_nL)/2 ≤ a₁ < L/2 is closed EXACTLY (|2a₁−L|=L−2a₁ ≤ u_nL there,
  R-COV' sufficiency ⇒ D ≤ u_nL) — the exact continuation of certified whole-tail-peel across
  a₁=L/2, tight on A^{(n)}, respecting VALLEY-TIGHT (no margin). REAL PROGRESS: the open valley
  shrinks from a₁<L/2 to the DEEP interior a₁<(L−u_nL)/2 (where |2a₁−L|>u_nL, WTC vacuous). Deep
  interior honestly surfaced as OPEN — needs unbounded multi-piece cancellation (Φ≤u_n via a
  4-element cancellation on {30,25,20,15,10}/100; bounded moves provably insufficient). Same
  first-gap/Subset-KK pigeonhole open since R7, now strictly confined to the deep interior.
- gen-func-transform (LOWER, Z-transform of the parity-measure at z=−1) — R15 RETHINK
  (unsolved; decisive negative, reviewer-verified). Z(z)=∫₀ᴸ z^g, Z(−1)=L−2μ{g odd} makes MID-core
  the single evaluation Z(−1)≤L−2 — but this identity is certified-MID repackaged, closes nothing.
  The two-band recursion (the slug's only non-repackaging content) is REFUTED: the bottom band
  carries weight (−1)^{N_F(t)}, and the deviation from a clean recursion in Z_{n−1}(−1) is EXACTLY
  −2∫_{O_F∩(0,L/2)}(−1)^{g'} = the certified dead SPLIT cross-term μ(O_F∩O_B) that Lemma MID was
  built to eliminate. DECISIVE COLLISION (reviewer reproduced exactly): n=4, F={8,5,3}, F_B={4,4},
  three admissible B_B all with Z_{n−1}(−1)=0 give Z_4(−1) ∈ {−4,−2,0}. So Z_n(−1) is NOT a
  function of (F,F_B,Z_{n−1}(−1)); no scalar-IH recursion exists. The transform re-imports the very
  overlap term MID removed — a reframing, not a reduction. 7th dead lower lever (the transform
  object). Do NOT re-seed any Z-transform / generating-function / roots-of-unity recursion on the
  static parity-measure.
- merge-interleave-pattern (LOWER, LP-vertex/word-polytope framing) — R14 RETHINK. The LP-dual/
  sparse-Farkas revision's own closing mechanism is REFUTED (reviewer-verified). GAP-EXTR (min L_T≥1
  at every vertex) is CONFIRMED at n=5 (min L_T=1, no sub-1 vertex), but certificate-existence is
  loss-free equivalent to GAP-EXTR (strong LP duality) — a reframing, not a reduction. Two handles
  dead: R14a (no ±1-equality certificate — box-interior n=4 witness {6,6,4,4,3,3,2,2,1}: unique ±1
  solution y_F=+1,y_tail=−1 forces Σy_g|g|=|F|−|B|=−3≠1=[m odd]) and R14b (box-free L_T=1 vertices
  can have ≥2 odd blocks — {6,6,4,4,4,4,2,1}, block sizes [2,4,1,1]). Certified reduction
  VERT-LOW+BLK+ATT stands; certified DUAL-CHAR + refutations. This is the SECOND dead lever inside
  the vertex-polytope framing (ONE-REC-tightness R12, LP-dual R14) — the framing is diagnosed a
  loss-free reframing, so back to the outliner for a genuinely NEW lower mechanism (NOT a restatement
  of "min L_T over the vertex polytope"; candidates flagged: dyadic-scale induction on D=μ{g odd}
  tracking odd-block mass via ONE-REC as a STRUCTURAL fact, or aimo-0493 dyadic-tagging).
- breakpoint-vertex (UPPER, LP-vertex → first-gap/Subset-KK pigeonhole) — R14 CHANGES REQUESTED.
  The extremal-tie / smoothing-minimax closing lever is REFUTED: the valley residual is
  ASYMPTOTICALLY TIGHT (NO margin). Reviewer-verified certified Lemma VALLEY-TIGHT: explicit valley
  family A^{(n)}={2^n,…,4,3,2}/(2^{n+1}+1) has true forced minimum Φ=1/(2^{n+1}+1) (full
  tree-realizable reachable set: 0 NOT reachable, min positive =1 exact at n=3,4,5), so
  Φ/u_n=(2^{n+1}−1)/(2^{n+1}+1)→1 (0.882,0.939,0.969,0.985,0.992,0.996 at n=3..8). The prior
  "worst 0.75 margin" was an under-sampling artifact. Consequence: ANY crude/margin-based valley
  bound is provably dead (also kills valley-differencing-construction's robustness premise). The
  certified reduction R-UV + FGR + R-COV'(sufficiency) STANDS and the residual (first-gap pigeonhole
  min_{∅≠T}descKK(T)≤u_n) is TRUE, tight, OPEN. Needs a genuinely TIGHT (not margin) lever.
- parity-measure-potential (framing B, global measure/parity, no induction) — PARTIAL.
  R4: NEW whole-tail-peel Branch (2) closes the ENTIRE upper-bound range a₁ ≥ L/2
  profile-independently (D = 2a₁−L ≤ u_kL for L/2 ≤ a₁ ≤ c(k)L; certified). REFUTED the
  mass-threshold subset-cover lever for a₁ < L/2 (rigorous counterexample (0.44,0.281,0.279),
  reviewer-verified: bisection D=1/500 ≤ 1/7, every threshold move unavailable). Lower bound:
  Case A + a=0 equal-bisection done; a=1 reduced by exact identity D(S)=f₁−D(S_L) to
  D(S_L)≤f₁−1 (GAP L1). Open: GAP U (a₁<L/2, needs D-tracking not mass), GAP L1, GAP L2 (a=0
  shredded top).
- induction-peel (framing A, strong induction on n / cancelling-pair peel) — PARTIAL.
  R4: corrected the FALSE round-3 "WLOG single top cut" premise (reviewer-confirmed: minimiser
  puts all n cuts on the top). Proved+certified Lemma PEEL (D=f₁−D(S∖f₁) for a unique max),
  Lemma SPLIT (disjoint-union cross term), Lemma ONE (≤1 piece >2^{n-1}). Reformulated lower
  bound as a refinement optimisation (no adaptivity); Case (a) done; exactly reduced Case (I)
  to (L⋆) D(S')≤f₁−1 via PEEL. Upper bound: entire dominant case a₁≥L/2 (§4A, incl. tight
  dyadic input). Open: GAP L = {(L⋆)=GAP L1, Case II}, GAP U (balanced a₁<L/2, needs
  non-multiplicative early-stopping potential).
- explicit-pairing-strategy — greedy-merge refuted; needs a corrected Xiang strategy (dormant).
- ballot-matching (framing J, lower wall — GAP MID-core via structured debit→credit transport/Hall
  certificate) — RETHINK (R11, reviewer-verified). The distinct MECHANISM collapses: on adversarial
  a=0 scans (n=3–6) every structured, inspectable adjacency fails — prefix (8.5%), suffix (30.4%),
  dyadic-scale interval-Hall / HALL-ENDPOINT (49%), value-dominating injection (49.6%) — and the
  GAP-TERMINAL premise `S_m=|F|−|B|<0` is FALSE (tight minimiser has |F|=|B|+1 ⇒ S_m=+1; reviewer
  confirmed a tight case {2,2,2,1}, D=1, |F|=|B|=2, S_m=0 — no forced terminal descent). Only the
  complete-bipartite transport is feasible, which is logically identical to the target `cw≥0`. The
  target (`Σ_{F even}v ≤ Σ_{B odd}v`, `cw≥0`) is reconfirmed TRUE (min cw≈5e-4, tight) but is
  irreducibly aggregate — no scalar reserve (R10), no structured matching (R11) closes it. The
  matching vehicle is dead; goes back to the outliner for a genuinely new global lower mechanism.

## Current best
The answer is **c(n) = 2^n/(2^{n+1}−1)**, minimax D = u_n = 1/(2^{n+1}−1); verified exact by
reviewer brute force (n = 0,1,2) and by the recursion/closed form for all n.

Rigorously established (all reviewer-verified; certified shared lemmas in `lemmas/`):
- **Lemma R (reduction):** claiming game gives Liu the odd-rank sum; Liu = (1+D)/2,
  D = Σ(−1)^{i+1}b_i ≥ 0 → scalar minimax of D.
- **Lemma M/I (measure identity):** D = μ{t : N(t) odd}; even multiplicity ⇒ D=0; toggle calculus.
- **Lemma P (cancelling pair):** D(S∪{v,v}) = D(S); the one-cut peel.
- **Lemma PEEL (R4):** unique max f₁ ⇒ D(S) = f₁ − D(S∖{f₁}). (verified exact)
- **Lemma SPLIT (R4):** D(X⊔Y) = D(X)+D(Y) − 2μ(O_X∩O_Y). (verified exact)
- **Lemma ONE (R4):** in a refinement of C_n, at most one final piece > 2^{n-1}.
- **Whole-tail-peel (R4, certified):** L/2 ≤ a₁ ≤ c(k)L ⇒ Xiang forces D = 2a₁−L ≤ u_kL exactly.
- **Upper bound, entire range a₁ ≥ L/2:** closed (bisect branch conditional on UB IH +
  unconditional whole-tail branch). Contains the tight dyadic input ⇒ answer tight.
- **Lower bound, top-piece-uncut (Case A/a):** D ≥ 2^{n-1} ≥ 1.
- **Base cases n = 0, 1** both directions; recursion u_n = u_{n-1}/(2+u_{n-1}).

**Two remaining walls (now shared across BOTH live approaches):**
- **Lower wall (L⋆ / GAP L1):** prove D(S')≤f₁−1 where S' = final multiset minus the unique
  piece f₁∈(2^{n-1},2^n), all pieces ≤2^{n-1}. Both approaches reduce Case I to this *same*
  inequality. Crude D(S')≤max≤2^{n-1} is short by "−1"; the SPLIT cross term must be carried.
  Plus (induction-peel Case II / parity GAP L2): D ≥ 1 when every piece ≤ 2^{n-1} (top shredded).
- **Upper wall (GAP U, a₁ < L/2):** mass-threshold/subset-cover is REFUTED here (verified
  counterexample); needs a genuine D-tracking argument (top-cut residual's exact D via
  PEEL/SPLIT, or smoothing/majorization).

Certified shared lemmas: `lemmas/{reduction-odd-rank, measure-identity, cancelling-pair,
strict-max-peel, split-cross-term, top-scale-dichotomy, whole-tail-peel,
top-band-decomposition, elementary-reductions, even-multiplicity-corrector,
mass-difference-reduction, leftover-realizability, valley-sharpness, band-landing,
recursed-dyadic-dichotomy, order-statistic-reformulation, one-sided-walk-cap,
subtraction-from-top-subfamily, subset-caterpillar-subfamily, clipped-tau-family,
confinement-reachable-set, multiset-doubling, vertex-reduction-lower, vertex-block-structure,
midcore-attainment, first-gap-recursion, covering-value-reduction}.md` (27 total; last 5 =
VERT-LOW, BLK, ATT, FGR, R-COV' certified round 12).

**R15 progress (still partial; no APPROVE). One lemma CERTIFIED (WTC → 30 total). UPPER boundary layer closed EXACTLY; LOWER transform lever dead (7th dead family).**
- **breakpoint-vertex (UPPER) — CHANGES REQUESTED, partial, GENUINE ADVANCE.** Certified Lemma WTC
  (`whole-tail-continuation`, reviewer re-derived + 0 fails/200k): descKK ≤ |2a₁−L| for any
  descending profile. Closes the boundary layer (L−u_nL)/2 ≤ a₁ < L/2 EXACTLY via Φ ≤ descKK(full)
  ≤ |2a₁−L| ≤ u_nL + R-COV' sufficiency — exact continuation of whole-tail-peel, tight on A^{(n)},
  respects VALLEY-TIGHT (no margin). Open valley shrinks to the DEEP interior a₁<(L−u_nL)/2 (WTC
  vacuous there, |2a₁−L|>u_nL). Deep interior honestly OPEN — needs unbounded cancellation; the
  first-gap/Subset-KK pigeonhole restricted to the deep interior is the residual. Elo leader, live.
- **gen-func-transform (LOWER) — RETHINK, unsolved.** Z-transform Z(−1)=L−2μ{g odd} is certified-MID
  repackaged; the two-band recursion is REFUTED — deviation from clean recursion = the dead SPLIT
  cross-term μ(O_F∩O_B); reviewer-reproduced collision (F={8,5,3},F_B={4,4},Z_{n−1}=0 → Z_4∈{−4,−2,0})
  proves no scalar-IH recursion exists. 7th dead lower lever; the transform re-imports the overlap
  MID removed. LOWER wall still has NO live vehicle → back to the outliner for a genuinely new object.

**R14 progress (still partial; no APPROVE). Two lemma-records CERTIFIED (VALLEY-TIGHT, DUAL-CHAR+R14a/b → 29 total). BOTH walls' latest closing levers REFUTED; NEITHER wall closed.**
- **merge-interleave-pattern (LOWER) — RETHINK.** LP-dual/sparse-Farkas mechanism refuted (R14a/R14b,
  reviewer-verified exact). GAP-EXTR de-risked to n=5 but is a loss-free reframing of MID-core; the
  vertex-polytope framing has now had TWO levers die. Back to the outliner for a NEW lower mechanism.
  Certified: DUAL-CHAR (box-free chain-certificate characterization + the two forced dead-mechanism
  refutations). VERT-LOW+BLK+ATT reduction still stands.
- **breakpoint-vertex (UPPER) — CHANGES REQUESTED.** Extremal-tie/margin closing lever refuted by
  VALLEY-TIGHT (reviewer-verified: full reachable set, 0 not reachable, Φ=1/(2^{n+1}+1), ratio→1).
  Valley residual is asymptotically tight — no margin exists, so all crude/margin bounds dead. The
  reduction (R-UV/FGR/R-COV') stands; residual = first-gap pigeonhole min_{∅≠T}descKK(T)≤u_n (TRUE,
  tight, OPEN). Needs a genuinely TIGHT lever (exact induction carrying the {…,4,3,2} near-extremal
  family, or transported LP-dual/discrepancy machinery). Elo leader; stays live.

**R12 progress (still partial; no APPROVE). Five lemmas CERTIFIED; both walls' current mechanisms exhausted.**
- **merge-interleave-pattern (LOWER) — CHANGES REQUESTED, partial.** Mandated cheap-kill PASSED
  (exact LP over all types×words: global min D = 1 for n=3,4, NO sub-1 vertex; reviewer reproduced on
  independent finer grids) — the LP-vertex framing is NOT refuted. CERTIFIED Lemma VERT-LOW (MID-core
  ⟺ every vertex of every P_T has alternating value L_T ≥ 1; loss-free), Lemma BLK (≤ n+3 distinct
  values at a vertex), Lemma ATT (explicit family B=C_{n-1}, F={2^{n-1},…,2,1,1} gives D=1 all n≥2 →
  lower bound tight). GAP-EXTR restated correctly ("min L_w ≥ 1 at every vertex", NOT "canonical value
  1"). REMAINING GAP: GAP-EXTR for general n is loss-free equivalent to MID-core — the vertex reduction
  reframes/sharpens (finite block-structured target) but does NOT close it. Two shortcuts refuted
  (integrality: non-integer vertices exist; constant-value: D varies across words). The builder itself
  flags the outline's GAP-EXTR *mechanism* ("ONE-REC tightness forces the spread") is UNSUPPORTED —
  ONE-REC is not a binding facet. Next: dyadic-scale induction on the block-structured vertex.
- **breakpoint-vertex (UPPER) — CHANGES REQUESTED, partial; covering-radius mechanism DEAD.** Mandated
  GATE FAILED: GAP TWO-CAP (two-cap covering-radius contraction to u_n) is REFUTED — worst max-gap/u_n
  = 3.2×…24.6× (n=3..7), saturates at ≈3–5·u_n exactly as R10 one-cap. Both one-cap (R10) and two-cap
  (R12) now dead; the whole covering-radius family is pruned. CERTIFIED Lemma FGR (μ_i =
  min(μ_{i-1}, dist(a_i,R_{i-1})), so μ_{n+1} = min_i dist(a_i,R_{i-1}); reviewer reproduced 0 fails) and
  Reduction R-COV' (sufficiency direction: μ_{n+1} ≤ u_n ⟹ upper bound in valley, via ESF-2, T=∅
  correctly excluded — the converse is NOT rigorous and is not certified). RESIDUAL correctly re-stated
  as the **first-gap pigeonhole** μ_{n+1} ≤ u_n (robustly true: 0 fails, worst 0.75, tight at dyadic
  boundary) — a global adaptive discrepancy claim, NOT a covering radius. The covering-radius vehicle
  should be retired; hand the first-gap pigeonhole to the outliner for a genuinely new lever.

**R11 progress (still partial; no APPROVE). Two lemmas CERTIFIED; one mechanism RETHINK.**
- **ballot-matching (LOWER) — RETHINK, mechanism REFUTED.** The structured debit→credit
  transport/Hall family collapses (reviewer-verified negatives: prefix/suffix/interval-Hall/
  value-dominating all fail; GAP-TERMINAL premise `S_m<0` is false — tight case S_m≥0). After R10
  (scalar-reserve family dead) and R11 (structured-matching family dead), GAP MID-core has NO
  surviving structured lower lever — needs a genuinely new global framing (aggregate ballot /
  cycle-lemma on the reachable word, or F-partition majorization vs the fixed ladder B).
- **breakpoint-vertex (UPPER) — CHANGES REQUESTED, two lemmas CERTIFIED; density substrate refuted.**
  Lemma CONF (`confinement-reachable-set`) CERTIFIED: `max R_i ≤ a_1` via one-line induction
  `|v−a_i|≤max(v,a_i)`, confining `R_{n+1}⊂[0,a_1)⊂[0,L/2)`. Lemma MD2 (`multiset-doubling`)
  CERTIFIED: reachable multiset `|M_i|=2^i`, support `=R_i`, enumerates all `2^{n+1}` subset-KK
  values; multiset pigeonhole gives a gap `<u_n/2` (but a gap is NOT reachable). COUNT `|R_{n+1}|=
  2^{n+1}` REFUTED (reviewer-verified exact: all-equal `a_i=1/(n+1)`, a genuine valley for n≥3, has
  `|R_{n+1}|=2`; n=2 witness `{7/16,9/32,9/32}` gives `|R_3|=5<8`). The COUNT+density-pigeonhole
  vehicle is a dead substrate; GAP U-cover (Covering claim `cov(A)≤u_n`) remains the honest open
  crux — needs a mechanism seeing both spread (gaps) and collision (small/zero reachable values).

**R9 progress (both walls advanced; still partial; no APPROVE). Two lemmas CERTIFIED.**
- **parity-measure-potential (LOWER) — GAP MID-core NOT closed.** Lemma ONE-REC
  (`recursed-dyadic-dichotomy`) CERTIFIED: scale-truncation `B_{≤ℓ}=⊔_{j≤ℓ}G_j` is a refinement of
  `C_ℓ` (partition-of-cuts), each `G_j` has ≤1 fragment `>2^{j−1}` (superincreasing), so certified
  Lemma ONE recurses down every dyadic sub-ladder — the shared structural dependency of BOTH walls,
  now de-risked. Exact residual reformulated: `μ{g odd}−1 = ∫_0^{2^{n−1}}φ(g)`, `φ(c)=1[c odd]−c`
  (reviewer-verified: `φ≥0⟺c≤1`, `φ<0⟺c≥2`); negative mass sits exactly on `{g≥2}`. REFUTED the
  outliner's `ρ_k` cumulative-surplus reserve (deficit grows with n, −30.5 at n=6; walk-height-only
  reserve `ψ(g(τ))` also impossible) — the correct reserve must be a whole-ladder F-mass-tracking
  object, not a local surplus. Honestly still open; correctly recorded as partial (not overclaimed).
- **breakpoint-vertex (UPPER) — GAP U-cover NOT closed.** Lemma BL (`band-landing`) CERTIFIED:
  descending survivor partial sums `P_0<…<P_n=L−a_1>a_1` cross `a_1` at a UNIQUE index `k≤n` (no
  straddle — finite strictly-increasing sequence), subset `T={a_1,…,a_k}` gives `r=a_1−P_{k−1}∈
  [0,s_k)⊆[0,β_nL)` realized by ESF-1 in exactly `n` moves. Reachability reformulation (Covering
  claim: `R_{n+1}` meets `[0,u_nL]`) and RIGOROUS refutation of the outline's step-3 recursion
  (greedy band-landing / flip-if-helps / drop-one ALL overshoot `u_nL`, machine-verified) — the
  residual is a GLOBAL covering problem, not a recursion. BL alone falls a factor `2^{n−1}` short
  (r=17/100>u_2 on the n=2 witness). Honestly still open; correctly recorded as partial.

**R8 progress (both built approaches advanced; still partial; no APPROVE).**
- **parity-measure-potential — GAP MID-core NOT closed; reformulation + new sub-case certified.**
  Lemmas OSR (`order-statistic-reformulation`) and OSR-cap (`one-sided-walk-cap`) CERTIFIED:
  `D(S)≥1 ⟺ Σ_{B odd rank}v ≥ Σ_{F even rank}v` (clean, no integral, from certified Lemma R +
  ΣF−ΣB=1), and the one-sided-walk sub-case `S_k≤1 ∀k` (⊋ old `0≤g≤1`) closed by Abel summation.
  Reviewer-verified both identities exact + sub-case never violated on 20000 refinements (n=2..6),
  minD=1.0003. Residual = aggregate overshoot regime (`max_k S_k≥2`, `|F|≥3`); reviewer-confirmed
  negative fact F1 (prefix form fails ~27%, 8043/30000) rules out any running-deficit monovariant.
  The core aggregate-compensation inequality is HONESTLY OPEN (builder did not hand-wave it).
- **breakpoint-vertex — Prop UV NOT closed; ESF-1/ESF-2 certified, Subset-KK residual honest.**
  Lemmas ESF-1 (`subtraction-from-top-subfamily`) and ESF-2 (`subset-caterpillar-subfamily`)
  CERTIFIED: explicit budget-exact (n-move) tree-realizable subfamilies of 𝓡(A) on certified P/DM;
  ESF-2 gives descending-KK realizability incl. the abs-flip branch. Reduction UV' reduces Prop UV
  to the **Subset-KK claim** (some subset's descending-KK value ≤u_nL) — a strictly cleaner explicit
  target, but LEFT OPEN. n=2 negative result reviewer-verified by exact arithmetic
  (A={9/20,7/25,27/100}: ESF-1 min 17/100>1/7, abs-flip {a2,a3}=1/100≤1/7) — the one-sided family is
  provably insufficient, so abs-flip is mandatory. Residual honestly stated, not overclaimed.

**R7 progress (all three built approaches advanced; still partial; no APPROVE).**
- **Lemma MID (mass-difference-reduction) CERTIFIED** (parity-measure): with g=N_F−N_B on
  (0,2^{n−1}), (a) D(S)=μ{g odd} and (b) ∫g=1 (=ΣF−ΣB=2^n−(2^n−1), the superincreasing signature).
  This ELIMINATES the SPLIT cross-term μ(O_F∩O_B) and the balanced/unbalanced dichotomy: the entire
  a=0 lower bound L2 is now EXACTLY equivalent to **GAP MID-core**: μ{g odd} ≥ ∫g (=1). Closed
  within it: |F|=2 (N_F even ⇒ μ{g odd}=D(B)≥1 by IH) and 0≤g≤1 (D(S)=1 exactly). Residual: |F|≥3.
  Reviewer verified MID exact (D(S)=μ{g odd}, ∫g=1) on hand-built + random a=0 refinements at n=4.
  Also REFUTED (reviewer-confirmed) the outliner's "O_B meets each dyadic gap in ≤1 interval"
  invariant with an explicit budget-respecting witness (2 intervals in gap (2,4)).
- **induction-peel: assigned aimo-0298 split-and-average mechanism REFUTED for D (DEAD-END lever).**
  Reviewer independently confirmed the averaging inequality D(S)≥½(D(S_O)+D(S_E)) fails on a large
  fraction of budget-enforced refinements (~28–45%), so it is not a theorem for the parity-measure
  D; also S_O,S_E are not valid IH instances (lose mass + ladder structure). Slug stays partial/live
  — its prior rigorous content (PEEL/SPLIT/ONE/TB/band-decomp, Case (a), trivial regime of L⋆, |F|=2
  sub-case, both telescoping identities, entire upper dominant case §4A) stands; only THIS round's
  lever died. GAP L2 must be closed upstream (MID route), not by monovariant-split.
- **Lemma RL (leftover-realizability) + Lemma VS (valley-sharpness) CERTIFIED** (breakpoint-vertex):
  the upper valley is reduced EXACTLY to **Prop UV** (min 𝓡(A)≤u_nL) via certified Reduction R-UV;
  RL characterizes 𝓡(A) as tree-realizable signed subset sums (strict subset of {0,±1} sums — no
  summing of positives), so a naive 2^{n+1}-subset pigeonhole is INVALID; VS proves no single DM
  move admits an IH(n−1) certificate in the valley (thresholds c(n)L, β_nL meet the boundary
  exactly), forcing ≥2 coordinated cuts (rigorous adaptivity). Theorem VERT (vertex finiteness) is
  proved profile-independently (LP-vertex / hyperplane arrangement), NOT a spot-check; but Prop UV
  itself is only numerically verified (387 valley profiles) — the discrepancy bound is UNPROVED.

**R6 progress (all four built approaches advanced; still partial).**
- **Lemma TB (top-band-decomposition) CERTIFIED:** for any refinement R of C_n, D(R)=e+D_low with
  e=(f₁−2^{n-1})⁺, D_low=μ{t<2^{n-1}:N_R odd}. Closes UNCONDITIONALLY the base case, the trivial
  regime f₁≥2^{n-1}+1 (⇒D≥1), and Case (a) top-uncut (⇒D≥2^{n-1}). Re-verified on 20000 refinements.
- **Lemma DM (elementary-reductions) CERTIFIED** and **Lemma U0 (even-multiplicity-corrector)
  CERTIFIED:** the DELETE/MATCH D-tracking move set + the bisect-all corrector (UB nontrivial only
  at full budget m=n+1). Both self-contained on P/M.
- **L2 SPLIT master inequality (parity-measure) VERIFIED:** D(S)≥|D(F)−D(B)| (re-verified on 20000
  random partitions); with IH D(B)≥1 this closes the entire |D(F)−D(B)|≥1 subregime of GAP L2,
  incl. all even-multiplicity fragmentations D(F)=0. Residual: cross-term bound GAP L2-exch.
- **smoothing-majorization REBUILT** as the finite DELETE/MATCH game: 3 of 4 upper cases closed
  by exact identities (3.1)/(3.3)/whole-tail-peel; only the balanced valley (a₁<L/2, a₂<β_nL) open.
- **induction-peel:** trivial regime of (L⋆) and the |F|=2 sub-case of Case II closed rigorously.

**Remaining shared walls (still open after R7 — both SHARPENED to cross-term-free scalar claims):**
- **Lower — GAP MID-core (supersedes GAP L2-exch):** prove μ{t∈(0,2^{n-1}):g(t) odd} ≥ ∫g = 1 for
  every a=0 refinement with |F|≥3, where g=N_F−N_B (Lemma MID). This is the ENTIRE residual of the
  lower bound (Case (a), trivial regime, |F|=2, and 0≤g≤1 all closed). It needs a monotone/exchange
  argument using the ladder structure of B at every scale (Lemma ONE recursed) — the pure-integral
  version is FALSE (g≡2 on measure ½). Same combinatorial content as induction-peel's exchange step
  and breakpoint-vertex's GAP L-fin; now expressed with NO cross-term, NO min-cap, NO
  balanced/unbalanced split.
- **Upper — Prop UV (supersedes GAP U-VALLEY):** prove min 𝓡(A) ≤ u_nL in the balanced valley,
  where 𝓡(A) = tree-realizable signed subset sums (Lemma RL). This is EXACTLY the upper bound in the
  valley (Reduction R-UV). A direct pigeonhole is invalid (not all {0,±1} patterns reachable); ≥2
  coordinated cuts are provably forced (Lemma VS). Only numerically verified so far.
