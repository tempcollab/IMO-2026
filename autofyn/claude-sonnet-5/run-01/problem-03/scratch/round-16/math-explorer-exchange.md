## imo-2026-03 — Framing 2 (mechanical greedy + exchange argument), Case C general m>=4

### 1. The canonical greedy rule as literally specifiable

Setup (per `universal-adversary-strategy`'s certified formalism): `A=(p_1≥...≥p_m)`
sorted descending, Case C means `p_1 < Σ(tail)`. Xiang Yu has `m-1` real marks.
The rule I formalized and tested (the only way to make "process tail
smallest-to-largest, carry a running deficit" fully mechanical, i.e. a single
pass with no lookahead/backtracking) is:

- Maintain `d := p_1` (the "deficit" — mass of `p_1` not yet assigned).
- Scan the tail in **ascending** order `t_{(1)}≤t_{(2)}≤...`. For each `t_{(i)}`
  in turn: if `d - t_{(i)} ≥ 0`, "match" it (spend 1 mark tying a split-off
  piece of `p_1` to it, `d -= t_{(i)}`); else leave it in the tail and move on
  (never revisit).
- When the scan ends (deficit either `0` or smaller than every remaining
  unmatched element), the residual `r=d` becomes a leftover piece of `p_1`
  (0 extra marks if `r=0` exactly, matching the certified Lemma
  DOM-boundary-slack; 1 mark otherwise).
- Recurse the **same rule** on the untouched remainder of the tail with the
  marks left over, i.e. this is exactly a `(marks,|A|)`-style recursion but
  with the *matching subset* chosen by this one deterministic scan instead of
  an existence claim.
- I also tested the natural companion rule for what to do with a lone
  leftover piece once nothing else remains to compare it to: split it in
  half whenever marks remain (Variant 2), and a "best-fit" variant that
  greedily picks the *largest* not-yet-used tail element `≤ d` at each step
  regardless of scan order (Variant 3), to check whether the specific
  scan-order choice was the failure point rather than the mechanism itself.

### 2. Mandatory cheap feasibility gate — RESULT: FAILS. This framing is DEAD ON ARRIVAL.

Implemented exactly (Python, `fractions.Fraction`, exact arithmetic throughout,
script at `/tmp/round-16/greedy_test.py`) and run against all three mandated
hard witnesses, three natural greedy variants:

| Witness | target | Variant 1 (ascending, no leftover-split) | Variant 2 (+ halve lone leftover) | Variant 3 (best-fit) |
|---|---|---|---|---|
| `T=(0.20,0.15,0.12,0.08)`, m=4 | `22/75≈0.2933` | `7/20=0.35` **FAIL** (margin `-17/300`) | `11/40=0.275` **PASS** (margin `11/600`) | `7/25=0.28` **PASS** (margin `1/75`) |
| `A=(1826,1563,1520,1514,765)/7188`, m=5 | `16/31≈0.5161` | `962/1797≈0.5353` **FAIL** | `1025/1797≈0.5704` **FAIL** (margin `-3023/55707`) | `7445/14376≈0.5179` **FAIL** (margin `-779/445656`) |
| `A=(14,12,10,9,8,4)`, m=6 (round-15 witness) | `608/21≈28.952` | `33` **FAIL** | `29` **FAIL** (margin `-1/21`) | `30` **FAIL** (margin `-22/21`) |

**No variant of the mechanical single-pass greedy passes all three witnesses.**
Variant 2 exactly reproduces the already-known and already-refuted
**contiguous-only** value `29` on the m=6 witness (matches
`universal-adversary-strategy`'s round-15 report to the exact fraction) — i.e.
this greedy, at its best, silently degrades into the SAME contiguous-menu
strategy that round 15 already proved insufficient at m=6, not a genuinely
new mechanism reaching the true `57/2` optimum.

**Root cause, diagnosed exactly.** The true optimum at m=6 needs the subset
match `{10,4}` (sum `14=p_1`), which requires *skipping* the intervening
elements `12,9,8` — in particular skipping `8`, a *smaller* element than `10`,
while still using `10`. No single deterministic ascending-or-descending scan
(with or without a "best current fit" rule) can produce this: greedy subset-sum
selection is classically known to fail to find an exact/optimal subset even
when one exists (this instance, tail-values `{12,10,9,8,4}` needing target `14`,
is essentially the textbook counterexample shape: ascending greedy grabs
`4,8` — sums to `12`, blocked at `9` — while the correct pair `{10,4}` needed
skipping `8`; best-fit grabs `12` first, blocked immediately). This is not a
tuning problem in the scan order or tie-break rule; it is the general fact that
**exact/optimal subset-sum has no correct single-pass greedy solution**, and
Lemma SLACK-COVER's needed matching is exactly an instance of that problem
(worse: a *value-optimizing*, not just sum-hitting, subset selection, jointly
with the recursive value of the leftover — see current.md's own diagnosis).

**Verdict: DEAD ON ARRIVAL as a literally-mechanical rule.** Per the mandated
gate, I stop here — no exchange/no-local-improvement argument was attempted,
since there is no fixed deterministic rule left to prove optimal.

### 3. Exchange argument shape — not attempted (gate failed)

Not developed, per instructions, since step 2 failed. For the record: an
exchange argument would need to operate on *which subset* is matched, not on
a scan order, so "adjacent transposition" would have to mean "swap one
matched element for one unmatched element" — but proving no such swap helps
is exactly proving the matched subset is already sum/value-optimal, i.e. it
presupposes the very existence-of-optimal-subset content SLACK-COVER needs;
there is no smaller sub-claim left to extract once the deterministic rule
itself is abandoned.

### 4. Honest assessment: does this duplicate solve2's Move 0-3 casework?

Yes, and worse: even in its best-passing form (Variant 2 on witness 1), the
greedy is *strictly weaker* than the already-certified non-contiguous menu —
it is a specific single deterministic instantiation of "some subset of the
tail matched to `p_1`," i.e. exactly one candidate for Move 2's subset choice,
with no mechanism to verify or search for a better one. Where it succeeds
(witness 1) it succeeds by lucky alignment of scan order with the true
optimal subset; where it fails (witnesses 2,3) it is strictly dominated by
the value that `solve2`'s exhaustive non-contiguous search already finds. So
this framing does not sidestep Lemma SLACK-COVER's existence question at all
— it is a strictly weaker special case of the exact same Move-2 subset-match
content, disguised as a "mechanical rule," and fails precisely where that
content is load-bearing (m=6). This is the same convergence-failure pattern
already flagged for `case-c-secondary-extremality` (round 11) and
`minimax-mixed-duality` (rounds 6-8): a superficially different framing that,
on inspection, reduces to (a strictly weaker instance of) the same open
content the sibling approach already owns.

### Distinct openings surfaced (for completeness, not pursued further this round)
- None new beyond what round 15 already isolated: the gap is specifically the
  existence of an optimal (value-maximizing, not just sum-hitting) subset of
  the tail for `p_1` to match, jointly with the recursive value of the
  untouched remainder — this round confirms (via a clean, independent
  mechanism) that no *mechanical, lookahead-free* rule can supply that
  subset in general, reinforcing (not just repeating) round 15's finding that
  the defect-Hall/König framing also could not supply it. Both of the two
  "avoid the existence question" framings tried across rounds 15-16 are now
  ruled out; any future attack on Lemma SLACK-COVER needs either (a) a
  genuine existence proof for the value-optimal subset (some kind of
  exchange/interval/majorization argument on the *matched-subset selection
  itself*, not on a scan order), or (b) an entirely different route to Case C
  that avoids constructing an explicit matching altogether (e.g., an
  averaging/potential-function argument over Xiang Yu's whole strategy space
  rather than an explicit greedy construction) — but note averaging routes
  were already killed in round 14 (`case-c-slack-covering`,
  `lemmas/uniform-tail-margin-negative.md`) for the one-level version; a
  *multi-level* averaging argument has not been tried and is not obviously
  subject to the same refutation, and might be worth a future round's
  attention as a third framing distinct from both greedy-construction and
  Hall/König.

### Candidate technique(s)
None recommended from this framing — it is refuted at the feasibility-gate
stage. If a future round wants to keep the "exchange argument" idea alive, it
must be applied to a genuine existence proof of the optimal matching (not a
mechanical scan), which is a fundamentally different (and harder) technical
target than what was scouted here.

### Cheap-kill candidates
The gate itself (implement the mechanical rule, test on 3 known hard
witnesses) *is* the cheap kill, and it worked as designed — this pruned the
whole framing in under 10 minutes of work rather than after a partial proof
attempt.

### Knowledge-base entries to use
None newly implicated; the relevant certified facts remain
`lemmas/pair-value.md` (subset-match value identity, hypothesis-free) and
`lemmas/uniform-tail-margin-negative.md` (kills one-level averaging) — both
already known to the population.

### Analogous past problems (cruxes)
`aimo-0003` (combinatorics, subtopics `invariants-and-monovariants` /
`processes-and-algorithms` / `bijections-and-encoding`) — three cruxes: (1)
reduce a permutation-invariance claim to invariance under one adjacent
transposition; (2) verify local invariance by exhaustive casework on how many
marked points fall in a critical arc; (3) encode a matching-count invariant as
the *minimum value of a running ±1 tally*, proved by an induction that
deletes an innermost matched pair. This is the crux round 15 pointed to as
motivating "exchange/running-deficit" framing — genuinely analogous in
*shape* (a running scalar tally read once over a sorted sequence, matched
pairs deleted by induction) but the underlying combinatorics is different in
a load-bearing way: aimo-0003's matching is a fixed nearest-neighbor
(non-crossing arc) structure with no value-optimization choice — the greedy
there is provably canonical because any two red/blue matchings differing by
one swap are shown *value-equivalent* by direct casework (3 cases: 0, 1, or 2
of the relevant points inside the critical arc). Case C's matching is
explicitly a value-*optimization* over subset choice (this round's witnesses
show different subsets give different, non-equivalent values — `{4,8}` gives
`29`, `{10,4}` gives `28.5`), so the aimo-0003 mechanism (prove all local
swaps are neutral) does not transfer: local swaps here are *not* neutral,
they are exactly where the value difference comes from. No other corpus
problem found closer in subtopic (`games-and-strategy`,
`processes-and-algorithms`) that resembles the joint covering+value existence
shape of SLACK-COVER specifically.

### Prior progress
Unchanged from `current.md`: lower bound fully closed; `m=1,3` fully closed;
Case C for general `m≥4` is the sole open gap, sharply isolated as Lemma
SLACK-COVER (a joint covering+recursive-value existence statement), proved
*necessary* (not avoidable via contiguous-only menu) at `m=6`, strong but
incomplete exact evidence it's avoidable at `m=4`.

### Dead ends (do not retry)
- **This round's mechanical greedy framing (all 3 variants tested)** — fails
  the mandated gate on 2 of 3 witnesses; classic greedy-subset-sum failure
  mode, not a tuning issue. Do not retry with different tie-break/scan-order
  variants — the obstruction is structural (need lookahead/backtracking or an
  existence proof, not a single deterministic pass).
- Defect-Hall/König-deficiency (round 15) — both natural bipartite encodings
  refuted (permissive: vacuous deficiency; restrictive/contiguous: wrong
  witness value).
- One-level averaging/pigeonhole (`case-c-slack-covering`, round 14) —
  exact algebraic refutation for every `m≥4`.
- Fixed-small-integer-count top-level pair constructions (round 11) —
  refuted by near-uniform-tail family for `m=4..100`.
- `case-c-secondary-extremality` (round 11) — refuted by value-equivalence
  of competing constructions, giving no independent leverage.
- Pure single-piece moves (DOM/HALVE/TAIL-SNIP alone) — refuted, need
  coordinated multi-piece splits (round 5).

### Small-case / intuition notes
Conjecture (evidence, not proof): the true optimal matched subset at each
level is a *value*-maximizing (not merely sum-feasible) subset of the tail —
witness 3 shows two different sum-14-hitting subsets are not even being
compared by a greedy scan ({4,8} sums to 12, undershoots; the exact-sum
subset {10,4} is reachable only by skipping a smaller feasible element first).
This reinforces that Lemma SLACK-COVER is intrinsically a *search/existence*
statement over subsets, not reducible to any single deterministic
construction rule — consistent with, and now doubly confirming (via a second,
independent mechanism after round 15's Hall/König result) the population's
long-standing diagnosis in `current.md`.
