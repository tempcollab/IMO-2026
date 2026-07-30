# Lemma: m ≤ n ⟹ D* = 0 (halving all pieces)

**Source:** `majorization-upper` Part III, round 5. Standalone (no IH, no imports
beyond Lemma 0).

## Statement

For any Liu config `L = (a_1 ≥ a_2 ≥ … ≥ a_m)` with `m ≤ n` pieces (summing to
1), Xiang Yu has `≤ n` marks forcing `D = 0` (the alternating sum of the sorted
refined multiset). Hence `D*(L) = 0 ≤ 1/D_n`.

## Proof

Xiang halves every piece: for each `i = 1, …, m`, split `a_i` into
`{a_i/2, a_i/2}`. This uses `m ≤ n` marks. The refined multiset is

```
M' = {a_1/2, a_1/2, a_2/2, a_2/2, …, a_m/2, a_m/2}.
```

**Even-multiplicity lemma.** If every distinct value in a sorted (non-increasing)
multiset appears an even number of times, then `D = 0`.

*Proof of lemma.* Sort the multiset non-increasingly. Group consecutive equal
values into blocks. Each block has even size `2k` (by hypothesis). A block of
`2k` equal values `v` at positions `p, p+1, …, p+2k−1` contributes

```
v · Σ_{j=0}^{2k−1} sign(p+j),
```

where `sign(i) = +` for odd `i`, `−` for even `i`. Over `2k` consecutive
positions, the signs alternate, giving exactly `k` pluses and `k` minuses
(regardless of starting parity, since `2k` is even). The contribution is
`v · (k − k) = 0`. Summing over all blocks, `D = 0`. ∎

**Application.** In `M'`, each value `v = a_i/2` appears exactly
`2 ×` (multiplicity of `a_i` in `L`) times — an even number. (If `a_i = a_j`
for `i ≠ j`, their copies merge into a group of size `2 ×` (combined
multiplicity), still even.) Hence every value in `M'` appears an even number of
times. By the even-multiplicity lemma, `D(M') = 0`.

Since Xiang achieves `D = 0 ≤ 1/D_n` (as `1/D_n > 0`), we have `D*(L) ≤ 0`. But
`D ≥ 0` for any non-increasing multiset (since `a_{2k−1} ≥ a_{2k}` for all `k`),
so `D*(L) = 0`. ∎

**Mark budget.** `m` marks, `m ≤ n`. ✓

## Verification

Exact-`Fraction` check, 10000 random trials (`n = 1..6`, random configs with
`m ≤ n`), all give `D = 0` after halving every piece. ✓

## Importable by

Any upper-bound approach needing the `m ≤ n` case closed for all `n`. The
even-multiplicity lemma is also used by `repeated-value-D-zero` (halving the
spine).
