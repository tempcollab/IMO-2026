# Proof-outliner report — imo-2026-06, round 3

## Read: current.md, all approaches/*.md, all lemmas/*.md, both round-3 explorer reports.

## Where the population stands (recap)
Two live, fully-reviewed reductions, both certified with **zero secondary gap**, both reduced to one
open combinatorial claim:

- `antichain-signature-closure` → **Antichain Stabilization** (equivalently, via certified
  `lemmas/self-closing-antichain-sufficiency.md`: *some $\mathcal A_N$ is self-closing*). Certified
  sufficient special case: `lemmas/absorption-lemma.md` (a prime-power term forces permanent
  singleton collapse).
- `dilworth-antichain-bound` → **P-Confinement (PC)**: every live generator's *untruncated* prime set
  stays $\subseteq P=\{\text{primes}\le L_0\}$. Proved PC $\Rightarrow$ Antichain Stabilization (PC is
  the stronger claim), certified as `lemmas/pc-implies-theorem.md`.

Dead, not to re-attempt (per current.md + both round-3 explorers, independently confirmed a third
time this round): $O(\log a_n)$ charging/witness-debt/covering-code in any dressing, Dilworth
chain-covering-by-window, aimo-0680 difference-quotient transplant, standalone "prime-power density"
target, sieve/PNT counting (same charging shape), "primes dividing $a_n$ eventually" compactness
framing (restates PC), numerical-semigroup/addition-closure transplant, finite-automaton-on-residues
framing taken alone (restates PC/No-Escape, doesn't supply new content per fresh-framing explorer §3).

Both round-3 explorers independently converge on the same diagnosis: **the wall is real content, not
an artifact of framing.** The fresh-framing explorer checked all five prescribed alternative top-level
framings and found each either equivalent to PC or a repackaging of the dead charging argument. This
is useful negative signal, not a stall — it means round 4+ should spend real effort *inside* the wall
(a direct attack on PC/Antichain Stabilization) rather than keep hunting for a bypass. But CLAUDE.md's
plateau rule still requires putting on the table this round at least one approach using a genuinely
different *mechanism* for the direct attack, not just another dressing of the antichain/CRT machinery
that both live approaches already share. I evaluate four leads (the two explorer reports proposed
four candidates) and design the round-3 field around them.

## Evaluating the four proposed leads

**Lead 1 (odd/even $a_1$ split).** The absorption-recurrence explorer's new 19-value simulation shows
a real, sharp, previously-unrecorded structural fact: **every observed absorption case has $2\mid a_1$,
and every observed non-absorption self-closing case has $a_1$ odd** (9 odd examples: 15, 105, 385,
1001, 1155, 5005, 7429, 15015, 255255, all self-close via a non-singleton antichain, none ever
produces a prime-power term). This is a genuine empirical dichotomy, not just a relabeling of one
mechanism — the two families reach stabilization via qualitatively different certified lemmas
(`absorption-lemma.md` vs `self-closing-antichain-sufficiency.md`). **Verdict: worth splitting into
two sub-approaches**, each targeting only one family with the mechanism the data suggests fits it.
This does not by itself solve anything (neither direction has a proof yet, only stronger empirical
support and a cleaner case boundary), but it narrows what each sub-argument must show and lets a
builder specialize instead of chasing one monolithic claim.

**Lead 2 (integer monovariant "$\#\{p\in P:$ not yet hit by any live generator$\}$").** I checked this
by hand against the round-2 $a_1=2310$ data already on record. At $n=893$ the antichain has $268$
generators, whose union of prime-sets covers many primes of $S=\{2,3,5,7,11\}$-generated primes... but
more importantly, at the **collapse** $n=893\to894$ (268 generators $\to$ singleton $\{\{2\}\}$), the
set of primes *covered by currently-live generators* **shrinks** from covering many primes down to
covering only $\{2\}$ — so the "not yet hit by any *live* generator" count **jumps up**, not down, at
exactly the collapse event. **This candidate is very likely false as literally stated** (collapses are
lossy: a departing generator's coverage is not preserved), exactly as the explorer flagged it should
be checked before trusting it. A repaired version that IS monotone: $\nu_n:=\#\{p\in P: p\text{ has
appeared in the prime-set of *some* generator at *some* time }\le n\}$ (cumulative, not "currently
live") is trivially non-decreasing and bounded above by $|P|$, hence eventually constant by
well-ordering — but "eventually constant" here only says the *set of primes ever used by a generator*
stabilizes, which is a restatement adjacent to PC, not obviously easier, and does not by itself rule
out further *growth events* that recombine already-seen primes into new incomparable subsets forever
(the antichain could still fail to stabilize even with a fixed prime palette, unless one also shows
the sub-lattice of subsets-of-a-fixed-finite-set argument closes — which is exactly Lemma A of
`signature-stabilization-and-crt-sufficiency.md`, already used elsewhere). **Verdict: the raw candidate
is refuted by the existing data (collapse counterexample); the repaired cumulative version is a
legitimate but different monovariant, not obviously easier than PC, and does not fold in for free.**
Worth assigning to a builder as a *targeted sub-lemma attempt* (does the cumulative "primes ever used"
set actually stabilize, and if so does that suffice?) rather than as a free win — flagged accordingly
in the skeleton below, with the collapse counterexample stated explicitly so no one re-derives the
disproved version.

**Lead 3 (finite-automaton/state-space reframing).** Both explorers independently concluded this
restates PC/Antichain Stabilization without adding new proof content (the fresh-framing explorer's §3
explicitly: "it does not supply a new argument for why the state space is finite; it just restates the
target"). **Verdict: not worth a standalone approach slug this round** — it's a useful *vocabulary* for
whichever approach eventually proves PC (eventual periodicity of a truncated-antichain walk once
finiteness is secured), but not new mechanism. I fold a pointer to it into the PC skeleton below as an
optional finishing move, not as the hard step.

**Lead 4 (per-prime divisor-chain decomposition, aimo-0477-style).** This is the one candidate both
explorers converge on as *technique*-different, not framing-different: instead of one global argument
about the antichain-of-subsets object, run $|P|=\pi(L_0)$ independent single-prime arguments and
recombine. The fresh-framing explorer is explicit that the literal transplant does not apply (no
sum-integrality forces per-prime monotonicity here, unlike aimo-0477's $d_n=\gcd(a_1,a_n)$
divisor-chain, which relies on $v_p(d_n)=\min(v_p(a_1),v_p(a_n))$ being forced nondecreasing by an
additive recurrence we don't have) — finding the right per-prime quantity is itself open. **Verdict:
this is exactly the "genuinely different mechanism" the plateau rule calls for.** It is speculative
(no monovariant candidate has been found yet, by either explorer), so it must go in as a real,
honestly-hard skeleton, not a disguised finished argument — but it attacks the object at a different
decomposition axis (per-prime, not per-antichain-subset) than every approach in the population so far,
so it satisfies CLAUDE.md's requirement without being a bypass-in-the-same-framing.

## Round-3 field

Four approaches: two copies of `antichain-signature-closure` splitting the odd/even case (Lead 1), one
continued advance of `dilworth-antichain-bound` attacking PC via the corrected cumulative monovariant
(Lead 2, honestly flagged as unproven-and-possibly-hard), and one new approach opening the per-prime
decomposition (Lead 4, the plateau-breaker). Lead 3 is folded in as a vocabulary note, not a slug.

---

### 1. `absorption-recurrence-even-case` (copy of `antichain-signature-closure`, gap-fill A)

**Target.** Antichain Stabilization for the case $2\in S=\mathrm{primes}(a_1)$, via the mechanism the
data actually shows fires in this family: eventually some term is a pure power of $2$, after which
`lemmas/absorption-lemma.md` closes the case immediately.

**Skeleton.**
1. Setup: $2\in S$. By `lemmas/gap-bound.md`, $a_{n+1}-a_n\le L_0$ for all $n$, and $2\mid$ every
   $a_n$ is *not* known a priori — this must be derived, not assumed (it is the conclusion of
   `absorption-lemma.md`(a), which itself presupposes a prime-power term already occurred; here we
   must instead show the *trigger* condition occurs).
2. **Hard step (genuinely open, not attempted by any prior approach):** show that when $2\in S$,
   some term of the sequence is eventually a pure power of $2$. Candidate sub-route: show that once the
   antichain's live generators are eventually confined to sets not all containing $2$ persistently
   growing in number (empirically antichain size climbs into the hundreds before the power-of-2 hit),
   there must exist infinitely many candidate windows $(a_n,a_n+L_0]$ containing a power of $2$, and
   argue by a counting/pigeonhole (not a fixed-budget charging argument — that shape is dead) that one
   of these windows eventually has *no smaller valid candidate available*, forcing the power of $2$ to
   be selected. This needs a genuinely new idea for *why* smaller candidates run out in exactly the
   windows containing a power of 2 — flag explicitly: simply counting available residues is the
   dead charging shape in new clothes if done naively; the builder must find why powers of 2
   specifically become forced, not just argue "eventually some window is favorable" vaguely.
3. Once a prime-power-of-2 term is established for some $m$, cite `lemmas/absorption-lemma.md`
   verbatim to finish: $\mathcal A_n=\{\{2\}\}$ for $n\ge m$, then Lemma 2/Corollary/Lemma 3 of
   `antichain-signature-closure.md` (already proved with zero residual gap) finish the theorem for
   this case.
4. **Explicitly out of scope for this slug:** the case $2\notin S$ (handled by sibling slug below).

**Honesty note for the builder:** step 2 is the entire content of this approach and is *not* a minor
gap — it is a new claim with no proof sketch yet beyond the empirical pattern (11/11 even-containing
$a_1$ trials absorbed in the round-3 simulation). If step 2 cannot be closed, report `partial` with
the trigger claim stated precisely as the residual gap (do not conflate it with the general Antichain
Stabilization claim — it is a strictly narrower, single-parity claim, which is the point of the split).

---

### 2. `self-closing-pair-density-odd-case` (copy of `antichain-signature-closure`, gap-fill B)

**Target.** Antichain Stabilization for the case $2\notin S$ (or, if the builder finds the argument
is parity-independent, state it for the complementary case to whatever Approach 1 actually covers),
via a **pair-covering density argument on primes**, distinct from any charging/budget shape: instead
of bounding how many primes a single term can introduce, argue directly about which *pairs* of primes
in $S$ (or a finite superset) must eventually co-occur in a common generator, using the fact
(certified, `lemmas/gap-bound.md` + `lemmas/constraint-domination.md`) that new generators are always
incomparable to all current ones.

**Skeleton.**
1. Cite the certified self-closing definition and `lemmas/self-closing-antichain-sufficiency.md`
   verbatim. Recall the $a_1=15$ worked example already on record: $\mathcal A_n$ stabilizes at
   $\{\{2,3\},\{2,5\},\{3,5\}\}$ — every pair from $\{2,3,5\}$ appears as (part of) a generator, and
   the antichain is self-closing because any set meeting all three pairs must contain $\ge2$ of
   $\{2,3,5\}$.
2. **Hard step (genuinely open):** formulate and prove a general claim of the shape: *for $a_1$ with
   $2\notin S$, the antichain eventually reaches a state where, for every prime $p\in S$, there is a
   live generator not containing $p$ but containing every other element of some fixed reference set* —
   i.e. directly construct/characterize the eventual self-closing antichain combinatorially (as a
   covering design on $S$, generalizing the "all pairs from a 3-set" pattern seen at $a_1=15$) rather
   than proving reachability as a dynamic limit. Check this pattern against the *other* odd examples
   already recorded by the round-3 explorer (105, 385, 1001, 1155, 5005, 7429, 15015, 255255 — note
   these do **not** all stabilize at "all pairs of $S$": e.g. $255255$ has $|S|=6$ but a final antichain
   of size $7$, not $\binom{6}{2}=15$, so the "all pairs" pattern from $a_1=15$ is a special case, not
   the general rule — the builder must find what actually determines the final self-closing set's
   shape, or prove existence without characterizing it exactly).
3. If a full characterization is too strong a target, fall back to a pure existence argument: show
   growth events cannot continue forever by a density/pigeonhole argument on *pairs* of primes from a
   provably finite candidate pool — but note (per both explorers) this again needs the pool to be
   provably finite, which is adjacent to PC. Flag honestly: this sub-target may turn out to require
   confining primes to a finite set as a lemma first (in which case it should explicitly reduce to or
   borrow from Approach 3's PC attempt, cited, not re-derived).
4. **Explicitly out of scope for this slug:** the even/absorption case (Approach 1).

**Honesty note for the builder:** the $255255$ counterexample to "self-closes at all pairs of $S$" must
be checked and reported regardless of outcome — do not silently drop it if the general pattern search
fails; report the refined empirical picture even if no proof results.

---

### 3. `dilworth-antichain-bound` (revise/advance existing slug)

**Target.** Continue attacking **P-Confinement (PC)** directly (the reduction PC $\Rightarrow$ theorem
is already certified with zero gap in `lemmas/pc-implies-theorem.md`; nothing to redo there).

**Skeleton for this round's new content.**
1. **Refuted candidate, record so it is not retried:** $\mu_n:=\#\{p\in P: p\notin D_i\ \forall
   i\in\mathcal A_n\}$ ("primes not covered by any *currently live* generator") is **not**
   monotone — it strictly increases at the $a_1=2310$, $n=893\to894$ collapse (antichain $268\to1$,
   coverage shrinks to just $\{2\}$). State this explicitly in the file so the false lead from the
   round-3 explorer report is closed out, not silently rediscovered.
2. **New candidate to attempt:** $\nu_n:=\#\{p\in P: p\in D_i\text{ for some generator index }i\text{
   that has ever been in }\mathcal A_m\text{ for some }m\le n\}$ ("primes ever used by a live
   generator, cumulative"). This is trivially non-decreasing and bounded above by $|P|$, hence
   eventually constant — **this much is free**, but the builder must determine (a) whether
   eventual constancy of $\nu_n$ is actually useful (does it imply PC, or even Antichain
   Stabilization?), and (b) if not directly, whether the *set* $P_\infty$ it stabilizes to, combined
   with the already-certified Lemma A machinery (`signature-stabilization-and-crt-sufficiency.md`,
   finite-lattice-of-subsets pigeonhole once a fixed finite prime palette is secured) closes the gap.
   Be explicit and honest if $\nu_n$'s stabilization turns out to be non-trivial to establish (a priori
   a generator could always be built from unboundedly many *distinct* primes across the infinite
   sequence, in which case $\nu_n\to|P|$ trivially but conveys nothing) or if it turns out equivalent
   in difficulty to PC itself (most likely outcome, per both explorers' diagnosis that this class of
   direct-attack lemma is the real content) — report `partial` with the precise obstruction, not an
   overclaim.
3. Optional finishing vocabulary (Lead 3, not a required step): if $\nu_n$ (or any other route) does
   secure a fixed finite prime palette for eventual generators, the remaining eventual-periodicity step
   can be phrased as "the truncated-antichain sequence is a walk on the finite state space $2^{P_\infty}$,
   hence eventually periodic by pigeonhole" — this is free once finiteness is secured (cite
   `lemmas/signature-stabilization-and-crt-sufficiency.md` Lemma A's argument shape) and needs no new
   proof, just restating already-certified content in this vocabulary if it reads more cleanly.

**Explicitly do not re-attempt:** the Dilworth/chain-covering-by-window mechanism (dead, recorded
round 2), the raw $\mu_n$ candidate (dead, established in step 1 above), any $O(\log a_n)$-budget
charging dressing.

---

### 4. `per-prime-divisor-chain-decomposition` (new — the plateau-breaker)

**Target.** A structurally independent attack on PC (or directly on Antichain Stabilization) by
decomposing the problem into $|P|=\pi(L_0)$ separate, single-prime arguments — a different
decomposition axis (per-prime) than every other approach in the population (per-antichain-subset).
This is speculative and may fail; that is acceptable and expected for a plateau-breaking slot per
CLAUDE.md — record the failure precisely if it occurs, do not force a fake win.

**Skeleton.**
1. Setup: for each fixed prime $p\in P=\{\text{primes}\le L_0\}$, define a per-prime *state*
   attached to the evolving antichain — candidates to try (not prescribed, the builder should pick
   the one that yields an actual monotone quantity, and report which ones it tried and why they
   failed if none work):
   - $\sigma_p(n):=1$ if some live generator $D_i$ ($i\in\mathcal A_n$) equals $\{p\}$ exactly (a
     "$p$-only" generator has appeared and not yet been dominated), else $0$. Ask: is $\sigma_p$
     eventually constant, and does $\sigma_p(n)=1$ for even one $p$ give a shortcut (it does: a
     $\{p\}$ generator is trivially self-closing on its own by the same argument as
     `absorption-lemma.md`, since $\{p\}\subseteq$ everything meeting it — but the question is
     whether such a *singleton* generator is forced to appear for some $p$, which is again exactly
     the even-case hard step of Approach 1; the builder should check whether this per-prime framing
     gives a genuinely new angle on that question, e.g. by looking at singleton-generator formation
     independently per prime rather than only for $p=2$).
   - $\tau_p(n):=$ the smallest generator (by $|D_i|$) among $i\in\mathcal A_n$ with $p\in D_i$, or
     $\infty$ if none. Ask whether $\tau_p$ is eventually non-increasing per prime and whether
     $\liminf$ behavior across all $p\in S$ simultaneously forces a bound on total antichain size.
   - A direct transplant attempt of aimo-0477's mechanism: is there any integrality-style constraint
     forcing $v_p$ of *something* derived from $a_n$ (not $a_n$ itself, since raw $v_p(a_n)$ is not
     obviously controlled) to be monotone? The fresh-framing explorer found no such quantity; the
     builder should either find one or state precisely, with a small worked counterexample from the
     existing simulation data, why none exists — a clean negative result here is valuable and
     publishable-quality progress even without a proof.
2. **Hard step (the whole approach, genuinely open):** find *any* single-prime quantity that is
   provably monotone (in either direction) and bounded, using only the problem's actual defining
   condition (pairwise-gcd-coprimality-to-all-predecessors), not an analogy to a different recursion's
   structure. If found, show how combining the $|P|$ per-prime facts (e.g. via a union bound or a
   simultaneous-stabilization pigeonhole) yields PC or Antichain Stabilization.
3. **Required honesty checkpoint:** if no candidate per-prime monovariant survives even a first
   sanity check against the $a_1=2310$/$a_1=15$/$a_1=255255$ data already on record, report `unsolved`
   with a precise account of which candidates were tried and why each failed (mirroring
   `dense-signature-vanishing`'s round-2 report style) — this is still valuable population diversity
   and a documented dead end per CLAUDE.md's "record everything" rule, not a wasted slot.

---

## Notes on ranking inputs for the outline-reviewer

- Approaches 1–2 (copies of `antichain-signature-closure`) each carry over that slug's already-
  certified, zero-gap machinery (Lemma 2/Corollary/Lemma 3, `absorption-lemma.md`,
  `self-closing-antichain-sufficiency.md`) for free — their *new* content is entirely the hard steps
  flagged above (the even-case absorption-trigger claim; the odd-case pair-density/characterization
  claim). Neither is a rehash of a dead mechanism; both are genuinely new sub-claims motivated by
  fresh round-3 data (the 19-value simulation), narrower and hence potentially more tractable than the
  monolithic Antichain Stabilization claim.
- Approach 3 continues the PC line with one dead candidate closed out (documented, not just dropped)
  and one new candidate ($\nu_n$) that is at minimum free progress (cumulative stabilization is
  trivially true) even if it doesn't close the gap — worth building to see how far $\nu_n$ actually
  gets, since even a partial characterization of $P_\infty$ would be new.
- Approach 4 is the required plateau-breaker: a decomposition axis (per-prime) genuinely orthogonal to
  the antichain-of-subsets machinery every other approach shares. It is the most speculative and most
  likely to end `unsolved`, but per the orchestrator's explicit plateau-breaking instruction this round
  must have it on the table regardless of predicted odds of success.
- I did not re-nominate `growth-bound-density`, `monovariant-telescoping`, `core-signature-pigeonhole`,
  `dense-signature-vanishing`, or `covering-construction-induction` for building this round — all five
  are superseded or reviewer-confirmed dead ends already recorded in `current.md`; no new information
  this round changes that assessment.

**Proposed field for outline-reviewer to rank and select a build set from:**
1. `absorption-recurrence-even-case` (copy of `antichain-signature-closure`, gap-fill A: even/absorption case)
2. `self-closing-pair-density-odd-case` (copy of `antichain-signature-closure`, gap-fill B: odd/non-absorption case)
3. `dilworth-antichain-bound` (revise/advance: PC via corrected cumulative monovariant $\nu_n$)
4. `per-prime-divisor-chain-decomposition` (new: plateau-breaking per-prime decomposition axis)
