## Status
partial

## Approaches tried
- **This round (new slug), global counting/density architecture (proof-by-contradiction on
  non-stabilization, not local minimal-counterexample induction) as dispatched.** Result: (1) a fully
  rigorous, **new** reduction ("$P'$-enlargement Master Lemma", below) showing Antichain Stabilization
  *alone* (no separate P-Confinement hypothesis) already implies the full theorem, with a clean,
  gap-free citation of `lemmas/periodicity-given-no-escape.md` (this incidentally repairs, via a
  different and more careful route, the citation-hygiene gap the reviewer flagged in
  `antichain-signature-closure.md` — see remark below); (2) a full, rigorous decomposition of "growth
  events" (indices where the antichain genuinely changes) into a **Type A** part that is provably
  finite (bounded, elementary pigeonhole, no gap) and a **Type B** (residual, PC-violating) part; (3)
  an attempted global smooth-number-density argument to bound Type B, which is proved **not to close**,
  with the precise mathematical reason identified and proved (Proposition 5 below: the property that
  makes a term "Type-B-eligible" — having a prime factor $>L_0$ — has density $\to 1$ among all
  integers, not density $\to 0$, so it is not a scarce resource and no counting-mismatch contradiction
  of the smooth/non-smooth shape can bound the number of such events). This is an honest, complete
  negative result for the specific mechanism dispatched, not a proof of Type B's finiteness. **Verdict
  (self-assessed): the reduction (1)+(2) is genuine new content and is promotable; the "central open
  task" (Type B finiteness) is NOT closed, and I show precisely why the proposed tool cannot close it.**

## Current best

### 0. Setup and imported notation
Fix $a_1$ odd (the even case is closed elsewhere; per `current.md` this is the entire remaining
content). Let $(a_n)_{n\ge1}$ be the greedy sequence, $S:=\mathrm{primes}(a_1)$,
$L_0:=\mathrm{rad}(a_1)=\prod_{p\in S}p$, $D_i:=\mathrm{primes}(a_i)$, and $P:=\{p\text{ prime}:p\le
L_0\}\supseteq S$ (finite). Import as certified:
- **Gap bound** (`lemmas/gap-bound.md`): $a_{n+1}-a_n\le L_0$, hence $a_N\le a_1+(N-1)L_0$.
- **Constraint Domination** (`lemmas/constraint-domination.md`): if $D_i\subseteq D_j$ ($i\ne j$),
  the constraint from index $j$ is redundant given the one from $i$.
- **Signature Stabilization, Lemma A** (`lemmas/signature-stabilization-and-crt-sufficiency.md`),
  stated *generically*: for **any** fixed finite prime set $P_0\supseteq S$, writing
  $D_i^{P_0}:=P_0\cap D_i$ and $R_n^{P_0}:=\{D_1^{P_0},\dots,D_n^{P_0}\}\subseteq
  2^{P_0}\setminus\{\emptyset\}$, the chain $(R_n^{P_0})_n$ is non-decreasing and stabilizes at some
  index $N_1(P_0)\le 2^{|P_0|}-1$.
- **Lemma B** (same file), generic in $P_0$: sufficiency of $x\bmod L_{P_0}\in G_{P_0}$ for validity,
  once $R_n^{P_0}$ has stabilized, where $L_{P_0}:=\prod_{p\in P_0}p$.
- **Periodicity given No-Escape** (`lemmas/periodicity-given-no-escape.md`), generic in any fixed
  finite $P_0\supseteq S$: No-Escape relative to $P_0$ (defined below) implies the theorem.

**Definition (antichain).** For $n\ge1$, let $\mathcal A_n$ denote the set of inclusion-minimal
elements of $\{D_1,\dots,D_n\}$ (a set of distinct prime-sets, i.e. duplicated values of $D_i$ collapse
to one element; this matches `lemmas/self-closing-antichain-sufficiency.md`'s usage). **Antichain
Stabilization** means: $\exists N^*$ such that $\mathcal A_n=\mathcal A_{N^*}$ for all $n\ge N^*$.

### 1. Growth-event characterization (new, fully proved, elementary)

**Definition.** For $n\ge2$, call $n$ a **growth event** if no $i<n$ satisfies $D_i\subseteq D_n$
(equivalently: $D_n$ is inclusion-minimal in $\{D_1,\dots,D_n\}$).

**Lemma 1 (Growth-Event Update).** For $n\ge2$:
(a) If $n$ is **not** a growth event (some $i<n$ has $D_i\subseteq D_n$), then $\mathcal
A_n=\mathcal A_{n-1}$.
(b) If $n$ **is** a growth event, then $D_n\notin\mathcal A_{n-1}$, and
$$\mathcal A_n=\big(\mathcal A_{n-1}\setminus\{B\in\mathcal A_{n-1}:D_n\subsetneq B\}\big)\cup\{D_n\},$$
in particular $\mathcal A_n\ne\mathcal A_{n-1}$.

*Proof.* Write $E:=\{D_1,\dots,D_{n-1}\}$, $E':=E\cup\{D_n\}$ (as sets of sets; duplicates collapse),
so $\mathcal A_{n-1}=\min(E)$, $\mathcal A_n=\min(E')$ (inclusion-minimal elements).

(a) Some $i<n$ has $D_i\subseteq D_n$, so $D_i\in E$ witnesses that $D_n$ is not inclusion-minimal in
$E'$ (if $D_i\subsetneq D_n$) or $D_n$ already equals an element of $E$ (if $D_i=D_n$); either way
$D_n\notin\min(E')\setminus\min(E)$, and adding a non-minimal (or already-present) element to a
finite poset does not change its set of minimal elements: for $x\in E$, minimality of $x$ in $E$
depends only on whether some $y\in E$, $y\ne x$, has $y\subseteq x$; this is unaffected by adjoining
$D_n$ unless $D_n\subseteq x$ for some $x$ that was minimal in $E$ — but if $D_n\subsetneq x$ for
minimal $x\in E$, then since $D_i\subseteq D_n\subsetneq x$ with $D_i\in E$, $x$ was already not
minimal in $E$ (contradiction), and if $D_n=x$ then $x\in E$ already so adjoining changes nothing. So
$\min(E')=\min(E)$, i.e. $\mathcal A_n=\mathcal A_{n-1}$.

(b) No $i<n$ has $D_i\subseteq D_n$; in particular $D_n\ne D_i$ for all $i<n$ (else $D_i=D_n\subseteq
D_n$), so $D_n\notin E\supseteq\mathcal A_{n-1}$. Also $D_n$ is minimal in $E'$ (nothing in $E$ is
$\subseteq D_n$, and $D_n\not\subsetneq D_n$). For $x\in E$: $x$ remains minimal in $E'$ iff no
element of $E'$ is a proper subset of $x$; the only new candidate is $D_n$, so $x$ stays minimal iff
$x$ was minimal in $E$ (unaffected by non-comparable or non-existent relations to other $E$-elements)
**and** $D_n\not\subsetneq x$. Conversely if $x\in E$ was minimal in $E$ and $D_n\not\subsetneq x$, it
remains minimal in $E'$. Any $x\in E$ not minimal in $E$ stays non-minimal in $E'$ (a witness in $E$
persists). Hence $\min(E')=(\min(E)\setminus\{x\in\min(E):D_n\subsetneq x\})\cup\{D_n\}$, i.e. the
claimed formula, and since $D_n\notin\mathcal A_{n-1}$ but $D_n\in\mathcal A_n$, $\mathcal
A_n\ne\mathcal A_{n-1}$. $\blacksquare$

**Corollary 1 (Stabilization $\Leftrightarrow$ finitely many growth events).** Antichain
Stabilization holds if and only if only finitely many $n\ge2$ are growth events.

*Proof.* ($\Leftarrow$) If growth events are finite, let $N^*$ be $1$ more than the largest one (or
$N^*=1$ if none); for $n>N^*$, $n$ is not a growth event so by Lemma 1(a) $\mathcal A_n=\mathcal
A_{n-1}$, giving $\mathcal A_n=\mathcal A_{N^*}$ for all $n\ge N^*$. ($\Rightarrow$) If $\mathcal
A_n=\mathcal A_{N^*}$ for all $n\ge N^*$, then for every $n>N^*$, $n$ is not a growth event (else
Lemma 1(b) would force $\mathcal A_n\ne\mathcal A_{n-1}$, contradicting both equal $\mathcal
A_{N^*}$), so growth events are confined to $\{2,\dots,N^*\}$, finite. $\blacksquare$

This gives a clean, self-contained restatement of the target with no reference to "self-closing": **it
suffices to show only finitely many $n$ are growth events.**

### 2. Master Lemma: Antichain Stabilization alone implies the theorem (new, fully proved)

This closes a gap wider than the one flagged for `antichain-signature-closure.md` (that file needed,
and did not fully verify, $P^*\supseteq S$ for a $P^*$ built from the eventual generators). Here we
build the enlarged prime set explicitly so the containment is automatic.

**Master Lemma.** If Antichain Stabilization holds (with witness $N^*$, $\mathcal A_n=\mathcal
A_{N^*}=:\mathcal A^\infty$ for $n\ge N^*$, a finite antichain), then there exist $T,L\ge1$ with
$a_{n+T}=a_n+L$ for all $n\ge1$.

*Proof.* Let $P':=P\cup\bigcup_{B\in\mathcal A^\infty}B$. This is finite: $P$ is finite, $\mathcal
A^\infty$ is a finite set of finite sets (each $B\in\mathcal A^\infty$ equals some $D_i$, a finite set
of primes dividing $a_i$), so the union is finite. Also $P'\supseteq P\supseteq S$.

Apply Lemma A/B (Signature Stabilization/CRT, generic form, §0) with $P_0=P'$: get $N_1'\le
2^{|P'|}-1$ and fixed $R'\subseteq2^{P'}\setminus\{\emptyset\}$ with $R_n^{P'}=R'$ for all $n\ge N_1'$,
and $G'\subseteq\mathbb Z/L_{P'}\mathbb Z$ with: for $n\ge N_1'$, $x\bmod L_{P'}\in G'\Rightarrow x$
valid (satisfies $\gcd(x,a_i)>1$ for all $i\le n$), and $y_{n+1}:=\min\{x>a_n:x\bmod L_{P'}\in
G'\}$ satisfies $a_{n+1}\le y_{n+1}$.

Let $N^{**}:=\max(N^*,N_1')$. **Claim (generalized PC relative to $P'$, for $n\ge N^{**}$):** every
$B\in\mathcal A_n$ satisfies $B\subseteq P'$. Indeed for $n\ge N^{**}\ge N^*$, $\mathcal
A_n=\mathcal A^\infty$, and every $B\in\mathcal A^\infty$ satisfies $B\subseteq\bigcup_{B'\in\mathcal
A^\infty}B'\subseteq P'$ by construction of $P'$.

Now repeat Steps A–D of `lemmas/pc-implies-theorem.md` verbatim with $P$ replaced by $P'$ and
$N_1$ replaced by $N^{**}$ (the proof there is generic in the finite prime set once PC holds
relative to it and $N_1'$-stabilization holds relative to it — both hold here for $n\ge N^{**}$):

- **Step A** ($R_n'^{P'}=\min(R_n^{P'})$ realized exactly by $\mathcal A_n$ for $n\ge N^{**}$): since
  $\mathcal A_n\subseteq2^{P'}\setminus\{\emptyset\}$ (Claim above) is precisely the inclusion-minimal
  elements of $\{D_1,\dots,D_n\}$, and truncation by $P'$ fixes every $B\in\mathcal A_n$ pointwise
  ($B\cap P'=B$ since $B\subseteq P'$), the same finite-poset argument as in `pc-implies-theorem.md`
  gives $\mathcal A_n=\min(R_n^{P'})$ as subsets of $P'$.
- **Step B**: for $n\ge N^{**}$ (so $R_n^{P'}=R'$), $x\bmod L_{P'}\in G'\iff\pi'(x)\cap B\ne\emptyset\
  \forall B\in\mathcal A_n$ (where $\pi'(x):=P'\cap\mathrm{primes}(x)$), by the same
  minimal-elements-suffice argument.
- **Step C**: for $B\in\mathcal A_n$, $B\subseteq P'$ gives $\pi'(x)\cap B=\mathrm{primes}(x)\cap B$,
  so $\pi'(x)\cap B\ne\emptyset\iff\gcd(x,a_i)>1$ for the (any) index $i$ with $D_i=B$; combined with
  Constraint Domination extending this to all $i\le n$: $x\bmod L_{P'}\in G'\iff x$ is a valid
  candidate for $a_{n+1}$.
- **Step D (No-Escape relative to $P'$)**: for $n\ge N^{**}$ and $a_n<x<y_{n+1}$, minimality of
  $y_{n+1}$ gives $x\bmod L_{P'}\notin G'$, so by Step C $x$ is invalid; combined with $a_{n+1}\le
  y_{n+1}$ and validity of $a_{n+1}$, get $a_{n+1}=y_{n+1}$ for all $n\ge N^{**}$.

By `lemmas/periodicity-given-no-escape.md` (generic in $P'$, hypothesis $S\subseteq P'$ satisfied),
No-Escape relative to $P'$ for $n\ge N^{**}$ implies $\exists T,L\ge1$ with $a_{n+T}=a_n+L$ for every
$n\ge1$. $\blacksquare$

**Remark.** This Master Lemma shows Antichain Stabilization is by itself already sufficient for the
full theorem — no separate "P-Confinement relative to the fixed $P=\{p\le L_0\}$" is needed, because
any finitely many "extra" primes appearing in the eventual stable antichain can always be folded into
an enlarged, still-finite prime set $P'$ before re-running the CRT machinery. In particular this
Master Lemma **also repairs** the citation gap flagged in `antichain-signature-closure.md` (round 2
review): instead of using an unverified $P^*$ built loosely from "the eventual generators," it uses
$P':=P\cup\bigcup\mathcal A^\infty$ where $P\supseteq S$ is fixed from the start, so $P'\supseteq S$
is automatic, not something that needs separate verification.

By Corollary 1, the entire remaining content of the theorem (odd case) is now:

$$\textbf{Target: only finitely many } n \text{ are growth events.}$$

### 3. Growth-event decomposition: Type A (closed) vs. Type B (open)

For $n\ge2$ define $D_n^P:=P\cap D_n$ ($P=\{p\le L_0\}$ as before) and $R_n:=\{D_1^P,\dots,D_n^P\}$.

**Definition.** A growth event $n$ is **Type A** if $D_n^P\notin R_{n-1}$ (equivalently $R_n\supsetneq
R_{n-1}$), and **Type B** otherwise (i.e. $D_n^P\in R_{n-1}$).

**Proposition 2 (Type A events are finite, bounded, unconditionally).** The number of $n\ge2$ with
$R_n\supsetneq R_{n-1}$ is at most $2^{|P|}-2$ (in particular finite), regardless of whether $n$ is a
growth event.

*Proof.* $(R_n)_{n\ge1}$ is a non-decreasing (w.r.t. $\subseteq$) sequence of subsets of the finite set
$2^P\setminus\{\emptyset\}$ (size $2^{|P|}-1$), with $R_1=\{D_1^P\}$ of size $1$ (nonempty since
$D_1=S\subseteq P$, so $D_1^P=S\ne\emptyset$). Each strict increase adds at least one element, so the
number of strict-increase indices is at most $(2^{|P|}-1)-1=2^{|P|}-2$. $\blacksquare$

**Proposition 3 (Type B events are exactly the PC-violating ones).** If $n$ is a Type B growth event,
then $D_n\not\subseteq P$ (i.e. $a_n$ has a prime factor $q>L_0$).

*Proof.* Suppose for contradiction $D_n\subseteq P$, so $D_n=D_n^P$. Since $n$ is Type B, $D_n^P\in
R_{n-1}$, i.e. $D_n^P=D_j^P$ for some $j<n$. Two cases: if $D_j\subseteq P$ too, then $D_j=D_j^P=D_n^P=D_n$,
so $D_j\subseteq D_n$ (equality), contradicting that $n$ is a growth event (Definition, §1: no $i<n$
with $D_i\subseteq D_n$). If $D_j\not\subseteq P$, then $D_j^P\subsetneq D_j$; but $D_j^P=D_n^P=D_n$
(using $D_n\subseteq P$ so $D_n^P=D_n$), so $D_n=D_j^P\subseteq D_j$, again contradicting that $n$ is a
growth event. Both cases are impossible, so $D_n\not\subseteq P$. $\blacksquare$

By Propositions 2–3 and Corollary 1: **the theorem reduces to showing only finitely many $n$ are
Type B growth events**, i.e. only finitely many indices $n$ are simultaneously (i) growth events
(genuinely new inclusion-minimal $D_n$), (ii) $D_n^P$ a repeat of an earlier truncated signature, and
(iii, automatic by Prop. 3) $a_n$ divisible by a prime $q>L_0$. This is precisely the "residual growth
events" identified in the outline and is exactly the same event set that `leftover-witness-confinement`
targets via its minimal-counterexample descent (see §5 below for the honest cross-check).

### 4. The attempted global counting argument, and why it does not close (the central negative result)

The outline's proposed mechanism (step 3(b)) is: bound the number of Type B events over a range
$[1,X]$ by comparing (i) how "scarce" $L_0$-smooth integers are, against (ii) the density with which
sequence terms occur (gap-bound: roughly one term per $\le L_0$ integers, so $\Theta(X)$ terms up to
$X$). We carry this out precisely and show it fails, with the exact reason.

**Proposition 4 ($L_0$-smooth counting bound, reproved from scratch).** Let $M>0$ be an integer and
$\pi(M)$ the number of primes $\le M$. The number of $M$-smooth positive integers $\le x$ is at most
$(\lfloor\log_2 x\rfloor+1)^{\pi(M)}$.

*Proof.* An $M$-smooth integer $m\le x$ factors as $m=\prod_{p\le M}p^{e_p}$ with $e_p\ge0$. For each
prime $p\le M$ used, $p^{e_p}\le m\le x$ gives $e_p\le\log_p x\le\log_2 x$ (since $p\ge2$), so
$e_p\in\{0,1,\dots,\lfloor\log_2 x\rfloor\}$, a set of size $\lfloor\log_2 x\rfloor+1$. The
factorization is determined by the tuple $(e_p)_{p\le M}$, of which there are $\pi(M)$ coordinates, so
at most $(\lfloor\log_2 x\rfloor+1)^{\pi(M)}$ distinct $M$-smooth integers $\le x$ (this counts tuples,
an over-count since some give $m>x$ or aren't achieved, but it is a valid upper bound). $\blacksquare$

**Proposition 5 (non-$L_0$-smooth integers have density $\to1$; the mismatch, made precise).** Let
$N_{\mathrm{sm}}(x)$ (resp. $N_{\overline{\mathrm{sm}}}(x)$) be the number of $L_0$-smooth (resp. not
$L_0$-smooth, i.e. having a prime factor $>L_0$) positive integers $\le x$. Then $N_{\mathrm
{sm}}(x)=O((\log x)^{\pi(L_0)})=o(x)$ (Proposition 4 with $M=L_0$), so
$$N_{\overline{\mathrm{sm}}}(x) = x - N_{\mathrm{sm}}(x) = x\,(1-o(1)) \quad (x\to\infty).$$

*Proof.* Immediate from Proposition 4: $N_{\mathrm{sm}}(x)/x\le(\log_2 x+1)^{\pi(L_0)}/x\to0$ as
$x\to\infty$ (polylogarithmic over linear), and $N_{\overline{\mathrm{sm}}}(x)=x-N_{\mathrm{sm}}(x)$
trivially since every positive integer $\le x$ is exactly one of smooth/not-smooth. $\blacksquare$

**Why this refutes the proposed counting mechanism.** By Proposition 3, every Type B growth event's
term $a_n$ is **not** $L_0$-smooth — a property Proposition 5 shows is held by a $(1-o(1))$-density
subset of all integers, i.e. it is the *generic*, overwhelmingly common property among integers, not a
scarce one. The smooth-number-counting technique closes a contradiction only when the required
property forces membership in a **sparse** set (density $\to0$) while the object being counted occurs
with **positive density** (this is exactly how it was used, in the opposite direction, in
`self-closing-pair-density-odd-case.md` Attempt 3: there, an arithmetic progression with
$\Theta(x)$ terms up to $x$ was forced to be $M$-smooth for a hypothetical bounded largest prime
factor, and $\Theta(x)$ terms $>$ the smooth count $O((\log x)^{\pi(M)})$ gave the contradiction).
Here the roles are reversed: the required property ("has a prime $>L_0$") is satisfied by *almost
all* integers, so pairing it against the sequence's $\Theta(N)$ term-density (gap-bound) gives **no
tension at all** — there is no shortage of integers with a large prime factor for the sequence's terms
to draw on; the "smoothness debt" intuition in the outline's step 3(b) points the wrong way. **This is
a genuine, checked mathematical fact, not merely a failure to find the argument**: any attempt to
derive Type B's finiteness from a smooth-vs-non-smooth density mismatch is provably impossible, since
the relevant density comparison runs in the direction that supports *abundance*, not *scarcity*, of
Type-B-eligible integers.

**Could a different, more restrictive "scarce resource" rescue the architecture?** We checked the two
natural refinements and both fail for reasons already independently established in the population,
not merely unexplored:
- *Bounding the total number of distinct large primes ever used across all Type B events* (a
  pigeonhole on the prime pool) is refuted by the already-proved fact (certified-worthy negative
  result in `self-closing-pair-density-odd-case.md` Attempt 3) that the total prime pool
  $\Pi=\bigcup_n\mathrm{primes}(a_n)$ is provably **infinite** once the sequence is eventually
  periodic — which, by the Master Lemma of §2, is exactly what Antichain Stabilization would force it
  to become. So no finite bound on "how many distinct primes $>L_0$ can ever be used" is available; a
  pigeonhole on the prime pool cannot work even in principle.
- *Restricting the counting to the actual valid & inclusion-minimal integers* (rather than all
  non-$L_0$-smooth integers) would require an independent density estimate for the set $V_n\cap
  \{x:x\text{ inclusion-minimal-eligible}\}$ — but $V_n$ is defined by intersecting the hitting
  conditions from *all* current antichain generators (§0), which is precisely the same object whose
  eventual finiteness/shape is Antichain Stabilization itself. Any density estimate for this
  restricted set precise enough to produce a counting contradiction against gap-bound's $\Theta(N)$
  term-density would already have to encode (a strong form of) the very conclusion being sought — this
  is the same circularity the outline warns against (its "Watch out for" note: don't collapse to a
  per-step budget). We checked concretely that no version of this refinement avoids depending, index
  by index, on which specific residues are still available given the *current* antichain state — i.e.
  it reduces to a local (per-$n$), not global, question, exactly the shape already refuted three times
  (per `current.md`'s Rules) for charging-style arguments.

### 5. Honest convergence note

As anticipated by the outline and the outline-reviewer, once made precise, this approach's residual
open target — "only finitely many Type B (PC-violating, repeated-truncated-signature) growth events
occur" — is **exactly** the event set `leftover-witness-confinement` attacks directly via minimal-
counterexample descent (its "Core open target... for an antichain all of whose blocks have size
$\ge2$..."). We did not find a way to make the global/density framing supply leverage this local
framing lacks; if anything, §4 shows the natural global tool (smooth-number density) is actively the
wrong shape for this specific residual target, since it would need to show scarcity of a generically
abundant property. This is consistent with — and reinforces — the outline-reviewer's diagnosis that
the underlying obstruction (which PC-violating events are permitted) is mechanism-agnostic, not an
artifact of the local/minimal-counterexample framing specifically.

## Full proof
(Not applicable — Status is `partial`. Antichain Stabilization, equivalently the finiteness of Type B
growth events, remains open. The Master Lemma of §2 and the Type A/B decomposition of §3 are complete
and gap-free; §4 is a complete, checked negative result for the specific global smooth-density
mechanism dispatched to this approach, not a proof of the residual target.)

## Promotable lemmas
- **Lemma 1 (Growth-Event Update) + Corollary 1 (Antichain Stabilization $\Leftrightarrow$ finitely
  many growth events)**, §1 above: fully proved, elementary, reusable by any approach working with the
  antichain-of-minimal-prime-sets object — gives a clean, self-closing-free restatement of the target.
- **Master Lemma ($P'$-enlargement): Antichain Stabilization alone $\Rightarrow$ the full theorem**,
  §2 above: fully proved, reusable, and closes the citation-hygiene gap flagged in
  `antichain-signature-closure.md` (round 2 review) via an explicit, verifiably-correct choice of
  enlarged prime set $P'=P\cup\bigcup\mathcal A^\infty$ (automatically $\supseteq S$). Recommend
  certifying as `lemmas/antichain-stabilization-implies-theorem.md` — this removes the separate need
  for "P-Confinement relative to the fixed $P=\{p\le L_0\}$" anywhere in the population; Antichain
  Stabilization is by itself the strictly weaker and sufficient target.
- **Propositions 2–3 (Type A/B growth-event decomposition)**, §3: fully proved; gives the precise,
  reusable reformulation "the theorem reduces to: only finitely many Type B growth events" with an
  explicit, checked bound ($\le2^{|P|}-2$) on Type A events. Reusable by
  `leftover-witness-confinement` or any successor to state their residual target in this cleaner
  vocabulary.
- **Propositions 4–5 (smooth-number counting bound and its density-mismatch consequence)**, §4: fully
  reproved from scratch (not merely cited) and repurposed as a *negative* result here — establishes
  precisely why a global smooth/non-smooth density argument cannot bound Type B events. Worth
  certifying as a documented dead-end-with-proof (parallel to the certified negative results already
  in `current.md`'s Rules) so no future round re-attempts this exact mechanism.
