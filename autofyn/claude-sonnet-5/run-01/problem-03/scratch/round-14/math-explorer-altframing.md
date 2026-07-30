## imo-2026-03 (alt-framing go/no-go for Case C upper bound, general m≥4)

### Scope of this report
Per dispatch: this round's job was a go/no-go check for a genuinely different
combinatorial framing of Claim PTBI's Case C (`p_1<Σ(A)/2`, general `m≥4`),
distinct from casework/matching, from the dead minimax-mixed-duality and
relaxed-adversary-transfer, and from case-c-secondary-extremality (RETHINK'd
as value-equivalent to the primary approach). I did NOT attempt to build or
close the gap — only scouted.

### What I did
1. Re-read `current.md` in full (the round-13 mark-accounting retraction) and
   the relevant sections of `approaches/universal-adversary-strategy.md`
   (the exact statement of Claim PTBI, the peel+halve attempt, Lemma
   DOUBLE-INSERT, the m=3 closure, the round 9-13 history of the Case-C gap).
2. Read `knowledge_base.md` in full for candidate techniques not yet tried
   on this problem (LP/duality, flow, extremal-principle, probabilistic
   method, Hall's theorem, monotone-subsequence tools).
3. Queried the crux corpus (`past_crux_moves_database.json`), filtered to
   `domain=combinatorics`, `subtopic=games-and-strategy` (39 cruxes) and
   skimmed `extremal-principle`/`linear-algebra-method`/`probabilistic-method`
   entries for an "adversary limits value" upper-bound technique not already
   tried here.
4. Ran independent numeric sanity checks (Python, `scipy.optimize.
   differential_evolution` over an exhaustive-over-mark-allocation-pattern
   search, exactly the methodology the round-13 proof-reviewer used) to
   test one specific candidate idea (see below) before reporting it.

### Candidate idea considered and REJECTED after testing: extremal-configuration-perturbation / interpolation argument
The natural "genuinely different" idea in this family is: let
`V(A) := min over Xiang-Yu strategies of oddrank(B)` (the true, correctly
mark-capped game value — I verified my own from-scratch implementation of
this reproduces the reviewer's round-13 finding exactly: `V((26,21,10)/57,
budget=2) = 31/57` on the nose). Then take `A*` maximizing `V(A)/Σ(A)` over
the compact simplex (a maximizer exists since `V` is a min of finitely many
functions, each piecewise-affine in `A` for a fixed combinatorial response
pattern, hence `V` is continuous) and try to derive a contradiction by
perturbing `A*` (interpolating with a nearby config) if `V(A*)/Σ(A*) >
c(m-1)`.

**This is not new — it is exactly `majorization-smoothing`'s framing
reapplied to the true value function instead of a restricted family.**
`V` is a min of finitely many affine functions of `A` (one per Xiang-Yu
combinatorial response type), which makes `V` **concave**, not convex — so
maximizing `V` over a polytope can genuinely occur in the polytope's
*interior*, not just at vertices. This is mathematically the same object
`majorization-smoothing` tried to exploit and which was killed 3 times
(RETHINK ×3, confirmed via a genuine nested convex kink, not a numeric
fluke). I did not re-run the exact killed computation (per the standing
rule "NEVER re-run majorization-smoothing's concavity claim"), but I did
independently verify the underlying fact that makes this framing structurally
doomed: `V` is not simply concave/well-behaved along line segments because
the identity of the optimal combinatorial response pattern changes across
the segment (a genuine "kink"), and near-tight witnesses do not sit at nice
interpolable points. Concretely, I checked `V` at the m=3 "extremal" point
`A=(3,2,2)/7` (the point `current.md` calls the closure point for the
certified *construction*, `min(TAIL-SNIP,BLOCK-RECURSE_1)=4/7` there) —
**the TRUE global game value there is actually `0.5 < 4/7`**, achieved by a
completely different pattern (halve `p_1`, not the certified menu's chosen
move) with real slack. This confirms: (a) the "tightness" recorded in
`current.md` at that point is tightness of a *specific certified
construction*, not of the true game value, so there is no clean interior
extremal point to interpolate around for a majorization-style contradiction;
(b) any interpolation/averaging argument across configs inherits the exact
convexity-kink obstruction that already killed `majorization-smoothing`.
**Verdict: do not open this as a new approach — it collapses into the
already-dead framing.**

### Candidate idea considered, more promising but NOT validated this round: LP/flow relaxation targeting the inequality directly (not the exact-tie identity)
`universal-adversary-strategy-exact-tie`'s Hall/exact-cover route targeted
the STRONGER conjectured identity `solve_full(A)=Σ(A)/2` and found it false
(the `(26,21,10)/57` witness). A genuinely different move: reformulate the
*existence* half of Case C as a **min-cost transportation / flow problem**
(not an exact 1-1 matching / exact-cover), i.e. allow Xiang Yu's tail
elements to be treated as fractional "mass" that can be split among several
"donor" targets, bound the achievable `oddrank` via **weak LP duality**
(any dual-feasible weighting gives an upper bound on the primal optimum,
without needing the primal's exact combinatorial optimum or an exact
matching to exist) — this only needs to prove an *inequality*, which is
structurally more forgiving than the identity Hall's-theorem route that
just failed. I did **not** have time this round to formalize the LP and
run a real numeric gate on it (this needs care: the "moves" are not a fixed
finite menu, they are a genuine combinatorial optimization over split
patterns, so setting up a valid, provably-sound dual certificate is real
work, not a five-minute check). I flag this as a **candidate worth a real
go/no-go test next round**, but I am NOT claiming it passes a gate — it is
untested, distinct from both dead LP/duality attempts (minimax-mixed-duality
duality was over Xiang Yu's *mixed strategy*/game value certificate and
collapsed into the same casework; the exact-tie route needed an *exact*
matching). A weak-duality inequality-only argument is a different object
from both, but I have not verified it clears the bar.

### Crux corpus findings
- `combinatorics` / `games-and-strategy` (39 cruxes): the closest analogue
  remains `aimo-0560` ("replace the adversary with a strictly stronger
  surrogate whose reply is pointwise at least as damaging, so a win against
  the surrogate transfers down") — this is exactly `relaxed-adversary-
  transfer`, already proven a clean dead end here (Theorem V-INF, wrong
  direction). No other crux in this subtopic gives a technique that maps
  onto "prove existence of a good response for every adversarial config" in
  a way not already tried — most are pairing/mirroring/invariant strategies
  for *win/lose* games, not continuous-value optimization games.
- `aimo-0117` (dyadic/geometric sequence where the top value exceeds the
  sum of the rest) is analogous to the **lower bound**'s geometric
  construction `A_n`, already fully proved and out of scope — not useful
  for Case C.
- `combinatorics` / `extremal-principle` and `inequalities-SOS-and-convexity`
  subtopics: skimmed several entries; nothing offers a technique for
  "min-over-adversary-responses ≤ target for every input" beyond the
  concavity/interpolation idea already ruled out above.
- `probabilistic-method`: the natural translation ("randomize the split
  ratio, bound the expectation") is mechanically the same failure mode as
  the already-dead `potential-averaging-bound` (averaging fixed candidate
  strategies failed the feasibility gate at `A=(1/3,1/3,1/3)`, `n=2`) —
  expectation-based existence arguments over a *small fixed family* of
  randomized strategies will hit the same budget-blindness diagnosis
  `potential-averaging-bound` already found. Not recommending it as new.
- No Hall's-theorem crux beyond what's already been tried (Lemma PAIR-VALUE
  / MATCH-HALVE-EXISTS route, still the sharpest known target).

### Verdict: STAY in the current casework/matching framing this round
No genuinely new, validated framing was found. The one candidate that
looked new on paper (extremal-configuration-perturbation) was tested and
shown to reduce to the already-3×-killed `majorization-smoothing` object
(via the concavity-of-`V` argument above) — this is a **structural**
finding, not just "didn't find a counterexample," and should be recorded so
no future round re-opens it under a different name. The LP/weak-duality
idea is flagged as the one genuinely-untested candidate worth a real
(not five-minute) go/no-go attempt, but it did not pass any gate this round
because it was not yet formalized — do not treat it as validated.

### Recommendation for the outliner
- Do NOT open a new top-level approach slug this round based on this
  report — nothing here clears the bar of "concrete evidence it might
  work." Per round-14 priorities in `run_state.md`, proceed with (1)
  rebuilding `solve(A,budget)` with correct real-mark accounting and (2)
  re-attacking Case C via the Hall-type non-contiguous subset-matching
  existence question (Lemma PAIR-VALUE / MATCH-HALVE-EXISTS), reusing
  Lemma NONNEG-EXCESS's reformulation.
- If a future round wants to try the LP/weak-duality-inequality idea, it
  needs an explicit finite (or well-defined infinite but tractable) dual
  certificate formalized and stress-tested BEFORE being written into an
  approach file, per the standing "mandatory numeric gate before any build"
  rule.
- Useful side confirmation for the builder: I independently re-verified
  (fresh Python, `differential_evolution`, exhaustive over the finitely
  many ways to distribute Xiang Yu's marks across pieces) that the
  round-13 corrected witness value `V((26,21,10)/57, budget=2) = 31/57`
  is exactly right — an independent third confirmation of that number,
  reinforcing that the round-13 correction is solid ground to build on.

### Dead ends (reconfirmed, do not retry)
- `majorization-smoothing` / any config-space interpolation-and-perturbation
  argument on the true value function `V(A)` — structurally doomed because
  `V` is a min of finitely many affine functions (hence concave, not
  convex), so its max over the simplex can be attained in the interior; a
  vertex/boundary-forcing contradiction argument does not generally exist.
  This subsumes and reconfirms the round 1/3/4 kills.
- `relaxed-adversary-transfer` mechanism (crux `aimo-0560`'s surrogate-adversary
  idea) — wrong direction here, confirmed round 7, reconfirmed by this
  round's crux search finding no new variant.
- Naive probabilistic/averaging existence arguments over a small fixed
  candidate-strategy family — same failure mode as `potential-averaging-bound`
  (budget-blindness), not worth re-trying without a genuinely budget-aware
  randomized strategy design (which would likely collapse into the existing
  casework anyway).

### Small-case / intuition notes (labeled conjecture/observation, not proof)
- Observation (verified numerically, not new): the true game value `V(A)`
  at "generic" (non-adversarially-chosen) points in Case C is typically far
  below the `c(m-1)` target with large slack; the entire difficulty of
  Case C is concentrated at a thin, adversarially-constructed set of
  near-tight configurations (the known `m=5` witness margin `≈0.00585`,
  `m=8` witness margin `≈-1.53e-4` before the round-12 fix). This is
  consistent with — not contradicting — 13 rounds of difficulty: a
  framing that works "on average" or "generically" (interpolation,
  probabilistic, simple fixed-menu) will always fail exactly at these thin
  extremal configurations, which is exactly the established pattern.
