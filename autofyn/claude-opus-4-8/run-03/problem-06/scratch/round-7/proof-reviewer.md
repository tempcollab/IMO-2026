# Proof-reviewer report — imo-2026-06, round 7

Problem is `proof_only` (no numeric answer to verify). Goal: prove eventual arithmetic-periodicity of
the greedy gcd sequence. Whole problem stays at Status **partial** — no solve flip. All three builders
recorded honest partial/negative Status; no overclaim detected in any file.

Numeric recheck (a_1∈{15,35,99,231}, 200 terms): 0 Window-Purity violations, 0 bad terms (CSP holds
empirically). Consistent with all prior rounds.

---

## 1. window-purity-class-cycle — VERDICT: CHANGES REQUESTED (Status: partial)

Scores — Correctness 10/10, Completeness 6/10 (honest GAP), Progress: real (crux strictly weakened).

Two load-bearing lemmas re-derived independently and confirmed gap-free:

- **Window Purity** (Lemma 1). x with a_n<x<a_{n+1}: if x∈E_∞ then x≥a_1 so x is a term (ENUM), but no
  term lies strictly between consecutive terms — contradiction. Non-covering: if S(x) covering then x
  shares a small prime with every a_i, so x∈E_∞. Trivial and correct. **CERTIFIED** (`window-purity.md`).

- **(FIN-Q)⟹theorem** (Lemma 2). Re-derived: under (FIN-Q), Q_rel=⋃Q(r) is a finite union of finite sets,
  hence finite; M=L_0·∏Q_rel. Via the certified dichotomy (★), membership in each class is: covering →
  always in; miss → always out; r∈R'_bad → an infinite conjunction over the fixed index set W(r) of
  conditions "∃q∈Q_i⊆Q_rel: q|m", each depending only on m mod M — so the conjunction depends only on m
  mod M. The infinite-conjunction step is valid (fixed index set, each conjunct a function of m mod M).
  Genuinely weaker hypothesis than (FIN-W) (W(r) may be infinite with Q(r) finite). **CERTIFIED**
  (`finite-connector-pool-periodicity.md`) — strengthens/supersedes `finite-witness-periodicity.md`.

**GAP (honest, correctly marked):** ¬(FIN-Q) (an inhabited bad class with infinitely many *distinct* large
connectors) is modelled as a revisiting walk on a finite ≤L_0-node class-graph, but the Step-5 descent
(5a strict prime descent per revisit / 5b first-hole over-constraint) is NOT produced. The builder is
explicit that the material assembled shows *ascent* (distinct q_k→∞), not descent, and refuses to assert a
monovariant from the q* floor — correct restraint. Step 3(a)-(c) contain no false claim presented as
proved; the "iterate the walk" in 3(b) is loose but inside the flagged gap. No dead-route reuse.

Real progress: first strict weakening of the wall since round 5 (FIN-W→FIN-Q). Builder's recorded Status
(partial) is accurate.

## 2. covering-small-part-descent — VERDICT: CHANGES REQUESTED (Status: partial)

Scores — Correctness 10/10, Completeness 6/10 (honest GAP at (6b)), Progress: real (2 lemmas + descent).

- **Lemma 7 (Window Purity)** — same as above, certified once.
- **Lemma 8 (Local Hub-Cover finite-capacity).** Re-derived: primes(h)=S(h)⊔Q(h); h a term ⇒ primes(h)
  covering (REAL 𝒯⊆𝒞); for B∈W(h), primes(B)∩S(h)=∅ forces primes(B)∩primes(h)=primes(B)∩Q(h)≠∅. Correct;
  pigeonhole for infinite W(h) is valid (Q(h) finite). LOCAL (one hub), NOT the dead global Σ1/p². **CERTIFIED**
  (`local-hub-cover.md`).
- **Lemma 9 (Minimal-bad-term descent).** Re-derived (i): v_p(m_0)≥2 ⇒ m'=m_0/p has primes(m')=C covering,
  S(m')=S(m_0) non-covering; if m'≥a_1 it is a term (REAL clause c), bad, <m_0 — contradiction; so m_0<a_1·p.
  (ii) redundant prime: primes(m')=C∖{p} covering, S(m')⊆S(m_0) still missed by the same witness B — bad;
  same conclusion. Both correct. m'>1 holds since |C|≥2. **CERTIFIED** (jointly with lex-rewrite Lemma X as
  `minimal-bad-term-floor-tightness.md`).

**GAP (honest, correctly marked):** (6b) unclosed — the descent is blocked exactly at the a_1 threshold
(REAL clause (c) certifies m' a term only when m'≥a_1; Prop D permits reduced value <a_1). Lemmas 7,8 do
not supply the value inequality tying a_1 to the covering structure. Builder is precise about the stall
point and bars the proven-dead closures. Status (partial) accurate.

## 3. lex-rewrite-descent — VERDICT: RETHINK (Status: unsolved as a route)

Scores — Correctness 9/10 (negative finding rigorous), Completeness n/a (route dead), Progress: pruning +
salvaged lemma.

The builder self-certifies the designed active-rewrite operator does NOT exist, and the negative finding
is rigorous:
- §1(a): the operator's success condition "produce a small-disjoint pair sharing a prime in (P_max,q*)" is
  *verbatim* the negation of q*'s minimality (certified Lemma A) — equal in strength to the theorem, a
  restatement not a reduction. Correct (definitional).
- §1(b): the covering-preserving exchange A→A·s/q needs one small prime s covering q's entire witness set
  and missing B; whether such s exists is a global covering question that the certified Prop D barrier
  permits to FAIL. So no local covering-combinatorial operator exists. Valid barrier argument.

Per my standing role rule (an approach that self-certifies its framing cannot close the crux → RETHINK,
salvage byproducts): the direct (q*,k) constructive rewrite is a dead route; sends back to the outliner.
Builder marked partial; I override the *route* to RETHINK/unsolved-as-route. **SALVAGE: Lemma X**
(minimal-bad-term floor-tightness) is correct (dichotomy (A)/(B); identical core to Lemma 9) and CERTIFIED.
§3 (aimo-0009 fallback) correctly reports no transplant — no dead-route claim, no progress.

---

## Lemmas certified this round (4)
- `lemmas/window-purity.md` — every interior integer of a gap is ∉E_∞ / non-covering. (both builders)
- `lemmas/local-hub-cover.md` — bad hub's finite Q(h) covers every color S(h) misses.
- `lemmas/finite-connector-pool-periodicity.md` — (FIN-Q)⟹theorem; strictly weakens/supersedes (FIN-W).
- `lemmas/minimal-bad-term-floor-tightness.md` — v_p(m_0)≥2 or redundant p ⇒ m_0<a_1·p. (Lemma 9 = Lemma X)

No lemma rejected. No overclaim found.

## Goal Progress
Ranking snapshot (Elo, post-outcome): covering-small-part-descent **1627** (top of built set),
window-purity-class-cycle **1568** (NEW, strong debut), lex-rewrite-descent **1483** (dead-end).
reduced-process-identity (~1630, parked) and enum-covering-primes remain in the field.

What advanced: the shared wall was **strictly weakened for the first time since round 5** —
(FIN-W)→(FIN-Q). Single-prime / finite-pool infinite witnessing is now provably harmless (certified), so
the sole surviving obstruction is an inhabited bad class with infinitely many *distinct* large connectors
(¬(FIN-Q)) — a revisiting walk on a finite class-graph. New local greedy levers (Window Purity, Local
Hub-Cover) and a downward value constraint (floor-tightness) are on the table but have not yet produced
the closing value/dynamics inequality. One route pruned (direct (q*,k) rewrite — do not re-field).
Status remains **partial**.
