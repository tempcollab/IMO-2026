# Lemmas: facts about the geometric configuration `A_n`

**Status:** certified (round 1). Source: `geometric-dominance-construction.md`
(Lemma 2, Proposition A) and `recursive-embedding-induction.md` (Lemma 2,
Lemma 3, Proposition 4) — statements agree where they overlap. Reviewer
independently verified Proposition 4 by exact `Fraction` computation for
`n = 1,...,6` (all matched `c(n)` exactly) and separately verified numerically
(via `scipy.optimize.differential_evolution` over all ways of distributing
Xiang Yu's marks among the pieces, with exact split points as free variables)
that `min_B oddrank(B) = c(n)` for the geometric configuration at `n = 2` and
`n = 3` — i.e. no tested adversary response beats `c(n)`, consistent with
(but not a substitute for) the still-open general lower bound.

## Setup

Fix `n ≥ 1`, `D := 2^{n+1}-1`, and `p_i := 2^{n+1-i}/D` for `i = 1,...,n+1`,
so `p_1 > p_2 > ... > p_{n+1} > 0` and `Σ p_i = 1` (finite geometric series
`Σ_{i=1}^{n+1} 2^{n+1-i} = 2^{n+1}-1 = D`). Write `A_n = {p_1,...,p_{n+1}}`
and `c(n) := p_1 = 2^n/D`.

## Lemma 2 (top-piece domination)

`p_1 > p_2 + p_3 + ⋯ + p_{n+1}`; precisely, `p_1 - Σ_{i≥2} p_i = 1/D`, and
`p_1 = Σ_{i=2}^{n+1} p_i + p_{n+1}` (identity `(∗)`).

*Proof.* `Σ_{i=2}^{n+1} p_i = 1 - p_1 = (D - 2^n)/D = (2^n-1)/D`, so
`p_1 - Σ_{i≥2}p_i = (2^n - (2^n-1))/D = 1/D > 0`. Identity `(∗)`:
`(2^n-1)/D + 1/D = 2^n/D = p_1`, since `p_{n+1} = 1/D`. ∎

## Lemma 3 (self-similarity)

Let `λ_n := Σ_{i=2}^{n+1} p_i = (2^n-1)/D = 1 - c(n)`. Then the tail
`{p_2,...,p_{n+1}}` of `A_n` equals `λ_n · A_{n-1}` termwise:
`p_{i+1} = λ_n · p'_i` for `i=1,...,n`, where `p'_i := 2^{n-i}/(2^n-1)` is the
`i`-th piece of the level-`(n-1)` geometric configuration.

*Proof.* Direct computation: `λ_n p'_i = (2^n-1)/D · 2^{n-i}/(2^n-1) =
2^{n-i}/D = p_{i+1}`. ∎

## Proposition A (lower bound, top-untouched sub-case)

If Xiang Yu's `≤ n` marks are placed only inside pieces of the tail
`T_0 = {p_2,...,p_{n+1}}` (none strictly inside `p_1`), producing a
refinement `T` of `T_0` (any size, any distribution of cuts, `Σ(T) = Σ(T_0)`),
and `B = {p_1} ∪ T`, then `oddrank(B) ≥ p_1 = c(n)`.

*Proof.* Every element of `T` is nonnegative, so no element of `T` exceeds
`Σ(T) = Σ(T_0) < p_1` (Lemma 2). Hence `p_1` strictly exceeds every element
of `T`, so `p_1` is the unique maximum of `B`, occupying rank 1. Sorting `T`
descending as `t_1 ≥ ⋯ ≥ t_r`, `B`'s sorted list is `(p_1, t_1,...,t_r)`, so
`B`'s rank-`(j+1)` element is `T`'s rank-`j` element for all `j`; ranks shift
by exactly one, flipping parity. Hence
`oddrank(B) = p_1 + (t_2+t_4+⋯) = p_1 + evensum(T) ≥ p_1`,
since `evensum(T) ≥ 0` (sum of nonnegative reals). ∎

## Proposition 4 (exact-equality construction, general `n`)

For every `n ≥ 1`, Xiang Yu has a response to `A_n` using exactly `n` marks
that achieves `oddrank(B) = c(n)` exactly: split `p_1` into the `n+1` parts
`q_i = p_{i+1}` (`i=1,...,n`), `q_{n+1} = p_{n+1}` (valid by identity `(∗)`),
merge with the untouched tail `{p_2,...,p_{n+1}}`. The merged multiset has
each of `p_2,...,p_n` appearing twice and `p_{n+1}` appearing three times;
sorted descending, the odd positions land exactly on one copy each of
`p_2,...,p_n` plus two copies of `p_{n+1}`, giving
`oddrank(B) = (Σ_{i=2}^n p_i) + 2p_{n+1} = (p_1 - 2p_{n+1}) + 2p_{n+1} = p_1 = c(n)`
(using `Σ_{i=2}^n p_i = Σ_{i=2}^{n+1}p_i - p_{n+1} = (p_1-p_{n+1})-p_{n+1}` from
`(∗)`). Hence `min_B oddrank(B) ≤ c(n)` for `A = A_n`, for every `n`.

*Reviewer verification:* re-computed exactly (Python `fractions.Fraction`)
for `n = 1,...,6`; matches `c(n) = 2^n/(2^{n+1}-1)` in every case.

## What remains open (not part of this certified lemma set)

The reverse inequality `oddrank(B) ≥ c(n)` for *every* Xiang-Yu response `B`
against `A_n` (needed to conclude `min_B oddrank(B) = c(n)` exactly, i.e. that
`A_n` is not merely an upper witness but the true minimax value) is proved
above only in the `k=0` sub-case (Proposition A: no marks touch `p_1`). The
general sub-case (`k ≥ 1` marks touch `p_1`, possibly together with further
splitting of the tail) is **open** — this is the shared central gap of both
`geometric-dominance-construction.md` and `recursive-embedding-induction.md`.
Likewise, the upper bound over *all* Liu Bang configurations (not just `A_n`)
— i.e. `max_A min_B oddrank(B) ≤ c(n)` — has not been attempted by either
approach yet.
