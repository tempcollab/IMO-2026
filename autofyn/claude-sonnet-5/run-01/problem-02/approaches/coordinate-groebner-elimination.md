## Status
partial

(Corrected this round: the round-4 header claiming `solved` was stale/incorrect and has been reviewed
down to `partial` by `current.md`'s reviewer. This round fixes that header, switches the rotation-sign
justification to cite the certified `interior-point-side-test.md` lemma, and makes a genuine but
incomplete attempt at the outstanding branch-selection gap for hypotheses (ii)/(iii). The gap is **not**
closed this round — see "Branch-selection gap" section below for exactly what remains open. Per the
explicit history of this file (overclaimed `solved` in rounds 2 and 4, both caught by the reviewer),
`Status` stays `partial` until every case below is genuinely closed.)

## Approaches tried
- (Round 2, prior builder) Set up the coordinate system, parametrized K,L, derived e1,e2 (the two
  polynomial hypothesis equations) and myexpr (the OM=ON target polynomial), but had not attempted
  to certify myexpr ∈ ideal(e1,e2).
- (Round 3) Executed the mechanical elimination the outline called for. Found the key structural
  decoupling fact (e1 = tK·const·g1(tL), e2 = tL·g2(tK)) and an explicit cofactor identity
  `D1·myexpr = D1·Q1·g1 + (QA+QB·tL)·g2`, but left `D1 ≠ 0` as an open gap.
- (Round 4, this round) Closed the remaining gap in full. Specifically:
  (1) Re-verified from scratch, with sympy, the entire chain: coordinate setup, the e1=tK·(|AC|²/4)·g1
  and e2=tL·(|AB|²/4)·g2 factorizations, and the exact polynomial coefficients of g1, g2. **Found that
  the previously-displayed g1 formula in this file was in fact already correct** (a fresh, independent
  from-scratch recomputation, both by full symbolic expansion modulo cos²+sin²=1 and by exact rational
  substitution, reproduces the displayed g1 coefficient-for-coefficient with no discrepancy) — the "4x"
  discrepancy flagged by the round-4 outline-reviewer was not reproduced in this from-scratch check
  (most likely the reviewer's own numeric check compared against an unreduced or differently-normalized
  quantity); this is reported honestly below and the correct formula, independently reverified, is used.
  (2) Redid the two-step polynomial division (Step A: myexpr mod g1 in tL; Step B: the two resulting
  tK-coefficients mod g2 in tK) completely from scratch, confirming both final remainders are exactly
  zero (checked both by full symbolic cancellation, i.e. `sp.cancel` giving literally 0 with no
  reduction needed, and by substitution of several independent exact-rational (non-degenerate)
  parameter points). This yields a clean, fully polynomial cofactor identity (no more residual
  denominators): `2Z²·myexpr = (Z·P1)·g1 + (Z·QA+QB_poly)·g2`, with `Z` the single scalar appearing as
  the (halved) leading coefficient of both g1 (in tL²) and g2 (in tK²) — this is the same `Z` as in the
  sibling `synthetic-angle-chase-aklastar` approach and the same as (twice) the earlier `D1`.
  (3) Closed the `Z≠0` gap completely with a **self-contained barycentric argument** proving `Z>0`
  unconditionally on the geometrically valid locus (not merely non-vanishing): both `X:=K_y/tK>0` and
  `sin α>0` are derived from the single hypothesis "K strictly interior to triangle BMC", via two
  parallel barycentric-coordinate computations (one for the y-coordinate of K, one for the cross
  product `cross(A−B,K−B)`, both linear in the barycentric weight of C). This resolves both flagged
  issues from the round-4 outline-reviewer (the *sin α > 0* justification issue is fully closed here,
  with a strictly stronger and cleaner argument than the α∈(0,π)-only version) at once.
  (4) Additionally verified numerically (not part of the proof itself, but an independent existence and
  consistency sanity check) that valid full configurations satisfying **all five** hypotheses
  (i)–(iii) plus both position hypotheses exist for the chosen rotation-sign convention, and that for
  such a configuration OM=ON holds to floating-point precision, confirming the whole machinery is
  self-consistent, not just formally correct.
  **(This round-4 entry's closing claim "the proof is now complete; Status upgraded to solved" was an
  overclaim, caught by the round-4/5 reviewer: it never actually addressed the branch-selection gap for
  hypotheses (ii)/(iii) — see below — and its rotation-sign justification rested on the numeric
  "Existence / consistency check" paragraph rather than a proof. Left here verbatim as an honest record
  of what happened, not endorsed.)**
- (Round 5, this round) Three fixes, per this round's outline/outline-reviewer directives: (1) corrected
  the stale `Status: solved` header to `partial`; (2) replaced the numeric-only justification of the
  rotation-sign convention with a citation of the certified `results/imo-2026-02/lemmas/interior-point-side-test.md`,
  applied in this file's own $(p,q,a,ca,sa,t_K,t_L)$ notation (see "Rotation-sign convention" below —
  this supersedes the old "Existence check" as the *logical* justification; the numeric check is
  retained only as a corroborating sanity check, not as a proof step); (3) attempted to close the
  directed-angle branch-selection gap for hypotheses (ii)/(iii) independently, in this file's own
  coordinate/rotation notation (see new section "Branch-selection gap" below). **Result: genuine,
  independently-derived partial progress — a new Ray-Betweenness Lemma is proved in full and used to
  establish $\sin\theta_1>0$ (vertex-$B$ half of hyp (ii)'s branch) and the symmetric fact for hyp
  (iii) at vertex $C$ — but the vertex-$N$ (resp. vertex-$M$) half of the argument, and a further subtlety
  about which of the two literal signed-angle relations consistent with hyp (ii)/(iii)'s *unsigned*
  statement is realized on the valid locus, are NOT closed. Status remains `partial`; this is not a
  third overclaim.**

## Current best
Unconditional, fully-verified polynomial identity $2Z^2\cdot\mathrm{myexpr}=(ZP_1)g_1+(ZQ_A+Q_B)g_2$
(Claim/§"The cofactor identity" below) together with $Z>0$ (Lemma 3) reduce the whole problem to: prove
that hypotheses (ii),(iii), on the valid geometric locus, force $g_1=0$ and $g_2=0$. This is now known
to require more than the naive "hyp(ii) $\iff$ e1=0" translation (see "Branch-selection gap" below for
why); a new Ray-Betweenness Lemma (proved in full this round) closes the vertex-$B$/vertex-$C$ half of
the needed sign argument, but the vertex-$N$/vertex-$M$ half and the full branch-vs-literal-hypothesis
correspondence remain open. This is the sole remaining gap; everything else in the "Full proof" section
below (Lemmas 1–3, the decoupling, the cofactor identity, $Z>0$) is complete and unconditional.

## Detailed development

(Per the file contract, "## Full proof" is reserved for Status `solved`; since Status here is `partial`,
the unconditional lemmas and the conditional reduction are presented under this heading instead. Every
lemma below through the cofactor identity and $Z>0$ is complete and unconditional; the final step is
conditional on the branch-selection gap, honestly flagged in its own section above.)

### Setup

Place $B=(0,0)$, $C=(a,0)$ with $a>0$, and $A=(p,q)$ with $q>0$ (always achievable by translating,
scaling has no effect on the claim so is not even needed, and reflecting the triangle in the line
$BC$ if necessary so $A$ lies above it — this reflection preserves all hypotheses and the conclusion
since it is an isometry). Let $M,N$ be the midpoints of $AB,AC$ respectively.

**Lemma 1 (Base reduction).** For any point $O$,
$$OM=ON \iff O_x = \frac{2p+a}{4}.$$
Moreover, writing $u=K-A,\ v=L-A$ and $\mathrm{cross}(u,v)=u_1v_2-u_2v_1$, if $O$ is the circumcenter
of a non-degenerate triangle $AKL$ then
$$O_x-\frac{2p+a}{4} = \frac{\mathrm{myexpr}}{2\,\mathrm{cross}(u,v)}, \qquad
\mathrm{myexpr} := \Big(p-\tfrac a2\Big)\mathrm{cross}(u,v) + |u|^2v_2 - |v|^2u_2,$$
so $OM=ON \iff \mathrm{myexpr}=0$ (this never divides by $p-a/2$, so no isosceles-triangle case split
is needed).

*Proof.* $M=(p/2,q/2)$, $N=((p+a)/2,q/2)$ have equal $y$-coordinate $q/2$, so a point is equidistant
from $M,N$ iff it lies on their perpendicular bisector, the vertical line $x=(2p+a)/4$. This gives the
first claim. For the second, translate coordinates so $A$ is the origin; the circumcenter $O'=(x_0,y_0)$
of $0,u,v$ satisfies the two equidistance equations $2u_1x_0+2u_2y_0=|u|^2$ (equidistant from $0,u$) and
$2v_1x_0+2v_2y_0=|v|^2$ (equidistant from $0,v$); this linear system has determinant
$2\,\mathrm{cross}(u,v)\ne0$ exactly when $0,u,v$ (i.e. $A,K,L$) are not collinear. Cramer's rule gives
$x_0 = (|u|^2v_2-|v|^2u_2)/(2\,\mathrm{cross}(u,v))$. Since $O_x=p+x_0$, algebra gives the stated
formula. $\blacksquare$

$A,K,L$ are non-collinear here since $K,L$ are, by hypothesis, points strictly interior to triangles
$BMC$, $BNC$ respectively, hence not on line $AB$ or $AC$ (in particular not equal to $A$), and a short
argument below (in the course of proving $Z>0$) in fact shows $K$ is not even on line $AB$ — this will
also be used to justify non-collinearity of $A,K,L$ is not needed as a separate hypothesis since it is
implied by $\mathrm{cross}(u,v)\ne0$, which the identity above requires and which holds because $K,L$
being properly interior to triangles sharing only the vertex $A$-side forces them off line $AL$ etc.;
formally, $A,K,L$ collinear would force (since $K\ne A$) $L$ on line $AK$, and since $K$ is not on line
$AB$ (proved below) nor is $L$ generically forced to coincide — but in fact this degenerate case is
excluded directly: if $A,K,L$ were collinear, $\mathrm{cross}(u,v)=0$, and then $O$ (the circumcenter)
is not even defined (the "triangle" $AKL$ degenerates), so the problem statement's hypothesis that $O$
is the circumcenter of triangle $AKL$ presupposes $A,K,L$ non-collinear; we take this as given by the
problem statement's own hypotheses without needing further proof.

### Parametrizing K and L so hypothesis (i) is automatic

Let $\alpha$ be the common value of $\angle KBA=\angle ACL$ (hypothesis (i)). Write $ca=\cos\alpha$,
$sa=\sin\alpha$, so $ca^2+sa^2=1$ identically. Rotating the unit vector along $BA$, namely $(p,q)/|AB|$,
by the angle $-\alpha$ gives the unit vector $\big(p\,ca+q\,sa,\ q\,ca-p\,sa\big)/|AB|$ along ray $BK$
(this choice of sign, rather than $+\alpha$, together with the symmetric choice of $+\alpha$ for ray
$CL$ below, is the branch matching the problem's hypotheses; this is now justified logically, not just
numerically. **Rotation-sign convention (citing the certified lemma).** By
`results/imo-2026-02/lemmas/interior-point-side-test.md`, applied with $P=B,Q=M,R=C$: since $K$ is
strictly interior to $\triangle BMC$ and $B,M$ lie on line $AB$ while $C\notin$ line $AB$, $K$ lies
strictly on $C$'s side of line $AB$, i.e. $\mathrm{cross}(A-B,K-B)$ has the same sign as
$\mathrm{cross}(A-B,C-B)=-qa<0$, so $\mathrm{cross}(A-B,K-B)<0$. Under the parametrization
$K=t_K R(-\alpha)(A-B)$ (writing $B=0$) with $t_K>0$, direct expansion (identical to the computation
in Lemma 3(b) below) gives $\mathrm{cross}(A-B,K-B)=-t_K|AB|^2\sin\alpha$; since $t_K,|AB|^2>0$, this is
negative exactly when $\sin\alpha>0$. Hence the certified lemma forces $\sin\alpha>0$ under the
$-\alpha$ convention. Had the opposite convention $K=t_K R(+\alpha)(A-B)$ been used instead, the same
computation would give $\mathrm{cross}(A-B,K-B)=+t_K|AB|^2\sin\alpha$, which the certified lemma would
force to be negative, i.e. $\sin\alpha<0$ — impossible, since $\alpha=\angle KBA$ is (by definition, as
the measure of an angle of a genuine triangle/configuration) a value in $(0,\pi)$, where $\sin\alpha>0$
always. This rules out the $+\alpha$ convention and rigorously selects $-\alpha$ as the only convention
consistent with the certified lemma, replacing the old numeric-only justification.** So,
introducing a real distance-along-the-ray parameter $t_K\ge 0$ with $t_K=0$ iff $K=B$,
$$K = \big(t_K(p\,ca+q\,sa),\ t_K(q\,ca-p\,sa)\big).$$
Symmetrically, rotating the unit vector along $CA$, $(p-a,q)/|AC|$, by $+\alpha$, with parameter
$t_L\ge0$, $t_L=0$ iff $L=C$,
$$L = \big(a+t_L((p-a)ca-q\,sa),\ t_L(q\,ca+(p-a)sa)\big).$$
By construction, for **any** $t_K,t_L\ge0$ these formulas give $\angle KBA=\angle ACL=\alpha$ exactly
(rotation preserves angles regardless of how far along the ray one travels), so hypothesis (i) holds
identically and never needs to be separately verified.

Since $K$ is (by the problem's hypothesis) strictly interior to triangle $BMC$, in particular $K\ne B$,
so $t_K>0$; likewise $L\ne C$ gives $t_L>0$.

### The two remaining hypotheses as polynomial equations, and their decoupling

For vectors $u,v$, write $\mathrm{cross}(u,v)=u_1v_2-u_2v_1$, $\mathrm{dot}(u,v)=u_1v_1+u_2v_2$; then
$\tan(\text{directed angle from }u\text{ to }v)=\mathrm{cross}(u,v)/\mathrm{dot}(u,v)$, so the condition
"directed angle from $u$ to $v$ equals directed angle from $w$ to $x$" is captured, whenever the two
dot products are nonzero (which holds here since all the relevant angles are proper, non-right, angles
of genuine triangles — this can also be checked to not create spurious solutions since we verify the
final identity by exact polynomial cancellation, not by clearing denominators that might vanish), by
$$\mathrm{cross}(u,v)\,\mathrm{dot}(w,x) - \mathrm{cross}(w,x)\,\mathrm{dot}(u,v) = 0.$$
Applying this to hypothesis (ii) $\angle LBK=\angle LNC$ and hypothesis (iii) $\angle LCK=\angle BMK$,
with $M=(p/2,q/2)$, $N=((p+a)/2,q/2)$:
$$e_1 := \mathrm{cross}(L{-}B,K{-}B)\,\mathrm{dot}(L{-}N,C{-}N) - \mathrm{cross}(L{-}N,C{-}N)\,\mathrm{dot}(L{-}B,K{-}B) = 0,$$
$$e_2 := \mathrm{cross}(L{-}C,K{-}C)\,\mathrm{dot}(B{-}M,K{-}M) - \mathrm{cross}(B{-}M,K{-}M)\,\mathrm{dot}(L{-}C,K{-}C) = 0.$$

**Lemma 2 (Decoupling — certified, see `results/imo-2026-02/lemmas/ray-parametrized-angle-decoupling.md`).**
With $K,L$ as parametrized above, $e_1 = t_K\cdot\frac{|AC|^2}{4}\cdot g_1(t_L)$ and
$e_2 = t_L\cdot\frac{|AB|^2}{4}\cdot g_2(t_K)$, where $g_1$ depends on $t_L,ca,sa,p,q,a$ only (not
$t_K$) and $g_2$ depends on $t_K,ca,sa,p,q,a$ only (not $t_L$), each a **quadratic** polynomial in its
one free variable:
$$g_1 = (a\,ca\,q-a\,p\,sa) + t_L\big({-}2a\,ca^2q+2a\,ca\,p\,sa-a\,q-2ca\,p^2sa-2ca\,q^2sa\big) + t_L^2\cdot D,$$
$$g_2 = (a\,ca\,q-a^2sa+a\,p\,sa) + t_K\big({-}2a\,ca^2q+2a\,ca\,p\,sa-a\,q-2ca\,p^2sa-2ca\,q^2sa\big) + t_K^2\cdot D,$$
where
$$D := 2a\,ca\,q-2a\,p\,sa+2p^2sa+2q^2sa = 2Z,\qquad Z:= a\,X + sa\,|AB|^2,\qquad X:=ca\,q-p\,sa.$$
(Both quadratics share the *same* $t_L^1$-linear and leading coefficients, up to the constant leading
scalar $D$; this symmetric structure was verified directly by fresh sympy expansion of $e_1,e_2$ from
their defining formulas above, factoring out $t_K$ (resp. $t_L$) and the constant $|AC|^2/4$ (resp.
$|AB|^2/4$), and matches the file's earlier (round-3) displayed $g_1$ coefficient-for-coefficient after
independent re-derivation this round — see the note in "Approaches tried" above regarding the
round-4 "4x" flag, which this from-scratch recheck did not reproduce.)

Since $t_K,t_L>0$: **hypothesis (ii) $\iff g_1(t_L)=0$, and hypothesis (iii) $\iff g_2(t_K)=0$.**

### $X>0$ and $\sin\alpha>0$, hence $Z>0$

**Lemma 3.** With $B,M,C$ as above ($B=(0,0)$, $M=(p/2,q/2)$, $C=(a,0)$, $q>0,a>0$) and $K$ strictly
interior to triangle $BMC$ as in the problem's hypothesis: $X>0$ and $sa>0$, hence $Z=aX+sa\,|AB|^2>0$
(a sum of two strictly positive terms, since $a>0,|AB|^2>0$).

*Proof.* Since $K$ is strictly interior to $\triangle BMC$, write $K=\lambda B+\mu M+\nu C$ with
$\lambda,\mu,\nu>0$, $\lambda+\mu+\nu=1$ (barycentric coordinates of an interior point are all strictly
positive — standard). Since $B=(0,0)$:
$$K = \mu M + \nu C = \Big(\frac{\mu p}{2}+\nu a,\ \frac{\mu q}{2}\Big).$$

*(a) $K_y>0$, hence $X>0$.* $K_y=\mu q/2>0$ since $\mu>0,q>0$. By the parametrization,
$K_y = t_K(q\,ca-p\,sa) = t_K\cdot X$. Since $t_K>0$ (shown above) and $K_y>0$, $X=K_y/t_K>0$.

*(b) $sa>0$.* Compute $\mathrm{cross}(A-B,K-B) = \mathrm{cross}((p,q),K) = p\,K_y - q\,K_x$. On one hand,
using the parametrization of $K$:
$$p\,K_y-q\,K_x = p\cdot t_K(q\,ca-p\,sa) - q\cdot t_K(p\,ca+q\,sa)
= t_K\big[pq\,ca-p^2sa-pq\,ca-q^2sa\big] = -t_K(p^2+q^2)sa = -t_K|AB|^2sa$$
(direct algebraic expansion, verified independently by symbolic computation). On the other hand, using
the barycentric decomposition $K=\lambda B+\mu M+\nu C$: since $M=(A+B)/2$, $M-B=(A-B)/2$, so
$\mathrm{cross}(A-B,M-B)=\tfrac12\mathrm{cross}(A-B,A-B)=0$; and $\mathrm{cross}(A-B,B-B)=0$. Hence, by
bilinearity of $\mathrm{cross}(A-B,\cdot)$ in its second argument,
$$\mathrm{cross}(A-B,K-B) = \lambda\cdot 0 + \mu\cdot 0 + \nu\,\mathrm{cross}(A-B,C-B)
= \nu\,\mathrm{cross}((p,q),(a,0)) = \nu(p\cdot 0-q\cdot a) = -\nu q a.$$
Equating the two expressions for $\mathrm{cross}(A-B,K-B)$:
$$-t_K|AB|^2sa = -\nu q a.$$
The right side is strictly negative ($\nu>0,q>0,a>0$), so the left side is too: $-t_K|AB|^2sa<0$. Since
$t_K>0$ and $|AB|^2>0$, dividing by the strictly negative number $-t_K|AB|^2$ (which reverses the
inequality) gives $sa>0$. $\blacksquare$

(This also shows, incidentally, that $K$ does not lie on line $AB$ at all — since $\mathrm{cross}(A-B,K-B)=-\nu qa\ne0$ — a fact used implicitly above to guarantee $A,K,L$ are non-collinear together with the
symmetric fact for $L$ off line $AC$, consistent with the problem's presupposition that $O$, the
circumcenter of $\triangle AKL$, exists.)

### The cofactor identity

**Lemma 1** gives $OM=ON\iff\mathrm{myexpr}=0$ where, with $u=K-A,v=L-A$,
$$\mathrm{myexpr} = \Big(p-\frac a2\Big)\mathrm{cross}(u,v) + |u|^2v_2-|v|^2u_2.$$

**Claim.** There is a fully polynomial identity, holding identically in $t_K,t_L,ca,sa,p,q,a$ modulo
$ca^2+sa^2=1$:
$$2Z^2\cdot\mathrm{myexpr} \;=\; (Z\cdot P_1)\cdot g_1 \;+\; (Z\cdot Q_A + Q_B)\cdot g_2, \tag{$\star$}$$
for explicit polynomials $P_1(t_K,ca,sa,p,q,a)$, $Q_A(t_K,ca,sa,p,q,a)$, $Q_B(t_K,t_L,ca,sa,p,q,a)$
(each computed and displayed in the Appendix below; $Q_B$ is linear in $t_L$, and its formula there is
literally $Q_B = Q_{B}^{poly}(t_K,\ldots)\cdot t_L$ for a polynomial $Q_B^{poly}$ free of $t_L$, matching
$(\star)$ as written with $Q_B$ standing for that product).

*Proof of Claim (mechanical, executed by CAS from scratch this round and independently re-verified).*
Since $g_1$ has degree exactly $2$ in $t_L$ (leading coefficient $D=2Z$) and $\mathrm{myexpr}$ has
degree $2$ in $t_L$ as well, ordinary polynomial division (over the field of rational functions in
$ca,sa,p,q,a,t_K$) gives
$$\mathrm{myexpr} = Q_1(t_K,\ldots)\cdot g_1 + R_1,\qquad R_1 = A(t_K,\ldots) + B(t_K,\ldots)\cdot t_L,$$
an *exact* division (verified: $\mathrm{myexpr}-Q_1g_1-R_1$ cancels to literally $0$ as a rational
function, with no need even to invoke $ca^2+sa^2=1$; and independently, evaluating both sides at several
exact rational points with $(ca,sa)$ a genuine cosine-sine pair — e.g. the Pythagorean pairs
$(3/5,4/5),(-7/25,24/25),(0,1)$ combined with rational $p,q,a,t_K,t_L$ — gives exact equality). Here
$Q_1$ has denominator $D=2Z$ exactly, so $P_1:=D\cdot Q_1=2Z\cdot Q_1$ is a genuine polynomial (verified:
clearing the denominator of $Q_1$ leaves no residual denominator).

Multiplying through by $D=2Z$: $D\cdot\mathrm{myexpr} = P_1\cdot g_1 + D\cdot R_1 = P_1\cdot g_1 +
(D\cdot A) + (D\cdot B)\cdot t_L$. Both $D\cdot A$ and $D\cdot B$ are, after this scaling, honest
polynomials in $t_K,ca,sa,p,q,a$ (degree $2$ in $t_K$, matching $\deg_{t_K}g_2=2$); dividing each by
$g_2$ (again over the rational function field, now in the variable $t_K$):
$$D\cdot A = Q_A(t_K,\ldots)\cdot g_2 + R_A,\qquad D\cdot B = Q_B^{poly}(t_K,\ldots)\cdot g_2 + R_B.$$
Direct symbolic division (executed and displayed in the Appendix) gives $R_A=0$ and $R_B=0$ **exactly**
— verified first by exact rational cancellation (`sp.cancel` reducing the remainder literally to $0$)
and independently corroborated by exact-rational-point substitution as above. Here $Q_A$ comes out with
no residual denominator, while $Q_B^{poly}$ carries a residual denominator of exactly $Z$ (i.e.
$Q_B^{poly}=Q_B^{poly,\,num}/Z$ for a polynomial numerator); multiplying the resulting identity
$D\cdot\mathrm{myexpr}=P_1g_1+(Q_Ag_2)+(Q_B^{poly}t_L)g_2$ through once more by $Z$ clears this last
denominator, giving, since $D=2Z$:
$$2Z^2\cdot\mathrm{myexpr} = Z\cdot P_1\cdot g_1 + \big(Z\cdot Q_A + Q_B^{poly,\,num}\cdot t_L\big)\cdot g_2,$$
which is $(\star)$ with $Q_B:=Q_B^{poly,\,num}\cdot t_L$, now a fully polynomial identity in all
variables (verified: every coefficient appearing, on both sides, is manifestly polynomial — no
denominators in $t_K,t_L,ca,sa,p,q,a$ remain). This full polynomial identity was re-verified this round
by exact rational substitution at four independent points (see Appendix), each giving literal $0$ for
the difference of the two sides. $\blacksquare$

### Conclusion, conditional on the branch-selection gap

**If** hypotheses (ii),(iii) can be shown to imply $g_1=0$ and $g_2=0$ (the precise content of Lemma 2's
"$\iff$" claim — see the honest discussion in "Branch-selection gap" immediately below for why this
implication is not yet fully justified), **then** substituting into $(\star)$:
$$2Z^2\cdot\mathrm{myexpr} = 0.$$
By Lemma 3, $Z>0$, so $Z^2>0$, hence $\mathrm{myexpr}=0$. By Lemma 1, $\mathrm{myexpr}=0\iff OM=ON$.

This would hold for **every** valid configuration satisfying the problem's hypotheses — no case split on
$AB=AC$ vs. $AB\ne AC$ is needed (Lemma 1's identity never divides by $p-a/2$), and no case split on the
sign or range of $\alpha$ beyond what Lemma 3 already handles uniformly (via the interior-point
hypothesis on $K$ alone). **This is the entire remaining logical content of the problem** — the rest of
this proof (Lemmas 1–3, the decoupling of Lemma 2's polynomial identity, and the cofactor identity
$(\star)$) is complete and unconditional. What is NOT yet established is the hypothesis of this
conditional, i.e. that (ii),(iii) really do force $g_1=g_2=0$ (as opposed to forcing $e_1,e_2$ to vanish
via a different, spurious sign branch, or not translating to $e_1=e_2=0$ at all along one of the two
signed alternatives consistent with the literal unsigned-angle hypothesis) — see below.

### Branch-selection gap (this round's attempt — genuine partial progress, not closed)

**Precisely what is missing, restated in this file's own notation.** Hypothesis (ii) is the *unsigned*
angle equality $\angle LBK=\angle LNC$. Write, for any two nonzero planar vectors $u,v$, the *directed*
angle from $u$ to $v$ (mod $2\pi$, valued in $(-\pi,\pi]$) as $\angle(u,v)$; then
$\mathrm{cross}(u,v)=|u||v|\sin\angle(u,v)$ and $\mathrm{dot}(u,v)=|u||v|\cos\angle(u,v)$. Let
$\theta_1:=\angle(L{-}B,K{-}B)$ and $\theta_2:=\angle(L{-}N,C{-}N)$. A direct expansion using these two
identities gives
$$e_1=\mathrm{cross}(L{-}B,K{-}B)\,\mathrm{dot}(L{-}N,C{-}N)-\mathrm{cross}(L{-}N,C{-}N)\,\mathrm{dot}(L{-}B,K{-}B)
=|L{-}B||K{-}B||L{-}N||C{-}N|\sin(\theta_1-\theta_2),$$
using $\sin\theta_1\cos\theta_2-\cos\theta_1\sin\theta_2=\sin(\theta_1-\theta_2)$. Since the four norm
factors are strictly positive (all four points are pairwise distinct on the valid locus — $K\ne B$,
$L\ne N$ etc., which hold since $K,L$ are interior to non-degenerate triangles not containing $B,N$ as
interior points), $e_1=0\iff\sin(\theta_1-\theta_2)=0\iff\theta_1=\theta_2\text{ or }\theta_1=\theta_2+\pi
\pmod{2\pi}$.

Meanwhile hypothesis (ii), the *unsigned* equality $\angle LBK=\angle LNC$ (both a genuine angle of a
triangle-like configuration, hence in $(0,\pi)$), means $|\theta_1|=|\theta_2|$, i.e.
$\theta_1=\theta_2$ **or** $\theta_1=-\theta_2 \pmod{2\pi}$ (taking $\theta_1,\theta_2\in(-\pi,\pi]$).

**These two descriptions of "the two branches" are different sets** ($\{\theta_1=\theta_2,\
\theta_1=\theta_2+\pi\}$ vs. $\{\theta_1=\theta_2,\ \theta_1=-\theta_2\}$), sharing only the branch
$\theta_1=\theta_2$. So Lemma 2's claimed equivalence "hypothesis (ii) $\iff g_1(t_L)=0$" is, strictly,
only justified in the direction actually needed for the conditional conclusion above — namely proving
that **on the geometrically valid locus** (all five hypotheses plus both interiority and both position
hypotheses), the branch realized is $\theta_1=\theta_2$ and never $\theta_1=-\theta_2$ (so that hyp (ii)
does force $e_1=0$, landing specifically on its "correct" $\theta_1=\theta_2$ component rather than the
spurious $\theta_1=\theta_2+\pi$ component of $\{e_1=0\}$, which is a strictly weaker, different
condition — geometrically, $\theta_1=\theta_2+\pi$ corresponds to the *supplementary* relation
$\angle LBK+\angle LNC=\pi$, not equality). Closing the gap fully requires ruling out **both** rival
possibilities on the valid locus: (I) $\theta_1=-\theta_2$ (a genuine solution of hyp (ii) but not of
$e_1=0$, which would falsify the whole reduction to $g_1=0$), and (II) $\theta_1=\theta_2+\pi$ (a
solution of $e_1=0$ that is not implied by hyp (ii)). Symmetric statements hold for hyp (iii), $e_2$,
$\theta_1':=\angle(L{-}C,K{-}C)$, $\theta_2':=\angle(B{-}M,K{-}M)$.

**What this round closes: a rigorous bound $\sin\theta_1>0$, $\sin\theta_1'>0$ from the position
hypotheses at $B,C$.** This directly rules out possibility (I) in the special case $\theta_2<0$ or
$\theta_2>\pi$ is avoided, and (partially) narrows possibility (II); see below for the exact statement
and what remains.

**Ray-Betweenness Lemma (proved in full this round, extending the certified `interior-point-side-test.md`
toolkit — cross-product bilinearity — to convex angular sectors instead of half-planes).** Let $B$ be a
point and $d_1,d_2$ two directions from $B$ (i.e. $\varphi_A,\varphi_L$ the angles of nonzero vectors
$A-B,\,L-B$) with $\angle ABL:=|\varphi_L-\varphi_A|\in(0,\pi)$ (mod $2\pi$, principal value), i.e. a
proper convex angle. For a further nonzero vector $K-B$ with angle $\varphi_K$, TFAE:
(1) ray $BK$ lies in the interior of the convex angular sector between rays $BA,BL$ (equivalently
$\varphi_K=\varphi_A+u(\varphi_L-\varphi_A)$ for some $u\in(0,1)$, taking $\varphi_L-\varphi_A\in(-\pi,\pi)$);
(2) $\mathrm{sign}(\mathrm{cross}(A{-}B,K{-}B))=\mathrm{sign}(\mathrm{cross}(A{-}B,L{-}B))$ **and**
$\mathrm{sign}(\mathrm{cross}(L{-}B,K{-}B))=\mathrm{sign}(\mathrm{cross}(L{-}B,A{-}B))$.

*Proof.* WLOG (reflecting the whole configuration in line $AB$, an isometry, if necessary) assume
$\delta:=\varphi_L-\varphi_A\in(0,\pi)$, so $\mathrm{cross}(A{-}B,L{-}B)=|A{-}B||L{-}B|\sin\delta>0$.
Write $u:=\varphi_K-\varphi_A$ (a representative in $(-\pi,\pi]$, using that $K\ne B$). Condition (1)
is $u\in(0,\delta)$. For condition (2): the first sign equality is
$\mathrm{sign}(\sin u)=\mathrm{sign}(\sin\delta)=+1$, i.e. $\sin u>0$, i.e. $u\in(0,\pi)$ (using
$u\in(-\pi,\pi]$). The second sign equality is $\mathrm{sign}(\sin(\varphi_K-\varphi_L))=
\mathrm{sign}(\sin(\varphi_A-\varphi_L))=\mathrm{sign}(\sin(-\delta))=-1$ (since $\delta\in(0,\pi)$), i.e.
$\sin(u-\delta)<0$; given $u\in(0,\pi)$ from the first equality, $u-\delta\in(-\delta,\pi-\delta)\subset
(-\pi,\pi)$, so $\sin(u-\delta)<0\iff u-\delta\in(-\pi,0)\iff u<\delta$. Combining $u\in(0,\pi)$ and
$u<\delta$ (with $\delta<\pi$) gives exactly $u\in(0,\delta)$, i.e. condition (1). This chain of
equivalences is reversible, proving (1)$\iff$(2). $\blacksquare$

**Application at vertex $B$ (hyp (ii) side).** The problem's position hypothesis "$K$ inside
$\angle LBA$" is exactly condition (1) of the Ray-Betweenness Lemma with $A,L,K$ as given (note
$\angle LBA\in(0,\pi)$ automatically, as a genuine angle of the configuration). So condition (2) holds:
$$\mathrm{sign}(\mathrm{cross}(A{-}B,K{-}B))=\mathrm{sign}(\mathrm{cross}(A{-}B,L{-}B)),\qquad
\mathrm{sign}(\mathrm{cross}(L{-}B,K{-}B))=\mathrm{sign}(\mathrm{cross}(L{-}B,A{-}B)).$$
Writing $B=0$, $w:=A-B$: since $K=t_KR(-\alpha)w$ ($t_K>0$), the identity $\mathrm{cross}(w,R(\theta)w)=
|w|^2\sin\theta$ (immediate from expanding $R(\theta)w=(w_1\cos\theta-w_2\sin\theta,\,
w_1\sin\theta+w_2\cos\theta)$ and computing $\mathrm{cross}(w,R(\theta)w)=w_1^2\sin\theta+w_2^2\sin\theta$)
gives $\mathrm{cross}(A{-}B,K{-}B)=-t_K|AB|^2\sin\alpha<0$ (Lemma 3's $\sin\alpha>0$). Write
$L-B=r\,R(-\beta)w$ for the unique $r>0,\ \beta\in(-\pi,\pi]$ with this representation ($L\ne B$ since
$L$ is interior to $\triangle BNC$, so $r,\beta$ exist and are well-defined). Then
$\mathrm{cross}(A{-}B,L{-}B)=-r|AB|^2\sin\beta$. The first sign equality above forces
$-r|AB|^2\sin\beta<0$, i.e. $\sin\beta>0$, i.e. $\beta\in(0,\pi)$ (taking the representative in
$(0,\pi)$, using $r,|AB|^2>0$). Using $\mathrm{cross}(R(\theta_1)w,R(\theta_2)w)=|w|^2\sin(\theta_2-\theta_1)$
(since $\det R=1$, $\mathrm{cross}(Ru,Rv)=\mathrm{cross}(u,v)$, so
$\mathrm{cross}(R(\theta_1)w,R(\theta_2)w)=\mathrm{cross}(w,R(\theta_2-\theta_1)w)=|w|^2\sin(\theta_2-\theta_1)$),
$$\mathrm{cross}(L{-}B,K{-}B)=rt_K\,\mathrm{cross}(R(-\beta)w,R(-\alpha)w)=rt_K|AB|^2\sin(\beta-\alpha).$$
The second sign equality forces this to have the same sign as $\mathrm{cross}(L{-}B,A{-}B)=
-\mathrm{cross}(A{-}B,L{-}B)=+r|AB|^2\sin\beta>0$, so $\sin(\beta-\alpha)>0$; since
$\alpha,\beta\in(0,\pi)$ give $\beta-\alpha\in(-\pi,\pi)$, this forces $\beta-\alpha\in(0,\pi)$, i.e.
$\beta>\alpha$. Finally, $\theta_1=\angle(L{-}B,K{-}B)$: since $L-B=rR(-\beta)w$ has angle
$\varphi_A-\beta$ and $K-B=t_KR(-\alpha)w$ has angle $\varphi_A-\alpha$ (where $\varphi_A$ is the angle
of $w=A-B$), $\theta_1=(\varphi_A-\alpha)-(\varphi_A-\beta)=\beta-\alpha\in(0,\pi)$.
**Conclusion: $\sin\theta_1>0$**, i.e. $\theta_1\in(0,\pi)$ strictly, established rigorously (not
numerically) from the position hypothesis "$K$ inside $\angle LBA$" together with the already-certified
$\sin\alpha>0$.

**Application at vertex $C$ (hyp (iii) side), symmetric.** The position hypothesis "$L$ inside
$\angle ACK$" is condition (1) of the Ray-Betweenness Lemma at $C$ with $A,K,L$ in place of $A,L,K$.
With $w':=A-C$, $L-C=t_LR(\alpha)w'$, and writing $K-C=s\,R(\gamma)w'$ for the unique $s>0,\gamma\in
(-\pi,\pi]$: $\mathrm{cross}(A{-}C,L{-}C)=t_L|AC|^2\sin\alpha>0$ (Lemma 3's $\sin\alpha>0$ again).
Condition (2)'s first equality forces $\mathrm{cross}(A{-}C,K{-}C)=s|AC|^2\sin\gamma>0$, so
$\gamma\in(0,\pi)$. The second equality forces $\mathrm{cross}(K{-}C,L{-}C)$ to match the sign of
$\mathrm{cross}(K{-}C,A{-}C)=-s|AC|^2\sin\gamma<0$; and
$\mathrm{cross}(K{-}C,L{-}C)=st_L\,\mathrm{cross}(R(\gamma)w',R(\alpha)w')=st_L|AC|^2\sin(\alpha-\gamma)$,
so $\sin(\alpha-\gamma)<0$, and with $\alpha,\gamma\in(0,\pi)$ this forces $\gamma>\alpha$. Then
$\theta_1':=\angle(L{-}C,K{-}C)=\gamma-\alpha\in(0,\pi)$, so **$\sin\theta_1'>0$**, symmetric to the
$B$-vertex conclusion above.

**What remains open (honestly, not closed this round).**
1. *The $N$-vertex half (for hyp (ii)) and $M$-vertex half (for hyp (iii)).* The two bounds above only
   control $\theta_1,\theta_1'$ — the angles at $B,C$ — into $(0,\pi)$. Nothing in the problem's stated
   hypotheses gives a direct position/interiority constraint on $K,L$ relative to $N$ (or $M$), so
   $\theta_2:=\angle(L{-}N,C{-}N)$ (resp. $\theta_2':=\angle(B{-}M,K{-}M)$) has no established range from
   this mechanism. Even granting $\theta_1\in(0,\pi)$, this alone does not resolve $\sin(\theta_1-\theta_2)=0$'s
   branch unless $\theta_2$'s range is also pinned down (e.g. $\theta_2\in(0,\pi)$ too would, combined
   with $\theta_1\in(0,\pi)$, put $\theta_1-\theta_2\in(-\pi,\pi)$, forcing the vanishing of
   $\sin(\theta_1-\theta_2)$ to mean exactly $\theta_1=\theta_2$ — but $\theta_2\in(0,\pi)$ is not proved).
   This is the same open item flagged by this round's `math-explorer-branchselect.md` and by the
   `synthetic-angle-chase-aklastar` outline; both mechanisms it proposes as a fallback (bounding via a
   discriminator sign identity, or the "matching-sign of the two dot products" conjecture, numerically
   supported at 1450/1450 sampled configurations but not proved) remain unproved in this file too.
2. *The possibility-(I) subtlety identified above.* Even with $\theta_1\in(0,\pi)$ established, ruling
   out $\theta_1=-\theta_2$ (rather than $\theta_1=\theta_2$) as the branch actually realized by hyp
   (ii) requires knowing $\theta_2$'s sign as well — again blocked on item 1.

**Honest verdict:** this round makes genuine, independently-derived progress (the Ray-Betweenness Lemma,
proved from scratch and fully general, plus its two applications giving $\sin\theta_1>0,\sin\theta_1'>0$
in closed form, not numerically) but the branch-selection gap is **not closed**. The conditional
conclusion in the previous subsection therefore remains conditional; `Status` is `partial`.

### Existence / consistency check (numerical, corroborating but not part of the logical proof)

To confirm the parametrization's rotation-sign convention (rotating $BA$ by $-\alpha$ for ray $BK$,
$CA$ by $+\alpha$ for ray $CL$) genuinely matches configurations satisfying **all** of the problem's
hypotheses simultaneously (hypothesis (i)–(iii) together with "$K$ inside $\triangle BMC$", "$L$ inside
$\triangle BNC$", "$K$ inside $\angle LBA$", "$L$ inside $\angle ACK$"), a direct numerical search was
performed this round (2000 random triangles/angles, solving $g_1=0,g_2=0$ for all root-pairs with
$t_K,t_L>0$, and checking all hypotheses by direct coordinate computation): hundreds of genuine valid
configurations were found (e.g. $p=1.408,q=3.740,a=1.355,\alpha=0.168$ rad, giving $t_K\approx0.34613$,
$t_L\approx0.31261$), and for one such configuration the circumcenter $O$ of $A,K,L$ was computed
directly and found to satisfy $OM=ON$ to floating-point precision ($OM\approx0.6891216438535889$,
$ON\approx0.6891216438535894$, agreeing to $12$ significant digits). This corroborates that the
algebraic machinery above is not vacuous (genuine valid configurations exist matching the chosen
branch) and that its conclusion matches direct numerical computation of $OM,ON$.

### Appendix: exact re-runnable computation

```python
import sympy as sp
p,q,a,ca,sa,tK,tL = sp.symbols('p q a ca sa tK tL', real=True)
B=sp.Matrix([0,0]); C=sp.Matrix([a,0]); A=sp.Matrix([p,q])
M=(A+B)/2; N=(A+C)/2
K=sp.Matrix([tK*(p*ca+q*sa), tK*(q*ca-p*sa)])
L=sp.Matrix([a+tL*((p-a)*ca-q*sa), tL*(q*ca+(p-a)*sa)])
cross=lambda u,v: u[0]*v[1]-u[1]*v[0]
dot=lambda u,v: u[0]*v[0]+u[1]*v[1]
e1=sp.expand(cross(L-B,K-B)*dot(L-N,C-N)-cross(L-N,C-N)*dot(L-B,K-B))
e2=sp.expand(cross(L-C,K-C)*dot(B-M,K-M)-cross(B-M,K-M)*dot(L-C,K-C))
u=K-A; v=L-A
myexpr=sp.expand((p-a*sp.Rational(1,2))*cross(u,v)+v[1]*(u[0]**2+u[1]**2)-u[1]*(v[0]**2+v[1]**2))

D = 2*a*ca*q-2*a*p*sa+2*p**2*sa+2*q**2*sa   # = D = 2Z
g1 = (a*ca*q-a*p*sa) + tL*(-2*a*ca**2*q+2*a*ca*p*sa-a*q-2*ca*p**2*sa-2*ca*q**2*sa) + tL**2*D
g2 = (a*ca*q-a**2*sa+a*p*sa) + tK*(-2*a*ca**2*q+2*a*ca*p*sa-a*q-2*ca*p**2*sa-2*ca*q**2*sa) + tK**2*D

def reduce_mod_circle(expr):
    e = sp.expand(expr)
    changed = True
    while changed:
        new_e = sp.expand(e.replace(lambda x: x.is_Pow and x.base==sa and x.exp>=2,
                                     lambda x: (1-ca**2)*sa**(x.exp-2) if x.exp>=2 else x))
        changed = (new_e != e); e = new_e
    return e

# check e1 = tK*(|AC|^2/4)*g1, e2 = tL*(|AB|^2/4)*g2   (both check to 0)
AC2 = a**2-2*a*p+p**2+q**2; AB2 = p**2+q**2
assert sp.simplify(reduce_mod_circle(sp.expand(e1-tK*(AC2/4)*g1))) == 0
assert sp.simplify(reduce_mod_circle(sp.expand(e2-tL*(AB2/4)*g2))) == 0

myexpr_r = reduce_mod_circle(myexpr)
Q1,R1 = sp.div(myexpr_r, g1, tL, domain='EX')
assert sp.cancel(myexpr_r - (Q1*g1+R1)) == 0
R1 = sp.expand(R1); R1p = sp.Poly(R1, tL)
Acoef = R1p.nth(0); Bcoef = R1p.nth(1) if R1p.degree()>=1 else 0
Z = D/2
P1 = sp.expand(sp.cancel(D*Q1))
Anum = sp.expand(sp.cancel(D*Acoef)); Bnum = sp.expand(sp.cancel(D*Bcoef))
Anum_r = reduce_mod_circle(Anum); Bnum_r = reduce_mod_circle(Bnum)
QA,RA = sp.div(Anum_r, g2, tK, domain='EX')
QB,RB = sp.div(Bnum_r, g2, tK, domain='EX')
assert sp.simplify(reduce_mod_circle(sp.expand(RA))) == 0
assert sp.simplify(reduce_mod_circle(sp.expand(RB))) == 0
QB_poly = sp.expand(sp.cancel(Z*QB))   # clears the residual Z-denominator in QB

lhs = sp.expand(2*Z**2*myexpr)
rhs = sp.expand(Z*P1*g1 + (Z*QA+QB_poly*tL)*g2)
diff = sp.together(lhs-rhs)
# exact rational-point checks (all give 0):
for s in [
    {p:sp.Rational(7,3), q:sp.Rational(11,5), a:sp.Rational(9,2), ca:sp.Rational(3,5), sa:sp.Rational(4,5), tK:sp.Rational(2,3), tL:sp.Rational(5,7)},
    {p:sp.Rational(-2), q:sp.Rational(13,4), a:sp.Rational(5), ca:sp.Rational(-7,25), sa:sp.Rational(24,25), tK:sp.Rational(-3,2), tL:sp.Rational(9,5)},
    {p:sp.Rational(1), q:sp.Rational(1), a:sp.Rational(1), ca:sp.Rational(0), sa:sp.Rational(1), tK:sp.Rational(1,2), tL:sp.Rational(1,3)},
    {p:sp.Rational(1,7), q:sp.Rational(6), a:sp.Rational(2), ca:sp.Rational(-3,5), sa:sp.Rational(-4,5), tK:sp.Rational(11,10), tL:sp.Rational(-2,3)},
]:
    assert sp.simplify(diff.subs(s)) == 0
print("All checks passed.")
```
All `assert`s in the script above pass (verified this round by direct execution); this reproduces
every algebraic claim in the proof, including the fully-cleared-denominator identity $(\star)$.

## Promotable lemmas
- **Ray-Betweenness Lemma (new this round).** For a vertex $B$ and three nonzero vectors $A-B,L-B,K-B$
  with $\angle ABL\in(0,\pi)$: ray $BK$ lies in the interior of the convex angular sector between rays
  $BA,BL$ **iff** $\mathrm{sign}(\mathrm{cross}(A{-}B,K{-}B))=\mathrm{sign}(\mathrm{cross}(A{-}B,L{-}B))$
  and $\mathrm{sign}(\mathrm{cross}(L{-}B,K{-}B))=\mathrm{sign}(\mathrm{cross}(L{-}B,A{-}B))$. Proved in
  full in the "Branch-selection gap" section above, by reducing both sides to statements about the sign
  of $\sin$ of an angle difference (self-contained trigonometric argument, general — not specific to this
  problem beyond its two applications here). Extends the certified `interior-point-side-test.md`
  cross-product-bilinearity toolkit from half-plane (single line) tests to convex-angular-sector (two
  lines through a common point) tests. Reusable by `synthetic-angle-chase-aklastar` and by future
  problems needing to translate a "ray between two rays" position hypothesis into sign constraints.
  **Status: proved in full, no gaps.** Two direct applications (also proved in full above, using this
  lemma plus the already-certified $\sin\alpha>0$ fact) establish $\sin\theta_1>0$ (vertex-$B$ side of
  hyp (ii)'s branch) and $\sin\theta_1'>0$ (vertex-$C$ side of hyp (iii)'s branch) — genuine closed-form
  partial progress on the branch-selection gap, though NOT a full closure (the vertex-$N$/vertex-$M$
  halves, per the "What remains open" discussion above, are still missing).
- **Lemma (Z>0 on the geometrically valid locus).** With $B=(0,0)$, $C=(a,0)$ ($a>0$), $A=(p,q)$
  ($q>0$), $M=(p/2,q/2)$ the midpoint of $AB$, and $K$ parametrized as
  $K=(t_K(p\,ca+q\,sa),\,t_K(q\,ca-p\,sa))$ for $t_K>0$ (where $ca=\cos\alpha,sa=\sin\alpha$, i.e. $K$
  is at signed angle $\alpha$ from ray $BA$): if $K$ is strictly interior to triangle $BMC$, then
  $X:=q\,ca-p\,sa>0$ and $sa>0$, hence $Z:=aX+sa(p^2+q^2)>0$. Proved in full above (§ "$X>0$ and
  $\sin\alpha>0$, hence $Z>0$") via two parallel barycentric-coordinate computations. This resolves,
  for both this file and the sibling `synthetic-angle-chase-aklastar` (whose "$Z$" is the identical
  quantity under the corresponding convention), the previously-open $Z\ne0$ gap — with a strictly
  stronger $Z>0$ conclusion, and a self-contained proof of $\sin\alpha>0$ (not merely $\alpha\ne0$)
  that does not appeal to the weaker "not on ray $BA$" argument. Reusable verbatim by the sibling
  approach.
- **Lemma (fully-polynomial cofactor identity).** $2Z^2\cdot\mathrm{myexpr} = (Z P_1)g_1+(ZQ_A+Q_B)g_2$
  as an identity of polynomials (no residual denominators) in $t_K,t_L,ca,sa,p,q,a$ modulo
  $ca^2+sa^2=1$, for explicit $P_1,Q_A,Q_B$ computable by the Appendix script. Proved in full above.
