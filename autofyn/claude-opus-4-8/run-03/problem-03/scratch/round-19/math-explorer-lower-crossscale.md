## imo-2026-03 — LOWER wall, cross-scale value×scale-of-origin joint object

**Verdict up front: NO surviving object found. HOLD LOWER (build nothing new on this axis).**
I ran the one theoretically-motivated candidate the dispatch pointed at (SUFFIX-★, previously
only *registered* as a HELD gate-only probe `cross-scale-injection`, never actually executed —
`.ranking.json` shows `expanded:0, last_outcome:null`) myself, from scratch, in exact `Fraction`
arithmetic. **It fails decisively.** I also traced why a g-LEVEL-crossing-keyed (rather than
dyadic-scale-keyed) pairing is structurally unlikely to work, without needing a full build to see
it. Details below.

### The gate I ran: SUFFIX-★ (12th dead lower lever, newly confirmed this round)

Setup exactly as in the certified R17 tagging (`α_{i,j}` = measure of level-`i` super-level
`{g≥2i}` intervals opened by a scale-`j` B-fragment; `β_{i,j}` = measure of level-`i` sub-level
`{g≤1−2i}` intervals closed by a scale-`j` B-fragment). Claim tested (both directions, the one
proposed in `cross-scale-injection.md`):
```
for every scale threshold J:  Σ_{j≥J} Σ_i α_{i,j} ≤ Σ_{j≥J} Σ_i β_{i,j}     (SUFFIX-★)
for every scale threshold J:  Σ_{j≤J} Σ_i α_{i,j} ≤ Σ_{j≤J} Σ_i β_{i,j}     (PREFIX mirror)
```
I generated random budget-respecting `a=0` refinements (`F` = random composition of `2^n` into
`≥3` exact-`Fraction` parts each `≤2^{n−1}`; `B` = random refinement of each ladder rung `2^j`,
`j=0..n−1`, with total cut budget `cF+cB≤n`), built the exact integer-valued step function `g`,
identified maximal super/sub-level intervals and their opening/closing B-crossing scale exactly
as R17 specifies, and checked both cumulative inequalities over all thresholds `J`.

**Result (exact Fraction, 400 configs/n):**

| n | configs | configs w/ ≥1 SUFFIX-★ violation | rate |
|---|---|---|---|
| 4 | 400 | 134 | 33.5% |
| 5 | 400 | 142 | 35.5% |
| 6 | 400 | 170 | 42.5% |

Failure rate **grows with n** (33.5%→35.5%→42.5%), and the worst deviation also grows
(max Σ-gap ≈1.9/3.9/11.9 across n=4,5,6) — the same "grows with n, doesn't shrink" signature that
killed every other same-family lever (R17 same-scale, R16 band-counting). PREFIX mirror fails
even more (up to 617 violating `(J,config)` pairs at n=6 vs 504 for suffix). Sanity check: (★)
itself holds 0/900 on the identical generator (confirms the code is not the cause of the failures
— it correctly reproduces the certified-true target while showing the SUFFIX cumulative is false).

**Conclusion: SUFFIX-★ is dead by the dispatch's own kill criterion 1 (fails outright, both
directions).** This is consistent with, and sharpens, the R17 diagnosis: the credit repaying a
scale-`j` super-level deficit is not even monotone-in-scale (neither "coarser pays finer" nor
"finer pays coarser" as a cumulative works) — the true repayment pattern must be scattered
non-monotonically across scales, which no single-direction (or dual-direction) cumulative sum can
express. **This is the 12th dead lower lever** (first one actually numerically gated by an
explorer rather than left as an un-built probe).

### Why a g-LEVEL-crossing-keyed (non-scale) pairing is also unlikely to survive — structural argument, not a full gate

The dispatch asks whether keying on *g-level crossings* rather than dyadic-scale-of-origin escapes
both R17 and R11's deaths. I traced the natural such object: view `g(t)` (t increasing 0→L) as an
integer lattice walk with `-1` steps at F-crossings and `+1` steps at B-crossings (this is literally
what the interval structure already is — crossing points are exactly the piece values, so
"level-crossing analysis" and "value analysis" are the same object here, not a new one). A
level-crossing (bracket-matching / Dyck-path style) pairing of each down-step with an up-step at the
*same integer level* (regardless of scale) discards the crossing points' **real magnitudes** —
but both sides of MID-core (`μ{g odd}` and `∫g=1`) are `dt`-*weighted* integrals, and the mass
identity `∫g=1` is derived from `∫N_F=ΣF=2^n`, `∫N_B=ΣB=2^n−1` (Fubini on the actual piece
*values*, not on crossing *counts*). A purely combinatorial level-crossing-count pairing (like the
standard up-crossing/down-crossing identity `U_ℓ−D_ℓ=[s>ℓ]`) is real and true, but it is a
**counting** fact independent of the interval *lengths*, so it cannot by itself supply the
length-weighted cancellation MID-core needs — any attempt to convert it into a length bound
would have to reintroduce exactly the kind of local/scale bookkeeping already shown false (R17,
now SUFFIX-★). I did not spend a full build cycle on this because the structural reason it fails
is the same one that sank R17/R16/R15: separating length-weight from level/scale-index destroys
the very quantity (`∫g`) both sides depend on. I flag this as a *plausibility argument*, not a
completed refutation — but given 12 dead levers and a clear structural reason, it is not worth a
build slot without a genuinely new idea for re-attaching lengths to a level-only pairing.

### Distinct openings (for the record, ranked by remaining plausibility)
1. **HOLD lower entirely this round** — no local/scale-keyed/level-keyed object survives; recommend
   the outliner not dispatch a 13th variant of "tag intervals by X, cap termwise" without a
   genuinely different global mechanism (aggregate/global argument, not local pairing).
2. (Low-confidence, unexplored) A **signed-measure/optimal-transport** formulation of MID-core:
   treat `φ(g)dt` as a signed measure on `(0,L)` and ask for an explicit (not per-scale, not
   per-level) transport plan moving mass from `{g≥2}` to `{g≤1}` bounded by the *total variation of
   g* (a Wasserstein/rearrangement-type bound) rather than any interval tagging. This is genuinely
   different in kind (a global transport-cost bound, not a local cap) from all 12 dead levers, but
   I did not build or gate it this round — flagging it as untried, not recommending it be built
   without first formulating and cheap-gating the specific transport-cost inequality.
3. Not recommended: any further scale-of-origin or level-crossing local pairing (both now dead or
   structurally implausible per above).

### Cheap-kill candidates
- Already executed: SUFFIX-★/PREFIX-★ exact-Fraction gate (done this round, both FAIL).
- For opening 2 (if pursued): first cheap-gate `∫φ(g) ≥ −TV(g)·const` or similar total-variation
  bound numerically before any prose — same discipline as all prior rounds.

### Knowledge-base entries relevant
- No new KB entries beyond what's already imported (Lemma MID, CLIP, ONE-REC, BL — all already
  certified and unaffected by this round's negative result).

### Analogous past problems (cruxes)
Re-confirming (not newly discovering) the two analogues the dispatch already named, now with their
verdict sharpened:
- **aimo-0009** (`algebra`, `size-bounding-and-descent` / `telescoping-and-summation`): "pair each
  below-threshold index with the count of above-threshold indices exceeding a *shifted* level" —
  this is precisely the same-scale self-referential shifted-level pairing R17 killed. Confirmed
  genuinely analogous in mechanism, and confirmed dead for this problem.
- **aimo-0127** (`combinatorics`, `double-counting`/`graph-theory-and-connectivity`): "rewrite a
  weighted total as a sum over thresholds of tail-counts, cap each threshold termwise via a
  window/acyclicity bound" — structurally the same "per-level cap, sum over levels" recipe; also
  the template SUFFIX-★ tried to weaken into a cumulative-over-scale version, which I've now shown
  fails here (aimo-0127's window bound is monotone in its threshold in a way that does not hold for
  this problem's cross-scale credit).
- No new analogue found beyond these two; searched `double-counting`, `invariants-and-monovariants`,
  `telescoping-and-summation`, `coloring-and-parity` in `combinatorics` for "level"/"scale"/
  "crossing"/"dyadic" — nothing else resembles the specific cross-scale credit-transport structure
  here closely enough to recommend as a fresh lead.

### Prior progress
Unchanged from R18: LOWER wall reduced (certified) to GAP MID-core / (★); UPPER wall (breakpoint-
vertex) is the live leader (Elo 1847, partial) with its own open deep-interior residual (not my
lens this round). No lemma certified this round on the lower side — pure negative result.

### Dead ends (do not retry)
- SUFFIX-★ / PREFIX-★ cumulative-in-scale Abel sum over the R17 tagging: **DEAD, 12th lever**
  (33.5–42.5% failure, growing with n, both directions). Do not re-propose any monotone-in-scale
  cumulative variant of the R17 tagging.
- Reconfirm (from run_state, unchanged): same-scale layer-cake (R17, 10th), band-parity count
  (R16, 9th), merge/collapse-to-|F|=2 (R18, 11th), Z-transform (R15, 7th), LP-vertex/DUAL-CHAR
  (R14, 6th), scalar reserve (R10), structured transport/Hall matching (R11) — all still dead, all
  untouched by this round's work.

### Small-case / intuition notes
- (Conjecture, well-supported numerically across 12 levers now): the cancellation certifying
  MID-core is **irreducibly global** — no decomposition indexed by a single local coordinate
  (dyadic scale j, g-level i, or their cumulative sums in either direction) suffices. The deficit
  at any fixed local coordinate is real and can be as large as the entire local budget (~2^j, or
  ~100% of one scale's mass), and is repaid by credit whose scale/level location is essentially
  unconstrained (not even monotone). This strongly suggests the correct proof needs either (a) a
  genuinely aggregate/whole-object argument (e.g. total-variation/transport bound, or an inductive
  argument on n that never separates into per-scale pieces), or (b) abandoning the (F,B) parity-
  measure decomposition altogether in favor of a different top-level target — but no evidence this
  round supports (b) being necessary; the reduction chain (MID/CLIP/(★)) itself is not in doubt,
  only the local-decomposition attack on it.
