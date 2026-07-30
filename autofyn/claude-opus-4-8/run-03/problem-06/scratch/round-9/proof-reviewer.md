# Proof-reviewer report — imo-2026-06, round 9

Reviewed 3 built approaches adversarially. Re-derived every load-bearing lemma independently; numerically
confirmed (CSP)⟺ℰ-small-only via seeds a_1∈{15,35,99,231} (CSP holds, no large-prime edge). No approach
closes the P6 crux; the field is exhausting reformulations of the single wall.

## minimal-cover-small-only — RETHINK / unsolved-as-route

- **Correctness:** all lemmas valid. Lemma A (one line from certified self-dual Lemma 2), Lemma B
  (edge-minimality), Lemma C (spawning), base case |P|=1, and NEW **Lemma D** ((CSP)⟺ℰ-small-only) all
  re-derived and correct. (II)⟹(I) via Realizability clause (c) power-inflation is sound.
- **Progress:** Lemma D proves the transversal target is **literally equivalent** to (CSP) — not weaker.
  The builder then honestly proves its only distinctive lever (partner map C↦C') is **horizontal**
  (C∩C'={q}, q∈C'), so it yields NO downward monovariant on any large-prime quantity. The framing
  self-certifies it adds no closing route beyond CSP itself.
- **Verdict rationale:** matches the round-4 self-dual-clutter-grading precedent — a NEW framing that
  self-certifies its distinctive lever collapses to another live lane's SAME open gap → RETHINK (not
  CHANGES REQUESTED: there is no gap for THIS builder to close that is not CSP). Byproduct lemmas salvaged.
- **Builder's recorded Status** (partial): downgraded — as a *route* it is dead. Lemmas are sound.
- **Certified from it:** Lemmas A/B/C (`intersecting-clutter-and-spawning.md`), Lemma D (canonical
  `csp-iff-E-small-only.md`, jointly with covering-small-part-descent Lemma 10).
- Scores: Correctness 10/10, Rigor 10/10, Progress 3/10 (equivalence pinned, no new lever).
- **True Status: unsolved-as-route.**

## covering-small-part-descent — CHANGES REQUESTED / partial

- **Correctness:** Lemmas 10, 12, 13 (EC-equivalence + W-inf), 14 (essentiality propagation) all
  re-derived independently and gap-free. EC (⟸) correctly uses A∪{q} covering ⟹ edge C''⊄A ⟹ q∈C'';
  propagation correctly uses Realizability clause (c) to derive the contradiction. Sound.
- **Progress:** genuine incremental advance — the crux gains a crisp **term-divisibility face (EC)**:
  "for every non-covering A and large q, some A-avoiding term is coprime to q", plus a self-reproducing
  propagation structure. But **q is preserved** under propagation, so no downward monovariant; honest gap
  = same wall (EC = ℰ-small-only = CSP).
- **Flaw found (non-fatal):** Lemma 11's claim "Case II is genuine" is illustrated by {2,3} for a_1=15,
  which is a large-prime-**free** minimal cover (rad 6<15), so it does NOT exhibit a large-prime edge with
  rad<a_1 — under the working hypothesis (a bad term exists) Case II's non-emptiness is not demonstrated.
  Not load-bearing for the crux; Lemma 11 NOT certified (pruning note only). Flagged in the file review.
- **Builder's recorded Status** (partial, advanced): accurate, no overclaim.
- **Certified from it:** Lemma 10 (`csp-iff-E-small-only.md`), Lemmas 13+14+W-inf
  (`essential-connector-equivalence.md`), Lemma 12 spawning (`intersecting-clutter-and-spawning.md`).
- Scores: Correctness 10/10, Rigor 9/10 (Lemma 11 example imprecision), Progress 5/10.
- **True Status: partial.** Gap to close next: force some A-avoiding term coprime to a large essential
  connector q — needs a genuinely new descent variable, not a q/rad/size monovariant (all proven to recur).

## bounded-window-distinctness — RETHINK / unsolved-as-route

- **Correctness:** Distinctness-by-Difference (q>N divides ≤1 element of a length-N window) is elementary
  and true. (R2′) is correct: large-prime-carrying witnesses confined to a value-band [a_1,V) are finitely
  many terms ⟹ Q(r_0) finite; contrapositive gives Q(r_0) infinite ⟹ unbounded witnesses.
- **Progress:** (R2′) is a rigorous **impossibility** result — the distinctness closer's needed
  confinement is EQUIVALENT to Q(r_0) finite, so it can only bite where ¬(FIN-Q) is already false. The
  route is decided in the negative (dead as closer), same wall as the proven-dead global Σ1/p² count.
- **Verdict rationale:** builder self-certifies RETHINK; the negative argument is sound. Salvage the true
  reusable local lemma.
- **Builder's recorded Status** (partial): the salvage lemma is real progress, but as a *route* it is dead
  → RETHINK.
- **Certified from it:** Distinctness-by-Difference (`distinctness-by-difference.md`, with a route-dead scope note).
- Scores: Correctness 10/10, Rigor 10/10, Progress 2/10 (negative certification + salvage lemma).
- **True Status: unsolved-as-route.**

## Goal Progress (for Eval History)

- **Ranking movement:** no Elo recompute here (reviewer does not rank); outcomes recorded —
  covering-small-part-descent `advanced` (Elo 1659, top live carrier), minimal-cover-small-only `dead-end`
  (1524), bounded-window-distinctness `dead-end` (1482). Two of three built = RETHINK.
- **Certified this round (4 lemmas):** `csp-iff-E-small-only.md` ((CSP)⟺ℰ-small-only, proved independently
  by TWO lanes — cross-check raises confidence); `essential-connector-equivalence.md` (EC + W-inf +
  propagation); `intersecting-clutter-and-spawning.md` (Lemmas A/B/C = Lemma 12 spawning);
  `distinctness-by-difference.md` (local, salvaged from a dead route).
- **The crux now:** UNCHANGED in substance — the single wall (CSP) = ℰ-small-only = **(EC)** = ¬(FIN-Q).
  New this round: a certified term-*divisibility* face (EC: force an A-avoiding term coprime to a large
  essential connector q) and a proof that essentiality is self-reproducing with q preserved (no monovariant).
- **Field diagnosis (flag for orchestrator):** 4th+ collapse to one wall; both new/re-attacked lanes
  self-certified their distinctive lever cannot close it (transversal monovariant horizontal; value-difference
  confinement vacuous). Per CLAUDE.md shared-gap rule, next round MUST field ≥1 approach from a genuinely
  different framing — NOT another CSP/ℰ/EC/FIN-Q reformulation (these are now certified-equivalent and
  exhausted as reformulations). The missing ingredient is a *value/dynamics lower-pressure* inequality tying
  a_1 to the covering structure (e.g. via the greedy successor choice), which no static-covering reframing has
  produced. Live carrier: covering-small-part-descent (EC form) — needs a new descent variable or a reframe.

## Per-slug verdicts
- **covering-small-part-descent: CHANGES REQUESTED (Status: partial)**
- **minimal-cover-small-only: RETHINK (Status: unsolved-as-route)**
- **bounded-window-distinctness: RETHINK (Status: unsolved-as-route)**
