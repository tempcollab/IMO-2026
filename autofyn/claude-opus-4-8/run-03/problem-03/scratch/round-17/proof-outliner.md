## imo-2026-03

Two walls, one field. LOWER gets a genuinely NEW cross-scale slug (direction (iii),
value-layer-cake × ONE-REC scale-of-origin); UPPER advances the leader on the deep interior
via the extremal/worst-profile recipe (the recipe that actually closed the boundary layer),
with the untested full-tree second moment demoted to a gated make-or-break FIRST STEP.
A third LOWER slug (rearrangement, direction (ii)) is put up as far-apart breadth but is
BUILD-GATED (no prose before a passing numeric gate). All 9 dead lower levers and 7 dead
upper mechanisms are respected — none re-opened; the closed boundary layer is not re-touched.

---

### scale-origin-layercake : new (LOWER)

Target: the whole lower bound — Liu Bang can guarantee ≥ c(n)L, i.e. D(S) ≥ u_n·(2^{n+1}−1) = 1
after the certified reduction, which is exactly MID-core `μ{g odd} ≥ 1` for every budget-respecting
`a=0` refinement with |F|≥3. Equivalently, prove the certified cross-scale residual

   (★)   Σ_{i≥1} μ{g ≥ 2i}  ≤  Σ_{i≥1} μ{g ≤ 1−2i}      (⟺ D ≥ 1, via D = 1 − 2∫⌊g/2⌋).

Technique: value-side layer-cake (co-area slicing by g-VALUE, a genuinely different axis than R16's
dead per-DOMAIN-band slicing) PAIRED with a self-referential per-cell cap indexed by dyadic
scale-of-origin — an aimo-0009-style "index-into-itself" structural cap (scale-of-origin `j` is the
second, structurally-determined index playing the role of `a_i` inside `a_{a_i}`). This is the FIRST
lower lever to use BOTH BLK (finite value count) and ONE-REC (per-scale mass `ΣG_j = 2^j`, ≤1 excess
fragment) jointly; every one of the 9 dead levers used at most one structural fact.

Skeleton:
  1. Import — no re-proof — Lemma MID (`D=μ{g odd}`, `∫g=1`, `g=N_F−N_B` on `(0,2^{n-1})`),
     Lemma CLIP (τ=0 face `∫φ(g)=D−1`), and the IDENTITY `D = 1 − 2∫⌊g/2⌋` (this is CLIP's τ=0 face
     rescaled by −½ per the Rules — use as an identity, do NOT attempt to re-certify it as "Lemma FLR").
     By the standard layer-cake split of `⌊g/2⌋` this makes the target exactly (★).
  2. Level-set structure — by BLK + ONE-REC. Each super-level set `{g ≥ 2i}` and each sub-level set
     `{g ≤ 1−2i}` is a finite union of intervals (BLK: ≤ n+2 distinct g-values), and every such
     interval sits inside a fragment whose boundary is generated at a determined dyadic scale-of-origin
     `j` (which ladder piece `2^j` it refines — ONE-REC gives `ΣG_j = 2^j`, ≤1 excess fragment per `j`).
     This assigns every unit of super-/sub-level measure a pair `(i, j)` = (g-level, scale-of-origin).
  3. Per-cell cap [THE HARD STEP] — build a per-`(i,j)` inequality of aimo-0009 form
     `α_{i,j} + β_{i,j} ≤ (structural bound from ONE-REC's 2^j mass)`, where `α_{i,j}` is the super-level
     measure at level `i` charged to scale `j` and `β_{i,j}` is a matching sub-level (credit) measure at
     a SHIFTED level, the shift/cap coming from the scale-of-origin constraint (not a running scalar).
     To exceed `g ≥ 2i` at a point you need ≥ 2i more F- than B-fragments covering it; ONE-REC bounds
     how much such excess a scale-`j` fragment can supply, and the same fragment's complementary mass
     forces matching low-`g` (credit) measure elsewhere in its scale — this is the cross-level lending
     the gate below shows is REAL (level 1 runs a deficit repaid by `i≥2`).
  4. Sum over `(i,j)` — the per-cell caps telescope against the fixed total `∫g = 1` (aimo-0127 pattern:
     level-indexed tail-count sum, each capped by a STRUCTURAL bound, summing exactly to the fixed total),
     yielding (★). Conclude D ≥ 1, hence the lower bound, for all |F| ≥ 3 (|F|=2 and 0≤g≤1 already closed).

Key lemmas (claim + one-line mechanism):
  - LEVEL-SCALE ASSIGNMENT — every interval of `{g≥2i}`/`{g≤1−2i}` has a well-defined scale-of-origin `j`
    with `ΣG_j = 2^j` — because ONE-REC makes `B_{≤ℓ}` a refinement of `C_ℓ` with ≤1 excess fragment per
    dyadic group, so each fragment carries a determined coarsest generating scale.
  - PER-CELL CAP `α_{i,j}+β_{i,j} ≤ f(2^j,i)` [LOAD-BEARING, UNPROVED] — because a scale-`j` fragment of
    total mass `2^j` can raise `g` above `2i` on at most a bounded sub-measure while its complement forces
    matching credit measure `{g ≤ 1−2i'}` at a shifted level within the same scale (the self-referential
    coupling), exactly the aimo-0009 `a_{a_i}` mechanism. THIS is the whole content; it must be stated as a
    concrete inequality and gated (below) before any prose.

Open gaps: step 3 (the per-cell cap) is the entire difficulty — the builder must (a) WRITE the exact
per-`(i,j)` inequality, (b) prove step 2's clean scale-assignment, (c) prove the telescoping in step 4.
Steps 1–2 are import + BLK/ONE-REC bookkeeping.

MAKE-OR-BREAK GATE (exact `Fraction`, n=4,5,6 — RUN BEFORE ANY PROSE):
  The builder must first commit the concrete per-cell inequality `C(i,j)` from step 3, then verify it has
  0 exceptions across ≥ 1000 budget-respecting adversarial `a=0` refinements per n, INCLUDING the
  explorer's i=1-termwise-FAILING witnesses (e.g. n=4 `F={7.586,0.932,7.482}, B={1,2,4,4.241,0.844,2.915}`
  scaled, where `μ{g≥2}=3.241 > μ{g≤−1}=2.915`). The gate must confirm the cap absorbs the i=1 deficit via
  the `i≥2` scale-credit — i.e. `C(i,j)` holds cell-by-cell even where the termwise per-level claim fails.
  KILL CONDITION: if no per-cell inequality summing to (★) survives (any exception on the i=1-failing
  witnesses), the direction collapses to plain layer-cake (i) = MID-core restated → retire (do NOT ship a
  dressed tautology). Do NOT gate (★) itself — it is certified true (0/900 last round); gate the CAP.

Cases to cover: |F|≥3 only (|F|=2, 0≤g≤1 closed by certified MID). Both parities of scale count.
Watch out for: (a) the per-cell cap silently BEING (★) rearranged (loss-free reframing = dead, like the
transform and vertex-polytope levers) — the reviewer must check `C(i,j)` is a genuinely LOCAL cell bound
proved from ONE-REC's `2^j` mass, not a global restatement; (b) do NOT slice by domain-position (dead R16);
(c) the scale-of-origin must be structurally determined, not a free running scan (all scalar reserves dead).

---

### breakpoint-vertex : advance (UPPER)

Target: the whole upper bound — Xiang Yu forces D ≤ u_nL for EVERY profile, hence c(n) is tight. Boundary
layer `a₁ ≥ (L−u_nL)/2` is CLOSED (Lemma WTC, do not re-touch). Sole open region: the DEEP interior
`a₁ < (L−u_nL)/2`, where the residual is the first-gap pigeonhole `min_{∅≠T} descKK(T) ≤ u_nL`
(certified FGR object, R-COV' sufficiency). Deep interior carries genuine, non-shrinking margin
(worst Φ/u_n = 0.34–0.56 at n=4..7) so a NON-tight lever is admissible here (VALLEY-TIGHT's no-margin ban
applies only to the closed boundary layer).

Technique (PRIMARY): extremal / worst-profile characterization + smoothing — the same "pin the extremizer,
bound it there, smooth everything else toward it" recipe that certified WTC (boundary) and VALLEY-TIGHT.
Redirected at the deep interior where a margin exists, so only a bound (not exact tightness) is needed.
This is NOT an averaging/ensemble argument (both fixed-order second-moment gates KILLED last round by the
rare-needle structure) and NOT any of the 7 dead upper mechanisms.

Skeleton:
  1. Import RL (𝓡(A) = tree-realizable signed subset sums), R-UV + R-COV' (sufficiency), FGR
     (`μ_{n+1}=min_i dist(a_i,R_{i−1})`), CONF (`max R_i ≤ a₁`), WTC (boundary closed). Target: over the
     deep-interior region `{a₁ < (L−u_nL)/2}`, `max_A μ_{n+1}(A) ≤ u_nL`.
  2. Finiteness/PL structure of the extremizer — by the LP-vertex / piecewise-linearity machinery already
     proven profile-independent in Theorem VERT: `μ_{n+1}` is piecewise-linear in the `a_i` (differencing
     values are `±`-combinations), so its max over the polytope `{a₁≥…≥a_{n+1}>0, Σ=L, a₁<(L−u_nL)/2}` is
     attained at a vertex — a profile with `n+1` active constraints, i.e. a structurally rigid (candidate
     near-dyadic) configuration, NOT a generic spread profile.
  3. Extremizer identification [HARD STEP H1] — characterize the vertex maximizer. Conjecture (to be
     pinned by the gate): a near-dyadic family, the deep-interior analogue of VALLEY-TIGHT's A^{(n)} but
     seated ≥ u_n/2 below L/2. Compute `μ_{n+1}` there and show ≤ u_nL with the observed 0.34–0.56 margin.
  4. Smoothing monotonicity [HARD STEP H2] — a local move (shift mass between two coordinates respecting
     the ordering + deep-interior constraint) that is `μ_{n+1}`-NONdecreasing, driving any deep-interior
     profile to the step-3 extremizer without lowering `μ_{n+1}`. Combined with step 3 gives the bound
     everywhere in the deep interior.

Key lemmas (claim + mechanism):
  - PL-VERTEX-MAX — `max μ_{n+1}` attained at a polytope vertex — because `μ_{n+1}` is a min of PL
    functions of the `a_i` (VERT machinery), and a min-of-PL max over a polytope is attained at a vertex
    of the induced arrangement.
  - SMOOTH-MONO [LOAD-BEARING] — the local mass-shift does not decrease `μ_{n+1}` — because moving toward
    the near-dyadic layout increases every forced first-gap distance `dist(a_i,R_{i−1})` monotonically
    (to be verified by the gate; this is the crux, analogous to WTC's two-sided invariant).

Open gaps: H1 (which vertex is the maximizer — is it near-dyadic?) and H2 (the smoothing move is
μ_{n+1}-nondecreasing). Steps 1–2 are import + the certified VERT PL argument.

MAKE-OR-BREAK GATE (exact `Fraction`, n=4,5,6 — RUN BEFORE PROSE):
  (G1) Extract the exact-`Fraction` argmax of `μ_{n+1}` over the deep-interior polytope at n=4,5,6.
       CONFIRM it is structurally rigid / near-dyadic (≤ a few free parameters), NOT a structureless spread.
       If the argmax is a generic spread with no pattern (as the FGR argmin was — |T|=2,3,5,4 scattered),
       H1 has no target → the extremal recipe fails, PIVOT to the gated second-moment probe below.
  (G2) Gate SMOOTH-MONO: on ≥ 500 deep-interior profiles per n, verify the conjectured local move is
       μ_{n+1}-nondecreasing with 0 exceptions. If it decreases μ_{n+1} anywhere, re-choose the move or
       PIVOT. Both gates use exact rationals, no floats.

CONDITIONAL PROBE (full-tree second moment) — build ONLY IF a gate passes; make-or-break FIRST:
  The explorer flagged the untested full tree-realizable ensemble 𝓡(A) (all Catalan-many binary
  differencing trees over all nonempty T, a strict superset of the fixed-order family). Both fixed-order
  averaging gates were KILLED (ratios 5×–100×+, growing with n) by the rare-needle structure; the full-RL
  ensemble is predicted to fail for the same reason. THEREFORE: gate it FIRST — exact-`Fraction`,
  `mean(V²)` over 𝓡(A) (or a natural sub-ensemble) ≤ (u_nL)² ROBUSTLY across n=3..6, on the same
  no-exact-zero deep-interior witnesses. Build proof text ONLY if the ratio stays < 1 with no n-growth.
  If it fails (expected), this probe is DEAD (do not ship) — the extremal recipe (primary) is the survivor.

Cases to cover: deep interior `a₁ < (L−u_nL)/2` only (boundary closed). T=∅ excluded (needs n+1 deletes).
Watch out for: (a) do NOT re-close the boundary layer or re-use any WTC-extension / single-anchor /
constructive-subset-selection bound (all dead R16); (b) the all-equal COUNT counterexample LIVES in the
deep interior — a naive dispersion/count argument is NOT automatically safe here despite the margin;
(c) if H1's extremizer is genuinely spread (not dyadic), the recipe is refuted — record it and pivot,
do not force a near-dyadic fit.

---

### block-rearrangement : new (LOWER, far-apart breadth — BUILD-GATED, no prose before a passing gate)

Target: same whole lower bound (MID-core `μ{g odd} ≥ 1`, |F|≥3) — a genuinely DIFFERENT mechanism than
scale-origin-layercake so the lower wall does not collapse to one framing (layer-cake pairing vs
rearrangement/majorization are far apart: co-area level-set pairing vs a Chebyshev/Schur inequality on the
finite multiset of block data). Put up as breadth insurance; NOT the priority.

Technique: rearrangement / symmetric-function (Chebyshev sum / majorization) on the finite multiset of
`(length_k, g_k)` over maximal constant-g blocks (≤ n+2 distinct values, BLK). Hypothesis: a provable
anti-correlation between block length and `|g_k|` (larger cancellation needs finer cuts, so high-`|g|`
blocks are short) that a Chebyshev-sum / SOS inequality converts into `μ{g odd} ≥ ∫g = 1`.

Skeleton:
  1. Import MID, BLK, ONE-REC. Reduce `μ{g odd}−∫g` to a sum over blocks `Σ_k ℓ_k·(1[g_k odd] − g_k)`.
  2. [HARD] State a concrete conjectural inequality (Chebyshev sum on sorted `(ℓ_k, |g_k|)`, or a
     majorization of the block-height profile against the fixed ladder B) that lower-bounds this sum by 0.
  3. Prove it via the rearrangement/Chebyshev inequality using the length–height anti-correlation as the
     ordering hypothesis, established from the budget constraint (only n cuts ⇒ few short high-g blocks).

Open gaps: steps 2 and 3 entirely — no concrete inequality exists yet.

MAKE-OR-BREAK GATE (mandatory BEFORE any prose, per the explorer's explicit warning): the builder must
FIRST formulate the specific Chebyshev/majorization inequality of step 2 and verify it exact-`Fraction`,
0 exceptions, n=4,5,6, ≥ 500 adversarial refinements each. If no concrete inequality can even be
formulated, or it fails the gate, DO NOT BUILD — retire as reserve. (The explorer did not gate this; it
is a reserve idea only, included so the reviewer has a far-apart lower option if scale-origin-layercake
stalls.)

Cases to cover: |F|≥3. Watch out for: the anti-correlation hypothesis may be FALSE (untested) — a single
counterexample of a long high-g block kills the ordering; gate it hard before trusting it.

---

Recommended build set for the outline-reviewer: **scale-origin-layercake (LOWER new, PRIORITY)** and
**breakpoint-vertex (UPPER advance, extremal primary + gated probe)**. block-rearrangement is reserve /
gate-only — promote to build only if the reviewer wants a second far-apart lower vehicle AND its step-2
inequality can be formulated. Every build is conditional on its make-or-break exact-`Fraction` gate.
