# Reduction R-COV' (T=∅-safe covering→value reduction) — CERTIFIED (round 12, sufficiency direction)

**Certification (round 12).** Reviewer-verified. The **sufficiency direction** (the one used by the
proof program) is rigorous: if `μ_{n+1} ≤ u_n` then Xiang forces `D ≤ u_n`. Realization is exact via
certified **Lemma ESF-2** — a nonempty subset `T` attaining `μ_{n+1}` (positive, or `0` via a nonempty
even cancellation) is realized in exactly `n` cuts: `(|T|−1)` MATCHes along the descending-KK
caterpillar (leader `t_1` is a resident piece, no cut) plus `(n+1−|T|)` DELETEs, total `n ≤ n`, with
final `D = μ_{n+1} ≤ u_n`. The `T=∅` value `0` is geometrically present in `R_{n+1}` but is NOT a legal
leftover (`n+1` DELETEs `> n` cuts); the produced value is always a nonempty-`T` value, so the
exclusion is handled correctly. Reviewer note: the converse direction as written in the source
("upper bound ⟹ `μ_{n+1}≤u_n`") is NOT rigorously established — it conflates the full achievable-leftover
set `R(A)` (all differencing trees, Lemma RL) with the descending include/skip family `R_{n+1}`, whose
minimum positive value can exceed `min R(A)`; the biconditional holds on valley profiles only because
`μ_{n+1} ≤ u_n` is (empirically) always true there. Only the sufficiency direction is certified and it
is the direction the reduction uses. Admitted (sufficiency).

**Statement (certified form).** In the full-budget balanced valley (`m=n+1`, `a_1<L/2`, `a_2<β_nL`),
```
        μ_{n+1} ≤ u_n L   ⟹   Xiang forces D ≤ u_n L   (upper bound in valley),
```
where `μ_{n+1} = min{v>0 : v∈R_{n+1}}` is the smallest positive value of the descending include/skip
reachable set. Realization is by exactly `n` DM moves (ESF-2), with the `T=∅` leftover `0` correctly
excluded as infeasible.

**Scope.** Reduces the UPPER bound in the valley to the **first-gap pigeonhole** `μ_{n+1} ≤ u_n`
(target robustly true: 0 fails over exact valley profiles n=2..7, worst `μ_{n+1}/u_n = 0.75`, tight
`= u_n` at the dyadic boundary). The first-gap pigeonhole itself is OPEN. Do NOT use the (non-certified)
converse direction.
