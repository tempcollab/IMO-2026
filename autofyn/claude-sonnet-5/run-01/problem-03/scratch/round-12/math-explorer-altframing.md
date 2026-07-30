## imo-2026-03 (alt-framing sanity check, round 12)

### Verdict (headline)
**NO-GO on opening a genuinely new top-level framing this round.** Stay in the
casework/adaptive-construction framing. Three consecutive rounds of dedicated
alt-framing scouting (rounds 7, 9, 10, 11) have already searched this space —
relaxed-adversary-transfer (∞-mark relaxation), minimax-mixed-duality (LP/dual
certificate), case-c-secondary-extremality (secondary statistic), and
majorization-smoothing (concavity-of-V(A) smoothing) — and every one of them
is a *provably* dead structural mismatch, not a stalled numeric search. I
re-verified (by re-reading, not re-deriving from scratch — time-boxed) that
none of these rulings look like a misdiagnosis, and I did not find a crux or
technique this round that escapes the same traps. The sharpest live thing to
add is a **refinement inside the matching framing** (Hall-deficient-set
deletion), not a new framing.

### What I checked against the 4 candidate "genuinely new" framings in the dispatch

1. **Smoothing/exchange directly on the configuration space A (not on Xiang
   Yu's response).** This is exactly what `majorization-smoothing` tried:
   prove `V(A) := min_B oddrank(B)/Σ(A)` is concave in `A`, so the
   maximizer (Case C's sup) sits at a low-dimensional vertex/canonical
   family, closing the upper bound by inspection of finitely many extremal
   shapes. **Already dead**, and dead for a structural reason, not a
   numerical near-miss: current.md confirms (round 3-4, re-confirmed round 5
   via the mandated Step-0 gate) that `V` has a genuine nested convex kink —
   `V` is the min of an affine piece and a genuinely convex piece, so
   concavity fails by construction, not just at one unlucky sample point.
   Any first-order/KKT variant of "smooth A toward canonical form" inherits
   the same problem: the objective is not smooth/concave in `A`, so a
   local-perturbation argument cannot conclude global optimality sits at a
   vertex without first handling the same convex-kink case split that killed
   the concavity route. This is a real obstruction to the whole "smooth the
   adversary directly" idea, not just to Lemma C's specific proof — do not
   revive it without a way around the kink.

2. **An LP/duality certificate specific to Case C, distinct from
   minimax-mixed-duality.** `minimax-mixed-duality` was explicitly retired
   (round 8) after 2 consecutive RETHINKs where **every** duality
   construction it produced reduced to an instance of
   `universal-adversary-strategy`'s own discrete tie-search — i.e. the dual
   object it kept finding *was* the same casework, just relabeled. I don't
   see a reason a fresh LP-duality attempt at Case C specifically (rather
   than the whole game) would behave differently: Case C's target
   (`oddrank(B) ≤ c(m)Σ(A)` for the winning response) is exactly the kind of
   min-max-with-equality-at-many-extremal-points structure where LP duality
   just re-derives "there exists a matching/chain achieving the bound" —
   the same existence statement the matching framework is already trying to
   prove directly. A new duality attempt would need a genuinely different
   dual *object* (not just "Case C's LP" as opposed to "the whole game's
   LP") to avoid collapsing the same way; I found no candidate for what that
   object would be.

3. **Entropy/potential-function argument.** No natural entropy functional
   suggests itself: the objective `oddrank` is a rearrangement-style linear
   functional (sum of odd-ranked elements after sorting), not a
   counting/multiplicative quantity where entropy methods (Shearer,
   compression) typically apply. `potential-averaging-bound`'s round-5
   attempt (a *static* potential — average of a few candidate constructions)
   already failed its own feasibility gate with an exact counterexample
   (`A=(1/3,1/3,1/3)`, n=2: every tested candidate gives `2/3 > c(2)`, true
   optimum `1/2`), and the per-round-8 rule notes explicitly that even the
   *dynamic/sequential* potential reading remains conceptually available but
   has never actually been exercised for Case C's existence question — it
   was scoped to the lower bound at the time. I looked for a natural
   "monovariant that decreases every round of the recursive-induction" for
   Claim PTBI's Case C specifically; the closest thing that already exists
   is Lemma THRESHOLD-REDUCTION's identity `c(k-1)=c(k)/(2(1-c(k)))`, which
   is already fully exploited by the current induction (it reduced 2 of the
   3 Claim PTBI cases). I don't see an additional monovariant beyond what's
   already certified; this is a "maybe worth a cheap probe" not a strong
   lead.

4. **Extremal graph theory / flow argument.** Case C's remaining gap is
   fundamentally: match some pieces of `A` (the donors) to subsets/values of
   the tail so that after splitting-and-tying, the resulting `oddrank` sits
   below target — a subset-sum/exact-cover matching, **not** a 1-1 SDR (per
   round 10's own diagnosis, confirmed correct: textbook Hall's marriage
   theorem doesn't directly apply because one donor piece can cover a whole
   *subset* of targets at once). A max-flow/min-cut reformulation of this
   (donors as sources, tail-subset-covers as sinks, capacities = piece
   sizes) is plausible in principle but is exactly the "reformulation as a
   hypergraph matching" idea round 10 already flagged as the promising
   unexplored angle — it is a refinement of the existing matching framing,
   not an escape from it.

### Crux corpus search (combinatorics, subtopics extremal-principle,
games-and-strategy, graph-theory-and-connectivity)

Filtered `past_crux_moves_database.json` for combinatorics × {extremal-
principle, games-and-strategy} plus keyword scan (smoothing/exchange/
extremal/majorization/rearrangement) across all combinatorics. Findings:

- **aimo-0117** (dyadic/geometric-domination, "largest value exceeds sum of
  rest") — already the crux behind the geometric config `A_n` itself
  (cited in current.md's Rules). Not new leverage for Case C.
- **aimo-0560** (IMO 2022 P6 gardener/lumberjack, "replace the adversary
  with a strictly stronger surrogate") — already tried as
  `relaxed-adversary-transfer`, cleanly RETHINK'd (round 7): the natural
  surrogate (relax Xiang Yu's mark budget to ∞) is config-independent
  (`V_∞(A)=1/2` always) and points the wrong direction. **Do not revive.**
- **aimo-0146** ("maximize a weighted sum of a sorted sequence by
  exchange-smoothing toward higher-coefficient positions" — degree-weighted
  edge-functional graph problem). This is the closest genuine analogue to a
  fresh smoothing idea I found, but it is mechanically the *same* move
  `majorization-smoothing` already tried and that died on the convex-kink
  obstruction (item 1 above) — `oddrank` is not the simple linear
  weighted-sum-of-sorted-sequence functional aimo-0146's exchange argument
  needs (the weights `1,0,1,0,...` depend on the *merged* multiset's rank
  order, which shifts nonlinearly as Xiang Yu's marks change piece counts —
  this rank-shift-under-refinement nonlinearity is exactly the mechanism
  behind the "convex kink"). Not a new lever.
- **aimo-0063** ("Hall-deficient-set-deletion: iterate — remove a
  Hall-violating set and its neighborhood, repeat, using a vertex adjacent
  to every candidate to force the terminal matching nonempty" — a fair
  division / cake-cutting matching problem). This is a genuinely useful
  **refinement** — not a new framing — for the matching/exact-cover gap
  Case C needs (round 10 already flagged this exact crux as the next thing
  to try and it has not yet been attempted by a builder). It is a technique
  *within* the matching framing (a deficiency-version of Hall's theorem for
  when a perfect 1-1 matching may not exist), adapted to a subset-cover
  bipartite-like structure. Worth trying next round, but it is not the
  "genuinely different framing" the dispatch is asking me to gate on — it's
  the natural continuation of `universal-adversary-strategy`'s own stated
  next step.
- **aimo-0438** ("among all optimal configurations, pick one maximizing a
  secondary alignment statistic, then show local deviation admits a
  strictly-increasing exchange") — already tried as
  `case-c-secondary-extremality`, RETHINK'd (round 11): its own feasibility
  gate showed the natural secondary statistic (tied-pair count) is
  algebraically value-equivalent to the primary approach's construction on
  the hard witness, giving zero independent leverage. **Do not revive
  without a genuinely different secondary statistic**, and I did not find
  one in this search.

No crux in the corpus stands out as a transferable "no configuration beats
the extremal one" template that Case C hasn't already tried and refuted —
the closest matches (aimo-0117, aimo-0560, aimo-0146, aimo-0438) are all
already in `results/imo-2026-03/`'s history, tried and either closed (0117)
or killed (0560, 0146-flavor, 0438).

### Recommendation for round 12

- Do **not** open a 4th top-level framing slug. The field is correctly
  narrowed to `universal-adversary-strategy`'s matching/adaptive-
  construction approach for Case C, `m≥4`.
- The one concrete, not-yet-tried lever from this search: adapt **aimo-0063's
  Hall-deficient-set-deletion** to Case C's subset-cover matching structure
  (donors = split pieces; each donor can cover a *subset* of tail targets at
  once, not just one). Round 10's math-explorer already flagged this same
  crux as the recommended next tool; round 11's builders did not use it
  (they tried fixed-shape templates instead, both refuted). This should be
  folded into `universal-adversary-strategy`'s next revision, not spun out
  as a separate slug — it's the same approach's next tool, not competing
  diversity.
- Secondary, lower-confidence lead: revisit whether Lemma
  THRESHOLD-REDUCTION's identity `c(k-1)=c(k)/(2(1-c(k)))` (already
  certified) admits a *sequential/dynamic potential* reading — i.e. track a
  running potential through the adaptive match-vs-chain-vs-halve decision
  process and show it's monotone — as a proof *organization* device for
  the existence argument (not a new bound, just possibly a cleaner
  induction skeleton). This is speculative and should be a cheap probe, not
  a mandated target.

### Dead ends confirmed (do not retry)
- Concavity-of-`V(A)` / smoothing directly on the Liu Bang configuration
  (majorization-smoothing mechanism) — structurally dead (convex kink),
  confirmed 3x, including a mandated reconciliation gate.
- ∞-mark relaxed-adversary surrogate (aimo-0560 style) — structurally dead,
  wrong-direction inequality (`relaxed-adversary-transfer`, round 7).
- Secondary-extremality / secondary alignment statistic on top of the
  primary matching construction (aimo-0438 style) — value-equivalent to the
  primary construction, no independent leverage (`case-c-secondary-
  extremality`, round 11).
- LP/mixed-strategy duality as an independent proof shape for the whole game
  or for Case C specifically — collapses into the same discrete casework
  every time it's been tried (`minimax-mixed-duality`, rounds 6-8, retired).
- Fixed small-integer-count top-level pairing templates (any number of
  pairs) as a universal Case C construction — refuted for all `m=4..100` by
  the near-uniform-tail witness family (round 11).
- Greedy largest-first subset-sum matching for the donor/target assignment —
  74% failure rate (round 10).

### Small-case / intuition notes
No new numeric probing was done this round (this was a framing-only sanity
check per dispatch); all evidence cited above is inherited from prior rounds'
independently-reviewer-verified numerics, which I did not need to re-run to
answer the go/no-go question.
