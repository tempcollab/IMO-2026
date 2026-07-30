## imo-2026-04 (Mulan's Triangle Game) — Shan-Yu's defense / adversarial lens

### Setup used throughout (verified algebraically + numerically)
Cutting at vertex with angle `a` (other two angles `b`, `c`, `a+b+c=180`) via a point P on
the side opposite `a`, parametrized by `x = angle(B,A,P) ∈ (0,a)`, produces exactly two
children:
- Child1 = `(b, x, a+c-x)`
- Child2 = `(c, a-x, b+x)`
(P's two angles at the cut are automatically supplementary; the split of `a` and the P-angle
are linked, not independent — confirmed by direct angle-sum bookkeeping and matches
`x=a`→Child2 degenerates / `x=0`→Child1 degenerates checks.)
Mulan's real move each turn is a **triple choice**: which vertex to split (a, b, or c) AND
the value x in the open interval — a genuinely 1-parameter-continuous choice per turn, times 3
branch choices of which vertex.

### Key structural fact: when can Mulan force a "double threat" (both children forced to contain θ, so Shan-Yu has NO safe reply that turn)?
Solved the 2×2 system exhaustively (child1 needs `x=θ` or `x=a+c-θ`; child2 needs `x=a-θ` or
`x=θ-b`; the "both children already have angle θ" case is excluded since the round-start check
would have ended the game already). Only two non-degenerate solutions exist:
1. **Case "vertex-doubling"**: `a = 2θ` (any vertex angle of the CURRENT triangle equals `2θ`,
   with `θ<90` so `2θ<180` is a valid angle) — then splitting that vertex at `x=θ` forces
   BOTH children to contain angle θ, regardless of which Shan-Yu keeps.
2. **Case "θ=90 universal"**: `a+b+c=2θ` — this is `180=2θ`, i.e. **θ=90 exactly** — and it holds
   for ANY triangle, not just a special one: picking the vertex `a` to be whichever angle is
   allowed to be ≥90 (always possible, since a triangle has at most one angle ≥90) and setting
   `x* = 90-b = a+c-90`, BOTH children get an angle of exactly 90°. **Verified numerically**
   (random triangle (34.39°,73.96°,71.66°) → children (73.96,16.04,90.00) and (71.66,18.34,90.00),
   both containing 90 exactly).

These are the ONLY two mechanisms by which a single move can leave Shan-Yu with zero safe
reply. (Other sign combos of the 2×2 system force a degenerate zero angle, impossible.)

### Consequence: a clean recursive characterization of Mulan's winning θ
Since Mulan's entire winning strategy must terminate at a double-threat move, and that move
requires either θ=90 (works immediately, from ANY triangle) or the *current* triangle already
having a vertex angle exactly `2θ` (requires θ<90), Mulan's problem for target θ<90, θ≠90
reduces to: *can she force the appearance of angle `2θ`* — which is exactly the same
sub-problem one level up (target `2θ` instead of `θ`), because reaching `2θ` is not itself a
stopping condition, so Shan-Yu will fight to avoid it exactly as hard as he fights θ, and the
identical case analysis applies to that sub-goal. This yields the recursion
`WIN(V) ⟺ V=90 or (V<90 and WIN(2V))`, and for `V>90` strictly, WIN(V) is **false** outright
(neither branch available: `2V>180` is not a valid angle, and `V≠90`).

Unwinding: **WIN(θ) is true iff the doubling orbit θ, 2θ, 4θ, 8θ, ... lands exactly on 90**,
i.e. **θ = 90/2^k for some integer k≥0** (θ = 90°, 45°, 22.5°, 11.25°, 5.625°, ...). If the
orbit ever strictly exceeds 90 without hitting it exactly (which happens for every non-dyadic
θ, and for every θ>90 immediately at k=0), the chain is dead and — on this analysis — Mulan
has no forcing mechanism at all.

**Numerically verified constructively**: from triangle (50,60,70), θ=45 (=90/2):
step 1 splits vertex 50 at x=90-60=30 → children (60,30,90) and (70,20,90) (both hit 90,
confirming Case 2). Step 2, from EITHER child, splits the 90° vertex at x=θ=45 → both
grandchildren contain 45° exactly: (60,30,90)→(60,45,75) and (30,45,105); (70,20,90)→
(70,45,65) and (20,45,115). So θ=45 is forced in exactly 2 moves from an arbitrary start,
matching the recursion exactly.

### Shan-Yu's escape (this lens's actual assignment)
If θ is not of the form 90/2^k, the forward doubling orbit of θ either overshoots 90 at some
finite stage `k` (giving a **finite** "poisoned set" `D = {θ, 2θ, 4θ, ..., 2^{k-1}θ}`, all <90,
after which the orbit escapes into the >90 region where no mechanism exists) or, if θ>90 to
start, `D={θ}` alone. Conjectured Shan-Yu strategy: **pick a starting triangle with no angle in
D, and at every round keep whichever child stays farthest (in the exact-equality sense) from
every element of D** — since a double-threat against value `V∈D` requires the *current*
triangle to already carry `2V` exactly (a single codimension-1 condition), and Shan-Yu only
needs one of his two children to dodge all of D, which fails only exactly at the case-1/case-2
configurations captured above. Numerically simulated 500 rounds of a locally-adversarial Mulan
(brute-force search over an x-grid, 3 vertex choices, greedy "minimize Shan-Yu's best safety
margin") against a Shan-Yu who avoids `{θ,2θ,4θ,8θ}` for θ=60°, starting from (20°,50°,110°):
Shan-Yu survives all 500 rounds without ever hitting 60° or triggering a double-threat (final
state (0.12°, 59.96°, 119.92°) — close but strictly off 60, consistent with "generic avoidance
always has room" on a continuum). This is evidence, not a proof — the search is a finite-grid
heuristic, not exhaustive over Mulan's true continuum of moves, and does not itself rule out a
smarter Mulan strategy outside the "single-target-chain" framework.

**Open gap for the outliner**: my derivation assumes Mulan's *only* useful strategy is a
"single value forcing chain" (θ → 2θ → 4θ → ... → 90). I have NOT ruled out a fundamentally
different multi-branch strategy where different Shan-Yu replies get funneled toward
*different* dangerous targets that all eventually converge on a double-threat for θ — i.e. a
genuine game tree, not a simple chain. This is the actual gap to close rigorously (most likely
by an explicit potential/invariant argument for Shan-Yu, e.g.: maintain the current triangle's
angles bounded away, by a fixed multiplicative or additive margin from the finite set D, and
show every Mulan move leaves at least one child still outside a slightly relaxed margin — a
standard "safety cushion shrinks by a bounded factor each round but never reaches 0" argument;
or a cleaner one showing D is literally forward-invariant-avoidable because it's finite and
Shan-Yu has a continuum of angle choices to dodge with).

### Distinct openings (for the outliner to pick from / diversify against)
1. **Forward/Mulan-side chain-forcing construction** (what I built above): prove Mulan wins
   exactly at θ=90/2^k by explicit induction on k, giving the constructive `k`-move winning
   strategy (base case θ=90 done in 1 move; inductive step reduces target θ to target 2θ).
2. **Shan-Yu-side finite-forbidden-set avoidance invariant** (this lens): show that whenever θ
   is NOT of that dyadic form, Shan-Yu can maintain, forever, a triangle whose angles avoid a
   FINITE set of forbidden real values, by a strict-inequality / open-condition compactness
   argument (each round the "unsafe" x values are finitely many isolated points/threats, so a
   generic choice always exists for at least one child). This is the necessary matching lower
   bound to opening (1); it is exactly the piece assigned to me and it is currently only
   numerically supported, not proven.
3. **Reflection/complementary-angle framing** (untried, flagged not fully explored): since
   only θ=90 has full "universal" 1-move power, consider whether θ and 180-θ (or some other
   involution) interact — checked and found NO symmetry θ↔180-θ in this game (the angle-sum
   constraint a+b+c=180 breaks any such duality), so this avenue appears to be a dead end, but
   worth the outliner double-checking independently since it's a natural first guess to rule
   out explicitly in the proof write-up.
4. **Degenerate-triangle / P-angle-only framing** (partially explored, not pursued further):
   thinking of Shan-Yu driving the triangle toward a very thin sliver (one angle → 0, one →
   180) does NOT obviously help or hurt — the recursion above is scale/shape-invariant and
   works from ANY starting triangle including thin ones, so extreme degeneracy is not needed
   by Mulan and does not obviously help Shan-Yu either; not the right invariant to chase.

### Candidate technique(s)
- Elementary triangle angle-chase + explicit algebraic case analysis (the 2×2 system above) —
  no deep theorem needed, this is a "compute all the ways a double-threat can occur" problem.
- Induction on a doubling/binary-expansion structure (dyadic rationals of 90°) for the Mulan
  side.
- For the Shan-Yu side: an explicit invariant / potential argument (finite forbidden set +
  strict avoidance), analogous in flavor to "invariants & monovariants" and "pursuit" style
  survival arguments.

### Cheap-kill candidates
- At most one angle of any triangle can be ≥90° (used directly in the θ=90 universal proof).
- The "both branches of a 2-equation linear system in x coincide" check (used to enumerate all
  double-threat mechanisms) is a 4-case finite check, cheap to redo/verify from scratch.
- Parity/orbit-termination check: `2^k θ = 90` has a solution in nonneg integers k iff θ=90/2^k
  — immediate from unique dyadic factorization, no computation needed.

### Knowledge-base entries to use
- **Invariants & monovariants** (knowledge_base.md line ~117, ~191) — directly the tool needed
  for Shan-Yu's forever-avoidance argument (need a monovariant/invariant showing the finite
  forbidden set stays avoidable every round).
- **Synthetic toolkit: angle chasing** (line ~129) — used throughout for the vertex-split
  angle bookkeeping (child1/child2 formulas).
- No circle/power-of-a-point / Ptolemy entries are relevant here (this problem is pure angle
  arithmetic + combinatorial game structure, not circle geometry).

### Analogous past problems (cruxes)
Searched `combinatorics` / `games-and-strategy` (39 cruxes) in the corpus. Closest in *spirit*
(a real-valued/continuous pursuit-and-avoidance game with a forever-survival side and a
forcing side), though none share the triangle-angle mechanics:
- `aimo-0236` — "token game", 2-adic valuation monovariant, one player nurses a witness to stay
  one step ahead forever (proving infinite survival) while the other's forced move must
  eventually terminate under a different regime. Structurally the closest analogy to Shan-Yu's
  side: a **binary/dyadic doubling-type valuation** driving both the forcing player's win
  condition and the escaping player's survival condition — same flavor as the 90/2^k dyadic
  structure found here, even though the underlying object (2-adic valuations of integers vs.
  triangle angles) is unrelated. Worth reading `aimo-0236`'s crux write-up for HOW it phrases
  the "regime preserved by both players' moves" invariant — likely reusable proof pattern for
  Shan-Yu's forever-avoidance lemma.
- `aimo-0663` — pigeonhole/component-counting to show a responder always has a legal reply
  forever (liveness argument): same general shape as what Shan-Yu needs ("show at least one of
  the two children is always safe"), though the mechanism (counting gaps in a discrete set) is
  discrete, not directly transferable to the continuous-angle setting here.
- No AoPS/crux match on the exact triangle-cutting mechanic; treat these as proof-pattern
  analogies only, not solution sources.

### Prior progress
None — this is the first exploration round (results/imo-2026-04/ was empty at start).

### Dead ends (do not retry)
- None recorded yet by other approaches (population was empty). From my own exploration:
  the θ↔180-θ reflection symmetry idea does NOT hold (checked directly against the a+b+c=180
  constraint) — don't waste a round rediscovering this; note it in the proof write-up as a
  ruled-out red herring instead.

### Small-case / intuition notes (all labeled conjecture except where marked verified)
- **Verified (constructive, not just numeric)**: θ=90° — Mulan wins in exactly 1 move from
  ANY starting triangle. This is a fully proven fact (closed-form x*, checked by direct
  substitution, matches numerically).
- **Verified (constructive)**: θ=45° — Mulan wins in exactly 2 moves from an arbitrary tested
  triangle (50,60,70); the construction is fully explicit and checks out by direct angle
  arithmetic, and by the general recursion this generalizes to ANY starting triangle (the
  θ=90 step is universal, so the first move works from any triangle, and the follow-up step
  needs only "some current angle is 90", which the first move always creates in both children).
- **Conjecture (numerically supported)**: for θ = 90/2^k (k≥0), Mulan wins in exactly k+1 moves,
  by iterating the same doubling construction; strongly believed to generalize but the general
  inductive proof (any k) has not been written out formally — that's for the outliner/builder.
- **Conjecture (numerically supported, 500-round simulation)**: for θ NOT of the form 90/2^k
  (tested θ=60°), Shan-Yu can survive indefinitely by avoiding the finite forbidden orbit
  `{θ,2θ,4θ,...}` (stopping once the orbit exceeds 90). This is the piece most needing a real
  proof — likely via an explicit "safety margin never reaches zero" argument, or a cleaner
  compactness/genericity argument since the forbidden set is finite and each round only
  threatens Shan-Yu via isolated exact-equality conditions.
- **Answer conjecture**: Mulan can force a win in finitely many steps **iff θ = 90°/2^k for
  some integer k ≥ 0** (θ ∈ {90°, 45°, 22.5°, 11.25°, 5.625°, ...}), otherwise Shan-Yu can
  survive forever. This is a clean, olympiad-plausible characterization (a countable dyadic
  set), consistent with all constructive checks performed. The remaining rigor gap is entirely
  on the "Shan-Yu escapes for all other θ" direction — the outliner should treat proving that
  as the primary remaining lemma, since the Mulan-wins direction (explicit k-move construction)
  is already essentially complete and just needs writing up as a clean induction.
