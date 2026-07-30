# Proof review — imo-2026-06 (IMO 2026 P6), round 1

Problem: a_1,a_2,... integers >1; a_{n+1} = smallest integer > a_n with gcd(a_{n+1},a_i)>1
for all i≤n. Prove ∃ positive integers T,L with a_{n+T}=a_n+L for every n.

All three builders correctly marked their files **partial** (no overclaim). Each is a genuine
rigorous reduction of the whole problem to a single finiteness crux, with the endgame proved.
I re-derived the load-bearing shared steps independently and verified them computationally.

## Independent verification (Bash/python3)
- Enumeration reduction (sequence = increasing enumeration of E_∞ ∩ [a_1,∞)): re-derived from
  scratch — correct. E_∞ ⊆ E_n gives "nothing of E_∞ strictly between consecutive terms," and
  each a_{n+1} ∈ E_∞; induction from a_1 gives equality. Airtight.
- Periodic-set ⇒ recurrence for EVERY n: re-derived via the shift bijection φ:x↦x+L. Airtight.
- Eventual-linear recurrence a_{n+T}=a_n+L confirmed numerically: a_1=15 ⇒ (T,L)=(8,30);
  a_1∈{6,10} ⇒ (1,2). The density file's larger (8008,30030) for a_1=15 is a valid non-minimal
  period — acceptable, problem asks only for existence.
- The three cruxes (Structural Lemma; Lemma A; G1') all hold with ZERO counterexamples across
  a_1 ∈ {15,35,99,33,55,...} on 120+ terms each — confirming they are TRUE but, as each file
  honestly states, UNPROVEN.

## enum-covering-primes — Status: partial. Verdict: CHANGES REQUESTED.
Scores: Correctness 5/5 (everything written is valid), Rigor 4/5 (one honest gap), Progress 5/5.
- Steps 1–4 (reduction + periodicity endgame + "for every n") fully proved and correct.
- R1 (exact characterization q∈R ⟺ some pair has prime-intersection {q}) is proved in both
  directions; the auxiliary equivalence (★) is correct. R2 uses only the needed direction
  (Lemma A ⇒ R ⊆ {primes ≤ P_max} finite), which is rigorous. The header phrase "R finite ⟺
  Lemma A" is loosely stated but the text uses only the sound direction — not a defect.
- GAP: **Lemma A** (no prime q>P_max is the unique common prime of two terms) is verified, not
  proved. This is the sole gap. Correctly labeled.

## density-bounded-recruitment — Status: partial. Verdict: CHANGES REQUESTED.
Scores: Correctness 5/5, Rigor 4/5, Progress 5/5.
- Steps 1–5 (including periodicity of E_∞ = {m: π(m) hits every color} mod L=∏R, and the
  conclusion for every n) fully proved and correct. (5b) smooth-term realization and (5c)
  E_∞=G are both airtight.
- Valuable recorded dead end is CORRECT and important: "only finitely many primes divide
  infinitely many terms" is false because E_∞ periodic ⇒ every prime meets it in positive
  density (I confirmed each of 2..73 divides terms for a_1=15). So pure asymptotic density
  cannot isolate load-bearing primes — the crux must be the per-pair magnitude statement.
- GAP: **Structural Lemma** (every two terms share a prime ≤ a_1) verified, not proved. Sole gap.

## finite-state-window — Status: partial. Verdict: CHANGES REQUESTED.
Scores: Correctness 5/5, Rigor 4/5, Progress 5/5.
- Lemmas 1–6 all fully proved and correct. Lemma 6 (finite sufficient R ⇒ tail-periodicity
  L=∏R ⇒ conclusion for every n) closes the forward-propagation/determinism concern rigorously.
  The "automatic direction" E_R(x) ⇒ x∈E_∞ and upward monotonicity of sufficiency are correct.
- Correctly disproves the earlier guess R ⊆ P∪{2,3} (a_1=99 recruits 5 — I confirmed 5 appears).
- GAP: **G1'** (R₀={primes ≤ maxfactor(a_1)} is sufficient) verified, not proved. The "mechanism"
  in §Mechanism is explicitly heuristic and NOT counted as proof — honest. Sole gap.

## Cross-cutting assessment
The three cruxes are three equivalent phrasings of ONE fact: **no prime larger than the largest
prime factor of a_1 is ever load-bearing.** This is the genuine difficulty of P6. None of the
three closes it; all three prove the entire scaffolding around it and verify it numerically.
None overclaims. This is a shared wall — next round the outliner should field ≥1 approach from a
different framing that attacks large-prime elimination head-on (extremal/minimality argument on a
hypothetical disjoint-color / unique-large-connector pair), rather than a fourth E_∞ variation.

## Lemmas certified for reuse (pass the full bar, sorry-free, statements no stronger than proved)
- lemmas/enumeration-of-E-infinity.md — sequence = increasing enumeration of E_∞ ∩ [a_1,∞).
- lemmas/periodic-set-enumeration.md — E tail-periodic from a ⇒ b_{n+T}=b_n+L for every n.
Bounded-gap (a_{n+1}-a_n ≤ a_1) and pairwise-non-coprimality are also fully proved and available
in all three files; folded into the reduction rather than cached separately.

## current.md
Updated to Status partial with the field summary and the single shared crux.
