## Status
solved

## Approaches tried
- `synthetic-angle-chase-aklastar` — **SOLVED, verified by reviewer.** Rounds 2–4 built up the full
  coordinate-reduction chain (circumcenter-x-coordinate reduction, rotation-parametrization of $K,L$
  with a rigorously forced sign convention, the decoupling of hypotheses (ii),(iii) into quadratics
  $A_1(T_L)=0,B_1(T_K)=0$, the unconditional cofactor identity
  $\mathrm{myexpr}\cdot Z = 2(q-T_KX)A_1+2(T_LX'-q)B_1$, and $Z>0$ via a barycentric interiority
  argument). Round 5 closed the last remaining gap — the directed-angle branch-selection for
  hypotheses (ii),(iii) — via a new **ray-betweenness sign lemma** (proved from scratch, a two-case
  directed-angle argument) applied at vertices $B,C$ using the position hypotheses "K inside
  $\angle LBA$"/"L inside $\angle ACK$", combined with two *new* applications of the already-certified
  `interior-point-side-test.md` lemma at vertices $N,M$ (on previously-unused edges $NC$ of
  $\triangle BNC$ and $MB$ of $\triangle BMC$). Together these pin all four relevant directed angles
  strictly into $(0,\pi)$, which — via the elementary fact "unsigned angle = |directed angle|" —
  converts the literal unsigned-angle hypotheses (ii),(iii) into **exact** directed-angle equalities
  (not merely equalities of absolute values), closing the branch ambiguity completely and in closed
  form (no numerics load-bearing). Reviewer independently re-verified every step from scratch (see
  "Full proof" below and the reviewer's verification notes).
- `coordinate-groebner-elimination` — Status **partial** (self-assessed correctly). Independently
  proved the identical cofactor identity and $Z>0$ argument as its sibling, and this round closed
  *half* of the branch-selection gap (the vertex-$B$/vertex-$C$ sides, via its own independently
  discovered "Ray-Betweenness Lemma", essentially the same fact as the certified
  `ray-betweenness-sign-lemma.md`), but explicitly left the vertex-$N$/vertex-$M$ halves open — the
  sibling closed those (via reusing `interior-point-side-test.md` on new edges) while this file did
  not. Genuine, honestly-scoped progress; not a third overclaim. Kept live per CLAUDE.md diversity
  guidance, though the problem itself is now closed via the sibling.
- `inversion-at-a-collinearity` — Status **partial** (self-assessed correctly). Found a genuinely new
  mechanism (Lemma 4, a cross-ratio-based "vertex-swap angle-to-concyclicity translation" needing no
  inversion center) that does translate hypotheses (ii),(iii) into explicit concyclicity statements —
  answering the round-4 diagnosis that these hypotheses were "invisible" to the single-inversion-center
  approach. The resulting three-concyclic-quadruple system (target + two new facts) is not yet chased
  to a closed loop; real structural progress, genuine remaining gap, kept live as an independent
  framing/hedge.
- `isosceles-locus-direct` — cut in round 2 (RETHINK), not revisited.

## Current best
(Superseded — see Full proof below.)

## Full proof

### Setup and reduction to a scalar identity

Place $B=(0,0)$, $C=(a,0)$ with $a>0$, and $A=(p,q)$ with $q>0$ (similarity normalization: rotate,
translate, scale so $BC$ lies on the $x$-axis with $B$ left of $C$, reflect if necessary so $A$ is
above the axis — none of the hypotheses or the conclusion depend on the choice of representative).
Then $M=\tfrac12(A+B)=(p/2,q/2)$, $N=\tfrac12(A+C)=((p+a)/2,q/2)$.

**Step 0.** $M,N$ have equal $y$-coordinate $q/2$, so their perpendicular bisector is the vertical
line $x=\mathrm{target}:=\dfrac{2p+a}{4}$. For the circumcenter $O=(O_x,O_y)$ of $\triangle AKL$:
$$OM=ON \iff O_x=\mathrm{target}.$$

**Step 1 (circumcenter formula).** Translate so $A$ is the origin: $u=K-A=(u_1,u_2)$, $v=L-A=(v_1,v_2)$.
The circumcenter $O'=(x_0,y_0)$ of $0,u,v$ satisfies $2u_1x_0+2u_2y_0=|u|^2$, $2v_1x_0+2v_2y_0=|v|^2$.
The determinant $\mathrm{cross}(u,v)=u_1v_2-u_2v_1\neq0$ since $A,K,L$ are non-collinear (a genuine
triangle by hypothesis). By Cramer's rule, $x_0=(|u|^2v_2-|v|^2u_2)/(2\,\mathrm{cross}(u,v))$. Since
$O_x=p+x_0$,
$$O_x-\mathrm{target} = \frac{\mathrm{myexpr}}{2\,\mathrm{cross}(u,v)},\qquad
\mathrm{myexpr}:=(p-\tfrac a2)\,\mathrm{cross}(u,v)+|u|^2v_2-|v|^2u_2.$$
Hence $OM=ON \iff \mathrm{myexpr}=0$ — this never divides by $p-a/2$, so $AB=AC$ needs no separate
case. (Certified: `lemmas/circumcenter-x-coordinate-reduction.md`; reviewer independently re-derived
$O_x-\mathrm{target}-\mathrm{myexpr}/(2\,\mathrm{cross}(u,v))=0$ symbolically.)

### Parametrizing $K,L$ using hypothesis (i), with a rigorous sign justification

Hypothesis (i): $\angle KBA=\angle ACL=:\alpha$. Set $T_K:=|BK|/|BA|>0$, $T_L:=|CL|/|CA|>0$. The two
candidate parametrizations are $K=B+T_KR(\mp\alpha)(A-B)$, similarly for $L$.

**Side test** (certified `lemmas/interior-point-side-test.md`): if $\triangle PQR$ has $P,Q$ on line
$\ell$ and $R\notin\ell$, every interior point lies strictly on $R$'s side of $\ell$. Applying with
$(P,Q,R)=(B,M,C)$ on line $AB$: $K$ (interior to $\triangle BMC$) lies on $C$'s side of line $AB$.
Since $\mathrm{cross}(A-B,C-B)=-qa<0$, $\mathrm{cross}(A-B,K-B)<0$. Direct computation with
$K=B+T_KR(-\alpha)(A-B)$ gives $\mathrm{cross}(A-B,K-B)=-T_Ks(p^2+q^2)$ ($s=\sin\alpha$), negative
iff $s>0$. Symmetrically at $C$ with $(P,Q,R)=(C,N,B)$ on line $AC$: $\mathrm{cross}(A-C,L-C)>0$ (since
$\mathrm{cross}(A-C,B-C)=qa>0$), and with $L=C+T_LR(\alpha)(A-C)$,
$\mathrm{cross}(A-C,L-C)=T_Ls((a-p)^2+q^2)$, positive iff $s>0$ — same condition. So:
$$K=B+T_K\,R(-\alpha)(A-B),\qquad L=C+T_L\,R(\alpha)(A-C),\qquad T_K,T_L>0. \tag{$\ast$}$$

**Recorded for later (F1):** $\mathrm{cross}(A-B,K-B)=-T_Ks(p^2+q^2)<0$,
$\mathrm{cross}(A-C,L-C)=T_Ls((a-p)^2+q^2)>0$.

### $\sin\alpha>0$

Write $K=\lambda B+\mu M+\nu C$ ($\lambda,\mu,\nu>0$, barycentric interior point). Then
$K_y=\mu q/2>0$. Line $AB$: $py-qx=0$; substituting $K$'s coordinates gives $-\nu qa\neq0$, so
$K\notin$ line $AB$, hence $\alpha=\angle KBA\in(0,\pi)$ strictly, so $s=\sin\alpha>0$. Also
$K_y=\mu q/2>0$.

### Hypotheses (ii),(iii) as polynomial equations

For nonzero $X,Y,W,Z$, with $\theta_1$ the directed angle ($\in(-\pi,\pi]$) from $X$ to $Y$ and
$\theta_2$ from $W$ to $Z$: $\mathrm{cross}(X,Y)\mathrm{dot}(W,Z)-\mathrm{cross}(W,Z)\mathrm{dot}(X,Y)
=|X||Y||W||Z|\sin(\theta_1-\theta_2)$ (angle-subtraction identity; direct from
$\mathrm{cross}=|\cdot||\cdot|\sin\theta$, $\mathrm{dot}=|\cdot||\cdot|\cos\theta$). Define
$$e_1:=\mathrm{cross}(L-B,K-B)\mathrm{dot}(L-N,C-N)-\mathrm{cross}(L-N,C-N)\mathrm{dot}(L-B,K-B),$$
$$e_2:=\mathrm{cross}(L-C,K-C)\mathrm{dot}(B-M,K-M)-\mathrm{cross}(B-M,K-M)\mathrm{dot}(L-C,K-C).$$
Let $\theta_1$: directed angle $L-B\to K-B$; $\theta_2$: $L-N\to C-N$; $\theta_1'$: $L-C\to K-C$;
$\theta_2'$: $B-M\to K-M$. Then $e_1=|L{-}B||K{-}B||L{-}N||C{-}N|\sin(\theta_1-\theta_2)$,
$e_2=|L{-}C||K{-}C||B{-}M||K{-}M|\sin(\theta_1'-\theta_2')$ (all four norm factors nonzero: $K,L$ are
strictly interior to their triangles, hence distinct from the triangles' vertices $B,C,M,N$).

**Unsigned angle = |directed angle|** (certified `lemmas/unsigned-angle-equals-abs-directed-angle.md`):
for nonzero $X,Y$ with directed angle $\theta\in(-\pi,\pi]$, the standard unsigned angle
$\angle(X,Y)=\arccos(\mathrm{dot}(X,Y)/(|X||Y|))=|\theta|$. Hence $\angle LBK=|\theta_1|$,
$\angle LNC=|\theta_2|$, $\angle LCK=|\theta_1'|$, $\angle BMK=|\theta_2'|$; hypothesis (ii) says
$|\theta_1|=|\theta_2|$ and (iii) says $|\theta_1'|=|\theta_2'|$ — a priori consistent with either sign
relation in each pair. Step 7 below pins all four angles strictly positive, forcing exact equality.

### Step 7: pinning the signs of $\theta_1,\theta_2,\theta_1',\theta_2'$

**Ray-betweenness sign lemma** (certified `lemmas/ray-betweenness-sign-lemma.md`): if $P,Q\notin$ line
$VR$ and $P$ lies in the interior of $\angle RVQ$ (same side of line $VR$ as $Q$, and same side of
line $VQ$ as $R$), then $\mathrm{sign}(\mathrm{cross}(P-V,Q-V))=\mathrm{sign}(\mathrm{cross}(R-V,P-V))$.

- **Vertex $B$:** "$K$ inside $\angle LBA$" is $P=K$ interior to $\angle RVQ$ with $V=B,R=A,Q=L$. The
  lemma gives $\mathrm{sign}(\mathrm{cross}(K-B,L-B))=\mathrm{sign}(\mathrm{cross}(A-B,K-B))=-1$ (F1),
  so $\mathrm{cross}(L-B,K-B)>0$.
- **Vertex $C$:** "$L$ inside $\angle ACK$" is $P=L$ interior to $\angle RVQ$ with $V=C,R=A,Q=K$. The
  lemma gives $\mathrm{sign}(\mathrm{cross}(L-C,K-C))=\mathrm{sign}(\mathrm{cross}(A-C,L-C))=+1$ (F1).
- **Vertex $N$** (via `interior-point-side-test.md` on a new edge): with $(P,Q,R)=(N,C,B)$ for
  $\triangle BNC$, $L$ (interior) lies on $B$'s side of line $NC$. Direct computation:
  $\mathrm{cross}(C-N,B-N)=-qa/2<0$, so $\mathrm{cross}(L-N,C-N)>0$.
- **Vertex $M$** (same lemma, new edge): with $(P,Q,R)=(M,B,C)$ for $\triangle BMC$, $K$ (interior)
  lies on $C$'s side of line $MB$. $\mathrm{cross}(B-M,C-M)=qa/2>0$, so $\mathrm{cross}(B-M,K-M)>0$
  directly.

All four cross products strictly positive $\Rightarrow$ $\theta_1,\theta_2,\theta_1',\theta_2'\in(0,\pi)$
(each equals its own absolute value). Hypothesis (ii) $|\theta_1|=|\theta_2|$ with both positive forces
the **exact** equality $\theta_1=\theta_2$ (not merely $|\theta_1|=|\theta_2|$), giving
$e_1=(\cdots)\sin(0)=0$. Identically $\theta_1'=\theta_2'$, giving $e_2=0$.

### Decoupling

**Certified** `lemmas/ray-parametrized-angle-decoupling.md`: $e_1=T_K\cdot A_1(T_L,c,s,p,q,a)$,
$e_2=T_L\cdot B_1(T_K,c,s,p,q,a)$ ($A_1$ free of $T_K$, $B_1$ free of $T_L$). Since $T_K,T_L>0$:
$e_1=0\iff A_1=0$, $e_2=0\iff B_1=0$. With $X:=cq-ps$, $X':=cq+s(p-a)$, $Z:=aX+s(p^2+q^2)$:
$$A_1=\big((a-p)^2+q^2\big)\Big(\tfrac Z2T_L^2-(\tfrac{cZ}2+\tfrac{aq}4)T_L+\tfrac{aX}4\Big),\qquad
B_1=\big(p^2+q^2\big)\Big(\tfrac Z2T_K^2-(\tfrac{cZ}2+\tfrac{aq}4)T_K+\tfrac{aX'}4\Big).$$

### The closing identity

Exact polynomial identity (verified independently from scratch by the reviewer with sympy, both by
full symbolic reduction modulo $c^2+s^2-1$ down to literally $0$, and at multiple exact rational
Pythagorean-pair points):
$$\mathrm{myexpr}\cdot Z = 2(q-T_KX)A_1+2(T_LX'-q)B_1.$$
Since $A_1=0,B_1=0$ (established above), $\mathrm{myexpr}\cdot Z=0$.

### $Z>0$

$K_y=T_K\cdot X$ exactly (the $y$-component of $R(-\alpha)(A-B)$ is $X=cq-ps$). Since $K_y=\mu q/2>0$
and $T_K>0$, $X=K_y/T_K>0$. Also $s>0$, $p^2+q^2>0$, $a>0$, so $Z=aX+s(p^2+q^2)>0$ (sum of two
strictly positive terms). Hence $Z\neq0$, and $\mathrm{myexpr}\cdot Z=0$ gives $\mathrm{myexpr}=0$.

### Conclusion

By Step 0–1, $\mathrm{myexpr}=0\iff OM=ON$. Every step is unconditional, covering every triangle $ABC$
satisfying hypotheses (i)–(iii) plus the two position hypotheses and $K,L$ strictly interior to their
respective triangles, with no case split for $AB=AC$ vs. $AB\neq AC$. Therefore $OM=ON$ for every
valid configuration. $\blacksquare$

## Reviewer's independent verification (round 5)
- Re-derived $O_x-\mathrm{target}-\mathrm{myexpr}/(2\,\mathrm{cross}(u,v))=0$ symbolically (sympy):
  confirmed exactly.
- Re-derived and confirmed the base cross-product facts: $\mathrm{cross}(A-B,C-B)=-qa$,
  $\mathrm{cross}(A-C,B-C)=qa$, $\mathrm{cross}(C-N,B-N)=-qa/2$, $\mathrm{cross}(B-M,C-M)=qa/2$ (sympy).
- Independently stress-tested the ray-betweenness sign lemma on 200,000 random configurations
  (constructed independently of the formula being tested, via `atan2`-interpolation + explicit
  same-side filtering) — 0 failures.
- Independently re-derived the decoupling and the cofactor identity
  $\mathrm{myexpr}\cdot Z=2(q-T_KX)A_1+2(T_LX'-q)B_1$ from the raw coordinate definitions with sympy:
  confirmed both by exact rational-point substitution (3 independent Pythagorean-pair points) and by
  full symbolic reduction modulo $c^2+s^2-1$ to literally $0$.
- Constructed 340 genuinely valid numerical configurations end-to-end (solving the actual $g_1=0,g_2=0$
  system for random $(p,q,a,\alpha)$, filtering to those satisfying **all** position/interiority
  hypotheses by direct coordinate tests), spanning $\alpha\in(0.007,1.32)$ — substantially broader than
  the previously-flagged narrow sample (all prior samples shared $\alpha=0.05$). In every case: the
  four cross-product sign predictions (S1)–(S4) held, and $OM=ON$ held to floating-point precision (one
  example checked to 12 significant digits).
- Conclusion: the branch-selection gap that stalled this problem since round 4 (and the $Z\ne0$ gap
  since round 2) is genuinely closed. Status upgraded to **solved**.

## Promotable lemmas (this round)
- `lemmas/ray-betweenness-sign-lemma.md` — certified.
- `lemmas/unsigned-angle-equals-abs-directed-angle.md` — certified.
(All other lemmas cited above were already certified in prior rounds.)
