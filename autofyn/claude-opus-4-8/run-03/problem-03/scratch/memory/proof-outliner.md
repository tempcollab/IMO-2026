# proof-outliner role memory

ALWAYS: for the claiming/greedy allocation game, use D = Liu − Xiang = Σ(−1)^{i+1} b_i
and the VERIFIED identity D = measure{ t : #{pieces>t} is odd } — it is a clean spine
for both bounds and is genuinely distinct from an induction framing (because imo-2026-03
round 1, identity confirmed on 20000 random multisets).

NEVER: propose "always bisect the largest piece" or "always split the smallest" as
Xiang's (adversary) strategy — both are recorded DEAD ENDS; the correct response is
adaptive/recursive (because imo-2026-03 explorers refuted them by counterexample).

ALWAYS: I only have the read-only sample_approaches ranker tool; registration/ranking is
done by the outline-reviewer, not me — just write approach files + report (imo-2026-03 r1).

ALWAYS: for imo-2026-03 upper bound, the correct Xiang move is a MULTI-PAIR subset peel —
cut a₁ into fragments matching a subset T of the smaller pieces, cancel |T| pairs at once,
reduce UB(n)→UB(n−j); closing condition 2Σ_T ≥ L(1−u_n/u_{n−j}) (verified, dyadic hits it
with equality). NEVER re-propose single-peel/greedy-merge (dead ends) (imo-2026-03 r2).

NEVER: propose "force odd-set ⊆ [0,u)" as the upper-bound positional target — FALSE: the
tight Xiang play on dyadic n=2 leaves odd-set at [u,2u), not [0,u) (checked, imo-2026-03 r2).

ALWAYS: for imo-2026-03 GAP L, prefer the EXACT dominant-cut identity D_new=D_C−2μ([0,p2)∩E_R)
(E_R = R's even-count set) over any "shadow-coupling map" — it is a verified equality, not an
existence claim, so it turns the coupling into algebra; pair it with a budget-monotonicity lemma
to reduce to a SINGLE top cut (imo-2026-03 r3, explorer verified numerically+symbolically).

ALWAYS: keep TWO approaches per shared wall but far apart by MECHANISM (GAP L: exact-identity vs
surrogate-domination; GAP U: subset-cover vs smoothing/majorization) so they don't die together
— same technique on same gap = same wall (imo-2026-03 r3).

ALWAYS: for imo-2026-03, the all-equal profile a_i=1/(n+1) is EASY (bisect one piece ⇒ D=0),
not a hard case; the multiplicative worst-case IH over-estimates BALANCED profiles, so a pure
peel+worst-case-IH cannot close them — need bisection/parity-collapse or majorization-to-dyadic
there (imo-2026-03 r2).

ALWAYS: for imo-2026-03 the LOWER wall L1 (critical band) and L2 (top-shredded) are the SAME
combinatorial object — interleave a free mass into the fixed ladder C_{n-1}, differing only by
below- vs above-gap insertion; state ONE unified gap-interleaving lemma, don't split the work
(explorer-lower r5). The (L*) inequality splits into a trivial regime w<=2^{n-1}-1 (one-line
max bound) and a critical band of width exactly 1 in f1 (the only real content).

NEVER re-propose for imo-2026-03 GAP U: global concavity of V (FALSE, V is min over chamber-
concave-not-affine funcs), cascading/sequential single-piece bisection (4.7x violation at n=5
near-uniform), or any single non-adaptive global threshold rule (fails near-equal profiles).
The live upper lever is extending Lemma U0 (m<=n=>D=0) to m=n+1 via SPLIT's EXACT cross term
(explorer-upper r5).

ALWAYS consider the LP-vertex/piecewise-linearity finiteness framing as the FRESH far route when
a cutting/splitting minimax field has collapsed: single-cut D is PL with slope in {-2,0,2}, so
optimal cuts are ties or bisections — can make an "imperfect cut" gap vacuous AND finitize a
continuum search (imo-2026-03 breakpoint-vertex, r5).

ALWAYS: for imo-2026-03 GAP L2-exch, the certified crux aimo-0298 (IMO-SL 2019 C9) is the
best structural analogue — its induction is NOT an adjacent transposition but a
minimal-scale-run SPLIT into two smaller sets S_O,S_E (parity classes) + average via IH; port
that as the exchange-step mechanism, not a value-slide (round 7).
ALWAYS: keep the two lower routes far apart by putting the fix in different PLACES —
induction-peel = monovariant/split mechanism (downstream), parity-measure = strengthen the IH
itself (upstream, per explorer "master ineq unclosable from D(B)>=1 alone"); same fix twice = one
wall (round 7).
NEVER: propose a naive full subset-sum pigeonhole for GAP U-VALLEY — only ~half of +-1 patterns
are differencing-tree-achievable, so it is short by factor ~2 (u_{n-1} not u_n); the achievability
deficit is THE hard step and must be flagged, not glossed (imo-2026-03 explorer, round 7).

ALWAYS: for imo-2026-03 the LOWER wall is ONE inequality (Sigma c_i w_i>=0 on the signed
merge-walk, c_i=1[i odd]-S_i); parity-measure and merge-interleave are the SAME inequality
(explorer-confirmed) — nominate ONE best vehicle (parity-measure, owns MID), do NOT advance both.
The genuinely-different SECOND lever must be a different MECHANISM (matching/transport certificate
vs induction), not a renotation (round 8).
ALWAYS: for imo-2026-03 the UPPER valley is ONE object (tree-realizable subset sums); breakpoint-vertex
(existential VERT enumeration) and subset-sum-pigeonhole (existential counting) are the SAME — the
genuinely-different framing is CONSTRUCTIVE (explicit sorted-differencing + DELETE-repair, aimo-0796),
not another existence proof. Note aimo-0796's ropad bound rho<a2 is off by up to 2^{n-1} vs u_n L, so
it alone cannot close it — a telescoping bound is mandatory (round 8).
NEVER: give induction-peel a MERGE-two-F-fragments monovariant for the lower bound — merging
INCREASES D (checked: n=3 example 2.2->3.0), so the minimizer is the HIGH-|F| canonical telescoping
config, not |F|=2; a "reduce to |F|=2" induction is backwards and wrong (round 8).

ALWAYS: for imo-2026-03 GAP MID-core, BOTH one-pass sign monovariants are dead — prefix P_k=1[k odd]-S_k>=0 fails ~27% (F1), suffix Q_j=sum_{i>=j}c_i<=0 fails ~89% (checked r9). The only live lower lever is a strengthened-IH GLOBAL potential with a cross-scale RESERVE term ro_k (repairs the refuted per-gap-local statement), using Lemma ONE recursed; never re-propose a value/index-Abel single sign (round 9).
NEVER: for imo-2026-03 propose ANY additive scalar reserve/potential Φ(τ) for LOWER MID-core — the
ENTIRE family (count- AND mass-based, incl. R_F(τ) mass-below/above with correct boundaries) is
provably DEAD (R10, n=7 witness Φ(8.944)=−2.07<0, κ unbounded in n). Reason: Φ(τ) only tests
prefix/threshold cuts, but the true min-cut sits on a NON-PREFIX set (union of dyadic bands with an
untouched gap). The only surviving lower lever is an EXPLICIT transport/min-cut certificate
(Gale–Hoffman, aimo-0129 endpoint-split verification), a global assignment not a scalar (round 11).
NEVER: for imo-2026-03 UPPER propose the two-case (generic/near-uniform) skeleton OR any fixed/bounded-
depth move lemma — both refuted R10 (required escape depth Θ(n), failures NOT localized to near-uniform,
52.9% at n=6). GAP U-cover needs a GLOBAL confinement×count×density invariant (max(R_i)≤a₁ confinement
is cheap+provable; |R_{n+1}|=2^{n+1} injectivity needs adversarial check; the crux is GAP→VALUE, since
pigeonhole gives a small GAP not a small element and the budget is exhausted) (round 11).
ALWAYS: when both explorers confirm a wall has NO far-apart second vehicle (upper subset-sum collapses
to the same tree-object; lower's only survivor is transport), a TIGHT one-vehicle-per-wall field is
correct — do NOT force a diluting third slug that would share a gap (single-gap trap). Breadth comes
from the two walls being far apart in mechanism, not from slug count (round 11).
NEVER: trust an all-INTEGER numeric sweep as evidence the ladder structure is unneeded for imo-2026-03 GAP MID-core — integrality accidentally excludes the half-integer witness F={0.5,0.5,0.5},B={0.5} (SigmaF-SigmaB=1,|F|=3, but D=0 via even multiplicity). The ladder (Lemma ONE) is load-bearing; any structure-free ballot/walk argument is provably false (round 9).

ALWAYS: for imo-2026-03 when a wall's obvious families are all dead, the far-apart pair is
LP-VERTEX/active-constraint-rank (reuse breakpoint-vertex Theorem VERT on a NEW polytope — the lower
reachable-word interleave polytope) vs MAJORIZATION+exchange (F-profile vs fixed dyadic ladder + a
B-refinement monotonicity GAP B-MONO). These are genuinely far apart (polytope-vertex rank vs
Schur/rearrangement), NOT near-variants, so putting both on the lower wall is legit breadth, not a
single-gap-trap double-up (round 12).
NEVER: for imo-2026-03 treat c_B=0 (B uncut) as a WLOG for the lower MID-core — explorer PROVED it
false (42.8% of B-cuts strictly lower D at n=5). Any majorization-vs-fixed-ladder argument needs a
SECOND ingredient (GAP B-MONO: min_B D(F,B)≥1 per fixed F). Flag to reviewer that GAP B-MONO risks
being MID-core restated unless the exchange step localises the minimising B to one aligned config
(round 12).
ALWAYS: for imo-2026-03 LOWER GAP-EXTR, the vertex objective collapses (provably, via certified Lemma
P) to L_T = alternating sum of ODD-multiplicity distinct values descending — even-length blocks are
cancelling pairs (net 0). This is the vertex-native μ{g odd} content; attack it by minimal-counterexample
+ BLK box-face dichotomy (delete-zero / top-peel-recurse / box-free-generic-characterize), NOT by the
continuum MID route (dead r7-r11). Whole covering-radius family AND the UPPER first-gap must telescope
against Σa_i=L (charge far pieces to total mass), never against max consecutive gap (round 13).
ALWAYS: for imo-2026-03 UPPER two-cap covering-radius recursion, insist it be a GLOBAL set invariant
over R_i (built on certified CONF+MD2), NOT a single-pass policy — every greedy/policy recursion is
refuted (R9, ≤11.4x overshoot); and mandate a numeric gate of the exact c_i≤f(c_{i-1},a_i) inequality
before prose, plus EXPLICIT T=∅ exclusion (skip-everything needs n+1 deletes, infeasible) (round 12).

ALWAYS: for imo-2026-03 LOWER GAP-EXTR, the closing lever is the LP-DUAL/exchange-smoothing
certificate on the certified P_T polytope: sparse Farkas multipliers (y_j=±1 on the n+1
dyadic group-sum equalities, single z=2 on ONE cross order-inequality) certify L_T≥1 on the
WHOLE polytope, no vertex enumeration. Same object as same-group exchange-smoothing (aimo-0146).
Mandate the n=5 dual-sparsity + odd-block-count cheap-kill BEFORE prose (round 14).
NEVER: for imo-2026-03 LOWER assume the minimizing vertex is a canonical ATT one-fragment-per-scale
layout — REFUTED n=4 (F={6,6,4}, level-3 split {3,3,2}, L_T=1 via CROSS-GROUP cancelling pairs).
"No straddling" (true, superincreasing) ≠ "no cross-group value coincidence" (false). Any dual
must certify the non-canonical cross-group-pair tied vertices too (round 14).
NEVER: certify Lemma DSUM for imo-2026-03 UPPER — its per-step bound dist(a_i,R_{i-1})≤a_1·2^{-(i-1)}
is FALSE (exact rational counterexample n=3, i=3,4); aggregate is numeric-only and wrong-direction.
The UPPER closer is the extremal-tie MINIMAX (max_{A∈valley} min_T |Σε_i a_i|, unique-achiever
perturbation → dyadic ladder is the tied maximizer with Φ=u_n L), NOT any forward reachable-set DP
(round 14).

NEVER: give induction-peel the MERGE/budget-domination lever for Case II (merge two top frags +
reallocate freed cut to tail, induct down to |F|=2) — REFUTED adversarially R15: per-config
"some merge+realloc gives D'<=D0" fails 9.2-14.5%; AND structurally the merged frag F_i+F_j>2^{n-1}
lands in the OPEN Case (I) critical band, not the solved |F|=2 bisection. This is the round-8
"reduce to |F|=2 is backwards" fact, now doubly confirmed (round 15).
ALWAYS: for imo-2026-03 UPPER valley, the VALLEY-TIGHT no-margin obstruction is a BOUNDARY-LAYER
phenomenon (the tight family A^(n) sits ~u_n/2 below L/2). So a TWO-REGION split is legit and does
NOT violate VALLEY-TIGHT: DEEP valley (a1<=L/2-c*u_n) has genuine margin (R15 cheap-kill: worst
Phi/u_n=0.37-0.56 at n=4,5), crude bound OK there; BOUNDARY layer handled by exact continuation of
the certified dominant formula D=2a1-L across a1=L/2. Mandate exact gate: deep margin must NOT
shrink to 0 as n grows (round 15).
ALWAYS: for a wall with NO live vehicle, a genfunc/transform reframing (Z(z)=int z^g, Z(-1)=L-2*mu{g
odd} = MID restated) is REPACKAGING unless a genuine two-band RECURSION for Z_n(-1) exists — open it
only as a GATED probe whose first+only committed step is the exact-arithmetic recursion cheap-kill;
if the top/bottom-band cross term = the dead SPLIT cross-term mu(O_F cap O_B), retire it. Do NOT let
it consume a builder as a dressed-up tautology (round 15).

NEVER: for imo-2026-03 UPPER deep interior, send a builder to CONSTRUCT any fixed/structured
subset-selection family (decimated/AP-index, contiguous-block, prefix, bounded-deletion) as the
descKK-min witness — ALL pre-killed by exact gate R16 (worst min/u_n = 1.05-8.2x, GROWS with n),
while true min over unrestricted subsets is 0.4-0.6 u_n with arg-min shape spread across all sizes.
The deep-interior residual is a NON-constructive existence/discrepancy statement; no bounded family
witnesses it (matches R9-R11 Θ(n)-depth pattern). The decimated/alternating opening the R16 explorer
flagged is refuted (round 16).

ALWAYS: for imo-2026-03 LOWER, after 9 dead levers, the ONLY genuinely-new axis is value-side
layer-cake (slice by g-VALUE, target (★) Σμ{g≥2i}≤Σμ{g≤1−2i}) crossed with ONE-REC scale-of-origin
as a self-referential index (aimo-0009 a_{a_i} template) — the FIRST lever using BOTH BLK and ONE-REC.
Gate the PER-CELL CAP (not (★), which is certified true 0/900); kill if it's just (★) rearranged
(reframing=dead, like transform/vertex-polytope). Termwise per-level is REFUTED (fails i=1) so the
cap MUST let i≥2 repay an i=1 deficit (round 17).
NEVER: for imo-2026-03 UPPER deep interior, propose ANY second-moment/averaging ensemble as PRIMARY —
fixed-order uniform + per-size both KILLED (rare-needle, ratios 5-100x growing with n); full-RL tree
ensemble predicted to fail same way, so demote it to a gated FIRST-STEP probe (build only if mean(V²)<
(u_n L)² robustly). The surviving PRIMARY is the extremal/worst-profile+smoothing recipe (the WTC/
VALLEY-TIGHT recipe) redirected at the deep interior where a 0.34-0.56 u_n margin exists (round 17).

ALWAYS: for imo-2026-03 UPPER, Φ = min_{∅≠T} descKK(T) EXACTLY equals the min over ALL differencing
trees/subsets (0 counterexamples, exact Fraction, full-tree n≤5, random sliver + A^{(n)} + sliver
perturbations) — the caterpillar/reflected-walk family is MINIMUM-COMPLETE, so the GAP-ACH factor-2
achievability deficit does NOT affect the minimum. A vector-balancing/Steinitz reframing over ALL
signings is unnecessary; the min already lives on tree-realizable caterpillars (round 18).
NEVER: for imo-2026-03 UPPER propose the single-target subset-sum density min_{S⊆tail}|a₁−Σ_S|≤u_n as a
CLOSING lever — REFUTED round 18 (fails 15-33% of sliver profiles, ratio up to 1.99 growing with n). It
is only ever an UPPER bound on Φ (WTC corollary), never itself ≤u_n; the true Φ needs genuine
differencing (≥2 tail pieces cancelling). Same family as the R16-dead per-subset WTC Ψ (round 18).
ALWAYS: for imo-2026-03 UPPER sliver, the sup Φ/u_n is attained at the sliver/boundary INTERFACE as a
continuous limit of the WTC-closed boundary and DROPS with depth (A^{(n)} family: 0.94 at boundary →
0.44 one u_n/4 deeper). So it is NOT a fresh tight problem — the right object is a SHARPENED-WTC
continuation (exact at the interface, slack growing with depth), not a margin argument (round 18).
ALWAYS: for imo-2026-03 LOWER, after 11 dead levers + the R18 proof that (★) is a pure algebraic
rewriting of D≥1 (floor-parity identity + ∫g=1, zero content), the honest call is HOLD — do not
dispatch a builder to write LOWER prose. The ONLY remaining lead is an EXPLICITLY cross-scale transport
(SUFFIX-★ scale-cumulative, aimo-0127×aimo-0009); offer it ONLY as a gate-only probe (round 18).

ALWAYS (imo-2026-03 UPPER, r19): the CERTIFIED Reduction R-UV makes `min R(A) ≤ u_nL`
(tree-realizable values, Lemma RL) an EXACT iff for the upper bound — the caterpillar object
μ_{n+1} (FGR) that breakpoint-vertex fought since R7 is a strictly HARDER sub-target
(min R(A) ≤ μ_{n+1}). When the explorer showed μ_{n+1}=min R(A) is FALSE, the right move was
NOT to bridge but to DROP the caterpillar and target min R(A) directly. Re-check whether a
long-standing sub-target is harder than a certified reduction's true target before building a
bridge to it.
NEVER (imo-2026-03 UPPER): re-outline any anchored-walk/caterpillar contraction, covering radius,
density pigeonhole with a constant factor, averaging/2nd-moment, or greedy `u_{n-1}(L−a₁)`-target
recursion — 9 dead upper mechanisms + VALLEY-TIGHT forbids ANY constant-factor margin (ratio→1).
Every UPPER outline must land EXACTLY at u_nL via `1/u_n=2/u_{n-1}+1`, and must carry the FGR
dist-recursion gate (not "min positive of the set" — drops exact-0 cancellations) on HARD families
(r19).
