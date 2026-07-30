# Proof-builder report — `minimax-mixed-duality`, round 6, imo-2026-03

## Task
First build pass on a brand-new approach (opened this round by the outliner
per the outline-reviewer's shared-gap-plateau rule): attack the upper-bound
half of `c(n) = max_A min_B oddrank(B)` via minimax/LP duality over Xiang
Yu's mixed (randomized) strategy space, per the skeleton's instruction to
do the cheap/exploratory work first (Gap 1: finite-type decomposition; Gap
2: empirical weight search on small witnesses) before the hard expectation
inequality (Gap 3).

## What I did
1. Read `current.md`, the approach skeleton, and the round-6 explorer's
   framing rationale; cross-checked the certified lemma files (`claiming-
   phase-value.md`, `generalized-domination-and-halving.md`, `split-and-
   tail-snip.md`) and `universal-adversary-strategy.md`'s in-progress
   (uncertified) `TIE-NECESSARY` / `PARTIAL-DOM` skeletons.
2. Numerically searched (Python, `scipy.optimize` global search over all
   mark-allocation types, exact-`Fraction` verification) the two known hard
   witnesses (`A=(1/3,1/3,1/3)` and `A=(4649,3042,2309)/10000`, both `n=2`)
   for the true optimal Xiang-Yu response and its structure, per Gap 2.
3. This search surfaced a previously-unknown construction: splitting the
   top piece `p_1` **asymmetrically** so its two parts straddle a lower tail
   element, rather than splitting it evenly (Lemma HALVE) or fully
   dominating the tail (Lemma DOM). Generalized it, derived a closed-form
   value formula and exact feasibility condition, and proved it in full
   (rank-shift bookkeeping, same technique family as the certified Lemma
   DOM/SPLIT).
4. Verified the new lemma (**Lemma SANDWICH**) with 30,000 exact-`Fraction`
   randomized trials across `m∈{3,5,7}`, zero mismatches.
5. Ran a systematic sweep of the `m=3` (`n=2`-relevant) configuration space
   to measure how much of it is now covered by `{DOM, HALVE, TAIL-SNIP,
   SANDWICH}`: **~74% (504/684 sampled generic points)**. Spot-checked 4 of
   the uncovered points against the true unconstrained numeric optimum:
   all satisfy `≤ c(2)`, via constructions (e.g. splitting `p_1` alone into
   3 parts) not yet in the menu — confirming the gap is in menu coverage,
   not a counterexample to the theorem.
6. Attempted a quick check of whether the same construction helps for even
   `m`; found (on a check that did not respect the construction's own
   feasibility precondition, so inconclusive) no reliable signal either way
   and explicitly left this open rather than claim a result.
7. Wrote up Lemma SANDWICH as a proposed (not yet reviewer-certified) lemma
   file, `results/imo-2026-03/lemmas/sandwich-split.md`, and updated
   `results/imo-2026-03/approaches/minimax-mixed-duality.md` (Status →
   `partial`; "Approaches tried" and "Current best" sections rewritten with
   the round's honest results; "Full proof" section updated with a
   concrete next-round punch list).

## Key result: Lemma SANDWICH
For sorted `A=(p_1≥⋯≥p_m)`, `m` odd, if `p_1 < p_2+p_m`: splitting `p_1`
into `x∈(max(p_3,p_1-p_m),p_2)`, `y=p_1-x` (1 mark) gives, exactly,
`oddrank(B) = p_2+p_3+p_5+⋯+p_m`, independent of `x` in that range. Beats
Lemma TAIL-SNIP on the exact witness `A=(4649,3042,2309)/10000` that
`split-and-tail-snip.md` used to prove TAIL-SNIP alone insufficient
(`0.5351` vs `0.58035`), using only 1 of the 2 available marks — the
round-5 file's claim that this witness needs "a coordinated simultaneous
split of two pieces at jointly-optimized non-half ratios" is superseded (a
different, simpler single-mark move also reaches the bound there).

## Honest assessment of the mixed-strategy framing itself
The skeleton's hoped-for payoff — an explicit `A`-dependent mixing
distribution over a small candidate set whose *expectation* beats `c(n)`,
avoiding exact-minimizer casework — did not pay off this round. Since only
`min_B oddrank(B) ≤ c(n)` is actually needed (not an expectation bound),
"find good mixing weights" reduces in practice to "find enough candidate
constructions that their min already beats `c(n)`" — the same casework
`universal-adversary-strategy` is doing directly. No LP-duality shortcut
around this was found. The genuine value delivered this round came from
the *exploratory numeric search* discipline (Gap 2's instruction), not from
the minimax framing per se — recorded honestly in the approach file rather
than overclaimed.

## Status left at end of round
`partial`. One new, general, rigorously proved lemma (SANDWICH, pending
reviewer re-verification/certification); upper bound still open in general
(menu coverage gap quantified, not closed); lower bound not attempted by
this approach (explicitly out of primary scope per the skeleton).

## Files touched
- `results/imo-2026-03/approaches/minimax-mixed-duality.md` (Status,
  Approaches tried, Current best, Full proof sections rewritten).
- `results/imo-2026-03/lemmas/sandwich-split.md` (new, proposed lemma,
  awaiting reviewer certification).

## Recommendation for the reviewer / next round
1. Independently re-verify Lemma SANDWICH's proof and exact-Fraction claim;
   certify into the shared lemma set if confirmed (it is immediately
   reusable by `universal-adversary-strategy`'s casework, which is
   attacking the same regime from a different construction).
2. If continuing this approach: search for the 3-way-split-type
   construction (and other multi-mark single/joint-piece moves) needed to
   close the remaining ~26% of the `m=3` menu-coverage gap found this
   round, rather than continuing to invest in the mixed-strategy framing
   itself, whose main structural promise did not materialize.
3. Decide even-`m` SANDWICH analogue is worth a dedicated pass (open,
   inconclusive this round) or should be deprioritized in favor of directly
   coordinating with `universal-adversary-strategy`'s own even-`m`
   "two-independent-ties" open regime, which may be the same phenomenon.
