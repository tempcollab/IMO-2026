# Lemma: universal-small-prime

## Status
CERTIFIED (round 1, proof-reviewer). For `n ≥ 2` the greedy rule requires `gcd(a_n, a_1) > 1` (a_1 is a past term when a_n is chosen), so a_n shares a prime of a_1; that prime divides `rad(a_1)` and is `≤ rad(a_1)`. Verified empirically.

## Statement
For the sequence defined by
```
a_1 > 1,   a_{n+1} = min{ m > a_n : gcd(m, a_i) > 1 for every i = 1, ..., n },
```
every term `a_n` (`n ≥ 1`) is divisible by at least one prime divisor of `a_1`. In particular, writing `R := rad(a_1)`, every `a_n` is divisible by a prime `p ≤ R`.

## Proof
For `n = 1`: every prime divisor of `a_1` divides `a_1` tautologically.
For `n ≥ 2`: the defining rule applied to `a_n` requires `gcd(a_n, a_1) > 1` (because `a_1` is among the past terms `{a_1, ..., a_{n-1}}` when `a_n` is chosen — concretely `a_n` is chosen at step `n-1` to hit every `a_i`, `i ≤ n-1`, which includes `a_1`). Hence `a_n` and `a_1` share at least one prime `p`. Every prime of `a_1` divides `R = rad(a_1)`, so `p | R`, and `p ≤ R`. ∎

## Notes
- Does NOT claim the set of all primes dividing some `a_n` is finite (it is not: large primes `> R` occur as free-riders, each alongside a prime of `a_1`).
- Does claim the *small* primes appearing are bounded: `S_0 := { p ≤ R : p prime, p | a_n for some n } ⊆ {primes ≤ R}`, a fixed finite set.

## Scope / reusability
Underpins the "fixed finite small-prime universe" used by every approach that builds a finite state on small primes. Cheap and unconditional.
