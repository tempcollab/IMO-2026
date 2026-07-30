## Lemma A (Signature stabilization, generic finite core set)

Let $P$ be *any* fixed finite set of primes with $\mathrm{primes}(a_1)\subseteq P$. For $n\ge1$
define the $P$-signature $D_n := P\cap\mathrm{primes}(a_n)$ (nonempty, since every $a_n$ shares a
prime with $a_1\in$-generated $S\subseteq P$ — see `gap-bound.md` Step 1). Let
$R_n:=\{D_1,\dots,D_n\}\subseteq 2^P\setminus\{\emptyset\}$. Then there exists $N_1\ge1$ and a fixed
$R\subseteq 2^P\setminus\{\emptyset\}$ such that $R_n=R$ for all $n\ge N_1$.

*Proof.* $R_n\subseteq R_{n+1}$ for all $n$ (adding one more signature only adds elements), so
$(R_n)$ is a non-decreasing chain of subsets of the finite set $2^P\setminus\{\emptyset\}$ (size
$2^{|P|}-1$). Such a chain can strictly increase at most $2^{|P|}-1$ times, so it stabilizes at some
$N_1\le 2^{|P|}$. $\blacksquare$ (Pigeonhole/extremal principle for monotone chains in a finite
poset.)

## Lemma B (CRT reduction and sufficiency)

With $P,R$ as above, let $L_P:=\prod_{p\in P}p$. For $x\in\mathbb Z$, $\pi(x):=P\cap\mathrm{primes}(x)$
depends only on $x\bmod L_P$ (since divisibility by each $p\in P$ depends only on $x\bmod p$, and
the primes of $P$ are pairwise coprime — Chinese Remainder Theorem). Define
$$G:=\{r\in\mathbb Z/L_P\mathbb Z : \pi(r)\cap D\ne\emptyset\ \text{for every } D\in R\}.$$
Then $0\in G$ (since $\pi(0)=P\supseteq D$ for every nonempty $D$). Moreover, for $n\ge N_1$: if
$x\bmod L_P\in G$ then $\gcd(x,a_i)>1$ for every $i=1,\dots,n$.

*Proof of the sufficiency claim.* Fix $i\le n$. Since $n\ge N_1$, $D_i\in R_n=R$ (Lemma A). Since
$x\bmod L_P\in G$, $\pi(x)\cap D_i\ne\emptyset$: some prime $p\in P$ divides both $x$ and $a_i$
(as $p\in D_i=P\cap\mathrm{primes}(a_i)$ means $p\mid a_i$), so $\gcd(x,a_i)\ge p>1$. $\blacksquare$

Consequently, defining $y_{n+1}:=\min\{x>a_n : x\bmod L_P\in G\}$ for $n\ge N_1$, one gets
$y_{n+1}-a_n\le L_P$ (the smallest multiple of $L_P$ exceeding $a_n$ has residue $0\in G$) and,
by the sufficiency claim, $a_{n+1}\le y_{n+1}$ (since $a_{n+1}$ is the *smallest* valid candidate
and $y_{n+1}$ is *a* valid candidate).

## Status
Certified as a **generic, reusable pair of lemmas**: they hold for *any* fixed finite prime set
$P\supseteq\mathrm{primes}(a_1)$, not tied to a specific choice (e.g. $P=\mathrm{primes}(a_1)$,
$P=\{p\text{ prime}: p\le\mathrm{rad}(a_1)\}$, or any other finite superset). Proved in full in
`core-signature-pigeonhole.md` (Lemmas 3–5), reviewed and confirmed correct (CRT usage and
pigeonhole chain argument both verified). Importable by any future approach that wants to try a
different candidate $P$.

**What this pair does NOT give**: only a one-directional inequality $a_{n+1}\le y_{n+1}$ (a valid
candidate is found within the window, so the true next term is at most that candidate). It does
**not** establish $a_{n+1}=y_{n+1}$ (i.e. that no smaller $x$ in $(a_n,y_{n+1})$ can also be valid
via a prime outside $P$) — that is the open "No-Escape" gap, which is a genuine additional fact
about the specific dynamics of the sequence, not automatic from CRT/pigeonhole alone.
