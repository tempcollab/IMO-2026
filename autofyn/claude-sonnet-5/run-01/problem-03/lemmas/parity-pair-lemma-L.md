# Lemma PARITY-PAIR and Lemma L (certified, round 5)

Source: `recursive-embedding-induction.md`, "Round 5: Lemma L proved in full,
by peel-the-top-block induction." Independently re-derived and verified by
the proof-reviewer (round 5): exhaustive enumeration for `n=1..8` (both the
constrained special case and the unconstrained general statement), 1,000,000+
exact-integer trials with zero violations, plus an independent from-scratch
re-derivation of the case-split recursion (`D = D'` when `c_1` even, `D = t_1
- D'` when `c_1` odd) verified against direct sorted-list recomputation
(24,000 exact-integer trials, zero mismatches).

## Setting

Fix `n ≥ 1`. Let `t_i := 2^{n-i}` for `i = 1, ..., n` (so `t_1 = 2^{n-1} >
t_2 > ... > t_n = 1`, each exactly twice the next). For nonnegative integers
`a_1, ..., a_n`, let `c_i := a_i + 1 ≥ 1` and let `m := Σ a_i`. Build the
sorted-descending list consisting of `n` blocks, block `i` being `c_i` copies
of `t_i` (in decreasing order of `i`). Define the alternating sum `D` of this
list, `D := Σ_{j} (-1)^{j+1} (\text{value at sorted position } j)`.

**Block formula (re-derived from scratch, not a black box).** Writing
`C_0 := 0`, `C_i := c_1 + ... + c_i`,
```
D = Σ_{i : c_i odd} (-1)^{C_{i-1}} t_i.
```
(A maximal run of `c` equal copies starting at position `p` contributes
`±t` to the alternating sum iff `c` is odd, with sign `(-1)^{p+1}`; even-length
runs cancel in pairs. Direct telescoping computation.)

## Lemma PARITY-PAIR

**Statement.** For every `n ≥ 1` and every choice of nonnegative integers
`a_1, ..., a_n` such that `n + m` is odd (`m = Σ a_i`, **no constraint on
`Σ a_i t_i` is needed**),
```
D ≥ t_n = 1.
```

**Proof (strong induction on `n`).**

*Base case `n = 1`.* `n + m` odd forces `a_1` even, so `c_1 = a_1 + 1` is
odd. Single block: `D = (-1)^0 t_1 = t_1 = 1 = t_n`. Equality.

*Inductive step, `n ≥ 2`.* Let `c_1 = a_1 + 1`. Let the "remainder" be blocks
`2, ..., n`, re-parametrized as their own level-`(n-1)` instance (`t'_j :=
t_{j+1} = 2^{(n-1)-j}`, `a'_j := a_{j+1}`, `m' := m - a_1`), with its own
fresh alternating sum `D'` (computed as if the remainder were the whole list).

- **Case A (`c_1` even, i.e. `a_1` odd).** Block 1 contributes `0` to `D`
  (even multiplicity). `C_1 = c_1` is even, so every remainder position's
  global sign equals its fresh-indexed sign: `D = D'`. Check
  `(n-1) + m' = (n+m) - 1 - a_1` = odd − 1 − odd = odd, so the IH applies at
  level `n-1`: `D' ≥ t'_{n-1} = t_n = 1`. Hence `D ≥ 1`.
- **Case B (`c_1` odd, i.e. `a_1` even).** Block 1 contributes `t_1` (sign
  `(-1)^0`). `C_1` is odd, so every remainder global sign is the *negative*
  of its fresh-indexed sign: `D = t_1 - D'`. The IH does **not** apply here
  (`(n-1)+m'` is even in this case) — instead bound `D' ≤ max(remainder) =
  t_2` by the already-certified Lemma D-BOUND (`0 ≤ D(Y) ≤ max(Y)`, see
  `lemmas/alternating-sum-toolkit.md`), valid since `n ≥ 2` guarantees the
  remainder is nonempty. So `D = t_1 - D' ≥ t_1 - t_2 = t_2 ≥ t_n = 1` (using
  `t_1 - t_2 = 2^{n-1}-2^{n-2}=2^{n-2}=t_2`, and `t_2 = 2^{n-2} ≥ 2^{n-n}=1`
  since `n ≥ 2`).

Both cases give `D ≥ 1`. ∎

## Lemma L (corollary)

**Statement.** For every `n ≥ 1` and every nonnegative-integer vector
`(a_1,...,a_n)` with `Σ a_i = n+1` (Lemma L's original cardinality
constraint; the value constraint `Σ a_i t_i = 2t_1` is *not* needed for this
conclusion — see remark), `D ≥ t_n = 1`, with equality attained by the
canonical vector `a_i = 1 (i<n), a_n = 2`.

**Proof.** Apply Lemma PARITY-PAIR with `m = n+1`: `n+m = 2n+1` is odd for
every `n`, so the hypothesis holds unconditionally. ∎

## What this closes (see approach files for full scope)

Combined with the already-certified Lemma V' (`alternating-sum-toolkit.md`),
this fully closes the "pure-anchor vertex" part of Proposition K's `k=n`,
tail-untouched sub-case, for every `n`. It does **not** close: the "one free
coordinate" vertex case of Lemma V' (open), the tail-refined `k<n` case
(open), or the upper bound (open).
