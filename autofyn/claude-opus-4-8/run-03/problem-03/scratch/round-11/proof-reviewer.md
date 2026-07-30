# Proof-reviewer — imo-2026-03, Round 11

Two approaches built; reviewed independently. Both report round-11 NEGATIVE results plus (for the
upper wall) two new lemmas. Neither is `solved`. No APPROVE this round.

---

## Slug 1: ballot-matching (LOWER wall — GAP MID-core)

**Verdict: RETHINK. Status: unsolved (mechanism refuted; no correct new progress toward closing MID-core).**

Scores — Correctness 5/5 (of the negative claims), Completeness 5/5 (honest, non-overclaimed),
Progress 1/5 (this is a mechanism refutation, not a step toward the proof).

### What I checked
The distinct contribution of this slug was a *structured* debit→credit transport / Hall certificate
for GAP MID-core (`Σ_i c_i w_i ≥ 0`, equivalently `Σ_{F even rank} v ≤ Σ_{B odd rank} v`). The
builder ran the mandated FIRST-ACTION explicit-construction de-risking and reports the whole family
collapses. I verified the load-bearing refutation facts:

- **GAP-TERMINAL premise is genuinely false.** The skeleton rested on `S_m = |F|−|B| < 0` ("forced
  terminal descent supplies guaranteed credit"). The tight minimiser has `|F| = |B|+1` (the top piece
  `2^n` shredded into one more fragment than the uncut ladder `B`), so `S_m = +1 > 0`. I reproduced a
  tight a=0 instance `S = {2,2,2,1}` (n=2): `D = 1` exactly, `|F|=|B|=2`, `S_m = 0` — NOT negative.
  So there is no forced terminal descent, and the defect-Hall deficiency budget the skeleton invokes
  does not exist. The refutation is sound.
- **Structured adjacencies all fail (numeric scans, sound as "for-all" refutations).** prefix (8.5%),
  suffix (30.4%), dyadic-scale interval-Hall / HALL-ENDPOINT (49%), value-dominating injection
  (49.6%). Each single failure within an admissible a=0 refinement refutes the corresponding "for
  all" structured certificate; the scans run on the certified reduction I have verified in prior
  rounds. The conclusion — only complete-bipartite adjacency is feasible, which is logically
  identical to the target `cw ≥ 0` — is a valid structural argument that the matching framing is
  vacuous.
- **Target still TRUE and tight.** `cw ≥ 0` never violated (min ≈ 5e-4). Consistent with the known
  answer; nothing here is a counterexample to the problem.

### Verdict rationale
The approach's *own* new vehicle (structured transport/Hall) is dead, corroborating R10's death of
the scalar-reserve family. The imported certified reduction stands but is not this slug's new
content. There is no path forward within this framing; per CLAUDE.md this is RETHINK — back to the
outliner for a genuinely new GLOBAL lower mechanism (aggregate ballot / cycle-lemma on the reachable
word, or F-partition majorization vs the fixed ladder B). **The builder's recorded Status ("partial,
mechanism REFUTED") is honest but the routing is RETHINK, not a live-partial continuation of this
mechanism.**

**No promotable lemmas** (builder proposed none; the round's content is negative facts, correctly not
offered for certification).

---

## Slug 2: breakpoint-vertex (UPPER wall — GAP U-cover)

**Verdict: CHANGES REQUESTED. Status: partial (real new certified lemmas; make-or-break gap open).**

Scores — Correctness 5/5, Completeness 4/5 (density substrate honestly pruned), Progress 3/5
(two reusable certified lemmas + a rigorous refutation that prunes a dead sub-route; the make-or-break
GAP U-cover did not move).

### What I checked (independently re-derived / recomputed)
- **Lemma CONF (`max R_i ≤ a_1`) — VALID, CERTIFIED.** The induction rests on `|v−a_i| ≤ max(v,a_i)`
  for `v,a_i ≥ 0`; I re-derived the case split (`v≥a_i`: `v−a_i≤v`; `v<a_i`: `a_i−v≤a_i`) — correct.
  With IH `v≤a_1` and sort `a_i≤a_1`, `max(v,a_i)≤a_1`, so `R_i⊆[0,a_1]`. One-line, profile-
  independent. Certified into `lemmas/confinement-reachable-set.md`.
- **Lemma MD2 (`|M_i|=2^i`) — VALID, CERTIFIED.** Doubling is immediate (disjoint union of a copy and
  its reflection); support `=R_i` and the leaf↔subset bijection is the same one behind certified
  Lemma ESF-2; leaf value = descending-KK caterpillar of the include-set. The multiset pigeonhole
  (gap `<u_n/2`) is correct but a gap is NOT reachable — I confirmed the builder flags this limitation
  honestly. Certified into `lemmas/multiset-doubling.md`.
- **COUNT `|R_{n+1}|=2^{n+1}` REFUTED — VERIFIED EXACT.** I recomputed the reachable SET on the
  all-equal profile `a_i=1/(n+1)`: `R_1={0,1/(n+1)}` then stable (`|0−1/(n+1)|=1/(n+1)`,
  `|1/(n+1)−1/(n+1)|=0`), so `|R_{n+1}|=2` for `n=3..6` (checked). It IS a genuine valley for `n≥3`
  (`a_1=1/(n+1)<1/2`; `a_2=1/(n+1)<β_n`, verified: n=3 `0.25<0.267`, n=6 `0.143<0.252`). The n=2
  witness `{7/16,9/32,9/32}` gives `R_3={0,1/8,5/32,9/32,7/16}`, `|R_3|=5<8` (recomputed, valley
  confirmed). So set-injectivity is genuinely false in the valley — the COUNT+density-pigeonhole
  substrate does not exist. Refutation is sound and correctly pruned.
- **Covering claim reconfirmed TRUE** (builder's scans, 0 exceptions n=2–6, worst cov/u_n=0.83);
  consistent with the answer. Not proved.

### Verdict rationale
The approach itself (LP-vertex / reachability-covering) is alive and remains the field's surviving
upper framing. This round it produced two genuinely reusable certified lemmas and rigorously pruned
the proposed round-11 density vehicle — real forward movement, but the make-or-break **GAP U-cover**
(the Covering claim `cov(A) ≤ u_n`) is unmoved. That is exactly CHANGES REQUESTED: keep the slug
live, attack the gap. The residual is now sharpened: a correct argument must handle BOTH the *spread*
regime (many distinct values, small non-reachable gaps) AND the *collision* regime (valley caps force
coincidences concentrating reachable mass at small/zero values) uniformly — density-pigeonhole sees
only one. **Builder's recorded Status ("partial") is correct.**

**Promotable lemmas certified:** CONF (`confinement-reachable-set.md`), MD2 (`multiset-doubling.md`).
Both held to the full bar (sorry-free, statements no stronger than proved — MD2's file explicitly
notes only the *multiset* count is a theorem, the *distinct* COUNT is false).

---

## Goal Progress (for Eval History)

- **Answer (unchanged, correct):** `c(n)=2^n/(2^{n+1}−1)`, minimax `D=u_n=1/(2^{n+1}−1)`.
- **Proved (standing):** full reduction to scalar minimax of D; upper bound entire range `a_1≥L/2`;
  lower bound base/trivial-regime/Case(a); 22 certified shared lemmas (+2 this round: CONF, MD2).
- **Two walls remain OPEN (both make-or-break; neither moved this round):**
  - **Lower — GAP MID-core:** `Σ_{F even}v ≤ Σ_{B odd}v` for a=0, `|F|≥3`. Now BOTH structured lever
    families are exhausted: scalar reserves (R10) and structured matchings/Hall (R11). Needs a new
    GLOBAL mechanism.
  - **Upper — GAP U-cover:** Covering claim `cov(A)≤u_n` in the balanced valley. COUNT+density
    substrate refuted (R11); confinement (CONF) + multiset enumeration (MD2) established but do NOT
    convert gap→value. Needs a spread+collision-uniform mechanism.
- **Elo movement:** ballot-matching 1512.9 (dead-end, RETHINK — mechanism refuted); breakpoint-vertex
  1678.1 (partial, CHANGES REQUESTED — 2 lemmas certified, leader retains top rank).
- **Per-slug verdict:**
  - `ballot-matching` → **RETHINK** (Status unsolved; structured-matching mechanism collapsed).
  - `breakpoint-vertex` → **CHANGES REQUESTED** (Status partial; CONF+MD2 certified, GAP U-cover open).
- **Orchestrator note:** the LOWER wall has now exhausted both scalar-reserve AND structured-matching
  families — this is a shared-gap plateau signal; next round should route ≥1 lower-wall approach on a
  genuinely different framing (aggregate ballot / cycle-lemma on the reachable word, or F-partition
  majorization vs the fixed ladder), not another transport/potential variant.
