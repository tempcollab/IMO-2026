## Lens: Hall's-marriage / exact-cover / subset-sum-matching reformulation for Claim PTBI Case C (general m≥4)

### 0. Correction to a premise in my brief

The brief describes "the m=5 witness A=(12,6,5,4,2)/29 giving oddrank=1/2<c(4)" as the
witness showing the current menu is insufficient. That is not quite right and I want to
flag it before anything else so the next round doesn't inherit a wrong target:

- `A=(12,6,5,4,2)/29` (round 9) is the witness the certified menu (BLOCK-RECURSE +
  DOUBLE-INSERT + TAIL-SNIP) **failed** on (best menu value `15/29 > c(4)=16/31`), but it
  was subsequently **closed** by Lemma PAIR-VALUE's SUBSET-DOM corollary, which matches
  `p_2 → {p_4,p_5}` (a non-prefix subset match) to get exactly `oddrank=1/2 < c(4)`. This
  witness is *solved*, not open.
- The witness that actually still defeats the **current, larger** menu
  (DOM, HALVE, MULTI-HALVE, BLOCK-RECURSE, TAIL-SNIP, PAIR-VALUE/SUBSET-DOM,
  ALL-BUT-MIN, MATCH-TAIL-PAIR) is the **round-10** one:
  `A = (1826,1563,1520,1514,765)/7188`, m=5, Σ=1, p_1≈0.254<1/2 (Case C holds).
  Neither ALL-BUT-MIN's threshold (`p_5≤1/31`) nor MATCH-TAIL-PAIR's threshold
  (`p_4-p_5≤1/31`) fires; their best value is `7937/14376≈0.5521`, exceeding
  `c(4)=16/31≈0.5161` by ≈0.036. A corrected brute-force search shows the true optimum
  `1199/2396≈0.5004` is achieved only by a **5-move deep recursive composition**
  (halve p_1; halve p_2; match p_3 to p_4 [near-tied residual ≈0]; then recursively
  match/halve several of the newly-created fragments against each other) — not an
  instance of any single closed-form lemma in the menu.

So: the concrete obstruction to focus on is the round-10 witness, not the round-9 one.
Everything below is about *that* obstruction.

### 1. What the Hall-deficient-set-deletion crux (aimo-0063) actually says, and whether it fits

`aimo-0063` (necklace/arc-fair-division, subtopic `graph-theory-and-connectivity` +
`induction-and-construction`) proves: fix one person Pip and her n arcs; build the
bipartite graph (people) × (Pip's arcs), edge iff a person values that arc ≥1. If no
perfect matching exists, Hall's theorem gives a deficient set B₁ (fewer neighbors than
members); **delete B₁ and its whole neighborhood**, and recurse on the *remaining*
graph, repeating until the survivors satisfy Hall's condition (guaranteed to terminate
nonempty because Pip herself is a universal vertex — any set containing her can never be
deficient, since her neighborhood is literally all n arcs). Commit the resulting partial
matching M (which is honest to be non-full — only the non-deficient part is matched).
Then a **second, independent** crux move finishes the induction: every *unmatched*
person Q has, by construction, value <1 on every committed arc (else Q would have been
an edge into M's target set), so deleting a committed arc merges at most two of Q's own
pieces into one whose value is still ≥1 (since (≥1)+(≥1)−(≤1)≥1) — this is what lets the
reduced instance still satisfy the induction hypothesis for the untouched people.

**Does this transfer here? Honestly: not directly, and the disanalogy is real, not
cosmetic.**

- aimo-0063's Hall move is a **feasibility/existence** question over a **binary**
  compatibility relation (arc worth ≥1 to a person, yes/no) — the graph is fixed in
  advance and Hall's theorem is applied to a genuine 0/1 bipartite adjacency structure.
  Our Case C problem has no such binary relation: whether a "donor" piece can profitably
  match a "target" subset is not a yes/no compatibility, it is an **exact numeric
  equality** requirement (the donor's split-off residual must equal the target subset's
  sum exactly, for Lemma PAIR-VALUE/SUBSET-DOM to fire with a clean value) or, in the
  now-needed generalization, a **multi-level recursive subset-sum problem** (the round-10
  witness needs the *newly created fragments* from earlier moves to themselves be matched
  further). There is no natural bipartite graph here whose Hall-deficient sets correspond
  to "the menu fails" — Hall's marriage theorem answers "does *some* system of distinct
  representatives exist," but our question is "does some numeric *value assignment*
  (subset partition into exactly-summing groups) exist that meets a specific numeric
  target `c(m-1)Σ`," which is an exact-cover / subset-sum flavor problem, not an SDR
  existence problem. Reformulating "donor i is compatible with target-set S" as an edge
  would require first *fixing the split ratios*, but the split ratios are exactly the free
  continuous parameters we are trying to choose — so the bipartite graph would have to be
  built *after* solving the continuous optimization, which is circular.
- The one part of aimo-0063's *mechanism* that could plausibly transfer, in spirit rather
  than letter, is the **peel-off-the-bad-part-and-induct-on-the-rest** shape: don't try to
  build one global closed-form construction; instead argue that *some* prefix of pieces
  can always be peeled off and matched/dominated cleanly (an "easy" region, the analogue
  of the non-deficient survivors), leaving a strictly smaller instance to which the
  induction hypothesis (Claim PTBI at size m−1 or less) applies. But this is exactly
  the shape Round 10's **Fact (Step 3, single-small-peel obstruction)** already proves is
  **provably insufficient**: any construction of the form "make one tied pair, defer to
  the (m−1)-strength IH on the rest" gives a bound `g(v) = c(m-2)Σ + v(1-2c(m-2))`, which
  is *always* worse than the target at `v=0` and only weakly improves — i.e. one level of
  induction is provably not enough, and this is a clean algebraic fact already proved this
  round, not a numerics-only observation. So even if one dresses up "peel the easy part,
  induct on the rest" as a Hall-deficient-set-style argument, it inherits the same
  structural weakness that Step 3 already rules out — deficient-set peeling in aimo-0063
  reduces the *count* of unmatched people by at least 1 each round while preserving full
  IH strength for each; the analogous move here would need to reduce the *induction
  budget* by exactly one level each time it peels, and one level of budget loss is
  already proved fatal.

**Assessment: the Hall's-theorem crux from aimo-0063, taken literally, does not adapt.**
Its load-bearing ingredient (a fixed 0/1 compatibility graph plus a genuine SDR question)
is not present in our problem, which is a continuous/exact-value subset-partition problem,
not a discrete existence-of-matching problem. Anyone tempted to force-fit it should not
spend a round trying to build "the" bipartite graph — there isn't a natural one, and the
reviewer's own framing ("closer to subset-sum/exact-cover") is the more accurate diagnosis
of what's needed, not literally Hall's theorem.

### 2. Precisely why the round-10 m=5 witness (1826,1563,1520,1514,765)/7188 defeats the menu

Every currently-certified constructive lemma (DOM, HALVE, MULTI-HALVE, BLOCK-RECURSE,
TAIL-SNIP, PAIR-VALUE and its SUBSET-DOM corollary, ALL-BUT-MIN, MATCH-TAIL-PAIR) is a
**single-shot, one-level** closed form: each expresses `oddrank(B)` as a fixed algebraic
function of `A`'s values once *one* particular partition-into-tied-pairs-plus-remainder is
chosen, and that partition is chosen from a *finite, fixed menu of shapes* (whole tail
domination, top-K halving, one donor-to-subset match, "all but the min," "the two
smallest"). None of them recurse into the *remainder* using a second independently-chosen
matching of the *same* general type.

The witness's true optimum requires exactly that: halve p₁, halve p₂ (two "self-pair"
moves), match p₃ to p₄ (a near-tied donor/target pair with residual ≈0), and *then*
recursively pair up several of the **newly created fragments** from the first three moves
against each other. That is, the optimal move sequence is a **composition of several
PAIR-VALUE instances stacked on top of each other**, where later instances operate on
values that did not exist in the original `A` — they are only produced by earlier splits.
No lemma in the menu expresses "apply PAIR-VALUE, then apply PAIR-VALUE again to the
result." Concretely:
- ALL-BUT-MIN and MATCH-TAIL-PAIR are each *exactly one* PAIR-VALUE instance (a single,
  fixed pairing of the *original* five pieces) — they cannot see the second-order
  fragment-pairing the optimum needs.
- SUBSET-DOM (also one PAIR-VALUE instance) is likewise one-shot: it matches one donor to
  one target subset of the *original* pieces, once.
- Round 10's Step 3 fact shows *why* stopping after one level and handing the rest to the
  bare induction hypothesis loses too much (the `g(v)` computation): each level of
  induction "spends" a full m-count-reduction's worth of strength, but the true optimum on
  this witness needs the recursive matching machinery itself to go *two or three levels
  deep* without paying the full IH-strength tax at each level — i.e. what's missing is not
  a stronger single formula, but a **general theorem that a good multi-level matching
  sequence always exists**, together with an accounting showing multi-level matching
  moves don't cost a full induction level each.

So the honest gap is: we have a **mechanism** (PAIR-VALUE, and it is not structurally
blocked — Step 1's corrected harness confirms the matching+self-halve framework, applied
recursively, does reach the true optimum on every tested witness) but **no existence
theorem** that some finite-depth recursive application of PAIR-VALUE always closes Case C
for every `m`, and no proof bounding *how deep* the recursion needs to go as a function of
`m` (the round-10 witness needed depth 2–3 out of `m-1=4` marks; it's unknown whether
depth ever needs to scale with `m`, which would matter for a clean induction).

### 3. Other crux moves relevant to this exact-cover/subset-sum matching problem

I queried `past_crux_moves_database.json` (domain=combinatorics, and cross-domain for
"subset-sum"/"matching"/"Hall"/"deficient"/"marriage" keywords). The most relevant hits,
ranked by actual fit (not just keyword overlap):

- **`aimo-0292` (combinatorics, subtopics `induction-and-construction` /
  `extremal-principle`) — genuinely the closest structural analogue found.** This is the
  IMO problem: n blocks each weighing ≥1, total weight `2n`; prove every target `r ∈
  [0,2n-2]` is hit within tolerance 2 by *some* subset sum. The proof is exactly the shape
  our Case C needs: strengthen the claim to "total weight `s≤2n`, tolerance-2 coverage of
  `[-2,s]`," then **induct by peeling the single largest block `x`** — apply the IH to the
  remaining `n-1` blocks to cover `[-2,s-x]`, then **add `x` back** to every subset in that
  covering to get `[x-2,s]` covered, and check the two intervals overlap
  (`x-2 ≤ s-x`, which follows from every block weighing ≥1 forcing `x ≤ s-(n-1)`). This is
  a genuine "approximate subset-sum coverage by one-block-peel induction" result, and it
  is a much closer model for what Case C actually needs (hit a numeric target within
  tolerance via a controlled subset/split choice, proved by peeling one element and
  re-including it) than aimo-0063's Hall move is. **Recommend this as the primary crux to
  adapt for a genuinely new attempt**, not aimo-0063. The adaptation is not immediate —
  our "tolerance" isn't a fixed additive constant like 2, it's the multiplicative slack
  `c(m-1)Σ` versus the achieved value, and our moves are "split and pair" rather than
  "include or exclude a whole block" — but the induction *shape* (peel the extremal
  element, solve the smaller instance, reattach, check an overlap/slack inequality) is
  exactly the shape that's been missing: every one of Round 10's failed attempts peeled
  one element and deferred to the **bare** `c(m-2)` IH; aimo-0292's proof instead peels
  and then does a controlled *reattachment* step whose slack is guaranteed by the
  "every remaining block ≥1" hypothesis. The open question for adaptation: is there an
  analogous per-piece lower bound (like "each block ≥1") in our problem that would supply
  the needed slack after peeling, given our target function is multiplicative
  (`c(m-1)·Σ`) rather than additive? This is worth a dedicated attempt but is genuinely
  new work, not a copy.

- **`aimo-0341` (combinatorics, `extremal-principle` — "defect Hall") and `aimo-0336`
  (`graph-theory-and-connectivity`) — same family as aimo-0063**, both use the identical
  "take a maximal deficient vertex set, delete it and its neighborhood, apply Hall to the
  survivors" move, in a covering/grid or matching-diagonal setting. Same disanalogy as
  aimo-0063 applies: both are 0/1-compatibility existence questions on a fixed graph, not
  exact-value subset-sum problems. Not a better fit than aimo-0063 for the reasons in §1.

- **`aimo-0938` (number_theory, `modular-arithmetic-and-CRT`) — subset-sum via
  Cauchy–Davenport.** Uses a sumset-growth bound (`|{0,c_1}+...+{0,c_m}| ≥ min(p,m+1)`,
  Cauchy–Davenport) to show a subset-sum set covers all of `Z/p`. Same *flavor* as what we
  want (existence of a subset achieving a target value) but the setting is finite/modular
  additive combinatorics, not continuous positive-real optimization with a domination
  structure — the sumset-growth mechanism doesn't obviously transfer to real-valued,
  order-sensitive `oddrank` computations. Low relevance, noted for completeness.

- **`aimo-0129` (combinatorics, `graph-theory-and-connectivity` + `double-counting`)** —
  a genuine Hall's-theorem SDR application (matching horizontal/vertical maximal sticks to
  cells), textbook and clean, but the underlying problem (grid dissection) has no
  subset-sum flavor at all; it's here only because it's a clean textbook Hall example,
  confirming that a *literal* Hall SDR argument, when it does apply in the corpus, applies
  to genuinely discrete 0/1-compatibility settings — reinforcing that our numeric problem
  is not that shape.

- **`aimo-0197` (combinatorics, `graph-theory-and-connectivity`)** — degree-regularity
  Hall's-condition certification (k-regular bipartite graph automatically satisfies
  Hall). Same comment: textbook Hall on a discrete graph, not applicable to a continuous
  value-matching problem.

### 4. Concrete assessment: is this a promising direction for the next builder?

**A literal "adapt aimo-0063's Hall-deficient-set-deletion" attempt: not promising, and I
would not dispatch a builder on it as stated.** The reviewer's framing ("closer to
subset-sum/exact-cover") is correct, but the specific suggested crux (aimo-0063) is a
discrete 0/1-compatibility SDR argument, and Case C's real difficulty (per the round-10
witness) is a **multi-level recursive value-matching** problem with no natural underlying
bipartite graph — building one would require the split ratios as input, which are exactly
what's unknown. A builder sent to force-fit aimo-0063 will most likely spend the round
discovering this disanalogy (as I did) rather than producing a proof.

**A promising, concretely different next attempt: adapt `aimo-0292`'s peel-and-reattach
subset-sum-coverage induction**, restated for this problem as: "peel the single largest
piece `p_1` (or `p_1,p_2` — whichever leaves a tail satisfying a clean per-piece lower
bound analogous to 'every block ≥1'), solve the tail as its own instance one level deeper,
then reattach and use a slack inequality (the analogue of `x-2≤s-x`) to show the two
covered ranges overlap." The genuinely open technical question this would need to answer,
which the round-10 file has *not* yet asked in this form: **is there a per-piece
lower-bound hypothesis available in Case C's setting** (something playing the role of
"each block weighs ≥1" in aimo-0292) that would let a peel-and-reattach induction avoid
the fatal `g(v)` one-level-loss diagnosed in Round 10 Step 3? If such a bound exists (e.g.
derived from `p_1<Σ/2` plus sortedness), the aimo-0292 mechanism gives a template for
turning "one level of induction is too weak" into "peel plus a slack-guaranteeing
reattachment is enough," which is structurally the missing piece. If no such per-piece
bound exists (plausible, since Case C explicitly allows `p_m` to be arbitrarily small,
unlike aimo-0292's uniform `≥1` floor), the aimo-0292 template will hit the same "how much
slack does peeling actually buy" wall that Step 3 already found — but this needs to be
checked directly, it has not been ruled out.

**Recommendation for the outliner:** do not dispatch a builder to literally search for a
Hall's-marriage-theorem bipartite graph for Case C (dead end, diagnosed above). Instead,
if this lens is pursued next round, retarget it explicitly at aimo-0292's peel-and-slack
mechanism, with the builder's first task being to determine whether Case C's hypotheses
(`p_1<Σ/2`, sortedness, `m≥4`) supply an analogue of aimo-0292's uniform per-block lower
bound sufficient to make a peel-then-reattach argument beat the `g(v)` obstruction — this
is a sharp, checkable sub-question, not vague optimism, and if it fails it should fail
fast and cheaply (a numeric check against the round-10 witness, analogous to the tests
already run this round).
