# Lemma: v_p union-bound (PARTIAL — B1' for n ≤ n_0(a_1))

## Status
CERTIFIED (round 2, proof-reviewer) as a PARTIAL result. Proved in `approaches/bounded-diff-finite-state.md` Lemma 6. Scope: B1' holds for `n ≤ n_0(a_1)` where `n_0` is astronomically large (e.g. `~10^{2000}` for `a_1=15`). **Does NOT prove B1' for all `n`** — the refined sieve argument fails beyond `n_0` (see the approach file). **Pre-stabilization scope gap flagged**: the induction step covers `n ≥ N` (stabilization index); the finitely many steps `1 < n < N` are not uniformly covered by the induction (they are a finite-per-`a_1` check, not a general argument).

## Statement
Let `Φ_R(M) := max{ Σ 1/q_i : q_1 < … < q_k primes > R, ∏ q_i ≤ M }`, and let `M_0(R)` be the least `M` with `Φ_R(M) ≥ 1`. Then (inductively, conditional on B1' for steps `≤ n` and `n ≥ N`): if every hypothetical shortcut `m ∈ (a_n, a_n+R] ∩ (A_n \ B_n)` has `Σ_{q ∈ Q(m)} 1/q < 1` (where `Q(m) = {primes q > R : q | m}`), then B1' holds at step `n+1`. Consequently B1' holds for all `n` with `a_n + R < M_0(R)`, i.e. for `n ≤ n_0(a_1) := (M_0(R) - R)/R` (plus the bounded pre-stabilization regime).

## Proof (sketch)
By the σ-periodicity lemma, each `σ*`-class is a union of APs with common difference `L'`, `gcd(L', q) = 1` for `q > R`. Within each AP the `σ*`-terms divisible by a fixed `q ∈ Q(m)` have density `1/q`. The union bound gives `|covered σ*-terms| ≤ |J*| · Σ 1/q + O(c*·|Q|)`. Coverage requires `1 ≤ Σ 1/q + O(log n / n)`, so as `n → ∞`, `1 ≤ Σ 1/q`. Contrapositive: `Σ 1/q < 1` ⟹ no shortcut. The threshold `n_0` is where `Φ_R(a_n + R)` first reaches 1. ∎

## Scope / reusability
A genuine partial result: B1' (hence full periodicity, via the conditional spine) for all `n ≤ n_0(a_1)`. Practically weak (`n_0` astronomical; B1' empirically holds for all `n`) but correctly stated. The obstruction beyond `n_0` (sieve error `~a_n` outpaces signal `~n·δ` since `δ < 1 ≤ L`) is structural and coupled to the spacing route's wall.
