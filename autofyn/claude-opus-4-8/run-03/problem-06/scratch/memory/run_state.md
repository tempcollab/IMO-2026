# Run State — imo-2026-06

## Goal
Produce a complete, rigorous prose proof of IMO 2026 Problem 6.

Problem: Let a_1,a_2,... be an infinite sequence of integers >1. For all n, a_{n+1} is
the smallest integer > a_n with gcd(a_{n+1}, a_i) > 1 for every i=1..n. Prove there exist
positive integers T and L such that a_{n+T} = a_n + L for every positive integer n
(the sequence is eventually — in fact everywhere — arithmetic-periodic with period T, shift L).

Metric: proof-reviewer verdict on results/imo-2026-06/current.md.
Eval: proof-reviewer adversarial judgement (solved | partial | unsolved).
Baseline (round 1 start): unsolved — empty workspace, no approaches yet.
Target: Status `solved` = APPROVE (complete, rigorous, no gaps).
Constraints: prose Markdown proof; no Lean; no web; every non-trivial step justified;
name every theorem and cite knowledge_base.md; no skipped cases; no hand-waving.

## Goal Updates
- [Round 1] Initial task set: solve imo-2026-06. No user changes since.

## Eval History
- Round 1 start: baseline = unsolved, empty approach population.
- Round 1 end: Status = partial (IMPROVED — from nothing to a full reduction). 4 approaches registered.
  Ranking (Elo, outline-reviewer): enum-covering-primes 1546, density-bounded-recruitment 1515,
  finite-state-window 1485, difference-sequence-squeeze 1454 (registered, not built). All 3 built = "advanced".
  proof-reviewer: all 3 CHANGES REQUESTED / partial (no overclaim). Scaffold FULLY PROVED + certified:
  (1) sequence = increasing enumeration of E_∞ ∩ [a_1,∞)  [lemma cache: enumeration-of-E-infinity.md];
  (2) E_∞ periodic mod L ⇒ a_{n+T}=a_n+L for EVERY n, T=#(E_∞∩[a_1,a_1+L)) [lemma cache: periodic-set-enumeration.md];
  (3) gaps a_{n+1}-a_n ≤ a_1 proved. SOLE OPEN CRUX (shared wall, 3 equivalent phrasings):
  no prime > largest prime factor of a_1 is ever load-bearing / every two terms share a prime ≤ a_1 /
  R₀={primes ≤ maxfactor(a_1)} sufficient. Verified 0 counterexamples on 20+ seeds, UNPROVEN.
  Disproved side-guesses: R⊆primes(a_1)∪{2,3} FALSE (a_1=99 recruits 5); pure asymptotic density can't
  isolate load-bearing primes (E_∞ periodic ⇒ every prime has positive density in it).
- Round 2 end: Status = partial (PLATEAU on solve flip, but IMPROVED structurally — crux narrowed + 2 route
  eliminations). 3 explorers scouted the crux from non-E_∞ angles; outliner opened 3 far-apart new framings;
  all 3 built + reviewed. Ranking: enum-covering-primes 1568, reduced-process-identity 1550 (NEW),
  density-bounded-recruitment 1525, cofactor-recruitment-smoothness 1503 (NEW), finite-state-window 1482,
  large-prime-capacity-counting 1473 (NEW, dead-end), difference-sequence-squeeze 1399.
  proof-reviewer verdicts: reduced-process-identity CHANGES REQUESTED/partial; cofactor-recruitment-smoothness
  CHANGES REQUESTED/partial; large-prime-capacity-counting RETHINK/unsolved-as-route (proven dead route).
  4 NEW certified/cached items this round:
  * lemmas/sole-connector-off-lattice.md (Prop C: a term whose only shared prime with some predecessor is >P_max
    is NEVER a multiple of a_1 — squeezed off the a_1-lattice into a length-<a_1 window). CERTIFIED.
  * lemmas/term-density-and-prime-capacity.md (C1 term density ⌊X/a_1⌋−1≤N(X)≤X; C2 per-prime pair cap;
    C3 large-prime pair capacity ≤ 0.202·X² via Σ_{p>P_max}1/p²). CERTIFIED.
  * reduced-process-identity: E* = small-support (≤P_max) compatible set is EXACTLY periodic mod L_0=∏(p≤P_max)
    by CRT (finitely many subsets) — RIGOROUS; whole theorem reduced to single inclusion (SL) E_∞∩[a_1,∞)⊆E*.
  * Prop D barrier (cofactor approach): the crux is FALSE at the pure covering-set/Helly level (explicit
    intersecting family {p1,q},{p2,q},{p1,p2} has large q in a minimal member) ⇒ ANY proof MUST use greedy
    dynamics; purely combinatorial (Helly/sunflower/covering) attacks are DEAD. Verified as barrier (its
    "any proof needs dynamics" reading is heuristic, not cached).
  Crux now 3 DISTINCT walls (diversity restored): (a) reverse termwise inequality a_{n+1} small-hits every
  predecessor [reduced-process-identity]; (b) witness cofactor P_max-smooth via window-minimality [cofactor];
  (c) localize-to-globalize [capacity — PROVEN insufficient alone]. Reviewer noted (SL)⟺LemmaA only has ⟹
  proved (two shared large primes could break reverse) — minor, doesn't affect verdict.

- Round 5 end: Status = partial (IMPROVED structurally — sub-gap (6a) UNBOUNDEDNESS is now CLOSED, though no
  solve flip). 3 explorers (nonsym-ascent, local-contradiction, greedy-dynamics) → outliner opened 2 far-apart
  NEW framings + advanced 1 → outline-reviewer built 3 → proof-reviewer all 3 CHANGES REQUESTED/partial.
  Ranking (Elo): reduced-process-identity 1630 (top, parked/not built), enum-covering-primes 1597,
  covering-small-part-descent 1577, bad-residue-witness-index 1520 (NEW), minimal-linking-prime-extremal 1492 (NEW).
  3 NEW lemmas CERTIFIED this round:
  * lemmas/bad-signature-geometric-family.md (Lemma 6): if m is bad then m·r^k is bad with the SAME non-covering
    signature S(m) and SAME witness, for every prime r|m and k≥0 (via certified Realizability clause c). CLOSES
    sub-gap (6a) — manufactures an explicit UNBOUNDED family of bad terms WITHOUT the symmetric Step-5 ascent,
    dissolving the round-4 m0↔witness symmetry obstruction. Caveat: single fixed-signature sparse orbit, so (6b)
    is untouched. CERTIFIED (reviewer re-derived independently).
  * lemmas/finite-witness-periodicity.md (Reduction Lemma): (FIN-W) "each term is small-disjoint from only
    finitely many terms" ⟹ theorem DIRECTLY via E_∞ periodicity mod enlarged M=L_0·∏Q_rel (bypasses CSP).
    Since (CSP)⟹(FIN-W)⟹theorem, strictly WEAKENS the crux. CERTIFIED gap-free.
  * lemmas/minimal-linking-prime-and-window-cap.md: q*=min large prime that is a sole connector of a bad pair
    (well-defined, floors every large link ≥ q*); per-window spacing cap ≤ a_1/q*+1 multiples of p≥q*. Modest
    but CERTIFIED; local, avoids dead global count.
  KEY FINDING: all three crux faces re-converged to ONE certified-equivalent wall — (6b) value-contradiction ≡
  (FIN-W) infinite-witness "star" branch (a hub term small-disjoint from an infinite off-lattice family divisible
  by one fixed large prime in one class mod L_0) ≡ (DESC) bad-window-index has no minimum. Reviewer: no overclaim
  in any Status. aimo-0016 "infinitely-often⇒always" template checked and does NOT transplant (no per-index local
  recurrence). Reviewer recommends next round seed a framing on the GREEDY DYNAMICS of how a_{n+1} is chosen.

- Round 7 end: Status = partial (IMPROVED structurally — crux STRICTLY WEAKENED FIN-W→FIN-Q; one route pruned
  dead; no solve flip). NOTE: round 6 never executed (empty /tmp/round-6, ranking was last_round=5); round 7
  picked up the round-6 plan. 3 explorers (greedy-dynamics, star-config, foreign-technique) → outliner opened 2
  NEW far-apart framings + advanced 2 → outline-reviewer built 3 (bad-residue-witness-index kept live/not built,
  converged onto window-purity framing) → proof-reviewer: 2 CHANGES REQUESTED/partial + 1 RETHINK/dead-end.
  Ranking (Elo): reduced-process-identity 1628 (top, parked), covering-small-part-descent 1627, enum-covering-
  primes 1597, window-purity-class-cycle 1568 (NEW), bad-residue-witness-index 1521, lex-rewrite-descent 1483
  (NEW, dead-end).
  4 NEW lemmas CERTIFIED this round:
  * lemmas/window-purity.md (Lemma 1/7): EVERY integer strictly between consecutive terms a_n, a_{n+1} is outside
    E_∞ (non-covering small part) — direct from ENUM + covering⟹E_∞. Local greedy handle. CERTIFIED (both
    window-purity-class-cycle & covering-small-part-descent proposed it; certified once).
  * lemmas/finite-connector-pool-periodicity.md ((FIN-Q)⟹theorem): STRICTLY WEAKENS the crux FIN-W→FIN-Q —
    periodicity holds as soon as each inhabited bad class r has a FINITE large-connector POOL Q(r)=⋃Q_i, EVEN IF
    its witness index set W(r) is INFINITE (membership dichotomy (★) is an infinite conjunction of conditions each
    depending only on m mod M, hence itself a function of m mod M). CERTIFIED. New crux = ¬(FIN-Q): an inhabited
    bad class with infinitely many DISTINCT large connector primes (q_k→∞), NOT the old single-fixed-prime star.
  * lemmas/local-hub-cover.md (Lemma 8): a bad term h's FINITELY many LARGE primes Q(h) jointly cover every color
    W(h) that S(h) misses (from Realizability 𝒯⊆𝒞 + pigeonhole). LOCAL capacity fact, distinct from dead global
    Σ1/p² count. CERTIFIED.
  * lemmas/minimal-bad-term-floor-tightness.md (Lemma X/9): downward dual of Lemma 6. Smallest bad term m_0 is
    floor-tight: v_p(m_0)≥2 ⟹ m_0<a_1·p (same for any redundant prime); removing an exponent/redundant prime
    yields a SMALLER bad term with same non-covering small part — genuine lower-pressure value constraint. CERTIFIED.
  KEY FINDINGS: (a) lex-rewrite-descent RETHINK/DEAD — the designed asymmetric rewrite operator PROVABLY does not
  exist: lowering the linking prime below q* is verbatim the negation of Lemma A minimality (equivalent-strength,
  circular), and covering-preserving exchange is blocked by Prop D. aimo-0009 shift-overshoot fallback has no
  inequality analogue. Salvaged Lemma X. (b) BOTH live carriers' gaps re-converged to the SAME sharpened value
  threshold: covering-small-part-descent's (6b) blocks EXACTLY at the a_1 threshold in Realizability clause (c)
  (reduced value can fall below a_1; abstract covering admits large minimal members — Prop D); crisp checkable
  target: "no minimal covering set containing a large prime has minimal realization ≥ a_1." window-purity-class-
  cycle's Step 5 descent (class-graph revisit) unclosed — q* is only a floor, refined star has q_k→∞ ascending so
  no monotone descent from assembled material. Reviewer: NO overclaim. Numerics: 0 bad terms across 29+ seeds
  (CSP may hold unconditionally).

- Round 9 end: Status = partial (PLATEAU on solve flip, IMPROVED — 4 lemmas certified incl a certified
  divisibility face (EC); 2 of 3 lanes SELF-CERTIFIED their distinctive lever dead). NOTE: round 8 ran only
  explorers→outliner→outline-reviewer (no build/review; ranking was last_round=7); round 9 completed the round-8
  flow. Built the round-8 build set: minimal-cover-small-only (NEW), covering-small-part-descent (ADVANCE),
  bounded-window-distinctness (NEW). proof-reviewer: covering-small-part-descent CHANGES REQUESTED/partial;
  minimal-cover-small-only RETHINK/dead-end; bounded-window-distinctness RETHINK/dead-end.
  Ranking (Elo): covering-small-part-descent 1660 (top live carrier), reduced-process-identity 1628 (parked),
  enum-covering-primes 1597, window-purity-class-cycle 1530, minimal-cover-small-only 1524 (DEAD), bad-residue-
  witness-index 1521, bounded-window-distinctness 1482 (DEAD).
  4 NEW lemmas CERTIFIED this round:
  * lemmas/csp-iff-E-small-only.md ((CSP)⟺ℰ-small-only: no large prime is load-bearing in ANY minimal covering
    set). Proved INDEPENDENTLY by TWO lanes (covering-small-part-descent + minimal-cover-small-only) — cross-check.
    CERTIFIED. Confirms the transversal face and the value face are the SAME certified-equivalent wall.
  * lemmas/essential-connector-equivalence.md (Lemma 13 EC + Lemma 14 propagation): CSP fails ⟺ some large prime
    q is an ESSENTIAL CONNECTOR for a non-covering set A (every A-avoiding term is divisible by q ⟺ A∪{q} covering,
    A not). NEW certified term-DIVISIBILITY face of the crux. Lemma 14: essentiality self-reproduces with q PRESERVED
    (every A-avoiding term B gives a failing config (primes(B)\{q}, q) with the SAME q). CERTIFIED.
  * lemmas/intersecting-clutter-and-spawning.md (Lemmas A/B/C = Lemma 12 spawning). CERTIFIED (salvaged from the
    dead minimal-cover-small-only route).
  * lemmas/distinctness-by-difference.md (local: a large prime q>window-length divides ≤1 term in a bounded value
    window). CERTIFIED (salvaged from the dead bounded-window-distinctness route).
  KEY FINDINGS: (a) minimal-cover-small-only RETHINK/DEAD — its Lemma D self-certifies the transversal target IS
  literally (CSP), and its only lever (partner map) is HORIZONTAL (no downward monovariant; primes unbounded
  upward), stalling exactly as the refined star did. (b) bounded-window-distinctness RETHINK/DEAD — its (R2′)
  RIGOROUSLY proves the distinctness closer is IMPOSSIBLE: confining the ¬(FIN-Q) new-prime pool to a bounded
  value-band [a_1,V) is EQUIVALENT to Q(r_0) being finite = the negation of ¬(FIN-Q) itself, so distinctness-by-
  difference can only bite where its conclusion is already assumed (vacuous). Sharpens round-8's heuristic Prop R
  to a rigorous impossibility. (c) 4th+ collapse to ONE wall; the wall is now certified-equivalent across
  (CSP)=ℰ-small-only=(EC)=¬(FIN-Q). Reviewer flag: next round MUST field a genuinely DIFFERENT framing — NOT
  another CSP/ℰ/EC/FIN-Q reformulation (exhausted). Missing ingredient = a VALUE/DYNAMICS lower-pressure
  inequality tying a_1 to the covering structure via the GREEDY SUCCESSOR CHOICE, which no static-covering
  reframing has produced. Reviewer: NO overclaim in any Status.

- Round 8 end: interrupted — ran only 3 explorers (red-n, value-inequality, foreign) → proof-outliner →
  outline-reviewer (build set: minimal-cover-small-only, covering-small-part-descent, bounded-window-distinctness).
  NO build/review (autocommit "ended without summary"). Field + build set carried into round 9 and executed there.

- Round 3 (interrupted): explorers (reverse-inequality, window-minimality) + outliner ran; NO review/build
  (autocommit "ended without summary"). Field carried into round 4.
- Round 4 end: Status = partial (PLATEAU on solve flip, IMPROVED structurally — round-2 (SL)⟸ gap CLOSED;
  crux recast in a NEW value-ascent form with a PROVEN ascent engine). Processed round-3 outliner field:
  outline-reviewer approved 4, built 3 (covering-small-part-descent NEW, reduced-process-identity advance,
  self-dual-clutter-grading NEW). proof-reviewer verdicts: covering-small-part-descent CHANGES REQUESTED/partial;
  reduced-process-identity CHANGES REQUESTED/partial; self-dual-clutter-grading RETHINK/unsolved-as-route.
  Ranking (Elo): reduced-process-identity 1609 (top), covering-small-part-descent 1577 (new), enum-covering-primes
  ~1568, reduced ... self-dual-clutter-grading 1508 (dead-end). 4 NEW lemmas CERTIFIED this round:
  * lemmas/generalized-sole-connector-off-lattice.md (GPC): two terms sharing NO small prime (any # of large,
    not just singleton) ⇒ a_1 divides neither. CLOSES the round-2 reviewer-flagged (SL)⟸ multi-large-prime gap.
    Supersedes sole-connector-off-lattice singleton phrasing. CERTIFIED.
  * lemmas/csp-implies-theorem.md: ORDER-FREE (CSP)⇒theorem via E*={m>1:S(m) hits every color}, periodic mod
    L_0=∏(p≤P_max); under (CSP) E*∩[a_1,∞)=E_∞∩[a_1,∞). Removes the (SL) intermediary. CERTIFIED.
  * lemmas/realizability-and-self-dual-clutter.md: 𝒞=𝒯 (every covering prime-set realized by an actual term
    m=(∏S)·p0^k∈E_∞) + self-dual clutter b(ℰ)=ℰ + every-term-meets-P. CERTIFIED (the value ingredient Prop D lacks).
  * lemmas/bad-partner-and-ascent.md: bad-partner lemma (every bad term has a bad witness sharing only large
    primes) + smallest-bad-term ascent (the smallest bad term has a strictly larger bad witness). CERTIFIED.
  KEY FINDING: all 3 framings (descent, redundancy, clutter-grading) collapse to the SAME wall — derive a
  contradiction from an INFINITE strictly-ascending, large-prime-linked chain of off-lattice bad terms, each in
  a length-<a_1 window with a good a_1-multiple within distance a_1. Ascent ENGINE now proven (Step 5); the gap
  is cleanly TWO-fold: (6a) UNBOUNDEDNESS — Step 5 gives only ONE ascent (witness relation is SYMMETRIC on a
  mutual bad pair, so m_1's witness can be m_0 again — no chain yet); (6b) CONTRADICTION from the chain (global
  capacity proven dead). self-dual-clutter-grading confirmed this same wall ⇒ RETHINK, lemmas salvaged.

- Round 10 end: ***SOLVED — BREAKTHROUGH.*** proof-reviewer APPROVE / Status = solved. Approach
  `smallest-essential-prime-descent` (NEW this round) produced a COMPLETE, rigorous proof of IMO 2026 P6.
  Mechanism: recognize the greedy sequence = increasing enumeration of E_∞∩[a_1,∞) (certified ENUM), define
  m≥a_1 "good" iff m∈E_∞, use the CRUDER notion "small prime := ≤a_1" (NOT P_max), and transplant the aimo-0030
  / 2015-ISL "Ana–Banana" game calculus: F1 (recursive good/bad char. from the greedy rule), F2/F3, Claims 1–3,
  and a minimal-pair value-descent proving the Main claim "similar (same primes ≤a_1) ⟹ same status". Hence E_∞
  tail-periodic mod M=∏_{p≤a_1}p; (ENUM)+(PER) give a_{n+T}=a_n+L for every n, T=#(E_∞∩[a_1,a_1+M))≥1, L=M.
  Reviewer INDEPENDENTLY re-derived F1,F2,F3,Claims 1–3, both descents; numerically 0 counterexamples for
  a_1∈{15,16,17,30,35,45,99,100,210,231}. current.md written with Full proof. Terminal lemma certified:
  lemmas/recursive-good-bad-and-similarity-closure.md. The 10-round certified wall ((CSP)=ℰ-small-only=(EC)=
  ¬(FIN-Q)) was BYPASSED, not broken — the crude ≤a_1 notion + "similar⟹same status" never needs the
  large-prime finiteness statement at all. Also certified this round: lemmas/hub-abundance-under-not-finq.md
  (Lemma 15, from covering-small-part-descent, gap-free; that lane self-diagnosed its value-monovariant stall —
  CHANGES REQUESTED, now moot). greedy-successor-jump-monovariant proposed but RETHINK at outline stage (ENUM
  makes greedy=static enumeration, no dynamical lever; dichotomy collapses to CSP — circular). GOAL ACHIEVED.

## Rules
- SOLVED (round 10): imo-2026-06 is SOLVED. Do NOT re-attempt. Full proof in results/imo-2026-06/current.md.
- KEY LESSON (round 10): the 10-round shared-gap plateau was broken by ABANDONING the framing that defined the
  wall. The P_max/covering framing (all 4 certified-equivalent faces) required proving "no large prime is
  load-bearing"; switching to the crude "small prime := ≤a_1" notion + a recursive good/bad calculus +
  "similar⟹same status" makes that statement UNNECESSARY. When a field collapses to one wall for 3+ rounds, the
  fix was a genuinely different OBJECT/definition (per CLAUDE.md shared-gap rule + foreign-technique corpus mine
  aimo-0030), not another reformulation. The corpus analog (aimo-0030 minimal-counterexample value-descent) was
  the decisive import.
- ALWAYS: keep rival approaches far apart in framing/route, not one idea tried many ways (CLAUDE.md, round 1).
- ALWAYS: each slug is a complete end-to-end attempt at the actual claim, never a proof split across slugs (CLAUDE.md, round 1).
- ALWAYS: read results/<id>/current.md, live approaches, knowledge_base.md before attempting (CLAUDE.md, round 1).
- REUSE: the scaffold (enumeration reduction + periodic-set endgame + gap bound) is CERTIFIED — builders import
  lemmas/enumeration-of-E-infinity.md and lemmas/periodic-set-enumeration.md, do NOT re-prove them (round 1).
- NEVER: field only E_∞-reduction variations — 3 of 4 approaches collapsed to ONE shared crux. Next round MUST
  field ≥1 genuinely different framing attacking large-prime elimination directly, e.g. an extremal/minimality
  argument on a hypothetical two-term pair whose only common prime is large (because a shared-gap plateau kills
  the whole field together, round 1).
- FALSE claims to avoid: R⊆primes(a_1)∪{2,3} is FALSE (a_1=99); pure density argument cannot close the crux (round 1).
- NEVER: try to close the crux via purely combinatorial covering/Helly/sunflower arguments — PROVEN DEAD by
  Prop D barrier (round 2): the crux is FALSE at the abstract covering-set level, so any proof MUST use the
  greedy DYNAMICS (window-minimality), not just the color set-system.
- NEVER: try to close the crux via global capacity/density counting (Σ1/p²) alone — PROVEN INSUFFICIENT
  (large-prime-capacity-counting RETHINK, round 2): capacity bounds only a positive fraction of pairs (~0.2X²),
  never zero, and reaching Ω(X²) sole-connector pairs requires E_∞ periodicity = circular. Counting lemmas
  C1/C2/C3 are cached and reusable, but not as the closing route.
- REUSE (round 2): import lemmas/sole-connector-off-lattice.md (sole-connector term is off the a_1-lattice,
  squeezed into a length-<a_1 window) and lemmas/term-density-and-prime-capacity.md — both CERTIFIED, do not re-prove.
- ALWAYS: the live crux now = the reverse termwise inequality / window-minimality step. The a_1-lattice squeeze
  (Prop C) + greedy window-minimality is the promising surviving surface — push builders there, NOT combinatorics.
- REUSE (round 4): import the 4 newly-certified lemmas — generalized-sole-connector-off-lattice.md (GPC, use
  INSTEAD of the singleton sole-connector), csp-implies-theorem.md (order-free CSP⇒theorem, skip the (SL) step),
  realizability-and-self-dual-clutter.md, bad-partner-and-ascent.md. Do NOT re-prove them.
- ALWAYS (round 4): the crux is now the value-ascent form — "no INFINITE ascending chain of large-prime-linked
  off-lattice bad terms." It splits into (6a) UNBOUNDEDNESS and (6b) CONTRADICTION. Step-5 ascent is symmetric on
  a mutual bad pair, so it gives only ONE step, NOT a chain — round 5's outliner MUST target (6a) with a
  NON-SYMMETRIC upward mechanism (break the m0↔witness symmetry), not assume the chain exists.
- NEVER: field self-dual-clutter-grading as a live SOLVE route — RETHINK/dead-end (round 4): its grading lever
  provably collapses to the descent Step 6→7 (same wall). Its lemmas (realizability, self-dual clutter) are
  cached and reusable, but the framing is not a distinct route. Send back to outliner only if reframed far.
- REUSE (round 5): import the 3 newly-certified lemmas — bad-signature-geometric-family.md (Lemma 6, the (6a)
  closer: bad m ⇒ m·r^k bad, same signature/witness), finite-witness-periodicity.md ((FIN-W)⟹theorem, the
  weakened crux target), minimal-linking-prime-and-window-cap.md (q* floor + per-window spacing cap). Do NOT
  re-prove them.
- ALWAYS (round 5): sub-gap (6a) UNBOUNDEDNESS is CLOSED (Lemma 6 gives an unbounded bad family for free) — the
  SOLE remaining crux is the single certified-equivalent wall with 3 phrasings: (6b) a value-level contradiction
  from an infinite off-lattice bad family / (FIN-W) infinite-witness "star" (a hub term small-disjoint from an
  infinite off-lattice family all divisible by one fixed large prime in one class mod L_0) / (DESC) the bad-window-
  index set has no minimum. Next round MUST target THIS wall; do NOT re-attack (6a) — it is done.
- NEVER (round 5): rely on the aimo-0016 "infinitely-often ⇒ always" downward-induction template for this problem
  — PROVEN not to transplant (bad family is a sparse multiplicative orbit m·r^k, no per-term-index local
  recurrence). Don't have a builder route through it.
- ALWAYS (round 5→6): the field has re-collapsed to ONE wall for the 2nd time — per CLAUDE.md shared-gap rule,
  round 6's outliner MUST put ≥1 approach on the GREEDY DYNAMICS of how a_{n+1} is actually chosen (smallest
  integer > a_n compatible with all predecessors), NOT another static E_∞/covering-set/value framing. The static
  reductions are exhausted as CLOSING routes; the contradiction (6b) provably needs the greedy value (Prop D).
- REUSE (round 7): import the 4 newly-certified lemmas — window-purity.md (every integer between consecutive
  terms is non-covering), finite-connector-pool-periodicity.md ((FIN-Q)⟹theorem, the NEW weakened crux target),
  local-hub-cover.md (h's large primes cover W(h), LOCAL capacity), minimal-bad-term-floor-tightness.md (Lemma X,
  m_0 floor-tight). Do NOT re-prove them.
- ALWAYS (round 7): the crux is now WEAKENED to ¬(FIN-Q): refute an inhabited bad class with infinitely many
  DISTINCT large connector primes q_k→∞ (NOT the old single-fixed-prime star — that phrasing is superseded).
  Crisp equivalent checkable target (from covering-small-part-descent): "no minimal covering set containing a
  large prime has minimal realization ≥ a_1." Both live carriers block at THIS a_1-threshold value inequality.
- NEVER (round 7): field the direct (q*, window-index) constructive REWRITE/exchange operator (lex-rewrite-descent
  RETHINK/DEAD) — lowering the linking prime below q* is verbatim the negation of Lemma A minimality (equivalent-
  strength, circular), and covering-preserving exchange is Prop-D-blocked. aimo-0009 shift-overshoot has no
  inequality analogue here. Lemma X salvaged & cached; the framing is dead as a solve route.
- NEVER (round 7): charging/injection arguments (aimo-0558/0718/0099 style) against the Lemma-6 geometric orbit
  m·r^k — its prime set is CONSTANT in k, no growing resource to charge (explorer-verified negative).
- WATCH (round 7): shared-gap has re-collapsed to ONE value threshold ("min realization of a large-prime-containing
  minimal covering set is < a_1"?) for the 3rd time. If it stalls again, per CLAUDE.md do NOT add a 4th FIN-Q/FIN-W
  variant — the outliner MUST attack that inequality with a genuinely new mechanism (e.g. reduced-process-identity's
  RED_n termwise route, still parked at top Elo and never advanced past round 4, may be the fresh angle).
- REUSE (round 9): import the 4 newly-certified lemmas — csp-iff-E-small-only.md ((CSP)⟺ℰ-small-only),
  essential-connector-equivalence.md (EC divisibility face + propagation preserving q), intersecting-clutter-
  and-spawning.md (Lemma 12 spawning), distinctness-by-difference.md (large prime q>window divides ≤1 term in a
  value window). Do NOT re-prove them.
- NEVER (round 9): field minimal-cover-small-only (pure transversal ℰ-small-only monovariant) as a live solve
  route — RETHINK/DEAD: its target IS literally (CSP) (Lemma D) and its only lever is HORIZONTAL (partner map,
  no downward well-founded monovariant; primes unbounded upward). Lemmas A/B/C/D salvaged & cached; framing dead.
- NEVER (round 9): field bounded-window-distinctness (distinctness-by-difference as the CLOSER) as a live route —
  RETHINK/DEAD: (R2′) proves confining the ¬(FIN-Q) new-prime pool to a bounded value-band [a_1,V) is EQUIVALENT
  to Q(r_0) finite = ¬¬(FIN-Q), so the closer is vacuous. The Distinctness-by-Difference local lemma is cached &
  reusable, but not as the closing route.
- ALWAYS (round 9): the wall is now CERTIFIED-EQUIVALENT across four faces — (CSP) = ℰ-small-only = (EC essential-
  connector divisibility) = ¬(FIN-Q). This is the 4th+ collapse. Per CLAUDE.md shared-gap rule, round 10's outliner
  MUST field ≥1 approach from a genuinely DIFFERENT framing — NOT another CSP/ℰ/EC/FIN-Q reformulation (all four are
  now certified-equivalent and EXHAUSTED as reformulations). The missing ingredient is a VALUE/DYNAMICS lower-
  pressure inequality tying a_1 to the covering structure via the GREEDY SUCCESSOR CHOICE (how a_{n+1} is picked =
  smallest integer > a_n compatible with all predecessors). The outline-reviewer's round-8 suggestion: a growth-
  RATE / recruitment argument — "each new distinct connector q_k must appear as a factor of some term within a
  bounded window, costing one slot per a_1-length window" — is a not-yet-tried framing distinct from all prior
  mechanisms. Do NOT unpark reduced-process-identity as a fresh attack (its explorer confirmed RED_n is only a
  REPACKAGING of the same Case-I(value)/Case-II(star) disjunction).
- WATCH: the target is REDUNDANCY, not smoothness — "a_{n+1} is P_max-smooth" is FALSE (a_1=231→237=3·79 is a
  good term with large prime 79 yet S(237)={3} covering). Never have a builder aim at smoothness of the witness.

## State
Done:
- Round 1: env set up (numpy/scipy/sympy); workspace results/imo-2026-06/ created; 4 approaches opened, 3 built.
  Problem fully reduced to one finiteness crux; endgame + reduction certified as reusable lemmas. Status: partial.
- Round 2: 3 explorers (extremal-minimality, recruitment-mechanism, covering-anchor) scouted crux off-E_∞.
  Outliner opened 3 far-apart new framings; all built + reviewed. Crux narrowed to a DYNAMICS/minimality step;
  2 non-dynamical routes ELIMINATED (Prop D barrier kills pure combinatorics; capacity counting proven
  insufficient). 4 new certified items (2 cached lemmas: sole-connector-off-lattice, term-density-and-prime-
  capacity; E* exact periodicity mod L_0; reduction to single inclusion (SL)). Status: still partial.
- Round 3: interrupted after outliner (explorers + outliner only, no build/review). Field carried into round 4.
- Round 4: completed round-3's flow. outline-reviewer approved 4 / built 3; proof-builders ×3
  (covering-small-part-descent NEW, reduced-process-identity advance, self-dual-clutter-grading NEW);
  proof-reviewer 2 CHANGES REQUESTED + 1 RETHINK. GPC closed the round-2 (SL)⟸ multi-large-prime gap; crux
  recast in value-ascent form with a PROVEN ascent engine (Step 5). 4 lemmas certified. Gap now (6a)+(6b).
  Status: partial.
- Round 3: interrupted after outliner (explorers + outliner only, no build). Field carried to round 4.
- Round 4: completed the round-3 flow — reviewed the outliner field, built 3 approaches, reviewed. GPC closed
  the round-2 (SL)⟸ gap; crux recast in new value-ascent form with a proven ascent engine; 4 lemmas certified.
- Round 5: 3 explorers (nonsym-ascent, local-contradiction, greedy-dynamics); outliner opened 2 NEW far-apart
  framings (bad-residue-witness-index, minimal-linking-prime-extremal) + advanced covering-small-part-descent;
  outline-reviewer approved+ranked+built 3; proof-builders ×3; proof-reviewer 3× CHANGES REQUESTED/partial.
  Sub-gap (6a) CLOSED (Lemma 6 certified). 3 lemmas certified. Crux re-collapsed to one wall. Status: partial.
- Round 6: NEVER EXECUTED (empty /tmp/round-6, ranking last_round=5). Round 7 picked up the round-6 plan.
- Round 7: 3 explorers (greedy-dynamics, star-config, foreign-technique); outliner opened 2 NEW far-apart framings
  (window-purity-class-cycle greedy-dynamics, lex-rewrite-descent foreign) + advanced covering-small-part-descent
  & bad-residue-witness-index; outline-reviewer built 3 (bad-residue-witness-index kept live/not built — converged
  onto window-purity framing); proof-builders ×3; proof-reviewer 2 CHANGES REQUESTED/partial + 1 RETHINK/dead-end.
  Crux STRICTLY WEAKENED FIN-W→FIN-Q. 4 lemmas certified. lex-rewrite route pruned dead. Status: partial.
- Round 8: INTERRUPTED — ran 3 explorers (red-n, value-inequality, foreign) → outliner → outline-reviewer only;
  no build/review. Build set (minimal-cover-small-only, covering-small-part-descent, bounded-window-distinctness)
  carried into round 9.
- Round 9: completed the round-8 flow. Built the 3-slug build set; proof-reviewer 1 CHANGES REQUESTED/partial
  (covering-small-part-descent) + 2 RETHINK/dead-end (minimal-cover-small-only, bounded-window-distinctness).
  4 lemmas certified (csp-iff-E-small-only, essential-connector-equivalence, intersecting-clutter-and-spawning,
  distinctness-by-difference). Two lanes self-certified their distinctive lever cannot close the wall. Status: partial.
- Round 10: ***SOLVED.*** 3 explorers (recruitment-counting, greedy-dynamics, foreign) → outliner fielded 3 lanes
  (2 NEW: smallest-essential-prime-descent [aimo-0030 game transplant], greedy-successor-jump-monovariant
  [aimo-0678]; +covering-small-part-descent advance) → outline-reviewer built {smallest-essential-prime-descent,
  covering-small-part-descent}, RETHINK'd greedy-jump (circular). proof-builders ×2; proof-reviewer APPROVE
  smallest-essential-prime-descent = COMPLETE SOLVE (independently re-derived + numerically verified) +
  CHANGES-REQUESTED covering-small-part-descent (Lemma 15 certified, self-diagnosed stall, moot). 2 lemmas
  certified. Status: SOLVED. GOAL ACHIEVED.
Broken:
- NONE — problem SOLVED (round 10). Full rigorous proof in results/imo-2026-06/current.md, reviewer-APPROVED.
--- superseded round-9 (the wall that was finally BYPASSED, not broken) ---
- Crux was open through round 9. The wall was CERTIFIED-EQUIVALENT across FOUR faces —
  (CSP) = ℰ-small-only = (EC essential-connector divisibility) = ¬(FIN-Q) — and reformulations are EXHAUSTED.
  4th+ collapse to one wall; 2 of 3 round-9 lanes (transversal monovariant; value-difference confinement)
  SELF-CERTIFIED their distinctive lever provably cannot close it (horizontal partner map; (R2′) vacuity).
  Sole live carrier: covering-small-part-descent (now in EC form) — (EC) propagation preserves q, no downward
  monovariant. Missing ingredient (unchanged in kind): a VALUE/DYNAMICS lower-pressure inequality tying a_1 to
  the covering structure via the GREEDY SUCCESSOR CHOICE. Dead for this wall: static covering/Helly (Prop D),
  global Σ1/p², aimo-0016, symmetric ascent, direct (q*,k) rewrite, transversal ℰ-small-only monovariant,
  distinctness-by-difference confinement. Next framing must be a genuinely new mechanism, not a 5th reformulation.
--- superseded round-7 ---
- Crux STILL open (no solve flip). Sub-gap (6a) CLOSED (round 5). Crux now WEAKENED to ¬(FIN-Q) (round 7): an
  inhabited bad class with infinitely many DISTINCT large connector primes q_k→∞ (supersedes the single-fixed-
  prime star). Both live carriers (covering-small-part-descent, window-purity-class-cycle) block at ONE crisp value
  inequality: "no minimal covering set containing a large prime has minimal realization ≥ a_1." q* is only a floor
  (refined star ascends q_k→∞, no monotone descent); the a_1 threshold in Realizability clause (c) is where every
  descent stalls (Prop D admits large minimal members). Dead for this wall: static covering/Helly, global Σ1/p²,
  aimo-0016, symmetric ascent, direct (q*,k) rewrite operator, charging vs the m·r^k orbit.
--- superseded ---
- (round 5) Crux STILL open (no solve flip), but sub-gap (6a) UNBOUNDEDNESS is now CLOSED (Lemma 6: bad m ⇒ m·r^k bad,
  same signature/witness — an unbounded bad family for free). The SOLE remaining wall is ONE certified-equivalent
  statement, 3 phrasings: (6b) a value-level CONTRADICTION from an infinite off-lattice bad family / (FIN-W)
  infinite-witness "star" branch (a hub term small-disjoint from an infinite off-lattice family all divisible by
  one fixed large prime q>P_max in one residue class mod L_0) / (DESC) the bad-window-index set has no minimum.
  The field has re-collapsed to this ONE wall for the 2nd time. Global Σ1/p² capacity and pure covering (Prop D)
  both PROVEN DEAD for it; Prop D says the contradiction MUST use greedy value.
Next:
- NONE — run complete. imo-2026-06 SOLVED (round 10). If continued, only optional polishing of the write-up in
  results/imo-2026-06/approaches/smallest-essential-prime-descent.md; no mathematical work remains.
--- superseded round-10 plan (executed and SUCCEEDED) ---
- Round 10: 4th+ collapse to ONE certified-equivalent wall ((CSP)=ℰ-small-only=(EC)=¬(FIN-Q)); reformulations are
  EXHAUSTED. Per CLAUDE.md shared-gap rule, round-10's outliner MUST field ≥1 approach from a genuinely DIFFERENT
  framing that attacks the value/dynamics lower-pressure inequality via the GREEDY SUCCESSOR CHOICE — NOT a 5th
  CSP/ℰ/EC/FIN-Q reformulation. STRONG candidate (outline-reviewer round-8): a growth-RATE / recruitment counting
  argument — "each new distinct connector prime q_k must appear as a factor of some term within a bounded (a_1-
  length) window, costing one slot per window" — genuinely new, not tried. Advance the sole live carrier
  covering-small-part-descent (EC form) only if a NEW descent variable / reframe is found — (EC) propagation
  preserves q with no monovariant, so a bare re-advance will stall. Import the 4 new certified lemmas. Do NOT
  re-field minimal-cover-small-only or bounded-window-distinctness (both dead), lex-rewrite (dead), or unpark
  reduced-process-identity as fresh (RED_n is only a repackaging of the same disjunction).
--- superseded round-8 plan (executed in round 9) ---
- Round 8: attack the ONE crisp value inequality "no minimal covering set containing a large prime has minimal
  realization ≥ a_1" (equiv. ¬(FIN-Q): no bad class with infinitely many distinct large connectors q_k→∞). This is
  the 3rd collapse to one wall — do NOT add a 4th FIN-Q/FIN-W/star reformulation. Advance covering-small-part-descent
  (its Lemma 9 minimal-bad-term descent is the closest handle — it needs to beat the a_1 threshold in Realizability
  clause (c)) and window-purity-class-cycle (class-graph descent, but q*-floor cannot force monotone descent — needs
  a genuinely new descent variable). STRONG candidate for the fresh angle: UNPARK reduced-process-identity (Elo top
  1628, never advanced since round 4) — its RED_n termwise reverse-inequality route directly targets the successor
  value and has NOT been tried against the now-weakened FIN-Q crux; the greedy-dynamics window-purity toolkit + Lemma
  X floor-tightness may finally crack RED_n. Import the 4 new certified lemmas. Do NOT re-field lex-rewrite (dead).
--- superseded round-6 plan (round 6 never ran; folded into round 7) ---
- Round 6: per CLAUDE.md shared-gap rule (2nd collapse to one wall), outliner MUST field ≥1 approach attacking the
  GREEDY DYNAMICS of how a_{n+1} is chosen (smallest integer > a_n compatible with all predecessors) — a genuinely
  new framing FAR from the static E_∞/covering/value reductions, which are now exhausted as CLOSING routes. Target
  the single wall in whichever phrasing the new framing prefers: kill the infinite-witness "star" (a hub term
  small-disjoint from an infinite off-lattice q-divisible family in one class mod L_0) using the greedy minimality,
  NOT static combinatorics or global density. Advance covering-small-part-descent ((6b) only now, since (6a) done)
  and bad-residue-witness-index (star branch of FIN-W). Import the 3 new certified lemmas (bad-signature-geometric-
  family, finite-witness-periodicity, minimal-linking-prime-and-window-cap). Keep reduced-process-identity (Elo
  top) and enum-covering-primes parked to import the crux proof once it lands. Do NOT re-attack (6a) — it is done;
  do NOT route through aimo-0016 (proven not to transplant).
