# Outline review — imo-2026-03, round 2

Answer c(n)=2^n/(2^{n+1}−1) (minimax D = u_n = 1/(2^{n+1}−1)) confirmed. Shared lemmas R,
M/I, T, P certified. Both live routes bottom out on the SAME two coupling gaps: lower
top-piece-cut (B2/L) and adaptive upper strategy (B3/U). Verified this round:
- `1 − u_n/u_{n−1} = c(n)` exactly (single-pair peel threshold `2r ≥ c(n)` recovered from
  the multi-pair identity `2r ≥ 1 − u_n/u_{n−j}`) — the multi-pair peel arithmetic is sound.
- All-equal profile a_i=1/(n+1) is genuinely EASY: for even m=n+1 Xiang does nothing
  (even multiplicity ⇒ D=0), for odd m one bisect ⇒ D=0. (My first script forced a bisect
  on the even-m case and got D>0; that was the wrong move, not a counterexample — the
  outliner's "easy" claim stands.)
- Explorers independently confirm the subset-sum / one-shot multi-way split is the correct
  replacement for greedy-merge and single-pair peel (both provably insufficient n≥3).
  Neither built approach smuggles greedy-merge or single-cancelling-pair as THE upper
  strategy — both have moved to the multi-pair subset peel. Good.

## parity-measure-potential — APPROVE (advance)  [Elo 1582, strongest]
Global measure identity + net-toggle symmetric-difference; no induction. Both bounds live.
- Technique sound and distinct from the recursion route (single measure computation on the
  final odd-set). Upper via subset-match cancellation (multi-pair, Lemma P per pair) — not
  greedy. Lower via measure-charging telescoping.
- Watch (carry into build, not blocking): (i) the charging bound in step 3 must bound the
  SYMMETRIC-difference shrinkage μ(O₀ △ ⨁E_i), never Σ|ΔD| per cut — the naive
  "1 cut kills 1 band" pigeonhole is FALSE (Lemma T; a single E_i spans several bands).
  This is the load-bearing move; state the "erase-top-creates-block-below" step
  quantitatively or it is hand-waving. (ii) Gap B3 must handle the a₁-balanced branch by
  bisection/parity-collapse, NOT matching alone (multiplicative bound over-estimates
  balanced profiles). Both are flagged in the outline; keep them explicit.

## induction-peel — APPROVE (advance)  [Elo 1530]
Strong induction on n via u_n = u_{n−1}/(2+u_{n−1}); multi-pair subset peel + shadow-coupling
lower bound.
- Technique sound; multi-pair peel replaces the stalling single peel. Arithmetic verified.
- Load-bearing gaps, both honestly named with a mechanism:
  - Subset-cover feasibility (gap U): the disjunction a₁≥Lc(n) (bisect) / a₁>Σrest
    (dominant match) / a₁≤Σrest (balanced bisect) must be proven EXHAUSTIVE. This is the
    real crux — the reason the field stalled. Builder must prove the three branches cover
    every sorted profile AND that each branch's cut respects the residual piece-count
    bound m−j ≤ (n−j)+1 so UB(n−j) applies. Do not assert exhaustiveness; derive it.
  - Shadow map φ (gap L): the one-directional inequality D(actual residual) ≥ D(φ(residual))
    via Lemma T net-toggle must be constructed, not asserted. "Cutting a scale costs that
    scale" is the intuition; the coupling map and the domination of odd-sets is the work.
- Note: the explorer confirmed a stronger superincreasing-IH does NOT repair Case B
  (bisection makes the residual non-superincreasing). Do not re-attempt that IH shape.

## two-box-balancing — APPROVE (new framing, register + build)  [Elo 1501]
D=|O|−|E| (odd-rank box minus even-rank box) as a two-box balancing game; scale-tracking
invariant induction, two-case step (top scale touched / untouched), adapts aimo-0117.
- Whole attempt (both bounds end to end), not a fragment. Genuinely different mechanism from
  the measure integral and the mass-peel recursion: a scale-by-scale invariant on box
  balance. Explorers rate it the strongest new lead.
- Real risk to resolve while building (flagged in the outline, correctly): a cut's fragment
  landing mid-list re-sorts ranks and flips O/E membership of MANY pieces at once — the
  invariant MUST be stated on dyadic SCALES (bands), not on fixed ranks, or the two-case
  step breaks. Do not assume the top scale keeps rank 1 after a mid-list fragment appears.
- Diversity note: its lower-bound "top scale re-enters one level down" shares intuition with
  induction-peel's shadow map ("cutting a scale costs that scale") — related, but the
  mechanisms differ (global box invariant vs value-level coupling map), so they will not die
  identically. Acceptable, but the orchestrator should watch that these two don't converge
  onto one wall; if they do, next round push a framing farther from the scale-recursion idea.

## lp-dual-weight — CHANGES REQUESTED (registered, NOT built this round)  [Elo 1471]
LP primal-dual: one static certificate for both bounds.
- Not doomed: the smoothing/majorization half (dyadic is Liu's pointwise-worst surrogate —
  true, since dyadic attains the max; smoothing toward the 2:1 ratio via an exchange argument
  can transport the proven dyadic upper bound to every profile) is a legitimate, genuinely
  different upper-bound route worth keeping in the pool for diversity.
- But the framing as written over-promises: the minimax is over CONTINUOUS cut placements
  and D is a min of a measure, not obviously an LP, so "one clean dual certificate settles
  both faces" is aspirational — the outline itself admits the dual may have no closed form
  and offers the smoothing half as fallback. Registered at cold start to preserve a distinct
  framing, but it is the weakest-supported line and is held out of this round's build set.
  If revisited: lead with the smoothing/majorization exchange argument (concrete), treat the
  LP dual certificate as optional. Do NOT conflate μ(⨁E_i) with Σμ(E_i).

## Field / diversity
Top of field is two proven-infrastructure advances (parity-measure-potential,
induction-peel) attacking the two shared gaps via different mechanisms (net-toggle measure
vs. recursion) plus one concrete new framing (two-box-balancing) that recasts the whole
minimax. That is adequate spread; lp-dual-weight held in reserve as a fourth, farther,
framing. explicit-pairing-strategy (greedy, proven insufficient) sinks to Elo 1416 and is
not built.

build set: parity-measure-potential, induction-peel, two-box-balancing
