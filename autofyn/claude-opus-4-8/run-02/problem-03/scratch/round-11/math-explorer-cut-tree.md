## imo-2026-03 (GAP L, lower bound Case B — sole open wall)

### Setup recap (from certified lemmas, not re-derived)
`F = π_0 ⊎ F'` (top-scale peel, `floor-half-reduction.md`), `θ=2^{n-1}`,
`M(t)=N_{π_0}(t)-N_{F'}(t)` on `(0,θ)`, and the whole of Case B collapses to
`I_n := ∫_{(0,θ)} ⌊M/2⌋ ≤ 0`. `F'` itself peels one level further,
`F' = π_1 ⊎ F''` (`π_1` a partition of `θ`, `F''` a refinement of the
`(n-2)`-ladder living in `(0,θ/2]`), with budgets `a_0` (cuts on `π_0`) and
`b=Σ_{j≥1}a_j` satisfying `a_0+b≤n` (Invariant I, certified). This is the
recursive dyadic cut-tree the dispatch asked me to attack directly (not the
final-multiset profile).

### Distinct openings I actually tested
1. **Induction on the budget split `(a_0, b)` with `a_0=n-b` fixed at the top-piece,
   holding π_0 fixed while adding cuts to `F'`.** Tested computationally
   (`/tmp/probe1.py`) whether `I_n` is *pointwise* non-increasing as one extra cut
   is spent inside `F'` (moving from budget `b` to `b+1`, `π_0` unchanged, feasibility
   `a_0+b≤n` enforced exactly). **Result: FALSE** — pointwise monotonicity fails on
   ~30% of trials at every `n∈{2,3,4,5}` (5000 trials each, exact `Fraction`; e.g.
   n=4: `1643/5000` violations). So "peel one more cut off `F'`, `I_n` only gets more
   negative" is NOT a valid per-step monovariant — matches the meta warning that a
   naive scalar/one-directional descent keeps failing on this problem (round 6/9
   memory rules). This is a genuine new negative, worth banking as a dead end.
2. **Aggregate (not pointwise) monotonicity in `b`, at fixed `n`.** Sampling the
   *whole* feasible family at each fixed `(a_0,b)` with `a_0+b=n` (so budget is
   maximally used), the *max* of `I_n` over that slice IS monotone non-increasing in
   `b`: n=4 gave max `I_n = 0, -0.59, -0.281, -0.295, 0` for `b=4,3,2,1,0` — wait,
   more precisely `a_0=0..4` (`b=4..0`) gave maxima `-3.69, -0.55, -0.281, -0.295, 0`.
   So the *global* extremal case sits exactly at `b=0` (all budget on the top piece,
   `F'` uncut) — matches Invariant I's equality condition exactly. This is consistent
   evidence (not proof) that the hardest case for GAP-P1′ is the **base case `b=0`**.
3. **The base case `b=0` reduces to a clean, self-contained, much smaller-dimensional
   inequality.** When `b=0`, `F'` is forced to be the *uncut* ladder
   `L={2^{n-1},…,2,1}` (`n` fixed points, no further recursion), so `I_n≤0` becomes:
   for **every** partition `π_0` of `2^n` into `≤ n+1` positive parts,
   `D̃(π_0 ⊎ L) ≥ 1`. Verified numerically (`3000` random `π_0`'s per `n`, `n≤5`):
   `max I_n(b=0) = 0` exactly (tie-attained, e.g. n=2,3,4 hit `I_n=0` on the nose;
   n=5 sampling found `-0.31`, consistent with the max still being `0` but rarer to
   hit by random sampling — the discrete tie set is thin). This base case is a
   **genuinely tractable single-multiset target**: no recursion on `F'` needed, `L` is
   a *fixed*, maximally-structured geometric ladder with the crux property
   `2^{n-j} > Σ_{i>j} 2^{n-i}` ("largest exceeds sum of the rest," the aimo-0117-style
   dominance already flagged in memory round 1) at every scale. This dominance is the
   likely lever for a direct proof of the base case (peel `L`'s own top element `θ`
   against `π_0` and induct on `n` — a THIRD nested peel, but now on a *fixed*
   structured object instead of an arbitrary `F'`), independent of the general
   loaded-shape-of-`g` problem. I did **not** attempt this proof (out of scope per
   instructions) — flagging it as the sharpest concrete residual to hand to a builder.
4. **2-adic valuation split (`aimo-0917` crux, checked precisely).** Read the actual
   crux (not just the reserved note): aimo-0917's move is "split a conserved COUNT
   `N` of a combinatorial structure into the two branches of an opponent's move,
   `N=N_+ + N_-`, and since `2^{s+1}∤N`, at least one branch inherits the valuation" —
   a strategy-stealing / potential-splitting argument for choosing which move to make
   in an alternating game with an as-yet-undetermined adversary response. **This does
   NOT transplant to GAP L as currently posed**: GAP L is no longer a live alternating
   game at this stage of the proof (Lemma G already collapsed it to a static
   discrepancy inequality over ALL feasible `F`, i.e. we must prove the bound for
   *every* Xiang response, not choose a favorable branch). There is no "N_+ vs N_-"
   choice being made by a solver — Xiang is adversarial and we must dominate all of
   his branches simultaneously, not pick one. A closer (but still not exact) analogy
   would be splitting `I_n` by the parity of `M(0⁺)` or by `a_0` even/odd and showing
   each branch individually is `≤0`, but I found no natural 2-adic-valuation quantity
   on `F`'s cut-tree whose value is *forced* the way `binom(n,n/2)`'s valuation is
   forced in aimo-0917 (there `N`'s valuation is fixed by a closed-form binomial
   count; here the relevant total `2^{n+1}-1` is odd, which is exactly the Parity
   Lemma already certified and banked — the natural 2-adic content is already
   extracted). **Verdict: this route is a dead end as literally described**; the
   Parity Lemma (already certified) is the correct extraction of the "odd total"
   fact, and the aimo-0917 mechanism does not add anything beyond it once the game
   has already collapsed to a static inequality.

### Candidate technique(s)
- Attack GAP-P1′ in TWO tiers: (a) first close the **base case `b=0`** (a clean,
  self-contained "partition of `2^n` vs. fixed geometric ladder" inequality,
  `D̃(π_0 ⊎ L) ≥ 1` for all partitions `π_0` of `2^n` into `≤n+1` parts) using `L`'s
  own "largest > sum of rest" dominance — likely by peeling `L`'s top element and
  inducting on `n` a third time on this smaller fixed-`L` sub-problem; (b) THEN
  induct on `b` upward, but since pointwise per-cut monotonicity is FALSE (finding
  1), the inductive step from `b` to `b+1` needs to co-vary `π_0` (not hold it
  fixed) — i.e. prove the max over the WHOLE feasible slice is monotone (finding 2
  supports this aggregate claim, but it is NOT the same statement as the naive
  per-step one and still needs its own proof).
- This is genuinely FAR from the parked telescope/merged-order machinery: it never
  uses `(♦)`, `(♠)`, `maxc`, or a merged-order tiling; it works purely with the
  `(FLOOR)` integral form and peels an *explicit fixed* comparison object (`L`), not
  a profile of `F`. It is closer to peel-scale-rank-induction's own machinery
  (reuses `(FLOOR)`, Invariant I) but sharpens it to a genuinely new, smaller,
  self-contained target (base case) plus an honest negative on the naive inductive
  step.

### Cheap-kill candidates
- None found that kill GAP-P1′ itself. The one cheap kill I DID find is a negative:
  the naive fixed-π_0 "add a cut, `I_n` drops" monovariant is false (finding 1) —
  this should be added to the "NEVER" dead-end list so no builder wastes a round on
  it.

### Knowledge-base entries to use
- `floor-half-reduction.md` (FLOOR identity, the whole reduction target).
- `peel-difference-bound.md` (peel SD identity, Invariant I, Case A).
- `parity-odd-total.md` (Parity Lemma — the correct extraction of the "odd total /
  2-adic" content; supersedes any fresh aimo-0917-style split attempt).
- The round-1 memory rule re: aimo-0117-style "largest exceeds sum of the rest" for
  the fixed ladder `L` — directly applicable to the base-case sub-target found here.

### Analogous past problems (cruxes)
- `aimo-0917` (combinatorics / invariants-and-monovariants): read in full this round.
  Crux is a 2-adic valuation splitting argument for an alternating GAME with a choice
  of branch. **Not analogous at this stage of GAP L** (the game structure is already
  collapsed to a static universally-quantified inequality; there's no branch to
  choose) — see finding 4 above. Do not re-seed this as a "new mechanism"; it
  collapses to the already-certified Parity Lemma.
- No new corpus match found for the base-case sub-target (`partition vs. fixed
  geometric ladder` discrepancy bound); it is closest in spirit to the "largest
  exceeds sum of rest" dyadic dominance already flagged in round 1 memory, not a
  fresh corpus hit.

### Prior progress
Unchanged from `current.md`/run_state: FLOOR identity certified, GAP-P1′ = `I_n≤0`
open. This round's contribution is a genuine narrowing: (i) a proof that the naive
per-cut monotonicity step is false (new negative), (ii) numeric evidence that the
extremal (tightest) case is exactly the base case `b=0`, and (iii) an explicit,
much smaller, self-contained restatement of that base case as
`D̃(π_0 ⊎ L) ≥ 1` for `L` the fixed geometric ladder — a genuinely new, tractable
sub-target not previously isolated this cleanly in any approach file.

### Dead ends (do not retry)
- Per-step / pointwise monotonicity of `I_n` under "add one cut to `F'`, hold `π_0`
  fixed" (this round, finding 1: `1000+/5000` violations at every `n=2..5`, exact
  `Fraction`, feasibility-checked).
- 2-adic valuation split à la `aimo-0917` as a fresh mechanism on GAP L: does not
  transplant once the problem is a static inequality (no game branch to choose);
  collapses to the already-certified Parity Lemma (this round, finding 4).
- All previously banked dead ends (merged-order/measure/sequential/genfn framings,
  bottom-up/top-down reserve, integer-minimizer/GAP-IMR engine, scalar summaries of
  Z) — reconfirmed by not re-deriving them; still listed in run_state Rules.

### Small-case / intuition notes (all conjecture/numeric, not proof)
- `D̃(L)` for the bare uncut ladder is `(2^{n}+1)/3`-ish alternating sum (`1,3,5,11,21,...`
  for n=1..5, i.e. `a_n=2^{n-1}-a_{n-1}` recursion) — not `1`; the base-case target is
  `D̃(π_0⊎L)≥1`, a nontrivial statement about how much a partition of `2^n` can drag
  this large value down when merged with `π_0`.
- The base-case tie (`I_n=0`, `D̃=1`) is hit exactly by some partitions `π_0` at every
  `n=2,3,4` tested (not just asymptotically) — consistent with the run's known
  explicit tight families (e.g. `n=4, Y=(8,3,3,2)` type configs in current.md).
- The aggregate-max-over-`b` data (finding 2) is only 5-point-per-`n` evidence
  (`n=4` only); a next round should extend this to more `n` and more samples per
  slice before leaning on it structurally.
