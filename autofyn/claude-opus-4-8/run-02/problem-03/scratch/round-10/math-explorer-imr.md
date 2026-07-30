## imo-2026-03 — GAP-IMR lens (integer-minimizer / mass-transfer for the lower bound)

- **Distinct openings** (mass-transfer / rounding mechanisms for GAP-IMR — "some global
  minimizer of D̃ over the continuum Φ_n is integer"):
  1. **Independent per-group largest-remainder rounding — TESTED, REFUTED (see below).**
     Round each dyadic group π_j's real parts to nearby integers preserving the group's
     integer total (classical folklore "round preserving sum" lemma), independently per
     group. Numerically this does NOT bound the change in D̃: rounding can silently
     re-permute the merged order (a value that was just above another can drop just
     below it after independent rounding in a different group), and D̃ is exquisitely
     order-sensitive. **Refuted this round**: 7847/18900 random trials increased D̃, worst
     gap +2.79 (n=4). Any per-group-independent rounding is dead; a correct rounding
     scheme MUST be **order-aware / jointly correlated across groups**, not applied group
     by group.
  2. **Correlated / order-respecting rounding (dependent rounding, discrepancy-style).**
     Instead of rounding per group, round the WHOLE merged vector at once with a scheme
     that (a) preserves each group's integer sum exactly (needed for feasibility) and
     (b) is constrained to *never* let two values cross past each other if that would
     flip a sign contribution unfavorably — i.e. round jointly so the *relative order* of
     the merged list is preserved wherever the current order already respects group
     boundaries, and control only the ties. This is close in spirit to Beck–Fiala /
     dependent-rounding-with-marginals techniques but needs a bespoke potential (D̃ itself,
     not a generic discrepancy bound) as the thing NOT to increase — not yet formulated as
     a clean LP/flow; UNTESTED this round, flagged as the natural repair of mechanism 1.
  3. **LP-duality / complementary-slackness at the true (global, not per-cell) optimum.**
     Rather than asking "is the vertex integral" (refuted, TU is false), ask what the
     *dual* certificate of global optimality looks like across the union of cells, and
     whether *strong LP duality plus integrality of the RHS* (all group sums 2^{n−j} are
     integers) forces an integral optimal *value* achieved at an integral point via a
     total-dual-integrality (TDI) argument restricted to the active/optimal face only.
     Heavier machinery than typical olympiad tools; flagged in the approach file as
     "Integral polytope for the optimal cells only — not attempted." No KB or crux-corpus
     support found for this (see below) — likely too far from olympiad technique to be the
     intended route.
  4. **Bypass GAP-IMR entirely: merge it with GAP-P1 (peel induction).** The peel identity
     `D̃(F) = λ(O_{π_0} △ O_{F'})` (certified, `peel-difference-bound.md`) already gives a
     strong-induction machine that proves `D̃≥1` directly on the REAL feasible set (no
     detour through "is the minimizer integer" at all) — Case A is closed this way with NO
     value-IH, purely from `D̃≤Σ`. The natural completion of Case B's residual
     `{|D̃(π_0)−D̃(F')|<1}` (GAP-P1's open gap) would, if found, prove the real-valued bound
     directly and make GAP-IMR moot (the Parity Lemma would then only be needed as
     flavor/insight, not as the actual finishing step — or could be folded IN as the base
     case of the induction, since integer configs are trivially closed by Part 1–2 of
     `vertex-integrality-parity.md`). This is not a new lemma, it's a *strategic*
     redirection: the induction route sidesteps the "prove integrality of the minimizer"
     problem altogether, which may be why it is closer to a real olympiad solution shape
     (IMO combinatorics problems essentially never invoke polytope-vertex integrality
     arguments; they use induction/exchange). Recommend treating GAP-IMR and GAP-P1 as
     candidates for a **merge**, not two independent walls — cf. run_state's own "WATCH"
     note.

- **Candidate technique(s):** classical "round a real vector to integers preserving a fixed
  integer sum with bounded change" (folklore, aka controlled/cascade rounding — related to
  Beck–Fiala discrepancy theory) — but must be made **order-aware**, since mechanism 1 shows
  the naive independent version fails badly. LP duality / complementary slackness (heavier,
  no clear precedent in the corpus). Strong induction on the peel decomposition (already
  certified machinery, opening 4) is the technique most consistent with olympiad style.

- **Cheap-kill candidates:**
  - Before building any global rounding scheme, cheap-test it exactly as I did here:
    generate many random fractional configs across cut vectors, apply the proposed
    rounding, and check `D̃(rounded) ≤ D̃(fractional)` numerically with exact `Fraction`
    arithmetic — a single violation kills the mechanism immediately (this is how
    mechanism 1 died in minutes). Do this FIRST for any new rounding proposal before
    writing algebra.
  - Parity/size check: any candidate rounding scheme must preserve **feasibility** (every
    group total stays exactly `2^{n−j}`, an integer) — this is automatic for "round
    preserving sum" schemes, so the real test is only the D̃-monotonicity, not feasibility.
  - Check whether the scheme needs to know the GLOBAL merged order across groups (not just
    within-group) — mechanism 1's failure mode was specifically a cross-group order flip,
    so any repair (mechanism 2) needs cross-group information, confirming the "global, not
    cell-local" diagnosis already in the approach file.

- **Knowledge-base entries to use:** "Piecewise-concavity smoothing" (Algebra &
  Polynomials) — the general shape (minimize over a domain, argue the min sits at a
  boundary/breakpoint where some coordinate hits an extreme value) is the right *language*
  for "vertex of the polytope is the minimizer," already used and exhausted by the approach
  file. "Extreme value theorem / Lagrange multipliers on a compact manifold" (Linear
  Algebra) is the closest KB entry to an LP-duality argument but is aimed at smooth
  manifolds, not polytopes with integrality goals — weak fit. No KB entry directly covers
  integer-vs-fractional-optimum-coincidence or TDI-style arguments.

- **Analogous past problems (cruxes):** Searched `combinatorics`/`algebra` domains,
  subtopics `linear-algebra-method`, `probabilistic-method`, `extremal-principle`,
  `invariants-and-monovariants` for rounding/integrality/mass-transfer/TU/vertex/lattice
  keywords. **None found that are genuinely analogous.** The closest superficial hits:
  - `aimo-0281` (`linear-algebra-method`): "confirm a reduced linear system has an integer
    (not merely rational) solution by exhibiting a key combination whose divisibility is
    guaranteed by an invariant's congruence condition" — this is about existence of AN
    integer solution to a linear reachability system (moves as net variables), not about a
    continuum OPTIMUM coinciding with an integer point. Different structure (feasibility,
    not optimality); not a real transplant.
  - No crux in the corpus addresses "global LP/polytope minimum attained at a lattice
    point" or "randomized/dependent rounding preserves an order-sensitive linear
    functional." This is consistent with GAP-IMR being an unusually LP-flavored
    (non-classical-olympiad) framing of the lower bound — reinforces opening 4 (prefer the
    induction/peel route, which DOES have olympiad-standard shape, over continuing to push
    the polytope-integrality machinery).
  - If forced to pick one crux to *partially* borrow, `aimo-0281`'s divisibility-invariant
    idea (find a "key combination" whose integrality/divisibility is forced by a structural
    invariant) is the right *flavor* for showing SOME specific coordinate combination in the
    optimal cell must be integral — but I could not map it onto D̃'s block structure in the
    time available; flag as a loose lead only, not a validated transplant.

- **Prior progress:** As recorded in `vertex-integrality-parity.md`: Parity Lemma (certified,
  `lemmas/parity-odd-total.md`) fully proves integer-config case; integer minimum = 1 with
  explicit attaining family for all n; minimizer is rational at a cell vertex (LP standard
  fact); global continuum optimum verified integer-attained for `n≤3` exactly. GAP-IMR itself
  (rounding claim) is open; the exact obstruction (odd fractional tie-blocks with
  `n_g·v ∉ ℤ` blocking single-block integralization) is correctly diagnosed as requiring a
  cross-block/global argument.

- **Dead ends (do not retry):**
  - TU / total unimodularity of the per-cell vertex polytope: REFUTED R9 (fractional
    minimizing vertices exist, e.g. `(4,2,½,½)`; per-cell LP min `1.667`; rounding to that
    cell's integer point overshoots `2→3`).
  - Single-block / per-block rounding (round one fractional tie-block to integers holding
    everything else fixed): PROVABLY IMPOSSIBLE when the group-block-sum `n_g·v ∉ ℤ`
    (approach file §3.2) — the values needed to reconstruct an integer split of that block
    do not exist.
  - **NEW this round: independent per-group ("largest remainder") rounding applied
    group-by-group across the whole config.** REFUTED numerically (7847/18900 violations,
    n=4, worst `ΔD̃ = +2.79`). The failure mechanism is cross-group order inversion: rounding
    one group's parts up/down can push a value past a value in an unrelated group, flipping
    which is odd/even rank and hence its sign in `D̃` — an effect no single-group rounding
    rule can control. Any viable rounding mechanism must jointly correlate decisions across
    ALL groups sharing comparable magnitudes (opening 2), not treat groups independently.

- **Small-case / intuition notes (all conjectural):**
  - Re-ran an independent random-search probe at **n=4** (not previously reported at this
    depth): best `D̃` found by pure random sampling over all 126 cut-vectors × 300 random
    real splits each was `≈ 1.0000053` (cut vector `(3,0,0,0,0)`, i.e. top piece cut into 4
    real parts, all other scales uncut) — consistent with (not proof of) the conjecture that
    the true continuum minimum is exactly `1` at `n=4` too, matching the certified `n≤3`
    result and the explicit integer-attaining family. This extends the numeric evidence for
    GAP-IMR one level further (still only a conjecture/consistency check, not a proof).
  - The refuted per-group rounding experiment's worst witness (`a=(2,1,1,0,0)`, fractional
    `D̃≈6.21` → rounded `D̃=9`) shows the failure is not a minor numeric artifact: rounding
    can more than triple the "gap above 1," underscoring that this mechanism is not a small
    fix away from working — it needs a structurally different (order-correlated) rounding
    rule, or abandonment in favor of the induction/peel merge (opening 4).
