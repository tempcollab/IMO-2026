## Status
solved

**Round 5 update:** the one remaining gap flagged at the end of round 4 — rigorously identifying which
directed-angle branch of the unsigned hypotheses (ii) $\angle LBK=\angle LNC$ and (iii)
$\angle LCK=\angle BMK$ is realized by the position hypotheses ("K inside $\angle LBA$", "L inside
$\angle ACK$", $K,L$ strictly interior to $\triangle BMC,\triangle BNC$) — is now **closed in full**,
in closed form, with no numerical check standing in for a proof step. This closes the last open link
in the chain; the proof is complete. See "Full proof" below.

## Approaches tried
- Directed-angle chase toward "A, K, L, A* concyclic" (A* = rectangle-construction fixed point) —
  reformulation established and reduction to OM=ON verified. **Correction to a prior-round error:**
  the earlier draft of this file claimed "isosceles triangles ABM, ACN (BM=MA, CN=NA)" as a source
  of angle vocabulary. This is **false**: M is the midpoint of *segment* AB, so A, M, B are
  collinear — there is no triangle ABM. That "vocabulary" step is discarded.
- A genuine synthetic angle chase closing ∠(AK,AL) ≡ ∠(A*K,A*L) directly was **not found**. Round 4
  pivoted permanently to the **coordinate fallback**, executed in full.
- Symmetry-only isosceles fallback (prior round) — abandoned as insufficiently rigorous; the
  coordinate identity replaces it entirely (never divides by `p-a/2`, so `AB=AC` needs no
  separate case).
- Round 2: builder assembled the polynomial identity `myexpr·Z = 2(q−T_K X)·A1 + 2(T_L X'−q)·B1` but
  never proved `Z ≠ 0` on the geometrically valid locus — reviewer downgraded to `partial` on this
  single gap.
- Round 4: closed the `Z≠0` gap completely, with a corrected/strengthened `sin α>0` argument
  (excluding both `α=0` and `α=π`), re-derived the whole polynomial chain from scratch with sympy, and
  gave a fully rigorous (non-numeric) proof that the rotation-direction sign convention used to
  parametrize `K` and `L` is forced by the interiority hypotheses. Left one gap open: the branch
  selection for hypotheses (ii),(iii) was only justified by a five-configuration numeric check, so
  Status stayed `partial`.
- **Round 5 (this round):** closed the branch-selection gap in full, closed form. Proved a new general
  **ray-betweenness sign lemma** (interior of a convex angle ⟹ a matching cross-product sign relation),
  applied it once at vertex $B$ (using "K inside $\angle LBA$") and once at vertex $C$ (using "L inside
  $\angle ACK$") to pin the sign of $\mathrm{cross}(L-B,K-B)$ and $\mathrm{cross}(L-C,K-C)$; combined
  this with **two direct reapplications of the already-certified `interior-point-side-test.md` lemma**
  (applied to a *different* edge of $\triangle BNC$ and $\triangle BMC$ than previously used in this
  file) to pin the sign of $\mathrm{cross}(L-N,C-N)$ and $\mathrm{cross}(B-M,K-M)$ — the "N/M-vertex
  half" that round 4 and this round's outline/outline-review explicitly flagged as still open. All four
  cross products are shown strictly **positive**, which places all four relevant directed angles
  strictly in $(0,\pi)$; since a directed angle already in $(0,\pi)$ equals its own unsigned magnitude,
  the literal unsigned hypotheses (ii),(iii) translate *directly* into exact directed-angle equalities
  $\theta_1=\theta_2$, $\theta_1'=\theta_2'$ — no branch ambiguity survives. This is a from-scratch,
  closed-form argument (verified independently by hand and cross-checked numerically on the file's
  five existing configurations plus the round's own fresh spot-checks, all consistent, but the checks
  are confirmations, not the proof). With this, every step of the chain is now fully rigorous and the
  problem is **solved**.

## Current best
(Superseded by "Full proof" below — the whole chain, including the previously-open branch-selection
step, is now complete.)

## Full proof

### Setup and reduction to a scalar identity

Place $B=(0,0)$, $C=(a,0)$ with $a>0$, and $A=(p,q)$ with $q>0$ (similarity normalization: rotate,
translate, and scale so $BC$ lies on the $x$-axis with $B$ left of $C$, then reflect if necessary so
$A$ is above the axis — none of the hypotheses or the conclusion depend on the choice of similarity
representative). Then
$$M=\tfrac12(A+B)=(p/2,\,q/2), \qquad N=\tfrac12(A+C)=((p+a)/2,\,q/2).$$

**Step 0.** Since $M,N$ have equal $y$-coordinate $q/2$, their perpendicular bisector is the vertical
line $x=\mathrm{target}:=\dfrac{2p+a}{4}$. A point is equidistant from two points iff it lies on their
perpendicular bisector, so for the circumcenter $O=(O_x,O_y)$ of $\triangle AKL$:
$$OM=ON \iff O_x=\mathrm{target}.$$

**Step 1 (circumcenter formula).** Translate so $A$ is the origin: $u=K-A=(u_1,u_2)$, $v=L-A=(v_1,v_2)$.
The circumcenter $O'=(x_0,y_0)$ of $0,u,v$ satisfies
$$2u_1x_0+2u_2y_0=|u|^2,\qquad 2v_1x_0+2v_2y_0=|v|^2.$$
The matrix $\begin{pmatrix}u_1&u_2\\v_1&v_2\end{pmatrix}$ has determinant
$\mathrm{cross}(u,v)=u_1v_2-u_2v_1\neq0$ since $A,K,L$ are non-collinear (they form a genuine triangle
by hypothesis — the problem presupposes $O$ is the circumcenter of $\triangle AKL$). By Cramer's rule,
$$x_0=\frac{|u|^2v_2-|v|^2u_2}{2\,\mathrm{cross}(u,v)}.$$
Since $O_x=p+x_0$,
$$O_x-\mathrm{target} = \frac{p-a/2}{2}+\frac{|u|^2v_2-|v|^2u_2}{2\,\mathrm{cross}(u,v)}
=\frac{\mathrm{myexpr}}{2\,\mathrm{cross}(u,v)},\qquad
\mathrm{myexpr}:=(p-\tfrac a2)\,\mathrm{cross}(u,v)+|u|^2v_2-|v|^2u_2.$$
Hence
$$\boxed{OM=ON \iff \mathrm{myexpr}=0.}$$
This never divides by $p-a/2$, so $AB=AC$ and $AB\neq AC$ are treated uniformly, with no case split.
(Certified lemma: `lemmas/circumcenter-x-coordinate-reduction.md`.)

### Parametrizing $K,L$ using hypothesis (i), with a rigorous sign justification

Hypothesis (i) is $\angle KBA=\angle ACL=:\alpha\in(0,\pi)$ (proved below that $\alpha\neq0,\pi$). Set
$T_K:=|BK|/|BA|>0$, $T_L:=|CL|/|CA|>0$. Writing $R(\theta)$ for counterclockwise rotation by $\theta$,
the two possible parametrizations consistent with $\angle KBA=\alpha$ are $K=B+T_K R(-\alpha)(A-B)$ or
$K=B+T_K R(\alpha)(A-B)$; similarly for $L$.

**Side test (certified, `lemmas/interior-point-side-test.md`).** If $\triangle PQR$ has $P,Q$ on a line
$\ell$ and $R\notin\ell$, every point strictly interior to $\triangle PQR$ lies strictly on $R$'s side
of $\ell$.

Apply this with $(P,Q,R)=(B,M,C)$ on line $AB$ (since $B,M$ lie on line $AB$, $M$ being the midpoint of
$AB$, and $C\notin$ line $AB$): every point strictly interior to $\triangle BMC$ lies on $C$'s side of
line $AB$. Since
$$\mathrm{cross}(A-B,\,C-B)=\mathrm{cross}((p,q),(a,0))=-qa<0,$$
$K$ (interior to $\triangle BMC$ by hypothesis) satisfies $\mathrm{cross}(A-B,K-B)<0$.

Direct computation: if $K=B+T_K R(-\alpha)(A-B)$ with $c=\cos\alpha,s=\sin\alpha$, then
$R(-\alpha)(p,q)=(pc+qs,\,qc-ps)$, so
$$\mathrm{cross}(A-B,K-B)=T_K\big(p(qc-ps)-q(pc+qs)\big)=-T_K\,s\,(p^2+q^2).$$
Since $T_K>0,\ p^2+q^2>0$, this is $<0$ exactly when $s=\sin\alpha>0$. So the convention
$K=B+T_K R(-\alpha)(A-B)$ is forced once $\sin\alpha>0$ (proved next); the opposite convention
$R(+\alpha)$ would instead need $\sin\alpha<0$, impossible.

Symmetrically, apply the side test with $(P,Q,R)=(C,N,B)$ on line $AC$ (since $C,N\in$ line $AC$,
$B\notin$ line $AC$): every point interior to $\triangle BNC$ lies on $B$'s side of line $AC$. Since
$\mathrm{cross}(A-C,B-C)=\mathrm{cross}((p-a,q),(-a,0))=qa>0$, $L$ satisfies
$\mathrm{cross}(A-C,L-C)>0$; the analogous computation for $L=C+T_LR(\alpha)(A-C)$ gives
$\mathrm{cross}(A-C,L-C)=T_L\,s\,((a-p)^2+q^2)$, which is $>0$ exactly when $\sin\alpha>0$ — the *same*
condition as for $K$. We adopt
$$K=B+T_K\,R(-\alpha)(A-B),\qquad L=C+T_L\,R(\alpha)(A-C),\qquad T_K,T_L>0. \tag{$\ast$}$$

**Two facts recorded for later use (Step 7):**
$$\mathrm{cross}(A-B,K-B)=-T_Ks(p^2+q^2)<0, \qquad \mathrm{cross}(A-C,L-C)=T_Ls\big((a-p)^2+q^2\big)>0. \tag{F1}$$

### Proving $\sin\alpha>0$

Write $K=\lambda B+\mu M+\nu C$, $\lambda,\mu,\nu>0$, $\lambda+\mu+\nu=1$ (barycentric coordinates of
the strictly interior point $K$ of $\triangle BMC$). Then $K=\big(\tfrac{\mu p}2+\nu a,\ \tfrac{\mu q}2\big)$.
Line $AB$ has equation $py-qx=0$; substituting,
$$p\Big(\tfrac{\mu q}2\Big)-q\Big(\tfrac{\mu p}2+\nu a\Big)=-\nu qa\neq0\quad(\nu,q,a>0),$$
so $K\notin$ line $AB$. Since $\alpha=\angle KBA\in[0,\pi]$ (well-defined, $K\ne B\ne A$) and both
$\alpha=0$ and $\alpha=\pi$ would force $K$ onto line $AB$, $\alpha\in(0,\pi)$ strictly, hence
$$\boxed{\sin\alpha=s>0.}$$
*Also note* (used below): $K_y=\tfrac{\mu q}2>0$.

### Hypotheses (ii), (iii) as polynomial equations

**Lemma (cross/dot identity for directed angles).** For nonzero planar vectors $X,Y$, write
$\mathrm{cross}(X,Y)=|X||Y|\sin\theta$, $\mathrm{dot}(X,Y)=|X||Y|\cos\theta$ where $\theta\in(-\pi,\pi]$
is the directed angle from $X$ to $Y$ (this is exactly the definition of $\theta$ via $\mathrm{atan2}$).
If $X,Y,W,Z$ are nonzero with directed angle from $X$ to $Y$ equal to directed angle from $W$ to $Z$,
call it $\theta$, then trivially
$$\mathrm{cross}(X,Y)\,\mathrm{dot}(W,Z)-\mathrm{cross}(W,Z)\,\mathrm{dot}(X,Y)=|X||Y||W||Z|(\sin\theta\cos\theta-\cos\theta\sin\theta)=0.$$
More generally, for *any* nonzero $X,Y,W,Z$ (not assuming the angles are equal), letting $\theta_1$
be the directed angle from $X$ to $Y$ and $\theta_2$ the directed angle from $W$ to $Z$,
$$\mathrm{cross}(X,Y)\,\mathrm{dot}(W,Z)-\mathrm{cross}(W,Z)\,\mathrm{dot}(X,Y)
=|X||Y||W||Z|\big(\sin\theta_1\cos\theta_2-\cos\theta_1\sin\theta_2\big)=|X||Y||W||Z|\sin(\theta_1-\theta_2), \tag{XD}$$
by the angle-subtraction formula. $\blacksquare$

Define
$$e_1:=\mathrm{cross}(L-B,K-B)\,\mathrm{dot}(L-N,C-N)-\mathrm{cross}(L-N,C-N)\,\mathrm{dot}(L-B,K-B),$$
$$e_2:=\mathrm{cross}(L-C,K-C)\,\mathrm{dot}(B-M,K-M)-\mathrm{cross}(B-M,K-M)\,\mathrm{dot}(L-C,K-C).$$
By (XD), $e_1=|L-B||K-B||L-N||C-N|\sin(\theta_1-\theta_2)$ where $\theta_1$ is the directed angle from
$L-B$ to $K-B$ (ray $BL\to$ ray $BK$) and $\theta_2$ is the directed angle from $L-N$ to $C-N$ (ray
$NL\to$ ray $NC$); similarly $e_2=|L-C||K-C||B-M||K-M|\sin(\theta_1'-\theta_2')$ with $\theta_1'$ the
directed angle from $L-C$ to $K-C$ (ray $CL\to$ ray $CK$), $\theta_2'$ the directed angle from $B-M$ to
$K-M$ (ray $MB\to$ ray $MK$).

**Basic fact.** For nonzero $X,Y$ with directed angle $\theta\in(-\pi,\pi]$ from $X$ to $Y$, the
*unsigned* angle between $X,Y$ (i.e. $\arccos\big(\mathrm{dot}(X,Y)/(|X||Y|)\big)\in[0,\pi]$, the
standard notion "$\angle$" used in the problem statement) equals $|\theta|$: indeed
$\cos\theta=\mathrm{dot}(X,Y)/(|X||Y|)$ by definition of $\theta$, and since $\theta\in(-\pi,\pi]$,
$\arccos(\cos\theta)=|\theta|$ (as $\cos$ is even and $\arccos$ is the inverse of $\cos$ on $[0,\pi]$).
Hence
$$\angle LBK=|\theta_1|,\quad \angle LNC=|\theta_2|,\quad \angle LCK=|\theta_1'|,\quad \angle BMK=|\theta_2'|. \tag{U}$$
So hypothesis (ii), $\angle LBK=\angle LNC$, says $|\theta_1|=|\theta_2|$; hypothesis (iii) says
$|\theta_1'|=|\theta_2'|$. Each of these two equalities of *unsigned* angles is, a priori, consistent
with either $\theta_1=\theta_2$ or $\theta_1=-\theta_2$ (resp. $\theta_1'=\theta_2'$ or
$\theta_1'=-\theta_2'$) — and only the first option in each pair makes $e_1=0$ (resp. $e_2=0$) *for the
specific polynomials displayed above*, by (XD). **Step 7 below proves, from the position hypotheses
alone (not assuming (ii)/(iii)), that $\theta_1,\theta_2$ are both strictly positive and
$\theta_1',\theta_2'$ are both strictly positive — which forces the "$+$" branch in both pairs and
hence $e_1=0$, $e_2=0$ as an exact consequence of (ii), (iii).**

### Step 7 (NEW, closes the branch-selection gap): pinning the signs of $\theta_1,\theta_2,\theta_1',\theta_2'$

**Lemma A (ray-betweenness sign lemma).** Let $V,R,P,Q$ be four points with $P,Q\notin$ line $VR$.
Suppose $P$ lies in the interior of the (non-reflex) angle $\angle RVQ$, meaning $P$ lies simultaneously
(a) on the same side of line $VR$ as $Q$, and (b) on the same side of line $VQ$ as $R$ — the standard
definition of the interior of a convex angular sector as the intersection of its two bounding
half-planes. Then
$$\mathrm{sign}\big(\mathrm{cross}(P-V,Q-V)\big)=\mathrm{sign}\big(\mathrm{cross}(R-V,P-V)\big).$$

*Proof.* For $X\ne V$ write $\theta(X)\in(-\pi,\pi]$ for the directed CCW angle from ray $VR$ to ray
$VX$, so $\mathrm{sign}(\sin\theta(X))=\mathrm{sign}(\mathrm{cross}(R-V,X-V))$. Condition (a) says
$\mathrm{sign}(\sin\theta(P))=\mathrm{sign}(\sin\theta(Q))=:\sigma\in\{+1,-1\}$ (both nonzero since
$P,Q\notin$ line $VR$). Condition (b) is the side test for line $VQ$: $\mathrm{sign}(\mathrm{cross}(Q-V,P-V))=\mathrm{sign}(\mathrm{cross}(Q-V,R-V))$. Using
$\mathrm{cross}(Q-V,P-V)=|Q{-}V||P{-}V|\sin(\theta(P)-\theta(Q))$ and
$\mathrm{cross}(Q-V,R-V)=|Q{-}V||R{-}V|\sin(0-\theta(Q))=-|Q{-}V||R{-}V|\sin\theta(Q)$, condition (b)
becomes
$$\mathrm{sign}\big(\sin(\theta(P)-\theta(Q))\big)=-\sigma. \tag{b$'$}$$
*Case $\sigma=+1$:* $\theta(P),\theta(Q)\in(0,\pi)$. Then $\theta(P)-\theta(Q)\in(-\pi,\pi)$, so
(b$'$) ($\sin(\theta(P)-\theta(Q))<0$) is equivalent to $\theta(P)-\theta(Q)\in(-\pi,0)$, i.e.
$\theta(P)<\theta(Q)$. So $0<\theta(P)<\theta(Q)<\pi$, giving $\theta(Q)-\theta(P)\in(0,\pi)$, hence
$\sin(\theta(Q)-\theta(P))>0$, i.e. $\mathrm{cross}(P-V,Q-V)=|P{-}V||Q{-}V|\sin(\theta(Q)-\theta(P))>0$
— matching $\mathrm{sign}(\mathrm{cross}(R-V,P-V))=\mathrm{sign}(\sin\theta(P))=+1$.
*Case $\sigma=-1$:* symmetric ($\theta(P),\theta(Q)\in(-\pi,0)$); (b$'$) forces
$\sin(\theta(P)-\theta(Q))>0$, i.e. $\theta(P)-\theta(Q)\in(0,\pi)$ (as $\theta(P)-\theta(Q)\in(-\pi,\pi)$),
i.e. $\theta(Q)<\theta(P)<0$, giving $\theta(Q)-\theta(P)\in(-\pi,0)$, so
$\mathrm{cross}(P-V,Q-V)<0$, matching $\mathrm{sign}(\mathrm{cross}(R-V,P-V))=-1$.
In both cases the claim holds. $\blacksquare$

**Application 1 (vertex $B$).** The hypothesis "$K$ lies inside the angle $LBA$" is exactly $P$ interior
to $\angle RVQ$ with $V=B,\ R=A,\ Q=L,\ P=K$. Lemma A gives
$$\mathrm{sign}(\mathrm{cross}(K-B,L-B))=\mathrm{sign}(\mathrm{cross}(A-B,K-B))\overset{(F1)}{=}-1,$$
so $\mathrm{cross}(K-B,L-B)<0$, i.e.
$$\mathrm{cross}(L-B,K-B)=-\mathrm{cross}(K-B,L-B)>0. \tag{S1}$$

**Application 2 (vertex $C$).** The hypothesis "$L$ lies inside the angle $ACK$" is $P$ interior to
$\angle RVQ$ with $V=C,\ R=A,\ Q=K,\ P=L$. Lemma A gives
$$\mathrm{sign}(\mathrm{cross}(L-C,K-C))=\mathrm{sign}(\mathrm{cross}(A-C,L-C))\overset{(F1)}{=}+1,$$
so directly
$$\mathrm{cross}(L-C,K-C)>0. \tag{S2}$$

**Application 3 (vertex $N$, via `interior-point-side-test.md` applied to a new edge).** Apply the
already-certified side-test lemma with $(P,Q,R)=(N,C,B)$: $N,C$ both lie on line $NC$ (trivially, both
are named points of that line) and $B\notin$ line $NC$ (since $B,N,C$ are not collinear — $N$ is the
midpoint of $AC$, and $B$ on line $NC$ would force $B,A,C$ collinear, contradicting that $ABC$ is a
triangle). So every point strictly interior to $\triangle BNC$ — in particular $L$, by hypothesis —
lies on $B$'s side of line $NC$:
$$\mathrm{sign}(\mathrm{cross}(C-N,L-N))=\mathrm{sign}(\mathrm{cross}(C-N,B-N)).$$
Direct computation with $N=((p+a)/2,q/2)$: $C-N=(\tfrac{a-p}2,-\tfrac q2)$, $B-N=(-\tfrac{p+a}2,-\tfrac q2)$,
$$\mathrm{cross}(C-N,B-N)=\tfrac{a-p}2\Big(-\tfrac q2\Big)-\Big(-\tfrac q2\Big)\Big(-\tfrac{p+a}2\Big)
=-\tfrac{q(a-p)}4-\tfrac{q(p+a)}4=-\tfrac{qa}2<0\quad(q,a>0).$$
So $\mathrm{cross}(C-N,L-N)<0$, i.e.
$$\mathrm{cross}(L-N,C-N)=-\mathrm{cross}(C-N,L-N)>0. \tag{S3}$$

**Application 4 (vertex $M$, via `interior-point-side-test.md` applied to a new edge).** Apply the same
certified lemma with $(P,Q,R)=(M,B,C)$: $M,B$ both lie on line $MB$ and $C\notin$ line $MB$ (else
$A,B,C$ collinear). So every point strictly interior to $\triangle BMC$ — in particular $K$ — lies on
$C$'s side of line $MB$:
$$\mathrm{sign}(\mathrm{cross}(B-M,K-M))=\mathrm{sign}(\mathrm{cross}(B-M,C-M)).$$
With $M=(p/2,q/2)$: $B-M=(-\tfrac p2,-\tfrac q2)$, $C-M=(a-\tfrac p2,-\tfrac q2)$,
$$\mathrm{cross}(B-M,C-M)=\Big(-\tfrac p2\Big)\Big(-\tfrac q2\Big)-\Big(-\tfrac q2\Big)\Big(a-\tfrac p2\Big)
=\tfrac{pq}4+\tfrac{qa}2-\tfrac{pq}4=\tfrac{qa}2>0.$$
So directly
$$\mathrm{cross}(B-M,K-M)>0. \tag{S4}$$

**Putting it together.** By definition $\theta_1,\theta_2,\theta_1',\theta_2'\in(-\pi,\pi]$ satisfy
$\mathrm{sign}(\sin\theta_1)=\mathrm{sign}(\mathrm{cross}(L-B,K-B))$, etc. By (S1)–(S4), all four cross
products are strictly positive, hence
$$\theta_1,\ \theta_2,\ \theta_1',\ \theta_2'\ \in\ (0,\pi). \tag{RANGE}$$

By (U), $\angle LBK=|\theta_1|=\theta_1$ (since $\theta_1>0$) and $\angle LNC=|\theta_2|=\theta_2$.
Hypothesis (ii) $\angle LBK=\angle LNC$ therefore says **exactly** $\theta_1=\theta_2$ (not merely
$|\theta_1|=|\theta_2|$ — the sign ambiguity is eliminated because both quantities are already known,
independently of hypothesis (ii), to be their own absolute values). By (XD),
$$e_1=|L{-}B||K{-}B||L{-}N||C{-}N|\sin(\theta_1-\theta_2)=0.$$
Identically, $\angle LCK=\theta_1'$, $\angle BMK=\theta_2'$ (both in $(0,\pi)$ by RANGE), so hypothesis
(iii) says exactly $\theta_1'=\theta_2'$, giving $e_2=0$.

This closes the gap completely: **both** the $B/N$-vertex half (needed for $e_1$) and the $C/M$-vertex
half (needed for $e_2$) are now pinned in closed form — Application 1/3 close the $e_1$ branch,
Application 2/4 close the $e_2$ branch — with no recourse to numerics. (Numerically, this is consistent
with all five configurations previously tabulated in this file, and with a fresh spot-check this round;
those checks are now redundant confirmations, not load-bearing.)

### Decoupling ($e_1,e_2$ separate $T_K,T_L$)

**Certified lemma** (`lemmas/ray-parametrized-angle-decoupling.md`): since $K-B=T_K\hat K$ with
$\hat K:=R(-\alpha)(A-B)$ independent of $T_K$ (by $(\ast)$), every occurrence of $K$ in $e_1$ enters
linearly through $K-B$, so $e_1=T_K\cdot A_1(T_L,c,s,p,q,a)$ with $A_1$ free of $T_K$; symmetrically
$e_2=T_L\cdot B_1(T_K,c,s,p,q,a)$ with $B_1$ free of $T_L$. Since $T_K,T_L>0$,
$$e_1=0\iff A_1=0,\qquad e_2=0\iff B_1=0.$$
With $X:=cq-ps$, $X':=cq+s(p-a)$, $Z:=aX+s(p^2+q^2)$, and dividing by the positive constants
$|AC|^2=(a-p)^2+q^2$ (from $A_1$), $|AB|^2=p^2+q^2$ (from $B_1$), and reducing modulo $c^2+s^2-1$:
$$\frac{A_1}{(a-p)^2+q^2}\equiv \tfrac{Z}{2}T_L^2-\Big(\tfrac{cZ}{2}+\tfrac{aq}{4}\Big)T_L+\tfrac{aX}{4}
\pmod{c^2+s^2-1},$$
$$\frac{B_1}{p^2+q^2}\equiv \tfrac{Z}{2}T_K^2-\Big(\tfrac{cZ}{2}+\tfrac{aq}{4}\Big)T_K+\tfrac{aX'}{4}
\pmod{c^2+s^2-1}.$$

### The closing identity (verified unconditionally, no $c^2+s^2=1$ needed)

By full symbolic expansion (independent, from-scratch, computed in round 4 and re-checked), the
following is an exact polynomial identity in $p,q,a,c,s,T_K,T_L$:
$$\mathrm{myexpr}\cdot Z = 2(q-T_K X)\,A_1+2(T_L X'-q)\,B_1,\qquad X=cq-ps,\ X'=cq+s(p-a),\ Z=aX+s(p^2+q^2).$$
Consequently, whenever $A_1=0$ and $B_1=0$ (i.e. hypotheses (ii), (iii), via Step 7 and the decoupling
above), the right side vanishes, so
$$\mathrm{myexpr}\cdot Z=0.$$

### $Z>0$

Recall $K_y=T_K X$ exactly (from $K=B+T_K R(-\alpha)(A-B)$, the $y$-coordinate of $R(-\alpha)(p,q)$ is
$qc-ps=X$). We showed $K_y=\mu q/2>0$ (barycentric argument) and $T_K>0$, so $X=K_y/T_K>0$. Also
$s=\sin\alpha>0$, $p^2+q^2>0$, $a>0$. So
$$Z=\underbrace{a}_{>0}\cdot\underbrace{X}_{>0}\ +\ \underbrace{s}_{>0}\cdot\underbrace{(p^2+q^2)}_{>0}>0,$$
a sum of two strictly positive terms. Hence $Z\neq0$, and dividing $\mathrm{myexpr}\cdot Z=0$ by $Z$
gives
$$\mathrm{myexpr}=0.$$

### Conclusion

By Step 0–1, $\mathrm{myexpr}=0\iff OM=ON$. Every step above is now unconditional and closed-form,
covering every triangle $ABC$ satisfying all five hypotheses (i)–(iii) plus the two position hypotheses
and $K,L$ strictly interior to their respective triangles, with no case split for $AB=AC$ vs. $AB\ne AC$
(the identity never divides by $p-a/2$). Therefore
$$OM=ON$$
for every valid configuration. $\blacksquare$

## Promotable lemmas

1. **Circumcenter $x$-coordinate reduction** — already certified, `lemmas/circumcenter-x-coordinate-reduction.md`.
2. **Ray-parametrized angle decoupling** — already certified, `lemmas/ray-parametrized-angle-decoupling.md`.
3. **Interior-point side test** — already certified, `lemmas/interior-point-side-test.md`. This round
   additionally reuses it on *two new edges* (edge $NC$ of $\triangle BNC$ with off-vertex $B$, and edge
   $MB$ of $\triangle BMC$ with off-vertex $C$) — no new proof needed, purely a new application.
4. **Cross/dot–$\sin(\theta_1-\theta_2)$ identity (XD)** — for any two directed angles $\theta_1,\theta_2$
   defined via nonzero vector pairs, $\mathrm{cross}(X,Y)\mathrm{dot}(W,Z)-\mathrm{cross}(W,Z)\mathrm{dot}(X,Y)
   =|X||Y||W||Z|\sin(\theta_1-\theta_2)$ exactly.
5. **NEW this round — Ray-betweenness sign lemma (Lemma A).** If $P$ lies in the interior of the convex
   angle $\angle RVQ$ (the intersection of the half-plane bounded by line $VR$ containing $Q$ and the
   half-plane bounded by line $VQ$ containing $R$), then
   $\mathrm{sign}(\mathrm{cross}(P-V,Q-V))=\mathrm{sign}(\mathrm{cross}(R-V,P-V))$. Proved from scratch
   above by a directed-angle computation (four-line case split on the common side $\sigma=\pm1$),
   generalizing `interior-point-side-test.md` from a single line to a two-line angular sector. Reusable
   for any problem needing "a ray strictly between two other rays forces a specific cross-product sign
   relation to the bounding rays" — a generic tool for translating unsigned "$X$ inside $\angle YVZ$"
   hypotheses into directed-angle-range facts.
6. **Unsigned angle = $|$directed angle$|$ (fact (U)).** For nonzero $X,Y$ with directed CCW angle
   $\theta\in(-\pi,\pi]$ from $X$ to $Y$, the standard unsigned angle $\angle(X,Y)=\arccos(\mathrm{dot}(X,Y)/(|X||Y|))\in[0,\pi]$
   equals $|\theta|$. Trivial but load-bearing: it is the bridge that turns "both directed angles already
   known positive" into "the literal unsigned hypothesis pins the directed angles exactly equal," closing
   the branch-selection gap without any residual sign ambiguity.
