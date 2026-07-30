# Lemma: Parity of the discrepancy for an integer multiset with odd total

**Statement (Parity Lemma).** Let `F` be a finite multiset of *positive integers* whose
grand total `ΣF` is *odd*. Sort `F` nonincreasingly as `w_1 ≥ w_2 ≥ … ≥ w_m` and set
`D̃(F) := Σ_{i=1}^m (−1)^{i−1} w_i` (the descending alternating sum; by the certified
Lemma G / level-measure identity this equals `λ(O_F) = O(F) − E(F)`, the game discrepancy).
Then `D̃(F)` is an **odd** integer, and since `D̃(F) ≥ 0`, we have `D̃(F) ≥ 1`.

**Proof.**
1. *Integrality.* All `w_i ∈ ℤ`, so `O(F) := Σ_{i odd} w_i` and `E(F) := Σ_{i even} w_i`
   are integers and `D̃(F) = O(F) − E(F) ∈ ℤ`.
2. *Parity.* `D̃ = O − E = (O + E) − 2E = ΣF − 2E ≡ ΣF (mod 2)`. Since `ΣF` is odd by
   hypothesis, `D̃` is odd.
3. *Nonnegativity.* Pair consecutive descending terms:
   `D̃ = (w_1−w_2) + (w_3−w_4) + …`. Every full pair `w_{2k−1}−w_{2k} ≥ 0` (nonincreasing
   order); if `m` is odd the final unpaired term is `+w_m > 0`. Hence `D̃ ≥ 0`.
4. An odd integer that is `≥ 0` is `≥ 1`. ∎

**Hypotheses (both necessary).** (i) integer parts; (ii) *odd total* (NOT odd part-count).
For the P3 feasible family the total is always `ΣF = Σ_{j=0}^n 2^{n−j} = 2^{n+1}−1` (odd,
forced by the dyadic weights, Structure Lemma), so hypothesis (ii) holds automatically; only
integrality of the parts is an extra assumption. This is the genuine non-local injection of
the constant `1` (the parity of the odd dyadic grand total) that the R8 meta shows no
measure/merged-order/sequential/genfn framing can supply — those all see only `D̃ ≥ 0`.

**Scope / what it does NOT give.** It gives `D̃(F) ≥ 1` only for *integer* configurations.
The feasible optimum of P3 can live on a fractional (continuum) face, so this lemma alone does
NOT close GAP L; it closes GAP L exactly on the integer sublattice and is the finishing device
for any approach that reduces the optimum to an integer configuration (open: the
Integer-Minimizer Reduction, GAP-IMR).

**Verification.** Exact `Fraction`: `0` even values and `0` negative values over `2·10⁵`
random positive-integer multisets of odd total; integer feasible minimum `= 1` (always odd)
by exhaustive enumeration of dyadic-feasible integer configs for `n ≤ 5`.

Certified round 9 (proof-reviewer). Source approach: `vertex-integrality-parity`.
