# Approach: dyadic-recursion-induction

## Status
unsolved

## Approaches tried
- (round 1) Skeleton laid down; no step reviewer-certified yet. Anchors: c(1) = 2/3 proved by hand (explorer, round 1); c(2) = 4/7, c(3) = 8/15 confirmed numerically to high precision; the recursion identity c(n) = c(n)/2 + c(n-1)(1 - c(n)) verified exactly in rationals for n ≤ 7.

## Current best
Nothing certified yet. The exact identities below are algebraically verified (rational arithmetic), and the n = 1 case has a hand proof in the round-1 explorer reports.

---

## Target (the whole claim)

**Answer: c(n) = 2^n / (2^{n+1} − 1).** Equivalently c(n) = 1/2 + 1/(2(2^{n+1}−1)). Both directions proved: Liu Bang has a strategy guaranteeing ≥ c(n), and Xiang Yu has a reply capping Liu Bang at ≤ c(n) (or ≤ c(n)+ε for every ε > 0, which suffices) against every Liu Bang placement.

## Framing

Induction on n, driven by a case split on the largest piece a1 of Liu Bang's partition. The engine is the exact recursion c(n) = c(n)/2 + c(n−1)(1 − c(n)): "Xiang Yu neutralizes the top of the sorted vector with one or all of his cuts, and the tail is a scaled (n−1)-instance."

## Skeleton

**Step 0 (shared lemma; propose for `lemmas/`). Greedy-claiming lemma.** In the claiming subgame on a fixed multiset a1 ≥ a2 ≥ … ≥ am (players alternate, each takes any remaining piece, each maximizes own total), optimal play for both is "take the current largest," so the first mover's optimal total is the odd-rank sum a1 + a3 + a5 + …
*Mechanism:* induction on m with an exchange argument — replacing a non-greedy pick by the current maximum never hurts the mover and never helps the opponent. GAP G0 (expected easy but must be written rigorously — the exchange must handle the opponent's changed subsequent options).

**Step 1. Reduction to a Stackelberg multiset game.** Only piece *sizes* matter: Liu Bang chooses a partition of 1 into k ≤ n+1 positive parts a1 ≥ … ≥ ak; Xiang Yu then refines it with ≤ n further cuts (a cut splits one part into two positive parts); Liu Bang's payoff is the odd-rank sum of the final sorted multiset. Physical positions on the stick are irrelevant because any desired split of any piece is realizable by a mark inside that piece (marks distinct from Liu's is a non-issue: a coincidence would mean the split already exists). By Step 0 this is exactly the original game's value.

**Step 2. Pair-collapse lemma.** If the sorted multiset is (p, p, b1, b2, …) with p ≥ b1, then odd-rank-sum = p + odd-rank-sum(b1, b2, …).
*Mechanism:* deleting a matched adjacent pair shifts all later ranks by 2, preserving parity. One line, but load-bearing for the whole recursion.

**Step 3. Lower bound (Liu Bang's construction).** Liu Bang plays the dyadic ladder D_n: pieces (2^n, 2^{n−1}, …, 2, 1)/(2^{n+1}−1). Claim: **every** refinement of D_n by ≤ n cuts has odd-rank sum ≥ c(n).
*Mechanism (to be proved — GAP G1):* induction on n using the super-increasing property (each rung strictly exceeds the sum of all smaller rungs, by exactly one unit 1/(2^{n+1}−1)). Case on the number j of Xiang cuts landing inside the top rung 2^n:
  - j = 0: the top rung is the unique largest final piece; Liu takes it (2^n units ≥ c(n)·(2^{n+1}−1) units), done immediately.
  - j ≥ 1: the top rung splits into j+1 sub-pieces summing to 2^n = (sum of all other rungs) + 1 unit; pair Liu's picks against Xiang's picks and recurse on the (n−1)-ladder formed by the untouched rungs with the remaining n−j cuts. The unit surplus survives every pairing, giving Liu ≥ 1/2 + (1 unit)/2.
  The reference computation (mirror-ladder reply, algebraically verified in round 1) shows this bound is tight, so no slack is available — the induction must be exact.

**Step 4. Upper bound (Xiang Yu's reply), strong induction on n.** For ANY Liu partition a1 ≥ … ≥ ak (k ≤ n+1), Xiang Yu caps Liu at ≤ c(n) (ε-approximately is enough). Base n = 1 is the hand-proved c(1) = 2/3. Inductive step, cases on a1, a2:
  - **Case A: a1 ≥ c(n) and a2 ≤ a1/2 — bisect the top.** Xiang bisects a1. The two halves a1/2 ≥ a2 form the top matched pair; by Step 2 and induction (the tail a2,…,ak is a partition of 1−a1 into ≤ n parts refined by Xiang's remaining n−1 cuts, i.e. a scaled (n−1)-instance), Liu ≤ a1/2 + c(n−1)(1−a1). This is **decreasing in a1** (since c(n−1) > 1/2) and at a1 = c(n) equals exactly c(n) by the verified identity c(n−1)(1−c(n)) = c(n)/2. Hence ≤ c(n).
  - **Case B: a2 ≥ c(n)/2 — shave the top to match.** Xiang cuts a1 into {a2, a1−a2} (valid: a1 ≥ a2; the pair (a2,a2) is on top provided a1−a2 ≤ a2, i.e. a1 ≤ 2a2 — when a1 > 2a2 we are in Case A instead, since a1 > 2a2 ≥ c(n) requires checking a1 ≥ c(n): if a1 < c(n) and a1 > 2a2 then a2 < c(n)/2, contradiction — so Cases A/B genuinely cover a2 ≥ c(n)/2 together with a1 ≥ c(n)). Then Liu ≤ a2 + c(n−1)(1−2a2), decreasing in a2 (since 2c(n−1) > 1), equal to c(n) at a2 = c(n)/2 by the same identity. Hence ≤ c(n).
  - **Case C: 1/2 ≤ a1 < c(n) — duplicate-and-remainder.** Xiang spends k−1 ≤ n cuts inside a1 making exact copies of a2, …, ak plus remainder r = 2a1 − 1 ≥ 0. Claim: the odd-rank sum is then exactly a1 < c(n). *Mechanism:* every value a2,…,ak occurs as a matched pair; repeatedly applying Step 2 from the top, Liu collects one member of each pair down to where r ranks, and the total telescopes to (1−a1) + r = a1 (verified by hand for n = 2 in round 1; the general bookkeeping when r interleaves the pairs is a sub-gap of G2).
  - **Case D (the hard residual case — GAP G2): a1 < 1/2 and a2 < c(n)/2.** Neither trick applies verbatim. Candidate resolution: prove the **strengthened claim** C(m): "against any partition into k ≤ m+1 parts, Xiang with m cuts caps Liu at max(a1, 1/2 + a1/2^{m+1})" — verified exactly consistent at the dyadic optimum (1/2 + c(n)/2^{n+1} = c(n), checked in rationals for n ≤ 7) and at the n = 1 closed form. The strengthened form gives the induction room precisely where the naive bound (≤ c(n−1) on the tail) is too lossy for small a1. Since a1 ≤ c(n) in Case D, C(n) yields the cap ≤ c(n).

**Step 5. Combine.** Steps 3 and 4 give c(n) = 2^n/(2^{n+1}−1); verify the answer at n = 1 (2/3, hand-proved) and consistency with the trivial bound Liu ≥ 1/2 (pairing a_{2i−1} ≥ a_{2i} termwise).

## Open gaps
- **G0**: rigorous exchange-argument proof of the greedy-claiming lemma (Step 0).
- **G1**: the lower-bound induction (Step 3) — the exact accounting of Xiang cuts across ladder rungs.
- **G2**: Case D of the upper bound — prove the strengthened claim C(m) (or another mechanism) for a1 < 1/2, a2 < c(n)/2; plus the remainder-interleaving bookkeeping in Case C.

## Cases to cover
Upper bound: A/B/C/D as above (proved above that they exhaust all (a1, a2)); also k < n+1 (Liu uses fewer marks) and Xiang using fewer than n cuts (allowed; upper-bound strategy may waste cuts by ε-splitting a corner — note ε-argument). Lower bound: all distributions of Xiang's j ≤ n cuts among the n+1 rungs.

## Watch out for
- Exact ties in the sorted order (equal pieces): harmless for odd-rank sums but the pair-collapse lemma must state its tie-breaking convention.
- ε-issues: Xiang may need exact equalities (copies); exact placement is available, but if a proof step prefers strict inequalities, use cuts within ε and conclude "Liu cannot guarantee more than c(n) + ε for all ε," which suffices for the upper bound.
- The subgame in Cases A/B is "a partition into ≤ n parts chosen by Liu *before* seeing Xiang's cuts" — same order of moves as the (n−1)-game, so the induction is legitimate; say this explicitly.
- Do NOT let the tail bound c(n−1)(·) be applied when the top pair condition (p ≥ every tail piece) fails — re-sort first.
