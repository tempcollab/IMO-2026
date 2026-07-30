# Lemma SANDWICH (single-mark top-piece straddle, odd piece-count)

**Status:** proposed this round (round 6) by `minimax-mixed-duality`, verified
by the builder via 30,000 exact-`Fraction` randomized trials across
`m ∈ {3,5,7}` (zero mismatches) and proved in full below by the same
rank-shift bookkeeping technique used for the already-certified Lemma DOM /
Lemma SPLIT. **Not yet independently re-derived by the proof-reviewer** —
flagged for certification next round if the reviewer confirms it.

This lemma applies to **any** sorted list of positive reals with an **odd**
number of pieces (not just the geometric configuration `A_n`), and targets
the arbitrary-configuration upper bound `max_A min_B oddrank(B) ≤ c(n)`,
same family as Lemma DOM / Lemma HALVE / Lemma SPLIT / Lemma TAIL-SNIP.

## Statement

Let `A = (p_1 ≥ p_2 ≥ ⋯ ≥ p_m)` be a sorted list of positive reals with `m`
**odd**, `m ≥ 3`. Suppose
```
p_1 < p_2 + p_m.
```
Then using exactly **1 mark**, Xiang Yu can split `p_1` into two parts
`x, y = p_1 - x` with
```
x ∈ ( max(p_3, p_1 - p_m), p_2 ),
```
(a nonempty open interval precisely because `p_1 < p_2 + p_m` and `p_3 <
p_2`), and for **every** such `x` the resulting multiset
`B = {x, y} ∪ {p_2,...,p_m}` satisfies, **exactly**,
```
oddrank(B) = p_2 + p_3 + p_5 + p_7 + ⋯ + p_m   (p_2 plus all odd-indexed-from-3 tail terms, using m odd)
```
independent of the specific choice of `x` inside the interval. In
particular `oddrank(B) = oddrank(A) - (p_1 - p_2) ≤ oddrank(A)`, i.e. the
move is always a weak improvement (strict when `p_1 > p_2`).

## Proof

Fix `x` in the stated interval and set `y = p_1 - x`. By construction:
- `x < p_2` and `x > p_3`, so `x` sits strictly between `p_2` and `p_3`.
- `y = p_1 - x`; since `x > p_1 - p_m` we get `y < p_m`, and since `x < p_1`
  (as `x < p_2 ≤ p_1`) we get `y > 0`.

Hence the sorted order of `B` is exactly
```
p_2 (rank 1), x (rank 2), p_3 (rank 3), p_4 (rank 4), ..., p_m (rank m), y (rank m+1),
```
i.e. `p_i` sits at global rank `i` for every `i = 2,...,m` (unchanged from
its rank in the tail-only list), `x` is inserted at rank 2, and `y` is
inserted at the very bottom, rank `m+1`. Since `m` is odd, `m+1` is even, so
`y` is **excluded** from `oddrank(B)`. Reading off the odd ranks
`1,3,5,...,m` (note `m` itself is odd, so it is included):
```
oddrank(B) = p_2 (rank 1) + p_3 (rank 3) + p_5 (rank 5) + ⋯ + p_m (rank m),
```
which is exactly the claimed formula, and manifestly independent of the
precise value of `x` within the feasible interval (`x` itself sits at the
even rank 2 and never appears in the sum). ∎

**Comparison to `oddrank(A)`.** In `A`, `p_1` occupies rank 1 (odd) and
`p_i` occupies rank `i` for `i ≥ 2` (unaffected by `p_1`'s presence at rank
1), so `oddrank(A) = p_1 + p_3 + p_5 + ⋯ + p_m` (same odd-tail-sum `p_3 +
p_5 + ⋯`). Hence `oddrank(B) - oddrank(A) = p_2 - p_1 ≤ 0`, proving the move
never worsens the value, with equality only in the degenerate case `p_1 =
p_2`. ∎

## Relation to the existing menu (DOM / HALVE / TAIL-SNIP)

- **Not** a special case of Lemma DOM (which requires `p_1 ≥ Σ_{i≥2} p_i`,
  the *full* tail sum, a strictly stronger hypothesis than `p_1 < p_2+p_m`
  used here — in fact DOM's and SANDWICH's hypotheses are typically on
  *opposite* sides for `m ≥ 4`, since `p_2+p_m ≤ Σ_{i≥2}p_i`). SANDWICH is
  the first tool in this problem's toolkit whose feasibility condition
  depends on only **two** tail values (`p_2` and `p_m`), not the whole tail
  shape — a genuinely weaker, easier-to-satisfy hypothesis, verified to
  apply in regimes where Lemma DOM, Lemma HALVE, and Lemma TAIL-SNIP all
  individually fail (see the worked witness below).
- **Not** a special case of Lemma HALVE (`p_1 ≥ 2p_2`): SANDWICH's example
  witness below has `p_1 < 2p_2` (HALVE's hypothesis explicitly fails
  there), yet SANDWICH still applies and gives a strictly better value than
  the (inapplicable) HALVE formula would.
- **Genuinely beats Lemma TAIL-SNIP** on a previously-recorded hard
  witness: for `A = (4649,3042,2309)/10000` (`m=3`, the exact instance
  `split-and-tail-snip.md` used to prove TAIL-SNIP alone insufficient),
  `p_1 = 0.4649 < p_2+p_3 = 0.5351`, so SANDWICH applies and gives
  `oddrank(B) = p_2+p_3 = 0.5351` **exactly**, strictly better than
  TAIL-SNIP's `0.58035` and better than the (inapplicable) DOM/HALVE values
  — using only **1** of the 2 available marks. (`split-and-tail-snip.md`'s
  own note that this witness "needs a coordinated simultaneous split of two
  pieces at jointly-optimized non-half ratios" is thereby **superseded**:
  a single clean 1-mark closed-form construction suffices here after all —
  the two-piece coordination it found was real but not load-bearing; a
  simpler single-piece move works too, once positioned correctly.)

## What is NOT established

- **Even `m` is not covered.** The same "straddle p_1 across (p_2,p_3)"
  construction was tested for even `m` and found, on the boundary
  `x → p_2⁻`, to degenerate to no improvement (`oddrank(B) → oddrank(A)`)
  in every case checked — but this was only checked in a regime where the
  feasibility precondition `y < p_m` (needed for the claimed rank
  ordering) was **not** verified to hold, so no reliable claim (positive or
  negative) is made here for even `m`; it is open.
- **This lemma alone does not close the general upper bound.** A direct
  numeric sweep over `m=3` (`n=2`-relevant) configurations shows the
  4-candidate menu `{DOM, HALVE, TAIL-SNIP, SANDWICH}` (each applied
  wherever its hypothesis fires, taking the best) still leaves roughly a
  quarter of the sampled configuration space uncovered (`min` of the
  applicable candidates `> c(2)`); spot-checking several of those
  uncovered points against the true numeric optimum (via unconstrained
  search over all `≤2`-mark responses) confirms the true optimum **is**
  `≤ c(2)` there, achieved instead by a 2-mark construction (splitting
  `p_1` alone into 3 parts, or splitting `p_1` and `p_2` jointly) not
  captured by any lemma in the current menu. So SANDWICH is a genuine,
  verified **addition** to the shared candidate toolkit, not a replacement
  for the still-open general casework.
