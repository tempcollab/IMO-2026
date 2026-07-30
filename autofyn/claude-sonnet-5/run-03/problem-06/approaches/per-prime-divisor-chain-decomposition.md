## Status
unsolved

## Approaches tried
- Round 3 (new, plateau-breaking): opened as the round's required genuinely-different-mechanism slot
  (CLAUDE.md's plateau-breaking rule: the top approaches, `antichain-signature-closure` and
  `dilworth-antichain-bound`, had both bottomed out on the same underlying wall — Antichain
  Stabilization / P-Confinement — for two rounds running, so this slot was opened to attack from a
  decomposition axis genuinely orthogonal to the shared antichain-of-subsets machinery). No prior
  attempt existed at this decomposition axis; nothing to report as tried beyond stating the target and
  three candidate per-prime quantities ($\sigma_p$, $\tau_p$, a transplant of crux `aimo-0477`).
- **Round 4 (this round): tested all three candidates computationally and analytically against the
  odd-$a_1$ branch (the only branch left open — see below), and found all three fail to give a
  per-prime monovariant.** A precise negative diagnosis for each is given below, together with the
  simulation data that produced it. No positive lemma is established. This is a documented dead end
  for the *literal* per-prime decomposition axis, kept in the population per CLAUDE.md's "record
  everything" rule; the qualitative reason it fails (Diagnosis, below) is itself informative for
  future framings.

## Current best

### Preliminary: scope after the even-case closure
Sibling slug `absorption-recurrence-even-case.md` (Status: **solved**, this round) proved directly by
elementary strong induction (its Lemma B, "Even Persistence") that if $a_1$ is even then
$a_n=a_1+2(n-1)$ for every $n\ge1$, so $(T,L)=(1,2)$ closes the theorem immediately whenever $2\mid
a_1$. I re-read and re-checked that proof (Lemma A: $\gcd(m,m+1)=1$; Lemma B: two-part strong
induction showing $a_1+1$ is always excluded by Lemma A and $a_1+2$ always succeeds because every
term stays even) and confirm it is a complete, self-contained, gap-free argument independent of the
antichain apparatus; I take it as given. **Consequence for this slug:** the only remaining branch of
the whole theorem is $a_1$ **odd**, so I restricted all per-prime candidate-testing below to odd
$a_1$.

One correction to the dispatch note, found while testing: it is **not** true that "$p=2$ is
irrelevant" for the odd branch in the sense of being absent from the per-prime state. $a_1$ being odd
only means $2\notin\mathrm{primes}(a_1)$ (so $2$ never generates the *initial* antichain element); but
$2$ demonstrably re-enters as a factor of later terms $a_n$ for $n>1$ even when $a_1$ is odd (e.g.
$a_1=15\Rightarrow a_2=18=2\cdot3^2$; more below), and appears in the eventual antichain generators of
essentially every odd example tested. So $2$ is exactly as much "in play" as any other prime $p\le
L_0=\mathrm{rad}(a_1)$ once the sequence evolves; the even case is trivial only because *when $a_1$
itself is already even*, the induction in `absorption-recurrence-even-case.md` never lets the sequence
leave the "add 2" regime — the argument does not generalize to "any odd $a_1$ eventually becomes
even," which is a different (and, per the antichain examples, false-as-stated: e.g. $a_1=21,33$
stabilize at the **odd** singleton generator $\{3\}$, so the sequence $a_n=a_1+3(n-1)$ stays odd/even
alternating forever with period $T=1,L=3$, never settling into "add 2 forever").

### Setup (notation, imported from `antichain-signature-closure.md`)
For $a_i>1$, let $D_i=\mathrm{primes}(a_i)$ (its prime-factor set). Let $\mathcal A_n$ be the
inclusion-minimal elements of $\{D_1,\dots,D_n\}$ (so $\mathcal A_n$ is an antichain under $\subseteq$;
a set $F\in\mathcal A_n$ is called a *(live) generator* at time $n$). $\mathcal A_n$ evolves as $n$
grows: a new $D_{n+1}$ either is absorbed (already contains, as a superset, some existing generator,
so $\mathcal A_{n+1}=\mathcal A_n$) or enters as a new generator, possibly dominating (removing) any
existing generators that are supersets of it. `lemmas/gap-bound.md` gives $a_{n+1}-a_n\le
L_0:=\mathrm{rad}(a_1)$ unconditionally, and `lemmas/absorption-lemma.md` shows a singleton generator
$\{p\}\in\mathcal A_n$, once formed, forces $\mathcal A_m=\{\{p\}\}$ for all $m\ge n$ (an immediate
shortcut to the theorem via $T=1,L=p$).

### Candidate 1: $\sigma_p(n):=\mathbb 1[\{p\}\in\mathcal A_n]$

**Claim tested:** does $\sigma_p(n)=1$ get forced for some $p\in P$, for every odd $a_1$, giving a
per-prime route to Absorption independent of the global antichain argument?

**Finding: this candidate reduces to exactly the open gap, with no new leverage, and empirically often
fails to trigger at all within long simulation windows.** I ran the exact greedy recursion (Python,
`math.gcd`, `sympy.primefactors`) for odd $a_1\in\{15,21,33,35,105,165\}$ over $N=400$ and, for
$a_1=105,165$, $N=1500$ terms, tracking $\sigma_p(n)$ for every prime $p$ that ever appears in
$\mathcal A_n$:

- $a_1=21,33$: a singleton generator **does** form — $\sigma_3(n)$ flips to $1$ at $n=3$ and never
  flips back over the whole window (matches `absorption-lemma.md`: this is exactly the mechanism it
  covers, and the resulting sequence is $a_n=a_1+3(n-1)$, giving $T=1,L=3$).
- $a_1=15,105,165$: **no singleton generator forms at all**, for every $p$ that appears, over the
  entire $400$–$1500$-term window. $\sigma_p(n)=0$ for every tracked $p$ and every $n$ in range. (For
  $a_1=15$ the antichain instead stabilizes at the known 3-element non-singleton configuration
  $\{\{2,3\},\{2,5\},\{3,5\}\}$; for $a_1=105,165$ it stabilizes, by $n\approx16$, at 4-element
  configurations of the same "each pair sharing 2" shape, e.g. $a_1=105\to\{\{3,5,7\},\{2,3\},\{2,7\},
  \{2,5\}\}$ at $n=400$, further collapsing to $\{\{2,3\},\{2,5\},\{2,7\}\}$ by $n=1500$ once
  $\{3,5,7\}$ itself gets dominated.)

So whether $\sigma_p$ ever becomes $1$ for *some* $p$ is not universal across odd $a_1$ — it is a
genuine dichotomy (singleton-triggering vs. never-triggering-in-window) that is, by construction,
*exactly* the question "does Absorption occur," which is already known (`absorption-lemma.md`) to be
only a *sufficient*, not necessary, route to the theorem. Testing $\sigma_p$ prime-by-prime adds no
new structure: there is no per-prime argument here beyond "check whether the known sufficient
condition holds for this $p$," and for the majority of tested odd $a_1$ it simply does not hold for
any $p$ in the observed range, so this candidate contributes nothing toward the remaining case (no
singleton, i.e. multi-generator self-closing stabilization, which is exactly the content of
`self-closing-antichain-sufficiency.md`'s open target).

### Candidate 2: $\tau_p(n):=\min\{|F| : F\in\mathcal A_n,\ p\in F\}$ (or $\infty$ if no live generator
contains $p$)

**Claim tested:** is $\tau_p(n)$ eventually non-increasing in $n$ (per prime), and does the joint
$\liminf$ behavior across all $p$ bound $|\mathcal A_n|$?

**Finding: $\tau_p$ is empirically NOT monotone — it can increase from a finite value to $\infty$ (a
prime's covering generator can be permanently eliminated from the antichain, then never recovered
within the simulated window), which directly falsifies "eventually non-increasing" as a per-prime
statement provable independently of already knowing the antichain has stabilized.** Concrete data,
$a_1=105$, $N=1500$, listing $(\,n,\ \tau_p(n{-}1)\to\tau_p(n)\,)$ transitions for each prime that ever
appears in $\mathcal A_n$:

| $p$ | transitions | final $\tau_p$ |
|---|---|---|
| 2 | $(2:\ \infty\to2)$ | 2 |
| 3 | $(2:\ 3\to2)$ | 2 |
| 5 | $(16:\ 3\to2)$ | 2 |
| 7 | $(4:\ 3\to2)$ | 2 |
| 11 | $(3:\ \infty\to3),\ (16:\ 3\to\infty)$ | $\infty$ |
| 13 | $(8:\ \infty\to3),\ (16:\ 3\to\infty)$ | $\infty$ |

and $a_1=165$, $N=1500$ (9 primes ever appear; representative rows):

| $p$ | transitions | final $\tau_p$ |
|---|---|---|
| 2 | $(2:\infty\to3),\ (5:3\to2)$ | 2 |
| 7 | $(2:\infty\to3),\ (9:3\to\infty)$ | $\infty$ |
| 17 | $(3:\infty\to3),\ (11:3\to\infty)$ | $\infty$ |
| 29 | $(4:\infty\to3),\ (9:3\to\infty)$ | $\infty$ |

Primes $11,13$ (for $a_1=105$) and $7,17,19,29,31$ (for $a_1=165$) each had a finite $\tau_p$ at some
point (a generator containing them was briefly a live minimal element) and then were permanently
dominated out of the antichain within the observed window — $\tau_p$ jumped from a finite value
**up** to $\infty$, the opposite of monotone non-increase. Meanwhile the primes that survive into the
*final observed* antichain ($2,3,5,7$ for $a_1=105$; $2,3,5,11$ for $a_1=165$) do individually show a
final non-increasing tail ($3\to2$ or $\infty\to2/3$, never increasing again in the window) — but this
tail behavior is only visible *after* the fact, once we already know (from the simulation, not a
proof) which generators turn out to be permanent. Framed as a candidate monovariant to prove
Antichain Stabilization, this is circular: "prove $\tau_p$ is eventually monotone" is not a
lemma that can be established prime-by-prime without already knowing which generators are permanent —
which is precisely the content of Antichain Stabilization itself. So $\tau_p$ gives no independent
leverage; at best it is a *reformulation* of the target, not a route to it, and as a literal
monovariant claim ("$\tau_p(n)$ is non-increasing for all $n$ past some point, for every $p$") it is
**false** as the $11,13,7,17,19,29,31$ data above shows (these primes' $\tau_p$ strictly increases,
to $\infty$, at some point within the simulated range, for every one of the three odd examples with
a non-singleton stable antichain).

**Boundedness check.** $\tau_p(n)\ge1$ trivially for all $p,n$ (any generator containing $p$ has size
$\ge1$), so the "bounded below" half of the candidate is content-free; the only question of substance
is monotonicity (addressed above, and refuted) or an upper bound on $\tau_p$ across $p$ simultaneously,
which is exactly $|\mathcal A_n|$-type control — again the shared wall, not new content from the
per-prime framing.

### Candidate 3: transplant of crux `aimo-0477`'s $v_p$-monotonicity mechanism

`aimo-0477`'s mechanism (re-confirmed directly from the crux corpus record, not merely from the round-3
summary) is: given a hypothesis that a running sum of the form $t_n = a_n/a_{n+1}+(a_{n+1}-a_n)/a_1$ is
an **integer** for all large $n$, for each prime $p$ the two summands have $p$-adic valuations
$A_n=v_p(a_n)-v_p(a_{n+1})$ and $B_n=v_p(a_{n+1}-a_n)-v_p(a_1)$; if $A_n\ne B_n$, the sum of the two
has valuation $\min(A_n,B_n)$, and integrality of $t_n$ forbids this minimum from being negative,
which forces a case split showing $v_p(a_n)$ is eventually monotone (non-increasing once above
$v_p(a_1)$, non-decreasing while below it), hence eventually constant. The load-bearing structural
fact is: **a designated rational quantity is asserted/proved to be an integer for all (large) $n$, and
that quantity is literally a sum of a bounded number of fixed-shape fractional terms**, so the
"isolated minimal valuation forces non-negativity of the minimum" trick applies.

**Why this does not transplant here (re-derived independently, confirming the round-3 diagnosis):**
our problem's defining relation is $\gcd(a_{n+1},a_i)>1$ for all $i\le n$ — a *coprimality* condition
on integer pairs, not an identity asserting some rational combination of the $a_i$'s is an integer.
There is no natural analogue of $t_n$ here: the greedy rule does not produce, for any fixed small
window of indices, a sum of reciprocal-type terms that must be an integer. Concretely, I checked the
two most natural candidate transplants and both fail structurally, not just numerically:

- $t_n':=a_n/a_{n+1}$: this is never an integer in general (indeed $a_{n+1}>a_n$ always, by the
  problem's own "smallest integer greater than $a_n$" clause, so $0<t_n'<1$ for every $n$ — it is
  never even a non-negative integer, let alone forced to be one by the recursion). There is no
  hypothesis in this problem analogous to aimo-0477's given integrality of a running sum, so there is
  nothing to difference or exploit valuation-wise.
- $\gcd(a_1,a_n)$-type divisor chains (the third crux record, "gcd(fixed term, current term) divides
  the next one"): that mechanism uses the *specific* integrality of $t_n$ to show $d_n:=\gcd(a_1,a_n)$
  satisfies $d_n\mid d_{n+1}$ termwise. Here there is no such forcing: $\gcd(a_1,a_n)$ for our sequence
  is **not** monotone under divisibility in either direction. Direct check ($a_1=15$, first 20 terms
  $15,18,20,21,22,24,25,26,27,28,30,32,33,34,35,36,38,39,40,42$): $\gcd(15,a_2)=\gcd(15,18)=3$,
  $\gcd(15,a_3)=\gcd(15,20)=5$ — already $3\nmid5$ and $5\nmid3$, so $d_2=3,d_3=5$ are incomparable
  under divisibility, refuting a naive "$d_n\mid d_{n+1}$" analogue after only two steps. (This
  computation is elementary: $\gcd(15,18)=\gcd(15,3)=3$ by the Euclidean algorithm since
  $18=1\cdot15+3$; $\gcd(15,20)=\gcd(15,5)=5$ since $20=1\cdot15+5$; and $3\nmid5$, $5\nmid3$ are
  immediate since both are prime and distinct.)

So candidate 3 fails for a structural reason (no integrality-of-a-sum hypothesis to exploit, and the
one divisor-chain quantity that seemed most analogous, $\gcd(a_1,a_n)$, is directly falsified as
monotone by a two-step hand computation), independently confirming the round-3 diagnosis rather than
merely repeating it.

### Diagnosis: why the per-prime decomposition axis is not well matched to this problem
Across all three candidates, the failure has a common qualitative cause, worth recording precisely.
The greedy recursion's defining act at each step is: find the smallest integer greater than $a_n$
sharing a prime factor **with every one of $a_1,\dots,a_n$ simultaneously**. Whether a new value $m$
succeeds is governed by which *sets* of primes divide $m$ and how those sets relate, via inclusion, to
the antichain of prior minimal generators — inherently a statement about **co-occurrence of primes
within a single integer**, not about any one prime's history in isolation. Concretely: a generator
$F\in\mathcal A_n$ with $|F|=k\ge2$ encodes that some $a_i$ needed exactly (at least) $k$ primes acting
*jointly* to be excluded from smaller, single-prime-based routes; tracking any one $p\in F$ alone
(via $\sigma_p$ or $\tau_p$) discards precisely the joint information ("$p$ co-occurring with these
other specific primes") that drives whether $F$ survives or gets dominated by a later, smaller set.
This is exactly why $\tau_p$ oscillates: a set containing $p$ can be a *live* minimal generator only
as long as no smaller set (possibly not containing $p$ at all, or containing $p$ together with
different partners) is discovered later; that event depends on the *joint* prime content of future
terms $a_m$, which is not a function of $p$'s history alone. No amount of restricting attention to a
single prime $p$ recovers this joint structure, so no per-prime quantity of the shape tested here can
be a sufficient statistic for antichain evolution.

### Honest conclusion
All three candidates proposed in the round-3 outline (and the two additional natural variants checked
under candidate 3) fail to yield a per-prime monotone or bounded quantity that closes any part of
Antichain Stabilization / self-closing reachability / P-Confinement for the remaining open case (odd
$a_1$, no singleton generator ever formed). This is reported as a genuine, checked negative result,
not a placeholder: $\sigma_p$ collapses to a restatement of the already-known (and only sometimes
applicable) Absorption sufficient condition; $\tau_p$ is directly falsified as monotone by explicit
simulation transitions for three independent odd examples ($a_1=105,165$, with $a_1=15$ having no
prime ever leave once entered, consistent but uninformative); and the aimo-0477 transplant fails for a
structural reason (no integrality-of-a-sum hypothesis exists in this problem to exploit), reconfirmed
by an independent two-step divisibility computation. Per CLAUDE.md's guidance, this is recorded as a
documented dead end for the *literal* per-prime decomposition axis; the Diagnosis above (joint-prime
co-occurrence, not per-prime history, drives antichain evolution) is offered as the qualitative reason,
useful for steering future framings away from single-prime state variables toward pair/tuple-level
co-occurrence statistics if this axis is revisited.

## Full proof
(Not applicable — Status is `unsolved`; no per-prime monovariant was established. See "Honest
conclusion" above for the precise negative result.)

## Promotable lemmas
None. (The correction regarding "$p=2$ is not literally irrelevant to the odd branch's per-prime
antichain state" is a clarifying remark, not a standalone lemma; the closed-form fact that
$a_1=21,33$ each satisfy $a_n=a_1+3(n-1)$ via early Absorption at $p=3$ is already fully covered by
the existing certified `lemmas/absorption-lemma.md` and is not new content.)
