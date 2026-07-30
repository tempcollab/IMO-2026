# Build report — breakpoint-vertex (UPPER wall, Subset-KK), Round 9

Status: **partial** (advance). The upper-valley residual is sharpened and reformulated; one new
lemma fully proven and proposed for certification; the outline's step-3 recursion is rigorously
refuted.

## What I proved this round (self-contained on certified P/DM/ESF-1/ESF-2)

1. **Lemma BL (band-landing / first crossing) — PROVEN (step 2 CLOSED, straddle settled).**
   The descending survivor partial sums `P_0 < P_1 < … < P_n = L−a_1 > a_1` cross `a_1` at a
   **unique** index `k` (finite strictly increasing sequence ⇒ no straddle/boundary case — the
   reviewer's flagged straddle is vacuous). The subset `T = {a_1,…,a_k}` gives
   `r = a_1 − Σ_T = |a_1 − Σ_T| ∈ [0, s_k) ⊆ [0, a_2) ⊆ [0, β_nL)`, realized by ESF-1 in exactly `n`
   moves. The strict valley `a_1 < L/2` is precisely what forces the crossing to exist with `k ≤ n`.
   Written to `results/imo-2026-03/lemmas/band-landing.md`, proposed for certification.

2. **Reachability reformulation of the Subset-KK claim (Covering claim).** Via ESF-2, define the
   descending include/skip reachable set `R_0={0}`, `R_i = R_{i−1} ∪ {|v−a_i| : v∈R_{i−1}}`. Then
   Subset-KK ⟺ `R_{n+1}` meets `[0, u_nL]` via a nonempty include-set (value 0 admissible via even
   cancellation, which covers the near-all-equal valley profiles whose minimal *positive* caterpillar
   can exceed `u_nL`). This is the cleanest equivalent form of the residual.

3. **Rigorous refutation of the outline's step-3 recursion (make-or-break negative result).** The
   greedy band-landing recursion, the flip-if-it-helps greedy, and the drop-one family ALL provably
   overshoot `u_nL` (machine-verified worst ratios: greedy band-landing 0.96→7.70, flip-if-helps
   0.98→11.38, drop-one 0.47→8.88 for `n=2..7`), while the true min over all subsets is always
   `≤ u_nL` (worst 0.84). The `n=2` witness `{9/20,7/25,27/100}` is an explicit rational
   counterexample to both greedies (they bottom at `17/100 > u_2 = 1/7`). Numerics are diagnostic
   only (rule out recipes); no numeric statement enters a proof step. **Consequence:** the good
   subset genuinely requires foresight; the residual is a GLOBAL covering problem, NOT a recursion.
   This prunes the entire deterministic-recursion class, including the valley-differencing reserve's
   greedy hope.

## Honest gap (unchanged make-or-break, now precisely characterized)

**GAP U-cover.** Prove the Covering claim: `R_{n+1}` meets `[0, u_nL]`. Needs a profile-independent
covering/dispersion invariant on the `R_i` that shrinks the covering radius near 0 to `≤ u_nL`, using
`Σa_i = 1`, `a_1 < L/2`, `a_2 < β_nL` jointly. Lemma BL gives the first landing `r ∈ [0, β_nL)`; the
residual is to cover the remaining factor `2^{n−1}` down to `u_nL` GLOBALLY (a per-step "gain one
dyadic band" statement is now proven FALSE). Mirrors the LOWER wall's aggregate reserve ρ_k.

## Constraints honored

- β_n = 2^{n−1}u_n exactly; the first-crossing bound `r < s_k ≤ a_2 < β_nL` is strict (constraint 1).
  Straddle case settled: there is none (unique crossing on a finite increasing sequence).
- IH target kept as a RATIO (`u_nL`) throughout; no degradation to O(a_1). aimo-0796's `< a_2` bound
  is explicitly identified as the BL first-landing (factor `2^{n−1}` short), not the mechanism
  (constraint 2).
- n=2 witness verified with exact arithmetic (constraint 3): BL crosses at k=2, r=17/100>u_2;
  abs-flip subset {a_2,a_3} → 1/100 ≤ u_2.
- Two-sided abs-flip kept (ESF-2); no raw 2^{n+1} pigeonhole (Lemma RL); no single DELETE/MATCH+IH
  (Lemma VS). All named, cited to lemma files.

## Files written

- `results/imo-2026-03/approaches/breakpoint-vertex.md` — Status/Approaches/Current best updated;
  new §4B.5 (Lemma BL, reachability reformulation, refutation, GAP U-cover); §5 assembly + Promotable
  lemmas updated.
- `results/imo-2026-03/lemmas/band-landing.md` — Lemma BL, proposed for certification.

## Spec concerns:
The outline's chosen route (VERT + band-landing pigeonhole with a two-step COMPOUND recursion of the
residual) does NOT close as a recursion — numerically refuted this round (greedy band-landing
overshoots up to 7.7×; every single-pass policy overshoots up to 11.4×). The correct residual
(GAP U-cover) is a GLOBAL covering/dispersion statement on the reachable set, which BOTH the outliner
and the reviewer framed as a step-3 recursion. Next round's outliner should re-plan step 3 as a
covering-radius invariant (aggregate, foresight-based), not a recursion, and note the shared
structural dependency with the LOWER wall's reserve ρ_k. Lemma BL (step 2) is done and certifiable.
