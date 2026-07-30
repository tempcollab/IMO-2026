## imo-2026-06 (lens: sub-gap 6a, non-symmetric upward mechanism)

### Distinct openings

**A. (NEW, most promising) "Badness is mod-L₀ periodic + fixed witness-index-set" mechanism.**
Re-derive from the *already-certified* Step 1a of `covering-small-part-descent.md`: for any integer
`m>1`, `S(m)` (hence whether `m∈E*`) depends only on `m mod L₀`. So "bad-ness" of a term is really a
property of its **residue class** `r ∈ Z/L₀Z`: define `R_bad ⊆ Z/L₀Z` = residues `r` such that
`S(r)` fails to meet `primes(a_i)` for at least one index `i`. For a fixed bad residue `r`, define
`W(r) := {i : primes(a_i) ∩ S(r) = ∅}` — the set of *witness indices* for that residue. `W(r)` is
**fixed data depending only on `r` and the colors `{primes(a_i)}`**, not on which specific bad term
in class `r` you're looking at. This is the source of the asymmetry the bad-partner lemma lacks:
the bad-partner relation pairs individual *terms*; this pairs a whole *residue class* with a fixed
witness set.
Consequence (not yet proved, but a clean new necessary condition): **every** term `m ≡ r (mod L₀)`
must, to even be a term (membership in `E_∞` requires `gcd(m,a_i)>1` for *every* `i`, not just an
existential witness), share a prime with *every* `a_i ∈ W(r)`; since `S(m)∩primes(a_i)=∅` for such
`i` (fixed by `r`), that shared prime must be **large**. If `W(r)` is infinite, `m` (one integer,
finitely many prime factors) must — by pigeonhole on `m`'s finite factorization — share a *single*
large prime `p | m` with **infinitely many** `a_i ∈ W(r)`, i.e. `p` divides infinitely many terms of
the sequence. This is a strong, concrete, non-symmetric structural handle that no current approach
has used: it converts "the bad class is inhabited" into "some fixed large prime divides infinitely
many actual terms," which is a very different (and possibly easier, or possibly exactly as hard —
untested) target than the ascent chain. If `W(r)` is *finite* instead, then only finitely many
colors ever fail to hit `S(r)`, and the divisibility constraints on `m` reduce to a *finite*
conjunction of "share one of finitely many primes with `a_i`" over `i∈W(r)` — a genuinely tractable
finite CRT-style object, worth exploring as an alternative route to bound (or rule out) bad terms in
class `r` directly, possibly bypassing 6a/6b's chain framing altogether.
**Caveat:** whether `W(r)` is finite or infinite is itself unresolved — this is a *new* fork, not a
proof; flag to the outliner as a genuinely different top-level target (attack via residue classes,
not via the bad-partner chain) rather than a repair of Step 6→7.

**B. Largest-bad-term hypothesis, checked and found NOT to give an immediate contradiction.**
Applying the bad-partner lemma to a *hypothetical maximum* bad term `m_max` (assuming Bad is finite)
gives a bad partner `B ≠ m_max`; by maximality `B < m_max`. No contradiction: the relation is
symmetric, so nothing forces `B` to also be an ascent target. **This route is a dead-end as stated**
— confirms the run-state's diagnosis that the partner relation alone can't be flipped by looking at
the top instead of the bottom.

**C. Monovariant candidates on the shared-prime data — assessed, none currently forced.**
- *Largest shared prime `q(m,B) = max(primes(m)∩primes(B))`* along a chosen ascent step: not shown
  to be monotonic — a later mutual pair could recruit a *smaller* large prime than an earlier one;
  no argument in the lemma files forces growth.
- *Number of distinct large primes recruited over a chain* (a "color budget" argument): plausible in
  spirit (finitely many large primes could in principle be reused, so this isn't obviously bounded
  either) but nothing in the certified lemmas bounds how many distinct large primes a bad chain can
  visit — would need a genuinely new argument, currently unproved and NOT circular per se, but
  requires establishing that revisiting the *same* large prime twice yields a contradiction (untested).
- *(value, large-prime-signature) lexicographic order*: circular as stated — "large-prime-signature"
  needs its own well-ordering criterion, and nothing in the lemma files supplies a signature that is
  forced to change monotonically; without an independent argument for why revisiting a signature is
  impossible, this reduces to restating the open gap.

**D. Local (bounded-band) pigeonhole inside a window — already flagged by the approach file (Levers
(iii)) as untried; still open and worth pursuing.** Since every bad term sits in an open window
`(ka_1,(k+1)a_1)` of length `<a_1` (Step 3, certified), and the crux corpus supplies a genuine
technique template for this shape (see below), a per-window pigeonhole capping the number of bad
terms per window — combined with mechanism A's residue-class structure — could be the way to force
either (i) a fresh window/residue is needed at every step (giving unboundedness directly, not via the
symmetric partner) or (ii) an outright finite bound on total bad terms (bypassing 6a into a direct
6a+6b merge).

### Candidate technique(s)
- CRT / periodicity-of-a-property-mod-L₀ (already used for E*, extend it to R_bad and W(r): opening A).
- Pigeonhole on a *finite* object's factorization forcing a shared prime across an infinite family
  (opening A's core step) — this is a clean, standard number-theory pigeonhole, not ad hoc.
- Window/interval pigeonhole à la "φ(d) elements of any d consecutive integers are coprime to d"
  (opening D) — a genuine crux template, see below.

### Cheap-kill candidates
- Check numerically (on a synthetic/forced-bad construction, if one can be built) whether `W(r)` for
  a bad residue tends to be finite or infinite — cheap sanity check before committing to opening A's
  infinite-`W(r)` branch. (Could not test on real seeds since CSP held with zero counterexamples in
  all seeds tried so far — no bad residue has ever been observed, so this can only be probed on an
  artificially constructed "what if" scenario, not on genuine data.)
- Parity/size check: `|R_bad|` (number of bad residues mod L₀) — bounded by `2^|P|-1` at most
  (number of non-covering subsets of primes(a_1)); cheap structural fact, doesn't resolve anything by
  itself but bounds the "number of independent fronts" opening A would need to handle.

### Knowledge-base entries to use
- **Pigeonhole / extremal principle** (knowledge_base.md ~line 108, 188) — underlies opening A's
  finite-factorization pigeonhole and opening D's window cap.
- **Modular arithmetic, CRT** (line 59) and **Dirichlet's theorem / eventual periodicity mod m**
  (lines 76, 80) — directly underlie opening A's "badness periodic mod L₀" framing (already exploited
  once for E*; opening A pushes it one level further, onto R_bad and W(r)).

### Analogous past problems (cruxes)
Filtered `number_theory` × {`pigeonhole`, `invariants-and-monovariants`, `modular-arithmetic-and-CRT`,
`sequences-and-recurrences`} (122 candidates scanned).
- **aimo-0144** (`pigeonhole`/interval-counting) — "Relax a coprimality condition to a divisor of the
  modulus and use that any window of `d` consecutive integers contains exactly `φ(d)` integers
  coprime to `d`, giving a per-window cap." Genuinely analogous **template** for opening D: a bounded
  window (there, length `d`; here, length `<a_1`) combined with a modular-coprimality count gives a
  hard per-window cap. Not directly transferable (their `d` is fixed and their target is a count
  identity, not an ascent), but the "window length ↔ modulus interaction forces an exact/bounded
  count" shape is the right template to imitate for a local pigeonhole in opening D.
- **aimo-0987** ("Estonia", `2^m+m ≡ 0 mod n` for some `m`) — induction on the modulus using
  "the remainders repeat periodically starting with some exponent `M`... the period cannot contain
  all remainders" — a genuine template for exploiting periodicity-of-a-derived-quantity (here, powers
  of 2 mod `a`) to force new behavior at larger scale. Weakly analogous: illustrates how "periodic mod
  m, but the period is strictly smaller than the full residue system" can be leveraged inductively —
  relevant in spirit to opening A (badness periodic mod L₀, but the bad-residue set `R_bad` is a
  strict, hopefully-empty subset), though the actual induction machinery doesn't transfer directly.
- No crux in the corpus directly matches "greedy sequence of pairwise-intersecting sets, prove
  eventual arithmetic periodicity" — this problem's overall shape (P6-level) has no close corpus twin;
  the two above are technique-template matches only, not structural analogues of the whole problem.

### Prior progress
Steps 1–5 of `covering-small-part-descent.md` (CERTIFIED via `lemmas/bad-partner-and-ascent.md`,
`lemmas/generalized-sole-connector-off-lattice.md`): (CSP)⇒theorem; base case `|P|=1`; bad terms are
off the `a_1`-lattice; every bad term has a *bad*, *mutual* witness sharing only large primes; the
smallest bad term has a strictly larger bad witness (ONE step only). This round's task (6a) is to go
beyond that one step.

### Dead ends (do not retry)
- **Largest-bad-term / maximum-element flip of Step 5** (checked this round, opening B above): gives
  no contradiction — the partner relation being symmetric means the maximum element's witness is
  simply forced *below* it, consistent with a finite Bad set. Do not resubmit this as a route without
  a genuinely new ingredient.
- (Carried from round 4, still valid) Global `Σ1/p²` capacity counting — proven insufficient
  (`lemmas/term-density-and-prime-capacity.md`'s own negative certification): caps only a positive
  fraction of large-prime pairs, never zero.
- (Carried from round 2) Pure combinatorial covering/Helly/sunflower arguments — dead (Prop D
  barrier): the crux is false at the pure covering-set level, dynamics/value structure is required.

### Small-case / intuition notes
- On every seed tested across rounds (`a_1 ∈ {15,35,99,231,1155}`), CSP holds with **zero** bad terms
  — so `R_bad = ∅` (empty) has held in every observed instance. This is consistent with either (i)
  `R_bad` is provably always empty (the actual theorem-proving target) or (ii) bad residues can occur
  only for larger/rarer `a_1` not yet tried. No seed has ever exhibited even a single bad term, so
  opening A's `W(r)`-finite-vs-infinite dichotomy is currently untestable numerically — it can only be
  investigated analytically (by trying to *construct* a bad residue and see what forces `W(r)` to be
  finite/infinite), not by search over more seeds. **Conjecture, unverified:** it's plausible that
  `R_bad=∅` is forced by a *direct* residue-level argument (not needing the ascent at all), which
  would make opening A a route to the WHOLE crux, not just 6a — worth telling the outliner this is a
  candidate for a genuinely new top-level approach, not merely a patch to `covering-small-part-descent`.
