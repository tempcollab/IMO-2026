## Lemma (LCR Global Validity Corollary)

**Statement.** Adopt the setup of `lemmas/local-congruence-reduction.md`. Fix $i\ge1$ and suppose
P-Confinement holds for every generator index $<i$. Then for **every** integer $x$ (no restriction
$x>a_{i-1}$): if $\pi(x)\cap D_j\ne\emptyset$ for every $j\in\mathcal A_{i-1}$, then $\gcd(x,a_j)>1$
for every $j=1,\dots,i-1$.

**Proof.** This is literally the ($\Leftarrow$) half of the proof of `local-congruence-reduction.md`,
read with the hypothesis $x>a_{i-1}$ deleted: that proof, verbatim, is: fix $j\in\mathcal A_{i-1}$;
$\pi(x)\cap D_j^P\ne\emptyset$ (given); by the induction hypothesis $D_j\subseteq P$ so $D_j^P=D_j$,
giving a common prime factor of $x$ and $a_j$, i.e. $\gcd(x,a_j)>1$; this holds for every
$j\in\mathcal A_{i-1}$, and by Constraint Domination (`lemmas/constraint-domination.md`) this is
equivalent to $\gcd(x,a_j)>1$ for every $j=1,\dots,i-1$. At no point does this chain of implications
use $x>a_{i-1}$; that hypothesis was only needed in the lemma's *other* half (validity $\Rightarrow$
residue condition) and in the final "so $x$ is a valid candidate" phrasing of the original lemma
(which presupposes $x$ is being considered as a candidate at all, a cosmetic framing, not a step used
in the derivation). $\blacksquare$

**Status.** Certified. Proved by `approaches/leftover-witness-confinement.md` (round 5), by direct
re-inspection of the already-certified `lemmas/local-congruence-reduction.md` proof text. Flagged as
needed by `math-explorer-minimal-counterexample.md` (round 5) and the round-5 outline-reviewer before
being relied upon elsewhere; now certified as its own standalone fact.

---

## Lemma (Leftover-Witness Dichotomy)

**Statement.** Adopt the minimal-counterexample setup for P-Confinement (PC): let $n\ge2$ be minimal
such that some generator index $n$ (i.e. $D_n$ is a genuine new inclusion-minimal element of
$\{D_1,\dots,D_n\}$ — see the Convention below) has $D_n\not\subseteq P$; fix a prime $q\mid a_n$
with $q>L_0$, let $e:=v_q(a_n)\ge1$, and $m:=a_n/q^e$. Then exactly one of:

- **Case A.** $m<a_1$; or
- **Case B.** $m=a_k$ for a (necessarily unique) index $k\in\{1,\dots,n-1\}$.

**Convention (non-redundancy of generator indices).** Throughout, "index $i$ is a generator" means:
$D_i$ is not a superset of, and not equal to, any $D_j$ for $j<i$. (This is the natural reading under
which $\mathcal A_n$, as used in `lemmas/pc-implies-theorem.md` Step A, is genuinely an antichain of
*distinct* sets, each entering the record exactly once, at its first — and only — occurrence as an
inclusion-minimal new set. It agrees with `lemmas/constraint-domination.md`'s literal "inclusion-minimal
index" definition except that it additionally excludes exact repeats of an earlier $D_j$ from counting
as a second, redundant occurrence of the same antichain element — repeats carry no extra information
for Constraint Domination either, so this refinement changes nothing about which lemmas apply.)

**Proof.**

By minimality of $n$, PC holds for every generator index $<n$. Since $n\ge2$, $a_{n-1}$ is defined and
(by the strictly increasing definition of the sequence) $a_1<a_2<\dots<a_{n-1}<a_n$.

*Step 1: $m$ is globally valid against $a_1,\dots,a_{n-1}$.* Since $a_n$ is itself a valid candidate at
its own step, $\gcd(a_n,a_j)>1$ for every $j=1,\dots,n-1$; in particular for every $j\in\mathcal
A_{n-1}\subseteq\{1,\dots,n-1\}$, so there is a common prime factor $p$ of $a_n$ and $a_j$. By the
induction hypothesis (PC for the generator $j<n$), $D_j\subseteq P$, so $p\in D_j\subseteq P$, i.e.
$p\in\pi(a_n)$. Hence $\pi(a_n)\cap D_j\ne\emptyset$ for every $j\in\mathcal A_{n-1}$. Now, $q\notin P$
(as $q>L_0$), so removing all copies of $q$ from $a_n$ does not change which primes of $P$ divide the
resulting integer: $\pi(m)=\pi(a_n)$ (every prime of $P$ dividing $a_n$ still divides $m=a_n/q^e$,
since it is coprime to $q$ and $a_n=q^e m$; conversely every prime of $P$ dividing $m$ divides $a_n$).
So $\pi(m)\cap D_j\ne\emptyset$ for every $j\in\mathcal A_{n-1}$. By the LCR Global Validity Corollary
above (applicable since PC holds for every generator index $<n$), $\gcd(m,a_j)>1$ for every
$j=1,\dots,n-1$.

*Step 2: $m<a_n$, and if $m>a_{n-1}$ then $m=a_n$ — a contradiction, forcing $m\le a_{n-1}$.* Since
$q$ is prime and $e\ge1$, $q^e\ge2$, so $m=a_n/q^e\le a_n/2<a_n$. Suppose for contradiction
$m>a_{n-1}$. By Step 1, $m$ is a valid candidate for step $n$ (it validates against $a_1,\dots,a_{n-1}$)
and $m>a_{n-1}$; by the defining minimality of $a_n$ (the smallest integer $>a_{n-1}$ valid against
$a_1,\dots,a_{n-1}$), $a_n\le m$. This contradicts $m<a_n$ from the previous sentence. Hence
$m\le a_{n-1}$.

*Step 3: dichotomy.* If $m<a_1$, we are in Case A and done. Otherwise $a_1\le m\le a_{n-1}$. Since
$a_1<a_2<\dots<a_{n-1}$ is strictly increasing, there is a unique $k\in\{1,\dots,n-1\}$ with
$a_{k-1}<m\le a_k$, where for $k=1$ this is read simply as $m\le a_1$ (there is no constraint from
"$a_0$"). We show $m=a_k$.

  - If $k=1$: we are given $a_1\le m$ (this sub-case's hypothesis) and $m\le a_1$ (definition of
    $k=1$), so $m=a_1=a_k$.
  - If $k\ge2$: by Step 1, $m$ validates against $a_1,\dots,a_{k-1}$ (a sub-collection of the $n-1$
    validated constraints, since $k-1\le n-2<n-1$), and $m>a_{k-1}$ (definition of $k$). By the
    defining minimality of $a_k$ (the smallest integer $>a_{k-1}$ valid against $a_1,\dots,a_{k-1}$),
    $a_k\le m$. Combined with $m\le a_k$ (definition of $k$), $m=a_k$.

  In either case $m=a_k$ for the unique $k\in\{1,\dots,n-1\}$, i.e. Case B.

Cases A and B are mutually exclusive ($m<a_1$ vs. $m\ge a_1$) and, by Step 3, exhaustive whenever
$m\ge a_1$ (Case B always resolves in that regime). $\blacksquare$

**Status.** Certified. Proved in full by `approaches/leftover-witness-confinement.md` (round 5),
sharpening the sketch in `math-explorer-minimal-counterexample.md` (which left the boundary case
$m=a_1$ and the general "find $k$" argument slightly informal): Step 2 above directly shows $m\le
a_{n-1}$ from $a_n$'s own minimality (bypassing the need to separately rule out $k=n$), and Step 3's
$k=1$ sub-case cleanly resolves the $m=a_1$ boundary as an instance of Case B with $k=1$, fixing the
convention ambiguity flagged by the round-5 outline. Computationally consistent with 1233/1233 checked
instances reported by the round-5 explorer (this proof establishes the dichotomy unconditionally, not
just empirically, under the stated minimal-counterexample hypotheses).

## Corollary (Case B is impossible for a genuine new generator)

**Statement.** In the setting of the Leftover-Witness Dichotomy, Case B cannot occur: $n$ being a
generator index (per the stated Convention) rules out $m=a_k$ for any $k<n$.

**Proof.** Suppose $m=a_k$, $k<n$. Then $a_n=q^e\cdot a_k$, so every prime factor of $a_k$ divides
$a_n$, i.e. $D_k\subseteq D_n$. Also $q\mid a_n$ with $q>L_0$; since $k<n$ is itself... (no assumption
needed on whether $k$ is a generator) we only need $D_k\subseteq D_n$ and $k<n$: by the Convention,
$n$ being a generator requires $D_n$ to not be a superset of (nor equal to) any $D_j$, $j<n$ — but
$D_k\subseteq D_n$ with $k<n$ violates exactly this (whether the inclusion is proper or an equality,
both are excluded by the Convention). Contradiction. $\blacksquare$

**Consequence.** At the first PC-violating generator index $n$, Case A holds: $m<a_1$, a **fixed
bound independent of $n$**.

**Status.** Certified alongside the Dichotomy above, same source.
