# Lemma: repeated value in m = n+1 config ⟹ D* = 0

**Source:** `majorization-upper` Part V, round 5. Uses certified
`spine-pair-cancellation` (S1) and the even-multiplicity lemma from
`m-le-n-halving-D-zero`.

## Statement

For a Liu config `L = (a_1 ≥ a_2 ≥ … ≥ a_{n+1})` with `m = n+1` and at least
one repeated value (`a_i = a_{i+1}` for some `i`), Xiang has `≤ n` marks
forcing `D = 0`. Hence `D*(L) = 0 ≤ 1/D_n`.

## Proof

By `spine-pair-cancellation` (S1, certified), for any sorted multiset `M`,
removing all adjacent-equal pairs preserves `D`: `D(M) = D(spine(M))`, where the
spine is the strictly-decreasing subsequence (all adjacent-equal pairs removed).

Since `L` has at least one repeated value (`a_i = a_{i+1}` for some `i`), the
spine of `L` has `m' ≤ n` pieces (we removed at least one pair from `n+1`
pieces, leaving `≤ n−1`; further pairs may be removed, only reducing the
count). In fact `m' ≤ n − 1 ≤ n`.

**Xiang's strategy: halve every spine piece.** Xiang identifies the spine
(strictly-decreasing subsequence) and halves each spine piece `s_j` into
`{s_j/2, s_j/2}`, using `m' ≤ n−1 ≤ n` marks. The paired pieces (the removed
duplicates) are left unsplit.

**Claim.** In the refined multiset `M'`, every value appears an even number of
times.

*Proof of claim.* The refined multiset `M'` consists of:
- For each spine piece `s_j`: two copies of `s_j/2` (the halves).
- For each pair-group value `v` (the removed adjacent-equal pairs): `2p`
  copies of `v`, where `p ≥ 1` is the number of pairs removed with value `v`
  (even).

Consider any value `w` in `M'`:
- If `w = s_j/2` for some spine piece `s_j` (and `w ≠ v` for any pair-group
  value `v`): the group is `{w}` with 2 copies (from halving `s_j`). Since the
  spine is strictly decreasing, the `s_j` are all distinct, so `s_j/2` are all
  distinct: no other spine piece contributes `w`. Size 2 (even). ✓
- If `w = v` for some pair-group value `v` (and `w ≠ s_j/2` for all `j`): the
  group has `2p` copies (even). ✓
- If `w = s_j/2 = v` for some `j` and some pair-group value `v`: the groups
  merge, giving `2 + 2p` copies (even). ✓
- If `w = s_j/2 = s_k/2` for `j ≠ k`: impossible, since `s_j ≠ s_k` (spine
  strictly decreasing) `⟹ s_j/2 ≠ s_k/2`.

In all cases, the group size is even. ∎ (claim)

By the even-multiplicity lemma (from `m-le-n-halving-D-zero`), `D(M') = 0`.
Since `D(M') = D(spine(M'))` by S1 (all pairs cancel in the refined config
too), and `D*(L) ≤ D(M') = 0`, and `D ≥ 0` always (for non-increasing
multisets), we have `D*(L) = 0`. ∎

**Mark budget.** `m' ≤ n − 1 ≤ n` marks. ✓

## Verification

Exact-`Fraction` check, 10000 random configs with `m = n+1` and at least one
repeated value (`n = 2..6`), all give `D = 0` after halving the spine. ✓

## Importable by

Any upper-bound approach needing the repeated-value sub-case of `m = n+1`
closed for all `n`. The remaining open case (strictly-decreasing `m = n+1`
where halving exceeds target or doesn't apply) is GAP-U2 in
`majorization-upper` Part VII.
