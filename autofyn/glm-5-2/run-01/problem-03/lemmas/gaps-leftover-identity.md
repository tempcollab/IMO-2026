# Lemma: gaps-leftover-identity (G1) — CERTIFIED (round 3)

**Statement.** Let `p_1 ≥ p_2 ≥ … ≥ p_m` be any nonincreasing list of nonnegative reals
(any `m ≥ 1`, any values — not restricted to tower refinements). Let
`D = p_1 − p_2 + p_3 − p_4 + …` be the alternating sum (sign `+` on odd indices). Then

$$D \;=\; \sum_{k=1}^{\lfloor m/2\rfloor}\bigl(p_{2k-1}-p_{2k}\bigr) \;+\; \mathbf{1}_{m\ \text{odd}}\cdot p_m.$$

Each summand `p_{2k−1}−p_{2k} ≥ 0` (sorted), and the "leftover" `p_m` (when `m` is odd) is `≥ 0`,
so `D ≥ 0` always.

**Proof.** This is a pure telescoping of the alternating sum, partitioned into consecutive
disjoint pairs.

- *`m` odd, `m = 2ℓ+1`.* Group the terms as
  `(p_1−p_2) + (p_3−p_4) + … + (p_{2ℓ−1}−p_{2ℓ}) + p_{2ℓ+1}`. Every index `1,…,2ℓ+1`
  appears exactly once with the correct sign: indices `2k−1` carry `+`, indices `2k`
  carry `−`, and the final odd index `2ℓ+1` is the lone unpaired `+` term. ∎

- *`m` even, `m = 2ℓ`.* Group as `(p_1−p_2) + … + (p_{2ℓ−1}−p_{2ℓ})`; every index is
  paired, no leftover. *Equivalent odd-form (padding):* append a phantom piece
  `p_{2ℓ+1} := 0`; the alternating sum is unchanged (adding a trailing `0` contributes
  `0`), and the odd-form identity gives `D = Σ_{k=1}^{ℓ}(p_{2k−1}−p_{2k}) + 0`, matching
  the even form. Thus the single odd-form formula with leftover `p_m` (taken to be `0`
  when `m` is even via padding) covers both parities. ∎

**Verified.** 0 mismatches over 20 000 random configs (mixed integer and rational values,
both parities of `m`).

**Importable by:** any approach that wants the gaps+leftover decomposition of the
alternating sum. Distinct from `D-equals-parity-integral` (`D = ∫(N mod 2)dt`) and
`block-contribution-formula` (`D = Σ_k 2^k(−1)^{C_k}(n_k mod 2)`) — same `D`, different
proof object (invites a charging/matching argument against the tower skeleton).

**Depends on:** none (pure algebra).
