## imo-2026-06 (lens: GREEDY DYNAMICS / WINDOW-MINIMALITY — what does "a_{n+1} = smallest compatible
integer" force about a bad term's rejection history? Second pass at this lens; round-5's greedy-dynamics
report already scouted the terrain broadly — this pass digs into the ONE surface the dispatch asked for:
the structure of the rejected integers strictly between a_n and a bad a_{n+1}.)

### New structural fact extracted this round (not previously stated as a lemma)

**Window Purity.** Fix n and let m = a_{n+1}. By ENUM (certified `enumeration-of-E-infinity.md`), the
sequence is *exactly* the increasing enumeration of E_∞ ∩ [a_1,∞); in particular **no element of E_∞ lies
strictly between a_n and m** (not merely "no element compatible with predecessors a_1..a_n" — literally no
element of the full membership set E_∞, since ENUM says the terms ARE E_∞ enumerated). Separately, the easy
direction "S(x) covering (shares a small prime ≤P_max with every term) ⟹ x ∈ E_∞" is immediate (a small
shared prime with every term ⟹ gcd(x,a_i)>1 for all i) and is already used implicitly (e.g. E* ⊆ E_∞ in
`reduced-process-identity.md` / `csp-implies-theorem.md`). Combining:

> For every integer x with a_n < x < a_{n+1}, S(x) is **not covering** — x fails to share a small prime
> with at least one term of the WHOLE sequence (not just a predecessor).

This is a genuinely sharper, window-wide statement than anything currently cached (existing lemmas only
pin the *endpoint* m off-lattice via GPC). It says the *entire open interval* between consecutive terms is
built from non-covering integers, which is exactly the "local pigeonhole" texture Prop D says any closing
argument must use. Flagging as a candidate lemma "Window Purity" for the outliner — cheap to state,
imports only ENUM + the easy covering⟹E_∞ direction, no new machinery.

### Applying window-minimality to the actual FIN-W star configuration (bad-residue-witness-index, Step 5)

Re-derived, from the greedy-value side, the *same* pigeonhole `bad-residue-witness-index.md` Step 5
already uses (finite prime factorization of the hub m forces the infinite witness family down to ONE
fixed large prime p by pigeonhole) — confirms that step independently via a different route, not new.
Pushing further with window-minimality on the star family T_p = {t_1<t_2<…} (all ≡ r* mod L_0, all
divisible by fixed p, hub m witnesses all of them):

- Since {t_j} is strictly increasing and unbounded while m is one FIXED term, m is a **predecessor** of
  t_j for all large j. Consider a hypothetical smaller candidate x ≡ r* (mod L_0), x < t_j, x in the
  window (a_{n_j}, t_j) — i.e. any earlier element of the SAME residue class. If x is compatible with
  every predecessor, minimality forces x to already have appeared (contradiction, x should be an earlier
  term). Working out compatibility of such an x with m specifically: since S(x)=s_1 is disjoint from
  primes(m)'s small part (that's what "small-disjoint from m" means), x is compatible with m **iff x is
  divisible by SOME large prime factor of m** — and m has only FINITELY many large prime factors
  (Q_m, fixed, independent of j).
- **Consequence (the key case split this round surfaces):** if the witness-index-set W(r*) of class r*
  is a SINGLETON {index of m} (i.e. m is the *only* obstruction class r* ever needs to clear), then
  minimality gives **no leverage at all** — EVERY x ≡ r* (mod L_0) divisible by any prime in Q_m
  automatically lies in E_∞ (compatible with m via that prime, compatible with everyone else automatically
  since r* only fails to cover m's slot). This exactly reproduces the (FIN-W)⟹theorem periodicity
  contribution for that single class (Q_rel piece = Q_m, finite) — i.e. **single-witness bad classes are
  automatically consistent with FIN-W and supply no contradiction, and no obstruction either.** This
  downgrades a natural first guess (try to derive a contradiction straight from "class r* has a witness")
  and **relocates the real difficulty to classes where the witness relation is MUTUAL AND INFINITE on
  BOTH sides** — i.e. r's witness set W(r) is infinite (contains r*'s inhabitants) AND r*'s own witness
  set W(r*) is ALSO infinite (so r* needs its own infinite family of large-prime connectors, recursively).
  This is a sharper target than the flat "star exists" phrasing: the crux is really about a
  **self-sustaining bipartite (or larger) infinite witness structure**, not a single hub-vs-family pair.
  Flag this refinement to the outliner as a way to prune the search: any attempted contradiction that
  only uses ONE hub's finiteness of large primes (as above) is automatically insufficient — it must use
  BOTH sides of the pairing, or an infinite CHAIN/CYCLE of classes r_0=r, r_1=r*, r_2, … each infinite-
  witnessing the next.

### Cheap-kill candidate tested and REFUTED (report honestly, so no one retries it)

Tested numerically whether, inside a single rejection window (a_n, a_{n+1}), there is always a SINGLE
predecessor index that alone accounts for every rejected candidate (a natural simplifying guess — "one
hub per window"). Computed, for a_1 ∈ {15,35,99,231,1155}, the first 200 windows, whether a common blocking
index exists across ALL rejected x in the window:
```
a1=15:  99/199 windows fully explained by ONE blocker (~50%)
a1=35:  94/199
a1=99:  89/199
a1=231: 199/199  (100% here, but not universal)
a1=1155: 100/199
```
So "one hub blocks the whole window" is FALSE in general (only ~45-50% of windows for most a_1) — do NOT
have a builder assume single-hub-per-window as a stepping stone; multi-hub joint rejection is the norm.
(This refines/corrects round-3's softer "often exactly one hub" observation — true in aggregate/frequency,
false as a universal per-window structural fact.)

### Distinct openings

1. **Window Purity** (above) as an explicit new cheap lemma — feeds any local pigeonhole attempt without
   invoking the dead global Σ1/p² count; strictly local (per-window), consistent with Prop D's mandate.
2. **Mutual-infinite-witness refinement** (above): recast the standing (FIN-W)/star wall as needing a
   BOTH-SIDES infinite pairing (or a longer cycle r_0→r_1→r_2→…→r_0 of classes each witnessing the next
   with infinite index sets), since single-sided infinite witness relocates harmlessly into FIN-W's own
   finite-Q_rel bookkeeping. This is a genuinely narrower, more attackable target than "rule out any star."
3. **Extremal principle on q\* (linking prime) — from round 5, still open, still promising**: well-order
   the set of ever-occurring sole/only-large-prime links by their prime value, not by term value, to escape
   the proven-symmetric term-value witness relation (bad-partner-and-ascent). Combine with Lemma B
   (`minimal-linking-prime-and-window-cap.md`, certified): multiples of any prime ≥ q* are spaced ≥ q*
   apart inside a length-a_1 window, giving a genuinely local (not global) counting handle. UNDEVELOPED.
4. **Chain/cycle-of-classes framing**: if the mutual-infinite-witness structure (opening 2) is real, model
   it as a directed graph on R_bad (r → r' if r' is a witness-inhabited class reachable via some index in
   W(r)), and ask whether this graph must be finite (only finitely many bad classes total, |R_bad| ≤ L_0
   is ALREADY certified finite) — so any "infinite cycle" must actually revisit classes; the interesting
   question becomes whether REVISITING a class r after some steps forces a strictly SMALLER large prime
   each time you can extract via pigeonhole (feeding into opening 3's q* well-ordering) — i.e. combine
   openings 2+3: a finite class graph (≤L_0 nodes) traversed by an infinite process must repeat a class,
   and repeated visits to the same finite class r with the SAME finite Q_m-type prime pool each time is a
   strong pigeonhole lever nobody has assembled yet. UNDEVELOPED but concrete; strongest lead to hand off.

### Candidate technique(s)
Extremal principle on a NEW object (linking prime q*, or class-graph cycle structure) rather than term
value (which is provably symmetric/stuck); local per-window pigeonhole (Window Purity + Lemma B spacing
cap), explicitly avoiding the dead global Σ1/p² route and the dead pure-covering/Helly route (Prop D).

### Cheap-kill candidates
- Window Purity (cheap, certifiable in ~5 lines, strengthens what's known about the interior of every gap).
- "Single hub per window" — TESTED, FALSE, do not use as a stepping stone (see above).
- "Single-witness bad class gives a contradiction" — TESTED ABSTRACTLY, gives NO obstruction (reproduces
  FIN-W's own finite bookkeeping); the true difficulty needs mutual/cyclic infinite witnessing (opening 2).

### Knowledge-base entries to use
"Pigeonhole / extremal principle" (finite classes R_bad ≤ L_0, finite Q_m per hub) — directly licenses
opening 4's class-graph pigeonhole; "Invariants & monovariants" — for framing q* or a class-graph
revisit-count as the monovariant; "Infinite descent" framing — motivates why a FRESH extremal object
(prime, or class, not term value) is needed to escape the symmetric term-value trap (per round 5's finding).

### Analogous past problems (cruxes)
- **aimo-0626** (`combinatorics`/`processes-and-algorithms`): "From a minimal-length nonnegative-sum
  certificate at one index, deduce every index it spans is also certified, so a left-to-right greedy sweep
  tiles the certified set into disjoint consecutive blocks" — a genuine structural analog for "minimality
  of a chosen witness forces rigid structure on everything it spans." The shape (minimal witness ⇒ every
  interior point inherits the same certification) is closer in spirit to Window Purity than anything found
  in prior rounds' corpus search, though the algebraic mechanism (nonnegative-sum minimality) doesn't
  transplant literally — worth the outliner reading `aimo-0626` in `past_problems_database.json` for the
  proof shape, not the algebra.
- **aimo-0620** (`processes-and-algorithms`): "reach the target by repeatedly deleting any element made
  redundant by the others, then argue the terminal irreducible state already IS that structure" — matches
  the already-explored RED_n / redundancy framing in `reduced-process-identity.md`; no new content beyond
  what's cached, listed for completeness only.
- aimo-0678, aimo-0514, aimo-0477 — already assessed in round 5's report (aimo-0678 closest structural
  donor for a process-level monovariant, aimo-0514/aimo-0477 weaker/re-collapse); not re-litigated here.

### Prior progress
Unchanged inherited terrain (all certified, reusable, do NOT re-prove): ENUM, PER, F1, GPC, CSP⇒theorem,
bad-partner+ascent (Step-5 single symmetric ascent), Lemma 6 (6a closer, unbounded fixed-signature family),
FIN-W⟹theorem (Reduction Lemma, strictly weakens crux), q*/window-cap (Lemma A/B). The crux remains the
single wall (6b)/(FIN-W star)/(DESC), still open. This round's contribution is NOT a closure — it is (i) a
new cheap lemma (Window Purity), (ii) a refutation of a tempting simplification ("single hub per window"),
and (iii) a sharpened target (mutual/cyclic infinite witnessing, not a flat single star) plus a concrete
combination (opening 4: finite class graph + repeat-visit pigeonhole) that no prior approach has assembled.

### Dead ends (do not retry)
All previously-recorded dead ends stand (pure covering/Helly — Prop D; global Σ1/p² capacity;
"smaller compatible candidate in an empty window" — G3; P_max-smoothness of witnesses — false,
a_1=231 counterexample; self-dual-clutter-grading's grading lever — RETHINK). NEW this round: "single
hub explains every rejection in a window" is false as a universal fact (only ~45-100% depending on a_1,
never reliably 100%) — do not build a proof step assuming it. "A single-witness bad class alone yields a
contradiction" is a dead lever (gives no obstruction at all, just reproduces FIN-W bookkeeping) — do not
have a builder spend effort trying to contradict a lone single-witness star; target mutual/cyclic
witnessing instead.

### Small-case / intuition notes (conjecture)
All empirical evidence (this round and prior rounds) is consistent with (CSP) holding always (zero
counterexamples across 20+ seeds and now explicit window-level rejection-structure checks on 5 seeds ×
200 windows). No real bad term, single-witness star, or mutual-witness structure has ever been observed to
occur — the obstruction, if it exists at all, is a genuine non-existence statement that cannot be
falsified further by simulation; it needs the proof. The new finding (opening 2) that single-sided
infinite witnessing is actually HARMLESS is itself a conjecture-strength structural claim derived from
abstract reasoning about the certified machinery (not yet peer-checked by the outliner/reviewer) — worth
flagging explicitly as "derived here, not yet certified" so the outliner verifies it independently before
building on it.
