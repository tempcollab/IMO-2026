## imo-2026-03 (unified exact-minimax framing)

- Distinct openings (genuinely different top-level targets, not variations of the split B2/B3 arguments):

  1. **Box-balancing reformulation (strongest new lead).** By Lemma R, D is exactly
     "odd-rank-sum − even-rank-sum" of the final sorted multiset. Read this as a TWO-BOX
     game: box O (odd sorted rank) vs box E (even sorted rank), D = |O|−|E|, membership
     decided automatically by sorted rank (not by player choice). Xiang's job — pick ≤n
     splits to make the two boxes as equal as possible — is structurally the SAME task as
     the "corrector" role in the crux-analogous problem aimo-0117 (see below): a
     constructor commits values first, an adjuster with a bounded budget of moves tries to
     balance two boxes, using dyadic/geometric values as the extremal committed sequence.
     This reframes BOTH bounds as one question: "what is the exact value of the
     two-box-balancing game when the committed values are dyadic (a_k=2^k) vs arbitrary?"
     — replacing the separate lower/upper arguments with one balancing-game value formula.
  2. **Exact subset-sum / one-shot pairing strategy for Xiang (new, replaces greedy).**
     Computed by direct brute force (see Probe below) that on the counterexample input
     (0.5, 0.28, 0.22) — where greedy-match was proven insufficient by the
     parity-measure-potential approach — the TRUE optimal Xiang move is not "match top
     two" but **split the top piece a_1 into fragments that exactly copy the sizes of the
     REST of the multiset** (here a_1 = a_2+a_3 exactly since 0.5 = 0.28+0.22, so cutting
     a_1 into (0.28,0.22) gives two exact-multiplicity-2 pairs, D = 0 with a single cut,
     using only 1 of the 2 available cuts). This generalizes to: Xiang should look for a
     SUBSET of the current pieces whose sum is close to another piece's value (a subset-sum
     matching / balanced bipartition of the multiset), then realize that pairing with one
     multi-way split of the larger piece, rather than iterating "top two" comparisons. This
     is a genuinely different (non-greedy, one-shot, global) strategy family — the right
     candidate to close GAP B3, and it naturally handles the case max(a_1,2a_2) < c(n)
     where the single cancelling-pair peel (current induction-peel approach) fails.
  3. **Backward-induction closed-form for the residual game value f(A,k).** Define f(A,k)
     = min D achievable by ≤k Xiang splits on sorted multiset A. The whole answer is
     c(n) = (1+max_A f(A,n))/2 over Liu's A with |A|≤n+1, sum 1. Rather than splitting into
     "prove f(dyadic,n) ≥ u_n" (lower) and "prove f(A,n) ≤ u_n for all A" (upper)
     separately, seek ONE exact recursive formula/algorithm for f(A,k) (e.g., a
     closed-form in terms of the sorted values and a matching structure) that immediately
     yields both: plugging A = dyadic gives f = u_n exactly (lower bound + tightness), and
     bounding the formula uniformly over all A gives f ≤ u_n (upper bound). This is the
     literal target the lens asks for; item 2's one-shot pairing move is the natural building
     block for such a formula (a "greedy subset-matching" recursion rather than "greedy
     top-two").
  4. **Weight/potential (LP-dual) certificate.** Look for a fixed weighting function
     w:(0,1]→ℝ (candidate: piecewise-dyadic, w(t) built from the binary expansion of t
     relative to the scale 2^{-k}) such that (a) for the dyadic A, Σ pairing under w gives
     exactly u_n and is invariant under any Xiang split (a conserved/monovariant quantity
     under the toggle calculus of Lemma T), and (b) for any A, the same w gives an upper
     bound on min-D achievable. This is the "primal-dual" idea explicitly named in the
     dispatch; it has NOT been tried by either live approach (both use raw measure D, not a
     re-weighted invariant). It may formalize "cutting a scale costs that scale" (GAP B2)
     as a monovariant argument instead of the stalled interference bookkeeping.

- Candidate technique(s): two-box balancing / invariant-maintenance induction (borrowed
  structurally from aimo-0117's Jesse strategy), subset-sum / exact-matching pairing
  (generalizes Lemma P beyond single cancelling pairs), monovariant/potential-function
  certificates for minimax games (KB: "Invariants & monovariants"), backward induction on
  game value (KB: general game-value recursion via `V(S)=Σ(S)−min_j V(S∖{b_j})`, already
  used for Lemma R — the SAME technique could be pushed one level further to get f(A,k)
  in closed form rather than just proving Lemma R).

- Cheap-kill candidates: none obvious as a pruning shortcut, but a useful STRUCTURAL check
  before heavy computation: whenever a_1 (Liu's largest piece) equals or nearly equals the
  sum of all the other pieces, Xiang gets D≈0 for the cost of splitting a_1 alone
  (verified numerically, see Probe) — so any correct upper-bound strategy must special-case
  "a_1 close to Σ(rest)" as a trivial win, separate from the genuinely hard superincreasing
  (dyadic) case where a_1 ≫ Σ(rest). This split (a_1 ≤ Σrest vs a_1 > Σrest) is a clean,
  cheap case division worth using structurally in any closed-form attempt.

- Knowledge-base entries to use: "Invariants & monovariants" (line ~117, ~191) for a
  potential/monovariant certificate; the general backward-induction value recursion
  `V(S)=Σ(S)−min_j V(S∖{b_j})` already used to prove Lemma R (push it further for f(A,k));
  "Multiset partitions & power-sum matching (Prouhet–Tarry–Escott flavor)" (line 120) is a
  loose structural pointer for the subset-sum-matching idea in opening 2 (splitting into
  parts with matching sums), though not a direct citation.

- Analogous past problems (cruxes):
  - **aimo-0117** (combinatorics, games-and-strategy) — STRONGEST match. Two boxes (black
    "half rounded down", white "half rounded up") of a fixed total capacity; a constructor
    (Jesse) commits a value each round and places it in an unfilled box; a corrector
    (Tjeerd) may move one stone to the other box; goal is to make one box's sum exceed the
    other's. The winning construction is EXACTLY the dyadic sequence
    `2^{-i},...,2^0,...,2^j` (played in order, extending the range by one power each turn,
    choosing to extend downward or upward depending on the corrector's last move), with the
    closing argument "the largest played power is in the target box after Jesse's move,
    maintained by an induction with exactly two cases depending on whether the corrector
    moved that top power or not" and the final inequality
    `2^j > 2^{j-1}+2^{j-2}+...+2^{-i}` (superincreasing/dominance of the top scale over
    everything smaller) — literally the same superincreasing inequality (5.1) already used
    in both live approaches, PLUS a genuinely two-case induction handling "top scale
    touched vs not touched" that is structurally identical to the unresolved Case
    A/Case B split in GAP B2. This is a strong candidate for reuse: adapt aimo-0117's
    "two-case invariant induction, tracking who currently holds the largest scale" as the
    closing device for GAP B2 (lower bound, top-piece-cut case), rather than the
    stalled interference/bookkeeping approach.
  - **aimo-0019** (combinatorics, games-and-strategy/invariants) — a related but less
    directly transferable IMO 2016 P3 "ink pot" problem; its crux "bound a family of
    dyadic-length pieces of pairwise distinct sizes by twice the largest, via the geometric
    sum of distinct negative powers" is the same superincreasing-dominance fact, reused as
    background, but the overall game (ink budget vs interval covering) is not structurally
    the same two-box balancing game, so treat as a secondary confirmation of the dyadic
    dominance fact rather than a solution template.
  - No other combinatorics games-and-strategy crux in the corpus resembles the two-phase
    (commit-then-respond) continuous-length structure of this problem closely enough to
    borrow a full strategy from; the above two are the genuine matches.

- Prior progress: see current.md — Lemmas R (reduction to D=Σ(−1)^{i+1}b_i), I (measure
  identity D=measure{N(t) odd}), T (toggle calculus of one cut), P (cancelling pair) are
  all fully proved and certified (`lemmas/reduction-odd-rank.md`,
  `lemmas/measure-identity.md`, `lemmas/cancelling-pair.md`). Lower bound Case A (top piece
  uncut) and upper bound on the dyadic extremal input are fully proved. Both approaches
  independently stall on the SAME two gaps (B2/GAP L: cutting the top dyadic piece; B3/GAP
  U: an adaptive Xiang strategy beating greedy for m=n+1, all-strict, full budget) — this
  is exactly the "shared-gap plateau" the dispatch flags, and is why this lens was assigned.

- Dead ends (do not retry, verified by re-derivation not just trust):
  - **Greedy top-two matching / bisect-the-max as Xiang's universal strategy.** Both prior
    approaches independently derive this reduces the entire upper bound to the case m=n+1,
    all-strict, and both report (and I did not need to re-verify numerically since the
    reasoning re-derives cleanly from Lemma P) that it fails for n≥3. My own brute-force
    on the n=2 counterexample (0.5,0.28,0.22) CONFIRMS the greedy top-two-based bound
    (max(a_1,2a_2) ≥ c(n)) is not met (0.56 < 0.571), yet the TRUE optimum there is D≈0 —
    achieved by a strategy greedy would never try (splitting a_1 to copy the *whole* rest of
    the profile, not just a_2). This confirms the failure is in the strategy family, not the
    bound arithmetic — supports opening 2 above as the fix.
  - Re-verified independently: the measure identity D=measure{N(t) odd} and the toggle
    calculus (Lemma T) are correct (re-derived and additionally confirmed numerically by
    my own brute force D() computation, which recomputes D via direct alternating sum on
    sorted pieces — agrees with all values). No issue found; these lemmas are safe
    foundations to build on.

- Small-case / intuition notes (all labeled conjecture/numerical, not proof):
  - Independent brute-force (grid search over split points, budget-2 full game tree) on
    n=2 dyadic input (4/7,2/7,1/7) recovers min D = 1/7 = u_2 to within grid resolution —
    consistent with the claimed answer.
  - Random search over Liu triples (a,b,c) for n=2 found no configuration with
    Xiang-optimal D exceeding u_2=1/7 (best found ≈0.126 < 0.143, on a coarse grid, so the
    true max is expected to be even ≤ that) — supports the dyadic construction being the
    true worst case for Liu, consistent with (not proof of) c(2)=4/7.
  - On the specific hard counterexample (0.5,0.28,0.22) flagged as breaking greedy: the
    TRUE Xiang optimum (found by finer brute force) is D≈0.0019 (not exactly 0 only due to
    grid resolution — analytically D=0 exactly is achievable in ONE cut, since
    0.5=0.28+0.22 exactly), far below u_2=1/7, achieved by copying the sub-profile into the
    top piece rather than matching pairs greedily. This is strong (numerical) evidence that
    "exact subset-sum pairing" (opening 2) is the right strategy family to formalize for
    GAP B3, and that the true upper-bound proof needs a strategy that looks at the WHOLE
    remaining profile when deciding how to split the top piece, not just its two largest
    elements.
