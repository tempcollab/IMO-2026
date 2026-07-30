# Lemma R — the conjectured closed form (algebraic recursion)

**Source.** Certified from approach `d-potential` (round 1). Pure algebra.

## Statement

Define `r_n := 2^n / (2^{n+1} − 1)` (the conjectured value `c(n)`) and
`Δ_n := 2^{n+1} − 1`, equivalently `D_n := 1/Δ_n` (the target alternating sum). Then

$$\frac{1}{r_n} \;=\; 1 + \frac{1}{2\,r_{n-1}} \qquad (n \ge 1, \; r_0 := 1),$$

and equivalently `1/D_n = 2/D_{n−1} + 1`. Unwinding gives the closed form

$$r_n \;=\; \frac{2^n}{2^{n+1}-1}, \qquad \frac{1}{r_n} = 2 - 2^{-n} = \sum_{k=0}^{n} 2^{-k}.$$

## Proof

Algebra:

$$1 + \frac{1}{2 r_{n-1}} = 1 + \frac{\Delta_{n-1}}{2^n} = 1 + \frac{2^n - 1}{2^n} = \frac{2^{n+1}-1}{2^n} = \frac{\Delta_n}{2^n} = \frac{1}{r_n}.$$

Unwinding: `1/r_n = 1 + 1/2 + 1/4 + … + 1/2^n = 2 − 2^{−n}`, hence `r_n = 1/(2 − 2^{−n}) = 2^n/(2^{n+1} − 1)`. ∎

## Verification (n=1,2,3,4)

| n | r_n | D_n |
|---|-----|-----|
| 1 | 2/3 | 1/3 |
| 2 | 4/7 | 1/7 |
| 3 | 8/15 | 1/15 |
| 4 | 16/31 | 1/31 |

## Caveat

This lemma is an **algebraic identity about the candidate closed form**, not a proof that
the game value `c(n)` satisfies the recursion. Proving `c(n) = r_n` requires both the
lower bound (Liu's tower guarantees `≥ r_n`) and the upper bound (Xiang caps Liu at
`≤ r_n`); both are open beyond `n=1`.
