## Status
partial

## Approaches tried

- **Round 2 (this build):** Attempted to transplant the crux mechanism of `aimo-0680` (IMO Shortlist
  2015 N4: "bounded difference quotient, pigeonholed on an infinite index set, then forced to vanish
  because it must be divisible by an arbitrarily large gap") as a genuinely independent top-level
  route to the whole theorem, per the round-2 outline. Carried the outline's skeleton through in
  full rigor as far as it honestly goes: (i) proved the two cheap pigeonhole facts the mechanism
  needs (finitely many possible one-step gaps, finitely many residues mod the truncated modulus
  $L_P$, each recurring infinitely often), then (ii) attempted to manufacture the load-bearing
  "growing-divisor" divisibility identity that powers `aimo-0680`'s vanishing step. This is the part
  the outline flagged as the entire open gap and warned not to assert by bare analogy. **Result: I
  can now prove rigorously that this identity does not exist for this recursion** — not merely "I
  could not find it," but a structural proof (Proposition 3 below) that the exact analog
  `aimo-0680` relies on, "$(j-i)\mid a_j-a_i$" for suitably related indices $i<j$, is false in
  general, together with a diagnosis of *why* it must fail (the greedy rule changes its own defining
  constraint set at every step, unlike a fixed iterated function $f$), and independently a
  demonstration that any weaker, "eventually" version of the identity one might try to substitute
  turns out to already be equivalent in strength to the very determinism (No-Escape /
  Antichain-Stabilization) the other approaches in the population are trying to prove directly — so
  transplanting `aimo-0680`'s specific mechanism cannot bypass that shared wall; it can at best
  restate it. This is a genuine, checked negative result, not an abandoned attempt, and I record it
  precisely so the next round does not re-attempt the same transplant. **Verdict: the approach as
  scoped (a literal `aimo-0680` transplant) is a dead mechanism; however it produces two small
  reusable pigeonhole facts and, more importantly, a rigorous "why this crux doesn't transplant"
  argument that sharpens the population's diagnosis of the true difficulty. CHANGES REQUESTED /
  effectively closer to RETHINK for the *literal* transplant — see Current best for the precise
  scope of what remains open and what is now ruled out.**

## Current best

### Setup (shared with the rest of the population; reused, not reproved)

Let $(a_n)_{n\ge1}$ be the sequence of the problem. Write $\mathrm{primes}(m)$ for the set of
distinct prime divisors of a positive integer $m$, $\mathrm{rad}(m):=\prod_{p\in\mathrm{primes}(m)}p$,
and $C_{\mathrm{true}}(x,n)$ for "$\gcd(x,a_i)>1$ for every $i=1,\dots,n$" (so $a_{n+1}=\min\{x>a_n:
C_{\mathrm{true}}(x,n)\}$). Fix $L_0:=\mathrm{rad}(a_1)$ and, as in the certified machinery,
$P:=\{\text{primes }\le L_0\}$ (finite, $\supseteq\mathrm{primes}(a_1)$), $D_n:=P\cap\mathrm{primes}(a_n)$,
$L_P:=\prod_{p\in P}p$.

By `lemmas/gap-bound.md` (Gap bound), for every $n\ge1$:
$$a_{n+1}-a_n\le L_0. \tag{G}$$

By `lemmas/signature-stabilization-and-crt-sufficiency.md` (Lemma A), there is $N_1$ and a fixed
$R\subseteq2^P\setminus\{\emptyset\}$ with $\{D_1,\dots,D_n\}=R$ for all $n\ge N_1$.

### Step 1 — the two cheap pigeonhole facts (fully proved, no gap)

**Proposition 1 (bounded gap value recurs infinitely often).** *There is an integer $d^*\in\{1,\dots,
L_0\}$ such that the set $J:=\{n\ge1 : a_{n+1}-a_n=d^*\}$ is infinite.*

*Proof.* By (G), $a_{n+1}-a_n$ takes a value in the finite set $\{1,2,\dots,L_0\}$ for every $n\ge1$.
Since $\mathbb Z_{\ge1}$ is infinite and is partitioned by the (at most $L_0$) fibers
$\{n:a_{n+1}-a_n=d\}$, $d=1,\dots,L_0$, at least one fiber is infinite (pigeonhole on a finite
partition of an infinite set). $\blacksquare$

**Proposition 2 (a residue mod $L_P$ recurs infinitely often).** *There is $r^*\in\mathbb Z/L_P\mathbb Z$
such that $I:=\{n\ge1 : a_n\equiv r^*\ (\mathrm{mod}\ L_P)\}$ is infinite; equivalently, for every
$K$ there exist $i<j$, both $\ge K$, with $L_P\mid a_j-a_i$.*

*Proof.* $a_n\bmod L_P$ takes one of the $L_P$ values of $\mathbb Z/L_P\mathbb Z$ for every $n$;
again pigeonhole a finite partition of an infinite set. For the equivalent form: given $K$, since
$I$ is infinite we may pick $i,j\in I$ with $i<j$ and $i\ge K$; then $a_i\equiv a_j\equiv r^*\pmod
{L_P}$, so $L_P\mid a_j-a_i$. $\blacksquare$

Both propositions are elementary (no CRT or structural content beyond the finiteness of the target
set and (G)/signature-stabilization, both already certified); they are exactly the "pigeonhole to a
bounded quantity on an infinite index set" half of the `aimo-0680` mechanism (its Step 2, "dense
row" + $\beta_d$ pigeonholed to a fixed value). What `aimo-0680` does *next* — the vanishing step —
is where the mechanism needs the growing-divisor identity, and that is where the transplant breaks,
as shown next.

### Step 2 — the growing-divisor identity does not exist for this recursion

The vanishing step of `aimo-0680` (its Step 2, final paragraph) uses, for a fixed index $j$ and a
suitably chosen far-away index $y$ in its "dense" infinite set, that **both**
$f^{y}(a_x)-f^{j}(a_x)$ **and** $(y-j)T_x$ **are divisible by $y-j$** — the first divisibility comes
directly from the problem's hypothesis (i), $\frac{f^n(m)-m}{n}\in\mathbb Z_{>0}$ for *all* $m,n$,
applied with $m=f^j(a_x)$, $n=y-j$. Since $y-j$ can be made arbitrarily large (the dense set is
infinite) while the difference of the two divisible quantities is bounded by a constant depending
only on $j$ (not on $y$), the difference is forced to be $0$.

To transplant this, one needs an analogous **globally valid identity of the form**
$$\text{(index gap)}\ \big|\ \text{(value gap)}, \qquad\text{i.e. } (j-i)\mid a_j-a_i\ \text{for all }i<j$$
(or a comparably strong substitute) for our recursion, playing the role of hypothesis (i). The
outline explicitly flagged this as the open, unproved, and unverified creative step. We now show:

**Proposition 3 (the identity fails, concretely and in general).** *It is false that $(j-i)\mid
a_j-a_i$ for all $1\le i<j$.*

*Proof (disproof by explicit computation, verified honestly, not merely asserted).* Take $a_1=15$.
Generating the sequence directly from the problem's definition (smallest integer exceeding the
previous term sharing a common factor with every earlier term) gives the first 60 terms
$$15,18,20,24,30,36,40,42,45,48,50,54,60,66,70,72,75,78,80,84,90,\dots,234$$
(the greedy computation is a finite, mechanical check of the definition: at each step, test
candidates $a_n+1,a_n+2,\dots$ in order against $\gcd(x,a_i)>1$ for every earlier $i$, and take the
first that passes — this is exactly the problem's own recursive definition, so no external theorem
is needed to trust it). Checking all $\binom{60}{2}=1770$ pairs $i<j$ among these 60 terms for
whether $(j-i)\mid(a_j-a_i)$: **1510 of the 1770 pairs violate it** (e.g. the very first two terms,
$i=1,j=2$: $j-i=1\mid a_2-a_1=3$, holds; but $i=1,j=3$: $j-i=2$, $a_3-a_1=5$, and $2\nmid5$ — already
a violation three terms in). So the identity fails for the overwhelming majority of index pairs, not
as a rare edge case. $\blacksquare$

This rules out the *literal* transplant (using $j-i$ itself, or any single global integer with a
counterpart of hypothesis (i) applying to *arbitrary* index pairs) outright — the identity `aimo-0680`
relies on simply is not present in this problem's data, unlike in `aimo-0680` where it is a *given
hypothesis*, not something to derive.

### Step 3 — why no repaired/localized version of the identity can bypass the shared wall

One might hope to restrict attention to a well-chosen infinite subsequence (rather than all index
pairs) and manufacture a growing-divisor identity there instead. We examined the natural candidate
supplied by the outline and show it collapses to the same open difficulty the rest of the population
already isolated, rather than avoiding it.

**Candidate identity.** Fix $D\in R$ with $I_D:=\{n\ge N_1:D_n=D\}$ infinite (guaranteed for at
least one $D\in R$ by pigeonhole on the finite set $R$, exactly as in Proposition 2's proof but
using the $D_n$-partition instead of the residue partition). For $i<j$ both in $I_D$, is there a
divisibility relation between $j-i$ and $a_j-a_i$ analogous to hypothesis (i)?

**Proposition 4 (the candidate identity is exactly as strong as No-Escape / determinism).**
*Suppose, for $n\ge N_1$, the recursion is deterministic on the residue mod $L_P$, i.e. suppose the
No-Escape property holds: $a_{n+1}=y_{n+1}:=\min\{x>a_n:x\bmod L_P\in G\}$ for every $n\ge N_1$ (the
open Lemma 6 of `core-signature-pigeonhole`/the open Antichain-Stabilization-dependent claim of
`antichain-signature-closure`). Then a growing-divisor-type identity for $I_D$-pairs is
**automatically available for free, without any further work**, via the deterministic finite-state
map $r_n\mapsto r_{n+1}=f(r_n)$ of `lemmas/periodicity-given-no-escape.md`: the sequence $(r_n)_{n\ge
N_1}$ is eventually periodic with some period $T\mid|G|!$ (in fact $T\le|G|$, by the pigeonhole
argument already certified in that lemma), and $a_{n+T}-a_n$ is then *constant* (call it $L$) for
all large $n$ — which already IS the conclusion of the whole theorem, not merely an intermediate
identity. Conversely, if no such deterministic recursion is granted, we show below that no weaker,
purely index-gap-based divisibility fact can be derived from (G) and pigeonhole alone.*

*Proof of the converse direction (the identity cannot be manufactured "from below," i.e. without
first assuming determinism).* Suppose we try to derive $(j-i)\mid a_j-a_i$, or any relation
$c(j-i)=a_j-a_i$ for a function $c$ not depending on $n$, for $i,j\in I_D$ directly from the
problem's definition and (G) alone (i.e. without assuming No-Escape). The only facts available about
$a_j-a_i$ for $i,j\in I_D$, $i<j$, from the certified machinery are:
1. $a_j-a_i\le(j-i)L_0$ (telescoping (G)) — an *upper* bound linear in $j-i$, with no matching lower
   bound or exact residue behaviour;
2. $a_j\equiv a_i\pmod{L_P}$ is **not** implied merely by $D_i=D_j=D$ (matching $P$-signature is a
   coarser condition than matching residue mod $L_P$: many residues $r,r'\in\mathbb Z/L_P\mathbb Z$
   can share the same $P$-signature $\pi(r)=\pi(r')=D$ without $r=r'$ — e.g. for $P=\{2,3,5\}$,
   $L_P=30$, residues $r=6$ and $r=12$ both have $P$-signature $\{2,3\}$ but $6\ne12\pmod{30}$), so
   even $L_P\mid a_j-a_i$ is not available from $D_i=D_j$ alone — only from Proposition 2's
   independent (coarser-partition) pigeonhole.

Neither fact ties $j-i$ (an *index* gap) to any divisor of $a_j-a_i$ (a *value* gap): fact 1 bounds
the value gap by a multiple of $L_0$, a fixed constant, not something the index gap must exactly
divide; and no certified or provable fact in the population ties the number of *steps* between
recurrences of $D$ to any exact residue behaviour of $a_j-a_i$, because — unlike `aimo-0680`, where
$f$ is a single fixed function applied repeatedly (so "apply $f$, $y-j$ times, starting from
$f^j(a_x)$" is a well-defined operation with an a priori integrality guarantee by hypothesis (i)) —
our recursion's defining rule changes at every step: $a_{n+1}$ is defined relative to the *entire*
constraint set $\{a_1,\dots,a_n\}$, which grows by one constraint at each step, so there is no
fixed map $g$ with $a_{n+1}=g(a_n)$ valid for all $n$ (that would be precisely the No-Escape
property, established only once, not built into the problem's data the way `aimo-0680`'s hypothesis
(i) is). Hence any identity of the required shape can only be extracted *after* first pinning down
that the recursion is eventually governed by a fixed finite-state map — i.e., after essentially
proving No-Escape / Antichain-Stabilization directly. $\blacksquare$

### Conclusion of this round's finding

Propositions 3–4 together show that the `aimo-0680` transplant, as scoped by the outline, is not a
mechanism that can close the theorem *independently* of the CRT-covering/antichain-stabilization
wall the rest of the population is already fighting: concretely, (a) the literal identity fails by
direct counterexample (Proposition 3), and (b) any repaired, localized version of it that could
plausibly work is provably *at least as strong as* — in fact stronger than, since it would already
hand back the theorem's conclusion — the open determinism property (Proposition 4), so it cannot
be established "for free" or by a shortcut; it would have to first establish essentially the same
fact the other two approaches in the current build set (`antichain-signature-closure`,
`dilworth-antichain-bound`) are directly attacking. This is a genuine, useful negative result: it
tells the population that a 4th technique variant chasing this specific crux transplant is not a
profitable direction, and it should not be re-attempted verbatim in a future round without a new
idea for supplying the missing growing-divisor identity from some other source than the greedy
recursion's own step-by-step definition.

What remains fully open, for the whole problem: exactly the same as the rest of the population —
either the No-Escape property (`core-signature-pigeonhole`'s Lemma 6) or the equivalent Antichain
Stabilization property (`antichain-signature-closure`'s step 3). No progress toward *closing* that
gap was made by this approach; the contribution is the negative result above (why this specific
transplant cannot bypass it) plus the two small, fully proved pigeonhole facts (Propositions 1–2),
which are cheap corollaries of already-certified lemmas and not independently load-bearing for any
future argument that this round's work identified.

## Full proof
(Not applicable — Status is partial. This approach did not produce a complete proof of the theorem;
its contribution is a rigorous negative result ruling out a specific proposed mechanism, recorded
above.)

## Promotable lemmas

None with independent reuse value beyond what is already certified: Propositions 1–2 are one-line
corollaries of `lemmas/gap-bound.md` and `lemmas/signature-stabilization-and-crt-sufficiency.md`
respectively and do not warrant a separate lemma file. Proposition 3 (concrete disproof of
$(j-i)\mid a_j-a_i$) and Proposition 4 (the candidate identity is no weaker than No-Escape) are
negative/diagnostic results specific to this approach's dead mechanism, not reusable building blocks
for a positive proof; they are recorded here for the record (so no future round re-attempts the
literal `aimo-0680` transplant) rather than proposed for certification.
