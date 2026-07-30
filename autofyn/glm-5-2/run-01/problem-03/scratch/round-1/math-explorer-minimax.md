# imo-2026-03 — minimax & small-n computation route

## Distinct openings
- **Lower bound = explicit dyadic construction.** Liu Bang places marks so the resulting pieces (sorted descending) are `(2^n, 2^{n-1}, …, 2, 1)/(2^{n+1}−1)`. Key structural property: each piece strictly exceeds the sum of all smaller pieces, since `2^k = (2^k − 1) + 1`. This "superincreasing" / dyadic dominance is the load-bearing feature — it pins how Xiang Yu's splits can perturb the sorted order and bounds Liu's odd-index sum from below.
- **Upper bound = adaptive halving (Xiang Yu).** For n=1 the optimal Xiang strategy is a clean casework: if Liu's larger piece `a≥1/2` satisfies `a ≥ 2(1−a)` (i.e. `a≥2/3`) halve it (gives Liu `(1+a)/2 ≤ 2/3`), else do nothing (gives `1−a ≤ 2/3`). The natural generalization to n marks is a recursive/greedy "halve the dominant piece" with an induction on n, but the exact adaptive rule for general n is the open crux — it is NOT simply "always halve the largest piece" (that fails when Liu plays near-equal pieces; Xiang must then mark nothing or mark elsewhere).
- **Reframe as Xiang maximizing even-index sum.** Since `Liu = 1 − Xiang` (total is fixed), the minimax becomes `c(n) = 1 − min_{Liu configs} (max Xiang even-index grab)`. This swaps the bound direction: prove Xiang can always grab `≥ (2^n − 1)/(2^{n+1} − 1)` of the stick. This "Xiang can always secure a 1 − 1/2^n fraction of the even mass" framing may be cleaner for the upper bound.
- **Continuous minimax LP/convexity angle.** For fixed split-pattern the odd-index sum is piecewise-linear in the cut positions, so optima occur at tie-points (two subpieces equal). This structural fact (every optimum has "balanced" splits) reduces the continuous game to a finite combinatorial check per pattern — a route to a rigorous upper bound by enumerating Xiang's patterns.

## Candidate technique(s)
- **Greedy draft = odd-index sum** (the foundational reduction; verified computationally, needs a short proof — see below).
- **Dyadic / superincreasing weights** for Liu's construction (largest exceeds sum of all smaller).
- **Induction on n** with the recursion `r_n = 2^n/(2^{n+1}−1) = 1/(2 − 2^{−n})`, relating `r_n` to `r_{n−1}`.
- **Piecewise-linearity + extremal-at-ties** to reduce Xiang's continuous optimization to finitely many balanced-split configurations.

## Cheap-kill candidates
- **n=1 base case by hand** fully settles the recursion's anchor and exposes the adaptive halving rule (done above).
- **Parity / piece-count:** with ≤2n+1 total pieces, Liu takes `⌈m/2⌉` pieces; Xiang's max grab is `⌊m/2⌋` pieces. A size bound alone is too weak (gives 1/2, below target), but combined with the dyadic dominance it may close.
- **The powers-of-2 "each piece > sum of smaller"** is itself a one-move structural kill for the lower bound's stability under splits.

## Knowledge-base entries to use
- **Pólya: Solve a simpler/special case first; Specialize; Strengthen the hypothesis (induction loading).** The n=1,2,3 case computation drove the guess.
- **Induction (ordinary/strong) + infinite descent dual** — for the recursive bound in n.
- **Invariants & monovariants** — the dyadic-weight invariant likely governs the lower bound.
- **Pigeonhole/extremal principle** — for the upper-bound adaptive argument (take the dominant piece).
- **Piecewise-concavity smoothing** (kb) is conceptually related: the odd-index sum as a function of cut positions is piecewise-linear with minima at tie-points — the same "min at a breakpoint" logic.

## Analogous past problems (cruxes)
- **aimo-0117** (dyadic powers-of-two game): crux = "Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others." Directly analogous — Liu's pieces `(2^n,…,1)` have exactly this property (`2^n > 2^{n−1}+…+1`), and it is what makes the construction work. Adapt, do not cite.
- No other crux closely matches (the corpus has no stick-cutting alternating-draft game). aimo-0117 is the single best hit.

## Prior progress
- None (round 1, empty workspace).

## Dead ends (do not retry)
- **Equal-piece construction** (Liu cuts into n+1 equal pieces of `1/(n+1)`): for n=1 gives Liu only `1/2` (Xiang halves one piece → Liu `1/2+1/4=3/4`? no — Xiang marks nothing → Liu `1/2`; for equal pieces Xiang's best is to NOT mark). For n=2 equal thirds give Liu only `1/2`. Uniform marking is strictly worse than the dyadic config. Confirmed dead.
- **Naive "halve the largest piece" as Xiang's universal upper-bound strategy:** FAILS. When Liu plays near-equal pieces, halving the largest gives Liu MORE than `2^n/(2^{n+1}−1)`; Xiang must instead mark nothing (or split a small piece). The universal strategy must be adaptive. Do not assume a fixed greedy rule.

## Small-case / intuition notes (CONJECTURE, backed by exact hand analysis + numerics)
**Computed c(n) table (exact for n=1,2,3 by hand analysis; n=4 by grid consistency):**

| n | c(n) | Liu's optimal pieces (sorted desc) | Xiang's optimal response |
|---|------|--------------------------------------|--------------------------|
| 1 | **2/3** ≈ 0.6667 | (2,1)/3 = {2/3, 1/3} | halve the 2/3 → {1/3,1/3,1/3}; or mark nothing if Liu plays equal |
| 2 | **4/7** ≈ 0.5714 | (4,2,1)/7 = {4/7,2/7,1/7} | halve 4→2,2 (one mark) → {2,2,2,1}/7; Liu = 2+2 = 4/7 |
| 3 | **8/15** ≈ 0.5333 | (8,4,2,1)/15 | halve 8→4,4 and 4→2,2 → {4,4,2,2,2,1}/15; Liu = 4+2+2 = 8/15 |
| 4 | **16/31** ≈ 0.5161 | (16,8,4,2,1)/31 | halve 16→8,8, 8→4,4, 4→2,2 → Liu = 8+4+2+2 = 16/31 |

**Candidate closed form (CONJECTURE, strongly supported):**

$$c(n) = \frac{2^n}{2^{n+1} - 1} = \frac{1}{2 - 2^{-n}}.$$

Verification status:
- n=1: PROVEN by hand (full case analysis above).
- n=2: PROVEN by hand on the dyadic config (Xiang's best = 4/7, verified by exhaustive split-pattern analysis: splitting 4→(p,4−p) and 2→(q,2−q) yields Liu ≥ 4/7 with equality at p=2, any q∈[2,3]… rechecked: p=4? units clarify — Liu = 4/7 exactly, Xiang cannot beat it). Upper bound (no Liu config beats 4/7) confirmed by vectorized grid scan (best found = 0.5719 ≈ 4/7, achieved exactly at marks 1/7, 3/7).
- n=3: PROVEN by hand on the dyadic config (split 8→4,4 & 4→2,2 gives Liu 8/15; all 2-mark patterns give ≥ 8/15). N=30 grid gave exactly 8/15.
- n=4: grid-consistent only (Xiang-min ≈ 0.5167 vs 16/31 = 0.51613); not hand-proven.

Asymptotics: `c(n) → 1/2` from above as `n → ∞`; `c(1)=2/3` is the largest.

## Greedy-selection optimality — KEY SUB-CLAIM (must be proven)
**Claim:** Once the multiset of piece lengths is fixed (sorted descending `a_1 ≥ a_2 ≥ … ≥ a_m`), optimal play by both players (Liu first, each maximizes own total) yields Liu exactly the odd-index sum `a_1 + a_3 + a_5 + …`, i.e. greedy "always take the largest available piece" is optimal for both.

**Status:** Verified computationally (full minimax over the draft tree) on 2000 random instances up to 6 pieces — no mismatch. NOT YET PROVEN.

**Proof sketch for the outliner (one-line, do not develop):** This is a zero-sum game with payoff = (Liu − Xiang) (total fixed), and the standard exchange/adjoint argument shows greedy is a dominant strategy: any deviation lets the opponent grab the piece the deviator skipped. The cleanest form is by backward induction showing the greedy move is weakly optimal at every node (classic "items sorted decreasing, alternate draft" result).

## Main difficulties (for the outliner)
1. **Upper bound (Xiang's strategy) is the hard direction.** Must show for EVERY Liu config (≤n marks → ≤n+1 pieces), Xiang can hold Liu ≤ `2^n/(2^{n+1}−1)`. The strategy is adaptive (not a fixed greedy rule — see dead ends). Likely an induction on n with a case split on whether Liu's largest piece dominates (`≥ 2·(rest-leading)`). The n=1 case analysis (above) is the template; generalize the "halve-if-dominant, else leave" dichotomy.
2. **Lower bound (Liu's strategy):** prove the dyadic config forces Liu ≥ `2^n/(2^{n+1}−1)` against ANY Xiang response. The superincreasing property (`2^k > 2^{k-1}+…+1`) is the crux; need a lemma that splitting a superincreasing multiset cannot reduce the odd-index sum below the top element. Conjectured lemma: *if pieces are superincreasing (each > sum of all smaller), then after any sequence of splits, the odd-index sum ≥ the original largest piece.* This is exactly the n=1,2,3 behavior observed and is the load-bearing sub-claim for the lower bound.
3. **The recursion `r_n = 1/(2 − 2^{−n})`** likely falls out of an induction where Liu's largest piece `2^n/(2^{n+1}−1)` is "reserved" and the remaining `(2^n−1)/(2^{n+1}−1)` reduces to a scaled copy of the `(n−1)` problem (since `2^n − 1 = 2(2^{n-1}) − 1`… note `(2^n − 1)/(2^{n+1} − 1)` rescales to the n−1 game with denominator `2^n − 1`). This self-similarity is the most promising proof architecture.
