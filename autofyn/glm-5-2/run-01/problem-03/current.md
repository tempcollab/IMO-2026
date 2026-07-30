# imo-2026-03 — IMO 2026 P3 (Liu Bang & Xiang Yu stick game)

## Status
partial

## Approaches tried
- `majorization-upper` — CHANGES REQUESTED (partial, round 6 REVISE). **HEADLINE: generalized
  the halving lemma to `halving-always-a-nplus1`** (certified round 6): for ANY strictly-decreasing
  m=n+1 config, halving a_1..a_n gives D = a_{n+1} — drops the bottom-dominance hypothesis. Proof
  is a clean parity/block-grouping argument (verified 0/20000 exact-Fraction trials n=2..6 incl.
  edge case a_i=2·a_{n+1}). **Corollary: the a_{n+1} ≤ 1/D_n region is CLOSED for all n**
  unconditionally — narrows GAP-U2 to ONLY the compressed case (a_{n+1} > 1/D_n). O1
  (split-bottom + exact-pair-rest) is **PROVABLY DEAD** (outline-reviewer: exact pairing impossible
  for (5,3,2)/10 for all x ≤ 1/D_n and all patterns; "PL-pairing-feasibility" is a category error).
  The compressed case (O2 split-LARGE-to-match-MEDIUM + bounded-spread pigeonhole) is honestly
  left as **GAP-U2-compressed** (verified 0/6000+ violations n=4, exhaustive n=2; NOT proved). The
  parity obstruction (2n+1 odd ⟹ D ≠ 0 with n marks) is noted — compressed case can only yield
  D = small leftover ≤ 1/D_n.
- `even-packing-upper` — CHANGES REQUESTED (partial, round 6 NEW). PROVED the even-position
  reframe D = 1 − 2E (certified `even-position-reframe`); the tower tightness E*(T_n) =
  (2^n−1)/D_n **upper direction** (halving achieves it = `parallel-halving-saturates-tower`
  restated). **OVERCLAIM FLAGGED:** the builder claims tower tightness "PROVED both directions" but
  the **lower direction** (E*(T_n) ≤ (2^n−1)/D_n) requires D*(T_n) ≥ 1/D_n = the TOWER LOWER
  BOUND, which is GAP-C-OPEN — NOT certified. The claim "for the TOWER specifically the lower
  bound D(T_n) ≥ 1/D_n is certified closed" is FALSE. `tower-even-packing-tight` REJECTED as a
  lemma (lower direction overclaimed; upper is already `parallel-halving-saturates-tower`).
  PROVED `halving-underpacks-compressed` (certified: E_halve = (1−a_{n+1})/2 < (2^n−1)/D_n when
  a_{n+1} > 1/D_n — explains why halving fails for compressed configs). The core gap
  GAP-U2-packing is logically EQUIVALENT to GAP-U2-compressed (trivial: E = (1−D)/2); the
  even-packing lens REFRAMES but does NOT bypass the crux (honestly acknowledged). The exchange
  argument fails (tower is an isolated extremum, discontinuous — pure continuity can't work).
  Verification (Part IV) correct: D* = 0 for compressed configs using ≤ n−1 marks (even count,
  parity obstruction doesn't apply).
- `tail-count` — CHANGES REQUESTED (partial, round 6 ADVANCE). NARROWED GAP-C(i) via the
  **mass-budget breakpoint inequality** (§15, certified `mass-budget-breakpoint-inequality`): at
  a breakpoint of T_n (cascade type), T ≥ 3F − 1 where F = surviving non-dyadic fragment mass,
  T = surviving tower mass. Proved (mass budget: each non-dyadic survivor appears ≥ 3 times,
  consuming ≥ 3w from the 2^n budget; dyadic non-survivors consume ≥ 2^k each). Verified 0
  violations (T_3 cascade 1/24 grid, tightness examples match). **Corollary 15a (proved,
  conditional):** block condition + D=1 at breakpoint ⟹ F=0 (spine dyadic) ⟹ D≥1 by §8
  (T ≤ −1 contradiction). **Corollary 15b (proved):** continuity rules out "all F at −" (D ≤ −1
  on adjacent cell contradicts D=1 vertex by PL continuity). So **block condition is SUFFICIENT
  for D=1 at breakpoints** — but NOT proved to hold. **GAP-C(i)-balance-implies-block REMAINS
  OPEN:** the mass-budget constrains F but doesn't force F=0 without the block-condition
  hypothesis. Any counterexample must have F>0 AND block condition failing. The 0/523
  block-condition verification is CORRECTLY re-classified by ORIGIN (fragment vs tower piece),
  not value-type (the round-5 "failures" were a misclassification bug). The "balance ⟹ block"
  step is NOT advanced by the mass-budget (it constrains magnitudes, not signs).
- `tail-count` — CHANGES REQUESTED (partial, round 5 REVISE). Round 5 (certified):
  **`mass-balance-lemma`** (`D = 2S₊ − D_n` pure algebra; `D = 1 ⟺ S₊ = 2^n ⟺` the
  all-top-`+`/all-below-`−` pattern on a block-condition cell; makes sub-gap (ii) VACUOUS
  — every block-condition `D=1` cell is settled directly by `telescoping-block-lemma` (d),
  no dyadic endpoint needed). **HONEST NEGATIVE RESULT**: the spine sign-pattern /
  multi-swap subset-sum framing (the nosaddle-close explorer's G1-closer) is **CIRCULAR**
  as framed — the "mass identity `F = T + 1`" is EQUIVALENT to `D(spine) = 1` under the
  assumed interleaving pattern (`D = F − T` when pattern holds, so `F − T = 1 ⟺ D = 1`),
  NOT an independent mass identity. Reviewer independently re-derived the decomposition
  `D(spine) = (F − T) + 2(t₊ − f₋)` and reproduced the `Fraction`-exact counterexample:
  `T_3` split `8→5+3, 4→3+1` gives spine `{5,2}`, pattern HOLDS, yet `F − T = 3 = D ≠ 1`.
  The single-swap (`2(t−v)=0⟹t=v`, power-of-2 vs non-power) and multi-swap subset-sum
  both presuppose `S₊ = F` (the pattern), so they are circular. This kills the spine
  sign-pattern route honestly — do NOT chase it. GAP-C sub-gap (i) (V-shape cell faces
  inherit block condition; verified `T_3`/`T_4`, open generally) remains the genuine open
  step. A non-circular argument (V-shape face block-condition inheritance, or a different
  mass/charging identity) is needed.
- `tail-count` — CHANGES REQUESTED (partial, round 4 verified-milestone). Lemma 0,
  layer-cake, D-integral, case-a, n=1 base all PROVED and certified (round 1).
  Round 2 (certified): per-split ΔD formula (§2); frontier recursion
  `D(T_n)+D(T_{n−1})=2^n` + closed form `D(T_n)=(2^{n+1}+(−1)^n)/3≥1` (§3);
  **single-split case (b-i) closed all n** (§4, PL slope-{0,−2}); **multi-split
  dyadic (balanced) case (b-ii-dyadic) closed all n** (§5, level-block dominance);
  PL+breakpoint reduction (§6). Round 3: two-split top-fragment PROVED all n (§7,
  certified `two-split-lower-bound`); even-group strong-breakpoint PROVED all n (§8,
  certified `even-group-spine-lower-bound`, INDEPENDENT from tower-induction S3);
  plateau-connectivity GLOBAL exchange developed (§9, V-shape confirmed, local FAILS).
  Round 4 NEW (certified this round): **GAP-B telescoping-block-lemma** (§11 — D
  constant on a PL cell where each split's fragments sit at same-sign positions;
  if all top-fragments at `+` and all below-tower at `−`, `D = 2^n − (2^n−1) = 1`
  DIRECTLY by the telescoping mass identity, no dyadic endpoint needed;
  non-dyadic generalization of `block-contribution-formula`); **GAP-A
  two-leftover-transport** (§12 — at a spine-3 cascade breakpoint, mass identity
  `a + d = t + 1` ⇒ `D = 1`; corollary of GAP-B(d)). GAP-C (star-shaped transport,
  §13) — OPEN: the G1-closer. Mechanism explained (V-shape cells have `D>1` in the
  interior; min-level set lives on tie FACES where the block condition holds;
  transport moves ALONG tie faces around the V-shape gradient), verified T_3
  (816/816 cascade, 322/322 split-larger, 17/17 split-tower) and T_4 (165/165
  cascade 3-split), NOT proved generally. Two sub-gaps: (i) V-shape cell faces
  inherit the block condition (verified T_3, open general); (ii) block-condition
  cells without the "all-top-+, all-below-−" sign pattern and without a dyadic
  endpoint (undetermined by GAP-B alone). Numerics correctly labeled
  verification-not-proof (per round-2 rule). GAP (U): upper bound general n
  deferred to `majorization-upper`.
- `tower-induction` — CHANGES REQUESTED (partial, round 3 verified-milestone).
  Round 2 (certified): F-block formula, F-rec (general parity-vector frontier
  recursion), F-min (`1≤D≤2^n−1` for every balanced refinement of `T_n`, all n —
  CLOSES all-balanced-splits sub-case of case (b)). Round 3 NEW (certified this
  round): **Lemma S1 spine-pair-cancellation** (value-agnostic, `D(M)=D(spine)`,
  0 mismatches over 20k configs); **Lemma S2 strong-breakpoint-group-structure**
  (non-dyadic fragments form adjacent-equal groups `≥ 2`; even groups cancel,
  odd leave one leftover); **Lemma S3 even-group-spine-lower-bound** (`D ≥ 1` at
  even-group strong breakpoints, all n — geometric dominance `2^{k_1} > 2^{k_1}−1`
  + nonempty via odd-total-mass; CLOSES even-group strong-breakpoint sub-case of
  G1 for all n, INDEPENDENT from `tail-count`'s §8). GAP (G2-odd): odd-count
  non-dyadic leftovers — OPEN (leftover sign is GLOBAL position-parity; frontier
  recursion does NOT extend to unbalanced splits; odd-group minimizers exist at
  `D=1`; candidate mechanism = splitting-tree sign-bookkeeping, undeveloped).
  Shared wall with `tail-count`'s G1 (opposite machinery: block/spine vs
  PL/plateau). GAP (U1, U2): upper bound general n — fallback only; deferred to
  `majorization-upper`.
- `gaps-leftover` — CHANGES REQUESTED (partial, round 3 NEW). Genuinely-different
  lower-bound framing: gaps+leftover identity + pairing/leftover bound + top-split
  inductive decomposition + scope-gap handling. Round 3 (certified): **Lemma G1
  gaps-leftover-identity** (`D = Σ(p_{2k−1}−p_{2k}) + [m odd]p_m`, both parities
  via phantom-zero padding; pure telescoping, 0 mismatches over 20k configs);
  **Lemma G2 pairing-leftover-bound** (`D ≥ p_m` odd `m`, `D ≥ 0` even `m`;
  closes the `p_m ≥ 1` sub-region of the tower lower bound). Top-split
  decomposition (G3, reduction conditional on `W(n−1)` — correctly NOT submitted
  for certification). Scope-gap handling: even-`m` / fewer-marks cases reduced to
  certified lemmas; uniform padded identity makes charging target well-defined
  both parities. GAP (G1 crux): deficit-covering inequality `Σ gaps + leftover
  ≥ 1` when `p_m < 1` — OPEN (charging/matching argument against tower skeleton
  unproved; verified `n=3,4`, 60k+ trials, 0 violations; deficits covered exactly
  at minimizers). The "1 is conserved" picture is a CONJECTURE supported by
  numerics, not a proof. No upper-bound progress (deferred to `majorization-upper`).
- `lp-dual-certificate` — CHANGES REQUESTED (partial, round 5 REVISE). **LP-2 SIGN
  ERROR FIXED and scipy-verified.** The corrected dual is the **inequality**
  `m_j − m_{j−1} ≤ d_j` with `d_j = (−1)^j − y_eq[b(j)]`, a nonneg mountain
  `m_k = −y_ub[k] ≥ 0` (so `y_ub ≤ 0`, NOT `≥ 0`) with sentinels `m_{−1} = m_{m−1} = 0`,
  and **slack** `s_j = d_j − (m_j − m_{j−1}) ≥ 0` with `s_j · p_j = 0` (complementary
  slackness — round-4's *equality* is valid only at interior points; at a breakpoint
  vertex with `p_j = 0` the constraint is slack). Reviewer independently re-derived and
  scipy-verified: round-4 infeasible `T_2` demo `b=(0,1,0,2,2)` now CORRECTED (uniform
  cert `y_eq=(+1,−1,−1), y_ub=0` feasible, `d=(0,0,0,0,2)`, slack `s_4=2` at `p_4=0`
  vertex, objective `1 = primal min`); the round-4 claimed cert `y_eq=(+1,−1,0)` (obj 2)
  correctly INFEASIBLE. Narrow interleaved sub-class parity FIXED: single-adjacent-2-piece
  interleaving cert works for `k` EVEN (0-based) with single-bump mountain `m_k=1`
  (round-4 had `k` odd, the opposite; reviewer scipy-confirmed odd-`k` needs
  `m_k ≤ −1`, violating `m ≥ 0`). Round 5 NEW (certified): **`lp-dual-odd-mass-parity`**
  (`D=0` infeasible by odd-total-mass parity — `D=0` ⟹ all adjacent pairs equal + trailing
  0 ⟹ even total mass, contradicting `D_n` odd; rigorous but insufficient since `min D`
  real); **`lp-dual-even-k-interleaved`** (narrow even-`k` single-adjacent interleaving
  closed via single-bump mountain). **Integrality shortcut attempted and FAILED** —
  reviewer exhaustively confirmed the per-type LP is NOT totally unimodular (`min D = 5/3`
  for `b=(0,1,0,0,2,1,3)` n=3; `13/3`, `17/3` also found), so the parity argument rules
  out only `min D = 0`, not `min D ∈ (0,1)`. GAP-LP1 (clean types) UNAFFECTED (y_ub=0
  makes sign irrelevant; certified intact). GAP-LP2 (structural sign-pattern feasibility
  for general interleaved types) OPEN, honestly G1-equivalent by strong duality (NOT a
  shortcut, per round-4 rule). Farkas route honestly flagged circular.
- `lp-dual-certificate` — CHANGES REQUESTED (partial, round 4 NEW). 4th genuinely-orthogonal
  LOWER-bound framing: LP strong duality / Farkas, certifying `min D ≥ 1` per
  combinatorial type from the constraint structure (bin-sum equalities + sort order).
  **GAP-LP1 (clean types) PROVED all n, both parities** — certified `lp-dual-clean-types`:
  for every clean type (each bin monochromatic in position parity), the dual cert
  `y_ub=0, y_eq[t]=s_t` is feasible, top-bin-at-`+1` by the `D≥0` mass contradiction,
  dyadic dominance `2^n > 2^n−1` gives objective `≥1`, LP strong duality gives `min D ≥ 1`.
  Closes the clean-types sub-case of G1 for all n. **SIGN ERROR in LP-2 (the dual
  derivation):** the mountain direction is flipped (builder claims nonneg prefix sums
  of `d_k = y_eq[b(k)] − (−1)^k`; correct is nonpos, or equivalently `d_k = (−1)^k − y_eq[b(k)]`
  for nonneg). The interleaved T_2 demonstrative example is INFEASIBLE (cert objective 2
  violates strong duality — actual LP min = 1, correct dual max = 1, verified scipy).
  The narrow interleaved sub-class has the wrong parity (k odd should be k even).
  LP-3 (clean types) is UNAFFECTED (y_ub=0, sign irrelevant). GAP-LP2 (structural
  sign-pattern feasibility lemma) OPEN, honestly marked G1-equivalent by strong duality
  (not a shortcut, per outline-reviewer correction). Non-circularity valid (refinement-min
  dual, not the round-3 claim-game dual). Gaps to close: fix LP-2 sign error, remove/correct
  infeasible example, fix sub-class parity, attack GAP-LP2 with corrected dual.
- `xor-overlap` — CHANGES REQUESTED (partial, round 5 NEW). 5th genuinely-orthogonal
  LOWER-bound framing: an **exact overlap/correlation decomposition** of the `D`-integral
  (NOT global-position parity, PL/variational, block/spine, gaps-leftover, or LP duality).
  Round 5 (certified): **`xor-overlap-identity`** (`D(M) = D_F + D_R − 2C` by bilinearity
  of parity; `Fraction`-exact 0/3000 refinements of `T_2..T_5`); **tight base `n=1`**
  (`D_F = 2C` exactly, `D = 1` for every top split); **inductive reduction**
  `G1(n) → G1(n−1) + GAP-X` (mark accounting sound; case (a) routed to certified
  `tower-top-unsplit`). GAP-X (overlap bound `C ≤ (D_F+D_R−1)/2`) OPEN, honestly
  G1-equivalent by (XOR-bound). Four attempted routes all documented with precise
  obstructions (trivial/Cauchy-Schwarz give only `D ≥ 0`; sufficient `D_F ≥ 2C` FAILS
  543/2196 breakpoints; dyadic-`R` covers only already-closed sub-case; per-fragment
  charging hits the global-interleaving wall). Non-circularity reproduction (dyadic-`R`
  reduces to certified `dyadic-refinement-lower-bound`).
- `majorization-upper` — CHANGES REQUESTED (partial, round 5 REVISE). **DROPPED** the
  V(n)←V(n−1) IH and the 3-mark cascade (both refuted as phantom-crux chasers: the crux
  regime gives `D* = 0` or tiny; the IH overshoots because V(n−1) is a worst-case bound
  blind to slack). NEW spine: the **DIRECT ADAPTIVE STRATEGY** (no induction on `n`).
  Round 5 NEW (certified): **`m-le-n-halving-D-zero`** (GAP-U3: `m ≤ n ⟹ D* = 0` by the
  even-multiplicity lemma — block of `2k` equal values contributes `v·(k−k)=0`; halving
  all pieces gives every value even multiplicity); **`bottom-dominant-halving`**
  (`m = n+1`, `a_n ≥ 2 a_{n+1} ⟹ D = a_{n+1}` by halving the `n` largest, residual at
  position `2n+1`; closes the `a_{n+1} ≤ 1/D_n` sub-case incl. the dominant tower-tail
  family, tower `T_n` tight); **`repeated-value-D-zero`** (`m = n+1` with a repeat ⟹
  `D* = 0` by `spine-pair-cancellation` S1 + halving the `≤ n−1`-piece spine +
  even-multiplicity). These close three sub-cases of the general-n upper bound
  unconditionally. GAP-U2 (pair-matching cascade for strictly-decreasing `m = n+1` where
  halving exceeds target or doesn't apply) OPEN, honestly a CONJECTURE (verified 3000
  trials n=4 worst ratio 0.52; NOT proved). Round-4 reviewer flag (`a_{n+1} ≤ 1/D_n`
  false-as-stated for non-dominant tower-tail) handled: the lemma scopes to
  bottom-dominant configs and states `a_{n+1} ≤ 1/D_n` as a hypothesis of the closed
  sub-case. `n=1,2,3` UPPER bounds COMPLETE (certified base, imported; the direct
  strategy recovers V(3)). GAP-U2 is the primary hard step for n≥4.
- `majorization-upper` — CHANGES REQUESTED (partial, round 4 REVISE). **MAX-BOUND
  CONJECTURE `D* ≤ M/2^n` FALSIFIED** by exact-Fraction counterexample
  `(7,6,5,3)/21` (n=3): `D*=1/21`, `M/8=1/24`, ratio `8/7>1` — VIOLATION exact;
  the actual target `1/D_3=1/15` is NOT violated (`1/21<1/15`); the answer
  `c(n)=2^n/(2^{n+1}−1)` survives. Max-bound dropped as spine. **NEW spine: V(n) =
  M_2/2^{n−1}** (second-largest piece). Round 4 NEW (certified): **`n2-max-bound`**
  (n=2 `D* ≤ max/4`, derived from `n2-upper-bound-complete`, all four regimes);
  **`v3-upper-bound`** (V(3): `D* ≤ M_2/4` for every n=3 config, two-case split —
  dominant `a_1≥2a_2` halve, non-dominant `a_1<2a_2` pair, both using `n2-max-bound`
  on the rest; outline-reviewer's dominant-needs-halving flag addressed). **n=3
  UPPER BOUND COMPLETE: `D* ≤ 1/15 = 1/D_3` for every n=3 Liu config** (all four
  regimes A/B1/C/B2 closed unconditionally; A/B1 by certified U2/U3, C/B2 by V(3)).
  OVERCLAIM FLAGGED: the builder writes `c(3) = 8/15` combining with the lower
  bound, but the n=3 LOWER bound is PARTIAL (G1/GAP-C open for n=3); the proved
  result is `c(3) ≤ 8/15`, not equality. V(n≥4) CONJECTURE (0 violations n=3,4,5,
  tight at tower, unproved in the crux `a_1<2a_2 ∧ a_3>a_1/2`). MB-Dom/MB-Pair
  re-derived under V(n−1) IH as conditional reductions (W(n−1) refuted for n−1≥3).
  The mutual W/V recursion + 3-mark pairing cascade are candidate structures
  (conjectures, not proofs). `n=1,2,3` UPPER bounds COMPLETE (n=1,2 certified base;
  n=3 this round).
- `d-potential` — HOLD (round 1 verified-milestone). Φ=D shown circular; no concrete Φ.
- `self-similar` — HOLD (subsumed by tower-induction's frontier recursion).
- `balanced-configs` — RETIRED (B3 circular); Lemma B1 harvested into majorization-upper.

## Current best
Proven and certified (importable from `results/imo-2026-03/lemmas/` — 31 lemmas total):

Round-1 (6):
1. **Lemma 0** (`claim-game-odd-index.md`) — claim game value = odd-index sum; greedy optimal.
2. **Lower bound case (a)** (`tower-top-unsplit.md`) — top unsplit ⇒ `D ≥ 1/D_n`, all n, no IH.
3. **n=1 base** (`n1-base-both-bounds.md`) — `c(1) = 2/3` (both bounds).
4. **Layer-cake identity** (`layer-cake-odd-index.md`) — odd-index = `∫⌈N(t)/2⌉dt`.
5. **D-integral** (`D-equals-parity-integral.md`) — `D = ∫(N(t) mod 2)dt`.
6. **Closed form** (`closed-form-answer.md`) — `r_n = 2^n/(2^{n+1}−1)` (algebraic identity; NOT a proof c(n)=r_n).

Round-2 (7):
7. **Frontier recursion** (`frontier-recursion.md`) — `D(T_n)+D(T_{n−1})=2^n`, closed form
   `D(T_n)=(2^{n+1}+(−1)^n)/3≥1`; general parity-vector recursions; balanced top split `T_n → T_{n−1}`.
8. **Block-contribution formula** (`block-contribution-formula.md`) — `D(M)=Σ_k 2^k(−1)^{C_k}(n_k mod 2)` for dyadic refinements.
9. **Dyadic-refinement lower bound** (`dyadic-refinement-lower-bound.md`) — `1≤D≤2^n−1` for every balanced-split refinement of `T_n`, all n.
10. **Single-split top lower bound** (`single-split-top-lower-bound.md`) — one split of `T_n`'s top ⇒ `D ≥ D(T_{n−1}) ≥ 1`, all n.
11. **Parallel-halving saturates tower** (`parallel-halving-saturates-tower.md`) — Xiang's n-mark halving of `T_n` gives `D=1/D_n` exactly (upper-bound witness).
12. **PL breakpoint minimum** (`pl-breakpoint-minimum.md`) — global min of `D` over refinements is at a breakpoint (tie) config (general).
13. **n=2 upper bound complete** (`n2-upper-bound-complete.md`) — `c(2)≤4/7`, tower `T_2` unique equality; exhaustively verified.

Round-3 (6, NEW — all certified this round):
14. **Two-split lower bound** (`two-split-lower-bound.md`) — every 2-mark top-fragment-split
    refinement of `T_n` has `D ≥ D(T_{n−2}) ≥ 1`, min at the dyadic cascade, all `n`
    (block-contribution + parity-constrained geometric bound, four-case check).
    **Scope:** top-fragment-split type fully proved; Type C (second split on a tower
    piece) verified `n=3..7`, NOT proved (gap). Type-4 (r-tower-tie) breakpoints
    reduce to Case 1 by config symmetry (verified, not separately proved).
15. **Spine pair-cancellation** (`spine-pair-cancellation.md`) — for ANY sorted multiset,
    removing adjacent-equal pairs preserves `D`; the spine is strictly-decreasing
    distinct values with `D(M) = D(spine(M))`. Value-agnostic (no power-of-2 structure).
16. **Strong-breakpoint group structure** (`strong-breakpoint-group-structure.md`) — at a
    strong breakpoint of `T_n`, non-dyadic fragments form adjacent-equal groups `≥ 2`;
    even groups fully cancel, odd leave one leftover.
17. **Even-group spine lower bound** (`even-group-spine-lower-bound.md`) — at an even-group
    strong breakpoint of `T_n`, `D ≥ 1` (all n). Geometric dominance + odd-total-mass.
    **Closes the even-group strong-breakpoint sub-case of G1 for all n** — proved
    INDEPENDENTLY in `tail-count` §8 (PL/variational) and `tower-induction` S3 (spine).
18. **Gaps+leftover identity** (`gaps-leftover-identity.md`) — `D = Σ(p_{2k−1}−p_{2k}) + [m odd]p_m`
    for any sorted multiset, both parities (phantom-zero padding). Pure telescoping.
19. **Pairing/leftover bound** (`pairing-leftover-bound.md`) — `D ≥ p_m` (odd `m`), `D ≥ 0`
    (even `m`); closes the `p_m ≥ 1` sub-region of the tower lower bound.

Round-4 (5, NEW — all certified this round):
20. **Telescoping block lemma** (`telescoping-block-lemma.md`) — on a PL cell where each
    split's fragments sit at same-sign positions (block condition), `D` is CONSTANT; if all
    top-fragments at `+` and all below-tower pieces at `−`, `D = 2^n − (2^n−1) = 1` directly
    (no dyadic endpoint needed). Non-dyadic generalization of `block-contribution-formula`.
    Settles block-condition cells (spine-3/5/7 cascade, split-larger, split-tower block cells).
21. **Two-leftover transport** (`two-leftover-transport.md`) — at a spine-3 cascade breakpoint
    of `T_n`, mass identity `a + d = t + 1` ⇒ `D = a − t + d = 1`. Corollary of
    `telescoping-block-lemma` (d); spine-length-3 instance of `gaps-leftover-identity`.
22. **n = 2 Max-bound** (`n2-max-bound.md`) — for every `m ≤ 3` multiset, `D* ≤ max/4`.
    Derived from `n2-upper-bound-complete` (all four regimes A/C/B1/B2). Equality iff `T_2`.
23. **V(3) upper bound** (`v3-upper-bound.md`) — for every n=3 Liu config (`m ≤ 4`),
    `D* ≤ M_2/4` (second-largest piece). Two-case split: dominant `a_1≥2a_2` halve,
    non-dominant `a_1<2a_2` pair, both applying `n2-max-bound` to the rest. Equality at `T_3`.
24. **LP-dual clean-types** (`lp-dual-clean-types.md`) — for every clean combinatorial type
    (each bin monochromatic in position parity) of a `≤n`-mark refinement of `T_n`,
    `min D ≥ 1` on the cell by LP strong duality (cert `y_ub=0, y_eq[t]=s_t`, objective
    `≥ 1` by dyadic dominance `2^n > 2^n−1`). Closes the clean-types sub-case of G1 for all n.

Round-5 (7, NEW — all certified this round):
25. **Mass-balance lemma** (`mass-balance-lemma.md`) — on a block-condition cell,
    `D = 2S₊ − D_n` (pure algebra); `D = 1 ⟺ S₊ = 2^n ⟺` the all-top-`+`/all-below-`−`
    pattern. Makes sub-gap (ii) of GAP-C VACUOUS: every block-condition `D=1` cell is
    settled by `telescoping-block-lemma` (d). Caveat: characterizes `D=1` cells; does NOT
    prove `D ≥ 1` on every block cell nor address V-shape cells.
26. **XOR-overlap identity** (`xor-overlap-identity.md`) — `D(M) = D_F + D_R − 2C` where
    `C = |Ω_F ∩ Ω_R|` is the overlap of the two odd-parity regions, by bilinearity of
    parity `(a+b) mod 2 = (a mod 2) + (b mod 2) − 2(a mod 2)(b mod 2)`. `Fraction`-exact
    0/3000. Structural decomposition (does NOT close G1; GAP-X open, G1-equivalent).
27. **m ≤ n halving ⇒ D=0** (`m-le-n-halving-D-zero.md`) — for `m ≤ n` Liu configs, Xiang
    halves every piece (`m ≤ n` marks); the even-multiplicity lemma (block of `2k` equal
    values contributes `v·(k−k)=0`) gives `D = 0`. Closes the `m ≤ n` case of the upper
    bound for ALL n.
28. **Bottom-dominant halving** (`bottom-dominant-halving.md`) — for `m = n+1` with
    `a_n ≥ 2 a_{n+1}`, halving the `n` largest pieces (residual `a_{n+1}` at position
    `2n+1`) gives `D = a_{n+1}`. Closes the `a_{n+1} ≤ 1/D_n` sub-case (incl. dominant
    tower-tail; tower `T_n` tight).
29. **Repeated-value ⇒ D=0** (`repeated-value-D-zero.md`) — for `m = n+1` with a repeated
    value, `spine-pair-cancellation` S1 leaves a `≤ n−1`-piece spine; halving all spine
    pieces (`≤ n−1 ≤ n` marks) gives every value even multiplicity; `D = 0`. Closes the
    repeated-value sub-case of `m = n+1` for ALL n.
30. **LP-dual odd-mass parity** (`lp-dual-odd-mass-parity.md`) — `D = 0` infeasible on any
    type-cell: `D=0` ⟹ all adjacent pairs equal + trailing 0 ⟹ even total mass,
    contradicting `D_n = 2^{n+1}−1` odd. Rigorous sub-result (`min D > 0`); insufficient
    for G1 (per-type LP not TU — `min D` real, e.g. `5/3`, `13/3`, `17/3`).
31. **LP-dual even-k interleaved** (`lp-dual-even-k-interleaved.md`) — narrow sub-class:
    single-adjacent-2-piece interleaving at even `k` (0-based), rest clean, closed by a
    single-bump mountain `m_k = 1` saturating (★) at `j = k, k+1`; objective `≥ 1` by
    dyadic dominance. Odd-`k` would violate `m ≥ 0` (honestly noted).

Round-6 (4, NEW — all certified this round):
32. **Halving-always-a-nplus1** (`halving-always-a-nplus1.md`) — for ANY strictly-decreasing
    m=n+1 Liu config, halving a_1..a_n gives D = a_{n+1} (parity/block-grouping; edge case
    a_i=2·a_{n+1} handled). Drops the bottom-dominance hypothesis of `bottom-dominant-halving`.
    **Closes the a_{n+1} ≤ 1/D_n region for all n unconditionally.** Verified 0/20000.
33. **Even-position reframe** (`even-position-reframe.md`) — D = 1 − 2E, E = even-position sum;
    Xiang minimizes D ⟺ maximizes E. Upper bound D* ≤ 1/D_n ⟺ E* ≥ (2^n−1)/D_n. Trivially
    correct from Lemma 0 + total = 1. Makes GAP-U2 equivalence transparent.
34. **Halving underpacks compressed** (`halving-underpacks-compressed.md`) — halving gives
    E_halve = (1−a_{n+1})/2; in compressed case (a_{n+1} > 1/D_n), E_halve < (2^n−1)/D_n.
    Diagnostic: explains why halving closes the a_{n+1} ≤ 1/D_n region but not the compressed
    region.
35. **Mass-budget breakpoint inequality** (`mass-budget-breakpoint-inequality.md`) — at a
    breakpoint of T_n (cascade type), T ≥ 3F − 1 (F = surviving non-dyadic fragment mass, T =
    surviving tower mass). Proved (mass budget: each non-dyadic survivor appears ≥ 3 times).
    **Corollary:** block condition + D=1 at breakpoint ⟹ F=0 ⟹ D≥1 by §8. Continuity rules out
    "all F at −". **Honest caveat:** constrains F but doesn't prove block condition without it;
    GAP-C(i) narrowed, not closed.

**REJECTED this round:**
- `tower-even-packing-tight` (`even-packing-upper` Part II) — REJECTED: the builder claims
  "E*(T_n) = (2^n−1)/D_n PROVED both directions" but the LOWER direction (E*(T_n) ≤
  (2^n−1)/D_n) requires D*(T_n) ≥ 1/D_n = the tower lower bound, which is GAP-C-OPEN. The upper
  direction is correct but already covered by `parallel-halving-saturates-tower`.

**REJECTED as standalone (conditional reductions, files marked "REDUCTION"):**
- `max-bound-dominant` (MB-Dom) — Max-bound `D* ≤ M/2^n` for dominant `a_1 ≥ 2a_2`,
  conditional on Max-bound IH `W(n−1)` (the Max-bound conjecture itself, proved only
  for base `n=0,1,2`). Analogous to round-2 `U2`.
- `max-bound-pairing-small-third` (MB-Pair) — Max-bound for non-dominant
  `a_1 < 2a_2 ∧ a_3 ≤ a_1/2`, conditional on `W(n−1)`. Analogous to round-2 `U3`.

**Best proven results:**
- **Lower bound `c(n)≥2^n/D_n`** — proved for ALL n in: case (a) top-unsplit;
  case (b-i) single-split; case (b-ii-dyadic) all-balanced-splits; case (b-ii)
  2-split top-fragment-split; even-group strong-breakpoint sub-case (two independent
  proofs); **block-condition cells** (`D=1` by telescoping mass identity, GAP-B);
  **spine-3 cascade** (GAP-A); **clean-types** (LP-dual); NEW round 5 — **sub-gap (ii)
  of GAP-C VACUOUS** (certified `mass-balance-lemma`: every block-condition `D=1` cell
  has the all-top-`+`/all-below-`−` pattern, settled by GAP-B(d) directly); **XOR
  identity + inductive reduction** (certified `xor-overlap-identity`, 5th framing).
  Non-dyadic multi-split `k ≥ 3` (G1/GAP-C) OPEN for all `n≥2` (the odd-count/
  deficit-covering crux — attacked from FIVE framings: PL/variational `tail-count`,
  block/spine `tower-induction`, gaps/leftover `gaps-leftover`, LP/Farkas
  `lp-dual-certificate`, overlap/correlation `xor-overlap` — all converging on the same
  wall). `n=1` fully proved. `n=2,3`: lower bound PARTIAL (GAP-C open even for n=3;
  verified T_3 816/816+322/322+17/17, NOT proved generally).
- **Upper bound `c(n)≤2^n/D_n`** — `n=1` proved (certified); `n=2` COMPLETE
  (certified); **`n=3` COMPLETE (round 4, unconditional)**: `D* ≤ 1/15 = 1/D_3`
  for every n=3 Liu config (all four regimes A/B1/C/B2 closed; A/B1 by certified U2/U3,
  C/B2 by V(3) = `M_2/4` proved via two-case split + `n2-max-bound`). General n≥4
  (round 5 + NEW round 6): three sub-cases closed UNCONDITIONALLY by the direct adaptive
  strategy (no induction on n) — **(U3) `m ≤ n` ⟹ `D* = 0`** (halving all pieces,
  even-multiplicity lemma, certified `m-le-n-halving-D-zero`); **repeated-value in
  `m = n+1` ⟹ `D* = 0`** (certified `repeated-value-D-zero`); **strictly-decreasing
  `m = n+1` with `a_{n+1} ≤ 1/D_n` ⟹ `D* ≤ a_{n+1} ≤ 1/D_n`** (NEW round 6: certified
  `halving-always-a-nplus1`, drops the bottom-dominance hypothesis — closes the
  a_{n+1} ≤ 1/D_n region for ALL n unconditionally, includes the tower-tail family
  and the non-bottom-dominant regime). GAP-U2-compressed OPEN: strictly-decreasing
  `m = n+1` with **`a_{n+1} > 1/D_n`** (compressed) — O1 (exact pairing) PROVABLY DEAD
  (outline-reviewer: impossible for (5,3,2)/10 all x≤1/D_n); O2 (split-large-to-match-medium)
  + bounded-spread pigeonhole are honest candidate mechanisms (verification 0/6000+ n=4,
  exhaustive n=2; NOT proved). The even-packing reframe (certified `even-position-reframe`,
  `halving-underpacks-compressed`) reframes GAP-U2-compressed as E* ≥ (2^n−1)/D_n but is
  logically EQUIVALENT (not a bypass). The V(n)←V(n−1) IH and 3-mark cascade are DROPPED
  (refuted as phantom-crux chasers). Max-bound `D* ≤ M/2^n` REFUTED (`(7,6,5,3)/21`).
  **GAP-U2 NARROWED: only the compressed case (a_{n+1} > 1/D_n) remains open.**
- **Combined:** `c(1)=2/3` fully proved. `c(2)=4/7`: upper bound proved; lower bound
  partial (pending G1). `c(3)`: upper bound `c(3)≤8/15` PROVED (round 4);
  lower bound partial (GAP-C open for n=3); equality `c(3)=8/15` NOT yet established.
  `c(n)` n≥4: both bounds partial (lower G1/GAP-C; upper GAP-U2-compressed).

Numerically verified (not proved): `c(n)=2^n/(2^{n+1}−1)` holds n=1..4 (0 violations
over 300k+ random refinements per n; equality at balanced-pairs config
`{2^{n−1},2^{n−1},…,2,2,1,1,1}/D_n`). Max-bound `D* ≤ M/2^n` verified 0 violations
n=2,3,4 (2860+ configs), tight uniquely at the tower.

## Full proof
Not yet complete. Two load-bearing gaps remain:
- **Lower bound (G1 / GAP-C, non-dyadic multi-split `k ≥ 3`):** when Xiang uses `≥ 3`
  marks with at least one unbalanced split of `T_n`, prove `D ≥ 1`. The PL+breakpoint
  reduction lands the global min at a breakpoint config; the 2-split top-fragment
  sub-case (certified `two-split-lower-bound`), even-group strong-breakpoint sub-case
  (certified `even-group-spine-lower-bound`, two independent proofs), single-split +
  dyadic breakpoints, **block-condition cells** (certified `telescoping-block-lemma`,
  `D=1` by mass identity), **spine-3 cascade** (certified `two-leftover-transport`),
  and **clean-types** (certified `lp-dual-clean-types`, LP strong duality) are
  settled. NEW round 5: **sub-gap (ii) VACUOUS** (certified `mass-balance-lemma`).
  NEW round 6: **mass-budget breakpoint inequality** (certified
  `mass-budget-breakpoint-inequality`): at a breakpoint of T_n, T ≥ 3F − 1; block
  condition + D=1 ⟹ F=0 (spine dyadic) ⟹ D≥1 by §8; continuity rules out "all F at −".
  **Block condition is SUFFICIENT for D=1 at breakpoints** — but NOT proved to hold.
  The open step is **GAP-C(i)-balance-implies-block**: prove the block condition (or
  F=0) at D=1 breakpoints directly. The mass-budget constrains F but doesn't force F=0
  without the block condition. Any counterexample must have F>0 AND block condition
  failing. **The spine sign-pattern / multi-swap subset-sum framing is CIRCULAR**
  (round 5): "F=T+1" ≡ D=1 under the assumed pattern (Fraction-exact: spine {5,2},
  F−T=3≠1). FIVE framings converge here (all OPEN on the same wall): `tail-count`,
  `tower-induction`, `gaps-leftover`, `lp-dual-certificate`, `xor-overlap`. Verified
  `n≤6` and T_3 exhaustively (816/816+322/322+17/17); open generally.
- **Upper bound (general n, n≥4, GAP-U2-compressed):** exhibit an explicit Xiang strategy
  (≤ n adaptive marks) forcing `D ≤ 1/D_n` against every Liu config. n=1,2,3 PROVED
  (certified). NEW round 6: the direct adaptive strategy (no induction on n) closes
  THREE sub-cases unconditionally for general n — **`m ≤ n` ⟹ `D* = 0`** (certified
  `m-le-n-halving-D-zero`); **`m = n+1` with a repeat ⟹ `D* = 0`** (certified
  `repeated-value-D-zero`); **`m = n+1` strictly-decreasing with `a_{n+1} ≤ 1/D_n` ⟹
  `D* ≤ a_{n+1} ≤ 1/D_n`** (NEW round 6: certified `halving-always-a-nplus1` — drops
  the bottom-dominance hypothesis, closes the a_{n+1} ≤ 1/D_n region for ALL n).
  GAP-U2 NARROWED to **GAP-U2-compressed**: strictly-decreasing `m = n+1` with
  **`a_{n+1} > 1/D_n`** (compressed) — O1 (exact pairing) PROVABLY DEAD; O2
  (split-large-to-match-medium) + bounded-spread pigeonhole are honest candidate
  mechanisms (verification 0/6000+ n=4, exhaustive n=2; NOT proved). The even-packing
  reframe (certified `even-position-reframe`, `halving-underpacks-compressed`) is
  logically EQUIVALENT to GAP-U2-compressed (E* ≥ (2^n−1)/D_n ⟺ D* ≤ 1/D_n), not a
  bypass. The V(n)←V(n−1) IH and 3-mark cascade are DROPPED. Max-bound REFUTED.
