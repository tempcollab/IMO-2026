# Lemma: OM=ON reduces to a circumcenter x-coordinate condition

**Source approaches:** `synthetic-angle-chase-aklastar` (Steps 0–1), `coordinate-groebner-elimination`
(§1). Certified by proof-reviewer, round 2 — independently re-derivable, elementary, no gaps.

**Statement.** Place $B=(0,0)$, $C=(a,0)$ with $a>0$, $A=(p,q)$ with $q>0$ (WLOG by similarity/
reflection normalization). Let $M,N$ be the midpoints of $AB,AC$. For any non-degenerate triangle
$AKL$ (i.e. $A,K,L$ not collinear) with circumcenter $O=(O_x,O_y)$:
$$OM=ON \iff O_x = \frac{2p+a}{4}.$$
Moreover, writing $u=K-A,\ v=L-A$, $\mathrm{cross}(u,v)=u_1v_2-u_2v_1$,
$$O_x - \frac{2p+a}{4} = \frac{\mathrm{myexpr}}{D}, \qquad
\mathrm{myexpr} := \Big(p-\tfrac a2\Big)\mathrm{cross}(u,v) + |u|^2 v_2 - |v|^2 u_2,\qquad
D := 2\,\mathrm{cross}(u,v) \neq 0,$$
so $OM=ON \iff \mathrm{myexpr}=0$, and this identity never divides by $p-a/2$ (handles $AB=AC$ and
$AB\neq AC$ uniformly).

**Proof.** $M=(p/2,q/2)$, $N=((p+a)/2,q/2)$ have equal $y$-coordinate, so their perpendicular
bisector is the vertical line $x=(2p+a)/4$; a point is equidistant from $M,N$ iff it lies on this
line (standard fact about perpendicular bisectors). This gives the first claim. For the second:
translate so $A$ is the origin; the circumcenter $O'=(x_0,y_0)$ of $0,u,v$ satisfies
$2u_1x_0+2u_2y_0=|u|^2$, $2v_1x_0+2v_2y_0=|v|^2$ (each from equidistance to $0$ and to the respective
vertex), a linear system with determinant $\mathrm{cross}(u,v)\neq0$ (nonzero iff $0,u,v$, i.e.
$A,K,L$, are not collinear). Cramer's rule gives $x_0=(|u|^2v_2-|v|^2u_2)/(2\,\mathrm{cross}(u,v))$;
since $O_x=p+x_0$, algebra gives the stated formula for $O_x-(2p+a)/4$. $\blacksquare$
