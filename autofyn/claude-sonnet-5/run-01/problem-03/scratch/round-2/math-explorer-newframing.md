## imo-2026-03

### Context / what I was asked to find
All 3 live approaches (`geometric-dominance-construction`, `recursive-embedding-induction`,
`equalization-potential-bound`) share one framing: reduce via Lemma 1
(claiming-phase = odd-rank sum) to `c(n) = max_A min_B oddrank(B)`, fix
`A = A_n` (the geometric sequence), and get stuck on the SAME gap — proving
`oddrank(B) ≥ c(n)` when Xiang Yu spends `k ≥ 1` of his marks splitting Liu
Bang's top piece. A 4th approach, `majorization-smoothing.md`, already exists
(unsolved, skeleton only) and is a genuinely different framing (continuous
calculus/concavity on the piecewise-linear value function) — I did **not**
duplicate that; instead I hunted the crux corpus and did targeted numerics
for a framing distinct from both the induction family and the smoothing
family.

### Distinct openings found this round
1. **"Surrogate / relaxed-adversary" framing (crux `aimo-0560`, IMO 2022-ish
   gardener/lumberjack problem):** the general technique is "replace the real
   adversary by a strictly more powerful surrogate whose reply is pointwise at
   least as damaging; if Liu Bang still guarantees `≥ c(n)` against the
   surrogate, he guarantees it against the weaker real Xiang Yu." **I tested
   the most natural instantiation numerically and it FAILS** — see Cheap-kill
   / dead-end note below. This is worth reporting precisely so the outliner
   doesn't waste a round rediscovering the failure: giving Xiang Yu *more
   marks* than `n` (a natural "relaxation") strictly *helps* him below
   `c(n)`, so budget-relaxation is not a valid domination direction here. A
   surrogate framing could still work if the relaxation is engineered to
   preserve the exact mark-count `n` while only removing *shape* constraints
   (e.g. "Xiang Yu may use up to `n` marks anywhere, in one global optimization,
   without the discrete combinatorial-type case split the other approaches are
   doing") — i.e. attack the SAME `max_A min_B` problem but skip casework by
   treating Xiang Yu's move as one continuous nonlinear program over an
   `n`-mark budget and finding its optimum by generic optimization theory
   (KKT/Lagrangian at fixed total mark count) rather than by "which piece gets
   how many marks" case enumeration. This is close in spirit to but distinct
   from `majorization-smoothing`'s calculus route: it targets the *budget
   constraint itself* (a single scalar constraint `Σ marks = n`) as the
   binding Lagrange constraint, rather than trying to prove concavity of the
   whole value function region-by-region.
2. **Binary-tree / Kraft-inequality framing (my own idea, no direct crux
   match found):** the answer `c(n) = 2^n/(2^{n+1}-1)` and the whole
   two-phase mark-then-cut structure has a "prefix code" flavor: model the
   at-most-`2n` total marks (both players' `≤ n` each) as building a binary
   tree of depth-annotated cuts, where Liu Bang's marks create the first
   `≤ n+1` leaves and Xiang Yu's marks refine `≤ n` of those into children,
   and try a Kraft-type inequality (`Σ 2^{-depth(leaf)} ≤ 1`) to directly
   bound `oddrank` combinatorially by leaf-depth rather than by piece-length
   case analysis. I could not find a clean way to make oddrank (a
   *rank*-based, not depth-based, functional) line up with tree depth in the
   time available — flag this as an interesting but UNVERIFIED direction,
   not a vetted opening. Do not over-invest without first checking whether
   depth and rank actually correlate monotonically in the optimal play (they
   do NOT obviously, since oddrank only cares about the sorted VALUES, and a
   piece's depth doesn't determine its value once splits are uneven).
3. **Direct KKT/Lagrangian-on-simplex framing**, closely related to opening 1:
   treat the whole thing as one joint optimization `max_p min_q L(p,q)`
   over two simplices (Liu Bang's `p ∈ Δ_{n+1}`, and Xiang Yu's response
   parametrized directly as a stochastic/fractional split matrix with a
   single linear budget constraint `Σ(#cuts) ≤ n`), and invoke von Neumann /
   Sion minimax type reasoning to swap `max min` and `min max`, computing the
   `min max` side instead (which may be more tractable since Liu Bang moves
   after fixing a response-shape). **Caveat found in `knowledge_base.md`:
   there is no minimax/LP-duality entry in the KB at all** — this route
   would be self-contained work, not KB-supported, and the objective
   (odd-rank sum) is only piecewise linear, not smooth, so classical
   minimax theorems need real care about compactness/continuity before
   they apply. Flag as promising but unsupported by any existing tool.

### Candidate technique(s)
- Budget-constrained Lagrangian/KKT optimization treating "number of marks
  used" as the single binding scalar resource (opening 1/3) — most concrete
  and closest to actionable of the three.
- Kraft-inequality/prefix-code combinatorial bound (opening 2) — speculative,
  unverified, likely needs a genuinely new invariant linking depth to rank.

### Cheap-kill candidates
- **Budget monotonicity check (I ran this numerically, n=2): confirmed
  DEAD END for the naive surrogate.** Giving Xiang Yu extra marks beyond his
  actual budget `n` strictly lowers the achievable `oddrank` below `c(n)`
  (see numeric table below) — so "relax Xiang Yu's power by loosening his
  mark budget" is NOT a valid one-directional domination for this problem;
  any surrogate argument MUST preserve the exact budget `n`, only relaxing
  the *shape* of his move space. Save the next round from re-trying this.
- Symmetry/parity: none obvious beyond what's already used (top-piece
  domination, Lemma 2).

### Knowledge-base entries to use
- `knowledge_base.md`'s "Piecewise-concavity smoothing" entry (line ~20) is
  the one relevant KB entry for the calculus-family route
  (`majorization-smoothing`, not mine) — worth the outliner cross-checking
  its exact statement (concave-on-subintervals ⇒ min at endpoints) against
  what `majorization-smoothing.md`'s Lemma C needs.
- No minimax/LP-duality/Kraft-inequality entries exist in `knowledge_base.md`
  — openings 1/3 and 2 above would be unsupported, self-contained arguments
  if pursued.

### Analogous past problems (cruxes)
- **`aimo-0117`** (Jesse/Tjeerd two-box stone game, Dutch olympiad) — genuinely
  analogous structural crux: *"Assign the played values as a two-sided
  geometric (dyadic) sequence so that the single largest value strictly
  exceeds the sum of all the others"* — this is exactly the top-piece
  domination already certified as Lemma 2 in `geometric-configuration-facts.md`.
  Confirms geometric/dyadic domination is a recognized, load-bearing crux
  for this class of two-phase adversarial value games — supports (but does
  not newly unlock) the existing framing. A second crux from the same
  problem, *"defer committing the extreme value until the opponent's move
  vacates its target cell,"* is a "wait-and-adapt" idea that none of the
  4 current approaches use — could be worth the outliner considering for
  the upper-bound half (arbitrary Liu Bang configs), which no approach has
  attempted yet: instead of assuming Liu Bang commits to `A_n` up front,
  check whether an adaptive/robustness argument bounds ANY configuration.
- **`aimo-0560`** (2022 IMO C6 gardener/lumberjack) — crux *"replace the
  adversary with a strictly stronger surrogate whose reply is pointwise at
  least as damaging, so a win against the surrogate transfers down and the
  reply collapses to a finite per-region menu"* — the general technique
  behind opening 1, but my numeric test shows the most natural
  instantiation (relax mark budget) fails here; a correct instantiation
  would need to relax shape, not budget.
- **`aimo-0663`** (IMO 2022 C? "no-consecutive picks" combinatorial game) —
  read but judged NOT closely analogous: its crux (component-counting /
  pigeonhole on gaps) doesn't transfer to a continuous-length claiming game.
  Mentioned for completeness, not recommended.
- No crux found that solves a length/interval-splitting alternating-claim
  game with a two-phase (mark-then-claim) structure exactly like this one —
  the corpus's `games-and-strategy` subtopic is dominated by discrete
  board/token games, not continuous-interval value games. This problem's
  precise shape (odd-rank-sum value + geometric-config domination) appears
  to be a genuinely hard, not-directly-precedented combination.

### Prior progress
See `current.md` — certified Lemma 1 (claiming value = oddrank), certified
Lemma 2/3/Prop A/Prop 4 (geometric config facts), and the interior-point
obstruction lemmas (D/E). Central open gap: `k ≥ 1` sub-case of the lower
bound against `A_n`, plus the entirely-untouched upper bound over arbitrary
(non-geometric) Liu Bang configurations.

### Dead ends (do not retry)
- Naive "relax Xiang Yu's mark budget above n" surrogate argument — **newly
  confirmed dead end this round** (numeric check below): it breaks the
  bound, doesn't preserve it. Any future surrogate/relaxation approach must
  keep the budget exactly `n`.
- (Carried over) `equalization-potential-bound`'s "LP shortcut is provably
  impossible" claim — still only conditionally correct per `current.md`;
  I did not re-verify this round, no new information.

### Small-case / intuition notes (numeric, n=2 config `A_2 = {4/7, 2/7, 1/7}`, `c(2) = 4/7 ≈ 0.5714`)
I ran a bounded nonlinear optimization (scipy, softmax-parametrized split
ratios, `Nelder-Mead`, many random restarts) over all combinatorial
allocations of Xiang Yu's marks among the 3 pieces of `A_2`, **budget = 2
(the real budget)**:
```
alloc (m1,m2,m3)   min oddrank found     c(2)
(0,0,2)            0.6429                0.5714
(0,1,1)            0.6429                0.5714
(0,2,0)            0.7143                0.5714
(1,0,1)            0.5714  <- exact      0.5714
(1,1,0)            0.5714  <- exact      0.5714
(2,0,0)            0.5714  <- exact      0.5714
```
**Conjecture-confirming (n=2 only, not a proof):** every allocation that puts
`≥ 1` mark into the top piece `p_1` achieves *exactly* `c(2)` (matches
Proposition 4's construction and its variants); every allocation that leaves
`p_1` untouched (`k=0`) achieves something *strictly larger* than `c(2)`
(consistent with Proposition A's inequality, and here bounded away, not just
approached in a limit, because only 2 marks are available so the tail can't
be split arbitrarily finely). This is useful auxiliary evidence for the
outliner: it suggests the shared central gap ("prove `oddrank(B) ≥ c(n)` for
`k ≥ 1`") is not just true but has an EXACT-equality flavor for essentially
every allocation touching `p_1`, not just Proposition 4's specific one — i.e.
there may be a wider family of optimal Xiang-Yu responses than currently
proven, which could make an exchange/invariance argument (showing all
"touches-`p_1`" allocations are equivalent up to the self-similarity of
Lemma 3) more tractable than pinning down one specific split.

Separately, I checked (numerically, same `A_2`) that **relaxing Xiang Yu's
budget above `n=2` strictly breaks the bound**:
```
budget    best oddrank found     c(2)
2         0.5714 (= c(2))        0.5714
3         0.5000                 0.5714
4         0.5000                 0.5714
6         0.5000                 0.5714
10        0.5000                 0.5714
```
i.e. with more marks than his true budget, Xiang Yu can drive `oddrank`
down to `1/2` (half the total stick length — the natural floor once he can
split everything into arbitrarily many pieces, since claiming alternates on
a huge equal-ish multiset). This is decisive numeric evidence (not a proof,
but for a single concrete `n`) that the naive budget-relaxation surrogate
argument (opening 1's most obvious instantiation) is false and must not be
attempted as stated — flagged as a confirmed dead end above.
