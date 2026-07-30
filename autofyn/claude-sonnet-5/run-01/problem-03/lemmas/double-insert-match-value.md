# Lemma DOUBLE-INSERT-MATCH-VALUE (certified, round 14)

Source: `case-c-slack-covering.md`, round 14, Step 0. A direct corollary
of the already-certified Lemma DOUBLE-INSERT (`lemmas/double-insert.md`).
Independently re-verified by the proof-reviewer with a from-scratch
`fractions.Fraction` script, 5000 random trials (list sizes 2–7, arbitrary
positive rational values, arbitrary choice of tail index `i`), zero
mismatches.

## Statement

Let `A = (p_1 \ge p_2 \ge \cdots \ge p_m)` be any sorted list of positive
reals, tail `T = (p_2,\ldots,p_m)`. Fix any index `i` with `t_i \le p_1`
(automatic, since `p_1 = \max(A)`). Split `p_1` into the two parts
`(t_i,\, r_i)` with `r_i := p_1 - t_i \ge 0`, forming the tied pair
`\{t_i,t_i\}` (one new copy, one already present in the tail) and leaving
the residual `r_i` as a new free element (omitted if `r_i = 0`). Write
`\mathrm{REST}_i := (T\setminus\{t_i\}) \cup (\{r_i\}\ \text{if}\ r_i>0)`.
Then, **exactly** (not an estimate), using `1` mark (or `0` marks if
`r_i = 0`, via the certified Lemma DOM-boundary-slack):
```
oddrank(A after this split) = t_i + oddrank(REST_i).
```

## Proof

The resulting multiset is exactly `REST_i \cup \{t_i,t_i\}`, i.e. Lemma
DOUBLE-INSERT applied with `T := REST_i` and `v := t_i`: inserting a
duplicated value `v` into any sorted list changes `oddrank` by exactly
`+v`, unconditionally on the rest of the array. Substituting gives the
stated identity directly. ∎

## Scope note

This lemma is an exact-value identity for one specific candidate move
(matching `p_1` against one designated tail element `t_i`); it says
nothing about which `i` is optimal, nor whether any single such move (or
any finite family of them, combined by min or by average) suffices to
prove Claim PTBI's Case C in general. See the companion **Fact
(uniform-tail worst-case margin)**, also certified this round, for a
proof that averaging (or taking the best member) of the family
`{UB_i}_{i=1}^{m-1}` built from this lemma is *insufficient* in general.
