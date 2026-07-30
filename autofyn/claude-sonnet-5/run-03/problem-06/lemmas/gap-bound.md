## Lemma (Gap bound)

For the greedy sequence $(a_n)$ of imo-2026-06 ($a_1>1$; $a_{n+1}$ is the smallest integer $>a_n$
with $\gcd(a_{n+1},a_i)>1$ for all $i=1,\dots,n$), let $L_0 := \mathrm{rad}(a_1) = \prod_{p\mid a_1} p$.
Then for every $n\ge 1$:
$$a_{n+1}-a_n \le L_0.$$

## Proof

**Step 1 (every term hits $S:=\mathrm{primes}(a_1)$).** For $i=1$ this is trivial. For $i\ge2$, by
the recursive definition (taking the constraint index $j=1$, valid since $i-1\ge1$),
$\gcd(a_i,a_1)>1$, so $a_i$ and $a_1$ share a prime factor, which by definition lies in $S$. Hence
$\mathrm{primes}(a_i)\cap S\ne\emptyset$ for every $i\ge1$.

**Step 2 (an explicit valid candidate within $L_0$ of $a_n$).** Fix $n\ge1$ and let $M$ be the
smallest multiple of $L_0$ with $M>a_n$; writing $a_n=qL_0+s$, $0\le s<L_0$, gives $M=a_n+(L_0-s)$,
so $0<M-a_n\le L_0$. Since $L_0=\prod_{p\in S}p$ divides $M$, every prime of $S$ divides $M$. For
each $i=1,\dots,n$, Step 1 gives a prime $p_i\in S\cap\mathrm{primes}(a_i)$; since $p_i\mid M$ and
$p_i\mid a_i$, $\gcd(M,a_i)\ge p_i>1$. So $M$ satisfies the full defining condition for $a_{n+1}$.

**Step 3 (conclude).** Since $a_{n+1}$ is by definition the *smallest* integer $>a_n$ satisfying
that condition, and $M$ is one such integer, $a_{n+1}\le M\le a_n+L_0$. $\blacksquare$

## Status
Certified. Proved independently (identically) in all three of `growth-bound-density`,
`core-signature-pigeonhole`, and `monovariant-telescoping`; reviewed and re-derived from scratch by
the proof-reviewer (round 1) and confirmed correct. Uses only the problem's definition; no external
theorem needed.

## Corollary (linear growth)
$a_N \le a_1 + (N-1)L_0$ for all $N\ge1$, by telescoping the Lemma over $n=1,\dots,N-1$.
