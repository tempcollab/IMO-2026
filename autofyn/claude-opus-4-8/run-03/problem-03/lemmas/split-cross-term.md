# Lemma SPLIT (disjoint-union cross term) — CERTIFIED (round 4)

**Statement.** For any partition of a finite multiset `S = X ⊔ Y` into sub-multisets,
```
    D(S) = D(X) + D(Y) − 2·μ(O_X ∩ O_Y),
```
where `O_X = {t : N_X(t) odd}`, `O_Y = {t : N_Y(t) odd}` are the odd-sets of `X,Y`.

**Proof.** `N_S = N_X + N_Y`, so pointwise
`1[N_S odd] = 1_{O_X} ⊕ 1_{O_Y} = 1_{O_X} + 1_{O_Y} − 2·1_{O_X}1_{O_Y}`.
Integrate over `t>0` and apply Lemma M (`D = μ{N odd}`). ∎

**Certification.** Verified exactly on 3000 random partitions (max error 1.1e-16, floating
round-off). Self-contained given certified Lemma M. Reviewer-approved round 4.

**Use.** Carries the cross term `2μ(O_X∩O_Y)` exactly; dropping it (i.e. `D(S) ≤ D(X)+D(Y)`)
is too lossy near the balanced regime (open gaps L⋆ / GAP L1).
