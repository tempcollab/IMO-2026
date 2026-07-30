## imo-2026-06

Shared context (read once). The whole problem is certified-reduced to ONE crux, phrased
equivalently as: **Lemma A** (no prime q>P_max is the exact common-prime intersection of two
terms) ⟺ **R ⊆ {primes ≤ P_max}** (R = union of the minimal prime-sets of terms) ⟺
**Structural Lemma** (every two terms share a prime ≤ P_max) ⟺ **Small-covering restatement**
(for every term a_i, the set primes(a_i) ∩ {primes ≤ P_max} is already a covering set — hits
every term). Importable, gap-free, from round 1:
- `lemmas/enumeration-of-E-infinity.md` — a = increasing enumeration of E_∞ ∩ [a_1,∞).
- `lemmas/periodic-set-enumeration.md` — E tail-periodic mod L ⇒ b_{n+T}=b_n+L for all n.
- `enum-covering-primes.md` Steps 1–4 + R1/R2 — covering characterization and the exact
  identity R = {q : some pair of terms has prime-intersection exactly {q}}, and R finite ⇒ theorem.
Certified auxiliary facts (round 1 + reconfirmed numerically this round on a_1∈{15,35,77,99}):
every multiple of a_1 is a term (k·a_1 ∈ E_∞, since primes(k·a_1) ⊇ P is covering); gaps
a_{n+1}−a_n ≤ a_1. So the terms contain the full AP a_1·ℤ ∩ [a_1,∞) — a lever the counting/
recruitment framings can use that the pure-set framing does not.

All four slugs below target the ACTUAL theorem end-to-end (import the reduction, so the only
open work is the crux). They are DIFFERENT attack surfaces on the same certified crux — a static
set-identity induction, a dynamic recruitment monovariant, and a global capacity count — chosen
to be far apart per the shared-gap Rule; the honest gap in each is flagged explicitly and NOT
faked as closed. Cheap kills already ruled out (do not re-outline): pure density/persistence
(false — big primes have positive density in periodic E_∞); local "smaller compatible number in
(a_{j-1},a_j)" (interval is empty by minimality); Helly/sunflower on colors (colors size 3–5, no
common prime); cofactor-peel as an independent route (circular — corollary of the crux).

---

enum-covering-primes: advance
Target: ∃ T,L with a_{n+T}=a_n+L for all n≥1 (the theorem).
Technique: certified E_∞-enumeration + covering reduction; the whole proof is complete except
Lemma A. This slug HOLDS the certified reduction and endgame — keep it live.
Skeleton: Steps 1–4 and R1/R2 are done (reviewer-certified). It imports whichever crux proof
lands from the three new framings below (all three prove a statement equivalent to its Lemma A),
then Step 4 delivers the theorem verbatim.
Key lemmas: none new — it is the reduction spine.
Open gaps: Lemma A only. Builder action this round: none required beyond wiring in a crux proof
if one of the new framings closes; otherwise it remains the standing partial.
Cases to cover: none (all discharged except Lemma A).
Watch out for: do not re-derive the reduction in the new slugs — import it.

---

reduced-process-identity: new
Target: the theorem (∃ T,L: a_{n+T}=a_n+L ∀n).
Technique: strong induction proving the true greedy sequence coincides TERMWISE with the
"small-primes-only" greedy sequence, which is manifestly finite-state ⇒ periodic. A static
set-identity / process-coincidence framing (explorer-1 opening 2), distinct from set-finiteness.
Skeleton:
  1. Import enumeration reduction: a_n = n-th element of E_∞ ∩ [a_1,∞). — certified lemma.
  2. Define the reduced compatible set E* := {m>1 : primes(m) ∩ primes(a_i) ∩ [2,P_max] ≠ ∅ for
     every i} and let b_1<b_2<… enumerate E* ∩ [a_1,∞). E* ⊆ E_∞ (a small-prime hit is a hit),
     so E* is a subset; membership in E* depends only on m mod L_0, L_0 = ∏_{p≤P_max} p (each
     constraint "m divisible by some prime of a fixed finite set" is a residue condition). Hence
     E* is exactly periodic mod L_0. — by CRT/covering-system (KB: Modular arithmetic, CRT).
  3. By the periodic-set-enumeration certified lemma applied to E*: b_{n+T}=b_n+L_0 for all n,
     with T = |E* ∩ (x,x+L_0]| ≥ 1. So the reduced sequence already satisfies the conclusion.
  4. CRUX, as a strong induction (index n): claim a_n = b_n for every n. IH: a_k=b_k for k≤n
     (so the two sequences share the same prefix, and by construction b_1..b_n pairwise share a
     prime ≤ P_max). Then a_{n+1}=min{m>a_n : gcd(m,a_k)>1 ∀k≤n} and b_{n+1}=min{m>a_n : m shares
     a prime ≤P_max with each a_k}. Since E*⊆E_∞, b_{n+1} ≥ a_{n+1} automatically. The reverse
     a_{n+1} ≥ b_{n+1} — i.e. a_{n+1} shares a prime ≤ P_max with EVERY a_k (k≤n), not merely
     some prime — is the whole difficulty.
  5. Once a_n=b_n ∀n, step 3 gives the theorem. — direct.
Key lemmas (claim + mechanism):
  - E* periodic mod L_0 — because "hit by some prime of a fixed finite set" is a union of residue
    classes; membership is a function of m mod L_0. (Solid, not the gap.)
  - b_{n+1} ≥ a_{n+1} (easy direction) — because E* ⊆ E_∞, so the reduced min is ≥ the true min
    with a matched prefix. (Solid.)
  - GAP: a_{n+1} shares a small prime (≤P_max) with every predecessor a_k. Equivalent to the
    Structural Lemma but packaged as "the sequences never diverge, even once" — verified termwise
    exactly on a_1∈{15,35,77,97,105,143,182,1155,2431}. The IH the builder MUST exploit (this is
    the new leverage over Lemma A stated bare): a_1..a_n are pairwise small-intersecting AND
    a_{n+1} is the MINIMUM compatible integer in the window (a_n, a_n+a_1]; the window contains
    the next multiple of a_1 (a genuine small-covering competitor is nearby), so a_{n+1} being
    minimal and yet large-prime-connected must be contradicted by producing a small-connected
    competitor ≤ a_{n+1}.
Open gaps: step 4 reverse inequality (the crux) — builder attempts the induction; if it cannot
close, record precisely where the minimality-of-window argument breaks.
Cases to cover: a_{n+1} vs each predecessor class; the (possibly vacuous) large-prime-only case.
Watch out for: the trap that the window ALWAYS contains a compatible number (true, e.g. next
multiple of a_1) does NOT immediately give a SMALL-only one — a_{n+1} may still legitimately be
smaller than any small-only competitor; the argument must use the pairwise-small-intersecting IH,
not generic window counting (explorer-1 opening 4 shows generic CRT counting fails: window a_1 can
be far below the CRT product). Do not smuggle in periodicity of E_∞ (that is the conclusion).

---

cofactor-recruitment-smoothness: new
Target: the theorem, via R ⊆ {primes ≤ P_max} (R finite).
Technique: a DYNAMIC recruitment monovariant — process terms in index order, track the finite set
R_i of load-bearing primes, and show a new prime enters only through the small-prime cofactor of a
greedily-minimal witness term, so R never reaches above P_max. Distinct from the static framings:
it analyses the factorization of the specific term that TRIGGERS each recruitment (explorer-2).
Skeleton:
  1. Import reduction: theorem ⟸ R ⊆ {≤P_max}, with R = {q : some pair shares exactly {q}} (R1).
  2. Recruitment order: define R_i = union of minimal members of {primes(a_1),…,primes(a_i)}.
     R_1 = P ⊆ {≤P_max}. A prime q first enters at step i iff primes(a_i) is a NEW minimal member
     containing q (no earlier term's prime-set is ⊊ primes(a_i)). — bookkeeping.
  3. Witness-cofactor structure: if a_i is a new minimal member with a prime q>P_max, then (R1
     derivation, importable) its small part S_i = primes(a_i) ∩ {≤P_max} is NON-covering on the
     prefix: some earlier term a_j has primes(a_j) ∩ S_i = ∅, so a_i, a_j share only large primes.
     Note S_i ≠ ∅ (a_i shares a prime of P with a_1). So recruitment of q is witnessed by a term
     a_i whose SMALL part fails to reach back to some a_j.
  4. CRUX (cofactor-smoothness): rule out step 3. Mechanism to attempt: a_i is the smallest
     integer in the window (a_{i-1}, a_{i-1}+a_1] compatible with all predecessors, and among
     compatible integers the multiples of rad(S) for a small covering S are spaced ≤ ∏_{p∈S} p
     apart; combined with "all multiples of a_1 are terms" (so a_j-type obstructions are themselves
     built from small primes), argue the minimal choice a_i cannot be forced onto a large prime.
Key lemmas (claim + mechanism):
  - R = {q : some pair shares exactly {q}} and "new minimal member ⇒ small part non-covering on
    prefix" — importable from enum-covering-primes R1. (Solid.)
  - Every multiple of a_1 is a term; gaps ≤ a_1 — certified. Gives the witness a_i a small-covering
    competitor (next multiple of a_1) within the window. (Solid.)
  - GAP: the triggering witness a_i has all its LOAD-BEARING prime factors ≤ P_max — i.e. the
    cofactor a_i/q^{v_q} that carries the connectivity is P_max-smooth in the relevant sense.
    Concrete failing instance to reproduce and generalize: a_1=99, term 110=11·10, cofactor 10=2·5
    both ≤ P_max=11 and both recruited. The mechanism is minimality-in-a-window, NOT size (a_i→∞).
Open gaps: step 4. Explorer-2 flags this exact cofactor-boundedness as the load-bearing, un-made-
rigorous claim; builder attempts a smooth-number / Bertrand-style bound on the minimal compatible
integer in a length-a_1 window.
Cases to cover: |S_i|=1 vs ≥2; q the unique large prime vs several large primes in primes(a_i).
Watch out for: the cofactor-PEEL observation ("v ≤ a_{i-1} and v compatible with all earlier") is
CIRCULAR (explorer-1 opening 3) — do not use "v is compatible" as a hypothesis; that is a corollary
of the crux. The non-circular content is WHY the minimal window-choice is smooth, which must come
from minimality + the a_1ℤ term-lattice, not from assuming compatibility of the peeled cofactor.

---

large-prime-capacity-counting: new
Target: the theorem, via R ⊆ {primes ≤ P_max} (R finite).
Technique: GLOBAL double-counting / prime-capacity contradiction adapted from crux aimo-0447
(place a covering prime per index-pair; bound how many pairs large primes can jointly cover via
Σ_{p} 1/p²). Distinct top-level target: instead of ruling out ONE witness pair locally, assume R
infinite and derive too-many-large-sole-connectors against a capacity bound (explorer-3 opening 3).
Skeleton:
  1. Import reduction: suffices to show R finite; suppose NOT — infinitely many distinct primes
     q>P_max lie in R, each (by R1) the exact intersection of some pair of terms.
  2. Capacity frame: among the terms in [a_1, X], let N(X) = #terms; N(X) ≥ X/a_1 (all multiples
     of a_1 are terms). Each prime p is the shared prime of ≤ C(⌊X/p⌋, 2) pairs of terms ≤ X
     (only terms divisible by p). — double counting (KB: Double counting; Pigeonhole).
  3. Large-prime capacity: Σ_{p>P_max} C(X/p,2) ≤ (X²/2)·Σ_{p>P_max} 1/p². Σ_p 1/p² ≈ 0.4522, and
     the tail Σ_{p>P_max} 1/p² is small — so pairs whose ONLY shared prime exceeds P_max are a
     vanishing fraction of the ~N(X)²/2 ≥ X²/(2a_1²) pairs. — PNT / prime-zeta tail (KB: prime
     counting, Bertrand).
  4. CRUX (localize-to-globalize): convert "q ∈ R" (one sole-connector pair, members possibly
     enormous) into a POSITIVE-DENSITY family of sole-connector pairs among terms ≤ X, so that
     step 3's capacity bound is actually violated. This is the real risk and the honest gap.
Key lemmas (claim + mechanism):
  - N(X) ≥ X/a_1; a prime p connects ≤ C(X/p,2) pairs ≤ X — certified / elementary. (Solid.)
  - Σ_{p>y} 1/p² → 0, so large primes have small pair-capacity — prime-zeta tail. (Solid; the
    aimo-0447 mechanism.)
  - GAP: one sole-connector witness ⇒ Ω(X²) sole-connector pairs among terms ≤ X (or: infinitely
    many DISTINCT large sole-connectors force, cumulatively, more large-prime-covered pairs than
    capacity allows). Explorer-3 flags this as NOT yet available without assuming periodicity
    (which would be circular). Possible non-circular seed: use the a_1ℤ term-lattice — from a
    single pair (A,B) sharing exactly {q}, translate along multiples to manufacture more disjoint
    sole-connector pairs, OR count minimal members directly (each distinct q>P_max in R gives a
    distinct term whose small part is non-covering — bound how many such "small-non-covering"
    terms can sit below X).
Open gaps: step 4 (localize-to-globalize). Builder should FIRST attempt the direct count of
"minimal members with a large prime below X" against capacity, before the pair-translation route.
Cases to cover: q just above P_max vs q≈X; finitely-many-but-unbounded R (must also be excluded,
not only R infinite — R finite is the target, so handle "R unbounded" = infinitely many large q).
Watch out for: Lemma A forbids even ONE witness pair, but counting only bounds a FRACTION — the
argument MUST reach zero, so the localize step is mandatory, not cosmetic. Do not assert periodicity
of E_∞ to get density (circular). If the localize step cannot be made non-circular, record that
precisely — this framing's value is testing whether capacity+lattice can replace the local argument.

---

Field handed to the outline-reviewer:
- enum-covering-primes (advance — holds certified reduction/endgame; imports any crux proof)
- reduced-process-identity (new — static process-coincidence induction)
- cofactor-recruitment-smoothness (new — dynamic recruitment monovariant / cofactor smoothness)
- large-prime-capacity-counting (new — global aimo-0447-style capacity contradiction)

Note: difference-sequence-squeeze (elo 1454, never expanded, stalled on an unmanufactured
divisibility "R2" in the raw gap sequence) is left un-nominated this round — it shares the crux
without the certified reduction scaffold and is dominated by the three new surfaces; revisit only
if all three new framings stall on the identical localize/minimality step.
