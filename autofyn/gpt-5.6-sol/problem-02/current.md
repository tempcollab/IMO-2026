## Status
solved

## Approaches tried
- Trigonometric circle factorization — partial: the ray parametrization, midpoint sine-law formulas, and circle determinant reduction were useful, but the asserted angles at K and L were incorrect, so the claimed incidence equations did not follow.
- Vector perpendicular-bisector formulation — worked: oriented ray coordinates turn the last two angle hypotheses into residuals, and an explicit two-residual polynomial certificate proves the circumcentre target.
- Four-circle midpoint web — worked: auxiliary points on the side lines produce a four-circle configuration, and explicit radical-axis equations prove that the relevant midpoints lie on the circumcircle of triangle $AKL$, after which equal powers give the result.

## Current best
Two independent complete proofs have been certified. The proof recorded below is the four-circle midpoint-web proof. Its key result is that, if $P$ and $Q$ are the midpoints of $BE$ and $CD$, respectively, then
\[
A,K,L,P,Q\text{ are concyclic}.
\]
Explicit circle equations show that the radical axis of $(CEMK)$ and $(APQ)$ is $BD$, while the radical axis of $(BDNL)$ and $(APQ)$ is $CE$, including the tangent interpretations in the two coincidence cases. Equal powers of $M$ and $N$ to this circle then imply $OM=ON$.

## Full proof
We use directed angles modulo \(\pi\), directed lengths on a fixed line, **Power of a Point**, its concyclicity converse, and the **Radical Axis theorem**, all from the Synthetic toolkit in the knowledge base.

Reflect the entire configuration if necessary, so that \(C\) lies above the oriented line \(AB\). Reflection preserves ordinary angles, midpoints, circles, circumcentres, and distances, so it is enough to prove the result in this orientation. Write
\[
AB=c,\qquad AC=b,\qquad \angle BAC=\alpha,
\]
and put
\[
x=\angle KBA=\angle ACL.
\]
Because \(K\) is an interior point of the triangle \(BMC\), the ray \(BK\) lies strictly inside \(\angle ABC\). Hence \(0<x<\angle ABC\). In particular
\[
0<\alpha+x<\alpha+\angle ABC<\pi,                 \tag{1}
\]
so \(\sin x>0\) and \(\sin(\alpha+x)>0\).

Define, on the full lines,
\[
D=BK\cap AC,\qquad E=CL\cap AB.
\]
These intersections are finite. Indeed, put \(A=(0,0)\), \(B=(c,0)\), and
\(C=b(\cos\alpha,\sin\alpha)\). The ray \(BK\) has direction
\((-\cos x,\sin x)\), while the ray \(CL\) has direction
\(-\bigl(\cos(\alpha+x),\sin(\alpha+x)\bigr)\). Solving the two line-intersection equations gives
\[
AD=\frac{c\sin x}{\sin(\alpha+x)},
\qquad
AE=\frac{b\sin x}{\sin(\alpha+x)}.                 \tag{2}
\]
The denominators are nonzero by (1). Moreover, both quantities in (2) are positive, so \(D\) and \(E\) lie on the rays \(AC\) and \(AB\), respectively; in particular neither is a point at infinity or equal to \(A\). Equation (2) gives
\[
AB\cdot AE=AC\cdot AD.                              \tag{3}
\]
Equivalently, by the converse of Power of a Point, \(B,C,D,E\) are concyclic. This is also the direct directed-angle consequence of
\(\angle DBE=\angle DCE\), which is the first given angle equality.

The other two given equalities give the remaining two circles in the web. Since \(B,D,K\) are collinear and \(C,D,N\) are collinear, the equality
\(\angle LBK=\angle LNC\) yields
\[
\measuredangle DBL=\measuredangle DNL,
\]
so \(B,D,L,N\) are concyclic when \(D\ne N\). Similarly, since \(C,E,L\) and \(B,E,M\) are collinear, the equality
\(\angle LCK=\angle BMK\) yields
\[
\measuredangle ECK=\measuredangle EMK,
\]
so \(C,E,K,M\) are concyclic when \(E\ne M\).

There are two possible coincidence cases in these statements, and the original angle equalities retain exactly the information needed there. If \(D=N\), then \(BK=BN\) as lines, and
\[
\angle LBN=\angle LNC;
\]
by the tangent-chord converse, \(AC\) is tangent at \(N\) to the circle through \(B,N,L\). If \(E=M\), then \(CL=CM\) as lines, and
\[
\angle MCK=\angle BMK;
\]
again by the tangent-chord converse, \(AB\) is tangent at \(M\) to the circle through \(C,M,K\). Thus no limiting argument is required.

For completeness, (3), together with \(AM=AB/2\) and \(AN=AC/2\), also gives
\[
AE\cdot AM=AD\cdot AN,
\]
so \(D,E,M,N\) are concyclic by the converse of Power of a Point (with the usual tangent interpretation if \(D=N\) or \(E=M\)). We now prove the stronger midpoint-web statement that closes the problem.

Let \(P\) and \(Q\) be the midpoints of \(BE\) and \(CD\), respectively. We claim that
\[
A,K,L,P,Q\quad\hbox{are concyclic}.                 \tag{4}
\]
The following calculation is an explicit proof of the required circle maps/radical axes; in particular, it replaces an otherwise unproved appeal to a composition of spiral similarities.

Take \(A\) as origin and let \(\mathbf u=\overrightarrow{AB}\),
\(\mathbf v=\overrightarrow{AC}\). These vectors form a basis because \(ABC\) is a triangle. Put
\[
U=\mathbf u\cdot\mathbf u=c^2,
\qquad W=\mathbf v\cdot\mathbf v=b^2.
\]
For positive real numbers \(e,d\), write
\[
E=e\mathbf u,\qquad D=d\mathbf v.
\]
Then (3) is exactly
\[
Ue=Wd.                                                \tag{5}
\]
Also
\[
M=\tfrac12\mathbf u,\quad N=\tfrac12\mathbf v,
\quad P=\frac{1+e}{2}\mathbf u,
\quad Q=\frac{1+d}{2}\mathbf v.                     \tag{6}
\]
Every point \(X\) has unique coordinates \(X=s\mathbf u+t\mathbf v\). A circle has an equation
\[
|X|^2+as+bt+g=0                                      \tag{7}
\]
for suitable constants \(a,b,g\): this is the usual Cartesian circle equation after expressing the linear term in the basis \(\mathbf u,\mathbf v\).

Let \(\Gamma=(APQ)\). It is a genuine circle because \(e,d>0\), so \(P\ne A\), \(Q\ne A\), and the nonzero vectors \(AP\), \(AQ\) lie on the two nonparallel sides of the triangle. Substitution of the three points in (6) into (7) gives
\[
\Gamma:\quad
|X|^2-U\frac{1+e}{2}s-W\frac{1+d}{2}t=0.             \tag{8}
\]
Indeed, the constant is zero because \(A\in\Gamma\); setting successively
\((s,t)=((1+e)/2,0)\) and \((0,(1+d)/2)\) determines the two displayed linear coefficients.

Let \(\Sigma_K\) be the circle through \(C,E,M,K\) when \(E\ne M\). When \(E=M\), let \(\Sigma_K\) be the circle through \(C,M,K\), which, as proved above, is tangent to \(AB\) at \(M\). In both cases its equation is
\[
\Sigma_K:\quad
|X|^2-U\left(e+\frac12\right)s
-\left(W+\frac{Ue}{2}\right)t+\frac{Ue}{2}=0.        \tag{9}
\]
Here is a derivation, including the coincidence case. If \(e\ne 1/2\), substitute
\(E=e\mathbf u\) and \(M=\mathbf u/2\) into (7). Subtracting the resulting equations gives
\[
(e-\frac12)\bigl(U(e+\frac12)+a\bigr)=0,
\]
so \(a=-U(e+1/2)\), after which either equation gives \(g=Ue/2\). Substitution of \(C=\mathbf v\) then gives \(b=-W-Ue/2\). If \(e=1/2\), tangency to \(AB\) at \(M\) says that the restriction of (7) to \(X=s\mathbf u\) has a double zero at \(s=1/2\). It is therefore
\(U(s-1/2)^2\), which gives the same values \(a=-U\), \(g=U/4\); substitution of \(C\) again gives the coefficient in (9).

Subtracting (8) from (9), and using (5), gives
\[
\Sigma_K(X)-\Gamma(X)
 =\frac12\bigl(Ue(1-s)-Wt\bigr)
 =\frac W2\bigl(d(1-s)-t\bigr).                     \tag{10}
\]
Consequently the radical axis of \(\Sigma_K\) and \(\Gamma\) is
\(t=d(1-s)\), precisely the line through \(B=(1,0)\) and \(D=(0,d)\). Since \(K\in\Sigma_K\) and \(K\in BD\), equation (10) gives \(K\in\Gamma\).

The argument for \(L\) is symmetric, but we print it to avoid leaving a hidden case. Let \(\Sigma_L\) be the circle through \(B,D,N,L\) if \(D\ne N\), and the circle through \(B,N,L\) tangent to \(AC\) at \(N\) if \(D=N\). Substitution, or the same double-root argument on the line \(AC\) in the tangent case, gives
\[
\Sigma_L:\quad
|X|^2-\left(U+\frac{Wd}{2}\right)s
-W\left(d+\frac12\right)t+\frac{Wd}{2}=0.           \tag{11}
\]
Subtracting (8) from (11), and using \(Wd=Ue\), gives
\[
\Sigma_L(X)-\Gamma(X)
 =\frac12\bigl(Wd(1-t)-Us\bigr)
 =\frac U2\bigl(e(1-t)-s\bigr).                     \tag{12}
\]
Thus the radical axis is \(s=e(1-t)\), precisely the line through
\(C=(0,1)\) and \(E=(e,0)\). Since \(L\in\Sigma_L\cap CE\), equation (12) gives \(L\in\Gamma\). We have now proved (4).

The problem states the circumcentre of triangle \(AKL\), so \(A,K,L\) are noncollinear and their circumcircle is well-defined. By (4), that circumcircle is exactly \(\Gamma\). Let its centre and radius be \(O\) and \(R\).

Finally orient \(AB\) from \(A\) to \(B\). From (6), the directed coordinates of \(A,M,P\) are \(0,1/2,(1+e)/2\), and hence Power of a Point gives
\[
\operatorname{Pow}_{\Gamma}(M)
 =\overline{MA}\,\overline{MP}
 =\left(-\frac c2\right)\left(\frac{ec}{2}\right)
 =-\frac14\,AB\cdot AE.                             \tag{13}
\]
Likewise, orienting \(AC\) from \(A\) to \(C\),
\[
\operatorname{Pow}_{\Gamma}(N)
 =\overline{NA}\,\overline{NQ}
 =-\frac14\,AC\cdot AD.                             \tag{14}
\]
The signs in (13) and (14) are the same and are not discarded. By (3), the two powers are equal. Since for a circle of centre \(O\) and radius \(R\),
\(
\operatorname{Pow}_{\Gamma}(X)=OX^2-R^2,
\)
we obtain
\[
OM^2-R^2=ON^2-R^2.
\]
Both distances are nonnegative, so \(OM=ON\), as required. ∎
