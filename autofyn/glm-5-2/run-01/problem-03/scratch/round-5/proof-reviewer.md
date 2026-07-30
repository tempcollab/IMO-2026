# Round-5 proof review — IMO 2026 P3 (`imo-2026-03`)

Reviewer independently verified every load-bearing claim with `Fraction`-exact arithmetic and
`scipy.optimize.linprog` strong-duality checks. All four slugs: **CHANGES REQUESTED (partial)**.
Seven new lemmas certified (24 → 31 total). Headline results: (a) the tail-count spine
sign-pattern / multi-swap framing is CIRCULAR (confirmed — a genuine negative result); (b) the
lp-dual LP-2 sign error is FIXED and scipy-verified; (c) three upper-bound sub-cases
unconditionally closed; (d) the XOR identity + tight n=1 base proved.

## `tail-count` — CHANGES REQUESTED (partial)

**Status:** partial (honestly marked). GAP-C (sub-gap (i), V-shape cell faces) still OPEN.

**Independent verification of the circularity finding (§14(B)).** I re-derived the
decomposition `(†)` `D(spine) = (F − T) + 2(t₊ − f₋)` from scratch and reproduced the
exact-`Fraction` counterexample: `T_3` with `8 → 5+3` (top) and `4 → 3+1` (below-top) gives
spine `{5, 2}` after pair-cancellation; the interleaving pattern HOLDS (position 1 = `5`
fragment at `+`, position 2 = `2` tower at `−`), yet `D(spine) = 5 − 2 = 3` and
`F − T = 5 − 2 = 3 ≠ 1`. So `F − T` equals `D` under the pattern, NOT the constant `1`. The
"mass identity `F = T + 1`" is therefore `D = 1` restated under the pattern — not an
independent mass identity. Confirmed: the single-swap (`2(t−v)=0 ⟹ t=v`) and the multi-swap
subset-sum argument both presuppose `S₊ = F` (the pattern), so they are circular as framed.
This is a valuable NEGATIVE result that kills an entire line of attack honestly — recorded so
no future round chases it.

**Mass-balance lemma (`lemmas/mass-balance-lemma.md`) — CERTIFIED.** The 3-line algebra
`D = S₊ − S₋ = 2S₊ − D_n` is pure and correct (`S₊ + S₋ = D_n`). The characterization
`D = 1 ⟺ S₊ = 2^n` (since `D_n` odd ⟹ `(D_n+1)/2 = 2^n`) is correct. The block-condition
case analysis (all-top-`−` ⟹ `S₊ ≤ 2^n−1 ⟹ D ≤ −1 ≠ 1`; all-top-`+` ⟹ `S₊ = 2^n ⟺`
all-below-`−`) does NOT presuppose the pattern — it uses the block condition (every split's
fragments at one sign) as a premise, then DERIVES that `D=1` forces the all-top-`+`/
all-below-`−` pattern. This makes sub-gap (ii) genuinely vacuous. The lemma's stated caveat
(it characterizes block-condition `D=1` cells; does NOT prove `D ≥ 1` on every block cell,
does NOT address V-shape cells) is honest and accurate. Sub-gap (i) (V-shape cell faces
inherit block condition) remains the genuine open step.

**Sharpest gap:** GAP-C sub-gap (i) — no proof that V-shape cell faces inherit the block
condition (verified `T_3`/`T_4`, open generally). The spine sign-pattern route is closed
(circular); a genuinely non-circular argument is needed.

**Verdict: CHANGES REQUESTED. Outcome: advanced** (sub-gap (ii) closed as vacuous; circularity
finding recorded; new lemma certified; main GAP-C still open).

## `majorization-upper` — CHANGES REQUESTED (partial)

**Status:** partial (honestly marked). GAP-U2 (pair-matching cascade) OPEN, explicitly a
conjecture.

**Three claimed unconditional sub-cases — all verified, all rigorous.**

1. **GAP-U3 (`m ≤ n ⟹ D* = 0`), `m-le-n-halving-D-zero` — CERTIFIED.** The even-multiplicity
   lemma is correct: a block of `2k` equal values at consecutive sorted positions contributes
   `v·(k − k) = 0` (over `2k` consecutive positions the signs alternate, `k` pluses and `k`
   minuses regardless of starting parity since `2k` is even). After halving every piece, each
   value `a_i/2` appears `2 ×` (multiplicity of `a_i`) times — even; collisions merge into
   even groups. So `D = 0`. Mark budget `m ≤ n`. I verified 0 violations over 10000 random
   trials. Rigorous and n-independent. Closes the `m ≤ n` case for ALL n.

2. **Bottom-dominant halving (`m = n+1`, `a_n ≥ 2 a_{n+1} ⟹ D = a_{n+1}`),
   `bottom-dominant-halving` — CERTIFIED.** The sorted-order preservation
   (`a_n/2 ≥ a_{n+1}` from the dominance) is the load-bearing step; I checked it directly:
   pairs `(a_i/2, a_i/2)` occupy positions `(2i−1, 2i) = (+,−)` and cancel; residual
   `a_{n+1}` at position `2n+1` (odd, `+`). `D = a_{n+1}`. Verified 0 violations / 10000
   random strictly-decreasing bottom-dominant configs. The corollary `D* ≤ a_{n+1} ≤ 1/D_n`
   when `a_{n+1} ≤ 1/D_n` (incl. the dominant tower-tail family, tower `T_n` tight) is correct.
   The round-4 reviewer flag (`a_{n+1} ≤ 1/D_n` false-as-stated for non-dominant tower-tail)
   is handled: the lemma explicitly scopes to bottom-dominant configs and does NOT claim
   `a_{n+1} ≤ 1/D_n` universally — it is a hypothesis of the closed sub-case.

3. **Repeated-value (`m = n+1` with a repeat ⟹ `D* = 0`), `repeated-value-D-zero` —
   CERTIFIED.** Uses certified `spine-pair-cancellation` (S1): spine has `≤ n−1` pieces;
   Xiang halves all spine pieces (`≤ n−1 ≤ n` marks). The case analysis proving every value
   appears an even number of times is exhaustive and correct (spine halves distinct since
   spine strictly decreasing; paired values give `2p` copies; collisions merge `2 + 2p`
   even). Then even-multiplicity lemma ⟹ `D = 0`. Rigorous.

**GAP-U2 honestly a conjecture.** The pair-matching cascade (split `a_n → {a_{n+1},
a_n−a_{n+1}}`, recurse) is described as a CONJECTURE with the precise obstruction stated
(residuals may not match in `n` steps; subset-sum / Diophantine condition; no general
guarantee). Numerics (3000 trials, n=4, worst ratio 0.52) are correctly labeled
verification-not-proof. The V(n)←V(n−1) IH and 3-mark cascade are DROPPED (refuted as
phantom-crux chasers). No overclaim.

**Sharpest gap:** GAP-U2 — strictly-decreasing `m = n+1` configs where halving exceeds target
(`a_{n+1} > 1/D_n`) or doesn't apply (non-bottom-dominant `a_n < 2 a_{n+1}`). No proof the
cascade always finds a match.

**Verdict: CHANGES REQUESTED. Outcome: advanced** (three sub-cases unconditionally closed;
GAP-U2 honestly conjectural).

## `xor-overlap` — CHANGES REQUESTED (partial)

**Status:** partial (honestly marked). GAP-X (overlap bound) OPEN, G1-equivalent.

**XOR identity (`lemmas/xor-overlap-identity.md`) — CERTIFIED.** The proof is rigorous:
Step 1 (count split `N_M = N_F + N_R` — sort does not affect a count above a threshold);
Step 2 (pointwise parity identity `(a+b) mod 2 = (a mod 2) + (b mod 2) − 2(a mod 2)(b mod 2)`,
verified by direct 4-case check); Step 3 (Tonelli integration of `{0,1}`-valued simple
functions with finite support, invoking certified `D-equals-parity-integral`). I verified
the identity `Fraction`-exact on 3000 random refinements of `T_2..T_5`: 0 failures. The
consistency check on the unsplit tower recovers `D(T_n) = 2^n − D(T_{n−1})` (certified
`frontier-recursion`). The objects are precisely defined (`N_P(t) = #{i: p_i ≥ t}`,
`Ω_P = {t: N_P(t) odd}`, `C = |Ω_F ∩ Ω_R|`).

**Tight base case `n=1` — VERIFIED.** For `F = (f, 2−f)`, `R = {1}`: I computed
`D_F = 2f−2`, `Ω_F = [2−f, f)`, `Ω_R = [0,1)`, `C = f−1`, giving `D_F = 2C` exactly and
`D = 2C + 1 − 2C = 1` for every `f ∈ [1,2)`. Tight (no slack at the base — the entire margin
is `D_R = 1` from the unsplit below-top piece). Verified `Fraction`-exact for `f ∈ {1.0, …, 1.9}`.

**Inductive reduction `G1(n) → G1(n−1) + GAP-X` — correctly set up.** Mark accounting (top
split into `k ≥ 2` fragments uses `k−1 ≥ 1` marks, leaving `≤ n−1` for `R`) is sound; `R`
is a `≤ (n−1)`-mark refinement of `T_{n−1}` = exactly the input class of `G1(n−1)`. Case (a)
(top unsplit) correctly routed to certified `tower-top-unsplit` (no IH).

**GAP-X honestly G1-equivalent.** By (XOR-bound), `C ≤ (D_F + D_R − 1)/2` is exactly
`D(M) ≥ 1` restated. The four attempted routes (trivial/Cauchy-Schwarz giving only `D ≥ 0`;
the sufficient `D_F ≥ 2C` FAILING at 543/2196 breakpoints; dyadic-`R` structure covering
only the already-closed `dyadic-refinement-lower-bound` sub-case; per-fragment charging
hitting the global-interleaving obstruction) are all documented with precise obstructions.
The non-circularity reproduction (dyadic-`R` sub-case reachable via XOR and reducing to a
certified lemma) is a genuine demonstration that the framing is non-circular. No overclaim.

**Sharpest gap:** GAP-X — no bound on `C` stronger than the trivial `C ≤ min(D_F, D_R)` /
`√(D_F D_R)` (both give only `D ≥ 0`). The `1` margin is not captured by generic inequalities.

**Verdict: CHANGES REQUESTED. Outcome: advanced** (XOR identity + tight base proved;
inductive framing set up; GAP-X open and honestly G1-equivalent).

## `lp-dual-certificate` — CHANGES REQUESTED (partial)

**Status:** partial (honestly marked). GAP-LP2 OPEN, G1-equivalent by strong duality.

**LP-2 sign fix — INDEPENDENTLY VERIFIED with scipy.** I re-derived the corrected dual
convention: for a min primal with `A_ub p ≤ 0`, the dual variable satisfies `y_ub ≤ 0`
(builder's corrected sign). Introducing the nonneg mountain `m_k := −y_ub[k] ≥ 0` with
sentinels `m_{−1} = m_{m−1} = 0`, the dual constraint becomes the **inequality**
`m_j − m_{j−1} ≤ d_j = (−1)^j − y_eq[b(j)]` (★), with complementary slackness
`s_j = d_j − (m_j − m_{j−1}) ≥ 0`, `s_j · p_j = 0`. I ran scipy on:

- The round-4 infeasible `T_2` demo `b = (0,1,0,2,2)`, n=2: primal min `D = 1.0`
  (`p = (2,2,2,1,0)`). The uniform cert `y_eq = (+1,−1,−1)`, `y_ub = 0` (mountain `m = 0`)
  is FEASIBLE under (★): `d = (0,0,0,0,2)`, slack `s_4 = 2` at the `p_4 = 0` vertex.
  Objective `4 − 2 − 1 = 1 = primal min`. Strong duality holds. The round-4 claimed cert
  `y_eq = (+1,−1,0)` (objective 2) is correctly INFEASIBLE (would violate weak duality).
  Sign fix confirmed.

- The even-`k` single-adjacent interleaving `b = (0,1,2,2)`, n=2 (`k = 2` even): primal min
  `D = 2.0`. The single-bump cert `y_eq = (1,−1,0)`, `m_2 = 1` is feasible, objective `2 =
  primal min`. ✓ For odd-`k` (`b = (0,1,1,2)`, `k = 1`): the single-bump would require
  `m_1 ≤ −1`, violating `m ≥ 0` — confirmed NOT certifiable by this cert (requires
  compensating interleaving, the open crux). Parity fix confirmed.

- Broad strong-duality sweep: 121 valid bin assignments (all bins `0..n` nonempty) for
  n=2..5, 0 with `primal min < 1` (consistent with G1). The corrected dual marginals
  satisfy `y_ub ≤ 0` throughout.

**Integrality shortcut FAILED — confirmed.** I exhaustively checked all 10224 valid bin
assignments for n=3: the per-type LP is NOT totally unimodular. Non-integer `min D` values
found: `5/3` (e.g. `b = (0,1,0,0,2,1,3)`), `13/3`, `17/3` — exactly matching the builder's
claims. So the parity argument (ruling out `D = 0`) is rigorous but insufficient (cannot
rule out `min D ∈ (0,1)` since `min D` is real). Honest and correct.

**Two new lemmas — CERTIFIED:**
- `lp-dual-odd-mass-parity` (§5b): `D = 0` infeasible by odd-total-mass parity. Rigorous:
  `D = 0` ⟹ (by `gaps-leftover-identity`) all adjacent pairs equal + trailing `0` ⟹ even
  total mass, contradicting `D_n = 2^{n+1}−1` odd. Correct. Caveat (insufficient for G1
  since `min D` real) honestly stated.
- `lp-dual-even-k-interleaved` (§5d): single-adjacent-2-piece interleaving at even `k`,
  rest clean. The single-bump mountain `m_k = 1` saturates both constraints at `j = k, k+1`;
  objective `≥ 1` by dyadic dominance. Rigorous, scipy-verified. The `k`-even restriction is
  load-bearing (odd-`k` would violate `m ≥ 0`); honestly noted.

**GAP-LP1 (clean types) intact.** With `y_ub ≡ 0` the sign correction is irrelevant
(`m ≡ 0` makes (★) the tautology `0 ≤ 0`); the certified `lp-dual-clean-types` stands
unaffected. The Farkas route (§5c) is honestly flagged circular (negation of dual-feasibility
IS the G1 statement). GAP-LP2 (structural sign-pattern feasibility) is OPEN, G1-equivalent
by strong duality (not a shortcut, per the round-4 rule).

**Sharpest gap:** GAP-LP2 — no general feasibility proof for the nonneg mountain `m`
absorbing the `d_j` mismatches on arbitrary interleaved types.

**Verdict: CHANGES REQUESTED. Outcome: advanced** (LP-2 sign error fixed and
scipy-verified; narrow sub-class closed; parity sub-result proved; GAP-LP2 open).

## Lemma certifications (round 5)

Certified (7 NEW, total 31):
1. `mass-balance-lemma` (tail-count) — algebra `D = 2S₊ − D_n` + characterization of `D=1`
   on block-condition cells; sub-gap (ii) vacuous.
2. `xor-overlap-identity` (xor-overlap) — `D = D_F + D_R − 2C` by bilinearity of parity.
3. `m-le-n-halving-D-zero` (majorization-upper) — `m ≤ n ⟹ D* = 0` via even-multiplicity.
4. `bottom-dominant-halving` (majorization-upper) — `m=n+1, a_n ≥ 2a_{n+1} ⟹ D = a_{n+1}`.
5. `repeated-value-D-zero` (majorization-upper) — repeat in `m=n+1` ⟹ `D* = 0`.
6. `lp-dual-odd-mass-parity` (lp-dual) — `D = 0` infeasible (odd total mass).
7. `lp-dual-even-k-interleaved` (lp-dual) — narrow even-`k` single-adjacent interleaving.

Rejected: none (all 7 pass the bar). The circularity finding in tail-count is recorded as a
negative result (NOT a lemma).

## Goal progress

- Lower bound G1/GAP-C: still OPEN. Sub-gap (ii) vacuous (mass-balance lemma); sub-gap (i)
  (V-shape cell faces) open. Spine sign-pattern route killed (circular). XOR identity +
  inductive reduction + LP sign-fix are genuine new machinery but do NOT close G1.
- Upper bound: n=1,2,3 COMPLETE (certified). General n: three sub-cases closed
  unconditionally (`m ≤ n`, repeated-value, bottom-dominant halving with `a_{n+1} ≤ 1/D_n`);
  GAP-U2 (pair cascade, strictly-decreasing) OPEN, conjectural.
- Total certified lemmas: 31. A solve needs BOTH GAP-C(i) closed AND GAP-U2 closed.
