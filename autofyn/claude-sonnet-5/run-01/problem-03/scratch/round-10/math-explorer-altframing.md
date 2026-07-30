## imo-2026-03

### Assessment question: is the field of 3 approaches collapsed too close together (shared-gap plateau) or genuinely narrowed to 2 finishing tasks?

**Verdict: NOT a shared-gap plateau requiring a new 4th framing. The two live lower-bound
approaches are on the SAME target statement but via two structurally different mechanisms
(nested-forest/tree recursion vs. direct two-block threshold estimate) — this is convergent
cross-verification, exactly the healthy case CLAUDE.md distinguishes from a collapsed field.
The upper-bound approach (`universal-adversary-strategy`) is on a wholly separate target
(Case C existence for general m via Hall's theorem) with its own distinct toolkit (BLOCK-RECURSE,
THRESHOLD-REDUCTION, PAIR-VALUE) that shares no mechanism with the lower-bound pair. This is a
3-approach field covering 2 independent problems with justified redundancy on one of them, not
a monoculture. Do NOT spend this round's diversity slot opening a genuinely new 4th framing —
that would dilute effort exactly when both remaining gaps look closeable by direct extension of
already-certified machinery.**

### Distinct openings (assessed, not new attacks — this is a sanity-check lens)

1. **Extend TREE-BOUND-RESIDUAL's induction to arbitrary impurity count, not just ≤1.**
   Read `lemmas/tree-bound-residual.md` closely: its induction is strong induction on `m`
   (piece-count depth) with a 3-way case split at each level (impurity below top level /
   impurity at top level, aligned / impurity at top level, residual). Nowhere in the actual
   case analysis does the proof use "at most one impurity in the WHOLE forest" as a hard
   constraint beyond bookkeeping — Case C's argument bounds `D(B)` via two applications of
   the already-certified Lemma D-BOUND applied to a remainder `X` that is itself an
   `(m-1,r'')`-forest, and the IH is invoked on `X`. If `X` is allowed to carry its OWN
   (possibly ≥1) impurities recursively, the induction hypothesis just needs restating as
   "`D(B)≥τ_m` for every `(m,r)`-forest with **any finite number of impurities placed
   anywhere**" rather than "at most one" — the peeling argument (top-level split into pure
   vs top-level-impure trees, recursing into a smaller `(m-1,r')` remainder) does not care
   how many impurities live inside that remainder, since the IH is applied to the whole
   remainder as a single object regardless of its impurity count. **This looks like a
   genuine, low-risk strengthening of an existing proof, not a new argument** — the natural
   next step for `recursive-embedding-induction`, not a new approach.

2. **Extend TWO-BLOCK to two (or more) distinct simultaneous threshold values.**
   `lemmas/two-block-residue-close.md`'s core mechanism is: pick threshold `v`, split `L`
   into `Y=\{>v\}`, `Z=\{≤v\}`, apply rank-shift-by-`|Y|` and bound each side by Lemma
   D-BOUND. For two disjoint clusters tied at different values `v_1>v_2`, the natural
   generalization is a **nested application**: first threshold at `v_1` to isolate the
   globally-largest block `Y_1` (unaffected by cluster 2, since `v_2<v_1` means every
   cluster-2 companion sits inside `Z_1`), get `D(L)` via `D(Y_1)` and `D(Z_1)`, then apply
   TWO-BLOCK again inside `Z_1` at threshold `v_2` (now `Z_1` itself contains cluster 2's
   tie plus everything below `v_1`). This is a mechanical composition of the SAME lemma
   twice, not a new lemma. **This is the concrete "multi-cluster" generalization the
   prompt asks about — it looks directly reachable by iterating Lemma TWO-BLOCK, once
   per distinct tie value, in decreasing order.** Worth flagging to the builder as the
   concrete construction to try before inventing anything new.

3. **A genuinely different top-level framing for the multi-cluster gap** (e.g. a global
   "sum over all clusters" potential function, or an inductive strip-off of clusters one
   at a time as a wholly separate lemma) was considered but is strictly *more* machinery
   than options 1–2 above, which reuse 100%-certified tools (D-BOUND, rank-shift-by-s)
   with no new primitives. Not recommending this route unless 1–2 stall.

### Cheap-kill / sanity checks performed
- Re-read both `tree-bound-residual.md` and `two-block-residue-close.md` in full. Confirmed
  the "at most one impurity" / "one shared tie value v" restriction is a SCOPING choice in
  how the theorem statement was written, not a mechanism-level obstruction baked into the
  proof technique of either — both proofs' core inequality steps (peeling + D-BOUND, or
  threshold + D-BOUND) are value-agnostic and don't reference "only one" anywhere in the
  actual algebra. This is consistent with the reviewer's own numerical finding (zero
  violations on 2–4 simultaneous independent minority splits, n up to 6) — the bound is very
  likely just as tight/true with the restriction lifted, and the proof machinery already in
  hand is very likely sufficient without new primitives.
- Verified the `universal-adversary-strategy` gap (general m≥4 Case C, Hall's-theorem
  matching) is textually and mechanically disjoint from the lower-bound gap — no shared
  lemma, no shared case-split object (one is about a single fixed config `A_n`'s exact
  value; the other is about all Liu-Bang configs simultaneously). Confirms these are 2
  independent gaps, not 1 gap attacked 2 ways — consistent with the dispatch's framing.

### Consolidation question: was closing "single cluster" twice wasteful?
No — per the Rules file ("NEVER treat two approaches independently proving the same statement
via different mechanisms as wasted... it's valuable cross-verification", round 5), this was
legitimate and caught nothing wrong (both routes agree on every tested witness). **Going
forward, however, do NOT triple-duplicate**: since option 1 (forest induction) is structurally
the more natural vehicle for an arbitrary-impurity-count generalization (strong induction on
`m` already carries an unconstrained remainder), recommend `recursive-embedding-induction` take
the lead on proving the general multi-cluster theorem, while `geometric-dominance-construction`
uses its independent TWO-BLOCK route as a **cross-check on the same explicit witnesses**
(the concrete 2–4-cluster numeric configs already stress-tested) rather than re-deriving a
fully independent general proof from scratch a third time — full independent re-derivation was
valuable for the single-cluster case (first time establishing the result) but re-running the
same "two independent full proofs" pattern for the multi-cluster generalization, when the
underlying mechanism is already agreed to be the same nested-peeling idea for both, has lower
marginal value than before.

### Crux-corpus check (combinatorics domain, "simultaneous/multiple independent perturbation")
Searched `past_crux_moves_database.json` (domain=combinatorics) for techniques matching
"simultaneous", "independent perturbation", "multiple ties", "exchange/smoothing", "product
combination of independent constructions". Findings:
- `aimo-0871` (hunter-and-invisible-rabbit, subtopic `bijections-and-encoding`): crux is
  "combine several independent finite colourings into one product colouring... so a single
  legal [object] reports every component's label at once" — a genuine pattern-match for
  "handle several independent things at once by a product/composition construction," but the
  underlying domain (pursuit/graph colouring) is not close enough to be a load-bearing analogy
  for imo-2026-03's specific tie-cluster arithmetic; it's a generic pattern reminder at best,
  not a technique to import directly.
- `aimo-0146` (university-dinner cost-maximization, subtopics `extremal-principle` /
  `invariants-and-monovariants` / `double-counting`): crux is "exchange-smoothing weight toward
  higher-coefficient positions until free coordinates equalize" — structurally closer in
  flavor (sorted-sequence weighted-sum bound, exchange arguments) to this problem's `D(B)`
  machinery, but its smoothing argument operates on a single global weighted sum with one
  degree of freedom, not multiple simultaneous independent ties at different depths; not a
  direct match for the multi-cluster gap specifically.
- **No crux in the corpus directly addresses "prove a bound survives when multiple
  independent local perturbations/ties happen at once" in a form transferable to this
  problem's forest/threshold machinery.** Both hits above are weak, generic pattern reminders,
  not concrete techniques to adopt. Consistent with the round-9 explorer's finding that this
  gap needs a direct extension of the existing induction, not an imported crux move.

### Candidate technique(s) for the builder this round
- For `recursive-embedding-induction`: restate Lemma TREE-BOUND-RESIDUAL's hypothesis as
  "any finite number of impurities, anywhere in the forest" (drop "at most one"), and check
  whether the existing 3-case peeling proof goes through verbatim with the IH applied to a
  remainder that may itself carry ≥1 impurities (very likely yes — the case split never
  inspects impurity count elsewhere).
- For `geometric-dominance-construction`: generalize Lemma TWO-BLOCK's Main Theorem to a
  finite decreasing sequence of tie values `v_1>v_2>\cdots>v_k` (one per cluster, clusters
  pairwise disjoint in piece-index), via `k` nested applications of the already-certified
  Lemma TWO-BLOCK (threshold at `v_1`, recurse on `Z_1` at `v_2`, etc.) — should reuse the
  existing Structural Lemma per-cluster with only bookkeeping additions.
- For `universal-adversary-strategy`: no change of technique needed — the Hall's-theorem
  matching existence argument (`knowledge_base.md` combinatorics entry, if present — recommend
  outliner verify exact entry name) for general m Case C remains the correct and only
  candidate; keep pushing it, don't redirect.

### Knowledge-base entries to use
- Hall's marriage theorem (matching/system-of-distinct-representatives existence) — the
  concrete tool flagged since round 9 for `universal-adversary-strategy`'s general-m Case C;
  confirm its exact name/entry in `knowledge_base.md` before the builder cites it.
- No new knowledge-base entry identified for the multi-cluster lower-bound gap; it is closed
  (if it closes) by direct extension of already-certified in-house lemmas (D-BOUND, D-INSERT,
  rank-shift-by-s), not an external KB theorem.

### Analogous past problems (cruxes)
None strong enough to import directly — see crux-corpus section above; `aimo-0871` and
`aimo-0146` are weak generic-pattern matches only, not genuine analogies to cite as a proof
template.

### Prior progress
See `results/imo-2026-03/current.md` (fully read) — round 9 closed the single-cluster
minority-part/deep-bracket residue sub-case of gap (b) twice independently (Lemma
TREE-BOUND-RESIDUAL, Lemma TWO-BLOCK); `m=3` upper bound fully solved (round 9). Remaining:
(1) multi-cluster generalization of gap (b) [lower bound], (2) general m≥4 Case C [upper
bound, Hall's-theorem existence argument].

### Dead ends (do not retry)
- majorization-smoothing (RETHINK ×3, dead).
- minimax-mixed-duality (retired round 8, 2× RETHINK, no independent leverage).
- relaxed-adversary-transfer (RETHINK, structurally degenerate ∞-mark relaxation).
- Do NOT re-attempt the round-9 plan's "virtual fully-split comparison" mechanism for the
  residual case — proven FALSE (159/600 violations), already correctly abandoned in favor of
  the direct induction extension (Case C of Sub-lemma ODD).
- Do NOT re-derive the single-cluster case a third time from scratch — it is closed twice,
  cross-verified, stable; further effort belongs on the multi-cluster generalization.

### Small-case / intuition notes (conjecture, not proof)
- The reviewer's own stress test (2–4 simultaneous independent minority-tied splits, n up to
  6, dense grids, exact Fraction) found zero violations of `D≥t_n` — strong numerical evidence
  the multi-cluster generalization is true, consistent with both mechanisms extending cleanly.
- My own read of both certified lemma files supports the conjecture that the "at most one
  impurity" / "one shared value v" restriction in each was a scoping choice for tractable
  write-up, not a genuine limit of either proof technique — recommend the outliner instruct
  both builders to attempt the direct generalization (options 1–2 above) as the concrete task,
  rather than treating the multi-cluster case as requiring new insight.

### Recommendation
**Focus the two live gaps with maximal builder effort. Do not open a new 4th approach this
round.** Dispatch build set as: `recursive-embedding-induction` (generalize TREE-BOUND-RESIDUAL
to arbitrary impurity count), `geometric-dominance-construction` (generalize TWO-BLOCK to
multiple simultaneous distinct-value clusters via nested application — used as a
cross-verification pass on the same witnesses once the sibling's general theorem exists, not
a from-scratch independent full proof this time), `universal-adversary-strategy` (push Hall's-
theorem existence argument for general m Case C, unchanged target). This is 3 builders on 2
sharply-defined gaps, which matches CLAUDE.md's guidance to rank/build every round without
diluting into a 4th competing framing when the field has already converged this close to
`solved`.
