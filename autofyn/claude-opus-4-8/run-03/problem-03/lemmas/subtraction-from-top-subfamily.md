# Lemma ESF-1 (subtraction-from-top subfamily) — CERTIFIED (round 8)

**Statement.** Let `A = {a_1 ≥ a_2 ≥ … ≥ a_{n+1}}` (full budget, sum `L`). For every
`T ⊆ {2,…,n+1}` with `Σ_{i∈T} a_i ≤ a_1`,
```
    a_1 − Σ_{i∈T} a_i  ∈  𝓡(A),
```
realized by exactly `n` DELETE/MATCH moves.

**Proof.** Write `T = {i_1,…,i_k}` in any order, `r_0 := a_1`, `r_j := r_{j−1} − a_{i_j}`. For each
`j`, `a_{i_1}+…+a_{i_j} ≤ Σ_{i∈T} a_i ≤ a_1`, hence `r_{j−1} = a_1 − (a_{i_1}+…+a_{i_{j−1}}) ≥
a_{i_j} ≥ 0`. So the running piece `r_{j−1} ≥` resident `a_{i_j}`, and MATCH`(r_{j−1}, a_{i_j})` is
legal: cut `r_{j−1}` into `{a_{i_j}, r_{j−1} − a_{i_j}}`; the created `a_{i_j}` cancels the resident
`a_{i_j}` (certified Lemma P), leaving `r_j = r_{j−1} − a_{i_j} ≥ 0`. Each MATCH is one cut (certified
Lemma DM). After the `k` MATCHes the pieces are `r_k = a_1 − Σ_T a_i` and the `n−k` untouched
non-top, non-`T` pieces; DELETE each of those (`n−k` bisect-and-cancel moves, Lemma DM). Total
`k + (n−k) = n` moves, single final piece `r_k`, so `D = r_k` (Lemma M). ∎

**Certification.** Self-contained on certified Lemmas P (`cancelling-pair`) and DM
(`elementary-reductions`). Budget exact (`n` moves = full budget). Every MATCH legality checked
(`r_{j−1} ≥ a_{i_j}`). Reviewer-approved round 8. Reusable for upper-bound valley constructions.

**Negative companion (recorded).** ESF-1 alone is provably insufficient to reach `u_nL` in the
valley: explicit rational `n=2` counterexample `A = {9/20, 7/25, 27/100}` (valley: `a_1 = 9/20 <
1/2`, `a_2 = 7/25 < β_2 = 2/7`) has ESF-1 minimum `min{9/20, 17/100, 9/50} = 17/100 > u_2 = 1/7`,
while the two-sided abs-flip subset `{a_2,a_3}` gives `|7/25 − 27/100| = 1/100 ≤ u_2`
(reviewer-verified by exact arithmetic). So the abs-flip (Lemma ESF-2) is mandatory.
