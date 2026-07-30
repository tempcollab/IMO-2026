time 5m 22s

# IMO 2026 Problem 4: Triangle-Cutting Angle Game

## Problem

Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal{T}$ with measurements of his choice. Then, they repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its three vertices. She then makes a straight cut from $P$ to the opposite vertex of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

## Solution

Let
$$
\Omega=180^\circ.
$$
We determine exactly for which values of $\theta\in(0^\circ,180^\circ)$
Mulan can force the game to end after finitely many cuts.

**Theorem.**
Mulan can guarantee victory if and only if
$$
\boxed{\theta=\frac{180^\circ}{n}}
$$
for some integer $n\ge 2$.

*Proof.*
We prove the two directions separately.

### A preliminary claim

**Claim.**
Suppose the current triangle contains an angle equal to $m\theta$,
where $m$ is a positive integer. Then Mulan can force a win in at
most $m-1$ further cuts.

*Proof.*
We use induction on $m$. If $m=1$, the triangle already has an
angle equal to $\theta$, so the game has ended and Mulan has won.

Now let $m\ge 2$, and suppose one angle of the current triangle is
$m\theta$. From the vertex of that angle, Mulan draws an interior ray
that makes an angle $\theta$ with one of the two adjacent sides. The
ray meets the opposite side at an interior point and splits the angle
$m\theta$ into
$$
\theta
\qquad\text{and}\qquad
(m-1)\theta.
$$
Thus one of the two resulting triangles has an angle $\theta$, while
the other has an angle $(m-1)\theta$. If Shan-Yu keeps the first
triangle, Mulan wins immediately. If he keeps the second, the induction
hypothesis applies. Hence Mulan wins after at most $m-1$ cuts.
∎

### Sufficiency

Assume that
$$
\theta=\frac{\Omega}{n}
$$
for some integer $n\ge 2$. Consider any current triangle, and write
its three angles as
$$
a\theta,\qquad b\theta,\qquad c\theta,
$$
where
$$
a,b,c>0
\qquad\text{and}\qquad
a+b+c=n.
$$
If one of $a,b,c$ is an integer, then the preliminary claim already
shows that Mulan can force a win. It remains to consider the case in
which none of $a,b,c$ is an integer.

We use the following elementary lemma.

**Lemma.**
Let $a,b,c>0$ be nonintegers whose sum is an integer $n\ge 2$.
After relabeling $a,b,c$, there is an integer $k$ such that
$$
b<k<a+b.
$$

*Proof.*
First suppose that one of the three numbers is greater than $1$.
Call that number $a$, choose either of the remaining numbers as
$b$, and set
$$
k=\lceil b\rceil.
$$
Because $b$ is not an integer,
$$
0<k-b<1<a,
$$
so indeed $b<k<a+b$.

Now suppose that all three numbers are less than $1$. Their sum is
an integer at least $2$ and strictly less than $3$, so their sum is
exactly $2$. Let $a$ and $b$ be the two largest of the three
numbers, and let the remaining number be $c$. Then
$$
b<1
\qquad\text{and}\qquad
a+b=2-c>1.
$$
Thus $b<1<a+b$, and we may take $k=1$.
∎

Label the vertices of the current triangle as $A,B,C$ so that
$$
\angle A=a\theta,
\qquad
\angle B=b\theta,
\qquad
\angle C=c\theta,
$$
and choose an integer $k$ satisfying
$$
b<k<a+b.
$$
From $A$, Mulan draws the interior ray meeting $BC$ at $P$ and
satisfying
$$
\angle BAP=(k-b)\theta.
$$
This is a legal cut because
$$
0<k-b<a.
$$

In triangle $ABP$, the angles at $A$ and $B$ have sum
$$
(k-b)\theta+b\theta=k\theta.
$$
Therefore
$$
\angle APB
 =\Omega-k\theta
 =(n-k)\theta.
$$
Since $B,P,C$ are collinear, the two angles at $P$ are
supplementary, and hence
$$
\angle APC
 =\Omega-(n-k)\theta
 =k\theta.
$$
Thus triangle $ABP$ contains the positive integral multiple
$(n-k)\theta$, while triangle $ACP$ contains the positive integral
multiple $k\theta$. Notice that
$$
0<b<k<a+b=n-c<n,
$$
so $1\le k\le n-1$, and both multiples are positive.

Whichever triangle Shan-Yu keeps, the preliminary claim applies.
Therefore Mulan can force a win in finitely many cuts. In fact, the
argument gives a uniform bound of at most $n-1$ cuts.

### Necessity

Now suppose that
$$
\frac{\Omega}{\theta}\notin\mathbb{Z}.
$$
Define the additive subgroup
$$
H=\{m\theta:m\in\mathbb{Z}\}
$$
of the real numbers. The assumption says precisely that
$$
\Omega\notin H.
$$

Shan-Yu begins with an equilateral triangle. Each of its angles is
$\Omega/3$, and $\Omega/3\notin H$: otherwise $\Omega/3=m\theta$ for some
integer $m$, which would imply $\Omega=3m\theta\in H$, a contradiction.

Shan-Yu will maintain the following invariant:
$$
\text{none of the three angles of the current triangle belongs to }H.
$$
Suppose the current triangle is $ABC$, with
$$
\angle A=a,
\qquad
\angle B=b,
\qquad
\angle C=c,
$$
and suppose $a,b,c\notin H$. Mulan chooses a point $P$ in the
interior of $BC$ and cuts along $AP$. Put
$$
x=\angle BAP,
$$
so that $0<x<a$. The two resulting triangles have angle triples
$$
ABP:\qquad x,\ b,\ \Omega-b-x,
$$
and
$$
ACP:\qquad a-x,\ c,\ b+x.
$$

We claim that at least one of these two triangles has no angle in
$H$. Suppose, to the contrary, that each resulting triangle has an
angle in $H$. Since $b,c\notin H$, one of
$$
x,
\qquad
\Omega-b-x
$$
must belong to $H$, and one of
$$
a-x,
\qquad
b+x
$$
must belong to $H$. There are four possible pairings:
$$
\begin{aligned}
x,\ a-x\in H
&\implies a=x+(a-x)\in H,\\
x,\ b+x\in H
&\implies b=(b+x)-x\in H,\\
\Omega-b-x,\ a-x\in H
&\implies c=(\Omega-b-x)-(a-x)\in H,\\
\Omega-b-x,\ b+x\in H
&\implies \Omega=(\Omega-b-x)+(b+x)\in H.
\end{aligned}
$$
Each conclusion is impossible. Therefore at least one of the two
resulting triangles has all three of its angles outside $H$.
Shan-Yu keeps such a triangle, preserving the invariant.

By repeating this strategy after every cut, Shan-Yu can ensure forever
that no angle of the current triangle lies in $H$. Since
$\theta\in H$, the current triangle never has an angle equal to
$\theta$. Thus Mulan cannot guarantee victory.

Combining the two directions, Mulan has a finite winning strategy
exactly for
$$
\boxed{
\theta\in
\left\{\frac{180^\circ}{n}:n=2,3,4,\ldots\right\}.
}
$$
∎
