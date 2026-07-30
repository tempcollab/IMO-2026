## imo-2026-04

Population was empty entering this round (first outline pass). All three approaches below are
NEW. `mcp__approach-ranker__register_approach` was not available in my toolset this round (only
`sample_approaches` was exposed) — the approach files below are written per the file contract;
whichever role owns registration should register these three slugs:
`chip-double-force`, `budget-partition-dimension`, `three-distance-avoidance`.

Verified independently this round (Bash/Python + hand algebra): the "Double-Forcing Lemma"
existence condition (∃ angle `t<θ` and angle `u<(n-1)θ` among the three) holds **exactly** when
not all three angles are `≥θ`, on 20 random triangles across random `n∈[3,8]` — this is the
crux mechanism of the forward-direction construction below and is solid.

---

chip-double-force: new
Target: Mulan can force a win in finitely many moves **iff** θ = 180°/n for some integer n≥2.
Technique: Two-lemma explicit induction on n (constructive strategy) for the forward direction;
linear-independence / "pure vs impure angle" genericity argument for the converse.
Skeleton:
  1. Master cut formula (exterior-angle theorem) — cite/re-derive, already triple-verified by
     explorers.
  2. **Lemma 1 (Double-Forcing)**: if not all angles ≥θ, one move forces Shan-Yu into a triangle
     with a vertex angle exactly (n-1)θ (or he loses immediately) — by t/u/w case analysis
     (proven, see file).
  3. **Lemma 2 (Chip-Reduction)**: if all angles ≥θ, ≤(n-2) deterministic chip moves (split at
     x1=θ, Shan-Yu forced away from the θ-child) produce an angle <θ — by strict decrease of the
     split vertex, bounded since it starts ≤(n-2)θ (proven, see file).
  4. Strong induction on n: base n=2 (θ=90°, classical 1-move universal win, Lemma 1 degenerates
     to the double-win case). Inductive step: apply Lemma 2 if needed, then Lemma 1, then chip
     the resulting kθ-vertex down to 2θ (k-2 further deterministic moves), then the 2θ-vertex
     split gives a genuine double-threat (both children forced to θ) — total O(n) moves, finite.
  5. Converse: choose a starting triangle with two free angles a0,b0 such that {1,a0,b0,θ} are
     ℚ-linearly independent (exists, open dense). Define "pure"/"impure" angles by whether their
     ℤ-affine expansion in this basis has zero a0,b0-coefficients. Impure angles can never equal
     θ exactly. Show (by induction on the game tree) Shan-Yu can always retreat to a
     child preserving "not currently at θ", using that Lemma 1's double-threat mechanism requires
     either θ=90 (excluded) or an existing angle =2θ exactly (impossible from a non-resonant
     start) — needs to be checked at ALL depths, not just depth 1 (open gap).
Key lemmas (claim + mechanism):
  - Double-Forcing Lemma — because the two P-angles of any cut are automatically supplementary
    (sum 180=nθ), so forcing one to θ forces the other to (n-1)θ exactly.
  - Chip-Reduction Lemma — because a single-target chip move (x1=θ) is a forced deterministic
    transition (Shan-Yu's only non-losing reply), strictly decreasing the split angle by θ each
    time, bounded by the starting value ≤(n-2)θ.
  - Genericity/impurity invariant (converse) — because θ is a "pure" real relative to the basis
    {1,a0,b0,θ} of the generic starting choice, and no ℤ-linear combination with a nonzero
    a0 or b0 coefficient can equal a pure value, by linear independence over ℚ.
Open gaps: converse direction is NOT closed — need the full induction (all move types, all
depths) showing Shan-Yu always has an impure/safe escape; forward direction is essentially
complete (both lemmas proven, induction laid out) but needs final write-up polish and an
explicit small-n worked example (n=3,4,5) for the builder to sanity check against.
Cases to cover: n=2 base case (handled specially — θ=90 is the degenerate double-win); "all
angles ≥θ" vs "some angle <θ" case split at every level of the induction (both covered).
Watch out for: degenerate coincidences where a+c-x1 accidentally also equals θ (need genericity
of Mulan's chosen x1 relative to OTHER equations, not just the targeted one — should not affect
correctness since an extra coincidental win is still a win, but worth the builder noting
explicitly rather than silently assuming); the converse argument's claim that "impure stays
impure/safe under EVERY move type" is currently checked only for the simple chip move, not the
P-angle-targeting move or arbitrary untargeted moves — this is the crux remaining gap.

budget-partition-dimension: new
Target: Same characterization (θ=180/n, n≥2 integer) — alternative routes to both directions.
Technique: Divide-and-conquer budget-splitting (n=p+q) for an alternate forward construction;
codimension/proper-subvariety induction on the AND-OR win-set W_d for the converse.
Skeleton:
  1. Master formula (shared, cite chip-double-force.md).
  2. Attempt to generalize Lemma 1 to a general split n=p+q (both >1): does there exist t<pθ,
     u<qθ among the three current angles whenever not all three exceed both thresholds? Not yet
     proven for general p,q (only the p=1 case is proven, in the sibling approach).
  3. If (2) succeeds: T(n) ≤ 1+max(T(p),T(q)) gives an O(log n)-depth construction via
     divide-and-conquer, recommended to be checked by hand against chip-double-force's O(n)
     construction on n=4,5,6 first.
  4. Converse: define W_d = triangles Δ from which Mulan wins in ≤d moves; claim each W_d is a
     finite union of proper (codimension ≥1) algebraic subsets of the plane {a+b+c=180} unless
     nθ=180, via checking each "exact-hit" equation used in the AND-OR recursion is a nontrivial
     linear constraint on (a,b,c) unless it reduces to an identity forced by a+b+c=180 (which
     happens exactly at nθ=180). Inductive step W_d proper ⟹ W_{d+1} proper is NOT yet done.
Key lemmas (claim + mechanism):
  - General p,q double-force existence (CONJECTURED, unproven) — because presumably the same
    "sum exceeds a threshold" argument as Lemma 1 generalizes, but the case count grows with p,q.
  - W_d codimension claim — because each forcing equation, viewed as a polynomial (linear)
    constraint on (a,b,c,θ), is either an identity (using a+b+c=180=nθ) or cuts a proper subset;
    Shan-Yu escapes proper subsets by choosing a starting triangle outside their (countable, at
    each fixed d) union.
Open gaps: the general p,q forcing lemma is unverified (may not even be true or may need many
sub-cases); the "W_d proper ⟹ W_{d+1} proper" induction step and the passage to d→∞ (need a
single triangle avoiding ALL W_d simultaneously, which is really the same genericity argument as
chip-double-force.md's converse, just packaged differently) is not completed — flagged in the
file as likely mergeable with chip-double-force.md's converse rather than fully independent.
Cases to cover: same n=2 base case; also need p=1 or q=1 as the degenerate case matching Lemma 1.
Watch out for: this approach's forward-direction novelty (O(log n) vs O(n) moves) is NOT needed
for the problem (only finiteness matters) — do not let the builder over-invest in optimizing
move count at the expense of correctness; if the general p,q lemma proves awkward, this approach
should defer entirely to chip-double-force.md's forward construction and focus builder effort
only on the converse codimension framing.

three-distance-avoidance: new
Target: Same characterization — this approach's sole distinct contribution is a different
*tool* (equidistribution / three-distance theorem) attempted on the converse direction; forward
direction is explicitly imported from chip-double-force.md, not re-derived.
Technique: Number-theoretic framing of the additive group G=θℤ+180ℤ, distinguishing the case
180/θ=n∈ℤ (θ generates G directly) from 180/θ=p/q non-integer rational or irrational (θ is a
proper multiple of G's true generator θ/q) — flagged as the least mature approach, needs a
validity spot-check before further investment.
Skeleton:
  1. Import forward direction from chip-double-force.md wholesale (no independent derivation).
  2. Compute G=θℤ+180ℤ: if 180/θ=n∈ℤ, G=θℤ (θ is primitive). If 180/θ=p/q in lowest terms with
     q≥2, G=(θ/q)ℤ, so θ=q·(generator) — θ is NOT primitive in G.
  3. (Gap, unproven) Argue this non-primitivity obstructs any UNIVERSAL forcing strategy (one
     that works from every starting triangle), because... — mechanism not yet nailed down; the
     "angles don't literally live on a circle mod L" mismatch is a real, currently unresolved
     obstacle to applying the three-distance theorem directly.
Key lemmas (claim + mechanism):
  - G-primitivity dichotomy — because gcd(p,q)=1 implies ℤ+(p/q)ℤ=(1/q)ℤ as subgroups of ℚ,
    a standard number-theory fact (elementary, easy to verify).
Open gaps: EVERYTHING past step 2 — the connection between "θ non-primitive in G" and "Shan-Yu
can survive" is currently only a heuristic analogy, not a proof; the three-distance theorem's
applicability is unconfirmed since the triangle-angle state space is not literally a circle.
Cases to cover: none enumerated yet (approach too immature).
Watch out for: per the file, the very next step for any builder assigned this slug should be a
cheap numerical sanity check (θ=50°, p/q=18/5) against explorer-verify's existing sweep data
BEFORE investing further proof effort — if the G-primitivity heuristic doesn't explain that data
point cleanly, abandon this approach in favor of chip-double-force.md's converse mechanism
(which already has a cleaner, partially-worked mechanism). This approach is a lower-priority
"insurance" slug, not the primary bet.

---

Recommended build-set for this round: **chip-double-force** (highest priority — forward
direction is essentially complete, needs write-up + the converse induction pushed further) and
**budget-partition-dimension** (secondary — mainly for the converse codimension framing, which
may cross-pollinate with chip-double-force's converse gap; the forward-direction novelty there
is optional/lower priority). **three-distance-avoidance** should get at most a light validity
check this round before further investment, since it is the least mature and most likely to be a
dead end — flagged explicitly as insurance diversity, not a primary bet.
