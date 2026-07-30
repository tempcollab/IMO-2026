## imo-2026-06 (lens: growth-rate / recruitment-counting)

### Verdict up front
The specific mechanism as dispatched — "each new distinct connector prime q_k must appear in a
bounded a_1-length window, costing one slot per window, so only finitely many can be recruited" —
is **NOT a genuinely new mechanism**. When made precise it decomposes into exactly the two pieces
already tried this run, one certified-but-insufficient and one certified-dead:
1. the **per-window spacing cap** (Lemma B, `lemmas/minimal-linking-prime-and-window-cap.md`,
   round 5, certified): a prime p ≥ q* occupies ≤ a_1/q*+1 multiples in any window W_k=(k·a_1,(k+1)a_1).
   That approach (`minimal-linking-prime-extremal`) already tried to turn "bounded occupancy per
   window" into a contradiction and got stuck exactly because bounding slots *per window* says
   nothing about the *number of windows* over which recruitment can occur — the sequence has
   infinitely many windows as n→∞, so a per-window cap caps a **rate**, not a **total**. Its residual
   gap (DESC: "a bad window forces a smaller-index bad window") was never closed and is
   difficulty-equivalent to the crux.
2. the **distinctness-by-difference / (R2′)** result (round 9, `bounded-window-distinctness`, RETHINK,
   certified as `lemmas/distinctness-by-difference.md`): confining all the new-large-prime-carrying
   witnesses to a *single bounded value-band* is **rigorously proved equivalent** to the connector
   pool Q(r_0) being finite — i.e. equivalent to ¬¬(FIN-Q), the thing we want to conclude. So "each
   new q_k lives in a bounded window" cannot be established without already assuming the crux.

Put together: a "slot-per-window" accounting can only ever bound the *density* of recruitment
events, never force recruitment to *terminate* after finitely many windows, because nothing in the
window-cap lemma limits how many windows exist or forces new windows to fail to contribute a fresh
large prime. To close ¬(FIN-Q) via counting you would need an argument that the *total number of
windows that can ever contribute a new connector* is itself finite — but that is a restatement of
the crux (Q(r_0) finite), not a consequence of window arithmetic. This is precisely the diagnosis
`bounded-window-distinctness`'s reviewer reached (round 9): the confinement needed is *equivalent to
the conclusion*, so it is vacuous as a closer.

### Precise statement, if one insists on formalizing it (for the record)
Let r_0 ∈ R'_bad with Q(r_0) := ⋃_{i∈W(r_0)} Q_i infinite (¬(FIN-Q), the crux target). Since each
Q_i is finite (a_i has finitely many prime factors), W(r_0) must be infinite. Enumerate W(r_0) as
i_1 < i_2 < …; a_{i_1} < a_{i_2} < … are actual terms, hence (certified bounded-gap fact)
a_{i_{j+1}} − a_{i_j} is NOT itself bounded in general (only *consecutive* terms a_n, a_{n+1} satisfy
gap ≤ a_1; witnesses i_j can be arbitrarily sparse in the full index set). So even the premise "the
witnesses occur every O(a_1) values" needs its own proof and is not free. The "one slot per window"
claim would need: (a) a fixed window length W (candidate a_1), (b) a bound S on how many *new*
distinct large primes can first appear across all Q_i for a_i in one window, and (c) a bound on the
*number* of windows that can hold a new-prime event. (a)+(b) are exactly Lemma B in spirit (and are
gettable); (c) is unavailable and is exactly ¬(FIN-Q) restated.

### Does it differ from the dead global Σ1/p² count?
No, not in kind. Σ1/p² (Lemma C3, certified dead as closer) bounds a *fraction* of pairs across
[a_1,X], never reaching zero as X→∞ — it fails because it only shows large-prime pairs are a
minority, not absent. The recruitment/window framing has the *same* failure shape one level up:
it would bound how many *new* primes can be recruited *per window*, but (i) cannot bound the number
of windows, and (ii) even the per-window cap derived (Lemma B) is a density statement (≤ a_1/q*+1
per window, still growing without bound in absolute count as q* is small), not a "≤ O(1) total"
statement. So this is the same "bounds a rate, not the total" failure mode as the capacity count,
merely relocated from term-pairs to windows/primes.

### Where GREEDY SUCCESSOR CHOICE could still matter (the one thing not yet exploited)
All the counting so far (Lemma B, distinctness-by-difference, Σ1/p²) uses only that a_i is *some*
term (an element of E_∞), never that a_{n+1} is the *smallest* admissible integer beyond a_n. Window
Purity is the only certified fact using minimality, and it says the interior of gaps is E_∞-free —
it does not itself bound how many *distinct new large primes* can appear across the sequence. A
genuinely new recruitment argument would need to convert minimality into a **cost that increases
monotonically and unboundedly with the number of large primes already recruited** (e.g., "each time
a new large prime becomes load-bearing, the smallest still-available candidate integer must jump by
more than the previous jump," forcing gap growth that contradicts the certified gap bound ≤ a_1). I
could not locate any certified or drafted lemma that supplies this; it would be new mathematical
content, not a repackaging — but I have NOT verified it is true, only that it is the one place this
lens has fresh room. This is speculative, one line, and not something I chased further.

### Assessment: viable opening?
As dispatched, **not viable as a closer** — it is a relabeling of two already-explored-and-
insufficient/dead mechanisms (per-window occupancy cap; value-difference confinement). I recommend
NOT dispatching a builder purely on "recruitment costs one slot per window" as stated; it will
self-certify RETHINK for the same reason bounded-window-distinctness did (round 9), burning a build
slot on a rediscovered dead end. If the outliner wants to use this lens productively, it should be
recast around the speculative greedy-minimality monovariant above (jump-size forced to grow with
recruited-prime count) — that is a different claim from "bounded slots per window" and has NOT been
tried or ruled out, but is unverified and would need to be built from scratch, likely still hitting
Prop D's warning that pure covering-structure arguments are insufficient without genuine dynamics.

### Candidate technique(s)
- Pigeonhole / finite-alphabet argument (knowledge_base.md Pigeonhole entry) — already fully used in
  the FIN-Q reduction and Lemma B; no new juice left in it for a pure occupancy count.
- Extremal principle (well-ordering on q*, on window index, on m_0) — already used three times
  (Lemma A, DESC framing, minimal-bad-term floor-tightness); exhausted for this specific lever.
- What is genuinely missing: a **monovariant tied to the greedy choice rule itself** (not to static
  occupancy) — no KB entry or crux move directly supplies this; would have to be built bespoke.

### Cheap-kill candidates
- Before building anything on this lens: ask the builder to state explicitly what bounds "the number
  of windows contributing a new connector" (not just "primes per window") — if they cannot supply an
  independent bound for that, the route is dead on arrival by the same argument as (R2′). This is a
  5-line pre-check that would have killed round-9's bounded-window-distinctness before a full build.
- Check: is a_i (i ∈ W(r_0)) required to be a "bad" term itself? No — a_i is just an ordinary
  covering term that happens to miss the fixed finite set S(r_0); it need not be part of a
  sole-connector bad pair, so GPC/sole-connector-off-lattice (which confines *bad* pairs off the
  a_1-lattice) does NOT directly confine witness terms a_i to any special window. This kills the
  literal "confined to a length-a_1 window" premise at the source (witnesses are NOT forced off the
  a_1-lattice at all — an a_i ∈ W(r_0) can perfectly well be a multiple of a_1's own primes, it's a
  covering term).

### Knowledge-base entries to use
- Pigeonhole principle, Extremal/well-ordering principle (both already cited by certified lemmas
  finite-connector-pool-periodicity.md, minimal-linking-prime-and-window-cap.md).
- No additional KB entry beyond what's already invoked (checked knowledge_base.md; no untried
  "growth-rate" or "recruitment" specific technique entry exists there for this problem).

### Analogous past problems (cruxes)
- **aimo-0727** (IMO-style, number_theory, subtopics divisibility-and-gcd / size-bounding-and-descent):
  crux move "if a bounded multiplier sequence (b_k) existed, all prime factors of the a_k would be
  confined to a finite set {≤B+2} ∪ primes(a_1,a_2), contradicting infinitely many primes appearing
  — hence (b_k) is unbounded." This is the closest analog to a "finite-prime-support ⟺ bounded
  parameter" contrapositive, i.e. the *mirror image* of what we want (we want to show the analogous
  parameter — recruited large primes — IS bounded / finite, they use unboundedness of primes to force
  a parameter unbounded). Genuinely instructive for the SHAPE of the argument, but NOT directly
  transplantable: aimo-0727's sequence has a *closed-form algebraic recursion* a_{k+1}=a_k(b_k+2)/b_{k+1}
  tying prime factors of a_k tightly to the single integer b_k, whereas imo-2026-06's a_{n+1} is
  defined by a greedy *search* with no such formula (consistent with the round-5 memory rule: KB/
  corpus donors with closed-form recursions do not transplant literally to this problem). Cite as
  flavor/inspiration only, not as a template to build directly.
- **aimo-0447** (size-bounding-and-descent): "a prime exceeding the interval length divides at most
  one element of the interval" — this IS exactly the source of the certified
  distinctness-by-difference lemma already in the cache and already proven a dead closer (R2′). Do
  not re-retrieve it as if fresh.
- No other corpus entry found that resembles a genuine "recruitment rate bounded by window occupancy
  forces finiteness of a growing prime pool" argument for a *greedy, non-algebraic* sequence; searched
  number_theory subtopics divisibility-and-gcd, pigeonhole, size-bounding-and-descent,
  sequences-and-recurrences for keywords (distinct prime, recruit, window, new prime factor) — the
  above two are the only genuine hits.

### Prior progress (unchanged by this lens)
Full certified scaffold (ENUM+PER+CSP⇒theorem) stands. Crux is the certified-equivalent wall
(CSP)=ℰ-small-only=(EC)=¬(FIN-Q). Sole live carrier: covering-small-part-descent (EC form), stalled on
"no downward monovariant, q is preserved under propagation." See run_state.md / current.md for full
history; nothing in this lens changes that picture except to rule out one more candidate closer.

### Dead ends (do not retry) — confirmed/reinforced by this lens
- **minimal-linking-prime-extremal**'s per-window spacing cap (Lemma B): correct and certified, but
  bounds a rate not a total; already known insufficient (round 5, DESC gap never closed). This lens
  would re-derive exactly this and stall the same way.
- **bounded-window-distinctness / (R2′)**: re-confirmed here from a different angle — the "confine
  new connectors to one window" premise this lens needs is exactly what (R2′) proved equivalent to
  assuming Q(r_0) finite. Do not re-field under the "recruitment counting" name.
- **Global Σ1/p² capacity**: same "bounds a fraction/rate, never zero/total" failure shape; already
  dead (round 2).
- NEW finding this round: witness terms a_i ∈ W(r_0) are NOT bad terms and are NOT confined off the
  a_1-lattice by GPC/Prop C — that confinement only applies to genuine sole/no-small-prime-connector
  BAD PAIRS, not to arbitrary witnesses of a bad residue class. So the dispatched premise "connector
  primes appear within a bounded a_1-length window" has no certified support at all; it would need to
  be established from scratch and, per the (R2′) equivalence, cannot be (it's equivalent to the
  crux).

### Small-case / intuition notes (conjecture only)
Numerics (round 8/9, echoed here, not re-run — CSP holds on every tested seed a_1 ∈
{15,35,99,105,231,1155}, up to 1200 terms, zero bad terms) give no way to observe a live ¬(FIN-Q)
instance to test any recruitment-rate hypothesis directly (there is no non-trivial "recruitment" to
watch — the sequence just never manufactures a bad class). This is consistent with CSP being
unconditionally true, but does not help decide which counting mechanism, if any, could prove it.
