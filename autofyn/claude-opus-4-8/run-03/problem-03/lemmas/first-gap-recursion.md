# Lemma FGR (first-gap recursion) — CERTIFIED (round 12)

**Certification (round 12).** Reviewer-verified independently. The recursion is an immediate
consequence of the reachable-set recursion `R_i = R_{i-1} ∪ {|v−a_i| : v ∈ R_{i-1}}`: the positive
elements of `R_i` are the positive elements of `R_{i-1}` (minimum `μ_{i-1}`) together with the
positive values `|v−a_i|` (`v ≠ a_i`), whose minimum is `dist(a_i, R_{i-1})` (distance to the nearest
point of `R_{i-1}` other than `a_i`). Numerically reproduced with 0 failures over 2000+ exact-rational
valley profiles (`n=2..6`). Admitted.

**Statement.** For the descending include/skip reachable set `R_0={0}`,
`R_i = R_{i-1} ∪ {|v−a_i| : v∈R_{i-1}}` (`a_1 ≥ … ≥ a_{n+1}`), let `μ_i = min{v>0 : v∈R_i}`
(`μ_0 = +∞`). Then for `i ≥ 1`
```
        μ_i = min( μ_{i-1}, dist(a_i, R_{i-1}) ),
```
`dist` being the distance from `a_i` to the nearest point of `R_{i-1}` other than `a_i`. Hence
```
        μ_{n+1} = min_{1 ≤ i ≤ n+1} dist(a_i, R_{i-1}).
```
Since `dist(a_1, R_0) = dist(a_1,{0}) = a_1` (irrelevant to a `≤u_n` bound), the operative content is
that some `a_i` (`2 ≤ i ≤ n+1`) lands within the target of a previously reachable subset-KK value —
a global, adaptive **first-gap pigeonhole**.

**Scope.** Exact identity. Correctly localises the UPPER residual as the first (smallest positive)
reachable value, which is FAR below the worst consecutive gap (covering radius) — the structural
reason every covering-radius surrogate saturates at `≈3–5·u_n` (one-cap R10, two-cap R12, both
refuted). Does NOT prove `μ_{n+1} ≤ u_n` (the first-gap pigeonhole is the open crux).
