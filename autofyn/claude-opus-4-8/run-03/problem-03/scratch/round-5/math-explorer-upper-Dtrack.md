## imo-2026-03 — LENS: GAP U (upper bound, balanced regime a1 < L/2), D-tracking exchange

### Setup recap (from current.md / parity-measure-potential.md / induction-peel.md)
- Whole range `a1 ≥ L/2` is CLOSED profile-independently (Branch 0 bisect for `a1≥c(k)L`,
  Branch 2 whole-tail-peel for `L/2≤a1≤c(k)L`, giving the EXACT identity `D=2a1-L`). This is a
  genuine exact identity (via Lemma P cancelling-pair), not a bound.
- Mass-threshold/subset-cover for `a1<L/2` is REFUTED (counterexample `(0.44,0.281,0.279)`,
  true `V=0.002 ≪ u_2=1/7`; the reduction only sees residual *mass*, but true `D` of the residual
  depends on its internal near-cancellation, invisible to a mass bound).
- `smoothing-majorization.md` proposes (SMOOTH): dyadic uniquely maximizes `V(A)`, transported by
  a dyadic-ward exchange; numerically confirmed as a premise (unique max at dyadic, n=2) but the
  monotone-exchange mechanism is NOT proved — the explicit lemma/potential is missing.
- No `lp-dual-weight.md` file exists in the repo; it appears to be a dormant/unwritten framing
  name, not a started approach.

### NEW numeric findings this round (both are refutations — report them as dead ends)

**(1) Global concavity of `V` is FALSE — kills the naive "LP/dual-weight" idea.**
I tested the natural conjecture that `V(A) := min_{Xiang} D(A)` is a CONCAVE function of the
sorted Liu profile `A` on the simplex (which, if true, would let a single first-order/KKT
certificate at the dyadic point `𝒟_n` certify the global max — an LP-duality-style proof). This
is numerically FALSE: for `n=2` (3 pieces, ≤2 cuts), computed (via a fine grid search over all
≤2-cut strategies, which only *overestimates* `V`, so violations found are genuine) the midpoints
between `𝒟_2=(4/7,2/7,1/7)` and other profiles, e.g. `(0.45,0.30,0.25)`:
```
λ=0.25: V(mid)=0.0393 < affine interp 0.0732   -- concavity VIOLATED
λ=0.50: V(mid)=0.0214 < affine interp 0.0964   -- concavity VIOLATED
λ=0.75: V(mid)=0.0821 < affine interp 0.1196   -- concavity VIOLATED
```
Reason (structural, not just numerical noise): for a FIXED combinatorial Xiang strategy
(sequence of match/bisect choices with fixed *rule*, e.g. "match a1 against a2"), `D_τ(A)` is
affine in `A`; but `V_τ(A) := min` over the *continuum* of legal cut-fraction choices for a fixed
combinatorial *shape* τ is itself only concave (min of an affine family), and `V(A) = min_τ V_τ(A)`
is then a min of finitely many CONCAVE (not affine) functions — which is NOT necessarily concave.
The sort-order of the final multiset changes across different regions of the simplex, breaking
global concavity. **This kills any hope of a single global-concavity / dual-certificate argument
without first partitioning into sort-order chambers** — a genuinely harder undertaking than a
plain LP duality argument. Do not pursue "prove V concave, exhibit KKT point at dyadic" as stated;
it is false as a blanket claim.

**(2) "Cascading bisection" (recursive drop-the-top-if-balanced) is ALSO refuted as a strategy —
a new, concrete negative result, distinct from mass-threshold and from greedy-merge.**
Natural candidate D-tracking exchange: at each step, if current top `a1 < L_cur/2`, bisect `a1`
(this contributes EXACTLY 0 to `D`, by Lemma P — an *exact* identity, no bound), and recurse on
the tail with one less cut; once `a1 ≥ L_cur/2` for the *current* residual, apply the
already-closed dominant formula (Branch 0/2) to finish exactly. This exactly reproduces the true
optimum on the 3-piece counterexample `(0.44,0.281,0.279)` (bottoms out after ONE bisection into
the 2-piece dominant case, giving the exact `D=0.002`). **But it fails badly for larger, near-equal
profiles**: for `n=5` (6 pieces), a near-uniform profile
`(0.2024,0.1965,0.1820,0.1789,0.1651,0.0750)` cascades down through 4 sequential bisections to a
final 2-piece dominant residual `{0.1651,0.0750}` (budget exhausted), giving `D≈0.075`, while
`u_5·L = 1/63 ≈ 0.0159` — a **4.7× violation**. Diagnosis: cascading always peels only the CURRENT
top piece one at a time; for near-uniform profiles the correct Xiang move is the Lemma-U0-style
*simultaneous* even-multiplicity pairing (all pieces near-equal ⇒ direct near-0 `D`, no bisection
chain needed), not a sequential single-piece peel. Sequential greedy peeling of one piece at a
time is provably NOT the right move-order for near-uniform tails — this reproduces (in a new
guise) the previously-recorded dead end "greedy-merge/single fixed rule insufficient." **Record as
a second dead end: no single fixed per-step rule (mass-threshold subset OR sequential
cascading-bisection) is uniformly correct across the full balanced regime; the correct strategy is
provably case-adaptive (bisect for skewed-but-balanced profiles like the 3-piece counterexample,
simultaneous even-pairing for near-uniform profiles).**

### The most alive concrete lever for the outliner

Both refutations point the same way: the correct D-tracking argument must be a **hybrid** that
recognizes, from the profile's shape, whether the tail is "near-uniform" (use Lemma U0's
even-multiplicity pairing, which is EXACT and cheap, already certified) or "has a clear near-max"
(use the certified whole-tail-peel/bisect exact formulas). The open content is a single dichotomy
lemma of the following shape (this is the concrete exchange lemma to target — not solved here):

> **Target Lemma (D-DICHOTOMY, open).** For any Liu profile `A` with `a1 < L/2` (balanced,
> `m=n+1` pieces, full budget `n`), EITHER (i) `A` is within some quantified closeness `δ` of a
> configuration admitting an exact even-multiplicity pairing of ALL `n+1` pieces via ≤ `n` cuts
> (extending Lemma U0's `m≤n` corrector to the boundary case `m=n+1` with one forced leftover),
> giving `D` small directly — OR (ii) `A` has a piece `a_j` (not necessarily `a1`) that is "locally
> dominant" relative to a natural sub-tail, letting a SINGLE whole-tail-peel (Lemma P + Lemma
> SPLIT, exact, not a bound) on that sub-tail close the bound. The two regimes must be shown to
> cover the whole `a1<L/2` simplex, with the transition point (where a profile is exactly on the
> boundary) mapping to the certified `a1=L/2` boundary case with `D=0`.

This reframes GAP U as "extend Lemma U0 (even-multiplicity, currently only proven for `m≤n`) to
the boundary case `m=n+1` with the SPLIT cross-term carried exactly," rather than as a
subset-mass threshold. It is a genuinely different lever from both refuted attempts: it uses the
EXACT identities (Lemma P, Lemma SPLIT — already certified, no re-proof needed) as its only
tools, never a worst-case mass bound, and never a single fixed strategy order.

### Candidate technique(s)
- Extend **Lemma U0 (even-multiplicity corrector)** — currently `m≤n ⇒ D=0` — to `m=n+1` with a
  single unavoidable "odd piece out," using **Lemma SPLIT**'s cross term `2μ(O_X∩O_Y)` to track
  exactly how much the one unpaired piece contributes, rather than bounding it crudely.
- **Lemma PEEL** (`D(S)=f1-D(S∖f1)` for a unique max) is the right tool once a genuinely dominant
  sub-piece is identified (not necessarily `a1` at the top level — could be identified after a
  partial pairing).
- Do NOT reuse: mass-threshold subset-cover (refuted, counterexample certified); sequential
  cascading-bisection (refuted this round, 4.7× violation at n=5); global concavity / naive
  LP-duality on `V` (refuted this round, explicit numeric violation, plus the structural reason
  why — sort-chamber boundaries break concavity of the min-over-strategies function).

### Cheap-kill candidates
- None new beyond the two refutations above (which ARE the cheap kills this round — both took
  <5 min of numeric probing to falsify and should not be re-attempted).
- A useful cheap discriminator for any future strategy proposal: test it FIRST on the near-uniform
  6-piece profile above (`n=5`) — this is now a certified stress-test that killed cascading-bisect;
  any proposed strategy should be checked against it before further development.

### Knowledge-base entries to use
- `lemmas/cancelling-pair.md` (Lemma P) — exact, zero-cost pairing; central to any correct route.
- `lemmas/split-cross-term.md` (Lemma SPLIT) — the tool most likely needed to extend Lemma U0 to
  `m=n+1`; carries the cross term exactly instead of dropping it (dropping it is flagged in
  `split-cross-term.md` itself as "too lossy near the balanced regime").
- `lemmas/strict-max-peel.md` (Lemma PEEL) — for the "locally dominant sub-piece" half of the
  dichotomy.
- `lemmas/whole-tail-peel.md` — the exact formula to invoke once a genuine dominant regime (at
  any recursion level, not just top) is identified.
- Lemma U0 / even-multiplicity corrector (`two-box-balancing.md`, "Lemma U0") — not yet in
  `lemmas/` as a certified file; worth promoting and then extending to `m=n+1`.
- `knowledge_base.md`'s piecewise-concavity-smoothing entry (line ~20) is the generic tool
  `smoothing-majorization.md` invokes — but per finding (1) above, plain concavity of `V` is
  false, so this entry can only be used AFTER restricting to a fixed sort-order chamber, not
  globally; flag this caveat to whichever approach uses it next.

### Analogous past problems (cruxes)
- **aimo-0146** (already used by `smoothing-majorization.md`): exchange-smoothing a fixed weighted
  sum of a sorted sequence, then a finite hand-checked endgame. Genuinely analogous in spirit
  (sorted alternating-weight objective) but the crux's weights are FIXED, while ours come from
  Xiang's own optimal response and change under perturbation — the smoothing approach already
  flags this gap; my finding (1) shows the naive fix (global concavity) does not exist, so the
  aimo-0146 pattern needs the chamber-restriction caveat above.
- **aimo-0560** (surrogate-opponent domination): used in `two-box-balancing.md`'s lower-bound GAP L
  attempt, not directly for GAP U, but the same "replace with a pointwise-dominant surrogate" idea
  could in principle be tried for GAP U (grant Xiang a surrogate who may freely re-pair any subset
  at zero cost, i.e. a relaxation of Lemma U0) — untried for the upper bound; flagging as an
  option, not verified.
- **aimo-0089** (supporting-line/supergradient bound derived from a weighted-average functional
  inequality): a generic analogue of the "exhibit dual weights at the candidate optimum" idea I
  tested and refuted in finding (1); not a strong structural match to this problem (different
  domain, functional equations) but the *technique name* (supporting-line argument) is the
  textbook version of what a correct local LP-duality argument would need IF concavity held in a
  single chamber — useful vocabulary, not a transplantable proof.
- No crux in `games-and-strategy` matches this problem's specific alternating-claim/cutting
  structure closely; the closest thematically (aimo-0560, aimo-0663) are about turn-parity /
  pairing-strategy games, not continuous-cut minimax, and are only loosely analogous.

### Prior progress
See current.md: entire `a1≥L/2` closed; GAP U (`a1<L/2`) open; mass-threshold lever refuted.
This round adds: cascading-bisection strategy refuted (new); global concavity of V refuted (new);
a concrete reframing of GAP U as "extend Lemma U0 to m=n+1 via Lemma SPLIT's cross term" (new
lever, not yet attempted by any approach).

### Dead ends (do not retry)
- Mass-threshold / subset-cover feasibility disjunction for `a1<L/2` (prior rounds; counterexample
  `(0.44,0.281,0.279)`).
- Sequential cascading-bisection ("bisect current top whenever it's <half the current residual
  total, recurse") as a UNIFORM strategy for all balanced profiles (this round; 4.7× violation on
  a near-uniform 6-piece profile at n=5). It DOES work as a special-case tool when the profile
  happens to have a clean dominant sub-piece at some recursion level (e.g. it exactly reproduces
  the true optimum on the original 3-piece counterexample) — so it is a valid TACTIC inside a
  case-adaptive strategy, just not a valid UNIFORM rule on its own.
- Global concavity of `V(A)` on the simplex, hence any "single dual-certificate at the dyadic
  point closes everything" argument (this round; explicit numeric violation plus the structural
  reason: `V` is a min over finitely many chamber-concave-but-not-affine functions, not a min of
  affine functions).

### Small-case / intuition notes (conjectural, numerically checked)
- The true hard sub-case of `a1<L/2` is neither "very skewed" (handled by whole-tail-peel once a
  local dominant piece emerges after ONE bisection, as in the 3-piece counterexample) nor "very
  uniform" (handled directly/cheaply by even-multiplicity pairing, `D≈0`); it is the INTERMEDIATE
  band where the tail is neither near-equal nor has a clear dominant element. Numerically, the
  worst-case profiles for naive strategies cluster near either (a) 3-piece profiles with a
  near-half-mass top and a near-equal pair tail (the known counterexample shape), or (b) profiles
  where TWO tail elements are close but a third is markedly smaller, breaking both pure pairing and
  pure peeling. A correct proof likely needs to handle "how many elements are within ε of the
  mean" as the case-split variable, not "is a1 above or below a fixed threshold."
- All numeric checks in this report are conjectural evidence about strategy adequacy on individual
  profiles, not proofs; the reviewer-certified facts remain exactly those already in `lemmas/`.
