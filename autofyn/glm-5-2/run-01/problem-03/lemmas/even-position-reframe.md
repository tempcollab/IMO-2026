# Lemma: even-position-reframe

**Status:** CERTIFIED (round 6, reviewer-certified).

**Statement.** Let L be a Liu config with total T(L) = 1 (unit stick), and let M' be Xiang's ≤ n-mark refinement (re-sorted non-increasingly). Write O = Σ_{j odd} b_j (odd-position sum) and E = Σ_{j even} b_j (even-position sum), so O + E = T(L) = 1. The alternating sum is D(M') = O − E, hence

$$D(M') = 1 - 2E, \qquad E = \frac{1 - D(M')}{2}.$$

Xiang (the outer minimizer of D) is equivalently the maximizer of E, the even-position mass. The upper bound D* ≤ 1/D_n is equivalently E* ≥ (2^n − 1)/D_n, where D_n = 2^{n+1} − 1.

**Proof.** By `claim-game-odd-index` (Lemma 0, certified), the alternating-draft value to Liu is the odd-index sum V = (T + D)/2, where T = Σ b_j = 1 and D = b_1 − b_2 + b_3 − ⋯. Decompose the total: O + E = T = 1, and D = O − E. Adding and subtracting: O = (1 + D)/2, E = (1 − D)/2. Hence D = 1 − 2E and E = (1 − D)/2.

Since D = 1 − 2E is strictly decreasing in E, Xiang (minimizing D) equivalently maximizes E. The upper bound D* ≤ 1/D_n is equivalently E* ≥ (1 − 1/D_n)/2 = (D_n − 1)/(2·D_n) = (2^{n+1} − 2)/(2·D_n) = (2^n − 1)/D_n. ∎

**Remark.** This is a trivial algebraic reframe of `claim-game-odd-index` + total = 1. It makes the GAP-U2 equivalence transparent: E* ≥ (2^n−1)/D_n ⟺ D* ≤ 1/D_n. The even-packing lens reframes but does NOT bypass the crux — the load-bearing step (exhibit marks creating ties/pairings with small leftover) is identical to GAP-U2-compressed.
