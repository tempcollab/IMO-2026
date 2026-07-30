# Lemma: bottom-dominant halving gives D = a_{n+1}

**Source:** `majorization-upper` Part IV, round 5. Standalone (no IH, no imports
beyond Lemma 0).

## Statement

For a Liu config `L = (a_1 ≥ a_2 ≥ … ≥ a_{n+1})` with `m = n+1` and
`a_n ≥ 2·a_{n+1}` ("bottom-dominant"), Xiang's strategy of halving the `n`
largest pieces (`a_1, …, a_n`) and leaving `a_{n+1}` unsplit uses `n` marks and
gives

```
D = a_{n+1}.
```

Hence `D*(L) ≤ a_{n+1}`.

## Proof

Xiang splits each `a_i` (`i = 1, …, n`) into `{a_i/2, a_i/2}`. This uses `n`
marks. The refined multiset is

```
M' = {a_1/2, a_1/2, a_2/2, a_2/2, …, a_n/2, a_n/2, a_{n+1}},
```

total `2n + 1` pieces.

**Sorted order.** Since `a_1 ≥ a_2 ≥ … ≥ a_n` (sorted), we have
`a_1/2 ≥ a_2/2 ≥ … ≥ a_n/2`. The bottom-dominant condition `a_n ≥ 2 a_{n+1}`
gives `a_n/2 ≥ a_{n+1}`. Hence the non-increasing sorted order of `M'` is
exactly

```
a_1/2, a_1/2, a_2/2, a_2/2, …, a_n/2, a_n/2, a_{n+1}.
```

(The two copies of each `a_i/2` are adjacent — they are equal, and
`a_i/2 ≥ a_{i+1}/2` so no value interposes. And `a_n/2 ≥ a_{n+1}` places
`a_{n+1}` last.)

**Alternating sum.** The pair `(a_i/2, a_i/2)` occupies positions `(2i−1, 2i)`:
position `2i−1` is odd (sign `+`), position `2i` is even (sign `−`).
Contribution: `+a_i/2 − a_i/2 = 0`. The residual `a_{n+1}` is at position
`2n+1` (odd, sign `+`). Contribution: `+a_{n+1}`.

```
D(M') = Σ_{i=1}^{n} 0 + a_{n+1} = a_{n+1}.
```

Since `D* ≤ D(any Xiang strategy) = D(M') = a_{n+1}`, we have
`D*(L) ≤ a_{n+1}`. ∎

**Mark budget.** `n` marks. ✓

## Corollary (dominant tower-tail)

For the tower-tail family `(a_1, 2^{n−1}, 2^{n−2}, …, 2, 1)/S` (geometric ratio
2 in the bottom `n` pieces, `S = a_1 + D_n − 1` the total), if `a_1 ≥ 2^n`
(dominant tower-tail, `S ≥ D_n`), then `D* ≤ a_{n+1} = 1/S ≤ 1/D_n`. The tower
`T_n` (`a_1 = 2^n`, `S = D_n`) is the tight member: `D* = 1/D_n` (by
`parallel-halving-saturates-tower`).

*Proof of corollary.* The tower-tail family satisfies `a_n = 2 ≥ 2·1 = 2 a_{n+1}`
(bottom-dominant, with equality). By the halving lemma, `D ≤ a_{n+1} = 1/S`.
For dominant tower-tail (`a_1 ≥ 2^n`), `S = a_1 + (2^n − 1) ≥ 2^n + (2^n − 1)
= D_n`, so `1/S ≤ 1/D_n`. ✓ For the tower itself (`a_1 = 2^n`, `S = D_n`),
`D* = 1/D_n` exactly (certified `parallel-halving-saturates-tower`). ∎

## When halving closes the case

For general bottom-dominant `m = n+1` configs, the halving lemma gives
`D* ≤ a_{n+1}`. This closes the case whenever `a_{n+1} ≤ 1/D_n` (equivalently,
`Σ_{i=1}^{n} a_i ≥ (D_n − 1)·a_{n+1} = 2(2^n − 1)·a_{n+1}`: the top `n` pieces
are "spread enough" relative to the tail). The dominant tower-tail family
attains this with equality at the tower; any config with a larger top (for
given `a_{n+1}`) is strict.

When `a_{n+1} > 1/D_n` (the halving bound exceeds the target), the halving bound
is an UPPER BOUND on `D*`; the actual `D*` may be smaller (the pair-matching
cascade, GAP-U2 in `majorization-upper` Part VII).

## Verification

Exact-`Fraction` check, 10000 random bottom-dominant strictly-decreasing configs
(`n = 1..6`), all give `D(halving) = a_{n+1}`. ✓

## Importable by

Any upper-bound approach needing the bottom-dominant `m = n+1` case. The halving
strategy is non-inductive (no `(n−1)`-target IH needed).
