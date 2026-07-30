## Lemma (Local Congruence Reduction, LCR)

**Statement.** Adopt the notation of `lemmas/pc-implies-theorem.md` / `dilworth-antichain-bound.md`:
$D_i:=\mathrm{primes}(a_i)$, $S:=D_1$, $L_0:=\mathrm{rad}(a_1)$, $P:=\{\text{primes}\le L_0\}$,
$L_P:=\prod_{p\in P}p$, and for $x\in\mathbb Z$, $\pi(x):=P\cap\mathrm{primes}(x)$. Let
$\mathcal A_n$ denote the antichain of inclusion-minimal indices among $\{D_1,\dots,D_n\}$
(`lemmas/constraint-domination.md`).

Fix $i\ge1$ and suppose **P-Confinement holds for every generator index $<i$**, i.e. every $j<i$
such that $D_j$ is inclusion-minimal among $\{D_1,\dots,D_j\}$ satisfies $D_j\subseteq P$. Then for
every integer $x>a_{i-1}$:
$$x\text{ is a valid candidate for }a_i\text{ (i.e. }\gcd(x,a_j)>1\text{ for all }j=1,\dots,i-1\text{)}
\iff x\bmod L_P\in G_{i-1},$$
where $G_{i-1}:=\{r\in\mathbb Z/L_P\mathbb Z:\pi(r)\cap D_j\ne\emptyset\ \forall j\in\mathcal
A_{i-1}\}$. In particular, under this hypothesis, validity of $x$ for $a_i$ depends only on
$x\bmod L_P$.

**Proof.**

($\Leftarrow$) Suppose $x\bmod L_P\in G_{i-1}$. Fix $j\in\mathcal A_{i-1}$; then $\pi(x)\cap
D_j^P\ne\emptyset$ where $D_j^P:=P\cap D_j$. By the hypothesis, $D_j\subseteq P$, so $D_j^P=D_j$;
hence there is a prime $p\in P$ with $p\mid x$ and $p\mid a_j$, so $\gcd(x,a_j)>1$. This holds for
every $j\in\mathcal A_{i-1}$; by Constraint Domination (`lemmas/constraint-domination.md`), validity
against every $j\in\mathcal A_{i-1}$ is equivalent to validity against every $j=1,\dots,i-1$. So $x$
is a valid candidate.

($\Rightarrow$) Suppose $x$ is a valid candidate. Fix $j\in\mathcal A_{i-1}\subseteq\{1,\dots,i-1\}$;
then $\gcd(x,a_j)>1$, so there is a common prime factor $p$ of $x$ and $a_j$, i.e. $p\in D_j$. By
the hypothesis $D_j\subseteq P$, so $p\in P$, giving $p\in\pi(x)\cap D_j$, i.e.
$\pi(x)\cap D_j\ne\emptyset$. This holds for every $j\in\mathcal A_{i-1}$, i.e. $x\bmod L_P\in
G_{i-1}$ (note $\pi(x)$ depends only on $x\bmod L_P$, since each $p\in P$ divides $x$ iff it divides
$x\bmod L_P$, by CRT / the definition of $L_P=\prod_{p\in P}p$). $\blacksquare$

**Source.** `approaches/dilworth-antichain-bound.md` (round 4, "Attempt 2"). Reviewed step by step;
both directions are short, correct, elementary consequences of Constraint Domination and the
definition of $\pi$. No gap found.

**Scope / value.** LCR isolates exactly what remains to be shown, at each inductive step, in order
to prove P-Confinement by strong induction on the generator index: given P-Confinement for all
smaller generator indices, $a_i$ is *exactly* the smallest integer exceeding $a_{i-1}$ lying in the
explicit union of residue classes $G_{i-1}\pmod{L_P}$ — a purely congruence-defined quantity with no
further dependence on antichain bookkeeping. It does **not** itself establish P-Confinement (the
question of whether this minimal congruence solution is always $L_0$-smooth remains open); it is a
reduction/reformulation lemma only, useful to any future approach attacking P-Confinement by
induction on the generator index.
