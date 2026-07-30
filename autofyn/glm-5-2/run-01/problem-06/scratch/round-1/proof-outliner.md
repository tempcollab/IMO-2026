## imo-2026-06

### Field summary

Round 1, empty workspace. Five rival approaches seeded, each a complete attempt at the whole claim (`∃ T,L>0: a_{n+T}=a_n+L for every n≥1`) with explicit gaps. Framings are deliberately far apart — they do NOT share one wall. The shared underlying difficulty (the "stabilization river": bounding the active/kernel prime set, call it B1) is approached by 4 distinct mechanisms, and 2 routes (compactness-konig, bijection-from-n1) attempt to AVOID B1 entirely via different gambles.

**Imported clean lemma (used by all routes, certify it in `lemmas/`):** `a_{n+1} - a_n ≤ R := rad(a_1)` for all n. Proof: the next multiple of `R` after `a_n` is divisible by every prime of `a_1`; every past term shares a prime of `a_1` with it; so it is a valid candidate. Non-circular.

**Verified empirical anchor (conjecture, drives the from-n=1 surprise):** the period holds FROM n=1 in every tested case (empty pre-period); `L` is always a multiple of `R = rad(a_1)`; kernel `S = primes(L) ⊇ primes(a_1)`; `T=1 ⟺` a single prime divides every term.

---

### Approaches

**bounded-diff-finite-state**: new
Target: `∃ T,L>0: a_{n+T}=a_n+L` for every n≥1.
Technique: bounded differences ≤ rad(a_1) ⇒ finite state `(a_n mod L, stable small-support family F)` ⇒ pigeonhole eventual periodicity ⇒ lift congruence to equality ⇒ strengthen "eventually" to "for every n". The "outer automaton" route — bounds active primes then pigeonholes.
Skeleton:
  1. Bounded diffs `≤ R=rad(a_1)` — by next-multiple-of-R candidate (clean).
  2. Finite active-prime set `S ⊇ P_1` with greedy determined by `(a_n mod L, F)` — by bounding active primes (B1 crux) via Bertrand vs. competing small-prime candidate.
  3. Determinism once F stable — CRT: admissible candidates are a union of residue classes mod L; large-prime shortcuts eventually stop (sub-gap).
  4. Pigeonhole ⇒ eventual periodicity mod L.
  5. Lift congruence to `a_{n+T}=a_n+L` (each residue visited once per period).
  6. Injectivity of transition on reachable residues ⇒ from-n=1.
Key lemmas:
  - Bounded diffs ≤ rad(a_1) — next multiple of rad(a_1) hits all past terms via primes of a_1.
  - Finite active set S ⊆ {primes ≤ R} — Bertrand + competing-candidate comparison (unproven B1).
  - Transition determined by (a_n mod L, F) — CRT + large-prime-shortcuts-stop.
  - Lift = L not kL — minimality + each residue once per period.
Open gaps: step 2 (B1 absolute bound on active primes); step 3 (large-prime shortcuts stop); step 5 (lift = L); step 6 (injectivity ⇒ from-n=1).
Cases: even a_1 / prime power (trivial T=1); odd ≥2 prime factors (hard).
Watch out for: modulus is L=∏S (kernel), NOT R and NOT ∏_{p≤R}p (periodicity mod ∏_{p≤R}p is FALSE — verified). Free-rider primes unbounded — do not claim finitely many primes. Use next MULTIPLE of R, not a_n+R.

**hitting-set-monovariant**: new
Target: whole claim.
Technique: attack kernel stabilization head-on via a well-founded monovariant on the minimal-hitting-set family `M_n`; once `M_n` stable, greedy is a deterministic walk on a fixed finite union of residue classes mod `L=∏(∪M)`. The "combinatorial kernel, explicit measure" route.
Skeleton:
  1. `A_n = ∪_{h∈M_n}{multiples of m_h}` (definitional; minimal hitting sets).
  2. Bounded diffs (imported).
  3. Cross-intersecting `M_n` ⇒ stable forever (clean: new term's support contains some `h∈M_n` meeting every `h'`, so nothing removed/added).
  4. Monovariant ⇒ `M_n` reaches cross-intersecting or singleton in finite time (THE CRUX B1+measure).
  5. Singleton collapse `{{p}}` ⇒ T=1, L=p (terminal).
  6. Stable M ⇒ `a_{n+T}=a_n+L`, T=|R|, L=∏(∪M) (CRT + cyclic successor).
  7. From-n=1 (residue "next" map is a bijection on R).
Key lemmas:
  - A_n = union of APs indexed by M_n — hitting-set definition + well-founded reduction.
  - Cross-intersecting M_n is self-sustaining — new support contains a current h meeting all h'.
  - M_n reaches cross-intersecting/singleton — well-founded measure decreasing at each non-closed step (crux, unproven; needs B1 to make the poset finite).
  - Stable M ⇒ a_{n+T}=a_n+L — iterating least-greater-than on a finite union of residue classes is a single cycle.
Open gaps: step 4 (B1 + well-founded measure — the heart); step 6 (each residue once per period); step 7 (from-n=1).
Cases: singleton collapse (T=1) vs. cross-intersecting closure (T>1) — both attractors must be handled.
Watch out for: "primes dividing some a_n is finite" is FALSE — object is M_n/∪M, not ∪supp. M need not be all (k−1)-subsets — singleton is the other attractor. `Σ|h|` alone is NOT well-founded without B1.

**periodic-set-iteration**: new
Target: whole claim.
Technique: FACTOR the problem — (I) an abstract theorem "iterating least-greater-than on a periodic set is a single cycle, periodic from the start" (pure combinatorics, likely short); (II) the admissible set `A_n` converges to a fixed periodic set. Distinctive escape: prove set-convergence via a profinite compactness argument on the chain of residue-class descriptions, possibly avoiding B1.
Skeleton:
  1. Theorem: iterating `f(x)=min(A∩(x,∞))` on a period-L set A from any x_0∈A gives `x_{k+T}=x_k+L` from k=0 (cyclic successor is a bijection/single cycle).
  2. `A_n` is a decreasing chain of periodic sets (each = union of APs).
  3. Common-period extraction: ∃ L,N with `A_n` a union of residue classes mod L for n≥N.
  4. `A_n` stabilizes as a set to `A` with period L — by finite kernel (B1, shared) OR profinite compactness escape (distinctive, unproven gamble).
  5. Compactness escape: `A_n` as clopen sets in `Ẑ`; decreasing chain; compactness ⇒ limit; extract finite periodic quotient.
  6. Apply Theorem 1 ⇒ from-n=1 (free corollary).
Key lemmas:
  - Theorem 1 (iteration on periodic set ⇒ single-cycle from start) — cyclic successor on sorted residues is a transitive bijection.
  - A_n decreasing chain of periodic unions — constraints accumulate + minimal-hitting-set AP decomposition.
  - A_n stabilizes to a periodic set — B1 (shared) OR profinite compactness (distinctive, gamble).
Open gaps: Theorem 1 proof (short); step 4/5 (A_n stabilizes — the gamble); step 6 (from-n=1 once stable).
Cases: trivial (A_n = "multiples of p" immediately); hard case full route.
Watch out for: `A_n` has NO common period initially (m_n = rad(lcm) grows) — must be extracted, not assumed. The orbit is NOT contained in `A_∞=∩A_n`. Profinite compactness move (step 5) is a research gamble — flag explicitly. High variance: elegant if it closes, collapses to B1 otherwise.

**compactness-konig-branch**: new
Target: whole claim.
Technique: NON-CONSTRUCTIVE existence via König's lemma on the tree of consistent finite residue-histories. Never bounds the kernel explicitly (aims to avoid B1); uses the rad(a_1) LOCAL gap bound to get finite branching, then König ⇒ infinite path ⇒ eventually periodic; uniqueness of the greedy path ⇒ it IS the periodic one.
Skeleton:
  1. Bounded diffs (imported).
  2. History tree T: nodes = consistent residue tuples mod M=R; greedy path is one infinite branch.
  3. Finite branching (THE CRUX of this route — local bound, not B1): next residue ∈ window of size R; node-state must be enriched to determine the future without re-importing B1.
  4. König ⇒ infinite path (if finitely branching).
  5. Infinite path in finitely-branching tree with finite node-types ⇒ eventually periodic.
  6. Congruence mod M ⇒ `a_{n+T}=a_n+L` (L = lift, M | L).
  7. Greedy path is the UNIQUE infinite path (greedy picks least continuation) ⇒ it equals any periodic path ⇒ from-n=1 (if cycle contains root).
Key lemmas:
  - History tree finitely branching — local rad(a_1) window (R choices); enriched state is the crux.
  - Infinite path ⇒ eventually periodic — finite directed graph ⇒ periodic walk.
  - Greedy path is the unique infinite path — greedy's least-continuation uniqueness.
  - Periodic path = single cycle from root — (deepest gap).
Open gaps: step 3 (finite branching with rich-enough state, WITHOUT B1 — the gamble); step 6 (lift = L); step 7 (uniqueness + cycle-from-root + from-n=1, watch for circularity).
Cases: trivial (single residue); hard case.
Watch out for: compactness GAMBLES on avoiding B1 — if finite branching secretly requires B1, collapses to bounded-diff-finite-state. König needs FINITE branching (residue window alone may not suffice — large primes affect future). Step 7's "unique infinite path ⇒ it is the periodic one" risks circularity (periodic path's existence is what we prove). Highest-variance route.

**bijection-from-n1**: new
Target: whole claim, DIRECTLY from n=1.
Technique: prove the transition `T` on the reachable residue set is INJECTIVE ⇒ bijection on the finite reachable set ⇒ single permutation cycle ⇒ periodicity-from-n=1 is FREE. Makes the from-n=1 surprise the spine, not a cleanup. Distinctive crux: injectivity of T (different shape of difficulty than bounding the kernel).
Skeleton:
  1. Bounded diffs (imported).
  2. Finite reachable residue set R mod L; T well-defined on R.
  3. Injectivity of T (THE CRUX): if T(r)=T(r') then r=r'. Candidate mechanism — the cyclic-successor on a shift-invariant admissible residue set is strictly monotone; OR a direct greedy-minimality + symmetry argument (gcd(a_{n+1},a_n)>1).
  4. Injective + finite ⇒ bijection ⇒ permutation ⇒ single cycle ⇒ `a_{n+T}≡a_n (mod L)` for all n≥1.
  5. Lift = L (cycle visits each residue once ⇒ cyclic gap sum = L).
  6. From-n=1 FREE (cycle contains a_1 mod L).
Key lemmas:
  - T well-defined on residues mod L — admissible set periodic (B1, hidden).
  - T injective — cyclic successor monotone OR direct greedy-minimality (crux, unproven; the route's distinctive attempt is to prove it WITHOUT first cleanly bounding the kernel).
  - Bijection ⇒ single cycle ⇒ from-n=1 — standard permutation fact.
  - Lift = L not kL — bijection visits each residue once.
Open gaps: step 2/3 (well-definedness AND injectivity — the whole route; B1 river); step 5 (lift = L).
Cases: trivial (R={0 mod p}); hard case.
Watch out for: if injectivity secretly requires "admissible set periodic" (= B1), this route is NOT genuinely distinct — it repackages bounded-diff-finite-state. Builder must test a DIRECT injectivity argument (not via periodicity of admissible set). From-n=1 payoff is real ONLY if injectivity holds globally from term 1. Reconcile lift step: a proper-subset cycle around the circle still sums to L (cyclic successor) — confirm vs. empirical T=|R| (full set).

---

### NEW approaches opened (slug + one-line framing)
- `bounded-diff-finite-state` — bounded diffs ≤ rad(a_1) ⇒ finite-state automaton on residues + stable small-support family ⇒ pigeonhole periodicity (the outer-automaton route).
- `hitting-set-monovariant` — minimal-hitting-set family M_n stabilizes via a well-founded monovariant ⇒ greedy walks a fixed finite union of APs (the combinatorial-kernel route).
- `periodic-set-iteration` — factor into an abstract "iteration on a periodic set is a single cycle" theorem + convergence of admissible sets (possibly via profinite compactness, the gamble route).
- `compactness-konig-branch` — König's lemma on the tree of consistent residue-histories; local rad(a_1) bound for finite branching; uniqueness of the greedy path ⇒ from-n=1 (the non-constructive route).
- `bijection-from-n1` — transition T on reachable residues is injective ⇒ bijection ⇒ single permutation cycle ⇒ from-n=1 periodicity is free (the injectivity route).

### REVISE / ADVANCE / COPY requests
- None. Round 1, empty workspace — all five are new seeds. No prior stuck approaches to revise, no live approaches to advance, no twin-gap situation to copy.

### Candidate build set (for the outline-reviewer to rank)
Proposed build set (all five new approaches — the reviewer ranks and may prune/reorder):
`bounded-diff-finite-state, hitting-set-monovariant, periodic-set-iteration, compactness-konig-branch, bijection-from-n1`

Diversity check (why the field does not collapse to one wall):
- `bounded-diff-finite-state` and `hitting-set-monovariant` both cross the B1 (active-prime-bound) river but via DIFFERENT mechanisms (pigeonhole-after-bound vs. explicit well-founded monovariant on the hitting-set family). If B1 is fundamentally hard they stall together — mitigated by the three routes below.
- `periodic-set-iteration` factors out an abstract theorem and gambles on a profinite-compactness escape from B1.
- `compactness-konig-branch` gambles on avoiding B1 via König's lemma + a LOCAL (rad-gap) branching bound.
- `bijection-from-n1` gambles on a direct injectivity argument that may avoid cleanly bounding the kernel.
Two high-variance gambles (`periodic-set-iteration`, `compactness-konig-branch`) and one structural-injectivity gamble (`bijection-from-n1`) hedge the two B1-crossing routes. The field is far apart in framing.

Priority hint for the reviewer (non-binding — ranking is the reviewer's job): the two B1-crossing routes (`bounded-diff-finite-state`, `hitting-set-monovariant`) are the most likely to close rigorously and should probably be ranked highest; the three gambles are higher-variance long shots that should stay live but rank lower until their distinctive step shows traction.
