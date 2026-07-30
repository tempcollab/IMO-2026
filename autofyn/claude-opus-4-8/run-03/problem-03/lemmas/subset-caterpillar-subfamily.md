# Lemma ESF-2 (subset-caterpillar subfamily) — CERTIFIED (round 8)

**Statement.** Let `A = {a_1 ≥ … ≥ a_{n+1}}` (full budget, sum `L`). For every nonempty
`T ⊆ {1,…,n+1}` and every ordering `t_1,…,t_k` of `{a_i : i∈T}`, the caterpillar value
```
    v_1 := t_1,   v_j := |v_{j−1} − t_j|  (2 ≤ j ≤ k),
```
satisfies `v_k ∈ 𝓡(A)`, realized by exactly `n` DELETE/MATCH moves. In particular the
descending-KK value (order `t_1 ≥ … ≥ t_k`) of any subset lies in `𝓡(A)`.

**Proof.** By induction on `j`: after `j−1` MATCHes the multiset has `v_{j−1}` as a current running
piece with the untouched pieces `{a_i : i ∉ {t_1,…,t_{j−1}}}` present. Base `j=1`: `v_1 = t_1` is a
resident piece. Step: `v_{j−1}` and `t_j` are both current pieces.
- If `v_{j−1} ≥ t_j`: MATCH`(v_{j−1}, t_j)` cuts `v_{j−1}` into `{t_j, v_{j−1} − t_j}`; the new `t_j`
  cancels the resident `t_j` (Lemma P), leaving `v_{j−1} − t_j = |v_{j−1} − t_j| = v_j`.
- If `v_{j−1} < t_j`: MATCH`(t_j, v_{j−1})` cuts the resident `t_j` (`≥ v_{j−1}`) into
  `{v_{j−1}, t_j − v_{j−1}}`; the new `v_{j−1}` cancels the running `v_{j−1}` (Lemma P), leaving
  `t_j − v_{j−1} = |v_{j−1} − t_j| = v_j`.
Either branch is a single legal MATCH (one cut), lowers the piece-count by one, leaves `v_j` running.
After `k−1` MATCHes the pieces are `v_k` and the `n+1−k` elements of `A` outside `T`; DELETE those
(`n+1−k` moves, Lemma DM). Total `(k−1) + (n+1−k) = n` moves; single final piece, `D = v_k`. ∎

**Certification.** Self-contained on certified Lemmas P (`cancelling-pair`) and DM
(`elementary-reductions`). Both abs-flip branches handled with explicit legality (`t_j ≥ v_{j−1}` in
the flip branch). Budget exact (`n` moves). ESF-1 is the special case with no sign flip; ESF-2 is
strictly larger. Reviewer-approved round 8.

**Reduction UV' (recorded, not yet a theorem).** By ESF-2 + certified Reduction R-UV, Prop UV
(`min 𝓡(A) ≤ u_nL` in the valley) follows from the residual **Subset-KK claim**: every full-budget
balanced-valley profile has a subset whose descending-KK caterpillar value is `≤ u_nL`. This claim
is NOT proved (a genuine restricted-discrepancy statement needing scale recursion); it is the honest
open residual of the upper valley.
