time 2m 38s

# IMO 2026 Problem 1: GCD–LCM Blackboard Process

## Problem

There are $2026$ integers greater than $1$ written on a blackboard, not
necessarily distinct. In one move, Confucius chooses two integers $m>1$ and
$n>1$ written in different positions and replaces them by
$$
\gcd(m,n)
\qquad\text{and}\qquad
\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}.
$$
He continues making moves for as long as a move is possible.

**(a)** Prove that, regardless of his choices, the process terminates
after finitely many moves with exactly one integer $M>1$ on the board.

**(b)** Prove that the value of $M$ is independent of all choices made
during the process.

## Solution

*Proof.*
Write the entries currently on the board as
$$
x_1,x_2,\dots,x_{2026}.
$$
Entries equal to $1$ remain on the board, but they cannot be selected for a
subsequent move.

### Part (a): termination and the final number of nontrivial entries

For every positive integer $x$, let
$$
\Omega(x)=\sum_{p} v_p(x),
$$
where the sum is over all primes and $v_p(x)$ is the exponent of $p$ in the
prime factorization of $x$. Thus $\Omega(1)=0$. At any stage of the process,
define
$$
T=\sum_{i=1}^{2026}\Omega(x_i)
\qquad\text{and}\qquad
R=\#\{i:x_i>1\}.
$$
We shall prove that the nonnegative integer
$$
\Phi=T+R
$$
strictly decreases after every move.

Suppose a move is made using $m,n>1$, and put
$$
d=\gcd(m,n),
\qquad
q=\frac{\operatorname{lcm}(m,n)}{d}.
$$
Fix a prime $p$, and write
$$
a=v_p(m),
\qquad
b=v_p(n).
$$
Then
$$
v_p(d)=\min(a,b)
$$
and
$$
v_p(q)
      =v_p(\operatorname{lcm}(m,n))-v_p(d)
      =\max(a,b)-\min(a,b)
      =|a-b|.
$$
Consequently,
$$
\begin{aligned}
\bigl(v_p(m)+v_p(n)\bigr)
      -\bigl(v_p(d)+v_p(q)\bigr)
      &=a+b-\min(a,b)-|a-b| \\
      &=\min(a,b).
\end{aligned}
$$
Summing over all primes gives
$$
T_{\mathrm{old}}-T_{\mathrm{new}}
      =\sum_p \min\bigl(v_p(m),v_p(n)\bigr)
      =\Omega(d).
$$

There are now two cases.

If $d>1$, then $\Omega(d)\ge 1$, so $T$ strictly decreases. The two selected
entries are replaced by at most two entries greater than $1$, so $R$ does not
increase. Hence $\Phi$ strictly decreases.

If $d=1$, then $T$ is unchanged. Since $m$ and $n$ are coprime,
$$
q=\operatorname{lcm}(m,n)=mn>1.
$$
Thus the two selected entries greater than $1$ are replaced by exactly one
entry greater than $1$ and one entry equal to $1$. Therefore $R$ decreases by
exactly $1$, and again $\Phi$ strictly decreases.

Since $\Phi$ is a nonnegative integer, it cannot decrease indefinitely. The
process therefore terminates after finitely many moves.

At termination there cannot be two entries greater than $1$, since any such
pair could be selected for another move. Hence $R\le 1$. On the other hand, a
move can never remove all entries greater than $1$: if $d>1$, then the new
entry $d$ is greater than $1$, while if $d=1$, then the new entry $q=mn$ is
greater than $1$. Since initially every entry is greater than $1$, we always
have $R\ge 1$. Thus the terminal board contains exactly one integer $M>1$.

### Part (b): determination and uniqueness of the final value

Fix a prime $p$. For a board with entries $x_1,\dots,x_{2026}$, define
$$
I_p=\gcd\bigl(v_p(x_1),v_p(x_2),\dots,v_p(x_{2026})\bigr),
$$
with the conventions $\gcd(0,t)=t$ and $\gcd(0,\dots,0)=0$.
We claim that $I_p$ is invariant under every move.

Indeed, suppose the two selected entries have $p$-adic valuations $a$ and
$b$. As shown above, after the move these two valuations become
$$
\min(a,b)
\qquad\text{and}\qquad
|a-b|.
$$
Moreover,
$$
\gcd\bigl(\min(a,b),|a-b|\bigr)=\gcd(a,b).
$$
For example, if $a\le b$, then
$$
\gcd\bigl(\min(a,b),|a-b|\bigr)
      =\gcd(a,b-a)
      =\gcd(a,b),
$$
and the case $b\le a$ is symmetric. Since all other $p$-adic valuations are
unchanged, the gcd of the entire list of valuations is unchanged. Therefore
$I_p$ is an invariant.

Let the initial entries be $a_1,\dots,a_{2026}$. On the terminal board, all
entries except $M$ are equal to $1$. Hence its list of $p$-adic valuations is
$$
v_p(M),0,\dots,0,
$$
so the terminal value of the invariant is
$$
I_p=v_p(M).
$$
Comparing with its initial value yields, for every prime $p$,
$$
v_p(M)
      =\gcd\bigl(v_p(a_1),v_p(a_2),\dots,v_p(a_{2026})\bigr).
$$
It follows that
$$
\boxed{
M=\prod_{p\mid a_1a_2\cdots a_{2026}}
       p^{\gcd\left(v_p(a_1),v_p(a_2),\dots,v_p(a_{2026})\right)}
}.
$$
Every exponent in this prime factorization is determined solely by the
initial board. By uniqueness of prime factorization, the final value $M$ is
therefore independent of all choices made by Confucius.
∎
