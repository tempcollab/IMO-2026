# Lemma: small-prime minimum lies in the window

## Status
CERTIFIED (round 2, proof-reviewer). Proved in `approaches/small-prime-window-lemma.md` §2/Lemma 2. (Overlaps with `bounded-difference.md`'s witness but states a distinct fact about `b_n` rather than `a_{n+1}`.)

## Statement
Let `R := rad(a_1)`, `P_R := {primes ≤ R}`, `M'_n` the minimal hitting sets of `F'_n = {σ(a_i) : i ≤ n}` (where `σ(a_i) = supp(a_i) ∩ P_R`), `B_n := ∪_{h ∈ M'_n}{multiples of m_h}`, and `b_n := min(B_n ∩ (a_n, ∞))`. Then `a_n < b_n ≤ a_n + R` for every `n ≥ 1`.

## Proof
Let `M := R · ⌈(a_n + 1)/R⌉` (the least multiple of `R` strictly greater than `a_n`). Then `a_n < M ≤ a_n + R`. `R` is divisible by every prime of `a_1`, so `primes(a_1) ⊆ σ(M) ∩ P_R`. By universal-small-prime, every `a_i` (`i ≤ n`) has `σ(a_i) ∩ primes(a_1) ≠ ∅`, so `σ(M) ∩ σ(a_i) ≠ ∅` for every `i ≤ n`. Thus `σ(M)` is a hitting set of `F'_n`; it contains some `h ∈ M'_n`, so `m_h | M`, i.e. `M ∈ B_n`. Hence `b_n ≤ M ≤ a_n + R`. ∎

## Scope / reusability
Localizes the B1' question to the window `W_n = (a_n, a_n + R]` (both `a_{n+1}` and `b_n` lie in it). Combined with the bounded-difference lemma gives `a_{n+1}, b_n ∈ W_n`.
