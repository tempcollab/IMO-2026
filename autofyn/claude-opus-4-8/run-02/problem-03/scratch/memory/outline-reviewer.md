# outline-reviewer role memory

ALWAYS: for game/minimax olympiad problems, brute-force the value on a grid divisible by the
conjectured denominator before ranking — a coarse grid (K=18 for a 1/7-denominator answer)
gave a wrong value 5/9 vs true 4/7 and would have looked like a refutation (round 1, imo-2026-03).
ALWAYS: independently confirm the shared spine lemma numerically (Lemma G "greedy=minimax" held
on 3000 random multisets) so you know a shared-lemma failure isn't a hidden single-gap trap (round 1).
NEVER: approve a "separable potential Φ=Σw(piece) is monotone in the odd-rank/pairing functional"
claim without flagging — pairing/ordering functionals are generically not controlled by a separable
per-piece sum; demand an early numeric existence gate (round 1, potential-certificate).

ALWAYS: numerically test a global CONVEXITY/CONCAVITY claim before approving it — the
concavity-lp approach claimed f(Liu partition)=min_Xiang D is concave on the simplex (so one
KKT certificate at dyadic proves global max); a midpoint test f(mid)>=avg failed 12/60 with
gaps up to 0.058, surviving 120 restarts. min-of-affine-PER-ORDER-TYPE is NOT min-of-GLOBAL-affine:
strategies available are p-dependent, so the envelope inequality g_S>=f fails off-region and
concavity breaks (round 2, imo-2026-03). RETHINK'd, not registered.
NEVER: trust a "spuriously low f(mid)" worry symmetric to the under-convergence warning —
under-convergence inflates min D (fake HIGH), so a surviving LOW f(mid) after heavy restarts is
a real concavity violation, not an artifact (round 2, imo-2026-03).

ALWAYS: when a twin proposes a CONCRETE deterministic schedule/strategy derived from a single
solver trace (e.g. dyadic-discrepancy-euclid's chained-pin rule from ONE k=3 trace), gate its build
on empirically confirming the canonical rule across many instances (rt_search.py, k=3,4) BEFORE the
builder invests — one trace is not a rule and the observed optimum used a non-obvious pivot order
(round 4, imo-2026-03).
ALWAYS: for "determine c(n)" bound+construction problems, upper and lower bounds are SEPARATE whole
sub-theorems (different objects: adversary strategy vs construction), so slugs split by bound-direction
are NOT the single-gap trap — each owns one direction end-to-end + shared spine (round 4, imo-2026-03).

ALWAYS: when a slug relies on a "pigeonhole gives a small gap" base, compute the constant vs the
target explicitly before approving — for imo-2026-03 GAP-U euclid, the one-shot gap c(k)Σ/(2k) beats
u_kΣ only for k≤2 (ratio 2^{k-1}/k grows past 1 at k=3), so the slug actually lives on the ITERATED
descent within the op budget, not the one-shot gap (round 6).
NEVER: rubber-stamp "two distinct mechanisms on one residual" as diverse without noting they share a
common TARGET INEQUALITY — if that inequality is the wall both die together; approve for one round but
tell the orchestrator to escalate to a different framing if both stall (round 6, imo-2026-03 both walls).

ALWAYS: when the top-Elo slugs are PARKED (their milestone, e.g. the upper bound, is done and must
not be rebuilt), state explicitly that the build set is the strongest LIVE slugs on the open wall,
not the top-Elo — Elo reflects proven achievement, build-set reflects who can still move the wall
(round 8, imo-2026-03: dyadic-discrepancy 1656 parked, built the GAP-L trio instead).
ALWAYS: brute the self-contained restatement of the residual over ALL small configs before ranking
its approaches — E(F)<=2^n-1 gave 0 violations & tight maxE at n=2,3,4, confirming the wall is a
missing MECHANISM not a false claim, so sharing that target across slugs is OK if it's proven-true
(round 8, imo-2026-03).

ALWAYS: when an approach claims "piecewise-linear min at an INTEGRAL vertex via total-unimodularity"
then applies a parity/integrality argument at that vertex, ENUMERATE the cell minima by LP first —
for imo-2026-03 vertex-integrality-parity the minimizing vertices were FRACTIONAL (smallest dyadic
group splits into a tied {1/2,1/2} pair) and per-cell LP min VALUES were non-integer (1.667, 4.333),
so both TU and the "some integral point achieves the min value" fallback were FALSE; the parity core
(integer multiset + odd total => D~ odd => >=1) is valid but only fires at integer configs, so the
real crux is the unstated integer-minimizer reduction, not the vertex claim (round 9). Partition-rows
stacked on order/difference-rows are generically NOT TU when group sums are odd.
NEVER: accept a per-cell "min value is an integer, hence odd, hence >=1" rescue without testing —
LP minima over non-optimal order cells are routinely fractional; only the GLOBAL min lands on an
integer config, and proving THAT is the hard part (round 9, imo-2026-03).

ALWAYS: distinguish "two mechanisms share a REDUCTION TARGET" (e.g. imo-2026-03 GAP-IMR: both
route to an integer minimizer then apply the certified Parity Lemma) from the single-gap trap —
it is an APPROVED branch (copy_approach) only when the two attack DIFFERENT halves of the same
obstruction (within-scale vs cross-scale mass transfer) AND a THIRD approach reaches the goal
without that target at all (peel induction proves the real-valued bound directly). If all the
target-sharers stall, tell the orchestrator NOT to add a 4th variant of the same target — seed
the reserved far framing that avoids the shared finishing device entirely (round 10).
ALWAYS: verify "parity/exchange through peel" proposals are the EXCHANGE-tool use (peel identity
as cross-scale mass-transfer FOR the integrality reduction), not the CIRCULAR use (Parity Lemma
as the peel-induction finisher) — the cross explorer proved the latter presupposes GAP-IMR on the
residual; the former is a genuinely new, non-circular use of the same certified lemma (round 10).

ALWAYS: when the outliner emits a NEW slug in the build set, check the approach file actually
exists (results/<id>/approaches/<slug>.md) — round 11 the outliner named allocation-vertex-corner
in the build set but never wrote its file; I seeded it from the outliner's plan before registering
so the builder had a file to own (imo-2026-03, round 11).
ALWAYS: distinguish "two whole attempts sharing a proven-TRUE gap" (stall risk only) from the fatal
single-gap trap (shared FALSE gap → both die) — round 11 both live GAP-L approaches shared the base
case b=0 ladder inequality AND a monotone-in-b claim; I brute-verified the base case true (min=1,
tie, n<=6, integer+fractional) so approved both but flagged the field has collapsed to one wall and
told the orchestrator to seed a far framing if BOTH stall (imo-2026-03, round 11).

ALWAYS: when an outliner proposes a STRICTLY STRONGER surrogate (weak majorization BO≻_w RE for
the target (★) ΣBO≥ΣRE), the real over-shoot test is not "does the surrogate hold" but "is there a
config where the TARGET holds yet the surrogate FAILS" — I ran 960k fractional configs n≤9 both
tie-breaks, 0 such gaps, confirming the surrogate is safe; approve strictly-stronger surrogates only
after this specific check + confirm a sibling targets the exact (weaker) claim as fallback (round 12).
ALWAYS: distinguish a co-varying DEFORMATION monovariant (concrete move: merge one F'-cut, hand freed
cut to π_0, budget conserved) from the DEAD GAP-IMR "max I_n over a cell = vertex" min-over-cell claim
— they look similar but the deformation is route (a) (live), the min-over-cell is route (b) (=GAP-IMR,
dead); the explorer's own report separated them, so I did not cut coupled-cut-descent (round 12).

ALWAYS: when an approach reduces "prove Q>=P" to "prove Q>=S" via a certified one-sided
  bound P<=S, VERIFY the strengthened target Q>=S is itself TRUE before approving — a lossy
  upper bound (S generically >> P) turns a true target into a false one. qlayer-charge-induction
  (round 13) proposed proving (NEG) Q>=S_pi off certified (POS) P<=S_pi; Q>=S_pi is false
  50-77% of configs and false at EVERY tie config (n=1 pi0={1,1},F'={1}: Q=0,S_pi=1). RETHINK.
NEVER: assume a base-slice-only approach advances the whole problem — for imo-2026-03 the b-lift
  (GAP-P1'-b) is a SEPARATE needed gap; three routes to (★) can all be sound yet leave the b-lift
  uncovered (round 13: coupled-cut dead, WM-IH refuted, qlayer doomed => b-lift had no live route).
  Flag uncovered shared gaps to the orchestrator.

ALWAYS: recognize the banned (NEG) Q>=S_pi bound even when it is re-dressed as a "NEW recursive
  intrinsic Q-bound" — round 14 peel-scale-rank-induction's ADVANCE outline reduced I_n=P-Q<=0 to
  "suffices Q>=Sum_{k<=K0} y_{2k}", which IS S_pi (the RHS of certified positive-layer-localization);
  it is FALSE at every tie (n=4 b=2 tie: Q=3 < S_pi=8), so no recursion can prove it. When a slug
  reduces Q>=P to Q>=(RHS of a certified one-sided P<=RHS bound), the target is the banned/lossy one
  regardless of the proposed proof mechanism -> RETHINK (imo-2026-03, round 14).

ALWAYS: when a b-lift/merge outline claims cutting a blue rung theta into r parts only shifts
  merge-ranks "local to the window (p_1,p_r)", CHECK it numerically — it is FALSE: removing theta
  and inserting r fragments shifts EVERY element below p_r by r-1 (verified n=8 config). The exact
  rank-parity correction is GLOBAL below p_r, not local. Flag as CHANGES REQUESTED (correction is
  still exact, just not local) not RETHINK (imo-2026-03, round 15).
NEVER: put a slug in the build set whose only closer is a "global matching/injection exists" with no
  stated mechanism, even if it is the Elo leader/machinery home — it is an unverified hand-off onto
  the bare shared wall; park it live, build only slugs with a concrete route (imo-2026-03, round 15).

ALWAYS: when a leaf-closer lemma is stated as an inequality on the SAME identity used to define the
  target (imo-2026-03 R16: (TEETH) I_S <= Δ(R,F'')+½θ+½D̃(ρ₁) is, by correction (C), literally
  Δ(R,F')>=0), flag it is the target restated, NOT an assumable lemma — approve the build only if
  (i) a DIFFERENT sub-case is independently closed (real bankable progress) AND (ii) the closer is a
  concrete non-scalar mechanism, not a bare "matching/injection exists" (round 16).
ALWAYS: an inductive lower bound (L̂B_{m−1}) is legitimately usable on a leaf even if only
  (P̂/Q̂_{m−1}) are the named IH, PROVIDED it follows unconditionally from them (here via the certified
  Lipschitz collapse) — verify the derivation chain, then check ALL its hypotheses hold on the leaf
  (budget a₀+b''<=m−1 comes from a₁>=1 spending a unit); confirmed 0-fail/31k before advancing (r16).

ALWAYS: when a b-lift/endpoint reduction claims "no red = θ ⟹ D̃ has slack", test WHETHER θ can be a
BLUE part (uncut top rung) not just a red — the literal claim was FALSE (endpoint config R sum 2^m,
F'={4,2,1} uncut, no RED=θ but blue θ, D̃=1); it only holds restricted to the cut-top-rung endpoint.
Route uncut-top-rung via the Case I induction, not the θ-red argument (round 17, imo-2026-03).
ALWAYS: check the trivial-band reduction (Δ≥0 ⟺ D̃ ≥ ΣR−2^m+1) BEFORE trusting a prior round's
"hard residual" label — R16 spent effort on a ΣR>θ TEETH charge that (S1) shows is trivial (RHS≤0,
D̃≥0) for all ΣR≤2^m−1; the real hard slice was only the endpoint ΣR=2^m (round 17, imo-2026-03).
