# Lemma: bounded-difference

## Status
CERTIFIED (round 1, proof-reviewer). Independently re-derived and verified numerically for `a_1 ∈ {15,35,77,135,175,187,221,6,9,25,33,45,105,385,91}`: `max(a_{n+1}-a_n) ≤ rad(a_1)` in every case. The candidate `M = R·⌈(a_n+1)/R⌉` is the next multiple of `rad(a_1)` after `a_n` and is admissible because every past term shares a prime of `a_1` with `M`. Non-circular: uses the greedy rule only on past terms.

## Statement
Let `a_1, a_2, ...` be the sequence defined by `a_1 > 1` integer and
```
a_{n+1} = min{ m > a_n : gcd(m, a_i) > 1 for every i = 1, ..., n }.   (★)
```
Let `R := rad(a_1) := ∏_{p | a_1} p` (squarefree product of the distinct primes dividing `a_1`). Then
```
a_{n+1} - a_n ≤ R   for every n ≥ 1.
```

## Proof
Fix `n ≥ 1`. Each past term `a_i` (`i ≤ n`) shares a prime with `a_1`: for `i = 1` tautologically; for `i ≥ 2`, rule (★) gives `gcd(a_i, a_1) > 1`. Let
```
M := R · ⌈(a_n + 1)/R⌉
```
be the smallest multiple of `R` strictly greater than `a_n`. Then `a_n < M ≤ a_n + R`. Since `R` is divisible by every prime of `a_1`, so is `M`. For any past term `a_i`, pick `p ∈ supp(a_i) ∩ supp(a_1)` (nonempty by the observation above); then `p | a_i` and `p | M`, so `gcd(M, a_i) ≥ p > 1`. Hence `M` is an admissible candidate (`M > a_n` and hits every `a_i`, `i ≤ n`), and by the minimality in (★),
```
a_{n+1} ≤ M ≤ a_n + R.
```
Thus `a_{n+1} - a_n ≤ R`. ∎

## Notes
- The candidate is the next **multiple** of `R`, not `a_n + R` (which need not be a multiple of `R`).
- Non-circular: (★) is used only on *past* terms, never on the term being defined.
- This bounds the gap by a constant (`R`) depending only on `a_1`, the foundational input for any finite-state / pigeonhole argument on the sequence.

## Scope / reusability
Reusable by every approach to `imo-2026-06` that needs a uniform gap bound. Does not depend on any unproved hypothesis.
