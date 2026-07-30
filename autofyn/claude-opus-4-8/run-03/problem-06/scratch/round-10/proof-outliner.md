## imo-2026-06

Context: 4th+ collapse to ONE certified-equivalent wall — (CSP) = ℰ-small-only = (EC) = ¬(FIN-Q),
all reformulations EXHAUSTED. Per the CLAUDE.md shared-gap rule this round fields TWO genuinely-new
framings (neither a 5th CSP/ℰ/EC/FIN-Q reformulation) plus one advance carrying a CONCRETE NEW descent
variable. The recruitment-counting lens self-certified "one slot per window" is a relabel of two dead
mechanisms — NOT fielded. Imports reused, do not re-prove: enumeration-of-E-infinity, periodic-set-
enumeration, csp-implies-theorem, essential-connector-equivalence (EC), csp-iff-E-small-only,
finite-connector-pool-periodicity (FIN-Q⟹thm), window-purity, minimal-bad-term-floor-tightness (Lemma 9),
bad-signature-geometric-family (Lemma 6), distinctness-by-difference, realizability-and-self-dual-clutter,
term-density-and-prime-capacity, generalized-sole-connector-off-lattice, and the gap bound a_{n+1}−a_n ≤ a_1.

---

smallest-essential-prime-descent: new
Target: the whole theorem — ∃ T,L with a_{n+T}=a_n+L ∀n — via (CSP): no large prime q>P_max is load-bearing.
Technique: minimal-counterexample value-descent transplanting aimo-0030 (IMO "Ana–Banana") Claim 3, whose
  proof establishes EXACTLY a "only primes ≤ threshold are load-bearing" statement of our crux's shape.
  Dictionary: k↔P_max, "n bad"↔non-covering set T, "good"↔covering; Claim 1↔support-monotonicity (certified),
  Claim 2↔Lemma 6 (certified). Our crux ≡ aimo-0030 Claim 3: "q>P_max, T non-covering ⟹ T∪{q} non-covering."
Skeleton:
  1. Reduce to (TARGET)≡(CSP)≡(EC) — imported certified scaffold + Lemma EC.
  2. Minimal counterexample: among essential configs (T,q) [T non-covering, T∪{q} covering], minimize the
     minimal term realization n(T,q) — by the extremal principle.
  3. Coprime witness: T non-covering ⟹ a T-avoiding term B; essentiality ⟹ q∣B (Lemma EC (a)).
  4. Cofactor decomposition B=q^r·y, U:=primes(y) non-covering & essential for q (certified propagation);
     manufacture the smaller object z = minimal power/covering realization inside U.
  5. Strict descent: floor/power chain (analog of y^α<ky<py=x/p^{r-1}<n/p^{r-1}) ⟹ new config realizes < n.
  6. Minimality contradiction (or iterated Claim-3 + support-monotonicity: B a term divides the manufactured
     bad multiple, contradicting bad status). ⟹ (TARGET) ⟹ theorem.
Key lemmas (claim + mechanism):
  - (TARGET)≡CSP — because Lemma EC certifies CSP-fails ⟺ ∃ non-covering T, T∪{q} covering (q large). Imported.
  - Coprime witness q-divisible — T-avoiding term meets covering T∪{q} only via q (Lemma EC (a)). Imported.
  - Cofactor U non-covering & essential — certified essentiality propagation (Lemma 14). Imported.
  - Floor/power descent inequality [GAP] — the exponent r≥1 of q + minimality of the power bound z below
    B/q^{r-1}, in aimo-0030's y^α<ky<py=x/p^{r-1}<n/p^{r-1} shape; term-value analog of "x<n" is certified
    floor-tightness m_0<a_1·p, used as an INTERNAL lemma (not the outer induction variable — the outer
    variable is n(T,q), value-indexed; branch onto prime q' inside U for the prime-indexed inversion).
Open gaps: (A) define z; (B) crux-equivalent strict descent inequality n(new)<n(T,q); (C) closure.
Cases to cover: r=1 vs r≥2; U contains another large prime q' (descend on q', prime-indexed branch);
  z<a_1 termination (support becomes small-prime-only = covering = contradiction, the base case).
Watch out for: GAP B must NOT collapse into horizontal propagation (Lemma 14 preserves q, no descent) — the
  cofactor POWER and exponent r must produce a STRICTLY smaller, genuinely changed object; if GAP B reduces
  verbatim to "no minimal covering set with a large prime realizes ≥ a_1" the lane has re-hit the wall (flag
  honestly), but the descent OBJECT is genuinely untried so collapse is not automatic.

---

greedy-successor-jump-monovariant: new
Target: the whole theorem, via (CSP)≡(FIN-Q), using the greedy successor rule as the engine.
Technique: min-of-a-failing-set PROCESS POTENTIAL with a FREEZE/JUMP phase dichotomy (aimo-0678 / IMO 2015
  SL N4 transplant), contradiction against the certified gap bound a_{n+1}−a_n ≤ a_1. Uses the greedy SMALLEST
  choice (only Window Purity does, and only passively) as an active per-step constraint — far from all four
  static faces.
Skeleton:
  1. Import scaffold + gap bound + Window Purity; suffices to prove (FIN-Q).
  2. Assume ¬(FIN-Q): distinct large primes q_1<q_2<… each first activate at indices n_1<n_2<…
  3. Define process potential Φ_n (candidate: least small-prime-compatible integer >a_n) and split steps into
     FREEZE (small-compatible successor) vs JUMP (a new large prime forced load-bearing in-window).
  4. Jump inequality: at n_k the color only q_k re-hits forces the in-window successor onto a q_k-multiple;
     q_k>a_1 multiples are >a_1 apart (certified distinctness-by-difference) ⟹ either a smaller prime already
     covers the color (q_k redundant, contradiction) or the least compatible integer exceeds a_{n_k}+a_1
     (contradicts the gap bound).
  5. Aggregate: FREEZE cannot replenish what a JUMP consumes ⟹ finitely many jumps ⟹ (FIN-Q) ⟹ theorem.
Key lemmas (claim + mechanism):
  - Gap bound ≤ a_1 — a_1 shares a prime with every term, so an a_1-multiple offset is always eligible in one
    window. Certified.
  - Large-prime spacing — q>window divides ≤1 integer per length-q window; certified distinctness-by-difference,
    used ONLY as the local spacing fact (NOT as a confinement closer — (R2′) barred that).
  - Jump forces overflow OR redundancy [GAP] — essential q_k is the sole connector to a color, so an in-window
    color-hitting successor must be a q_k-multiple, but consecutive q_k-multiples are q_k>a_1 apart.
  - Finitely many jumps ⟹ periodicity — finite-connector-pool-periodicity. Certified.
Open gaps: (1) construct Φ with a clean bounded/monotone FREEZE/JUMP dichotomy (aimo-0678 w_n analog — its
  invariant sum s_n has NO ready-made analog, this is the design gap); (2) crux-equivalent jump inequality;
  (3) aggregate finitely-many-jumps.
Cases to cover: q_k∈(P_max,a_1] vs q_k>a_1 (spacing bites only for q_k>a_1); phase alignment (a q_k-multiple
  may land in-window for special n — handle ALL n); witnesses a_i∈W(r_0) NOT confined off the a_1-lattice.
Watch out for: do NOT degrade GAP 2 into the per-window OCCUPANCY count (Lemma B bounds a rate not a total,
  certified insufficient) — the escape is the per-STEP existence constraint from greedy minimality, not a
  statistic; do NOT reintroduce bounded-value-band confinement (R2′ vacuous). If Φ has no monotone form the
  phase split is cosmetic — flag honestly.

---

covering-small-part-descent: advance (with a CONCRETE NEW descent variable — NOT a bare re-advance)
Target: the whole theorem via (CSP)/(EC); this is the sole live carrier of the value mechanism.
NEW descent variable (the reframe, required because EC propagation preserves q with no monovariant):
  ITERATED floor-tightness on the HUB VALUE along the ¬(FIN-Q) class-graph walk. Lemma 9 (minimal-bad-term-
  floor-tightness) has only ever been applied ONCE, to the single global smallest bad term. New plan: model
  ¬(FIN-Q) as a revisiting walk on the finite (≤L_0-node) class-graph (round-7 framing); define v_k = the
  term value of the k-th revisited hub; apply Lemma 9's shed-a-prime step at EVERY node with a running bound
  tying v_k to a_1·(product of primes shed so far). Since the walk lives on ≤L_0 residue nodes, pigeonhole on
  the residues forces a repeat; if the iterated value bound forces v_k strictly monotone modulo the finitely
  many residues, the repeat is a contradiction (cycle with strictly-decreasing value).
Skeleton (advance the existing file):
  1. Import its certified EC recast (Lemmas 13/14) + Lemma 9 + window-purity (all certified).
  2. Set up the class-graph walk (≤L_0 nodes) for a ¬(FIN-Q) bad class r_0.
  3. Define v_k = k-th revisited hub value; apply Lemma 9 shed-step per node ⟹ running value bound. [GAP]
  4. Pigeonhole on ≤L_0 residues ⟹ repeated node; strict value monovariant ⟹ contradiction. [GAP]
Key lemmas: iterated floor-tightness — because each shed of a sheddable prime p gives m'<a_1·p and, iterated
  along the walk, ties the hub value to a_1·∏(shed primes); the finiteness of the residue node set (≤L_0)
  converts an unbounded walk into a forced repeat (pigeonhole).
Open gaps: (i) the per-node iterated value bound actually decreases (Lemma 9 gives m_0<a_1·p only at the
  GLOBAL minimum — extending it to every node needs a local minimality per node, the real gap); (ii) case A
  of Lemma 9's dichotomy (no sheddable prime: C a minimal covering set with a large prime) stalls the shed —
  must be handled by the walk structure, not a single shed.
Cases to cover: Lemma 9 dichotomy case A (minimal cover, no shed) vs case B (sheddable, m_0<a_1·p) at each node.
Watch out for: this shares Lemma 9 as a TOOL with smallest-essential-prime-descent but differs in well-founded
  order (value-walk pigeonhole here vs prime-indexed minimal counterexample there) — keep them apart. If the
  per-node bound cannot be made to strictly decrease (case A recurs), this advance stalls at the same a_1
  threshold — the reviewer should weigh whether the two NEW lanes (prime-descent, jump-monovariant) carry more
  novelty and this advance is the conservative hedge.

---

Field summary for the outline-reviewer: 2 genuinely-new framings satisfying the shared-gap mandate
(smallest-essential-prime-descent = prime/value minimal-counterexample descent, aimo-0030; greedy-successor-
jump-monovariant = process potential vs gap bound, aimo-0678) + 1 advance with a concrete new descent variable
(covering-small-part-descent, iterated-hub-value walk). All three keep explicit crux-equivalent gaps and are
far apart in mechanism (constructive value descent / dynamical process monovariant / graph-walk pigeonhole).
Recommend building all three; if slot-limited, prioritize the two NEW lanes.
