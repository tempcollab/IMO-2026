# Lemma: Cevian cut formula and identity (★)

**Statement.** Label the current triangle by its angles $(p,q,r)$, $p+q+r=180°$, all
positive. A legal Mulan move picks a vertex (angle $p$) and a point $X$ in the open
interior of the opposite side, and cuts from $X$ to that vertex. Writing
$x_1=\angle QPX\in(0,p)$ for the portion of angle $p$ cut off (where $Q,R$ are the
other two vertices, angles $q,r$), $x_1$ ranges over the *entire* open interval
$(0,p)$ as $X$ ranges over the open segment $QR$ (by the Intermediate Value Theorem
applied to the continuous, strictly monotone map $X\mapsto x_1$, with $x_1\to0$ as
$X\to Q$ and $x_1\to p$ as $X\to R$). The two resulting triangles have angle-sets
$$A=\{q,\,x_1,\,r+p-x_1\},\qquad B=\{r,\,p-x_1,\,q+x_1\}.$$

**Identity (★).** $(r+p-x_1)+(q+x_1)=p+q+r=180°$ for every $x_1$: the two "new"
(at-$X$) angles of $A$ and $B$ are always supplementary.

**Proof.** In triangle $PXQ$ (=A): angles are $x_1$ (at $P$), $q$ (at $Q$, unchanged
from the original triangle), and $s:=\angle PXQ = 180°-x_1-q$ (angle sum). In triangle
$PXR$ (=B): angles are $p-x_1$ (at $P$), $r$ (at $R$, unchanged), and $\angle PXR =
180°-s$ (since $Q,X,R$ are collinear) $= x_1+q$. Using $r+p-x_1=(180-q)-x_1=180-x_1-q=s$,
the two triangles' angle-sets are exactly as stated. Identity (★) is then immediate
algebraic cancellation of $x_1$: $(r+p-x_1)+(q+x_1)=p+q+r=180°$. $\blacksquare$

**Source.** Independently derived and cross-verified in `dyadic-scaffold`,
`corrected-genericity-bound`, and `binary-word-invariant` (all identical). Certified by
proof-reviewer round 2 by direct hand re-derivation.
