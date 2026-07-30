# Outline review — imo-2026-06 (round 2)

Context: the whole problem is certified-reduced (round 1) to ONE crux, phrased equivalently as
Lemma A / Structural Lemma / R ⊆ {primes ≤ P_max} / small-covering restatement. All four round-1
approaches shared this wall. The outliner opened three deliberately far-apart NEW framings that each
attack the crux directly, plus keeping the reduction spine `enum-covering-primes` live. I independently
re-verified the load-bearing new target (the reduced-process coincidence) below.

## Independent check performed
Ran the true greedy vs the "small-primes-only" (primes ≤ P_max) greedy for
a_1 ∈ {15,35,77,97,99,105,143,182,1155,2431}, 120 terms each: **exact termwise MATCH on every seed.**
So `reduced-process-identity`'s induction target (a_n = b_n ∀n) is a TRUE statement, and the "easy"
direction b_{n+1} ≥ a_{n+1} (from E* ⊆ E_∞) is sound. The framing builds toward a real theorem, not a
false conjecture. Good.

---

## enum-covering-primes — APPROVE (advance), but NOT built this round
The certified reduction + endgame spine (Steps 1–4, R1/R2 reviewer-certified). Sound; it is the
standing partial and the import target for whichever crux framing lands. Per the build-set rule, it is
built only when there is fresh crux work to WIRE IN. The three crux framings are only being *built* this
round; none has closed yet, so there is nothing new to import. Leave it live to import next round.
No changes.

## reduced-process-identity — APPROVE (new), register + build
Technique: strong induction proving true sequence = small-primes-only sequence termwise; reduced
sequence is manifestly finite-state periodic mod L_0 = ∏_{p≤P_max} p (CRT / covering system — solid).
- Skeleton is valid: Step 2 (E* periodic mod L_0) and Step 3 (periodic-set certified lemma ⇒
  b_{n+T}=b_n+L_0) follow; Step 5 is immediate once a_n=b_n.
- The gap is honestly flagged and correctly localized: Step 4 reverse inequality a_{n+1} ≥ b_{n+1}
  ("a_{n+1} shares a prime ≤ P_max with EVERY predecessor"), equivalent to the crux but re-packaged as
  "the two sequences never diverge, even once." The IH leverage (a_1..a_n pairwise small-intersecting
  AND a_{n+1} minimal in window (a_n,a_n+a_1]) is genuinely stronger than bare Lemma A.
- Circular-trap check: PASSES. The file explicitly forbids assuming periodicity of E_∞ (the conclusion)
  and forbids generic CRT window counting (correctly noted to fail: window a_1 can be below the CRT
  product). Does not use the circular cofactor-peel.
- Builder instruction: exploit the pairwise-small-intersecting IH, not generic counting. If the
  minimality-of-window argument cannot close, record precisely where it breaks.
Strongest new framing (cleanest target, verified true, best leverage).

## cofactor-recruitment-smoothness — APPROVE (new), register + build
Technique: dynamic recruitment monovariant — track R_i, show a new prime enters only via the
P_max-smooth cofactor of a greedily-minimal witness term. Distinct surface (analyses the factorization
of the term that TRIGGERS recruitment; concrete traced instance a_1=99, 110=11·10, cofactor 10=2·5).
- Steps 1–3 import certified R1 machinery and the certified "every multiple of a_1 is a term / gaps ≤ a_1"
  — solid. Step 3's "new minimal member ⇒ small part non-covering on prefix" is importable from R1.
- Circular-trap check: PASSES, and notably well. The file NAMES the circular cofactor-peel trap
  (explorer-1 opening 3: "peeled cofactor v is compatible with all earlier" is a corollary of the crux)
  and explicitly forbids using it as a hypothesis — it restricts to the non-circular content (WHY the
  minimal window-choice is smooth, from minimality + the a_1·ℤ lattice). This is exactly the discipline
  the trap requires.
- Gap honestly flagged: Step 4 cofactor-smoothness bound on the smallest compatible integer in a
  length-a_1 window (candidate tool Bertrand / smooth density), NOT a size bound. This is the real,
  unclosed difficulty — acceptable as a live population member.
- Far enough from reduced-process-identity: both use window-minimality, but attack different objects
  (sequence coincidence vs. R_i cofactor monovariant). Keep both.

## large-prime-capacity-counting — APPROVE (new), register + build
Technique: global prime-capacity double-counting (aimo-0447 analogue). Assume R infinite; a prime p is
the shared prime of ≤ C(⌊X/p⌋,2) pairs; Σ_{p>P_max} 1/p² tail is small ⇒ large-prime-only pairs are a
vanishing fraction. Steps 1–3 are elementary/certified and sound.
- Genuinely different top-level target (global density contradiction vs. local witness elimination) —
  the diversity the shared-gap Rule demands.
- Gap honestly flagged: Step 4 localize-to-globalize. The file is candid that Lemma A forbids even ONE
  witness while counting only bounds a FRACTION, so the localize step is mandatory, not cosmetic, and
  the honest risk is that a single witness pair with enormous members contributes nothing to density
  among terms ≤ X. It correctly forbids asserting periodicity of E_∞ to manufacture density (that would
  be circular).
- Weakest of the three (the localize gap may prove un-closable), but it is a legitimate exploratory
  test of whether capacity + the a_1·ℤ lattice can replace the local argument — worth one build cycle.
  Builder should first attempt the direct count of "minimal members with a large prime below X" against
  capacity, and if the localize step cannot be made non-circular, record exactly where.

## difference-sequence-squeeze — not nominated, correctly left in pool
Never expanded, stalled on an unmanufactured divisibility (raw gap-sequence R2), lacks the certified
scaffold, dominated by the three new surfaces. Left un-built. Revisit only if all three new framings
stall on the identical minimality/localize step.

---

## Diversity assessment
The field is now well-spread: a reduction spine (enum-covering-primes) plus three far-apart crux
attacks — a static process-coincidence induction (reduced-process-identity), a dynamic
recruitment/cofactor monovariant (cofactor-recruitment-smoothness), and a global capacity count
(large-prime-capacity-counting). They do NOT share a single gap: process-identity's gap is a termwise
reverse inequality, cofactor's is a smooth-number window bound, capacity's is a localize-to-globalize
density step. This directly answers round 1's shared-wall warning. If all three still stall on the same
underlying "minimality/localize" obstruction next round, that is the signal to seed a fourth,
even-more-distant framing (or revisit difference-sequence-squeeze).

## Ranking after update (Elo)
enum-covering-primes 1568 · reduced-process-identity 1550 · density-bounded-recruitment 1525 ·
cofactor-recruitment-smoothness 1503 · finite-state-window 1482 · large-prime-capacity-counting 1473 ·
difference-sequence-squeeze 1399.

## Build set rationale
Build the three new far-apart crux framings in parallel (one builder each, separate files, no collision).
Exclude enum-covering-primes this round — no fresh crux proof exists yet to import; it stays the standing
partial and wires in a crux next round if one lands.

build set: reduced-process-identity, cofactor-recruitment-smoothness, large-prime-capacity-counting
