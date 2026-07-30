## Status
solved

## Approaches tried
- **Round 6 (this round, new approach, built to completion).** Transplanted, fully re-derived from
  scratch (not cited), the "good numbers" machinery of crux `aimo-0030` (IMO 2022 P3), applied
  **globally** with the fixed threshold $k:=a_1$ (as opposed to the round-5 refuted *local* per-step
  transplant against the moving floor $a_{i-1}$, concrete counterexample $a_1=15$, $a_{i-1}=1009$ vs.
  $q=17$ — that attempt is unrelated to this one and stays dead). Built four pieces in full: (1) a
  self-contained recursive re-definition of "good" avoiding all game-theoretic language; (2) the
  **Correspondence Lemma** identifying the good numbers $\ge a_1$ exactly with the terms of $(a_n)$
  (flagged by the outline as "bookkeeping," confirmed to be a clean, complete one-page induction, no
  hidden difficulty); (3) the **Purification Lemma** (`aimo-0030`'s Claim 4) with its size bound
  $x^*\le b$ derived in full, closing the outline's first flagged gap; (4) the **Signature Determinacy
  Theorem** (`aimo-0030`'s Claims 4–5, Solution 2's full similarity-classification argument) via
  minimal-counterexample-by-$\max$ induction, closing the outline's second flagged gap, with the
  circularity risk the reviewer flagged explicitly checked and avoided (every step of the induction
  uses only the *recursive definition* of good/bad and the already-established Purification Lemma, never
  the determinacy conclusion itself). Combined with an elementary periodic-enumeration argument, this
  gives a complete, unconditional proof of the theorem **for every $a_1\ge2$** (both parities), not just
  odd — the even case is reproduced as the special instance $T=1,L=2$, consistent with
  `lemmas/even-persistence.md` but not depending on it. **Verdict: solved**, no dependence on the
  antichain-of-prime-sets machinery, PC, Antichain Stabilization, or "Step 6" at all — a fully
  independent, self-contained proof of the whole theorem.
- Computational sanity checks performed (not part of the written proof, per CLAUDE.md's rule that a
  numeric check is not a proof step, but used to validate the logic before committing to the full
  write-up): for $a_1\in\{9,15,21,45\}$, brute-force computed "good" via the literal recursive
  definition on $[a_1,250]$ and confirmed it exactly matches the greedy sequence $(a_n)$
  (Correspondence Lemma, 0 mismatches); for $a_1\in\{15,45,105\}$, brute-force checked 0 mismatches
  between the good/bad status of any two integers in $[a_1,600]$ sharing the same small-prime signature
  (Signature Determinacy, 0 mismatches across all repeated signatures found).

## Current best
Superseded by the full proof below — the theorem is fully solved by this approach, independent of the
odd/even split and independent of every other approach in the population.

## Full proof

Throughout, fix $a_1=:k\ge2$ (any positive integer $>1$; we do not use parity anywhere, so this proof
covers both cases of the theorem, in particular the odd case, which is all that remained open). Write
$(a_n)_{n\ge1}$ for the sequence given in the problem: $a_1=k$, and for $n\ge1$, $a_{n+1}$ is the
smallest integer $>a_n$ such that $\gcd(a_{n+1},a_i)>1$ for every $i=1,\dots,n$. The problem statement
guarantees this is a well-defined infinite sequence of integers $>1$; in particular $(a_n)$ is strictly
increasing and unbounded.

### 0. A self-contained recursive object: "good" integers

Call a prime $p$ **small** if $p\le k$ and **big** if $p>k$. For an integer $x\ge k$ define its
**signature** $\pi(x):=\{p\text{ prime}: p\le k,\ p\mid x\}$ (possibly empty), and call two integers
$x,x'\ge k$ **similar** if $\pi(x)=\pi(x')$.

Define a function $\mathrm{good}:\{k,k+1,k+2,\dots\}\to\{\text{True},\text{False}\}$ by strong
recursion on $x$:
$$\mathrm{good}(x) \;:=\; \Big[\,\text{every } m \text{ with } k\le m<x \text{ and } \gcd(m,x)=1 \text{ satisfies } \mathrm{good}(m)=\text{False}\,\Big].$$
This is a legitimate recursive definition: the well-founded order on $\{k,k+1,\dots\}$ (order-isomorphic
to $\mathbb N$) lets us define $\mathrm{good}(x)$ using only the values $\mathrm{good}(m)$ for $m<x$,
already defined by the induction hypothesis; for $x=k$ there is no valid $m$ (the range $k\le m<k$ is
empty), so the bracketed condition is vacuously true and $\mathrm{good}(k)=\text{True}$ automatically,
with no separate base case needed. We call $x$ **good** if $\mathrm{good}(x)=\text{True}$, and **bad**
otherwise. Unwinding the definition: $x$ is bad if and only if there exists $m$ with $k\le m<x$,
$\gcd(m,x)=1$, and $m$ good. (This is exactly the notion of "good number" from the two-player game in
`aimo-0030`/IMO 2022 P3, but we do not use any game-theoretic language or reasoning below — the
recursive definition above is self-contained and all subsequent claims are proved directly from it.)

**Fact 1 (pairwise sharing).** Any two distinct good integers $g,g'\ge k$ satisfy $\gcd(g,g')>1$.

*Proof.* Say $g<g'$ (the case $g'<g$ is symmetric after renaming). Suppose for contradiction
$\gcd(g,g')=1$. Then $m:=g$ satisfies $k\le m<g'$, $\gcd(m,g')=1$, and $m=g$ is good; by the recursive
definition this exactly witnesses that $g'$ is bad — contradicting $g'$ good. Hence $\gcd(g,g')>1$. $\blacksquare$

### 1. Correspondence Lemma: the good integers $\ge k$ are exactly the terms of $(a_n)$

**Lemma 0.** For every $n\ge1$:
(i) $a_n$ is good;
(ii) every integer $x$ with $a_n<x<a_{n+1}$ is bad;
(iii) $\{x\in[k,a_n] : x\text{ good}\}=\{a_1,\dots,a_n\}$.

*Proof.* Induction on $n$.

*Base $n=1$.* $a_1=k$ is good (shown above, vacuously). For (iii): the only integer in $[k,a_1]=[k,k]$
is $k=a_1$ itself, so $\{x\in[k,a_1]:x\text{ good}\}=\{a_1\}$. For (ii): let $a_1<x<a_2$. By the
minimality defining $a_2$ (the smallest integer $>a_1$ with $\gcd(\cdot,a_1)>1$), and since $x>a_1$
fails to be $a_2$ despite being smaller, we must have $\gcd(x,a_1)\le1$, i.e. $\gcd(x,a_1)=1$. Since
$a_1$ is good, $k\le a_1<x$, and $\gcd(a_1,x)=1$, the integer $m=a_1$ witnesses that $x$ is bad.

*Inductive step.* Assume (i)–(iii) hold for $n$; we prove them for $n+1$.

**(a) $a_{n+1}$ is good.** Let $m$ be any integer with $k\le m<a_{n+1}$ and $\gcd(m,a_{n+1})=1$; we show
$m$ is bad, which (since $m$ ranges over exactly the integers the recursive definition of "good" quantifies
over for $x=a_{n+1}$) establishes $\mathrm{good}(a_{n+1})=\text{True}$.
- If $a_n<m<a_{n+1}$: by the inductive hypothesis (ii) for $n$, $m$ is bad.
- If $k\le m\le a_n$: by the inductive hypothesis (iii) for $n$, either $m\in\{a_1,\dots,a_n\}$ or $m$ is
  bad. If $m=a_i$ for some $i\le n$, then by the defining property of $a_{n+1}$ (it satisfies
  $\gcd(a_{n+1},a_j)>1$ for every $j\le n$) we get $\gcd(a_{n+1},m)=\gcd(a_{n+1},a_i)>1$, contradicting
  $\gcd(m,a_{n+1})=1$. So $m\notin\{a_1,\dots,a_n\}$, forcing $m$ bad.

In both cases $m$ is bad, so every valid $m$ is bad, so $a_{n+1}$ is good.

**(b) (iii) for $n+1$.** By the inductive hypothesis (iii) and (ii) for $n$, and part (a) just proved:
$$\{x\in[k,a_{n+1}]:x\text{ good}\}=\{x\in[k,a_n]:x\text{ good}\}\ \cup\ \{x\in(a_n,a_{n+1}):x\text{ good}\}\ \cup\ \{a_{n+1}\}$$
$$=\{a_1,\dots,a_n\}\ \cup\ \varnothing\ \cup\ \{a_{n+1}\}=\{a_1,\dots,a_{n+1}\}.$$
(The middle set is empty by inductive hypothesis (ii): every integer strictly between $a_n$ and
$a_{n+1}$ is bad.)

**(c) (ii) for $n+1$.** Let $a_{n+1}<x<a_{n+2}$. By minimality defining $a_{n+2}$ (the smallest integer
$>a_{n+1}$ with $\gcd(\cdot,a_j)>1$ for every $j\le n+1$), and $x$ failing to be $a_{n+2}$, there is some
$i\le n+1$ with $\gcd(x,a_i)=1$. By part (b), $a_i\in\{a_1,\dots,a_{n+1}\}$ is good, and $a_i\le
a_{n+1}<x$, so $m=a_i$ witnesses that $x$ is bad.

This completes the induction, proving (i)-(iii) for all $n\ge1$. $\blacksquare$

**Corollary (Lemma 0).** $\{x\ge k : x\text{ good}\}=\{a_1,a_2,a_3,\dots\}$.

*Proof.* "$\supseteq$" is Lemma 0(i). For "$\subseteq$": let $x\ge k$ be good. Since $(a_n)$ is strictly
increasing and unbounded (given), there is $n$ with $x\le a_n$. By Lemma 0(iii), $x\in\{a_1,\dots,a_n\}$. $\blacksquare$

### 2. Purification Lemma

**Lemma 1 (Purification).** Let $b\ge k$ have at least one small prime factor. Then there exists an
integer $x$ with $k\le x\le b$, similar to $b$ ($\pi(x)=\pi(b)$), and having **no big prime factor**
(every prime factor of $x$ is $\le k$).

*Proof.* If $b$ itself has no big prime factor, take $x=b$; then $\pi(x)=\pi(b)$ trivially, $k\le x\le
b$, done. Otherwise fix a small prime $p\mid b$ and a big prime $q\mid b$ (both exist by hypothesis and
by the case we are in). Let
$$a:=\prod_{\substack{p'\text{ prime},\, p'\mid b\\ p'\le k}} p'$$
be the (squarefree) product of the *distinct* small primes dividing $b$; note $\pi(a)=\pi(b)$ (both
equal the set of small primes dividing $b$) and $a$ has no big prime factor. Also $a\mid b$: each prime
in the product divides $b$, the primes are pairwise distinct, so their product (being squarefree)
divides $b$. Since $p\mid a$ by construction, $a\ge p$.

Let $n\ge0$ be the least integer with $x:=p^n a\ge k$. Then $\pi(x)=\pi(a)=\pi(b)$ (multiplying $a$ by
extra copies of the small prime $p$, already a factor of $a$, introduces no new prime and removes none),
and $x\ge k$ by choice of $n$. It remains to show $x\le b$.

*Case $n=0$.* Then $x=a$. Since $a\mid b$ and $q\mid b$ with $q\nmid a$ ($q$ big, $a$ has only small
prime factors), $b/a$ is a multiple of $q>1$, so $b>a=x$; in particular $x\le b$.

*Case $n\ge1$.* By minimality of $n$, $p^{n-1}a<k$, so $x=p^n a=p\cdot(p^{n-1}a)<pk$. Since $p\le a$
(shown above) and $k<q$ (as $q$ is big), we get
$$x<pk\le ak<aq.$$
Now $a$ and $q$ are coprime ($a$ has only small prime factors, $q$ is big), and both divide $b$
($a\mid b$ shown above, $q\mid b$ by choice); hence $aq\mid b$, so $aq\le b$. Combining,
$$x<aq\le b,$$
so $x\le b$ (in fact $x<b$).

In both cases $k\le x\le b$, $\pi(x)=\pi(b)$, and $x$ has no big prime factor. $\blacksquare$

### 3. Signature Determinacy Theorem

**Theorem A.** If $a,b\ge k$ are similar ($\pi(a)=\pi(b)$), then $a$ and $b$ are both good or both bad.

*Proof.* Suppose not. Then the set of pairs $(a,b)$ of similar integers $\ge k$ with one good and one
bad is nonempty; by well-ordering, choose such a pair with $\max(a,b)$ minimal, and relabel so that $a$
is bad and $b$ is good.

Since $a$ is bad, by the recursive definition there exists $r$ with $k\le r<a$, $\gcd(r,a)=1$, and $r$
good.

$r$ has a small prime factor: $\gcd(r,k)>1$ (if $r\ne k$, this is Fact 1 applied to the two distinct
good integers $r,k$; if $r=k$, then $\gcd(r,k)=k\ge2>1$ trivially), so any prime $p_0\mid\gcd(r,k)$
satisfies $p_0\mid k$, hence $p_0\le k$, i.e. $p_0$ is a small prime dividing $r$.

Apply Lemma 1 to $b:=r$ (satisfying its hypothesis): there is $r'$ with $k\le r'\le r$, $\pi(r')=\pi(r)$,
and $r'$ having no big prime factor.

We claim $r'$ is good. If $r'$ were bad, then $(r',r)$ would be a pair of similar integers $\ge k$
(similar since $\pi(r')=\pi(r)$) with $r'$ bad and $r$ good — a counterexample to Theorem A — and
$\max(r',r)=r$ (as $r'\le r$). But $r<a\le\max(a,b)$, so $\max(r',r)<\max(a,b)$, contradicting the
minimality of $(a,b)$ among counterexamples. Hence $r'$ is good.

Now $r'$ and $b$ are both good, so $\gcd(r',b)>1$: if $r'\ne b$ this is Fact 1; if $r'=b$ then
$\gcd(r',b)=r'\ge k\ge2>1$ trivially. Let $p$ be a prime dividing $\gcd(r',b)$. Since $r'$ has no big
prime factor, $p$ is small ($p\le k$).

Since $p$ is small and $p\mid r'$: because $\pi(r')=\pi(r)$, $p\in\pi(r)$, so $p\mid r$.
Since $p$ is small and $p\mid b$: because $\pi(a)=\pi(b)$ (the original similarity hypothesis on the
pair $(a,b)$), $p\in\pi(a)$, so $p\mid a$.

Thus $p\mid a$ and $p\mid r$, so $\gcd(a,r)\ge p>1$ — contradicting $\gcd(r,a)=1$ established above.

This contradiction shows no counterexample pair exists, proving Theorem A. $\blacksquare$

(No circularity: the induction above is on $\max(a,b)$ over pairs of *integers*, using only Fact 1 —
which follows directly from the base recursive definition of good/bad, not from Theorem A — and Lemma 1
— proved independently in Section 2. At no point is Theorem A's conclusion assumed for a pair before it
has been established for a strictly smaller $\max$.)

### 4. Periodicity and conclusion

Let $L:=\prod_{p\le k,\ p\text{ prime}}p$ (product of all small primes; a finite, well-defined positive
integer, $L\ge2$).

**Fact 2.** If $x,x'\ge k$ and $x\equiv x'\pmod L$, then $\pi(x)=\pi(x')$.

*Proof.* For any small prime $p\le k$, $p\mid L$ (as $p$ is one of the factors composing $L$), so
$x\equiv x'\pmod L$ implies $x\equiv x'\pmod p$; hence $p\mid x\iff p\mid x'$. As this holds for every
small prime $p$, $\pi(x)=\pi(x')$. $\blacksquare$

**Corollary (periodicity of "good").** For $x\ge k$: $x$ is good $\iff$ $x+L$ is good.

*Proof.* $x\equiv x+L\pmod L$ and $x,x+L\ge k$, so by Fact 2, $\pi(x)=\pi(x+L)$, i.e. $x,x+L$ are
similar. By Theorem A, $x$ good $\iff$ $x+L$ good. $\blacksquare$

Let $G:=\{x\ge k: x\text{ good}\}$. By the Corollary (Section 1), $G=\{a_1,a_2,\dots\}$. Define
$$T:=\#\big(G\cap[k,k+L)\big).$$
Since $a_1=k\in[k,k+L)$ (as $L\ge1$) and $a_1\in G$, $T\ge1$.

**Claim.** $a_{n+T}=a_n+L$ for every $n\ge1$.

*Proof.* By the periodicity Corollary above, for every $x\ge k$: $x\in G\iff x+L\in G$. Hence the map
$\varphi(x):=x+L$ is an order-preserving bijection from $G\cap[k,\infty)$ onto $G\cap[k+L,\infty)$:
it clearly maps into $G\cap[k+L,\infty)$ (if $x\in G$, $x\ge k$, then $x+L\in G$ by periodicity, and
$x+L\ge k+L$); it is injective (as a shift); and it is surjective onto $G\cap[k+L,\infty)$ because for
$y\in G$ with $y\ge k+L$, we have $y-L\ge k$, and periodicity (applied to $x:=y-L\ge k$) gives
$y-L\in G\iff y\in G$; since $y\in G$, also $y-L\in G$, and $\varphi(y-L)=y$.

Since $G=\{a_1,a_2,\dots\}$ listed increasingly, and exactly $T$ of these terms ($a_1,\dots,a_T$) lie in
$[k,k+L)$ by definition of $T$ (the increasing enumeration puts the smallest $T$ elements of $G$, which
are precisely $G\cap[k,k+L)$, at positions $1,\dots,T$), the remaining terms $a_{T+1},a_{T+2},\dots$ are
precisely the increasing enumeration of $G\cap[k+L,\infty)$: that is, $a_{T+n}$ is the $n$-th smallest
element of $G\cap[k+L,\infty)$, for each $n\ge1$.

Since $\varphi$ is an order-preserving bijection $G\cap[k,\infty)\to G\cap[k+L,\infty)$, it carries the
$n$-th smallest element of $G\cap[k,\infty)$ (which is $a_n$) to the $n$-th smallest element of
$G\cap[k+L,\infty)$ (which is $a_{T+n}$). That is,
$$\varphi(a_n)=a_n+L=a_{T+n}=a_{n+T}$$
for every $n\ge1$. $\blacksquare$

### Conclusion

Taking $T$ and $L$ as constructed above (both positive integers, $T\ge1$, $L\ge2$), we have shown
$a_{n+T}=a_n+L$ for every positive integer $n$. This is exactly the statement of the theorem, established
here for **every** $a_1=k\ge2$ — in particular for every odd $a_1$, which was the theorem's entire
remaining open content. $\blacksquare$

**Sanity check (not part of the proof, a consistency check only).** For even $a_1=k$, this construction
gives $L=\prod_{p\le k}p\ge2$ and one can check directly for $k=2$: $L=2$, $G\cap[2,4)=\{2\}$ so $T=1$,
giving $a_{n+1}=a_n+2$, i.e. $a_n=2+2(n-1)=2n$ — matching the independently-certified even-case result
`lemmas/even-persistence.md` ($a_n=a_1+2(n-1)$ for $2\mid a_1$, here $a_1=2$) exactly, though this proof
does not use or depend on that lemma. This is a coherence check only, not a citation.

**Computational corroboration (not a proof step).** For odd $a_1\in\{9,15,21,45\}$, the sequence
$(a_n)$ computed directly from the problem's recursion up to 250 terms was checked to coincide exactly
with the set of integers $x\ge a_1$ satisfying the literal recursive "good" definition of Section 0 (0
mismatches), confirming Lemma 0. For odd $a_1\in\{15,45,105\}$, every pair of integers in $[a_1,600]$
sharing the same small-prime signature was checked to have matching good/bad status (0 mismatches),
confirming Theorem A. These checks validate the logic above; the written proof stands independently of
them.

## Promotable lemmas

The following are fully proved in Section 0–4 above and are proposed for certification (self-contained,
importable by any other approach without dependence on the antichain/PC framework):

1. **Correspondence Lemma** (Lemma 0 + Corollary, Section 1): for the sequence $(a_n)$ defined by the
   problem's recursion with $a_1=k$, and "good" defined by the self-contained recursion of Section 0,
   $\{x\ge k : x\text{ good}\}=\{a_1,a_2,a_3,\dots\}$.
2. **Purification Lemma** (Lemma 1, Section 2): for $b\ge k$ with a small prime factor ($p\le k$,
   $p\mid b$), there is $x$ with $k\le x\le b$, $\pi(x)=\pi(b)$, and $x$ $k$-smooth.
3. **Signature Determinacy Theorem** (Theorem A, Section 3): similar integers $\ge k$ (same small-prime
   signature $\pi$, threshold $k$) are both good or both bad.
4. **Periodic-Enumeration Lemma** (Section 4's Claim, stated generally): if $G\subseteq\mathbb Z_{\ge
   k}$ satisfies $x\in G\iff x+L\in G$ for all $x\ge k$ (some fixed $L\ge1$), and $G$ is infinite with
   increasing enumeration $a_1<a_2<\cdots$, then with $T:=\#(G\cap[k,k+L))$, $a_{n+T}=a_n+L$ for every
   $n\ge1$.

Together these four lemmas constitute a complete, independent proof of the whole theorem (Section 4's
Conclusion) — the full theorem for every $a_1\ge2$, not merely a partial result.
