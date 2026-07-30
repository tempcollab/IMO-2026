## imo-2026-03 (GAP L, lower-bound Case B residual — genfn/dyadic/count-parity lens)

### Distinct openings

1. **Greedy-tiling / bounded-window nonneg-block argument (genuinely new framing, from crux
   `aimo-0626`).** The target `λ_{(0,θ)}{M odd} ≥ ∫_{(0,θ)}M` (equivalently `D̃−1=Σψ(c_i)Δw_i≥0`,
   §3 of `induction-recursion-telescope.md`) has EXACTLY the shape of "prove `Σ_{k∈T}a_k≥0` where
   `T` = indices with *some* bounded-length window summing `≥0`" (aimo-0626, IMO-shortlist style).
   That problem's crux move is: certify each "good" term by its *minimal witnessing window* (length
   `≤m`), then **greedily tile the whole line left-to-right into disjoint blocks, each of nonnegative
   sum**, by repeatedly consuming the first good index and its witnessing window. Applied here: treat
   each interval `i` with `ψ(c_i)≥0` (i.e. `c_i≤1`, "locally good," Lemma T's per-term win) as a seed,
   and try to tile the WHOLE merged order into disjoint consecutive blocks each with net `Σψ(c_i)Δw_i
   ≥0`, where a "bad" run (`c_i≥2`) is absorbed into the block by extending it (bounded by the local
   cut-budget) to include enough adjacent "good" mass. This is structurally different from the
   currently-pursued Abel/lattice-path identity `(♠)` (which is a *global running-sum* argument): it
   is a **local block-decomposition** claim, but crucially NOT the refuted "1-1 anchor matching" (§10
   of the telescope file) — aimo-0626's greedy blocks are *many-to-one* and *bounded by m*, not
   matched pairwise by value/width domination. The natural analogue of "`m`" here is the **total cut
   budget `n`** (or the *local* number of extra fragments `a_j` at a given scale): since
   `Σ_{j}a_j≤n`, only `n` extra "T" or "B" tokens exist beyond a perfectly-alternating skeleton, so
   any `c_i≥2` excursion can only last while consuming budget, giving an a priori bound on how many
   bad blocks there are and how deep they run. Worth scouting whether a **left-to-right greedy
   block-tiling of the merged list** (not a matching, not a running Abel sum) closes `(♠≥0)` directly.
   This sidesteps §10's refutation because it never asserts a per-run *value* domination — only a
   *net block-sum* domination, which is exactly what survived in the counterexample of §10 (single
   big `Y`-value dominated by SEVERAL smaller `Z`-odd values *summed*, which is precisely a
   nonnegative-block claim, not an injection).

2. **Induct on total cut-budget `k=Σa_j` (not on dyadic depth `n`).** All prior work inducts on `n`
   (via the Structure Lemma's recursive dyadic decomposition, §5 of the telescope file, or the IH
   `P(n−1)` applied to `Z`). An orthogonal induction variable is the **number of cuts already made**:
   start from the "all-uncut" configuration (`F={1,2,…,2^n}` itself, trivially `E(F)=2^{n-1}·(...)`,
   easily `≤2^n−1` — check by hand) and show that **each additional cut** (splitting one current
   part into two) changes `E(F)` by a bounded, sign-controlled amount, so that `E(F)≤2^n−1` is
   an invariant maintained cut-by-cut rather than proved by a global identity. This is a genuinely
   different top-level target (a monovariant/invariant argument over the sequence of `≤n` cut moves,
   cf. knowledge_base "Invariants & monovariants" and "Constructive/incremental: realize every value
   by starting from an extreme and adding one unit at a time"). It has NOT been tried by either
   induction-recursion slug (both use IH on `Z`'s sub-multiset via dyadic *depth*, not step-by-step
   *cut count*). Caution: a single cut can change many ranks at once (inserting an element shifts the
   parity-role of everything below it), so the per-cut increment of `E(F)` is not obviously simple —
   this needs to be checked before committing, but it is untried terrain.

3. **2-adic / signed-digit recast, mirroring the already-certified UPPER BOUND proof.** The
   certified `lemmas/upper-bound.md` proves `D≤u_n·Σ` via a `{−1,0,1}`-subset-sum pigeonhole on the
   `2^{n+1}` subset sums of the Liu partition (Realizability Lemma / Theorem R). The lower bound's
   residual `E(F)≤2^n−1` is the DUAL inequality on the SAME dyadic weights `{1,2,…,2^n}`. It is
   tempting to seek a matching "signed-digit" argument: every simultaneous refinement `F=⊎π_j` of the
   dyadic partition corresponds to choosing, for each dyadic level `j`, a partition of `2^{n-j}` into
   `a_j+1` parts; encode each part's rank-parity contribution as a `±1` weighted digit and try a
   roots-of-unity / generating-function identity (cf. crux `aimo-0155`: "roots-of-unity filter turns
   an even-minus-odd difference into one sum over roots of unity," and `aimo-0509`/`aimo-0050`:
   "encode a statistic as generating polynomial, read equal-block claims off cyclotomic
   divisibility"). Concretely: define `f(x)=Σ_{π∈F} x^{rank(π)}` or a bivariate polynomial tracking
   `(value, rank-parity)`, and ask whether `E(F)≤2^n-1` becomes a **coefficient inequality** provable
   by evaluating at `x=−1` (which directly recovers `O(F)−E(F)=D(F)`, already known) — this doesn't
   obviously add power beyond `(♠)` unless a *second* generating variable (tracking cut-budget/scale)
   gives extra structure, e.g. a `q`-analogue where `q` marks dyadic scale `j` and the target becomes
   a coefficientwise or evaluated inequality in `q` at `q=1/2`. This is the most speculative opening —
   flag it as worth ONE probe (try `n≤3` explicit polynomials by hand/sympy) before investing, since
   the "not pointwise" obstruction noted in `(♣)`'s note (§2 of telescope file: `1[M odd]≤M` fails
   pointwise, only holds after integration) suggests a naive generating-function coefficient argument
   will hit the same wall unless the two-variable (value × scale) structure is genuinely exploited.

### Candidate technique(s)
- Greedy left-to-right block-tiling with bounded lookahead (opening 1) — a genuinely different
  top-level argument shape than Abel-summation / lattice-path (currently owned by both induction
  slugs), and explicitly NOT refuted by §10 (which only killed 1-1 value/width matching, not
  many-to-one bounded-block domination).
- Cut-count induction / monovariant (opening 2) — untried induction variable.
- 2-adic/generating-function recast dual to the certified upper-bound pigeonhole (opening 3) —
  speculative, needs a cheap hand-probe at n≤3 before committing effort.

### Cheap-kill candidates
- For opening 1: before building the full tiling argument, hand-check on the two documented
  hard witnesses (`n=5,Y=(17.9,14.1),Z=(11.418,8,4.582,4,2,1)` from §10, and the tie config
  `n=4,Y=(8,3,3,2),Z=(8,2,2,2,1)` from §14) whether a **greedy left-to-right block partition** of
  the merged list into consecutive blocks each with `Σψ(c_i)Δw_i≥0` actually exists. If it does on
  both witnesses, this is strong evidence for opening 1; if it provably can't (e.g. the negative
  block at the very start of the list has no available "good" mass to its LEFT within any bounded
  window — since greedy tiling in aimo-0626 goes strictly left-to-right consuming what's ahead, not
  behind), that kills it fast. NOTE the direction matters: aimo-0626 tiles using the window
  *following* each good index; our sequence's bad excursions (`c_i≥2`) tend to occur in the *middle*
  of a T-run, with the compensating "anchor" mass (`Z`'s big pieces) typically ABOVE the excursion in
  value order (they appear EARLIER in the descending merged list, i.e. to the left) — so the natural
  direction for tiling may need to run right-to-left or use a two-sided window; check both before
  concluding.
- For opening 3: literally hand-compute `f(x,q)` or the `x=-1` evaluation for the `n=2` and `n=3`
  worked examples already in the telescope file (§4, §6) to see if a clean identity falls out in
  under 30 minutes; if not, deprioritize — this is the most speculative opening and should not
  consume a full round if the n≤3 probe doesn't show a pattern quickly.

### Knowledge-base entries to use
- "Invariants & monovariants" and "Constructive/incremental: realize every value by starting from
  an extreme and adding one unit at a time" (Combinatorics section) — for opening 2.
- "Pigeonhole / extremal principle" — already the backbone of the certified upper bound
  (`Subset-Sum Pigeonhole`); opening 3 tries to dualize it.
- No SOS/LP entry applies (potential-certificate slug already showed no separable per-piece
  potential works — a relevant negative fact to keep in mind for opening 2's per-cut invariant: a
  *separable* invariant is refuted, but a *non-separable, order-aware* invariant maintained
  cut-by-cut is NOT the same claim and is not covered by that refutation).

### Analogous past problems (cruxes)
- **`aimo-0626`** (IMO-shortlist-style "good index" problem, subtopic `prefix`/discrepancy-adjacent,
  domain combinatorics). Crux: certify each good index by a *minimal witnessing window*, then
  **greedily tile the sequence into disjoint nonnegative-sum blocks** left-to-right; extend to a
  cyclic/asymptotic version by concatenating `N` copies. This is the best structural analogue found —
  the target shape `Σ_{k∈T}a_k≥0` (T = a "locally good" index set) matches our
  `λ_{(0,θ)}{M odd}≥∫_{(0,θ)}M` almost exactly if one reads `T={t:M(t) odd}` as the good set and
  `a` as the density `M(t)dt`. Recommend the outliner read this crux's `how_used` field in full via
  `past_crux_moves_database.json` (problem_id `aimo-0626`) before building on opening 1.
- **`aimo-0715`** (2-adic-valuation extremal sequence construction, subtopic `signed-sum`/`prefix`):
  crux is "index terms by the 2-adic valuation of position so every window has a unique
  maximal-valuation position" and "greedily choose signs to pull partial sums toward zero, forcing
  bounded prefix-sum windows." Thematically dyadic and about bounded prefix-sum excursions, but the
  problem (extremal sequence length avoiding signed-zero-subsums) is not structurally close enough
  to our rank-sum inequality to import a move directly — flag as a weak analogue only, for the
  "bounded excursion via 2-adic indexing" intuition, not for a specific lemma.
- **`aimo-0155`** (roots-of-unity filter turning an even/odd-count difference into a sum over roots
  of unity): relevant ONLY if opening 3 (generating-function recast) is pursued; not otherwise
  analogous (their problem is a genuine modular/coloring count, ours is a rank-sum on a real-valued
  dyadic partition, no natural modulus).
- No crux found that is a strong match for the "dyadic cut-tree with cut-budget ≤n" structure itself
  — this appears to be a genuinely bespoke structure for this problem; do not expect a crux to hand
  over the whole mechanism, only local techniques (tiling, invariant bookkeeping).

### Prior progress
See `induction-recursion-telescope.md` — fully certified up through the position-parity identity
`(♠)`/`(♠′)` and the self-contained restatement `E(F)≤2^n−1` (§8–§9). Lemma T closes `maxc≤1`
(certified `lemmas/termwise-lattice.md`). Threshold-split identity `(△)` (§13) localizes the residual
to `(0,θ)` with bounded mass `≤1`. All of this is importable as-is; my lens does not need to re-derive
it, only find the missing final step.

### Dead ends (do not retry)
- Local 1-1 value/width-dominating injection `{Y even-pos}→{Z odd-pos}` — REFUTED (§10, 21% failure
  rate, explicit witness). Any new approach must NOT propose a per-run/per-anchor pairwise match.
- Top-down reserve of `Z` (`Z`'s odd-measure leads its even-measure from the top`) — REFUTED (§14,
  7306/4·10⁵ violations). The surplus is bottom-inclusive; do not propose threshold-`τ`-indexed
  reserves that only look above `τ`.
- Scalar/count summary of `Z` (replacing `Z` by any multiset with the same sum and `altsum≥1`) —
  REFUTED (probes 5–7, round 4). Any closure must use `Z`'s actual dyadic origin (Structure Lemma),
  not just its aggregate statistics.
- Unconditional Termwise Lemma (`D≥sum(Y)-sum(Z)` without the `maxc≤1` guard) — explicitly flagged
  FALSE in `lemmas/termwise-lattice.md`'s Guard section; never invoke without the hypothesis.

### Small-case / intuition notes (conjectural, numerically supported by prior rounds only)
- The residual `E(F)≤2^n−1` has verified `0` violations over `4·10^5` random configs (n≤5), with
  equality attained at zigzag/tie configs — so the inequality itself is very likely TRUE (strong
  numerical confidence), the only issue is finding a rigorous *mechanism*, not the truth of the claim.
- My own read of the counterexample to local matching (§10: `Y_even=(14.1)` dominated by
  `ΣZ_odd=18` from THREE separate `Z`-parts at three different scales) suggests the true mechanism is
  a **sum over an unbounded-looking but actually budget-bounded set of compensating terms** — exactly
  the shape a bounded-window greedy tiling (opening 1) or a cut-budget induction (opening 2) would
  produce, reinforcing that these two are the most promising openings to pursue next, over a
  generating-function recast (opening 3, more speculative).
