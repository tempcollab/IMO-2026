## imo-2026-06

Round 1, fresh population (0 approaches). Four genuinely rival framings opened. A central rigorous
reduction was found and numerically verified (a_1 ∈ {15,35,77,105,143,255}): **the sequence is exactly
the increasing enumeration of the compatible set E_∞ = {m : gcd(m,a_i)>1 ∀i} starting at a_1**, and E_∞
is *exactly* periodic mod L = ∏(relevant primes) — which is why a_{n+T}=a_n+L holds from n=1, not just
eventually. This collapses the whole problem to one finiteness statement. The field attacks that
finiteness (and the periodicity) from four far-apart directions.

Key pitfall confirmed by computation (hand to every builder): the clean "m eligible ⟺ divisible by ≥2
of the core primes" predicate is FALSE (a_1=35: E_∞ has 34 residues mod 210, not the 70 with ≥2 of
{2,3,5,7}). The correct rule is the covering-set condition. Do not use ≥2. Also L ≠ ∏(recruited covering
primes) by heuristic; L = ∏R with R the relevant (minimal-covering) prime set.

---

enum-covering-primes: new  (FLAGSHIP — status partial, reduction proven, one isolated gap)
Target: a_{n+T}=a_n+L for every n.
Technique: structural reduction to a periodic compatible set E_∞ + covering-prime characterization + CRT counting. No dynamics pigeonhole.
Skeleton:
  1. All terms pairwise non-coprime ⇒ every term ∈ E_∞ (incl. a_1) — by the defining rule + symmetry.  [proven]
  2. Sequence = increasing enumeration of E_∞ from a_1, i.e. a_{n+1}=min{m∈E_∞:m>a_n} — because E_∞⊆E_n and a_{n+1}∈E_∞ is min(E_n∩(a_n,∞)), so no compatible integer is skipped.  [proven — the new idea; kills the transient, gives "every n" free]
  3. m∈E_∞ ⟺ primes(m) covering ⟺ primes(m)∩R covering — minimal covering sets ⊆ R.  [proven]
  4. R finite ⇒ E_∞ periodic mod L=∏R (globally) ⇒ enumeration gives a_{n+T}=a_n+L, T=#(E_∞ mod L), for every n.  [proven modulo Lemma F]
Key lemmas:
  - Step-2 reduction — E_∞⊆E_n and each term lies in E_∞, so the greedy min never skips a compatible value.
  - Enumeration-of-periodic-set — a set periodic mod L advances by L every T=#(residues) steps from its first element.
  - Bounded gaps a_{n+1}-a_n ≤ a_1 (least multiple of a_1 above a_n is compatible) ⇒ E_∞ syndetic.
  - LEMMA F (GAP): R finite. Conjectured explicit R ⊆ primes(a_1)∪{2,3} (holds on all 6 seeds). Mechanism: a relevant prime is an irreplaceable witness in a minimal covering set; use syndeticity (gap≤a_1) + "every term divisible by a prime of a_1" to show a large prime witness can always be replaced by a small one.
Open gaps: Lemma F only (finiteness of relevant primes). Steps 1–4 complete.
Cases to cover: within Lemma F, "no prime > maxfactor(a_1) relevant" and "no small prime beyond 2,3 recruited".
Watch out for: the ≥2 predicate is false; inclusion direction E_∞⊆E_n is the crux of Step 2; L=∏R not ∏(recruited).

finite-state-window: new  (status unsolved — independent pigeonhole route, avoids E_∞)
Target: a_{n+T}=a_n+L for every n.
Technique: bounded gaps + finite color alphabet ⇒ finite state; pigeonhole a recurring state; forward-propagate by greedy determinism (aimo-0079/0274 window skeleton).
Skeleton:
  1. Bounded gaps ≤ a_1.  [proven]
  2. Finite color alphabet c(a_i)=primes(a_1)-divisors, 2^{|P_1|}-1 values.  [proven]
  3. Recruited-prime set Q finite (GAP G1).
  4. Finite state (a_n mod ∏Q + last-W colors) recurs by pigeonhole.
  5. Forward propagation (GAP G2): next term depends only on recorded finite state — fights the unbounded-memory rule.
  6. Subsequence recurrence ⇒ all n.
Key lemmas: bounded gaps; Q finite (aimo-0421 pigeonhole on persistent primes); state-determinism (the hard, corpus-unmatched step).
Open gaps: G1 (Q finite), G2 (state determinism / propagation).
Cases to cover: none beyond G1/G2.
Watch out for: aimo-0079 propagation is a single reindex, far weaker than needed; keep G2 independent of the covering characterization or this collapses into enum-covering.

density-bounded-recruitment: new  (status unsolved — analytic attack on the finiteness fact)
Target: a_{n+T}=a_n+L for every n.
Technique: prime density / Bertrand / counting to bound load-bearing primes by magnitude (distinct mechanism from enum-covering's combinatorics), then covering-periodicity endgame.
Skeleton:
  1. Bounded gaps ⇒ term density ≥ 1/a_1.  [proven]
  2. Large prime q covers density-≤1/q of terms — too sparse to be forced.
  3. Persistent-prime set finite (GAP): primes>a_1 excluded by sparsity vs syndeticity; primes≤a_1 finite. Target Q ⊆ {p ≤ maxfactor(a_1)}.
  4. Import covering-periodicity (enum-covering Steps 3–4) ⇒ conclusion for every n.
Key lemmas: density≥1/a_1; persistent-prime finiteness (analytic analogue of Lemma F); imported covering periodicity.
Open gaps: persistent-prime finiteness (Step 3).
Cases to cover: primes>a_1 vs primes≤a_1.
Watch out for: gap bound is loose (needs only finiteness); keep the argument genuinely analytic so it doesn't share enum-covering's wall.

difference-sequence-squeeze: new  (status unsolved — exploratory, imports aimo-0680 squeeze)
Target: a_{n+T}=a_n+L for every n.
Technique: gap sequence d_n∈{1..a_1} over finite alphabet; pigeonhole a repeated block; upgrade to exact global periodicity via aimo-0680 divisibility-squeeze.
Skeleton:
  1. d_n ≤ a_1 finite alphabet.  [proven]
  2. Bounded "responsibility" data per step (GAP R1).
  3. Pigeonhole a repeated length-W block at x<x'.
  4. Divisibility-squeeze: discrepancy divisible by witness spacing yet bounded ⇒ vanishes (GAP R2, aimo-0680).
  5. Anchor to n=1, combine classes via lcm.
Key lemmas: bounded gaps; repeated block (pigeonhole); squeeze upgrade (must manufacture a genuine divisibility — the make-or-break).
Open gaps: R1 (responsibility alphabet), R2 (the divisibility powering the squeeze — not guaranteed by analogy).
Cases to cover: lcm-combine of responsibility classes.
Watch out for: need an HONEST divisibility for the squeeze; if none exists, record dead end rather than hand-wave.

---

Diversity note (per CLAUDE shared-gap rule): enum-covering and density-bounded-recruitment both need
"finitely many relevant/persistent primes" but via DIFFERENT mechanisms (combinatorial minimal-covering
witnesses vs. analytic density/Bertrand) — deliberately two independent attacks on the one true crux.
finite-state-window and difference-sequence-squeeze attack completely different objects (automaton state;
gap sequence) with different walls (propagation; squeeze divisibility), so the field does not collapse to
one wall. enum-covering is the clear leader (proven reduction, single isolated gap).

Candidate slugs for outline-reviewer to rank:
  enum-covering-primes (advance/build — closest to done), finite-state-window, density-bounded-recruitment, difference-sequence-squeeze
