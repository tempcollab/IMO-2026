## imo-2026-03 (lens: UPPER BOUND gap — general m≥4 Case C of Claim PTBI)

- Distinct openings:
  1. **Direct existence-of-a-good-matching approach (the round-9 plan's own
     next step)**: formalize "does some choice of donor(s)/target-subset(s)
     always exist so that recursively applying Lemma PAIR-VALUE's SUBSET-DOM
     corollary reaches `oddrank(B) ≤ c(m-1)Σ`" as an induction on `m`, using
     a combinatorial selection principle (existence, not construction) for
     *which* subsets to match. Hall's theorem is one *candidate* tool but —
     see "Cheap-kill candidates" and "Small-case notes" below — the
     structure needed is closer to a **subset-sum/exact-cover feasibility**
     question than a classical 1-1 bipartite SDR, so Hall's marriage theorem
     in its textbook form may not directly apply; it may need to be invoked
     on a cleverly-redefined bipartite graph (candidate target subsets as
     hyperedges) or replaced by a direct greedy/potential-function existence
     argument specific to this problem.
  2. **Reformulate via Fact 0 (already proved in the approach file,
     "evensum = max sum-of-mins over pairings")**: since `oddrank(A) =
     Σ(A) − evensum(A)` and evensum is maximized (over ways to partition a
     *fixed* multiset into pairs) by the consecutive pairing, the real
     question is which multisets are *reachable* from `A` by ≤`m-1` marks,
     and whether some reachable multiset's consecutive-pairing evensum is
     large enough. This reframes Case C as: "does there exist a
     budget-`(m-1)` sequence of splits whose result's *own* consecutive
     pairing achieves evensum `≥ (1-c(m-1))Σ`?" — a cleaner single target
     to induct on, not yet tried by any live approach; could be a genuinely
     different framing to put on the table (per CLAUDE.md's diversity rule)
     rather than one more variant of "which subset to match."
  3. **Induction on `m` splitting off *two* elements at once (not one)**:
     since the round-9 witness's winning move pairs `p_2` with `{p_4,p_5}`
     while independently halving `p_1` and `p_3`, a natural induction shape
     is "peel the *pair* `(p_1,p_2)` jointly, recurse on the rest" rather
     than "peel `p_1` alone" (Case A/B's shape) — untested this round but
     flagged as a concrete alternative induction skeleton.

- Candidate technique(s): Lemma PAIR-VALUE / SUBSET-DOM (already certified,
  hypothesis-free) supplies the *value* of any donor/subset match; the
  missing piece is a **general existence theorem** for a good match, at
  every recursion depth, within budget `m-1`. Strong induction on `m` is
  the intended proof shape (already set up by THRESHOLD-REDUCTION for
  Cases A/B); Case C needs either (a) Hall's-theorem-flavored existence, or
  (b) a direct subset-sum/greedy selection argument proved correct by
  induction, or (c) the Fact-0 reformulation above.

- Cheap-kill candidates: **Greedy largest-first subset-sum selection is
  cheaply falsified — do not propose it as the general rule.** Verified
  numerically this round (`/tmp/ptbi_greedy.py`-style script): choosing the
  donor = current largest element and greedily filling the target subset
  with the largest available elements (largest-first, first-fit) that fit
  under the donor fails on **74% of 2000 random Case-C trials** (`m=4..8`),
  worst gap `≈0.128` found at `m=7`; it even reproduces the known-suboptimal
  `BLOCK-RECURSE` value (`15/29≈0.517`) rather than the true optimum
  (`1/2`) on the certified `m=5` witness `A=(12,6,5,4,2)/29`, precisely
  because greedy takes `p_3,p_4` (largest that fit) instead of *skipping*
  `p_3` to match `\{p_4,p_5\}`. This is a genuine, cheap structural
  obstruction: **the correct subset choice needs global information, not a
  local/greedy rule** — any proposed construction must be checked against
  this exact witness before being trusted.

- Knowledge-base entries to use: **Hall's marriage theorem / SDR** entry
  (`knowledge_base.md`, combinatorics section) — but see caveat above about
  whether it's the right formal object. Also relevant: general
  pigeonhole/extremal-principle framing if a direct existence argument
  (rather than matching) is pursued.

- Analogous past problems (cruxes): searched `past_crux_moves_database.json`
  filtered to `domain=combinatorics`, matching on Hall's-theorem/matching
  language (exact field names per `crux_moves_documentation.md`:
  `technique`, `how_used`, `subtopic`, `domain`).
  - **`aimo-0063`** (subtopic `graph-theory-and-connectivity`) — genuinely
    the closest analog found. Problem: cupcakes/people covering problem
    where each person has *their own* valid partition into `n` arcs, and
    the goal is a simultaneous assignment satisfying everyone. The crux:
    "when a perfect matching doesn't exist outright, **iterate Hall-deficient-
    set deletion** — find the Hall-violating subset `B_1`, delete `B_1` and
    its neighborhood, retry on the remainder, repeat" — using a universal
    vertex ("Pip", present in every candidate matching) to guarantee the
    terminal matching is nonempty. This is directly adaptable **if** the
    outliner sets up the m≥4 Case C existence proof as a literal bipartite
    matching (e.g. "donors" vs "targets", one edge per feasible single-value
    match) and Hall's condition fails on some subset — the fix is not to
    give up but to iteratively strip the violating subset and its neighbors,
    then recurse. Worth reading in full if this route is chosen.
  - **`aimo-0129`** (subtopic `graph-theory-and-connectivity`) — an
    `n×n` sieve/stick-partition problem whose crux also invokes "verifying
    Hall's marriage condition on the bipartite graph of the two
    axis-aligned maximal-piece families" to produce a system of distinct
    cells. Less structurally similar to the donor/subset matching here
    (it's a genuine 1-1 SDR, not a subset/hyperedge matching), but
    illustrates the standard pattern of using Hall to produce a concrete
    combinatorial object rather than just an existence statement — useful
    as a template for how a Hall-based lemma should be *stated and used* in
    a write-up, if that route is chosen.
  - No crux found that resembles the subset-sum/"donor covers an arbitrary
    target subset by exact value" structure specifically (as opposed to 1-1
    matching) — if the outliner pursues this framing, it is likely to need
    an from-scratch combinatorial argument rather than a direct crux
    transplant.

- Prior progress: `m=3` (n=2) general upper bound is **fully closed**
  (Case A/B via `lemmas/ptbi-threshold-reduction.md`; Case C via the
  corrected `BLOCK-RECURSE_1`/`TAIL-SNIP` 2-parameter algebra, round 9,
  independently reviewer-verified — see
  `approaches/universal-adversary-strategy.md` lines ~1426–1536). Lemma
  PAIR-VALUE (`lemmas/pair-value.md`) is fully certified and strictly
  generalizes BLOCK-RECURSE/DOUBLE-INSERT to arbitrary (non-prefix) subset
  matches, and its SUBSET-DOM corollary closes the one known concrete `m=5`
  falsifying witness (`A=(12,6,5,4,2)/29`, exact value `1/2 < c(4)=16/31`).
  What does **not** generalize from `m=3` to `m≥4`: the `m=3` closure works
  because with only 2 tail elements there is exactly **one** nontrivial
  donor/subset choice (`j=1`, match `p_1` to `p_2` — no combinatorial
  choice at all), so the whole proof reduces to a clean 2-parameter
  piecewise algebra (`B1` vs `B2` sub-cases). For `m≥4` there are
  exponentially many candidate donor/subset pairs and potentially several
  simultaneous non-conflicting donor actions (as the `m=5` witness shows),
  so a genuine **selection/existence** argument is needed — this is new
  mathematical content, not more casework of the `m=3` type.

- Dead ends (do not retry): the round-9 "no violation found" empirical
  closure of `m=3` is solid (independently re-verified, `200,000`-trial
  search, exact algebra) — do not re-derive. **Greedy largest-first subset
  selection for general `m` (this round's finding, see "Cheap-kill
  candidates")** — cheaply falsified, 74% violation rate; do not propose as
  the SUBSET-DOM selection rule without a smarter mechanism. Prior dead
  ends (already recorded, still valid): `majorization-smoothing`
  (structural non-concavity obstruction), static single-threshold rules
  (`p_1 \gtrless 2p_2`, `2S`, etc. — all falsified with concrete witnesses),
  `minimax-mixed-duality`'s duality-certificate framing (converged/
  non-independent for 2 rounds, flagged for retirement/merge).

- Small-case / intuition notes (all conjecture/numerical evidence, not
  proof):
  - Built a from-scratch exhaustive brute-force construction search
    (`/tmp/ptbi_probe2.py`): recursively try **every** donor-index +
    every subset of the remaining elements (as an exact-value target,
    cost = subset size, or size−1 at the `r=0` boundary) plus a "self-halve"
    move, choosing whichever recursively gives the smallest `oddrank`,
    within budget `m−1`. On the certified `m=5` witness this exactly
    reproduces the known optimum `1/2` (matching the certified proof
    exactly). Ran this exhaustive search on **300 random Case-C
    configurations** (`m∈{4,5,6}`, `p_1<Σ/2`) — **zero violations** of
    `oddrank ≤ c(m-1)`. Additionally ran a **simulated-annealing adversarial
    search** (150 iterations, perturbing toward maximizing the gap
    `best_achievable − c(m-1)`) at `m=5` and `m=6` — the search could not
    push the gap above `0` (best found: `−0.0097` at `m=5`, `−0.0052` at
    `m=6`, i.e. approaching but never crossing the target from below,
    consistent with the extremal geometric configuration `A_{m-1}` being
    the true worst case). **This is strong numerical evidence that Claim
    PTBI is true for `m` up to 6 under the full arbitrary-subset-match +
    self-halve move set**, but it is an exhaustive/annealed *search*, not a
    proof of existence for general `m` — it does not by itself supply the
    inductive argument the outliner needs, and the search cost is
    exponential in `m` (infeasible much past `m=6-7`), so it cannot be
    extended computationally to "confirm for all `m`."
  - No counterexample to Claim PTBI itself was found at `m=4,5,6` (i.e. no
    evidence the theorem is false) — the obstruction is purely that a
    *general proof of existence* of the right matching/subset choice is
    missing, not that the claimed bound is wrong. This is consistent with
    (and sharpens) round 9's own diagnosis.
  - The Fact-0 reformulation (opening 2 above) was not numerically tested
    this round due to time; flagged as untested but potentially fruitful,
    since it turns "which subset to match" into "which reachable multiset
    maximizes evensum," a single scalar target rather than a discrete
    matching-existence question.
