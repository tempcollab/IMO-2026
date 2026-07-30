## Lemma (P-Confinement $\Rightarrow$ full theorem)

Let $(a_n)_{n\ge1}$ be the greedy sequence of imo-2026-06. Let $S:=\mathrm{primes}(a_1)$,
$L_0:=\mathrm{rad}(a_1)$, $P:=\{p\text{ prime}:p\le L_0\}\supseteq S$ (finite), and
$\mathcal A_n:=\{i\le n: D_i:=\mathrm{primes}(a_i)\text{ is inclusion-minimal in }\{D_1,\dots,D_n\}\}$.

**Definition (P-Confinement, PC).** For every $n\ge1$ and every $i\in\mathcal A_n$, the full,
untruncated prime set $D_i=\mathrm{primes}(a_i)$ satisfies $D_i\subseteq P$.

**Claim.** If PC holds, there exist positive integers $T,L$ with $a_{n+T}=a_n+L$ for every $n\ge1$
(the full theorem).

## Proof

Cited verbatim (already certified): `lemmas/gap-bound.md`, `lemmas/constraint-domination.md`,
`lemmas/signature-stabilization-and-crt-sufficiency.md` (Lemma A gives $N_1$ and fixed
$R\subseteq2^P\setminus\{\emptyset\}$ with $R_n:=\{D_1^P,\dots,D_n^P\}=R$ for $n\ge N_1$, where
$D_k^P:=P\cap D_k$; Lemma B gives $L_P:=\prod_{p\in P}p$, $G:=\{r\in\mathbb Z/L_P\mathbb Z:\pi(r)\cap
D\ne\emptyset\ \forall D\in R\}$ with $\pi(x):=P\cap\mathrm{primes}(x)$, and $a_{n+1}\le y_{n+1}:=
\min\{x>a_n:x\bmod L_P\in G\}$ for $n\ge N_1$), `lemmas/periodicity-given-no-escape.md` (No-Escape,
i.e. $a_{n+1}=y_{n+1}$ for all $n\ge N_1$, $\Rightarrow$ the theorem's conclusion; note $P\supseteq S$
by construction, so this lemma's hypothesis $\mathrm{primes}(a_1)\subseteq P$ is genuinely satisfied
here).

Assume PC. Fix $n\ge N_1$ and let $R'_n:=\{D_i:i\in\mathcal A_n\}$ (the *true*, untruncated prime
sets of the live generators at time $n$); by PC, $R'_n\subseteq2^P\setminus\{\emptyset\}$.

**Step A ($R'_n=\min(R_n)$, the inclusion-minimal elements of $R_n$).**
- $R'_n\subseteq R_n$: for $i\in\mathcal A_n$, PC gives $D_i\subseteq P$, so $D_i^P=D_i\in R_n$.
- Every element of $R_n$ is a superset (in $2^P$) of some element of $R'_n$: fix $k\le n$. In the
  finite poset $\{D_1,\dots,D_n\}$ under $\subseteq$, every element has an inclusion-minimal element
  below or equal to it (finite nonempty poset), so there is $j\le n$ with $D_j\subseteq D_k$ and $D_j$
  inclusion-minimal, i.e. $j\in\mathcal A_n$. By PC, $D_j\subseteq P$, so $D_j=D_j\cap P\subseteq
  D_k\cap P=D_k^P$, i.e. $D_k^P\supseteq D_j\in R'_n$.
- $R'_n$ is itself an antichain (distinct elements of $\mathcal A_n$ have incomparable $D_i$'s by
  definition), and every element of $R_n$ is a superset of some $R'_n$-element (previous bullet), so
  $\min(R_n)=R'_n$.

**Step B ($G$'s condition reduces to checking $R'_n$).** By Step A and the elementary fact that "for
$x\in\mathbb Z$, $\pi(x)\cap D\ne\emptyset$ for every $D\in R_n$" holds iff it holds for every
$D\in\min(R_n)=R'_n$ (necessity trivial; sufficiency because every $D\in R_n\setminus R'_n$ is a
superset of some $D_j\in R'_n$), we get, for $n\ge N_1$ (so $R_n=R$):
$$x\bmod L_P\in G\iff\pi(x)\cap D_i\ne\emptyset\ \ \forall i\in\mathcal A_n.$$

**Step C (translate to the true validity condition).** For $i\in\mathcal A_n$, PC gives $D_i\subseteq
P$, so $\pi(x)\cap D_i=(P\cap\mathrm{primes}(x))\cap D_i=\mathrm{primes}(x)\cap D_i$. Hence
$\pi(x)\cap D_i\ne\emptyset\iff\mathrm{primes}(x)\cap\mathrm{primes}(a_i)\ne\emptyset\iff\gcd(x,a_i)>1$.
Combining with Step B and Constraint Domination (extending from $i\in\mathcal A_n$ to all $i\le n$):
$$x\bmod L_P\in G\iff x\text{ is a valid candidate for }a_{n+1}\text{ (i.e. }\gcd(x,a_i)>1\ \forall
i\le n).$$

**Step D (No-Escape).** Fix $n\ge N_1$ and any $x$ with $a_n<x<y_{n+1}$. By minimality of $y_{n+1}$,
$x\bmod L_P\notin G$, so by Step C $x$ is invalid. Combined with $a_{n+1}\le y_{n+1}$ (already
certified) and $a_{n+1}$ being a valid candidate $>a_n$, we get $a_{n+1}=y_{n+1}$: this is exactly the
No-Escape hypothesis of `lemmas/periodicity-given-no-escape.md` for every $n\ge N_1$.

**Conclusion.** By `lemmas/periodicity-given-no-escape.md`, No-Escape implies there exist $T,L\ge1$
with $a_{n+T}=a_n+L$ for every $n\ge1$. $\blacksquare$

## Status
Certified. Proved in full in `approaches/dilworth-antichain-bound.md` (round 2); reviewed and
re-derived step by step by the proof-reviewer (round 2) — Steps A–D checked independently, no gap
found. Uses only already-certified lemmas plus elementary finite-poset reasoning. Unlike the parallel
reduction attempted in `approaches/antichain-signature-closure.md` (which builds a *new* prime set
$P^*$ from the eventual generators and must re-verify $P^*\supseteq\mathrm{primes}(a_1)$ before citing
`periodicity-given-no-escape.md`, a check that approach's current text does not carry out), this lemma
uses the fixed $P=\{\text{primes}\le L_0\}\supseteq\mathrm{primes}(a_1)$ throughout, so
`periodicity-given-no-escape.md`'s stated hypothesis is genuinely satisfied with no patch needed.

## What remains open
PC itself (the hypothesis) is **not** proved here and is a genuine, well-posed open lemma — verified
computationally with zero violations across multiple values of $a_1$ (see
`approaches/dilworth-antichain-bound.md`), but not proved for general $a_1$. PC is at least as strong
as Antichain Stabilization (PC $\Rightarrow$ Antichain Stabilization, shown informally in the source
approach file) and is not known to be strictly easier; treat it as another restatement of the same
central obstruction (see `current.md`), useful because it discharges the *entire* remaining theorem
with zero secondary gap once granted.
