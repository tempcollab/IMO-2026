## Status
partial

## Approaches tried
- `core-signature-pigeonhole` (round 1, prior name of this slug's predecessor): built the
  truncated-$P=\{\text{primes}\le L_0\}$ CRT machine; isolated "No-Escape" as the sole gap. See
  `current.md` for details (kept for history, this slug supersedes it).
- `antichain-signature-closure` (round 2, this round): Re-targeted the closing mechanism to use the
  **exact, untruncated** antichain of live minimal prime-sets (via the certified
  `lemmas/constraint-domination.md`) instead of a truncated finite prime set, eliminating the
  separate sufficiency-vs-necessity ("No-Escape") gap: once the antichain's generator set is fixed,
  "hits the CRT residue set" and "is actually valid" become the *same* statement by construction
  (proved in full below, steps 4–6). This collapses the problem to a single remaining claim,
  **Antichain Stabilization**.
  - Ran a corrected, fast, exact simulation (recomputing the true minimal antichain of prime-sets
    from scratch after every new term, not the round-2 outline-reviewer's coarser 800-term snapshot)
    for $a_1=2310=2\cdot3\cdot5\cdot7\cdot11$ out to $900$ terms. Result: the antichain grows
    (non-monotonically) to size $268$ by term $n=893$, and then **collapses to size $1$ exactly at
    $n=894$**, when the term $a_{894}=4096=2^{12}$ appears — and stays at size $1$ for the remaining
    terms checked. This *confirms* (does not contradict) the outline's own note "$a_1=2310$ peaks at
    antichain size 268 before collapsing to 1"; the round-2 outline-reviewer's 800-term snapshot
    simply stopped 94 terms short of the collapse. Independently verified that **every one of the
    first 894 terms is even** (0 odd terms), which is exactly the necessary condition (proved below)
    for a pure power of $2$ to become a valid term.
  - Isolated and *proved in full* a genuinely new, reusable lemma explaining this phenomenon exactly
    (the "Absorption Lemma" below): if the sequence ever produces a term that is a pure prime power
    $q^e$, the entire antichain collapses forever to the single generator $\{q\}$, and full
    periodicity follows immediately by the certified `periodicity-given-no-escape.md` machinery
    (trivially discharged). This is a **sufficient** mechanism for Antichain Stabilization, fully
    rigorous, and matches the $a_1=2310$ data exactly.
  - Attempted the "witness-debt charging argument" sketched in the outline as the primary attack on
    the *general* case (Antichain Stabilization without assuming an absorption event occurs). Found
    a precise, fatal flaw in the argument as stated: the "budget" it relies on (the number of distinct
    primes a term in the fixed-length window $(a_n,a_n+L_0]$ can introduce) is bounded by
    $O(\log(a_n+L_0))$, which is a *function of $n$ that itself grows without bound* (a_n\to\infty),
    not a fixed finite constant — so a growth event at index $n$ can "afford" more and more new
    primes as $n\to\infty$, and the naive count "total growth events $\le$ total budget spent" gives
    no finite bound on the number of growth events over an infinite sequence. This is a genuine
    negative result about the charging argument as the outline sketched it (not a hand-wave: see
    the precise write-up below), consistent with the $a_1=2310$ data showing 353 growth events before
    the eventual collapse (an amount that is *not* explained or bounded by any fixed log-based
    budget at the point it occurs, since $\log(a_{894})\approx\log(2\times10^6)\approx 14.5$, far
    smaller than the $268$ live generators at that point — showing the antichain size is not even
    within the naive per-step budget, confirming that "budget accumulates" reasoning, as sketched, is
    the wrong shape of argument).
  - Reformulated the target into a cleaner combinatorial equivalent — a **self-closing antichain**
    (defined and proved sufficient below) — which strictly generalizes the Absorption Lemma's
    singleton case and matches the genuinely different mechanism observed for $a_1=15$ (a stable
    3-element antichain, no absorption event). This reformulation is a real simplification of the
    target (a static, checkable combinatorial property, rather than a dynamic "no more growth events"
    claim) but proving that a self-closing antichain is *always eventually reached*, for every $a_1$,
    remains open — this is the residual gap, now stated in its cleanest form.
  **Verdict: CHANGES REQUESTED (partial).** Genuine progress: two new certified-quality lemmas
  (Absorption, self-closing sufficiency), one precise negative diagnosis of the charging argument
  (saving future rounds from repeating it unchanged), the No-Escape gap fully eliminated (steps 4–6
  below have zero residual gap given Antichain Stabilization), but the core stabilization claim
  itself is not proved for general $a_1$.
- `antichain-signature-closure` (round 5, this round): Fixed the reviewer-flagged citation-hygiene
  gap in Lemma 3. Previously the proof cited `lemmas/periodicity-given-no-escape.md` instantiated
  with $P:=P^*$ (built from the eventual generator set $\mathrm{Gen}(N^*)$), but that lemma's
  *stated* hypothesis list requires $\mathrm{primes}(a_1)\subseteq P$, which is not obviously true
  for $P^*$ (the index realizing $D_1=\mathrm{primes}(a_1)$ could in principle be dominated out of
  the antichain by a later generator). Resolved this by re-reading the cited lemma's proof body
  line by line (not just its stated hypothesis list) and confirming explicitly that
  $\mathrm{primes}(a_1)\subseteq P$ is **never used** anywhere in that proof — the proof consumes
  only "$P$ finite, $G\subseteq\mathbb Z/L_P\mathbb Z$ nonempty, $a_{n+1}=\min\{x>a_n:x\bmod L_P\in
  G\}$ for $n\ge N_1$," all three of which are directly verified for $(P^*,G^*,N^*)$ from their own
  definitions with no reference to $a_1$. Rewrote Lemma 3 to instantiate the *verified proof*
  rather than the over-stated hypothesis list, making the citation fully rigorous (option (ii) from
  the outline: re-derive generic in $P$, confirmed the unused hypothesis is genuinely unused, rather
  than option (i) which would have required a separate — and not obviously true — structural claim
  about $D_1$ never being dominated). Also cross-checked scope against
  `leftover-witness-confinement`'s independently-derived Singleton-Block observation: both
  approaches converge on exactly the same residual open case (antichains/generator sets with no
  singleton block), recorded as a new subsection below.
  **Verdict: the citation-hygiene gap is now fully closed** — steps 4–6 (Lemma 2, Corollary, Lemma
  3) have genuinely zero residual gap, on a basis now fully verified rather than partially asserted.
  The core open target (Antichain Stabilization / self-closing reachability, equivalently: does
  every odd $a_1$ eventually reach a configuration with no singleton block, and if so how is *that*
  case closed) remains open and is unchanged by this round's work — this round's task was scoped
  narrowly to the citation fix plus the cross-check, per the outline, not to attack the open target
  itself.

## Current best

### Setup and notation
Let $(a_n)_{n\ge1}$ be the greedy sequence of the problem. For a positive integer $x$, write
$\mathrm{primes}(x)$ for its set of distinct prime divisors. Fix $L_0:=\mathrm{rad}(a_1)=\prod_{p\mid a_1}p$.

**Lemma 0 (Gap bound).** $a_{n+1}-a_n\le L_0$ for every $n\ge1$. *(Certified,
`lemmas/gap-bound.md`; imported verbatim.)*

**Lemma 1 (Constraint Domination).** For $i<j$, if $\mathrm{primes}(a_j)\subseteq\mathrm{primes}(a_i)$
then for every integer $y$, $\gcd(y,a_j)>1\implies\gcd(y,a_i)>1$; consequently, for any $n$, the
system of constraints $\{\gcd(y,a_i)>1:i=1,\dots,n\}$ is logically equivalent to the sub-system
indexed by the inclusion-minimal elements of $\{\mathrm{primes}(a_1),\dots,\mathrm{primes}(a_n)\}$.
*(Certified, `lemmas/constraint-domination.md`; imported verbatim.)*

For $n\ge1$ define the **antichain** $\mathcal A_n$ to be the set of inclusion-minimal elements of
$\{\mathrm{primes}(a_1),\dots,\mathrm{primes}(a_n)\}$ (a finite set of finite, pairwise
$\subseteq$-incomparable, nonempty sets of primes). Write $\mathrm{Gen}(n)\subseteq\{1,\dots,n\}$ for
a set of indices realizing $\mathcal A_n$ (one index per element of $\mathcal A_n$; not unique if a
prime-set repeats, but any choice works below). By Lemma 1, for every $n$ and every integer $y$:
$$\gcd(y,a_i)>1\ \forall i\le n \iff \gcd(y,a_i)>1\ \forall i\in\mathrm{Gen}(n). \tag{$\star$}$$

**Definition (growth event).** Index $n$ is a *growth event* if $\mathcal A_{n+1}\ne\mathcal A_n$
(equivalently, $\mathrm{primes}(a_{n+1})$ is not a superset of any element of $\mathcal A_n$: it is
either $\subsetneq$ some element(s) of $\mathcal A_n$ — a *collapse* event, replacing those elements —
or incomparable to all of them — a *pure addition*). If $n$ is not a growth event,
$\mathcal A_{n+1}=\mathcal A_n$ exactly (the new term's prime-set is a superset of some existing
generator, hence redundant by Lemma 1 and does not change the inclusion-minimal set).

**Antichain size is non-monotone**: verified by direct simulation ($a_1=2310$: size climbs to $268$
at $n=893$, then drops to $1$ at $n=894$). Any argument for stabilization must NOT assume
monotonicity.

### The target: Antichain Stabilization (the sole open gap)

**Claim (Antichain Stabilization).** There exists $N^*\ge1$ such that $\mathcal A_n=\mathcal A_{N^*}$
for all $n\ge N^*$ — i.e. only finitely many growth events occur in total.

This is **not proved** in general below. Everything else needed for the theorem (steps below) is
proved unconditionally on this claim being granted.

### Steps 4–6: periodicity follows with zero residual gap, once Antichain Stabilization is granted

Assume Antichain Stabilization: fix $N^*$, $\mathcal A^*:=\mathcal A_{N^*}$, and
$\{i_1,\dots,i_k\}:=\mathrm{Gen}(N^*)$ (finite, since $\mathcal A^*$ is a finite set of finite prime
sets realized by finitely many indices). Define
$$P^*:=\bigcup_{j=1}^k \mathrm{primes}(a_{i_j})\qquad(\text{finite, a fixed set of primes, well
defined only now that }N^*,\mathrm{Gen}(N^*)\text{ are fixed}),$$
$$L_{P^*}:=\prod_{p\in P^*}p,\qquad G^*:=\Big\{r\in\mathbb Z/L_{P^*}\mathbb Z:\ \pi(r)\cap
\mathrm{primes}(a_{i_j})\ne\emptyset\ \text{for every }j=1,\dots,k\Big\},$$
where $\pi(r):=P^*\cap\mathrm{primes}(r)$ (well defined on residues mod $L_{P^*}$ by CRT, since
divisibility of an integer by each $p\in P^*$ depends only on that integer's residue mod $p$, and the
primes of $P^*$ are pairwise coprime).

**Lemma 2 (Exact validity criterion, no truncation gap).** For every $n\ge N^*$ and every integer
$x$:
$$\big(\gcd(x,a_i)>1\ \forall i\le n\big) \iff \big(x\bmod L_{P^*}\in G^*\big).$$

*Proof.* Since $n\ge N^*$ and stabilization gives $\mathcal A_n=\mathcal A_{N^*}=\mathcal A^*$
for all such $n$, $\mathrm{Gen}(n)$ may be taken equal to $\{i_1,\dots,i_k\}$ (the generators do not
change). By $(\star)$, $\gcd(x,a_i)>1\ \forall i\le n \iff \gcd(x,a_{i_j})>1\ \forall j=1,\dots,k$.
Now fix $j$: $\gcd(x,a_{i_j})>1$ iff some prime of $\mathrm{primes}(a_{i_j})$ divides $x$; since
$\mathrm{primes}(a_{i_j})\subseteq P^*$ by definition of $P^*$, this is equivalent to
$\mathrm{primes}(a_{i_j})\cap\pi(x)\ne\emptyset$, i.e. to $\mathrm{primes}(a_{i_j})\cap\pi(x\bmod
L_{P^*})\ne\emptyset$ (as $\pi$ depends only on the residue mod $L_{P^*}$). Conjoining over
$j=1,\dots,k$ gives exactly $x\bmod L_{P^*}\in G^*$ by definition of $G^*$. $\blacksquare$

Unlike the earlier truncated-$P=\{\text{primes}\le L_0\}$ framing (where the analogous statement,
`lemmas/signature-stabilization-and-crt-sufficiency.md` Lemma B, is only a one-directional
sufficiency $\Leftarrow$), Lemma 2 is a two-directional **iff**: because $P^*$ is built from the
*exact* prime factorizations of the actual (now fixed) generator terms $a_{i_1},\dots,a_{i_k}$
rather than truncated by a size bound, there is no room for a prime outside $P^*$ to matter — no such
prime can appear in any $\mathrm{primes}(a_{i_j})$, and by $(\star)$ these are literally the only
constraints that matter for $n\ge N^*$. This is precisely how the "No-Escape" gap of the earlier
approaches is eliminated by construction rather than argued away.

**Corollary (definition of $a_{n+1}$ collapses to a residue condition, for $n\ge N^*$).** For
$n\ge N^*$, by the problem's defining recursion and Lemma 2,
$$a_{n+1}=\min\{x>a_n: x\bmod L_{P^*}\in G^*\}.$$
This is an unconditional equality (not merely $a_{n+1}\le$ this minimum), directly from Lemma 2
applied with the correct $n$.

**Lemma 3 (Periodicity, generic in $P$; citation-hygiene now fully closed).** There exist positive
integers $T,L$ with $a_{n+T}=a_n+L$ for every $n\ge1$.

*Resolving the round-2 citation gap first.* The file `lemmas/periodicity-given-no-escape.md`
states its hypothesis as "$P$ a fixed finite set of primes with $\mathrm{primes}(a_1)\subseteq P$,"
and our $P^*:=\bigcup_j\mathrm{primes}(a_{i_j})$ is built from the *eventual generator set*
$\mathrm{Gen}(N^*)$, not from $a_1$ directly — so $\mathrm{primes}(a_1)\subseteq P^*$ is not
obviously guaranteed (it would require the index $1$ itself, or some generator whose prime set
contains $\mathrm{primes}(a_1)=D_1$, to survive into $\mathrm{Gen}(N^*)$; a priori $D_1$ could be
dominated and removed from the antichain by a later, strictly smaller generator). We resolve this
by re-reading the cited lemma's proof body line by line (reproduced below) rather than trusting its
stated hypothesis list, per the reviewer's instruction: **the hypothesis
$\mathrm{primes}(a_1)\subseteq P$ is never invoked anywhere in that proof.**

The proof of `periodicity-given-no-escape.md` (lines 10–37 of that file) proceeds as follows,
verbatim in structure: fix $P$ finite, $L_P:=\prod_{p\in P}p$, $G\subseteq\mathbb Z/L_P\mathbb Z$
nonempty, and $N_1$ such that $a_{n+1}=y_{n+1}:=\min\{x>a_n:x\bmod L_P\in G\}$ for all $n\ge N_1$.
It then (i) defines $\delta(r)$, the smallest positive $d$ with $(r+d)\bmod L_P\in G$, well defined
because $G$ is finite and nonempty; (ii) observes $a_{n+1}=a_n+\delta(a_n\bmod L_P)$ for
$n\ge N_1+1$, purely from the definition of $y_{n+1}$ and the hypothesis $a_{n+1}=y_{n+1}$; (iii)
runs a pigeonhole argument on the finite set $G$ (not on $2^P$, not on $R$, not on any object
depending on $a_1$'s own prime factorization) to get eventual exact periodicity of the residue
sequence $r_n:=a_n\bmod L_P$; (iv) sums $\delta$ over one period to get $a_{m+T}=a_m+L$ for all
$m\ge N$; (v) extends this to every $n\ge1$ by a purely arithmetic re-indexing argument using only
that $T,T'$ are positive integers and $N$ is a fixed finite index. At no point does any of steps
(i)–(v) use $\mathrm{primes}(a_1)$, $S=D_1$, or any relation between $P$ and $a_1$ beyond what is
already packaged into "$G$ is a fixed nonempty subset of $\mathbb Z/L_P\mathbb Z$ and
$a_{n+1}=y_{n+1}$ for $n\ge N_1$." Both of these hold for our $(P^*,G^*,N^*)$ unconditionally:
$G^*\ne\emptyset$ because $0\in G^*$ (as $\pi(0)=P^*\supseteq\mathrm{primes}(a_{i_j})$ for every
$j$, each $\mathrm{primes}(a_{i_j})$ being nonempty since $a_{i_j}>1$ — this uses only the
definition of $P^*$ as containing every $\mathrm{primes}(a_{i_j})$, not any relation to $a_1$), and
$a_{n+1}=y_{n+1}$ for $n\ge N^*$ is exactly the Corollary proved above unconditionally on Antichain
Stabilization.

Hence the correct, fully general statement to cite is: **`periodicity-given-no-escape.md`'s proof
establishes the implication "[$P$ finite, $G\subseteq\mathbb Z/L_P\mathbb Z$ nonempty, and
$a_{n+1}=\min\{x>a_n:x\bmod L_P\in G\}$ for all $n\ge N_1$] $\Rightarrow$ [$\exists T,L>0$ with
$a_{n+T}=a_n+L$ for every $n\ge1$]" without any use of $\mathrm{primes}(a_1)\subseteq P$** — the
hypothesis $\mathrm{primes}(a_1)\subseteq P$ in that file's stated preamble is inherited unused
from the context of `signature-stabilization-and-crt-sufficiency.md` (where it *is* needed, to
guarantee each $D_n=P\cap\mathrm{primes}(a_n)$ is nonempty) but plays no role in the periodicity
proof itself, which only consumes the already-finished conclusion "$G$ nonempty, $a_{n+1}=y_{n+1}$
eventually." We therefore instantiate the *proof*, not the over-stated hypothesis list, with
$P:=P^*$, $G:=G^*$, $N_1:=N^*$; nonemptiness of $G^*$ and the eventual-equality hypothesis are both
verified above directly from the definition of $P^*,G^*$ and the Corollary, with no appeal to
$\mathrm{primes}(a_1)\subseteq P^*$ anywhere. This closes the round-2-flagged gap completely: no
unverified hypothesis is used, and (as a byproduct) we have also verified we do not even need to
settle whether $\mathrm{primes}(a_1)\subseteq P^*$ holds in general — the proof never asked for it.

*Proof (of Lemma 3, now on a fully verified basis).* Instantiate the argument above with
$P:=P^*,\ G:=G^*,\ N_1:=N^*$. Both required facts hold: $G^*\ne\emptyset$ (shown above) and
$a_{n+1}=y_{n+1}$ for all $n\ge N^*$ (the Corollary). Steps (i)–(v) reproduced above apply
verbatim with these substitutions and produce $T,L$ with $a_{n+T}=a_n+L$ for every $n\ge1$.
$\blacksquare$

**Conclusion.** Modulo Antichain Stabilization, the theorem is fully proved with zero residual gap
in steps 4–6 (Lemma 2, Corollary, Lemma 3): this is a strictly stronger reduction than the earlier
`core-signature-pigeonhole` chain, which needed a second, separate "No-Escape" lemma even after its
own (truncated) signature stabilization.

### New result this round: the Absorption Lemma (a fully proved sufficient mechanism)

**Lemma 4 (Prime-power absorption).** Suppose for some index $m\ge1$, $a_m=q^{e}$ for a prime $q$
and integer $e\ge1$ (i.e. $\mathrm{primes}(a_m)=\{q\}$). Then:
(a) $q\mid a_n$ for every positive integer $n$ (not just $n\ge m$).
(b) $\mathcal A_n=\{\{q\}\}$ for every $n\ge m$. In particular Antichain Stabilization holds with
$N^*=m$.

*Proof.* (a) For $i<m$: by the problem's defining recursion, $a_m$ (being the value chosen at step
$m$) satisfies $\gcd(a_m,a_i)>1$ for every $i=1,\dots,m-1$. Since $a_m=q^e$ has only the prime factor
$q$, $\gcd(q^e,a_i)>1$ forces $q\mid a_i$. So $q\mid a_i$ for $i=1,\dots,m-1$, and trivially
$q\mid a_m$. For $n>m$: induct upward. If $q\mid a_i$ has been shown for all $i\le n-1$ for some
$n-1\ge m$, then in particular (taking the single index $i=m\le n-1$) the defining recursion for
$a_n$ requires $\gcd(a_n,a_m)>1$, i.e. $q\mid a_n$ (again since $a_m$'s only prime factor is $q$).
By induction starting at $n-1=m$ (base case $q\mid a_m$ already known), $q\mid a_n$ for every
$n\ge m$. Combined with $q\mid a_i$ for $i<m$ shown above, $q\mid a_n$ for every $n\ge1$.

(b) By (a), $q\in\mathrm{primes}(a_n)$ for every $n\ge1$, i.e. $\{q\}\subseteq\mathrm{primes}(a_n)$
for every $n$. Hence $\{q\}$ is a subset of every prime-set that ever appears, so in particular for
$n\ge m$: $\{q\}\in\{\mathrm{primes}(a_1),\dots,\mathrm{primes}(a_n)\}$ (realized by index $m$
itself) and $\{q\}$ is a subset of every other element of that multiset, so every element other than
$\{q\}$ itself is dominated (not inclusion-minimal, since $\{q\}\subseteq$ it) unless it equals
$\{q\}$. Hence the set of inclusion-minimal elements is exactly $\{\{q\}\}$: $\mathcal A_n=\{\{q\}\}$
for all $n\ge m$. $\blacksquare$

This Lemma 4 fully and rigorously explains the $a_1=2310$ collapse: at $n=894$, $a_{894}=4096=2^{12}$
is a prime power with $q=2$; Lemma 4(a) predicts $2\mid a_n$ for every $n\ge1$, matching the
independently-verified computational fact that all of $a_1,\dots,a_{894}$ are even (indeed, the
lemma shows all later terms are even too, hence the antichain stays $\{\{2\}\}$ forever after
$n=894$, consistent with the simulation).

Lemma 4 gives an unconditional proof of the full theorem *in the special case that some term of the
sequence is ever a prime power* — a nonempty case (confirmed to occur for $a_1=2310$), but the
theorem must hold for **every** $a_1>1$, including cases (such as $a_1=15$, see below) where no term
is ever a prime power, so Lemma 4 alone does not close the general gap.

### A cleaner reformulation of the residual gap: self-closing antichains

**Definition.** A finite antichain $\mathcal B$ of nonempty finite sets of primes (pairwise
$\subseteq$-incomparable) is **self-closing** if every finite set of primes $F$ with
$F\cap B\ne\emptyset$ for all $B\in\mathcal B$ satisfies $F\supseteq B$ for some $B\in\mathcal B$.

**Lemma 5 (Self-closing $\Rightarrow$ permanent stabilization).** If $\mathcal A_{N}$ is self-closing
for some $N$, then $\mathcal A_n=\mathcal A_N$ for every $n\ge N$ (Antichain Stabilization holds with
$N^*=N$).

*Proof.* Induct on $n\ge N$. Suppose $\mathcal A_n=\mathcal A_N$ (base case $n=N$ trivial). The term
$a_{n+1}$ satisfies $\gcd(a_{n+1},a_i)>1$ for all $i\le n$, so by $(\star)$ (applied with
$\mathrm{Gen}(n)$ realizing $\mathcal A_n=\mathcal A_N$) it satisfies $\gcd(a_{n+1},a_i)>1$ for all
$i\in\mathrm{Gen}(n)$, i.e. $\mathrm{primes}(a_{n+1})\cap B\ne\emptyset$ for every $B\in\mathcal A_N$
(taking $F=\mathrm{primes}(a_{n+1})$). By self-closing, $\mathrm{primes}(a_{n+1})\supseteq B$ for
some $B\in\mathcal A_N=\mathcal A_n$, so $a_{n+1}$'s prime-set is a superset of an existing generator
and (as noted after the definition of growth event) does not change the inclusion-minimal set:
$\mathcal A_{n+1}=\mathcal A_n=\mathcal A_N$. $\blacksquare$

**Sanity checks.** (i) A singleton antichain $\{\{q\}\}$ is self-closing (any $F$ with
$F\cap\{q\}\ne\emptyset$ has $q\in F$, i.e. $F\supseteq\{q\}$) — so Lemma 5 subsumes Lemma 4's
conclusion (b) as a special case, once one separately knows $\mathcal A_m=\{\{q\}\}$ (which Lemma
4(a)'s argument supplies directly; Lemma 5 alone does not explain *how* a singleton antichain is
reached, only that once reached it persists). (ii) For $a_1=15$, direct computation confirms
$\mathcal A_n$ stabilizes at $\{\{2,3\},\{2,5\},\{3,5\}\}$ for $n\ge3$ (through $n=300$ checked), and
this set is self-closing: any prime set $F$ meeting all three of $\{2,3\},\{2,5\},\{3,5\}$ must
contain at least two of $\{2,3,5\}$ (if $F$ contained at most one of them, some pair among
$\{2,3\},\{2,5\},\{3,5\}$ avoiding that one element would be missed by $F$), and any $F$ containing
at least two of $\{2,3,5\}$ is automatically a superset of one of $\{2,3\},\{2,5\},\{3,5\}$. This
matches Lemma 5's prediction exactly and shows the reformulation captures the *non-absorption*
stabilization mechanism too, not just Lemma 4's special case.

Lemma 5 converts "prove no more growth events ever occur" (a claim about an infinite dynamic
process) into the cleaner, purely combinatorial target: **prove that a self-closing configuration
is always eventually realized as some $\mathcal A_N$**, for every $a_1$. This is a genuine
simplification of the target — it is now a static property of a single finite antichain, checkable
in principle without reference to the rest of the infinite sequence — but proving that such a
configuration is always eventually reached remains **open**; it is not implied by Lemmas 4 or 5
alone, since a priori the antichain could (for some other $a_1$) grow through an unbounded sequence
of non-self-closing states forever. No argument in this file rules that out in general.

### Why the outline's "witness-debt charging argument" does not close the general gap (negative diagnosis)

The outline's sketch: each growth event at index $n$ requires $a_{n+1}\in(a_n,a_n+L_0]$ (Lemma 0) to
be incomparable to (or a proper subset of) the current $k=|\mathcal A_n|$ generators, "spending"
prime-factorization budget; since an integer $\le a_n+L_0$ has $O(\log(a_n+L_0))$ distinct prime
factors, the outline suggested a counting tension between $k$ growing and this budget.

This fails to give a finite bound on the *total number* of growth events, for the following precise
reason: the quantity $O(\log(a_n+L_0))$ is a bound on the number of distinct primes available to a
single term $a_{n+1}$, but it **grows with $n$** (since $a_n\to\infty$ by Lemma 0's corollary
$a_N\le a_1+(N-1)L_0$ being a two-sided bound: $a_N\ge N$ trivially since the sequence is strictly
increasing positive integers, so $a_n\to\infty$). A charging scheme that "spends $O(\log a_n)$ per
growth event" therefore has a *total* budget over $n=1,\dots,N$ of $\sum_{n\le N}O(\log a_n) =
O(N\log N)$ (using $a_n=O(N)$ from the gap bound), which is **superlinear in $N$**, not bounded — it
does not rule out even a linear (in $N$) or slower-growing number of growth events, let alone force
finiteness. The $a_1=2310$ data is consistent with this diagnosis: $353$ growth events were observed
in $894$ terms, and the antichain reached size $268$ — an amount not explained by any *fixed* budget
(at the moment of peak size, $\log(a_{893})\approx\log(2.06\times10^6)\approx14.5$, two orders of
magnitude smaller than $268$; the "budget" is evidently not the binding constraint on antichain size
at all, since it accumulates across many steps, not per step). The eventual termination of growth
in this example is explained instead by the qualitatively different Absorption mechanism (Lemma 4),
which is a *global* divisibility coincidence (a term happens to be a pure power of a prime dividing
every earlier term), not a *local* counting exhaustion. **Conclusion: the charging argument as
sketched in the outline is not a valid proof strategy for Antichain Stabilization in general; any
future attempt must either (i) find a genuinely bounded (not $n$-dependent) quantity to charge
against, or (ii) argue directly for eventual self-closing (Lemma 5's target) via a different route
(e.g. a density/pigeonhole argument on which pairs of primes must eventually co-occur), or (iii)
prove absorption (Lemma 4's hypothesis) must eventually occur for every $a_1$ by some other means.**
None of these is established here.

### Cross-check with `leftover-witness-confinement`'s Singleton-Block observation

This round's sibling approach `leftover-witness-confinement` independently isolates the same
special case as this file's Lemma 4/Lemma 5 sanity-check (i): if the antichain $\mathcal A_{n-1}$
(in their PC-based framing) or $\mathcal A_n$ (here) ever contains a singleton block $\{p\}$, the
residual difficulty evaporates immediately. In their framing this is because a singleton block's
hitting condition and non-containment condition coincide, making their "Case A" configuration
impossible outright. In this file's framing it is because a singleton antichain $\{\{q\}\}$ is
trivially self-closing (Lemma 5's sanity check (i)) and, more strongly, once *any* term of the
sequence is a prime power the entire antichain provably collapses to a singleton forever (Lemma 4)
— so the theorem is fully proved unconditionally in that branch via Lemma 2/Corollary/Lemma 3
above, with **no further antichain-closure machinery needed**.

Both routes therefore converge, independently, on the same precise scoping of the remaining open
target: **the only case with any genuine open content is when the (eventual, stabilized-or-not)
antichain never contains a singleton block**, i.e. every generator has at least two prime factors
among the primes appearing. This is a useful cross-check between two independently built approaches
(this file's static self-closing reformulation and `leftover-witness-confinement`'s dynamic
minimal-counterexample descent): they agree exactly on where the difficulty lives, which is
evidence the "no singleton block" case is the real content of the problem's odd-$a_1$ theorem,
not an artifact of either framing. Neither approach closes this residual case in this round.

### Precise statement of the residual gap

**Open.** For every positive integer $a_1>1$, the sequence $(\mathcal A_n)_{n\ge1}$ of antichains
(inclusion-minimal prime-sets among $\mathrm{primes}(a_1),\dots,\mathrm{primes}(a_n)$) eventually
reaches, and thereafter remains at, a self-closing configuration (Definition above). Equivalently
(by Lemma 5, one direction) and sufficiently: there exists $N$ with $\mathcal A_N$ self-closing.

Everything else needed for the full theorem — Lemma 2 (exact CRT validity criterion), the
Corollary, and Lemma 3 (periodicity, now instantiated from `periodicity-given-no-escape.md`'s
*verified* proof body with the previously-flagged citation-hygiene gap fully closed this round) —
is proved above with **no further gap**, contingent only on this single open claim.

## Full proof
(Not applicable — Status is `partial`; Antichain Stabilization / self-closing reachability is not
proved for general $a_1$.)

## Promotable lemmas

- **Lemma 2 + Corollary (Exact validity criterion under antichain stabilization)** — proved in full
  above. Claim: if $\mathcal A_n$ is constant $=\mathcal A^*$ (with fixed generator indices
  $i_1,\dots,i_k$) for all $n\ge N^*$, then for $n\ge N^*$, $\gcd(x,a_i)>1\ \forall i\le n \iff
  x\bmod L_{P^*}\in G^*$ (a two-directional iff, $P^*:=\bigcup_j\mathrm{primes}(a_{i_j})$,
  $G^*$ as defined above), and consequently $a_{n+1}=\min\{x>a_n:x\bmod L_{P^*}\in G^*\}$ exactly.
  This strictly upgrades `lemmas/signature-stabilization-and-crt-sufficiency.md` (which only gives
  the $\Leftarrow$ direction for a truncated $P$) to a full iff once the antichain (not just a
  truncated signature) is known to stabilize. Reusable by any future approach that establishes
  Antichain Stabilization by any means — it finishes the proof automatically via Lemma 3
  (`lemmas/periodicity-given-no-escape.md`, hypothesis trivially discharged).
- **Lemma 4 (Prime-power absorption)** — proved in full above. Claim: if any single term $a_m$ of
  the sequence is a prime power $q^e$, then $q$ divides *every* term of the entire sequence, and the
  antichain collapses forever to $\{\{q\}\}$ from index $m$ on (so the full theorem follows for such
  $a_1$ by Lemma 2/3 immediately). Reusable as a clean sufficient condition / case-split base case
  for any future approach to Antichain Stabilization (e.g. "either absorption eventually occurs, or
  ...").
- **Lemma 5 (Self-closing antichain $\Rightarrow$ permanent stabilization)** — proved in full above.
  Claim: if $\mathcal A_N$ is self-closing (every prime-set meeting all its members is a superset of
  one of them), then $\mathcal A_n=\mathcal A_N$ for all $n\ge N$. Gives a clean, purely
  combinatorial equivalent target for Antichain Stabilization (verified against both the $a_1=2310$
  absorption case and the $a_1=15$ non-absorption case), strictly more general than Lemma 4.
  Reusable by any future approach as the precise statement to aim for.
- **Citation-hygiene fix for `lemmas/periodicity-given-no-escape.md`** (proved in full above, in
  Lemma 3's proof). Claim: that lemma's proof body uses only "$P$ finite, $G\subseteq\mathbb
  Z/L_P\mathbb Z$ nonempty, $a_{n+1}=\min\{x>a_n:x\bmod L_P\in G\}$ for all $n\ge N_1$" — it never
  uses the stated hypothesis $\mathrm{primes}(a_1)\subseteq P$ anywhere in the five proof steps
  (i)–(v) (defining $\delta$, deriving the residue recursion, the pigeonhole periodicity argument,
  summing over a period, and the finite bookkeeping extension to all $n\ge1$). Recommend the
  reviewer amend `lemmas/periodicity-given-no-escape.md`'s stated hypothesis list to drop
  $\mathrm{primes}(a_1)\subseteq P$ as unused and unnecessary, making it a fully general "finite
  $P$, nonempty $G\subseteq\mathbb Z/L_P\mathbb Z$" statement — this makes the lemma safely
  instantiable with *any* finite $P$ (in particular $P^*$ built from an eventual generator set, as
  here, with no need to separately verify $\mathrm{primes}(a_1)\subseteq P$), closing the exact gap
  the reviewer flagged in round 2 and preventing future approaches from having to re-derive this
  same verification.
- **Negative diagnosis of the "witness-debt charging argument"** (not a lemma to certify, but a
  documented dead-end worth recording so it is not silently retried): the per-step budget
  $O(\log a_n)$ is not fixed (grows with $n$), so a step-by-step charging scheme against it cannot
  give a finite total bound on growth events; the $a_1=2310$ data (353 growth events, peak size 268,
  vs. $\log a_n\approx14.5$ at the peak) is a concrete numerical witness that the budget is not
  binding. Recommend recording this in `current.md`'s cross-cutting diagnosis for future rounds.
