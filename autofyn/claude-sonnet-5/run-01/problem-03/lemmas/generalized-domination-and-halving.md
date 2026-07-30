# Lemmas: generalized domination construction and halving reduction

**Status:** certified (round 2). Source: `universal-adversary-strategy.md`
(Lemma DOM, Lemma HALVE). Reviewer independently verified both identities by
exact-`Fraction` randomized testing (3000 trials each, arbitrary tail shapes,
arbitrary refinements) — no violation found; both are exact algebraic
identities, not heuristics.

These lemmas apply to **any** sorted list of positive reals (not just the
geometric configuration `A_n`), and are aimed at the arbitrary-configuration
upper bound `max_A min_B oddrank(B) ≤ c(n)`.

## Lemma DOM (Generalized Domination Construction)

Let `A = (p_1 ≥ p_2 ≥ ⋯ ≥ p_m)` be any sorted list of positive reals
(any `m ≥ 1`), tail `T := (p_2,...,p_m)` (size `k := m-1`), `S := Σ(T)`.
Suppose `p_1 ≥ S`. Then, using exactly `k` marks (all inside `p_1`), splitting
`p_1` into `q_i = p_{i+1}` (`i=1,...,k`), `q_{k+1} = r := p_1-S ≥ 0`, and
merging with the untouched tail `T` gives `B = {q_1,...,q_{k+1}} ∪ T` with
`oddrank(B) = p_1` **exactly**.

*Proof.* Write `T = (t_1≥⋯≥t_k)`. The merge before inserting `r` is
`E := {t_1,t_1,...,t_k,t_k}` (each tail element duplicated once, from `T`
itself and once from `{q_1,...,q_k}={t_1,...,t_k}`). In `E`, the pair of
copies of `t_i` occupies ranks `2i-1,2i`, so `oddrank(E)=evensum(E)=Σt_i=S`
(both odd- and even-rank sums equal `S`, since the two copies of each value
are numerically identical). Now insert `r`: let `j` be the number of `t_i≥r`.
`r` lands at global position `2j+1` (odd) in the merged sorted list of size
`2k+1`; the block before it (ranks `1..2j`) contributes `t_1+⋯+t_j` to
`oddrank`; `r` itself contributes `r`; the block after it (ranks
`2j+2,...,2k+1`, a shift by the odd number `2j+1` from its internal order)
contributes `t_{j+1}+⋯+t_k` to `oddrank` regardless of the parity flip,
since its internal odd-sum and even-sum are equal (both `= t_{j+1}+⋯+t_k`,
by the duplicate-pair argument above, applied to the sub-tail). Summing:
`oddrank(B) = (t_1+⋯+t_j) + r + (t_{j+1}+⋯+t_k) = S + r = S + (p_1-S) = p_1`,
for every `j`, i.e. unconditionally once `p_1 ≥ S`. ∎

**Corollary DOM'.** If `p_1 ≥ S` and `p_1 ≤ c(n)`, then `k=m-1 ≤ n` marks
suffice for Xiang Yu to force `oddrank(B) = p_1 ≤ c(n)`. This settles the
entire regime `S ≤ p_1 ≤ c(n)` of the arbitrary-configuration upper bound,
for any tail shape.

## Lemma HALVE (Halving reduction)

Let `A=(p_1≥p_2≥⋯≥p_m)`, tail `T=(p_2,...,p_m)`, and suppose `p_1 ≥ 2p_2`
(so `p_1/2 ≥ p_2 ≥` every element of `T`). Using 1 mark, split `p_1` into two
equal halves `p_1/2,p_1/2`. Then for **any** further refinement `T'` of `T`
(using any number of further marks, not touching the two halves),
`oddrank(B) = p_1/2 + oddrank(T')`, where `B = {p_1/2,p_1/2} ∪ T'`.

*Proof.* Since `p_1/2 ≥ p_2 ≥` every element of `T'` (refining only shrinks
individual pieces), the two copies of `p_1/2` occupy ranks `1,2` of `B`, and
`T'`'s internal rank `i` becomes global rank `i+2` — a shift by the even
number `2`, preserving parity. Hence `oddrank(B) = p_1/2 + oddrank(T')`
(rank 1, odd, contributes `p_1/2`; rank 2, even, the second copy, excluded;
the rest matches `T'`'s own odd/even split unchanged). ∎

## What remains open (not part of this certified lemma set)

Lemma DOM and Lemma HALVE each settle only a sub-case (`S≤p_1≤c(n)`, resp.
`p_1≥2p_2` with a *further* inductive hypothesis on `T'` that is not yet
established). Neither lemma, nor their claimed combination, closes the
general arbitrary-configuration upper bound: numerical counterexamples
(recorded in `universal-adversary-strategy.md`, "Dead ends" section) show the
correct optimal Xiang-Yu response sometimes must split *both* `p_1` and a
non-adjacent tail piece simultaneously, ruling out any single static
threshold rule built from these two lemmas alone. Only `n=1` is fully closed
this way so far.
