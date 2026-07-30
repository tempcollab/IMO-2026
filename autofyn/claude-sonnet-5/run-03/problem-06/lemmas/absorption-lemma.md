## Lemma (Prime-power absorption)

Let $(a_n)_{n\ge1}$ be the greedy sequence of imo-2026-06. Suppose for some index $m\ge1$,
$a_m=q^{e}$ for a prime $q$ and integer $e\ge1$ (i.e. $\mathrm{primes}(a_m)=\{q\}$). Then:

(a) $q\mid a_n$ for every positive integer $n$ (not just $n\ge m$).

(b) Writing $\mathcal A_n$ for the antichain of inclusion-minimal elements of
$\{\mathrm{primes}(a_1),\dots,\mathrm{primes}(a_n)\}$, $\mathcal A_n=\{\{q\}\}$ for every $n\ge m$.
In particular the antichain permanently stabilizes at $N^*=m$.

## Proof

(a) For $i<m$: by the problem's defining recursion, $a_m$ (the value chosen at step $m$) satisfies
$\gcd(a_m,a_i)>1$ for every $i=1,\dots,m-1$. Since $a_m=q^e$ has only the prime factor $q$,
$\gcd(q^e,a_i)>1$ forces $q\mid a_i$. So $q\mid a_i$ for $i=1,\dots,m-1$, and trivially $q\mid a_m$.
For $n>m$: induct upward. If $q\mid a_i$ is known for all $i\le n-1$ for some $n-1\ge m$, then in
particular (taking the single index $i=m\le n-1$) the defining recursion for $a_n$ requires
$\gcd(a_n,a_m)>1$, i.e. $q\mid a_n$ (again since $a_m$'s only prime factor is $q$). By induction
starting at $n-1=m$ (base case $q\mid a_m$ already known), $q\mid a_n$ for every $n\ge m$. Combined
with $q\mid a_i$ for $i<m$ shown above, $q\mid a_n$ for every $n\ge1$.

(b) By (a), $q\in\mathrm{primes}(a_n)$ for every $n\ge1$, i.e. $\{q\}\subseteq\mathrm{primes}(a_n)$
for every $n$. Hence $\{q\}$ is a subset of every prime-set that ever appears, so every element of
$\{\mathrm{primes}(a_1),\dots,\mathrm{primes}(a_n)\}$ other than $\{q\}$ itself is dominated (not
inclusion-minimal, since $\{q\}\subsetneq$ it), while $\{q\}$ itself is realized (by index $m$) and
is trivially inclusion-minimal. Hence the set of inclusion-minimal elements is exactly $\{\{q\}\}$:
$\mathcal A_n=\{\{q\}\}$ for all $n\ge m$. $\blacksquare$

## Status
Certified. Proved in full in `approaches/antichain-signature-closure.md` (round 2, Lemma 4); reviewed
and re-derived from scratch by the proof-reviewer (round 2), confirmed correct — a genuinely
self-contained induction using only the problem's definition, no external theorem needed.
Independently confirmed to match computation: for $a_1=2310$, $a_{894}=4096=2^{12}$ is the first
prime-power term, and all of $a_1,\dots,a_{894}$ (indeed the whole sequence checked) are even, exactly
as (a) predicts.

## Reuse note
Gives a clean sufficient condition (and a base case / case-split option) for Antichain Stabilization:
"if the sequence ever produces a term that is a pure prime power, the antichain collapses forever to
a singleton and the full theorem follows immediately via `signature-stabilization-and-crt-sufficiency.md`
+ `periodicity-given-no-escape.md`." Does **not** by itself prove Antichain Stabilization for general
$a_1$ (e.g. $a_1=15$ never produces a prime-power term through the terms checked, yet the antichain
still stabilizes there by a different mechanism — see `self-closing-antichain-sufficiency.md`).
