# Corollary 2 — `D = ∫ (N(t) mod 2) dt` (alternating sum as a parity integral)

**Source.** Certified from approach `tail-count` (round 1).

## Statement

For a multiset of piece lengths `ℓ_1 ≥ … ≥ ℓ_m` summing to `S`, with `N(t) = #{i : ℓ_i ≥ t}`,
the alternating sum `D = ℓ_1 − ℓ_2 + ℓ_3 − …` satisfies

$$D \;=\; \int_0^\infty \bigl(N(t) \bmod 2\bigr)\, dt.$$

## Proof

Using the identity `⌈N/2⌉ = N/2 + (N \bmod 2)/2` and Lemma 1 (`layer-cake-odd-index`):

$$\text{odd-index sum} \;=\; \int_0^\infty \left\lceil\frac{N(t)}{2}\right\rceil dt \;=\; \frac{1}{2}\int_0^\infty N(t)\,dt \;+\; \frac{1}{2}\int_0^\infty (N(t) \bmod 2)\,dt.$$

By the same Tonelli argument, `∫_0^∞ N(t)\,dt = \sum_i ℓ_i = S`. And
`odd-index sum = (S + D)/2` (Lemma 0). Substituting:

$$\frac{S + D}{2} \;=\; \frac{S}{2} + \frac{1}{2}\int_0^\infty (N(t)\bmod 2)\,dt,$$

so `D = ∫_0^∞ (N(t) mod 2) dt`. ∎

## Equivalent form

`N(t) mod 2 = 1` exactly on the intervals `(ℓ_{k+1}, ℓ_k]` with `k` odd, so
`D = (ℓ_1 − ℓ_2) + (ℓ_3 − ℓ_4) + …`, recovering the alternating sum directly.

## Caveat

This identity is an exact rewriting; it does **not** by itself prove the lower or upper
bound for the stick game, because the parities of `N(t)` at different thresholds are
**coupled** through the global sorted order (one Xiang mark re-sorts the whole list and
shifts parities on a long range of `t` simultaneously). It is a structural language, not
a solver.
