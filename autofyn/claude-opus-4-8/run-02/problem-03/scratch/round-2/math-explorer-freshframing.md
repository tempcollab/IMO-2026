## imo-2026-03

### Assigned lens
A genuinely different global framing for BOTH bounds at once, away from the shared
odd-level-measure discrepancy D framing that all three current approaches
(dyadic-discrepancy, induction-recursion, potential-certificate) use and are all
stuck on at the same wall (GAP U: no non-myopic Xiang strategy for a general Liu
partition).

### Distinct openings found

**1. LP/concavity framing (the strongest new lead — recommend opening as a 4th approach).**
Key structural fact, checked and essentially provable from the *already-proved*
cut-flip lemma (`lemmas/cut-flip.md`): for a **fixed combinatorial order-type**
(i.e. fixed relative ranking of all final pieces), `D = Σ ± (piece length)` is an
*exactly affine* (in fact a signed linear) function jointly of (a) Liu's piece
lengths and (b) Xiang's free cut positions. This is because D is literally a
signed sum over final pieces, and within one order-type the sign pattern is fixed.
Consequence for a single cut of a piece `ℓ=x+(ℓ-x)`: if the two children land on
*opposite* parity-ranks, D is affine in `x` with slope `±2`; if they land on the
*same* parity-rank, D is **constant** in `x` (a tie region). So **Xiang's
optimum on one cut is never a genuine interior optimum — it is always attained at
a boundary of an order-type region** (either `x→0`, i.e. no cut, or a tie
crossing into a new order-type). With several simultaneous cuts (on distinct
original pieces) the objective is still jointly affine per region, so minimizing
it is literally an LP over a polytope of order-type regions, and by LP theory the
optimum is at a **vertex** (a specific finite tie-pattern), never a generic
interior point. This matches exactly what is already observed empirically: the
n=1 optimal Xiang rule is "bisect" (a specific tie: the two children equal) or
"leave uncut" (x→0) or "pin the median" (a tie between a Xiang-created piece and
an existing Liu piece) — never a free interior value.

Consequence for BOTH bounds: define `f(Liu partition) := min_Xiang D`. Since `f`
is a **min of finitely many affine functionals of Liu's partition vector**
(one affine functional per reachable vertex/tie-pattern), `f` is **concave** on
the simplex of Liu partitions. Maximizing a concave function over a convex domain
means: **any point satisfying first-order (KKT / subgradient) optimality is the
global maximum.** So instead of constructing Xiang's response for *every* Liu
partition (GAP U as currently posed), the task becomes: exhibit enough "active"
affine pieces (tie-patterns) at the dyadic partition to certify a subgradient
condition — a **local, finite check at one point**, not a case analysis over all
partitions. This attacks the upper bound and would automatically re-derive the
lower bound from the same local data (the active affine pieces at dyadic *are*
Xiang's optimal responses there, giving `f(dyadic)=u` directly), so it genuinely
targets **both bounds with one mechanism**, as the assigned lens asks.

I numerically tested this: computed `f` (via a grid-search LP-style brute force
over ≤2-cut Xiang responses at n=2, 3 initial Liu pieces) along five different
perturbation directions away from the dyadic partition `(4/7,2/7,1/7)`. In every
direction, `f` **decreased monotonically and apparently affinely** moving away
from dyadic (see transcript below) — strong (but only numerical/conjectural)
evidence that dyadic is a strict local max of `f`, consistent with the concavity
picture. This is new evidence beyond what the three existing approaches report
(they only verified `min D = u` *at* dyadic, not that dyadic is a local max of
the whole `f` landscape over partition space).

```
along dir (-0.02,0.01,0.01): f = .14286, .13086, .11886, .10286  (s=0,.3,.6,1)
along dir (+0.02,-0.01,-0.01): f = .14286, .13986, .13686, .13286
along dir (-0.01,-0.01,0.02):  f = .14286, .13386, .12486, .11286
along dir (+0.01,+0.01,-0.02): f = .14286, .13686, .13086, .12286
along dir (-0.03,+0.02,+0.01): f = .14286, .12486, .10686, .08286
u_2 = 1/7 = 0.142857
```

**Caveats (be honest about the gap this new framing still has):**
- The single-cut "affine, optimum at boundary" fact looks straightforward to
  prove rigorously (it is essentially a refinement of the already-proved
  cut-flip lemma), but the **joint LP-vertex claim for ≤n simultaneous cuts**
  and the **global (not just locally-near-dyadic) concavity of f on the whole
  simplex** are NOT yet proven — only checked numerically near one point. The
  family of "reachable order-types" could in principle be large (combinatorial
  blow-up in n), so enumerating/bounding it is itself work.
- The KKT/subgradient certificate at dyadic (showing no directional derivative
  of `f` is positive there) is exactly the content that would replace GAP U —
  it is not free; it requires identifying the *right* finite set of active
  ties at dyadic (the analogue of the n=1 "bisect vs no-cut" crossing) and this
  has NOT been done for general n. So this is a promising **new route into**
  GAP U, not a proof of it.
- This framing is mathematically adjacent to the discrepancy language (D is the
  same object), but it is a genuinely different *proof strategy*: LP-duality /
  concavity + local optimality certificate, vs. explicit case-by-case adversary
  strategy construction. It should count as materially distinct from the three
  existing approaches, which never invoke concavity or LP-vertex structure.

**2. Direct reciprocal/potential reframing (weaker, more cosmetic — mention only).**
`1/c(n) = 2 − 2^{-n}` is a strikingly clean closed form (checked: n=1 → 3/2,
n=2 → 7/4, matches). This suggests tracking `W_n := 2 − 1/c(n) = 2^{-n}`, which
*exactly halves* with each extra (Liu-mark, Xiang-cut) pair. This is algebraically
equivalent to the existing recursion `c_n = 2c_{n-1}/(2c_{n-1}+1)` already found
by induction-recursion (§7) and doesn't obviously offer a new *mechanism* for
GAP U beyond re-deriving the same recursion; flagging it mainly because it might
suggest a cleaner inductive quantity to carry (a literal "halving" monovariant)
if the outliner wants an amortized argument, but I do not see it dissolving the
crux on its own. Lower priority than opening 1.

**3. Direct game-tree / strategy-stealing on n (checked, does not obviously
work as a standalone new framing).** One might hope for a scale-invariance /
strategy-stealing argument showing the n-game value literally *is* a rescaled
(n-1)-game after Xiang's first move, proven by a symmetry argument rather than
via D. But the game is not sequential in the right way for strategy-stealing:
Xiang commits all ≤n cuts in one shot after seeing Liu's whole partition, so a
"first cut, then recurse" argument requires knowing Xiang's cuts interact with
Liu's *entire* partition, not just the top piece — which is exactly the
induction-recursion approach's Case B struggle (GAP L/GAP-LB), already explored
and stuck. I do not see a way to make this genuinely different from what
induction-recursion already tried; not recommending as new.

### Candidate technique(s)
- **Opening 1 (recommend):** LP duality / vertex-optimum for piecewise-affine
  objectives + concavity + first-order (KKT/subgradient) global-optimality
  argument. Matches KB entry **"Piecewise-concavity smoothing"** (knowledge_base.md,
  Algebra & Polynomials section) — that entry is stated for trigonometric-sum
  minimization but the *mechanism* (min of pieces each affine/concave on
  sub-intervals ⇒ global min/max at a breakpoint) is exactly the mechanism
  needed here, just generalized to a multi-dimensional simplex domain instead of
  a single angle. Also relevant: **"Standard inequalities... equality cases pin
  down the extremal configuration"** and the general extremal-principle /
  smoothing toolkit.
- Opening 2/3 are weaker; do not recommend as standalone new approaches.

### Cheap-kill candidates
None obvious for opening 1 beyond the numerical concavity check already done
above (which passed, i.e. did NOT kill it). Worth a slightly larger numerical
sweep (finer grid, more directions, n=3) before committing an approach's full
effort, but the round budget didn't allow it here — the outliner/builder should
treat this as "promising, not yet falsified" rather than fully verified.

### Knowledge-base entries to use
- **Piecewise-concavity smoothing** (knowledge_base.md, Algebra & Polynomials) —
  the closest KB analogue to the mechanism in Opening 1.
- **Standard inequalities / equality-case extremal pinning** (same section).
- (Shared spine, already certified, reusable regardless of framing:) Lemma G and
  the cut-flip lemma in `lemmas/greedy-claim.md` and `lemmas/cut-flip.md` — the
  affine-per-order-type fact in Opening 1 is literally a corollary of cut-flip.

### Analogous past problems (cruxes)
Searched combinatorics subtopics `games-and-strategy`, `linear-algebra-method`,
and free-text ("stick", "cake", "alternately claim", "divide") across both
crux-corpus files. **None found that are genuinely analogous.** The closest
surface matches (aimo-0063, a cupcake/interval fair-division problem using
Hall's theorem; various `games-and-strategy` pairing-strategy problems like
aimo-0117's "geometric/dyadic sequence with largest term exceeding the sum of
the rest") are structurally different (no two-stage cut-then-claim game, no
discrepancy/LP structure) and would be forcing a match — I do not recommend
citing them as analogous. Honest verdict: **no strong crux precedent**; this
problem's mechanism (alternating claiming = greedy = odd-rank sum, already
proven as Lemma G) appears to be closer to a folklore fact than to any single
cataloged crux move.

### Prior progress
See `results/imo-2026-03/current.md`: full reduction to a discrepancy minimax
`D* = u` is proven and shared; n=1 fully solved both directions; lower-bound
Case A (top piece uncut) proven; GAP L (lower, top piece cut) and GAP U (upper,
general n) both open. All three existing approaches share these same two gaps
because they all attack via explicit-strategy/explicit-cancellation arguments
in the D language.

### Dead ends (do not retry)
- Separable per-piece potential Φ=Σw(piece) — refuted by potential-certificate
  (clean witness + LP infeasibility). Confirmed as a real dead end (checked the
  reasoning: it's correct — a local split's effect on the order-dependent
  odd-rank functional genuinely can have either sign depending on context, which
  no additive potential can capture).
- Bisection-only Xiang / "bisect the n largest" — refuted numerically by two
  independent approaches (n=2: Liu can reach 3/4 or 0.65 against these rules,
  both > c(2)=4/7). Confirmed real: myopic/uniform bisection genuinely cannot
  cap Liu.
- Strategy-stealing / "first cut then recurse on n-1" as a standalone new
  framing (my own check, §3 above) — does not obviously avoid the induction-
  recursion approach's already-identified Case B obstruction (parity
  cancellation under a shared cut budget); not a genuinely new mechanism.

### Small-case / intuition notes (conjectural, labeled as such)
- Numerically (n=2, 3-piece Liu partitions, grid-search Xiang response), the
  function `f(Liu partition) = min_Xiang D` **appears to be concave with a
  strict local max exactly at the dyadic partition** in every one of 5 tested
  directions — this is new evidence (not previously reported by the other three
  approaches) but is only a numerical probe on a coarse grid at one problem size
  (n=2); it is a conjecture, not a proof, and has not been checked at n=3 or with
  a finer grid / more directions.
- The identity `1/c(n) = 2 − 2^{-n}` is exact (verified n=0,1,2,3) and is a
  cleaner-looking but algebraically equivalent restatement of the known
  recursion; flagged as a minor secondary lead, not a new mechanism.
