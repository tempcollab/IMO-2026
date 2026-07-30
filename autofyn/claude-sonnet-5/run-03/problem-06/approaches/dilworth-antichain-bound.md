## Status
partial

## Approaches tried
- **Round 4 (this round): scope narrowed to odd $a_1$ (per sibling `absorption-recurrence-even-case`,
  now certified `solved`: if $a_1$ is even then $a_n=a_1+2(n-1)$ for all $n$, a trivial induction —
  see that file, confirmed by reading it in full this round). So PC (and the whole theorem) is now
  only open for odd $a_1$; this round attacked PC with that restriction in view. Ran three lines of
  attack (all reported precisely below, with the negative ones stated as such, not hidden):
  (1) tested the outline's cumulative monovariant $\nu_n$ candidate and found it carries **no new
  content** beyond an already-certified lemma (see "Attempt 1" below); (2) derived a genuinely new
  structural fact — **Local Congruence Reduction (LCR)** — that pins down exactly what PC's inductive
  step must show, and gives a precise diagnosis of why it looks like it needs non-elementary
  (smooth-number-density-type) input, not just more antichain bookkeeping; (3) tested and **refuted**
  by explicit computation a natural odd-case simplification candidate ("every generator beyond $D_1$
  contains the prime 2"). PC itself remains open; the gap is now stated more precisely than before
  (as a smallest-smooth-solution-of-a-congruence question), which is genuine progress in
  *characterizing* the wall even though it does not remove it. Verified all computational claims below
  independently (fresh simulation code, not reused from a prior round's script).
- **Round 2 (this round), Dilworth/chain-covering mechanism as outlined:** Attempted to formalize
  the outline's "extends" relation on prime-sets realizable within one greedy step and cover it by
  finitely many chains (à la crux `aimo-0716`'s cone+line covering of a triangular poset) to bound
  $\max_n|\mathcal A_n|$ by a function of $\omega(a_1)$ alone. **Found this specific mechanism does
  not close**: the only available static bound on "how many distinct primes can freshly enter a
  window of length $\le L_0$" is $O(\log(a_n+L_0))$ (the number of distinct prime factors of an
  integer of that size), which is **not bounded independently of $n$** — it grows (slowly) with
  $n$, since $a_n\to\infty$. So the chain-covering bound this outline proposes is not actually
  $n$-independent as claimed; a literal transplant of `aimo-0716`'s static geometric covering does
  not apply here because the "window" here has arithmetic content (which primes are available)
  that is unbounded as $n\to\infty$, unlike `aimo-0716`'s fixed geometric triangle. This confirms
  the outline's own flagged risk (Open gaps, point (a)) and is reported here as a genuine negative
  finding for the *literal* Dilworth/chain-covering-by-window-size mechanism — not a proof failure
  to hide, but a real obstruction to this specific technique.
- **Round 2, reformulation that replaces the failed mechanism (new content this round):** Instead of
  bounding antichain *size*, isolated and precisely proved the *exact target that would suffice*:
  a clean, checkable property called **P-Confinement (PC)** of antichain generators (defined below),
  and gave a **complete, rigorous proof that PC $\Rightarrow$ the full theorem**, by showing PC lets
  the two already-certified generic lemmas
  (`lemmas/signature-stabilization-and-crt-sufficiency.md`, `lemmas/periodicity-given-no-escape.md`)
  close with **zero residual gap**, using $P:=\{\text{primes}\le L_0\}$ (the same finite set as
  `core-signature-pigeonhole`, no truncation-by-generator-set needed as in
  `antichain-signature-closure`). This is new, complete mathematics (see Current best), not present
  in any other approach file, though PC itself remains open and is (by the analysis below) very
  likely of comparable difficulty to Antichain Stabilization / No-Escape, not a strictly easier
  target. Verified computationally with **zero violations** across 13 values of $a_1$ (with
  $\omega(a_1)$ ranging from 1 to 7) over up to 1200 terms each. **Verdict: real partial progress —
  a complete new sufficient reduction plus an honestly-flagged open lemma, and a documented dead end
  for the literal chain-covering-by-window technique.**

## Current best

### Setup (shared with the rest of the population; all cited, not re-derived)
Let $(a_n)_{n\ge1}$ be the greedy sequence: $a_1>1$ fixed, and for $n\ge1$, $a_{n+1}$ is the
smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for every $i=1,\dots,n$. Write
$D_n:=\mathrm{primes}(a_n)$ (the set of primes dividing $a_n$), $S:=D_1=\mathrm{primes}(a_1)$,
$L_0:=\mathrm{rad}(a_1)=\prod_{p\in S}p$, and $P:=\{p\text{ prime}: p\le L_0\}\supseteq S$ (finite).
For $x\in\mathbb Z$ write $\pi(x):=P\cap\mathrm{primes}(x)$.

Cite verbatim (all certified in `results/imo-2026-06/lemmas/`):
- **Gap bound** (`lemmas/gap-bound.md`): $a_{n+1}-a_n\le L_0$ for all $n\ge1$; in particular every
  $D_n$ meets $S$ (hence meets $P$).
- **Constraint Domination** (`lemmas/constraint-domination.md`): for fixed $n$, the system
  $\{\gcd(x,a_i)>1: i=1,\dots,n\}$ is logically equivalent to the sub-system indexed by
  $\mathcal A_n:=\{i\le n: D_i\text{ is inclusion-minimal in }\{D_1,\dots,D_n\}\}$ (the antichain of
  "live generator" indices).
- **Signature stabilization / CRT sufficiency** (`lemmas/signature-stabilization-and-crt-sufficiency.md`),
  applied with this specific $P$: writing $D_n^P:=P\cap D_n$ and $R_n:=\{D_1^P,\dots,D_n^P\}$, there is
  $N_1$ with $R_n=R$ (fixed) for all $n\ge N_1$; and with $L_P:=\prod_{p\in P}p$,
  $G:=\{r\in\mathbb Z/L_P\mathbb Z:\pi(r)\cap D\ne\emptyset\ \forall D\in R\}$, hitting $G$ is
  **sufficient** for validity against all $i\le n$ ($n\ge N_1$); defining
  $y_{n+1}:=\min\{x>a_n : x\bmod L_P\in G\}$ gives $a_{n+1}\le y_{n+1}$ unconditionally.
- **Periodicity given No-Escape** (`lemmas/periodicity-given-no-escape.md`): IF, in addition,
  $a_{n+1}=y_{n+1}$ for all $n\ge N_1$ (No-Escape), THEN there exist $T,L\ge1$ with $a_{n+T}=a_n+L$
  for **every** $n\ge1$ (the full theorem) — proved in full there, mechanical bookkeeping only.

### The new reduction: P-Confinement (PC) $\Rightarrow$ No-Escape $\Rightarrow$ theorem

**Definition (P-Confinement, PC).** Every generator index $i$ (i.e. every $i$ such that $D_i$ is
inclusion-minimal in $\{D_1,\dots,D_j\}$ for the value $j=i$ at which it is first added to the
antichain — equivalently, $i\in\mathcal A_n$ for the antichain computed at any $n\ge i$ for which
$D_i$ has not yet been dominated, and in particular $i\in\mathcal A_i$) satisfies $D_i\subseteq P$.

More precisely and more usefully, we use the following equivalent finite-$n$ formulation, which is
all that is needed below: **for every $n\ge1$ and every $i\in\mathcal A_n$ (the antichain of live
generators at time $n$), $D_i\subseteq P$.** (If $i\in\mathcal A_n$ for some $n$, then in particular
$D_i$ was inclusion-minimal among $\{D_1,\dots,D_i\}$ when it first appeared, since inclusion-
minimality among a smaller list is implied by inclusion-minimality among the initial segment up to
its own index — a superset relation $D_j\subsetneq D_i$ with $j\le i$ would already show $D_i$ non-
minimal at time $i$, hence at every later time too. So the two formulations agree.)

**Claim (Lemma PC$\Rightarrow$Theorem).** If PC holds, the full theorem holds: there exist $T,L\ge1$
with $a_{n+T}=a_n+L$ for every $n\ge1$.

*Proof.* Fix $n\ge N_1$ (the stabilization index from signature stabilization applied to this $P$),
and let $R'_n:=\{D_i : i\in\mathcal A_n\}$ — the *true* (untruncated) prime sets of the live
generators at time $n$; by PC, $R'_n\subseteq 2^P\setminus\{\emptyset\}$.

**Step A ($R'_n$ = the inclusion-minimal elements of $R_n$).** Recall $R_n=\{D_1^P,\dots,D_n^P\}$
where $D_k^P=P\cap D_k$. We show $R'_n=\min(R_n)$ (inclusion-minimal elements of $R_n$ under
$\subseteq$).

  - $R'_n\subseteq R_n$: for $i\in\mathcal A_n$, PC gives $D_i\subseteq P$, so $D_i^P=D_i$; hence
    $D_i=D_i^P\in R_n$ (as $i\le n$).
  - Every element of $R_n$ is a superset (in $2^P$) of some element of $R'_n$: fix $k\le n$. In the
    finite poset $\{D_1,\dots,D_n\}$ under $\subseteq$, every element has some inclusion-minimal
    element below or equal to it (a finite nonempty poset has minimal elements, and one can descend
    from any element to a minimal one by repeatedly replacing by a smaller comparable element — this
    terminates since the poset is finite). So there is $j\le n$ with $D_j\subseteq D_k$ and $D_j$
    inclusion-minimal, i.e. $j\in\mathcal A_n$. By PC, $D_j\subseteq P$, so
    $D_j=D_j\cap P\subseteq D_k\cap P=D_k^P$. Thus $D_k^P\supseteq D_j\in R'_n$.
  - Combining: $R'_n\subseteq R_n$ and $R'_n$ is itself an antichain (distinct elements of
    $\mathcal A_n$ have incomparable $D_i$'s, by definition of inclusion-minimal), while every
    element of $R_n$ is a superset of some element of $R'_n$. Hence $\min(R_n)=R'_n$: no element of
    $R'_n$ can be a proper superset of another $R_n$-element that is itself a superset of an
    $R'_n$-element (that would violate the antichain property of $R'_n$ unless they coincide), and
    every non-$R'_n$ element of $R_n$ properly contains some $R'_n$ element by the previous bullet
    (if it equalled that element it would itself lie in $R'_n$ by the first bullet's converse
    reasoning — concretely, if $D_k^P=D_j$ for $D_j\in R'_n$ then $D_k^P\in R'_n$ trivially).

**Step B ($G$'s defining condition reduces to checking $R'_n$).** By Step A and the elementary fact
that for $x\in\mathbb Z$, "$\pi(x)\cap D\ne\emptyset$ for every $D\in R_n$" holds if and only if it
holds for every $D$ in $\min(R_n)=R'_n$ (necessity: $R'_n\subseteq R_n$; sufficiency: if
$D\in R_n\setminus R'_n$ then $D\supseteq D_j$ for some $D_j\in R'_n$ by Step A, so
$\pi(x)\cap D_j\ne\emptyset\Rightarrow\pi(x)\cap D\ne\emptyset$) — we get, for $n\ge N_1$ (so
$R_n=R$):
$$x\bmod L_P\in G \iff \pi(x)\cap D\ne\emptyset\ \ \forall D\in R \iff \pi(x)\cap D_i\ne\emptyset\ \ \forall i\in\mathcal A_n.$$

**Step C (translate to the true validity condition).** For $i\in\mathcal A_n$, PC gives
$D_i\subseteq P$, so $\pi(x)\cap D_i=\bigl(P\cap\mathrm{primes}(x)\bigr)\cap D_i
=\mathrm{primes}(x)\cap D_i$ (since $D_i\subseteq P$ already). Hence
$\pi(x)\cap D_i\ne\emptyset\iff\mathrm{primes}(x)\cap\mathrm{primes}(a_i)\ne\emptyset\iff\gcd(x,a_i)>1$.
Combining with Step B:
$$x\bmod L_P\in G \iff \gcd(x,a_i)>1\ \text{ for every }i\in\mathcal A_n.$$
By Constraint Domination, the right side is equivalent to $\gcd(x,a_i)>1$ for **every** $i=1,\dots,n$,
i.e. to the true validity condition for $x$ at time $n$. So for $n\ge N_1$:
$$x\bmod L_P\in G \iff x\text{ is a valid candidate for }a_{n+1}.$$

**Step D (No-Escape).** Fix $n\ge N_1$ and any $x$ with $a_n<x<y_{n+1}$. By definition of $y_{n+1}$
as the *smallest* $x>a_n$ with $x\bmod L_P\in G$, $x<y_{n+1}$ forces $x\bmod L_P\notin G$, hence by
Step C, $x$ is not a valid candidate. So no valid candidate lies strictly between $a_n$ and
$y_{n+1}$; combined with the already-established $a_{n+1}\le y_{n+1}$ (from sufficiency, certified)
and the fact that $a_{n+1}$ *is* a valid candidate $>a_n$ (by definition of the sequence), we get
$a_{n+1}=y_{n+1}$. This is exactly the No-Escape hypothesis of `lemmas/periodicity-given-no-escape.md`
for every $n\ge N_1$.

**Conclusion.** By `lemmas/periodicity-given-no-escape.md`, No-Escape (just proved from PC) implies
there exist $T,L\ge1$ with $a_{n+T}=a_n+L$ for every $n\ge1$. $\blacksquare$

### Round 4: scope reduction to odd $a_1$, and three new attempts on PC

**Scope reduction (free, cited not re-derived).** `approaches/absorption-recurrence-even-case.md`
(Status: solved, reviewed and read in full this round) proves: if $2\mid a_1$, then $a_n=a_1+2(n-1)$
for every $n\ge1$ by a direct two-line induction (Lemma A: consecutive integers are coprime; Lemma B:
even persistence), giving the full theorem with $(T,L)=(1,2)$ with **no dependence on PC or on any of
the antichain machinery**. Consequently, for the remainder of this file, **PC only needs to be proved
for $a_1$ odd** — the even case of the whole theorem (and a fortiori of PC, though PC is not even
needed there) is already closed. Everything below assumes $a_1$ odd, i.e. $2\notin S$.

**Attempt 1 ($\nu_n$, the outline's cumulative "primes ever used by a live generator" candidate) —
no new content.** Define, exactly as proposed in round 3's outline,
$\nu_n:=\bigl|\{p\in P: p\in D_i\text{ for some }i\text{ that has been in }\mathcal A_m\text{ for
some }m\le n\}\bigr|$ (cumulative count of primes ever seen inside a live generator's *truncated*
signature, i.e. $p\in D_i^P$ for some generator $i$ observed by time $n$). This is trivially
non-decreasing in $n$ and bounded above by $|P|$, so it is eventually constant — but on inspection
this is not new information: it is *exactly* the content of the already-certified
`lemmas/signature-stabilization-and-crt-sufficiency.md` Lemma A, restated as a scalar rather than as
the underlying set $R=\bigcup_{i\in\text{(eventual generators)}}D_i^P$. (Lemma A shows $R_n$ itself —
the set of $P$-truncated signatures achieved — stabilizes to a fixed $R$ by an index $N_1$; the union
of primes appearing in the elements of $R$ is precisely the eventual value of $\nu_n$.) Knowing $\nu_n$
stabilizes gives a finite palette of primes that appear in *truncated* signatures, but says nothing
about whether the *untruncated* $D_i$ of a newly created generator stays inside that palette — which
is exactly PC. So $\nu_n$'s stabilization is real but **already implied by** Lemma A (cited, not
reproved) and does **not** independently advance PC; it is a repackaging, not new content. This
matches the outline's own prediction ("most likely outcome... equivalent in difficulty to PC itself")
and is recorded here so it is not retried.

**Attempt 2 (Local Congruence Reduction, LCR) — a genuinely new structural fact, isolating exactly
what PC's inductive step must show.**

Suppose (strong induction hypothesis) that PC holds for every generator index $<i$, i.e. every
$j<i$ with $D_j$ inclusion-minimal among $\{D_1,\dots,D_j\}$ has $D_j\subseteq P$. We show:

> **Claim (LCR).** Under this hypothesis, for every integer $x>a_{i-1}$, $x$ is a valid candidate for
> $a_i$ (i.e. $\gcd(x,a_j)>1$ for every $j=1,\dots,i-1$) **if and only if** $x\bmod L_P\in G_{i-1}$,
> where $G_{i-1}:=\{r\in\mathbb Z/L_P\mathbb Z : \pi(r)\cap D_j\ne\emptyset\ \forall\,j\in\mathcal
> A_{i-1}\}$ is built from the *current* (time-$(i-1)$) live generators only. In particular, validity
> of $x$ for $a_i$ depends **only on $x\bmod L_P$**, not on any other prime factor of $x$.

*Proof.* ($\Leftarrow$) If $x\bmod L_P\in G_{i-1}$, then for every $j\in\mathcal A_{i-1}$,
$\pi(x)\cap D_j^P\ne\emptyset$; by the induction hypothesis $D_j\subseteq P$ so $D_j^P=D_j$, giving a
prime $p\in P$ with $p\mid x$ and $p\mid a_j$, i.e. $\gcd(x,a_j)>1$. By Constraint Domination
(`lemmas/constraint-domination.md`), validity against every $j\in\mathcal A_{i-1}$ is equivalent to
validity against every $j=1,\dots,i-1$, so $x$ is a valid candidate.
($\Rightarrow$) If $x$ is a valid candidate, then in particular $\gcd(x,a_j)>1$ for every
$j\in\mathcal A_{i-1}$; by the induction hypothesis $D_j\subseteq P$, so this common prime factor lies
in $D_j=D_j^P$ and also divides $x$, hence lies in $\pi(x)$. So $\pi(x)\cap D_j\ne\emptyset$ for every
$j\in\mathcal A_{i-1}$, i.e. $x\bmod L_P\in G_{i-1}$. $\blacksquare$

**Consequence.** Under the induction hypothesis, $a_i$ is *exactly* the smallest integer $>a_{i-1}$
with $a_i\bmod L_P\in G_{i-1}$ — a purely congruence-defined quantity, with **no freedom at all**: it
is the literal minimum of a fixed, explicit arithmetic condition. PC's inductive step (does this
specific integer avoid all primes $>L_0$?) is therefore **not** a further question about the dynamics
of the sequence or about domination bookkeeping — those are fully resolved by LCR — but a question
purely about the integer $a_i$ *itself*, viewed as "the smallest element of a fixed union of
residue classes mod $L_P$ exceeding $a_{i-1}$."

**Diagnosis of why this resists an elementary finish.** LCR shows PC's remaining content is exactly:
*is the smallest solution $x>a_{i-1}$ of $x\bmod L_P\in G_{i-1}$ always $L_0$-smooth (free of prime
factors $>L_0$)?* This is a **smooth-numbers-in-a-window** question, not a combinatorial antichain
question. Two observations:
- Being in $G_{i-1}$ constrains $x$ only via which primes of $P$ divide $x$ (through $\pi(x)$); it
  places **no constraint whatsoever** on any prime factor of $x$ larger than $L_0$. So a priori, the
  smallest $x>a_{i-1}$ with $x\bmod L_P\in G_{i-1}$ could easily be a product of one qualifying small
  prime and an unrelated large cofactor — nothing in the residue condition forbids this.
- Yet the gap bound (`lemmas/gap-bound.md`) guarantees a *specific* always-valid, always-smooth
  candidate $M\le a_{i-1}+L_0$ (all prime factors in $S\subseteq P$), so $a_i\le M$; the true minimal
  valid $x$ therefore lies in a window of length $\le L_0$ (much shorter than $L_P$, since $L_P$
  typically has extra prime factors beyond $L_0$'s), which somewhat narrows the search — but a window
  of length $L_0$ around a term $a_{i-1}$ that is unboundedly large as $i\to\infty$ still contains,
  generically, plenty of non-$L_0$-smooth integers (smooth numbers have density $\to0$ in long ranges
  by the classical smooth-number estimates, e.g. via the Dickman $\rho$-function), so "the smallest
  valid $x$ happens to be smooth" is **not** something that follows from density/pigeonhole
  considerations alone; if it is true, it must be true for a structural reason specific to how
  $G_{i-1}$ is built (from prime sets that are themselves *unions of previously realized generator
  primes*, which by the induction hypothesis are already confined to $P$), not from a generic
  probabilistic argument, since the naive density heuristic actually points the *wrong* way (would
  predict PC to fail eventually). I could not find or complete such a structural argument in the time
  available. This is a **sharper, more honest statement of the open gap** than "No-Escape" or the raw
  PC statement: LCR shows the gap reduces to a single, precisely-stated question about minimal
  solutions of a residue condition avoiding large prime factors, with the induction hypothesis fully
  absorbed and no combinatorial bookkeeping left to do.

**Attempt 3 (odd-case simplification candidate: "every generator beyond $D_1$ contains the prime
2") — refuted by direct computation.** Motivated by the observation that for several odd $a_1$
(e.g. $15,105,165,1001,1155,5005,15015,255255$), every newly-created generator set past the first
($D_1=S$) happens to contain $2$, I tested whether this holds in general (which would let one restrict
attention to a much smaller sub-lattice $\{D\subseteq P: 2\in D\}\cup\{S\}$ and might make the LCR
question tractable in that restricted setting). **This is false**: for $a_1=21$, the new generator
$D=\{3\}$ appears (from the term $a_3=27$) with no $2$; for $a_1=33$, seven of nine new generators
omit $2$ (e.g. $\{3,13\}$ from $a_3=39$, $\{3,5\}$ from $a_5=45$, up to $\{3\}$ from $a_{17}=81$); for
$a_1=35$, the generator $\{3,5\}$ (from $a_4=45$) omits $2$; for $a_1=385$, the generators
$\{3,7,19\}$ (from $a_5=399$) and $\{3,7,11\}$ (from $a_{38}=693$) omit $2$; for $a_1=7429$, sixteen
of fifty-six new generators omit $2$ (e.g. $\{3,19,131\}$, $\{3,7,19\}$, $\{3,19,137\}$, ...,
$\{3,19\}$). So this simplification does **not** hold in general, and the odd case genuinely requires
handling generators with arbitrary parity, not just an even-augmented sub-lattice. (Verified by direct
simulation of the exact greedy sequence and its inclusion-minimal antichain, independent fresh code
this round.)

### What remains open: PC itself

PC is now the **entire remaining gap** for this reduction. It is a clean, self-contained,
falsifiable statement:

> **P-Confinement (PC).** For every $n\ge1$ and every generator index $i\in\mathcal A_n$ (the
> antichain of inclusion-minimal elements of $\{D_1,\dots,D_n\}$), the *full, untruncated* prime set
> $D_i=\mathrm{primes}(a_i)$ satisfies $D_i\subseteq P=\{\text{primes}\le L_0\}$, i.e. no generator
> ever uses a prime larger than $L_0=\mathrm{rad}(a_1)$.

I verified PC computationally with **zero violations** across 13 values of $a_1$
($15,105,6,210,2310,30030,1001,77,35,1155,385,1309,510510$, giving $\omega(a_1)\in\{1,\dots,7\}$),
tracking the exact (untruncated) antichain over up to 1200 greedy steps each and checking every
generator event's prime set against $P$; none ever included a prime $>L_0$, even though individual
*non-generator* terms routinely do (e.g. for $a_1=15$, $a_{24}=102=2\cdot3\cdot17$ has $17>15=L_0$,
but $\{2,3,17\}\supsetneq\{2,3\}$ or $\{3\}$/$\{2\}$ which have already appeared, so this term is
immediately dominated and is never itself a generator).

I attempted, but could not complete in the time available, a proof of PC by minimal counterexample
(take the first index $n$ at which a new generator $D_n\not\subseteq P$ is created, and try to derive
a contradiction from the minimality of $a_n$ among valid candidates). The natural attempt — show the
"boring" candidate $M$ (next multiple of $L_0$ after $a_{n-1}$, whose own primes are exactly
$S\subseteq P$, always valid by `lemmas/gap-bound.md`) forces $a_n=M$ whenever $a_n\ne M$ would
require an extra large prime — does **not** immediately work, because $a_n<M$ can happen for
reasons unrelated to $M$'s own factorization (there can be a smaller valid $x<M$ whose primes are a
*different* subset of $P$ even without needing any large prime, so "$a_n\ne M$" alone does not force
"$a_n$ needs a large prime"; ruling this out needs control over exactly which subsets of $P$ are
already "covered" by earlier generators at the specific point $n-1$, which is again an instance of
the finite-state stabilization question). So: **PC is a genuine, well-posed open lemma, apparently
of comparable difficulty to Antichain Stabilization** (the target in `antichain-signature-closure`)
— I do not claim it is strictly easier, only that it is a cleaner and more directly *usable* single
target, since (unlike Antichain Stabilization) I have now shown explicitly and rigorously that
granting it closes the **entire** theorem with **zero secondary gap** (no separate charging/counting
argument needed afterward, and no separate necessity-vs-sufficiency check as in the old
`core-signature-pigeonhole` framing).

### Relation to sibling approaches
- This is logically closely related to, but *not identical to*, `antichain-signature-closure`'s
  Antichain Stabilization target: PC is a *pointwise* statement (every generator, at the moment it
  is created, avoids large primes) rather than an *eventual* one (the antichain's generator set
  becomes fixed from some point on). PC is in fact **stronger and would also imply** Antichain
  Stabilization: if PC holds, then $\mathcal A_n$'s true generator sets always lie in the finite
  lattice $2^P\setminus\{\emptyset\}$ (size $2^{|P|}-1$), so the chain $R'_n\subseteq 2^P$ can only
  be refined finitely often (matching `lemmas/signature-stabilization-and-crt-sufficiency.md`
  Lemma A's pigeonhole argument, now applicable because $R'_n=\min(R_n)$ by Step A above, and $R_n$
  itself stabilizes by Lemma A) — giving Antichain Stabilization as a byproduct, for free, once PC is
  known. I do not claim the converse (Antichain Stabilization $\Rightarrow$ PC) and did not attempt
  it; the two targets may or may not be equivalent, but PC is sufficient and is what a future round
  should attempt directly, since it is the more mechanically productive target (Direction "PC
  $\Rightarrow$ theorem" is now fully discharged, unlike the antichain-family approaches' charging
  argument, which the sibling approach `antichain-signature-closure` reports as still unfinished this
  round).
- The chain-covering-by-window mechanism this approach was originally assigned (bounding
  $|\mathcal A_n|$ by $\omega(a_1)$ via a static Dilworth-style cover) is a **documented dead end**:
  see "Approaches tried" above. It is superseded within this same file by the PC reformulation,
  which needs no antichain *size* bound at all — only a *membership* condition on which primes
  generators may use.

### Round 4 update: scope and sharper restatement
Since the even case ($2\mid a_1$) is now fully closed by `absorption-recurrence-even-case.md` without
any use of PC, **PC only needs to be established for odd $a_1$** to finish the theorem in full. Round
4's LCR analysis (above) shows PC's remaining content, restricted to this case, is precisely: *at each
step where a genuinely new inclusion-minimal signature is required, is the smallest integer solving
the resulting explicit congruence condition mod $L_P$ automatically free of prime factors $>L_0$?*
This is a sharper, fully precise restatement of the same open gap — not a new, easier target, and not
yet resolved — but it removes all remaining antichain/domination bookkeeping from the open question,
leaving a single, self-contained number-theoretic question about minimal solutions of a residue
condition (see "Diagnosis of why this resists an elementary finish" above for the precise obstruction:
naive smooth-number density considerations do not resolve it, and the specific structural reason (if
any) why $G_{i-1}$'s particular congruence class always admits a smooth minimal solution was not found
this round).

## Full proof
(Not applicable — Status is `partial`. The theorem is reduced, with a complete and rigorous proof of
sufficiency, to the single open lemma **P-Confinement (PC)** stated above, now known to be needed only
for odd $a_1$ and restated precisely via Local Congruence Reduction (LCR); PC itself is unproved.)

## Promotable lemmas

**Lemma (PC $\Rightarrow$ Theorem).** *Statement:* If P-Confinement holds (every antichain generator's
full prime set is a subset of $P=\{\text{primes}\le\mathrm{rad}(a_1)\}$), then there exist positive
integers $T,L$ with $a_{n+T}=a_n+L$ for every $n\ge1$. *Proof:* given in full above ("The new
reduction: P-Confinement (PC) $\Rightarrow$ No-Escape $\Rightarrow$ theorem", Steps A–D plus the
Conclusion), using only already-certified lemmas (`gap-bound.md`, `constraint-domination.md`,
`signature-stabilization-and-crt-sufficiency.md`, `periodicity-given-no-escape.md`) plus elementary
finite-poset reasoning (existence of minimal elements below any element of a finite poset). This is a
genuinely new, complete, reusable reduction — strictly cleaner than the reduction in
`lemmas/periodicity-given-no-escape.md` alone, because it identifies a *single, checkable, purely
combinatorial* hypothesis (PC) that discharges No-Escape with **no separate argument**, unlike the
prior open formulations (No-Escape relative to $P=\{\text{primes}\le L_0\}$ needed an independent
proof; Antichain Stabilization in `antichain-signature-closure` still needs a further CRT/necessity
step after stabilization is granted — here that step is folded into the single PC hypothesis).
Recommend certifying this to `results/imo-2026-06/lemmas/pc-implies-theorem.md` so any future
approach that manages to prove PC (by whatever technique) can cite this lemma directly to finish the
whole problem with no further work. (Already certified as of round 2/3; unchanged this round.)

**Lemma (Local Congruence Reduction, LCR) — new this round.** *Statement:* Fix $i\ge1$ and suppose
P-Confinement holds for every generator index $<i$ (every $j<i$ with $D_j$ inclusion-minimal among
$\{D_1,\dots,D_j\}$ has $D_j\subseteq P$). Then for every integer $x>a_{i-1}$: $x$ is a valid
candidate for $a_i$ (i.e. $\gcd(x,a_j)>1$ for all $j=1,\dots,i-1$) if and only if $x\bmod L_P\in
G_{i-1}:=\{r\in\mathbb Z/L_P\mathbb Z:\pi(r)\cap D_j\ne\emptyset\ \forall j\in\mathcal A_{i-1}\}$; in
particular validity depends only on $x\bmod L_P$. *Proof:* given in full above ("Attempt 2 (Local
Congruence Reduction...)"), a short two-line argument using only `lemmas/constraint-domination.md` and
the definition of $\pi$, $\pi$ depending on $x\bmod L_P$ by CRT (as in
`lemmas/signature-stabilization-and-crt-sufficiency.md` Lemma B). This is a clean, reusable,
fully-proved local (single-step, not asymptotic) fact — recommend certifying to
`results/imo-2026-06/lemmas/local-congruence-reduction.md`. Its value: it isolates PC's entire
remaining content, under its own induction hypothesis, to a single question about minimal solutions of
an explicit congruence avoiding large prime factors (stated precisely in "Diagnosis of why this
resists an elementary finish" above) — useful to any future approach attempting PC by strong induction
on the generator index, since it removes all antichain/domination bookkeeping from each inductive
step.
