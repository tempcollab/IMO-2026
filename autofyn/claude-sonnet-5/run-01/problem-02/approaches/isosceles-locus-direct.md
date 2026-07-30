## Status
unsolved

## Approaches tried
- None yet built — this is a fresh, more speculative opening proposed this round, kept in the
  population for diversity (it uses power-of-a-point at M, N directly as the finishing tool,
  unlike all other live approaches which route through the auxiliary point A* or through raw
  coordinate elimination).

## Current best
Vector fact (elementary, no hypothesis needed): for any point O and the fixed segment MN,
  OM² − ON² = 2·(N−M)·(O − midpoint(MN))
so since N−M is a fixed nonzero vector parallel to BC, OM=ON reduces to one linear (dot-product)
condition on O along the BC-direction — consistent with the coordinate approach's "Re(O)=target"
criterion but phrased without fixing coordinates.

Since O is the circumcenter of AKL, for any circle ω=circle(AKL) with center O and radius R, and
any point P: pow(P, ω) = PO² − R². Hence for P=M, P=N:
  pow(M,ω) − pow(N,ω) = OM² − ON²
so **OM=ON ⟺ pow(M, circle(AKL)) = pow(N, circle(AKL))**. This is a reformulation that, unlike the
A*-concyclicity route, never introduces a fourth point — it stays with power-of-a-point at the two
given midpoints M, N directly.

**Idea (unverified):** pow(M, circle(AKL)) can be computed via the secant line through M and A
(since A is on the circle): if this line meets circle(AKL) again at a second point X, then
pow(M,ω) = MA · MX (signed). Since BM = MA (M is the midpoint of AB, so triangle ABM is isosceles
at M), this connects the power at M to the length MA = MB, a quantity tied to the original
triangle. Hypothesis (iii) ∠LCK = ∠BMK involves an angle *at M* directly (∠BMK), which is the
natural place such a computation would need to plug in — suggesting X (the second intersection of
line AM with circle(AKL)) is determined by hypothesis (iii), though this has not been checked.
Symmetrically, hypothesis (ii) ∠LBK = ∠LNC involves an angle at N, suggesting the second
intersection of line AN with circle(AKL) is determined by hypothesis (ii).

**Open gap (large, unverified):** (1) identify the second intersection point of line AM with
circle(AKL) in terms of the given hypotheses (is it K? L? a new point?) — this has not been
checked even numerically yet; (2) same for line AN; (3) show the resulting two power expressions
are forced equal by combining what's derived in (1)-(2) with the remaining hypothesis (i)
(∠KBA=∠ACL). If step (1) or (2) fails to identify a clean second-intersection point, this approach
should be marked dead-end and dropped rather than forced.

## Full proof
(not present — Status is unsolved)
