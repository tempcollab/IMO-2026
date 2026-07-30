# Build report — breakpoint-vertex (round 7)

Status: **partial** (upper valley reduced exactly to one discrepancy inequality; two new lemmas
proven in full; residual Prop UV open). File: `results/imo-2026-03/approaches/breakpoint-vertex.md`.

## What I closed / added (all rigorous, self-contained on certified DM/P/U0)

1. **Reduction R-UV (exact).** For the upper bound only *sufficiency* is needed, so I model Xiang by
   the certified DELETE/MATCH game (Lemma DM). Each move drops the tracked piece-count by 1, so from
   the $m=n+1$ valley pieces, $n$ moves reach a **single leftover** $\rho$ with $D=\rho$. Hence the
   upper bound in the valley $\iff \min\mathcal R(A)\le u_nL$, where $\mathcal R(A)$ is the
   achievable-leftover set. Profile-independent, no VERT needed (VERT = optimality, only relevant to
   the lower bound / finite-search certification).

2. **Lemma RL (realizability) — PROVEN + proposed for certification.** $\mathcal R(A)$ = tree-realizable
   signed **subset** sums $|\sum_{i\in T}\varepsilon_i a_i|$, and is a **strict** subset of all
   $\{0,\pm1\}$ signed sums (MATCH only ever differences, never sums two positive pieces). Proof by
   tracking each piece's $\{0,\pm1\}$ coefficient vector.

3. **Corrected a round-6 error.** The prior "one core leftover over all $n+1$ pieces" (no-DELETE)
   framing is **wrong in the valley**: full-support differencing trees overshoot $u_nL$ on 214/516
   random valley profiles (worst $7.5\times$), whereas allowing DELETE (subset-selection) gives
   $\min\mathcal R\le u_nL$ on all 387 tested (worst $0.56\times$). Budget $\le n$ enforced in all
   checks. So DELETE is essential — the GAP is over the full $\mathcal R(A)$, not full-support trees.

4. **Lemma VS (valley-sharpness) — PROVEN + proposed.** Rigorous, profile-independent proof that in
   the valley NO single move admits an IH$(n-1)$ certificate: single DELETE needs $a_i\ge c(n)L>L/2$
   (fails, $a_1<L/2$); single MATCH needs smaller part $y\ge\beta_nL$ (fails, $y\le a_2<\beta_nL$).
   The two thresholds $c(n)L,\beta_nL$ meet the valley's defining inequalities exactly. Conclusion:
   $\ge2$ coordinated cuts are forced — a rigorous version of "the valley is genuinely adaptive,"
   subsuming every numerically-refuted deterministic single-rule.

## What remains (honest gap)

- **Prop UV (OPEN):** $\min\mathcal R(A)\le u_nL$ in the balanced valley — the *restricted*
  signed-subset-sum discrepancy bound (minimize $|\sum_{i\in T}\varepsilon_i a_i|$ over subsets and
  *tree-realizable* signs). Verified true (exact on dyadic extremal; $\le u_nL$ on all 387 valley
  profiles, budget enforced), but no profile-independent proof. Note Lemma RL shows a direct
  $2^{n+1}$-subset pigeonhole is invalid (not all $\{0,\pm1\}$ patterns reachable — the explorer's
  factor-2 achievability deficit). This is the shared upper wall (with subset-sum-pigeonhole,
  smoothing-majorization).

## Lemmas proposed for certification
- **Lemma RL (leftover realizability)** — §4B.1, depends only on certified P/DM.
- **Lemma VS (valley-sharpness)** — §4B.2, depends only on the closed forms $u_n,c(n),\beta_n$.

## Spec concerns
None on correctness. Minor: the dispatch asked to "close" GAP U-VALLEY; the honest outcome is a
tight *reduction* + two supporting lemmas + a rigorous adaptivity proof, not a full closure — Prop UV
(the restricted discrepancy bound) is genuinely IMO-crux-hard and remains open. The round-6
"even-pairing over all pieces" plan is refuted here (needs DELETE); future work should attack Prop UV
as a subset-selection discrepancy problem, not a full-support pairing.
