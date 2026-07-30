# Outline Review — imo-2026-03 (IMO 2026 P3), Round 12

Sole open wall: GAP L (lower bound, Case B) ⟺ `I_n ≤ 0` ⟺ base-slice `(★)` + the `b`-lift.
Upper bound certified/DONE (do not touch). The field this round is well-structured: it hedges
BOTH open gaps with TWO far-apart framings each (single-gap trap avoided) —
(★): value-domination (peel §11) vs Abel/parity pairing (ladder-abel); `b`-lift: WM-loaded-IH
(peel §11.5) vs co-varying descent (coupled-cut-descent). I verified the load-bearing numerics
myself before ranking.

## Independent verification I ran
- **WM does not over-shoot (the flagged risk).** `probe_wm.py`: 960k exact-`Fraction` fractional
  configs, `n=2..9`, BOTH tie-break conventions. `0` WM failures, `0` `(★)` failures, and — the
  decisive check — `0` configs where `(★)` holds but WM fails. So on the tested range WM is not a
  strictly-stronger claim that breaks where `(★)` survives. Combined with the outliner's integer-
  exhaustive `n≤6` and the explorer's 280k `n≤8`, the over-shoot danger is negligible. The field
  also carries an exact-`(★)` fallback (ladder-abel), so even a large-`n` over-shoot is covered.

## peel-scale-rank-induction — CHANGES REQUESTED (advance; primary)
Verdict: sound, keeps its slug (already registered, leader Elo 1704). §11 adds the WM/HLP route.
- Technique is right: value-domination (weak majorization / HLP threshold form) is the correct
  object for a cross-block dominance, and it is explicitly NOT the refuted per-block same-block
  charge (51% fail) nor a positional running-margin scan (margins → −2^{n−1}, refuted). The
  self-similar truncation view (§11.2) legitimately reduces `(HLP)` to a uniform-in-`t` tail-
  integral family — the standard Karamata/HLP toolkit applies.
- Load-bearing lemmas have mechanisms: `(DOM) b_i = 1+Σtail` (geometric, one rung dominates its
  whole tail — the cross-block cancellation) and `(m₀≤1)` (two reds >θ sum >2^n) are both proven
  and correctly stated.
- Issues to close while building:
  1. **§11.4 is still the whole crux (GAP-P1′-a).** The "charge red-even mass onto blue-odd of ≥
     value uniformly in `t`" step is stated but not proven. This is the real work. Do NOT let the
     builder present the truncation reduction as if it closes it — the tail-charge inequality must
     be exhibited, not asserted.
  2. **Use partial-sum (weak) majorization, never termwise 1-1.** Termwise `k`-th BO ≥ `k`-th RE
     is FALSE (explorer: `n=3, π_0=(2,2,2,2)`, BO=[4,1], RE=[2,2], `1<2`). Flag this in the build
     so the builder does not waste effort on a naive value injection.
  3. **§11.5 loaded-IH continuation (the `b`-lift, GAP-P1′-b).** Adopting `(WM)` as the loaded IH
     is a legitimate way to unify both gaps and dodge the slice-max mirage (the slice-max is flat
     `=0` for all `b<n`, so no `b`-slack exists — confirmed by the slice-reduction explorer). The
     inheritance-under-one-peel step (`F'=π_1⊎F''`) is unproven and is the open crux of the lift.
     Keep it clearly labeled OPEN; do not overclaim the colour-sum generalization (`(C)=1` for any
     `F'`, which IS verified) as if it closed inheritance.

## ladder-abel-pairing — APPROVE (new; build; the exact-`(★)` hedge)
Verdict: sound and genuinely diverse. Registered (Elo 1557). Targets `(★)` EXACTLY via Abel
summation / summation-by-parts rung-telescoped, with a global parity closer — a positional/parity
dual to the value-domination route, far from it. This is the correct hedge against WM over-shoot.
- Skeleton is valid: `D̃ = Σ_{j odd}(w_j−w_{j+1})` (each gap ≥0, elementary); the distinct move is
  re-pairing each odd-rank rung against the even-reds in its `(DOM)`-dominated tail; boundary =
  lone leading red (`(m₀≤1)`, rank 1, contributes 0); parity of `ΣL=2^n−1` odd forces residual ≥0.
  Crux analogue aimo-0388 (baby-P3 coin split, parity ⇒ |diff|≥1) is a genuine structural match.
- Issues to close while building:
  1. **Step 3 (rung-telescoped pairing) is the sole real difficulty** and is stated, not proven —
     same status as peel §11.4 but reached by a different mechanism. That is fine (diversity), but
     the builder must produce the actual telescoped inequality with the `(DOM)` cross-`k`
     cancellation, not just describe it.
  2. **Watch the refuted trap it names:** must NOT collapse to a one-directional positional
     running-margin scan (top-down/bottom-up reserves refuted; margins → −2^{n−1}). The approach
     file flags this correctly; enforce it — the parity closer must be GLOBAL, not a bounded-buffer
     prefix scan.
  3. **Tie check:** at the `n+1` tie configs red/blue alternate perfectly after the lead red, both
     sides of `(★)` are 0 ⇒ equality. The pairing must give equality there (correctness gate).

## coupled-cut-descent — CHANGES REQUESTED (new; build; the `b`-lift hedge)
Verdict: sound framing, genuinely distinct, but the hard step is real — build it as the second,
far-apart attack on the `b`-lift wall. Registered (Elo 1514).
- **It is NOT the dead GAP-IMR vertex route.** I checked this specifically (dispatch item 2). The
  slice-reduction explorer explicitly separates route (a) co-varying descent (a concrete budget-
  conserving deformation move: merge one `F'`-cut, hand the freed cut to `π_0`) from route (b)
  "max `I_n` over a cell = vertex", which IS the dead GAP-IMR integer-minimizer framing. This
  approach is route (a); it explicitly disavows route (b) and the refuted `π_0`-fixed monovariant.
  It is a genuine co-varying monovariant with a finite tie carve-out — not GAP-IMR in disguise. Not
  cut.
- Issues / honest risks to flag to the builder:
  1. **Step 3 (descent lemma) is the hard open step.** The explorer verified only per-config
     EXISTENCE of a `D̃`-non-increasing coupled move (1395/1396 at `n=4`, sole failure = an exact
     tie). A clean SELECTION RULE + monotonicity proof at general `n` is missing and is the entire
     difficulty. Do not let the builder pass off "a good move exists per config (n=4)" as a proof.
  2. **Tie carve-out is MANDATORY, not optional.** Slice-max is flat `=0` for every `b<n` (zero
     `b`-slack), so the descent is max-preserving and stalls exactly on the `n+1` tie family. Step
     5 must close that finite family explicitly (ladder-interleaving: both sides of `(★)` are 0),
     AND confirm the tie set is exactly `n+1` for all `n` (verified only `n≤6`).
  3. The base slice `(★)` it imports is itself still open — so coupled-cut-descent is not a
     standalone finish; it closes the lift conditional on a sibling closing `(★)`. Acceptable given
     the field structure (this is the b-lift specialist).

## allocation-vertex-corner — RETIRE (concur)
I concur with retirement. The `φ(b)` scalar-`b` pruning engine is DEAD (R11: exact ties `I_n=0` at
`b=2,3`; scalar `b` has no separating power — reconfirmed by the slice-reduction explorer's flat
slice-max). Its Positive-Layer Localization Lemma is banked/certified and imported by
ladder-abel-pairing, so nothing is lost. Not built; ranked as a dead-end loser (Elo 1461).

## Field / diversity note for the orchestrator
The plateau is R3–R11 (9 rounds), but the field is now genuinely diversified across BOTH sub-gaps:
- `(★)` (base slice): value-domination (peel §11) **vs** Abel/parity pairing (ladder-abel).
- `b`-lift: WM-loaded-IH inheritance (peel §11.5) **vs** co-varying descent (coupled-cut-descent).
No dead framing re-seeded (checked against the ban list: measure/merged-order/sequential/genfn/
scalar-summary/GAP-IMR integer-minimizer/b-cutoff — none present). If BOTH `(★)` routes stall on
the same tail-charge next round, escalate: the two `(★)` routes, while far in technique, share the
target inequality `(★)` — that is a proven-TRUE target (min `=1`, tie, verified), so sharing it is a
stall risk, not the fatal single-gap trap. Next round's contingency is the reserved aimo-0917 2-adic
split or a direct cut-tree structural induction on `(★)` — not any banned route.

build set: peel-scale-rank-induction, ladder-abel-pairing, coupled-cut-descent
