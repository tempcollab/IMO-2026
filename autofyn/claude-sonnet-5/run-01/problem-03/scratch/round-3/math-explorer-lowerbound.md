## imo-2026-03 (lens: open lower-bound gap, k≥2 / simultaneous top+tail splitting)

- Distinct openings:
  1. **Vertex-optimality reduction (new angle, cheap to prove, not yet used).**
     For a FIXED composition (which pieces get how many of Xiang Yu's marks),
     `oddrank(B)` as a function of the continuous split ratios is
     **piecewise-linear** (sorting + summing a subset of coordinates is
     piecewise-linear in the coordinates). A linear function on a compact
     convex polytope (the simplex of valid splits for that composition) attains
     its minimum at a **vertex** of the polytope — i.e. at a point where either
     some sub-piece degenerates to length 0, or two elements of the merged
     multiset become exactly equal (a sorted-order tie/crossing). This is
     exactly `majorization-smoothing.md`'s dormant "Lemma C" idea (currently
     `unsolved`, aimed at the wrong sub-problem — Xiang Yu's best response to
     an *arbitrary* Liu Bang `p`, i.e. the harder two-sided problem) but it
     specializes cleanly to just our fixed-`A_n` lower-bound question: it
     converts "prove an inequality over a continuum of real split ratios" into
     "check a finite (though `n`-growing) list of degenerate/tied
     configurations." This is a genuinely different top-level route from the
     other approaches' direct case-split-by-`k` framing: it attacks the
     *shape of the minimizer* first, before attempting any inequality.
  2. **"Wasted mark" reduction / dominated-move lemma.** Numerically (see
     below), splitting the *currently smallest* piece of `B` never strictly
     helps Xiang Yu — it is always at best a tie with reallocating that mark to
     the top piece instead. If provable in general (it looks like a clean
     "inserting two sub-threshold elements at the very bottom of a sorted list
     changes `oddrank` by a fixed, non-favorable amount" fact), this would let
     the proof assume WLOG that Xiang Yu never spends a mark on the current
     minimum piece, shrinking the composition space Xiang Yu must be checked
     against — a genuine size reduction, orthogonal to case-splitting on `k`.
  3. **Peel-one-mark-at-a-time induction on the self-similar recursion**
     (a sharpening of `recursive-embedding-induction`'s stalled Lemma G): instead
     of treating Xiang Yu's whole composition on `p_1` at once (as
     `geometric-dominance-construction`'s Attempt 2 does), induct on `n` by
     peeling off *only the first mark* Xiang Yu spends on `p_1`. That first cut
     produces `p_1 = x + r` (`x` the larger part). By Lemma 3 (self-similarity,
     already certified), the tail `T_0 = λ_n·A_{n-1}`, so the residual game is
     "the level-`(n-1)` game on `A_{n-1}` (rescaled by `λ_n`), but with one
     *extra* piece `r` injected, and `n-1` marks remaining." This is *not* a
     clean instance of the level-`(n-1)` problem (the injected `r` piece is the
     obstruction), but it isolates the entire difficulty into one crisply-stated
     sub-lemma: "how does one extra adversarial piece, of size in a bounded
     range depending on `n`, injected into the (`n-1`)-level self-similar
     sub-game, change the minimax value?" — this is a smaller, better-defined
     open question than the current diffuse "general `k`, general tail-split"
     framing, and is the natural next target for an inductive hypothesis
     strengthening (per the certified negative result that a purely-scalar
     induction cannot work — this framing tells you exactly *what* ordered
     data to carry: the value and rank-position of the single injected piece
     `r`, not more).

- Candidate technique(s): (i) **vertex/extreme-point argument for piecewise-linear
  objectives on a polytope** (standard LP fact, no KB entry names it explicitly
  but it's the rigorous form of "Pólya: specialize / exploit structure" and of
  `majorization-smoothing`'s Lemma C) to legally restrict attention to
  degenerate split configurations; (ii) an **adjacent-transposition / exchange
  argument** (standard technique family, akin to rearrangement inequality
  proofs and greedy-exchange proofs; not itself a single named KB entry, but
  the "General Proof Methods" and "Pólya" sections both point at this style)
  to rule out non-optimal order-types once the vertex reduction cuts the
  option space down to finitely many combinatorial interleavings per `(n,k)`;
  (iii) **strong induction on `n`** via Lemma 3/Lemma G1's self-similarity,
  strengthened per opening 3 above to track the *position* of one extra
  injected piece, not just its value — this directly respects the certified
  negative result in `merge-by-sums-counterexample.md` (sums-only induction is
  false) by explicitly carrying positional data forward.

- Cheap-kill candidates: **splitting the current minimum piece is (numerically)
  never strictly beneficial to Xiang Yu** — tested at `n=2,3,4,5`, reallocating
  that mark to the top piece instead always gives the exact same value to
  machine precision (evidence, not proof; a real proof of this would be a
  legitimate size-reduction lemma, letting the proof ignore compositions that
  touch the smallest piece). Also: **no composition with zero marks on `p_1`
  ever ties `c(n)`** for `n≥2` (all such compositions are numerically strictly
  `> c(n)`, consistent with the certified Proposition A/Lemma 2 margin
  argument) — this is already proved, just confirmed again as a sanity check,
  and marks a clean boundary: any successful general argument must specifically
  handle "at least one mark on top" as the tight/binding regime.

- Knowledge-base entries to use: no single KB entry names "vertex of a
  piecewise-linear-on-simplex minimization" or "exchange/adjacent-transposition
  argument" directly by that name — closest matches are the **General Proof
  Methods** section ("Pigeonhole/extremal: take the largest/smallest object and
  argue it forces the result") and the **Monotone Subsequences /
  Erdős–Szekeres/Dilworth/patience-sort** section (KB has machinery for
  tracking `(I_p,D_p)`-type positional invariants under a sorted sequence,
  conceptually adjacent to what's needed here — tracking how a new element's
  *position* in a sorted merge affects a rank-parity sum — though it is not a
  drop-in tool, just the closest structural analog in the KB). Recommend the
  outliner treat the vertex-reduction step as a KB-free, self-contained LP fact
  to be proved from scratch (it is short: linear function, compact polytope,
  extreme point).

- Analogous past problems (cruxes): searched `combinatorics` / `games-and-strategy`
  (39 cruxes) and skimmed `extremal-principle`/`inequalities-SOS-and-convexity`
  headers. Best candidate: **`aimo-0117`** ("Assign the played values as a
  two-sided geometric (dyadic) sequence so that the single largest value
  strictly exceeds the sum of all the others") — this is the *same*
  super-increasing-sequence idea as our certified Lemma S/Lemma 2 (`p_i >
  Σ_{j>i}p_j`), independently discovered in a different (box-filling alternating)
  game. It is a genuine structural analog for *why* the geometric ratio-2
  configuration is the right one to guess, but its game mechanics (claim
  whole stones into two boxes with capacity constraints) are different enough
  from our stick-cutting/claiming game that its actual proof technique (an
  induction on "largest unplayed dyadic value stays in the target box," a
  positional invariant maintained move-by-move) does not transplant directly
  — it is a validation of the geometric-answer intuition, not a reusable proof
  step for the specific merge-minimization lemma we need. I did **not** find a
  crux that directly proves an "odd-rank/even-rank of a merged sorted multiset"
  minimization result of this shape; recommend flagging this as a genuine gap
  in the corpus for this specific problem, not a dead end in the search itself.

- Prior progress: `k=0` (Proposition A) and `k=1` tail-untouched (Lemma F1) are
  fully certified for all `n`. `n=1` is fully closed (Lemma G0, every `k`).
  The "doubling family" `C_k = {p_2,...,p_{k+1}, p_1-Σp_i}` is confirmed (both
  by the certified Proposition 4 recipe and independent numeric optimization)
  to achieve exact equality `oddrank = c(n)` when the tail is untouched, for
  every tested `n,k`. New this round: full composition-level numeric sweep
  (all ways to allocate `n` marks among the `n+1` pieces of `A_n`, continuous
  split ratios optimized per composition via `scipy.optimize` with many random
  restarts, `n=2,3,4`) finds **no violation of the conjectured bound
  `oddrank(B) ≥ c(n)`** in any tested composition, strongly reinforcing the
  conjecture at the "all marks used, any allocation, any split ratios" level
  (this is the first check that includes simultaneous top+tail splitting, not
  just the tail-untouched sub-case).

- Dead ends (do not retry, verified again): (a) the "merge-by-sums-alone"
  candidate lemma (bounding `oddrank`/`evenrank` of a merge using only
  aggregate sums `Σ(S)`,`Σ(T)`) is **certified false** — re-confirmed the
  counterexample in `merge-by-sums-counterexample.md` is correct (exact
  arithmetic, reproduces `oddrank(S∪T)=109/100 < Σ(S)=110/100`); do not
  attempt any induction-on-`n` argument that only uses the scalar recursion
  `c(n)=2λ_n c(n-1)` without carrying positional/ordered data. (b) The naive
  extension of Lemma F1 to "tail simultaneously refined with unboundedly many
  pieces" is false (confirmed: `oddrank → 0.501 < c(2) = 0.571` as tail-split
  count `N→∞`) — but this is a red herring for the *actual* bounded-marks game:
  my new composition-level sweep (which respects the `≤n`-marks budget
  strictly) found no violation, so the true obstruction is specifically
  "unboundedly fine splitting," not "any simultaneous tail split," and future
  rounds should not treat Lemma F1's failure-to-extend as evidence the general
  bounded-marks claim is in danger.

- Small-case / intuition notes (all conjecture, from numerics, `n=2,3,4`):
  - **Correction to a naive first guess:** my initial small-`n` (`n=2,3`) sweep
    suggested "any composition with ≥1 mark on `p_1` ties `c(n)` exactly,
    regardless of how the rest are allocated." This is **false** at `n=4`: out
    of 55 tested compositions with `comp[0]≥1` (`4` marks total), only 15 tie
    `c(n)` exactly; the other 40 give strict excess (e.g. `comp=(1,0,0,0,3)`,
    i.e. 1 mark on top and 3 marks squandered splitting the smallest piece,
    gives `0.5806 > c(4)=0.5161`). So "touches the top" is necessary but far
    from sufficient for tightness — the *tie set* is a specific, structured
    subset (e.g. `(4,0,0,0,0)`, `(3,1,0,0,0)`, `(3,0,1,0,0)`, `(2,1,1,0,0)`,
    `(1,1,1,0,1)`, ... — 15 total at `n=4`), and its pattern looks consistent
    with marks being spent *recursively down the self-similar chain* (matching
    Lemma G1's `c(n)=2λ_n c(n-1)` structure: spend one mark on top, then
    recursively either split the resulting remainder further or split the next
    tail level, one level at a time) rather than any single "prefix" or "top
    mark count" rule. This refines opening 3 above: the correct inductive
    invariant is almost certainly this specific self-similar mark-cascade
    pattern, not a flat characterization of "which compositions tie."
  - Splitting the last piece is a genuine tie/wash in every case checked
    (`n=2..5`), supporting cheap-kill (opening 2) as a real, provable-looking
    lemma, not just noise.
  - No tested composition (any `n≤4`, any mark allocation, any split ratio)
    ever went *below* `c(n)` — strong (though non-exhaustive, discrete-restart)
    numeric support for the lower bound as a whole.
