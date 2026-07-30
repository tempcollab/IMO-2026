## Lemma (Self-closing antichain $\Rightarrow$ permanent stabilization)

Let $(a_n)_{n\ge1}$ be the greedy sequence of imo-2026-06, and for $n\ge1$ let $\mathcal A_n$ be the
antichain of inclusion-minimal elements of $\{\mathrm{primes}(a_1),\dots,\mathrm{primes}(a_n)\}$.

**Definition.** A finite antichain $\mathcal B$ of nonempty finite sets of primes (pairwise
$\subseteq$-incomparable) is **self-closing** if every finite set of primes $F$ with $F\cap B\ne
\emptyset$ for all $B\in\mathcal B$ satisfies $F\supseteq B$ for some $B\in\mathcal B$.

**Claim.** If $\mathcal A_N$ is self-closing for some $N$, then $\mathcal A_n=\mathcal A_N$ for every
$n\ge N$ (Antichain Stabilization holds with $N^*=N$).

## Proof

Induct on $n\ge N$. Suppose $\mathcal A_n=\mathcal A_N$ (base case $n=N$ trivial). The term $a_{n+1}$
satisfies $\gcd(a_{n+1},a_i)>1$ for all $i\le n$ by the problem's defining recursion, so by
Constraint Domination (`lemmas/constraint-domination.md`), applied with a set of indices
$\mathrm{Gen}(n)$ realizing $\mathcal A_n=\mathcal A_N$, it satisfies $\gcd(a_{n+1},a_i)>1$ for all
$i\in\mathrm{Gen}(n)$, i.e. $\mathrm{primes}(a_{n+1})\cap B\ne\emptyset$ for every $B\in\mathcal A_N$
(taking $F=\mathrm{primes}(a_{n+1})$). By self-closing, $\mathrm{primes}(a_{n+1})\supseteq B$ for some
$B\in\mathcal A_N=\mathcal A_n$, so $a_{n+1}$'s prime-set is a superset of an existing generator and
hence is dominated: it does not change the inclusion-minimal set. So $\mathcal A_{n+1}=\mathcal A_n=
\mathcal A_N$. $\blacksquare$

## Status
Certified. Proved in full in `approaches/antichain-signature-closure.md` (round 2, Lemma 5); reviewed
and confirmed correct by the proof-reviewer (round 2) — a direct, gap-free consequence of Constraint
Domination and the definition of self-closing. Subsumes `absorption-lemma.md`'s conclusion as the
special case $\mathcal B=\{\{q\}\}$ (any singleton is trivially self-closing). Verified against two
independent computational examples: $a_1=2310$ (self-closing reached via absorption, singleton
$\{\{2\}\}$ at $n=894$) and $a_1=15$ (self-closing reached without absorption, $\mathcal A_n=
\{\{2,3\},\{2,5\},\{3,5\}\}$ for $n\ge3$).

## What remains open
This lemma converts "prove no more growth events ever occur" into the purely combinatorial target
"a self-closing configuration is always eventually reached, for every $a_1$." That reachability claim
is **not** proved by this lemma and remains the central open gap of the antichain-family approaches
(see `current.md`).
