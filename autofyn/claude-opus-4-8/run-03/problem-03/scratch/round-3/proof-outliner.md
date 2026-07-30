## imo-2026-03

Field this round: 2 lower-bound attacks kept far apart (exact-identity vs surrogate), 2
upper-bound attacks kept far apart (subset-cover vs smoothing). Answer fixed: c(n)=2^n/(2^{n+1}-1),
minimax D=u_n=1/(2^{n+1}-1). Shared reduction (Lemmas R/M/T/P) and Lemma U0 are certified/imported.

---

induction-peel: revise (GAP L re-planned; GAP U unchanged, secondary)
Target: for every n, largest c Liu guarantees is c(n)=2^n/(2^{n+1}-1) (whole claim, both bounds).
Technique: strong induction on n via the cancelling-pair peel, now with an EXACT dominant-cut
  recursion for the lower bound (replaces the informal shadow-coupling map).
Skeleton (GAP L, the revised part):
  1. Budget-monotonicity lemma: L(C,b)=min_{<=b cuts}D(C) is non-increasing in b (extra cuts
     wasted as no-ops) — by restriction of strategy set. WLOG Xiang spends exactly ONE cut on the
     top piece a_1 before touching the tail.
  2. Exact dominant-cut identity: with p strictly largest over rest R, cutting p->(p1,p2) gives
     D_new = D_C - 2 mu([0,p2) cap E_R), E_R={t:N_R(t) even} — by Lemma T toggle set
     E=[0,p2)u[p1,p) plus dominance p>max R (parity on [0,max R) is exactly E_R).
  3. After the single top cut, R = uncut dyadic-(n-1) tail, so E_R/O_R are explicit alternating
     bands and mu(E_R cap [0,p2)) is explicit piecewise-linear in p2. Post-cut D = u_nL - (explicit).
  4. Propagate the remaining <=n-1 cuts either (a) by re-applying identity (2) at each cut on the
     current global max (exact branching recursion), or (b) show residual dominates a genuine
     order-(n-1) dyadic instance and invoke LB(n-1) after absorbing the cross term 2mu(O_R cap[0,p2)).
     Key checkable inequality: post-cut value + LB(n-1) contribution >= u_nL for all p2 in (0,a1/2].
Key lemmas (claim + mechanism):
  - Budget-monotone L(C,b) non-increasing in b — because a b-cut strategy is a b'-cut strategy
    (b'>=b) with wasted cuts; strategy set only grows. PROMOTE lemmas/budget-monotone.md.
  - Exact dominant-cut identity D_new=D_C-2mu(E_R cap[0,p2)) — because the only region a top cut
    can flip to even is R's already-even set E_R, capped at measure 2p2 ("cutting a scale costs
    that scale" as an equality). Verified numerically (35 trials n=2..4) + symbolically (sympy).
    PROMOTE lemmas/dominant-cut-identity.md.
Open gaps: GAP L step 4 (the exact-recursion propagation / cross-term inequality — builder fills).
  GAP U (balanced upper case) still open in this approach but NOT the focus this round.
Cases to cover: p_1 in [2^{n-1}, 2^n) (imperfect top cut, incl. near-bisection p_1->2^{n-1}+);
  perfect bisection already closed; Case A already closed.
Watch out for: the cross term 2mu(O_R cap[0,p2)) has the WRONG sign to drop — must be carried
  exactly, not bounded away; the near-bisection limit p_1->2^{n-1}+ is where the margin ->0, so
  the inequality in step 4 must be tight-safe there.

---

smoothing-majorization: new
Target: for every n, c(n)=2^n/(2^{n+1}-1) (whole claim). New file
  results/imo-2026-03/approaches/smoothing-majorization.md.
Technique: exchange/smoothing (majorization) — prove the minimax value V(A)=min_Xiang D is
  maximized at the dyadic profile, so V(A)<=u_n for ALL A in one shot. NO subset enumeration.
  Genuinely different framing from the subset-cover wall shared by the other three approaches.
Skeleton:
  1. Lemma U0 reduces upper bound to full-budget simplex Delta (m=n+1). — certified.
  2. V is u.s.c. on compact Delta, attains a max A* — by maximum-theorem continuity (Lemma M).
  3. (SMOOTH) a dyadic-ward exchange step does not decrease V: V(A')>=V(A) — by pulling back
     Xiang's optimal response tau*(A') to a legal response against A via Lemma T toggle algebra,
     odd-set-measure change <=0 in the dyadic-ward direction.
  4. Iterate: any A smooths to D_n (or to a finite extremal family), V(A)<=V(D_n)=u_n.
  5. Finite endgame (aimo-0146): if only finitely many extremal candidates survive, hand-check
     each has V<=u_n (for n=2 the survivor set is the single point D_2).
Key lemmas (claim + mechanism):
  - (SMOOTH) exchange toward the 2:1 dyadic ratio does not decrease V — because D is a fixed
    alternating-weight sum of the sorted final multiset (the aimo-0146 shape), so mass wants the
    high-coefficient positions and the tail drains; the pullback of Xiang's optimal tree keeps the
    move legal. Crux aimo-0146 (smooth-then-enumerate) and aimo-0560 (surrogate/extremal transfer).
  - V(D_n)=u_n — certified (bisect-top chain upper + Case A lower).
Open gaps: GAP U-SM (prove SMOOTH survives the min-over-Xiang layer — the whole crux). GAP L
  imported from the lower-bound approaches when certified.
Cases to cover: dominant a_1>=1/2 (already easy elsewhere) folds into the same smoothing; the hard
  region is balanced a_1<1/2 sub-threshold — exactly where subset-cover stalls, here handled
  uniformly. Finite endgame list per n.
Watch out for: the minimax layer is the real difficulty absent from aimo-0146 (weights come from
  Xiang's optimal-response sort, which itself shifts under the exchange) — do NOT assume tau* is
  stable; prove the pullback is legal and D-nondecreasing. Prove the inequality V<=V(D_n), not the
  (numerically-true but unneeded) uniqueness of the maximizer.

---

parity-measure-potential: advance (leader elo~1582; push GAP U subset-cover)
Target: c(n)=2^n/(2^{n+1}-1), both bounds, via the measure identity D=mu{N(t) odd}.
Technique: strong induction UB(k) with the multi-pair peel threshold; subset-cover feasibility.
Skeleton (advance the open GAP U): prove the disjunction is exhaustive — every sorted full-budget
  profile admits Branch (0) (a_1>=c(k)L) OR a multi-pair peel (j,T) with Sigma_T in [L theta_j, a_1],
  theta_j=u_k 2^{k-j}(2^j-1). NEW lever for the builder (from explorer, not yet in file):
  **GAP U is self-similar/closed** — a j-pair peel of a full-budget profile (n+1 pieces, budget n)
  lands in ANOTHER full-budget profile ((n+1-j) pieces, budget (n-j), and (n+1-j)=(n-j)+1 exactly),
  so the induction never leaves the full-budget family; Lemma U0 handles the boundary once. Use the
  greedy-fill j* (fill the tail prefix until it would exceed a_1) and check r against theta_{j*}.
Key lemmas (claim + mechanism):
  - Subset-cover feasibility — because theta_j increases in j while Sigma_T<=a_1 caps the take;
    the greedy-fill j* is the sum-maximizing size-j choice under the a_1 cap. NOT yet reduced to a
    clean pigeonhole — this is the crux to close.
Open gaps: GAP U (subset-cover feasibility, balanced sub-threshold regime, first at k=2). Also
  GAP L1 (a=1: prove D(S_L)<=f_1-1) and GAP L2 (a=0 shredded top) — its lower-bound gaps, which
  the exact dominant-cut identity in induction-peel may also settle (LB-id = p2->0 case).
Cases to cover: a_1>=c(k)L (Branch 0, done); balanced a_1<c(k)L AND a_2<c(k)L/2 (open crux);
  all-equal is easy (D=0), not the hard case.
Watch out for: the greedy-fill j* clearing theta_{j*} has only been spot-checked, never proved
  profile-independently — that is exactly the gap; do not present a spot-check as a proof.

---

two-box-balancing: revise (GAP L via surrogate-opponent domination; distinct lower-bound lever)
Target: c(n)=2^n/(2^{n+1}-1), both bounds, in the |O|-|E| two-box framing.
Technique: strong induction; lower bound Case B via a STRONGER surrogate Xiang (crux aimo-0560) —
  a mechanism deliberately distinct from induction-peel's exact-identity route, so the two
  lower-bound approaches stay far apart and do not die on one wall together.
Skeleton (revised GAP L):
  1. Grant surrogate Xiang the free power to re-merge the fragment pair {p_1,p_2} back to 2^n at
     no cut cost, then continue with his real <=n-1 cuts.
  2. Domination: min_{real} D >= min_{surrogate} D (surrogate strictly more dangerous). Show
     re-merge-then-recut never raises the achievable minimum (via Lemma T), so surrogate-optimal
     play WLOG re-merges to clean 2^n, landing on D_n with <=n-1 cuts.
  3. By budget-monotonicity (import lemmas/budget-monotone.md) + IH L(n-1)>=1, surrogate value >=1,
     hence real value >=1 = u_n (integer units).
Key lemmas (claim + mechanism):
  - Surrogate domination — because every real continuation is available to the surrogate (he can
    decline the re-merge), so min over the larger strategy set is <= ; the useful direction needs
    re-merge to be D-nonincreasing, verified via Lemma T net-toggle.
  - Budget-monotone (shared with induction-peel).
Open gaps: GAP L (SL for imperfect top cuts) — the domination inequality's direction (surrogate
  <= real in D) and the re-merge D-nonincreasing claim.
Cases to cover: imperfect top cut p_1 != p_2 (SL Case A and perfect bisection already closed).
Watch out for: the inequality MUST point surrogate<=real; if re-merge could raise D the argument
  inverts — builder must verify via Lemma T that re-merge-then-recut never increases the minimum.
  Also GAP U (subset-match) remains open here but is not the focus (covered by the two upper attacks).

---

Field summary for the reviewer: 4 approaches, two per wall, kept far apart by mechanism.
- Lower (GAP L): induction-peel (exact dominant-cut toggle identity + budget-monotone, revise) and
  two-box-balancing (surrogate-opponent domination, revise) — different levers, not variations.
- Upper (GAP U): parity-measure-potential (subset-cover feasibility + self-similar-closure, advance)
  and smoothing-majorization (dyadic-uniquely-maximizes-V exchange/smoothing, new) — different framings.
New promotable lemmas proposed this round: budget-monotone, dominant-cut-identity.
