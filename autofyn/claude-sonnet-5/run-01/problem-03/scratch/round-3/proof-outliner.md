## imo-2026-03

geometric-dominance-construction: advance
Target: The full lower bound half of `c(n) = 2^n/(2^{n+1}-1)`: for the geometric
witness `A_n = (2^n,...,2,1)/(2^{n+1}-1)`, show `min_B oddrank(B) ≥ c(n)` over
EVERY Xiang-Yu response `B` (every composition of ≤n marks across pieces of
`A_n`, every continuous split ratio) — completing what `k=0` (Prop A) and
`k=1` tail-untouched (Lemma F1) already close.
Technique: LP vertex-extremality (reduce a continuum of split ratios to
finitely many degenerate/tied configurations) + a dominated-move size
reduction, then strong induction using the certified self-similarity (Lemma
3/S) with an ENRICHED invariant (value AND rank-position of an injected
extra piece), per math-explorer-lowerbound's openings 1–3.
Skeleton:
  1. Import Lemma 1 (claiming-phase value), Prop A (k=0), Lemma F1 (k=1
     tail-untouched), Lemma S (self-similarity) — all certified.
  2. New Lemma V (vertex reduction): for a FIXED composition (mark count per
     piece of `A_n`), `oddrank(B)` as a function of the continuous split
     ratios is piecewise-linear on the compact convex polytope of valid
     splits for that composition — by <standard LP fact: sorting + summing a
     coordinate subset is piecewise-linear>; hence its minimum over that
     polytope is attained at an extreme point (a sub-piece degenerating to 0,
     or a rank-order tie). This turns "check a continuum of split ratios"
     into "check finitely many degenerate configurations per composition."
  3. New Lemma W (wasted-mark / dominated-move): spending a mark to split the
     CURRENT smallest piece of `B` is never strictly better for Xiang Yu than
     reallocating that mark to the top piece instead — by a direct
     rank-shift comparison of the two resulting merged multisets (generalize
     the Lemma F1 rank-shift argument from "one mark on top" to "one mark
     anywhere," comparing the two placements' contributions to `oddrank`
     term-by-term). This lets the proof ignore compositions that touch the
     current minimum, shrinking the case space Lemma V must range over.
  4. Combine Lemma V + Lemma W: the only compositions that can be extremal
     are the numerically-observed "doubling family" `C_k = {p_2,...,
     p_{k+1}, p_1-Σp_i}` and its self-similar tail-recursive analogues (the
     15-of-55 tie set found at `n=4` — matches "spend one mark on top, then
     recurse down the self-similar chain").
  5. Prove the doubling family achieves exactly `c(n)` AND dominates every
     other vertex composition, by strong induction on `n` peeling ONE mark
     at a time off `p_1` (math-explorer-lowerbound opening 3): first mark
     splits `p_1 = x+r`; by Lemma S, the untouched original tail rescales to
     `λ_n·A_{n-1}`, so the residual game is "the certified `(n-1)`-level
     self-similar game PLUS one extra injected piece `r`, with `n-1` marks
     left." Strengthen the induction hypothesis to carry `(value, sorted
     rank-position of r)` — NOT just totals (this respects the certified
     negative result that pure-scalar induction is false).
  6. Conclude `min_B oddrank(B) ≥ c(n)` for every composition ⇒ full lower
     bound for `A_n`, all `n`, all `k`.
Key lemmas:
  - Lemma V (vertex/extreme-point reduction) — because a linear function on
    a compact convex polytope attains its optimum at an extreme point;
    reduces a continuum to finitely many degenerate cases.
  - Lemma W (wasted-mark domination) — because moving a mark from the
    current minimum piece to the top piece can be tracked as an explicit
    rank-shift on the merged sorted list, and the shift is never unfavorable
    to Xiang Yu (needs the same rank-shift bookkeeping already used in
    Lemma F1/DOM/HALVE, applied to a different pair of positions).
  - Peel-induction invariant (value + position of injected piece `r`) —
    because Lemma S's self-similarity turns "one extra mark on `p_1`" into a
    smaller instance of the SAME problem with one foreign element inserted,
    and the foreign element's rank (not just its size) determines how it
    shifts parity for everything below it.
Open gaps: Lemma V and Lemma W are stated but not proved (both look like
short, self-contained arguments — LP fact + direct rank-shift computation).
The peel-induction's case split by rank-of-`r` (top/mid/bottom of
`A_{n-1}`'s structure) is not yet worked out. The "doubling family
dominates" claim is numerically confirmed (n≤5) but not proved to be the
true minimizer over ALL vertex compositions.
Cases to cover: rank position of the injected piece `r` relative to
`A_{n-1}` (top / interior / bottom); composition sizes `k=0,1,...,n`.
Watch out for: Lemma W must be proved for a mark on ANY piece, not just
adjacent-to-top — don't silently assume the smallest piece is unique or that
"smallest" stays fixed across the induction as pieces are split.

recursive-embedding-induction: advance
Target: Same lower bound as above (`min_B oddrank(B) ≥ c(n)` for `A_n`,
every `k`), via the self-similar recursion `c(n)=2λ_n c(n-1)` (Lemma G1,
certified) rather than vertex/LP reduction — a genuinely different
mechanism (direct recursive induction, no LP extremality step) so this stays
a distinct rival route from geometric-dominance-construction even though
both now use "peel one mark, carry position."
Technique: strong induction on `n` with an ENRICHED hypothesis that tracks
the value AND ordered rank-position of one (or more) foreign injected
pieces through the self-similar recursion — directly targeting the gap the
certified merge-by-sums counterexample identified (scalar-only induction is
false; must carry order-type).
Skeleton:
  1. Import Lemma 1, Lemma G0 (n=1, full), Lemma G1 (recursion, certified),
     Lemma 3 (self-similarity).
  2. Formalize the "injected extra piece" sub-problem precisely: after
     Xiang Yu's first mark splits `p_1 = x+r` (`x` the larger resulting
     part), the residual game is the `(n-1)`-level self-similar sub-game on
     `T_0 = λ_n·A_{n-1}` (by Lemma 3) with one extra element `r` present and
     `n-1` marks remaining, which Xiang Yu may spend anywhere in `T_0∪{r}`.
     Define `V_{n-1}(r) := min` over such responses of `oddrank(T_0∪{r}∪
     refinement)`.
  3. New Lemma R (injected-piece bound): case-split on where `r` falls
     relative to `A_{n-1}`'s pieces (rescaled by `λ_n`):
     (a) `r` large enough to itself dominate `T_0` (becomes new effective
     top) — reduces to a Lemma-DOM-style rank shift;
     (b) `r` comparable to an interior piece of `T_0` — a rank-shift
     argument like Lemma F1/W but with the FOREIGN element inserted at a
     specific interior rank;
     (c) `r` negligible / below all of `T_0` — shown to reduce to the pure
     `(n-1)`-level value with no correction term.
     Prove `V_{n-1}(r) ≥` the appropriate case-specific expression in each
     regime, via explicit rank-shift bookkeeping (same style as the
     certified DOM/HALVE proofs — insert one new element into a sorted
     merge and track how its rank shifts parity of everything past it).
  4. Combine Lemma R with the certified recursion `c(n) = 2λ_n c(n-1)` to
     close the induction: base case `n=1` (Lemma G0, already fully closed).
Key lemmas:
  - Lemma R (injected-piece three-case bound) — because inserting one
    element into a sorted list shifts every element after it by exactly one
    position, and whether that shift preserves or flips odd/even parity for
    everything below depends only on the injected element's RANK, not its
    exact value — the same mechanism already certified in Lemma DOM/HALVE,
    specialized to "one extra foreign element" instead of "a whole
    refinement."
Open gaps: Lemma R's three cases are stated but the case-by-case rank-shift
computations are not done. Handling MULTIPLE injected pieces (if later
marks also touch places other than straight down the self-similar chain)
is not yet reduced to the single-injection case — may need a second
induction layer (induct on number of "foreign" pieces present).
Cases to cover: the three regimes for `r`'s rank in Lemma R; whether more
than one mark can be spent off the self-similar chain simultaneously (if
so, Lemma R needs a k-fold generalization, not assumed here).
Watch out for: don't let this collapse back into the already-refuted
sums-only induction — every step of Lemma R must explicitly use `r`'s
RANK/position, not just its value, per the certified counterexample.

universal-adversary-strategy: advance
Target: The full upper bound `max_A min_B oddrank(B) ≤ c(n)` for EVERY Liu
Bang configuration `A` (arbitrary, non-geometric), all `n` — completing the
upper-bound half of the minimax (n=1 for arbitrary A already closed via
Lemma DOM + Lemma HALVE this file).
Technique: strong induction on the combined state `(piece count m, remaining
budget r)`, using three certified/near-certified recursive moves as the only
strategy primitives — Lemma DOM, Lemma HALVE, and the new Lemma PEEL — per
math-explorer-upperbound's finding (zero violations found, n=2,3,4, both
random and adversarial-optimizer search).
Skeleton:
  1. Import Lemma DOM, Lemma HALVE (both certified, any tail shape).
  2. New Lemma PEEL (prove in full — flagged by the explorer as likely
     EASIER than DOM/HALVE): if `A=(p_1≥p_2≥p_3≥...)` (tail past `p_2`
     automatically satisfies `p_2 ≥ max(rest)` by sortedness — no extra
     hypothesis needed beyond `A` being sorted), then for ANY refinement
     `T'` of `(p_3,p_4,...)` using any number of marks not touching `p_1,
     p_2`: `oddrank({p_1,p_2}∪T') = p_1 + oddrank(T')`, using ZERO marks.
     Proof: `p_1,p_2` occupy global ranks 1,2 unconditionally (both dominate
     every element of any refinement of the tail); rank 1 (odd) contributes
     `p_1`, rank 2 (even) is excluded, and the tail's own ranks all shift by
     exactly 2 (even shift ⇒ parity preserved), giving `oddrank(T')`
     unchanged for the rest. This is the same rank-shift mechanism as
     Lemma DOM/HALVE, one level simpler (no marks spent at all).
  3. Define the recursive strategy via case split on ANY sorted `A=(p_1≥
     p_2≥...≥p_m)` with budget `r`:
     - Case `p_1 ≥ S` (S = sum of tail): apply Lemma DOM (uses `m-1` marks,
       done — `oddrank = p_1 ≤ c(n)` since `p_1≥S` forces `p_1` in the
       tight regime, already proved).
     - Case `p_1 < S` and `p_1 ≥ 2p_2`: apply Lemma HALVE (1 mark), then
       recurse on the tail `T` (size `m-1`, mass `S`, budget `r-1`) via the
       SAME inductive strategy (not a fixed sub-rule).
     - Case `p_1 < 2p_2` (so `p_1,p_2` close together): apply Lemma PEEL
       (0 marks; automatically valid since tail past `p_2` is smaller than
       `p_2` by sortedness), then recurse on `T=(p_3,...)` (size `m-2`,
       mass `S-p_2`, budget `r` UNCHANGED) via the same inductive strategy.
  4. Prove these three cases are EXHAUSTIVE (every sorted `A` falls in
     exactly one, using the two comparisons `p_1≷S` and `p_1≷2p_2` — note
     `p_1<S` and `p_1≥2p_2` can coexist, and `p_1<2p_2` is the complementary
     regime) and that the recursion TERMINATES: DOM ends immediately;
     HALVE strictly decreases `r` (well-founded, `r≥0` bounded); PEEL
     strictly decreases `m` by 2 without touching `r` (well-founded, `m≥1`
     bounded) — so the pair `(r, m)` under the lexicographic-ish combined
     measure strictly decreases at every step, giving a valid strong
     induction on `(m,r)` (not `n` alone), per the explorer's diagnosis.
  5. Set up the PROPER scaled inductive hypothesis: for any config of ≤m'
     pieces summing to mass `μ` (not just `μ=1`) with budget `r'`, Xiang Yu
     achieves `oddrank ≤ C(r')·μ` where `C(r')` is defined by the SAME
     recursion as `c(n)` but indexed by remaining budget `r'` (i.e. verify
     `C(r') = c(r')` under the existing closed form, by homogeneity of
     `oddrank` in the mass and of the DOM/HALVE/PEEL identities, which are
     all linear in the piece values). Prove `C(r') ≤ c(n)`-consistent bound
     by induction using step 3's case split, closing the induction with
     base case `m'=1` trivial (`oddrank=μ`, `C(0)=1` consistent) and using
     `n=1` (already closed in this file) as a sanity check of the base
     step for `r'=1`.
Key lemmas:
  - Lemma PEEL — because `p_1,p_2` dominate any refinement of the tail
    unconditionally (sortedness alone), so their global ranks 1,2 are fixed
    and the tail's ranks shift by an even amount (2), preserving which of
    its elements are globally odd-ranked.
  - Case exhaustiveness + termination on `(m,r)` — because `p_1<S` and
    `p_1≥2p_2` can coexist (HALVE regime) while `p_1<2p_2` is the
    complementary case handled by PEEL, and each of the two non-terminal
    moves (HALVE, PEEL) strictly decreases one of `r` or `m` while never
    increasing the other, so `(m,r)` is a valid well-founded measure.
Open gaps: Lemma PEEL itself (short, should close quickly). The formal
scaled inductive hypothesis `C(r')` and its identification with `c(r')`
(step 5) — needs the homogeneity argument spelled out and the case-3
recursive bound (`C(r) ≤` value expression involving `C(r)` applied to a
STRICTLY SMALLER `m` at the SAME `r` — must confirm this terminates, since
`r` doesn't decrease in the PEEL branch, only `m` does, so the induction
must be on `m` first, `n`/`r` second, or a genuine combined well-order).
Cases to cover: the three regimes in step 3; the tie boundaries `p_1=S` and
`p_1=2p_2` (must land in a well-defined branch, not both/neither).
Watch out for: don't let the induction silently assume `r` decreases in the
PEEL branch — it doesn't; the induction must be properly on `m` (with `r`
fixed) nested inside induction on `r`, not naively on `n`.

majorization-smoothing: revise (corrected concavity — NOT the same
falsified Lemma C; a genuinely different proof mechanism)
Target: The FULL minimax `c(n) = max_A min_B oddrank(B)` at once (both
bounds simultaneously), via global concavity of the value function, as an
alternative unifying framing distinct from the case-recursion routes above.
Technique: prove `V(p) := min_B oddrank(B)`, as a function of the SORTED
descending Liu-Bang vector `p` on the sorted-simplex, is a min of AFFINE
(not merely concave) functionals of `p` — one per discrete "split
combinatorial type" — hence concave; then apply the KB's
**piecewise-concavity smoothing** technique (crux `aimo-0861`'s
shift-to-kink-points pattern: a piecewise-concave function's extremum over
its domain occurs at a breakpoint) to reduce "check the whole simplex" to
"solve finitely many tie/breakpoint equations," and verify the geometric
`p*=A_n` is the unique breakpoint solving them with value `c(n)`.
Skeleton:
  0. **MANDATORY GATE, do first, before any other work**: round-1's
     outline-reviewer numerically falsified an earlier "Lemma C" concavity
     claim (`V(mid)=0.52 < avg(endpoints)=0.525`). math-explorer-newframing2
     this round independently computed, with EXACT `Fraction` arithmetic on
     the properly sorted-descending simplex domain, that `V` is concave at
     `n=1` (closed form: slope 1 on `[1/2,2/3]`, slope −1/2 on `[2/3,1]`,
     single downward kink) and found no violation at `n=2` (coarse grid,
     both interior and boundary test pairs). Before writing ANY further
     step, the builder must reproduce round-1's exact falsifying instance
     with exact-fraction arithmetic on the CORRECT domain (sorted, both
     endpoints and midpoint genuinely on the sorted-descending simplex,
     `V` computed as the true `min_B oddrank(B)` not an approximation) and
     determine whether the violation reproduces. If it reproduces, STOP —
     this is still a dead end, report RETHINK with the reconciled numbers.
     If it does NOT reproduce (e.g. round 1 used an un-sorted pair, or an
     approximate/heuristic `V`, or a different quantity entirely), record
     precisely what was different, and only then proceed.
  1. Import Lemma 1 (shared reduction).
  2. Lemma C' (corrected): for each fixed discrete "split type" `T`
     (a combinatorial choice of which pieces get how many of Xiang Yu's `n`
     marks), first solve the INNER minimization over continuous split
     ratios (for fixed `p`) — this is the delicate step the old skeleton
     flagged and did not resolve: show the resulting value, as a function
     of `p` alone (with the inner ratios optimized out), is genuinely
     AFFINE in `p` — not just piecewise-linear with its own internal kinks
     — for each fixed type `T`. (If this fails — the inner optimum's
     argmin itself changes combinatorial branch as `p` varies within type
     `T` — then `f_T` is only piecewise-affine, and the type index `T` must
     be refined further, splitting `T` into sub-types until each piece IS
     affine; do this refinement explicitly rather than assuming it away.)
  3. `V(p) = min_T f_T(p)`, a min of (refined, now genuinely) affine
     functionals of `p` ⇒ concave, by the standard convex-analysis fact
     (min of affine functions is concave).
  4. Apply the KB's piecewise-concavity smoothing (crux `aimo-0861`
     pattern): the global maximizer `p*` of the concave `V` over the
     compact simplex occurs at a breakpoint where two of the affine pieces
     `f_T` tie (a kink) — reduce to solving these finitely many tie
     equations explicitly, and verify `p* = A_n` (the certified geometric
     config) is a solution with `V(p*) = c(n)`.
  5. Concavity ⇒ `V(p) ≤ V(p*) = c(n)` for all `p` (upper bound, one
     subgradient inequality at `p*` instead of case-by-case DOM/HALVE/PEEL
     recursion) AND `V(p*) = c(n)` is exactly the lower bound already
     targeted by geometric-dominance-construction / recursive-embedding-
     induction — so if this framing closes, it proves BOTH halves at once
     from one concavity fact.
Key lemmas:
  - Lemma C' (each split-type value `f_T(p)` is affine, after any needed
    type-refinement) — because the odd-rank-sum of a merged sorted
    multiset, restricted to one fixed combinatorial assignment of ranks to
    original vs. inserted elements, is literally a fixed linear combination
    of the `p_i` (no further optimization once the combinatorial type,
    including internal order, is fixed) — the risk is only whether "type"
    needs to include the internal split ratios' own optimum branch, which
    must be checked, not assumed.
  - Breakpoint/kink characterization at `p*=A_n` — because concave
    piecewise-affine functions attain their max exactly where two active
    affine pieces cross (standard LP/convex-analysis fact, the `aimo-0861`
    pattern).
Open gaps: Step 0's reconciliation gate (must be done first — this is the
single biggest risk given the round-1 falsification). Step 2's refinement
procedure (showing type-splitting terminates in finitely many genuinely
affine pieces) is not carried out for general `n`. Step 4's explicit kink
system for general `n` is not solved (only `n=1` closed-form is in hand).
Cases to cover: whichever finitely many split-types the refinement in step
2 produces (grows with `n`, not bounded here).
Watch out for: this is a previously-killed idea; the reviewer must confirm
the gate in Step 0 was genuinely passed (with the exact reproduction
attempt shown) before treating any later step as progress — do NOT let the
builder skip Step 0 and jump to asserting concavity from the new
explorer's evidence alone, since that evidence used a coarse grid at n=2
and only exact closed form at n=1.
