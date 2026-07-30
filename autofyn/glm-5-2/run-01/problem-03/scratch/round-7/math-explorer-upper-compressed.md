# imo-2026-03 — UPPER BOUND, GAP-U2-compressed (lens: a_{n+1} > 1/D_n)

Scout of the only remaining open sub-case of the upper bound. All findings are
terrain (conjectures labeled), not a proof. Verified by exact-`Fraction` search.

## 1. Terrain (what is closed, what is the wall, precise statement)

**Precise statement of GAP-U2-compressed.** For a strictly-decreasing Liu config
L = (a_1 > ... > a_{n+1}) with m = n+1 (all distinct) and **a_{n+1} > 1/D_n**
(compressed — the smallest piece exceeds the target 1/D_n = 1/(2^{n+1}−1)),
exhibit a ≤ n-mark Xiang strategy with D ≤ 1/D_n. (D = odd-index sum of the
refined sorted multiset; Liu's take = (1+D)/2; upper bound c(n) ≤ 2^n/D_n ⟺ D* ≤ 1/D_n.)

**CLOSED (certified, all n):** m ≤ n ⟹ D*=0 (`m-le-n-halving-D-zero`); m=n+1
with a repeat ⟹ D*=0 (`repeated-value-D-zero`); m=n+1 strictly-decreasing with
a_{n+1} ≤ 1/D_n ⟹ D ≤ a_{n+1} ≤ 1/D_n (`halving-always-a-nplus1`). The tower
T_n = (2^n,...,1)/D_n has a_{n+1} = 1/D_n exactly (the boundary, NOT compressed)
and D*(T_n) = 1/D_n (tight, `parallel-halving-saturates-tower`). n=1,2,3 fully
closed. So GAP-U2-compressed is strictly the interior region a_{n+1} > 1/D_n.

**The wall.** In the compressed region the halving bound D = a_{n+1} OVERSHOOTS
(a_{n+1} > 1/D_n). The even-packing reframe (D = 1−2E) is EQUIVALENT, not a
bypass. O1 (split-bottom + exact-pair-rest) is PROVABLY DEAD. Parity obstruction:
≤ n marks on strictly-decreasing m=n+1 ⟹ refined count ≤ 2n+1 (odd) ⟹ D ≠ 0
always; so the target is D = small leftover ≤ 1/D_n, never D = 0 via exactly n
marks (though D = 0 IS reachable with < n marks when the structure allows — see
below). Tower is the UNIQUE isolated maximizer of D* (every perturbation drops
D* to 0 or tiny); pure continuity/exchange is blocked by this discontinuity.

**CRITICAL METHODOLOGY FINDING (load-bearing).** The correct refinement model
allows RECURSIVE splits: each mark splits ANY current piece (including a
previously-created fragment), not just an original Liu piece. With k marks on
one piece of value a, you partition a into k+1 arbitrary positive parts. So a
≤ n-mark refinement = distribute k_i ≥ 0 marks to the n+1 pieces (∑ k_i ≤ n),
partition each a_i into k_i+1 parts. The earlier round-6 "violations" of the
compressed claim for (7,4,2,1)/14 etc. were a SEARCH BUG — they only split
ORIGINAL pieces, missing the fragment-splitting structure that is the actual O2
mechanism (e.g. split a_1=7 → {4,3} then split the fragment 3 → {2,1}, giving
{4,4,2,2,1,1}, D=0). **The recursive model is mandatory; the halving lemma and
block-contribution formula already handle fragments (they sort the whole refined
multiset).** O1's deadness is unaffected (O1 was about exact-pairing the REST,
a different and genuinely impossible target).

## 2. Route O2 terrain (split-LARGE-to-match-MEDIUM)

**Exact reduction (the clean sufficient condition).** Given compressed
a_1 > ... > a_{n+1} with a_{n+1} > 1/D_n, the O2 strategy is:
- Pick a subset S ⊆ {a_2, ..., a_{n+1}} of the smaller pieces to REPRODUCE from
  a_1 (split a_1 into the parts {a_i : i ∈ S} ∪ {leftover}, where leftover =
  a_1 − sum(S) ≥ 0). This uses |S| marks if leftover > 0, |S|−1 if leftover = 0.
- HALVE every un-reproduced piece a_j (j ∉ S, j ≥ 2): split a_j → {a_j/2, a_j/2}
  (1 mark each); the two halves form an adjacent-equal pair, contributing 0.
- Total marks: (|S| or |S|−1) + (n − |S|) = n (or n−1). ✓
- Result: every reproduced value a_i (i ∈ S) appears TWICE (once from a_1, once
  original) ⟹ even block ⟹ contributes 0. Every halved value a_j/2 appears
  twice ⟹ even block ⟹ 0. The ONLY odd-multiplicity value is the leftover
  (multiplicity 1), and by `halving-always-a-nplus1`'s Step-4 argument all
  blocks above it are even ⟹ it starts at an ODD position ⟹ contributes
  +leftover. So **D = leftover = a_1 − sum(S)**.

So O2 reduces to: **find S ⊆ {a_2,...,a_{n+1}} with sum(S) ∈ [a_1 − 1/D_n, a_1]**
(equivalently leftover ∈ [0, 1/D_n]). Then D = leftover ≤ 1/D_n. This is a
SUBSET-SUM existence problem (Prouhet-Tarry-Escott / multiset-equal-sums flavor;
KB "Multiset partitions & power-sum matching").

**Is it a known theorem?** Not directly — it is a subset-sum DENSITY claim on a
bounded-spread set of n real values, with target window width 1/D_n. No KB
entry subsumes it; the closest KB tool is "Pigeonhole / extremal" and
"Multiset partitions & power-sum matching." The hard step is the density claim
(see §3).

**Regime split (verified, 300 random Fraction-exact configs per n):**
- **a_1 ≤ 2^n/D_n regime (~70–80% of compressed configs):** the subset-sum
  target interval [a_1 − 1/D_n, min(a_1, 1−a_1)] is NONEMPTY (since a_1 ≤ 2^n/D_n
  ⟺ a_1 − 1/D_n ≤ 1 − a_1). The subset-sum strategy ALWAYS found a hitting
  subset in my tests (0 violations, worst ratio ~0.999 — i.e. leftover nearly
  1/D_n, at near-tower configs). This is the PROVABLE core via subset-sum density.
- **a_1 > 2^n/D_n regime (~20–30% of compressed configs, "large top"):** NO
  subset of {a_2,...,a_{n+1}} can reach a_1 − 1/D_n (max subset sum = 1 − a_1 <
  a_1 − 1/D_n). The subset-sum-from-a_1 strategy is IMPOSSIBLE here. But the
  FULL recursive search (allowing splits of multiple pieces, not just a_1)
  still finds D ≤ 1/D_n for ALL tested configs (0 violations, n=2,3 full
  search; n=4,5,6 breakpoint search). The achieving strategy splits MULTIPLE
  large pieces (e.g. halve a_1 AND halve a_2, or halve a_1 AND split a_2 to
  reproduce a_3, etc.). **This regime is the genuine hard step of O2** — it
  does not reduce to a clean single-piece subset-sum.

**Exact numerics (recursive breakpoint search, exact Fraction):**
- n=2: 0 violations / 8397 compressed integer configs (maxsum=100). Worst ratio
  0.9579 at (54,27,14)/95 (a_1 = 2·a_2, near-tower). Tower (4,2,1)/7 ratio 1.000.
- n=3: 0 violations / 2018 configs (maxsum=45). Worst ratio 0.8824 at
  (8,4,3,2)/17 (a perturbation of T_3 = (8,4,2,1)/15). The (7,4,2,1)/14 config
  (a_1 = a_2+a_3+a_4 = 1/2) achieves D = 0 by splitting a_1 → {a_2,a_3,a_4}.
- n=4: 0 violations / 408 configs (maxsum=30). ALL configs achieve D = 0
  (the compressed region is "loose" for n=4 — full cancellation always
  reachable). Tower (16,8,4,2,1)/31 ratio 1.000.
- Large-a_1 sub-cases (n=3,4): (12,4,3,2)/21 a_1=0.571>0.533 ⟹ subset-sum
  fails, but halving a_1+a_4 gives D = a_2−a_3 = 1/21 < 1/15. (16,9,5,3,2)/35
  (a_1<1/2) ⟹ D=0 via a_1 → {a_2,a_3,a_4,a_5} (a_1 = sum of rest = 1/2).

**No counterexample found.** The candidate answer c(n) = 2^n/D_n survives
across n=2..6 (thousands of configs, 0 violations). A counterexample would need
a_1 > 2^n/D_n (large top) AND a compressed bottom AND a middle-gap structure
resisting every multi-piece split — none found, but this regime is NOT proved.

## 3. Route bounded-spread pigeonhole terrain

**Derivation.** Compressed: a_i ≥ a_{n+1} > 1/D_n for all i, ∑ a_i = 1 ⟹
a_1 = 1 − ∑_{i≥2} a_i < 1 − n·a_{n+1} < 1 − n/D_n = (D_n − n)/D_n. So the
spread a_1/a_{n+1} < D_n − n = 2^{n+1} − 1 − n. All pieces lie in a factor-
< (2^{n+1}−1−n) ≈ 2^{n+1} range.

**Pigeonhole statement (naive, NOT tight).** The 2^n subset sums of
{a_2,...,a_{n+1}} lie in [0, 1−a_1] < [(n+1−?)/D_n, ...]. For a subset sum to
hit the window [a_1−1/D_n, min(a_1,1−a_1)] of width 1/D_n, naive pigeonhole
needs 2^n · (1/D_n) > (range) ≈ a_1 < (D_n−n)/D_n, i.e. 2^n > D_n − n =
2^{n+1}−1−n, i.e. n+1 > 2^n. **FALSE for n ≥ 3.** So the naive subset-sum
pigeonhole is NOT tight — there are fewer subset sums (2^n) than buckets
(D_n−n ≈ 2^{n+1}). The density must come from the STRUCTURE of compressed
configs (the a_i are themselves in a narrow range, so subset sums cluster, and
the window 1/D_n is wide relative to the piece sizes), not from a raw count.

**Tighter pigeonhole (candidate).** Since all a_i > 1/D_n and there are n of
them, and they lie in [a_{n+1}, a_1] with spread < D_n−n, consecutive a_i (after
sorting) satisfy a_i − a_{i+1} < (a_1 − a_{n+1})/(n) < (D_n−n)·a_{n+1}/n. The
gaps are < (D_n/n)·(1/D_n) = 1/n-ish. A GREEDY cascade "split a_1 to match a_2,
then the remainder to match a_3, ..." (Euclidean-algorithm flavor) may force a
hit. NOT proved — this is the hard step, and it is the same density claim as O2.
The pigeonhole and O2 routes CONVERGE on the same subset-sum density core.

**Verdict on Route 2.** The bounded-spread derivation is correct and cheap, but
the pigeonhole-to-matchable-structure step is NOT tight as a raw count and
reduces to the same subset-sum density as O2. It is a DIAGNOSTIC (the compressed
region has bounded spread, so pieces are "matchable") not an independent proof.
Worth keeping as the intuition for WHY O2 should work, but the outliner should
not skeleton a pure-pigeonhole proof — it will hit the same 2^n < D_n−n gap.

## 4. Cleaner direct strategy (dispatch option c — strongest candidate)

**Greedy "split the largest piece to match the next smaller" cascade.** Process:
split a_1 → {a_2, a_1 − a_2} (1 mark, creates a tie at a_2; the pair a_2,a_2
cancels). Now the "active remainder" is r_1 = a_1 − a_2. If r_1 ≥ a_3, split r_1
→ {a_3, r_1 − a_3} (1 mark, tie at a_3). Continue: at step k, the active
remainder r_{k−1} is split to match a_{k+1} if r_{k−1} ≥ a_{k+1}. This is a
GREEDY EUCLIDEAN-style reduction. Each step pairs one more a_i (cancels it) and
reduces the active remainder. After ≤ n−1 steps, either all a_2..a_{n+1} are
paired (D = 0 if remainder = 0, or D = small remainder) or the remainder falls
below a_{k+1} and we halve it (self-pair, 1 mark) leaving D = 0.

**Potential function.** The active remainder r_k is strictly decreasing (each
step subtracts a_{k+1} ≥ a_{n+1} > 1/D_n). The number of un-paired a_i strictly
decreases. The process terminates in ≤ n−1 steps with a remainder r ≤ a_{n+1}
(or 0). If r ≤ 1/D_n, done (D = r ≤ 1/D_n). If r > 1/D_n... but r < a_{k+1}
(the next a_i, which it couldn't match), and a_{k+1} could be > 1/D_n.

**Why this is promising but unproven.** The greedy matches the O2 witnesses
exactly (e.g. (7,4,2,1)/14: a_1=7 → match a_2=4, remainder 3 → match a_3=2,
remainder 1 → match a_4=1, remainder 0, D=0; uses 2 marks = n−1). It explains
the D=0 cases (when a_1 = a_2+a_3+...+a_{k} for some prefix, the greedy hits
remainder 0). The hard step: when the greedy remainder r_k falls BELOW a_{k+1}
but ABOVE 1/D_n (stuck between two a_i, both > 1/D_n). In the bounded-spread
compressed region, this "stuck" case may be ruled out by the gap bound
(a_{k+1} − a_{k+2} < ... ), but I could NOT prove this. The greedy is the
cleanest candidate for a UNIFIED direct strategy (handles both regimes without
the subset-sum/pigeonhole detour), and it reduces to a potential-function /
monovariant argument (KB "Invariants & monovariants"). **This is the route I
recommend the outliner skeleton first** — it is genuinely different from O2's
subset-sum (it is sequential/greedy, not existential) and may dodge the a_1 >
2^n/D_n hard regime.

**Reduction to certified halving via perturbation.** Another clean idea: the
tower is an isolated extremum; any compressed config is a perturbation. If we
could find a single preprocessing split that moves the config INTO the
a_{n+1}' ≤ 1/D_n region (where halving closes it), we'd be done. Concretely:
split a_1 (the largest) into {x, a_1−x} where x is chosen so the NEW smallest
piece is ≤ 1/D_n. But the smallest is a_{n+1} (unchanged by splitting a_1
unless a_1−x < a_{n+1}); to make a_{n+1}' ≤ 1/D_n we'd need to split a_{n+1}
itself, which is O1's dead route. So this perturbation idea reduces to O1 and
is dead. Do NOT pursue.

## 5. Concrete recommendations for the outliner

**Recommendation: ADVANCE `majorization-upper` (do NOT open a new slug).** The
O2 mechanism is the natural closure of Part VII-bis; it imports
`halving-always-a-nplus1`, `block-contribution-formula`, `spine-pair-cancellation`
(all certified) and uses the recursive-split model that those lemmas already
handle. A new slug would re-derive the same scaffolding.

**Skeleton the proof in TWO independent sub-claims (do not collapse to one —
the a_1 > 2^n/D_n regime does not reduce to subset-sum):**

(A) **Subset-sum regime (a_1 ≤ 2^n/D_n):** prove the density claim — for n
bounded-spread values a_2,...,a_{n+1} ∈ (1/D_n, a_1] with a_1 ≤ 2^n/D_n, SOME
subset sums into [a_1 − 1/D_n, min(a_1, 1−a_1)]. The O2 strategy then gives
D = leftover ≤ 1/D_n. Hard step: the density claim (2^n < D_n−n, so raw
pigeonhole fails — need the bounded-spread STRUCTURE). Candidate tool: a
greedy partial-sum walk (the §4 cascade restricted to a_1) with a monovariant.

(B) **Large-top regime (a_1 > 2^n/D_n):** prove D ≤ 1/D_n via a multi-piece
split (NOT subset-sum-from-a_1). The full search confirms it always holds (0
violations n=2,3) but the achieving strategy varies (halve a_1+a_2, or
a_1+a_{n+1} giving D = middle alternating, or reproduce a_2..a_k from a_1 then
halve the rest). Hard step: find a UNIFYING sufficient condition. The greedy
cascade (§4) is the best candidate — it is sequential and may handle both
regimes uniformly; skeleton IT first as the primary spine, with (A) as a
fallback for the regime where the greedy provably terminates cleanly.

**Most promising single route: the greedy "split largest to match next smaller"
cascade (§4) with a monovariant (active remainder, # un-paired a_i).** It is
genuinely different from O2's existential subset-sum (it is constructive/
sequential), matches all witnesses, and may dodge the a_1 > 2^n/D_n hard regime
that kills the subset-sum reduction. The hard step to skeleton: prove the
greedy remainder never gets "stuck" in (1/D_n, a_{k+1}) — i.e., either it
reaches ≤ 1/D_n or it matches the next a_i. The bounded-spread gap bound
(a_{k+1} − a_{k+2} < (D_n/n)·a_{n+1}) is the candidate tool, but I could not
close it — flag it as the GAP.

**Respect the dead ends:** O1 (dead — exact pairing impossible, IVT category
error), V(n)←V(n−1) IH (phantom), 3-mark cascade (phantom), Max-bound D*≤M/2^n
(refuted by (7,6,5,3)/21), Schur/majorization (dead — D* not Schur-convex),
even-packing as bypass (=equivalent reframe), pure continuity/exchange (blocked
— tower is isolated discontinuous extremum). The perturbation-to-halving-region
idea (§4 last paragraph) reduces to O1 and is also dead.

**Small-case / intuition notes (all CONJECTURES, labeled):**
- The recursive-split model is essential; fragment-splitting is what makes O2
  work (CONJECTURE: the breakpoint optimum always allows fragment splits, per
  `pl-breakpoint-minimum`).
- D = 0 is achievable for MOST compressed configs (all n=4 tested, most n=3);
  the tower is the unique config where D = 1/D_n is forced. CONJECTURE: the
  compressed region has D* = 0 generically, with D* → 1/D_n only as the config
  approaches the tower boundary a_{n+1} → 1/D_n from above.
- The worst non-tower ratios are at near-tower perturbations ((8,4,3,2)/17
  ratio 0.88, (54,27,14)/95 ratio 0.96) — the difficulty concentrates at the
  tower boundary, not in the deep compressed interior.
- The a_1 > 2^n/D_n "large top" regime is ~20–30% of compressed configs (random
  real sampling) but rarer for integer configs; it is the subset-sum-resistant
  core and the primary target for the greedy direct strategy.
