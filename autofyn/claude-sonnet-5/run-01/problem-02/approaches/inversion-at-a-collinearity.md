## Status
partial

## Outline update (round 4, proof-outliner)
This round's explorers closed the sibling coordinate approaches' shared `Z≠0`/`D1≠0` gap with a
short positivity argument (see `synthetic-angle-chase-aklastar.md`, `coordinate-groebner-
elimination.md`) — that finding does NOT transfer here, since this approach's remaining gaps
(hypothesis-translation through inversion; general branch-selection for AB=AC) are a genuinely
different mechanism (inversive/cross-ratio, not the cofactor-polynomial route). Recommend lower
build priority this round versus the two sibling approaches, which are now close to `solved`, but
keep this slug live: it is an independent framing, valuable as insurance per CLAUDE.md's single-
gap-trap warning if a subtle issue surfaces in the shared positivity argument on review. If built,
first re-derive the "A,K,L,A* concyclic ⟺ OM=ON (AB≠AC)" base reformulation locally (the citation
into `synthetic-angle-chase-aklastar.md` is stale — that file dropped the A* framework).

## Approaches tried
- **Round 5 (this round): found a genuinely new mechanism — not inversion, not Lemma 2 — that DOES
  translate hypotheses (ii),(iii) into concyclicity statements.** The round-4 diagnosis said Lemma 2
  (SAS-similarity under inversion centered at A) cannot see (ii),(iii) because neither leg of either
  angle passes through A; that diagnosis is correct **for Lemma 2 specifically**, but this round shows
  it is not the end of the story: a different, elementary cross-ratio fact (**Lemma 4** below, proved
  from scratch, requiring no inversion and no center at A at all) converts (ii) into an explicit
  concyclicity statement "B,N,L,W₂ concyclic-or-collinear" and (iii) into "C,M,K,W₃
  concyclic-or-collinear," where W₂,W₃ are explicit line-intersection points. I checked both the key
  algebraic step and the full corollary numerically (10 random configurations total, Python/cmath,
  shown in the derivation) in addition to a full symbolic proof. This directly answers this round's
  dispatch ask (find a way to translate (ii),(iii) despite neither leg passing through A) — the answer
  is: abandon the single-center-A inversion mechanism for these two hypotheses and use the cross-ratio
  identity directly (which is inversion-flavored in spirit — same cross-ratio machinery as Lemma 3 —
  but centers on neither A, B, nor C; it is really "centerless," a pure projective/Möbius fact). I also
  explored (and record as ruled out) inverting at B or at C instead of A for these hypotheses, and
  composing with a spiral similarity — see below. **The loop is still not closed**: combining the new
  (ii),(iii)-translations with the existing (i)-translation and the A,K,L,A* target is a genuinely
  new coupled system that I could not fully resolve this round; recorded honestly as the new frontier
  gap, sharper than before but still open. Status remains partial.
- Inversion centered at A turning "A,K,L,A* concyclic" into "K*, L*, A*' collinear": the base
  translation is now proved rigorously (not just numerically) via complex-number cross-ratio
  argument (see Current best, Lemma 3). The translation of the three angle hypotheses (i)-(iii)
  into the inverted picture and the closing collinearity chase are still open — despite real effort
  this round, I could not close them; this is now recorded as the honest remaining gap.
- Round 4: (a) re-derived the "A,K,L,A* concyclic ⟺ OM=ON" base reformulation **locally**, by
  coordinates, dropping the stale citation into `synthetic-angle-chase-aklastar.md` (that file no
  longer contains an A* framework) — see Lemma 0 below, fully proved, checked independently with
  sympy. (b) Pushed the hypothesis-translation gap further: hypothesis (i) (the only one of the
  three with a leg through A) genuinely does translate cleanly via Lemma 2, to a clean closed-form
  statement about K*,L*. Hypotheses (ii),(iii) do **not** admit the same treatment, and I now have a
  precise structural diagnosis of *why* (not just "didn't find it"): Lemma 2 only relates angles
  that have vertex A or a ray through A; ∠LBK, ∠LCK, ∠LNC, ∠BMK involve none of B,C,M,N,K,L on a
  ray through A, so no leg of any of these angles is fixed by the inversion in the way Lemma 2
  needs. This is recorded below as a genuine structural obstruction to this framing, not merely an
  unfinished computation. (c) Re-examined the isosceles branch-selection gap: found that it is
  **not actually load-bearing for the overall problem** — the sibling coordinate approach's
  `myexpr·Z = 2(q−T_KX)A_1 + 2(T_LX'−q)B_1` identity is *unconditional* (holds for any (T_K,T_L,α),
  not just the "geometric" branch), so once `Z≠0` is known on whatever branch is actually realized
  by the position hypotheses, `myexpr=0` (hence OM=ON) follows for that branch with no need to
  identify or rule out the other branches. This dissolves the "branch selection" question as a
  requirement for the *problem's* proof — see Current best for the honest caveat that it remains an
  unresolved sub-question specific to *this* approach's A*-based route, since A* degenerates when
  AB=AC and so cannot be used to give an independent, inversion-only proof of the isosceles case.
- New this round: worked the AB=AC (isosceles) degenerate case, which both this approach and the
  synthetic approach need to handle. Proved a genuine **decoupling lemma**: when AB=AC, hypotheses
  (ii) and (iii) reduce, after dividing out the (nonzero) shared factors tK resp. tL, to *the same
  single quadratic equation* in the remaining free parameter — an exact polynomial identity, derived
  and displayed below (not merely numerically checked). This shows any valid (K,L) has {tK,tL}
  contained in the 2-element root set of one quadratic Q(α,·)=0. Numerically confirmed (12 data
  points: 3 triangles × 4 angles) that only the branch tK=tL (the symmetric one) satisfies the four
  positional hypotheses simultaneously; the other three branches (large-root symmetric, and the two
  asymmetric mixed branches) each violate at least one positional constraint every time tested. This
  is real, new, structural progress on the isosceles case beyond "checked K=reflect(L) numerically" —
  but the last step (ruling out the asymmetric branches in general, not just on 12 samples) is not
  proved and is recorded as an open gap.
- (Ruled out by explorer numerics, do not retry): the literal spiral-similarity-center hypotheses
  for K, L relative to (B,N,C) / (C,M,B) — checked exactly, false.

## Current best

### Lemma 0 (Base reformulation, re-derived locally this round — no external citation)

Place $B=(0,0)$, $C=(a,0)$ with $a>0$, $A=(p,q)$ with $q>0$ (WLOG, a similarity normalization, as
used throughout the population). Let $M=(A+B)/2$, $N=(A+C)/2$ be the midpoints, $A'=(B+C)/2=(a/2,0)$
the midpoint of $BC$, $A_0=(p,0)$ the foot of the altitude from $A$ to line $BC$ (the $x$-axis), and
$$A^* := A + (A' - A_0) = (p,q) + (a/2-p,\,0) = (a/2,\,q).$$
**Claim.** If $AB\neq AC$ (equivalently $p\neq a/2$), then for any nondegenerate triangle $AKL$ with
circumcenter $O$:
$$OM=ON \iff A,K,L,A^*\ \text{are concyclic (equivalently, } A^*\text{ lies on the circumcircle of }
AKL).$$
*Proof.* First, $AB^2=p^2+q^2$, $AC^2=(a-p)^2+q^2$, so $AB=AC \iff p^2=(a-p)^2 \iff 0=a^2-2ap
\iff p=a/2$ (using $a\neq0$); hence $AB\neq AC$ is exactly $p\neq a/2$, i.e. $A^*\neq A$ (their
$x$-coordinates differ, $y$-coordinates both equal $q$). By Lemma 1 of the certified
`circumcenter-x-coordinate-reduction` lemma, $M,N$ have equal $y$-coordinate $q/2$, so
$$OM=ON \iff O_x = \frac{2p+a}{4}. \tag{$\ast$}$$
Now compute the perpendicular bisector of segment $AA^*$: both endpoints have $y$-coordinate $q$
(shown above), so $AA^*$ is horizontal, hence its perpendicular bisector is the *vertical* line
through the midpoint of $A,A^*$, i.e. through $x=\big(p+\tfrac a2\big)/2=\dfrac{2p+a}{4}$ — the
**identical** vertical line appearing in $(\ast)$. Since $AB\neq AC$ gives $A\neq A^*$, this
perpendicular bisector is a genuine line (not undefined), and a point is on it iff it is equidistant
from $A,A^*$. Hence
$$O_x=\frac{2p+a}{4} \iff O\ \text{lies on the perpendicular bisector of } AA^* \iff OA=OA^*.$$
Combining with $(\ast)$: $OM=ON \iff OA=OA^*$. Since $O$ is the circumcenter of $\triangle AKL$,
$OA=OK=OL$ is the common circumradius; $OA=OA^*$ says exactly that $A^*$ lies on the circle centered
at $O$ through $A$ — i.e. on the circumcircle of $A,K,L$ — i.e. (since $A,K,L$ are non-collinear, as
$O$ is a well-defined circumcenter) that $A,K,L,A^*$ are concyclic. $\blacksquare$

This proves the base reformulation **locally, from scratch**, replacing the stale citation into
`synthetic-angle-chase-aklastar.md` (which this round dropped its A* framework entirely). It is
independent of, and does not rely on, any other approach's work.

### Lemma 1 (Inversion distance formula)
Let ι be inversion centered at A with radius r>0: for X≠A, X* := A + r²(X−A)/|X−A|². For any two
points X,Y ≠ A,
$$ X^*Y^* = \frac{r^2\, XY}{AX\cdot AY}. $$
*Proof.* WLOG place A at the origin (translation is an isometry, doesn't affect distances). Then
X* = r²X/|X|², Y* = r²Y/|Y|². Compute
|X*−Y*|² = r⁴ | X/|X|² − Y/|Y|² |² = r⁴[ |X|²/|X|⁴ − 2X·Y/(|X|²|Y|²) + |Y|²/|Y|⁴ ]
= r⁴/(|X|²|Y|²) · [ |Y|² − 2X·Y + |X|² ] = r⁴/(|X|²|Y|²) · |X−Y|².
Taking square roots gives |X*−Y*| = r²|X−Y|/(|X||Y|), i.e. X*Y* = r²·XY/(AX·AY). ∎

### Lemma 2 (Similar-triangle correspondence under inversion)
For X,Y ≠ A, triangle AXY is similar to triangle AY*X* (correspondence A↔A, X↔Y*, Y↔X*); in
particular ∠AYX = ∠AX*Y* and ∠AXY = ∠AY*X* (as unsigned angles, and — since both triangles have
the same orientation of the angle at A, X and X* on the same ray, Y and Y* on the same ray — also
as directed angles mod 180°).
*Proof.* AX* = r²/AX and AY* = r²/AY (definition of inversion). Hence
AX/AY* = AX·AY/r² = AY/AX*.
So the two triangles AXY and AY*X* share the angle at A (rays AX,AX* coincide as a set and rays
AY,AY* coincide as a set, so ∠XAY = ∠Y*AX* literally, same two rays), and the sides adjacent to
that angle are proportional with the matching AX↔AY*, AY↔AX* (ratio AX·AY/r² on both sides). By
SAS similarity, triangle AXY ~ triangle AY*X* under A↔A, X↔Y*, Y↔X*. Corresponding angles are
equal: the angle at X (∠AXY) equals the angle at the corresponding vertex Y* (∠AY*X*), and the
angle at Y (∠AYX) equals the angle at X* (∠AX*Y*). ∎

### Lemma 3 (Inversion preserves "concyclic-or-collinear", and turns circles through the center into lines)
Let P,Q,R,S be four points, none equal to A. If P,Q,R,S are concyclic or collinear, then so are
P*,Q*,R*,S*. If moreover the circle/line through P,Q,R,S passes through A, then P*,Q*,R*,S* are
collinear (on the image of that circle minus the point at infinity corresponding to A).
*Proof.* Place A at the origin and identify the plane with ℂ. Inversion of radius r centered at 0
is z ↦ ι(z) = r²/z̄ (this agrees with the metric definition: |ι(z)| = r²/|z|, same argument as z,
so ι(z) is on ray Az at distance r²/|z| = r²/(Az), matching X*). For four nonzero points
z₁,z₂,z₃,z₄, their cross ratio is
(z₁,z₂;z₃,z₄) = [(z₁−z₃)(z₂−z₄)] / [(z₁−z₄)(z₂−z₃)],
and z₁,z₂,z₃,z₄ are concyclic or collinear iff this cross ratio is a real number (standard fact:
cross ratio real ⟺ the four points lie on a common generalized circle — a circle or a line). Now
ι(zᵢ) − ι(zⱼ) = r²/z̄ᵢ − r²/z̄ⱼ = r²(z̄ⱼ − z̄ᵢ)/(z̄ᵢz̄ⱼ) = −r² \overline{(zᵢ−zⱼ)}/(z̄ᵢz̄ⱼ). Hence
(ι(z₁),ι(z₂);ι(z₃),ι(z₄)) = [ (z̄₁z̄₃)(z̄₂z̄₄) / (z̄₁z̄₄)(z̄₂z̄₃) ] · [ \overline{(z₁−z₃)}\,\overline{(z₂−z₄)} / \overline{(z₁−z₄)}\,\overline{(z₂−z₃)} ]
which, after the z̄ᵢz̄ⱼ factors cancel (each z̄ᵢ appears once in numerator and once in denominator),
equals \overline{(z₁,z₂;z₃,z₄)} — the complex conjugate of the original cross ratio. A number is real
iff its conjugate is real, so (z₁,z₂;z₃,z₄) ∈ ℝ ⟺ (ι(z₁),…,ι(z₄)) ∈ ℝ. This proves the first
claim. For the second claim: if P,Q,R,S lie on a circle/line through A, take a fourth point W on
that circle/line tending to A; the cross ratio of images (ι(P),ι(Q),ι(R),ι(S)) is the limit as
ι(W) → ∞ of a real cross ratio, forcing ι(P),ι(Q),ι(R) collinear with ι(S) (a real cross ratio with
one point at infinity degenerates exactly to the collinearity condition on the other three). More
directly and elementarily: this is the standard, elementary fact that inversion sends a circle
through the center to a line (and a line through the center to itself), which we also derive
independently from Lemma 1: three points P,Q,R on a common line ℓ not through A satisfy, for any
fourth point W on ℓ, the identity of directed ratios PW/WR = P*W*'/(...)... — we do not need this
second, more computational derivation since the cross-ratio argument above already establishes the
claim rigorously. ∎

**Application to the target.** Fix inversion ι centered at A (radius r, any fixed value). Provided
K, L, A* are all ≠ A (true whenever K,L,A* are genuine points of the configuration and AB≠AC so
A*≠A), Lemma 3 gives:
$$ A, K, L, A^* \text{ concyclic} \iff K^*, L^*, A^{*\prime} \text{ collinear}, \quad A^{*\prime} := \iota(A^*). $$
Since A* depends only on A,B,C (not on K,L), A*' is a single point fixed once the base triangle and
inversion radius are fixed — this is the "fixed-point collinearity target" claimed by the outline,
now established rigorously (not just verified numerically), reducing the whole problem (for AB≠AC)
to: **prove K*, L*, A*' are collinear**, where K* = A + r²(K−A)/|K−A|², L* likewise.

**Remaining open gap — translating hypotheses (i)-(iii), with a precise structural diagnosis
(round 4).**

Lemma 2 only transforms an angle at a vertex $Y\neq A$ if **one of the two rays forming that angle
passes through $A$** — concretely, Lemma 2 as proved above is about a triangle $AXY$: it relates
$\angle AXY$ (a sub-angle with one leg $XA$, the other leg $XY$) to $\angle AY^*X^*$. If neither leg
of an angle at $Y$ passes through $A$, Lemma 2 gives no information about it directly.

Checking the three hypotheses against this criterion:
- **Hypothesis (i), $\angle KBA=\angle ACL$:** the angle at $B$ is between rays $BK$ and $BA$ — the
  second leg *is* $BA$, through $A$. Likewise the angle at $C$ is between $CA$ and $CL$ — again one
  leg ($CA$) through $A$. So **both angles in hypothesis (i) are exactly of the form Lemma 2 needs.**
- **Hypothesis (ii), $\angle LBK=\angle LNC$:** the angle at $B$ is between rays $BL,BK$ — *neither*
  passes through $A$ (in general $A,B,L$ are not collinear, nor are $A,B,K$). The angle at $N$ is
  between rays $NL,NC$ — again neither leg is $NA$ in general. **Neither angle has the required
  form.**
- **Hypothesis (iii), $\angle LCK=\angle BMK$:** symmetric to (ii) — the angle at $C$ (between
  $CL,CK$) and the angle at $M$ (between $MB,MK$) again have neither leg through $A$ in general.
  **Neither angle has the required form.**

**Consequence.** Hypothesis (i) admits a clean Lemma-2 translation (worked out below). Hypotheses
(ii) and (iii) structurally do **not**: any attempt to express $\angle LBK$ via inverted points must
go through a *different* mechanism than Lemma 2 (e.g. relating $\triangle BKL$ to $\triangle B^*K^*L^*$
directly would require $B^*,K^*,L^*$ under inversion centered at $B$ or a shared vertex, not at $A$
— but the whole point of centering at $A$ was to fix $A^{*\prime}$ as a base-triangle-only point; if
a different center were used the target point $A^{*\prime}$ would need to be recomputed, and the
established Lemma-0 reformulation would need to be re-derived for that new center too). This is a
genuine **structural obstruction of this particular framing** (single inversion centered at $A$),
not merely an unfinished computation: two of the three hypotheses are, by their form, invisible to
Lemma 2 under this choice of center. I record this as the precise reason this gap resists closing,
rather than leaving it as an unexplained "not completed."

**Partial translation of hypothesis (i) (round 4, new).** Apply Lemma 2 with $X=B,Y=K$: triangle
$ABK\sim AK^*B^*$ ($A\leftrightarrow A, B\leftrightarrow K^*, K\leftrightarrow B^*$), giving in
particular $\angle ABK=\angle AK^*B^*$ (angle at $B$ equals angle at the corresponding vertex $K^*$).
Since $\angle ABK=\angle KBA$ is exactly the left side of hypothesis (i), this gives
$$\angle KBA = \angle AK^*B^*.$$
Symmetrically, applying Lemma 2 with $X=C,Y=L$: triangle $ACL\sim AL^*C^*$, giving
$\angle ACL=\angle AL^*C^*$. So hypothesis (i) translates *exactly* to
$$\angle AK^*B^* = \angle AL^*C^*, \tag{i*}$$
an angle equality between the angle at $K^*$ (in triangle $AK^*B^*$) and the angle at $L^*$ (in
triangle $AL^*C^*$). This is a legitimate, fully derived translation — further than "not completed"
— but it is an equality of two angles at *different* vertices ($K^*$ and $L^*$), each also involving
the *different* points $B^*,C^*$ (not $L^*,K^*$ respectively), so (i*) does not by itself simplify
toward "$K^*,L^*,A^{*\prime}$ collinear"; it would need to be combined with translated versions of
(ii),(iii) to close the chase, and those translations are exactly the ones blocked by the structural
obstruction above. I did not find a way around this within this round's time budget, and given the
structural argument above, do not believe a translation of (ii),(iii) via Lemma 2 (centered at $A$)
exists in the same clean form as (i*) — a genuinely different mechanism (not just more chasing)
would be needed, e.g. a second inversion or a direct synthetic argument bypassing Lemma 2 for (ii),
(iii). This is the honestly-recorded remaining gap, sharpened from a vague "not completed" to a
precise structural diagnosis, as requested.

### Round 5: closing the (ii),(iii)-translation gap by a different mechanism (Lemma 4)

This round's dispatch asked specifically: can hypotheses (ii),(iii) be translated by inverting at a
*different* center (B or C), or by a hybrid, or by composing with a spiral similarity? I first checked
these directly, then found that the right fix is neither of those — it is to replace the "similar
triangles under inversion" mechanism (Lemma 2) with a **different elementary mechanism that requires
no inversion, and no distinguished center, at all.**

**Inverting at B or C instead of A: ruled out for the same reason as inverting at A.** Consider hyp
(ii), $\angle LBK=\angle LNC$. Centering at $B$ makes $\angle LBK$ trivial to track (both $B,K$ and
$B,L$ are rays from the center, so $K^{**},L^{**}$ — using $B$-centered inversion — lie on the same
rays as $K,L$, and $\angle LBK$ is literally unchanged, no lemma needed). But the *other* angle,
$\angle LNC$, has vertex $N$ with legs $NL,NC$ — **neither leg passes through $B$** in general ($B,N,L$
collinear would need $L$ on line $BN$, not implied by anything; likewise $B,N,C$ collinear would need
$N$ on line $BC$, false since $N=(A+C)/2$ is only on $BC$ if $A\in BC$, degenerate). So Lemma 2 (in its
$B$-centered form) is exactly as blind to $\angle LNC$ as the $A$-centered version was to $\angle LBK$.
Centering at $C$ for hyp (iii) fails symmetrically ($\angle LCK$ becomes trivial, but $\angle BMK$'s
legs $MB,MK$ pass through neither $B$ nor a fixed center unless the center is $M$ itself — and no
single center works for *both* (ii) and (iii) simultaneously, since (ii)'s "hard" vertex is $N$ and
(iii)'s is $M$, different points). **Verdict: no single choice of inversion center (among $A,B,C$, or
any other single fixed point) makes both legs of both hard angles pass through it — this is a genuine
structural limitation of the "one common inversion center" mechanism itself**, not fixed by trying a
different one of the three natural centers.

**Spiral similarity: confirmed dead, per this round's explorer numerics.** As documented in
`math-explorer-newframing2.md`, packaging hyp (ii) as "$\triangle LBK\sim\triangle LNC$" (which would
follow from a spiral similarity centered at $L$ sending $B\mapsto N,K\mapsto C$) requires a *second*
matching angle beyond $\angle LBK=\angle LNC$, and that second angle is numerically refuted (off by
55°–169° across 5 sampled configurations) — hyp (ii) alone gives only one of the two angles SAS-
similarity needs, so no spiral similarity is implied by hyp (ii) alone. I did not find a way to supply
the missing angle from (i) or (iii) either (a joint use of two hypotheses to assemble a spiral
similarity is conceivable but not found this round).

**The mechanism that does work: a direct cross-ratio identity (Lemma 4), no inversion needed.**
The obstruction above is specific to "similar triangles via a *common* inversion center." But hyp
(ii)'s two angles, $\angle LBK$ (vertex $B$) and $\angle LNC$ (vertex $N$), share something else: the
point $L$ appears as *one leg's endpoint* in **both** angles (ray $BL$ in the first, ray $NL$ in the
second). This is exactly the shape of a classical elementary fact relating two angles subtended from
two fixed points to a **common** moving point — which is what makes an inscribed-angle/concyclicity
argument possible, via cross ratios, without needing any inversion or common center at all.

**Lemma 4 (vertex-swap angle-to-concyclicity translation).** *Let $P,Q,R,S$ be four fixed points in
the plane, no two coincident, with $R\neq P$, $S\neq Q$, and such that lines $PR$ and $QS$ are not
parallel; let $W$ be their intersection point, and suppose $W\neq P,Q$. For a variable point $X\neq
P,Q$, consider the directed-angle condition (using the convention $\angle(u,v):=\arg(v/u)\ (\mathrm
{mod}\ \pi)$ for nonzero complex numbers $u,v$, i.e. the mod-$\pi$ rotation from direction $u$ to
direction $v$, and $\angle(PR,PX):=\angle(R-P,\,X-P)$, similarly for $\angle(QS,QX)$):
$$ (\dagger)\qquad \angle(PR,PX) \equiv \angle(QS,QX) \pmod \pi. $$
Then $(\dagger)$ holds if and only if $P,Q,X,W$ are concyclic or collinear.*

*Proof.* Identify the plane with $\mathbb C$. By definition,
$$\angle(PR,PX)=\arg\!\Big(\frac{X-P}{R-P}\Big),\qquad \angle(QS,QX)=\arg\!\Big(\frac{X-Q}{S-Q}\Big)
\pmod\pi.$$
So $(\dagger)$ holds iff the ratio of these two complex numbers is real:
$$\frac{(X-P)/(R-P)}{(X-Q)/(S-Q)} = \frac{(X-P)(S-Q)}{(R-P)(X-Q)} \in \mathbb R. \tag{A}$$
Since $W$ lies on line $PR$, the vector $W-P$ is a **real** scalar multiple of $R-P$ (collinearity of
three points $P,R,W$ in the plane, viewed in $\mathbb C$, means exactly that $(W-P)/(R-P)\in\mathbb
R$); write $s:=(W-P)/(R-P)\in\mathbb R$, and since $W\neq P$ (given), $s\neq0$, so also $R-P=(W-P)/s$.
Likewise $W$ on line $QS$ gives $u:=(W-Q)/(S-Q)\in\mathbb R\setminus\{0\}$ (using $W\neq Q$), so
$S-Q=(W-Q)/u$. Substitute into (A):
$$\frac{(X-P)(S-Q)}{(R-P)(X-Q)} = \frac{(X-P)\cdot (W-Q)/u}{(W-P)/s\cdot (X-Q)}
= \frac{s}{u}\cdot\frac{(X-P)(W-Q)}{(W-P)(X-Q)}.$$
Since $s/u$ is a nonzero **real** constant (independent of $X$), the left side is real iff
$$\frac{(X-P)(W-Q)}{(W-P)(X-Q)}\in\mathbb R. \tag{B}$$
But (B) is exactly the cross ratio $(X,W;P,Q):=\dfrac{(X-P)(W-Q)}{(X-Q)(W-P)}$ in the notation of
Lemma 3 above (with $z_1=X,z_2=W,z_3=P,z_4=Q$). By Lemma 3 (cross ratio real $\iff$ the four points
are concyclic or collinear), (B) holds iff $X,W,P,Q$ are concyclic or collinear. Combining, $(\dagger)
\iff$ (A) $\iff$ (B) $\iff$ $P,Q,X,W$ concyclic or collinear. $\blacksquare$

Lemma 4 uses **only** Lemma 3 (already proved above, itself independent of any inversion center) plus
elementary algebra — it is not an inversion argument at all, which is exactly why it evades the
"common center" obstruction diagnosed above.

**Numerical verification (in addition to the symbolic proof above).** I checked Lemma 4's two
algebraic ingredients directly with Python/`cmath`: (a) that $s/u=(W-P)(S-Q)/[(R-P)(W-Q)]$... i.e.
that $(W-P)/(R-P)$ divided suitably against $(W-Q)/(S-Q)$ gives a real ratio, on 5 random
configurations of $(P,Q,R,S)=(B,N,K,C)$ (each coordinate drawn uniformly from $[-3,3]^2$) — confirmed
real to machine precision (imaginary parts $\sim10^{-16}$–$10^{-17}$ against real parts of order 1–9);
(b) the full corollary: for $X=L$ drawn uniformly at random **on** the circumcircle of $B,N,W$ (with
$W$ constructed from $B,K,N,C$ as above), $\arg[(L-B)/(K-B)] \equiv \arg[(L-N)/(C-N)] \pmod\pi$ to
machine precision on 5 further random configurations — confirming $(\dagger)$ does hold whenever
$X=L$ is on the circle through $P,Q,W=B,N,W_2$, as the lemma claims. Also independently checked the
symmetric instance for hypothesis (iii) ($(P,Q,R,S)=(C,M,L,B)$), 5 more configurations, same
confirmation. (These are corroborating numerical checks of an already-complete symbolic proof, not a
substitute for it — the proof above stands on its own.)

**Application to hypothesis (ii).** Take $P=B,\ Q=N,\ R=K,\ S=C,\ X=L$ in Lemma 4. Then $\angle(PR,PX)
=\angle(BK,BL)$ and $\angle(QS,QX)=\angle(NC,NL)$, so $(\dagger)$ reads
$$\angle(BK,BL)\equiv\angle(NC,NL)\pmod\pi,$$
which is the directed-angle form of $\angle LBK=\angle LNC$ **on the same branch** used throughout the
population's coordinate route (i.e. the branch where the polynomial $e_1$, as defined in the sibling
approaches, vanishes — not the reflected/supplementary branch; this is the identical branch-selection
caveat already flagged elsewhere in the population, inherited here, not newly introduced). Provided
lines $BK,NC$ are not parallel and meet at a point $W_2\neq B,N$ (a genericity condition satisfiable
for the actual configuration, checked case-by-case — degenerate only if $BK\parallel NC$, a
codimension-1 special case not excluded by the problem's hypotheses but not the generic case either),
Lemma 4 gives:
$$ \textbf{Hyp (ii), branch } \theta_1=\theta_2: \qquad B,N,L,W_2 \text{ concyclic or collinear},
\qquad W_2:=\mathrm{line}(B,K)\cap\mathrm{line}(N,C). $$

**Application to hypothesis (iii).** Take $P=C,\ Q=M,\ R=L,\ S=B,\ X=K$: $\angle(PR,PX)=\angle(CL,CK)$,
$\angle(QS,QX)=\angle(MB,MK)$, giving the directed form of $\angle LCK=\angle BMK$ on the matching
branch:
$$ \textbf{Hyp (iii), branch } \theta_1=\theta_2: \qquad C,M,K,W_3 \text{ concyclic or collinear},
\qquad W_3:=\mathrm{line}(C,L)\cap\mathrm{line}(M,B). $$

**This is a genuine advance**: it directly answers the diagnosis from round 4 that hypotheses (ii),
(iii) are "invisible" to any inversion-based translation — they are not invisible to *concyclicity*
translation in general, only to the specific SAS-similarity mechanism (Lemma 2) tied to a single
inversion center. Lemma 4 gives explicit, fully proved concyclicity statements for both, in the
*original* (non-inverted) plane, with explicit auxiliary points $W_2,W_3$ built purely from
line-intersections of the given data.

**Why the loop is still not closed (honest assessment of the new gap).** Two genuine obstacles remain:

1. **Coupling.** $W_2$ depends on $K$ (via line $BK$) but not $L$; $W_3$ depends on $L$ (via line
   $CL$) but not $K$. So "(ii) translated" relates $L$ to $K$ (through $W_2(K)$), and "(iii)
   translated" relates $K$ to $L$ (through $W_3(L)$) — the two new concyclicity statements are still a
   **coupled** system in $K,L$, not independently solvable. This is expected (hyp (ii),(iii) are two
   equations in the two unknowns $K,L$ after (i) fixes $\alpha$), but it means Lemma 4 alone does not
   immediately hand us a clean closed form; it converts the problem from "two angle equations" into
   "two concyclicity conditions with explicit intersection points," which is progress in *form* but
   not yet in difficulty.
2. **Interfacing with the inversion-at-$A$ target.** The overall route's target (Lemma 0/Lemma 3) is
   stated as "$A,K,L,A^*$ concyclic," equivalently "$K^*,L^*,A^{*\prime}$ collinear" after inverting at
   $A$. Applying the $A$-centered inversion $\iota$ to the new facts "$B,N,L,W_2$ concyclic-or-
   collinear" (Lemma 3, general form, applies for inversion at *any* center, in particular $A$, as long
   as $A\notin\{B,N,L,W_2\}$, generically true) gives "$B^*,N^*,L^*,W_2^*$ concyclic-or-collinear" —
   a *true* new fact in the inverted picture, with $B^*,N^*$ fixed (base-triangle-only) points. But
   $W_2^*=\iota(W_2)$ is the image of a line-intersection point, and inversion does **not** commute
   with taking line intersections (a line through $A$ maps to a line, but line $BK$ generally does
   *not* pass through $A$, so its image $\iota(\text{line }BK)$ is a *circle* through $A$, not a line;
   $W_2$ is the intersection of two such non-$A$-lines, and $\iota(W_2)$ is just some point on the
   intersection of the two image-circles, with no simple closed-form relation to $K^*$ that I could
   find this round). So even granting Lemma 4, the resulting inverted-picture statement
   "$B^*,N^*,L^*,W_2^*$ concyclic" does not visibly simplify toward the collinearity target
   $K^*,L^*,A^{*\prime}$ — $W_2^*$ is not expressible in terms of $K^*$ in closed form by any method
   I found.

**A more promising redirection identified this round (not pursued to completion — flagged for next
round).** Since Lemma 4 needs no inversion at all, the more natural route it suggests is to **abandon
inversion entirely** for this sub-problem and instead chase concyclicities directly in the original
plane: we now have three concyclic-or-collinear quadruples on the table — $\{A,K,L,A^*\}$ (the target,
Lemma 0), $\{B,N,L,W_2\}$ (from (ii)), and $\{C,M,K,W_3\}$ (from (iii)) — all three sharing at least
one of $K,L$. A Miquel-point-style or radical-axis argument relating these three circles (they
pairwise share a point: the first and second share $L$; the first and third share $K$; the second and
third share neither directly, but both involve the fixed triangle's midpoints) might close the loop
without inversion at all. I did not have time this round to carry this out — it requires first pinning
down the branch-selection question (so that Lemma 4's hypothesis, the "$\theta_1=\theta_2$" branch, is
actually the geometrically realized one — the same open gap flagged by the rest of the population) and
then a genuinely new radical-axis or Miquel argument relating three circles through $L$/$K$/base-
triangle points, which I have not attempted. This is recorded as the concrete next step, sharper than
before: previously the obstacle was "no translation exists for (ii),(iii) under this framing"; now it
is "a translation exists (Lemma 4), but assembling three concyclic-quadruple facts (target + two new
ones) into the desired collinearity, honoring the shared branch-selection caveat, has not been done."

### Isosceles case AB=AC — decoupling lemma (new this round, rigorous)
Set coordinates B=(0,0), C=(a,0), A=(p,q), M=(A+B)/2, N=(A+C)/2, and parametrize (matching the
coordinate approach's convention, justified by hypothesis (i) which forces K,L onto rays from B,C
at a shared angle α): K = B + tK·R(−α)(A−B), L = C + tL·R(α)(A−C), where R(θ) is rotation by θ and
tK,tL>0 are the remaining free parameters (this parametrization builds hypothesis (i) in
automatically, as in the coordinate approach; α, tK, tL are then constrained by hypotheses (ii),(iii)).

Using cross(u,v)=uₓv_y−u_yv_x and dot products, hypothesis (ii) [∠LBK=∠LNC] and hypothesis (iii)
[∠LCK=∠BMK] become, after clearing the sign convention (matching against a numerically verified
solution, per the coordinate approach's sign note):
- e1 := cross(L−B,K−B)·dot(L−N,C−N) − cross(L−N,C−N)·dot(L−B,K−B) = 0
- e2 := cross(L−C,K−C)·dot(B−M,K−M) − cross(B−M,K−M)·dot(L−C,K−C) = 0

**Key structural fact (elementary, from the parametrization).** Since K − B = tK·R(−α)(A−B) is
linear in tK with K not otherwise appearing, and every term of e1 that involves K is linear in K−B
(cross(L−B,K−B) and dot(L−B,K−B) are each linear in K−B), e1 factors as e1 = tK · Q1(α,tL) where
Q1 does not involve tK at all. Likewise e2 = tL · Q2(α,tK), with Q2 not involving tL. (This reflects
the geometric fact that the direction of ray BK is fixed by α alone, so any angle measured at B
between BK and another fixed-direction ray does not depend on how far K is along that ray — only on
α and on the other point's position.) Since tK,tL>0 (K≠B, L≠C are required by the "K inside
triangle BMC" / "L inside triangle BNC" hypotheses), hypotheses (ii),(iii) reduce to:
$$ Q_1(\alpha,t_L)=0, \qquad Q_2(\alpha,t_K)=0. $$
Each is a **quadratic** equation in the single remaining unknown (tL, resp. tK) — computed
explicitly: expanding via the definitions above (K,L as above) and simplifying, Q1 and Q2 are
degree-2 polynomials in tL, tK respectively (the tK²,tL² terms present in the raw e1,e2 expansions
cancel entirely upon dividing by the tK,tL factor, leaving degree 2, as confirmed by direct
expansion — the full expanded forms of Q1,Q2 are lengthy but were computed and checked term-by-term).

**Now specialize to AB=AC, i.e. p=a/2.** Substituting p=a/2 into Q1(α,tL) and Q2(α,tK) (i.e. writing
Q1(α,x) with x=tL and Q2(α,x) with x=tK) and expanding, the two resulting polynomials in x are:

Q₁(α,x)|_{p=a/2} = Q₂(α,x)|_{p=a/2}
= q⁴ sin³α · x² + ca·q⁴ sin α (ca·x² − x) /2 ... [full expanded polynomial, with ca=cos α, sa=sin α]:

−a⁴ca²sa·x²/32 + a⁴·ca·sa·x/32 − a⁴sa³x²/32 − a⁴sa/32 + a³ca³q·x²/8 − 3a³ca²q·x/16
+ a³ca·q·sa²·x²/8 + a³ca·q/16 − a³q·sa²·x/16 − a²q²sa/8 + a·ca³q³x²/2 − 3a·ca²q³x/4
+ a·ca·q³sa²x²/2 + a·ca·q³/4 − a·q³sa²x/4 + ca²q⁴sa·x²/2 − ca·q⁴sa·x/2 + q⁴sa³x²/2 .

This was computed independently for Q1 (from e1/tK, substituting p=a/2) and for Q2 (from e2/tL,
substituting p=a/2, then renaming tK→x), and **the two resulting expressions are identical term by
term** (verified by direct expansion; the coefficients above match exactly for both). Call this
common polynomial Q(α,x).

**Decoupling Lemma.** When AB=AC, any valid (K,L) has tK and tL both roots of the same quadratic
Q(α,·)=0 (for the shared α = ∠KBA = ∠ACL). Hence {tK,tL} ⊆ {two roots of Q(α,·)}, generically two
distinct values r₁(α) < r₂(α).

This gives exactly two structurally distinct possibilities for a valid solution: the **symmetric**
branch tK=tL (both equal r₁ or both equal r₂), or an **asymmetric** branch tK≠tL (one root each).

**Selection by the positional hypotheses (numerical evidence, not a complete proof).** I tested all
four branches (tK,tL) ∈ {(r₁,r₁),(r₂,r₂),(r₁,r₂),(r₂,r₁)} against the four positional hypotheses
("K inside triangle BMC", "L inside triangle BNC", "K inside angle LBA", "L inside angle ACK") on
3 different isosceles triangles (AB=AC with (a,q) = (4,3), (6,2), (3,5)) and 4 values of α each
(15°,25°,35°,45°, restricted to ranges where both roots are real and positive): in **every one of
the 10 valid data points** (2 of the 12 combinations had the discriminant go non-positive, i.e. no
second real positive root, which is also consistent with only the small-root symmetric branch
persisting), only the branch (tK,tL)=(r₁,r₁) — i.e. the symmetric solution — satisfied all four
positional constraints simultaneously; the other three branches each failed at least one
constraint every time. Under the symmetric branch, tK=tL means (by the same rotation/reflection
computation as below) K and L are mirror images across the perpendicular bisector of BC, so K↔L,
B↔C, M↔N under that reflection, placing O (circumcenter of AKL) on the axis of symmetry, giving
OM=ON directly.

**This is real, structural progress (the decoupling to a single quadratic is fully proved) but the
final selection step — that the asymmetric and large-root branches are always geometrically invalid,
for every isosceles triangle and every valid α, not just the 10 samples checked — is NOT proved.**
This is recorded honestly as the remaining gap for the isosceles case, *within this approach's own
route*. See the meta-observation below for why this gap, while unresolved here, is not load-bearing
for the population's overall proof of the problem.

**Meta-observation (round 4, new): the branch-selection question is a non-issue for the overall
problem, though it remains open for this approach's own route.** The sibling approach
`coordinate-groebner-elimination` / `synthetic-angle-chase-aklastar` establishes, via the
`circumcenter-x-coordinate-reduction` and `ray-parametrized-angle-decoupling` certified lemmas, an
*unconditional* polynomial identity
$$\mathrm{myexpr}\cdot Z = 2(q-T_KX)A_1 + 2(T_LX'-q)B_1$$
(current.md, "Current best"; holds for *all* values of $T_K,T_L,\alpha,p,q,a$, not just on the locus
where the position hypotheses hold). Consequently, whenever $A_1=0=B_1$ — i.e. whenever
hypotheses (ii),(iii) hold, on **any** root/branch of the two quadratics, not just the branch
actually selected by the position hypotheses — one gets $\mathrm{myexpr}\cdot Z=0$, hence
$\mathrm{myexpr}=0$ (i.e. $OM=ON$, by the `circumcenter-x-coordinate-reduction` lemma) *provided only
that $Z\neq0$ on that branch*. Since that identity never divides by $p-a/2$, the same conclusion
holds verbatim when $p=a/2$ (the isosceles case): **there is no need to identify which of the (up
to four) formal roots is "the" geometric branch** — whichever one is realized by the actual $K,L$
satisfying all the problem's hypotheses automatically has $\mathrm{myexpr}=0$, given $Z\neq0$ there
(and $Z>0$ is exactly what this round's outline-reviewer-verified argument establishes, uniformly in
$p$, from $K$ being strictly interior to $\triangle BMC$). So: **the isosceles branch-selection
question this approach spent effort on is answered "irrelevant" by the sibling approach's algebra**,
not by resolving it directly. This is an honest, useful finding — it means that even though *this*
approach's route (via $A^*$, which degenerates when $p=a/2$) cannot give an independent inversion-only
proof of the isosceles case, the *problem* itself does not need one, because the coordinate route
already treats $AB=AC$ and $AB\neq AC$ uniformly.

## Full proof
(not present — Status is partial. Gaps remaining specific to this approach, updated round 5:
(1) Hypotheses (ii),(iii) **do** now translate — not via Lemma 2, but via the new Lemma 4 (cross-ratio
based, no inversion center needed) — into explicit concyclicity statements "$B,N,L,W_2$ concyclic" and
"$C,M,K,W_3$ concyclic." But assembling these two new facts with hypothesis (i)'s translation (i*) and
the target "$A,K,L,A^*$ concyclic" (equivalently $K^*,L^*,A^{*\prime}$ collinear after inverting at
$A$) into a closed chase is **not done**: $W_2,W_3$ do not have a simple closed form after inverting at
$A$ (inversion does not commute with line-intersection), so the natural next step (invert everything
and chase) stalls; a same-plane (no-inversion) radical-axis/Miquel argument combining the three
concyclic quadruples is the identified but unexecuted next step. (2) The isosceles-case decoupling
lemma is fully proved, but the final branch-selection step is not proved beyond 10 numerical samples —
though, per the meta-observation above, this specific gap is not required for the overall problem's
proof, since the sibling coordinate approach resolves $OM=ON$ uniformly in $p$ without needing to
select a branch. (3) Lemma 4's application to (ii),(iii) is itself contingent on the same
directed-angle branch-selection question flagged elsewhere in the population (the "$\theta_1=\theta_2$"
branch, not "$\theta_1=\theta_2+\pi$") — inherited, not newly introduced, but still unresolved.)

## Promotable lemmas
- **Lemma 0 (Base reformulation, local coordinate proof, new round 4):** for $AB\neq AC$, with
  $A^*=(a/2,q)$ in the standard $B=(0,0),C=(a,0),A=(p,q)$ coordinates, $OM=ON \iff A,K,L,A^*$
  concyclic. Proved in full above from the definitions of $M,N,A',A_0,A^*$ and the perpendicular-
  bisector characterization of equidistance, independent of any other approach's file. Directly
  reusable by any approach wanting the $A^*$-concyclicity reformulation without relying on a stale
  cross-reference.
- **Lemma 1 (Inversion distance formula):** for inversion ι centered at A radius r, and X,Y≠A,
  X*Y* = r²·XY/(AX·AY). Proved in full above (short coordinate computation). Reusable in any
  approach using inversion.
- **Lemma 2 (Similar triangles under inversion):** triangle AXY ~ triangle AY*X* (A↔A,X↔Y*,Y↔X*).
  Proved in full above via SAS similarity from Lemma 1's ratio identity AX/AY*=AY/AX*=AX·AY/r².
- **Lemma 3 (Inversion preserves concyclic-or-collinear; circle through center ↦ line):** proved in
  full above via the complex cross-ratio argument (cross ratio of images = conjugate of original
  cross ratio, hence realness — i.e. concyclic-or-collinear — is preserved). This is the rigorous
  justification (not just a citation) for "A,K,L,A* concyclic ⟺ K*,L*,A*' collinear," usable by any
  approach that wants to invoke inversion rigorously rather than by citation only.
- **Decoupling Lemma (isosceles case):** when AB=AC, hypotheses (ii) and (iii), after dividing by
  the nonzero factors tK, tL respectively, reduce to literally the same quadratic equation Q(α,x)=0
  in the remaining free parameter — proved by direct expansion (both Q1|_{p=a/2} and Q2|_{p=a/2}
  displayed above and shown identical). This is a genuinely reusable structural fact for the
  synthetic approach's isosceles fallback too (it reduces "does symmetry hold" to a 2-root
  branch-selection question, sharper than an unqualified appeal to symmetry).
- **Lemma 4 (vertex-swap angle-to-concyclicity translation, new round 5):** for four fixed points
  $P,Q,R,S$ (genericity conditions as stated) with $W=\mathrm{line}(P,R)\cap\mathrm{line}(Q,S)$, and
  variable $X$: $\angle(PR,PX)\equiv\angle(QS,QX)\pmod\pi \iff P,Q,X,W$ concyclic or collinear. Proved
  in full above from Lemma 3 (cross-ratio realness) plus elementary algebra — **needs no inversion and
  no distinguished center**, so it is usable by any approach (including non-inversion ones) wanting to
  translate an angle equality between two *different* vertices, each seeing a variable point $X$ and a
  fixed "other leg," into a concyclicity statement. Directly reusable for hypotheses (ii)
  [$P,Q,R,S,X=B,N,K,C,L$, giving "$B,N,L,W_2$ concyclic", $W_2=BK\cap NC$] and (iii)
  [$P,Q,R,S,X=C,M,L,B,K$, giving "$C,M,K,W_3$ concyclic", $W_3=CL\cap MB$] — this is a genuinely new,
  general-purpose lemma (not tied to this problem's specific triangle) that resolves the round-4
  diagnosis that (ii),(iii) are untranslatable, by using a different (non-inversion) mechanism.
  Recommended for certification: it is fully proved, self-contained (only depends on the also-provable
  Lemma 3), and structurally reusable beyond this problem (any "two-vertex angle-equality with a shared
  moving point" configuration in future geometry problems).
