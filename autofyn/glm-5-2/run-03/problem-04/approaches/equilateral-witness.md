# equilateral-witness — Mulan's triangle game (IMO 2026 P4)

## Status
solved

## Approaches tried
- (round 1) **Equilateral-witness exclusion via the obtuse-angle safe set.** The outliner's original crux ("the equilateral E=(60,60,60) is self-closed under the supplementary reflection for every non-divisor θ") was REFUTED by the gate: for θ=72°, cutting E to a vertex with α=48° yields child (48,60,72), which carries θ. Fixed by abandoning the claim that E *alone* is closed and instead identifying the genuinely reflection-closed safe set **S = {triangles with every angle ≤ 90°}** for the clean half-range θ∈(90°,180°). The supplementary identity P₁+P₂=180 forces the two fresh P-angles to straddle 90°, so at most one child leaves S — Shan-Yu keeps the other. This is a geometric (not arithmetic-taint) framing, independent of the shared wall for half the non-divisor range. The remaining non-divisor range θ∈(0°,90°] is covered by the taint-free casework (shared lemma, proved in full below). Inclusion via the alignment move (M1) + reduce descent (M2), proved end-to-end. Both directions complete. — outcome: SOLVED.

## Current best
Complete characterization: Mulan guarantees victory in finitely many steps if and only if θ = 180°/n for some integer n ≥ 2. Both directions proved; the exclusion's distinct contribution is the geometric obtuse-angle safe set S for θ∈(90°,180°), an independent framing of the supplementary-reflection leverage, with the taint-free casework carrying θ∈(0°,90°].

## Full proof

**Answer.** Mulan can guarantee victory in finitely many steps, regardless of how Shan-Yu plays, if and only if
\[
\theta=\frac{180^{\circ}}{n}\quad\text{for some integer }n\ge 2
\]
(equivalently, $180^{\circ}/\theta$ is an integer $\ge 2$).

We prove both directions. Throughout angles are measured in degrees and every triangle is nondegenerate (three positive angles summing to $180^{\circ}$). We invoke the **cut operation** (verified by direct angle-chasing, KB: *Invariants & monovariants*): if Mulan cuts to the vertex of angle $A$ with parameter $\alpha\in(0,A)$ (the part $\angle BAP$ on the side of $B$), and the other two angles are $B,C$, the two children are
\[
C_1=(\alpha,\;B,\;180-\alpha-B),\qquad C_2=(A-\alpha,\;C,\;B+\alpha).
\]
Both sum to $180$ and all six entries are positive ($\alpha\in(0,A)$ gives $\alpha>0$, $A-\alpha>0$; the P-angles $180-\alpha-B=A+C-\alpha>C>0$ and $B+\alpha>0$, and each $<180$ since the co-P angle is positive). Reparametrizing $\beta=B+\alpha\in(B,\,180-C)$, the two *fresh* angles at $P$ are $180-\beta$ and $\beta$ — **supplementary** (sum $180^{\circ}$). This supplementary pairing is the structural lever of the whole proof.

---

### I. Inclusion: $\theta=180^{\circ}/n\;(n\ge 2)$ $\Rightarrow$ Mulan wins

We give a bounded forcing strategy (KB: *Invariants & monovariants* + *Induction / infinite descent*). Fix $n\ge 2$ and $\theta=180^{\circ}/n$. Let the current triangle have angles $(A,B,C)$, $A+B+C=180=n\theta$.

#### Lemma M2 (reduce / descent).
*If some angle of the current triangle equals $m\theta$ with $m\ge 2$, then Mulan forces a win in at most $m-1$ further moves.*

*Proof.* Let the angle $m\theta$ sit at vertex $V$; write the triangle as $(m\theta,\,B,\,C)$ with $B+C=180-m\theta=(n-m)\theta>0$ (so $m\le n-1$, since $m\theta<180$). Mulan cuts to $V$ with $\alpha=\theta$ (valid: $\theta<m\theta$ since $m\ge 2$). The two children are
\[
C_1=(\theta,\;B,\;180-\theta-B)=(\theta,\,B,\,(m-1)\theta+C),
\]
\[
C_2=((m-1)\theta,\;C,\;B+\theta).
\]
Child $C_1$ has $\theta$ as its $\alpha$-slot angle, so if Shan-Yu keeps $C_1$ the game stops immediately with a Mulan win. To survive, Shan-Yu must keep $C_2$, whose vertex-$V$ angle is $(m-1)\theta$. All angles of $C_2$ are positive: $(m-1)\theta>0$ ($m\ge 2$), $C>0$ (inherited), $B+\theta\in(\theta,\,B+m\theta)\subset(0,180)$ since $B+m\theta=B+A=180-C<180$. Thus after one forced move the tracked vertex carries $(m-1)\theta$, still a positive integer multiple of $\theta$ at the *same geometric vertex* (no relocation needed — the tracked vertex is invariantly "the vertex Mulan just cut").

If several angles are multiples of $\theta$ simultaneously, Mulan commits to descending one fixed vertex; its angle decreases by exactly $\theta$ per move and stays a multiple of $\theta$ throughout, so the commitment cannot cycle. Iterating, the level runs $m\to m-1\to\cdots\to 2$. At level $2$ the same cut ($\alpha=\theta$) gives $C_1$ the $\alpha$-slot $\theta$ and $C_2$ the $\alpha$-slot $2\theta-\theta=\theta$: **both** children contain $\theta$, so Mulan wins regardless of Shan-Yu's discard. The descent takes $m-2$ reduce moves to reach level $2$, plus one winning move: $m-1\le n-2$ moves total. ∎

#### Lemma M1 (alignment) for $n\ge 3$.
*From any triangle not containing $\theta$ (whether or not it contains a higher multiple), Mulan can in one move create an exact positive multiple of $\theta$ in **both** children's P-slots.*

*Proof.* Cut to a largest angle $A$ (so $A\ge 60^{\circ}$, since the largest angle of any triangle is at least $60^{\circ}$). We have $\theta=180^{\circ}/n\le 60^{\circ}$. If $A=60^{\circ}$ then the triangle is equilateral and $A=B=C=60^{\circ}$; in that case $60^{\circ}=\theta$ forces $n=3$, and the equilateral already contains $\theta$ — Mulan has already won (excluded from the "not containing $\theta$" hypothesis). Hence, under the hypothesis, $A>60^{\circ}\ge\theta$, so $A>\theta$ (strictly: if $\theta=60^{\circ}$ then $A>60^{\circ}=\theta$; if $\theta<60^{\circ}$ then $A\ge 60^{\circ}>\theta$).

The open interval $(B,\,A+B)$ has length $A>\theta$. Multiples of $\theta$ are spaced exactly $\theta$ apart, so by the **pigeonhole principle** (KB: *Pigeonhole / extremal*) an open interval of length strictly greater than $\theta$ contains a multiple of $\theta$ strictly in its interior: there is an integer $k$ with $B<k\theta<A+B$. Set $\beta=k\theta$, i.e. $\alpha=k\theta-B\in(0,A)$. Then
\[
\text{P-angle of }C_2 = B+\alpha=k\theta,\qquad
\text{P-angle of }C_1 = 180-\beta=180-k\theta=(n-k)\theta,
\]
using $180=n\theta$. Both children carry an exact positive multiple of $\theta$ in a P-slot.

Bounds: $k\theta>B>0\Rightarrow k\ge 1$; $k\theta<A+B=180-C<180=n\theta\Rightarrow k<n$, so $k\le n-1$; hence $1\le k\le n-1$ and likewise $1\le n-k\le n-1$. Thus $k\theta,(n-k)\theta\in[\theta,(n-1)\theta]\subset(0,180)$. Positivity of all six child angles: $C_1=(k\theta-B,\,B,\,(n-k)\theta)$ with $k\theta-B>0$ (above), $B>0$, $(n-k)\theta>0$; $C_2=(A+B-k\theta,\,C,\,k\theta)$ with $A+B-k\theta=(A+B)-k\theta>0$ (above), $C>0$, $k\theta>0$. All valid. ∎

#### Putting inclusion together ($n\ge 3$).
Mulan's strategy: if $\theta$ is already present, win (0 moves). Else if some angle is $m\theta$, $m\ge 2$, apply M2 (win in $\le m-1\le n-2$ moves). Else (no angle a multiple of $\theta$) apply M1 once: both children now carry a positive multiple $k\theta$ and $(n-k)\theta$ ($1\le k\le n-1$). Whichever child Shan-Yu keeps carries some $m\theta$ with $1\le m\le n-1$; if $m=1$ it already has $\theta$ (win in the 1 alignment move), and if $m\ge 2$ apply M2 (win in $\le m-1\le n-2$ further moves). Total $\le 1+(n-2)=n-1$ moves.

#### Boundary $n=2$ ($\theta=90^{\circ}$).
Cut to a largest angle $A\ge 60^{\circ}$. If $A=90^{\circ}$ the triangle already has $\theta$ (win). If $A>90^{\circ}$ then $B+C=180-A<90^{\circ}$, so $B,C<90^{\circ}$. If $A<90^{\circ}$ the triangle is acute, so $B,C<90^{\circ}$. In every non-already-won case $B<90^{\circ}$ and $C<90^{\circ}$, hence $\alpha=90^{\circ}-B$ satisfies $\alpha>0$ (since $B<90$) and $\alpha<A$ (since $\alpha<90-A+B$...: $A>\alpha=90-B\iff A+B>90\iff 180-C>90\iff C<90$, true). With $\beta=B+\alpha=90^{\circ}$, both P-angles are $90^{\circ}=\theta$: both children contain $\theta$, and Mulan wins in one move regardless of the discard.

So for every $n\ge 2$, $\theta=180^{\circ}/n$ lets Mulan force a win in at most $n-1$ moves. ∎ (inclusion)

---

### II. Exclusion: $\theta\ne 180^{\circ}/n$ $\Rightarrow$ Shan-Yu wins

We give **two independent** safe-set constructions. Part A is the distinct geometric framing of this approach (a closed safe set built from the supplementary reflection, not from the taint arithmetic); it covers the clean half-range $\theta\in(90^{\circ},180^{\circ})$. Part B is the shared taint-free casework, which covers all non-divisor $\theta\in(0^{\circ},180^{\circ})$ (in particular the range $\theta\in(0^{\circ},90^{\circ}]$ that Part A does not reach). Together they exclude every non-divisor $\theta$.

Note first that **no** $\theta\in(90^{\circ},180^{\circ})$ is a divisor: $n\ge 2\Rightarrow 180^{\circ}/n\le 90^{\circ}$, so $\theta>90^{\circ}$ is automatically a non-divisor. Thus Part A's range consists entirely of non-divisors.

#### Part A. The obtuse-angle safe set (covers $\theta\in(90^{\circ},180^{\circ})$).

Define
\[
\mathcal S=\{\,\text{nondegenerate triangles }T:\text{ every angle of }T\text{ is }\le 90^{\circ}\,\}.
\`

**(A1) $\mathcal S$ contains the equilateral.** $(60,60,60)\in\mathcal S$.

**(A2) No triangle in $\mathcal S$ has an angle equal to $\theta$.** Every angle of a member of $\mathcal S$ is $\le 90^{\circ}<\theta$ (since $\theta>90^{\circ}$).

**(A3) $\mathcal S$ is closed under the game:** for every $T\in\mathcal S$ and every Mulan cut, at least one child lies in $\mathcal S$.

*Proof of (A3).* Let $T=(A,B,C)\in\mathcal S$, so $A,B,C\le 90^{\circ}$ (and $>0$, sum $180$). Mulan cuts to some vertex; relabel so she cuts to $A$ with $\alpha\in(0,A)$. The children are $C_1=(\alpha,\,B,\,180-\alpha-B)$ and $C_2=(A-\alpha,\,C,\,B+\alpha)$. Write $P_1=180-\alpha-B$ and $P_2=B+\alpha$ for the two fresh P-angles; the **supplementary identity** gives
\[
P_1+P_2=(180-\alpha-B)+(B+\alpha)=180.
\]
The non-P angles are all $\le 90^{\circ}$: in $C_1$, $\alpha<A\le 90^{\circ}$ and $B\le 90^{\circ}$; in $C_2$, $A-\alpha<A\le 90^{\circ}$ and $C\le 90^{\circ}$. Hence the *only* angle in each child that can exceed $90^{\circ}$ is its P-angle. Because $P_1+P_2=180$, at most one of $P_1,P_2$ exceeds $90^{\circ}$ (if both did, their sum would exceed $180$). Concretely:
- If $P_2\le 90^{\circ}$ (equivalently $B+\alpha\le 90^{\circ}$), then $C_2\in\mathcal S$.
- If $P_2>90^{\circ}$, then $P_1=180-P_2<90^{\circ}$, so $C_1\in\mathcal S$.
- If $P_2=90^{\circ}$, then $P_1=90^{\circ}$ and both children lie in $\mathcal S$.

These three sub-cases exhaust $\alpha\in(0,A)$, so in every case at least one child lies in $\mathcal S$. Shan-Yu keeps such a child. ∎

**(A4) Shan-Yu's strategy and termination of Mulan's attempt.** Shan-Yu opens with the equilateral $E\in\mathcal S$. After each Mulan cut, by (A3) at least one child lies in $\mathcal S$; Shan-Yu discards the other and keeps an $\mathcal S$-child. By induction the triangle stays in $\mathcal S$ forever, so by (A2) no angle ever equals $\theta$. Mulan never wins. ∎

*Distinctness note.* Part A uses only the supplementary identity $P_1+P_2=180$ (the reflection $\beta\leftrightarrow 180-\beta$) and the geometric bound $\le 90^{\circ}$; it makes no reference to integer multiples of $\theta$. It is an independent exclusion of the entire half-range $\theta\in(90^{\circ},180^{\circ})$, breaking the shared-wall dependence (the taint casework of Part B) for that range.

*Why the equilateral alone is not closed (honest record of the refuted crux).* The original outline claimed $E=(60,60,60)$ itself is closed under one move for every non-divisor $\theta$. This is **false**: for $\theta=72^{\circ}$, cutting $E$ to a vertex with $\alpha=48^{\circ}$ gives $C_1=(48,60,72)$, which contains $\theta=72^{\circ}$. (Generally, for $\theta\in(60^{\circ},120^{\circ})$, $\alpha=120^{\circ}-\theta\in(0,60^{\circ})$ makes $C_1$'s P-angle $=\theta$.) The fix is exactly Part A: one enlarges the witness from the single point $E$ to the closed set $\mathcal S\supsetneq\{E\}$, and closure is then a genuine property of $\mathcal S$ under the supplementary reflection — not of $E$ alone. The set $\mathcal S$ is strictly smaller than the full taint-free set (it is defined by $\le 90^{\circ}$, not by avoidance of multiples of $\theta$) and is a distinct, genuinely reflection-closed safe set as requested.

#### Part B. The taint-free invariant (covers all non-divisor $\theta\in(0^{\circ},180^{\circ})$).

This is the shared exclusion lemma (KB: *Casework / exhaustion* + *Invariants & monovariants*); we prove it in full. Fix $\theta\in(0,180^{\circ})$ with $\theta\ne 180^{\circ}/n$ for every integer $n\ge 2$ (i.e. $180^{\circ}/\theta\notin\{2,3,4,\dots\}$). Call an angle $x$ **$\theta$-tainted** iff $x=k\theta$ for some integer $k\ge 1$. A triangle is **taint-free** iff none of its angles is tainted.

**(B1) A taint-free initial triangle exists.** The set of tainted angle-values is $\{\theta,2\theta,\dots,\lfloor 180^{\circ}/\theta\rfloor\theta\}$, which is **finite** (at most $\lfloor 180/\theta\rfloor$ values, finite since $\theta>0$). Its complement in the open angle-simplex $\{(A,B,C):A,B,C>0,\,A+B+C=180\}$ is therefore nonempty (indeed dense). Shan-Yu picks any taint-free triangle as the start. (When $60^{\circ}$ is not a multiple of $\theta$, the equilateral serves; otherwise a generic triangle avoids the finite forbidden set.)

**(B2) The taint-free invariant is closed.** Let $T=(A,B,C)$ be taint-free ($A,B,C$ all untainted). Mulan cuts to vertex $A$ with $\alpha\in(0,A)$; the children are $C_1=(\alpha,B,180-\alpha-B)$ and $C_2=(A-\alpha,C,B+\alpha)$. We show **at least one child is taint-free**. Suppose for contradiction that **both** children are tainted. Since $B$ and $C$ are untainted (inherited from the parent), a tainted angle of $C_1$ must be either the $\alpha$-slot $\alpha$ or the P-slot $180-\alpha-B$; a tainted angle of $C_2$ must be either the $\alpha$-slot $A-\alpha$ or the P-slot $B+\alpha$. This gives four disjoint cases (one witness slot per child):

- **(α-slot, α-slot):** $\alpha=k_1\theta$ and $A-\alpha=k_2\theta$. Adding, $A=(k_1+k_2)\theta$, so $A$ is tainted — contradicting the parent's taint-freedom. ✗

- **(α-slot $C_1$, P-slot $C_2$):** $\alpha=k_1\theta$ and $B+\alpha=k_2\theta$. Then $B=(k_2-k_1)\theta$; and $B+\alpha>\alpha$ forces $k_2>k_1$, so $k_2-k_1\ge 1$, making $B$ tainted — contradiction. ✗

- **(P-slot $C_1$, α-slot $C_2$):** $180-\alpha-B=k_1\theta$ (so $\alpha=180-B-k_1\theta$) and $A-\alpha=k_2\theta$. Substituting, $A-(180-B-k_1\theta)=k_2\theta$, i.e. $(A+B-180)=(k_2-k_1)\theta$. Since $A+B=180-C$, this reads $-C=(k_2-k_1)\theta$, i.e. $C=(k_1-k_2)\theta$. From $180-\alpha-B > A-\alpha$ (equivalently $180-B>A$, equivalently $A+B<180$, equivalently $C>0$) we get $k_1\theta>k_2\theta$, so $k_1-k_2\ge 1$ and $C$ is tainted — contradiction. ✗

- **(P-slot, P-slot):** $180-\alpha-B=k_1\theta$ and $B+\alpha=k_2\theta$. Adding eliminates $\alpha$ and $B$:
\[
180=(k_1+k_2)\theta,\qquad\text{i.e.}\quad \theta=\frac{180}{k_1+k_2}.
\]
Here $k_1,k_2\ge 1$, so $k_1+k_2\ge 2$ is an integer — this would make $\theta=180^{\circ}/(k_1+k_2)$ a divisor, contradicting the hypothesis $\theta\ne 180^{\circ}/n$. ✗

All four cases contradict the hypothesis; hence at least one child is taint-free, and Shan-Yu keeps it. The invariant is preserved.

**(B3) Irrational and rational-non-divisor $\theta$.** In case (P-slot, P-slot) the equation $180=(k_1+k_2)\theta$ has no solution with integer $k_1+k_2\ge 2$:
- If $\theta$ is irrational, $180/(k_1+k_2)$ is rational, never equal to the irrational $\theta$. ✗
- If $\theta=180\cdot(p/q)$ in lowest terms with $p>1$ (so $180/\theta=q/p\notin\mathbb N$), the equation becomes $q=(k_1+k_2)p$, forcing $p\mid q$, contradicting $\gcd(p,q)=1$ unless $p=1$; but $p>1$. ✗
So for every non-divisor $\theta\in(0,180^{\circ})$ — rational or irrational — case 4 is impossible.

**(B4) Shan-Yu's strategy.** Start taint-free (B1); after each cut keep a taint-free child (exists by B2–B3). The triangle stays taint-free forever, so in particular no angle ever equals $\theta=\,1\cdot\theta$ (which is tainted). Mulan never wins. ∎

#### Combining Parts A and B.
Part A excludes every $\theta\in(90^{\circ},180^{\circ})$ (all non-divisors, since $180/n\le 90$ for $n\ge 2$). Part B excludes every non-divisor $\theta\in(0^{\circ},180^{\circ})$, which includes the remaining range $\theta\in(0^{\circ},90^{\circ}]$ not reached by Part A, and independently re-confirms the range $(90^{\circ},180^{\circ})$. Hence every $\theta\ne 180^{\circ}/n$ is a Shan-Yu win. ∎ (exclusion)

---

### III. Verification of the answer

We have proved:
- *Inclusion:* $\theta=180^{\circ}/n$ ($n\ge 2$ integer) $\Rightarrow$ Mulan wins (in $\le n-1$ moves, by M1+M2; $n=2$ in one move).
- *Exclusion:* $\theta\ne 180^{\circ}/n$ for every integer $n\ge 2$ $\Rightarrow$ Shan-Yu wins (Part A for $\theta\in(90^{\circ},180^{\circ})$; Part B for all non-divisor $\theta\in(0^{\circ},180^{\circ})$).

The two directions are exhaustive and complementary, so the characterization is
\[
\boxed{\text{Mulan can guarantee victory in finitely many steps}\iff \theta=\frac{180^{\circ}}{n}\text{ for some integer }n\ge 2.}
\]

*Direct check of the boundary.* $\theta=90^{\circ}=180/2$: inclusion gives a one-move win (both P-angles $=90^{\circ}$); exclusion does not apply (it is a divisor). $\theta=60^{\circ}=180/3$: inclusion gives $\le 2$ moves (align to $120^{\circ}=2\theta$, then reduce). $\theta=72^{\circ}$ (non-divisor, $180/72=2.5\notin\mathbb N$): excluded by Part B (and is in the range where the equilateral alone is not closed, $72\in(60,90)$, handled by the taint casework). $\theta=120^{\circ}$ ($180/120=1.5\notin\mathbb N$, and $120>90$): excluded by Part A (and also by Part B). All consistent. ∎
