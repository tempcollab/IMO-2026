# Lemma: n=1 full closure, the c(n) recursion, and a certified negative result

**Status:** certified (round 2). Source: `recursive-embedding-induction.md`
(Lemma G0, Lemma G1, and the refuted Candidate Lemma). Reviewer independently
verified: Lemma G1's recursion by exact `Fraction` computation for `n=1..7`
(all matched); the counterexample to the Candidate Lemma by exact `Fraction`
arithmetic (reproduced below, confirmed).

## Lemma G0 (full n=1 lower bound, all k)

At `n=1`, `A_1={2/3,1/3}`, `c(1)=2/3`. For every Xiang-Yu response (either
`k=0`, mark unused/spent on `p_2`, or `k=1`, mark splits `p_1` into
`s_1≥s_2>0`, `s_1+s_2=2/3`), `oddrank(B) ≥ c(1) = 2/3`, with equality
attainable. (`k=0`: trivial, `p_1` survives, dominates `p_2` since `p_1>p_2`.
`k=1`: the only achievable order-types of `{s_1,s_2,1/3}` are the interleaved
one, `s_1 ≥ 1/3 ≥ s_2`, giving `oddrank = s_1+s_2 = 2/3` exactly for
*every* `s_2 ∈ (0,1/3]`; the other order-types are shown to collapse to the
same boundary point by direct algebra, not a separate region.) This is a
complete closed form for `n=1`, both values of `k`, every split.

## Lemma G1 (recursive identity)

`c(n) = 2λ_n c(n-1)` for every `n≥1`, where `λ_n := 1-c(n) = Σ_{i≥2}p_i`.
Equivalently `p_2 = λ_n c(n-1)`.

*Proof.* By self-similarity (`geometric-configuration-facts.md`, Lemma 3),
`p_2 = λ_n p'_1` where `p'_1` is the top piece of `A_{n-1}`, i.e. `p'_1 =
c(n-1)`. So `p_2 = λ_n c(n-1)`, and since `p_1 = 2p_2` (direct from the
closed form `p_1=2^n/D`, `p_2=2^{n-1}/D`), `c(n)=p_1=2p_2=2λ_n c(n-1)`. ∎

## Certified negative result: "merge-by-sums-alone" is FALSE

**(Refuted) Candidate Lemma.** *If `S`,`T` are finite multisets of positive
reals with `Σ(S)=σ > τ=Σ(T)`, then `evenrank(S∪T) ≤ τ` (equivalently
`oddrank(S∪T) ≥ σ`).*

**Counterexample** (exact `Fraction` arithmetic):
`S = {37/100, 37/100, 36/100}` (`Σ(S)=11/10`), `T = {73/200,71/200}`
(`Σ(T)=18/25 < 11/10`). Merged and sorted descending (common denominator 200):
`74,74,73,72,71` (units of `1/200`). Odd ranks (1,3,5): `74+73+71=218`, so
`oddrank(S∪T) = 218/200 = 109/100 < Σ(S) = 110/100`. The Candidate Lemma's
conclusion fails.

**Consequence.** No argument bounding `oddrank`/`evenrank` of a merge using
only the aggregate sums `Σ(S)`, `Σ(T)` (discarding individual/ordered values)
can be correct in general — this rules out a purely scalar induction on `n`
(via Lemma G1 alone) from closing the general lower-bound gap; any successful
proof must track the specific ordered structure of the tail through the
induction, not just its total mass. Reusable to prevent future rounds from
re-attempting this specific shortcut in
`geometric-dominance-construction.md`, `recursive-embedding-induction.md`, or
`universal-adversary-strategy.md`.
