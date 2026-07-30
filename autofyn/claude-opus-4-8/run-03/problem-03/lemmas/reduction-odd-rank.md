# Lemma R (Reduction / greedy claiming) — CERTIFIED round 1

**Statement.** Fix a finite multiset of nonnegative reals sorted descending
`b_1 ≥ b_2 ≥ … ≥ b_M`. Two players alternately claim one unclaimed element, Liu (first
mover) and Xiang, each maximising his own total. Under optimal play Liu's total is the
odd-rank sum `b_1 + b_3 + …` and Xiang's is `b_2 + b_4 + …` (equivalently: "take a
currently-largest unclaimed piece" is optimal for whoever moves). With `Σ b_i = 1`,
Liu's total `= (1+D)/2` where `D := Σ_i (−1)^{i+1} b_i ≥ 0`.

**Proof.** Let `V(S)` be the first mover's optimal total on multiset `S`. If the first
mover takes `b_j`, the opponent is first mover on `S∖{b_j}` and secures `V(S∖{b_j})`,
leaving the first mover `Σ(S) − V(S∖{b_j})`; maximising,
`V(S) = Σ(S) − min_j V(S∖{b_j})`. Strong induction on |S|: removing the largest `b_1`
yields sorted remainder `c` with `c_i = b_{i+1}`; removing any `b_j` (j≥2) yields `d` with
`d_i = b_i` (i<j), `d_i = b_{i+1}` (i≥j), so `d_i ≥ c_i` componentwise. The odd-rank sum is
a nonnegative combination of sorted coordinates, hence `oddsum(d) ≥ oddsum(c)`; the minimum
is at `j=1`, giving `V(S) = Σ(S) − (b_2+b_4+…) = b_1+b_3+…`. Then
`D = 2V − Σ = Σ(−1)^{i+1}b_i ≥ 0` (pair `b_{2i-1} ≥ b_{2i}` plus nonneg tail). ∎

Verified numerically (2000 random multisets, `V = oddsum`) by the reviewer, round 1.
Approach-agnostic; importable by any approach.
