# Outline Review — Round 4 — imo-2026-06

Context: whole problem is certified-reduced to a single crux, phrased as **(CSP): no term
has a non-covering small part** S(m)=primes(m)∩[2,P_max]. Endgame (enumeration + periodicity),
Prop C, capacity lemmas C1–C3 are certified. DEAD routes (never field): pure covering/Helly/
sunflower (Prop D), global capacity/density (Σ1/p²), smaller-competitor window-minimality in
the empty window (a_n,a_{n+1}) (G3). I verified independently this round (python, 7 seeds
{15,35,77,99,231,1155,2431}): F1 holds (every term-pair shares a prime) and **zero bad terms**
on all seeds — so (CSP) is the correct true target, and the (SL)⟸(CSP) two-liner is valid
(a covering S(A) meets primes(B) in a small prime ⇒ shared small prime).

## covering-small-part-descent — APPROVE (new)
Best diversity bet; a genuinely new proven step and a gap off the dead window-minimality wall.
- I hand-checked the load-bearing new step (Step 5, smallest-bad-term ascent) and it is sound:
  m₀ bad ⇒ ∃ term B with primes(B)∩S(m₀)=∅ ⇒ any shared prime of m₀,B is large (a small shared
  prime would lie in S(m₀)); if S(B) were covering it would meet primes(m₀) in a small prime,
  contradiction ⇒ B bad. S(m₀)≠∅ always (m₀ shares a small prime with a_1, whose primes are all
  ≤P_max) ⇒ B≠m₀ ⇒ minimality forces B>m₀. Valid.
- Honest open gap correctly located at **Step 6→7**: an infinite strictly-ascending chain of bad
  terms is NOT itself a contradiction (there could be infinitely many). The contradiction must be
  produced (candidate levers (i) larger a_1-multiple good term within distance a_1 as an upper
  bound — a legitimate LARGER-competitor bound, not the dead smaller one; (ii) monovariant on the
  linking large prime q). This is the real work; flagged as GAP, no overclaim.
- To fix while building: do NOT let Step 6 reintroduce a smaller competitor (dead G3) — only
  larger known a_1-multiples as upper bounds, as the outliner already cautions.

## reduced-process-identity — APPROVE (advance, top live Elo)
- Certified §1–§4 kept; the multi-large-prime patch via **generalized Prop C** (if two terms share
  no small prime then a_1 divides neither — I checked the proof: a_1|A ⇒ P⊆primes(A), and B meets
  a_1 in a small p∈P⊆primes(A)∩primes(B), contradiction) correctly closes the reviewer's flagged
  (SL)⟺Lemma A ⟸ gap. This is a certifiable win independent of the crux.
- Reorientation to **redundancy** (not the FALSE "witness is P_max-smooth"; a_1=231 has term 237=3·79)
  is the right correction. Open gap = the direct-value inductive step (Step 3) = the shared crux in
  induction phrasing; honestly flagged, "smaller compatible competitor" explicitly forbidden. Good.
- Note: its gap is the same redundancy statement as cofactor's Gap G (see below).

## cofactor-recruitment-smoothness — APPROVE but NOT in build set (advance)
- Sound and correctly reoriented (Gap G restated as redundancy; generalized Prop C promoted;
  circular cofactor-peel explicitly forbidden). No fatal flaw.
- BUT its reoriented gap ("witness a_i with sole large partner a_j can't exist because S(a_i) would
  be non-covering while a_i is compatible with all") is essentially identical to
  reduced-process-identity's redundancy gap. Building both spends two builders on one wall, against
  the standing rule to keep the field diverse. Stays live/registered; not built this round.

## self-dual-clutter-grading — APPROVE (new, second far framing)
- Distinct framing (clutter/blocker duality + value-grading). It explicitly acknowledges Prop D
  (self-duality alone is insufficient; the a_1=15 self-dual triangle has no Helly centre) and adds
  the grading/value axiom, so it does NOT re-field the dead pure-covering route.
- RISK, flag for builder: Step 4 (the grading lever) is the crux and is currently vague. The outliner
  itself says "if Step 4 cannot use value, drop it." Build it as an exploration bet; if the argument
  cannot consume integer value/size it collapses to the dead covering level and should be recorded
  dead, not dressed up. Steps 1–3 (E self-dual, (CSP)⟺H_s covering-dense) are provable set-theory
  and worth cementing regardless.

## Field diversity
Restored and healthy: descent (value well-ordering / infinite ascent), self-dual-clutter-grading
(clutter grading), and the redundancy pair (reduced-process-identity / cofactor) span three
distinct framings. The redundancy pair shares one wall — hence only one of them (the top-Elo
reduced-process-identity) is built this round. All three built approaches promote/certify
generalized Prop C as a shared reusable lemma, a guaranteed byproduct independent of crux progress.
enum-covering-primes stays parked to import the crux proof once it lands.

## Ranking (post-update)
reduced-process-identity 1609 · enum-covering-primes 1597 · covering-small-part-descent 1577 ·
density-bounded-recruitment 1511 · self-dual-clutter-grading 1508 · cofactor-recruitment-smoothness
1492 · finite-state-window 1458 · large-prime-capacity-counting 1396 (dead) ·
difference-sequence-squeeze 1351.

build set: covering-small-part-descent, reduced-process-identity, self-dual-clutter-grading
