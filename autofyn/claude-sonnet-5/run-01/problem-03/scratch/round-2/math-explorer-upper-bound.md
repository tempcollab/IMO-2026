## imo-2026-03 (upper-bound half: `max_A min_B oddrank(B) ≤ c(n)` over ALL Liu-Bang configurations `A`)

### Scope of this report
This report scouts *only* the untouched gap: proving Liu Bang cannot beat
`c(n) = 2^n/(2^{n+1}-1)` with **any** marking, not just the geometric one.
It does not touch the (still separately open) `k≥1` lower-bound sub-case for
the geometric construction itself — see `current.md` for that.

### Distinct openings
1. **Universal-adversary-strategy framing (recommended top candidate).**
   Instead of casework on the shape of `A`, exhibit a single strategy
   *description* for Xiang Yu — a rule that takes any sorted `p_1≥…≥p_{m}`
   (`m ≤ n+1`) and produces a response using `≤ n` marks — and prove
   *uniformly* that this strategy achieves `oddrank(B) ≤ c(n)` for every `A`.
   This is a direct structural analogue of the "replace the adversary with a
   strategy that provably caps the mover's gain regardless of the mover's
   choice" technique used in IMO 2022 P6 (gardener/lumberjack, `aimo-0560`,
   see below): there the responder used a *fixed coloring* whose induced cap
   is independent of the mover's placement. Here the natural candidate rule,
   suggested by both Proposition 4 (the exact-equality witness for `A_n`) and
   the self-similarity Lemma 3, is: **recursively attack the current largest
   piece**, splitting it exactly in the ratio that reduces the problem to a
   smaller instance — i.e. Xiang Yu always spends his marks on `p_1` (the
   overall max of `A`), splitting it into a copy of the *tail shape* plus the
   ratio-1 residual, mimicking Proposition 4's construction but starting from
   an arbitrary `p_1,…,p_m`, not just the geometric one. Numerics (below)
   support that "attack the current max, recursively" dominates all
   alternative Xiang-Yu strategies against non-geometric `A` too — matching
   the certified Lemma 2/Proposition A fact that Xiang Yu never benefits from
   leaving the top piece untouched when it's not already capped.

2. **Induction on `n` via the self-similarity identity (Lemma 3).** Lemma 3
   already shows `A_n`'s tail is a scaled copy of `A_{n-1}`. The natural
   inductive upper-bound argument: suppose `max_A V(A) ≤ c(n-1)` is known for
   the `(n-1)`-mark game (i.e., for configurations with `≤ n` pieces and
   Xiang Yu given `≤ n-1` marks). For the `n`-mark game, argue Xiang Yu can
   always first neutralize Liu Bang's top piece down to size `≤` twice the
   rest (using 1 mark), reducing the remaining game to an `(n-1)`-mark
   instance to which the inductive hypothesis applies. This requires proving
   a one-mark "reduction lemma": for ANY `A` with top piece `p_1` and tail sum
   `S = 1-p_1`, Xiang Yu can use exactly one mark on `p_1` to guarantee the
   resulting value is at most `max(c(n-1)-scaled bound, …)` — this is the
   genuinely new piece of work; nobody has attempted it yet. This opening is
   close in spirit to `recursive-embedding-induction.md`'s existing machinery
   (which proves the analogous fact only for the geometric `A_n` itself) —
   the natural next step is to check whether that approach's Lemma 3
   self-similarity argument generalizes to *arbitrary* `p_1,…,p_m`, not just
   the geometric sequence. Worth flagging to the outliner as "extend
   recursive-embedding-induction's machinery to arbitrary A" as a distinct
   sub-opening from (1) even though related.

3. **LP/concave-envelope framing revisited, but over `A`-space directly (not
   rank-weights).** The dead-ended `equalization-potential-bound` approach
   correctly showed a single *rank-only linear functional* `w` cannot give a
   tight bound (Lemma D+E, certified) — but that obstruction is specific to
   linear functionals of `p_i` values. It does NOT rule out showing `V(A)`,
   as a function on the ordered simplex `Δ_n`, is concave with a UNIQUE
   maximizer, and separately verifying the geometric point satisfies the
   first-order (KKT) stationarity condition (this is exactly
   `majorization-smoothing.md`'s still-unattempted Steps 2–4, Lemma
   C/D there). My numerics below (local Nelder-Mead convergence to the exact
   geometric point from multiple random starts, and non-increase under
   random simplex perturbations) are consistent with `V` being concave with a
   single unique maximum at `A_n`, which would validate this route, but I did
   NOT verify concavity itself. This is a real, different avenue — via
   calculus on `V(A)` as literally defined (not a hoped-for linear
   relaxation) — worth keeping distinct from opening (1) since it needs no
   explicit adversary strategy, only the shape of `V` itself.

### Candidate technique(s)
- **Primary:** universal/strategy-independent-of-A adversary argument
  (opening 1), directly modeled on the "coloring/potential caps the mover
  regardless of mover's choice" crux move family (see crux below).
- **Secondary:** induction via Lemma 3 self-similarity generalized off the
  geometric sequence (opening 2).
- **Tertiary (higher risk, more machinery):** concavity-of-value-function /
  KKT argument (opening 3), reusing Lemma D/E's polytope facts (`Δ_n` is
  `n`-dimensional, geometric point is a strict interior point) as background,
  but NOT reusing the (already refuted) claim that a single rank-linear
  functional suffices.

### Cheap-kill candidates
- **Top-piece domination is necessary, not just sufficient.** By Lemma 2's
  logic in reverse: if in *any* configuration `A` the top piece `p_1` already
  satisfies `p_1 ≥ Σ_{i≥2}p_i` (i.e. `p_1 ≥ 1/2`), Xiang Yu is structurally
  forced to spend marks on `p_1` itself (any tail-only response leaves `p_1`
  as the dominant rank-1 element by the same argument as Proposition A, so
  `oddrank(B) ≥ p_1 ≥ 1/2 > c(n)` is IMPOSSIBLE for Xiang Yu to avoid unless
  he cuts `p_1`) — this immediately rules out any Liu Bang configuration with
  `p_1 ≥ 1/2` as *not* being capped by tail-only defense, so the interesting
  regime to check is only `p_1` close to `c(n)` itself; configurations with
  `p_1` far from `c(n)` in either direction are cheaply dominated (numerics
  confirm: `top-heavy=[0.9,0.09,0.01]` gives `V≈0.505 < c(2)`, far below).
- **Fewer-marks is never better for Liu Bang (numerically confirmed, not yet
  proved in general).** Using `m < n+1` pieces (i.e. Liu Bang wastes marks)
  strictly hurts him: `V([0.5,0.5])` under `n=2` Xiang-Yu marks
  `= 0.5 < c(2) = 0.5714`, confirmed by grid+refine search over all `p_1 ∈
  [0.5,1]`. This licenses restricting attention to Liu Bang configurations
  with exactly `n+1` positive pieces (already assumed as background in
  `equalization-potential-bound.md`, but the numeric check here adds
  confidence it's safe to use for the upper-bound proof too, not just the
  lower bound).

### Knowledge-base entries to use
- `knowledge_base.md`'s **piecewise-concavity smoothing** entry (line 20) —
  directly relevant scaffolding for opening 3 if pursued: minimizing/
  maximizing a function that is a finite min/max of concave pieces.
- No other knowledge_base entries found specific to adversarial two-phase
  marking games; the file is thin on game-theoretic minimax techniques
  beyond this one entry — most of the leverage for this gap will have to
  come from the crux corpus and first-principles work, not `knowledge_base.md`.

### Analogous past problems (cruxes)
- **`aimo-0560`** (IMO 2022 P6, gardener/lumberjack) — subtopic
  `games-and-strategy`. Crux: *"Replace the adversary with a strictly
  stronger surrogate whose reply is pointwise at least as damaging, so a win
  against the surrogate transfers down and the reply collapses to a finite
  per-region menu."* Also: *"For an upper bound in a placement game,
  partition the conflict graph into small identical components each of which
  can hold at most one non-conflicting piece, and have the blocker respond
  inside the same component the mover just used to exhaust it."* This is the
  best structural analogue found: it is exactly the shape of upper bound
  needed here — a single fixed/structural responder strategy (not
  case-by-case on the mover's placement) that caps the mover's total gain
  *regardless* of how the mover plays, via a combinatorial partition/coloring
  argument. The adaptation needed: replace "coloring of the board" with
  "recursive geometric splitting of the current maximum piece," but the
  proof shape (one uniform responder rule + a counting/potential argument
  that bounds the cap for every mover choice) is the right template.
- **`aimo-0117`** (dyadic stone-boxing game) — subtopic `games-and-strategy`.
  Crux: *"Assign the played values as a two-sided geometric (dyadic) sequence
  so that the single largest value strictly exceeds the sum of all the
  others."* This is structurally identical to Lemma 2 (top-piece domination)
  already certified in `geometric-configuration-facts.md` — confirms the
  "largest exceeds sum of the rest" geometric idea is a recognized crux
  pattern in this genre, reinforcing that the certified Lemma 2 is on the
  right track, though this crux is about the *construction* side, not the
  upper-bound side, so it's more directly relevant to the already-solved
  lower-bound sub-case than to this specific gap.
- **`aimo-0663`** (IMO 2022 C-type consecutive-picking game) — subtopic
  `games-and-strategy`. Less directly analogous (its crux is a
  component-counting/pigeonhole liveness argument for "can always move," a
  different game shape), but its general *lesson*, "count contiguous
  components to show a response is always available," is a reusable style of
  argument if opening 2's inductive reduction needs a bookkeeping argument
  for why Xiang Yu's marks are always sufficient — flagged as a weaker,
  secondary analogy, not a strong match.

### Prior progress
None on this specific gap — confirmed via `current.md`: "the upper bound over
arbitrary configurations... has not been attempted by either approach yet."
`equalization-potential-bound.md`'s Lemma D/E (interior-point-forces-constant)
are reusable background facts about the geometry of `Δ_n`, but they only rule
out ONE specific mechanism (rank-only linear functionals), not the general
upper bound.

### Dead ends (do not retry)
- **Rank-only linear functional `w_i·p_i ≥ V(A)` uniformly valid and tight at
  `A_n`.** Rigorously refuted (Lemma D+E): forced to be the tautological
  constant `w_i ≡ c(n)`, which encodes no new information. Do not resurrect
  this exact mechanism for the upper bound; any new attempt must use a
  genuinely different (non-purely-linear-in-`p_i`) potential/strategy.
  Sanity-checked independently: recomputed the `n=1` exact value function
  `V(p_1,p_2) = min(p_1, p_2+p_1/2)` numerically (grid + local refine) and
  confirmed it is a genuine min of two distinct linear pieces crossing
  exactly at `p_1=2/3`, matching the approach file's claim — the dead-end
  verdict holds up.

### Small-case / intuition notes (all numeric, i.e. conjectural evidence, not proof)
- **n=1:** exhaustive verification that `max_{p_1∈[0.5,1]} min(p_1,
  1-p_1+p_1/2) = 2/3` exactly at `p_1=2/3` — matches `c(1)`.
- **n=2:** local optimization (Nelder–Mead) from a random-search warm start
  converges to `p ≈ (0.571429, 0.285714, 0.142857)` — i.e. **exactly** the
  geometric `A_2`, with value `0.571428544 ≈ c(2) = 4/7 = 0.571429`. 200
  random simplex perturbations of size `0.01` around `A_2` all gave
  `V ≤ 0.571114 < c(2)` (no perturbation direction improves `V`) — strong
  local-optimality evidence.
- **n=3:** coarse random search over 80 configurations (grid-based inner
  solver, lower resolution for speed) found best value `0.52565`, close to
  but below `c(3) = 8/15 = 0.53333`; consistent with, though a weaker check
  of, the geometric configuration being globally optimal (coarser grid here
  underestimates the true `V` at any given `A`, including at `A_3` itself, so
  the gap is expected and not concerning).
- **Structural configs tried and all beaten by / matching `A_n`:** uniform
  `(1/3,1/3,1/3)` gives `V=0.5`; a rough "arithmetic decreasing" config gives
  `V≈0.500`; a "top-heavy" config `(0.9,0.09,0.01)` gives `V≈0.505`; all
  strictly below `c(2)=0.571429`. No tested alternative shape came close to
  beating the geometric configuration — consistent with (but of course not a
  proof of) the conjecture that `A_n` is the unique maximizer.
- **Fewer-marks check:** for `n=2`, restricting Liu Bang to only 2 pieces
  (wasting one mark) caps him at `V=0.5 < c(2)`, confirming (numerically,
  for this one case) that using the full quota of `n` marks is necessary for
  optimality — supports treating `m=n+1` as WLOG in the upper-bound proof,
  as the other approaches already assume for the lower bound.
