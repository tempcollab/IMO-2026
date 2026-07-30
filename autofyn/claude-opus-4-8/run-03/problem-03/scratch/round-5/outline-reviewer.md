# Outline review — imo-2026-03, round 5

Scope: adversarial gate on the outliner's field (proof-outliner.md) before any build effort.
Two shared walls this round: LOWER (L1 critical band `D(S')≤f1-1` + L2 top-shredded `D≥1`) and
UPPER (GAP U, balanced `a1<L/2`). All four candidates verified against the recorded dead ends
(global concavity of V FALSE; cascading bisection fails 4.7x on near-uniform n=5 tail;
mass-threshold subset-cover non-exhaustive; false "WLOG single top cut"). None reinstates a
refuted lever.

Numerical checks I ran this round (decisive):
- **VERT is TRUE (supports breakpoint-vertex).** Restricting Xiang to tie/self-bisection cuts
  matches the full grid optimum over 300 random profiles (m∈{2,3}, ≤2 cuts); worst
  vertex−general gap ≈ 1e-17. So "min over all responses = min over vertex responses" is not a
  fantasy — the finiteness theorem's conclusion is numerically exact.
- **Gap-interleaving band split holds (supports induction-peel).** For n=3,4,5 the inequality
  `D(S')≤f1-1` holds with large slack in the trivial regime (`w≤2^{n-1}-1`) and tightens only in
  the width-1 critical band, consistent with the explorer's tight-extremal telescoping. The
  identity `D=Σ(t_k−g_k)=(2^n-1)−w=f1-1` (below-insertion) is structurally sound.

---

## breakpoint-vertex (NEW, framing F) — APPROVE

Verdict: APPROVE. Register (done, Elo 1500) and build. This is the genuinely-far framing the
SHARED-WALL-BREAK rule demands: it attacks BOTH walls through one finiteness theorem, not a
variation of the interleaving/measure framing the rest of the field shares.

- **PL1 (single-cut piecewise-linearity, slopes ∈{-2,0,2}, min at a breakpoint):** sound. The
  slope computation `g'(s)=(-1)^{i+1}-(-1)^j` with `d(ℓ-s)/ds=-1` is a correct exact fact; a PL
  function on an interval attains its min at an endpoint/breakpoint. No objection.
- **Theorem VERT (the crux, flagged open):** the JOINT statement is genuinely load-bearing and is
  NOT yet proved — the outliner is honest about this. My numeric test says VERT is *true*, so the
  builder is not chasing a false lemma. BUT the proposed proof (settle cuts outermost-first, "a
  smaller later cut cannot un-tie a frozen larger tie") is currently a heuristic, not an argument.
  The real hazard: settling one cut changes the background lengths seen by the others, so a cut
  previously at a tie can be un-tied, and the naive potential "# non-breakpoint cuts" need not
  decrease. **Required of the builder:** prove VERT via a well-founded monovariant — e.g. take an
  optimal response minimizing (lexicographically) the sorted vector of "distance of each cut to its
  nearest breakpoint", and show any non-breakpoint cut can be slid to a breakpoint WITHOUT
  increasing D AND without increasing that lex vector (sliding along a flat slope-0 segment, or
  collapsing a V at a breakpoint). Do NOT hand-wave "reorder freely": the final multiset is
  order-free but the settling induction is not. If VERT cannot be made rigorous, §4A/§4B are the
  easy payoff and the approach collapses — so VERT is the make-or-break deliverable.
- **§4A (GAP L vacuous):** I checked the potential contradiction — against dyadic C_n the true
  minimiser (interleaving, D=1) is a NON-tie response, so "optimal ⇒ tie" is only WLOG (existence
  of *a* tie optimum). Confirmed consistent: cutting 2^n into exact tail values {2^{n-1},…,2,1,1}
  is a tie response that also gives D=1 exactly (I verified the measure computation). So §4A does
  not contradict the certified interleaving fact. Good.
- **Watch:** §4B ("pair near-equal pieces, bisect the odd one, bound leftover ρ≤u_nL via SPLIT")
  overlaps smoothing-majorization's regime (i) endgame — see diversity note below.

## induction-peel (REVISE, framing A) — APPROVE (advance)

Verdict: APPROVE. Build. The lower-wall unified gap-interleaving lemma is the cleanest closable
gap in the field, backed by the explorer's numerics and mine.

- **Trivial/critical band split** (`w≤2^{n-1}-1` one line via `D(S')≤max≤2^{n-1}≤f1-1`; critical
  band width exactly 1): correct and confirmed. Keep the two-subcase split — do NOT seek one
  uniform bound (margin is 0 at the band's right edge; any lossy step, in particular dropping the
  SPLIT cross term, fails there — quantified by the explorer, gap up to 2^{n-1}).
- **Unified Gap-Interleaving Lemma (closes L1 AND L2):** the telescoping `D=Σg_k−Σt_i` is a real
  exact identity (Lemma M), and L1 (below-insertion → `f1-1`) / L2 (above-insertion → `1`) are two
  instantiations of one object. This is a legitimate unification, NOT a split-proof-across-slugs
  (both L1 and L2 are proved inside this one whole attempt). **Real remaining content = the
  EXCHANGE step** ("one-per-gap is extremal; any fragment outside a canonical gap, or a second
  fragment in an occupied gap, moves D in the safe direction"). This is honestly flagged as open;
  the per-cut `|dD|≤2s_2` bound is correctly noted as too loose. Required of the builder: write the
  bespoke adjacent-pair exchange with the gap-occupancy invariant (which gaps are occupied), not a
  mass/piece-count bound. Standard olympiad move but must be written, not asserted.

## smoothing-majorization (REVISE, framing E) — APPROVE (revise)

Verdict: APPROVE. Build — but the builder MUST REPLACE the file's existing SMOOTH content, not
extend it. The old (SMOOTH) "V nondecreasing along a dyadic-ward exchange" relies on global
concavity of V, which is REFUTED this round (explorer-upper, explicit n=2 violations; my role
memory already flags interior valleys). The new plan (D-DICHOTOMY, extend certified Lemma U0 from
m≤n to m=n+1 carrying SPLIT's cross term exactly) genuinely avoids concavity — it uses only exact
identities (Lemma P even-multiplicity + Lemma SPLIT), never a min-over-strategies convexity claim.

- Regime (i) NEAR-UNIFORM must be SIMULTANEOUS even-pairing (not sequential cascading — refuted,
  4.7x on the n=5 profile). The outliner's watch-out correctly names the stress-test profile;
  require the builder to run any candidate on `(0.2024,0.1965,0.1820,0.1789,0.1651,0.0750)` FIRST.
- **Open gap (must close): exhaustiveness of (i)+(ii)** over the `a1<L/2` simplex — the
  "δ-cluster" case split. This is the crux and is honestly flagged. Also the exact leftover bound
  `ρ≤u_nL`. Do NOT present a sample-point check as exhaustiveness (repeated reviewer rule).

## parity-measure-potential (ADVANCE, framing B) — APPROVE (advance, low-risk)

Verdict: APPROVE. Build. Two concrete deliverables, both valuable:
1. **Certify Lemma U0 (m≤n ⇒ D=0) as a shared lemma file.** This is a DEPENDENCY imported by both
   smoothing-majorization (regime i) and breakpoint-vertex (§4B) — certifying it unblocks two other
   approaches. Low-risk, mechanical, high leverage. Even if deliverable 2 stalls, this stands.
2. **GAP L2 via toggle/measure calculus** — a DIFFERENT derivation route to the same interleaving
   fact induction-peel attacks by exchange. Legitimate insurance, but see diversity note: it shares
   the *target object* with induction-peel's L2. If the toggle route can't be made rigorous, the
   outliner's own fallback (degrade to U0 certification) is acceptable — do not force it.
   Do NOT re-derive L1 here by the refuted mass-cover (the watch-out is correct).

---

## Diversity assessment (single-gap-trap guard)

The field is adequately far apart in framing, but two closeness risks to flag for the orchestrator:

1. **Lower wall — induction-peel L2 (exchange) vs parity-measure L2 (toggle/measure) target the
   SAME combinatorial object** (one-per-gap interleaving telescoping). They differ in *technique*
   only, which CLAUDE warns is "too close." If the interleaving-extremal fact is harder than the
   numerics suggest, both stall together. **Mitigant already present:** breakpoint-vertex attacks
   the lower wall from a completely different direction (VERT makes L1/L2 vacuous, never touching
   the interleaving object). That is the genuinely-different lower-wall framing the SHARED-WALL rule
   asked for — keep it in the build set as the insurance line.
2. **Upper wall — breakpoint-vertex §4B and smoothing-majorization regime (i)** both end with
   "pair near-equal pieces, one leftover, bound ρ≤u_nL via SPLIT." The *routes in* differ (finiteness
   theorem vs explicit regime dichotomy) so the framings are distinct, but the endgames converge.
   Acceptable this round; if both stall on the leftover bound next round, that endgame is the shared
   wall to challenge.

No approach is a fragment or a split-across-slugs proof: each targets the whole minimax claim end
to end (both bounds), differing only in which wall it advances. No RETHINK this round.

---

build set: breakpoint-vertex, induction-peel, smoothing-majorization, parity-measure-potential
