ALWAYS: for the "cut a stick, alternate claiming largest" family, reduce to the scalar
D=sum (-1)^{i+1} b_i (Liu=(1+D)/2) and use the measure identity D=|{t: #pieces>t odd}| plus
the cancelling-pair identity D(S∪{v,v})=D(S) — these three are the reusable engine (imo-2026-03, round 1).
NEVER: claim an inductive "peel the largest piece, recurse on (n-1) instance" closes without
checking the global descending SORT doesn't couple the peeled block with the tail — for
imo-2026-03 both bounds' peels stalled exactly there (symmetric-difference too lossy on the lower
bound; single-pair peel fails when max(a1,2a2)<L*c(n) on the upper bound), round 1.
ALWAYS: numerically brute-force the second player's best response on small n BEFORE trusting a
proposed strategy — it instantly killed "greedy pair top two" and "bisect largest" as universal
Xiang rules (imo-2026-03, round 1).

ALWAYS: on imo-2026-03, the upper bound cleanly reduces to m=n+1 via Lemma U0 (m<=n =>
Xiang forces D=0 with a top-copy chain making every final length even-multiplicity;
Corollary of Lemma M). Fully rigorous, verified. (round 2)
NEVER: on imo-2026-03, claim the dominant a_1>c(n) branch is closed by "replicate-all then
bisect leftover" — replicate-all already spends all n cuts, no spare cut exists (cut-count
obstruction GAP U1). (round 2)

ALWAYS: for imo-2026-03 lower bound, use the dichotomy "at most one final piece exceeds
2^{n-1}" (superincreasing) and the exact identity D(S)=f_1-D(S_L) in the a=1 case — it
converts the lower bound into an upper-type inequality D(S_L)<=f_1-1 (tight, verified), round 2.
NEVER: assume D is additive over a multiset union split by scale — D depends on the GLOBAL
sort; use g_S = g_{S_L} XOR 1[t<f_1] via Lemma I instead (round 2).

ALWAYS: for imo-2026-03 upper bound, split on a_1 vs L/2 — the DOMINANT case a_1≥L/2 CLOSES
cleanly (bisect a_1 if a_1≥Lc(n); else match whole tail into a_1 → single leftover 2a_1-L<u_nL),
and it contains the extremal dyadic input. This is a real, complete chunk (round 2).
NEVER: try to close the BALANCED case a_1<L/2 (upper) or all-equal by ANY multiplicative IH —
single-leftover reaches Δ(a)=min signed sum which exceeds u_nL for all-equal-odd; balanced needs
early-stopping WITH EVEN MULTIPLICITIES (all-equal ⇒ D=0). Verified B(a,n)≤u_nL numerically but
the potential is non-multiplicative (imo-2026-03, round 2).

NEVER: for imo-2026-03 upper bound, pursue the "mass-threshold subset-cover disjunction is
exhaustive" lever for a_1<L/2 — it is provably FALSE: A=(0.44,0.281,0.279) (k=2) defeats every
threshold move yet has minimax D=0.002 (bisect wins). The reduction bounds residual by MASS only,
but residual D depends on internal structure (near-cancelling tail). a_1<L/2 needs a D-TRACKING
argument (induction-peel exact toggle identity, or smoothing), round 4.
ALWAYS: for imo-2026-03 upper bound, the a_1>=L/2 region is fully+cleanly closed by whole-tail
peel: cut a_1 into all m-1 tail values (Lemma P kills every pair) -> single piece 2a_1-L, D=2a_1-L
<=u_kL iff a_1<=c(k)L, using c(k)=(1+u_k)/2; Branch 0 bisect covers a_1>=c(k)L. Profile-independent, round 4.

ALWAYS: for imo-2026-03 lower bound, treat it as a REFINEMENT optimisation (each original piece
partitioned, total extra parts <= n) — D depends only on the final multiset, no adaptivity. The
true min-D minimiser cuts the top 2^n into n+1 fragments interleaving the UNCUT tail (each frag
slightly > a tail piece), telescoping D = sum(frags) - sum(tail) = 2^n-(2^n-1) = 1 (round 4).
NEVER: trust "budget-monotonicity => WLOG Xiang makes ONE top cut" for imo-2026-03 lower bound —
FALSE; the minimiser puts ALL n cuts on the top (verified). Budget-monotone points the wrong way
(more cuts weakly help Xiang), so it cannot force a single top cut (round 4).
ALWAYS: use the clean strict-max peel identity D(S)=f1-D(S\f1) (unique max f1) — proved via Lemma M
by splitting the line at the 2nd-largest value. It reduces the "one piece > 2^{n-1}" lower-bound
case to the upper-type inequality D(S')<=f1-1 (imo-2026-03 GAP L1), round 4.

ALWAYS: for imo-2026-03 breakpoint-vertex, prove the joint VERT via a GLOBAL polytope-vertex
argument, NOT a sequential settle-one-cut monovariant (reviewer rejected the latter as un-tying).
D is linear on each equal-length "sort chamber", so min over the refinement product-of-simplices
P_tau is at an arrangement vertex; a rank count (active zero+tie constraints, rank N-M on the
direction space) forces #distinct positive values <= |A| <= n+1. Fully rigorous, no settling order,
no un-tying hazard (round 5).
NEVER: claim VERT alone closes GAP L / GAP U for imo-2026-03 — it only FINITIZES them (reduces the
continuum to a finite tie-pattern search); the finite check D>=1 on refinements of C_n and the
leftover rho<=u_nL via SPLIT still remain and are NOT automatic (round 5).

## imo-2026-03 (breakpoint-vertex), round 6
ALWAYS: for the C_n lower bound, split the Lemma-M integral at the top threshold 2^{n-1}; Lemma ONE forces N<=1 there so the top band contributes exactly (f1-2^{n-1})^+ (Lemma TB). This closes trivial regime f1>=2^{n-1}+1 and top-uncut Case (a) in one line, reducing everything to D_low bound (because it isolates the excess cleanly, round 6).
NEVER: try to close L1/L2 by bounding SPLIT's cross term crudely -- worst-case gives only D>=|D(X)-D(Y)|>=0, never >=1; the cross term must be computed via the one-per-gap interleaving (verified insufficient otherwise, round 6).

ALWAYS: for imo-2026-03 GAP L2 (a=0 lower bound), use the SPLIT master inequality
D(S) >= |D(F)-D(B)| (Lemma SPLIT + mu(O_F cap O_B) <= min(D(F),D(B))=min via Lemma M), with
D(B) >= 1 from IH LB(n-1). This closes every config with |D(F)-D(B)|>=1 incl. all
even-multiplicity fragmentations (D(F)=0). Residual = balanced regime |D(F)-D(B)|<1, needs
cross-term bound mu(O_F cap O_B) <= (D(F)+D(B)-1)/2 (round 6).
NEVER: for imo-2026-03 L2, use the "self-pairing => WLOG distinct fragments" reduction — deleting
a fragment pair {v,v} via Lemma P is D-preserving but LOSES the refinement-of-C_n structure
(top mass drops from 2^n), so it does NOT set up the induction. Use the F/B SPLIT decomposition
instead (round 6).

ALWAYS: for imo-2026-03 lower bound, the cut budget <=n is ESSENTIAL — the UNLIMITED-cut versions
of both (L*) and Case II are numerically FALSE (refuted n=2..4, round 6). So no mass-only/cut-free
bound closes it; the extremiser uses ALL n cuts (one fragment per gap). Clean rigorous sub-wins:
trivial regime of (L*) via D(S')<=max(S')<=2^{n-1}<=f1-1 (one line), and Case II |F|=2 forces
F={2^{n-1},2^{n-1}} => N_S=N_T+2*1[t<2^{n-1}] same parity => D(S)=D(T)>=1 by IH (round 6).
ALWAYS: for imo-2026-03 UPPER bound, model Xiang as a finite DELETE/MATCH reduction game (Lemma DM,
via Lemma P): DELETE x (bisect) -> D(S\{x}); MATCH x>y -> D((S\{x,y})∪{x-y}). Both 1 cut. Only
LEGAL+SUFFICIENT needed (not optimal), so no VERT. Closes all cases but the balanced valley
{a1<L/2, a2<beta_n L}, beta_n=2^{n-1}/(2^{n+1}-1). Reduce-to-ONE-piece is REFUTED (nested-diff 28x)
(round 6).
NEVER: expect a single deterministic Xiang rule to close the balanced valley — always-MATCH-top 4.2x,
always-DELETE-a1 25x, two-rule hybrid 10.7x; V has interior valleys, needs adaptive potential or VERT
finitization (round 6).

NEVER: for imo-2026-03 lower gap L2-exch, transfer aimo-0298's split-and-average monovariant to the
parity-measure D. REFUTED (round 7, budget-enforced valid refinements): D(S)>=1/2(D(S_O)+D(S_E))
fails ~28%; S_O,S_E aren't valid IH instances (lose mass 2^n-1 + ladder structure, can have D<1);
aimo-0298 works because w=sum 2^{-r} is a MASS-FREE additive per-element potential, our D>=1 is a
mass statement with no such formulation.
ALWAYS: for imo-2026-03 L2-exch, remember the gap is UNCLOSABLE from the scalar D(B)>=1 alone —
mu(O_F cap O_B)<=D(F)/2 fails ~65%. The fix is UPSTREAM (structural invariant on where O_B sits vs
the ladder), not a sharper downstream overlap cap (round 7).

## imo-2026-03 (breakpoint-vertex), round 7
ALWAYS: for the upper bound only SUFFICIENCY is needed (exhibit one good Xiang response), so VERT
(optimality) is NOT the operative tool there — reduce via certified DM: n moves on n+1 pieces reach
ONE leftover rho, D=rho, upper bound <=> min over achievable rho <= u_n L (Reduction R-UV), round 7.
NEVER: for imo-2026-03 valley, use a full-support (no-DELETE) differencing tree over all n+1 pieces
-- REFUTED numerically (214/516 valley profiles overshoot, worst 7.5x). DELETE / subset-selection is
ESSENTIAL; the achievable set is signed-SUBSET sums (Lemma RL), a STRICT subset of all {0,+-1}
patterns (differences only, never sum two positives) -> naive 2^{n+1}-subset pigeonhole invalid, round 7.
ALWAYS: the valley boundary is SHARP (Lemma VS): single DELETE needs a_i>=c(n)L>L/2, single MATCH
needs smaller-part y>=beta_n L; both fail since a_1<L/2 and a_2<beta_n L -> >=2 coordinated cuts
forced (rigorous adaptivity, subsumes all deterministic-single-rule numeric refutations), round 7.

## imo-2026-03 (parity-measure-potential), round 7
ALWAYS: for imo-2026-03 a=0 lower bound, use Lemma MID (mass-difference reduction): g=N_F-N_B on
(0,2^{n-1}) gives D(S)=mu{g odd} AND int g = ΣF-ΣB = 2^n-(2^n-1) = 1 (layer-cake). So D(S)>=1 <=>
mu{g odd}>=int g. This is CROSS-TERM-FREE — kills the SPLIT min-cap and the balanced/unbalanced
split in one move. |F|=2 and 0<=g<=1 close inside it; residual |F|>=3 (round 7).
NEVER: use the "O_B meets each dyadic gap in <=1 interval" invariant for imo-2026-03 — FALSE,
budget-respecting witness B={1,1.865,2,2.135,2.915,5.085} meets gap (2,4) in TWO intervals;
interval count is cut-budget-dependent. Only Lemma ONE recursed (<=1 B-excursion at the TOP of each
sub-ladder) survives, and it does NOT propagate per-gap (round 7).

ALWAYS: for imo-2026-03 a=0 lower bound, the cleanest reformulation is Lemma OSR — D(S)=Σ(-1)^{i+1}v_i
(Lemma R on merged S) minus ΣF-ΣB=1 gives D-1=Σ((-1)^{i+1}-e_i)v_i, so D≥1 ⟺ Σ_{B at odd rank}v_i ≥
Σ_{F at even rank}v_i. No integral/MID(a) needed. Sub-case S_k≤1 ∀k (g≤1) closes by Abel (P_k≥0), round 8.
NEVER: for imo-2026-03 MID-core, try a prefix/running-deficit monovariant on the merge order — the
PREFIX form Σ_{i≤k,Feven}v ≤ Σ_{i≤k,Bodd}v FAILS ~27% of admissible refinements while the GLOBAL
inequality holds always. Compensation is irreducibly aggregate; only a value-weighted transport works, round 8.

ALWAYS: for imo-2026-03 Prop UV (upper valley), use ESF-2 realizability — ANY caterpillar over ANY subset in ANY order is tree-realizable in exactly n DM moves (abs-flip v<t is the legal MATCH(t,v) cutting the resident). This converts the abstract min 𝓡(A) into an explicit constructive family; the residual "Subset-KK claim" = some subset's descending-KK ≤ u_nL (round 8).
NEVER: try to close Prop UV with the one-sided subtraction family a1−ΣT — PROVEN insufficient by explicit rational valley counterexample {9/20,7/25,27/100} (n=2): ESF-1 min 17/100 > u_2=1/7. abs-flip is mandatory (round 8).

ALWAYS: for imo-2026-03 lower bound (MID-core), the clean residual is mu{g odd}-1 = int phi(g),
phi(c)=1[c odd]-c, phi>=0 iff c<=1 -- neg mass EXACTLY on {g>=2}, pos on {g<=0}. Any reserve/
potential must be a WHOLE-LADDER object tracking remaining F-mass above tau; a cumulative-surplus
reserve int_tau^top phi(g) goes to -30 (grows with n) in BOTH scan directions, and a walk-height
reserve psi(g(tau)) fails because {g=2} bands have unbounded measure per unit height (round 9).
ALWAYS: "Lemma ONE recursed" for imo-2026-03 = scale-truncation B_{<=l}=union G_j (j<=l) of a
refinement of C_m is itself a refinement of C_l (partition-of-cuts, no cut crosses pieces) + each
G_j has <=1 fragment>2^{j-1}. Reduces to certified Lemma ONE. Proved+certifiable, shared by both
walls (round 9).

## imo-2026-03 (breakpoint-vertex), round 9
ALWAYS: for imo-2026-03 Subset-KK (upper valley), the FIRST band-landing is rigorous and clean
(Lemma BL): descending survivor partial sums cross a_1 (finite increasing seq => UNIQUE crossing, NO
straddle case; strict a_1<L/2 forces it), landing subset {a_1..a_k} with r=a_1-Σ_T ∈[0,a_2)⊂[0,β_nL),
realized by ESF-1. But this only reaches β_nL=2^{n-1}u_nL, a factor 2^{n-1} short (round 9).
NEVER: try to close Subset-KK by ITERATING band-landing as a recursion, or by ANY deterministic
single-pass greedy (band-landing recursion, flip-if-helps, drop-one) — ALL provably overshoot u_nL
(machine-verified worst 7.7x/11.4x/8.9x for n=2..7); true subset-min always ≤u_nL (0.84). The good
subset needs FORESIGHT; residual is a GLOBAL covering statement (descending include/skip reachable set
R_{n+1} meets [0,u_nL]; value 0 admissible via even cancellation for near-all-equal), NOT a recursion (round 9).

ALWAYS: for imo-2026-03 UPPER (breakpoint-vertex), the "two-level/bounded-depth existential move" generic
lemma is REFUTED — depth-2-to-dominant escape fails on a fraction GROWING with n (2.4/14.6/52.9% at
n=4/5/6) and failures are NOT near-uniform; escape depth is Theta(n) = the full covering claim. Do not
re-propose any fixed-depth move-search for the generic case (round 10).
NEVER: for imo-2026-03 UPPER, hope a single-window covering-radius bound reaches u_n — the true invariant
rho_i<=a_i/2 on [0,a_i] (validated 0/47516, but only a_{i-1}/2 is easily provable) SATURATES at
a_{n+1}/2 >> u_n on near-uniform; u_n needs a density/pigeonhole among tree-realizable values (Lemma RL),
not a covering radius (round 10).

## imo-2026-03 (parity-measure-potential), round 10
NEVER: use ANY additive scalar-reserve potential Phi(tau)=int_tau^L phi(g)+kappa*rho(tau) for
imo-2026-03 MID-core — the WHOLE FAMILY is REFUTED (mass-below sum_{f<=tau}f grows neg with n -27.7;
mass-above 2*tau*N_F LOOKS validated min Phi=0 kappa=2 on random+interleave samples but is FALSE:
adversarial n=7 witness F={63.01,62.86,2.13}, B a 12-piece C_6 refinement gives Phi(8.944)=-2.07<0
while D(S)=15>=1; required kappa unbounded in n). Cause: a wide high {g>=2} band's deficit can't be
carried DOWN to slow {g<=0} credit by a shrinking scalar reserve, round 10.
ALWAYS: BEFORE trusting a potential/reserve for imo-2026-03, adversarially sample the TWO-large-F-
fragment case (F has >=2 fragments near 2^{n-1}, creating a wide g=2 band) AND cut the tail piece
2^{n-1} into many small pieces (slow credit recovery). Uniform-random+interleave sampling MISSES this
and gives false min Phi=0. This is what flipped kappa=2 from 'validated' to refuted, round 10.
ALWAYS: the clean SALVAGE from the potential route is the clipped-D identity: for any tau,
int_tau^L phi(g) = D(S'_tau) - (SigmaF'-SigmaB'), S'_tau={p-tau: p>tau} (Lemma M on the clip). At tau=0
this IS MID-core. Casts the target as order-statistic transport Sigma_{F' even}v' <= Sigma_{B' odd}v'
+ tau|F'| -- the exact input a Hall/matching proof must supply. Compensation is value-weighted +
non-local (prefix fails 27%), so a debit->larger-credit MATCHING (aimo-0129), NOT a running scalar,
is the route -> pivot to ballot-matching slug, round 10.

ALWAYS: adversarially/exactly test surprising 'always-injective' numeric claims with structured-tie rational profiles before building on them (COUNT |R_{n+1}|=2^{n+1} was random-only 'true' but exact all-equal a_i=1/(n+1) valley profile gives |R|=2 — the outline's whole density substrate was dead; round 11).

## imo-2026-03 (ballot-matching), round 11
NEVER: attack MID-core with any STRUCTURED transport/Hall certificate — REFUTED R11 (adversarial n=3..6):
HALL-ENDPOINT local dyadic-scale interval-Hall fails 49%, value-dominating injection F_even->B_odd fails
50%, prefix (charge-earlier) fails 8.5%, suffix (charge-later) fails 30.4%. The credit repaying a top
debit is globally spread down to the BOTTOM scale (n=7 witness: single debit at value~63 must charge
credit at values 20..1). Only complete-bipartite adjacency is feasible <=> the target itself. The
matching MECHANISM collapses (round 11).
NEVER: rely on GAP-TERMINAL "walk ends net-negative S_m=|F|-|B|<0" for imo-2026-03 lower bound — FALSE.
S_m=+1 is the MOST common value and holds exactly in the TIGHT minimiser (B=uncut ladder |B|=n, F=n+1
interleaving fragments, D=1). No forced terminal descent, no defect-Hall deficiency budget (round 11).
NEVER: try induction-on-|F| by merging two F-fragments (keep D non-increasing to reach |F|=2 base) —
7.3% of instances have NO D-non-increasing valid merge (merge-two-smallest fails 22%) (round 11).
ALWAYS: after R10(scalar family dead)+R11(structured-matching family dead), the lower wall MID-core has
NO surviving structured lever. Next lower attack must be a genuinely NEW global mechanism: aggregate
ballot/cycle-lemma on the reachable word, or F-partition majorization vs the fixed ladder B — NOT a
scalar potential and NOT a structured matching (round 11).

## imo-2026-03 (breakpoint-vertex), round 12
NEVER: use ANY covering-radius / max-gap object for imo-2026-03 UPPER — GATE-REFUTED both one-cap (R10)
and two-cap (R12). The covering radius c_i=½·max-gap(R_i) contracts geometrically but SATURATES at ~3-5·u_n
and NEVER reaches u_n even with a_i<beta_n applied at every level; worst max-gap/u_n = 3.2/6.1/8.9/15.8/24.6
at n=3..7. The whole covering-radius family is dead (round 12).
ALWAYS: for imo-2026-03 UPPER the true target is the FIRST GAP mu_{n+1}=min{v>0:v in R_{n+1}}<=u_n (holds
0-fail worst 0.70, tight =u_n at dyadic boundary), which is INCOMPARABLE to the covering radius (dense near
0, sparse near a_1). Proven recursion mu_i=min(mu_{i-1},dist(a_i,R_{i-1})) => mu_{n+1}=min_i dist(a_i,R_{i-1}):
a global adaptive first-gap pigeonhole (some a_i approaches R_{i-1} within u_n), NOT a covering radius,
NOT a fixed-level bound (single-i dist(a_{n+1},R_n) fails a few %). Next attack: Abel/telescope on sorted
M_{n+1} pairing values whose DIFFERENCE is reachable (RL tree-realizability = the obstruction), round 12.
ALWAYS: T=∅ exclusion for imo-2026-03 UPPER is exact — nonempty subset T costs exactly n cuts (leader free
+ (|T|-1) MATCH + (n+1-|T|) DELETE via ESF-2); empty set costs n+1 (infeasible). So value 0=v(empty) is
geometrically in R but never a legal leftover; Reduction R-COV' always yields a nonempty-T value (round 12).

ALWAYS: on imo-2026-03 MID-core, D is the ALTERNATING sum v1-v2+v3-... of descending pieces, NOT
Σ_{odd}v_i — the sign bug gave min L=8 instead of 1 (round 12). D=Σ(-1)^{k+1}v_k = μ{N odd}.
NEVER: on imo-2026-03 lower wall, claim ONE-REC per-scale single-excursion is a binding polytope
facet — it is AUTOMATIC from group-sum=2^j + positivity (two frags >2^{j-1} sum >2^j), so any vertex
mechanism resting on "ONE-REC tightness forces spread" is unsupported (round 12).
ALWAYS: the LP-vertex reduction (min-at-vertex) for MID-core is rigorous but LOSS-FREE equivalent to
MID-core itself — a reframe, not a closure; cheap-kill n=3,4 gives min D=1 (no clumped vertex) but
general-n vertex bound stays open. D is NOT integral at vertices (kills integrality shortcut), round 12.

ALWAYS: when the target allows value 0 (even cancellation over a nonempty subset), the residual is `min over nonempty subsets` NOT `min positive reachable value` — using min-positive spuriously refutes a true claim (breakpoint-vertex imo-2026-03, round 13: min-positive "failed" 128/442 at n=3, min-nonempty-subset had 0 fails).
NEVER: propose a mass-telescope that charges n+1 per-piece "far" distances against total mass L when the threshold is u_n=1/(2^{n+1}-1): (n+1)u_n→0 and Σ dist(a_i,R_{i-1}) ≤ a_1(2-2^{-n})<2a_1<1 — the sum is bounded ABOVE, wrong direction, impossible (imo-2026-03 GAP-TELE, round 13).

ALWAYS: run the numeric gate over the EXACT stated domain AND on structured (near-extremal) families, not just random samples (round 14): imo-2026-03 upper-valley "worst ratio 0.75" was an under-sampling artifact — the exact family {2^n,...,4,3,2}/(2^{n+1}+1) gives ratio→1, so the valley residual is asymptotically tight, refuting any margin/crude-bound closing mechanism. Random search missed it (local maxima).
NEVER: trust a claimed "margin to spare" in a minimax residual without testing structured near-extremal families (round 14) — the tight point may sit just inside the domain via a small perturbation of the global extremal.

ALWAYS: on imo-2026-03 LOWER wall, before trusting an "LP-dual sparse Farkas certificate"
mechanism, remember the certificate-existence is (strong duality) LOSS-FREE EQUIVALENT to the
target min L_T>=1 — it is a reframing, not a reduction, unless a UNIFORM CLOSED-FORM provable
multiplier pattern exists. R14: it does not (dual varies by type; ±1-equality form proven
impossible at the n=4 box-interior witness via complementary slackness + binary-rep uniqueness of
Σ±2^k=1 forcing Σ y_g|g|=[m odd] which the ±1 choice violates). (round 14)
NEVER: assume "box-free vertex has <=1 odd block" for imo-2026-03 — FALSE, tight L_T=1 vertex
{6,6,4,4,4,4,2,1} has two odd singleton blocks {2},{1}, one not even value 1 (round 14).

## imo-2026-03 (gen-func-transform), round 15
NEVER: attack imo-2026-03 LOWER (MID-core) with a Z-transform / generating-function recursion
Z(z)=int z^g evaluated at z=-1 — GATE-REFUTED R15 (7th dead lower lever, the transform object).
The two-band split gives Z_n(-1)=TopBand + int_0^{L/2}(-1)^{N_F}(-1)^{g'}; the weight (-1)^{N_F}
flips inside the sub-instance domain whenever F has a fragment <L/2 (the OPEN |F|>=3 interior case),
and the deviation from a clean recursion is EXACTLY -2*mu(O_F cap O_B) = the certified dead SPLIT
cross-term. Decisive: fixed (F={8,5,3},F_B={4,4},Z_{n-1}(-1)=0) gives three distinct Z_4(-1) in
{-4,-2,0}. Evaluating at z=-1 re-imports the very term MID removed -> reframing not reduction.
ALWAYS: to refute a claimed IH-carrying recursion, fix the top-level data + the sub-value and search
(exact, budget-respecting) for a COLLISION: same (top-data, sub-value) -> different top-value proves
the recursion is not well-defined as a function. Faster and more decisive than trying to bound it
(imo-2026-03 gen-func gate, round 15).

## imo-2026-03 (breakpoint-vertex), round 15
ALWAYS: for imo-2026-03 UPPER, the certified target Φ is min over NONEMPTY subsets of the
descending-KK caterpillar (0 admissible via nonempty even cancellation), NOT min-positive of R_{n+1}
— {30,25,20,15,10}/100 has min-positive 1.55u4 (spurious refute) but Φ=0 via subset {30,25,20,15}
(round 15).
ALWAYS: the boundary layer of the valley (a1 near L/2, where VALLEY-TIGHT's family A^(n) lives) is
closed EXACTLY by Lemma WTC: largest-first differencing K=descKK(a1..a_m) <= |2a1-L|, proven by the
two-sided invariant a1-P_k <= v_k <= |a1-P_k| (P_k=a2+..+ak). Full profile is a nonempty subset so
Phi<=K<=|2a1-L|; for a1>=(L-un)/2 this is <=un. Tight (equality) on A^(n). Margin-free continuation
of certified whole-tail-peel across a1=L/2 (round 15).
NEVER: hope for a bounded (1-2 move) mechanism in the DEEP valley a1<(L-un)/2 — the deep minimiser
needs unbounded-order cancellation ({30,25,20,15,10}/100 needs a 4-element subset); numeric margin
~0.6-0.7 exists but no analytic bounded lever. Deep interior = the still-open R7 crux (round 15).

ALWAYS: for imo-2026-03 MID-core (mu{g odd}>=1), the clean loss-free reformulation is
D=1-2*int floor(g/2), so target = int_0^{2^{n-1}} floor(g/2) <= 0. Sub-case g<=1 everywhere
is then TRIVIALLY closed (floor(g/2)<=0 pointwise) and generalizes MID's 0<=g<=1. Also robust:
g(0+)=|F|-|B|<=1 always (budget: |B|>=n, |F|+|B|<=2n+1). Residual = {sup g>=2} only (round 16).
NEVER: for imo-2026-03 lower wall, pursue a PER-BAND or PREFIX (scale-local) counting inequality
int_{I_k} floor(g/2)<=0 -- both FAIL by exact witness (n=3: F={12/5,14/5,14/5},B={1,2,2,2} has top
band int floor(g/2)=+4/5, compensated only by band I_0=-1). Cancellation is irreducibly CROSS-BAND,
so any block-parity/band count collapses to global MID-core restated (round 16, G1 STOP confirmed).

## imo-2026-03 (scale-origin-layercake), round 17
NEVER: attack imo-2026-03 LOWER (★)=Σμ{g≥2i}≤Σμ{g≤1−2i} with a per-cell cap local to the ONE-REC
dyadic SCALE-OF-ORIGIN j — 10th dead lower lever. The unique structural B-tagging (super-level {g≥2i}
opened by a scale-j B-value → α_{i,j}; sub-level {g≤1−2i} closed by a scale-j B-value → β_{i,j}) is
loss-free (Σα=LHS, Σβ=RHS exact) but its scale-local aggregate Σ_iα_{i,j}≤Σ_iβ_{i,j} is FALSE ~50%
(exact Fraction n=4,5,6, deficit up to full 2^j, 113/122 i=1-failing witnesses fail). Any local
per-(i,j) cap summing to (★) implies that per-scale statement (sum over i) — so it is impossible.
The credit repaying a scale-j super-deficit is generated at OTHER scales; the aimo-0009 self-
referential same-scale a_i+b_i pairing cannot work here (excess and credit are at different scales).
ALWAYS: to kill a "loss-free tagging + local cap" lever fast, first check the tagging reproduces the
target exactly (Σα=LHS, Σβ=RHS), THEN gate the per-group aggregate (sum over the non-group index) —
if the aggregate fails, every local cap that sums to target is dead by the summation argument, no need
to search level-shifts (imo-2026-03 round 17).

## imo-2026-03 (breakpoint-vertex), round 17
NEVER: trust the "deep interior a1<(L-un)/2 is margin-tolerant (Phi/un~0.34-0.56)" premise for
imo-2026-03 UPPER — REFUTED exact R17: sup_{deep} Phi/un -> WTC boundary value (2^{n+1}-1)/(2^{n+1}+1)
-> 1 as a1 -> (L-un)/2 from below. The 0.34-0.56 margin only holds for a1<=L/2-un (c=1); the u_n/2-wide
sliver a1 in (L/2-un, L/2-un/2) that WTC leaves open has Phi/un->1, as tight as the boundary layer.
So NO margin-tolerant lever closes the whole deep interior; the sliver needs an EXACT argument.
NEVER: expect the full-tree second moment over 𝓡(A) (all binary differencing trees) to concentrate for
imo-2026-03 UPPER — DEAD R17 (8th mechanism), worst mean(V^2)/un^2 = 14.7/72/242 at n=3,4,5, GROWING
with n, worse than the fixed-order probes. Rare-needle kills every average.
NEVER: use the smoothing move "shift mass from smallest part up to a1" as Phi-nondecreasing for
imo-2026-03 UPPER — REFUTED R17, decreases Phi on ~80% of random deep profiles (family-specific
monotonicity on A^(n) is NOT general). SMOOTH-MONO as conjectured is false.
ALWAYS: for imo-2026-03 UPPER deep interior, the clean sharpening is WTC on T={a1}∪S:
Phi <= min_{S⊆tail}|a1-Σ_S|, so the bound follows from a single-target subset-sum un-density around a1
(likely = FGR/band-landing, don't double-certify). The crux is one sliver deeper than WTC (round 17).

## imo-2026-03 (breakpoint-vertex), round 18
NEVER: attack imo-2026-03 UPPER deep interior/sliver with a post-crossing / reflected-walk /
anchored-caterpillar contraction (w_k=|w_{k-1}-a_k| continued past the band-landing crossing) — GATE-REFUTED
R18 (9th dead upper mechanism, exact Fraction). min over ALL post-crossing stops minpost/u_n saturates
4.5/9.1/13.9/24.3 at n=3..6 (~2x per unit n = covering-radius signature). Root cause: the walk is anchored
at a1 (every prefix contains a1) but the true minimiser is a TAIL subset EXCLUDING a1 (size up to n), e.g.
A={1/3,13/40,13/40,1/120,1/120}: minpost=3/10=9.3u4 but Phi=0 via {13/40,13/40}. Any single anchored pass
is the dead covering-radius family in disguise.
ALWAYS: the imo-2026-03 UPPER deep residual is a restricted signed-subset-sum discrepancy EXISTENCE claim
(exists nonempty T with |Σ ε_i a_i|<=u_n, signs tree-realizable per Lemma RL) — the next lever must be a
Steinitz/vector-balancing/prefix-discrepancy bound over ALL tree-realizable signings, NOT any anchored walk,
covering radius, density/COUNT, per-subset WTC, single-target subset-sum density, 2nd moment, or margin. The
growing ~2^{n-1} ratio every gate shows is the Steinitz signature (round 18).

ALWAYS: for imo-2026-03 UPPER, compute mu_{n+1} via FGR dist-recursion mu_i=min(mu_{i-1},dist(a_i,R_{i-1})),
NEVER "min positive of accumulated set" — the naive filter silently drops exact-0 even-cancellations
(explorer landmine, confirmed round 19: (17,16,11,8,4) has min R=0 on {13/40,13/40}-type tail subset).
NEVER: for imo-2026-03 UPPER, attempt any single object over the reachable-value set R(A) (walk /
balanced full-partition / band-restart / covering radius) — all saturate at Theta(1)*u_n growing with n;
the true minimiser is an anchor-EXCLUDING tail subset, so full partitions and a1-anchored walks provably
miss it (9 dead mechanisms, round 19). Needs a global existence (Steinitz) argument or sliver perturbation.
