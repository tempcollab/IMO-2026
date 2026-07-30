time 13m 19s

# IMO 2026 Problem 3: Mark-and-Claim Stick Game

## Problem

Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of
length $1$. First Liu Bang marks at most $n$ points on the stick, and
then Xiang Yu marks at most $n$ further points; all marked points are
distinct. The stick is cut at every marked point. The players then
alternately claim unclaimed pieces, with Liu Bang moving first, and
each player seeks to maximize the total length of the pieces he
claims. Determine the largest number $c$ that Liu Bang can guarantee,
regardless of Xiang Yu's play.

## Solution

**Theorem.**
For every positive integer $n$, the required value is
$$
\boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
$$

We begin with three lemmas.

**Lemma (Value of the claiming phase).**
Suppose the final piece lengths, in nonincreasing order, are
$$
x_1\ge x_2\ge \dots \ge x_m>0.
$$
Then the value of the claiming phase for the first player is
$$
x_1+x_3+x_5+\cdots.
$$
Equivalently, if
$$
\operatorname{Alt}(x_1,\dots,x_m)
  :=x_1-x_2+x_3-x_4+\cdots,
$$
then the first player receives, under optimal play,
$$
\frac{1+\operatorname{Alt}(x_1,\dots,x_m)}{2}.
$$

*Proof.*
If the first player always takes a largest remaining piece, then just
before his $j$th move at most $2j-2$ pieces have been removed. Hence
at least one of the original $2j-1$ largest pieces remains, so the
piece he takes on that move has length at least $x_{2j-1}$. Thus he
can guarantee
$$
x_1+x_3+x_5+\cdots.
$$

Conversely, suppose the second player always takes a largest remaining
piece. Just before his $j$th move, exactly $2j-1$ pieces have been
removed, so at least one of the original $2j$ largest pieces remains.
He therefore takes a piece of length at least $x_{2j}$. Hence the
second player can guarantee at least
$$
x_2+x_4+x_6+\cdots,
$$
leaving the first player at most the complementary sum
$x_1+x_3+x_5+\cdots$. This proves the first assertion. Since the total
length is $1$, the second formula follows.
∎

**Lemma (Cancellation of equal pairs).**
Suppose a multiset of positive numbers consists of some equal pairs,
together with a residual multiset of total sum $d$. If all the numbers
are arranged in nonincreasing order, then their alternating sum is at
most $d$.

*Proof.*
In a nonincreasing list, equal entries occur consecutively. Deleting
two adjacent equal entries does not change the alternating sum: their
contributions cancel, and every later index shifts by $2$, preserving
its parity. Deleting all prescribed equal pairs therefore leaves the
alternating sum of the residual entries alone. For a nonincreasing
residual list $z_1\ge\cdots\ge z_s>0$, this alternating sum is
$$
(z_1-z_2)+(z_3-z_4)+\cdots,
$$
with an additional final term $z_s$ when $s$ is odd. It is
nonnegative and no larger than $z_1+\cdots+z_s=d$.
∎

**Lemma (Matching two families of intervals).**
Let one family consist of $p$ intervals of total length $A$, and a
second nonempty family consist of $q$ intervals of total length $B$,
where $A\ge B$. Using at most $p+q-1$ cuts in these intervals, one can
subdivide them so that every fragment from the second family is
matched by an equal-length fragment from the first family, while the
unmatched fragments from the first family have total length $A-B$.

*Proof.*
Order the intervals arbitrarily within each family and concatenate
them conceptually, obtaining intervals $[0,A]$ and $[0,B]$. On the
common portion $[0,B]$, refine both concatenation partitions by taking
the union of their boundary points. The resulting subinterval lengths
on $[0,B]$ are identical for the two families.

To realize this common refinement in the original intervals, on the
first side it is enough to insert the $q-1$ internal boundaries of the
second concatenation and, if necessary, the point $B$. This uses at
most $q$ cuts. On the second side, it is enough to insert those
internal boundaries of the first concatenation that lie in $(0,B)$,
using at most $p-1$ cuts. Thus at most $p+q-1$ cuts are needed. The
part of the first concatenation lying beyond $B$ has total length
$A-B$ and is precisely the unmatched part.
∎

*Proof.*[Proof of the theorem]
Set
$$
u:=\frac{1}{2^{n+1}-1}.
$$
We prove matching upper and lower bounds.

### Upper bound
We show that, after any choice by Liu Bang, Xiang Yu can arrange that
<a id="eq:p3-upper-alt"></a>
$$
\operatorname{Alt}(x_1,\dots,x_m)\le u.
$$
By the first lemma, this will hold Liu Bang to at most
<a id="eq:p3-upper-value"></a>
$$
\frac{1+u}{2}
  =\frac{2^n}{2^{n+1}-1}.
$$

Suppose first that Liu Bang uses $r<n$ marks, producing $r+1\le n$
pieces. Xiang Yu bisects each of these pieces. Every final length then
occurs in an equal pair, so the second lemma gives
$\operatorname{Alt}(x_1,\dots,x_m)=0$. Thus it remains only to consider the case in
which Liu Bang uses exactly $n$ marks and creates $n+1$ initial pieces.
Let their lengths be
$$
a_1,a_2,\dots,a_{n+1}.
$$

Consider the $2^{n+1}$ subset sums
$$
s(S):=\sum_{i\in S}a_i,
  \qquad S\subseteq\{1,2,\dots,n+1\}.
$$
They all lie in $[0,1]$, and the smallest and largest are $0$ and $1$.
When these subset sums are listed in nondecreasing order, the
$2^{n+1}-1$ consecutive gaps have total sum $1$. Hence two distinct
subsets $S,T$ satisfy
<a id="eq:p3-subset-gap"></a>
$$
|s(S)-s(T)|\le \frac{1}{2^{n+1}-1}=u.
$$
Delete the common indices and put
$$
P:=S\setminus T,
  \qquad
  Q:=T\setminus S.
$$
After interchanging $P$ and $Q$ if necessary, we may assume
$$
\sum_{i\in P}a_i\ge \sum_{i\in Q}a_i.
$$
Define
$$
d:=\sum_{i\in P}a_i-\sum_{i\in Q}a_i.
$$
Then $P$ and $Q$ are disjoint, not both empty, and by [the displayed equation](#eq:p3-subset-gap),
<a id="eq:p3-residual-bound"></a>
$$
0\le d\le u.
$$
Let
$$
R:=\{1,2,\dots,n+1\}\setminus(P\cup Q).
$$

If $Q$ is nonempty, apply the matching lemma to the pieces indexed by
$P$ and $Q$. It uses at most $|P|+|Q|-1$ cuts and produces equal pairs
of fragments, except for unmatched fragments on the $P$-side whose
total length is $d$. Xiang Yu also bisects every piece indexed by $R$,
using $|R|$ additional cuts. The total number of cuts is at most
$$
|P|+|Q|-1+|R|=n.
$$

If $Q$ is empty, Xiang Yu simply leaves the pieces indexed by $P$
unmatched and bisects every piece indexed by $R$. Since $P$ is
nonempty, this uses
$$
|R|=n+1-|P|\le n
$$
cuts, and the total length of the unmatched pieces is again $d$.

In either case, all final pieces except for a residual collection of
total length $d$ occur in equal pairs. The cancellation lemma and [the displayed equation](#eq:p3-residual-bound)
therefore give
$$
\operatorname{Alt}(x_1,\dots,x_m)\le d\le u,
$$
which proves [the displayed equation](#eq:p3-upper-alt) and hence the desired upper bound.

### Lower bound
Liu Bang marks the points
<a id="eq:p3-marks"></a>
$$
(2^k-1)u,
  \qquad k=1,2,\dots,n.
$$
The resulting $n+1$ initial pieces have lengths
<a id="eq:p3-initial-lengths"></a>
$$
u,2u,4u,\dots,2^n u,
$$
whose sum is
$$
(1+2+\cdots+2^n)u=(2^{n+1}-1)u=1.
$$
We show that, whatever cuts Xiang Yu makes, the final alternating sum
satisfies
<a id="eq:p3-lower-alt"></a>
$$
\operatorname{Alt}(x_1,\dots,x_m)\ge u.
$$

Let Xiang Yu introduce $k\le n$ cuts. There are then
$$
m=n+1+k\le 2n+1
$$
final pieces. Arrange their lengths in nonincreasing order,
$$
x_1\ge x_2\ge\cdots\ge x_m>0,
$$
breaking ties arbitrarily, and pair them as
$$
(x_1,x_2),\ (x_3,x_4),\ \dots.
$$
If $m$ is odd, leave $x_m$ unpaired. Thus
<a id="eq:p3-alt-pairs"></a>
$$
\operatorname{Alt}(x_1,\dots,x_m)
  =\sum_j (x_{2j-1}-x_{2j})
   +\begin{cases}
      x_m,&m\text{ odd},\\
      0,&m\text{ even}.
\end{cases}
$$

Construct a multigraph $G$ with one vertex for each of the $n+1$
initial pieces in [the displayed equation](#eq:p3-initial-lengths). Every final fragment lies in a unique initial
piece. For each paired pair of final fragments, draw an edge between
the two vertices corresponding to their initial pieces; a pair whose
fragments come from the same initial piece produces a loop. Parallel
edges are allowed. If $m$ is odd, also remember the vertex containing
the unpaired fragment $x_m$.

The graph has $n+1$ vertices and
$$
\left\lfloor\frac{m}{2}\right\rfloor\le n
$$
edges. Hence at least one connected component of $G$ is a tree. Indeed,
a connected multigraph that is not a tree has at least as many edges
as vertices, so if no component were a tree, the whole graph would
have at least $n+1$ edges.

Choose a tree component $C$. Since $C$ is bipartite, assign signs
$\varepsilon_v\in\{+1,-1\}$ to its vertices so that adjacent vertices
have opposite signs. Let $a_v$ denote the length of the initial piece
corresponding to $v$.

Every paired fragment arising from a vertex of $C$ is paired with a
fragment from another vertex of $C$, because $C$ is a connected
component. For an edge $e=vw$ of $C$, let $\lambda_{e,v}$ and
$\lambda_{e,w}$ be the lengths of its two endpoint fragments. Since
$\varepsilon_w=-\varepsilon_v$, the contribution of these two
fragments to the signed sum is
$$
\varepsilon_v\lambda_{e,v}
  +\varepsilon_w\lambda_{e,w}
  =\varepsilon_v(\lambda_{e,v}-\lambda_{e,w}).
$$
Its absolute value is exactly the difference between the two lengths
in the corresponding ranked pair. If the unpaired fragment $x_m$
comes from a vertex of $C$, it contributes $\pm x_m$. Summing over the
component and applying the triangle inequality to [the displayed equation](#eq:p3-alt-pairs), we obtain
<a id="eq:p3-signed-bound"></a>
$$
\left|\sum_{v\in C}\varepsilon_v a_v\right|
  \le \operatorname{Alt}(x_1,\dots,x_m).
$$

The numbers $a_v$ are distinct members of
$$
u,2u,4u,\dots,2^n u.
$$
Let $2^J u$ be the largest one represented in $C$. Its absolute
contribution to the signed sum in [the displayed equation](#eq:p3-signed-bound) is $2^J u$, whereas the sum of
all possible smaller contributions is at most
$$
(1+2+\cdots+2^{J-1})u=(2^J-1)u.
$$
Consequently,
<a id="eq:p3-signed-lower"></a>
$$
\left|\sum_{v\in C}\varepsilon_v a_v\right|
  \ge 2^J u-(2^J-1)u=u.
$$
Combining [the displayed equation](#eq:p3-signed-bound) and [the displayed equation](#eq:p3-signed-lower) proves [the displayed equation](#eq:p3-lower-alt).

By the claiming-phase lemma, Liu Bang can therefore guarantee at least
$$
\frac{1+u}{2}
  =\frac{2^n}{2^{n+1}-1}.
$$
Together with the upper bound, this completes the proof.
∎
