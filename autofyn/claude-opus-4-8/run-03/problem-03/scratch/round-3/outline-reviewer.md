# Outline review — imo-2026-03, round 3

Answer treated as CONFIRMED c(n)=2^n/(2^{n+1}-1), minimax D=u_n=1/(2^{n+1}-1). Certified lemmas
R/M/T/P and U0 taken as given. Field: 4 rival approaches, two per shared wall (GAP L lower, GAP U
upper), plus two dormant ones (lp-dual-weight, explicit-pairing-strategy) in the population.

Numeric checks I ran this round (n=2, grid minimax solver, measure identity for D):
- V(dyadic 4/7,2/7,1/7) = 1/7 exactly; every other tested profile strictly below. So the smoothing
  TARGET (MAX): dyadic uniquely maximizes V — is TRUE.
- V is NOT monotone along straight balanced->dyadic interpolation: interior valleys, e.g.
  (0.34,0.33,0.33)->dyadic gives V path ...0.0714, 0.0423, 0.004, 0.0503, 0.0966, 0.143 (dips then
  recovers); (0.45,0.30,0.25)->dyadic gives 0.0593, 0.0514, 0.0271, 0.0124, 0.0214,... The V-landscape
  has genuine interior minima. This directly bears on the smoothing mechanism (below).

---

## induction-peel — APPROVE (build; advance GAP L)

Verdict: sound, strongest lower-bound lever. The revised GAP L closure rests on two named tools each
with a stated mechanism:
- Budget-monotonicity (L(C,b) non-increasing in b) — mechanism given (strategy-set inclusion, extra
  cuts wasted as no-ops). Valid. Reduces to a single top cut cleanly.
- Exact dominant-cut identity D_new = D_C - 2 mu(E_R cap [0,p2)) — mechanism spelled out via Lemma T
  toggle set plus dominance p>max R, symbolically verified. This is a real equality, not a bound, so
  step-4 propagation becomes algebra in explicit dyadic bands. That is the right kind of engine.

Issues to close while building (CHANGES-flavored, not fatal):
- Step 4 is a genuine gap, not yet done: the "post-cut value + LB(n-1) contribution >= u_nL for all
  p2 in (0,a1/2]" inequality must be carried EXACTLY — the cross term 2mu(O_R cap [0,p2)) has the
  wrong sign to drop (the outline itself flags this). Do not let the builder bound it away.
- Tight-safe check at the near-bisection limit p2 -> a1/2 (p1 -> 2^{n-1}+) where the margin -> 0 is
  mandatory; that is exactly where a loose inequality would fail. Require the builder to evaluate the
  closing inequality symbolically at p1 = 2^{n-1} (equality boundary), not just at sample points.
- Route (a) exact branching recursion vs route (b) dominance+LB(n-1): the builder should commit to one
  and verify it end to end; (a) is cleaner given the identity is exact, prefer it.

No circularity: LB(n-1) is a strictly smaller instance. Case coverage (a)/(b) is disjoint and
exhaustive; the p2->0 degenerate is the LB-id case shared with parity-measure. Build.

## parity-measure-potential — APPROVE (build; advance GAP U)

Verdict: sound, standing leader; the concrete new lever (GAP U self-similar closure: a j-pair peel of
a full-budget (n+1)-piece / budget-n profile lands in another full-budget ((n+1-j)-piece / budget-(n-j))
profile, and (n+1-j)=(n-j)+1 holds) is correct arithmetic and keeps the induction inside the
full-budget family — a real structural gain. The a=1 identity D(S)=f1-D(S_L) is proven and clean.

Issues to close while building:
- The crux GAP U (subset-cover feasibility) is still the disjunction "Branch(0) a1>=c(k)L OR some
  (j,T) with L theta_j <= Sigma_T <= a1." The greedy-fill j* clearing theta_{j*} has only been
  spot-checked. Do NOT present a spot-check as a proof (per role memory). The builder must prove
  greedy-fill j* meets theta_{j*} PROFILE-INDEPENDENTLY, first at k=2 on the balanced sub-threshold
  regime (a1<c(k)L AND a2<c(k)L/2, e.g. (0.5,0.28,0.22)).
- Lower gaps L1 (D(S_L)<=f1-1) and L2 (a=0 shredded top telescope) remain in this file; they are
  secondary this round (the lower wall is owned by induction-peel). The builder may import
  induction-peel's exact dominant-cut identity to settle L1 (= p2->0 case) rather than re-derive.
- Self-similar closure handles the interior of the induction; verify the Lemma U0 boundary is invoked
  exactly once (m<=n branch) so the recursion terminates.

No circular step; UB(k-j) is a strictly smaller instance. Build.

## two-box-balancing — CHANGES REQUESTED (hold from build this round)

Verdict: technique sound (surrogate-opponent domination, crux aimo-0560) and it is a genuinely
distinct lower lever from induction-peel — good for diversity. Lemma U0 is fully proven and valuable.
But two concerns keep it out of this round's build set:
- The load-bearing claim is a DOMINATION DIRECTION that the outline itself flags as invertible: it
  needs surrogate value <= real value in D, i.e. "re-merge {p1,p2} back to 2^n then recut can only
  LOWER the achievable minimum." The mechanism ("verify via Lemma T net-toggle") is named but not
  established, and if re-merge can raise D the whole argument inverts. This is exactly the kind of
  unverified hand-off to push back on. It must be proven (not asserted) via Lemma T before this lever
  is trusted.
- On the same lower wall, induction-peel's exact identity is more concrete and already symbolically
  verified; running both lower levers this round is redundant. Advance induction-peel first; if it
  stalls at step 4, two-box's surrogate route is the natural next-round fallback.

Not fatal — keep it live in the population. Do not build this round.

## smoothing-majorization (NEW) — CHANGES REQUESTED (register; hold from build this round)

Verdict: genuinely different upper-bound framing (the only non-subset-cover attack on GAP U), and its
TARGET (MAX) is numerically TRUE (my check: V(dyadic)=1/7, unique global max). Registered at cold-start.
But the core mechanism (SMOOTH) is the entire proof and, as written, is refuted in its naive form:

- (SMOOTH) claims a "dyadic-ward exchange step does not decrease V." My numerics show V has INTERIOR
  VALLEYS along natural balanced->dyadic paths (V dips from ~0.07 to ~0.004 before recovering to 0.143).
  So a monotone "move toward dyadic and V never drops" argument is false for the obvious exchange
  directions. The min-over-Xiang layer (which the outline correctly flags as the real difficulty
  absent from aimo-0146) is precisely what creates these valleys: tau* re-sorts under the perturbation.
- The outline names the mechanism (pull back tau*(A') to a legal response against A via Lemma T,
  odd-set-measure change <=0) but does not exhibit a SPECIFIC exchange direction along which the
  measure change is provably <=0. Without that, iterating "toward dyadic" is not well-defined and the
  numerics say the generic direction fails. This is an unverified hand-off on the whole crux.
- The finite-endgame fallback (2.4) is honest but, if invoked, collapses back to enumerating extremal
  survivors — i.e. essentially the subset-cover casework it claims to avoid. So the fallback does not
  by itself deliver the promised "one-shot, no enumeration" advantage.

What to change before this is worth a builder: identify a CONCRETE exchange/majorization direction
(likely a Schur-convexity argument on the FIXED alternating-weight functional evaluated at Xiang's
STRUCTURED optimal response, not a straight-line move) and prove the pullback's measure change is <=0
along THAT direction, handling the interior valleys — OR reformulate as "V is Schur-convex-ish so its
max is at the majorization-extreme point" with the tau*-instability addressed. Because (MAX) is true,
the framing is worth keeping alive; but building it this round with the refuted naive exchange would
waste a builder. Hold; hand back to the outliner to pin the exchange direction next round.

## Field diversity note (for the orchestrator)

- LOWER wall (GAP L): induction-peel (exact toggle identity) and two-box (surrogate domination) are
  genuinely different levers — good. Advancing induction-peel this round.
- UPPER wall (GAP U): parity-measure (subset-cover) is the only upper attack being built this round.
  smoothing was seeded as the diverse non-subset-cover upper framing but its mechanism is not yet
  viable (interior valleys). The upper wall is therefore still effectively single-framing in the build
  set. If parity-measure's subset-cover feasibility stalls again next round, the orchestrator should
  push the outliner to make smoothing's exchange direction concrete (or seed a third upper framing),
  not add another subset-cover bookkeeping variant.

build set: induction-peel, parity-measure-potential
