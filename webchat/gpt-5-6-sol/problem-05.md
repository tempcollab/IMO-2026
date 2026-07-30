time 2m 36s

# IMO 2026 Problem 5: Double-Inequality Functional Equation

## Problem

Determine all functions $f\colon \mathbb{R}_{>0}\to\mathbb{R}_{>0}$ such that
$$
\sqrt{\frac{x^2+f(y)^2}{2}}
\geq \frac{f(x)+y}{2}
\geq \sqrt{x f(y)}
$$
for every $x,y\in\mathbb{R}_{>0}$.

## Solution

**Theorem.**
The functions satisfying the inequality are exactly
$$
\boxed{f(x)=x+c\qquad(x>0),}
$$
where $c\geq 0$ is an arbitrary constant.

*Proof.*
For $n\geq 0$, let $f^{\circ n}$ denote the $n$-fold iterate of $f$, with
$f^{\circ 0}$ equal to the identity map. Define
$$
d(x):=f(x)-x \qquad (x>0).
$$

### 1. A basic identity and nonnegativity of $d$

Set $x=f(y)$ in the given double inequality. Since $f(y)>0$, both outer
terms are equal to $f(y)$:
$$
\sqrt{\frac{f(y)^2+f(y)^2}{2}}=f(y),
\qquad
\sqrt{f(y)f(y)}=f(y).
$$
Consequently the middle term is also equal to $f(y)$, and hence
$$
\frac{f(f(y))+y}{2}=f(y).
$$
Thus
<a id="eq:p5-iterate-identity"></a>
$$
f(f(y))=2f(y)-y.
$$
In terms of $d$, this gives
<a id="eq:p5-d-invariant"></a>
$$
d(f(y))=f(f(y))-f(y)=f(y)-y=d(y).
$$

We claim that for every $y>0$ and every integer $n\geq 0$,
<a id="eq:p5-iterates"></a>
$$
f^{\circ n}(y)=y+n d(y).
$$
Indeed, the assertion is clear for $n=0$. If it holds for some $n$, then
[the displayed equation](#eq:p5-d-invariant) implies
$$
d\bigl(f^{\circ n}(y)\bigr)=d(y),
$$
and therefore
$$
f^{\circ(n+1)}(y)
 =f^{\circ n}(y)+d\bigl(f^{\circ n}(y)\bigr)
 =y+(n+1)d(y).
$$
This proves [the displayed equation](#eq:p5-iterates) by induction.

Every iterate $f^{\circ n}(y)$ lies in $\mathbb{R}_{>0}$. If $d(y)<0$, then the
right-hand side of [the displayed equation](#eq:p5-iterates) is nonpositive for all sufficiently large $n$, a
contradiction. Hence
<a id="eq:p5-d-nonnegative"></a>
$$
d(y)\geq 0 \qquad\text{for every }y>0.
$$

### 2. Any two positive values of $d$ are equal

The first half of the given inequality is equivalent to
$$
f(x)+y\leq \sqrt{2\bigl(x^2+f(y)^2\bigr)}.
$$
Since
$$
f(x)+y=x+f(y)+d(x)-d(y),
$$
we obtain
<a id="eq:p5-phi-bound"></a>
$$
d(x)-d(y)\leq \Phi\bigl(x,f(y)\bigr),
$$
where, for $r,s>0$, we set
$$
\Phi(r,s):=\sqrt{2(r^2+s^2)}-r-s.
$$
Rationalizing gives the useful identity
<a id="eq:p5-phi-identity"></a>
$$
\Phi(r,s)
 =\frac{(r-s)^2}{\sqrt{2(r^2+s^2)}+r+s}.
$$

Suppose that $d(u)=a>0$ and $d(v)=b>0$. By [the displayed equation](#eq:p5-d-invariant) and [the displayed equation](#eq:p5-iterates), the points
$$
u_n:=f^{\circ n}(u)=u+na,
 \qquad
 v_m:=f^{\circ m}(v)=v+mb
$$
satisfy
$$
d(u_n)=a,
 \qquad
 d(v_m)=b
$$
for all $m,n\geq 0$.

For every sufficiently large $n$, define
$$
m_n:=\left\lfloor\frac{u_n-v-b}{b}\right\rfloor.
$$
Then $m_n\geq 0$ and
<a id="eq:p5-close-iterates"></a>
$$
0\leq u_n-\bigl(v+(m_n+1)b\bigr)<b.
$$
Because $f(v_{m_n})=v+(m_n+1)b$, applying [the displayed equation](#eq:p5-phi-bound) with
$x=u_n$ and $y=v_{m_n}$ yields
$$
a-b\leq \Phi\bigl(u_n,f(v_{m_n})\bigr).
$$
Using [the displayed equation](#eq:p5-phi-identity) and [the displayed equation](#eq:p5-close-iterates), we find
$$
0\leq \Phi\bigl(u_n,f(v_{m_n})\bigr)
 <\frac{b^2}{u_n+f(v_{m_n})}.
$$
Moreover, [the displayed equation](#eq:p5-close-iterates) implies $f(v_{m_n})>u_n-b$, so the denominator tends to
infinity as $n\to\infty$. Therefore
$$
\Phi\bigl(u_n,f(v_{m_n})\bigr)\longrightarrow 0,
$$
and consequently $a-b\leq 0$. Interchanging $u$ and $v$ gives
$b-a\leq 0$, so $a=b$.

It follows that either $d$ is identically zero, or there exists a fixed
constant $c>0$ such that
<a id="eq:p5-two-values"></a>
$$
d(x)\in\{0,c\}
 \qquad\text{for every }x>0.
$$

### 3. The values $0$ and $c$ cannot both occur

Assume now that $c>0$ occurs, and define
$$
Z:=\{x>0:d(x)=0\},
 \qquad
 P:=\{x>0:d(x)=c\}.
$$
By [the displayed equation](#eq:p5-two-values), the sets $Z$ and $P$ form a partition of $\mathbb{R}_{>0}$. We show that
both are open in $\mathbb{R}_{>0}$.

First let $z\in Z$. Then $f(z)=z$. Applying the first half of the given
inequality with $y=z$ gives
$$
f(x)+z\leq \sqrt{2(x^2+z^2)},
$$
and hence
<a id="eq:p5-zero-neighborhood"></a>
$$
d(x)\leq \sqrt{2(x^2+z^2)}-x-z.
$$
The right-hand side of [the displayed equation](#eq:p5-zero-neighborhood) is a continuous function of $x$ and is equal
to $0$ at $x=z$. Thus it is strictly smaller than $c$ whenever $x$ is
sufficiently close to $z$. Since $d(x)\in\{0,c\}$, equation [the displayed equation](#eq:p5-zero-neighborhood) then
forces $d(x)=0$. Hence $Z$ is open.

Next let $p\in P$, so $f(p)=p+c$. If $x\in Z$, then $f(x)=x$, and the
second half of the given inequality, with $y=p$, would imply
<a id="eq:p5-positive-neighborhood"></a>
$$
\frac{x+p}{2}\geq \sqrt{x(p+c)}.
$$
At $x=p$, however, [the displayed equation](#eq:p5-positive-neighborhood) is false, because
$$
p<\sqrt{p(p+c)}.
$$
By continuity, [the displayed equation](#eq:p5-positive-neighborhood) remains false for every $x$ in some neighborhood of
$p$. No point of that neighborhood can therefore belong to $Z$. By [the displayed equation](#eq:p5-two-values),
every such point belongs to $P$, and hence $P$ is open.

The interval $(0,\infty)$ is connected, so it cannot be written as a
union of two disjoint nonempty open subsets. Since $P$ is nonempty, we
must have $Z=\varnothing$. Therefore $d(x)=c$ for every $x>0$.
Combining this conclusion with the case $d\equiv 0$, we obtain
$$
f(x)=x+c
$$
for some constant $c\geq 0$.

### 4. Verification

Conversely, let $f(x)=x+c$ for some $c\geq 0$. Then
$$
f(y)=y+c
 \quad\text{and}\quad
 \frac{f(x)+y}{2}
 =\frac{x+c+y}{2}
 =\frac{x+f(y)}{2}.
$$
Thus the desired inequalities become
$$
\sqrt{\frac{x^2+f(y)^2}{2}}
 \geq \frac{x+f(y)}{2}
 \geq \sqrt{x f(y)},
$$
which are exactly the root-mean-square--arithmetic-mean inequality and
the arithmetic-mean--geometric-mean inequality, applied to the positive
numbers $x$ and $f(y)$. Hence every function $f(x)=x+c$ with $c\geq 0$
is a solution.
∎
