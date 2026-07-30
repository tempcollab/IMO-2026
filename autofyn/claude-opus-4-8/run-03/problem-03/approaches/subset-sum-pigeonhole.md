## Status
unsolved (new — round 7 skeleton; upper-valley pigeonhole route, hard step flagged)

## Approach: subset-sum-pigeonhole (framing G — restricted subset-sum / number-partitioning pigeonhole for the upper valley)

Target (the whole claim): for every positive integer n, the largest c Liu can guarantee is
c(n)=2^n/(2^{n+1}−1), equivalently minimax D=u_n=1/(2^{n+1}−1).

**Why far from the field.** Every prior upper attempt is a move-induction (DM greedy) or a
mass/measure bound. This approach reads the numerology directly: the denominator 2^{n+1}−1 is
exactly the number of gaps between the 2^{n+1} subset sums of the n+1 Liu pieces, so a
**subset-sum pigeonhole** is the natural mechanism. This is distinct from the refuted
mass-threshold subset-cover (a single-threshold search); no built approach has run a full
sorted-subset-sum-gap pigeonhole.

Imports (certified, no re-proof): Lemmas R, M/T, P, PEEL, SPLIT, ONE, TB, DM, U0, whole-tail-peel.

### Reduction
By Lemma R/M the game is the scalar minimax of D over refinements. By U0(c) the upper bound is
nontrivial only at full budget m=n+1 (fewer pieces ⇒ D=0 with ≤n cuts). By whole-tail-peel the
range a₁≥L/2 is closed. Residual: the balanced valley {m=n+1, a₁<L/2, a₂<β_nL, β_n=2^{n-1}/(2^{n+1}−1)}.

### The pigeonhole
1. The 2^{n+1} subset sums of A={a₁,…,a_{n+1}} lie in [0,L]. Pigeonhole ⇒ two distinct subsets
   S,S′ with |Σ_S a − Σ_{S′} a| ≤ L/(2^{n+1}−1)=u_nL. Their symmetric difference yields a nonzero
   ε∈{−1,0,+1}^{n+1} with |Σ ε_i a_i| ≤ u_nL.
2. **Achievability = differencing-tree realizability.** A sequence of n DM moves on the n+1 pieces
   (MATCH subtracts one current piece from another, DELETE zeroes one) leaves exactly one core
   leftover ρ=|Σ ε_i a_i| for the ± pattern realised by that binary differencing tree, and by
   Lemma P/PEEL D(final)=ρ. So the achievable D-values are exactly the tree-realizable signed
   combinations of the a_i.
3. Run the pigeonhole RESTRICTED to the achievable family; force an achievable ρ≤u_nL, giving a
   legal ≤n-cut Xiang response with D≤u_nL.

### Lower bound
Imported from the certified reduction + TB; the lower exchange (L2-exch) is the field's shared
open gap, carried by the lower slugs (not this approach's contribution).

## Open gaps
**GAP-ACH (make-or-break).** Not every ±1 pattern is tree-realizable — numerically only ~half
(2^{n-2} of 2^{n-1} magnitude classes for n=4, explorer). A naive restricted pigeonhole over ~2^n
achievable values gives only gap ≤ u_{n-1}L, short of u_nL by a factor ≈2. Must close this deficit:
candidate mechanisms — (i) spend one free DELETE to drop to n numbers and restore the factor, then
pigeonhole the remaining 2^n subset sums; (ii) prove the achievable value set is monotone/sorted so
consecutive achievable sums are ≤u_nL apart; (iii) identify the achievable family with VERT's
tie-graph family and count it exactly. Prove the family size for all n (not just n=4).

## Approaches tried
- (round 7, new) registered as skeleton; pigeonhole reduction + achievability identity laid out;
  the factor-2 achievability deficit is the sole hard step. Lower bound imported/deferred.

## Current best
Import of the full certified reduction; upper bound reduced (via U0, whole-tail-peel) to the
balanced valley, reframed as: min over tree-realizable signed combinations |Σε_i a_i| ≤ u_nL. The
2^{n+1}−1 = subset-sum-gap-count numerology matches the target exactly, motivating the pigeonhole;
the achievability restriction (GAP-ACH) is the open content.
