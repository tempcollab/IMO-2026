## imo-2026-03 (Liu Bang's side — lower-bound strategy space)

- **Reduction confirmed**: the claiming phase is content-free strategy-wise — with pieces sorted
  descending L1≥L2≥…≥Lm (m = total pieces after both players cut), the greedy-take-largest
  dominant strategy is forced for BOTH players (taking anything but the current max is weakly
  dominated: it can only let the opponent grab a larger piece next). So Liu Bang's payoff is
  exactly L1+L3+L5+… (odd positions). The whole problem reduces to a one-shot Stackelberg game on
  a multiset of positive reals summing to 1: Liu Bang picks a partition into ≤ n+1 parts (n cuts),
  Xiang Yu then adds ≤ n more cuts (splitting existing parts) to minimize Liu Bang's odd-position
  sum. Only the *sizes* of pieces matter, not their physical location on the stick — Xiang Yu's
  cut only "sees" which piece (by size) it lands in, so the game is entirely about multisets, not
  geometry. This is important: it turns a continuous-geometry problem into a pure multiset/greedy
  game, which is the right level of abstraction for the whole proof, not just my lens.

- **Distinct opening families explored**:
  1. *Equal-thirds-generalization (arithmetic spacing)*: for n=1, cutting at 1/3 (pieces 1/3, 2/3)
     is provably optimal (see below) — but I checked whether the natural generalization to n=2
     (cut at 1/5, 3/5, aiming for pieces 1/5,2/5,2/5 that Xiang Yu is "forced" to equalize into
     five 1/(2n+1)-pieces) is optimal. **It is not** — numerically Xiang Yu has a much better
     reply (see Dead ends below): this whole family is a trap and should not be proposed as the
     answer-achieving construction.
  2. *Dyadic opening (the one that works)*: Liu Bang's n cuts create n+1 pieces of lengths
     `2^0, 2^1, …, 2^n` (in any left-to-right order), each scaled by `1/(2^{n+1}-1)` so they sum to
     1. This family gives, against Xiang Yu's best reply I could find, exactly
     `2^n/(2^{n+1}-1)` for n=1,2,3 (verified both by hand-algebra for n=1 and by heavy numerical
     optimization for n=2,3 — see Small-case notes). This is the strongest lower-bound candidate.
  3. *Bait-one-large-piece*: leaving one very large piece (close to the whole stick) and many tiny
     ones — dominated by the dyadic construction in every case I tested; the single huge piece
     just gets bisected by Xiang Yu into two pieces that both beat it in the sort order, costing
     Liu Bang more than the graduated dyadic ladder does.
  4. *Symmetric bisection opening* (Liu Bang cuts to make n+1 nearly equal pieces): weakly worse
     than dyadic in all tests — nearly-equal pieces let Xiang Yu's cuts each demote exactly one
     Liu Bang position with no "protection" from a size gap, unlike the dyadic ladder where each
     level is protected by a factor of 2.

- **Xiang Yu's counter to the dyadic opening (worked out exactly, matches numerics for n=1,2,3)**:
  Against pieces `{2^0,…,2^n}/(2^{n+1}-1)`, Xiang Yu spends all n of his points *inside the single
  largest piece* `2^n/(2^{n+1}-1)`, splitting it into `n+1` sub-pieces of sizes
  `2^{n-1}, 2^{n-2}, …, 2^1, 2^0, 2^0` (i.e. mirror the existing dyadic ladder below it, but with
  the bottom rung duplicated instead of a `2^{-1}`). Check the count/sum: `n` sub-pieces summing to
  `2^n - 1` (the ladder `2^{n-1}+...+2^0`) plus one extra `2^0` gives sum `2^n` and `n+1` parts from
  `n` cuts — correct. Combined with the untouched pieces `{2^0,…,2^{n-1}}`, the final multiset (2n+1
  pieces total) is: three copies of `2^0`, and **two** copies of `2^k` for each `k=1,…,n-1`. Sorted
  descending and reading off odd positions (Liu Bang's take) telescopes exactly to
  `2^{n-1}+2^{n-2}+…+2^1 (one of each pair, from the top n-1 levels) + 2·2^0 (two of the three
  bottom copies)` = `(2^n - 2) + 2 = 2^n`. Scaled by `1/(2^{n+1}-1)` this is **exactly**
  `2^n/(2^{n+1}-1)` — matching the numerics exactly, algebraically, not just as a coincidence.
  This is a genuine hand-checkable identity, worth handing to the outliner as a concrete
  computation, but it only shows Xiang Yu *can* hold Liu Bang to this value with *one specific*
  reply — it does NOT yet show Xiang Yu cannot do better (push Liu Bang lower), nor that Liu Bang
  cannot open differently to beat `2^n/(2^{n+1}-1)`. Both remain gaps.

- **Candidate technique(s)**: greedy/exchange-argument to justify the reduction to the sorted
  odd-position sum (no game-tree search needed for the claiming phase — this should be proved as a
  clean lemma up front, likely by an exchange/domination argument, i.e. "Standard inequalities /
  extremal principle" flavor plus a short induction on remaining pieces). Then the real
  combinatorial core is a **minimax over partitions of an interval**, which smells like an
  induction on n (build the n-cut optimum from the (n-1)-cut optimum by "adding one more dyadic
  rung"), or an exchange/smoothing argument bounding how much any single Xiang-Yu cut can shift the
  odd-position sum (a "one cut moves the sorted-sum by at most X" lemma, proved by tracking how
  splitting one piece re-indexes the sorted order — akin to the KB's piecewise-concavity/smoothing
  entries and to the invariants-and-monovariants style).

- **Cheap-kill candidates**:
  - *Domination argument for the claiming phase*: if a player ever takes something other than the
    current largest remaining piece, swapping that choice for the largest piece is weakly better
    for them and weakly worse for the opponent — a one-line exchange argument that should be
    proved once and cited everywhere (avoids re-deriving "greedy is optimal" per approach).
  - *Piece-count bound*: total pieces ≤ 2n+1, so Liu Bang's take is a sum of at most `n+1` terms —
    gives a trivial (loose) upper bound of `1` and a trivial lower bound c(n) ≥ 1/(2n+1) (take the
    smallest piece each time) — not tight but a sanity check on any proposed formula (formula must
    lie in `(1/(2n+1), 1)`, comfortably satisfied by `2^n/(2^{n+1}-1) → 1/2`).
  - *Monotonicity in n*: c(n) should be non-increasing as n grows (more power to Xiang Yu, same
    power to Liu Bang, but Liu Bang also gets more cuts — needs checking whether c(n) is monotone
    at all; numerics 2/3 > 4/7 > 8/15 > … confirm it's decreasing towards 1/2 for the dyadic family,
    consistent with intuition and a good consistency check for any final answer).

- **Knowledge-base entries to use**:
  - *Piecewise-concavity smoothing* (Algebra & Polynomials) — the flavor of argument (track how a
    perturbation/split affects a sorted/aggregated sum, minimum occurs at a structural breakpoint)
    is the closest KB analogue to what's needed to show Xiang Yu's best reply against a fixed Liu
    Bang opening occurs at a "boundary" configuration (pieces tying/matching), not generic.
  - *Invariants & monovariants* (Combinatorics) — track a monovariant like "number of pieces at or
    above threshold `2^k/(2^{n+1}-1)`" across Xiang Yu's cuts.
  - *Extremal principle / pigeonhole* (Combinatorics, General Proof Methods) — for the upper-bound
    direction (Xiang Yu's side) not mine, but relevant to see the population converge on a shared
    minimax argument.
  - *Constructive vs. existence* (General Proof Methods) — reminder that the "determine c(n)"
    task needs BOTH the Liu Bang construction (my lens) AND a matching Xiang Yu strategy proof
    (the other lens) — a partial that only has one side is `partial`, not `solved`.

- **Analogous past problems (cruxes)**: I searched `combinatorics` × `games-and-strategy`,
  `invariants-and-monovariants`, `processes-and-algorithms`, `extremal-principle` in
  `past_crux_moves_database.json`, and searched `past_problems_database.json` for
  stick/cake/interval-cutting-game statements. **No close analogue exists in the corpus.** The
  nearest thematically-similar entries (`aimo-0019`, a paint-pot/dyadic-interval covering game
  with a "respond just past the frontier" strategy and a "sum of distinct negative powers of 2 ≤
  2×largest" bound) share the *dyadic-ladder flavor* of the construction I found here, but the
  game mechanics (adversary chooses interval length via `1/2^m` moves, not a static multiset
  greedy-claim game) are different enough that it's not a real crux match — flag it only as a
  distant structural echo (dyadic partitions bound geometric sums), not an adaptable move. No
  other candidate crosses domain+subtopic with genuine mechanical similarity. Recommend the
  outliner not force-fit a crux here; this problem's core trick (the dyadic ladder achieving
  exactly `2^n/(2^{n+1}-1)`) appears to be a fresh construction for this run.

- **Prior progress**: none — workspace was empty at round start (first round).

- **Dead ends (do not retry)**:
  - **Equal/arithmetic-spacing opening** (e.g. n=2 cuts at 1/5, 3/5, aiming for eventual
    equal-fifths): numerically falsified. Xiang Yu's best reply is NOT to equalize the big pieces;
    it's to bisect the *smallest* piece (1/5 → two 1/10's), producing pieces
    `{0.1,0.1,0.4,0.4}` and capping Liu Bang at exactly **0.5**, far below the target 3/5 = 0.6.
    Verified with `scipy.optimize.differential_evolution` (see Small-case notes for exact numbers).
    Any approach proposing arithmetic/equal-share Liu-Bang openings for n≥2 should be flagged as
    almost certainly suboptimal.
  - **Nearly-equal / symmetric-bisection opening**: dominated by dyadic in every numeric test; do
    not spend builder effort trying to make "equal pieces" work for n ≥ 2.

- **Small-case / intuition notes** (numeric evidence, all CONJECTURE except n=1 which is proved
  by hand):
  - **n=1 (proved by hand, not just numerics)**: Liu Bang cuts at `a`. If `a ≤ 1/3` Xiang Yu's best
    reply gives Liu Bang `(1+a)/2`; if `a > 1/3` it gives `1-a`. Both are maximized at `a = 1/3`,
    where they agree: **c(1) = 2/3**, achieved by all pieces becoming exactly `{1/3,1/3,1/3}`
    after Xiang Yu's optimal reply (bisecting the 2/3 piece).
  - **n=2**: exhaustive-type search (enumerated all structural ways Xiang Yu can spend ≤2 points
    against a 3-piece Liu Bang opening — split one piece in half wasting a point, split two
    different pieces, or split one piece into three with both points — each optimized with
    multistart local optimization) plus an outer grid+Nelder-Mead search over Liu Bang's two cut
    points converged to `a=1/7, b=5/7` (pieces `{1/7, 4/7, 2/7}`, the dyadic ladder), value
    `0.571428571... = 4/7` to high precision. `4/7 = 2^2/(2^3-1)`.
  - **n=3**: generic `differential_evolution` (400 iters, popsize 40, no assumed structure, full
    3-D search over Xiang Yu's points) against the dyadic opening `{1/15,3/15,7/15}` (pieces
    `{1,2,4,8}/15`) converged to value `0.5333333333... = 8/15 = 2^3/(2^4-1)` — matching the
    formula to 10 significant digits.
  - **Closed-form derivation of the value against the specific "mirror the ladder" Xiang-Yu reply**
    (algebraic, not numeric): splitting the top piece `2^n` into `2^{n-1},…,2^1,2^0,2^0` (n cuts,
    n+1 sub-pieces, sum checks: `(2^n-1)+1=2^n`) and combining with the untouched `{2^0,…,2^{n-1}}`
    gives a multiset with two copies of `2^k` for `k=1,…,n-1` and three copies of `2^0`. Sorted
    descending, Liu Bang's odd-position sum telescopes to `(2^{n-1}+…+2^1) + 2·2^0 = (2^n-2)+2 =
    2^n`, i.e. exactly `2^n/(2^{n+1}-1)` after rescaling. This matches the DE optimum in all three
    cases (n=1,2,3) — strong evidence the dyadic opening is exactly optimal and this specific
    Xiang-Yu reply is exactly his best one, though neither optimality claim is proved yet.
  - **CONJECTURE: c(n) = 2^n / (2^{n+1} - 1)**, decreasing in n from 2/3 toward 1/2 as n→∞ (unlike
    the naive `(n+1)/(2n+1)` guess, which was cleanly falsified at n=2: (n+1)/(2n+1) predicts 3/5 =
    0.6 for n=2, but the true optimum found is 4/7 ≈ 0.5714 < 0.6). **Flag this clearly to the
    outliner: `(n+1)/(2n+1)` is a tempting but wrong guess — do not let any approach assume it.**
  - **Gaps remaining for the full lower-bound proof** (what a builder needs to close): (1) prove
    Xiang Yu cannot do *better* than the "mirror the ladder inside the top piece" reply against the
    dyadic opening (i.e. this really is his minimizing response, for all n, not just n≤3) — likely
    an induction/exchange argument on how splitting any piece re-sorts the multiset; (2) prove Liu
    Bang cannot open *better* than the dyadic ladder (i.e. no other partition into ≤n+1 pieces beats
    `2^n/(2^{n+1}-1)` against Xiang Yu's best reply) — this is really the upper-bound problem in
    disguise (would need to be established jointly with Xiang Yu's-side reasoning) and is likely
    best attacked by strong induction on n showing the dyadic opening's value is a fixed point of
    the minimax recursion.
