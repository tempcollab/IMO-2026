# Run State — imo-2026-03

## Goal
Solve IMO 2026 P3 (imo-2026-03), a `hard` combinatorics problem (difficulty 9).
Statement: Stick of length 1. Liu Bang marks ≤n points, then Xiang Yu marks ≤n points
(all distinct). Cut at all marks. Players alternately claim pieces (Liu Bang first),
each maximizing own total length. For each n, determine the largest c that Liu Bang
can guarantee regardless of Xiang Yu's play.

Metric: proof-reviewer verdict on the population of approaches in results/imo-2026-03/.
Eval: proof-reviewer reads results/imo-2026-03/current.md + approaches/*.md → verdict
  (solved | partial | unsolved) + APPROVE / CHANGES REQUESTED / RETHINK.
Baseline (round 0): unsolved — no approaches yet, no answer conjectured.
Target: `solved` — closed-form c(n) with proven lower bound (Liu Bang strategy) AND
  upper bound (Xiang Yu strategy), verified.
Constraints: prose Markdown proof; full rigor per CLAUDE.md; no web/cheating.

## Goal Updates
- [2026-07-28 R1] Initial task: solve imo-2026-03. No prior work.

## Eval History
- R0 baseline: unsolved, no approaches, answer unknown.
- R1: BREAKTHROUGH on answer + spine. Answer CONJECTURED & reduction PROVEN:
  **c(n) = 2^n/(2^{n+1}−1)** (c(1)=2/3, c(2)=4/7, c(3)=8/15), verified n=1..4.
  3 approaches all `partial`, all CHANGES REQUESTED: dyadic-discrepancy (leader,
  Elo~1531), induction-recursion (closest to lower-bound gap), potential-certificate
  (weakest, near-duplicate, RETHINK candidate if it stalls).
  CERTIFIED lemmas (shared cache): Lemma G (greedy claim = odd-rank sum), level-measure
  identity (D = meas{t: #pieces>t odd}), cut-flip/cut-budget/domination lemma.
  n=1 FULLY solved both bounds. Lower-bound Case A done.
  Two OPEN gaps (both numerically true, proof unwritten):
   - GAP U (THE CRUX): general-n upper bound — Xiang's non-myopic ≤n-cut strategy
     capping Liu at c(n). Naive "bisect n largest" + myopic greedy both REFUTED.
   - GAP L: lower-bound Case B (Xiang cuts Liu's top dyadic piece); needs
     cut-budget-refined induction.
- R2: IMPROVED (field reshaped). concavity-lp opened then KILLED (RETHINK): min-Xiang
  f is NUMERICALLY NON-CONCAVE (12/60 midpoint violations) — no global KKT/LP
  certificate. potential-certificate RETIRED (near-duplicate, separable-potential
  dead-end already banked). Field narrowed to 2 live D-language approaches on 2
  different walls: dyadic-discrepancy (GAP U), induction-recursion (GAP L). Both
  CHANGES REQUESTED. Elo: dyadic 1558, induction 1500.
- R3: IMPROVED (both walls reduced; NO reviewer ran — outcomes recorded late in R4).
  GAP U reduced to balanced Case (iii): builder PROVED greedy/black-box "single-move +
  RT(k-1)" telescopes ABOVE u_k for k≥3 — needs a strengthened potential, not greedy.
  New machinery: Invisible-Pair Lemma, Residual-Total (RT) reduction. GAP L reduced to
  doubly-balanced GAP-LB′; PROVED one-sided confinement of O_Z is refuted; needs a
  JOINT interleaving invariant. Half-total single-crosser lemma proved.
- R4: IMPROVED (both walls narrowed to a last sub-case; 2 new lemmas certified).
  Orthogonal-framing explorer came up DRY — no genuinely orthogonal route exists
  (scale-invariance ≡ induction-recursion algebraically; 2-adic recast circular).
  GAP U: Pivot Lemma (certified) closes Case (iii-a) Σ/2≤ℓ₁<c(k)Σ for ALL n via
  accumulator pin (residual 2ℓ₁−Σ ≤ u_kΣ ⟺ ℓ₁≤c(k)Σ). BOTH GAP-U twins
  (dyadic-discrepancy, dyadic-discrepancy-euclid) bottom on the SAME residual:
  super-balanced ℓ₁<Σ/2 (iii-b / U-B). aimo-0340 one-param reserve potential does
  NOT close it (recursion depends on ℓ₂,ℓ₃ individually).
  GAP L: Termwise Lattice Lemma T (certified) closes EVERY tight/equality D̃=1 config
  (prefix #T−#B≤1 ⇒ D̃≥1) via merged-order signed sum — NOT the refuted scalar fill.
  Residual = "run" sub-case maxc≥2 (a top-fragment run gets ≥2 ahead); needs
  two-level anchor-domination induction on Z's own dyadic cut-tree. Exchange/
  degenerate-boundary route (induction-recursion) proved UNABLE to close GAP-LB′
  (honest negative). All 4 CHANGES REQUESTED / partial. Elo (R3 advances folded):
  dyadic-discrepancy 1598, dyadic-discrepancy-euclid 1553, induction-recursion 1516,
  induction-recursion-telescope 1495, potential-certificate 1396 (retired).

- R5: (explorer-only round, no reviewer) math-explorer scouted GAP-U super-balanced
  ℓ₁<Σ/2 and GAP-L run-case; produced probes. No build/review ran.
- R6: (planning-only round, ended without summary/autocommit) explorers gated 2 distinct
  MECHANISMS per wall; outliner put 2 rival mechanisms on EACH residual; outline-reviewer
  ranked & emitted build set (all 4 live slugs) with a SHARPENED WARNING: single-gap
  pigeonhole reaches only c(k)Σ/(2k) = 2^{k−1}/k · u_kΣ, so it is NOT enough for k≥3;
  euclid slug lives/dies on bounding the subtractive-descent CHAIN LENGTH vs ≤k op budget.
  No builders dispatched (round interrupted).
- R7: **BREAKTHROUGH — GENERAL-n UPPER BOUND FULLY PROVEN & CERTIFIED** (wall open since
  R1). Resumed R6's build set: 4 builders + 1 reviewer. BOTH GAP-U slugs independently
  closed c(n) ≤ 2^n/(2^{n+1}−1) for ALL n and ALL Liu plays:
   - dyadic-discrepancy §4.7: Realizability Lemma + subset-sum pigeonhole selects the
     globally-optimal {−1,0,1} sign pattern (dissolves the k=4 pin-top-2 near-miss);
     Physical-Decomposition remark proves D(actual final multiset)=D(effective) via
     Invisible-Pair Lemma.
   - dyadic-discrepancy-euclid Theorem R: sign-pairing strong induction, contract a +/−
     pair to coin |x_p−x_q| ⇒ min Reach(U) = min ±1 signed sum EXACTLY. Op-budget
     RESOLVED: play uses exactly n cuts (n+1−s bisects + s−1 pins), chain length s−1≤n,
     no Euclidean overrun; piece-count-<n gap trivial (bisect all ⇒ D=0).
   Reviewer re-derived + simulated the actual physical cut sequence (D≤u_n, worst ratio
   0.9998, ≤n cuts, mass conserved, 0 violations, exact Fraction). CERTIFIED
   lemmas/upper-bound.md. Verdicts: dyadic-discrepancy CHANGES REQUESTED/partial (UB done,
   whole problem partial via GAP L); dyadic-discrepancy-euclid CHANGES REQUESTED/partial
   (near-duplicate UB); induction-recursion-telescope CHANGES REQUESTED/partial (GAP L
   sharpened not closed — see below); induction-recursion RETHINK (budget-count route
   exhausted, natural sub-route provably FALSE). Elo: dyadic-discrepancy 1634,
   dyadic-discrepancy-euclid 1535, induction-recursion-telescope 1519,
   induction-recursion 1474 (dead-end), potential-certificate 1396 (retired).
   GAP-L status: telescope PROVED exact threshold-split identity (△)
   D̃(F)=(y₁−θ)⁺+λ_(0,θ)(O_Y△O_Z) and localized to bounded-mass (△⋆)
   λ_(0,θ){M odd} ≥ ∫_(0,θ)M = 1−β ≤ 1; but KILLED the outliner's Step-5 top-down
   reserve IH (7306/4e5 violations — surplus lives in the near-0 count-parity band, not a
   top anchor). So BOTH GAP-L IH shapes now refuted (local match R4, top-down reserve R7).
- R8: CONVERGENT NEGATIVE (no APPROVE; whole class of GAP-L framings pruned as
  provably equivalent to the target). Per plateau rule, seeded 3 far-apart framings on
  GAP L; all partial with rigorous structural NEGATIVES (3 lemmas certified):
   - induction-recursion-telescope (CHANGES REQUESTED/partial, leader): bounded-window
     nonneg-block TILING is CIRCULAR — a valid tiling exists IFF the target D̃≥1 (single
     block [1,m] works iff Σ≥0). NO local-window certificate (both-directional greedy
     fails 222/2e5; witness n=3 Y=(3.382,2.553,2.065) Z=(4,1.042,1,0.958): lone deficit
     s₄=−2.046 exceeds each adjacent surplus separately ⇒ certifying block non-local).
     Lemma H (maxc≤|Y|=a₀+1) + identity (△△) ∫(⌊M⁺/2⌋−⌈M⁻/2⌉)=½∫M−½D̃ certified
     (lemmas/merged-order-layer.md): EVERY merged-order/measure form is a measure-algebra
     restatement giving only D̃≥0 (trivial layer bound off by ½). The missing ½ MUST be
     injected by the dyadic budget Σaⱼ≤n NON-LOCALLY. Merged-order block/window/matching
     family now EXHAUSTED.
   - cut-sequence-potential (RETHINK/unsolved): Reserve⇔Target Equivalence Theorem PROVEN
     & certified (lemmas/reserve-target-equivalence.md) — an admissible sequential reserve
     exists IFF GAP L holds ⇒ the amortized monovariant has NO independent leverage. Whole
     sequential-count/potential family pruned (also explains why induction-recursion died).
     Per-cut law ΔD̃=λ(S)−2λ(S∩O) on exact toggle set S=[0,x)∪[L−x,L) verified.
   - even-rank-doublecount (RETHINK/unsolved): reformulation (⊞) E(F)=∫⌊N/2⌋dt,
     D̃=∫⊕ⱼ1[Nⱼ odd]dt certified (lemmas/scale-parity-xor.md, verified 0/2e4). But genfn
     engine FAILS (empirical cheap-kill: scale-XOR non-additive, tight cases front-loaded,
     margin ≥4 in prefix-ok slice) — recasts to same non-additive count-parity wall.
   META (rigorously established for the 2 measure/sequential framings, empirical for genfn):
   merged-order + measure-algebra + sequential-count + genfn framings are ALL equivalent to
   GAP L and CANNOT inject the ½. The missing mechanism must exploit Z's RECURSIVE dyadic
   cut-tree ORIGIN directly, using Σaⱼ≤n non-locally. PLATEAU (now R3–R8, 6 rounds).
   Elo: dyadic-discrepancy 1656 & euclid 1540 (parked UB ref); telescope 1538 (leader,
   live); cut-sequence-potential ~1520 (RETHINK); even-rank-doublecount ~1490 (RETHINK);
   induction-recursion 1444 (dead); potential-certificate 1360 (retired).

- R9: IMPROVED (plateau framing BROKEN; sharpest GAP-L reduction yet; +1 mechanism now
  UNDERSTOOD; 2 lemmas certified). Per R8 meta, seeded 2 far-apart cut-tree/2-adic
  approaches; both partial/CHANGES REQUESTED. Bottom-up reserve of Z REFUTED (63496/1e5).
   - vertex-integrality-parity (NEW): **Parity Lemma CERTIFIED** (lemmas/parity-odd-total.md):
     integer multiset + odd TOTAL (always 2^{n+1}−1 here) ⇒ D̃=ΣF−2E ≡ ΣF ≡ 1 (mod 2) odd,
     with D̃≥0 ⇒ D̃≥1. THIS is the non-local +1 injector no measure/merged-order/sequential/
     genfn framing could supply (they were all off by ½). Integer min=1 tight (explicit family
     ∀n). Main Reduction easy direction proven. WHOLE PROBLEM now reduces to a single clean
     crux **GAP-IMR**: the global infimum over the continuum is ATTAINED at an integer config
     (⟹ Parity Lemma finishes). Verified n≤3 (every optimal cell has an integer-vertex global
     minimizer), proven NON-circular (about WHERE the min lives, not its value). NOTE: the
     naive TU/integral-vertex claim was REFUTED (minimizers generically fractional; LP-min 2
     but integer-min 3); GAP-IMR needs a global mass-transfer/rounding argument, not per-cell.
   - peel-scale-rank-induction (NEW, far-apart): **Case A (a₀=0) FULLY CLOSED** (D̃(F)=2^n−D̃(F'),
     D̃(F')≤ΣF'=2^n−1 ⇒ D̃≥1). Peel SD identity D̃(F)=λ(O_{π_0}△O_{F'}) + difference bound
     D̃(F)≥|D̃(π_0)−D̃(F')| + Invariant I M(0⁺)=(a₀+1)−|F'|≤1 all proven & **CERTIFIED**
     (lemmas/peel-difference-bound.md); diff bound closes 80.8% of Case B. Sole crux **GAP-P1**:
     a LOADED dyadic-shape IH on F' closing the near-balance residual {|D̃(π_0)−D̃(F')|<1};
     plain value-IH proven INSUFFICIENT (F' reaching D̃=0.146). Open.
   Both cruxes bottom on the same "global +1 injection" wall but from far-apart routes — and
   the +1 mechanism itself is now understood (parity of the odd dyadic total). GAP L is closer
   than ever: from a diffuse count-parity band (R7–R8) to two concrete structural cruxes.
   Elo after ranking gate: dyadic-discrepancy 1673 (parked UB), telescope 1579 (parked leader),
   peel-scale 1537, vertex-parity 1510; reviewer recorded both R9 builds as advanced.

- R10: IMPROVED (sharpest GAP-L reduction of the run; the whole GAP-IMR/integrality line
  PRUNED as equivalent-to-target). Advanced 3 slugs on GAP L; all partial, mixed verdicts;
  2 lemmas certified. **peel-scale-rank-induction (NEW LEADER, CHANGES REQUESTED, Elo 1595):**
  proved & CERTIFIED the FLOOR identity (lemmas/floor-half-reduction.md)
  **D̃(F)=1−2∫_(0,θ)⌊M/2⌋, M=N_{π_0}−N_{F'}** ⇒ ALL of Case B collapses to a SINGLE scalar
  inequality **I_n:=∫_(0,θ)⌊M/2⌋ ≤ 0** (tie-attained at 0 ⇒ D̃=1). Verified 0 violations
  over 6·10⁴ feasible fractional Case-B configs (n≤6). Layer form I_n=Σ_k(λ{M≥2k}−λ{M≤−(2k−1)})
  exposes even/odd threshold asymmetry as arithmetic source of the missing ½. Two structural
  findings: budget Σaⱼ≤n enters the reduction ONLY through M(0⁺)≤1 (reconfirms non-locality),
  and M(0⁺)≤1 ALONE is insufficient (§7a decoy) ⇒ loaded IH must control the SHAPE of g=N_{F'}
  (Z's cut-tree origin). Open crux GAP-P1′: prove I_n≤0 via loaded dyadic-shape IH on g.
  **vertex-integrality-parity (RETHINK, dead-end, Elo 1546):** GAP-IMR proven LOGICALLY
  EQUIVALENT to the target (once integer-min=1 is used) — a reformulation, NOT a reduction;
  the R9 "non-circularity" claim was WRONG. Order-aware smoothing engine REFUTED (no
  D̃-non-increasing descent at isolated fractional vertices; n≤3 every min-cell already returns
  an integer vertex ⇒ mechanism vacuous). Standalone integer-minimizer engine DEAD; Parity
  Lemma survives only as a finishing device. **peel-integral-exchange (CHANGES REQUESTED,
  partial, Elo 1540):** CERTIFIED Lemma OB (odd-block alt-value formula D̃=Σ(−1)^{p−1}u_{(p)},
  even tie-blocks cancel) + Lemma V (optimal cell-vertex has K≤n+1 distinct values), reduces
  GAP-IMR to finite GAP-IMR′="some optimal cell-vertex is integer" — but GAP-IMR′ is STRONGER
  than target (⇒ not ⇐, possibly unattainable at large n), and cross-scale mass transfer is
  BLOCKED by hard equalities Σπ_j=2^{n−j} (merging even block can raise D̃: {½,½}→{1} sends
  2→3 at (4,2,½,½)). Whole integrality/GAP-IMR framing now equivalent-to-or-stronger-than
  target ⇒ dead as an independent engine. GAP L PLATEAU continues (R3–R10) but reduction is
  now a clean scalar inequality. Elo: dyadic-discrepancy 1673 (UB), peel-scale 1595 (leader),
  telescope 1580 (parked), vertex-parity 1546 (dead), peel-integral-exchange 1540.

- R11: IMPROVED (GAP L sharpened to one clean extremal-slice inequality; 2 lemmas certified;
  the b-pruning finite-corner engine PRUNED). Advanced leader + 1 new far approach on GAP L
  (I_n≤0). peel-scale-rank-induction (CHANGES REQUESTED/partial, LEADER Elo~1646):
  **ladder-interleaving identity CERTIFIED** (lemmas/ladder-interleaving-identity.md):
  D̃(π_0⊎L)=1+2(Σ_{blue-odd}−Σ_{red-even}), L={2^{n−1},…,2,1} the uncut ladder ⇒ extremal
  base case b=0 collapses to the clean combinatorial inequality **(★) Σ_{blue-odd} ≥ Σ_{red-even}**
  (tie=equality; 0 mismatches n≤6, exact Fraction). Also closed unconditionally: the {M≤1}
  sub-region (~88%), the (DIFF)-shell |D̃(π_0)−D̃(L)|≥1 with exact D̃(L)=(2^n−(−1)^n)/3, and n=1.
  TWO gaps remain: GAP-P1′-a (cross-block ladder-dominance proof of (★); naive per-block charge
  insufficient ~51%, needs cross-block tail cancellation) and GAP-P1′-b (slice-max reduction of
  general b to b=0; the pointwise per-cut π_0-fixed monovariant is FALSE ~30%). allocation-vertex-
  corner (RETHINK/unsolved-as-engine, Elo~1502): its φ(b) b-pruning premise ("only b=0 reaches the
  tie") REFUTED — exact ties I_n=0 at b=2 (F={8,8,5,4,2,2,1,1}) and b=3, so scalar b has NO
  separating power; engine dead → back to outliner. But **Positive-Layer Localization Lemma
  CERTIFIED** (lemmas/positive-layer-localization.md): Σ_k λ{M≥2k} ≤ Σ_{k=1}^{⌊(a_0+1)/2⌋} y_{2k}
  (positive layers bounded by π_0's even-ranked parts alone; tight, 0/2e4). Whole problem partial;
  UB certified. Plateau now R3–R11 (9 rounds) but GAP L pinned to (★) on the extremal slice.

- R12: (interrupted, ended without summary/autocommit) explorers + outliner + outline-reviewer
  ran; build set {peel-scale-rank-induction, ladder-abel-pairing, coupled-cut-descent} emitted.
  Only coupled-cut-descent built: single-cut co-varying b→b−1 descent RIGOROUSLY REFUTED at n=5
  (non-tie failure π_0={16,16}, top rung 2^4 cut {10,4,2}, min reachable D̃=5>3). Lemma TIE
  (D̃=1⟹I_n=0, ties auto-good — tie family NOT the obstruction) + Lemma ΔM proved. No reviewer ran.
- R13: **BREAKTHROUGH — (★) BASE SLICE FULLY PROVEN & CERTIFIED** (wall open since R3). GAP L now
  reduced to ONLY the b-lift. Explorers: opening (D) ladder-length induction found; peel §11.5
  full-WM-IH b-lift REFUTED (prefix majorization fails off-ladder 477/12000). Outliner opened 2 new
  slugs; qlayer-charge-induction KILLED by outline-reviewer ((NEG) Q≥S_π false, 50–77% fail, fails
  tie family). Built ladder-length-deficient-induction + peel; both CHANGES REQUESTED/partial.
   - ladder-length-deficient-induction (NEW, verified-milestone, Elo ~1583→ up): CLOSED (★)
     D̃(π_0⊎L)≥1 via MUTUAL INDUCTION ON LADDER LENGTH m: deficient-total (P_m: Δ_m≥0 when ΣR=2^m)
     coupled to complementary (Q_m), with per-part ≤2^m + #R≤m+2 hypotheses (cap load-bearing,
     3230 fails when dropped). KEY UNLOCK: D̃-Lipschitz lemma (I4) — (LB_m) Δ_m(R)≥min(0,2^m−ΣR)
     collapses to (P_m) by 1-Lipschitz continuity in ΣR (shrink ΣR by ε to hit 2^m, apply (P_m),
     incur −ε) — injects the missing ½ by CONTINUITY not a razor estimate. Reviewer re-derived all
     3 peel identities + Lipschitz + base m=1 exactly, confirmed NON-circular, does NOT hide the ½,
     both branches (up to 3 reds >θ) settled via uniform red-peel. 0 violations 30k–45k configs.
   - peel-scale-rank-induction (LEADER, advanced, Elo 1730): HLP breakpoint reduction certified
     (WM) ⟺ (★) ∧ [Φ(b_i)≥0]; Φ(θ)=0 closed unconditionally; residual i≥2 shown to be the SAME
     self-similar deficient-ladder object ladder-length proves ⇒ two leading (★) routes are the
     same wall, ladder-length discharges both. Dropped its refuted §11.5 WM-IH b-lift.
   CERTIFIED: lemmas/base-slice-star.md (base-slice theorem + engine + peel/Lipschitz sub-lemmas),
   lemmas/hlp-breakpoint-reduction.md. coupled-cut-descent + allocation-vertex-corner marked dead.
   Elo: peel 1730 (leader), ladder-length 1583, telescope 1582, abel 1566 (live, unbuilt hedge).
   SOLE OPEN WALL: the b-lift (GAP-P1′-b) — reduce general F' (b>0) to the ladder base case; NO
   live route (single-cut descent + WM-IH inheritance both dead, qlayer-charge dead).
- R14: CONVERGENT NEGATIVE (no APPROVE; both b-lift twins RETHINK; wall SHARPENED + 1 master lemma
  certified). Explorers surfaced 2 fresh openings (ABSORB one-scale identity Δ_m(R,Z)=θ+Δ_{m−1}(R⊎π_1,Z')
  verified 0/2000; two-parameter (P_{m,k})/(Q_{m,k}) split-rung generalization). Outliner opened both as
  NEW slugs; outline-reviewer KILLED the leader peel-scale-rank-induction (RETHINK — its R14 move reduced
  I_n≤0 to the BANNED (NEG) Q≥S_π bound, reconfirmed FALSE at n=4 b=2 tie Q=3<S_π=8). Built both new slugs;
  BOTH RETHINK/dead-end after independent verification:
   - split-rung-mutual-induction: outline's clean sign-flip identity (I1′) is FALSE 3931/4000 (witness
     m=2,R={1},Z={3/2,1/2,1}: true Δ=3/2, clean form gives 3). Honest identity carries residual
     I_S=λ(O_{ρ_1}∩O_{R⊎Z'}) = the certified odd-set OVERLAP term = GAP-P1 (the shared wall). Re-encodes,
     no new content.
   - absorb-rescale-induction: on the b-lift instance ABSORB is a BOOKKEEPING TAUTOLOGY (R̄⊎F''=π_0⊎F'
     as multisets ⇒ claim = original D̃≥1); rescaled closer gives −2θ, STRICTLY WEAKER than trivial
     D̃≥0 (−θ−½). Count-cap accounting is moot. Residual gap = split-rung's (I1′) ⇒ NOT independent of
     twin (single-gap trap, both builders flagged diversity collapse).
   CERTIFIED: lemmas/top-peel-general.md (MAXPEEL refinement-blue max-peel + generalized red-peel (I3′),
   subsuming both banked forms, 0-fail exact-Fraction). WALL RE-STATED: the b-lift content IS the missing
   ½ living in the overlap term λ(O_{π_0}∩O_{F'})=GAP-P1; needs a NON-SCALAR cut-tree invariant on F'
   (every scalar/telescoping bound is vacuous or restates it). Plateau on the b-lift now R11–R14 (post-(★)).

- R15: IMPROVED (b-lift pinned to a SINGLE leaf case; budget now a live unused resource; 2 lemmas
  certified; far-apart framing retired via rigorous negative). Explorers: overlap-tree flagged a
  value-ranked NEG-lemma opening (Q≥Σz_{2k-1}) — outliner CHEAP-KILLED it 100% (Q is the negative part
  of M=N_{π₀}−N_{F'}, so no π₀-dropping bound can lower-bound it; ALL clean layer forms fail incl. a
  proven b=0 config); game-semantics explorer honest NEGATIVE (every game route reduces to certified
  dead shapes: reserve⇔target, merged-order circularity, or universal split identity D̃(A⊎B)=D̃(A)+D̃(B)
  −2λ(O_A∩O_B) for ANY bipartition — banning π₀/F' specifically does NOT evade it) + 2 numeric cheap-kills
  (hard per-rung equality Σπ_j=2^{n-j} supplies most of +1, min D̃→0.386 at n=4 if dropped; cross-rung
  effects strongly non-additive ⇒ NO Sprague-Grundy independent-subgame decomposition). Built 2:
   - ladder-length-deficient-induction (CHANGES REQUESTED/partial, PRIMARY, advanced): **budget-aware
     mutual induction (P̂_m)/(Q̂_m)/(L̂B_m)** generalizing the certified engine from blue=uncut-ladder to
     blue=BUDGETED refinement (Σρᵢ=2^{m−i}, Σaᵢ cuts). CLOSED EVERY case whose top blue rung is UNCUT
     (via MAXPEEL (A1) + (I2)-general (A2) + (I3′) red-peel (A3) + Lipschitz collapse; uncut base = certified
     (★)). Reviewer re-verified exact-Fraction: correction (C) 0/30000, (A1)(A2)(A3) 0/15000 each, targets
     0-fail 44k/50k. SPEC CORRECTION (reviewer-confirmed): "D̃(π₀⊎F')≥1 for ANY refinement" is FALSE without
     budget (witness π₀={2,2},F'={3/2,3/2} gives D̃=0) — budget Σaᵢ≤n is LOAD-BEARING & non-local, now
     carried explicitly. Whole b-lift REDUCED to a SINGLE leaf: the CUT TOP RUNG (a₁≥1), where the cut-peel
     does NOT flip Δ's sign and the correction lands on the certified GAP-P1 overlap I_S=λ(O_{ρ₁}∩O_W) —
     BUT now equipped with the fresh, previously-UNUSED hypothesis Σaᵢ≤m. This is the first live route since
     R11: the wall is the same overlap term but a NEW resource (the budget) is in hand on that leaf.
   - bottom-band-peel-induction (RETHINK/unsolved, RETIRED): far-apart bottom-scale/near-0 Parity route.
     Cheap-kill gate FAILED all 3 sub-routes (reviewer reproduced witnesses): bottom-band overlap identity
     D̃(F)=D̃(F_{>τ})+(−1)^{|F_{>τ}|}D̃(F_{≤τ}) is correct (0/30000) but SPLIT-AGNOSTIC (odd branch = certified
     DIFF/overlap wall verbatim); bottom-SCALE peel needs D̃(G)≥2, refuted by budget (F={2,2,1,1,1}: D̃(F)=1
     but D̃(G)=0); bottom-VALUE-BAND has no inductive engine (F_{>τ} not a dyadic feasible instance,
     F={4,4,2,2,1,1,1}: D̃(F_{>1})=0); near-0 surplus is INTEGER-ONLY (z_min→0 kills it, GAP-IMR needed =
     equivalent-difficulty R10). Honest negative — banked the identity.
   CERTIFIED: lemmas/cut-top-rung-correction.md (correction (C) D̃(R⊎F')=D̃(ρ₁)−D̃(W)+2λ(E∩O_W),
   E={N_{ρ₁} even}∩(0,θ), carrying the exact GLOBAL below-p_r tail flip; + uncut-rung reductions (A1)(A2)(A3)),
   lemmas/bottom-band-overlap.md (bottom-band overlap identity). Elo: peel-scale 1739 (parked leader),
   dyadic-discrepancy 1682 (UB ref), ladder-length-deficient ~1573→up (live primary), others unchanged.
   Plateau on the b-lift now R11–R15 (5 rounds) BUT materially narrowed: from "no live route" (R14) to a
   single leaf with a fresh unused resource.

- R16: IMPROVED (the leaf's ΣR≤θ half CLOSED; the budget-trade unlock FOUND & verified; residual
  narrowed to ΣR>θ). Explorers: budget-trade explorer found the R16 key — on the cut-top-rung leaf,
  a₁≥1 SPENDS a budget unit (a₀+b''≤m−1, ΣR≤2^m in range), so the FULL deficient LOWER bound
  (L̂B_{m−1}) Δ(R,F'')≥min(0,θ−ΣR) is admissible (not just the (Q̂) upper bound the R15 file inherited)
  — 0-fail ~70k trials. per-rung-equality explorer came up DRY (recursive form = existing (P̂/Q̂) engine;
  additive form re-encodes refuted subadditivity/scalar-b) — no slug. Outliner revised the sole live
  approach + made a LEAN call (no filler diversity slug; every alternative re-encodes a dead wall);
  outline-reviewer concurred + verified the banking before advancing. Built + reviewed:
   - ladder-length-deficient-induction (CHANGES REQUESTED/partial, PRIMARY, advanced, Elo ~1679):
     BANKED 2 reviewer-verified (0-fail) sub-results — (L̂B-inherit) the genuine budget-trade
     (a₁≥1 ⇒ full deficient lower bound admissible on W, 0/76k) and (ΣR≤θ closure) Δ(R,F')≥½(θ−D̃(ρ₁))>0
     via (C)+I_S≤D̃(ρ₁)+alternating-sum D̃(ρ₁)≤p₁<θ (0/58k) — CLOSING the ΣR≤θ half of the cut-top-rung
     leaf completely. Proved (†) I_S≤Δ+½θ+½D̃(ρ₁) is LITERALLY the target restated by (C) (parity-mismatch
     measure ≥1, 0/57k) ⇒ every scalar I_S-ceiling is vacuous (naive scalar inconclusive 62% of oversized
     configs, truth always ≥0); builder correctly does NOT assume it. SOLE OPEN GAP now the ΣR>θ
     (oversized-red) residual + its mirror Case IIa via the (TEETH) per-tooth comb mechanism: bound
     I_S=λ(O_{ρ₁}∩O_W) using the comb structure of O_{ρ₁} (⌈r/2⌉ teeth, a₁ controls tooth COUNT not
     MEASURE, D̃(ρ₁) NOT a₁-monotone) charged against O_W's ≤2m−a₁ budget-limited breakpoints. NO banned
     route smuggled ((L̂B) is the certified R13 deficient-total, not the refuted scalar fill). Reviewer
     DECLINED certifying the 2 banked results as standalone lemmas — they are CONDITIONAL on the open IH
     (P̂_{m−1}), valid inductive-step reductions banked in the approach file, not theorems yet.
   Plateau on the b-lift now R11–R16 BUT materially advanced: from "single leaf with a fresh unused
   resource" (R15) to "half the leaf closed + the budget-trade proven; residual = one per-tooth comb bound
   on oversized reds". Elo: peel-scale 1714 (parked reference), ladder-length-deficient 1679 (live primary).

- R17: IMPROVED (whole ΣR>θ residual COLLAPSED to a measure-zero endpoint slice; b-lift now 2 razor-tight
  endpoint leaves). Explorers: TEETH comb-geometry (found "all-or-nothing tooth capture" ⇒ I_S = 0/1 tooth
  selection = rank/interleave matching) — but the OUTLINER then REFUTED that capture claim (6481/8000 leaf
  configs have a W-part strictly inside a tooth; surviving form = merged-order alt-sum = target, R8-banned).
  cheap-kill explorer: both R16-logged speculative directions DEAD (run-length recast has zero separating
  power = R8 meta on the leaf; red-side MAXPEEL re-routes to the (Q̂) mirror wall). So NO far-apart slug —
  lean field, revise the sole live approach. Built + reviewed ladder-length-deficient-induction
  (CHANGES REQUESTED/partial, LEADER Elo 1736, edging parked peel-scale 1715):
   - **(S1) trivial band CLOSED unconditional** (reviewer 0/240k): Δ(R,F')=½(D̃(R⊎F')−ΣR+ΣF'), ΣF'=2^m−1 ⇒
     Δ≥0 ⟺ D̃≥ΣR−2^m+1; on ΣR≤2^m−1 the RHS≤0 so certified (NN) D̃≥0 closes it. SUBSUMES the entire R16
     cut-top-rung θ<ΣR≤2^m−1 machinery (that "TEETH residual" was mostly TRIVIAL — only ΣR=2^m is hard).
   - **(S2) Lipschitz fill CLOSED (conditional reduction, 0-fail)**: 2^m−1<ΣR<2^m reduces to the endpoint
     ΣR=2^m via certified (I4) with decrease ε=2^m−ΣR∈(0,1) (fill feasible: ≥2 reds ⇒ slack ≥ε). DEFERS
     the +1 to the endpoint (does not inject it) — honest.
   - **Anchor D̃(F')≥1 (≤m−1 cuts)**: uncut-branch unconditional (MAXPEEL); cut-branch = (P̂_{m−1}) at
     endpoint ΣR̄=2^{m−1}, budget a₁+b''≤m−1 — a STRICTLY SMALLER b-lift instance (descent in m), non-
     circular, spare budget unit load-bearing (min D̃ drops <1 only at m cuts). Verified.
   - The whole b-lift = the single endpoint slice ΣR=2^m (integer-rigid, measure-zero). Split by F''s top
     rung: 2 leaves CLOSE by descent (S3-U big-red → (P̂_{m−1}); pure-blue/{θ,θ} tail → anchor); 2 leaves
     OPEN & razor-tight (min D̃=1 exactly): (i) S3-U all-reds≤θ needs the (Q̂_{m−1}) cut-top-rung endpoint
     upper bound Δ(R,F'')≤−1 (a genuinely NEW UB; existing (Q̂_m) is 2^m too weak); (ii) S3-C all-reds≤θ =
     the (C) overlap wall I_S≤Δ+½θ+½D̃(ρ₁) = target restated on this slice (NOT assumed).
   - RETRACTED (both reviewer-confirmed FALSE): the "no red=θ ⟹ D̃≥13/12" slack claim (witness R={3,3,2},
     F'={2,2,2,1}, top rung {2,2} cut, no red=θ, D̃=1) AND the outline-reviewer's cut-top-rung-restricted
     min≈1.12 version (same witness kills it). No θ-red-forcing split usable.
   Bans/circularity audit CLEAN. No new standalone lemma certified (S1 = 1-line corollary of (NN); S2 +
   anchor cut-branch conditional on open IH). Plateau on b-lift now R11–R17 BUT the residual is at its
   smallest ever: a measure-zero endpoint slice with 2 concrete open leaves. Elo: ladder-length-deficient
   1736 (live leader), peel-scale 1715 (parked reference).

## Rules
- ALWAYS keep rival approaches far apart in framing, not just technique (because
  same-framing variants share one wall, CLAUDE.md).
- NEVER present a conjectured answer as proven; find-all needs bound + construction.
- NEVER let a builder use "Xiang bisects the n largest pieces" or any myopic-greedy
  Xiang play as the upper-bound strategy — both REFUTED (let Liu reach ~3/4), round 1.
  Xiang's optimal upper-bound play is NON-MYOPIC.
- ALWAYS import the certified shared lemmas from results/imo-2026-03/lemmas/
  (greedy-claim.md = Lemma G + level-measure; cut-flip.md) rather than re-proving,
  round 1.
- The whole field shares GAP U (upper bound). Watch for a shared-gap plateau: if it
  stays open 3+ rounds, tell the outliner to open a genuinely DIFFERENT framing for
  the upper bound (CLAUDE.md shared-gap rule).
- NEVER let a builder use the scalar-summary lower-bound fill D̃ ≥ sum(Y)−sum(Z) (or
  any fill using only aggregate stats of Z like D_bot≥1): PROVEN FALSE with 3
  counterexamples (R3–R4). GAP L needs Z's RECURSIVE dyadic cut-tree origin, a JOINT
  interleaving invariant — not one-sided confinement (also refuted).
- NEVER let a GAP-U builder use greedy / black-box "single-move + RT(k-1)": PROVEN to
  telescope ABOVE u_k for k≥3 (R3). Optimal balanced-case play is non-greedy
  (chain of pin-ops / accumulator). The aimo-0340 one-parameter reserve potential does
  NOT close ℓ₁<Σ/2 (recursion depends on ℓ₂,ℓ₃ individually) — R4.
- ALWAYS import certified lemmas from results/imo-2026-03/lemmas/: greedy-claim.md,
  cut-flip.md, pivot-lemma.md (R4, closes GAP-U Case iii-a), termwise-lattice.md
  (R4, closes GAP-L equality core), upper-bound.md (R7, THE WHOLE UPPER BOUND for all n).
  Do not re-prove.
- GAP U (UPPER BOUND) IS DONE (R7): c(n)≤2^n/(2^{n+1}−1) fully proven & certified
  (lemmas/upper-bound.md) via Realizability+subset-sum (dyadic-discrepancy) and Theorem R
  sign-pairing (euclid). NEVER reopen the upper bound or re-attempt GAP U — the ONLY open
  wall is GAP L (lower bound, Case B). Retire/park both GAP-U slugs' UB work; they are the
  UB reference. Do NOT spend builder budget on the upper bound again.
- NEVER let a GAP-L builder use a top-down / top-anchor reserve IH (Z's odd measure leads
  its even measure from the top): REFUTED R7 (7306/4e5 violations; surplus lives in the
  near-0 count-parity band). Both scalar-summary (R3–R4) AND top-down reserve (R7) IH
  shapes are now dead. GAP-L compensation is bottom-inclusive/global across dyadic scales.
- ALWAYS attack GAP L via the certified exact identity (△) D̃=(y₁−θ)⁺+λ(O_Y△O_Z) and its
  bounded-mass localization (△⋆) λ_(0,θ){M odd} ≥ ∫M = 1−β (R7, telescope). The residual
  is now this single clean bounded-mass count-parity inequality — not the run-case framing.
- The min-Xiang value f is NON-CONCAVE (R2): no global concavity/KKT/LP certificate
  works. Do NOT reopen concavity-lp or any separable-per-piece potential (both refuted).
- NEVER let a GAP-L builder use ANY merged-order / measure-profile / sequential-cut /
  generating-function framing to close D̃≥1: ALL PROVEN EQUIVALENT to the target itself
  (R8, certified). Bounded-window nonneg-block tiling is CIRCULAR (tiling⟺target,
  merged-order-layer.md); any sequential reserve exists IFF GAP L (reserve-target-
  equivalence.md); genfn recasts to the same non-additive wall (scale-parity-xor.md).
  These framings give only the trivial D̃≥0 (measure layer bound off by ½). The missing ½
  MUST be injected NON-LOCALLY by the dyadic budget Σaⱼ≤n — via Z's RECURSIVE dyadic
  cut-tree ORIGIN, not any static profile of the final multiset.
- ALWAYS import certified R9 lemmas: parity-odd-total.md (integer multiset + odd total ⇒
  D̃=ΣF−2E odd ⇒ D̃≥1 — the non-local +1 injector), peel-difference-bound.md (peel SD
  identity D̃(F)=λ(O_{π_0}△O_{F'}), difference bound D̃(F)≥|D̃(π_0)−D̃(F')|, Invariant I
  M(0⁺)=(a₀+1)−|F'|≤1, Case A closed). Do not re-derive.
- NEVER re-attempt bottom-up reserve of Z (dual of top-down): REFUTED R9 (63496/1e5). NEVER
  claim total-unimodularity / integral vertices of the D̃-minimization polytope: REFUTED R9
  (minimizers generically fractional; LP-min 2 vs integer-min 3). GAP-IMR needs a GLOBAL
  mass-transfer/rounding argument to an integer minimizer, not a per-cell/TU claim.
- ALWAYS import certified R8 lemmas: merged-order-layer.md (identity (△△) + tiling
  circularity + Lemma H maxc≤|Y|), reserve-target-equivalence.md (sequential family⟺GAP L),
  scale-parity-xor.md ((⊞) E(F)=∫⌊N/2⌋dt, D̃=∫⊕ⱼ1[Nⱼ odd]dt). Do not re-derive these.
- GAP-L PLATEAU ACUTE (now R3–R8, 6 rounds; R9 outliner MUST act): every static/profile
  framing is now proven equivalent to the target (R8 meta). R9 outliner MUST seed the
  framing the meta POINTS TO and nothing else: attack the lower bound using Z's RECURSIVE
  DYADIC CUT-TREE ORIGIN directly — the Σaⱼ≤n budget spent NON-LOCALLY down the tree
  (e.g. structural induction on Z's cut-tree bounding how the budget can create odd-count
  bands, or a two-level anchor-domination on Z's own subtree splits). Do NOT seed a 4th
  measure/merged-order/sequential/genfn mechanism — they are dead (equivalent to target).
  induction-recursion-telescope is the leader/machinery home (owns (△)/(△⋆)/(△△)/(⊞));
  cut-sequence-potential and even-rank-doublecount are RETHINK — send back to outliner to
  re-plan onto the cut-tree framing or retire (their (⊞)/equivalence lemmas are banked).
- ALWAYS import certified R10 lemmas: floor-half-reduction.md (FLOOR identity
  D̃(F)=1−2∫_(0,θ)⌊M/2⌋ ⇒ Case B ⟺ I_n=∫_(0,θ)⌊M/2⌋≤0, the sharpest GAP-L reduction;
  M=N_{π_0}−N_{F'}), odd-block-vertex.md (Lemma OB: D̃=Σ_p(−1)^{p−1}u_{(p)} over distinct
  odd-multiplicity values, even tie-blocks cancel; Lemma V: optimal cell-vertex has ≤n+1
  distinct values). Do not re-derive. The NEW leader is peel-scale-rank-induction (owns the
  FLOOR reduction); attack GAP L as I_n≤0.
- ALWAYS import certified R11 lemmas: ladder-interleaving-identity.md (D̃(π_0⊎L)=1+2(Σ_blue-odd
  −Σ_red-even), extremal base case b=0 ⟺ (★) Σ_blue-odd≥Σ_red-even; exact D̃(L)=(2^n−(−1)^n)/3),
  positive-layer-localization.md (Σ_k λ{M≥2k} ≤ Σ_{k=1}^{⌊(a_0+1)/2⌋} y_{2k}, positive I_n-layers
  bounded by π_0's even-ranked parts alone). Do not re-derive.
- NEVER let a GAP-L builder use a scalar b-cutoff / φ(b) finite-corner pruning ("only b=0 or b<K
  reaches the tie"): REFUTED R11 — exact ties I_n=0 exist at b=2 and b=3 (F={8,8,5,4,2,2,1,1}), and
  the tie needs b up to n−1; scalar b has NO separating power. The allocation-vertex-corner engine is
  DEAD (its positive-layer lemma is banked). GAP L's residual is (★) Σ_blue-odd≥Σ_red-even, a
  cross-block dominance needing tail cancellation, NOT a per-block or per-b charge.
- NEVER re-seed the GAP-IMR integer-minimizer framing (vertex-integrality-parity's order-aware
  smoothing OR peel-integral-exchange's cross-scale rounding): DEAD R10. GAP-IMR is proven
  LOGICALLY EQUIVALENT to the target (not a reduction), GAP-IMR′ is STRONGER than target, and
  cross-scale mass transfer is blocked by the hard equalities Σπ_j=2^{n−j} (merging an even
  block can raise D̃). The Parity Lemma + Lemmas OB/V are banked only as FINISHERS once an
  integer minimizer is reached by other means — not as an engine to reach one.
- The (★) BASE SLICE IS DONE (R13): D̃(π_0⊎L)≥1 (⟺ Σ_blue-odd≥Σ_red-even, the b=0/uncut-ladder
  base case of GAP L) fully proven & certified (lemmas/base-slice-star.md) via ladder-length mutual
  induction (P_m)/(Q_m) + the D̃-Lipschitz collapse. NEVER re-attempt (★). ALWAYS import
  lemmas/base-slice-star.md (base-slice theorem + peel identities + D̃-Lipschitz lemma) and
  lemmas/hlp-breakpoint-reduction.md (WM ⟺ (★)∧[Φ(b_i)≥0], HLP ramp/breakpoint tool). The ONLY open
  wall is now the b-lift (GAP-P1′-b): reduce general F' (b>0) to the ladder base case.
- NEVER let a b-lift builder use a single-cut co-varying b→b−1 descent monovariant: REFUTED R12 at
  n=5 (non-tie failure, min reachable D̃=5>3). NEVER adopt full weak-majorization (WM) as a loaded
  IH inherited under one peel: REFUTED R13 (prefix majorization fails OFF the ladder, 477/12000; WM
  is ladder-only). NEVER use the (NEG) Q≥S_π numeric-layer bound for the b-lift: FALSE (50–77% fail,
  fails tie family — over-strengthens Q≥P by the lossy P≤S_π). The tie family is NOT the b-lift
  obstruction (Lemma TIE: D̃=1⟹I_n=0).
- NEVER let a b-lift builder use ANY π₀-fixed comparison (single-cut OR global multi-cut merge of F'→L
  with π₀ held fixed): the WHOLE family is DEAD R14 (multi-cut merge fails 970–2073/3000 n=2..5; the
  obstruction is structural in "π₀ fixed", not a granularity artifact). NEVER use the ABSORB identity
  Δ_m(R,Z)=θ+Δ_{m−1}(R⊎π_1,Z') as a b-lift ENGINE: on the b-lift instance it is a BOOKKEEPING TAUTOLOGY
  (R̄⊎F''=π_0⊎F' as multisets), and its rescaled closer gives −2θ, strictly WEAKER than trivial −θ−½
  (R14). NEVER use the clean sign-flip split-rung identity (I1′) Σ(−1)^{i−1}c_i≤θ: FALSE 3931/4000 (R14);
  the honest split-rung peel carries the OVERLAP residual λ(O_{ρ_1}∩O_{R⊎Z'}).
- THE b-lift wall IS the overlap term λ(O_{π_0}∩O_{F'})=GAP-P1 (R14): the missing ½ lives there and EVERY
  scalar/telescoping/sign bound either restates it or is vacuous. ALWAYS attack it with a NON-SCALAR
  invariant on F''s RECURSIVE dyadic cut-tree (Σaⱼ≤n), NOT any static per-scale/per-part charge. ALWAYS
  import lemmas/top-peel-general.md (R14: MAXPEEL refinement-blue max-peel + generalized red-peel (I3′));
  do not re-derive. A genuinely new far framing is needed (multi-cut/global re-choice AND single-peel
  fold-together both re-encode the wall) — seed one per CLAUDE.md shared-gap rule (plateau R11–R14).
- THE b-lift is now REDUCED to a SINGLE LEAF (R15): the CUT TOP RUNG case (a₁≥1) of the budget-aware
  mutual induction (P̂_m)/(Q̂_m)/(L̂B_m). EVERY uncut-top-rung case is CLOSED & reviewer-verified (uncut base
  = certified (★)). ALWAYS import lemmas/cut-top-rung-correction.md (correction (C) D̃(R⊎F')=D̃(ρ₁)−D̃(W)
  +2λ(E∩O_W), E={N_{ρ₁} even}∩(0,θ); + uncut-rung reductions (A1)(A2)(A3)) and continue this engine — do
  NOT re-derive or restart the b-lift from scratch. The leaf lands on the SAME GAP-P1 overlap I_S=
  λ(O_{ρ₁}∩O_W) BUT with a FRESH previously-UNUSED resource: the cut budget Σaᵢ≤m on that leaf. R16 MUST
  attack the cut-top-rung leaf USING Σaᵢ≤m — a cut rung SPENDS budget (a₁≥1), so the induction has a
  strictly smaller budget for W; find the invariant that trades the spent cut against the overlap I_S.
- NEVER re-attempt the NEG-lemma value-ranked lower bound Q≥Σz_{2k-1} (or Q≥Σz_{2k}/Σy_{2k}/termwise/tail/
  prefix layer forms): CHEAP-KILLED R15 (100% fail; Q is the negative part of M=N_{π₀}−N_{F'}, so NO bound
  dropping π₀ can lower-bound it — structural). NEVER seek a Sprague-Grundy / independent-subgame-sum
  decomposition across dyadic rungs: cross-rung D̃ effects are strongly NON-ADDITIVE (R15, joint−sum gap up
  to 6.5). The hard per-rung equality Σπ_j=2^{n-j} (NOT just the aggregate budget) supplies most of the +1
  (R15: min D̃→0.386 at n=4 if only aggregates kept). The universal split identity D̃(A⊎B)=D̃(A)+D̃(B)
  −2λ(O_A∩O_B) holds for ANY bipartition — banning π₀/F' specifically does NOT evade the overlap wall.
- THE cut-top-rung leaf's ΣR≤θ HALF IS DONE (R16): via (L̂B-inherit) [a₁≥1 spends a budget unit ⇒ the
  FULL deficient lower bound Δ(R,F'')≥min(0,θ−ΣR) is admissible on W, 0/76k] + (ΣR≤θ closure)
  Δ(R,F')≥½(θ−D̃(ρ₁))>0 [via (C), I_S≤D̃(ρ₁), alternating-sum D̃(ρ₁)≤p₁<θ, 0/58k]. Both banked in
  approaches/ladder-length-deficient-induction.md (NOT certified as standalone lemmas — conditional on the
  open IH (P̂_{m−1})). NEVER re-derive them; import from the approach file. The (L̂B-inherit) budget-trade
  IS the genuine new leverage R15 asked for — the wall is NO LONGER "no budget in hand on the overlap".
- THE SOLE OPEN GAP (R16) is the ΣR>θ (oversized-red) residual + its mirror Case IIa of the cut-top-rung
  leaf. It MUST be closed via the (TEETH) per-tooth comb mechanism: bound I_S=λ(O_{ρ₁}∩O_W) using the comb
  structure of O_{ρ₁} (⌈r/2⌉ teeth, a₁ controls tooth COUNT not MEASURE — D̃(ρ₁) is NOT a₁-monotone)
  charged against O_W's ≤2m−a₁ budget-limited breakpoints. NEVER assume the bare (TEETH)/(†) inequality
  I_S≤Δ+½θ+½D̃(ρ₁) as a lemma: it is LITERALLY the target restated by (C) (parity-mismatch measure ≥1,
  0/57k) ⇒ circular. NEVER use a scalar I_S-ceiling: VACUOUS (naive scalar inconclusive 62% of oversized
  configs, R16). The closer MUST be a genuine per-tooth (non-scalar) geometric charge.
- NEVER re-attempt the bottom-scale / bottom-value-band / near-0 Parity peel for the b-lift: DEAD R15.
  The bottom-band overlap identity D̃(F)=D̃(F_{>τ})+(−1)^{|F_{>τ}|}D̃(F_{≤τ}) (lemmas/bottom-band-overlap.md)
  is SPLIT-AGNOSTIC (odd branch = certified DIFF wall); bottom-SCALE needs D̃(G)≥2 (refuted by budget);
  bottom-VALUE-BAND F_{>τ} is not a dyadic feasible instance (no IH); near-0 surplus is INTEGER-ONLY
  (GAP-IMR needed = equivalent-difficulty R10). Import the identity as a fact; do not use it as an engine.
- THE b-lift ΣR>θ residual COLLAPSED R17 to a MEASURE-ZERO ENDPOINT SLICE ΣR=2^m. ALWAYS use, from
  approaches/ladder-length-deficient-induction.md (banked, reviewer-verified 0-fail — do NOT re-derive):
  (S1) ΣR≤2^m−1 is TRIVIAL (Δ≥0 ⟺ D̃≥ΣR−2^m+1, RHS≤0, closed by certified (NN) D̃≥0 — subsumes ALL of
  R16's θ<ΣR≤2^m−1 cut-top-rung machinery); (S2) 2^m−1<ΣR<2^m reduces to the endpoint via certified (I4)
  Lipschitz (decrease ε=2^m−ΣR); anchor D̃(F')≥1 for budgeted refinements with ≤m−1 cuts (cut-branch =
  (P̂_{m−1}) at endpoint, strictly smaller, non-circular). The whole b-lift = the ONE endpoint slice ΣR=2^m.
- THE b-lift's 2 SOLE OPEN LEAVES (R17, both razor-tight, min D̃=1 exactly at ΣR=2^m): (i) S3-U all-reds≤θ
  needs the (Q̂_{m−1}) CUT-TOP-RUNG endpoint upper bound Δ(R,F'')≤−1 — a genuinely NEW upper bound (existing
  (Q̂_m) is 2^m too weak, so build the sharpened (Q̂) at its cut-top-rung endpoint); (ii) S3-C all-reds≤θ =
  the (C) overlap wall I_S≤Δ+½θ+½D̃(ρ₁), which is the target RESTATED on this slice ⇒ NEVER assume it;
  needs a non-scalar cut-tree invariant on O_{ρ₁} vs O_W's budget-limited breakpoints. These two are the
  LAST pieces before solved.
- NEVER use the R17 "all-or-nothing tooth capture" claim (each tooth wholly inside one O_W band ⇒ I_S a 0/1
  tooth selection / rank-interleave matching): REFUTED R17 (6481/8000 leaf configs have a W-part strictly
  inside a tooth; its surviving global form = merged-order alt-sum = target, R8-banned). NEVER use a θ-red-
  forcing slack split ("no red=θ ⟹ D̃≥13/12" or the cut-top-rung min≈1.12 variant): BOTH FALSE R17 (witness
  R={3,3,2}, F'={2,2,2,1}, cut top rung {2,2}, no red=θ, D̃=1). Both R16-logged speculative directions also
  DEAD R17 (run-length recast: zero separating power; red-side MAXPEEL: re-routes to the (Q̂) mirror wall).

## State
### Done
- R1: workspace + env. Answer c(n)=2^n/(2^{n+1}−1) found & reduction proven. 3 rival
  approaches opened, ranked, built to `partial`. 3 lemmas certified. n=1 fully solved.
- R2: concavity-lp killed (f non-concave), potential-certificate retired. Field = 2
  live approaches on 2 walls.
- R3: GAP U → balanced Case (iii); GAP L → doubly-balanced GAP-LB′. New machinery
  (Invisible-Pair, RT reduction, half-total single-crosser). No reviewer ran.
- R4: 4-approach field (2 twins/wall). Pivot Lemma certified (GAP-U Case iii-a closed
  ∀n). Termwise Lattice Lemma T certified (GAP-L equality core closed). Both walls
  narrowed to ONE last sub-case each. All partial. Orthogonal framing confirmed absent.
- R5: explorer-only (no reviewer). R6: planning-only (interrupted, autocommit, no build).
- R7: **UPPER BOUND CLOSED ∀n & certified (lemmas/upper-bound.md)** — resumed R6 build
  set, both GAP-U slugs proved c(n)≤2^n/(2^{n+1}−1) independently (Realizability+subset-sum;
  Theorem R sign-pairing, op-budget resolved). GAP L sharpened: exact identity (△) +
  bounded-mass (△⋆) certified-machinery; top-down reserve IH refuted. induction-recursion
  RETHINK. Only GAP L (lower bound) remains open.
- R8: CONVERGENT NEGATIVE — no APPROVE, but a whole class of framings pruned. Seeded 3
  far-apart framings on GAP L (tiling, sequential potential, genfn double-count); all
  partial. Certified 3 lemmas (merged-order-layer, reserve-target-equivalence,
  scale-parity-xor) establishing that merged-order/measure/sequential/genfn framings are
  ALL equivalent to the target D̃≥1 and give only the trivial D̃≥0 (off by ½). Meta:
  the missing ½ must be injected NON-LOCALLY via Z's recursive dyadic cut-tree origin.
  telescope CHANGES REQUESTED (leader); cut-sequence-potential & even-rank-doublecount
  RETHINK (engines dead, lemmas banked). Field now sharply directed for R9.
- R9: plateau framing BROKEN. Seeded 2 far-apart cut-tree/2-adic approaches (vertex-
  integrality-parity, peel-scale-rank-induction); both partial/CHANGES REQUESTED. Certified
  parity-odd-total.md (the +1 injector) and peel-difference-bound.md. GAP L reduced from a
  diffuse count-parity band to TWO concrete far-apart cruxes: GAP-IMR (integer-minimizer
  reduction) and GAP-P1 (loaded dyadic-shape IH). The +1 mechanism is now understood (parity
  of the odd dyadic total 2^{n+1}−1). No APPROVE; sharpest LB progress of the run.
- R10: IMPROVED. Advanced 3 GAP-L slugs; certified 2 lemmas (floor-half-reduction.md,
  odd-block-vertex.md). peel-scale-rank-induction became LEADER: FLOOR identity collapses
  ALL of Case B to a single scalar inequality I_n=∫_(0,θ)⌊M/2⌋≤0 (M=N_{π_0}−N_{F'}). The
  whole GAP-IMR/integrality line (vertex-integrality-parity RETHINK, peel-integral-exchange)
  PRUNED: GAP-IMR proven logically EQUIVALENT to target (not a reduction); GAP-IMR′ is
  stronger than target; cross-scale transfer blocked by hard sums. No APPROVE.

- R11: IMPROVED. Advanced leader peel-scale-rank-induction + new far approach allocation-vertex-
  corner on GAP L (I_n≤0). Certified 2 lemmas (ladder-interleaving-identity, positive-layer-
  localization). Extremal base case b=0 collapsed to the clean inequality (★) Σ_blue-odd≥Σ_red-even;
  {M≤1} region + (DIFF)-shell + n=1 closed. b-scalar pruning engine REFUTED (exact ties at b=2,3) ⇒
  allocation-vertex-corner RETHINK (positive-layer lemma banked). peel CHANGES REQUESTED. Two gaps:
  GAP-P1′-a (prove (★) via cross-block dominance) + GAP-P1′-b (slice-max reduction b→0). No APPROVE.
- R12: interrupted (autocommit, no reviewer). Only coupled-cut-descent built; it REFUTED its own
  single-cut b-descent mechanism at n=5. Lemma TIE + ΔM proved. See Eval History above.
- R13: **BREAKTHROUGH — (★) base slice FULLY PROVEN & certified** (open since R3). ladder-length-
  deficient-induction closed (★) via ladder-length mutual induction (P_m)/(Q_m) + D̃-Lipschitz
  collapse (missing ½ injected by CONTINUITY). peel confirmed its (★) route is the same wall (HLP
  breakpoint reduction certified). qlayer-charge-induction killed ((NEG) false). Certified
  base-slice-star.md + hlp-breakpoint-reduction.md. GAP L now reduced to ONLY the b-lift (no live
  route). Both builds CHANGES REQUESTED/partial; whole problem still partial.
- R14: CONVERGENT NEGATIVE on the b-lift. 2 explorers (multicut + peelinduction) surfaced ABSORB
  identity + two-param split-rung openings; outliner opened both as NEW slugs; outline-reviewer
  killed leader peel-scale (RETHINK, reused banned (NEG) bound). Built split-rung-mutual-induction +
  absorb-rescale-induction; BOTH RETHINK (independently verified: (I1′) FALSE 3931/4000, ABSORB a
  bookkeeping tautology, π₀-fixed multi-cut merge dead). WALL SHARPENED to overlap term
  λ(O_{π_0}∩O_{F'})=GAP-P1. Certified lemmas/top-peel-general.md. Whole problem still partial.
- R15: IMPROVED. b-lift REDUCED to a SINGLE LEAF (cut top rung a₁≥1) via a budget-aware mutual induction
  (P̂_m)/(Q̂_m); ALL uncut-top-rung cases CLOSED & reviewer-verified. Fresh unused resource on the leaf:
  the cut budget Σaᵢ≤m. bottom-band-peel-induction RETHINK/retired (rigorous negative). Certified
  cut-top-rung-correction.md + bottom-band-overlap.md. NEG-lemma value forms + independent-subgame
  decomposition cheap-killed. See Eval History R15 for full detail. Whole problem still partial.
- R16: IMPROVED. Closed the cut-top-rung leaf's ΣR≤θ half via (L̂B-inherit) budget-trade + (ΣR≤θ closure);
  both 0-fail reviewer-verified, banked (conditional on open IH, not certified). Residual = ΣR>θ TEETH.
- R17: IMPROVED. Whole ΣR>θ residual COLLAPSED to a measure-zero endpoint slice ΣR=2^m. (S1) ΣR≤2^m−1
  trivial (closed by D̃≥0, subsumes R16's TEETH machinery) + (S2) Lipschitz fill to endpoint + anchor
  D̃(F')≥1 (≤m−1 cuts) all banked & 0-fail verified. R17 TEETH all-or-nothing capture REFUTED; θ-red slack
  split FALSE; both speculative directions DEAD (no far-apart slug — lean field). 2 razor-tight endpoint
  leaves left: (i) (Q̂_{m−1}) cut-top-rung UB Δ(R,F'')≤−1; (ii) (C) overlap wall. CHANGES REQUESTED/partial.
  Elo: ladder-length-deficient 1736 (leader), peel-scale 1715 (parked).

### Broken (b-lift COLLAPSED R17 to a measure-zero endpoint slice ΣR=2^m, 2 open leaves; (★) DONE R13; UB DONE R7)
- GAP L (b-lift, GAP-P1′-b) — THE SOLE OPEN WALL. Reduced (R15) to the cut-top-rung leaf; R16 closed the
  ΣR≤θ half; **R17 COLLAPSED the whole ΣR>θ residual** via (S1) [ΣR≤2^m−1 trivial, closed by D̃≥0] + (S2)
  [2^m−1<ΣR<2^m → endpoint via (I4) Lipschitz]. The whole b-lift now = the single **measure-zero endpoint
  slice ΣR=2^m** (integer-rigid). Split by F''s top rung: 2 leaves CLOSED by descent (S3-U big-red →
  (P̂_{m−1}); pure-blue/{θ,θ} tail → anchor D̃(F')≥1 at ≤m−1 cuts). **THE 2 SOLE OPEN LEAVES** (both razor-
  tight, min D̃=1 exactly): (i) **S3-U all-reds≤θ** needs the (Q̂_{m−1}) CUT-TOP-RUNG endpoint upper bound
  Δ(R,F'')≤−1 — a genuinely NEW UB (existing (Q̂_m) is 2^m too weak); (ii) **S3-C all-reds≤θ** = the (C)
  overlap wall I_S≤Δ+½θ+½D̃(ρ₁) = target restated on this slice ⇒ NEVER assumed; needs a non-scalar cut-tree
  invariant on O_{ρ₁} vs O_W's budget-limited breakpoints. Dead so far (do NOT re-run): the (TEETH) per-tooth
  comb charge + all-or-nothing capture (R17, REFUTED 6481/8000); θ-red-forcing slack split (R17, FALSE);
  single-cut b→b−1 descent (R12); full-WM-IH (R13); (NEG) Q≥S_π (R13/R14); scalar b-cutoff (R11); ALL
  π₀-fixed comparison incl. multi-cut merge (R14); ABSORB engine + clean split-rung (I1′) (R14); NEG-lemma
  value forms + independent-subgame decomposition (R15); bottom-band/near-0 Parity peel (R15); all measure/
  merged-order/sequential/genfn/GAP-IMR framings (R8/R10); run-length recast + red-side MAXPEEL (R17). These
  2 endpoint leaves are the LAST pieces before `solved`.

### Broken — HISTORICAL (both now CLOSED; kept for context)
- GAP L (lower bound, Case B): Xiang cuts Liu's top piece; need D̃≥1 (i.e. D≥u_n)
  against every ≤n-cut response. R7 REDUCED it to a single clean statement via certified
  exact identity (△) D̃=(y₁−θ)⁺+λ_(0,θ)(O_Y△O_Z), localized to bounded-mass (△⋆):
  λ_(0,θ){t: M(t) odd} ≥ ∫_(0,θ) M = 1−β  (M=N_Y−N_Z, β=(y₁−θ)⁺, always ≤1).
  Min D̃=1 EXACTLY, tie-attained (e.g. n=4 Y=(8,3,3,2) Z=(8,2,2,2,1)) — prove NON-STRICT.
  Refuted so far: scalar/aggregate-of-Z summary (R3–R4), exchange/difference-h (R4),
  top-down/top-anchor reserve IH (R7), global budget-count (R7 RETHINK). Compensation is
  bottom-inclusive/global across dyadic scales — surplus concentrates in the near-0
  count-parity band. R8 PROVED all static/profile framings are equivalent to the target
  (dead ends): merged-order tiling (circular), sequential potential (reserve⟺target),
  genfn (non-additive). The ½ must come NON-LOCALLY from Z's recursive dyadic cut-tree
  origin (Σaⱼ≤n). R10 SHARPENED the reduction to a single clean scalar inequality (below).
- GAP L (R10 sharpest form): via certified FLOOR identity (lemmas/floor-half-reduction.md)
  D̃(F)=1−2∫_(0,θ)⌊M/2⌋, M=N_{π_0}−N_{F'}, ALL of Case B ⟺ **I_n:=∫_(0,θ)⌊M/2⌋ ≤ 0**,
  tie-attained at 0. Verified 0 violations n≤6. Budget Σaⱼ≤n enters ONLY via M(0⁺)≤1, which
  ALONE is insufficient (§7a decoy) ⇒ must control the SHAPE of g=N_{F'} (Z's cut-tree
  origin). Open crux GAP-P1′: prove I_n≤0 via loaded dyadic-shape IH on g. The GAP-IMR
  integrality route is now DEAD (equivalent-to/stronger-than target).
### Next (R18)
- SOLE FOCUS: the b-lift (GAP-P1′-b) — the LAST open piece. (★) base slice + upper bound are
  DONE/certified — NO builder on either. R17 COLLAPSED the whole ΣR>θ residual to a MEASURE-ZERO ENDPOINT
  SLICE ΣR=2^m (via (S1) trivial + (S2) Lipschitz, both banked/verified). Import (S1),(S2),the anchor from
  approaches/ladder-length-deficient-induction.md — do NOT re-derive. This is the closest the run has ever
  been: 2 razor-tight endpoint leaves left.
- PRIMARY (advance ladder-length-deficient-induction): close the 2 open endpoint leaves at ΣR=2^m.
  LEAF (i) S3-U all-reds≤θ: prove the (Q̂_{m−1}) CUT-TOP-RUNG endpoint upper bound Δ(R,F'')≤−1 — a
  genuinely NEW upper bound; the existing (Q̂_m) is 2^m too weak, so BUILD the sharpened (Q̂) at its
  cut-top-rung endpoint (this is the (Q̂) mirror of the R16 (P̂) budget-trade work). LEAF (ii) S3-C
  all-reds≤θ: the (C) overlap wall — target restated on this slice ⇒ NEVER assume the bare I_S≤Δ+½θ+½D̃(ρ₁);
  needs a genuine non-scalar cut-tree invariant on O_{ρ₁} vs O_W's budget-limited breakpoints. NOTE both
  leaves are integer-rigid / measure-zero — the endpoint's arithmetic rigidity is a NEW resource not yet
  exploited (ΣR=2^m exactly, all parts dyadic-feasible); tell the explorer to scout whether integrality at
  the endpoint (parity-odd-total.md / Parity Lemma as a FINISHER now that the slice is integer-rigid) can
  finish where the continuum could not — GAP-IMR was equivalent-difficulty on the CONTINUUM, but this slice
  is already measure-zero/rigid.
- DIVERSITY (shared-gap rule, plateau R11–R17): R17 confirmed no far-apart slug survives (all-or-nothing
  capture REFUTED, both speculative directions DEAD, θ-red split FALSE). Do NOT open filler. If the 2
  endpoint leaves STALL, the explorer must first cheap-kill: (a) the endpoint-integrality/Parity-finisher
  idea above, (b) the (Q̂) cut-top-rung sharpened-UB before committing a builder to it.
- Dispatch: 1 explorer (endpoint-slice ΣR=2^m terrain: the (Q̂_{m−1}) cut-top-rung UB + whether integrality
  finishes) → outliner → outline-reviewer → builder (advance ladder-length-deficient) → one proof-reviewer.
  peel-scale-rank = parked reference. bottom-band-peel-induction + ladder-abel-pairing retired. Do NOT
  rebuild (★) or the upper bound.
- Once BOTH endpoint leaves close: the whole b-lift closes ⇒ assemble full proof (UB from
  lemmas/upper-bound.md + LB = Case A + (★) base-slice-star.md + the budget-aware b-lift engine + (S1)/(S2)/
  anchor + endpoint closure) into current.md ## Full proof, flip Status to solved → end_session candidate.
  c(n)=2^n/(2^{n+1}−1).
