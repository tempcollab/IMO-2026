## imo-2026-03 — scouting Lemma L (the `k=n`, tail-untouched sub-case)

### Exact statement of Lemma L (as recorded)
From `approaches/recursive-embedding-induction.md` (§ "What Lemma V' reduces
Proposition K to") and `lemmas/alternating-sum-toolkit.md`:

Normalize `t_i := 2^{n-i}` for `i=1..n` (so `T=(t_1,...,t_n)=(2^{n-1},...,1)`
is the geometric tail, `t_n=1`). **Lemma L**: for every `n≥1` and every choice
of nonnegative integers `a_1,...,a_n` with `Σa_i = n+1` and `Σ a_i t_i = 2t_1`
(i.e. `a` is a composition-multiplicity vector for a split of `p_1` into
`n+1` anchor-valued parts), the merged multiset `T ∪ {t_i with extra
multiplicity a_i}` has alternating sum `D ≥ t_n (=1)`. Verified by full
enumeration (not sampling) for `n=1,...,7` (`current.md` says up to 8);
minimum is uniquely attained at the "canonical" vector `a_i=1 (i<n), a_n=2`.
This is the vertex-reduced (via Lemma V', LP-vertex argument) end-state of
Proposition K, itself the `k=n` (all marks on `p_1`, tail untouched)
instance of the general lower-bound gap.

### Is Lemma L secretly the same claim as the round-2 "doubling family" conjecture?

**Yes — confirmed, for the `k=n` instance specifically.** In
`geometric-dominance-construction.md` (round 2, §"Attempt 2: general k, tail
untouched"), the "doubling family" is defined as
`C_k := {p_2,...,p_{k+1}, p_1 - Σ_{i=2}^{k+1}p_i}`, and the open claim there
is "no `(k+1)`-part composition of `p_1` beats `C_k`'s odd-sum, for every
`0≤k≤n`." I checked by direct substitution: at `k=n`,
`p_1 - Σ_{i=2}^{n+1}p_i = p_{n+1}` (Lemma 2's identity `(∗)`), so
`C_n = {p_2,...,p_n, p_{n+1}, p_{n+1}}` — exactly Proposition 4's
exact-equality construction, and exactly Lemma L's "canonical vector"
(`a_i=1` for `i<n`, `a_n=2`, in the `t_i=p_{i+1}` relabeling). So:

- The round-2 "doubling family" conjecture, restricted to `k=n`, **is
  literally Lemma L** (same extremal object, same claimed minimality),
  just stated once as an unproved continuous-LP/numerical-optimizer
  observation (round 2, verified `n≤5` via `scipy` + exact-`Fraction`
  family check) and once — this round — as a *reduced, finite, exactly
  verified* integer combinatorial statement (`n≤7-8`) after the rigorous
  Lemma V' vertex-reduction closes the gap between "checked a family" and
  "checked the true LP minimum."
- Lemma L is **strictly sharper progress** on the same claim: round 2 only
  had numerical evidence that `C_k` beats a scipy-searched competitor;
  round 3/4's Lemma V' proves (not just observes) that the true minimum
  *must* occur at an anchor/near-anchor vertex, then Lemma L is the
  remaining finite check. Closing Lemma L for general `n` closes both the
  `k=n` doubling-family instance and (as the reduced form) is the natural
  first rung of a full induction on `k` that would settle the general
  "doubling family" claim for all `k≤n`.
- **High value confirmed**: a general proof of Lemma L is not a third,
  independent open problem — it *is* the `k=n` case of the shared gap
  named in `current.md` gap 1, phrased in the cleanest available
  (integer, finite, exactly-checkable) form. Any progress on Lemma L
  should immediately be checked against whether it generalizes to `k<n`
  (extending Lemma V' to the "tail-also-refined" case is explicitly
  flagged open in gap 1(b) — the vertex-reduction argument's proof did
  not use `T`'s fixedness essentially, per the approach file, but this
  was not verified this round).

### Is Lemma L the same claim as Claim ★'s `s≥3` counterexample (insertion-and-abstract-reduction.md)?

**Related but NOT the same claim — different generality axis.** Claim ★ is
an *abstraction*: it tries to bound `oddrank(R∪T)` using only two scalar
summaries of `T` (`max(T)` and `oddrank(T)`), for **arbitrary** `T`
satisfying those summaries and **arbitrary** `s`-part composition `R` of
`2q`. It is proved for `s∈{1,2}` and refuted for `s≥3` by an explicit
adversarial `T` (`={1/8}`) and adversarial 3-part `R` chosen so no part of
`R` dominates `T`.

Lemma L is the **opposite regime**: `T` is not adversarial or abstracted at
all — it is the fully explicit, fixed geometric tail (`t_i=2^{n-i}`
exactly), and `s=k+1=n+1` can be much larger than 3. So the Claim ★
counterexample does **not** refute Lemma L; it only refutes the specific
*proof strategy* of reducing an arbitrary-`T` sub-case to a 2-summary
abstraction and hoping the same one-shot insertion argument (Lemma I) works
for `s≥3`. This is exactly consistent with `geometric-dominance-
construction.md`'s own diagnosis under "Attempt 2": *"the clean 'insert the
dominant element first' argument no longer applies [for k≥2] without a
genuinely new idea."* Claim ★'s counterexample is the rigorous, general
confirmation of *why* that diagnosis is correct — it shows the insertion-
only method is provably insufficient once `s≥3`, for **any** `T`, not just
the geometric one. Lemma L survives this because it does not rely on
Claim ★'s abstraction; it uses `T`'s exact ratio-2 structure via Lemma
D-INSERT/V' machinery instead.

**Conclusion on the relationship:** Claim ★ (`s≥3` counterexample) explains
why the *general, T-agnostic* route to `k≥2` is structurally dead — this
constrains what kind of proof of Lemma L can work (it must use `T`'s actual
values, not a 2-number summary — consistent with what Lemma V'/D-INSERT
already do). It is not the same combinatorial statement as Lemma L, but it
is a **certified negative constraint on Lemma L's proof space**: ruling out
"treat the tail via `(max(T),oddrank(T))` only" as a viable strategy, even
though the k=n/tail-untouched instance (Lemma L) does not literally need
that abstraction since its `T` is fully known.

### Candidate proof strategies for Lemma L (not attempted — for the outliner)

1. **Peel-the-top-block induction on `n`, mirroring Lemma D-BOUND's own
   induction.** Write `c_1 := a_1+1` (multiplicity of the top value `t_1` in
   the merge). By Lemma D-INSERT's block formula, block 1 contributes
   `±t_1` to `D` if `c_1` is odd, `0` if even, and the *sign of the next
   block* depends on the parity of `c_1` (i.e. whether the remaining
   `2n+1-c_1` elements start counting from an odd or even position). This
   suggests a genuine strong induction on `n` where the inductive
   hypothesis is Lemma L at `n-1`, applied to `t_2,...,t_n` (which is
   exactly `2×` the `t_i`-normalization for level `n-1`, since
   `t_{i+1}=t_1/2^i` matches Lemma 3's self-similarity) — case-split on the
   parity of `c_1` and on whether `a_1=0` (no extra copies of `t_1`, i.e.
   `k<n` really, already covered) vs `a_1≥1`. This looks like the most
   direct route and reuses already-certified tools (D-INSERT, D-BOUND,
   Lemma 3's self-similarity, Lemma G1's `c(n)=2λ_n c(n-1)` recursion) —
   likely the strategy to hand the next builder.
2. **Discrete exchange/rearrangement argument directly on the vertex `a`
   vector.** Since Lemma V' already reduces to (at most one free
   coordinate, else) integer anchor vectors, a local-move argument
   ("moving one unit of multiplicity from `a_i` to `a_{i-1}`/`a_{i+1}`,
   preserving the two linear constraints, never decreases `D`") would
   directly prove the canonical vector is the unique minimizer without
   needing a separate induction on `n`. This is the "exchange argument"
   pattern common in the crux corpus's `extremal-principle` /
   `induction-and-construction` subtopics (e.g. aimo-0333's "exchange
   argument swapping a pigeonhole-repeated block").
3. **Reformulate as a base-2 digit/carry statement.** The constraint
   `Σ a_i 2^{n-i} = 2^n` is literally "a representation of `2^n` using
   `n+1` parts drawn from `{2^{n-1},...,1}` with prescribed total part
   count `n+1`" — structurally close to classical "representations of a
   power of 2 as an ordered/multiset sum of smaller powers of 2" problems
   (carries, greedy binary expansion). Worth trying a direct combinatorial
   encoding (e.g. via binary carries of `a_i` against the all-1s vector)
   rather than the LP/alternating-sum route, though this has not been
   tried by either approach yet.

None of these is attempted or verified beyond what's already on file —
flagging as candidate directions only.

### Cheap-kill candidates
- **None obvious that would kill Lemma L quickly** — it has already survived
  full enumeration to `n=7/8` with the extremal vector unique and matching
  the construction exactly; no parity/pigeonhole quick disproof is visible.
  The likely path is a genuine (if short) inductive proof, not a
  counterexample search.
- One thing worth a cheap check next round: verify computationally whether
  strategy 2 (single-unit local exchange) actually monotonically decreases
  `D` when moving away from the canonical vector, for `n` up to ~10 — this
  is a fast `Fraction`/integer script and would strongly derisk strategy 2
  before a builder commits to writing it up.

### Knowledge-base entries relevant
Nothing in `knowledge_base.md` was found specific to alternating-sum/rank
games; the relevant machinery is entirely internal (Lemma 1, Lemma 3,
D-REFORM/D-BOUND/D-INSERT/V', Lemma I/Claim ★). (I did not find a
generically-named "minimax on sorted lists" or "alternating sum" entry in
`knowledge_base.md` — worth double-checking with a direct grep if the
outliner wants to cite something external, but the existing certified
lemma files already are the load-bearing tools.)

### Analogous past problems (cruxes)
Searched `combinatorics`/`number_theory` subtopics `games-and-strategy`,
`extremal-principle`, `inequalities-SOS-and-convexity`, `p-adic-valuation`,
`invariants-and-monovariants` for "alternating sum," "sorted," "power of
two," "binary representation," "compositions," "claim/take turns." No crux
is a tight match to Lemma L's exact block-parity/alternating-sum claim.
Two loosely-analogous ones, worth a look but NOT close enough to import a
move from directly:
- **`aimo-0764`** (Sir Alex's cell game: build `2^n` in a row of 9 cells by
  repeatedly merging equal powers of 2; the certified crux move is "bound
  occupied cells below by the base-2 popcount of the total, via a lemma
  that a fixed sum of powers of 2 needs at least popcount(total) terms
  unless merges happen"). Thematically close (representations of a power
  of 2 as sums/merges of powers of 2, with a counting lemma), but the
  actual mechanics (merge game vs. alternating-sum-of-sorted-list) are
  different enough that no direct move transfers.
- **`aimo-0117`** (stone-game with two boxes; crux move: assign a two-sided
  dyadic/geometric sequence so the largest value strictly dominates the sum
  of all later ones, then defer commitment). Same *flavor* of dyadic
  domination as this problem's own Lemma 2/geometric construction (already
  independently discovered and certified here), not new information for
  Lemma L specifically.
- Conclusion: **no crux is a genuine solution-transferable analog for
  Lemma L**; the alternating-sum/block-parity formulation appears to be a
  bespoke construction of this problem, not a standard corpus pattern.

### Prior progress (Lemma L specifically)
Certified tools feeding it (D-REFORM, D-BOUND, D-INSERT, Lemma V') are all
independently reviewer-verified. Lemma L itself: verified by full
enumeration for `n=1..7` (approach file) / `n=1..8` (per `current.md`'s
summary — check which is authoritative, minor discrepancy, not
substantive), extremal vector always unique and matches the canonical
`C_n`/Proposition-4 construction. **Not proved for general `n`.**

### Dead ends (do not retry)
- The "Refuted Candidate Lemma" (bounding `evenrank(S∪T)` by `Σ(T)` alone,
  ignoring individual values) — proven false by an exact counterexample in
  round 2. Any attempted proof of Lemma L that reduces to this sums-only
  bound will fail; already ruled out.
- Claim ★ generalized naively to `s≥3` using only `(max(T),oddrank(T))` —
  proven false (see above). Do not attempt to prove Lemma L via this
  2-summary abstraction of the tail; must use `T`'s exact ratio-2
  structure.
- `majorization-smoothing` (global concavity of `V(p)` framing) — proven
  dead via a structural non-concavity obstruction (`min` of concave and
  convex pieces); irrelevant to Lemma L directly but confirms the general
  "smooth/convex-analysis shortcut" family of approaches is not viable here
  either — reinforces that Lemma L likely needs a discrete/inductive
  argument (strategy 1 or 2 above), not a continuous-optimization shortcut.

### Small-case / intuition notes (conjecture, not proof)
- The extremal vector is always the canonical one (`a_i=1, i<n`; `a_n=2`),
  matching Proposition 4's construction exactly — strong (but only
  small-`n`, exhaustive-not-asymptotic) evidence that Lemma L is a true,
  provable statement, not an artifact that breaks at larger `n`.
  Uniqueness of the minimizer (not just achieving the bound) at every
  tested `n` is itself informative: it suggests an inductive proof should
  be able to show *strict* inequality away from the canonical vector,
  which is often easier to induct on than a non-strict bound with many
  ties.
- Given the confirmed identity between Lemma L (`k=n` case) and the
  round-2 doubling-family conjecture, a proof of Lemma L should be framed
  by the outliner as directly resolving (not just partially informing) one
  named open sub-claim from two independent approaches at once — worth
  flagging in the outline as a priority target with double payoff.
