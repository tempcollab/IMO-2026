# Outline review — imo-2026-03, round 16 (ranking gate)

I ran the outliner's MANDATORY pre-build gate for odd-block-counting myself (exact-value +
integer-vertex enumeration). Result flips the naive read: the make-or-break is genuinely
promising at the object BLK lives on (vertices), and the apparent "collapse" is an artifact of
non-integer breakpoints — a real, flagged risk, not a refutation.

---

## odd-block-counting (NEW, LOWER) — VERDICT: CHANGES REQUESTED (build, with a hardened mandate)

**What I tested (the outliner's own gate).** The make-or-break "band-parity count" claims: at a
vertex the odd-level mass of the integer step function `g = N_F − N_B` (`∫g = 1`) is forced `≥ 1`
by the fixed dyadic group sums `2^j` — i.e. a UNIQUE band contributes an odd-level interval of
mass `≥ 1`, so `μ{g odd} ≥ 1` without cross-band cancellation.

I validated my evaluator against the certified MID example (`F={7,6,3}, B={1,2,1.5,2.5,3,5}`):
it reproduces `D(S)=5.0` exactly. Then two searches:

1. **Random NON-integer admissible refinements (float, n=3,4,5).** Here the mechanism *appears*
   to fail: near-tight `D≈1` samples do NOT concentrate (n=3: 0/21 have a single band `≥1`), and
   there are explicit admissible configs with `D≥1` but EVERY band `<1`
   (e.g. n=3 `F=[0.8,2.549,0.798,3.853], B={1,2,4}`: `D=1.695`, bands `[0.999,0,0.696]`). Taken
   alone this looks like the "collapse to MID-core restated" STOP condition.

2. **Integer refinements = vertex proxies (exact enumeration, n=3,4).** Here the mechanism is
   CLEAN: `minD=1.0`, and EVERY minimizer concentrates — n=3: **5/5** minimizers have a single
   band `≥1`; n=4: **18/18**; and there are **ZERO** admissible integer `D≥1` configs with every
   band `<1`. The per-band single-band-`≥1` rule holds with **0 exceptions** at the integer
   vertices where BLK's block structure is native.

**Reading.** The spread in (1) is caused by breakpoints falling at NON-dyadic locations, so an
odd-level interval straddles a band edge; it is not a failure of the count, it is a
breakpoint-alignment issue. At integer/dyadic-aligned vertices the count is exact and positive.
This is a real, untried mechanism (a parity-pigeonhole on the integer counts `g`, NOT an LP-dual
certificate, NOT enumeration, NOT a potential/matching/transform/merge), so it is NOT one of the 8
dead lower levers, and it is NOT the R14-banned LP-dual/Farkas lever (DUAL-CHAR bans certificate-
existence, not a direct parity count on `g`). It is the strongest lower signal since the wall went
dark at R14. Register + build.

**Hardened mandate for the builder (these are the load-bearing gaps to close, not wave through):**
- **[G1] The non-integer / non-dyadic-breakpoint case is the whole difficulty.** My gate PROVES
  the single-band rule FAILS when breakpoints are non-integer (explicit `D≥1`, all bands `<1`
  witnesses above). VERT-LOW gives min at a vertex, and R12 records that NON-integer vertices
  exist. So the builder must do ONE of: (i) prove the minimizing vertex can be taken
  dyadic-aligned / integer (a reduction), OR (ii) make the band-count ROBUST to non-dyadic
  breakpoints (bound odd-mass per band using the fixed group sum `2^j` even when an odd interval
  straddles an edge). If neither is provable, the lever recovers `≥1` only by SUMMING per-band
  bounds — which IS `μ{g odd} ≥ ∫g` = MID-core restated — and it must report the collapse and STOP.
  Do NOT ship a proof that silently assumes integer breakpoints.
- **[G2] No vertex enumeration (dead #5 / R14).** The count MUST be a scale-by-scale parity /
  pigeonhole INEQUALITY pinned by the group sum `2^j` and the ladder-fixed `N_B` parity staircase.
  "Search the vertices" is the dead vertex-polytope framing in disguise — STOP if that is the only
  proof.
- **[G3] Use integer-valuedness of `g` (counts), never integrality of block values `v_i`**
  (non-integer vertices exist). The pure-integral version is FALSE (`g≡2` on measure 1/2) — the
  dyadic group sums and ladder baseline parity are load-bearing and must be used explicitly.
- **[G4] `|F|≥3` only** (`|F|=2` and `0≤g≤1` closed inside MID). Cover all `≤ n+2` block counts.

## breakpoint-vertex (ADVANCE, UPPER) — VERDICT: HOLD from build (stays live, leader)

The outliner PRE-KILLED the constructive decimated/selection families (my read agrees; the upper
explorer independently confirms the true minimizer is an unbounded alternating-decimated
subsequence and no fixed selection family realizes `u_n`). The re-planned NON-constructive
existence-toggle lever is, as written, at high risk of being the DEAD covering-radius family in
disguise: it needs a chain of residual toggles with **step `≤ u_n`**, but individual pieces are
`≫ u_n`, and the covering-radius family was refuted precisely because per-level increments
saturate at `3–5·u_n` and never reach `u_n`. The outliner itself recommends HOLD. I concur: do NOT
spend a build slot re-deriving a covering-radius refutation on the more-tightly-constrained wall.
breakpoint-vertex remains the live UPPER vehicle (Elo 1808, leader; boundary layer closed exactly
via certified WTC; deep interior isolated, carries genuine margin `Φ/u_n≈0.3–0.6`). The
decimated-lever refutation is recorded so no future round re-tries a constructive selection family.

## Field / diversity note
The two walls remain genuinely far apart in mechanism (upper: reachable-value existence
discrepancy; lower: dyadic block-parity count), so no single-gap-trap. The LOWER wall finally has a
live, positively-gated vehicle again (first since R14). If the [G1] non-integer reduction fails,
the lower wall is back to needing a genuinely new global reformulation and the run should escalate.

## Ranking (updated this round)
- breakpoint-vertex 1808 (leader, UPPER, advanced/live — HELD from build)
- parity-measure-potential 1634 (LOWER, stale family, partial)
- odd-block-counting **1549** (NEW LOWER, positive integer-vertex gate — BUILD)
- merge-interleave-pattern 1549 (dead-end)
- gen-func-transform 1497 (dead-end)
- ballot-matching 1414 (dead-end)
odd-block-counting anchored above the three dead lower levers and drawn with the stale
parity-measure family; below the advanced upper leader.

build set: odd-block-counting
