## Status
solved

## Full proof

**Solved round 10** by approach `smallest-essential-prime-descent` (proof-reviewer APPROVE). The
10-round "no large prime > P_max is load-bearing" wall is bypassed: instead of the P_max/covering
framing, one works directly with the cruder notion "small prime := prime ≤ a_1" and transplants the
recursive good/bad calculus + minimal-pair descent of the aimo-0030 game. Every step was independently
re-derived and numerically confirmed (0 counterexamples for a_1 ∈ {15,16,17,30,35,45,99,100,210,231}).

Let a_1<a_2<… be the greedy sequence and E_∞ = {m>1 : gcd(m,a_i)>1 ∀i≥1}. Two certified imports:
**(ENUM)** [`lemmas/enumeration-of-E-infinity.md`] {a_n}=E_∞∩[a_1,∞), enumerated increasingly; **(PER)**
[`lemmas/periodic-set-enumeration.md`] if E_∞ is tail-periodic from a_1 with period L>0 then a_{n+T}=a_n+L
for all n, with T=#(E_∞∩[a_1,a_1+L))≥1. So it suffices to prove E_∞ tail-periodic from a_1.

For m≥a_1 call m **good** if m∈E_∞ (= a term, by ENUM), else **bad**. A **move** m→x: gcd(m,x)=1,
a_1≤x<m. Small prime := ≤a_1; a,b≥a_1 are **similar** if they share the same primes ≤a_1. M:=∏_{p≤a_1}p≥2.

**F2** goods pairwise non-coprime (a_j chosen with gcd(a_j,a_i)>1, i<j). **F3** a_1 good.
**F1** m good ⟺ no good x∈[a_1,m) is coprime to m (⟹ by F2; ⟸ if m>a_1, goods <m are {a_1,…,a_j},
hypothesis gives gcd(m,a_l)>1 ∀l≤j, so the rule forces a_{j+1}≤m and maximality of a_j forces a_{j+1}=m).

**Claim 1** n good, n∣n', n'≥a_1 ⟹ n' good (else move n'→x good, gcd(x,n)=1: x,n coprime goods, contra F2).
**Claim 2** rs≥a_1 bad ⟹ r²s bad (same prime set, transplant the move); contrapositive r²s good ⟹ rs good.
**Claim 3** n≥a_1 bad, p>a_1 prime ⟹ np bad. Minimal counterexample (p,n): move n→x good, gcd(x,n)=1,
a_1≤x<n. gcd(x,p)=1 would give move np→x (np bad, contra), so p∣x, x=p^r y (p∤y). If y=1, x=p^r>a_1
coprime to a_1 gives move x→a_1 ⟹ x bad, contra; so y≥2. Let α least with y^α≥a_1 (y^{α-1}<a_1). y^α is
bad (gcd(y^α,np)=1 ⟹ coprime goods contra F2). Descent y^α=y·y^{α-1}<y·a_1≤y·p, ×p^{r-1}: p^{r-1}y^α<p^r
y=x<n. By minimality Claim 3 holds below n; induction j=0..r gives p^r y^α bad. But x=p^r y ∣ p^r y^α ⟹
(Claim 1) p^r y^α good — contradiction.

**Main claim** similar a,b same status. Reduce to (★): c≥a_1, d a multiple of c similar to c ⟹ same status
(apply to (a,ab),(b,ab)). Minimal counterexample (c_0,d_0): Claim 1 ⟹ c_0 bad, d_0 good, d_0≥2c_0. Pick
p∣(d_0/c_0); then d_0/p=c_0u is a multiple of c_0 similar to c_0 with d_0/p<d_0. If p≤a_1: p∣c_0 (similar)
and p∣d_0/c_0 ⟹ p²∣d_0, contrapositive of Claim 2 (r=p,s=d_0/p²) ⟹ d_0/p good. If p>a_1: n=d_0/p≥a_1,
np=d_0 good ⟹ (Claim 3) n good. Either way (c_0,d_0/p) is a smaller counterexample — contradiction.

**Conclusion.** For n≥a_1, n and n+M share the same primes ≤a_1, so are similar; Main claim ⟹
n∈E_∞ ⟺ n+M∈E_∞. Thus E_∞ is tail-periodic from a_1 with period L=M; (ENUM)+(PER) give a_{n+T}=a_n+L for
every n≥1 with T=#(E_∞∩[a_1,a_1+M))≥1 and L=M>0. ∎

Full write-up: `approaches/smallest-essential-prime-descent.md`. Terminal lemma certified:
`lemmas/recursive-good-bad-and-similarity-closure.md`.

## Status (history)
partial

## Approaches tried
- **enum-covering-primes** (round 1) — Rigorous reduction: sequence = increasing enumeration of E_∞ ∩ [a_1,∞); E_∞ periodic ⇒ conclusion for every n. Crux isolated to **Lemma A**: for no prime q > P_max (largest prime factor of a_1) do two terms have prime-intersection exactly {q}. Verified numerically, UNPROVEN. Status: partial (advanced).
- **density-bounded-recruitment** (round 1) — Same reduction+endgame, fully proved. Crux isolated to the **Structural Lemma**: every two terms share a prime factor ≤ a_1 (colors pairwise intersecting). Verified numerically, UNPROVEN. Correctly recorded a dead end: the asymptotic "only finitely many primes divide infinitely many terms" is FALSE (E_∞ periodic ⇒ each prime meets it in positive density), so pure density cannot isolate load-bearing primes. Status: partial (advanced).
- **finite-state-window** (round 1) — Same reduction; packages the endgame as a finite-state map. Crux isolated to **G1'**: R₀ = {primes ≤ maxfactor(a_1)} is a sufficient prime set. Verified numerically, UNPROVEN. Correctly disproved the earlier guess R ⊆ P∪{2,3} (a_1=99 recruits 5). Status: partial (advanced).

All three converge on ONE genuine crux — **no prime larger than the largest prime factor of a_1 is ever load-bearing** — phrased three equivalent ways. That crux is the real difficulty of P6 and remains an honest open gap.

- **reduced-process-identity** (round 2) — Static process-coincidence framing. Rigorously built the reduced set E* = {m>1 : m shares a prime ≤ P_max with every term}, proved it exactly periodic mod L_0 = ∏_{p≤P_max}p, contained in E_∞, containing a_1 and every multiple of a_1; hence theorem ⟸ **(SL): E_∞∩[a_1,∞) ⊆ E\*** (every two terms share a small prime), with explicit L = L_0, T = #(E*∩[a_1,a_1+L_0)). E* periodicity + reduction-to-inclusion are gap-free (certified this round). (SL) is the honest gap = the standing crux. Minor imprecision: the note "(SL) ⟺ Lemma A" only has the (SL)⟹Lemma A direction rigorous; (SL) may be formally stronger. Status: partial (CHANGES REQUESTED).
- **cofactor-recruitment-smoothness** (round 2) — Dynamic recruitment/cofactor framing. NEW certified **Prop C** (lemmas/sole-connector-off-lattice.md): a term whose only shared prime with another term is q ∉ P is never a multiple of a_1 — a positive constraint confining any large-prime witness to a length-<a_1 window. **Prop D** (barrier, correct as stated): the covering+intersection structure of F alone does not forbid a large minimal member, so any proof must use greedy dynamics — accepted as covering-axiom-insufficiency (its stronger "all proofs need dynamics" reading is heuristic, not a theorem). Residual = **Gap G** (cofactor smoothness of the greedy witness) = the crux. Status: partial (CHANGES REQUESTED, recorded advanced).
- **large-prime-capacity-counting** (round 2) — Global prime-capacity double-counting. NEW certified **Lemmas C1–C3** (lemmas/term-density-and-prime-capacity.md): N(X)=Θ(X); per-prime pair capacity C(⌊X/p⌋,2); large pairs ≤ (X²/2)·Σ_{p>P_max}1/p² < 0.21·X²/2 (constant verified: P(2)−1/4 = 0.2022). But the approach **self-certifies that this framing CANNOT close the crux**: capacity bounds only a positive FRACTION of pairs (never zero), and "R infinite" forces only o(X²) large-sole pairs, so the localize-to-globalize step needs a circular periodicity input. Solving route is a proven dead-end. Status: unsolved as a route (RETHINK) — but the counting lemmas + negative certification are valuable pruning.

**Round 2 net:** no approach closed the crux; the field still shares ONE wall. New rigorous byproducts: Prop C (positive lattice constraint), capacity Lemmas C1–C3 + a negative certification (capacity counting is dead), Prop D (set-level barrier ⇒ dynamics required), and the E* periodicity/reduction repackaging. The capacity framing is now provably incapable; the live routes are the two local/minimality framings (reduced-process-identity, cofactor-recruitment-smoothness), both bottoming out on the same greedy-minimality statement.

- **covering-small-part-descent** (round 4, NEW) — Value well-ordering / infinite-ascent framing. Rigorously and self-containedly proved: (i) **(CSP) ⇒ theorem** without the (SL) intermediary (certified `lemmas/csp-implies-theorem.md`); (ii) base case |P|=1; (iii) **bad-partner lemma** — every bad term has a *bad* partner sharing only large primes, both off-lattice (certified `lemmas/bad-partner-and-ascent.md`); (iv) **ascent** — the smallest bad term has a strictly larger bad partner. Honest GAP: Step 6→7, upgrading the single ascent step (the partner relation is *symmetric*, so it need not yield an infinite chain) into an unbounded family AND extracting a contradiction. Reviewer: CHANGES REQUESTED / partial (advanced). This is the value-ordering carrier of the crux — a genuinely different framing from the induction route.
- **reduced-process-identity** (round 4, advance) — Patched the reviewer-flagged (SL)⟸ multi-large-prime gap: proved **generalized Prop C (GPC)** in full (certified `lemmas/generalized-sole-connector-off-lattice.md`), retiring the strictly-weaker singleton "Lemma A"; target correctly (SL)⟺(CSP). Reframed the inductive step as **redundancy (RED_n)** (S_{n+1} covers the predecessor list), correcting the FALSE "a_{n+1} is P_max-smooth" (237=3·79 is good for a_1=231). Honest GAP: (RED_n), the crux, in reverse-inequality/induction form. Reviewer: CHANGES REQUESTED / partial (advanced — the (SL)⟸ gap is now closed).
- **self-dual-clutter-grading** (round 4, NEW) — Clutter/blocker-duality + value-grading framing. Rigorously proved (all certified): **realizability 𝒞=𝒯** (every covering set is a term prime-set), **self-dual clutter b(ℰ)=ℰ**, **(CSP)⟺H_s covering-dense**, every-term-meets-P, base case |P|=1, GPC (`lemmas/realizability-and-self-dual-clutter.md`, `lemmas/generalized-sole-connector-off-lattice.md`). But the builder **self-certifies** that its distinctive Step-4 grading lever does NOT close the crux — it collapses to exactly covering-small-part-descent's open Step 6→7. Reviewer: **RETHINK** / unsolved-as-route (no distinct gap for this builder to close; its reformulation lemmas are salvaged into the cache). Keep as a reformulation, not a live solve route.

- **covering-small-part-descent** (round 5, ADVANCE) — Closed sub-step **(6a)** rigorously via
  **Lemma 6 (bad-signature geometric family)**: if m is bad then m·r^k (r∣m, k≥0) is a bad term with
  the SAME small part S(m) and SAME witness, so one bad term forces an unbounded family. Reviewer
  re-derived it independently from the certified Realizability clause (c) (every integer ≥a_1 whose
  prime set contains a covering set is a term) — CORRECT and gap-free; CERTIFIED as
  `lemmas/bad-signature-geometric-family.md`. Caveat: the family is a single fixed-signature orbit
  (density →0), so it does not feed the dead global count; the substantive crux **(6b)** (value-level
  contradiction) is entirely untouched. Reviewer: CHANGES REQUESTED / partial (advanced — (6a) closed).
- **bad-residue-witness-index** (round 5, NEW) — Residue-class reformulation. **NEW gap-free Reduction
  Lemma:** the theorem follows from **(FIN-W)** — every term is small-disjoint from only finitely many
  terms — via DIRECT periodicity of E_∞ mod M=L_0·∏Q_rel, WITHOUT routing through (CSP). Reviewer
  verified the three-case residue-determination argument end to end; genuinely WEAKENS the crux
  ((CSP)⟹(FIN-W)⟹theorem, (FIN-W) strictly weaker). CERTIFIED as `lemmas/finite-witness-periodicity.md`.
  Honest GAP: (FIN-W) itself — pigeonhole reduces its failure to a "star configuration" (one term
  small-disjoint from an infinite family all divisible by one fixed large prime, one residue class mod
  L_0), not contradicted = the standing wall relocated. Reviewer: CHANGES REQUESTED / partial (advanced).
- **minimal-linking-prime-extremal** (round 5, NEW) — Extremal principle on the minimal linking prime
  q* + local per-window count. Steps 1–4 correct (imported certified + elementary): q* floors every
  large link (non-symmetric handle), per-window spacing cap ≤ a_1/q*+1. Both CERTIFIED (modest) as
  `lemmas/minimal-linking-prime-and-window-cap.md`. Correctly DROPPED the round-4 false "finitely-many-
  windows-collide-with-single-ascent" closure. Honest GAP: **(DESC)** (a bad window forces a
  smaller-index bad window) — difficulty-equivalent to (CSP), no descent produced (all three natural
  descents relocate the 6a wall). No gap closed. Reviewer: CHANGES REQUESTED / partial (no advance).

**Round 5 net:** no solve flip; substantive crux is now uniformly **(6b) / (FIN-W)-infinite branch /
(DESC)** — three faces of the SAME wall: *an unbounded fixed-signature / star / bad-window family is
not by itself a contradiction*. Real progress: (6a) unconditionally closed (Lemma 6); crux strictly
weakened (CSP)→(FIN-W) (Reduction Lemma, gap-free). 3 lemmas certified. The field has converged to one
object again (single recurring bad configuration with no lower pressure). Per the diversity mandate,
next round should seed ≥1 framing attacking the greedy DYNAMICS of the actual successor a_{n+1}
(window-minimality — how a_{n+1} is CHOSEN), the one surface no live approach exploits.

- **window-purity-class-cycle** (round 7, NEW — mandated greedy-dynamics route). Two NEW certified
  lemmas + a STRICT weakening of the wall. (i) **Window Purity** (certified `lemmas/window-purity.md`):
  every integer strictly between consecutive terms is ∉E_∞, hence has non-covering small part — a local
  greedy-value handle (Prop-D-compliant), gap-free from ENUM. (ii) **(FIN-Q)⟹theorem** (certified
  `lemmas/finite-connector-pool-periodicity.md`): periodicity holds as soon as every inhabited bad class
  r has a FINITE large-connector pool Q(r)=⋃_{i∈W(r)}Q_i — *even if W(r) is infinite*. Strictly weaker
  hypothesis than the certified (FIN-W); rigorises "single-sided infinite witnessing is harmless" (an
  infinite conjunction of conditions each depending on m mod M is a function of m mod M). Reviewer
  re-derived both; gap-free. Honest GAP: **¬(FIN-Q)** (an inhabited bad class with infinitely many
  DISTINCT large connectors) modelled as an infinite revisiting walk on a finite (≤L_0-node) class-graph;
  the Step-5 descent (5a strict-prime-descent-per-revisit / 5b first-hole over-constraint) is NOT
  extracted. Reviewer: CHANGES REQUESTED / partial (advanced — 2 lemmas + crux weakened FIN-W→FIN-Q).
- **covering-small-part-descent** (round 7, ADVANCE — attacked (6b)). Three gap-free items, two newly
  certified: **Lemma 7 = Window Purity** (same as above, `lemmas/window-purity.md`); **Lemma 8 = Local
  Hub-Cover finite-capacity** (certified `lemmas/local-hub-cover.md`): for a bad term h, its finitely
  many large primes Q(h) jointly cover every color S(h) misses (W(h)⊆⋃_{q∈Q(h)}{B:q|B}) — a LOCAL
  capacity fact on one hub, distinct from the dead global Σ1/p²; **Lemma 9 = Minimal-bad-term descent**
  (certified as `lemmas/minimal-bad-term-floor-tightness.md`, jointly with lex-rewrite's Lemma X):
  v_p(m_0)≥2 ⟹ m_0<a_1·p, same for a redundant prime — a genuine DOWNWARD constraint. Honest GAP: (6b)
  unclosed — the descent is blocked exactly at the a_1 threshold; Lemmas 7,8 supply no value inequality
  tying a_1 to the covering structure. Reviewer: CHANGES REQUESTED / partial (advanced — 2 lemmas + a
  descent-structure lemma; crux sharpened to "no minimal covering set with a large prime realizes ≥a_1").
- **lex-rewrite-descent** (round 7, NEW — aimo-0960 active-rewrite transplant). **Route PROVEN DEAD as
  framed** (self-certified, reviewer confirmed rigorous). The designed (q*,k)-lowering operator does not
  exist: §1(a) producing a link in (P_max,q*) is *verbatim* the negation of q*-minimality (equal in
  strength to the theorem, circular, not a reduction); §1(b) the covering-preserving exchange A→A·s/q
  needs one small prime covering q's entire witness set, which Prop D permits to fail — no local
  covering-combinatorial operator exists. SALVAGE: **Lemma X (minimal-bad-term floor-tightness)** = the
  same fact as covering-small-part-descent's Lemma 9, certified. Reviewer: **RETHINK** / unsolved-as-route
  (no gap for this builder to close — the framing self-certifies it cannot); Lemma X salvaged into cache.

**Round 7 net:** no solve flip; the shared wall persists but is **strictly weakened** for the first time
since round 5 — the crux goes (FIN-W)→(FIN-Q): single-prime / finite-pool infinite witnessing is now
provably harmless, so the ONLY surviving obstruction is an inhabited bad class drawing on *infinitely many
distinct* large connector primes (¬(FIN-Q)) — modelled as a revisiting walk on a finite class-graph, its
descent step open. 4 lemmas certified (Window Purity, Local Hub-Cover, (FIN-Q)⟹theorem, minimal-bad-term
floor-tightness). One route pruned (direct (q*,k) rewrite is dead — do not re-field). The dynamics surface
(Window Purity) is now on the table but has not yet produced the closing value inequality.

- **covering-small-part-descent** (round 9, ADVANCE — CHANGES REQUESTED / partial). Two NEW gap-free
  equivalence/structure lemmas recasting the crux in a term-*divisibility* face, all reviewer re-derived and
  certified: **Lemma 10 = (CSP) ⟺ ℰ-small-only** (certified canonical `lemmas/csp-iff-E-small-only.md`,
  crediting the independent `minimal-cover-small-only` Lemma D); **Lemma 13 = essential-connector equivalence
  + Lemma 14 = essentiality propagation** (certified `lemmas/essential-connector-equivalence.md`): CSP fails
  ⟺ some large prime q is an *essential connector* for a non-covering A (every A-avoiding term divisible by q
  ⟺ A non-covering, A∪{q} covering), and in any such config (A,q) essentiality propagates to (primes(B)∖{q},q)
  with **q preserved**; Lemma 12 spawning certified as `lemmas/intersecting-clutter-and-spawning.md`. Honest
  GAP unchanged in kind: (EC) = ℰ-small-only = CSP; propagation gives NO downward monovariant (q recurs), so
  the value/essential-witness mechanism stalls at the same wall. Reviewer: CHANGES REQUESTED / partial
  (advanced — 3 new certified lemmas; crux recast to the crisp arithmetic (EC), not closed). Minor imprecision
  flagged: Lemma 11's "Case II genuine" is illustrated by a large-prime-FREE minimal cover ({2,3} for a_1=15),
  so it does not exhibit a large-prime edge with rad<a_1; Lemma 11 NOT certified (pruning note only).
- **minimal-cover-small-only** (round 9, NEW — RETHINK / unsolved-as-route). Rigorous and honest, but
  **self-certifies no distinct closing route**: its NEW **Lemma D** proves the pure-transversal target
  ℰ-small-only is *literally equivalent* to (CSP) (same statement as covering-small-part-descent's Lemma 10;
  certified jointly as `lemmas/csp-iff-E-small-only.md`), and the builder proves its only distinctive lever —
  the essential-witness partner map C↦C' — is **horizontal** (C∩C'={q} keeps the SAME large prime q∈C'), so it
  supplies no strictly-decreasing quantity on the large-prime data (max large prime, |Q_C|, ∏Q_C, min/max all
  non-decreased). Base case |P|=1 (a_1 a prime power) fully proved via the transversal mechanism (certified
  Lemmas A,B,C in `lemmas/intersecting-clutter-and-spawning.md`). Per the single-gap-trap rule (cf. round-4
  self-dual-clutter-grading), routed RETHINK: the transversal framing adds no closing route beyond CSP; its
  byproduct lemmas (A intersecting-clutter, B essential-witness, C/12 spawning, D equivalence) are salvaged into
  the cache. Reviewer: RETHINK / unsolved-as-route.
- **bounded-window-distinctness** (round 9, RE-ATTACK — RETHINK / unsolved-as-route). The requested abstract
  step-4 argument was executed and **decides the route in the negative**: NEW gap-free **(R2′)** proves the
  distinctness engine's needed confinement (new-large-prime-carrying witnesses in a bounded value-band) is
  *equivalent* to Q(r_0) being finite — so distinctness can only bite where ¬(FIN-Q) is already false; the
  bound is local and O(N), never global. This is a rigorous impossibility argument for the closer, not merely
  "unverified". SALVAGE: the true reusable **Distinctness-by-Difference** local lemma (certified
  `lemmas/distinctness-by-difference.md`). Reviewer: RETHINK / unsolved-as-route (value-difference counting
  barred against ¬(FIN-Q), same wall as global Σ1/p² and Prop D).

**Round 9 net:** no solve flip; **no new closing lever** — the field is exhausting reformulations of the ONE
wall (CSP = ℰ-small-only = (EC) = ¬(FIN-Q)). Real progress is bookkeeping/pinning: the equivalence
(CSP)⟺ℰ-small-only is now certified (proved independently by two lanes), and the crux gained a crisp
term-divisibility face (EC) with a self-reproducing (q-preserving) propagation structure. 4 lemmas certified
(csp-iff-E-small-only, essential-connector-equivalence, intersecting-clutter-and-spawning,
distinctness-by-difference). TWO of three built approaches routed RETHINK (both self-certified their
distinctive lever cannot close the crux: transversal monovariant is horizontal; value-difference confinement
is vacuous). This is the 4th+ collapse to one wall — per the CLAUDE.md shared-gap rule the next round MUST
field ≥1 approach from a genuinely different framing (NOT another CSP/ℰ/EC/FIN-Q reformulation); the missing
ingredient remains a *value/dynamics lower-pressure* inequality tying a_1 to the covering structure, which no
static-covering reformulation has produced. covering-small-part-descent stays the live carrier of the value
mechanism (EC form) but must find a genuinely new descent variable or be reframed.

**Round 4 net:** no solve flip; crux (CSP)/(SL) still open, shared wall unbroken. But real progress: the reviewer-flagged (SL)⟸ multi-large-prime gap is CLOSED (GPC certified), and the crux is now recast in a genuinely new **value-ascent** framing (covering-small-part-descent) with a proven ascent engine (bad-partner + smallest-bad-term step), reducing the whole crux to: *derive a contradiction from an infinite strictly ascending, large-prime-linked chain of off-lattice bad terms* (Step 6→7 = 6a unbounded family + 6b contradiction). 5 new certified lemmas: GPC, CSP⇒theorem (order-free), realizability 𝒞=𝒯, self-dual clutter, bad-partner+ascent. The clutter-grading framing is proven (by its own builder) to add no distinct route beyond the descent gap.

## Current best
The whole problem is rigorously reduced to a single finiteness statement, and the endgame is fully proved (reviewer-verified, computationally confirmed):

1. **Enumeration reduction** (certified, lemmas/enumeration-of-E-infinity.md): the greedy sequence is exactly the increasing enumeration of E_∞ ∩ [a_1,∞), where E_∞ = {m>1 : gcd(m,a_i)>1 ∀i}. Removes all order/history dependence.
2. **Periodic-set enumeration** (certified, lemmas/periodic-set-enumeration.md): if E_∞ is tail-periodic from a_1 with period L, then a_{n+T}=a_n+L for EVERY n with T = #(E_∞ ∩ [a_1,a_1+L)). Both T,L positive.
3. **Covering / finite-state periodicity**: if the set R of relevant primes is finite (equivalently: every two terms share a small prime / no large prime is a unique connector / R₀ is sufficient), then E_∞ is a union of residue classes mod L = ∏R, hence periodic, and (1)+(2) give the theorem.

The SOLE remaining gap, common to all approaches: **the relevant-prime set is finite** — no prime exceeding the largest prime factor of a_1 is ever load-bearing. Verified with zero counterexamples on 20+ seeds (round-4 recheck: a_1∈{15,35,99,231,1155}, CSP holds, no bad terms); not yet proved. Bounded-gap fact a_{n+1}-a_n ≤ a_1 also proved.

**Sharpest form of the crux (round 5).** Sub-gap **(6a) is CLOSED** (Lemma 6, certified): a single bad
term forces an unbounded fixed-signature family of bad terms unconditionally. The whole remaining crux
is now the single value-level statement, appearing in three certified-equivalent faces:
- **(6b)** [covering-small-part-descent]: derive a contradiction from an unbounded family of bad terms.
- **(FIN-W) infinite branch** [bad-residue-witness-index]: rule out a "star" — one term small-disjoint
  from infinitely many terms all divisible by one fixed large prime in one residue class mod L_0.
- **(DESC)** [minimal-linking-prime-extremal]: a bad window forces a smaller-index bad window.
All three are difficulty-equivalent and unproved. The proven-dead closures stay barred: global Σ1/p²
capacity (bounds a positive fraction, never zero) and pure covering/Helly (Prop D barrier). GPC confines
every bad term off the a_1-lattice; the missing ingredient is *lower pressure* (a value/dynamics inequality
a minimal bad realizer cannot satisfy), which no static-E_∞ framing has supplied.

**Certified this round:** GPC (multi-large-prime off-lattice), CSP⇒theorem (order-free reduction), realizability 𝒞=𝒯, self-dual clutter b(ℰ)=ℰ, bad-partner+ascent. Next round should attack (6a)/(6b) — a monovariant forced to increase along any bad→bad step, or a localized (bounded-band) pigeonhole avoiding the dead global count. The clutter-grading framing added no distinct route; the two live carriers are the induction form (reduced-process-identity: RED_n) and the value-ascent form (covering-small-part-descent: Step 6→7).

**Sharpest form of the crux (round 7 update).** The wall is strictly weakened to **¬(FIN-Q)** (certified
`lemmas/finite-connector-pool-periodicity.md`): the ONLY way periodicity can fail is an E_∞-inhabited bad
class r_0 whose large-connector pool Q(r_0)=⋃_{i∈W(r_0)}Q_i is INFINITE — infinitely many *distinct* large
primes across its witness colors (equivalently a "refined star": a hub small-disjoint from an infinite
off-lattice family in one class mod L_0 carrying distinct unbounded large primes; the old single-prime star
is now excluded). This is a revisiting walk on a finite ≤L_0-node class-graph. New local levers on the
table: Window Purity (interior of every gap is E_∞-free), Local Hub-Cover (a hub's finite Q(h) covers all
its missed colors), minimal-bad-term floor-tightness (m_0<a_1·p downward). Missing ingredient unchanged in
kind: a value/dynamics inequality tying a_1 to the covering structure (e.g. "no minimal covering set with a
large prime realizes ≥a_1"), or a strict large-prime descent per class-graph revisit. PROVEN-DEAD closures
stay barred: global Σ1/p² capacity; pure covering/Helly (Prop D); symmetric bad-partner ascent; aimo-0016
template; AND now the direct (q*,k) active rewrite (lex-rewrite-descent §1, pruned).
