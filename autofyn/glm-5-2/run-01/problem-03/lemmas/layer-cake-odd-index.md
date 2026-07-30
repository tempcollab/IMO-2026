# Lemma 1 — layer-cake / tail-count identity for the odd-index sum

**Source.** Certified from approach `tail-count` (round 1). Verified on 2000 random
multisets, 0 mismatches.

## Statement

For a multiset of piece lengths `ℓ_1 ≥ ℓ_2 ≥ … ≥ ℓ_m` (nonnegative, summing to `S`), let

$$N(t) \;:=\; \#\{i : \ell_i \ge t\}, \qquad t \ge 0.$$

Then the odd-index sum satisfies

$$\sum_{i\ \text{odd}} \ell_i \;=\; \int_0^\infty \left\lceil \frac{N(t)}{2} \right\rceil\, dt.$$

## Proof

For each fixed `t ≥ 0`, the pieces with `ℓ_i ≥ t` are exactly the *largest* `N(t)` pieces
(the list is sorted descending), i.e. those at indices `{1, 2, …, N(t)}`. Among these, the
ones in odd positions number exactly `⌈N(t)/2⌉` (positions `1, 3, 5, …` up to `N(t)`).
Hence

$$\sum_{i\ \text{odd}} \mathbf{1}_{\ell_i \ge t} \;=\; \left\lceil \frac{N(t)}{2} \right\rceil.$$

Integrating in `t` and applying Tonelli's theorem (a finite sum of nonnegative measurable
functions — no convergence issue):

$$\sum_{i\ \text{odd}} \ell_i \;=\; \sum_{i\ \text{odd}} \int_0^\infty \mathbf{1}_{\ell_i \ge t}\, dt \;=\; \int_0^\infty \!\left(\sum_{i\ \text{odd}} \mathbf{1}_{\ell_i \ge t}\right) dt \;=\; \int_0^\infty \left\lceil \frac{N(t)}{2} \right\rceil dt. \quad\blacksquare$$
