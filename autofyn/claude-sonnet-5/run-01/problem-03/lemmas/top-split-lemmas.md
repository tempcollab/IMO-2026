# Lemmas: super-increasing structure and the single-mark top-split bound

**Status:** certified (round 2). Source: `geometric-dominance-construction.md`
(Lemma S, evenrank reformulation, Lemma F1). Reviewer independently verified
Lemma S by direct algebra and Lemma F1 by exhaustive exact-`Fraction` random
search (500 trials per `n`, `n=1..6`, `a` ranging uniformly over `[0,p_1/2]`) —
no violation found; matches the closed-form proof below.

## Setup

Fix `n ≥ 1`, `D := 2^{n+1}-1`, `p_i := 2^{n+1-i}/D` for `i=1,...,n+1`
(the geometric configuration `A_n`, as in `geometric-configuration-facts.md`).
Write `T_0 := {p_2,...,p_{n+1}}` for the tail.

## Lemma S (universal super-increasing identity)

For every `i = 1,...,n+1` (empty sum convention: sum is `0` past the end),
`p_i = Σ_{j=i+1}^{n+1} p_j + 1/D`.

*Proof.* `Σ_{j=i+1}^{n+1} p_j = Σ_{l=0}^{n-i} 2^l/D = (2^{n-i+1}-1)/D` (finite
geometric series, substituting `l=n+1-j`). So
`p_i - Σ_{j>i}p_j = 2^{n+1-i}/D - (2^{n+1-i}-1)/D = 1/D`. ∎

This strictly generalizes Lemma 2 of `geometric-configuration-facts.md`
(the `i=1` instance) to every truncation level, with the same uniform margin.

## Evenrank reformulation (trivial bookkeeping fact)

For any refinement `B` of `A_n` (any number of cuts), `oddrank(B) ≥ p_1`
if and only if `evenrank(B) ≤ 1-p_1 = Σ(T_0)`.

*Proof.* `oddrank(B)+evenrank(B) = Σ(B) = 1` since cutting preserves total
length and every element sits at exactly one rank. So
`oddrank(B) ≥ p_1 ⟺ 1-evenrank(B) ≥ p_1 ⟺ evenrank(B) ≤ 1-p_1`. ∎

## Lemma F1 (single-mark top-split lower bound, tail untouched, all `n`)

Fix `n ≥ 1`. Suppose Xiang Yu spends exactly one mark splitting `p_1` into
two parts `x ≥ a ≥ 0` (`x+a=p_1`) and leaves every piece of `T_0` untouched.
Then for **every** `a ∈ [0, p_1/2]`, `oddrank({x,a} ∪ T_0) ≥ p_1 = c(n)`.

*Proof.* `x = p_1-a ≥ p_1/2 = p_2 ≥` every element of `T_0`, so `x` is a
maximum of `{x,a}∪T_0` and can be placed at rank 1; the rest of the sorted
list is the sorted merge of `T_0` with the single value `a`. By the
rank-shift argument (prepending a dominant max shifts all subsequent ranks
up by one, flipping parity),
`oddrank({x,a}∪T_0) = x + evenrank(T_0 ∪ {a})`,
so it suffices to show `evenrank(T_0∪{a}) ≥ a` for `a ∈ [0,p_2]`.

Let `j := #{i : p_{i+1} ≥ a}` (ties broken toward inclusion); inserting `a`
into the sorted tail places it at position `j+1`.

- **`j` odd:** position `j+1` is even, so `a` itself is one of the terms of
  `evenrank(T_0∪{a})`; since every other term is nonnegative,
  `evenrank(T_0∪{a}) ≥ a` immediately (true for *any* tail multiset, not
  just the geometric one).
- **`j` even:** let `m=j+1` (odd). Then `a ≤ p_m` (by definition of `m`
  as the smallest tail element `≥ a`, or the boundary `m=n+1`). The merged
  list is `(p_2,...,p_m,a,p_{m+1},...,p_{n+1})`; since `m` is odd, `a` sits at
  an odd position and does not contribute to `evenrank`, and direct position
  tracking gives
  `evenrank(T_0∪{a}) = (p_3+p_5+⋯+p_m) + (p_{m+1}+p_{m+3}+⋯)`,
  a sum of nonnegative terms including `p_m` itself (with the boundary
  sub-case `m=n+1` handled identically, giving `evenrank(T_0) ∋ p_{n+1}`).
  Hence `evenrank(T_0∪{a}) ≥ p_m ≥ a`.

Both cases give `evenrank(T_0∪{a}) ≥ a`, hence `oddrank({x,a}∪T_0) ≥ p_1`. ∎

## What remains open (not part of this certified lemma set)

Lemma F1 settles only `k=1`, tail completely untouched. It does **not**
cover `k=1` with the tail simultaneously refined (refuted by an explicit
counterexample — see `merge-by-sums-counterexample.md`), nor `k ≥ 2` in
general (a "doubling family" of splits is numerically observed to be optimal
but not proved to be the true minimizer over all compositions). This is the
shared open gap of `geometric-dominance-construction.md`,
`recursive-embedding-induction.md`, and (for the arbitrary-configuration
upper bound) `universal-adversary-strategy.md`.
