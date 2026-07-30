# Round 5 proof-outliner field — imo-2026-03

Conjectured answer (NOT proven as equality): `c(n) = 2^n/(2^{n+1}−1)`. Two walls remain:
the lower G1 (non-dyadic multi-split, GAP-C) and the upper V(n≥4) crux. This round's three
explorers reshape both: the nosaddle explorer found a direct GAP-C close (mass-balance +
spine sign-pattern lemma), the upper explorer found the V(n≥4) crux is a phantom (direct
halving strategy), and the 5th-framing explorer found a genuinely-new XOR/overlap angle.

---

## imo-2026-03

### tail-count — REVISE (close GAP-C via the spine sign-pattern lemma)
Target: the whole lower bound `D ≥ 1` for every `≤ n`-mark Xiang refinement of `T_n`, all n
(equivalently `c(n) ≥ 2^n/D_n`); combined with the certified upper bound for n≤3 this yields
`c(3) = 8/15` and the general-n lower bound.
Technique: PL/breakpoint reduction + mass-balance sign-forcing + combinatorial subset-sum
(the telescoping mass identity at the spine level).
Skeleton:
  1. By `pl-breakpoint-minimum` (certified), the global min of D over all refinements is at a
     breakpoint (tie) config. Reduce to proving `D ≥ 1` at every breakpoint.
  2. By `spine-pair-cancellation` (S1, certified), adjacent-equal pairs cancel, so
     `D(config) = D(spine)` where the spine is strictly-decreasing: tower-valued pieces
     (unsplit tower pieces, distinct powers of 2) + unpaired fragments (non-tower values).
  3. MASS-BALANCE LEMMA (immediately certifiable, 3-line proof): on any block-condition
     cell, `D = 2S₊ − D_n` where `S₊` = mass at + positions. `D = 1 ⇔ S₊ = 2^n`. The top
     piece (value `2^n`) is all-at-+ or all-at-−. If all-at-−: `S₊ ≤ 2^n−1 < 2^n ⇒ D ≤ −1`.
     If all-at-+: `S₊ = 2^n + (tower mass at +)`, so `S₊ = 2^n ⇔` all tower pieces at −.
     This proves sub-gap (ii) (block-condition cells without the all-top-+/all-below-−
     pattern and without a dyadic endpoint) is VACUOUS.
  4. SPINE SIGN-PATTERN LEMMA (the closer, the hard step — GAP-C): at every `D = 1`
     breakpoint of `T_n`, the spine interleaves as (fragment, tower, fragment, tower, …)
     with ALL fragments at + (odd) positions and ALL tower-valued pieces at − (even)
     positions. Then `D(spine) = (Σ fragments) − (Σ towers) = 1` by the mass identity
     `F = T + 1` (total mass `D_n` odd, paired mass even ⇒ spine mass `S = F+T` odd ⇒
     `D = 1 ⇔ S₊ = (S+1)/2 = F`, so `S₊ = F` is FORCED). Verified 0/523 violations across
     T_3/T_4/T_5.
  5. Conclude: every `D = 1` breakpoint is settled by the spine lemma (GAP-B(d) at the
     spine level); every `D > 1` breakpoint is fine; `min D ≥ 1`. G1 closes for all n.
Key lemmas (claim + one-line mechanism):
  - Mass-balance `D = 2S₊ − D_n` on block-condition cells — because D = odd-index sum and
    the block condition makes each split's two fragments share a position-parity.
  - Spine mass identity `F = T + 1` — because `D_n = 2^{n+1}−1` is odd, paired mass is even
    (each pair `2v`), so the unpaired spine mass `S = F+T` is odd, and `D = 1 ⇔ S₊ = F`.
  - Single-swap impossibility: swapping one fragment `v` (at +) with one tower `t` (at −)
    changes D by `2(t−v)`; `D = 1` preserved ⇒ `t = v`, but `t` is a power of 2 and `v` is
    not. RIGOROUS.
Open gaps:
  - GAP-C-hard = the MULTI-swap argument (step 4): swapping `k` fragments (total `f`) with
    `j` towers (total `t`) preserves `D = 1` iff `f = t`, requiring a subset-sum equality
    between fragments and tower pieces. Single-swap is rigorous (power-of-2 vs non-power);
    the MULTI-swap (subset-sum) is verified 0/523 but NOT proved. The naive value-type
    argument FAILS in isolation (`3 = 2+1`); the mass identity + breakpoint structure must
    supply the obstruction. THIS IS THE LOAD-BEARING UNPROVED STEP.
Cases to cover: all split types (cascade, split-larger, split-tower) at `D = 1`; the
enumeration table (523 configs, 0 violations) is verification-not-proof.
Watch out for: (a) the multi-swap subset-sum obstruction is NOT just "powers of 2 vs
non-powers" — `3 = 2+1` is a counterexample in isolation; the breakpoint structure (fragments
come from splitting powers of 2, so their values are tied to the tower structure) is what
must prevent the equality. (b) The spine lemma operates at the SPINE level (after pair
cancellation), NOT the full-config level — the all-top-+/all-below-− pattern at full config
is IMPOSSIBLE for split-tower types (too many below-tower pieces).

### majorization-upper — REVISE (direct adaptive strategy; the V(n≥4) crux is a phantom)
Target: the whole upper bound `c(n) ≤ 2^n/D_n` — exhibit an explicit `≤ n`-mark adaptive
Xiang strategy forcing `D ≤ 1/D_n` against EVERY Liu config, all n.
Technique: direct config-adaptive Xiang strategy (bottom-up halving + pair-matching cascade),
NO induction on n (drop the V(n)←V(n−1) IH and the 3-mark cascade — both refuted as
phantom-crux chasers).
Skeleton:
  1. Scope: Liu config `(a_1 ≥ a_2 ≥ … ≥ a_m)`, `m ≤ n+1` (only `m = n+1` is hard; `m ≤ n`
     ⇒ Xiang halves all `m` pieces → `m` canceling pairs → `D = 0`; CONJECTURE verified n=4,
     GAP-mark-count). Base `n=1,2,3` CERTIFIED (imported: `n1-base`, `n2-upper-bound-complete`,
     `v3-upper-bound`).
  2. BOTTOM-DOMINANT regime `a_n ≥ 2·a_{n+1}` (P1 strategy): Xiang halves the `n` largest
     pieces, leaving the smallest `a_{n+1}` unsplit. The `n` equal-pairs `(a_i/2, a_i/2)`
     sit adjacent in sorted order (since `a_i/2 ≥ a_{i+1}/2 ≥ … ≥ a_n/2 ≥ a_{n+1}`), cancel
     at positions `(1,2),(3,4),…,(2n−1,2n)`, residual `a_{n+1}` at position `2n+1` (odd, +).
     `D = a_{n+1}`. This is the clean formula.
  3. TOWER-TAIL sub-family `(a_1, 2^{n−1}, …, 2, 1)/S` (the hard family inside bottom-
     dominant): `D = a_{n+1} = 1/S ≤ 1/D_n ⇔ S ≥ D_n`. The tower `T_n` (`S = D_n`) is the
     worst member (tight). PROVE `D = a_{n+1}` for the tower-tail family (the halving
     strategy's correctness on this family) and `1/S ≤ 1/D_n`.
  4. NON-BOTTOM-DOMINANT regime `a_n < 2·a_{n+1}` (P2 strategy): Xiang uses a pair-matching
     cascade — split pieces to create matching fragments (ties), cascading until all pieces
     pair up. Result: `D = 0` (all cancel) for most configs; small residual for some. Always
     `≪ 1/D_n` (worst ratio 0.52 over 3000 trials). PROVE `D = 0` or `D ≪ 1/D_n` here.
  5. Conclude: bottom-dominant gives `D = a_{n+1} ≤ 1/D_n` (step 3); non-bottom-dominant
     gives `D ≪ 1/D_n` (step 4); `m ≤ n` gives `D = 0` (step 1). So `D* ≤ 1/D_n` for every
     config. `c(n) ≤ 2^n/D_n`.
Key lemmas (claim + one-line mechanism):
  - Halving-cancel: halving the `n` largest pieces leaves pairs at adjacent sorted positions
    `(2i−1, 2i)` canceling, residual `a_{n+1}` at `+` — because `a_i/2 ≥ a_{i+1}/2` keeps
    each pair's two halves adjacent in the sorted order.
  - Tower-tail tightness `1/S ≤ 1/D_n` — because `S ≥ D_n` (the tower has minimum total
    mass among configs with `n+1` pieces in geometric ratio ≥ 2; a counting/AM-GM step).
Open gaps:
  - GAP-U1 (the hard step): prove `a_{n+1} ≤ 1/D_n` for the bottom-dominant tower-tail
    family, i.e. `S ≥ D_n` — a counting/AM-GM bound on the bottom `n` pieces. The tower is
    the minimizer of `S` subject to `a_i ≥ 2·a_{i+1}` for `i ≤ n` (geometric ratio ≥ 2).
  - GAP-U2: prove non-tower-tail bottom-dominant configs admit a strategy with
    `D ≤ 1/D_n` (the halving bound `D = a_{n+1}` may be loose; the real `D*` is smaller).
    This is an exchange/continuity argument localized to the bottom-dominant regime.
  - GAP-U3: prove `m ≤ n ⇒ D = 0` (the halving-all-pieces strategy always cancels).
    CONJECTURE, verified n=4.
  - GAP-mark-count: handle `m < n+1` (fewer marks) rigorously.
Cases to cover: `m ≤ n` (D=0); `m = n+1` bottom-dominant (halving); `m = n+1` non-bottom-
dominant (pair cascade). n=1,2,3 certified as base.
Watch out for: (a) the halving strategy is NOT optimal for non-tower-tail bottom-dominant
configs (e.g. `(10,8,4,2,1)/25`: halving gives `D=0.04` but `D*=0`) — the bound `D = a_{n+1}`
is an UPPER bound on `D*`, tight only for tower-tail. (b) The pair-matching cascade for non-
bottom-dominant is a CONJECTURE from computation (3000 trials, worst ratio 0.52), NOT a proof.
(c) Do NOT revive the V(n)←V(n−1) IH or the 3-mark cascade — both refuted (phantom crux;
the crux regime gives D*=0 or tiny, the IH overshoots because V(n−1) is a worst-case bound
blind to slack). (d) Do NOT conflate `c(3) ≤ 8/15` (proven) with `c(3) = 8/15` (needs lower
bound, still partial).

### xor-overlap — NEW (the genuine 5th lower framing, plateau-break mandate)
Target: the whole lower bound `D ≥ 1` for every `≤ n`-mark Xiang refinement of `T_n`, all n
— attacked via an overlap/correlation decomposition, NOT global-position-parity or PL geometry.
Technique: exact XOR identity `D = D_F + D_R − 2C` + strong induction on n + a decoupled
overlap bound on `C` (a correlation of two separately-structured parity functions).
Skeleton:
  1. EXACT IDENTITY (proved algebraically, 0 failures / 6000+ trials): split the refinement
     into top-fragments `F` (mass `2^n`, from splitting the top piece) and below-top pieces
     `R` (mass `2^n−1`, a `≤ (n−1)`-mark refinement of `T_{n−1}`). With
     `N(t) = N_F(t) + N_R(t)` and `(a+b) mod 2 = (a mod 2)+(b mod 2)−2(a mod 2)(b mod 2)`:
     `D = D_F + D_R − 2C`, where `D_F = ∫(N_F mod 2)dt` (standalone alternating sum of F),
     `D_R = ∫(N_R mod 2)dt` (standalone D of R = D of a `≤ (n−1)`-mark refinement of
     `T_{n−1}`), `C = ∫(N_F mod 2)(N_R mod 2)dt` (overlap of the two odd-parity regions).
  2. INDUCTION: by strong IH on n, `D_R ≥ 1` (R refines `T_{n−1}` with `≤ n−1` marks; the
     IH is G1 itself at size `n−1`). Base `n=1`: `F = {f, 2−f}`, `R = {1}`,
     `D_F = 2f−2`, `C = f−1`, so `D_F = 2C` EXACTLY, `D = 2C + 1 − 2C = 1`. TIGHT.
  3. OVERLAP BOUND (the hard step — GAP-X): prove `C ≤ (D_F + D_R − 1)/2`. With `D_R ≥ 1`
     (IH), this gives `D = D_F + D_R − 2C ≥ D_F + D_R − (D_F + D_R − 1) = 1`.
  4. Conclude `D ≥ 1` for all n. G1 closes via the induction + overlap bound.
Key lemmas (claim + one-line mechanism):
  - XOR identity `D = D_F + D_R − 2C` — because `(a+b) mod 2 = a⊕b` and the integral is
    linear, so the parity of `N = N_F + N_R` decomposes into the two marginals minus twice
    their overlap.
  - Base tightness `D_F = 2C` at `n=1` — because with `R = {1}` (odd on `[0,1]`), the
    F-odd region is `[0, f−1]` (a single interval), and `C = f−1 = D_F/2` exactly.
Open gaps:
  - GAP-X (the hard step, HONESTLY G1-equivalent): the decoupled overlap bound
    `C ≤ (D_F + D_R − 1)/2`. The trivial bounds `C ≤ min(D_F, D_R)` and
    `C ≤ √(D_F·D_R)` (Cauchy-Schwarz) give only `D ≥ 0` (the gaps-leftover G2 trivial
    bound). The "1" needs tower structure NOT captured by these generic inequalities.
    The R-odd region is dyadic ONLY when R is unsplit/dyadic (already-closed sub-case);
    for non-dyadic R (the G1 hard case of R), the R-odd region is non-dyadic (~37%/29%/24%
    of refined R have purely-dyadic odd regions for T_2/T_3/T_4), and the overlap bound
    there is G1(n−1)-equivalent. THIS IS NOT A SHORTCUT — it is a genuinely-different
    ATTACK ANGLE (a correlation/overlap of two decoupled parity functions, with a clean
    inductive reduction `G1(n) → G1(n−1) + overlap`), kept far from PL/spine/charging/LP.
Cases to cover: R unsplit (dyadic R-odd, easy, closed by `dyadic-refinement-lower-bound`);
R dyadic-refined (still dyadic R-odd); R non-dyadic-refined (the hard case, GAP-X).
Watch out for: (a) the sufficient condition `D_F ≥ 2C` FAILS at minimizers (543/2196 T_4
breakpoints, worst deficit `−6` at `F={9,3,3,1}`) — do NOT attempt this route; the slack
`D_R > 1` must compensate, and the EXACT bound `D_F + D_R ≥ 2C + 1` is just `D ≥ 1`
restated (circular). (b) The "dyadic-misalignment lemma" (bound C by exploiting dyadic
structure of R-odd) covers ONLY the already-closed sub-case (R unsplit/dyadic); for
non-dyadic R it is G1(n−1)-equivalent. Do not oversell it as a shortcut.

### lp-dual-certificate — REVISE (fix the LP-2 sign error; reframe GAP-LP2 as the
LP-feasibility witness of the spine sign-pattern lemma)
Target: the whole lower bound `D ≥ 1` for every `≤ n`-mark refinement of `T_n`, all n —
certified via LP strong duality / Farkas from the constraint structure.
Technique: LP strong duality + Farkas separating-hyperplane (a genuinely-different PROOF
MECHANISM for the spine sign-pattern lemma — LP feasibility vs combinatorial subset-sum).
Skeleton:
  1. Fix the LP-2 SIGN ERROR (round-4 reviewer flag): the mountain direction is flipped
     (builder claimed nonneg prefix sums of `d_k = y_eq[b(k)] − (−1)^k`; correct is NONPOS,
     or equivalently `d_k = (−1)^k − y_eq[b(k)]` for nonneg). The interleaved T_2
     demonstrative example is INFEASIBLE (cert objective 2 violates strong duality —
     actual LP min = 1, correct dual max = 1, verified scipy). The narrow interleaved sub-
     class has the wrong parity (k odd should be k even). Correct the dual derivation,
     remove/correct the infeasible example, fix the sub-class parity.
  2. UNIFY: GAP-LP2 (the structural sign-pattern feasibility lemma for interleaved types)
     IS the spine sign-pattern lemma (tail-count step 4) in LP language. The dual certificate
     `y_eq[t]` IS the spine's sign assignment (fragments at + ⇒ `y_eq = +1`, towers at − ⇒
     `y_eq = −1`), giving objective `(Σ fragments) − (Σ towers) = 1`. By strong duality,
     `dual ≥ 1 ⇔ min D ≥ 1`. So GAP-LP2 and the spine lemma are the SAME fact.
  3. ATTACK the spine sign-pattern lemma via LP FEASIBILITY (a different mechanism than
     tail-count's combinatorial multi-swap subset-sum): prove the corrected dual
     `y_eq[fragment-bin] = +1, y_eq[tower-bin] = −1` is FEASIBLE (satisfies the corrected
     nonpos-mountain constraint) for every interleaved type at `D = 1`. This is a Farkas/
     separating-hyperplane argument: if no feasible sign-pattern exists, a primal witness
     certifies `min D < 1` — but `D ≥ 1` (the target) rules this out. The LP-feasibility
     proof and the combinatorial subset-sum proof are genuinely different routes to the
     same lemma; if one stalls, the other may succeed.
  4. GAP-LP1 (clean types) stands CERTIFIED (imported, unaffected by the sign error —
     `y_ub = 0`, sign irrelevant).
Key lemmas (claim + one-line mechanism):
  - Corrected dual feasibility: `y_eq[t] = +1` for fragment bins, `−1` for tower bins
    satisfies the nonpos-mountain constraint `d_k = (−1)^k − y_eq[b(k)] ≥ 0` — because the
    spine interleaves (fragment, tower, fragment, …) so fragment bins land at odd `k`
    (`(−1)^k = −1`, `y_eq = +1`, `d_k = −1 − 1 = −2 < 0`... wait, sign needs care; the
    builder must verify the exact sign convention after the fix).
  - Strong duality: `dual max = primal min`, so a feasible dual with objective `≥ 1`
    certifies `min D ≥ 1` — the LP certificate IS the proof, no primal evaluation needed.
Open gaps:
  - GAP-LP2 (now = the spine sign-pattern lemma, attacked via LP feasibility): prove the
    corrected dual is feasible for every interleaved type at `D = 1`. HONESTLY G1-equivalent
    by strong duality (not a shortcut). The LP-feasibility mechanism (Farkas) is genuinely
    different from tail-count's combinatorial subset-sum — keep both live as rival proofs.
  - GAP-LP2-sign: fix the round-4 sign error (mountain direction, parity, infeasible
    example) — a correctness fix regardless of whether GAP-LP2 closes.
Cases to cover: clean types (CERTIFIED, GAP-LP1); interleaved types (GAP-LP2, the open
crux, = spine sign-pattern lemma).
Watch out for: (a) GAP-LP2 is G1-equivalent — do NOT present it as a shortcut. It is a
rival PROOF MECHANISM (LP feasibility/Farkas) for the same closing lemma as tail-count's
spine sign-pattern. (b) The sign error in LP-2 must be fixed BEFORE any new feasibility
claim — the round-4 infeasible T_2 example proves the old derivation was wrong. (c) Only
0–3% of odd types admit the single uniform cert — the feasibility lemma needs a family of
sign-patterns, not one. (d) This slug and tail-count share the closing lemma (spine sign-
pattern); they are NOT single-gap-trap because they use genuinely different proof mechanisms
(combinatorial subset-sum vs LP feasibility/Farkas) — but if BOTH stall on the same lemma
for 3 rounds, retire one.

### tower-induction — HOLD (certified S1/S2/S3 stand as scaffolding; G2-odd recognized
as the spine sign-pattern lemma, attacked in tail-count/lp-dual this round — do NOT build
to avoid a three-slug single-gap trap on the same lemma)
Target: the whole lower bound (same as tail-count, via block/spine machinery).
Certified importable: `spine-pair-cancellation` (S1), `strong-breakpoint-group-structure`
(S2), `even-group-spine-lower-bound` (S3, closes even-group G1 independently). The open
G2-odd (spine sign-bookkeeping) is now recognized as the spine sign-pattern lemma — the
same wall tail-count and lp-dual attack. Hold; if both rival mechanisms stall, revive
tower-induction's spine-value arithmetic as a third mechanism next round.

### gaps-leftover — HOLD (certified G1/G2 stand as scaffolding; deficit-covering crux
recognized as the spine sign-pattern lemma)
Target: the whole lower bound (same wall, via gaps+leftover charging/matching).
Certified importable: `gaps-leftover-identity` (G1), `pairing-leftover-bound` (G2). The
deficit-covering `Σ gaps + leftover ≥ 1` when `p_m < 1` is the same wall (the spine sign-
pattern lemma in charging language). Hold; do not build this round.

### d-potential, self-similar, balanced-configs — RETIRED/HOLD (no change; certified
sub-results harvested).

---

## Build set (proposed)

`tail-count` (REVISE — close GAP-C via mass-balance + spine sign-pattern lemma, hard step =
multi-swap subset-sum), `majorization-upper` (REVISE — direct adaptive halving/pair-cascade
strategy, drop phantom V(n≥4) IH, hard step = `a_{n+1} ≤ 1/D_n` for tower-tail), `xor-overlap`
(NEW — 5th framing, exact XOR identity + induction, hard step = decoupled overlap bound,
honestly G1-equivalent), `lp-dual-certificate` (REVISE — fix LP-2 sign error, reframe GAP-LP2
as LP-feasibility witness of the spine lemma, rival mechanism to tail-count's combinatorial
route).

Four builders, one per slug, in parallel. `tower-induction` and `gaps-leftover` HELD (their
open gaps are the same spine sign-pattern lemma — building them would be a single-gap trap).
