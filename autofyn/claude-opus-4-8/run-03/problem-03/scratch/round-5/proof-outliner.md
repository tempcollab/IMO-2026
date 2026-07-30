## imo-2026-03

Field this round breaks the shared wall on THREE distinct mechanisms plus a fresh far framing.
Both walls are shared (GAP L = L1 critical band + L2 top-shredded; GAP U = balanced a1<L/2).
Recorded dead ends to avoid: global concavity of V is FALSE; cascading-bisection fails on
near-uniform tails (4.7x at n=5); mass-threshold subset-cover non-exhaustive; dropping the SPLIT
cross term is fatally lossy in the critical band; single global non-adaptive threshold rule fails
on near-equal profiles; necklace-splitting/Hobby-Rice/Grundy inapplicable.

---

induction-peel: revise
Target: for every n, c(n)=2^n/(2^{n+1}-1); minimax D=u_n. (Attacks the LOWER wall, Case I+II.)
Technique: strong-induction refinement optimisation + a single UNIFIED gap-occupancy exchange
  lemma that closes L1 and L2 together (they are the SAME combinatorial object: interleave a free
  mass into the fixed geometric ladder C_{n-1}={2^{n-1},...,1}, differing only in below- vs
  above-gap insertion). Distinct from breakpoint-vertex (no finiteness theorem) and from
  smoothing (no continuous transport).
Skeleton:
  1. Import Lemmas R, M, PEEL, SPLIT, ONE; Case (a) top-uncut done (certified). — as in current file.
  2. Split (L*) D(S')<=f1-1 into TWO sub-cases by w:=2^n-f1:
     (i) TRIVIAL regime w<=2^{n-1}-1 (i.e. f1>=2^{n-1}+1): D(S')<=max(S')<=2^{n-1}<=f1-1 in ONE
         line — every piece of S' is <=2^{n-1} by Lemma ONE. Closes the vast majority for free.
     (ii) CRITICAL band w in (2^{n-1}-1, 2^{n-1}) (width exactly 1 in f1): the only nontrivial
         regime; the SPLIT cross term must be carried. — by the Gap-Interleaving Lemma below.
  3. Gap-Interleaving Lemma (UNIFIED, closes L1 critical band AND L2 Case II):
     interleaving a free mass into the ladder C_{n-1} with the available cuts is extremised by the
     canonical "one fragment per open gap (t_{i+1},t_i)" layout, whose D telescopes exactly. For
     L1 (fragments BELOW each t_i, mass w<2^{n-1}): D(S')<= (2^n-1)-w = f1-1. For L2 (fragments
     ABOVE each t_i, n+1 fragments straddling all n gaps): D >= 2^n-(2^n-1)=1. — by Lemma M
     (compute D of the merged sorted list t_1,g_1,t_2,g_2,... : odd ranks = g's, even = t's,
     D=Sum g_k - Sum t_i telescopes) + the exchange step in the key lemma.
  4. Assemble: Case (a) + Case I via PEEL+step 2/3 + Case II via step 3 => LB(n)>=1. Combine with
     §4A dominant-case upper bound (certified) => minimax D=u_n.
Key lemmas (claim + mechanism):
  - Split into trivial/critical — because f1-1>=2^{n-1} iff w<=2^{n-1}-1, so the crude
    max-bound D(S')<=2^{n-1} already beats f1-1 outside a band of width exactly 1.
  - Gap-Interleaving (one-per-gap is extremal) — because ANY fragment placed outside a canonical
    gap (t_{i+1},t_i), OR a second fragment in a gap already occupied, can be exchanged toward the
    one-per-gap layout with D moving in the safe direction (rearrangement/exchange on an adjacent
    fragment-vs-tail-value pair); the extremal D is then the exact telescoping Sum g_k - Sum t_i.
Open gaps: the EXCHANGE step in the Gap-Interleaving Lemma ("one more cut / one displaced fragment
  cannot overshoot the ceiling"). Per-cut |dD|<=2s_2 summed is TOO LOOSE (allows unbounded growth);
  needs a bespoke adjacent-pair exchange argument (standard olympiad move, not yet written).
Cases to cover: Case (a) top-uncut [done]; Case I trivial regime [one line]; Case I critical band
  [interleaving]; Case II top-shredded [interleaving, above-insertion]. All four are enumerated.
Watch out: do NOT drop the SPLIT cross term anywhere in the critical band (margin is exactly 0 at
  w->2^{n-1}). "Leave tail uncut is extremal" is TRUE only inside the band; outside it is false but
  harmless (huge slack) — keep the two-subcase split, do not seek one uniform bound.

---

breakpoint-vertex: new  (file: results/imo-2026-03/approaches/breakpoint-vertex.md)
Target: for every n, c(n)=2^n/(2^{n+1}-1); minimax D=u_n. (Fresh far framing; attacks BOTH walls.)
Technique: LP-vertex / piecewise-linearity finiteness. Prove Xiang has an optimal response in
  which EVERY cut is a tie (Lemma-P cancelling pair) or a self-bisection — never a generic interior
  split. Collapses the continuous minimax to a finite tie-pattern search; makes GAP L vacuous and
  finitizes GAP U. Not a potential (B), not an induction peel (A), not a transport (E).
Skeleton:
  1. Lemma PL1 (single-cut breakpoint): cutting length l into (s,l-s) with background frozen,
     g(s)=D is piecewise-linear, slope in {-2,0,+2}, min at a breakpoint (endpoint = wasted cut,
     or tie = Lemma-P pair / bisection). — by g'(s)=(-1)^{i+1}-(-1)^{j} with only s,l-s moving,
     d(l-s)/ds=-1 (exact, verified numerically by explorer-fresh: slopes exactly {-2,0,2}).
  2. Theorem VERT (joint): WLOG all <=n Xiang cuts are simultaneously ties/bisections. — settle
     cuts one at a time, outermost (largest fragment) first; PL1' gives no-increase per settle; a
     later smaller cut cannot un-tie an already-frozen larger tie.
  3. §4A: against dyadic C_n an optimal top cut is a tie (p2 = a tail value) or bisection
     (p1=p2=2^{n-1}); both are already-closed sub-cases, so the imperfect p1!=p2 case is VACUOUS.
     Finite check D>=1 on the tie/bisection family via the recursion.
  4. §4B: balanced a1<L/2 becomes a finite tie-pattern optimization; exhibit one pattern with
     D<=u_nL (pair near-equal pieces, bisect the odd one), bound the leftover rho via SPLIT.
Key lemmas (claim + mechanism):
  - PL1 slopes in {-2,0,2} — because within a fixed rank region only s and l-s move (anti-
    correlated), so dD/ds is a difference of two alternating-rank signs = an even integer in {-2,0,2}.
  - VERT (all cuts at breakpoints) — because min of a PL function is at a breakpoint (PL1'), and
    settling largest-fragment-first is stable: smaller later cuts introduce only smaller lengths
    that cannot cross a frozen larger tie.
Open gaps: GAP VERT — the joint statement (settling one cut does not un-settle earlier ties); the
  lexicographic outermost-first induction is proposed but NOT proved (this is the crux). Plus the
  §4A finite check and §4B leftover bound (both expected easy once VERT holds).
Cases to cover: tie vs bisection vs degenerate for each cut; §4A dyadic response family; §4B
  tie-patterns of a balanced multiset.
Watch out: the min-at-breakpoint direction is exactly what the LOWER bound needs (min over ALL
  responses = min over VERTEX responses, so checking vertices suffices to prove D>=u_n) AND what
  the upper bound needs (exhibit one good vertex) — state both usages. The rank structure shifting
  under settling is the real danger; do NOT hand-wave "reorder freely" — the final MULTISET is
  order-free but the settling induction is not, so prove the no-un-tie sub-claim explicitly.

---

smoothing-majorization: revise
Target: for every n, c(n)=2^n/(2^{n+1}-1); minimax D=u_n. (Attacks the UPPER wall, balanced a1<L/2.)
Technique: REPLACE the refuted global-concavity SMOOTH monotonicity with an even-multiplicity
  D-DICHOTOMY: extend the certified corrector Lemma U0 (m<=n => D=0) to the boundary m=n+1 by
  carrying Lemma SPLIT's cross term EXACTLY for the single unpaired leftover. Genuinely different
  D-tracking lever from breakpoint's finiteness and from the refuted mass/subset-cover.
Skeleton:
  1. Import Lemmas R, M, P, SPLIT, whole-tail-peel; promote Lemma U0 (m<=n => D=0) — certified in
     step via parity-measure. Upper bound nontrivial only for m=n+1 (full budget).
  2. Lemma D-DICHOTOMY: for balanced A (a1<L/2, m=n+1, budget n) EITHER
     (i) NEAR-UNIFORM regime: A admits a SIMULTANEOUS even-multiplicity pairing of all n+1 pieces
         via <=n MATCH cuts leaving ONE forced leftover rho, with rho<=u_nL — D from SPLIT's exact
         cross term, not a crude bound; OR
     (ii) LOCALLY-DOMINANT regime: some piece a_j dominates a natural sub-tail, so a single
         whole-tail-peel (certified, exact D=2a_j-subtail) closes the bound.
  3. Coverage: (i) and (ii) tile the a1<L/2 simplex; the transition boundary maps to the certified
     a1=L/2 case with D=0. Case-split variable = "how many pieces are within delta of the mean"
     (NOT a fixed a1 threshold).
  4. Assemble with §4A dominant case (certified) => UB(n): D<=u_nL for all A.
Key lemmas (claim + mechanism):
  - U0 extension to m=n+1 — because pairing n of the n+1 pieces by MATCH gives even multiplicity
    (Lemma P kills those), and the one leftover's contribution is the SPLIT cross term
    2 mu(O_X ∩ O_Y), computed EXACTLY rather than bounded, giving rho<=u_nL.
  - Regime exhaustion — because a profile with no even-pairing to a small leftover must have a
    piece separated from a near-equal cluster, i.e. a locally dominant a_j for whole-tail-peel.
Open gaps: (1) the exact leftover bound rho<=u_nL in regime (i); (2) proving (i)+(ii) are
  EXHAUSTIVE (the delta-cluster case split). Both open.
Cases to cover: near-uniform (even-pairing); locally-dominant (whole-tail-peel); boundary
  (a1=L/2, D=0, certified).
Watch out: cascading (sequential single-piece) bisection is REFUTED as a uniform rule (4.7x
  violation on the near-uniform 6-piece n=5 profile) — regime (i) must be SIMULTANEOUS even-pairing,
  not sequential peeling. Stress-test any candidate FIRST on that n=5 profile
  (0.2024,0.1965,0.1820,0.1789,0.1651,0.0750). Global concavity of V is FALSE — do NOT reinstate
  the old SMOOTH step; the piecewise-concavity KB tool is valid only inside a fixed sort chamber.

---

parity-measure-potential: advance
Target: for every n, c(n)=2^n/(2^{n+1}-1); minimax D=u_n. (Leader; keep alive with a DISTINCT
  lower-wall mechanism so the field does not starve to one line.)
Technique: global measure/parity-toggle calculus (Lemma M/T) — advance by (1) certifying Lemma U0
  as a shared lemma file, and (2) proving GAP L2 (Case II, all pieces <=2^{n-1} => D>=1) DIRECTLY
  via toggle calculus, a DIFFERENT derivation route than induction-peel's exchange argument for the
  same fact (two far-apart mechanisms on the lower wall = insurance against the single-gap trap).
Skeleton:
  1. Certify Lemma U0 (m<=n => D=0) as lemmas/even-multiplicity-corrector.md (currently only prose
     in two-box-balancing) — importable by smoothing-majorization and breakpoint-vertex.
  2. GAP L2 via measure: top 2^n shredded into fragments all <=2^{n-1}, tail a refinement of
     C_{n-1}. Compute D directly as mu{N(t) odd} using Lemma M on the merged sorted list; the
     above-gap interleaving telescopes to D>=1 (mirror of L1). — by Lemma M + toggle sets, no PEEL.
  3. Import the Gap-Interleaving Lemma (from induction-peel, once proven) for L1 and assemble the
     full lower bound; combine with the certified whole-tail-peel upper bound.
Key lemmas (claim + mechanism):
  - GAP L2 D>=1 via measure — because the merged sorted sequence has odd ranks = top fragments
    (each just above its paired tail value t_k) and even ranks = tail, so
    D = Sum g_k - Sum t_i = 2^n-(2^n-1)=1 exactly at the extremal interleaving, and any deviation
    only raises D (toggle calculus on adjacent atoms).
Open gaps: same exchange content as induction-peel's Gap-Interleaving (why one-per-gap is extremal)
  but derived via Lemma M/T instead of rearrangement — kept as a SECOND mechanism, not a duplicate.
Cases to cover: Case II only (this advance); L1 imported.
Watch out: do NOT re-derive L1 here by the refuted mass-cover; use only the measure identity.
  If the exchange content cannot be made rigorous via toggle calculus, this advance degrades to
  the U0 certification deliverable (still valuable, low-risk).

---

Suggested build set (reviewer decides): induction-peel (lower wall, unified interleaving),
breakpoint-vertex (fresh far framing, both walls), smoothing-majorization (upper wall, U0
extension). parity-measure-potential advance is optional/low-risk (U0 certification + L2 via
measure) — include if a fourth builder is available; it keeps the leader alive with a distinct
lower-wall mechanism.
