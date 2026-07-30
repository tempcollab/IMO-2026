## Definitions
$Q := \{$primes $q$ : $q$ divides $a_n$ for infinitely many $n\}$.

## Lemma (Q-cover)
For every $i\ge1$, $a_i$ has a prime factor in $Q$. In particular $Q\ne\emptyset$.

*Proof.* Write $a_i=\prod_{j=1}^k r_j^{e_j}$ ($k\ge1$). Suppose none of $r_1,\dots,r_k\in Q$, i.e.
each $r_j$ divides only finitely many terms; let $M_j:=\max\{n : r_j\mid a_n\}$ (finite, and exists
since $r_j\mid a_i$), $M:=\max(M_1,\dots,M_k,i)$. For $n>M$, no $r_j$ divides $a_n$, so
$\gcd(a_n,a_i)=1$. But the recursive definition (applied at step $m=n-1\ge i$, constraint index
$j=i$) forces $\gcd(a_n,a_i)>1$ for every $n>i$ — contradiction at $n=M+1$. $\blacksquare$

## Proposition (Density inequality)
$\sum_{q\in Q}\tfrac1q \ge \tfrac1{L_0}$, where $L_0=\mathrm{rad}(a_1)$.

*Proof.* Fix $N$. By the Q-cover lemma, $\{1,\dots,N\}=\bigcup_{q\in Q}\{i\le N: q\mid a_i\}$, so by
the union bound $N\le\sum_{q\in Q}\#\{i\le N: q\mid a_i\}$. Since $a_1<\dots<a_N$ are distinct
positive integers $\le a_N$, $\#\{i\le N: q\mid a_i\}\le\lfloor a_N/q\rfloor\le a_N/q$. So
$N\le a_N\sum_{q\in Q}1/q$, i.e. $\sum_{q\in Q}1/q\ge N/a_N$. By the gap-bound corollary,
$a_N\le a_1+(N-1)L_0$, so $N/a_N\to 1/L_0$ as $N\to\infty$; taking $N\to\infty$ gives
$\sum_{q\in Q}1/q\ge 1/L_0$. $\blacksquare$

## Status
Certified: both results proved in full in `monovariant-telescoping.md` (Lemma 2, Proposition 3),
reviewed and confirmed correct (the Q-cover argument is a clean finite-maximum contradiction; the
density bound is a valid one-directional union-bound estimate). Reusable as general-purpose facts
about the sequence, independent of $S=\mathrm{primes}(a_1)$.

**Important caveat, established by the reviewer (round 1) and required reading before reuse**: $Q$
is **not** small in general, and proving $|Q|<\infty$ (the goal `monovariant-telescoping` set for
itself) is not merely open but appears to be **false**. Reason: if the sequence's difference is
eventually periodic with period $T$ and total shift $L$ (i.e. exactly the theorem's own
conclusion), then for *every* prime $p\nmid L$, the arithmetic progression $a_n+kL\ (k=0,1,2,\dots)$
cycles through every residue mod $p$ and so hits $0\bmod p$ infinitely often — i.e. $p\in Q$. Hence
$Q$ would be cofinite in the primes (complement contained in the divisors of $L$), not finite. This
was directly confirmed by simulation for $a_1=15$ (gaps eventually periodic with period 8, sum
$L=30$; primes $7,11,13,\dots,101$ each divide hundreds of the first 3000 terms, hence lie in $Q$)
and for $a_1=21$ (all terms are multiples of 3; every prime $p\ne3$ still divides infinitely many
terms). This directly contradicts `monovariant-telescoping.md`'s reported empirical claim that
"$Q=\{2,3\}$ for $a_1=15$" and "$Q=\{3\}$ for $a_1=21$" — those specific claims are factually wrong
(see the proof-reviewer's round-1 review for the corrected simulation). **Any approach reusing
these two lemmas should not attempt to prove $|Q|<\infty$**; a different finite invariant is
needed.
