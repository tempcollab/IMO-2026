# proof-builder report — small-prime-window-lemma (round 2, IMO 2026 P6)

**Slug:** `small-prime-window-lemma`. **Verdict sought:** close B1' via spacing + covering.
**Outcome:** partial. The spacing mechanism gives a genuine, rigorous *necessary* condition
(localizes the obstruction to recent `σ*`-terms), but the *sufficiency* (covering) does not close,
and the clean value-window version is empirically REFUTED. The conditional spine (B1' ⟹
periodicity from `N_0`) is fully rigorous and the seed sub-gap is dissolved for free.

## What I proved (rigorous, complete)

1. **Clean reduction to the single claim B1'.** Using `M'_n` (minimal hitting sets of small
   supports `σ_i = supp(a_i) ∩ P_R`) as the object — automatically finite-valued over the
   definitional finite universe `P_R = {primes ≤ R}` — the problem's crux collapses to B1' =
   "`a_{n+1} = min(B_n ∩ (a_n,∞))` for all `n`" (window form: no `m ∈ (a_n, b_n) ∩ (A_n \ B_n)`).
   I also recorded the **equivalence** `B1' ⟺ M_n = M'_n` (no large prime in any minimal hitting
   set of the full supports), confirming B1' is the SAME wall the other routes hit, now one claim.

2. **Lemma 1** (`B_n ⊆ A_n`, hence `a_{n+1} ≤ b_n`). Definitional: a small-prime hit is a genuine
   hit.

3. **Lemma 2** (`b_n ≤ a_n + R`, the small-prime minimum lies in `W_n`). The next multiple of `R`
   after `a_n` is small-prime-admissible (divisible by all primes of `a_1`, which hit every past
   `σ_i` by universal-small-prime). So `a_{n+1}, b_n ∈ W_n`. This LOCALIZES B1' to the window.

4. **Lemma 3 (spacing fact).** A prime `q > R` divides at most one integer of `W_n` (length `R <
   q`). Rigorous; but weak — at `a_1=35, n=221`, large primes touch `15/35` window slots.

5. **Lemma 4 + Corollary 5 (value bound / unkillable value window).** A shortcut `m ∈ (a_n, b_n) ∩
   (A_n \ B_n)` missing `σ*` hits a `σ*`-term `a_j` via large `q` ONLY IF `a_j ≤ a_n + R - q` (since
   `m - a_j ≥ q > R`). Hence every `σ*`-term in `(a_n + R - q_min(m), a_n]` escapes `m`'s large
   primes entirely. This is the genuine rigorous content of the spacing mechanism: it forces a
   shortcut to find a recent `σ*`-term within `q_min(m) - R` in value, OR achieve deeper
   number-theoretic coincidences on older terms.

6. **Conditional spine (B1' ⟹ periodicity from `N_0`).** All rigorous given B1':
   - Lemma 6: `F'_n` stabilizes over finite `P_R` at some `N_0`; `M'_∞`, `B` fixed; modulus is the
     KERNEL product `L = ∏_{p ∈ ∪M'_∞} p` (verified `30` for `a_1=15`, NOT `30030`).
   - Lemma 7: seed `a_{N_0} ∈ B` is AUTOMATIC (B1' at step `N_0-1` puts `a_{N_0} ∈ B_{N_0-1}`;
     trivially hits `σ_{N_0} = σ(a_{N_0})`). **Dissolves old sub-gap B1(b) for free.**
   - Theorem 8: Theorem 1 (imported) ⟹ `a_{n+T} = a_n + L` for `n ≥ N_0`, `T = |B ∩ [0,L)|`,
     single cycle.

7. **Trivial cases** (`a_1` even ⟹ `T=1,L=2`; `a_1=p^k` ⟹ `T=1,L=p`): imported, settled.

## What did NOT close (honest gaps)

- **[GAP B1' — covering sufficiency, THE HEART].** Prove (Cov): for every shortcut `m` and missed
  class `σ*`, some `σ*`-term escapes `m`'s large-prime reach. Corollary 5 gives (Cov) for free
  whenever a `σ*`-term lies in the value window `(a_n + R - q_min(m), a_n]`; the unproved case is
  when no `σ*`-term lies there. **The clean value-window version FAILS empirically** (753–48153
  violations per `a_1`; `σ*`-terms too sparse in length-`(q_min - R)` windows). The value-gap to
  the most-recent missed term reaches 747–763, so no uniform "recent-`σ*`-term" bound works
  either. The real obstruction is number-theoretic (which large primes divide which past terms),
  not pure spacing/density. This **confirms the outline-reviewer's coupling warning**: spacing +
  covering, in every clean formulation I found, does not close B1'. Three slugs
  (`small-prime-window-lemma`, `periodic-set-iteration`, `bounded-diff-finite-state`'s `v_p` move)
  share this heart; if (Cov) is genuinely unprovable by spacing, all three die together.

- **[GAP B2 — from-n=1] (secondary).** Even with B1', periodicity is from `N_0` (≥ 3 typically),
  not `n = 1`. The single-cycle property of Theorem 1 removes the pre-period INSIDE `B`, but for
  `n < N_0` the governing set `B_n ⊋ B` admits "prematurely valid" candidates. Empirically the
  pre-period is always empty (all 13 tested `a_1`, incl. stubborn `187` T=484, `221` T=334); no
  proof. Separate from B1'.

## Empirical work done (conjecture-grade, labeled as such in the proof)

- B1' holds for 300–1500 terms on `a_1 ∈ {15,35,77,91,105,135,175,385}` (true greedy == small-prime
  greedy, zero divergence).
- Large primes appear late (first large-prime term at index 23 for `a_1=15`, 54 for `a_1=35`,
  never within 120 terms for `a_1=385`).
- Spacing alone insufficient: up to 15/35 window slots touched by large primes, yet no shortcut.
- Value-window (Cov) REFUTED (thousands of violations).
- Seed automatic + kernel product `L` verified on all 8 required `a_1`.

## Spec / coupling concerns for the reviewer

1. **The spacing+covering heart is empirically refuted in its clean form.** I did not paper over
   this — it is flagged as [GAP B1'] with the refutation data recorded. The conditional spine is
   real, rigorous value (the seed dissolves; the modulus is corrected to the kernel product), but
   B1' itself is no closer to closed than in round 1, and the mechanism (spacing) is now
   empirically shown INSUFFICIENT in its natural formulation. Recommend the reviewer NOT advance
   this slug on the spacing mechanism; route further B1' work through the genuinely-independent
   `hitting-set-monovariant` (duality) or `frozen-invariant-reduce-mod-lcm` (different proof
   shape) instead, OR challenge B1' from a new framing next round.

2. **`periodic-set-iteration` and `bounded-diff-finite-state`'s `v_p` move are coupled to this
   slug** (same covering-bound heart, per the outline-reviewer). My empirical refutation of the
   clean value-window version applies to all three. If the reviewer agrees, consider retiring the
   spacing mechanism as the B1' attack across all three and re-routing.

3. **Promotable lemmas proposed:** the spacing fact (Lemma 3), the small-prime-minimum-in-window
   (Lemma 2), and the value-bound/unkillable-window lemma (Lemma 4+Cor.5). All proved in full and
   reusable; the value-bound lemma is the genuine rigorous residue of the spacing attack even
   though (Cov) fails.

## Self-assessed status
**partial.** Rigorous: reduction to B1', Lemma 1, Lemma 2, Lemma 3, Lemma 4+Cor.5, Lemma 6, Lemma
7, Theorem 8 (conditional), trivial cases. Open: [GAP B1'] (covering sufficiency — heart, clean
version empirically refuted), [GAP B2] (from-n=1). Honest about both; no overclaim.
