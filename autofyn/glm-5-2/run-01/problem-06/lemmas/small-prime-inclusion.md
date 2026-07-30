# Lemma: small-prime one-sided inclusion

## Status
CERTIFIED (round 2, proof-reviewer). Proved in `approaches/hitting-set-monovariant.md` §3/Lemma 4.

## Statement
Let `M_n` be the minimal hitting sets of the full supports `F_n = {supp(a_i) : i ≤ n}`, `M'_n` the minimal hitting sets of the small-prime supports `F'_n = {σ(a_i) = supp(a_i) ∩ P_R : i ≤ n}`. Then `M'_n ⊆ M_n` (hence `B_n := ∪_{h ∈ M'_n}{mult of m_h} ⊆ A_n := ∪_{g ∈ M_n}{mult of m_g}`), so `a_{n+1} ≤ b_n := min(B_n ∩ (a_n,∞))` for every `n`.

## Proof
Let `h ∈ M'_n`. `h` meets every `σ(a_i)`, hence every `supp(a_i)` (a hit by a small prime is a genuine hit). Minimality for `F_n`: for `p ∈ h`, minimality for `F'_n` gives `i` with `σ(a_i) ∩ (h \ {p}) = ∅`; since `h ⊆ P_R`, `supp(a_i) ∩ (h \ {p}) = σ(a_i) ∩ (h \ {p}) = ∅`, so `h \ {p}` misses `supp(a_i)`. Hence `h` is minimal for `F_n`, so `h ∈ M_n`. ∎

## Scope / reusability
The one-sided inequality underpinning the small-prime lattice. The reverse inclusion is the crux B1'.
