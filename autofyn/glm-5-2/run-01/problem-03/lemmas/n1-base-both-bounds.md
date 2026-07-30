# Lemma — `n=1` base case, both bounds: `c(1) = 2/3`

**Source.** Certified from approaches `tail-count`, `d-potential`, `tower-induction`
(round 1; all three prove it by hand).

## Statement

For `n=1`, the value of the Liu Bang / Xiang Yu stick game is `c(1) = 2/3`. That is:
Liu has a 1-mark strategy guaranteeing a take `≥ 2/3`, and Xiang has a 1-mark strategy
holding Liu's take `≤ 2/3` against every Liu config.

## Proof

Recall (Lemma 0, `claim-game-odd-index`) that for a sorted multiset Liu's optimal take
is the odd-index sum.

### Lower bound: Liu `≥ 2/3`

Liu plays the tower `T_1 = (2/3, 1/3)`. Xiang has `≤ 1` mark.

- *0 marks:* multiset `(2/3, 1/3)`; odd-index = `2/3`. ✓
- *Split the `2/3` piece* into `p + (2/3 − p)`, `p ≥ 1/3`. Then `2/3 − p ≤ 1/3 ≤ p`, so
  sorted = `(p, 1/3, 2/3−p)` and odd-index = `p + (2/3 − p) = 2/3`. ✓ (equality)
- *Split the `1/3` piece* into `q + (1/3 − q)`, `q ≥ 1/6`. Sorted
  `(2/3, q, 1/3−q)`; odd-index = `2/3 + (1/3 − q) = 1 − q ≥ 1 − 1/3 = 2/3` (since `q ≤ 1/3`). ✓

So Liu `≥ 2/3` in every case. ✓

### Upper bound: Xiang `≤ 2/3`

Liu's config has `≤ 2` pieces summing to 1; write it `{a, 1−a}` with `a ≥ 1/2` (or a
single piece `a=1`).

- *Liu plays one piece* (`a=1`): Xiang splits it into halves `{1/2, 1/2}`; odd-index
  `= 1/2 ≤ 2/3`. ✓
- *Two pieces `{a, 1−a}`, `a ≥ 2/3` (dominant):* Xiang splits `a` into halves
  `{a/2, a/2}`. Since `a ≥ 2/3`, `a/2 ≥ 1/3 ≥ 1−a`, so sorted = `(a/2, a/2, 1−a)` and
  odd-index `= a/2 + (1−a) = 1 − a/2 ≤ 1 − 1/3 = 2/3`. ✓
- *Two pieces, `a < 2/3` (non-dominant):* Xiang marks nothing. Odd-index `= a < 2/3`. ✓

So Xiang holds Liu `≤ 2/3` against every config. ✓

Combined: `c(1) = 2/3`. ∎

## Use

This is the base case for any inductive approach to the general bound
`c(n) = 2^n/(2^{n+1}−1)`.
