# Lemma: value-bound / unkillable value window (necessary condition for a shortcut)

## Status
CERTIFIED (round 2, proof-reviewer). Proved in `approaches/small-prime-window-lemma.md` §5/Lemma 4 + Cor 5. Necessary condition only (honestly labeled).

## Statement
Let `R := rad(a_1)`, `B_n := ∪_{h ∈ M'_n}{multiples of m_h}` (small-prime admissible set), `b_n := min(B_n ∩ (a_n,∞))`, and suppose `m ∈ (a_n, b_n) ∩ (A_n \ B_n)` is a hypothetical shortcut missing small-support class `σ* ∈ F'_n` (i.e. `σ(m) ∩ σ* = ∅`). Then:
- (Value bound) For each `σ*`-term `a_j` (`j ≤ n`) and the large prime `q_j > R` with `q_j | m, q_j | a_j`, we have `a_j ≤ a_n + R - q_j`.
- (Unkillable window) Let `q_min(m) := min{q | m : q > R}`. Every `σ*`-term `a_j` with `a_n + R - q_min(m) < a_j ≤ a_n` is NOT divisible by any large prime of `m`, hence escapes `m` entirely (no small-prime hit because `σ(m) ∩ σ* = ∅`; no large-prime hit by the bound). So a shortcut requires that NO `σ*`-term lies in `(a_n + R - q_min(m), a_n]` AND every earlier `σ*`-term is divisible by an appropriate large prime of `m`.

## Proof
Since `q_j | m` and `q_j | a_j`, `m ≡ a_j ≡ 0 (mod q_j)`, so `m - a_j` is a positive multiple of `q_j` (positive because `m > a_n ≥ a_j`). Hence `m - a_j ≥ q_j`, giving `a_j ≤ m - q_j`. By `m ∈ (a_n, b_n)` and `b_n ≤ a_n + R`, `m ≤ a_n + R - 1 < a_n + R`, so `a_j ≤ a_n + R - q_j` (integers). For the corollary, every large prime `q` of `m` satisfies `q ≥ q_min`, so a `σ*`-term with `a_j > a_n + R - q_min` has `a_j > a_n + R - q`, contradicting the value bound; hence no large prime of `m` divides it. ∎

## Scope / reusability
The rigorous content the spacing mechanism extracts on B1' (necessary condition only). Localizes the obstruction to RECENT `σ*`-terms (within `q_min(m) - R ≤ R` in value of `a_n`); outside that band, deeper number-theoretic coincidences (`q_j | a_j` with `q_j | m`) are required. The clean value-window sufficiency version is EMPIRICALLY REFUTED (the `σ*`-terms are too sparse in the short value window).
