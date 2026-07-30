# Lemma BL (band-landing / first crossing) — CERTIFIED (round 9)

**Certification (round 9).** Reviewer-verified independently. (1) `P_0<…<P_n=L−a_1>a_1` (strict from
`a_1<L/2`), `P_0=0≤a_1` ⇒ unique first crossing index `k≤n`; finite strictly-increasing sequence, no
straddle — correct. (2) `r=a_1−P_{k−1}∈[0,s_k)`, `s_k≤a_2<β_nL` — correct. (3) all running values
`a_1−P_{j−1}≥r≥0` for `j≤k` ⇒ no abs-flip, caterpillar value `=r`, exactly certified Lemma ESF-1 with
`Σ_{i=2}^k a_i=P_{k−1}≤a_1`, `n` moves — correct. n=2 witness reproduced exactly (`k=2, r=17/100`).
Does NOT reach `u_nL` (r=17/100>u_2; greedy iteration overshoots) — honestly recorded; GAP U-cover
stays open. Admitted.


**Statement.** Let `A = {a_1 ≥ a_2 ≥ … ≥ a_{n+1}}` be a full-budget balanced-valley profile
(sum `L`, `a_1 < L/2`). Let the survivors be `s_1 = a_2 ≥ s_2 = a_3 ≥ … ≥ s_n = a_{n+1}` with
descending partial sums `P_0 = 0`, `P_j = s_1 + … + s_j` (`1 ≤ j ≤ n`). Then:

1. `P_n = L − a_1 > a_1`, so the strictly increasing finite sequence `P_0 < P_1 < … < P_n` crosses
   `a_1`: there is a **unique** index `k ∈ {1,…,n}` with `P_{k−1} ≤ a_1 < P_k`.
2. For the subset `T = {a_1, a_2, …, a_k}`, the value `r := a_1 − P_{k−1} = a_1 − Σ_{i=2}^{k} a_i`
   satisfies
   ```
        0 ≤ r < s_k ≤ a_2   (hence r < β_n L under the valley cap a_2 < β_n L),
   ```
   where `β_n = 2^{n−1}/(2^{n+1}−1)`.
3. `r` equals the descending-KK caterpillar value of `T` and lies in `𝓡(A)`, realized by exactly
   `n` DELETE/MATCH moves (certified Lemma ESF-1).

**Proof.**
(1) The survivors are positive, so `P_0 < P_1 < … < P_n` is strictly increasing, and
`P_n = Σ_{i=2}^{n+1} a_i = L − a_1`. The valley hypothesis `a_1 < L/2` gives `L − a_1 > L/2 > a_1`,
i.e. `P_n > a_1`, while `P_0 = 0 ≤ a_1`. A strictly increasing finite real sequence that starts `≤ a_1`
and ends `> a_1` has a unique first index `k` with `P_k > a_1`; then `P_{k−1} ≤ a_1 < P_k`. This is a
discrete intermediate-value statement about a totally ordered finite list — no continuity is invoked,
and there is **no straddle/boundary ambiguity**: exactly one index satisfies the two-sided
inequality. Since `P_n > a_1`, we have `k ≤ n`, so `T` uses only real survivors.

(2) From `P_{k−1} ≤ a_1`: `r = a_1 − P_{k−1} ≥ 0`. From `P_k = P_{k−1} + s_k > a_1`:
`s_k > a_1 − P_{k−1} = r`, i.e. `r < s_k`. Finally `s_k ≤ s_1 = a_2` by the sorting, and `a_2 < β_n L`
in the valley, giving `r < β_n L`.

(3) Order `T` descending: `a_1 ≥ a_2 ≥ … ≥ a_k`. For `2 ≤ j ≤ k` the running value after subtracting
`a_2,…,a_j` is `a_1 − Σ_{i=2}^{j} a_i = a_1 − P_{j−1} ≥ a_1 − P_{k−1} = r ≥ 0` (since `j ≤ k` gives
`P_{j−1} ≤ P_{k−1}`); in particular every subtraction stays nonnegative, so no abs-flip occurs and the
caterpillar value is `a_1 − P_{k−1} = r`. Since `Σ_{i=2}^{k} a_i = P_{k−1} ≤ a_1`, this is exactly
certified Lemma ESF-1 with subset `{2,…,k}`, realized by `k−1` MATCHes and `n−(k−1)` DELETEs `= n`
moves, with `D = r`. ∎

**Certification notes.** Self-contained on the sorting hypothesis and certified Lemmas P
(`cancelling-pair`), DM (`elementary-reductions`), ESF-1 (`subtraction-from-top-subfamily`),
M (`measure-identity`). The strict valley inequality `a_1 < L/2` is exactly what forces `P_n > a_1`
(the crossing to exist with `k ≤ n`). Verified on the `n=2` witness `A = {9/20, 7/25, 27/100}`:
survivors `28/100 ≥ 27/100`, `P_1 = 28/100 ≤ a_1 = 45/100 < P_2 = 55/100`, so `k = 2`,
`r = 45/100 − 28/100 = 17/100 ∈ [0, s_2 = 27/100) ⊂ [0, β_2 = 2/7)` (exact arithmetic).

**Role / limitation (recorded).** Lemma BL lands the FIRST subset value `r ∈ [0, β_n L)`, one dyadic
band below the `a_1` scale. It does NOT by itself reach `u_n L`: on the `n=2` witness `r = 17/100 >
u_2 = 1/7`, and iterating BL as a greedy recursion provably overshoots (worst ratio up to `11.4×` for
`n ≤ 7`, machine-checked). The residual after BL — closing the remaining factor `2^{n−1}` down to
`u_n L` — is a GLOBAL covering statement (see `breakpoint-vertex.md` §4B.5, GAP U-cover: the
descending include/skip reachable set meets `[0, u_n L]`), not a recursion.
