## imo-2026-03

- Distinct openings (genuinely new framing, not a variant of geometric/odd-rank casework):

  **A. Concave-value-function / LP-duality framing (main finding, strongly recommend opening a new slug).**
  Fix the reduction `c(n) = max_A min_B oddrank(B)` (Lemma 1, already shared/certified —
  keep this, it is domain-agnostic and every approach needs it). Define, for a fixed
  "shape" (Liu Bang uses exactly `n` marks, `m = n+1` pieces), the value function
  `V(p) := min_B oddrank(B)` as a function of the SORTED vector `p = (p_1 ≥ ... ≥ p_{n+1} ≥ 0)`,
  `Σp_i = 1` — i.e. Xiang Yu's best response value as a function of Liu Bang's
  configuration. The sorted-descending simplex `{p_1≥p_2≥...≥0, Σp_i=1}` is itself a
  convex polytope (convex combinations of sorted vectors stay sorted), so "is V concave
  on this domain" is a well-posed question distinct from anything in the current field.
  **I numerically verified (exact `Fraction` arithmetic, brute-force enumeration of Xiang
  Yu's discrete split-allocations + fine grids over continuous split ratios) that V IS
  concave on this domain**: for `n=1` (`m=2`) I get the *exact* closed form
  `V(p_1,p_2) = p_1` for `p_1 ∈ [1/2, 2/3]` (slope 1) and `V(p_1,p_2) = 1-p_1/2` for
  `p_1 ∈ [2/3,1]` (slope −1/2) — a single downward kink at `p_1 = 2/3` (i.e.
  `p_1 = 2p_2`), non-increasing slopes ⇒ concave. This kink location and the two slopes
  match exactly the regimes already isolated by the certified `Lemma DOM` (dominance,
  `p_1 ≥ S`) and `Lemma HALVE` (`p_1 ≥ 2p_2`) in `generalized-domination-and-halving.md`
  — i.e. **concavity is not a new, unrelated conjecture, it is the natural global
  packaging of the two lemmas the population already has.** For `n=2` (`m=3`,
  2-dimensional sorted simplex) I ran 15 random-pair midpoint tests (both interior pairs
  and pairs mixing an interior point with a boundary point `p=(1,0,0)`) with the same
  brute-force `V` computation, coarse grid (resolution 6–8) — **zero concavity
  violations found**. This is only numerical evidence (conjecture, not proof) but it is
  a real, independent structural fact, not a restatement of the existing framing.

  Why this could close BOTH gaps at once (the ask in the dispatch): if `V` is concave on
  the sorted-simplex domain, then (i) **upper bound**: for ANY Liu Bang configuration
  `p`, a single supporting-hyperplane/subgradient inequality at the conjectured optimum
  `p* = (2^n,...,2,1)/(2^{n+1}-1)` gives `V(p) ≤ V(p*) + ⟨g, p−p*⟩` for any subgradient
  `g` of the concave `V` at `p*`; if the RHS is `≤ V(p*)` for all `p` in the simplex
  (i.e. `⟨g,p−p*⟩ ≤ 0` — a single linear inequality check against the *whole* simplex),
  this replaces the current case-by-case "which regime does Xiang Yu use" enumeration
  (`universal-adversary-strategy`'s open gap) with one linear-algebra fact about the
  gradient at one point. (ii) **lower bound**: concavity + the exact `n=1` closed form
  above suggests a general recursive kink structure — the same `Lemma S`/self-similarity
  fact already certified in `geometric-configuration-facts.md` (top-piece domination,
  self-similar structure under removing the top piece and rescaling) is exactly the kind
  of recursive identity that would let you compute `V` at `p*` and its subgradient
  directly from the `n-1` case, closing the induction without needing the interleaving
  casework that both `geometric-dominance-construction` and `recursive-embedding-induction`
  are stuck on. In short: concavity turns "prove no interleaved split beats the doubling
  family" into "prove one linear inequality at the kink points of a piecewise-linear
  function" — genuinely different proof obligations from the stuck gap.

  **B. Global optimality via "piecewise-concave ⇒ minimum/maximum at a breakpoint"
  (a specific proof technique for closing framing A's Step 4, found in the KB and the
  crux corpus — worth flagging explicitly to the outliner as the mechanism, not just the
  concavity claim in isolation).** `knowledge_base.md`'s **"Piecewise-concavity
  smoothing"** entry (Algebra & Polynomials section) states exactly this pattern: if a
  function is piecewise-concave on a partition of an interval/domain by finitely many
  breakpoints, its extremum over the whole domain occurs at a breakpoint (or domain
  vertex), reducing "check everywhere" to "check the finite discrete set of
  combinatorial-type transitions." The crux corpus has a directly analogous solved
  problem, `aimo-0861` (subtopic `inequalities-SOS-and-convexity`): shift all variables
  by a common parameter `t` to turn one side of a symmetric inequality into a
  ONE-PARAMETER function that is piecewise-concave (concave on each interval between
  consecutive sign-changes of `|x_i ± x_j + 2t|`), then argue the global minimum over `t`
  occurs at an interval endpoint (a "kink"), reducing the general claim to finitely many
  special configurations. This is precisely the mechanism `majorization-smoothing`'s
  Step 4 (global optimality) needs and currently only gestures at informally — the
  outliner/builder should use `aimo-0861`'s exact proof pattern (shift-to-kink-points,
  concavity forces extremum at breakpoints) as the template, not reinvent it.

  **C. Why NOT pursue (and note for completeness per the dispatch): entropy/continuous
  relaxation.** I looked for a natural entropy or measure-theoretic relaxation of the
  problem (idea 2 in the dispatch) — found none. `oddrank`/`V` is piecewise LINEAR (not
  logarithmic/entropic) in the piece lengths; there is no natural "spreading out" cost
  function here analogous to entropy-maximization arguments (those apply where the
  objective has a strictly concave, differentiable, symmetric-in-all-coordinates form
  like `Σ x log x`; here the objective is a rank-selection sum, which is piecewise-linear
  with combinatorial kinks, not smooth). Recommend NOT opening an entropy-based slug;
  framing A (concavity/LP-duality) already captures the "avoid interleaving casework"
  benefit an entropy method would have tried to buy, with actual numerical support.

  **D. Why NOT pursue: Sprague-Grundy / combinatorial-game potential functions (idea 3).**
  This is a SCORING game (players maximize a continuous real payoff, no last-player-wins
  condition), not a normal/misère impartial combinatorial game, so Sprague-Grundy theory
  (which classifies win/loss for impartial games under normal play) does not apply.
  `Lemma 1`'s backward-induction value formula is already the correct game-theoretic tool
  for the *claiming* phase and is exact/closed; the open difficulty is entirely in the
  *marking* phase's continuous optimization (a Stackelberg/minimax-over-reals game), which
  is squarely an LP/concave-analysis problem (framing A), not a combinatorial-game-value
  problem. No Grundy-type tool from the KB looks applicable; did not find a matching
  entry.

- Candidate technique(s): concavity of the Xiang-Yu-best-response value function `V(p)`
  on the sorted-descending simplex, established via "min of the (continuous-split-optimized)
  linear-in-p functionals per discrete allocation type is concave" (needs the careful
  two-level-minimax argument the existing `majorization-smoothing.md` skeleton already
  flags as the main risk — my numerics support it but don't prove it); combined with the
  KB's "Piecewise-concavity smoothing" breakpoint-reduction technique and its crux-corpus
  worked example `aimo-0861`.

- Cheap-kill candidates: none new beyond what's already used (dominance/halving
  regime-splits, already certified as `Lemma DOM`/`HALVE`). One useful new cheap check
  for the builder: my numeric `n=1` computation gives V's two linear pieces EXACTLY
  matching `Lemma DOM`/`Lemma HALVE`'s regimes — this is a free sanity check the builder
  should redo analytically (should take <1 page) before investing in the general-`n`
  concavity proof, to make sure "concave packaging of DOM+HALVE" really is equivalent to
  those two certified lemmas and not secretly a stronger/different claim.

- Knowledge-base entries to use: **"Piecewise-concavity smoothing"** (Algebra &
  Polynomials section, near top of `knowledge_base.md`) — directly reusable mechanism for
  Step 4 of `majorization-smoothing.md`. (Standard convex-analysis facts — concave
  function attains max on a compact convex set at a point satisfying first-order/KKT
  conditions, and a min of concave... n.b. actually need min of LINEAR functions is
  concave, standard fact — are used but are not separately named KB entries; cite as
  standard convex analysis when building.)

- Analogous past problems (cruxes): **`aimo-0861`** (algebra,
  `inequalities-SOS-and-convexity`) — crux: "Shift all variables by a common parameter to
  make one side of a symmetric two-sided inequality invariant, turning the other side
  into a one-parameter piecewise-concave function; then use that concavity to reduce
  proving the inequality everywhere to proving it only at the function's kink points."
  Genuinely analogous mechanism (piecewise-concave ⇒ check only breakpoints) though the
  problem itself (a sum-of-square-roots inequality) is not otherwise close to the stick
  game. **`aimo-0117`** (combinatorics, `games-and-strategy`) — crux: "Assign the played
  values as a two-sided geometric (dyadic) sequence so that the single largest value
  strictly exceeds the sum of all the others" — this is the SAME dyadic-dominance idea
  the current field already uses (geometric configuration, top-piece domination); flagged
  for completeness but it's confirmation of the existing framing, not a new one. No other
  crux in `games-and-strategy`, `inequalities-SOS-and-convexity`, or `extremal-principle`
  (checked all three subtopics, ~70 cruxes total) is closely analogous to a continuous
  Stackelberg stick-division game; most `games-and-strategy` cruxes are discrete
  pairing/mirroring/invariant strategies for combinatorial (not continuous-value) games
  and do not transfer.

- Prior progress: (see `current.md`) — shared reduction to `c(n)=max_A min_B oddrank(B)`
  certified; `k=0` and `k=1`-tail-untouched lower bound cases closed; `n=1` fully closed
  both directions (two independent routes); Lemma DOM/HALVE certified for arbitrary tail
  shape in restricted regimes. `majorization-smoothing.md` exists as an approach file
  (Status: unsolved) with a skeleton for exactly framing A above but was NOT built this
  round — its core claim (Lemma C, concavity) was open/unverified. **This report provides
  the first actual evidence for Lemma C** (numeric, `n=1` exact + `n=2` random spot
  checks, no violations) — recommend the outliner treat `majorization-smoothing` as the
  slug to advance/build next round using this evidence, rather than opening yet another
  fresh slug, since it already contains the right skeleton.

- Dead ends (do not retry): entropy/relaxation framing (checked, no natural entropy
  structure — piecewise-linear objective, not smooth-concave); Sprague-Grundy/potential-
  function combinatorial game theory (checked, doesn't apply — this is a scoring/
  Stackelberg game, not impartial normal-play). Do not resurrect these as separate slugs.
  (Existing dead ends from `current.md` — `equalization-potential-bound`'s flawed
  impossibility argument, and the refuted "bound the merge by aggregate sums alone"
  class from `merge-by-sums-counterexample.md` — remain dead; not re-examined here, no
  new evidence bearing on them.)

- Small-case / intuition notes (all labeled conjecture except where marked exact):
  - **Exact (verified by direct enumeration + fine grid, `n=1`):** `V(p_1,1-p_1)` for
    `p_1∈[1/2,1]` is exactly `p_1` on `[1/2,2/3]` and `1-p_1/2` on `[2/3,1]` — a single
    downward kink at `p_1=2/3`; consistent with concavity and with `Lemma DOM/HALVE`'s
    regime boundary.
  - **Conjecture (numeric spot-check, `n=2`, coarse grid, 15+10 random trials, no
    violation):** `V(p)` is concave on the full sorted 2-simplex, including at the
    boundary (a piece of length 0).
  - **Conjecture (not tested this round, flagged for the builder):** the general-`n`
    version of the kink structure recursion — whether `V`'s kink locations/slopes satisfy
    the same self-similar halving recursion `c(n)=2λ_n c(n-1)` already derived (as an
    equality, not yet an inequality-everywhere fact) in `recursive-embedding-induction`'s
    Lemma G1 — checking whether Lemma G1's recursion is literally the "value at `p*`"
    special case of the general concave `V`'s recursive structure would be the natural
    next computational step.
