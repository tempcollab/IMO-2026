## Status
solved

## Approaches tried
- Vector/dot-cross formulation targeting the fixed perpendicular bisector of $MN$ — live; the circumcentre calculation and exact ordered-vector translation were completed in round 1, leaving one polynomial identity.
- Rotation-scale telescoping — dead end alone: it introduces unrelated positive scale factors and supplies no required length relation.
- Oriented ray coordinates plus a two-residual certificate — worked: the first equality is absorbed into the coordinates, the other two give $F_2=F_3=0$ without tangent division, and an explicit coefficient identity gives the circumcentre target.

## Current best
A complete proof is below. Its central identity is
\[
\sin(A+x)T+P_3F_3+P_2F_2=0,
\]
where $F_2,F_3$ are the remaining angle residuals and $T=0$ is exactly the certified circumcentre linear certificate.

## Full proof
We use **angle chasing** and **coordinates** from the knowledge-base entries **Synthetic toolkit** and **Coordinates / complex / barycentric**, followed by the certified **circumcentre linear-certificate lemma**.

Reflect the configuration if necessary so that $A,B,C$ occur counterclockwise. Reflection preserves ordinary angles, incidence, betweenness, midpoints, circles, circumcentres, and distances, hence all hypotheses and the conclusion. Write
\[
AB=c>0,\quad AC=b>0,\quad \angle BAC=A,
\]
let $B=\angle ABC,C=\angle ACB$, and set
\[
 A=(0,0),\quad B=(c,0),\quad C=(b\cos A,b\sin A).
\]
Put
\[
x=\angle KBA=\angle ACL,\qquad r=BK>0,
\qquad s=CL>0.
\]
Because $L$ is interior to $BNC$, the ray $BL$ lies strictly inside $\angle ABC$. Because $K$ lies strictly inside $\angle LBA$, ray $BK$ lies strictly between $BL$ and $BA$. Therefore
\[
0<x=\angle KBA<\angle LBA<B. \tag{1}
\]
Consequently
\[
0<A+x<A+B=\pi-C<\pi. \tag{2}
\]
The first angle equality, with these ray orders, gives
\[
K=(c-r\cos x,r\sin x),
\qquad L=C-s(\cos(A+x),\sin(A+x)). \tag{3}
\]
Indeed, the directions of $BK,CL$ are respectively $\pi-x,\pi+A+x$, and $r,s>0$. Thus (3) retains the ordinary-angle branch.

Abbreviate
\[
u=\cos A,\,v=\sin A,\,p=\cos x,\,q=\sin x,
\,g=\cos(A+x),\,h=\sin(A+x). \tag{4}
\]
The angle-addition equations and their inverse are
\[
g=up-vq,\quad h=vp+uq, \tag{5}
\]
\[
u=gp+hq,\quad v=hp-gq, \tag{6}
\]
and
\[
u^2+v^2=p^2+q^2=g^2+h^2=1. \tag{7}
\]
By (1), $q>0$, and by (2),
\[
h>0. \tag{8}
\]

For vectors $X,Y$, write $X\cdot Y$ for their dot product and $X\times Y$ for their oriented determinant. The ray orders show that $\angle LBK$ and $\angle LNC$ have the same orientation. Equality of these ordinary angles implies the cross-multiplied sine-cosine equation
\[
 ((L-B)\times(K-B))((L-N)\cdot(C-N))
 =((L-N)\times(C-N))((L-B)\cdot(K-B)), \tag{9}
\]
where $N=C/2$. No dot product is divided out, so this includes a common angle of $90^\circ$.

All four factors expand as
\[
\begin{aligned}
(L-B)\times(K-B)&=r(bh-cq-2sgq-sv),\\
(L-B)\cdot(K-B)&=r(-bg+cp-2shq+su),\\
(L-C/2)\times(C/2)&=\frac{bsq}{2},\\
(L-C/2)\cdot(C/2)&=\frac{b(b-2sp)}4.
\end{aligned} \tag{10}
\]
Substitution in left minus right in (9), then cancellation of the positive factor $br/4$, gives
\[
\begin{aligned}
0={}&(bh-cq-2sgq-sv)(b-2sp)\\
&-2sq(-bg+cp-2shq+su)\\
={}&b^2h-bcq-bsv-2bshp\\
&+s^2(4gpq+2vp+4hq^2-2uq). \tag{11}
\end{aligned}
By (6),(7), the final bracket equals
\[
\begin{aligned}
4gpq+2vp+4hq^2-2uq
&=4gpq+2(hp-gq)p+4hq^2-2(gp+hq)q\\
&=2h(p^2+q^2)=2h. \tag{12}
\end{aligned}
\]
Hence
\[
F_2:=(b^2+2s^2-2bsp)h-bcq-bsv=0. \tag{13}
\]

Likewise, the third angle equality gives, with $M=B/2$,
\[
 ((L-C)\times(K-C))((B-M)\cdot(K-M))
 =((B-M)\times(K-M))((L-C)\cdot(K-C)). \tag{14}
\]
Again this is a cross-multiplied sine-cosine equation, not tangent division. Its factors are
\[
\begin{aligned}
(L-C)\times(K-C)&=s(ch-bq-2rgq-rv),\\
(L-C)\cdot(K-C)&=s(bp-cg-2rhq+ru),\\
(B/2)\times(K-B/2)&=\frac{crq}{2},\\
(B/2)\cdot(K-B/2)&=\frac{c(c-2rp)}4.
\end{aligned} \tag{15}
\]
Subtracting right from left and cancelling the positive factor $cs/4$ gives
\[
\begin{aligned}
0={}&(ch-bq-2rgq-rv)(c-2rp)\\
&-2rq(bp-cg-2rhq+ru)\\
={}&c^2h-bcq-crv-2crhp\\
&+r^2(4gpq+2vp+4hq^2-2uq).
\end{aligned} \tag{16}
\]
Using (12),
\[
F_3:=(c^2+2r^2-2crp)h-bcq-crv=0. \tag{17}
\]
Thus right-angle cases remain included; the only cancelled factors were the positive numbers $br/4,cs/4$.

We invoke the certified **circumcentre linear-certificate lemma**. The stated circumcentre of triangle $AKL$ entails that $A,K,L$ are noncollinear. The lemma says it suffices to prove $T=0$, where
\[
T=2((C-B)\times L)|K|^2+2(K\times(C-B))|L|^2
 -(K\times L)(b^2-c^2). \tag{18}
\]
Define
\[
P_3=bcv+bsq-csh,
\qquad P_2=-bcv+brh-crq. \tag{19}
\]
We prove the certificate
\[
hT+P_3F_3+P_2F_2=0. \tag{20}
\]
Here is an explicit coefficient check. Insert
\[
|K|^2=c^2+r^2-2crp,
\qquad |L|^2=b^2+s^2-2bsp \tag{21}
\]
in (18), and (13),(17),(19) in the left side $E$ of (20). Replace $u,v$ via (6), and set
\[
\Delta=p^2+q^2-1,
\qquad \Gamma=g^2+h^2-1. \tag{22}
\]
Ordinary multiplication and collection by powers of $r,s$ gives this complete table (all omitted coefficients are zero):
\[
\begin{array}{c|l}
 r^is^j&[r^is^j]E\\ \hline
 r^2s&-2h(\Delta\Gamma bq+\Delta bq-\Delta ch+\Gamma bq)\\
 r^2&-2\Delta bch(-gq+hp)\\
 rs^2&2h(-\Delta\Gamma bh-\Delta bh-\Gamma bh+\Gamma cq)\\
 rs&4b^2h^2p(\Delta\Gamma+\Delta+\Gamma)\\
 r&-b\bigl(2\Delta^2\Gamma b^2h^2+2\Delta^2b^2h^2
 +4\Delta\Gamma b^2h^2-2\Delta\Gamma bchq\\
 &\qquad+3\Delta b^2h^2-2\Delta bchq
 +2\Gamma b^2h^2-2\Gamma bchq+\Gamma c^2q^2\bigr)\\
 s^2&2\Gamma bch(-gq+hp)\\
 s&bc\bigl(-4\Delta\Gamma bh^2-\Delta bh^2+4\Gamma bghpq
 +4\Gamma bh^2q^2-4\Gamma bh^2+\Gamma bq^2-2\Gamma chq\bigr)\\
 1&2b^3ch(-gq+hp)(\Delta\Gamma+\Delta+\Gamma).
\end{array} \tag{23}
\]
This table is hand-checkable directly: distribute the displayed formulas (13),(17)--(19),(21), substitute $u=gp+hq,v=hp-gq$, collect each $r^is^j$, and replace $p^2+q^2,g^2+h^2$ by $1+\Delta,1+\Gamma$. It uses no unreported algebraic or numerical assertion.

By the Pythagorean identities (7), $\Delta=\Gamma=0$, so every entry in (23) is zero. The table contains every coefficient of $E$, proving (20).

Now (13),(17),(20) give $hT=0$. Since $h>0$ by (8), $T=0$. The certified circumcentre linear-certificate lemma yields $OM=ON$, as required. ∎

## Promotable lemmas
- **Two-residual vector certificate.** In notation (3)--(7), the residuals (13),(17), target (18), and multipliers (19) satisfy $hT+P_3F_3+P_2F_2=0$. It is proved by the coefficient table (23).
