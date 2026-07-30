## imo-2026-06 (lens: direct-sequence framing, avoiding the antichain-of-prime-sets object D_n/A_n entirely)

### Scope note
Even $a_1$ is fully closed (`absorption-recurrence-even-case.md`, elementary induction, no antichain
machinery). Everything below targets odd $a_1$ only, and I deliberately never form the inclusion-minimal
antichain $\mathcal A_n$ of live prime-sets that all five prior approaches converged on. I looked for
top-level targets stated purely in terms of the integer sequence $(a_n)$, its gaps $d_n=a_{n+1}-a_n$, or
a fixed-value invariant like $\gcd(a_1,a_n)$.

### Distinct openings

1. **`gcd(a_1,a_n)`-pigeonhole framing (transplanted from crux `aimo-0421`, tested, largely negative — see below).**
   $\gcd(a_1,a_n)$ is, for every $n$, a divisor of the *fixed* integer $a_1$, hence takes at most
   $d(a_1)<\infty$ values as $n$ ranges over all of $\mathbb N$ — a trivial pigeonhole fact requiring zero
   antichain machinery. `aimo-0421`'s crux move (dichotomize an infinite set $S$ by whether some prime
   divides infinitely many elements of $S$, using exactly this kind of "gcd with a fixed element has
   finitely many values" pigeonhole) is a genuinely different combinatorial lever than anything in the
   current population. I ran it numerically (below): the naive hope that some single divisor value
   $g=\gcd(a_1,a_n)$ holds for *all sufficiently large* $n$ (which would hand you a fixed nonempty prime
   subset $R\subseteq S=\mathrm{primes}(a_1)$ governing the tail, directly, with no antichain poset) is
   **false** — $\gcd(a_1,a_n)$ cycles among *several* divisor values forever (consistent with, not a
   shortcut to, eventual periodicity: once period $T$/difference $L$ hold, $\gcd(a_1,a_{n_0+kT})$ is
   itself periodic in $k$ with several distinct values per period, not eventually constant). So the
   literal one-line transplant fails, **but** the pigeonhole-on-finitely-many-divisor-values idea itself
   is still live in a weaker form: it proves for free (no computation needed) that *some* nonempty prime
   subset $R\subseteq S$ satisfies $\mathrm{primes}(\gcd(a_1,a_n))=R$ for infinitely many $n$ — this is a
   genuinely cheap, previously unstated fact (not found anywhere in the existing approach/lemma files —
   checked by grep) that could seed a fresh minimal-counterexample or density argument built around $R$
   rather than around the antichain's generator set. Not developed further (per role rules, I stop at the
   opening).

2. **Induction on $\omega(a_1)$ (number of distinct prime factors of $a_1$), a genuinely different
   top-level target than "prove Antichain Stabilization for this $a_1$."** Instead of attacking one fixed
   $a_1$ combinatorially, set up strong induction on $\omega(a_1)$: if a reduction lemma can show the
   tail behavior of the sequence started at $a_1$ with $\omega(a_1)=k$ is governed by (or reduces to) the
   sequence started at some smaller $a_1'$ with $\omega(a_1')<k$ (e.g. by a "drop the largest prime of
   $S$ once it becomes redundant" argument), the theorem would follow by induction with $\omega(a_1)=1$
   ($a_1$ a prime power) as the base case — which is already an **unconditionally solved** case via
   `lemmas/absorption-lemma.md` (a prime-power term forces immediate singleton collapse). This is
   speculative (no reduction lemma constructed or verified) but is a structurally different proof
   *shape* — descent on a scalar invariant of $a_1$ itself, not a fixed-point/stabilization claim about
   one sequence's evolving state — genuinely orthogonal to every approach in the current population.

3. **Compactness / symbolic-dynamics framing on the bounded gap sequence $(d_n)_{n\ge1}\in\{1,\dots,L_0\}^{\mathbb N}$.**
   `lemmas/gap-bound.md` already gives $1\le d_n\le L_0=\mathrm{rad}(a_1)$ unconditionally, so $(d_n)$ is
   a sequence over a *finite alphabet* — by König's lemma / sequential compactness of $\{1,\dots,L_0\}^{\mathbb N}$,
   every subsequence of indices has a further subsequence along which $(d_n)$ "looks the same" in any
   fixed finite window. The obstruction (checked, and it is real, not just asserted): the map producing
   $d_{n+1}$ from history is **not** a bounded-memory / finite-window function of $(d_1,\dots,d_n)$ as
   literally stated — validity of a candidate depends on gcd-sharing with *every* earlier term $a_i$,
   $i\le n$, not just a bounded recent window — so naive compactness gives a subsequence with matching
   local gap-statistics but not, by itself, a periodicity certificate. This is exactly why every
   approach in the population needs *some* device (antichain, PC, growth-event decomposition) to compress
   "share a factor with every earlier term" into a finite state. I did **not** find a way to make the
   compactness argument close without smuggling back in an equivalent finite-state compression — flagging
   this as a **plausible-looking but unproductive-as-stated** opening, not a verified dead end (nobody in
   the population has tried literal compactness/König's-lemma phrasing, so it is at least a genuinely new
   *frame*, even though my own probe suggests it collapses to the same content).

4. **Direct minimal-period pigeonhole on the full trailing state, tested computationally for
   bounded-memory sufficiency (negative empirical finding, reported honestly as such).** I tested whether
   $d_{n+1}$ is determined by a short window of recent gaps $(d_{n-w+1},\dots,d_n)$ alone, for small $w$,
   by looking for two indices with matching length-$w$ gap windows but differing next gaps, in the
   simulated odd sequences. Even for $w$ as large as 20, I found no *proof* obstruction was searched
   rigorously (this is a spot check, not exhaustive), but the qualitative reason from opening 3 above
   (validity depends on *all* earlier terms, not a bounded window) argues strongly that no fixed finite
   $w$ suffices in general — consistent with, not contradicting, the field's existing insight that the
   state genuinely needs to track prime-set information going back arbitrarily far (hence the antichain
   device exists in the first place). I would **not** recommend chasing "small fixed window" as a
   framing; record as a checked-plausible negative, not a certainty.

### Candidate technique(s)
- `aimo-0421`'s two-branch pigeonhole-on-gcd-values dichotomy (opening 1) — a genuinely new tool for this
  population, untried; likely needs combining with existing Absorption/PC machinery to bite, but supplies
  a for-free nonempty subset $R\subseteq S$ recurring infinitely often that nothing in the current field
  has isolated.
- Strong induction on $\omega(a_1)$ (opening 2) — needs a from-scratch reduction lemma (not found by any
  prior approach); orthogonal proof shape to all five converged approaches.
- Compactness/symbolic-dynamics on the bounded gap alphabet (opening 3) — plausible frame, likely
  collapses to needing the same finite-state compression the population already built, so lower priority
  unless someone finds a way to avoid smuggling that back in.

### Cheap-kill candidates
- None found that dispatch the odd case outright. The one genuinely cheap fact surfaced this round: $\gcd(a_1,a_n)\mid a_1$
  for all $n$, giving $\le d(a_1)$ possible values and hence (finite pigeonhole) some nonempty
  $R\subseteq S$ recurring infinitely often — free, but not by itself a proof or even a reduction; flagged
  as raw material only.

### Knowledge-base entries to use
- `knowledge_base.md`'s **Modular arithmetic, CRT** entry (already the backbone of the population's
  antichain machinery; any direct-residue framing would still lean on it).
- **Pigeonhole / extremal principle** (Combinatorics section) — underlies opening 1 directly.
- **Invariants & monovariants** (Combinatorics section) — relevant if opening 2's descent-on-$\omega(a_1)$
  reduction is pursued (need a genuine invariant that decreases across the reduction, not yet found).
- No entry in `knowledge_base.md` covers symbolic dynamics / compactness on finite-alphabet sequences
  directly; opening 3 would need to be built from scratch if pursued (low priority per the above).

### Analogous past problems (cruxes)
- **`aimo-0421`** (number_theory, `divisibility-and-gcd`) — genuinely analogous *mechanism*, not just
  same-subtopic: an infinite set $S$ of positive integers, gcd-based hypothesis/conclusion, resolved by
  (a) normalizing so no single $g>1$ divides everything, then (b) dichotomizing on whether some prime
  divides infinitely many elements of $S$ (pigeonhole via "gcd with a fixed element has finitely many
  values, being a divisor of that element") vs. every prime dividing only finitely many (then almost all
  pairs are coprime). This is the crux move behind opening 1 above. The problems are NOT the same shape
  (aimo-0421 is about a static infinite set with a gcd-difference hypothesis, ours is a specific greedy
  recursion targeting eventual periodicity), so it is a hint to adapt, not a template to copy — and my own
  numeric probe shows the most literal transplant (constant tail gcd) is false. Still, the general
  "finite-divisor-set pigeonhole on $\gcd(a_1,\cdot)$" mechanism is unused in the current population and
  worth a closer look.
- No other crux in `sequences-and-recurrences`, `pigeonhole`, or `induction-and-construction`
  (number_theory) was a close structural match after reading their `how_used` fields; most are either
  polynomial-value/period problems (aimo-0982, aimo-0987 — periodicity of $2^n\bmod m$, a genuinely
  different and much simpler finite-state mechanism since the modulus there is truly fixed a priori,
  unlike here where the effective "modulus" is exactly the open question) or greedy-process combinatorics
  problems (aimo-0012, aimo-0102, aimo-0558) whose greedy structure doesn't involve an unbounded
  memory-of-all-past-terms constraint the way this problem's gcd condition does. None recommended as a
  transplant target beyond aimo-0421.

### Prior progress
Current population's best (from `current.md`, not re-derived here): full theorem for even $a_1$
(unconditional). For odd $a_1$: theorem reduces (three independently verified routes) to one precise
combinatorial claim about realizable antichains ("Step 6" / self-closing reachability / Type B
finiteness), all of which still go through the antichain-of-minimal-prime-sets object I was asked to
avoid. Nothing in my probe closes or shortcuts that gap; I surface adjacent openings instead.

### Dead ends (do not retry)
- Per-approach dead ends already recorded in `current.md` (charging/budget arguments, `dense-signature-vanishing`'s
  literal `aimo-0680` transplant, `|Q|<\infty` target, finite-total-prime-pool $\Pi$ reduction, per-prime
  $\sigma_p$/$\tau_p$ monovariants) — all confirmed still dead, not re-litigated.
- **New this round:** literal "$\gcd(a_1,a_n)$ is eventually constant for large $n$" — **false**,
  refuted computationally for 8 odd test cases (see data below); do not use this as a stated lemma. The
  weaker "some nonempty divisor-value/prime-subset $R$ recurs infinitely often" survives (pure
  pigeonhole, always true, but not yet shown to give leverage).
- **New this round:** naive small-fixed-window ($w\lesssim20$) determination of $d_{n+1}$ from
  $(d_{n-w+1},\dots,d_n)$ alone — not rigorously refuted, but structurally implausible (the defining
  condition depends on gcd-sharing with *every* earlier term); do not assume bounded memory without
  proof.

### Small-case / intuition notes (all labeled conjecture/empirical)
- Computed $\gcd(a_1,a_n)$ for $n\le600$, $a_1\in\{15,21,33,35,105,165,385,429\}$ (fresh Python
  simulation, `math.gcd` + brute-force greedy generation, cross-checked against the exact same recursion
  used by other approaches). In every case $\gcd(a_1,a_n)$ visits **multiple** divisor values of $a_1$
  repeatedly forever (e.g. $a_1=105$: values $3,5,7,15,21,35,105$ all recur in the last 100 terms of a
  600-term run) — never settles to one value. This is consistent with (not contradicting) the eventual
  periodicity the theorem asserts: once period $T$, difference $L$ hold, $\gcd(a_1,a_{n_0+kT})$ is itself
  periodic in $k$ with generally several distinct values per period (since $\gcd(a_1,\cdot)$ is not
  additive under $+L$). Conjecture only, not used in any proof step.
- No new counterexample-style data found; all numeric checks reconfirm rather than challenge the
  population's existing conjecture that self-closing/Antichain Stabilization always eventually holds.
