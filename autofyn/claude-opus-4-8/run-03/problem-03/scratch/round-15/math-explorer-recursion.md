## imo-2026-03 (lens: direct strategy-construction / self-similar recursion, never touching reachable-set/word/vertex-polytope/subset-sum/covering)

- **Distinct openings:**
  1. **The self-similar recursion is already the `induction-peel` engine, and it is alive (not
     in the dead-family list).** Lemmas R/M/P/PEEL/SPLIT/ONE reduce the whole game to a scalar
     "parity measure" D, and Lemma PEEL (`D(S)=f₁−D(S∖{f₁})` for a unique max) IS the honest
     self-similar reduction step — it recurses the n-instance to an (n−1)-shaped residual exactly
     when the top fragment is a strict global max. This is a genuinely different object from the
     reachable-set/word/vertex-polytope/covering families (those are used only inside
     `merge-interleave-pattern`/`breakpoint-vertex`); D-measure/PEEL/SPLIT never touch them. So
     this route is legitimately "outside" the six/seven dead families and should NOT be discarded
     — it should be reinforced with a NEW reduction step (aimo-0298's averaging step is dead,
     but PEEL/SPLIT/ONE/HALF are all still standing and certified).
  2. **NEW lead — budget-domination for Case II (numerically supported, not yet proved):**
     in Case II (top not cut past 2^{n-1}, |F|≥2 top fragments, budget split
     (|F|−1)+c_T ≤ n), the sub-case |F|=2 (single top bisection F={2^{n-1},2^{n-1}}, all
     remaining n−1 cuts spent on the tail) is ALREADY proved via IH to give D(S)=D(T)≥1, tight.
     My numeric search (n=3,4; hundreds of thousands of random budget-respecting refinements)
     finds NO |F|≥3 configuration beating D=1: strictly-interior |F|=3 configs (top fragments
     bounded away from the boundary 2^{n-1}) bottom out at D≈1.05–1.09, only approaching D=1 in
     the limit where one top fragment → 2^{n-1} exactly (i.e. degenerating back to the |F|=2
     case). This suggests the true closing lever for Case II is a **budget-domination / merge
     argument**: show that merging any two top fragments into one (freeing a cut, reallocating it
     to the tail) never increases D, so induction on |F| downward to the already-solved |F|=2
     floor closes ALL of Case II at once — a genuinely new reduction step, NOT aimo-0298
     averaging, and structurally different (a monotone merge on the TOP block only, not a
     split-and-average on the whole bounded sub-multiset).
  3. **The critical-band (L⋆) sub-case is a different animal — do not expect the same merge
     trick.** There the extremal (below-insertion) layout genuinely needs |A|=n−1 interleaved
     fragments (one per dyadic gap), so a "collapse to 2 fragments" merge argument cannot apply
     symmetrically; L⋆ is really Xiang MAXIMIZING D(S') subject to a *upper*-type constraint —
     it is the lower-bound proof's own miniature upper-bound sub-problem (interleaving into a
     fixed ladder). This hints the critical band and breakpoint-vertex's UPPER wall genuinely
     share DNA (both are "insert free mass into gaps of a fixed dyadic ladder, bound the
     alternating sum") — worth flagging to the outliner as a possible SHARED lever between the
     lower L⋆ residual and the upper GAP U residual, attacked via the SAME gap-interleaving
     exchange lemma (stated but unproved in `induction-peel` §3.3) rather than two separate
     mechanisms.
  4. **Single-recursion-closes-both-walls idea (run_state's own suggestion, §Next):** since
     u_n=u_{n-1}/(2+u_{n-1}) is exact, a strengthened induction hypothesis carrying BOTH "Liu
     guarantees ≥u_{n-1}L on any (n−1)-residual" AND "Xiang forces ≤u_{n-1}L on any (n−1)-residual"
     simultaneously (i.e. inducting on the FULL minimax equality, not the two one-sided bounds
     separately) is exactly what PEEL delivers for Case I: D(S)=f₁−D(S′), so IF f₁ is pinned to
     the dyadic value exactly (=2^{n-1}+u_{n-1}/(1+u_{n-1})·something) the SAME PEEL identity
     gives both directions from one inequality on D(S′). This is worth exploring as the
     "single-lever" unification but has NOT been attempted computationally this round — flagged
     as an opening, not verified.
  5. **A genuinely fresh recursion candidate not yet tried by any approach:** define the game
     recursively on the TOP TWO dyadic scales at once (2-step self-similar recursion,
     D(n)=φ(D(n−2)) directly) rather than peeling one scale at a time — this could sidestep the
     awkward |F|≥3 "partial top" cases entirely by working in blocks of two scales where the
     top-quarter/second-quarter dynamics might have a cleaner closed form. Purely a suggestion;
     not probed numerically due to time budget.

- **Candidate technique(s):** exchange/rearrangement argument on Lemma SPLIT's cross term
  (an "adjacent-pair slide" monovariant, per `induction-peel`'s stated but unproved
  Gap-Interleaving Lemma) — this is a classic olympiad "smoothing towards canonical form"
  technique (majorization/rearrangement), NOT the refuted aimo-0298 split-and-average. Also: a
  **merge/budget-reallocation dominance argument** (new, see opening #2) — closer in spirit to
  "spending a resource more efficiently strictly helps," a standard extremal-principle move.

- **Cheap-kill candidates:** the budget-domination conjecture (opening #2) is itself a cheap
  numeric gate the outliner/builder should run FIRST before investing in a full merge-argument
  proof: verify (n=3,4,5, large random samples, strictly interior |F|≥3 vs. best |F|=2) that
  |F|=2 always weakly dominates Case II. I ran this for n=3,4 with no violations found (see
  Small-case notes below) — the builder should extend to n=5 and to ADVERSARIAL (not just
  random) search before trusting it as a lever.

- **Knowledge-base entries to use:** none of `knowledge_base.md`'s general theorems were checked
  this pass (time budget spent on numerics + corpus); the relevant machinery is entirely the
  problem's own certified lemma set (`lemmas/strict-max-peel`, `split-cross-term`,
  `elementary-reductions`, `even-multiplicity-corrector`).

- **Analogous past problems (cruxes):** `aimo-0117` (combinatorics, `games-and-strategy`) — Jesse
  vs. Tjeerd stone-claiming game with box capacities. Its crux move "assign played values as a
  two-sided geometric (dyadic) sequence so the single largest value strictly exceeds the sum of
  all the others" is EXACTLY the superincreasing dyadic construction Liu already uses (Lemma ONE /
  the C_n={2^n,...,1} profile) — confirms the dyadic-superincreasing idea is a recognized crux
  move in this genre, but it is already fully exploited in this run (not a new lever). A second
  crux from the same problem, "defer committing the extreme value until the opponent's move
  vacates its target cell," is an ADAPTIVE-Liu idea that does NOT apply here (Liu commits all
  marks upfront, no adaptivity) — noted as a false lead, do not import. No other corpus entry in
  `games-and-strategy` (39 total, scanned all titles) resembles the alternating-claim /
  parity-measure structure closely enough to be load-bearing; the rest are pairing/blocking/
  parity-invariant games on discrete boards, a different shape.

- **Prior progress:** as recorded in `results/imo-2026-03/current.md` / `approaches/induction-peel.md`:
  full scalar reduction (Lemmas R, M, P certified), recursion u_n=u_{n-1}/(2+u_{n-1}) proved and
  numerically re-confirmed exact through n=7 this round, base cases n=0,1 both directions, entire
  upper dominant case a₁≥L/2 closed (§4A), lower Case (a) and trivial regime of L⋆ closed, |F|=2
  sub-case of Case II closed via IH. Two residuals remain: **GAP L2** (critical band of L⋆ +
  Case II |F|≥3, both need the still-unproved Gap-Interleaving exchange lemma) and **GAP U**
  (balanced upper case a₁<L/2, needs a non-multiplicative early-stopping potential).

- **Dead ends (do not retry):** the aimo-0298 split-and-average monovariant is REFUTED for D
  (28% failure rate on budget-enforced refinements, §3.4 of induction-peel.md) — confirmed by
  reading the file, not re-tested. Do not resurrect it or any termwise/per-element additive
  potential for the same reason parity-measure's scalar-reserve family died (R9/R10): D is a
  measure of an odd-parity SET, not a sum of independent per-element weights, so per-element
  additive arguments structurally cannot see the global reshuffle a deletion causes.

- **Small-case / intuition notes (CONJECTURE, numeric only):**
  - n=3, Case II |F|=3 (top {8}→3 fragments, tail budget 1 on C₂={4,2,1}): 200k random
    budget-respecting refinements gave min D→1.0000 only in the limit of one fragment→4
    (boundary with |F|=2); restricting strictly interior (max fragment ≤3.9) pushed min D up to
    ≈1.09, i.e. a genuine positive gap away from 1 in the interior.
  - n=4, Case II: |F|=2 (forced {8,8}, tail budget 3 on C₃={8,4,2,1}) attains D=1.0000 exactly
    (matches theory); |F|=3 with tail budget only 2 found min D≈1.047 over 300k trials — no
    violation of the conjectured |F|=2 dominance.
  - Recursion u_n=u_{n-1}/(2+u_{n-1}) verified exactly (exact `Fraction` arithmetic) against
    1/(2^{n+1}−1) for n=0..7 — 100% match, no discrepancy found.
  - These are CONJECTURES from random sampling only, not adversarial/exhaustive search — per the
    run's own repeated Rule ("random search misled R11's COUNT claim"), the next builder MUST run
    an adversarial/targeted search (e.g. gradient descent toward min D, or exact vertex
    enumeration for small n) before trusting the |F|=2-dominates conjecture as a proof target.
