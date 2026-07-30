# Proof-reviewer — Round 2 (imo-2026-06)

Reviewed three built approaches. None claims `solved`; all are honest partials. I re-derived
the load-bearing new sub-lemmas independently and numerically checked the constants and the
crux equivalences. No approach closes the standing crux (no large prime is load-bearing);
all three still share that one wall. Overall problem Status: **partial** (unchanged headline,
real byproduct progress).

Verified independently (python/sympy): P(2) − 1/4 = 0.20225 (Lemma C3 constant); across
a_1 ∈ {15,35,77,99,105,143,182,231,1155,2431}, first 120 terms, (SL) holds, Lemma A holds,
and NO pair shares only large primes ("large-only" = 0) — so empirically (SL) and Lemma A
coincide, but this is not proved (see approach-1 note).

---

## reduced-process-identity — Status: partial — Verdict: CHANGES REQUESTED

Recorded Status `partial` is CORRECT (no overclaim).

Imports used validly: enumeration-of-E-infinity and periodic-set-enumeration are invoked with
their hypotheses met (E* nonempty, periodic mod L_0, a = a_1).

Independently checked the NEW sub-results:
- (F1)–(F3), (P1)–(P4): all correct. E* ⊆ E_∞ (P1) and E* periodic mod L_0 = ∏_{p≤P_max}p (P2)
  are rigorous — membership depends only on D(m) = {p≤P_max : p|m}, a function of m mod L_0 by CRT,
  with finitely many distinct small-support constraints. a_1 ∈ E* and every multiple of a_1 ∈ E*
  (P3) correct.
- §3 reduction "E_∞∩[a_1,∞) ⊆ E* ⟹ theorem" is VALID: with P1 the inclusion forces set equality,
  hence a_n = b_n termwise, and (★) from the periodic lemma gives a_{n+T_0}=a_n+L_0. Explicit
  L = L_0, T = #(E*∩[a_1,a_1+L_0)) ≥ 1. Correct and gap-free.
- No smuggling of E_∞ periodicity: E* periodicity is derived from finiteness of small-support
  subsets, independent of the conclusion. Clean.

GAP (honest, correctly flagged): (SL) = E_∞∩[a_1,∞) ⊆ E*, i.e. every two terms share a prime
≤ P_max. This is the standing crux, unproven. §4/§5/§6 (base case, IH, G1–G4 sharpenings, G3
"minimality route blocked", G6 gap) are correct observations, not a proof.

MINOR IMPRECISION to fix (does not affect the partial verdict): the prose asserts "(SL) is
exactly Lemma A re-packaged / (SL) ⟺ Lemma A." Only (SL) ⟹ Lemma A is immediate; the reverse
(Lemma A ⟹ (SL)) is NOT established — two terms could a priori share a set {q1,q2} of large
primes, violating (SL) without giving a singleton sole-connector. Empirically they coincide, but
a future builder must not treat "prove Lemma A" as automatically discharging (SL). Flag, not fatal.

Promotable lemmas: BOTH certifiable and correct — E* periodicity (P1–P4) and reduction-to-inclusion
(§3). They largely repackage the certified enumeration+periodic endgame in small-support language;
correct and gap-free, so admissible. (Not separately cached — subsumed by the two existing certified
lemmas plus this framing's own file; no new independent reusable content beyond repackaging.)

Scores: Correctness 9/10 (one imprecise equivalence claim), Rigor 8/10 (crux is an honest gap),
Progress 6/10 (clean reduction, but same wall as round 1).

---

## cofactor-recruitment-smoothness — Status: partial — Verdict: CHANGES REQUESTED

Recorded Status `partial` is CORRECT.

Imports and (★)/recruitment bookkeeping (Steps 1–2) used validly; the reprove of R1's core is
consistent with the certified enum-covering-primes.

Independently checked the NEW results:
- **Prop C** (Step 4): "primes(A)∩primes(B) = {q}, q ∉ P ⟹ D ∤ A, D ∤ B." Re-derived from
  scratch: if D|A then P ⊆ primes(A); B shares some p ∈ P with a_1; p ∈ primes(A) and p|B force
  p ∈ {q}, so p = q ∉ P, contradiction. RIGOROUS. Genuinely new positive constraint (confines a
  large-prime witness off the a_1-lattice, into a length-<a_1 window). CERTIFIED →
  cached at lemmas/sole-connector-off-lattice.md.
- **Prop D** (Step 5): the construction G' = {{p1,q},{p2,q},{p1,p2}} is pairwise intersecting and
  has {p1,q} as a minimal covering set containing the large prime q — I verified: dropping p1 gives
  {q} which misses {p1,p2}; dropping q gives {p1} which misses {p2,q}; so {p1,q} is minimal covering.
  Correct AS a covering-axiom-insufficiency result: "intersecting + covering-closed" alone does not
  forbid a large minimal member. ACCEPTED as a barrier. CAVEAT: the stronger reading "therefore ANY
  proof must use greedy dynamics" is a heuristic/steering claim, not a theorem (it shows the covering
  axioms insufficient; it does not show G' is realizable by an actual greedy sequence). This is worth
  keeping as steering but I do NOT cache it as a formal reusable lemma — its strong phrasing overreaches.

No circularity: Gap G left open, and the doc correctly refuses the circular cofactor-peel
("peeled cofactor compatible with all earlier terms" is a corollary of Lemma A, not a hypothesis).

GAP (honest): Gap G — the connectivity-carrying cofactor of the greedy witness is P_max-smooth.
The standing crux, dynamical, unproven.

Scores: Correctness 9/10, Rigor 8/10 (Prop D's meta-claim slightly strong), Progress 7/10
(Prop C is a real new certified constraint; crux still open).

---

## large-prime-capacity-counting — Status: unsolved (as a solving route) — Verdict: RETHINK

Recorded Status `partial` is arguably generous: the approach PROVES its own framing cannot close
the crux. As a route to solving P6 it is a dead-end; hence RETHINK (back to the outliner), while
salvaging the certified counting lemmas.

Independently checked the NEW results:
- **Lemma C1**: ⌊X/a_1⌋−1 ≤ N(X) ≤ X. Correct (multiples of a_1 are terms; terms are distinct
  integers ≤ X).
- **Lemma C2**: pairs with p|gcd ≤ C(⌊X/p⌋,2) ≤ (X/p)²/2. Correct double counting.
- **Lemma C3**: L(X) ≤ (X²/2)·Σ_{p>P_max}1/p² < 0.21·X²/2. Tail bound Σ_{p>y}1/p² < 1/y
  (telescoping) correct; sharp constant P(2) − 1/4 < 0.2023 — I recomputed P(2) = 0.452247,
  P(2) − 1/4 = 0.20225. Correct. CERTIFIED (C1–C3) → cached at
  lemmas/term-density-and-prime-capacity.md.
- **Negative certification** (Step 4 / §5): rigorously correct. Capacity bounds only a positive
  FRACTION of pairs (Consequence: L/Π ≤ 0.21·a_1², never 0); and "R infinite" (imported R1) forces
  only o(X²) large-sole pairs; the only mechanism giving Ω(X²) is periodicity of E_∞, which is the
  CONCLUSION (circular). So the framing cannot close the crux. This is a valid, valuable pruning
  result — not overclaimed.

No smuggling: the circular escape is explicitly identified and refused.

Why RETHINK not CHANGES REQUESTED: there is no gap for the same builder to "close" — the approach
has demonstrated the gap is un-closable in this framing. Re-planning (a different framing) is the
correct route. The certified byproducts (C1–C3, the negative result) are retained.

Scores: Correctness 9/10, Rigor 9/10 (the negative certification is careful), Progress 4/10 as a
solution route (proven incapable), but high pruning value.

---

## Summary

| slug | Status | Verdict | new certified content |
|---|---|---|---|
| reduced-process-identity | partial | CHANGES REQUESTED | E* periodicity + reduction-to-inclusion (correct; repackaging) |
| cofactor-recruitment-smoothness | partial | CHANGES REQUESTED | Prop C (cached); Prop D barrier (accepted, not cached) |
| large-prime-capacity-counting | unsolved (route) | RETHINK | Lemmas C1–C3 + negative certification (cached) |

The field still shares ONE crux (no large prime load-bearing = Lemma A = (SL) = Gap G). Capacity
counting is now provably dead. The two live routes are the local/minimality framings, both bottoming
on the same greedy-minimality statement. Per run_state's steering rule, next round should still push
≥1 genuinely different framing at the crux; Prop C (witness off the a_1-lattice, length-<a_1 window)
and Prop D (dynamics are required) are the sharpest new levers to hand the outliner.

current.md updated (Status: partial; per-approach round-2 progress recorded).
Cached lemmas: lemmas/sole-connector-off-lattice.md, lemmas/term-density-and-prime-capacity.md.
