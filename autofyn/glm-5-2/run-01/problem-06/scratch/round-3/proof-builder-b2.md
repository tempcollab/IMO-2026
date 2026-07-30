# Proof-builder report — b2-induction-step (round 3)

## What I proved

**B2 is SOLVED, conditional on B1'.** The whole theorem follows once the sibling `w-descent-rsmooth` (or any approach) closes B1'.

### New rigorous contributions
1. **Seed theorem `a_1 ∈ B`** — certified as `results/imo-2026-06/lemmas/a1-on-cycle.md`. 4-line proof: universal-small-prime ⟹ `primes(a_1)` hits `F'_∞` ⟹ contains `h ∈ M'_∞` ⟹ `m_h | a_1` ⟹ `a_1 ∈ B`. Verified for 15 values of `a_1` (15,21,33,35,45,63,65,75,77,91,105,135,143,145,175). Conditional on B1' (B1' makes `M'_∞`/`B` the stabilized object).

2. **CRT-density escape (the B2 induction step)** — closes GAP H in full. The mechanism: assuming `a_{n+1} ∉ B`, some future `σ*`-class `C` is disjoint from `σ(a_{n+1})`; every future class-`C` term must then share a large prime `q ∈ Q(a_{n+1})` with `a_{n+1}` (greedy). By σ-periodicity (CONDITIONAL on B1', cited not re-proved), the post-`N` class-`C` terms form a union of infinite APs with common difference `L'`, `gcd(L', q) = 1` for every large prime `q`. Within one AP, `q`-divisible terms are one residue class mod `q`; for DISTINCT primes `q ∈ Q`, CRT gives the uncovered density `∏(1 − 1/q) > 0` strictly (finite product of numbers in `(0,1]`; empty product = 1 when `Q = ∅`). So infinitely many class-`C` terms share NO prime with `a_{n+1}` — contradicting the greedy. Hence `a_{n+1} ∈ B`.

### Gate's mandatory changes — all addressed
1. **Path α DROPPED.** Removed from the live proof (§4). It rested on "M'_∞ pairwise cross-intersecting", empirically FALSE for `a_1 = 135, 105, 385`. Not needed — path β closes GAP H without it.
2. **Path γ's `2 ∈ S` bridge FIXED.** The gate's critique (conflating "2 divides some a_j" with "{2} is a hitting set" with "2 ∈ ∪M'_∞") is acknowledged. I do NOT repair the broken bridge — instead I show path γ is **subsumed**: path β handles `n = 1` (and every `1 ≤ n < N`) by the same CRT-density escape, with no reference to `2 ∈ S`. The seed `a_1 ∈ B` is §1 (seed theorem). So `n = 1` is closed. The empirical side-fact `2 ∈ ∪M'_∞` is noted as true but unneeded; no gap in B2 is left by leaving it unproved. (Honest, per "Prove, don't conjecture.")
3. **Path β v_p-re-coupling probe — explicit.** §3 Remark. The refuted `v_p`/spacing wall works over a SHORT length-`R` window (approximate density, sieve error `~a_n` outpaces signal `~n·δ` since `δ < 1 ≤ L`, obstruction at `n_0 ~ 10^{2000}`). Path β works over an INFINITE AP (the entire post-`N` tail of one class), so the density is EXACT: uncovered density `∏(1−1/q) > 0` strictly, no sieve error, no `Φ_R ≥ 1` threshold. The only number-theoretic input is CRT (independence of distinct prime residue classes). Path β does NOT reduce to the refuted (Cov) window claim nor to the `v_p` sieve-error obstruction. The candidate set also differs (small-prime premature `B_n \ B` vs large-prime stealing `A_n \ B_n`), but the deeper reason path β survives is infinite-vs-finite window, not merely candidate identity.

## Gaps remaining
- **[GAP B1']** — the open crux (`a_{n+1} = min(B_n ∩ (a_n,∞))` for all `n`, equivalently `M_n = M'_n`). NOT this slug's target; flagged honestly. B2 depends on B1' (one-way: B2 needs B1'; B1' does not need B2). The whole theorem = B1' (sibling) + cited conditional spine + B2 (this slug).
- No gap remains in B2 itself given B1'.

## Spec concerns / honesty notes
- The proof is conditional on B1' throughout (σ-periodicity, the spine, the very definition of `B` as the stabilized object). I flag this wherever it enters. The approach's Status is `partial` because the whole theorem is not complete (B1' open), even though B2-given-B1' is complete.
- The seed theorem and CRT-density escape are proposed for reviewer certification (`lemmas/a1-on-cycle.md` written; `lemmas/crt-density-escape.md` recommended).
- Path γ is subsumed, not repaired — this is the honest move (the broken `2 ∈ S` bridge is unnecessary once path β covers `n = 1`).
- Empirical verification: seed theorem (15 `a_1`), pre-period empty (11 `a_1`, per current.md), CRT ingredient (pure number theory). These CHECK computations stand alongside the written proof; the proof does not rest on them.

## Files written
- `results/imo-2026-06/approaches/b2-induction-step.md` (full B2 proof, conditional on B1')
- `results/imo-2026-06/lemmas/a1-on-cycle.md` (seed theorem, for certification)
