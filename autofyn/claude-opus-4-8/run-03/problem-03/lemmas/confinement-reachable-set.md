# Lemma CONF (confinement of the reachable set) — CERTIFIED (round 11)

**Certification (round 11).** Reviewer-verified independently. The induction is valid: the
elementary inequality `|v − a| ≤ max(v, a)` holds for all reals `v, a ≥ 0` (case split `v ≥ a`
vs `v < a`), and with `v ≤ a_1` (IH) and `a_i ≤ a_1` (sort order) gives `|v − a_i| ≤ a_1`.
Numerically reproduced (0 failures, random + near-tie valley profiles n=3–6); equality `max R = a_1`
is attained (subset `{a_1}`). Admitted.

**Statement.** Let `A = {a_1 ≥ a_2 ≥ … ≥ a_{n+1}}` be sorted descending. Define the descending
include/skip reachable **set** `R_0 = {0}`, `R_i = R_{i-1} ∪ {|v − a_i| : v ∈ R_{i-1}}`. Then for
every `0 ≤ i ≤ n+1`,
```
        max R_i ≤ a_1,     i.e.   R_i ⊆ [0, a_1].
```
In particular, in the balanced valley (`a_1 < L/2`), `R_{n+1} ⊆ [0, a_1] ⊂ [0, L/2)`.

**Proof.** Strong induction on `i`. Base `i=0`: `R_0 = {0}`, `max R_0 = 0 ≤ a_1`. Step: assume
every `v ∈ R_{i-1}` satisfies `0 ≤ v ≤ a_1`. Each element of `R_i` is either such a `v` (so `≤ a_1`)
or `|v − a_i|` for some `v ∈ R_{i-1}`. For the latter, the elementary inequality
`|v − a_i| ≤ max(v, a_i)` holds for `v, a_i ≥ 0` (if `v ≥ a_i` then `|v − a_i| = v − a_i ≤ v`; if
`v < a_i` then `|v − a_i| = a_i − v ≤ a_i`). By the IH `v ≤ a_1`, and by sorting `a_i ≤ a_1`, so
`max(v, a_i) ≤ a_1`, whence `|v − a_i| ≤ a_1`. All elements are `≥ 0`. Hence `max R_i ≤ a_1`. ∎

**Scope.** Depends only on the sort order `a_i ≤ a_1`; profile-independent, no budget assumption.
It confines all reachable descending-KK values but does NOT by itself bound the covering value toward
`u_n` (the residual factor `2^{n-1}` from `β_n` to `u_n` is not addressed). Used by the upper-wall
approach `breakpoint-vertex` (GAP U-cover).
