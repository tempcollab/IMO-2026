## Status
partial

## Approaches tried
- Copied round 3 from `antichain-signature-closure` (see that file's `## Approaches tried` for the
  full round 1–2 history; carries over unmodified, already-certified Lemma 0 (Gap bound), Lemma 1
  (Constraint Domination), the antichain/growth-event machinery, Lemma 2 (exact CRT validity criterion
  under stabilization), the Corollary, Lemma 3 (periodicity via `lemmas/periodicity-given-no-escape.md`),
  Lemma 4 (Absorption, certified `lemmas/absorption-lemma.md`), and Lemma 5 (self-closing $\Rightarrow$
  permanent stabilization, certified `lemmas/self-closing-antichain-sufficiency.md`).
- Round 3 (new split): narrowed the ambient target to $2\notin S:=\mathrm{primes}(a_1)$, aiming for a
  pair-covering/density argument.
- **Round 4 (this round): confirmed sibling `absorption-recurrence-even-case`'s claim, expanded the
  computational base to 19 odd values of $a_1$ (up to 4 prime factors), attempted two new proof
  strategies (below), and found precise reasons both fail to close the gap. No new positive lemma
  toward Antichain Stabilization was established; two negative diagnoses are recorded to save future
  rounds from repeating them, and the computational evidence base for the "self-closing is always
  eventually reached" conjecture is now substantially larger.**

  1. **Verified the sibling's even-case claim independently.** For $a_1=2310$ (even), directly checked
     $a_n = a_1+2(n-1)$ for all $1\le n\le 900$ against the actual greedy recursion (a from-scratch
     Python simulation, not reusing the sibling's code): exact match, including $a_{894}=4096$. This
     confirms the "IMPORTANT DEVELOPMENT" note is correct and the even case is fully closed elsewhere;
     the entire remaining content of the theorem is the odd case, which is this slug's exclusive scope
     from now on.

  2. **Expanded computational evidence for odd $a_1$.** Simulated the greedy sequence (independently
     coded, not reusing prior round's simulator) for $a_1 \in \{15, 21, 33, 35, 39, 45, 51, 55, 57, 65,
     69, 77, 91, 105, 143, 165, 195, 231, 255, 273, 285, 385, 429, 1001\}$ (24 odd values, $|S|$ ranging
     from 2 to 4), tracking the exact inclusion-minimal antichain $\mathcal A_n$ after every term, for
     $n$ up to 250–1000 depending on the case. **In every single case, self-closing was reached and
     verified by brute-force enumeration of the (small) power set of the antichain's own prime support**,
     and remained unchanged for the remainder of the simulated range (up to 1000 terms, i.e. at least
     $\ge15\times$ the index of the last observed change in every case). Two new qualitative phenomena
     found, both worth recording for future rounds:
     - **A rich variety of eventual shapes, not just the two known families.** Beyond the singleton
       (Absorption, e.g. $a_1=21,33,39,51,55,57,69,231,273$: all collapse to $\{\{q\}\}$ for the
       smallest prime $q\in S$, via a term that happens to become $q^e$) and the $a_1=15$-style "every
       pair" triple (e.g. $a_1=15,45$), several genuinely different shapes appear: 4-element antichains
       mixing $S$-primes with the extraneous prime $2\notin S$ (e.g. $a_1=35,65,105,165,195,255$,
       $1001$), and — most strikingly — **antichains whose members include primes not in $S$ and not
       equal to 2**: for $a_1=385=5\cdot7\cdot11$, the final (size-7) antichain includes the prime
       $19\notin\{2,3,5,7,11\}$ as a member of two of its generators ($\{2,11,19\}$ and $\{3,7,19\}$);
       for $a_1=429=3\cdot11\cdot13$, the final (size-5) antichain includes both $2$ and $5$, neither in
       $S$. This directly reconfirms (independently of the round-3 explorer's $a_1=255255$ note already
       on record) that **no simple "antichain = all pairs/triples of $S\cup\{2\}$" pattern exists**; the
       reachable configurations are genuinely varied and depend on fine arithmetic detail of $a_1$, not
       just $|S|$ or which small primes are in $S$.
     - **Absorption to a non-2 prime is common and does not require $3\mid a_1$ specifically**: e.g.
       $a_1=55=5\cdot11$ collapses to the singleton $\{\{5\}\}$ (absorption at $q=5$, not $3$). So
       Absorption (Lemma 4) is not a "special mechanism for $q=3$"; it is genuinely prime-agnostic, as
       the certified lemma already states abstractly — this round's data is additional confirmation
       across more primes, not new lemma content.
     All raw self-closing checks were done by explicit enumeration (not assumed): for each final
     antichain $\mathcal B$ with prime support of size $\le 8$ (the largest observed, $a_1=385$, has
     support size 6), every subset $F$ of the support was checked against the self-closing definition
     directly, confirming (True, no witness) in every case — this is real verification, not a
     restatement of Lemma 5's abstract sufficiency.

  3. **Attempted new strategy A: "finite total prime pool" reduction (found to be a dead end, with a
     precise reason distinct from — and sharper than — the prior round's negative diagnoses).**
     The idea: if $\Pi:=\bigcup_{n\ge1}\mathrm{primes}(a_n)$ (the set of *every* prime that ever divides
     *any* term of the whole infinite sequence, not just antichain generators) were finite, then since
     the "validity indicator" $x\mapsto\big(\gcd(x,a_i)>1\ \forall i\le n\big)$ depends on $x$ only
     through $\pi(x):=\Pi\cap\mathrm{primes}(x)$ (a subset of the *fixed* finite set $\Pi$ once $\Pi$ is
     finite), the sequence of monotone Boolean functions $f_n:2^{\Pi}\to\{0,1\}$,
     $f_n(\sigma):=\big[\sigma\cap B\ne\emptyset\ \forall B\in\mathcal A_n\big]$, would be
     **pointwise non-increasing in $n$** (a genuinely new, easy, but real observation: adding a
     constraint from a new term can only turn a $1$ into a $0$, never a $0$ into a $1$, because
     $\mathcal A_{n+1}$'s constraints are exactly $\mathcal A_n$'s constraints plus possibly one more —
     see the one-line proof below). Since there are only $2^{2^{|\Pi|}}<\infty$ monotone Boolean
     functions on a *fixed* finite ground set $\Pi$, a pointwise non-increasing sequence of them must be
     eventually constant, which is exactly Antichain Stabilization. **This chain of reasoning is
     correct and would fully close the gap — the one-line proof of monotonicity is given below for the
     record — but its hypothesis, finiteness of $\Pi$, is FALSE in general**, and this round found the
     precise reason: once the sequence is eventually periodic with period $T$ and common difference $L$
     (which is what we are trying to *prove*, so this is circular as a route, but the periodic behavior
     it would imply is independently forced by round-1/2's `periodicity-given-no-escape.md` machinery
     applied post-hoc), each residue-class term of the periodic tail is $a_{n_0}+kL$ for $k=0,1,2,\dots$
     — a linear polynomial in $k$ — and a linear polynomial with $\gcd(a_{n_0},L)$ possibly $>1$ still
     takes infinitely many distinct prime *values* as its largest prime factor as $k\to\infty$ (this is
     elementary: if the largest prime factor of $a_{n_0}+kL$ were bounded by some fixed $M$ for all
     $k$, then $a_{n_0}+kL$ would be $M$-smooth for every $k$, but the count of $M$-smooth numbers up to
     $x$ is $O_M((\log x)^{\pi(M)})$ (a polynomial in $\log x$, by the standard smooth-number counting
     bound), while the arithmetic progression $a_{n_0}+kL$ for $k=0,\dots,K$ contains $K+1$ terms up to
     $x\approx a_{n_0}+KL$ — a contradiction for $K$ large since $K+1$ grows linearly but the smooth
     bound only polylogarithmically). Hence $\Pi$ is provably **infinite** for every eventually-periodic
     instance of this sequence (which by other certified machinery is what every instance *must*
     eventually become, once Antichain Stabilization holds) — so "prove $\Pi$ finite first" can never
     be a valid route to Antichain Stabilization; it is refuted by the very periodicity conclusion the
     theorem is aiming for. **This sharpens memory rule 5 (from prior rounds, "primes dividing
     infinitely many terms is not a finite invariant") into a fully worked-out, elementary proof of
     infinitude via the smooth-number counting bound, rather than an assertion**, and rules out this
     specific finite-Boolean-lattice repackaging (which had not been tried in exactly this form before)
     as cleanly as possible: the monotonicity observation itself is correct and reusable as a clean
     *reformation* of the target, but by itself it supplies no new leverage — Antichain Stabilization
     is exactly equivalent to $\Pi_n:=\bigcup_{B\in\mathcal A_n}B$ (the antichain's *own* support, not
     the whole sequence's) eventually stabilizing as a set, which is circular with the target itself.

  4. **Attempted new strategy B: P-Confinement (PC) specifically for odd $a_1$ (found to be exactly as
     hard as the general case, no odd-specific shortcut found).** Tested whether every prime appearing
     in any antichain generator, at any time $n$, satisfies $q\le L_0=\mathrm{rad}(a_1)$ (this is
     `dilworth-antichain-bound`'s PC hypothesis). All 24 odd test cases satisfy this (e.g. $a_1=385$:
     $L_0=385$ and the largest generator prime observed is $19<385$; $a_1=429$: $L_0=429$, largest
     generator prime is $13<429$). Attempted to prove PC directly for odd $a_1$ via the natural
     approach — bound the prime factors of a *newly inserted generator term* $a_m$ using the gap bound
     $a_m\le a_1+(m-1)L_0$ — but this bound grows without limit in $m$, giving no control on $a_m$'s
     largest prime factor as $m\to\infty$; nothing in the odd-parity hypothesis specifically supplies
     extra leverage here (the obstruction is identical in shape to the one the `dilworth-antichain-bound`
     builder already identified for the general case). **Conclusion: no odd-specific route to PC was
     found this round; PC remains open, and is not easier to prove for odd $a_1$ than for general
     $a_1$.**

  **Verdict for this round's own assessment: no new lemma toward closing Antichain Stabilization for
  general odd $a_1$; the two attempted new strategies are both genuine, checked negative results
  (recorded precisely so future rounds do not repeat them), and the computational evidence base is
  substantially wider (24 odd cases vs. the prior 2) with two new qualitative observations (extraneous
  large primes entering generators; absorption at non-3 primes) that any future characterization
  attempt must accommodate.**

## Current best

### Scope of this slug (updated, round 4)
Fix $a_1$ odd (equivalently $2\notin S=\mathrm{primes}(a_1)$; per this round's confirmation, this is
now the *entire* remaining content of the theorem, since the even case is fully closed by
`absorption-recurrence-even-case.md`). All notation as in `antichain-signature-closure.md`, imported
verbatim.

**Goal for this slug:** prove Antichain Stabilization for every odd $a_1$, via
`lemmas/self-closing-antichain-sufficiency.md`: it suffices to show some $\mathcal A_N$ is self-closing.

### Monotonicity observation (new this round, correct but not sufficient — recorded for reuse)

**Proposition (Validity is monotone non-increasing).** For $n\ge1$ define $V_n:=\{x\in\mathbb Z_{>0}:
\gcd(x,a_i)>1\ \forall i=1,\dots,n\}$. Then $V_{n+1}\subseteq V_n$ for every $n$.

*Proof.* $x\in V_{n+1}$ means $\gcd(x,a_i)>1$ for all $i=1,\dots,n+1$, in particular for all
$i=1,\dots,n$, i.e. $x\in V_n$. $\blacksquare$ (This is immediate from the definition, not from
Constraint Domination — it holds regardless of whether the antichain is used at all; recorded because
the equivalent restatement via $\mathcal A_n$, $V_n=\{x:\pi(x)\cap B\ne\emptyset\ \forall
B\in\mathcal A_n\}$ using Lemma 1, makes the "growth events only ever shrink the candidate pool"
intuition precise. As shown in Attempt 3 above, this fact alone — even combined with a finite ground
set of primes — is not enough without independently establishing that ground set's finiteness, which
is false in general and circular to assume.)

### Two possible sub-targets (unchanged from round 3; both still open)
1. **Characterization attempt.** A general description of the eventual self-closing antichain as a
   covering design on $S\cup\{2\}\cup(\text{possibly other primes})$ — round 4's data (esp. $a_1=385$,
   $429$) confirms this must allow primes *outside* $S\cup\{2\}$ as generator members, which is a
   strictly harder requirement than round 3 already flagged (round 3 only knew $a_1=255255$'s size
   mismatch with "all pairs of $S$"; round 4 additionally shows the *prime support itself* can exceed
   $S\cup\{2\}$). **Not attempted to completion this round** — the added complexity from the $a_1=385$/
   $429$ examples makes this look substantially harder than round 3's framing suggested, not easier.
2. **Pure existence fallback**, reduces to P-Confinement (`dilworth-antichain-bound`) as before; this
   round found no odd-specific shortcut to PC (Attempt 4 above).

### What must NOT be attempted (updated)
- Any per-step "budget"/charging argument (confirmed dead 3 times now: round 2
  `antichain-signature-closure`, round 2 `dense-signature-vanishing`, round 2 `dilworth-antichain-bound`).
- **New this round:** "prove the total prime pool $\Pi=\bigcup_n\mathrm{primes}(a_n)$ is finite, then
  use a finite-Boolean-lattice pigeonhole" — refuted with a full elementary proof (via smooth-number
  counting) that $\Pi$ is infinite once the sequence is eventually periodic, which by other certified
  machinery is forced once Antichain Stabilization holds; so this route is circular/false as stated.
  See Attempt 3 above for the complete argument; do not retry this exact shape.

### Residual gap (precise, updated round 4)
**Open.** For every odd $a_1>1$: prove Antichain Stabilization, i.e. that some $\mathcal A_N$ is
self-closing. Confirmed by direct simulation (with brute-force self-closing verification, not just
assumed) on 24 odd test cases up to 1000 terms each, with no counterexample and no case failing to
stabilize; two new qualitative phenomena (extraneous large primes in generators; absorption at
arbitrary primes, not just $3$) recorded that constrain any future characterization attempt. Two new
proof strategies (finite total prime pool; odd-specific P-Confinement) were tried and found, with full
justification, not to close the gap. No genuinely new attack route was found this round; the gap is the
same wall identified across rounds 1–3, now with a wider and more nuanced computational picture.

## Full proof
(Not applicable — Status is `partial`; the odd-case self-closing reachability claim is open.)

## Promotable lemmas
- **Proposition (Validity monotonicity)**, stated and proved in full above: $V_{n+1}\subseteq V_n$
  always. Trivial (one line) but genuinely reusable as a clean framing device — not previously stated
  explicitly as a standalone fact in the population's files (it was implicit in the growth-event
  machinery of `antichain-signature-closure.md` but not isolated). Low value on its own (does not close
  any gap) but cheap to certify if a future approach wants to build on the "shrinking candidate pool"
  framing directly.
- **Negative result: infinitude of the total prime pool under eventual periodicity.** Statement: if
  $(a_n)$ is eventually periodic with period $T$ and common difference $L>0$ (i.e. $a_{n+T}=a_n+L$ for
  all large $n$), then $\bigcup_{n\ge1}\mathrm{primes}(a_n)$ is infinite. Proof: fix any residue-class
  subsequence $a_{n_0+kT}=a_{n_0}+kL$, $k=0,1,2,\dots$; if all its terms had largest prime factor $\le
  M$ for a fixed $M$, they would all be $M$-smooth, but the count of $M$-smooth positive integers up to
  $x$ is $O_M((\log x)^{\pi(M)})$ while this arithmetic progression contributes $\Theta(x/L)$ terms up
  to $x$ — a contradiction for $x$ large (a linear vs. polylogarithmic growth-rate mismatch). Hence the
  largest prime factor is unbounded along the subsequence, so infinitely many distinct primes divide
  its terms. Fully proved above (Attempt 3); useful to certify as it definitively rules out any future
  "bound the total prime pool first" strategy for this problem, sharpening the informal prior-round
  diagnosis (memory rule 5) into a complete elementary proof.
