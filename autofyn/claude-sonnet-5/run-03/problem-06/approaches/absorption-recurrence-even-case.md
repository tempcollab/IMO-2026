## Status
solved

## Approaches tried
- Copied round 3 from `antichain-signature-closure` (see that file's `## Approaches tried` for the
  full round 1–2 history: it carries over, unmodified and already certified, Lemma 0 (Gap bound),
  Lemma 1 (Constraint Domination), the antichain/growth-event machinery, Lemma 2 (exact CRT validity
  criterion under stabilization), the Corollary, Lemma 3 (periodicity via
  `lemmas/periodicity-given-no-escape.md`), Lemma 4 (Absorption, certified as `lemmas/absorption-lemma.md`),
  and Lemma 5 (self-closing $\Rightarrow$ permanent stabilization, certified as
  `lemmas/self-closing-antichain-sufficiency.md`).
- Round 3: narrowed the ambient target from the source file's fully general **Antichain
  Stabilization** to the single case $2\in S:=\mathrm{primes}(a_1)$, aiming to prove it via the
  "power-of-2 trigger" mechanism suggested by simulation (an eventual pure-power-of-2 term, closing
  the case via `lemmas/absorption-lemma.md`). Left as an **open** Trigger Claim; no proof attempt was
  recorded beyond the empirical pattern.
- **Round 4 (this round): found a direct elementary proof that bypasses the entire antichain/
  absorption apparatus for this case.** Rather than chase the power-of-2 trigger, I proved directly
  by induction that if $a_1$ is even, then $a_{n+1}=a_n+2$ for *every* $n\ge1$ — i.e. the whole
  sequence is the fixed arithmetic progression $a_n=a_1+2(n-1)$, with no exceptions, ever. This gives
  $T=1,L=2$ immediately and closes this slug's entire scope (Antichain Stabilization for $2\in S$)
  as an instant corollary, with a *much* stronger conclusion than the stabilization claim itself
  required. Verified computationally against 30 random even $a_1$ (up to 10000) over 150 terms each,
  plus the on-record examples ($a_1=2310$, $a_1=30030$, $a_1=510510$), all with zero deviation from
  $a_n=a_1+2(n-1)$. The "eventual power-of-2 term" empirically observed in prior rounds is real but
  is now understood as an *incidental* fact about this specific fixed arithmetic sequence (some term
  $a_1+2(n-1)$ happens to be a power of $2$), not a causal mechanism — it plays no role in the proof
  below.

## Current best
Full proof below; Status `solved` for this slug's scope ($2\mid a_1$). See `Full proof`.

(Historical note on why earlier rounds missed this: the antichain/absorption framework tracks the
*set of primes ever seen as inclusion-minimal generators*, which does grow over time even though the
gaps $a_{n+1}-a_n$ never do — e.g. for $a_1=2310$ the reviewer's count of "353 growth events in the
first 893 terms" refers to new minimal prime-sets entering the antichain, not to gap sizes exceeding
2. Both facts are simultaneously true and consistent: the terms increase by exactly 2 each step, while
new primes appear as factors of $a_1+2(n-1)$ as $n$ grows. The antichain machinery is a strictly more
complicated route to the same conclusion in this branch; it is not wrong, just unnecessary here.)

## Full proof

### Setup
Let $(a_n)_{n\ge1}$ be the sequence of the problem: $a_1$ is given, and for every $n\ge1$, $a_{n+1}$
is the smallest positive integer greater than $a_n$ with $\gcd(a_{n+1},a_i)>1$ for every
$i=1,\dots,n$. This slug's scope: assume $a_1$ is **even**.

### Lemma A (consecutive integers are coprime)
For every positive integer $m$, $\gcd(m,m+1)=1$.

**Proof.** If $d\mid m$ and $d\mid m+1$, then $d\mid (m+1)-m=1$, so $d=1$. Hence the only common
divisor of $m$ and $m+1$ is $1$, i.e. $\gcd(m,m+1)=1$. $\blacksquare$

### Lemma B (Even Persistence)
If $a_1$ is even, then for every $n\ge1$: $a_n$ is even, and $a_{n+1}=a_n+2$.

**Proof.** By strong induction on $n\ge1$, we simultaneously prove the two-part statement
$P(n)$: "$a_1,\dots,a_n$ are all even, and $a_{n+1}=a_n+2$."

*Base case $n=1$.* $a_1$ is even by hypothesis. We must show $a_2=a_1+2$.
- By definition, $a_2$ is the smallest integer greater than $a_1$ with $\gcd(a_2,a_1)>1$ (the single
  constraint $i=1$).
- The candidate $a_1+1$ fails: by Lemma A with $m=a_1$, $\gcd(a_1+1,a_1)=1$, so $a_1+1$ does not
  satisfy the required condition (it does not have $\gcd(\cdot,a_1)>1$).
- The candidate $a_1+2$ succeeds: since $a_1$ is even, $a_1+2$ is also even, so $2$ divides both
  $a_1+2$ and $a_1$, giving $\gcd(a_1+2,a_1)\ge2>1$.
- Since $a_1+1$ is excluded and $a_1+2$ is the very next integer after it and satisfies the
  condition, and $a_2$ is by definition the *smallest* integer $>a_1$ satisfying the condition, we
  conclude $a_2=a_1+2$. In particular $a_2$ is even, so $a_1,a_2$ are both even. $P(1)$ holds.

*Inductive step.* Fix $n\ge1$ and assume $P(n)$ holds, i.e. $a_1,\dots,a_n$ are all even and
$a_{n+1}=a_n+2$. We must show $P(n+1)$: $a_1,\dots,a_{n+1}$ all even (which already follows: $a_{n+1}
=a_n+2$ is even since $a_n$ is even, by the inductive hypothesis) and $a_{n+2}=a_{n+1}+2$.

By definition, $a_{n+2}$ is the smallest integer greater than $a_{n+1}$ such that
$\gcd(a_{n+2},a_i)>1$ for every $i=1,\dots,n+1$.
- The candidate $a_{n+1}+1$ fails: by Lemma A with $m=a_{n+1}$, $\gcd(a_{n+1}+1,a_{n+1})=1$. Taking
  $i=n+1$ in the required condition, this candidate fails to satisfy $\gcd(\cdot,a_{n+1})>1$, so it
  is excluded.
- The candidate $a_{n+1}+2$ succeeds against every index $i=1,\dots,n+1$: since $a_{n+1}$ is even (as
  just noted), $a_{n+1}+2$ is even. Every $a_i$ for $i=1,\dots,n+1$ is even (the $i\le n$ cases by the
  inductive hypothesis $P(n)$, and $i=n+1$ shown just above). Hence $2\mid a_{n+1}+2$ and $2\mid a_i$
  for every such $i$, giving $\gcd(a_{n+1}+2,a_i)\ge2>1$ for all $i=1,\dots,n+1$.
- As before, $a_{n+1}+1$ is the only integer strictly between $a_{n+1}$ and $a_{n+1}+2$, it is
  excluded, and $a_{n+1}+2$ satisfies every required condition; since $a_{n+2}$ is the smallest such
  integer, $a_{n+2}=a_{n+1}+2$.

This establishes $P(n+1)$, completing the induction. By induction, $P(n)$ holds for every $n\ge1$:
every $a_n$ is even, and $a_{n+1}=a_n+2$ for every $n\ge1$. $\blacksquare$

### Corollary (closed form)
If $a_1$ is even, then $a_n=a_1+2(n-1)$ for every $n\ge1$.

**Proof.** Immediate telescoping of Lemma B's recursion $a_{n+1}=a_n+2$ starting from $a_1$: by
induction on $n$, $a_1=a_1+2\cdot0$ (trivial base case), and if $a_n=a_1+2(n-1)$ then
$a_{n+1}=a_n+2=a_1+2(n-1)+2=a_1+2n=a_1+2((n+1)-1)$. $\blacksquare$

### Conclusion (Theorem, in this slug's scope)
If $2\mid a_1$, take $T=1$ and $L=2$ (both positive integers). By Lemma B, for every positive integer
$n$: $a_{n+T}=a_{n+1}=a_n+2=a_n+L$. This is exactly the required conclusion of the problem,
$a_{n+T}=a_n+L$ for every $n$, established with an explicit, verified $(T,L)=(1,2)$ — indeed with the
sequence shown to be *literally* the arithmetic progression $a_n=a_1+2(n-1)$ from the very first term,
which is far stronger than mere eventual periodicity. $\blacksquare$

### Relation to the rest of the population
This proof supersedes, for the case $2\mid a_1$, the antichain-stabilization machinery inherited from
`antichain-signature-closure.md` (Lemmas 0–5, `absorption-lemma.md`,
`self-closing-antichain-sufficiency.md`) and the round-3 "power-of-2 trigger" framing: none of that
apparatus is needed to close this branch, though it remains correct and is still the operative route
for the complementary case (odd $a_1$, handled by sibling slugs such as
`self-closing-pair-density-odd-case`). This slug's scope — Antichain Stabilization (indeed the full
theorem) whenever $2\in\mathrm{primes}(a_1)$ — is now fully and rigorously closed.

**Scope caveat, stated precisely.** This file proves the theorem only for $a_1$ even. It says nothing
about $a_1$ odd; that case is out of scope here (see `current.md` and the odd-case sibling slug for
the state of that branch). Whether the same phenomenon ($a_{n+1}=a_n+2$ forever) can also occur or
fail for some odd $a_1$ is not addressed by this file.

## Promotable lemmas
- **Lemma B (Even Persistence)**: *If $a_1$ is even, then $a_n$ is even for every $n\ge1$ and
  $a_{n+1}=a_n+2$ for every $n\ge1$; consequently $a_n=a_1+2(n-1)$ for all $n$.* Proved in full above
  by elementary strong induction, using only Lemma A (consecutive integers are coprime) and the
  problem's defining recursion — no dependence on any other lemma in the population (gap bound,
  antichains, absorption, etc. are all unnecessary here). This is a complete, self-contained proof of
  the full theorem's even branch and should be certified as a standalone lemma
  (`lemmas/even-persistence.md`) so any other approach or the final write-up can cite it directly to
  dispose of the case $2\mid a_1$ in one step, leaving only $a_1$ odd as the remaining branch of the
  whole problem.
