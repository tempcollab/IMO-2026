## imo-2026-06 (lens: direct attack on Step 6 / realizability structure of the greedy recursion's antichain)

### Headline finding: this problem's exact source theorem is already solved in the crux corpus

`imo-2026-06`'s greedy recursion — "$a_{n+1}$ is the smallest integer $>a_n$ with
$\gcd(a_{n+1},a_i)>1$ for all $i\le n$" — is **literally** the "good numbers" construction
described in Comment 2 of the crux corpus problem **`aimo-0030`** (IMO 2022 Problem 3, "Game of
Numbers"): "$b_0=k$; $b_{n+1}$ is the smallest $b>b_n$ coprime to none of $b_0,\dots,b_n$." Setting
$k:=a_1$, this is termwise identical to our $(a_n)$. I confirmed this by reading `aimo-0030`'s full
problem statement and both official solutions in `past_problems_database.json`/`past_crux_moves_database.json`
(query: `problem_id=="aimo-0030"`, `domain="number_theory"`).

Crucially, **Comment 4** of that solution states explicitly that the committee's original proposal
contained a harder alternative question — "(b) to show that the word $W_k$ [[[the indicator sequence
of which integers $\ge k$ are 'good']]] is periodic" — which they replaced with the (nominally weaker,
but actually all that's needed) statement they *did* prove: **"if $n,n'\ge k$ have the same set of
prime divisors $\le k$ ('similar'), then $n,n'$ are both good or both bad."** `imo-2026-06` is
precisely this harder periodicity question, restated for the year-2026 competition.

**Why the proven theorem already gives our periodicity conclusion almost for free.** If "goodness"
(membership in our sequence, up to the game-vs-greedy-sequence identification) is a function only of
a number's set of prime divisors $\le k=a_1$ ("small-prime signature"), then since that signature is
literally periodic in $n$ with period $L:=\prod_{p\le a_1}p$ (a fixed integer — adding a multiple of
$L$ changes no residue mod any prime $\le a_1$, hence changes no small-prime-divisibility), the set of
good numbers is itself periodic mod $L$ on $[a_1,\infty)$. Enumerating this periodic set in increasing
order immediately gives $a_{n+T}=a_n+L$ for **every** $n\ge1$ (not just eventually), where
$T:=\#\{\text{good numbers in }[a_1,a_1+L)\}$ — exactly the theorem's conclusion. **This is not a
formal citation** (per CLAUDE.md's rule, "every borrowed step must still be proven from scratch" — the
game-theoretic framing, the "good/bad" recursive characterization, and the identification with our
greedy-defined $(a_n)$ all need to be redone directly for our recursion, not imported), but it is a
strong, concrete **reduction target**, and — crucially — a genuinely different proof *technique* from
everything the population has tried: **Claims 1–5** of `aimo-0030`'s two official solutions supply a
template for proving the "signature classification" theorem directly, using **strong downward
induction on $\max(\cdot,\cdot)$ over similar pairs**, not the population's upward
minimal-counterexample-on-index descent.

### The key transplantable technique: purification (Claim 4)

`aimo-0030` Solution 2's **Claim 4**: for any integer $b\ge k$ having at least one prime factor $\le
k$, there is an integer $x$ *similar* to $b$ (same set of primes $\le k$ dividing it) with $b\ge x\ge
k$ and **$x$ has no prime factor $>k$ at all**. Construction: let $p$ be a small prime factor of $b$,
$a:=\prod(\text{small primes of }b)$, and $x:=p^n a$ for the least $n\ge0$ with $x\ge k$; the proof
that $x\le b$ uses precisely $k<q$ for $q$ a large prime factor of $b$ (i.e., **the threshold is
primes $\le a_1$, not primes $\le\mathrm{rad}(a_1)$** — see discrepancy note below).

This is a **direct, constructive purification** — not an abstract existence/pigeonhole argument, and
not a witness-hitting-set combinatorial claim like Step 6. It builds, from any large-prime-carrying
generator $b$, an honest *smaller* (or equal) representative with the same relevant small-prime
footprint and zero large primes. Claim 5 then uses this (via a strong-induction-on-$\max$ argument,
choosing a minimal counterexample pair $(b,b')$ of good numbers sharing only large primes) to force a
contradiction. **This is a structurally different route to PC/Antichain-Stabilization than anything
tried so far in the population** (no antichain-of-abstract-sets object, no hitting/containing witness
sets, no growth-event counting) — it works directly with actual integers and their factorizations.

### $P=\{p\le\mathrm{rad}(a_1)\}$ vs. $P=\{p\le a_1\}$ — a live discrepancy worth flagging

The current population's PC/Antichain-Stabilization framing fixes $P:=\{\text{primes}\le
L_0=\mathrm{rad}(a_1)\}$. The `aimo-0030` template naturally uses the **larger** set
$P':=\{\text{primes}\le a_1\}\supseteq P$ (since $\mathrm{rad}(a_1)\le a_1$, with equality iff $a_1$
squarefree). I ran a computational check (see below): for all odd $a_1$ tested (including
non-squarefree ones where $P\subsetneq P'$ strictly, e.g. $a_1=45,63,75,99,117,135,\dots$, up to 120
terms each), **zero violations** of "every pair of sequence terms shares a common prime $\le
\mathrm{rad}(a_1)$" were found — i.e. the *smaller*, already-adopted $P$ seems empirically sufficient
for the pairwise-sharing fact in every case checked. This does not mean $P=\mathrm{rad}(a_1)$ is
provably correct for the transplanted Claim-4/5 argument (the official proof's inequality specifically
needs $k<q$, i.e. threshold $=a_1$, not $\mathrm{rad}(a_1)$, to make the size comparison $x\le b$ work)
— but it suggests **the theorem may hold with the smaller $P$ too**, and the outliner should treat
"which $P$ is actually load-bearing" as an open sub-question when adapting Claims 4–5, not assume the
population's existing $P=\mathrm{rad}(a_1)$ is automatically compatible with the transplanted technique
without re-deriving the size inequality for it.

### Distinct openings

1. **(Primary, new this round) Transplant `aimo-0030`'s Claims 1–5 directly**, re-derived from scratch
   for our greedy-defined sequence (not via the two-player game), proving a **signature-classification
   theorem** ("validity/membership of $x\ge a_1$ in the eventual generator-relevant structure depends
   only on $x$'s set of small-prime divisors") by strong downward induction on value (not the
   population's upward index-induction), using the purification construction (Claim 4) as the core
   engine. If this closes, periodicity follows essentially immediately via the periodic-set argument
   above, **entirely bypassing PC / Antichain Stabilization / Step 6's abstract hitting-witness
   question** — a genuinely different top-level target, not a bypass-in-the-same-framing.
2. **(Secondary, narrower) Attack Step 6 itself using purification as a structural constraint on
   realizability.** Rather than trying to characterize which *abstract* antichains are realizable
   (hard, as the reviewer's counterexample shows), use Claim-4-style purification to show that any
   realized generator with a large prime factor can be "downgraded" to a same-signature witness with
   only small primes and size $\le$ the generator — this witness itself is a strong candidate for the
   very $H$ that Step 6 needs to rule out (or, if the purification witness is shown to always coincide
   with an *earlier actual generator*, this could directly resolve Step 6's Case-A/Case-B dichotomy in
   `leftover-witness-confinement.md` by strengthening Case-A back into Case-B).
3. **(Tertiary, cheap-kill hunting on realized-antichain structure)** Ran fresh computation (below):
   realized eventual antichains are **not always "complete-graph" shaped** (contra the hope in
   `leftover-witness-confinement.md`'s Step 6 point 3): e.g. $a_1=385$'s eventual antichain has 7
   blocks of mixed sizes (2 and 3), including the prime 19 (which does not divide $a_1$ but is
   $\le\mathrm{rad}(a_1)=385$). This rules out "always complete-graph" as a general realizability
   constraint — a genuine negative finding, saving a round from chasing it further.

### Important caveat: this is not simply re-running round 5's already-flagged attempt

Per `/tmp/memory/math-explorer.md` rule 13 (round 5): a **literal, local** transplant of Claim 4's
inequality (used *per step* $i$, with the sequence's own current floor $a_{i-1}$ playing the role of
$k$) was already tried and found broken, because $L_0$ (fixed split point) and $a_{i-1}$ (growing
floor) are different quantities and the required inequality $a_{i-1}<q$ fails once $i$ is large
(concrete counterexample recorded: $a_1=15$, $a_{i-1}=1009$ vs. $q=17$). **This round's proposal is
different in structure**: instead of applying purification locally at each step against the moving
floor $a_{i-1}$, the goal is to prove a single **global** classification theorem — "$x\ge a_1$'s
relevant status is determined by its signature w.r.t. primes $\le a_1$" — with the *fixed* threshold
$a_1$ playing **both** roles (split point and floor) simultaneously, exactly as in the original
`aimo-0030` game (where the floor $k$ never moves). This sidesteps the specific mismatch round 5 found,
but it is a materially different (and harder, more global) claim to set up than the local per-step
attempt, and **no proof of it exists yet** — the outliner should treat this as a fresh, unattempted
direction, not assume it inherits round 5's failure, but also not assume it is free of new obstacles;
the actual "good/bad" recursive definition from the game has no literal analog yet in our
greedy-sequence-only setup and would need to be built from scratch (e.g. via strong downward induction
on candidate value, defining "x is dominated" recursively) before Claims 1–5's proof pattern can even
be stated for our object.

### Cheap-kill candidates
- **Pairwise-sharing-at-small-prime is empirically universal** (0 violations, several $a_1$, up to 120
  terms) — worth trying to prove directly and cheaply (it's much weaker than full PC/Step 6, an easier
  first target that might already unlock the periodic-set argument if strengthened correctly).
- **"Star" realizability (all blocks share one common prime) essentially never occurs** past antichain
  size 2 — already established last round (0 occurrences among 1000+ snapshots); not a fruitful angle,
  don't re-try without new evidence.
- **"Complete-graph" realizability does NOT always hold** — confirmed false this round by direct
  computation ($a_1=385$'s 7-block, mixed-size-2/3 antichain). Do not assume general antichains reduce
  to this shape.

### Candidate technique(s)
- `aimo-0030`'s purification construction (Claim 4) + strong downward induction on value for minimal
  counterexample pairs of "similar" numbers (Claim 5's proof pattern) — the primary new technique to
  transplant.
- Knowledge-base entries: **Pigeonhole / extremal principle**, **Minimal-counterexample /
  Infinite descent** (General Proof Methods section) are the closest generic KB matches; the KB has no
  entry specific to "hitting set vs. antichain" combinatorics, consistent with why Step 6's abstract
  combinatorial framing has stalled — the KB's closest analog is really the crux corpus find above, not
  anything in `knowledge_base.md` itself.

### Knowledge-base entries to use
- **Pigeonhole / extremal principle** (`## Combinatorics`) — underlies Claim 4's "least $n$ with
  $p^na\ge k$" minimality argument.
- **Contradiction / Infinite descent / minimal counterexample** (`## General Proof Methods`) — the
  proof shape of Claim 5 (minimal violating pair by $\max(b,b')$).
- No KB entry directly covers "hitting set on pairwise-intersecting antichain" (Step 6's literal
  object) — this gap in the KB is itself a signal that Step 6's framing may not be the natural attack
  surface; the `aimo-0030` route avoids needing such a tool at all.

### Analogous past problems (cruxes)
- **`aimo-0030`** (IMO 2022 P3, "Game of Numbers") — **very strong match, arguably the source
  problem**: literally the same recursive construction (Comment 2), same open periodicity question
  (Comment 4(b)), and a full, correct, checkable two-solution proof of the closely related
  "signature-classification" theorem (Claims 1–5) that would resolve our problem's entire remaining
  content if adapted. This is the best single lead found this round by a wide margin.
- No other crux in `number_theory`/`divisibility-and-gcd`/`sequences-and-recurrences` or
  `combinatorics`/`graph-theory-and-connectivity`/`extremal-principle` (searched by keyword: coprime,
  gcd, greedy, antichain, hitting set, vertex cover, sunflower, Helly — see search log) came close to
  matching Step 6's literal hitting/containing-set combinatorics; nothing else is worth reporting as
  analogous.

### Prior progress
Per `current.md` and `/tmp/round-6/proof-reviewer.md`: even $a_1$ fully solved; odd $a_1$ reduced
(three independently-verified routes) to Step 6 — no realized, pairwise-intersecting, no-singleton
antichain admits a bounded hitting-but-not-containing witness set. Steps 1–5 of
`leftover-witness-confinement.md` are fully proved and certified; PC $\Rightarrow$ theorem and
Antichain-Stabilization $\Rightarrow$ theorem are both fully certified reductions
(`lemmas/pc-implies-theorem.md`, `lemmas/antichain-stabilization-implies-theorem.md`).

### Dead ends (do not retry)
- **Abstract antichain-only Step 6** (no realizability constraint) is false — reviewer's counterexample
  $\{1,2\},\{1,3\},\{1,4\}$ stands.
- **"Star" realizability** as an extra constraint — empirically absent from real data (0/1000+), no
  structural proof found either round; do not re-attempt without a new idea.
- **"Complete-graph" realizability as a general constraint** — this round's computation ($a_1=385$)
  refutes it as a universal shape; only usable as a special-case sanity check ($k\ge3$), not a route to
  the general claim.
- **Witness-debt / per-step charging arguments** (population-wide, multiple rounds) — proven
  non-viable (budget grows with $n$, not fixed); do not retry in any dressing.
- **Global smooth-number density scarcity** — rigorously refuted this round by
  `global-smooth-density-contradiction.md` (wrong density direction).

### Small-case / intuition notes (all conjectural except where explicitly computed)
- Verified by direct simulation (Python, `sympy.primefactors`, up to 120–400 terms per $a_1$): for
  every odd $a_1\in\{15,45,63,75,99,105,117,135,147,175,225,385\}$, **every pair of sequence terms
  shares a common prime $\le\mathrm{rad}(a_1)$** (0 violations) — this is *conjectural* evidence for a
  pairwise-sharing strengthening of PC, not a proof; consistent with, but not implying, full PC/Step 6.
- Eventual antichain shapes vary widely: singleton (absorption, $a_1=63,117$), 3-block "triangle"
  (complete-graph $K_3$, $a_1=15,45,225$), and genuinely irregular mixed-size antichains up to size 7
  with primes not dividing $a_1$ itself appearing as block elements ($a_1=385$: block $\{19,2,11\}$,
  $19\nmid385$, but $19\le\mathrm{rad}(385)=385$). This variety is why searching for one clean
  structural realizability shape (star, complete-graph) has failed twice — the `aimo-0030` route, which
  needs no such shape classification at all, looks like the more promising direction.
