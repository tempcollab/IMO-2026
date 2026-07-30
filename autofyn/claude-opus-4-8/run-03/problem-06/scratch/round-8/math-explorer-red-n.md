## imo-2026-06 — lens: RED_n reverse-inequality route vs the weakened ¬(FIN-Q) crux

### 1. RED_n stated precisely
Notation as in `reduced-process-identity.md`: P=primes(a_1), P_max=max P, S(m)=primes(m)∩[2,P_max]
("small support"), S_i:=S(a_i).

**(RED_n):** S_{n+1} meets S_k for every k≤n — i.e. the small support of the newly-chosen term
already intersects the small support of every predecessor.

Equivalent phrasing via the "Easy/reverse" split: let
β := min{m>a_n : S(m)∩S_k≠∅ ∀k≤n}. The certified enumeration gives the **easy direction**
a_{n+1} ≤ β (β is itself E_n-compatible, being a multiple of a_1 by (F2)). (RED_n) is exactly the
**reverse inequality β ≤ a_{n+1}**, i.e. a_{n+1} IS one of the candidates β competes for — the
already-minimal greedy value happens to have a small support that is predecessor-covering. Ranging
over all n, (RED_n ∀n) is proved (§4 of the approach file) to be **exactly equivalent to (SL)/(CSP)**:
this is not an approximation, it is an if-and-only-if (checking a_{j} against predecessors at every
step n≥j-1 exhausts every ordered pair (i,j), i<j).

### 2. Do the new certified lemmas give leverage on RED_n? (concrete check)

**Window Purity — NO new leverage; it is a strictly weaker restatement of a fact RED_n's own
authors already used.** Window Purity says: no x with a_n<x<a_{n+1} lies in E_∞ (the GLOBAL
compatibility set, checked against ALL terms). But §5(G3) of reduced-process-identity already uses
the STRONGER fact that no x in (a_n,a_{n+1}) lies in E_n (compatible with only the first n
constraints) — since E_∞⊆E_n, "∉E_n" ⟹ "∉E_∞", so Window Purity is logically implied by (and
weaker than) what the approach already had. Concretely: G3 already says "(SL_n) cannot be
established by exhibiting a compatible integer smaller than a_{n+1}: no such integer exists" — this
IS Window Purity's content, already on the page since round 4. **Verdict: no new leverage from
Window Purity specifically.**

**minimal-bad-term-floor-tightness (Lemma 9) — genuine new leverage, but it exposes a bifurcation,
not a closing.** Key move: since the sequence is strictly increasing, "smallest bad term by VALUE"
= "first bad term to APPEAR by index." Suppose RED_n first fails at index n (a_{n+1} misses some
predecessor a_k, k≤n). Two structurally different scenarios are consistent with this:
- **Case (I): a_{n+1} itself is the global minimal bad term m_0.** This holds provided a_1,…,a_n are
  each *globally* good (S(a_i) covers every term, past AND future — not just pairwise among
  themselves). Under that provision, Lemma 9 applies directly to m_0=a_{n+1}: C:=primes(a_{n+1}) is
  covering (REAL), S(a_{n+1}) non-covering (bad), and the dichotomy gives either (B) a sheddable
  prime p with a_{n+1}<a_1·p, or (A) a_{n+1} squarefree with C a *minimal covering set containing a
  large prime* — precisely the dispatch's crisp value target ("no minimal covering set containing a
  large prime has minimal realization ≥a_1"). So in Case (I), RED_n's failure reduces EXACTLY to the
  crisp value target already on record from covering-small-part-descent/lex-rewrite-descent — no new
  target, but a genuine confirmation that RED_n's induction, run to its first failure, lands on the
  identical crisp statement.
- **Case (II): a_{n+1} is not itself bad — it merely reveals that an EARLIER, already-fine-looking
  predecessor a_k is bad, via a_{n+1} as a *future* witness.** This is only possible if a_k satisfied
  RED at its own step (met all ITS predecessors) but is missed by a much LATER term a_{n+1}. This is
  **exactly the star / ¬(FIN-Q) configuration** already isolated in round 5–7 (bad-residue-witness-
  index, window-purity-class-cycle): a hub that looks compatible with everything checked so far, later
  found small-disjoint from an infinite/large-prime-linked family. In Case (II) Lemma 9 does NOT apply
  to a_{n+1} (it isn't m_0) — it applies to a_k, but a_k's badness witness (a_{n+1} or later terms) is
  precisely the unresolved ¬(FIN-Q) machinery, not new content.

Both cases are logically exhaustive of "RED_n fails at step n." **Conclusion: minimal-bad-term
floor-tightness does not close RED_n; it proves RED_n's failure mode bifurcates into exactly the two
already-open faces of the crux** — the crisp value target (Case I) and ¬(FIN-Q)/star (Case II). No
new open sub-problem is created, but this bifurcation itself could be worth certifying as an
organizing lemma: it shows a full resolution of ¬(FIN-Q) + the crisp value target automatically
disposes of RED_n too — so RED_n is not an independent thing to separately solve.

**Local Hub-Cover** — adds nothing new beyond what §5(G5)(c) of reduced-process-identity already
notes (the missed predecessors' bridging large primes need not be distinct) — Local Hub-Cover
formalizes that the finitely many large primes of a bad hub jointly cover every missed color, which
is the same content G5(c) already flags as "the residual difficulty," not a new fact for RED_n.

### 3. Is RED_n mechanistically different, or does it collapse to the same wall?
**It collapses.** Per point 2's Case (I)/(II) split: RED_n's reverse inequality, pursued via
well-ordering + Lemma 9, does not open a third avenue — it exactly reproduces the disjunction
{crisp value target, ¬(FIN-Q) star} that the descent (covering-small-part-descent) and dynamics
(window-purity-class-cycle) routes already stand on. The "genuinely new" framing promised by the
dispatch does not materialize as an independent mechanism; RED_n is best understood as the
*induction-indexed* packaging of the identical crux, not a separate route. This matches the approach
file's own honest §5/§6 accounting (unchanged since round 4): the reverse inequality is a property of
the VALUE a_{n+1}, not an existence-of-competitor statement, and no combinatorial/CRT trick manufactures
a smaller candidate (G3) — exactly why Window Purity adds nothing (same fact) and why Lemma 9 only
sharpens which of the two known wall-faces is in play.

### 4. Dead ends / do not retry
- Competitor/minimality in the empty window (G3): proven structurally impossible — the interval
  (a_n,a_{n+1}) is void of E_n, so no smaller compatible integer can be exhibited. Do not re-attempt
  "find a smaller candidate" arguments under any name (this is also why Window Purity, despite being
  freshly certified, is not new ammunition here).
- The false target "a_{n+1} is P_max-smooth" (G2 caveat; a_1=231, 237=3·79 is a good term with a large
  prime factor) — already flagged, still correct to avoid.
- Direct (q*,k) active-rewrite (lex-rewrite-descent §1) — independently pruned, applies equally here:
  no local covering-preserving exchange operator exists (Prop D barrier).
- Global Σ1/p² capacity counting — proven incapable (bounds a positive fraction, never zero).

### Recommendation for the outliner
Given the collapse in point 3, reduced-process-identity's RED_n framing should NOT be advanced as if
it were a fresh independent attack; its only remaining value is as a clean *packaging* (via the
Case I/II split above) that shows solving ¬(FIN-Q) AND the crisp minimal-covering-set value target
together is fully sufficient and necessary — i.e. it is a certifiable reformulation lemma ("RED_n
failure ⟹ Case I [crisp value target] or Case II [¬(FIN-Q) star], both already-open"), not a new
proof route. The genuinely open surface remains what round 7 identified: either (a) prove no minimal
covering set containing a large prime has realization ≥a_1 (closes Case I and, by the Lemma-9 chain,
subsumes most of (6b)), or (b) rule out ¬(FIN-Q) directly (an infinite-distinct-large-connector star).
Neither is touched by this round's RED_n excursion. If a genuinely different top-level attack is
wanted this round (per the diversity mandate), it should NOT be another repackaging of the same
induction/descent machinery — it needs a structurally different invariant (e.g., an analytic/counting
argument on Q(r) growth rates, or a direct construction ruling out infinite distinct-large-connector
pools via a growth-rate contradiction on how fast new large primes could recruit new class members
without violating the a_1-window bound (F3): each new distinct connector q_k must itself appear as a
factor of some term within a bounded window, which costs at least one "slot" per a_1-length window —
this counting has NOT been tried in this exact form and is worth a dedicated approach next round,
distinct from RED_n/(6b)/covering-descent.

### Analogous past problems (crux corpus)
Queried `past_crux_moves_database.json` filtered to subtopics `processes-and-algorithms`,
`invariants-and-monovariants`, `sequences-and-recurrences` for "greedy"/"minimal element" moves.
- **aimo-0626** (crux: "from a minimal-length nonnegative-sum certificate at one index, deduce every
  index it spans is also certified, so a left-to-right greedy sweep tiles the certified set into
  disjoint blocks"). Genuinely analogous IN STRUCTURE: it is exactly the same shape of move attempted
  here — using minimality of a witnessed object to force a covering/structural property on everything
  it touches, then tiling. Worth reading as a template for HOW a minimality argument closes a covering
  gap, though the P6 setting (multiplicative/prime-support, not additive) means no direct transplant —
  it's a mechanism analogy, not a technique transplant.
- **aimo-0718** (Elisa's chests): pigeonhole on the r+1 smallest objects to dominate a greedy minimum —
  same "greedy min forced below rank-r+1 objects" shape as (F3)'s bounded-gap fact, but for a
  majorization/potential-function proof, not a finiteness/periodicity proof; less analogous than
  aimo-0626, only the pigeonhole-on-smallest flavor transfers.
- No corpus entry directly resembles the multiplicative covering-set / prime-connector machinery of
  P6 (this problem's mechanism — periodicity of a residue-defined set via CRT + covering hypergraph —
  appears to be genuinely unusual relative to the corpus's greedy/invariant problems).

### Prior progress (unchanged by this scouting)
Whole problem reduced (gap-free) to ¬(FIN-Q): rule out an E_∞-inhabited bad residue class with an
infinite distinct-large-connector pool, equivalently: no minimal covering set containing a large prime
realizes ≥a_1. RED_n is proved equivalent to (SL)/(CSP) globally but, per this report, offers no new
proof surface beyond that disjunction.

### Small-case / intuition notes (conjecture only)
No bad term / RED_n failure has EVER been observed computationally (20+ seeds, a_1 up to several
thousand, 40–200 terms). This is consistent with, but does not prove, ¬(FIN-Q) / the crisp target
being unconditionally true. No new numeric probing was run this round (would only reconfirm existing
zero-counterexample evidence, already recorded).
