## imo-2026-06

Standing crux (round 7): the whole problem is gap-free reduced to **(CSP)** = "no term is bad"
(`lemmas/csp-implies-theorem.md`), weakened to **¬(FIN-Q)** / the crisp value inequality "no minimal
covering set containing a large prime has minimal realization ≥ a_1". This is the 3rd collapse of the
field to ONE wall. The field below attacks that wall with genuinely different MECHANISMS — no 4th
FIN-Q/star reformulation. Shared notation: P=primes(a_1), P_max=max P, S(m)=primes(m)∩[2,P_max],
L_0=∏_{p≤P_max}p; a prime is *small* if ≤P_max, *large* if >P_max; a prime set is *covering* iff it
meets primes(a_i) ∀i; 𝒞=covering sets, 𝒯=term prime-sets, ℰ=minimal covering sets (edges of the
self-dual clutter). Certified imports reused verbatim (do NOT re-prove): ENUM, PER, F1, REAL (𝒞=𝒯,
clause (c)), self-dual clutter b(ℰ)=ℰ, CSP⇒theorem, GPC, Window Purity, Local Hub-Cover,
minimal-bad-term floor-tightness, FIN-Q⇒theorem.

---

### minimal-cover-small-only : NEW  *(priority — fresh pure-clutter mechanism)*

Target: the full IMO-2026-P6 claim (the greedy sequence is eventually arithmetic-progression-periodic:
a_{n+T}=a_n+L for all n, for some T,L>0).

Technique: hypergraph-transversal minimality on the certified self-dual clutter ℰ — a purely
set-theoretic argument about *which primes can be load-bearing in a minimal cover*, with NO induction
on term value (this is the mechanism that makes it far from every value-descent/FIN-Q route). The
endgame is a certified one-liner; the whole weight is on one clutter statement.

Skeleton:
  1. Reduce to (CSP): theorem ⟸ "no term is bad" — by certified `csp-implies-theorem.md`.
  2. Suppose a bad term exists; let m_0 be the smallest (well-ordering). C:=primes(m_0) is covering
     (REAL 𝒯⊆𝒞); S(m_0)=C∩[2,P_max] is non-covering (m_0 bad).
  3. C covering + finite ⟹ C contains an edge C'∈ℰ — by self-dual clutter (𝒞 is an up-set; every
     covering set contains a minimal one).
  4. **ℰ-small-only (THE GAP):** every edge C'∈ℰ satisfies C'⊆[2,P_max] (no large prime is load-bearing
     in any minimal cover).
  5. Closure: by (4) C'⊆[2,P_max], and C'⊆C, so C'⊆C∩[2,P_max]=S(m_0); supersets of covering sets are
     covering, so S(m_0)⊇C' is covering — contradicting m_0 bad. Hence no bad term; (CSP) holds; done
     by step 1. (This bypasses Lemma 9's stalled a_1-descent entirely — no value induction.)

Key lemmas (claim + mechanism):
  - **Edge-closure endgame (steps 3+5)** — because 𝒞 is an up-set of finite sets so contains minimal
    members (self-dual clutter, certified), and covering is superset-closed; both already on record.
    This half is essentially free.
  - **Entry lever F1' (partial, toward the gap)** — if an edge C∈ℰ contains a large prime q, then
    C∖{q} is non-covering (edge minimality), so a witness term B has primes(B)∩(C∖{q})=∅; C covering
    forces primes(B)∩C={q} exactly, i.e. q|B and B shares NO other prime of C. Since q large, q∤a_1,
    so B≠a_1; applying F1 to the pair (a_1,B) — wait, F1 says a_1 meets C via a prime, and that prime
    can't be q (q∤a_1), so **C∩P≠∅**: every large-prime edge is forced to also carry a small prime of
    a_1's own factor set. (One-line consequence of certified F1 + edge minimality; safe to use.)
  - **Essential-witness structure (the lead for closing the gap)** — because ℰ is a clutter, EACH prime
    p∈C is essential: there is a witness term B_p with primes(B_p)∩C={p}. For the large prime q, B_q is
    a term divisible by q whose small part S(B_q) is disjoint from C's small primes C∩[2,P_max]. Since
    B_q is a term, primes(B_q) is covering (REAL) and contains its own edge C''∈ℰ with primes(B_q)∩C={q}
    (so q∈C'' or C''∩C=∅). Two sub-leads to push F1' into a contradiction: (a) a well-founded monovariant
    on edges (e.g. minimal-counterexample edge minimizing its largest prime q, then derive an edge with a
    strictly smaller large prime from B_q's structure); (b) apply certified Local Hub-Cover to h=B_q to
    bound Q(B_q) and force q redundant in C via B_q's coverage. Neither is completed — this IS the gap.

Open gaps: step 4 (ℰ-small-only) — the builder must convert the F1'/essential-witness lever into a full
contradiction. Steps 1,2,3,5 are gap-free from certified lemmas.

Cases to cover: within the gap, an edge may contain one large prime or several (Q_C=C∩(P_max,∞) with
|Q_C|≥1) — the argument must handle |Q_C|≥1 general, not just the singleton (the old "Lemma A" singleton
is strictly weaker and already superseded by GPC).

Watch out for: (i) ℰ-small-only is logically ≥ the crisp value target, so it may be crux-equivalent — the
*payoff* is the genuinely different mechanism (pure transversal, no value induction), which is exactly the
diversity the field needs; if the essential-witness monovariant is not well-founded (primes unbounded
upward), the argument stalls — the builder must find a *downward* well-founded quantity (largest prime,
or |Q_C|, or ∏Q_C) that strictly decreases. (ii) Do NOT reintroduce value-descent here — that is
covering-small-part-descent's lane; keep this one purely set-theoretic. (iii) {q} alone is never covering
(q∤a_1), so every large-prime edge has size ≥2 — a sanity floor.

---

### covering-small-part-descent : ADVANCE

Target: the full P6 claim (via (CSP), same as its file).

Technique: value well-ordering / minimal-bad-term descent (value/dynamics mechanism — DISTINCT from the
pure-clutter route above and from the counting route below). Keep its target as the **crisp value
inequality** (no minimal covering set containing a large prime realizes ≥a_1), NOT ℰ-small-only — so it
does not share minimal-cover-small-only's gap (avoids the single-gap trap: the two attack the same wall
with different targets and mechanisms).

Skeleton (all steps 1–6 + Lemmas 6,7,8,9 already gap-free/certified):
  1–6. (imported/certified) reduce to (CSP); smallest bad term m_0, C=primes(m_0) covering, S(m_0)
       non-covering; Lemma 9 floor-tightness: v_p(m_0)≥2 or a redundant prime ⟹ m_0<a_1·p — the descent
       is blocked exactly at the a_1 threshold.
  7. **GAP (6b), the value inequality:** the minimal realization of C (an edge-carrying covering set with
     a large prime) is ≥a_1 is impossible — i.e. force m_0<a_1, contradicting m_0≥a_1.

Key lemmas (new lever to attempt this round):
  - **Realization-vs-a_1 via greedy Window Purity** — because m_0 minimal bad ⟹ (Lemma 9) m_0 is
    squarefree on its redundant part and a *minimal-covering skeleton*; the missing inequality is a lower
    bound on ∏(edge primes) forcing the squarefree product ≥a_1 to fail. Lead: combine Window Purity (the
    interior of every gap is E_∞-free) with the essential-witness terms B_p of C (each a term, each ≥a_1)
    to bound m_0's realization below a_1 — every essential witness B_q is divisible by the large prime q
    and ≥a_1, and its small part avoids C_s; count the value pressure this puts on m_0's window.
  - (fallback, if the builder finds it cleaner) it MAY adopt the edge-extraction endgame (steps 3+5 of
    minimal-cover-small-only) as an alternative closure — but only if it can supply a DISTINCT sub-lever
    (the value inequality), else it should stay on the value-descent lane to keep the field diverse.

Open gaps: step 7 (6b) — the value inequality tying a_1 to the covering structure.

Cases to cover: none new (Lemma 9's (i) repeated-prime and (ii) redundant-prime cases already covered).

Watch out for: do NOT merge into minimal-cover-small-only's ℰ-small-only gap — keep the crisp *value*
target so the two remain independent bets on the wall. Proven-dead closures stay barred: global Σ1/p²
capacity, pure covering/Helly (Prop D), symmetric bad-partner ascent, direct (q*,k) rewrite.

---

### bounded-window-distinctness : NEW  *(value-difference engine, far from covering framing)*

Target: the full P6 claim (via ruling out ¬(FIN-Q), certified `finite-connector-pool-periodicity.md`).

Technique: bounded-window pigeonhole + **distinctness-by-difference** (aimo-0415/aimo-0447 transplant):
a prime exceeding a window's value-length divides at most one element of the window. Operates on VALUES
(differences), not on abstract set-covering — genuinely different from every covering/descent route and
from the class-graph revisit walk; this is the one surveyed lever that touches values.

Skeleton:
  1. Reduce to ¬(FIN-Q): theorem ⟸ FIN-Q — certified. Suppose ¬(FIN-Q): an E_∞-inhabited bad class r_0
     mod L_0 with infinite pool Q(r_0)=⋃_{i∈W(r_0)}Q_i (infinitely many distinct large connectors).
  2. Membership dichotomy (★, certified): m≡r_0 (mod L_0) lies in E_∞ iff for every i∈W(r_0) some prime
     of Q_i divides m.
  3. **Distinctness-by-difference:** for any value-window of length W, a large prime q>W divides at most
     one term whose value lies in that window (else q | (difference), but 0<|difference|<W<q, impossible).
  4. **GAP — cluster the infinite pool into a bounded window:** show the witnesses i∈W(r_0) that
     contribute *new* distinct large primes to Q(r_0) recur within a bounded value-band (length O(a_1) or
     O(L_0)). Then step 3 caps the number of distinct large primes usable inside that band by (band
     length), contradicting an infinite pool — closing ¬(FIN-Q).
  5. Contradiction ⟹ FIN-Q ⟹ theorem.

Key lemmas (claim + mechanism):
  - **Local half-capacity count (reusable)** — because the certified global estimate Σ_{p>P_max}1/p² <
    0.2022 (`lemmas/term-density-and-prime-capacity.md`, Lemmas C1–C3) re-scopes to a bounded window: in
    a window of length N, small primes fill < half the slots, so ≥half must carry primes >N — feeding
    step 3. Re-scope, do NOT re-derive the numeric bound.
  - **Window localization (THE GAP)** — because the bounded-gap fact a_{n+1}-a_n≤a_1 + Window Purity
    (gap interiors E_∞-free) + linear growth a_n≍n·a_1 confine consecutive terms tightly; the lead is to
    show a hub's missed-color witnesses (Local Hub-Cover: W(h)⊆⋃_{q∈Q(h)}{B:q|B}) that introduce distinct
    NEW large primes cannot all be pushed to arbitrarily large values without each costing a slot in a
    bounded band. This clustering is NOT automatic (witnesses are spread over the unbounded sequence) —
    it is the honest hard step.

Open gaps: step 4 (window localization / clustering the distinct-large-prime witnesses into a bounded
value-band). Steps 1,2,3,5 are gap-free.

Cases to cover: within the gap, a prime may recur in infinitely many Q_i (the "recurring-prime" branch)
vs. contribute once — the count must handle both; note the recurring-prime branch alone does NOT make the
pool infinite (that needs infinitely many DISTINCT primes), so distinctness is what step 3 must exploit.

Watch out for: differences WITHIN one residue class mod M are multiples of M (unbounded) — step 3 needs
same-VALUE-window, not same-class; do not conflate. Dead branches barred: finite-fiber gcd pigeonhole
(aimo-0421) and sunflower/Δ-system both collapse to Prop D via the "extra irrelevant primes in Q_i"
escape — do NOT re-propose; Zsigmondy manufactures primes (wrong direction).

---

### window-purity-class-cycle : ADVANCE  *(direct ¬(FIN-Q) class-graph carrier)*

Target: the full P6 claim (via FIN-Q, its file's route).

Technique: revisiting walk on the finite (≤L_0-node) class-graph — a finite-state/monovariant mechanism.
Kept because it is the direct ¬(FIN-Q) carrier and is complementary to bounded-window-distinctness (which,
if it lands step 4, plugs the missing value inequality straight into this walk's Step-5 descent).

Skeleton (Steps 1–4 + Window Purity + FIN-Q⇒theorem gap-free/certified):
  5. **GAP (Step-5 descent):** an E_∞-inhabited bad class drawing on infinitely many distinct large
     connectors is modelled as an infinite revisiting walk on the finite class-graph; extract a
     contradiction from a revisit.

Key lemmas (lever to attempt):
  - **Strict-prime-descent-per-revisit (5a) or first-hole over-constraint (5b)** — because a deterministic
    monovariant on the walk (e.g. "least available connector prime at each revisit") would force a strict
    decrease on a well-founded quantity across a revisit of the same class node, contradicting an infinite
    walk. The lead is to import bounded-window-distinctness's value-difference cap as the monovariant
    (each revisit within a bounded value-band must reuse a prime, closing the walk).

Open gaps: Step-5 descent (the deterministic transition / monovariant on the class-graph).

Cases to cover: none new.

Watch out for: the class-graph has no *deterministic* step map yet (foreign-explorer finding: which large
prime is "used" at a witness is not a function of the class alone) — the builder must CONSTRUCT the
monovariant, not assume it; aimo-0964/aimo-0351 are shape-inspiration only, not importable transitions.
Keep distinct from bounded-window-distinctness: this one is the finite-state carrier, that one is the
value-count engine — they share the ¬(FIN-Q) target but attack it with different machinery, and one feeds
the other.

---

**Field for the outline-reviewer:** minimal-cover-small-only (NEW, priority — pure clutter/transversal,
ℰ-small-only gap), covering-small-part-descent (ADVANCE — value descent, crisp value inequality),
bounded-window-distinctness (NEW — value-difference distinctness engine, window-localization gap),
window-purity-class-cycle (ADVANCE — class-graph revisit descent, feeds off the value-difference cap).
Four distinct mechanisms — transversal minimality / value descent / value-difference counting /
finite-state revisit — all aimed at the one wall from genuinely different directions.
