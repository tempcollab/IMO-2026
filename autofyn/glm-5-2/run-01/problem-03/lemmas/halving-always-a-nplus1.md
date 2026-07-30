# Lemma: halving-always-a-nplus1

**Status:** CERTIFIED (round 6, reviewer-certified).

**Statement.** For a strictly-decreasing Liu config L = (a_1 > a_2 > ... > a_{n+1}) with m = n+1 (all pieces distinct), Xiang's strategy of halving the n largest pieces (a_1, ..., a_n) and leaving a_{n+1} unsplit uses n marks and gives

$$D = a_{n+1}.$$

No bottom-dominance hypothesis is required. Hence D*(L) ≤ a_{n+1} for EVERY strictly-decreasing m = n+1 config.

**Generalizes `bottom-dominant-halving`** (drops the a_n ≥ 2·a_{n+1} hypothesis).

**Proof.** Xiang splits each a_i (i = 1, ..., n) into {a_i/2, a_i/2}. This uses n marks. The refined multiset is

$$M' = \{a_1/2, a_1/2, \ldots, a_n/2, a_n/2, a_{n+1}\},$$

total 2n+1 pieces.

**Step 1 — block decomposition.** Sort M' non-increasingly and group consecutive equal values into maximal blocks.

**Step 2 — every value v ≠ a_{n+1} appears an even number of times.** The values that can appear are {a_1/2, ..., a_n/2, a_{n+1}}. Since L is strictly decreasing (a_1 > ... > a_n), the values a_1/2 > ... > a_n/2 are pairwise distinct. Each a_i/2 (i = 1,...,n) appears exactly 2 times (the two halves of a_i), UNLESS a_i/2 = a_{n+1} (i.e., a_i = 2·a_{n+1}). For each i with a_i ≠ 2·a_{n+1}: the value a_i/2 appears exactly 2 times (even), and no other a_j/2 equals it (distinctness). So every block whose value is ≠ a_{n+1} has even size.

**Step 3 — a_{n+1} appears an odd number of times.** The value a_{n+1} appears 1 (the unsplit tail) + 2·#{i : a_i = 2·a_{n+1}} times. Since L is strictly decreasing, at most one i has a_i = 2·a_{n+1}. So multiplicity is 1 (k=0) or 3 (k=1), both ODD.

**Step 4 — the a_{n+1}-block starts at an odd position.** In the sorted order, the a_{n+1}-block is preceded by blocks whose values are ≠ a_{n+1} (all even size, by Step 2). The total number of pieces preceding the a_{n+1}-block is the sum of these even block sizes — an EVEN number. Adding 1 (positions are 1-indexed), the a_{n+1}-block starts at position 1 + (even) = ODD.

**Step 5 — block-contribution formula** (`block-contribution-formula`, certified). A block of size s starting at position p contributes v·(#plus − #minus over positions p,...,p+s−1):
- s even (= 2k): k plus, k minus, contributes 0.
- s odd (= 2k+1), p odd: (k+1) plus, k minus, contributes +v.

**Step 6 — assemble.** Every block with value v ≠ a_{n+1} has even size ⟹ contributes 0. The a_{n+1}-block has odd size and starts at an odd position (Steps 3–4) ⟹ contributes +a_{n+1}. Therefore D(M') = a_{n+1}. ∎

**Mark budget.** n marks. ✓

**Edge case a_i = 2·a_{n+1} (handled explicitly).** When some a_i = 2·a_{n+1} (necessarily a unique i by strict decrease), the value a_{n+1} appears 3 times (odd). The three copies form a single size-3 block. The blocks above it are all even-sized, so the size-3 block starts at an odd position; its contribution is +a_{n+1} (Step 5, 2k+1=3, k=1, at odd start: 2 plus, 1 minus). So D = a_{n+1} still. Verified: (4,2,1)/7 with a_2=2=2·1 gives D=1/7; (6,2,1)/9 gives D=1/9.

**Corollary (region closure, all n).** For every n and every strictly-decreasing m=n+1 Liu config L with a_{n+1} ≤ 1/D_n, Xiang has ≤ n marks with D ≤ 1/D_n (namely, halving a_1,...,a_n, giving D = a_{n+1} ≤ 1/D_n). This closes the a_{n+1} ≤ 1/D_n region for all n, unconditionally.

**Numerical verification.** Exact-`Fraction` check, 0 violations / 20000 random strictly-decreasing configs (n=2..6), including 495 configs with the edge case a_i = 2·a_{n+1}. ✓
