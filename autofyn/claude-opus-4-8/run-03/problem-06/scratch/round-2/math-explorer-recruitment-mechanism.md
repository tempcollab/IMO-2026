## imo-2026-06

### Scope of this report
Assigned lens: the direct dynamics of prime recruitment (why/when a new prime becomes
necessary, and whether it can exceed `maxfac(a_1)`). I did **not** re-derive the E_∞
reduction (already certified — see `lemmas/enumeration-of-E-infinity.md` and
`lemmas/periodic-set-enumeration.md`); I probed the recruitment mechanism itself with
concrete sympy experiments and traced actual failing witnesses.

### Compatibility as a covering/hitting-set condition (framing, confirmed)
`m` compatible with `a_1..a_n` ⟺ for every `i`, `π(m) ∩ π(a_i) ≠ ∅` (shares a prime).
So `E_∞ = {m : π(m) hits π(a_i) for every i}` is exactly a (possibly infinite) **hitting-set /
covering** condition — `m`'s prime set must be a "transversal" of the hypergraph
`{π(a_i)}_{i≥1}`. This is the right lens (matches Hall's-marriage/SDR-flavored KB entry,
though the direct correspondence isn't a literal SDR — see Analogous problems below).

### Confirmed baseline: every term hits P = primes(a_1) (Lemma 1+3, already certified)
For every `i`, `gcd(a_i,a_1) > 1`, so every term has a prime factor in `P := primes(a_1)`,
and `P ⊆ {primes ≤ maxfac(a_1)}` trivially. **This alone is proven but is NOT sufficient**:
`R = P` is known-false (a_1=99 recruits 5, which does not divide 99). So the interesting
content is exactly which primes beyond `P` get recruited, and why they stay bounded.

### Direct experiment: traced an actual recruitment event (a_1 = 99)
`P = {3,11}`, `maxfac(a_1)=11`. I found the *exact minimal sufficient R* by testing
periodicity of the observed term-set mod various `L` (zero mismatches over thousands of
candidates = exact):
- `R = {2,3,5,11}` (`L=330`): **0 mismatches** over ~3800 candidates — exact.
- Dropping 5 (`R={2,3,11}`, `L=66`): **294 mismatches** — 5 is genuinely necessary.
- Dropping 11 (`R={2,3,5}`, `L=30`): **148 mismatches** — 11 necessary (expected, ∈P).
- Dropping 2,5 (`R={3,11}`=P, `L=33`): **1040 mismatches** — confirms P alone fails badly.
- **7 is never needed** even though `7 ≤ maxfac(a_1)=11`: `R0={2,3,5,7,11}` also gives 0
  mismatches but is not minimal; the true minimal R is a *proper subset* of R0. So
  `maxfac(a_1)` is only an upper envelope, not tight — the actual recruited set can omit
  primes below the bound.

**Traced the mechanism for exactly why 5 is recruited.** Candidates `x=171,159,219`
(all `≡39 mod 66`, i.e. divisible by 3 only among `{2,3,11}`, with a large-prime cofactor)
all fail compatibility — and I found the *specific failing witness term* for each: **all
three fail against the same term `a_i = 110 = 2·5·11`.** `110` was accepted into the
sequence because it shares `11 ∈ P` with `a_1=99` (and everything earlier), but as the
*smallest* number ≥ (previous term)+1 divisible by 11, it forced in the cofactor `10=2·5`
— and *that* cofactor's small primes (2 and 5) become independently load-bearing: any
later candidate not divisible by 11 must now also avoid needing 2 or 5, i.e. must
literally collide with 110's factor set, so 2 and 5 get "recruited" as covering primes
in their own right. Concretely: `105=3·5·7` (a genuine term) passes against `110` via the
shared prime `5`; `171=3²·19` does not (no factor among `{2,5,11}`) and is correctly
excluded from `E_∞`.

**This is the actual recruitment mechanism, made concrete: new primes enter R via the
*cofactor* of a greedily-minimal witness term that was pulled in to satisfy an earlier
(small) prime constraint.** The bound "cofactor primes stay ≤ `maxfac(a_1)`" is not
automatic from size (the term itself, `a_n`, is unbounded as `n→∞`) — it must come from
minimality of the greedy choice (the term is the *smallest* candidate in a window of size
`≤ a_1`, Lemma 2, so it tends to be built from small primes) combined with an inductive
argument that the covering structure never needs to "reach" for a fresh large prime once
enough small-prime classes are already present. **This minimality-of-cofactor argument is
NOT yet made rigorous by any approach in the population — it is the load-bearing gap,
now localized to a specific, checkable claim** (see Candidate sub-lemma below).

### Refuted: "a single small prime always wins" (checked broadly, mixed result)
Tested whether some single `p ∈ P` divides *all* sufficiently late terms (tail of 200 out
of 800 generated terms), across many `a_1`:
- **True** (single winner) for: `a_1 ∈ {25,49,121,169}` (prime powers, `|P|=1`, trivial)
  and also `{55,33,21,231}` (here `|P|>1` but one prime, e.g. 3 or 5, still dominates).
- **False** (no single winner, genuinely multi-prime residue-class structure) for:
  `a_1 ∈ {15,35,45,65,77,91,95,99,105,143,165,385}`.
So the finite-state-window / density-bounded-recruitment "one winning prime" mental
model is **an oversimplification that fails on the majority of tested seeds** — the
correct target is the *set* R (usually size ≥ 2), not a single dominant prime. Any
sub-lemma phrased as "some prime of P eventually divides every term" will be **false in
general** and should not be pursued as a shortcut.

### R0-sufficiency: strong direct numerical confirmation (new, stronger than prior rounds)
Directly tested the *actual claim needed* (not a proxy): is `E_∞` periodic mod
`L0 = ∏(primes ≤ maxfac(a_1))`? Checked via **exact enumeration matching** (`x ∈ E_∞ ⟺
x+L0 ∈ E_∞` for all `x` in a wide range, using the certified enumeration lemma so this is
a faithful test, not a heuristic):
`a_1 ∈ {15,35,45,55,65,77,91,95,99,105,121,143,165,33,21,25,49}` — **0 mismatches in every
case**, including the two seeds requiring a much longer sequence (`a_1=65,91`, `L0=30030`,
verified with 9000 generated terms). This is the same fact the field already isolated as
the crux (G1/G1'/Lemma F/Structural Lemma), now re-verified with a cleaner, more direct
test (residue-shift equality rather than proxy "big primes never appear" checks, which
earlier explorers rightly noted is a different and false claim — big primes DO appear
constantly in the factorizations, they're just never *load-bearing*).

### Cheap-kill / pruning ideas tried
- Checking "no term isolates a large prime as sole R0-witness" is a red herring: I
  confirmed (a_1=99, 3000 terms) that **no term has R0-intersection equal to a single
  large-ish prime** — the recruitment is not "one isolated pinning term" but the joint
  covering effect of a witness term's whole cofactor (see mechanism above). Approaches
  that look for "the load-bearing witness pair" (single pair with disjoint-except-one-
  prime colors) are looking at the wrong granularity; the real object is a term's full
  cofactor once one prime from P is fixed.
- Tried "primes dividing infinitely many terms are exactly R0": **false** — confirmed
  (consistent with density-bounded-recruitment's recorded dead end) that arbitrarily
  large primes divide infinitely many terms (positive density, since E_∞ is periodic and
  every residue class meets a period). Persistence (dividing infinitely many terms) is
  the wrong invariant; necessity/load-bearing-ness is the right one, and they diverge.

### Candidate sub-lemma to hand to the outliner (new, concrete, checkable)
**Cofactor-boundedness lemma (candidate).** For every term `a_i` (`i ≥ 2`) with `p ∈ P`
its witnessing prime from Lemma 1/3, write `a_i = p^{v}·c` with `p ∤ c`. Claim: `c` has a
prime factor `≤ maxfac(a_1)` **or** `c` has no prime factor that is ever load-bearing
(i.e. `c`'s prime factors beyond `maxfac(a_1)` never become necessary for any future
candidate). This is exactly what happened concretely with `110 = 11 · 10`: cofactor
`10 = 2·5`, both `≤ 11 = maxfac(a_1)`, and both became load-bearing. Proving this reduces
to a *greedy-minimality* argument: because `a_i` is chosen as the smallest integer in a
window of length `≤ a_1` above `a_{i-1}` satisfying divisibility by *some* prime of the
(by-then-established) covering family, and minimal integers divisible by a fixed prime
`p` in a window preferentially factor through small cofactors (Bertrand/smooth-number
density style argument) — **this direction (bounding cofactor primes via minimality of
the greedy choice, not via density of persistence) is a genuinely different attack angle
from all four current approaches**, none of which analyze the cofactor structure of the
witness term that triggers recruitment. Flagging this as the outliner's best new lever.

### Knowledge-base entries to use
- **Bertrand's postulate** — plausible tool for bounding smallest-multiple-in-a-window
  cofactor size/smoothness (the greedy witness `a_i` sits in a window of length `≤ a_1`).
- **Hall's marriage theorem / SDR** — the covering/hitting-set framing is SDR-adjacent
  (a transversal of `{π(a_i)}`); worth checking if a finite-hypergraph-covering compactness
  argument (each `E_n` nonempty, need `∩E_n` behavior) can be phrased via a compactness/
  König-type duality, though I did not find a clean fit — flag as speculative.
- **Pigeonhole / extremal principle** — used above to refute "single winning prime" and to
  observe some `p∈P` always divides infinitely many terms (trivial pigeonhole on finite
  `P`), but this alone (as shown) is insufficient; do not oversell it as the crux-closer.
- **Order of an element / periodicity mod m** — supports the periodicity endgame (already
  handled by the certified lemmas), not the recruitment gap itself.

### Analogous past problems (cruxes)
Searched `number_theory` subtopics `divisibility-and-gcd`, `sequences-and-recurrences`,
`processes-and-algorithms`, and combinatorics `processes-and-algorithms`, filtering by
keyword ("gcd", "greedy", "smallest", "prime", "coprime", "sequence") against
`past_problems_database.json` statements. No problem in the corpus has the same
"greedy-smallest-integer-compatible-with-all-predecessors" structure. Closest (weak,
not a real analogue — flagging honestly rather than forcing a match):
- `aimo-0678` (`divisibility-and-gcd` / `size-bounding-and-descent` / `modular-arithmetic-and-CRT`)
  — crux move "construct a min-of-a-set integer monovariant... then reduce the other
  coordinate modulo the lcm of the bounded coordinate's attainable values, turning the
  state pair into a deterministic map on a finite set." Structurally resembles the
  finite-state-window endgame (bounded quantity ⇒ finite state ⇒ eventual periodicity)
  but the *recruitment* mechanism (which lcm-factors are attainable) is not addressed by
  its solution — no transferable crux move for our actual gap.
- `aimo-0503` (`divisibility-and-gcd` / `size-bounding-and-descent`) — "bound the gap
  between two consecutive terms from below by their gcd" — same flavor of gcd-gap
  reasoning as our bounded-gaps Lemma 2, but for a different (non-greedy) sequence; not
  a match for the recruitment question.
**Conclusion: no strong analogue for the finiteness/recruitment crux exists in the
corpus.** The field should not expect to import a crux move here; this looks like a
genuinely novel argument the builder must construct.

### Prior progress
See `current.md` — all three E_∞-based approaches (enum-covering-primes,
density-bounded-recruitment, finite-state-window) are fully reduced to one finiteness
crux (G1/G1'/Lemma F/Structural Lemma), all rigorously proved up to that point. The
fourth approach (difference-sequence-squeeze) is unsolved, working with the gap sequence
directly and stalled on an unmanufactured divisibility ("R2").

### Dead ends (do not retry)
- **R ⊆ P ∪ {2,3}**: false (a_1=99 needs 5, not 2 or 3-flavored).
- **Persistence (divides infinitely many terms) as a proxy for load-bearing**: false —
  arbitrarily large primes divide infinitely many terms by density; persistence and
  necessity are different properties. Do not resurrect density arguments on raw
  persistence.
- **Single small prime dominates eventually**: false for the majority (12/16) of tested
  seeds; only true for prime-power `a_1` and a handful of others. Do not build a proof
  that assumes a unique winning prime exists in general.
- **Isolated single-term witness pinning a large prime**: no such witness was found for
  the recruited prime 5 in the a_1=99 case over 3000 terms — the recruitment operates via
  a term's whole cofactor set jointly, not a lone large-prime witness. Approaches
  searching for "the one term that forces prime q" are looking at the wrong object.

### Small-case / intuition notes (all labeled conjecture except where computation is exact)
- **Conjecture (matches G1'/Lemma F exactly)**: `E_∞` is periodic mod
  `L0 = ∏_{p ≤ maxfac(a_1)} p` — verified exactly (0 mismatches) on 16 distinct seeds
  including two requiring 9000-term sequences, strongest direct evidence yet for this
  exact statement.
- **New observation (not previously reported)**: minimal sufficient R can be a *strict*
  subset of `R0` (e.g. a_1=99: minimal R={2,3,5,11} ⊊ R0={2,3,5,7,11}), so the bound
  `maxfac(a_1)` is a correct but non-tight envelope — proving `R ⊆ R0` (not `R = R0`) is
  the right target, consistent with what the population already targets.
- **New mechanism (the main contribution of this report)**: recruitment happens via the
  *cofactor* of a greedily-chosen witness term (e.g. `110 = 11·10`, cofactor `10=2·5`
  both recruited), not via an isolated large-prime witness. This reframes the crux as a
  claim about **the smallest compatible integer in a bounded window being built from
  small-prime cofactors** — a minimality/smoothness argument, structurally different
  from the covering-replacement and density mechanisms the three live approaches
  currently propose. Recommend the outliner add or redirect an approach toward this
  cofactor-minimality angle as the "genuinely different framing" CLAUDE.md calls for
  when a shared gap persists 3+ rounds.
