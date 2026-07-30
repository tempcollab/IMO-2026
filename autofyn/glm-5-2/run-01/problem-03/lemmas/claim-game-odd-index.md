# Lemma 0 — claim game = odd-index sum; greedy is optimal

**Source.** Certified from approach `tower-induction` (round 1). The clean proof below is
the reviewer-adapted version of `tower-induction`'s derivation (which is sign-correct);
note the `tail-count` approach's write-up of the same lemma contains a sign error in the
displayed formula and must NOT be used as written — see "Proof" below.

## Statement

Let `a_1 ≥ a_2 ≥ … ≥ a_m` be a fixed multiset of nonnegative reals (the pieces), total `T`.
In the zero-sum alternating draft where the player to move claims any one remaining piece
and both play optimally (first mover maximising his total), the value to the first mover is

$$V \;=\; a_1 + a_3 + a_5 + \cdots \quad\text{(odd-index sum)} \;=\; \frac{T + D}{2},$$

where `D = a_1 − a_2 + a_3 − …` is the alternating (signed) sum of the sorted-descending
multiset. The greedy rule "always take the largest remaining piece" is optimal for both
players. (Technique: backward induction on `m`; knowledge_base "Induction".)

## Proof

For a remaining multiset `S` (sorted desc), let `V(S)` denote the *advantage* of the player
to move (their take minus the opponent's take). We prove by induction on `|S|` that
`V(S) = D(S)` (the alternating sum of `S`) and that taking the largest element attains it.
Since the first mover's payoff `= (T + V)/2 = (T + D(S_full))/2`, the lemma follows.

*Base.* `|S|=0`: `V=0=D(∅)`. `|S|=1`, `S={a_1}`: the mover takes `a_1`;
`V = a_1 = D({a_1})`. ✓

*Inductive step.* Let `S = {a_1 ≥ … ≥ a_m}`, `m ≥ 2`. If the mover takes `a_j`, the
opponent is then to move on `S\setminus{a_j}` and, by the IH, achieves advantage
`D(S\setminus{a_j})` over the mover's *remaining* pieces. Hence the mover's net advantage
from taking `a_j` is

$$\text{payoff}_j \;=\; a_j - D(S\setminus\{a_j\}).$$

Compute `D(S\setminus{a_j})`: removing `a_j` leaves the sorted list
`a_1,…,a_{j−1},a_{j+1},…,a_m`; elements after position `j` shift left by one, so their sign
flips relative to `D(S)`:

$$D(S\setminus\{a_j\}) \;=\; \sum_{i<j}(-1)^{i+1}a_i \;+\; \sum_{i>j}(-1)^{i}\,a_i.$$

Meanwhile `D(S) = \sum_{i<j}(-1)^{i+1}a_i + (-1)^{j+1}a_j + \sum_{i>j}(-1)^{i+1}a_i`. The
two tail sums (`i>j`) cancel in pairs since `(-1)^i + (-1)^{i+1}=0`, so

$$\text{payoff}_j - D(S) \;=\; a_j\bigl(1-(-1)^{j+1}\bigr) \;-\; 2\sum_{i<j}(-1)^{i+1}a_i.$$

- **`j` odd (`j ≥ 3`):** `1−(−1)^{j+1}=0`, so `payoff_j − D(S) = −2\sum_{i<j}(−1)^{i+1}a_i
  = −2[(a_1−a_2)+(a_3−a_4)+…+(a_{j−2}−a_{j−1})]`. Each bracket `a_{2i−1}−a_{2i} ≥ 0`
  (descending), so `payoff_j − D(S) ≤ 0`. Equality at `j=1` (empty sum).

- **`j` even (`j ≥ 2`):** `1−(−1)^{j+1}=2`, and `\sum_{i<j}(−1)^{i+1}a_i =
  (a_1−a_2)+…+(a_{j−3}−a_{j−2})+a_{j−1}` (the last term `i=j−1` is odd, sign `+`). Hence
  `payoff_j − D(S) = 2a_j − 2[(a_1−a_2)+…+(a_{j−3}−a_{j−2})+a_{j−1}] = −2[(a_1−a_2)+(a_3−a_4)+…+(a_{j−1}−a_j)] ≤ 0`.

In both parities `payoff_j ≤ D(S)`, with equality at `j=1` (greedy, empty pre-sum). Hence
`max_j payoff_j = D(S)`, attained by the greedy move `j=1`, and `V(S)=D(S)`. ∎

(Computational countercheck: full minimax game-tree value equals the odd-index sum on 300
random multisets of sizes 2–6, 0 mismatches.)

## Warning about the `tail-count` write-up

The `tail-count` approach records this lemma with the formula
`T_1 − T_j = a_1 + (a_3−a_2) + (a_5−a_4) + …`, which is **incorrect** (a sign/ordering
error). The correct formula (used above) is `T_1 − T_j = (a_1−a_2) + (a_3−a_4) + … + (a_{j−2}−a_{j−1})`
for `j` odd. The *conclusion* of the `tail-count` write-up (greedy is optimal, value =
odd-index sum) is correct, but the displayed derivation is not; use this certified proof
instead.
