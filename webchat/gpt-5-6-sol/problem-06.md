time 15m 10s

# IMO 2026 Problem 6: Eventual Translation of a Greedy Sequence

## Problem

Let $a_1,a_2,a_3,\ldots$ be an infinite sequence of positive integers greater than $1$.
Suppose that, for every positive integer $n$, the number $a_{n+1}$ is the smallest
integer greater than $a_n$ such that
$$
\gcd(a_{n+1},a_i)>1
\qquad (1\le i\le n).
$$
Prove that there exist positive integers $T$ and $L$ such that
$$
a_{n+T}=a_n+L
$$
for every positive integer $n$.

## Solution

*Proof.*
Define
$$
\mathcal{S}
:=
\bigl\{x\in\mathbb{Z}_{>0} : \gcd(x,a_i)>1\text{ for every }i\ge 1\bigr\}.
$$
We shall prove that $\mathcal{S}$ is periodic and that the sequence
$a_1,a_2,\ldots$ lists, in increasing order, precisely the elements of $\mathcal{S}$
that are at least $a_1$.

First observe that any two terms of the sequence have greatest common divisor
larger than $1$: when the later term was chosen, it was required to have this
property with every earlier term. Hence $a_n\in\mathcal{S}$ for every $n$.

Because the sequence is strictly increasing, it is unbounded. We claim that
<a id="eq:p6-enumeration"></a>
$$
\{a_1,a_2,\ldots\}
=
\mathcal{S}\cap [a_1,\infty).
$$
The inclusion from left to right was just proved. Conversely, suppose that
$x\in\mathcal{S}$, $x\ge a_1$, and $x$ is not a term of the sequence. Since $a_1$
is a term, we have $x>a_1$; by unboundedness there is an $n$ for which
$$
a_n<x<a_{n+1}.
$$
The definition of $\mathcal{S}$ gives $\gcd(x,a_i)>1$ for $1\le i\le n$, so $x$
was an admissible candidate for $a_{n+1}$. The minimality of $a_{n+1}$ would
then imply $a_{n+1}\le x$, a contradiction. Thus [the displayed equation](#eq:p6-enumeration) holds.

The set $\mathcal{S}$ is upward closed under divisibility: if $x\in\mathcal{S}$ and
$x\mid y$, then $y\in\mathcal{S}$. In particular, if
$$
\operatorname{rad}(x):=\prod_{p\mid x}p
$$
denotes the squarefree kernel of $x$, then
<a id="eq:p6-radical"></a>
$$
x\in\mathcal{S}
\quad\Longleftrightarrow\quad
\operatorname{rad}(x)\in\mathcal{S}.
$$
Indeed, $\operatorname{rad}(x)\mid x$, and $x$ and $\operatorname{rad}(x)$ have exactly the same prime
divisors.

We next record two consequences of the definition of $\mathcal{S}$ and of the
greedy rule.

**Lemma.**
Any two elements of $\mathcal{S}$ have a nontrivial common divisor. In other words,
$$
x,y\in\mathcal{S} \quad\Longrightarrow\quad \gcd(x,y)>1.
$$

*Proof.*
Suppose, to the contrary, that $x,y\in\mathcal{S}$ and $\gcd(x,y)=1$. Choose a
positive integer $k$ such that $k\equiv 1\pmod y$ and $kx\ge a_1$. Because
$\mathcal{S}$ is closed under taking multiples, $kx\in\mathcal{S}$. By [the displayed equation](#eq:p6-enumeration), $kx$ is a
term of the sequence. Since $y\in\mathcal{S}$, it must therefore satisfy
$\gcd(y,kx)>1$. But $\gcd(y,k)=\gcd(y,x)=1$, so $\gcd(y,kx)=1$, a
contradiction.
∎

**Lemma.**
If $x>a_1$ and $x\notin\mathcal{S}$, then there exists a term $a_i<x$ such that
$$
\gcd(x,a_i)=1.
$$

*Proof.*
Since $x\notin\mathcal{S}$, the number $x$ is not a term of the sequence. Thus, by
unboundedness, there is an $n$ such that
$$
a_n<x<a_{n+1}.
$$
If $\gcd(x,a_i)>1$ held for every $1\le i\le n$, then $x$ would be an
admissible candidate for $a_{n+1}$, contradicting the minimality of
$a_{n+1}$. Hence $\gcd(x,a_i)=1$ for at least one $i\le n$, and then
$a_i\le a_n<x$.
∎

Let $\mathcal{M}$ be the set of squarefree elements of $\mathcal{S}$ that are minimal
under divisibility. Explicitly,
$$
m\in\mathcal{M}
\quad\Longleftrightarrow\quad
\begin{cases}
        m\in\mathcal{S},\quad m\text{ is squarefree},\\
        d\notin\mathcal{S}\text{ for every proper divisor }d\mid m.
\end{cases}
$$
The set $\mathcal{M}$ is nonempty: by [the displayed equation](#eq:p6-radical), $\operatorname{rad}(a_1)\in\mathcal{S}$, and among the
finitely many divisors of $\operatorname{rad}(a_1)$ that lie in $\mathcal{S}$ one may choose a
minimal one.

Moreover, every $x\in\mathcal{S}$ is divisible by some member of $\mathcal{M}$. Indeed,
by [the displayed equation](#eq:p6-radical) the number $\operatorname{rad}(x)$ lies in $\mathcal{S}$; among its divisors belonging to
$\mathcal{S}$, choose one minimal under divisibility. It is squarefree and hence is
an element of $\mathcal{M}$. Consequently,
<a id="eq:p6-union"></a>
$$
\mathcal{S}=\bigcup_{m\in\mathcal{M}}m\mathbb{Z}_{>0}.
$$

We now prove that only finitely many primes occur in the members of $\mathcal{M}$.
Set $A:=a_1$.

**Lemma (Descent lemma).**
Let $m\in\mathcal{M}$, and let $q$ be a prime divisor of $m$. Then there is an
$m'\in\mathcal{M}$ such that
$$
q\mid m'
\qquad\text{and}\qquad
\frac{m'}{q}\le A.
$$

*Proof.*
Start with $m_0:=m$. Suppose that $m_j\in\mathcal{M}$, that $q\mid m_j$, and that
$m_j/q>A$. Since $m_j$ is minimal in $\mathcal{S}$, its proper divisor
$$
x:=\frac{m_j}{q}
$$
does not belong to $\mathcal{S}$. The preceding lemma therefore gives a term
$a_i<x$ such that $\gcd(a_i,x)=1$.

By [the displayed equation](#eq:p6-radical), $\operatorname{rad}(a_i)\in\mathcal{S}$. Choose $m_{j+1}\in\mathcal{M}$ dividing
$\operatorname{rad}(a_i)$. Then
<a id="eq:p6-descent"></a>
$$
m_{j+1}
\le \operatorname{rad}(a_i)
\le a_i
<x
=\frac{m_j}{q}
<m_j,
$$
and, because $m_{j+1}\mid\operatorname{rad}(a_i)$, we also have
$\gcd(m_{j+1},x)=1$.

Both $m_j$ and $m_{j+1}$ lie in $\mathcal{S}$, so the first lemma yields
$\gcd(m_j,m_{j+1})>1$. Now $m_j$ is squarefree and $m_j=qx$, while
$m_{j+1}$ is coprime to $x$. It follows that the only possible common prime
divisor is $q$. Hence $q\mid m_{j+1}$.

Thus, whenever $m_j/q>A$, we can replace $m_j$ by a strictly smaller element
$m_{j+1}\in\mathcal{M}$ that is still divisible by $q$. This descent cannot
continue indefinitely. At its terminal stage we obtain an $m'\in\mathcal{M}$ with
$q\mid m'$ and $m'/q\le A$, as required.
∎

Let $P$ be the set of primes that divide at least one member of $\mathcal{M}$.
Suppose for contradiction that $P$ is infinite. For each $q\in P$, the
descent lemma supplies an element
$$
m_q=q c_q\in\mathcal{M}
\qquad\text{with}\qquad
1\le c_q\le A.

$$
Because $c_q$ is a proper divisor of the minimal element $m_q\in\mathcal{M}$, we
have $c_q\notin\mathcal{S}$.

There are only finitely many possible values of $c_q$. Hence there is a fixed
integer $c\in\{1,2,\ldots,A\}$ such that
<a id="eq:p6-fixed-cofactor"></a>
$$
qc\in\mathcal{M}
$$
for infinitely many distinct primes $q$. For this $c$ we have
$c\notin\mathcal{S}$, so by the definition of $\mathcal{S}$ there is some term $a_j$
with
$$
\gcd(c,a_j)=1.
$$
For each prime $q$ satisfying [the displayed equation](#eq:p6-fixed-cofactor), both $a_j$ and $qc$ belong to $\mathcal{S}$.
The first lemma therefore gives
$$
\gcd(a_j,qc)>1.
$$
Since $a_j$ is coprime to $c$, this forces $q\mid a_j$. Thus the fixed
positive integer $a_j$ is divisible by infinitely many distinct primes, an
impossibility. We conclude that $P$ is finite.

Every member of $\mathcal{M}$ is squarefree and all of its prime divisors lie in
the finite set $P$. Hence $\mathcal{M}$ itself is finite. Define
$$
L:=\prod_{p\in P}p.
$$
Every $m\in\mathcal{M}$ divides $L$. Using [the displayed equation](#eq:p6-union), we therefore obtain, for every
$x\in\mathbb{Z}_{>0}$,
$$
\begin{aligned}
x\in\mathcal{S}
&\Longleftrightarrow
      m\mid x\text{ for some }m\in\mathcal{M}\\
&\Longleftrightarrow
      m\mid x+L\text{ for some }m\in\mathcal{M}\\
&\Longleftrightarrow
      x+L\in\mathcal{S}.
\end{aligned}
$$
Thus membership in $\mathcal{S}$ is periodic with period $L$.

Let
$$
T:=\bigl|\mathcal{S}\cap\{1,2,\ldots,L\}\bigr|.
$$
This number is positive: $\mathcal{M}$ is nonempty, every $m\in\mathcal{M}$ divides
$L$, and $\mathcal{S}$ is closed under taking multiples, so $L\in\mathcal{S}$.
Periodicity implies that every interval of $L$ consecutive integers contains
exactly $T$ elements of $\mathcal{S}$. In particular, the interval
$$
(a_n,a_n+L]
$$
contains exactly $T$ elements of $\mathcal{S}$, and its right endpoint belongs to
$\mathcal{S}$ because $a_n\in\mathcal{S}$.

By [the displayed equation](#eq:p6-enumeration), the sequence lists the elements of $\mathcal{S}\cap[a_1,\infty)$ in
strictly increasing order. Hence the $T$-th term after $a_n$ is exactly the
last element of $\mathcal{S}$ in $(a_n,a_n+L]$, namely $a_n+L$. Therefore
$$
\boxed{a_{n+T}=a_n+L}
$$
for every positive integer $n$.
∎
