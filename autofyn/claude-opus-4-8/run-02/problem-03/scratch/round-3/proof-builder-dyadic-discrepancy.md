# Build report — dyadic-discrepancy (GAP U), Round 3

**Problem:** imo-2026-03 (IMO 2026 P3). **Slug:** dyadic-discrepancy. **Status: partial.**
Answer unchanged and reaffirmed: `c(n) = 2^n/(2^{n+1}-1) = (1+u_n)/2`, `u_n = 1/(2^{n+1}-1)`.
File updated: `results/imo-2026-03/approaches/dyadic-discrepancy.md` (§4.5 rewritten; top matter,
summary, promotable lemmas updated).

## What I closed / advanced this round

1. **Invisible-Pair Lemma (IP), fully proven.** For any multiset `R` and `v>0`,
   `D(R ∪ {v,v}) = D(R)` — adjoining two equal pieces adds `2·1[t<v]` (even) to `N(t)` at every
   threshold, so the odd-set is unchanged. This unifies and strengthens the round-2 Cor. F2
   (bisection-invisibility is the special case `v = ℓ/2`).

2. **Two exact removal ops + Residual-Total reduction, fully proven.** From IP:
   - **Bisect** `ℓ_i` (1 cut): deletes `ℓ_i` from the discrepancy; total drops by `ℓ_i`.
   - **Generalized pin** `ℓ_j` into `ℓ_i` (any `ℓ_i>ℓ_j`, 1 cut): cut `ℓ_i → {ℓ_j, ℓ_i-ℓ_j}`, the
     equal pair `{ℓ_j,ℓ_j}` is invisible, effective multiset loses `ℓ_i,ℓ_j` and gains `ℓ_i-ℓ_j`;
     total drops by `2ℓ_j`.
   - Free deletion of any existing equal pair (0 cuts).
   Each op preserves "final D = discrepancy of the current effective multiset." Since
   `D ≤ b_1 ≤ total`, this gives the **Residual-Total Theorem (RT):** forcing effective total
   `≤ u_n` forces `D ≤ u_n`. GAP U is thereby reduced to a clean combinatorial claim RT(k).

3. **RT induction, Cases (i) and (ii) closed for ALL n (conditional on RT(k-1)).** With
   `c(k) = 1 - u_k/u_{k-1} = 2^k/(2^{k+1}-1)` (identity verified symbolically):
   - trivial: `m ≤ k` pieces ⇒ bisect all ⇒ total 0;
   - **(i) dominant** `ℓ_1 ≥ c(k)Σ`: bisect `ℓ_1`, apply RT(k-1) ⇒ total `≤ u_k Σ`;
   - **(ii) balanced-top** `ℓ_1 < c(k)Σ ≤ 2ℓ_2`: pin `ℓ_2` into `ℓ_1` (or free-delete if `ℓ_1=ℓ_2`),
     apply RT(k-1) ⇒ total `≤ u_k Σ`.
   This **subsumes** the round-2 Prop. D (which was case (i) only) and now handles the balanced-top
   regime uniformly for every n. GAP U is reduced to a **single** remaining case.

## What remains open (precise unproven claim)

**GAP U — Case (iii), the balanced regime.** Assume RT(k-1). Prove RT(k) for `m = k+1` pieces with
`max(ℓ_1, 2ℓ_2) < c(k)Σ` (all pieces small; no removal op deletes a `c(k)`-fraction): Xiang with
`≤ k` ops reaches effective total `≤ u_k Σ`, hence `D ≤ u_k`.

This is the ONE gap between here and a full general-n upper bound. Proven at n=1,2 (n=2 = Cases a,b
of §4.4). Numerically true and tight for all tested n≤5 (dyadic partition, which lies on the
Case-(i) boundary `ℓ_1 = c(n)Σ`, is the unique maximizer; Case (iii) is strictly sub-extremal).

## Spec concerns (issues with the planned mechanism itself)

- **The outline's planned mechanism (U.a gap-greedy optimality + U.b pigeonhole) does NOT close
  Case (iii) as stated, and I proved a rigorous OBSTRUCTION.** Any greedy "remove-max-total"
  (equivalently any black-box single-move + RT(k-1)) strategy has a guarantee that telescopes to
  `r_k ≤ 2/((k+1)(k+2))`, which **exceeds** `u_k = 1/(2^{k+1}-1)` for `k ≥ 3` (k=3: 1/10 > 1/15).
  Moreover the deterministic max-greedy strategy *numerically violates* `u_k` from k=3 (worst
  residual 0.074 > 1/15). So U.a's "gap-greedy is at least as good as any allocation" is **false**
  as a route to the bound: greedy is strictly worse than optimal in the balanced regime. The
  optimal (min over all B/P/free-pair sequences) does achieve `≤ u_n` — verified numerically — but
  the winning strategy is genuinely non-greedy.
- **Consequence for next round:** Case (iii) needs a *strengthened* potential / IH that credits the
  post-move balance, i.e. a bound `residual ≤ ψ(k, β)Σ` with `β = ℓ_1/Σ`, `ψ(k, c(k)) = u_k`, and
  `ψ` solving the balanced recursion (bisecting the small top piece leaves an even-more-balanced
  multiset). Black-box RT(k-1) alone is provably insufficient. This is a real research step, not
  bookkeeping — I did not paper over it.
- The RT framing (residual TOTAL) is possibly slightly lossy vs targeting `D` directly, but the
  restricted-move min-D search also hits `u_n`, so RT is not the obstruction; the obstruction is
  the balanced recursion.

## Diversity note for orchestrator
GAP U's balanced case is the shared wall. A genuinely different framing (per the round-2 diversity
flag) — e.g. an amortized-halving monovariant `W = 2^{-#cuts remaining}` tied to the balanced
recursion, or a direct order-aware potential on the sorted sequence — is what the balanced case
needs; the constructive strategy route bottoms out exactly here.
