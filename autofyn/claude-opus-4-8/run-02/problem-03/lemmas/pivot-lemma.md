# Lemma (Pivot / Accumulator) — CERTIFIED round 4

Depends on: certified Invisible-Pair Lemma (IP) and the generalized-pin / bisect removal ops
(`lemmas/cut-flip.md` spine; IP proved in `approaches/dyadic-discrepancy.md` §4.5). Reviewer-verified
round 4 (algebra + 2·10⁴ exact-Fraction / float instances, 0 violations).

## Statement
Let a current effective multiset be `ℓ₁ ≥ ℓ₂ ≥ … ≥ ℓ_m > 0` (pivot = largest, `ℓ₁`). Let
`S ⊆ {ℓ₂,…,ℓ_m}` with `sum(S) ≤ ℓ₁`. Then Xiang, using **exactly `m−1` removal ops** — bisect every
piece of `{ℓ₂,…,ℓ_m}∖S` (deleted by IP), then pin the pieces of `S` into the pivot one at a time in
decreasing order — reaches an effective multiset of total exactly `ℓ₁ − sum(S) ≥ 0`.

Equivalent deterministic form (accumulator, `dyadic-discrepancy-euclid` §5): if `ℓ₁ ≥ Σ/2`, the
schedule "repeatedly pin the second-largest into the largest, free-deleting equal pairs" is legal,
uses `≤ m−1` ops, keeps the accumulator the unique maximum (invariant `sum(rest) ≤ accumulator`,
self-restoring), and terminates at effective total `2ℓ₁ − Σ`.

## Proof
Bisecting each piece `∉S` deletes it (IP), using `m−1−|S|` ops and leaving effective multiset
`{ℓ₁} ∪ S`. Then subtract `S = {s₁ ≥ … ≥ s_r}` into the pivot in decreasing order: before step `i`
the pivot is `R_i = ℓ₁ − (s₁+…+s_{i−1})`; the pin of `s_i` (cut pivot into `{s_i, R_i−s_i}`, equal
pair `{s_i,s_i}` deleted by IP) is legal since `R_i − s_i = ℓ₁ − (s₁+…+s_i) ≥ ℓ₁ − sum(S) ≥ 0`
(equality → free-delete). Block uses `|S|` ops; total `(m−1−|S|)+|S| = m−1`. Final total
`R_{r+1} = ℓ₁ − sum(S)`. ∎

## Consequence (Case (iii-a) of GAP U, all n)
With `Σ` the total, `S = {ℓ₂,…,ℓ_m}` (admissible iff `Σ−ℓ₁ ≤ ℓ₁`, i.e. `ℓ₁ ≥ Σ/2`): residual
`= 2ℓ₁ − Σ`. Since `2c(k)−1 = u_k` (`c(k)=2^k/(2^{k+1}−1)`), if `ℓ₁ < c(k)Σ` then residual
`< u_kΣ`, and by `D ≤ (effective total)` (Residual-Total Theorem) `D < u_kΣ`. This closes the whole
slab `Σ/2 ≤ ℓ₁ < c(k)Σ` of GAP U, tight at `ℓ₁ = c(k)Σ` (dyadic boundary), for every `n`.
Remaining GAP U sub-case: `ℓ₁ < Σ/2` (super-balanced, (iii-b)) — OPEN.
