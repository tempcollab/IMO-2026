# imo-2026-03 (IMO 2026 P3) — tracking

## Status
partial  (UPPER BOUND fully proven & certified for all n. GAP L / lower-bound Case B: the extremal
base slice `b=0` `(★) Σ_{blue odd}≥Σ_{red even}` — equivalently `D̃(π_0⊎L_n)≥1` for any partition
`π_0` of `2^n` into `≤n+1` parts — is **FULLY PROVEN & CERTIFIED** (round 13,
`lemmas/base-slice-star.md`). **Sole remaining open wall: the general-`b` lift (GAP-P1′-b)**. Round 15
reduced the whole b-lift, via a budget-aware ladder-length mutual induction, to the SINGLE case
"the top blue rung is CUT" (`a₁≥1`). **Round 16 further split that leaf on `ΣR` and CLOSED the
`ΣR≤θ` half** (Case IIb-1): the key was the previously-overlooked inheritance of the FULL deficient
lower bound `(L̂B_{m−1})` on `(R,F'')` — admissible because a cut top rung `a₁≥1` spends a budget
unit, freeing `a₀+b''≤m−1` — which gives `Δ(R,F'')≥min(0,θ−ΣR)=0` there, and then `(C)` +
`I_S≤D̃(ρ₁)≤p₁<θ` yields `Δ(R,F')≥½(θ−D̃(ρ₁))>0`. Reviewer independently re-verified (C),
(L̂B-inherit), the IIb-1 chain, and the budget accounting: 0 fails / 76k. **Round 17 — ENDPOINT
COLLAPSE (reviewer-verified):** the whole `ΣR>θ` residual is subsumed — `(S1)` `ΣR≤2^m−1` is TRIVIAL
by `D̃≥0` (since `Δ≥0 ⟺ D̃(R⊎F')≥ΣR−2^m+1`, RHS `≤0`), and `(S2)` `2^m−1<ΣR<2^m` Lipschitz-reduces to
the endpoint via certified `(I4)`. So the entire b-lift `(P̂_m)` collapses to the SINGLE integer-rigid
slice `ΣR=2^m`. That endpoint splits on the top rung of `F'` into four leaves: two CLOSE by induction
descent (S3-U big-red → `(P̂_{m−1})` interior; pure-blue/`{θ,θ}` tail → verified anchor `D̃(F')≥1` at
`≤m−1` cuts, whose cut branch is `(P̂_{m−1})` at endpoint), and TWO remain OPEN, both razor-tight on
the measure-zero endpoint: (i) S3-U all-reds-`≤θ` → `(Q̂_{m−1})` cut-top-rung endpoint branch; (ii)
S3-C all-reds-`≤θ` → the `(C)` overlap wall (`D̃=1` attained at `{3,3,2}⊎{2,2,2,1}`). The round-17
draft's `θ`-red-forcing slack claim was FALSE (same witness, `D̃=1`, no red `=θ`) and is correctly
retracted. Reviewer independently re-verified S1 (0/240k), S2 Lipschitz (0 viol), the anchor
(min=1 at `≤m−1` cuts, drops <1 at `m` cuts), the retraction witness, and the endpoint target
(min `D̃=1`). No banned/circular closer smuggled. The whole problem stays `partial` until these two
endpoint leaves close.)

## Answer (target, verified)
c(n) = 2^n / (2^{n+1} − 1)  =  (1+u)/2  with  u := 1/(2^{n+1} − 1).
Values: c(1)=2/3, c(2)=4/7, c(3)=8/15. Confirmed by full-game brute force at
n=1 (=2/3) and n=2 (=4/7). The UPPER bound c(n) ≤ 2^n/(2^{n+1}−1) is now proven for ALL n
(round 7, certified `lemmas/upper-bound.md`; reviewer-verified end-to-end). The LOWER bound
is complete except Case B (GAP L), so the full determination is not yet closed.

## Approaches tried
- **dyadic-discrepancy** — partial (leader). Proves the shared spine (Lemma G, level-measure
  identity, cut-flip), reduces the game to the discrepancy minimax D* = u, fully solves n=1
  (both bounds), and closes lower-bound Case A (top piece uncut ⇒ D ≥ u). Open: GAP L
  (lower-bound Case B) and GAP U (general upper bound). Does NOT use the refuted "bisect n
  largest" rule.
- **induction-recursion** — partial. Same proven spine; additionally derives the exact
  block-split identity D = λ(O_top)+λ(O_bot)−2λ(O_top∩O_bot) for Case B and the recursion
  u_n = u_{n−1}/(2+u_{n−1}). Refutes bisection-only Xiang rigorously (via cut-flip). Open:
  GAP-LB (parity cancellation under shared cut budget), GAP-UB (general Xiang strategy).
- **potential-certificate** — partial (weakest / near-duplicate). Proves a genuine dead-end
  (no separable per-piece potential can certify the odd-rank functional — clean witness + LP),
  then pivots to the SAME order-aware level-set certificate as the other two. Imports the
  lower bound; upper bound open. Distinct contribution is the separability gate result.

## Current best
The problem is exactly reduced to a static discrepancy minimax. Fully proven and certified:
- **Lemma G** (`lemmas/greedy-claim.md`): alternating greedy claiming ⇒ first player's total =
  odd-rank sum b₁+b₃+…; greedy is optimal for both (ties handled).
- **Level-measure identity** (`lemmas/greedy-claim.md`): D := 2·Liu−1 = b₁−b₂+b₃−⋯
  = λ{t>0 : #(pieces>t) odd}.
- **Cut-flip / cut-budget** (`lemmas/cut-flip.md`): one cut of L into x,L−x toggles N-parity
  exactly on [0,x)∪[L−x,L); |ΔD| ≤ 2min(x,L−x); bisecting a set S keeps D(S^c); D ≥ 2b₁−1.
- **Reduction**: c(n) = (1+D*)/2 with D* = max_Liu min_Xiang D; target ⇔ D* = u.
- **n=1**: both bounds, D* = 1/3, c(1) = 2/3 (with explicit adaptive Xiang threshold rule).
- **Lower bound Case A**: dyadic partition, top piece uncut ⇒ b₁ = 2^n u ⇒ D ≥ u.

## Open gaps — round-7 status
- **GAP U (upper bound): CLOSED for all n (round 7). CERTIFIED `lemmas/upper-bound.md`.**
  Proof (dyadic-discrepancy §4.7, independently dyadic-discrepancy-euclid §A–§G): reachable
  effective totals = `{−1,0,1}`-signed sums (Realizability Lemma / Theorem R); a subset-sum
  pigeonhole on the `2^{n+1}` subset sums yields a nonzero pattern of value `≤ u_nΣ`, realized
  in `≤ n` cuts; `D = D(effective) ≤ effective total ≤ u_nΣ`. Physical-decomposition remark
  gives `D(physical)=D(effective)` via one invisible equal-pair per op. Reviewer-verified
  end-to-end (simulated physical cuts, exact arithmetic, n≤5: `D≤u_n` worst ratio 0.9998,
  `≤n` cuts, mass conserved; Theorem R 0 mismatches). Supersedes the round-4 RT (iii-a/iii-b)
  split. No refuted move (bisect-n-largest, myopic greedy, fixed schedule) is used.
- **GAP L (lower bound, Case B):** dyadic, Xiang cuts the top. Integer-unit target `D̃≥1`,
  `F=Y⊎Z`, `sum(Y)−sum(Z)=1`. Reformulated via `M=N_Y−N_Z` to `∫1[M odd] ≥ ∫M=1`.
  Proven closed on `{y₁≥2^{n−1}+1}`, `{|D_top^<−D_bot|≥1−D_top^>}`, `{|h|≤1}` (Sufficient Lemma),
  and **the whole merged-order `maxc≤1` region — CLOSED round 4** (Termwise Lattice Lemma T,
  certified `lemmas/termwise-lattice.md`; contains every tight D̃=1 config numerically).
  **OPEN residual: `maxc≥2` ("T-run" ≥2 ahead)** — provably needs `Z`'s recursive dyadic cut-tree
  (Structure Lemma anchors); scalar/count summary of `Z` is refuted. Fragment-count obstruction
  (R4): for b≥2, `|h|≥3` near 0 is forced, so the `|h|≤1`/exchange route cannot finish there.

Round-7 verdict: problem remains **partial**, but the UPPER bound is now **fully proven and
certified for all n** (`lemmas/upper-bound.md`) — GAP U is closed. The ONLY remaining wall is
GAP L (lower-bound Case B, residual `E(F) ≤ 2^n−1` ⇔ `(♠≥0)` ⇔ `(△⋆)`), owned by the two
induction slugs; it is sharply isolated but unproven (local matching, scalar/count summary of
Z, and top-down reserve of Z are all refuted — needs a global bottom-inclusive count-parity
amortization through Z's dyadic cut-tree). Once GAP L closes, the problem is solved.

## Round 8 — three far-apart framings each provably CANNOT inject the budget non-locally
Three approaches attacked the residual `(△⋆)`/`E(F)≤2^n−1` from independent framings; the
reviewer verified each result (algebra re-derived, numerics reproduced). Collectively they
establish a meta-conclusion that redirects the field: the merged-order **measure**, the
**sequential-cut**, and the **static double-count/genfn** framings are each provably equivalent
to GAP L itself (or empirically reduce to its shared non-additive core) and cannot supply the
missing constant `1` locally.

- **induction-recursion-telescope — partial (CHANGES REQUESTED), leader on the wall.** The
  assigned merged-order bounded-window nonneg-block *tiling* (crux aimo-0626) is **rigorously
  refuted as a local certificate**: (i) a consecutive nonneg-block tiling of `Σψ(c_i)Δw_i`
  exists **iff** the total is `≥0` — circular; (ii) no bounded/one-sided local window certificate
  exists (both-directional greedy fails `222/2·10⁵`; minimal witness verified — a lone depth-2
  deficit exceeds each adjacent surplus, needing the whole list). New CERTIFIED lemmas: **Lemma H**
  `maxc≤|Y|` and identity **`(△△)`** `∫(⌊M⁺/2⌋−⌈M⁻/2⌉)=½∫M−½D̃` (`lemmas/merged-order-layer.md`),
  proving every layer/summed/`(♠)`/`(△⋆)` form is a pure measure-algebra restatement of `D̃≥1`
  (trivial bound gives only `D̃≥0`, off by `½`). Merged-order block/window/matching family now
  fully eliminated (matching §10, scalar §2, top-reserve §14, tiling §15). Keep live to advance
  on `(△⋆)` via a genuinely non-local argument through Z's cut-tree.
- **cut-sequence-potential — unsolved (RETHINK).** Proves a **Reserve⇔Target Equivalence Theorem**
  (CERTIFIED `lemmas/reserve-target-equivalence.md`): an admissible amortized reserve over Xiang's
  ordered cuts exists **iff** the GAP-L target holds. So the sequential monovariant carries no
  independent leverage — it is logically no easier than the theorem. Coarse and summed-magnitude
  reserves independently ruled out. This prunes the entire sequential-count/potential family (and
  retroactively explains the retired `induction-recursion`). Approach as an independent engine is
  fatally broken; back to the outliner.
- **even-rank-doublecount — unsolved (RETHINK for the genfn mechanism).** New CERTIFIED
  reformulation **`(⊞)`** `D̃(F)=∫⊕_j 1[N_j odd] dt = ½∫(1−∏_jσ_j)` (`lemmas/scale-parity-xor.md`) —
  game-free, measure-free, keeps every scale separate. But the bivariate/scale-graded generating
  function does NOT close `E(F)≤2^n−1`: the XOR target is non-additive across scales, and the
  cheap-kill shows every near-tight config is *front-loaded* (budget on top scales) while the
  prefix-budget-ok slice has huge margin (`min D̃=4/8/9`). Genfn mechanism refuted (empirically);
  the reformulation `(⊞)` is preserved and may seed a covering/discrepancy framing next round.

**Meta-conclusion (rigorously established for the two measure/sequential framings; empirical for
the genfn).** GAP L cannot be closed by any reshuffle of the profile `M` (merged-order tiling),
by any sequential-cut potential, or by a per-scale genfn identity — each is equivalent to the
target. Next round must route through Z's **recursive dyadic cut-tree ORIGIN** (the budget
`Σa_j≤n` entering non-locally), e.g. a covering argument on the `s_j` from `(⊞)`, a two-level
joint induction across scales, or a strategy-stealing route bypassing the merged-order reduction
entirely.

## Round 9 — two far-apart NEW mechanisms, both partial; GAP L still OPEN (verdict: no APPROVE)
Two genuinely new (non-profile, not caught by the R8 meta) mechanisms attacked GAP L. Both are
honest partials with reviewer-verified new machinery; neither closes the wall. GAP L remains the
sole open gap. All lemmas below were re-derived and reproduced by the reviewer with exact
`Fraction` arithmetic.

- **vertex-integrality-parity — partial (CHANGES REQUESTED).** The original TU/vertex-integrality
  core was refuted at the R9 outline stage and correctly deleted. What survives and is CERTIFIED:
  the **Parity Lemma** (`lemmas/parity-odd-total.md`) — for any *integer* multiset of *odd* total,
  `D̃ = ΣF − 2E ≡ ΣF (mod 2)` is odd, and with `D̃ ≥ 0` gives `D̃ ≥ 1`. This is the genuine
  non-local `+1` upgrade of the trivial `D̃ ≥ 0` that no measure/merged-order/sequential/genfn
  framing can supply. Also proven: the easy direction of the **Main Reduction** (compactness +
  Parity ⇒ target, given an integer minimizer) and integer feasible min `= 1` with an explicit
  attaining family (verifies the answer is tight; enumerated `n ≤ 5`). **Sole open gap GAP-IMR:**
  prove the *global* continuum infimum `inf_{Φ_n} D̃` is attained at (equals `D̃` of) an integer
  configuration — verified `n ≤ 3` exact, non-circular (makes no reference to the value `1`), but
  the optimum can live on a fractional flat face and single-block rounding is blocked by fractional
  group-block-sums `n_g·v ∉ ℤ`, so closure needs a *global* integral mass-transfer / optimal-cell-TU
  argument. Not closed.

- **peel-scale-rank-induction — partial (CHANGES REQUESTED).** Strong induction on `n`, peeling the
  top dyadic scale `F = π_0 ⊎ F'`. CERTIFIED bundle (`lemmas/peel-difference-bound.md`): the peel
  **symmetric-difference identity** `D̃(F)=D̃(π_0)+D̃(F')−2λ(O_{π_0}∩O_{F'})=λ(O_{π_0}△O_{F'})`; the
  **difference bound** `D̃(F) ≥ |D̃(π_0)−D̃(F')|` (closes Case B on `{|D̃(π_0)−D̃(F')|≥1}`);
  **Case A (`a_0=0`) closed unconditionally** via `D̃(F)=2^n−D̃(F') ≥ 1` (uses only `D̃ ≤ Σ`, no
  value-IH — a clean new result); and **Invariant I** `M(0⁺)=(a_0+1)−|F'| ≤ 1`. **Sole open gap
  GAP-P1:** Case B on the residual near-balance region `{|D̃(π_0)−D̃(F')|<1}` needs a *loaded
  dyadic-shape* invariant on `F'`; the plain value-IH `D̃(F')≥1` is provably insufficient (verified
  witness `D̃(F')=2.506`, `D̃(π_0⊎F')=0.146`). The loaded invariant is not yet proven both inherited
  and sufficient; circularity risk (must be strictly stronger than `D̃≥0` yet not the target itself)
  is spelled out but unresolved. Not closed.

**R9 meta.** Both new mechanisms bottom out on the *same* residual difficulty: injecting the
constant `1` requires a genuinely GLOBAL argument (integer-minimizer reduction across all dyadic
scales; loaded IH capturing `F'`'s recursive dyadic origin). This is the "inject the `½`
non-locally via Z's cut-tree" wall, now approached from two non-profile directions but still open.
Both route the `+1` through the odd-total parity / dyadic `+1` dominance; if both stall again, the
shared-wall signal says seed a mechanism that routes the constant WITHOUT the odd-total parity
(2-adic valuation through the ±-operation tree; shadow/position-map to the `D̃=1` zigzag family).

## Round 10 — GAP L still OPEN; one route sharpened, the integer-minimizer engine refuted
Three GAP-L builds; no APPROVE. GAP L remains the sole open wall. Reviewer re-derived every new
identity and reproduced all numerics with exact `Fraction`.

- **peel-scale-rank-induction — partial (CHANGES REQUESTED), sharpest route.** NEW **floor-half
  reduction (FLOOR)** CERTIFIED (`lemmas/floor-half-reduction.md`): `D̃(F)=1−2∫_{(0,θ)}⌊M/2⌋`, so the
  *entire* Case B collapses to the single scalar inequality `I_n:=∫_{(0,θ)}⌊M/2⌋ ≤ 0` (tie `D̃=1`
  ⟺ `I_n=0`). Proof self-contained from the certified peel identity + `1[m odd]=m−2⌊m/2⌋`; reviewer
  re-derived (`∫M=1−β`) and verified `0` mismatches. Layer form exposes even-vs-odd thresholds as the
  arithmetic origin of the missing `½`. Two structural findings pinned: the budget `Σa_j≤n` enters
  ONLY via `M(0⁺)≤1` (Invariant I), and `M(0⁺)≤1` alone is insufficient (decoy) — the loaded IH must
  control the *shape* of `g=N_{F'}`. **Sole open gap GAP-P1′:** prove `I_n ≤ 0` (a single scalar
  inequality with explicit integrand). Genuine sharpening of R9 GAP-P1; the reduction is unconditional
  and exact, only the closing IH is open.

- **peel-integral-exchange — partial (CHANGES REQUESTED), NEW slug.** Two NEW promotable lemmas
  CERTIFIED (`lemmas/odd-block-vertex.md`): **Lemma OB** `D̃=Σ_p(−1)^{p−1}u_{(p)}` (descending
  odd-multiplicity values; even blocks cancel) and **Lemma V** `K≤n+1` distinct values at a minimizing
  cell-vertex (LP active-constraint count). Reduces GAP-IMR to the finite lattice statement **GAP-IMR′**
  ("some optimal cell-vertex is integer ⇒ target", via Parity Lemma), and localizes all vertex
  fractionality to *even* tie-blocks fed `≥2` parts by one scale (harmless to `D̃`, but obstructing
  integralization). **Open wall:** cross-scale non-increasing integral rounding — mass cannot cross a
  scale's hard sum `Σπ_j=2^{n−j}`, and a budget-reallocating merge of a small-scale even block can
  raise `D̃` (`(4,2,½,½): 2→3`). GAP-IMR′ verified `n≤3`. CAUTION: shares the integer-minimizer wall
  shown equivalent-difficulty below; GAP-IMR′ is stronger than target (⇒ but not ⇐), so it may be
  unattainable at large `n` — keep only if OB/V lead somewhere the peel route does not.

- **vertex-integrality-parity — RETHINK (engine refuted).** Round-10 is a rigorous NEGATIVE. (i)
  PROVED **GAP-IMR ⟺ target** (`⟺ μ=1`) once integer-min`=1` (Part 2, proven) is used: the
  integer-minimizer framing is a *reformulation*, not a difficulty-reducing reduction — this corrects
  the R9 "non-circularity" note. (ii) REFUTED the order-aware smoothing engine: its only non-trivial
  case (a fractional global minimizer) is vacuous for `n≤3` (exact LP: `0/90`, `0/1134` min-value
  vertices are integer), and at the isolated fractional vertices that exist off-optimum
  (`{4,2,⅓,⅓,⅓}`, `D̃=7/3`) NO `D̃`-non-increasing feasible move exists, so the descent cannot start.
  The Parity Lemma (already certified) and the reduction survive only as a *finishing device* folded
  into the peel route. The standalone integer-minimizer/mass-transfer engine cannot close GAP L — back
  to the outliner (per the builder's own recommendation: retire the standalone engine, concentrate on
  the peel real-valued induction).

**R10 meta.** The integer-minimizer routing (both GAP-IMR slugs) is now proven equivalent-difficulty
to the whole lower bound — no free lunch from integrality. The cleanest live route is
`peel-scale-rank-induction`'s FLOOR reduction: GAP L `⟺ I_n=∫⌊M/2⌋≤0`, a single explicit scalar
inequality whose only open content is a loaded dyadic-shape IH on `g=N_{F'}`. Lemma OB (exact even/odd
block decomposition) is a natural potential for a global monovariant descent to the canonical integer
`D̃=1` family. Certified this round: `lemmas/floor-half-reduction.md`, `lemmas/odd-block-vertex.md`.

## Round 11 — GAP L still OPEN; extremal base case reduced to one clean inequality; b-pruning refuted
Two GAP-L builds; no APPROVE. GAP L remains the sole open wall. Reviewer re-derived every new
identity and reproduced all numerics with exact `Fraction`.

- **peel-scale-rank-induction (LEADER, CHANGES REQUESTED, partial).** Attacked `I_n≤0` on the
  extremal slice `b=0`, where `F'` is forced to the uncut ladder `L={2^{n−1},…,1}`. NEW **ladder-
  interleaving identity `(★-id)`** CERTIFIED (`lemmas/ladder-interleaving-identity.md`, reviewer
  re-derived + verified `0` mismatches): colouring the descending merge of `π_0⊎L` red/blue,
  `D̃(π_0⊎L) = 1 + 2(Σ_{blue odd} − Σ_{red even})`, so the entire base case is the single clean
  inequality `(★) Σ_{blue odd} ≥ Σ_{red even}`, `D̃=1` iff equality. Base case closed on (a) `{M≤1}`
  (≈88%), (b) the `(DIFF)` shell `|D̃(π_0)−D̃(L)|≥1` with exact `D̃(L)=(2^n−(−1)^n)/3`, and (c) all
  `n=1`. **Open GAP-P1′-a:** the residual cross-block ladder-dominance form of `(★)` (the naive
  per-block charge `Σ_{red even}≤Σ⌈m_i/2⌉b_i` is proven INSUFFICIENT, fails ≈51%; needs cross-`k`
  tail cancellation). **Open GAP-P1′-b:** reduction of general `b` to `b=0` (the pointwise per-cut
  monovariant holding `π_0` fixed is FALSE, ~30% violations — must be a slice-max statement).

- **allocation-vertex-corner (RETHINK, unsolved as an engine).** Non-recursive finite classification
  of the allocation vector via certified Lemma V. Its intended pruning engine — an allocation-monotone
  `φ(b)` with `φ(b)<0` for `b≥1`, isolating the tie to `b=0` — is **REFUTED by exact witnesses**
  (reviewer-reproduced): exact ties `I_n=0` occur at `b=2` (`n=4`, `F={8,8,5,4,2,2,1,1}`, `D̃=1`) and
  `b=3` (`F={8,8,3,3,2,2,2,2,1}`, `D̃=1`), so the scalar `b` has NO separating power for the tie set.
  What SURVIVES and is CERTIFIED: the **Positive-Layer Localization Lemma**
  (`lemmas/positive-layer-localization.md`, reviewer re-derived + verified `0` violations, tight)
  `P := Σ_k λ{M≥2k} ≤ Σ_{k=1}^{⌊(a_0+1)/2⌋} y_{2k}` — the positive layers of `I_n` are controlled by
  `π_0`'s even-ranked parts; positive contribution requires `a_0` large. The route's engine is dead
  (closing `I_n=P−Q≤0` still needs `Q≥P`, i.e. `F'`'s recursive cut-tree — the shared wall); back to
  the outliner. Lemma banked.

**R11 meta.** GAP L is now pinned to a single combinatorial inequality on the extremal slice:
`(★) Σ_{blue odd} ≥ Σ_{red even}` in the merge of any `π_0` (`Σ=2^n`) with the uncut ladder `L`. Its
truth is certain (min `D̃=1` exactly, `n≤6`); the missing step is a cross-block ladder-dominance
charge surviving cross-`k` cancellation (GAP-P1′-a), plus the slice-max reduction of general `b` to
`b=0` (GAP-P1′-b). The `b`-scalar carries no pruning power (exact ties at `b=2,3`). Certified this
round: `lemmas/ladder-interleaving-identity.md`, `lemmas/positive-layer-localization.md`.

## Round 15 — b-lift reduced to the SINGLE cut-top-rung case (uncut cases all closed); one negative retired; 2 lemmas certified
Two b-lift builds; no APPROVE (whole problem stays `partial`). Reviewer re-derived every identity
and reproduced all numerics with exact `Fraction` (4 identities 0-fail; (P̂)/(Q̂) statements
0-fail 44k/50k).

- **ladder-length-deficient-induction — partial (CHANGES REQUESTED), leader on the b-lift.** A
  budget-aware ladder-length mutual induction `(P̂_m)/(Q̂_m)/(L̂B_m)` generalises the certified
  `(P_m)/(Q_m)/(LB_m)` engine from blue = uncut ladder `L` to blue = an arbitrary BUDGETED dyadic
  refinement `F'` (rung `i` sums to `2^{m−i}`, `Σa_i` cuts, budget `a₀+Σa_i≤m`). **Every case whose
  top blue rung is UNCUT is rigorously closed** (Case I via the Δ-form reductions (A1)/(A2)/(A3) +
  the inherited `(P̂_{m−1})/(Q̂_{m−1})`; `(L̂B_m)` via the certified D̃-Lipschitz collapse; `(Q̂_m)`
  `y>θ` branch unconditionally). The certified base slice `(★)` is exactly the all-uncut subcase.
  **The whole b-lift is thereby reduced to the SINGLE residual case "top blue rung is CUT"**, whose
  exact peel is the new CERTIFIED correction **(C)** `D̃(R⊎F')=D̃(ρ₁)−D̃(W)+2λ(E∩O_W)` (equiv.
  `Δ(R,F')=Δ(R,F'')+½θ+½D̃(ρ₁)−I_S`, `I_S=λ(O_{ρ₁}∩O_W)`, `E={N_{ρ₁} even}∩(0,θ)`), which carries
  the below-`p_r` tail flip exactly. **Sole open gap:** bound `I_S` (= the certified GAP-P1 overlap
  wall) — now with the NEW available resource that the cut budget `a₀+Σa_i≤m` constrains `a₁`
  non-locally (so far unexploited). SPEC FACT confirmed: the b-lift is FALSE without the budget
  (`π₀={2,2}, F'={3/2,3/2}` at n=2 gives `D̃=0`; rung-sums + 7 cuts at n=2 gives `D̃=0`) — the
  budget `Σa_i≤n` is load-bearing and non-local (consistent with rounds 6–14). Certified:
  `lemmas/cut-top-rung-correction.md` ((C) + (A1)/(A2)/(A3), all 0-fail). Advance vs R14, which had
  NO live route: the b-lift is now a single concrete case with a fresh (budget) resource.

- **bottom-band-peel-induction — unsolved (RETHINK / retired).** Honest structural NEGATIVE. The
  value-threshold bottom split has the exact CERTIFIED identity `D̃(F)=D̃(F_{>τ})+(−1)^{|F_{>τ}|}
  D̃(F_{≤τ})` (`lemmas/bottom-band-overlap.md`), but it is split-agnostic: the odd branch IS the
  certified DIFF/overlap wall. Three cheap-kill sub-routes each die (verified witnesses): scale peel
  needs `D̃(G)≥2` which fails on the budget (`F={2,2,1,1,1}`, `D̃(G)=0`); value-band peel has no IH
  (`F_{>τ}` is not a feasible sub-instance, `F={4,4,2,2,1,1,1}`, `D̃(F_{>1})=0`); the parity/near-0
  injector needs integers (`z_min→0` on reals; GAP-IMR is equivalent-difficulty, R10). Framework
  retired; its exact identity banked.

**R15 meta.** The b-lift is now pinned to ONE case (cut top rung) with a NEW load-bearing resource
(the global budget constrains how finely the top rung can be cut). The overlap term `I_S`
(= GAP-P1) is still the wall, but for the first time it is isolated to a single split with the
budget explicitly available. Next round: attack `I_S≤½θ+½D̃(ρ₁)+Δ(R,F'')` using `a₁≤m−a₀−Σ_{i≥2}a_i`
via a NON-scalar invariant on the cut rung's fragment structure. Certified this round:
`cut-top-rung-correction.md`, `bottom-band-overlap.md`.

## Round 16 — cut-top-rung leaf split on ΣR: the ΣR≤θ half CLOSED; residual sharpened to the oversized-red TEETH parity; no APPROVE
One b-lift build (ladder-length-deficient-induction); no APPROVE (whole problem stays `partial`).
Reviewer independently re-derived (C) and re-verified every banked step with exact `Fraction`
(76k leaf configs, 0 fails on all of: the (C) identity, (L̂B-inherit), the IIb-1 bound chain, the
budget accounting `a₀+b''≤m−1`, the mass identity `D̃(W)=2Δ(R,F'')+ΣR−(θ−1)`, the even-complement
identity `λ(E∩O_W)=D̃(W)−I_S`, and the parity-mismatch reformulation).

- **ladder-length-deficient-induction — partial (CHANGES REQUESTED), leader on the b-lift.** TWO
  sound, honestly-reported advances: **(1) (L̂B-inherit)** — on the cut-top-rung leaf the FULL
  deficient lower bound `(L̂B_{m−1})` (not merely `(Q̂_{m−1})`, as the R15 file wrongly stated) is
  admissible on `(R,F'')`, because `a₁≥1` spends a budget unit so `a₀+b''≤m−a₁≤m−1` — exactly the
  hypothesis set of `(L̂B_{m−1})` (itself `(P̂_{m−1})` + certified Lipschitz collapse). Yields
  `Δ(R,F'')≥min(0,θ−ΣR)`. This is the genuine budget-trade R16 was asked to find. **(2) ΣR≤θ closure
  (IIb-1)** — with `ΣR≤θ` the floor is `0`, so `Δ(R,F')≥½θ+½D̃(ρ₁)−I_S≥½(θ−D̃(ρ₁))>0` via
  `I_S≤D̃(ρ₁)` and the alternating-sum bound `D̃(ρ₁)≤p₁<θ` (largest part `<θ` since the rung is cut).
  Both correct. **Sole open wall: the OVERSIZED-red leaf `ΣR>θ` (Case IIb-2 + `(Q̂)`-mirror IIa).**
  Reviewer confirmed the builder did NOT overclaim it: the required `I_S`-bound `(†)` is proven
  (verified) to be *logically equivalent to the target*, so it is honestly marked open (not assumed as
  a lemma) — no circular reasoning is passed off as progress. The scalar `I_S≤D̃(ρ₁)` ceiling is
  vacuous here (true min `Δ→0.062`, razor-tight); closure needs a per-tooth comb charge on `O_{ρ₁}`
  (`⌈r/2⌉` teeth) versus the `≤2m−a₁` budget-limited breakpoints of `O_W`.

**R16 meta.** Real forward motion — the leaf, opened in R15, is now half-closed (`ΣR≤θ`) with the
budget spent non-locally exactly as the plateau plan required; the wall shrinks to the oversized-red
`ΣR>θ` TEETH parity. NOT certified this round: (L̂B-inherit) and (ΣR≤θ closure) are valid
inductive-step reductions but each is CONDITIONAL on the still-open IH `(P̂_{m−1})` (the induction has
not closed while IIb-2/IIa remain open), so they are not standalone unconditional theorems yet — they
stay banked in the approach file and will be certifiable once the leaf closes. No banned route was
smuggled: the `(L̂B)` inheritance is the certified R13 deficient-total form (NOT the refuted scalar
`D̃≥ΣY−ΣZ`), and the vacuous scalar `I_S`-ceiling is used ONLY where it is valid (`ΣR≤θ`) and
explicitly avoided on the oversized leaf.

## Round 14 — b-lift: two new framings BOTH RETHINK (each provably re-encodes the certified overlap wall); one master lemma certified
Two far-apart b-lift approaches were built; both are honest structural NEGATIVES (no APPROVE). GAP L
still reduces to the b-lift (GAP-P1′-b). Reviewer re-derived every identity and reproduced all
numerics with exact `Fraction` (5 identities, 0 fails each).

- **split-rung-mutual-induction — unsolved (RETHINK).** The outline's load-bearing clean split-rung
  identity `(I1′)` `Δ_m=2^m−1−ΣR−Δ_{m−1}(R,Z')+D̃(ρ_1)` is **FALSE** — reviewer-confirmed witness
  (`m=2`, `R={1}`, `ρ_1={3/2,1/2}`, `Z'={1}`): true `Δ_2=3/2`, clean form gives `3`; exact sweep
  fails `3931/4000`. The honest split-rung peel identity `(†)`
  `D̃(R⊎ρ_1⊎Z')=D̃(R⊎Z')+D̃(ρ_1)−2λ(O_{ρ_1}∩O_{R⊎Z'})` (verified 0/4000) is just the certified
  SD/PEEL, whose residual `I_S=λ(O_{ρ_1}∩O_{R⊎Z'})` is exactly the certified odd-set OVERLAP wall
  (GAP-P1). The only clean scalar bound `0≤I_S≤D̃(ρ_1)` telescopes to the vacuous `Δ_m≥½(D̃(R)−ΣR)≤0`.
  The route as posed re-encodes the shared wall and cannot close → back to the outliner.
- **absorb-rescale-induction — unsolved (RETHINK).** The ABSORB identity
  `Δ(R,Z)=θ+Δ(R⊎π_1,Z')` (verified 0/3000) is on this instance a **bookkeeping tautology**:
  `R̄⊎F''=π_0⊎F'` as multisets, so `Δ_m(R̄,F'')=½D̃(π_0⊎F')−2^m−½` and the "reduced" statement
  `Δ_m(R̄,F'')≥−θ` is *literally the original target* `D̃(π_0⊎F')≥1`. The outline's rescaled deficient
  bound gives only `Δ_m(R̄,F'')≥min(0,2^m−ΣR̄)=−2θ`, **strictly weaker than the trivial `D̃≥0` bound**
  (`−θ−½`) by `θ−½` (reviewer-confirmed, `m=2..5`). Its only scale-reduction step runs through the
  split-rung split-top-rung peel `(I1′)`, so it is NOT independent of the sibling approach → back to
  the outliner.

**R14 meta (diversity collapse — orchestrator action).** Both live b-lift approaches bottom out on
the SAME object: the split-top-rung odd-set overlap `λ(O_{ρ_1}∩O_{R⊎Z'})` (= GAP-P1). They are not
independent (absorb's only closer is split-rung's `(I1′)`); by the single-gap rule they would die
together. Next round MUST seed ≥1 genuinely different b-lift framing that attacks the overlap term
with a NON-scalar loaded invariant on `F'`'s recursive cut-tree — not another top-rung peel.
**Certified this round:** `lemmas/top-peel-general.md` (master top-peel `D̃(P)=max(P)−D̃(P∖max)` +
its arbitrary-blue red-peel corollary `(I3′)`, subsuming both approaches' banked forms; a bookkeeping
tool, NOT a closer). No lemma over-claimed as a closer.
