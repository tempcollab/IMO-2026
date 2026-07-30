# Lemma: seed `a_1 ∈ B` (conditional on B1')

## Status
CERTIFIED (round 3, proof-builder `b2-induction-step`), CONDITIONAL on B1' (i.e. on `M'_n = M'_∞` being well-defined as the stabilized minimal-hitting-set family of the small-prime supports `F'_∞`). Verified computationally (Python/sympy) for 15 values of `a_1` (15,21,33,35,45,63,65,75,77,91,105,135,143,145,175): `primes(a_1)` hits `F'_∞` and `a_1 ∈ B` in every case.

## Statement
Let `a_1, a_2, …` be the greedy sequence of `imo-2026-06`. Let `R := rad(a_1)`, `P_R := {primes ≤ R}`, `σ(a_i) := supp(a_i) ∩ P_R`, `F'_∞ := {distinct σ(a_i) : i ≥ 1}`, `M'_∞` the family of inclusion-minimal hitting sets of `F'_∞` over the universe `P_R`, and `B := ∪_{h ∈ M'_∞}{multiples of m_h}` where `m_h := ∏_{p ∈ h} p`. **Assuming B1' holds** (so `M'_∞`, `B`, `L` are well-defined as the stabilized objects), the seed `a_1 ∈ B`.

## Proof
By the **universal-small-prime lemma** (CERTIFIED, `lemmas/universal-small-prime.md`), every term `a_i` (`i ≥ 1`) is divisible by at least one prime of `a_1`; that prime lies in `P_R`. Hence for every `σ*-class` `C ∈ F'_∞` there is some `a_i` with `σ(a_i) = C`, and `primes(a_1) ∩ σ(a_i) ≠ ∅`, i.e. `primes(a_1) ∩ C ≠ ∅`. Thus `primes(a_1) ⊆ P_R` is a hitting set of `F'_∞`.

By well-foundedness of inclusion, `primes(a_1)` contains an inclusion-minimal hitting set `h ∈ M'_∞`. Since `h ⊆ primes(a_1) = supp(a_1)`, every prime of `h` divides `a_1`, so `m_h | a_1`. By definition `B` contains every multiple of `m_h`, hence `a_1 ∈ B`. ∎

## Notes
- The argument is the canonical "the seed lies on the cycle" mechanism; it does NOT need `2 ∈ ∪M'_∞` or any cross-intersection property of `M'_∞`. It only uses universal-small-prime + the definition of `M'_∞`.
- Conditional on B1': B1' is what guarantees `F'_∞` (and hence `M'_∞`, `B`) is the stabilized object the orbit eventually lives on. Without B1' the symbol `B` is not yet tied to the greedy's long-run behavior.

## Scope / reusability
The seed half of B2 (extending periodicity from `n ≥ N` back to `n = 1`). Imported by `b2-induction-step` and available to any B2-targeting approach.
