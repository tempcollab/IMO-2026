# Build report — enum-covering-primes (imo-2026-06), round 1

## Status: partial (advanced; single sharp gap remains)

## What was closed (full rigor, no gaps)
- **Steps 1–4** written out completely, including the **enumeration-of-a-periodic-set lemma** with full proof (gives a_{n+T}=a_n+L for *every* n from n=1, T = #residues mod L in E_∞, L = ∏R).
- **Two-way reduction "R finite ⟺ Lemma A"**, resting on the new **exact identity**
  R = { q : ∃ terms a_i,a_j with primes(a_i)∩primes(a_j) = {q} }  (proved both directions, R1),
  and R2: primes ≤ P_max are finite, so R finite ⟺ no prime q>P_max is a "unique connector" ⟺ Lemma A. Verified numerically that R(min-edges) = R(unique-pair) on 8 seeds.

## The remaining gap (sharpened, not closed)
- **Lemma A:** for no prime q > P_max do two terms share prime-intersection exactly {q}.
  This is now the sole gap and is a crisp, elementary, self-contained statement — a strict improvement over the outline's vague "replacement/syndeticity mechanism." Verified (0 violations) on a_1 ∈ {15,35,77,105,143,255,182,6,30}.
- Established: any such pair forces A=q^α u, B=q^β v with distinct P-primes p|u, p′|v (coprime cofactors). Showed a purely *local* "smaller compatible number in (a_{j-1},a_j)" argument cannot work (that interval is empty by definition of the greedy min), so Lemma A needs a non-local/extremal argument — not completed.

## Guidance for next round
- Attack Lemma A directly: it is equivalent to "the terms divisible by a fixed prime q>P_max pairwise share a small prime." Extremal choice (minimal larger term B of a bad pair) + the cofactor structure (every q-term = q·(P-multiple)) is the promising line; the density approach (density drops per new term are NOT bounded below — checked — so a soft density/counting bound on the number of new terms fails). 
- The reduction to Lemma A is import-ready for density-bounded-recruitment (it can now aim its analytic argument at exactly "no unique-connector prime q>P_max" instead of the fuzzier "persistent primes finite").

## Promotable lemmas (for reviewer to certify)
1. Enumeration-of-a-periodic-set lemma (Step 4) — full proof.
2. Greedy sequence = increasing enumeration of E_∞ ∩ [a_1,∞) (Steps 1–2).
3. Covering characterization + exact identity R = {q : unique-connector pair} (Step 3 + R1).

## Spec concerns
None. Problem is proof_only / answer_type none; no final answer to verify.
