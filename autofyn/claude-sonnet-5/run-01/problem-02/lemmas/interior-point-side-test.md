## Lemma (Interior-point side test)

**Statement.** Let $\triangle PQR$ have $P,Q$ on a line $\ell$ and $R\notin\ell$. Then every point
strictly interior to $\triangle PQR$ lies strictly on $R$'s side of $\ell$ (the open half-plane
bounded by $\ell$ containing $R$).

**Proof.** Write $\ell$ through the origin (translate if necessary) with direction vector $d\ne0$; a
point $X$ is on the side where $\mathrm{cross}(d,X)>0$ or the side where $\mathrm{cross}(d,X)<0$
(constant sign on each open half-plane bounded by $\ell$, standard fact about the sign of a linear
functional). Let $Z$ be strictly interior to $\triangle PQR$: write $Z=\lambda P+\mu Q+\nu R$ with
$\lambda,\mu,\nu>0$, $\lambda+\mu+\nu=1$ (barycentric coordinates of an interior point are all
strictly positive). Since $P,Q\in\ell$, $\mathrm{cross}(d,P)=\mathrm{cross}(d,Q)=0$, so by bilinearity
$$\mathrm{cross}(d,Z)=\lambda\cdot 0+\mu\cdot 0+\nu\,\mathrm{cross}(d,R)=\nu\,\mathrm{cross}(d,R).$$
Since $\nu>0$, $\mathrm{cross}(d,Z)$ has the same sign as $\mathrm{cross}(d,R)$, i.e. $Z$ is on $R$'s
side. $\blacksquare$

**Application (imo-2026-02).** With $B=(0,0)$, $C=(a,0)$ ($a>0$), $A=(p,q)$ ($q>0$), $M=(A+B)/2$ the
midpoint of $AB$: since $B,M$ lie on line $AB$ and $C\notin$ line $AB$, every point $K$ strictly
interior to $\triangle BMC$ lies strictly on $C$'s side of line $AB$, i.e.
$\mathrm{cross}(A-B,K-B)$ has the same (strictly negative, since $\mathrm{cross}(A-B,C-B)=-qa<0$)
sign as $\mathrm{cross}(A-B,C-B)$. This is used twice in `synthetic-angle-chase-aklastar.md`:
(a) to show $K\notin$ line $AB$ (hence $\angle KBA=\alpha\in(0,\pi)$ strictly, so $\sin\alpha>0$), and
(b) to rigorously fix the rotation-direction sign in the parametrization
$K=B+T_K\,R(-\alpha)(A-B)$ (as opposed to $R(+\alpha)$) — since expanding
$\mathrm{cross}(A-B,K-B)=-T_K\sin\alpha\,|AB|^2$ under this parametrization and comparing signs with
the side-test conclusion forces consistency exactly when $\sin\alpha>0$ (already established), and
the opposite convention $R(+\alpha)$ would instead require $\sin\alpha<0$, which is impossible.

**Status.** Proved in full, general (not specific to this problem beyond the application), no gaps.
Certified from `synthetic-angle-chase-aklastar.md` (round 4).
