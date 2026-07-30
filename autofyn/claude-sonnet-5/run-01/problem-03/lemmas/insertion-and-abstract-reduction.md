# Insertion Lemma, rank-shift-by-s, and Claim ★ (s ≤ 2, with s ≥ 3 counterexample)

Certified from `geometric-dominance-construction.md` (round 4). Independently
re-verified by the proof-reviewer with exact-`Fraction` randomized search
(200,000+ trials, zero violations for the positive statements; the s≥3
counterexample re-verified by direct exact substitution).

## Lemma I (Insertion Lemma)

*Statement.* Let `T` be any finite, nonempty multiset of nonnegative reals,
and let `a` be any real with `0 ≤ a ≤ max(T)`. Then `evenrank(T ∪ {a}) ≥ a`.

*Proof.* Sort `T` descending as `t_1 ≥ t_2 ≥ ... ≥ t_r`. Let `j := #{i : t_i ≥ a}`
(ties toward inclusion); `j ≥ 1` since `a ≤ t_1`. Inserting `a` places it at
position `m := j+1` among the `r+1` elements.
- If `j` is even, position `j` still holds `t_j ≥ a`, and `evenrank` sums the
  value at position `j` (even), so `evenrank(T∪{a}) ≥ t_j ≥ a`.
- If `j` is odd, position `m=j+1` (even) holds `a` itself, so
  `evenrank(T∪{a}) ≥ a` directly (all terms nonnegative). ∎

This is a fully general, structure-free fact — no geometric configuration is
assumed.

## Rank-shift-by-s fact

*Statement.* Let `T` be any finite multiset and `R` a finite multiset with
`min(R) ≥ max(T)` (`|R| = s`). Writing `R` sorted descending `r_1≥...≥r_s`:
- if `s` even: `oddrank(R∪T) = oddrank(R) + oddrank(T)`,
- if `s` odd: `oddrank(R∪T) = oddrank(R) + evenrank(T)`.

*Proof.* Since every element of `R` dominates every element of `T`, the
sorted merge is `R` followed by `T`; `T`'s element at internal rank `i` now
sits at rank `s+i`, whose parity flips relative to `i` iff `s` is odd. ∎

## Claim ★ (abstract reduction, s ∈ {1,2})

*Statement.* Let `q > 0`. Let `T` be any finite multiset of nonnegative reals
with `max(T) ≤ q` and `oddrank(T) ≥ q`. Let `R = {r_1≥...≥r_s}` with
`Σ R = 2q`. For `s ∈ {1,2}`, `oddrank(R∪T) ≥ 2q`.

*Proof, s=1.* `R={2q}` dominates `T` (`2q>q≥max(T)`); rank-shift-by-1 gives
`oddrank(R∪T) = 2q + evenrank(T) ≥ 2q`.

*Proof, s=2.* `r_1≥q` always (average of two nonnegatives summing to `2q`),
so `r_1 ≥ q ≥ max(T)`, i.e. `r_1` dominates `T`. Sub-cases on `r_2`:
- `r_2 ≤ max(T)`: by rank-shift-by-1 (singleton `{r_1}` dominating `T∪{r_2}`)
  and Lemma I, `oddrank(R∪T) = r_1 + evenrank(T∪{r_2}) ≥ r_1+r_2 = 2q`.
- `r_2 > max(T)`: `R` (both elements) dominates `T`; rank-shift-by-2 gives
  `oddrank(R∪T) = r_1 + oddrank(T) ≥ q+q = 2q`. ∎

## Negative result: Claim ★ is FALSE for s ≥ 3

Exact counterexample (reviewer re-verified by direct substitution):
`q=1/8`, `T={1/8}` (so `max(T)=oddrank(T)=1/8=q`, hypotheses hold with
equality), `R = {649/4000, 116181/2000000, 59319/2000000}` (a 3-part
composition of `2q=1/4`, `Σ R = 1/4` exact). Then
`oddrank(R∪T) = 440681/2000000 = 0.2203405 < 1/4 = 2q`.

*Diagnosis.* For `s≥3`, an adversarial `s`-way composition of `2q` can have
largest part `<q` (e.g. equal split gives `2q/3<q`), so no element of `R` need
dominate `T`; `max(T)` and `oddrank(T)` alone do not carry enough information
about `T`'s internal structure to compensate. Rules out any argument for the
`k≥2` gap based only on these two scalar summaries of `T`.

## Status
Certified. Reusable by any approach doing rank-shift/insertion bookkeeping.
