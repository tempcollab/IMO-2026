# Scouting report: does Absorption-type collapse recur/eventually-fire? (round 3)

## TL;DR
Full prime-power **Absorption** is only the *sufficient special case* the population already has
(`lemmas/absorption-lemma.md`). It is **not** the general mechanism. New simulation (well beyond the
existing $a_1=2310$ / $a_1=15$ data points, 15+ fresh values of $a_1$, one run out to $n=30000$) shows
the *real* general phenomenon is **self-closing stabilization without full absorption**: the antichain
grows — sometimes to a large peak, non-monotonically — then permanently locks onto a small
**self-closing antichain of size $\ge 2$** (the `self-closing-antichain-sufficiency.md` mechanism, of
which absorption/singleton is only the $|\mathcal B|=1$ case). In every one of ~19 fresh trials, growth
eventually stopped and stayed stopped for thousands of subsequent terms — no counterexample to
Antichain Stabilization found — but **no density/recurrence argument for hitting a prime-power term
was found**, and I now believe chasing "prime powers recur infinitely often" specifically is close to a
dead end: most trajectories stabilize via a non-singleton self-closing set and **never produce a
prime-power term at all** in range. The right generalization to chase is "self-closing configurations
are reached with `positive-density-ish` frequency," not "prime powers occur infinitely often." I did
not find a proof; below is the terrain, the negative results, and the most promising concrete next
step (a discrete-geometry / lattice-covering reframing of self-closing, plus one crux transplant
candidate that looks more apt than anything cited so far).

## 1. What forces a term to be a pure prime power? Density argument?

Read `lemmas/absorption-lemma.md`, `lemmas/gap-bound.md`, `lemmas/constraint-domination.md`. Absorption
requires $a_m=q^e$ exactly, i.e. $\mathrm{primes}(a_m)=\{q\}$ — an extremely restrictive event (a
single-prime constraint-set at the *minimal* generator level, not just "$a_m$ has few prime factors").
There is **no known density/counting argument** anywhere in the population or in
`knowledge_base.md` for how often a greedily-selected term is a pure prime power, and I don't think one
is easy: whether $a_m$ can be a prime power depends on whether $q^e$ (for the *smallest* valid $q,e$)
happens to lie in the current forced gap-window $(a_{m-1}, a_{m-1}+L_0]$ *and* beats every other
candidate in that window — this is exactly as hard to control as the antichain's overall combinatorics,
not an independent handle. **Verdict: no positive lemma found here; this specific sub-question (density
of prime-power terms) looks like a dead end as a standalone target** — it's asking for MORE structure
than we need (full absorption) when the data shows the weaker "self-closing" event is what actually
governs almost every trajectory.

## 2. Weaker "partial absorption" / self-closing recurrence — the real mechanism, still open

This is the promising direction, and it's already exactly what `self-closing-antichain-sufficiency.md`
targets (not new, but the fresh data below sharpens what "reachability" needs to look like). Key
reframe: a self-closing antichain $\mathcal B$ is a **covering code condition** — $\mathcal B$ is
self-closing iff no finite prime-set $F$ can "hit" every $B\in\mathcal B$ without containing one of them
outright. Equivalently (dualizing), $\mathcal B$ is self-closing iff the family of complements
$\{P\setminus B : B \in \mathcal B\}$ (over the ambient prime universe) has no "partial transversal"
that misses being a full miss of some single $B$ — this is a **hypergraph covering / VC-type**
condition on the antichain, not obviously about size at all: `dilworth-antichain-bound`'s $L_0$-bounded
window argument already tried a covering-code framing and hit the same $O(\log a_n)$ per-step-budget
wall (confirmed dead per round 2 diagnosis and per `current.md`'s cross-cutting note — do not re-scout
that shape). What's *not* been tried: treating self-closing-ness as a property of a **CRT residue set**
directly (via `signature-stabilization-and-crt-sufficiency.md`'s $G\subseteq\mathbb Z/L_P\mathbb Z$) and
asking whether $G$ eventually becomes "downward closed under the greedy step" — i.e. reformulate
Antichain Stabilization as **eventual periodicity of the residue set $G_n$ mod a *fixed* modulus**,
which is a finite-state question (finitely many subsets of $\mathbb Z/L_P\mathbb Z$ for FIXED $P$, once
you're willing to over-approximate primes by $P=\{\text{primes}\le L_0\}$ as `dilworth-antichain-bound`
already does). This is basically PC again, so it doesn't sidestep the wall, but it does suggest a
concrete finite-state argument shape (see §4/knowledge_base note) that hasn't been tried: **model the
whole recursion as a walk on the finite state space $2^{2^P}$ (all possible antichains truncated to
$P$) and ask whether this walk, PROVEN deterministic given history, must enter a cycle** — see the crux
`aimo-0514` below, which is exactly this shape for a different problem and got a purely-periodic (not
just eventually-periodic) conclusion from *reversibility*. Our map is very likely NOT reversible
(distinct antichains can map to the same successor — collapse events are lossy), so we'd only get
"eventually periodic," which is fine, but proving the *state space is actually finite* requires PC
(confining generators to $P$) as a hypothesis, so this is a reformulation of PC, not a bypass. **Still,
it is a cleaner target: "the sequence of truncated antichains $(\mathcal A_n \cap P)_n$, as a walk on the
finite set $2^{2^P}\setminus\{\emptyset\}$, is eventually periodic" is a weaker-sounding claim than raw
PC and might be attackable by a pigeonhole-on-states argument if one can show the walk's transition
rule is well-defined purely as a function of the current truncated antichain (i.e. a genuine
Markov/deterministic-automaton structure) — this has NOT been checked and is worth a dedicated
approach next round.**

## 3. Crux corpus search

Searched `past_crux_moves_database.json` (2434 entries) via keyword grep on technique/how_used text for
`absorb`, `trap`, `greedy`, `eventually periodic/constant`, `stabiliz`, `confinement`, filtered to
`number_theory` and `combinatorics`, subtopics `processes-and-algorithms`, `invariants-and-monovariants`,
`extremal-principle`, `sequences-and-recurrences`. Best hits:

- **`aimo-0134`** (number_theory, `size-bounding-and-descent` / `sequences-and-recurrences`): sequence
  $a_k$ defined by "smallest nonneg residue making a running sum divisible by $k$"; prove eventually
  constant. Solution: define $b_k=\frac1k(a_1+\cdots+a_k)$, show it's a **non-increasing sequence of
  nonnegative integers** hence eventually constant by well-ordering, then recover $a_k$'s eventual
  constancy from $b_k$'s. **This is the classic "integer-valued monovariant, bounded below, hence
  eventually constant" shape** — exactly the shape a fixed-budget charging argument needs, but round 2
  already showed the natural analogue (per-step prime-introduction budget) is $n$-dependent, not fixed,
  so it does *not* transplant directly. It DOES suggest looking for a genuinely different integer
  monovariant that is honestly bounded below and non-increasing — e.g. **not** antichain size (which
  provably goes up and down, confirmed non-monotone by simulation), but something like "the number of
  primes $\le L_0$ *not yet* covered by any live generator" (this is non-increasing in $n$ within a
  fixed finite range $[1,|P|]$ once you fix $P=\{\text{primes}\le L_0\}$ — worth checking rigorously
  next round; if it's genuinely monovariant it gives PC almost for free by the aimo-0134 mechanism).
- **`aimo-0916`** (combinatorics-flavored NT, saddle-pair problem): uses "a descending chain of images
  of a self-map on a *finite* set stabilizes, then some power of the map restricted to the stable core
  is the identity." Structurally close to what we'd want for a finite-state antichain-transition map,
  but **requires the state space to be finite up front** (here, finitely many rows/columns) — for us
  that's exactly PC again. Not a bypass, but confirms the "finite state $\Rightarrow$ eventual
  periodicity of a deterministic self-map" pattern is a recognized, previously load-bearing move once
  finiteness is secured.
- **`aimo-1025`** (extremal graph closure, Mathbook problem): "run a canonical greedy version of a
  closure operation until it gets stuck; any process that reaches the full object must have this
  canonical run terminate there" + a potential function $\theta$ additive under merges with a linear
  lower bound. Interesting as a *pattern* (greedy canonicalization + additive potential with a linear
  bound) but the problem shape (finite graph, monotone edge-adding closure) doesn't match our infinite,
  non-monotone antichain process — **not a good transplant candidate**, noted for completeness.
- **`aimo-0514`** (`processes-and-algorithms`/`invariants-and-monovariants`): deterministic process on a
  finite set proven *reversible* (bijective transition map) $\Rightarrow$ purely periodic, not just
  eventually periodic. Same finiteness caveat as `aimo-0916`; also our transition (antichain $\to$ next
  antichain) is almost certainly not injective (many different $\mathcal A_n$ can produce the same
  $\mathcal A_{n+1}$ after a big collapse — confirmed by simulation, see §4, where a peak of 2145 drops
  straight to 7), so reversibility is off the table; only "eventually periodic from finiteness"
  (`aimo-0916`'s weaker conclusion) is in scope, and even that needs PC as an input.
- Also grepped `divisibility-and-gcd`, `p-adic-valuation`, `modular-arithmetic-and-CRT` subtopics for
  "greedy"/"minimal"/"antichain" specifically combined with gcd/coprimality — **no crux found** that
  matches "greedily construct a sequence enforcing pairwise-gcd $>1$ against all predecessors" as a
  *problem shape*. This appears to be a genuinely novel recursion in the corpus (consistent with round
  1/2's own conclusion that no direct transplant exists) — confirms there's no off-the-shelf crux to
  import for the core recursion itself; the corpus is only useful for the generic "eventual
  stabilization via monovariant / finite-state" *pattern*, not a specific transplant.

**No refutation and no new proof found in the corpus.** Confirms round 2's conclusion
(`dense-signature-vanishing`'s Prop. 4) that this problem's core mechanism is not a disguised version of
a known crux; the useful transplants are at the *pattern* level (integer monovariant bounded below;
finite deterministic self-map $\Rightarrow$ eventual periodicity), both of which still require solving
essentially PC/self-closing-reachability to even become applicable.

## 4. Simulation: does Absorption always eventually fire? (NEW — 19 fresh $a_1$ values, one to $n=30000$)

Ran the exact antichain-update simulation (frozenset prime-factor tracking, `sympy.primefactors`,
identical logic to the certified lemmas' definitions) for many new $a_1$ beyond the two on record
($2310$, $15$). Summary table (n = index of last growth event unless noted; all runs confirmed
**stabilized and stayed stable** for $\ge$ several thousand further terms after their last growth
event, i.e. genuinely self-closing, not just "no growth observed yet"):

| $a_1$ | primes | last growth $n$ | peak antichain size | final antichain size | absorption (prime power)? |
|---|---|---|---|---|---|
| 6, 30 | 2 primes | 2 | 1 | 1 | yes (trivial) |
| 12, 60 | $2^2\cdot3$ etc. | 3 | 2 | 1 | yes |
| 15 | 3,5 | 3 | 3 | 3 | **no** — self-closes at size 3 |
| 105 | 3,5,7 | 16 | 5 | 4 | **no** |
| 210 | 2,3,5,7 | 24 | 13 | 1 | yes |
| 385 | 5,7,11 | 38 | 7 | 7 | **no** (picks up outside prime 19!) |
| 462 | 2,3,7,11 | 26 | 14 | 1 | yes |
| 1001 | 7,11,13 | 59 | 30 | 4 | **no** |
| 1155 | 3,5,7,11 | 75 | 26 | 5 | **no** |
| 2310 | 2,3,5,7,11 | 894 | 268 | 1 | yes (round-2 baseline, reproduced) |
| 2730 | 2,3,5,7,13 | ~684 | 209 | 1 | yes |
| 3003 | 3,7,11,13 | 1187 | 264 | 1 | yes |
| 4290 | 2,3,5,11,13 | 1952 | 534 | 1 | yes |
| 5005 | 5,7,11,13 | 104 | 31 | 5 | **no** |
| 7429 | 17,19,23 | 119 | 43 | 5 | **no** |
| 15015 | 3,5,7,11,13 | 1293 | 124 | 6 | **no** |
| 30030 | 2,3,5,7,11,13 | 1370 | 588 | 1 | yes |
| **255255** | 3,5,7,11,13,17 | **21357** | **2145** | **7** | **no** — checked to $n=30000$ |
| 323323 | 7,11,13,17,19 | (still active at 5000, not run to convergence — truncated) | 1211 (at $n=5000$) | 831 (at 5000) | unknown, likely converges (not confirmed) |

**Key finding (new, refines round 2's picture): absorption (prime-power collapse) is the exception, not
the rule.** It fires reliably only when $2\in\mathrm{primes}(a_1)$ *and* the other prime factors are
small (so a nearby power of 2 can beat all rivals in the forced window) — every observed absorption
case has $2\mid a_1$ except none of the odd cases (`15,105,385,1001,1155,5005,7429,15015,255255`) ever
absorbed, they all **self-close directly to a small non-singleton antichain instead**, exactly the
`self-closing-antichain-sufficiency.md` mechanism, generalizing the $a_1=15$ example the lemma already
cites. The $255255$ run is the most dramatic new data point: the antichain climbs to **2145** live
generators before collapsing all the way down to **7** at a single stroke around $n=21357$, then stays
at exactly that self-closing 7-element antichain for $\ge 8600$ more terms with zero further growth
events — strong non-monotone-but-eventually-locking behavior, consistent with the theorem but nowhere
near proving it. **No counterexample to Antichain Stabilization was found** in any of the ~19 trials
(the one "truncated, still active" case, $323323$, ran out of time budget mid-growth at $n=5000$ with
antichain size 831 and no sign of having peaked — this is NOT evidence against stabilization, just an
unconverged run; it should be re-run with a larger time budget before drawing any conclusion from it).

**Practical implication for next round's outliner:** don't chase "prime powers recur infinitely often"
as the target — most trajectories never produce one. The right general claim is squarely
`self-closing-antichain-sufficiency.md`'s "self-closing is always eventually reached," and the useful
new empirical fact is that **odd $a_1$ (no factor of 2) never absorbs but always still self-closes**,
suggesting the mechanism for odd vs. even $a_1$ may need genuinely different combinatorial arguments (a
possible source of the "genuinely different framing" the orchestrator wants) — e.g. an argument
specific to "no term is ever squarefree-minimal-of-size-1" cases might isolate a cleaner sub-case to
attack first (prove Stabilization for the "eventually absorbs" family rigorously as a full sub-theorem,
separately from the "self-closes without absorbing" family), rather than one monolithic argument for
both.

## Assessment: promising vs. dead end

- **Dead end, don't re-scout:** "prime powers occur with positive density / recur infinitely often" as
  a standalone target (§1) — no handle found, and empirically it's not even the generic behavior (most
  odd $a_1$ never hit one).
- **Dead end, already confirmed twice, don't re-scout:** any $O(\log a_n)$-per-event fixed-budget
  charging argument, in any dressing (witness-debt, Dilworth/chain-covering per round 2; this round's
  covering-code framing in §2 hits the identical wall).
- **Promising, concrete, not yet tried:** the integer-monovariant candidate from `aimo-0134`'s pattern —
  "number of primes $\le L_0$ not yet hit by any live generator" (or a similarly-shaped genuinely
  non-increasing integer quantity, distinct from raw antichain size which is proven non-monotone) —
  worth a dedicated approach next round to check rigorously whether it is actually monovariant (I did
  NOT verify this; it's a candidate, not a lemma).
- **Promising reframing, still equivalent to PC, but cleaner:** "the truncated-to-$P$ antichain sequence
  is a walk on a finite state space, eventually periodic" (§2) — worth trying as an explicit finite
  automaton argument (state = current truncated antichain, if the transition can be shown to depend
  only on the current state) rather than as a size/counting argument.
- **New, actionable empirical split:** odd vs. even $a_1$ show qualitatively different stabilization
  mechanisms (self-closing-without-absorption vs. absorption) — consider splitting the top-level proof
  strategy into two sub-cases next round, which is also a genuine "different framing" per the
  orchestrator's plateau-breaking guidance, not just a bypass of the same wall.
