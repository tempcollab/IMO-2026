# Outline review — imo-2026-03, round 7

Answer CONFIRMED c(n)=2^n/(2^{n+1}−1), minimax D=u_n=1/(2^{n+1}−1). 10 certified lemmas.
Field lives on exactly two residual walls: LOWER GAP L2-exch (μ(O_F∩O_B)≤(D(F)+D(B)−1)/2,
i.e. D(S)≥1 in the balanced band, |F|≥3) and UPPER GAP U-VALLEY (a₁<L/2, a₂<β_nL, full budget).
The outliner keeps both walls covered with 5 rival slugs, kept far apart by mechanism. Reviewed
adversarially below.

## Sanity checks run
- u₃/u₄ = 2.0667: the naive restricted subset-sum pigeonhole (over the DM-tree-realizable family,
  ~half of all ±1 patterns) yields only gap ≤ u_{n-1}L — genuinely short of u_nL by a factor ≈2.
  Confirmed the flagged GAP-ACH deficit is REAL, not an artifact. Also confirmed the TRUTH holds:
  min reachable ρ over random 5-element profiles is comfortably ≤ u₄L (0.002–0.015 vs bound
  ~0.07). So subset-sum's difficulty is entirely in the proof lever, not the claim.

## Per-approach verdicts

### induction-peel (revise) — APPROVE
Lower exchange via a split-and-average monovariant modeled on certified crux aimo-0298
(minimal-scale sorted-adjacent pair, split by position parity into E/O, IH on the two smaller
multisets). Sound technique: this is the concrete, corpus-backed way to WRITE the un-written
adjacent-pair exchange, and it correctly carries the SPLIT cross term rather than the refuted
min-cap μ≤min(D(F),D(B)) (the D(F)=D(B)=1 → D(S)=2 case kills the cap; the outline explicitly
avoids it). Not a recorded dead end. Load-bearing step with mechanism stated: step 5, the
inequality D(S) ≥ ½(D(S_O)+D(S_E)) + run-term, justified via SPLIT + the superincreasing gap
structure (Lemma ONE one level down). Issues to close while building:
  - The IH invocation MUST enforce the cut budget one level down: (|F|−1)+c_T ≤ n−1. The explorer
    verified that an un-budgeted checker manufactures false D(S)<1 "counterexamples." Builder must
    prove S_O, S_E each have ≤ n−1 cuts before invoking LB(n−1).
  - Must degenerate correctly to the closed |F|=2 case (run of length 2) as a check.
Right technique, fixable gaps → build.

### parity-measure-potential (revise) — APPROVE
Lower exchange via a STRENGTHENED structural IH: replace scalar D(B)≥1 with a per-gap occupancy
invariant on O_B (each dyadic gap of C_{n-1} met in ≤1 interval, via Lemma ONE recursed), then
bound μ(O_F∩O_B) gap-by-gap. This is the explorer's #1 opening and directly attacks WHY the master
inequality is unclosable from D(B)≥1 alone (the fix is upstream, not a sharper overlap cap).
Genuinely different mechanism from induction-peel's monovariant → good plateau-break diversity.
Mechanisms stated for both load-bearing lemmas (single-interval-per-gap; gap-wise overlap with the
−1 telescoping deficit distributed one unit across gaps). Issues to close:
  - Step 3 (the invariant is inductively preserved under a cut) is the real content — must be
    proven, not asserted; check the top gap where an F-excursion may exceed 2^{n-2}.
  - Step 4 must recover the exact −1/2 deficit by summation (Σε_k=1), not a loose bound.
  - Do NOT fall back to sharpening the overlap cap in isolation (the whole point is the richer IH).
Right technique, fixable gaps → build.

### breakpoint-vertex (advance) — APPROVE
Upper valley by cashing out the PROVEN Theorem VERT into an explicit tie-pattern bound. VERT +
PL1's rank-count are re-verified solid infrastructure (explorer re-checked the derivative algebra
and rank argument, no flaw); the numeric min-over-vertex-cuts = min-over-fine-grid match (my R5
check) confirms the finiteness lemma is TRUE. The remaining work is genuinely GAP U-fin: the
profile-independent min-over-tie-patterns ≤ u_nL. Mechanism stated: "one mark short" of U0(b) full
cancellation ⇒ exactly one core leftover ρ=D, bounded via the SPLIT cross term. Issues:
  - Must argue the min is achieved at the SIMULTANEOUS even-pairing type, not enumerate all types
    by hand — sequential/cascading single bisection is refuted (4.7×), and deterministic DM rules
    are refuted (4.2×–25×). Pairing must be simultaneous.
  - VERT gives a per-n finite family, NOT an n-independent closed form: expect the induction on n
    to carry the n-dependence (explorer confirmed VERT finitizes within one step, not the recursion).
Right technique, ready to advance → build. This is the safe, established upper lever.

### subset-sum-pigeonhole (new) — APPROVE (register), HOLD from build
Restricted subset-sum / number-partitioning pigeonhole for the upper valley. Genuinely new
framing, distinct from the refuted mass-threshold subset-cover (which was a single-threshold
search, not a full sorted-subset-sum-gap pigeonhole) — not a recorded dead end. NOT circular. But
the make-or-break step GAP-ACH is a verified factor-2 deficit (my check: u_{n-1}/u_n ≈ 2.07;
only ~half the ±1 patterns are DM-tree-realizable), and all three proposed closers (spend a free
DELETE / monotone-consecutive-sums / identify with VERT's tie-graph family) are speculative and
unproven. Honestly flagged by the outliner as "lives or dies on" this one step. It is a legitimate
diversity bet for the population, but too speculative to spend a scarce builder slot on this round
while breakpoint-vertex is the ready upper advance. Registered at 1500 (now 1452 after ranking);
revisit for build once a concrete deficit-closer is in hand.

### merge-interleave-pattern (new) — APPROVE (register), HOLD from build
Lower exchange as a reachable-word extremal problem: encode the descending F/B merge as a word w,
D(S)=L_w(values) a linear functional, characterize reachable words (≤1 F-letter per dyadic gap),
minimise to the canonical telescoping value 1. A THIRD independent lower framing, kept far from the
monovariant (induction-peel) and structural-IH (parity-measure) routes — good for population
breadth. NOT circular; the outliner explicitly guards against it collapsing into induction-peel's
adjacent-swap. But both steps (GAP-REACH reachable-word characterization; GAP-EXTR the min is the
canonical interleave) are fully open in the skeleton, and the reachability claim needs the cut
budget (|F|−1)+c_T≤n−1 enforced or the reachable set is over-counted (explorer's harness warning).
Minor note: the telescoping arithmetic printed as "(2^n−1)−(2^n−2)=1" differs cosmetically from
current.md's "2^n−(2^n−1)=1"; both give 1, builder should state one consistently. With two stronger
lower routes already in the build set, hold this as the population diversity bet; promote if the
two revises stall on the same wall next round.

## Ranking (updated this round; stale flags cleared)
parity-measure-potential 1668.9 (leader) > induction-peel 1597.2 > smoothing-majorization 1533.4 >
breakpoint-vertex 1510.8 > merge-interleave-pattern 1466.6 > subset-sum-pigeonhole 1451.9.
Newcomers anchored against advanced established opponents (both lose to the advanced lower/upper
routes; merge-interleave > subset-sum since subset-sum's factor-2 GAP-ACH is a verified hole).

## Diversity note for the orchestrator
Both walls stay covered by INDEPENDENT framings. Lower: two genuinely different mechanisms
(split-and-average monovariant vs structural per-gap IH), plus a third dormant framing
(reachable-word counting) held in reserve — this satisfies the plateau-break rule without
diluting the build. Upper: the ready VERT-finitization advance, with the subset-sum pigeonhole
held as a novelty bet. The two lower routes now share the SAME target inequality (L2-exch) for a
4th round; if both stall again next round, promote merge-interleave-pattern (furthest framing) and
reconsider whether the target inequality itself needs re-planning.

## Verification the builders actually run
R3 and R5 both stalled after outline-review with builders never executing. The orchestrator MUST
confirm the 3 build-set builders run and the reviewer records outcomes (check ranking last_round
advances to 7 and /tmp/round-7/proof-builder-*.md exist) before closing the round.

build set: parity-measure-potential, induction-peel, breakpoint-vertex
