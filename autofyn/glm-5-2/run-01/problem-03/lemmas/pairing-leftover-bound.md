# Lemma: pairing-leftover-bound (G2) — CERTIFIED (round 3)

**Statement.** Let `p_1 ≥ p_2 ≥ … ≥ p_m` be a nonincreasing list of nonnegative reals
(any `m ≥ 1`, any values) with total `T = Σ_i p_i`. Let `D = p_1 − p_2 + p_3 − …` be the
alternating sum. Then

- if `m` is odd, `D ≥ p_m` (equivalently Liu's odd-index take `≥ (T + p_m)/2`);
- if `m` is even, `D ≥ 0` (equivalently Liu's odd-index take `≥ T/2`).

**Proof.** By `gaps-leftover-identity` (G1), `D = Σ_{k=1}^{⌊m/2⌋}(p_{2k−1}−p_{2k}) + [m odd]·p_m`.
Since the list is sorted, `p_{2k−1} ≥ p_{2k}` for every `k`, hence every gap
`g_k := p_{2k−1}−p_{2k} ≥ 0`.

- *`m` odd:* `D = Σ g_k + p_m ≥ p_m` (each `g_k ≥ 0`). Equivalently
  `Liu = (T+D)/2 ≥ (T + p_m)/2`. ∎
- *`m` even:* `D = Σ g_k ≥ 0`. Equivalently `Liu ≥ T/2`. ∎

**Corollary (tower sub-region closure).** For a refinement of the tower `T_n` (tower
units, total `D_n`), if `m` is odd and `p_m ≥ 1` (the smallest piece is at least the
smallest tower piece), then `D ≥ 1` by this lemma. This closes the `p_m ≥ 1` sub-region
of the lower bound for the tower. (When `p_m < 1`, the deficit `1 − p_m` must be covered
by the gaps — the open G1 crux in the `gaps-leftover` framing.)

**Verified.** 0 violations over 20 000 random configs (both parities).

**Importable by:** any approach needing the basic pairing/lowerbound on the alternating
sum. The `p_m ≥ 1` corollary closes a clean sub-region of the tower lower bound.

**Depends on:** `gaps-leftover-identity` (G1).
