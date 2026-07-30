# Lemma L-a — tower resists refinement when the top piece is unsplit (lower bound, case a)

**Source.** Certified from approaches `tail-count`, `d-potential`, `tower-induction`
(round 1, all three prove it independently).

## Statement

Let `D_n = 2^{n+1} − 1`. Liu plays the **dyadic tower**

$$T_n \;=\; \frac{1}{D_n}(2^n,\,2^{n-1},\,\ldots,\,2,\,1), \qquad \sum = 1.$$

Suppose Xiang's refinement (using `≤ n` marks) **leaves the top piece `2^n/D_n` unsplit**
(he may refine the rest arbitrarily). Then the alternating sum of the final sorted multiset
satisfies `D ≥ 1/D_n`, equivalently Liu's odd-index take `≥ 2^n/D_n`.

This holds for **all `n` simultaneously** — no induction hypothesis is used.

## Proof

Write the refined rest (sorted descending) as `R' = (r_1 ≥ r_2 ≥ …)`, summing to
`(2^n − 1)/D_n` (the rest of the tower). The tower's defining property is

$$2^n \;>\; 2^n - 1 \;=\; (\text{sum of all smaller tower pieces}),$$

so the top piece `A := 2^n/D_n` *strictly exceeds* the total of the rest, hence strictly
exceeds every rest piece: `A > r_1`. Therefore in the global sorted order the top piece
occupies position 1 (sign `+` in the alternating sum), and the rest fills positions
`2, 3, …`:

$$D \;=\; A \;-\; (r_1 - r_2 + r_3 - \cdots) \;=\; A - D(R').$$

For any descending multiset `R'`, `D(R') ≤ r_1 ≤ \text{total}(R')`: indeed
`D(R') = r_1 - r_2 + r_3 - … = r_1 + (-r_2+r_3) + (-r_4+r_5) + … ≤ r_1` because each
bracket `(-r_{2i}+r_{2i+1}) ≤ 0` (descending). Hence `D(R') ≤ \text{total}(R') =
(2^n−1)/D_n`, and

$$D \;=\; A - D(R') \;\ge\; \frac{2^n}{D_n} - \frac{2^n-1}{D_n} \;=\; \frac{1}{D_n}. \quad\blacksquare$$

**Equivalent shorter form** (used by `d-potential`): since the top piece alone equals
`2^n/D_n` and occupies an odd slot, Liu's odd-index sum `≥ a_1 = 2^n/D_n` directly — no
estimate on `D(R')` needed.

## Note

This is only **case (a)** of the lower bound. The complementary **case (b)** (Xiang *does*
split the top piece) is the load-bearing open gap: the strict dominance `2^n > 2^n−1` is
lost, and the fragments of the split top interleave non-trivially with the refined rest.
Verified numerically for `n ≤ 4` (0 violations over 300 000+ random refinements per n),
but no general proof exists yet.
