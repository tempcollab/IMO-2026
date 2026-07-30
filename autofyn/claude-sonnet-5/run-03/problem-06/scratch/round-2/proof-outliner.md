## imo-2026-06

### Cross-cutting note for this round
Both explorers agree the old "No-Escape relative to P = {primes ≤ rad(a_1)}" formulation
(`core-signature-pigeonhole` Lemma 6) is strictly weaker than necessary: it truncates to an
a-priori bounded prime set and then has to separately rule out "escapes" via primes outside that
set. Using the **exact, untruncated antichain** of live constraints (already characterized exactly
by the certified `lemmas/constraint-domination.md`) collapses sufficiency and necessity into ONE
statement with no secondary gap. This is a genuine strict improvement, not a re-patch with a
"slightly different finite prime set" (the thing the round-1 memory rule forbids) — it removes a
whole proof step, it doesn't just relabel P. Because of this, `growth-bound-density` (which already
owns the Constraint Domination lemma but never built the full CRT/periodicity machine on top of it)
is now subsumed by the revised `core-signature-pigeonhole` chain below; it is left out of this
round's build set to avoid two approaches chasing the identical target claim (per the CLAUDE.md
diversity rule), but its certified lemmas remain reusable and it stays in the population unmodified
(available to revive later if a genuinely different repair is found for it specifically).

The `windowed-witness-bound` fact found by the minimal-counterexample explorer (any prime
$q>L_0=\mathrm{rad}(a_1)$ divides at most one integer in any window $(a_n,a_n+L_0]$) is fully
proved, cheap, and reusable by any approach that needs to bound how "large-prime escapes" can pile
up; it should be certified to `lemmas/windowed-witness-bound.md` this round regardless of which
approach ends up using it (both `antichain-signature-closure` and `dense-signature-vanishing` can
cite it).

---

antichain-signature-closure: revise (was `core-signature-pigeonhole`)
Target: There exist positive integers $T,L$ such that $a_{n+T}=a_n+L$ for every positive integer
$n$ (the full theorem).
Technique: Same overall spine as `core-signature-pigeonhole` (pigeonhole + CRT + periodicity of a
finite-state map), but re-targeted so the CRT modulus is built from the **exact** antichain of live
constraints (via the certified Constraint Domination lemma) instead of the truncated
$P=\{\text{primes}\le L_0\}$. This eliminates the separate "No-Escape" step entirely — sufficiency
and necessity become the same statement by construction.
Skeleton:
  1. Reuse `lemmas/gap-bound.md`: $a_{n+1}-a_n\le L_0=\mathrm{rad}(a_1)$ for all $n$ — unconditional,
     already certified.
  2. Reuse `lemmas/constraint-domination.md`: for each $n$, the system of constraints
     $\{\gcd(y,a_i)>1: i\le n\}$ is *logically equivalent* (not just "usually equivalent") to the
     sub-system indexed by the inclusion-minimal elements of $\{\mathrm{primes}(a_1),\dots,
     \mathrm{primes}(a_n)\}$ — call this the antichain $\mathcal A_n$ (as a set of *indices*
     realizing the minimal prime-sets, so $\mathcal A_n\subseteq\{1,\dots,n\}$).
  3. **Key new lemma — Antichain Stabilization** (the sole open gap): there exists $N^\*$ such that
     the antichain $\mathcal A_n$ (as a set of prime-sets, i.e. which minimal prime-sets are
     currently "live") is unchanged for all $n\ge N^\*$ — equivalently, no index $n>N^\*$ ever
     introduces $a_n$ whose prime set is $\subseteq$-incomparable to every currently-live minimal
     set (a "growth event"), from $N^\*$ on. — by a counting/charging argument (see Key lemmas
     below); NOT by a naive monovariant (antichain size is proved non-monotone by simulation:
     $a_1=2310$ peaks at antichain size 268 before collapsing to 1).
  4. Given step 3, let $\{i_1,\dots,i_k\}$ be the (now fixed, finite) set of indices realizing the
     stabilized antichain's generators, and define $P^\*:=\bigcup_{j=1}^k\mathrm{primes}(a_{i_j})$
     (finite, since $k$ is finite and each $a_{i_j}$ is a fixed integer with finitely many prime
     factors — no truncation by size, unlike the old $P=\{\text{primes}\le L_0\}$). By step 2, for
     $n\ge N^\*$, $C_{\mathrm{true}}(x,n) \iff \gcd(x,a_{i_j})>1$ for all $j=1,\dots,k$
     $\iff$ ($x\bmod L_{P^\*}$) shares a prime of $P^\*$ with each $D_{i_j}:=\mathrm{primes}(a_{i_j})$
     — an EXACT (not merely sufficient) CRT characterization by the Chinese Remainder Theorem, since
     $C_{\mathrm{true}}(x,n)$ for $n\ge N^\*$ depends only on the finitely many *fixed* generators,
     not on $n$ at all.
  5. Import `lemmas/periodicity-given-no-escape.md` **verbatim**, instantiated with $P:=P^\*$: its
     hypothesis (No-Escape, i.e. $a_{n+1}=y_{n+1}$ for all $n\ge N_1$) is now **automatically true**
     by step 4 — there is no approximation left to escape from, since $G$ built from $P^\*$ *is*
     the exact validity condition, not a sufficient-but-not-necessary one. This is the crux
     simplification: the lemma's generic proof already handles the finite-state pigeonhole
     (existence of $T,L$) once $G$, $L_{P^\*}$ are fixed; only the *hypothesis-discharge* step
     changes (trivial now, vs. an open conjecture before).
  6. Conclude $a_{n+T}=a_n+L$ for all $n\ge1$ exactly as in the certified lemma's bookkeeping tail.
Key lemmas (claim + mechanism):
  - **Antichain Stabilization** (step 3) — because: (charging argument, to be completed by the
    builder) each growth event at index $n$ requires $a_{n+1}$ to simultaneously (i) lie within
    $(a_n,a_n+L_0]$ (the fixed window, Lemma `gap-bound.md`) and (ii) be incomparable to every one
    of the currently $k$ live generators, i.e. contain at least one NEW prime not already forcing
    comparability with any generator, while still being $\le$ the "boring" always-valid candidate
    (the next multiple of $L_0$). Since an integer $\le a_n+L_0$ has $O(\log a_n)$ distinct prime
    factors, and each growth event effectively "spends" prime-factorization budget to become
    incomparable to a growing antichain, there is a counting tension between $k$ (antichain size)
    growing and the bounded number of factorization slots available in a bounded window — this is
    the "witness debt" charging scheme the round-2 explorer scouted but did not complete; it is the
    concrete mechanism the builder should attempt first.
  - Fallback mechanism if charging stalls: the Dilworth/covering-style antichain bound (crux
    `aimo-0716`) — cover the poset of achievable prime-sets by chains determined by which
    generator's primes they extend, and bound the antichain by the number of chains needed; flagged
    by the explorer as needing real adaptation (the window's arithmetic content changes with $n$), not
    a direct transplant.
Open gaps: Step 3 (Antichain Stabilization) only — everything else (steps 1,2,4,5,6) is either
already certified or is a mechanical consequence once step 3 is granted, with **no residual gap**
(unlike the old No-Escape formulation, which needed a *separate* sufficiency-vs-necessity check even
after signature stabilization).
Cases to cover: none beyond the general argument (no casework on $\omega(a_1)$ needed at the outline
level; the explorer's data shows transient length scales with $\omega(a_1)$ but the *proof* need not
case-split on it, since $N^\*$ is just "some finite number").
Watch out for: (1) do not conflate "antichain size stabilizes" with "antichain size is monotone" —
it is NOT monotone (verified by simulation); the stabilization claim is only about the antichain
becoming constant *eventually*, not about it being non-decreasing along the way. (2) The charging
argument must account for a growth event that simultaneously causes several old generators to become
dominated (collapse), not just adds one new element — the observed sharp collapses (588→1) show a
single index can remove many antichain elements at once, so "count growth events" and "count net
antichain size change" are different quantities; the charging scheme should count *events*, not net
size. (3) Verify $P^\*$ is well-defined only once $N^\*$/the generators are fixed — do not attempt to
define $P^\*$ before Antichain Stabilization is proved, since the generator set can still change
before $N^\*$.

---

dense-signature-vanishing: new
Target: There exist positive integers $T,L$ such that $a_{n+T}=a_n+L$ for every positive integer
$n$ (the full theorem) — via a genuinely different top-level mechanism from CRT-covering/
antichain-closure: a **pigeonholed bounded-difference-quotient + forced-vanishing** argument,
transplanted from crux `aimo-0680` (IMO SL 2015 N4).
Technique: Partition (using the *already-certified*, cheap part of the machinery — signature
stabilization on a fixed finite $P\supseteq\mathrm{primes}(a_1)$, e.g. $P=\{\text{primes}\le L_0\}$
from `lemmas/signature-stabilization-and-crt-sufficiency.md`, reused only as a partitioning device,
NOT as the closing mechanism) the tail of indices into finitely many recurring $P$-signature
classes. For each class that recurs infinitely often, derive an integer-valued difference quotient
between consecutive occurrences that is a priori bounded, pigeonhole it to a single fixed value on
an infinite subsequence of that class, then use the "bounded quantity forced to be divisible by an
unboundedly large number ⟹ it vanishes" trick to upgrade "true on an infinite subsequence" to "true
for ALL sufficiently large indices" — closing the gap WITHOUT ever fully ruling out individual
"escapes" one at a time (the thing that stalled `core-signature-pigeonhole`'s Lemma 6 and the
literal minimal-counterexample attempt).
Skeleton:
  1. Fix $P=\{\text{primes}\le L_0\}$, $L_0=\mathrm{rad}(a_1)$, and let $D_n:=P\cap\mathrm{primes}(a_n)$
     be the $P$-signature of $a_n$ (as in the certified stabilization lemma). By
     `lemmas/signature-stabilization-and-crt-sufficiency.md`, $\{D_1,\dots,D_n\}$ stabilizes to a
     fixed set $R$ for $n\ge N_1$ — reused verbatim, no new proof needed.
  2. For each $D\in R$, let $I_D:=\{n\ge N_1 : D_n=D\}$. Since $R$ is finite and every $n\ge N_1$
     belongs to exactly one $I_D$, at least one $I_D$ is infinite (pigeonhole on a finite partition
     of an infinite set — trivial but load-bearing).
  3. **Key new step (the actual content, currently a gap):** for $D\in R$ with $I_D$ infinite, show
     that for $i<j$ both in $I_D$, the quantity $\beta(i,j):=(a_j-a_i)/(j-i)$ — or a better-chosen
     analog if this ratio is not naturally integral — takes only finitely many values as $i,j$ range
     over $I_D$ with $j-i$ large, by combining: (a) the gap bound $a_{n+1}-a_n\le L_0$ (so
     $a_j-a_i\le(j-i)L_0$, giving an a priori upper bound on any such ratio), and (b) a divisibility
     identity to be manufactured (the "creative step" the explorer flagged as missing): e.g. show
     that once $D_n=D$ recurs, $a_n\bmod L_P$ (for $L_P=\mathrm{lcm}(P)$) also eventually recurs on a
     sub-subsequence, giving $j-i \mid$ (some bounded quantity built from $a_j-a_i$ and the fixed
     modulus $L_P$) — analogous to `aimo-0680`'s $d\mid f^d(m)-m$. This divisibility identity does
     NOT yet exist for our recursion and must be derived from scratch; it is the open gap.
  4. Given step 3's finitely-many-values conclusion, pigeonhole again: some fixed value $\beta^\*$ is
     taken by $\beta(i,j)$ for infinitely many pairs $(i,j)$ with $i,j\in I_D$. Apply the
     `aimo-0680` vanishing trick: for two such pairs with a common $i$ but arbitrarily large $j-j'$,
     the bounded difference $\beta(i,j)-\beta(i,j')$ (bounded because both lie in the finite value
     set from step 3) must be divisible by an unboundedly growing quantity (built from $j-j'$), so it
     is exactly $0$ — forcing $\beta(i,j)=\beta^\*$ for ALL sufficiently large $j\in I_D$, not just
     infinitely many. This upgrades "true infinitely often" to "true cofinally" for free, exactly the
     upgrade the other approaches could not get past.
  5. Repeat step 4 for every $D\in R$ with $I_D$ infinite (there are only finitely many such $D$,
     since $R$ is finite); combine the resulting eventually-linear behavior on each class to get
     $a_{n+T}=a_n+L$ for $n$ large, where $T=\mathrm{lcm}$ of the periods forced on each class and
     $L$ the corresponding total shift — then extend to all $n\ge1$ by the same finite bookkeeping
     tail as `lemmas/periodicity-given-no-escape.md`.
Key lemmas (claim + mechanism):
  - Pigeonhole on signature classes gives an infinite recurring class (step 2) — trivial, finite
    partition of an infinite set.
  - **The manufactured divisibility identity** (step 3) — this is the load-bearing, NOT-yet-found
    piece; the mechanism must come from the structure of the greedy recursion itself (candidates for
    the identity: the recursion $a_{n+1}=a_n+\delta(a_n\bmod L_P)$ once signatures stabilize, so
    consecutive returns to the same residue class force $a_j-a_i$ to be a sum of $\delta$-values
    over a cycle — worth checking directly whether this sum is forced into a fixed residue mod
    $(j-i)$ or similar).
  - Vanishing-by-unbounded-divisibility (step 4) — because a bounded integer divisible by
    arbitrarily large numbers must be $0$ (standard fact, the `aimo-0680` crux move).
Open gaps: Step 3 (manufacturing the divisibility identity) is the ENTIRE open content; steps 1-2 are
already certified/trivial, and steps 4-5 are mechanical once step 3 is granted (this mirrors how
`antichain-signature-closure` isolates its own single gap, but the two approaches' gaps are
different in kind — one is a counting/charging claim about antichain growth events, the other is an
algebraic/divisibility claim about return times — so they do not share a wall).
Cases to cover: none at outline level; the class-by-class argument (step 5) already handles all of
$R$ uniformly.
Watch out for: (1) `aimo-0680`'s identity $d\mid f^d(m)-m$ came from an *iterated function*
structure (orbits of $f$); our recursion is only piecewise-linear/deterministic *after* signature
stabilization, so the analog must be derived, not assumed — do not let a builder simply assert
"by analogy with aimo-0680" without deriving the actual divisibility fact for THIS recursion. (2) the
explorer's numerical check of "recurrence gap boundedness" for signature classes was inconclusive
(gaps up to 300-580 out of 800 terms, not obviously converging, measured with a slow simulator) — a
builder relying on any boundedness claim here should re-verify with a fast bitmask simulator before
assuming it, per the standing memory rule.

---

dilworth-antichain-bound: revise (was `covering-construction-induction`, previously unbuilt/empty)
Target: There exist positive integers $T,L$ such that $a_{n+T}=a_n+L$ for every positive integer
$n$ (the full theorem) — via a THIRD distinct mechanism for the shared Antichain Stabilization /
No-Escape target: a direct chain-covering (Dilworth-style) bound on the antichain of live prime-sets,
transplanted from crux `aimo-0716`, reformulating the problem as a poset-covering question instead
of a counting/charging or algebraic-divisibility one.
Technique: Dilworth-style chain decomposition + extremal bound on antichain size as a function of
$\omega(a_1)$, replacing `covering-construction-induction`'s original (abandoned) "explicit covering
system + minimal counterexample" plan — that plan's sub-strategy 3(b) is now superseded by
`dense-signature-vanishing` above (a cleaner version of the same idea using the crux `aimo-0680`
mechanism instead of an ad hoc contradiction), so this revision replaces it rather than duplicating.
Skeleton:
  1. Reuse steps 1-2 of `antichain-signature-closure` verbatim (gap bound, Constraint Domination,
     antichain $\mathcal A_n$ of live indices/prime-sets) — already certified, no new proof.
  2. **Key new step (the gap):** construct an explicit poset structure on the finite subsets of
     primes that can arise as $\mathrm{primes}(a_n)$ for some $n$, where two prime-sets are
     comparable if one is reachable from the other via a "cheap" (small, bounded-window) extension —
     concretely, define a chain relation using the fixed window $(a_n,a_n+L_0]$: prime-set $D'$
     *extends* $D$ if some integer with prime-set $D'$ can follow, within one greedy step, a term
     with prime-set $D$. Attempt to cover the set of all prime-sets that ever appear as antichain
     generators by finitely many chains under this relation (number of chains bounded by a function
     of $\omega(a_1)$ alone, NOT of $n$), then apply Dilworth's theorem (or the direct double-count
     analog used in `aimo-0716`) to bound the antichain's size by the number of chains — giving an
     a priori finite bound $B(\omega(a_1))$ on $\max_n|\mathcal A_n|$, from which stabilization
     follows by a simpler pigeonhole (a bounded-size antichain over a well-ordered index set that
     never revisits an already-dominated shape must stop growing after finitely many events, since
     each growth event either increases size, held below $B$, or replaces elements — bound the total
     number of *distinct antichain shapes* visited by $2^{B\cdot(\text{something})}$, finite).
  3. Given the resulting stabilization, finish exactly as in `antichain-signature-closure` steps
     4-6 (reuse `lemmas/periodicity-given-no-escape.md` with $P^\*$ from the now-fixed generators).
Key lemmas (claim + mechanism):
  - **Chain-covering bound on antichain size** (step 2) — because: the "extends" relation, restricted
    to prime-sets realizable within a single bounded-window greedy step, has bounded "width" tied to
    the number of distinct primes that can be freshly introduced in a window of length $\le L_0$
    (itself bounded by $O(\log L_0)$, since any integer in the window has $O(\log L_0)$ distinct
    prime factors) — this is the mechanism that must be made precise; the explorer flagged that the
    window's arithmetic content changes with $n$ (so the chain relation is not literally static),
    which is the genuine adaptation difficulty, not present in the geometric-poset setting of
    `aimo-0716`.
Open gaps: All of step 2 — both (a) defining a workable static/bounded version of the "extends"
relation despite the window's content changing with $n$, and (b) actually proving the chain-covering
bound $B(\omega(a_1))$. This is a substantial reformulation gap, honestly harder to scope than the
other two approaches' gaps; include it in the field for diversity (a poset/covering reformulation,
genuinely different in flavor from both the counting/charging mechanism of
`antichain-signature-closure` and the algebraic/divisibility mechanism of
`dense-signature-vanishing`), but do not expect it to close quickly — if a builder cannot even make
step 2(a) precise in one pass, that is useful negative information to report, not a failure to hide.
Cases to cover: sanity-check $\omega(a_1)=1$ (a_1 a prime power): antichain is always size 1 (only
one prime available), so $B(1)=1$ trivially — use as a base-case check that the bound formula is
non-vacuous before attempting the general argument.
Watch out for: do not let this approach silently collapse into re-deriving
`antichain-signature-closure`'s charging argument under a different name — the distinguishing content
must be the *static chain-covering bound* $B(\omega(a_1))$, not just "count growth events" restated;
if the builder finds no natural bound independent of $n$, report that explicitly as a dead end for
this specific mechanism rather than quietly switching to the charging argument.

---

growth-bound-density: no action this round (not selected)
Rationale (for the outline-reviewer, not a build instruction): its remaining open gap (antichain
stabilization) is now strictly subsumed by `antichain-signature-closure`'s cleaner reduction (same
target claim, but the revised approach has already built the full CRT/periodicity machine on top of
it with zero secondary gap, whereas `growth-bound-density` never built that machine). Building it
this round would be the exact "re-patch with a slightly different finite prime set" the CLAUDE.md
diversity rule and the round-1 memory rule warn against. Its certified lemmas (`gap-bound.md`,
`constraint-domination.md`) remain live and reusable. Leave it in the population untouched; revisit
only if a genuinely different repair (not just antichain stabilization again) is proposed for it
specifically.

monovariant-telescoping: no action this round (RETHINK from round 1, do not revive as-is)
Its target $|Q|<\infty$ is proved false; both new explorer reports reconfirm this structurally
(large primes recur constantly but are never the *unique* witness — recurrence and necessity are
different, and only necessity is the right invariant). Its certified lemmas (Q-cover,
`q-cover-and-density.md`) remain reusable as background facts but are not being built on this round.
