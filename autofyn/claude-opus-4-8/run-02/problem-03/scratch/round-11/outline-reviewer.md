# Outline review — imo-2026-03 (Round 11)

Sole open wall: **GAP L** (lower bound, Case B) = the scalar inequality `I_n := ∫_{(0,θ)}⌊M/2⌋ ≤ 0`
(FLOOR reduction, certified). Upper bound is DONE/certified — no approach touches it (confirmed:
both approaches explicitly leave UB alone). Plateau on GAP L is R3–R10 (8 rounds); diversity was
scrutinized hard.

## Verdicts

### peel-scale-rank-induction — APPROVE (advance), LEADER, primary build
Sound. Route is a recursive top-scale peel through the certified FLOOR reduction to a **fixed
extremal base object** (uncut ladder `L={2^{n−1},…,1}`) — a cut-tree-origin route, not caught by
the R8 measure/merged-order/sequential/genfn "equivalent-to-target" meta, not the R10 dead
integer-minimizer engine. The reduction machinery (SD/PEEL/DIFF/Invariant I/FLOOR) is all certified;
the round-11 sharpening is the isolation of a clean, self-contained base case.
- **Base case `b=0`** (`D̃(π_0⊎L)≥1` for every partition `π_0` of `2^n` into `≤n+1` parts): I
  brute-checked it — min exactly `1`, tie-attained, `n≤6`, for BOTH integer and fractional `π_0`
  (0 violations). Proven-true target with an explicit mechanism (ladder dominance
  `2^{n−j} > Σ_{i>j}2^{n−i}`). This is the concrete deliverable — prioritize it; propose as a
  promotable lemma once proven.
- **Reduction-to-base (step 3, slice-max monotone in `b`)** is the real remaining gap. NOTE the
  distinction the outliner correctly flags: the POINTWISE fixed-`π_0` per-cut monovariant is FALSE
  (~30% violations, banked dead end R11) — the builder must prove the extremal-over-slice (π_0
  co-varies) statement, which is a genuinely different and harder fact. Do not conflate them, and do
  not wave the near-balance shell through with (DIFF) — enumerate it (where dominance is load-bearing).
- Watch-outs to enforce: no merging even tie-blocks toward `L` (can RAISE D̃, `{4,2,½,½}:2→3`,
  banked R10) — the reduction must add cuts, never merge; no scalar/aggregate summary of `F'`.

### allocation-vertex-corner — APPROVE with CHANGES REQUESTED (new, secondary build)
Registered (Elo 1500 cold-start → 1502 after ranking). Its STRUCTURE is genuinely different from
the leader: non-recursive, no induction on `n`, no fixed comparison object — a finite classification
of the discrete allocation `a`-vector via Lemma V vertices. It operates on the ALLOCATION, not a
static final-multiset profile, so it is NOT the R8-dead measure family; and it uses Lemma V to bound
a corner, NOT to claim an integer minimizer, so it is NOT the R10-dead GAP-IMR engine. This is a
legitimate whole attempt end-to-end (base + reduction), not a fragment.

Required changes (the engine walks up to two banned lines — the builder must not cross them):
1. **`φ(b)` must not be a bare scalar-summary of the allocation** (the refuted `sum(Y)−sum(Z)`-style
   fill, run_state Rules). Per the outliner's own watch-out (i), `φ(b)` is permissible ONLY if the
   surviving corner is then verified case-by-case against the TRUE recursive shape (Lemma V vertices),
   NOT asserted from the allocation count alone.
2. **The `φ(b)` mechanism ("odd-threshold negative side grows more than even-threshold positive side
   per cut") is at risk from the cross-`k` witness** `a=(1,2,0,0,0)` (loaded-IH explorer Route C:
   `pos[1]` is balanced by `neg[1]+neg[2]` jointly). The derivation must survive cross-`k`
   cancellation — do NOT assume a single-`k` termwise pairing (refuted).
3. **Do not slide into the GAP-IMR integer-minimizer claim** (dead R10). Lemma V bounds a corner only.
4. **Import the base case `b=0` from the leader** once certified — do not re-prove it (shared
   deliverable).

## Diversity / single-gap-trap assessment (the load-bearing judgement)
The two approaches share the certified FLOOR reduction (a proven tool, not a gap) and share BOTH
open gaps: (i) the base case `b=0` ladder inequality, and (ii) a monotonicity-in-`b` claim (leader's
"slice-max monotone", allocation's "`φ(b)`"). They differ in the MECHANISM for closing gap (ii) —
recursive loaded IH vs finite LAYER-form `φ(b)` over the allocation. So this is a "two mechanisms on
one target" configuration, not one proof split across slugs (each is a whole end-to-end attempt).

- **Not a fatal single-gap trap:** both shared gaps are numerically TRUE (base case verified above,
  min exactly 1; `I_n≤0` verified 0 violations n≤6), so neither will be refuted out from under both —
  the risk is stall, not collapse to a false claim.
- **But the field HAS collapsed to one wall** (`I_n≤0` via base case `b=0` + monotone-in-`b`),
  attacked two ways, with NO third live approach escaping this target (telescope is parked and gives
  only `D̃≥0`; all integer-minimizer/measure/sequential slugs are dead). This is exactly the plateau
  signal.
- **Action for the orchestrator:** build both this round (the base case is a genuinely new, tractable,
  proven-true deliverable — real forward motion). **If BOTH stall on the monotone-in-`b` step next
  round**, do NOT add a third variant of the same `I_n≤0`/monotone target. Per the run_state R11
  plateau rule, seed ONE genuinely far `+1`-injection framing that does NOT route through the
  monotone-in-`b` claim — e.g. a direct structural induction on Z's cut-tree bounding how `Σa_j≤n`
  creates the `⌊M/2⌋>0` layers, or the reserved 2-adic valuation split — and keep telescope parked as
  the machinery cross-check.

## Ranking (after this round's update)
dyadic-discrepancy 1682 (parked, UB milestone) · **peel-scale-rank-induction 1646 (leader, live)** ·
induction-recursion-telescope 1580 (parked machinery) · vertex-integrality-parity 1534 (dead) ·
peel-integral-exchange 1527 (dead engine) · **allocation-vertex-corner 1502 (new, live)** ·
even-rank-doublecount 1425 · cut-sequence-potential 1414 · induction-recursion 1369.
(Note: Elo reflects proven achievement — dyadic-discrepancy leads on the certified UB but is PARKED;
the build set is the strongest LIVE slugs on the open wall, not the top Elo.)

build set: peel-scale-rank-induction, allocation-vertex-corner
