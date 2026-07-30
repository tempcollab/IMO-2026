## imo-2026-03 — LENS: UPPER wall, Steinitz / 1-D vector-balancing / prefix-discrepancy existence route

### Distinct openings

1. **Two-step bridge (the route the dispatch asks me to scout).** Certified reduction R-COV'
   needs only `μ_{n+1} ≤ u_nL`, where `μ_{n+1}` is the min POSITIVE value of the caterpillar-only
   reachable set `R_{n+1}` (FGR). The bridge idea: (a) prove an easy Steinitz/discrepancy bound on
   the much bigger, easier-to-search family `R(A)` = ALL tree-realizable signed subset sums (Lemma
   RL); (b) show `min R(A)` is *attained* (or nearly attained) by a caterpillar-realizable value —
   i.e. `μ_{n+1} = min R_{n+1} = min R(A)` (or `≤ min R(A) + o(u_n)`). **I tested step (b) directly
   (exact `Fraction`, n=4) and it is FALSE as an equality in general** — see Small-case notes below.
   This is new information this round: the "bound the easy big object then transfer via
   completeness" bridge cannot close with an exact-equality lemma; at best it could survive as an
   *inequality-with-slack* (`μ_{n+1} ≤ min R(A) + gap`, `gap` provably `o(u_n)` on the hard/sliver
   profiles specifically) — unverified, and my random-integer test is the wrong regime to trust
   either way (see caveat below).

2. **Direct existence bound on `R(A)` (skip the bridge, attack `min R(A) ≤ u_nL` for its own
   sake).** `R(A)` is a genuinely richer object than `R_{n+1}` (allows arbitrary binary
   differencing-tree topologies over any nonempty subset, not just the linear/caterpillar chain
   in global descending order). If a Steinitz/vector-balancing argument gives `min R(A) ≤ u_nL`
   cheaply, that is *not* by itself useful for `R-COV'` (which needs the caterpillar-restricted
   object) UNLESS opening (1)'s bridge is repaired — so this opening is subordinate to (1), not
   independent, but worth scouting because it isolates exactly how hard the "easy" half of the
   bridge really is.

3. **Reject the bridge; attack `μ_{n+1} ≤ u_nL` directly, respecting the a₁-exclusion lesson from
   R18.** The 9th-dead-mechanism diagnosis (R18) is that *any single a₁-anchored pass* cannot see
   tail-only minimizers. But `μ_{n+1}` as defined by FGR is *already* the min over ALL subsets
   (via the skip/include walk), not a single anchored pass — the walk's SET `R_{n+1}` already
   contains every caterpillar value, including tail-only ones (skip a₁ at step 1, start the walk
   at a₂). What died in R18 was a specific *stopping-rule/contraction-constant* operationalization
   of a single trajectory (the "post-crossing reflected residual", i.e. only PREFIX subsets
   `{a_1,...,a_k}`), not the full `R_{n+1}` object. So a live opening is: prove `μ_{n+1}≤u_nL`
   directly as a genuine pigeonhole/counting/induction fact about the *whole* caterpillar-walk set
   `R_{n+1}` (size `2^{n+1}` as a multiset, MD2), not routed through the harder-to-characterize
   `R(A)`. This sidesteps needing completeness at all — but it is exactly the "first-gap
   pigeonhole" that has been open (and repeatedly refuted in every operationalization) since R7.

4. **Localize to just the sliver, separately from the strictly-deep region.** The sliver
   `a₁∈(L/2−u_n, L/2−u_n/2)` is only `u_n/2` wide (R17/R18). A bespoke, much more local
   perturbative argument around the WTC boundary (rather than a global existence bound covering
   the whole deep interior) may be more tractable: expand `Φ` as a function of `a₁` near the
   boundary and show the WTC value's "excess" over `u_nL` there can always be absorbed by ONE
   additional matched pair drawn from `a₂,a₃` (not a general `S`), since the sliver's excess
   `|2a₁−L| − u_nL` is itself `O(u_n)` there, not `O(1)`. This is a narrower, more concrete target
   than a Steinitz existence theorem for the whole deep interior; NOT yet gated.

### Candidate technique(s)
- Steinitz rearrangement lemma (1-D case is nearly vacuous — see below), Beck–Fiala /
  vector-balancing style existence arguments, prefix-discrepancy pigeonhole on the reachable-set
  multiset (MD2-style), and a recursive/inductive argument tied to `u_n = u_{n-1}/(2+u_{n-1})`
  (the SEED(p) family — already dead, R13). None of the classical 1-D discrepancy tools give
  anything close to the needed *exponential* smallness `u_n ~ 2^{-n}` — see the "does a₁<L/2
  suffice" analysis below.

### Cheap-kill candidates
- **The "min-positive of the set" definitional trap (already flagged in Rules, R15) is a live
  landmine for any C1/completeness gate — I fell into it myself this round** (see below): when
  computing `μ` via `R = {0} ∪ reflections` and then filtering `min(v>0 : v∈R)`, a genuine
  nonempty-subset cancellation that lands exactly on 0 gets silently absorbed into the *trivial*
  `0∈R_0` and is invisible. The correct object is the FGR recursion `μ_i=min(μ_{i−1},
  dist(a_i,R_{i−1}))` (tracks the distance at each step, so a genuine `a_i∈R_{i−1}\{trivial}` hit
  registers `0` correctly). ANY future gate script computing `μ_{n+1}` or comparing it to `min
  R(A)` MUST use the dist-recursion form, never "min positive element of the accumulated set."
  (I verified this bug changes an apparent counterexample `mu_cat=3` into the true `Φ=0` on
  `{36,33,33,24,12}/138` — pre-build check: re-derive any C1/completeness script from the
  dist-recursion, not the naive set-filter, before trusting its output.)
- **Cheap pre-build gate for n=4,5,6 (exact `Fraction`, structured + adversarial, NOT random
  integers):** compute, on the R17/R18 hard-witness family and its perturbations (`A={1/3,13/40,
  13/40,1/120,1/120}` at n=4, the `{30,25,20,15,10}/100` family, and the sliver family `A^{(n)}`
  perturbed inward by `u_n/K`), BOTH `μ_{n+1}` (correct dist-recursion) and `min R(A)` (full
  subset+tree search, feasible up to n≈5–6 by memoized recursion over index-subsets). Report the
  gap `μ_{n+1} − min R(A)` in units of `u_n`. If the gap is bounded (say `≤ C` for an
  n-independent constant, or `→0`) on the *hard* family specifically, the bridge is salvageable
  as an inequality; if the gap grows with n on the hard family (as several other "easy object,
  hope it transfers" levers have — R17 single-target density, R18 anchored contraction), the
  bridge is dead and opening (3)/(4) above are the only live routes.
- **Cross-check whether random-integer profiles are the wrong regime.** My own test (n=4,
  random integers 1..60, a1<L/2) found `min R(A) < μ_{n+1}` strictly on 3/283 samples, but ALL
  of these had SMALL relative gaps (`0.16–0.55·u_n`) and involved exact integer TIES (e.g. two
  equal parts `{33,33}`) — a coincidence structure essentially absent from real-valued/adversarial
  sliver profiles. This is a genuine caveat: random small-integer profiles over-produce ties and
  may make `R(A)` spuriously rich (lots of exact-0 hits) relative to what happens on the actual
  hard (irrational-ratio, no repeats) sliver family. The mandatory gate must use the hard family,
  not random integers, exactly as R17/R18's own gating discipline already insists.

### Knowledge-base entries to use
- `knowledge_base.md` has **no entry specifically on Steinitz's lemma, discrepancy theory,
  Beck–Fiala, or prefix-balancing** — checked directly (`grep -i "steinitz|discrepancy|beck-fiala|
  balancing|prefix"` returns nothing). The only generically relevant KB entries are the two
  **Pigeonhole/extremal principle** bullets (lines 108, 188) — generic "take the max/min
  configuration" and "if count exceeds containers, two collide" — both already effectively
  exhausted by this problem's MD2 (multiset pigeonhole, dead as a GAP→VALUE mechanism) and the
  9 dead upper mechanisms. No new KB lever is available for this route; any Steinitz-type argument
  here has to be built from scratch, not cited.

### Analogous past problems (cruxes)
- **aimo-0493** (combinatorics, `extremal-principle`/`invariants-and-monovariants`): "no element
  can more-than-double its distance from the minimum without becoming k-good" — a dyadic-doubling
  gap argument bounding how many elements of a scale-indexed structure can dodge a covering
  property. Structurally the CLOSEST analogue in the corpus (same 2-adic/dyadic-doubling flavor as
  this problem's certified `ONE-REC`/`Lemma ONE`), but it is a *counting* bound on how many points
  can avoid a property, not an *existence* bound that some signed combination is small — it does
  not supply the missing lever, and it is already effectively subsumed by `ONE-REC` (certified,
  round 9) in this problem's toolkit.
- **No genuine crux for "some signed subset sum lands within ε of a target" was found.** I
  filtered `combinatorics`/`number_theory` cruxes on `discrepancy, signed sum, subset sum,
  balancing, steinitz, rearrangement, closest, nearest, target value, within, partial sum,
  partition into two, split into two groups, sum close to`, and cross-checked `games-and-strategy`
  problems mentioning stick/segment/cut/mark. None of the hits (aimo-0015 distinct-subset-sums,
  aimo-0146/aimo-0287 exchange-smoothing majorization, aimo-0035 equal-sum partition
  construction, aimo-0561 defect-transport-to-nearest-deficit) are really analogous: they either
  build/construct a partition from scratch (no adversarial "find SOME small signed sum among a
  restricted, already-fixed set of numbers" existence claim) or are exchange-smoothing on a
  DIFFERENT kind of extremal object (already the exhausted vertex-polytope framing on the LOWER
  wall, R14). Honest conclusion: **no analogous crux exists in the corpus for this exact
  existence-of-a-small-signed-subset-sum claim** — the corpus does not contain a discrepancy-theory
  problem of this flavor.

### Prior progress
Certified and unchanged (import, do not re-derive): Lemma WTC (boundary layer `a₁≥(L−u_nL)/2`
closed exactly), Lemma RL (characterizes `R(A)` as tree-realizable — strictly `⊊` all `{0,±1}`
sums), Lemma FGR (`μ_{n+1}=min_i dist(a_i,R_{i−1})`, the correct dist-recursion — NOT "min
positive of the accumulated set"), Reduction R-COV' (sufficiency: `μ_{n+1}≤u_nL ⟹` upper bound,
via ESF-2's exact `n`-move realization), Lemma CONF (`R_{n+1}⊆[0,a₁]`), Lemma MD2 (multiset
`|M_{n+1}|=2^{n+1}`, but the *gap*-pigeonhole corollary is explicitly NOT a value-reachability
argument — dead as a closing mechanism). The open residual, precisely: `μ_{n+1}≤u_nL` for
`a₁<(L−u_nL)/2` (deep interior), with the sliver `a₁∈(L/2−u_n,L/2−u_n/2)` singled out as the
hardest sub-region (`Φ/u_n→1` there, R17/R18).

### Dead ends (do not retry)
All 9 dead upper mechanisms from the Rules (round-11 through round-18): covering-radius (one-cap
R10, two-cap R12), density/COUNT (R11), greedy band-landing recursion (R9), bounded-depth escape
(R10), mass-telescope/GAP-TELE (R13), margin/extremal-tie (R14), full-tree second moment — both
fixed-order (R16) and gated-first over the FULL `R(A)` ensemble (R17) — and the a₁-anchored
walk/reflected-contraction CLASS (R18, includes any stopping-rule variant of the prefix-only
family). Also dead: the R17 single-target subset-sum density `min_{S⊆tail}|a₁−Σ_S|≤u_n` (FALSE,
ratio→1.99). **New this round (not previously recorded): literal completeness `μ_{n+1}=min R(A)`
is FALSE as an exact equality** (explicit counterexamples below) — any future lever assuming
equality (not just an inequality with controlled slack) is unsound on arrival.

### Small-case / intuition notes (labeled conjecture/counterexample as appropriate)
- **CONJECTURE-BREAKING FINDING (exact `Fraction`, n=4, verified by hand-tracing the recursion):**
  the caterpillar-only minimum `μ_{n+1}` and the full tree-realizable minimum `min R(A)` are NOT
  always equal. Counterexamples (random integer profiles, `a₁<L/2`):
  - `A=(17,16,11,8,4)`: `μ_{n+1}=1`, `min R(A)=0` (gap `=0.55·u₄`).
  - `A=(59,55,53,44,17)`: `μ_{n+1}=2`, `min R(A)=0` (gap `=0.27·u₄`).
  - `A=(54,43,35,32,28)`: `μ_{n+1}=3`, `min R(A)=2` (gap `=0.16·u₄`).
  These are genuine, exact, hand-traceable violations of naive completeness (3/283 random `a₁<L/2`
  profiles tested at n=4). **CAVEAT (labeled explicitly):** these are small-integer profiles with
  exact numeric ties (e.g. `{33,33}` in an earlier version), which make `R(A)` spuriously rich via
  coincidental cancellations — not necessarily representative of the adversarial sliver family
  where all ratios are irrational-like and no repeats occur. So this is evidence that **naive
  completeness cannot be certified as an unconditional identity**, but it does NOT settle whether a
  *bounded-gap* (`μ_{n+1} ≤ min R(A) + o(u_n)`) version survives on the actually-hard profiles —
  that requires the structured exact-Fraction gate above, not yet run.
- **The naive Steinitz/greedy-differencing bound is off by an exponential factor, confirmed
  quantitatively.** The classical bound (sort descending, greedily sign to keep the running sum
  small) gives discrepancy `≤ max part = a₁` — this is *exactly* what certified Lemma WTC already
  proves (`K≤|2a₁−L|`), and it is already known (R15–R18) to fall short by design in the deep
  region, where `|2a₁−L|≫u_nL`. Since `u_n=1/(2^{n+1}−1)` is exponentially small in `n` while `a₁`
  is only bounded by a constant fraction of `L`, **`a₁<L/2` alone is nowhere near sufficient**: any
  bound achievable from `a₁` alone (or from any single fixed-depth reflection) is `Θ(1)`-order in
  `L`, not `Θ(2^{-n})`. Closing the gap needs a mechanism that genuinely exploits the exponentially
  large search space (`2^{n+1}` subsets / tree topologies), which is exactly why every "cheap"
  single-object bound (covering radius, one fixed walk, one density count) has died — none of them
  scale with the right exponential rate. This is consistent with, and sharpens, the standing Rule
  that the next lever must be a genuinely global EXISTENCE argument over the *whole* signing
  family, not any single anchored or fixed-depth object — but my finding above shows even the
  natural "whole signing family" object (`R(A)`) does not transfer its minimum to the caterpillar
  family for free; the transfer itself needs proof and may not hold as a clean equality.
- **Recommendation to the outliner:** before building any C1/GAP-ACH/bridge-style approach, run the
  cheap-kill gate above (dist-recursion `μ_{n+1}` vs. full subset+tree `min R(A)`, on the R17/R18
  hard witnesses specifically, not random integers) to determine whether the bridge survives with a
  bounded (ideally vanishing) gap. If it does not, opening (3) (a direct, self-contained pigeonhole
  on `R_{n+1}` itself, never routing through `R(A)`) or opening (4) (a narrow perturbative argument
  confined to the `u_n/2`-wide sliver) are the remaining live candidates; both are unexplored as
  concrete build targets this round.
