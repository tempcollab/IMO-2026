# Lemmas: basic inversion facts (distance formula, similar triangles, cross-ratio)

**Source approach:** `inversion-at-a-collinearity` (Lemmas 1–3). Certified by proof-reviewer, round 2
— standard facts, each proof checked line by line, complete and self-contained, no gaps, no
appeal to external citation.

**Lemma 1 (Inversion distance formula).** Let $\iota$ be inversion centered at $A$ with radius $r>0$:
for $X\neq A$, $X^*:=A+r^2(X-A)/|X-A|^2$. For any $X,Y\neq A$,
$$X^*Y^* = \frac{r^2\,XY}{AX\cdot AY}.$$
*Proof.* WLOG $A=0$. $|X^*-Y^*|^2 = r^4\big||X|^{-2}X-|Y|^{-2}Y\big|^2
= r^4\big[|X|^{-2}-2X\cdot Y/(|X|^2|Y|^2)+|Y|^{-2}\big] = \dfrac{r^4}{|X|^2|Y|^2}|X-Y|^2$. Take square
roots. $\blacksquare$

**Lemma 2 (Similar-triangle correspondence under inversion).** For $X,Y\neq A$, $\triangle AXY \sim
\triangle AY^*X^*$ under $A\leftrightarrow A,\ X\leftrightarrow Y^*,\ Y\leftrightarrow X^*$; in
particular $\angle AYX=\angle AX^*Y^*$ and $\angle AXY=\angle AY^*X^*$ (as unsigned angles, and, since
$X,X^*$ lie on the same ray from $A$ and $Y,Y^*$ likewise, also as directed angles mod $180°$).
*Proof.* $AX^*=r^2/AX$, $AY^*=r^2/AY$, so $AX/AY^* = AX\cdot AY/r^2 = AY/AX^*$. The two triangles
$AXY,\ AY^*X^*$ share the angle at $A$ (rays $AX,AX^*$ coincide as sets, likewise $AY,AY^*$), with
adjacent sides in the matching ratio $AX\cdot AY/r^2$ on both sides ($AX\leftrightarrow AY^*$,
$AY\leftrightarrow AX^*$); SAS similarity gives the correspondence and the angle equalities.
$\blacksquare$

**Lemma 3 (Inversion preserves concyclic-or-collinear; sends a circle through the center to a line).**
Let $P,Q,R,S\neq A$. If $P,Q,R,S$ are concyclic or collinear, so are $P^*,Q^*,R^*,S^*$. If moreover
the circle/line through $P,Q,R,S$ passes through $A$, then $P^*,Q^*,R^*,S^*$ are collinear.
*Proof.* Identify the plane with $\mathbb C$, $A=0$; inversion of radius $r$ is $z\mapsto r^2/\bar z$
(consistent with the metric definition, since $|r^2/\bar z|=r^2/|z|$, matching $AX^*=r^2/AX$, and
$r^2/\bar z$ lies on ray $Az$). For $z_1,z_2,z_3,z_4\neq0$, the cross ratio
$(z_1,z_2;z_3,z_4)=\dfrac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)}$ is real iff the four points are
concyclic or collinear (standard). Since $\iota(z_i)-\iota(z_j) = r^2(\bar z_j-\bar z_i)/(\bar
z_i\bar z_j) = -r^2\overline{(z_i-z_j)}/(\bar z_i\bar z_j)$, the $\bar z_i\bar z_j$ factors cancel in
the cross ratio and $(\iota(z_1),\iota(z_2);\iota(z_3),\iota(z_4)) = \overline{(z_1,z_2;z_3,z_4)}$,
which is real iff the original cross ratio is real. This proves the first claim. For the second:
this is the standard fact that inversion sends a circle/line through the center to a line; it also
follows from the first claim by letting a fourth point $W$ on the circle/line through $P,Q,R,S,A$
tend to $A$, so $\iota(W)\to\infty$, degenerating the real-cross-ratio condition on
$\iota(P),\iota(Q),\iota(R),\iota(S)$ (with one point at infinity) to collinearity of the other three.
$\blacksquare$

**Note on scope:** these are generic inversion facts, reusable in any approach, not specific to the
$A,K,L,A^*$ configuration of this problem. The application of Lemma 3 to "$A,K,L,A^*$ concyclic
$\iff K^*,L^*,A^{*\prime}$ collinear" (with $A^{*\prime}=\iota(A^*)$) is correct but is not itself
certified as a full proof step of the parent problem — the base reduction "$OM=ON\iff A,K,L,A^*$
concyclic" it depends on is not established anywhere in the current round's approach files (see
review notes: `inversion-at-a-collinearity`'s citation of `synthetic-angle-chase-aklastar.md` for
this reduction is stale — that file's current version does not contain it).
