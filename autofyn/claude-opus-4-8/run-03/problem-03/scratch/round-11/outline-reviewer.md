# Outline review — imo-2026-03, round 11

Field = two mandated vehicle-switches, one per wall (ballot-matching LOWER, breakpoint-vertex UPPER),
both `revise` of already-registered slugs. No new slug to register, no branch/copy requested. The
outliner correctly declined a third slug on either wall (single-gap-trap Rule): both explorers
independently confirmed there is no far-apart *second* vehicle per wall (upper subset-sum-pigeonhole
collapses onto the same tree-realizable object; lower's only surviving post-R10 lever is
matching/transport). parity-measure-potential is correctly held as a non-scalar reserve only, not built.

Neither approach violates a standing refutation Rule: ballot-matching is a global transport certificate,
NOT any scalar potential Φ(τ) (R10-dead family avoided); breakpoint-vertex is a global
confinement×count×density invariant, NOT a fixed/bounded-depth move lemma (R10), NOT ρ_i≤a_i/2 alone
(R10), NOT a recursion/greedy (R9). Both comply.

---

## ballot-matching (LOWER) — CHANGES REQUESTED (build)

Technique is the only surviving lower lever after R10 (matching/Hall-transport), so it is the right
tool by elimination. Skeleton is honest: the reduction (step 1) is fully certified (R/M/TB/MID/ONE-REC/CLIP),
the two make-or-break claims (HALL-ENDPOINT step 5, GAP-TERMINAL step 6) are named WITH a mechanism
(ONE-REC's ≤1-fragment-per-scale cap; the forced terminal descent as the def(G) budget), not bare labels.

The single-gap-trap warning the dispatch flagged is REAL and the skeleton's escape is conditional, not
guaranteed. My round-8 rule stands: a "later-credit" Hall condition on a line (debit-above-τ ≤
credit-below-τ) is exactly the prefix-sum inequality by LP duality and collapses to parity-measure's
Σc_iw_i≥0. The skeleton escapes this ONLY if the min-cut genuinely sits on a NON-PREFIX set — which R10
actually proved (the n=7 witness Φ(8.944)=−2.07 breaks every prefix-testing scalar). So the transport
framing is not vacuous *provided the ladder adjacency is not a threshold order*. That is the entire bet.

Requirements the builder MUST honor (else this is a dressed-up dead route):
- Do the FIRST ACTION before any general proof: construct ONE fully explicit transport map (hand / small
  LP / max-flow, scipy.optimize.linprog) on the n=7 CLIP witness F={63.0119,62.8559,2.1322} + its 12-piece
  B, AND on n=3..5 a=0 witnesses. Exhibit the actual debit→credit assignment and empirically locate the
  min-cut (prefix vs union-of-bands). The field has NO worked matching instance — this is the cheap
  de-risking step and it either finds the mechanism or falsifies "local scale-adjacency only" immediately.
- RECURSION-COLLAPSE guard (explorer + outliner both flagged): if step 5's endpoint-split is unrolled as a
  literal induction on n via ONE-REC scale-by-scale, it IS parity-measure's recursion and dies on the same
  wall. The distinct content must be an explicit min-cut description checkable by inspection, NOT "invoke
  Hall's name and induct." If the build reduces to induction-on-n, declare it collapsed, do not ship it.
- The cheap-kill probe (step 2, even-c_i Abel floor) is correctly labeled a probe, not assumed — fine.
- GAP-TERMINAL rests on S_m=|F|−|B|<0 (|B|≥|F|). Verify this holds for every a=0 refinement with |F|≥3
  before leaning on it as the deficiency budget — it is stated as "B refines the full ladder" but not proved
  in the skeleton; confirm on the worked instances.
- Gale–Hoffman / transportation-feasibility is NOT in knowledge_base.md — state and cite it explicitly as a
  named classical fact (per "name your tools").

Verdict: buildable, only surviving lower lever, honest cruxes, concrete falsifiable first step. Build it,
but the worked explicit certificate comes first and the collapse guard is mandatory.

## breakpoint-vertex (UPPER) — CHANGES REQUESTED (build)

Right technique (global strengthened invariant, not a refuted move-lemma/recursion). I ran the cheap
adversarial sanity check the outliner asked for:
- CONFINEMENT max(R_i)≤a₁: 0 failures across random + near-tie-injected n=3..6. The one-line proof
  (|v−a_i|≤max(v,a_i), both ≤a₁) is correct. This is a genuine cheap deliverable — certify it this round.
- COUNT |R_{n+1}|=2^{n+1}: 0 failures even under near-tie injection. Still RANDOM/near-tie-only — exact
  collisions need v+w=2a_i exactly (measure zero), which perturbation search cannot find. The outliner
  correctly labels COUNT "adversarial check required, not a theorem yet." Treat as conjecture; a proof must
  show the valley caps a₁<L/2, a₂<β_n exclude v+w=2a_i exactly. Do NOT build on COUNT as certified.
- min(R_{n+1}\{0})/u_n worst = 0.66/0.70/0.55/0.40 (n=3..6): Covering target holds with GROWING margin,
  consistent with a robust (not knife-edge) argument existing — mild encouragement.

GAP→VALUE (step 5) — the dispatch asked me to judge plan vs hand-waving. Verdict: currently a research
direction, NOT yet a concrete mechanism, and the outliner is honest about that ("make-or-break OPEN").
Route (a) "show the small gap occurs adjacent to 0" states no mechanism for WHY the near-0 gap lands at 0.
Route (b) "3-parameter joint confinement×count×local-density induction on m_i=min(R_i\{0})" is the genuine
idea but is explicitly "not yet formulated as a clean invariant"; the explorer notes the single-closest-point
version m_i≤dist(a_i,R_{i-1}) was already refuted as insufficient (saturates a_{n+1}/2≫u_n), so the whole
weight rests on the un-formulated local-density refinement. This is the real residual and it is not closed
by this skeleton.

Requirements:
- Certify CONFINEMENT this round (cheap, real).
- Adversarially/deterministically test COUNT (design exact-tie profiles) before using it; if it fails,
  the pigeonhole substrate changes.
- Do NOT present step-4 pigeonhole as a proof: it yields a small GAP between two reachable points, not a
  small element, and the budget is exhausted (explorer's + R10's explicit caveat). A build that stops at
  step 4 is partial, not solved.
- The round's honest deliverable is CONFINEMENT + COUNT verification + a serious attempt at the m_i local-
  density invariant. Expect partial/CHANGES REQUESTED, not solved.

Verdict: right vehicle, cheap wins bankable, GAP→VALUE remains genuinely open (honestly flagged). Build it.

## Field / diversity note

The two walls remain fully independent (LOWER transport certificate vs UPPER reachable-set invariant) —
no shared gap, good. The intra-wall single-gap-trap risk is entirely on ballot-matching (collapse to
parity-measure's Σc_iw_i≥0) — this is the field's one live convergence risk and is guarded by the
explicit-certificate-first requirement. If ballot-matching collapses to induction-on-n this round, next
round the lower wall has NO far-apart vehicle left (a structural warning for the orchestrator, not a
this-round action): the whole lower wall would then be one framing and the field needs a genuinely new
lower mechanism seeded.

## Ranking (this round)

Anchored to last outcomes: breakpoint-vertex (advanced R10, live route, cheap CONFINEMENT win, verified
substrate) ranked above both ballot-matching (unbuilt, no worked instance yet) and parity-measure-potential
(1754 but its forward scalar-reserve family was REFUTED R10 — negative go-forward evidence; nudged down to
break incumbent lock-in). ballot-matching placed above the dead/dormant lower siblings (induction-peel
dead-end, merge-interleave held, lp-dual/explicit-pairing weak) but below parity-measure (which still
carries more certified progress). Post-update leaders: parity-measure 1752, breakpoint-vertex 1678,
induction-peel 1542, ballot-matching 1513. Stale flags cleared on the compared set.

build set: ballot-matching, breakpoint-vertex
