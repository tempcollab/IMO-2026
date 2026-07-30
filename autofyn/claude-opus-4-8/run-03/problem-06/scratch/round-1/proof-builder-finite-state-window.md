# Build report — finite-state-window (imo-2026-06), round 1

**Status: partial** (major advance from unsolved).

## What is now fully rigorous (Lemmas 1–6, all proved in-file)
1. All terms pairwise non-coprime ⇒ every term ∈ E_∞; every term shares a prime with a_1.
2. Bounded gaps a_{n+1} − a_n ≤ a_1.
3. Envelopes: a_1·ℤ ⊆ E_∞ ⊆ ⋃_{p∈P} pℤ.
4. Sequence = increasing enumeration of E_∞ ∩ [a_1,∞) — collapses the unbounded history to the static set E_∞.
5. **Enumeration Lemma**: tail-periodicity of E_∞ from a_1 (period L) ⇒ a_{n+T}=a_n+L for **every n** (not just eventually), T = #(E_∞ ∩ [a_1,a_1+L)). Fully proved via an order-preserving shift bijection. This is the machinery that yields the "for every n" strength the problem demands.
6. **Finite-State Reduction (closes G2)**: a *finite* sufficient prime set R ⇒ E_∞ is a union of residue classes mod L=∏R ⇒ tail-periodicity ⇒ conclusion. The finite "state" is x mod ∏R; the greedy next-term map is a deterministic function of that finite state. This dissolves the reviewer's G2 objection (unbounded-memory rule) — via Lemma 4 the whole history reduces to E_∞, and sufficiency makes E_∞ finite-state.

## The one remaining gap (G1, = the genuine crux of P6)
Existence of a finite sufficient R. Reduced to a clean bounded statement **G1′: R₀ = {primes ≤ maxfactor(a_1)} is sufficient** — no prime beyond the largest prime factor of a_1 is ever relevant. Verified computationally on 25+ seeds, zero counterexamples. Mechanism identified (accumulating {p, q_j} constraints from the winning small-prime class override every large-prime witness; e.g. a_1=33 ⇒ E_∞=3ℤ, a_1=55 ⇒ E_∞=5ℤ). Not proved.

## Correction to prior guidance (important)
The outliner/reviewer's conjectured "R ⊆ P ∪ {2,3}" is **FALSE**. Computed counterexample a_1 = 99 = 3²·11 recruits the prime 5: R = {2,3,5,11}. The correct finite target is R ⊆ {primes ≤ maxfactor(a_1)} (holds on every seed tested). Any approach committing to P∪{2,3} will fail — pass this to enum-covering / density builders.

## Relationship to rival approaches (independence preserved)
This route reaches its gap through a *different door*: Lemmas 4–6 give a self-contained finite-state reduction (state = residue mod ∏R, deterministic transition), never invoking a covering predicate for E_∞. The endgame (Lemma 5, Lemma 6) is reusable by ALL approaches and should be promoted. The shared crux is finiteness (as the reviewer predicted G1 ≈ Lemma F), but the packaging "R₀ sufficient / no prime > maxfactor(a_1) relevant" is a concrete new bounded formulation worth handing to the density and covering builders.

## Promotable lemmas (for reviewer certification)
Lemmas 1–6 as stated in the approach file. Lemmas 5 and 6 are the highest-value: they turn any future finiteness result into the full "for every n" theorem with a two-line application.

## Spec concerns
None. Problem is proof_only, answer_type none; no final answer to verify. The claim "for every n" (from n=1, not eventual) is correctly targeted and is delivered in full by Lemma 5 once G1 is closed.
