# Lemma: periodic-set-iteration (Theorem 1)

**Proposed by:** approach `periodic-set-iteration`. **Status: CERTIFIED (round 1, proof-reviewer).**

**Canonical version.** This is the canonical statement of the "cyclic successor on a periodic set" theorem. The duplicate file `lemmas/cyclic-successor.md` (same theorem, same proof) is to be merged INTO this file; until then treat this one as authoritative. Independently re-derived and verified on the `a_1 = 15` data (residues `{0,6,10,12,15,18,20,24} mod 30`, `T = 8`, orbit `15,18,20,24,30,36,40,42,45` matches the empirical greedy exactly, `x_{k+8}=x_k+30` from `k=0`).

## Statement

Let `A ⊆ ℤ` be a nonempty set which is periodic with positive period `L` (i.e. `A + L = A`), and let
`R = A ∩ [0, L) = {r_1 < r_2 < … < r_T}` be the (nonempty, finite) set of residues of `A` modulo `L`,
`T = |R|`. Define `f_A(x) = min{ y ∈ A : y > x }` (well-defined because a nonempty periodic set is
unbounded above). Then for every `x_0 ∈ A`, the orbit `x_{k+1} = f_A(x_k)` satisfies

  `x_{k+T} = x_k + L`   for all `k ≥ 0`.

In particular, periodicity holds from `k = 0` (no pre-period).

## Proof

`A` is `L`-periodic and nonempty, so `A + L = A`; hence `A` is unbounded above (if `a ∈ A` then
`a + jL ∈ A` for every `j ≥ 0`), and `f_A` is well-defined on all of `ℤ`. Because `A + L = A`, an
integer `m` belongs to `A` if and only if `m mod L ∈ R`. The set `R` is nonempty (since `A` is),
and `T = |R| ≥ 1`.

Fix `x_0 ∈ A`; write `ρ_0 = x_0 mod L ∈ R`. More generally let `ρ_k = x_k mod L`. We claim the
sequence of residues `(ρ_k)` is exactly the cyclic successor on the ordered list
`r_1 < r_2 < … < r_T`:

  (CS)   if `ρ_k = r_i` with `i < T`, then `ρ_{k+1} = r_{i+1}`;
         if `ρ_k = r_T`, then `ρ_{k+1} = r_1`.

Indeed, suppose `ρ_k = r_i` with `i < T`. Consider the candidate
`y = x_k + (r_{i+1} − r_i)`. Then `y > x_k`, `y ≡ r_{i+1} (mod L)`, hence `y ∈ A`; so
`f_A(x_k) ≤ y`. Conversely, every `z` with `x_k < z < y` satisfies `z mod L ∈ (r_i, r_{i+1})`
(here `(r_i, r_{i+1})` is the open interval of residues strictly between `r_i` and `r_{i+1}`),
which is disjoint from `R` by the definition of consecutive elements of the sorted set `R`; hence
`z ∉ A`, so `f_A(x_k) ≥ y`. Therefore `f_A(x_k) = y`, and `ρ_{k+1} = r_{i+1}`. The case
`ρ_k = r_T` is identical with the candidate `y = x_k + (L − r_T) + r_1` (the wrap-around to the
next period): every `z` with `x_k < z < y` has `z mod L ∈ (r_T, L) ∪ [0, r_1)`, again disjoint
from `R`, so `y` is the least element of `A` greater than `x_k`. This proves (CS).

The cyclic successor (CS) is, by construction, a single cycle of length `T` on `R` (it advances
one step along the ordered list and wraps around). Hence `ρ_{k+T} = ρ_k` for all `k ≥ 0`. Moreover,
the displacement over one full residue period telescopes:

  `x_{k+T} − x_k = Σ_{j=0}^{T-1} (x_{k+j+1} − x_{k+j})`.

Each summand is one of `r_{i+1} − r_i` (for `i < T`) or `L − r_T + r_1` (the wrap step). Summed
around the full cycle these cancel telescopically and leave exactly

  `(r_2−r_1) + (r_3−r_2) + … + (r_T − r_{T-1}) + (L − r_T + r_1) = L`.

Therefore `x_{k+T} = x_k + L` for every `k ≥ 0`, with periodicity from `k = 0`. ∎

## Corollary (from the start)

Because the cyclic successor is a bijection (a single cycle) on `R` rather than merely an
eventually-periodic map, the equality `x_{k+T} = x_k + L` holds beginning at `k = 0` once the
orbit lies in a fixed periodic set `A`. No pre-period is incurred inside `A`.

## Use

This is the clean "lift = L" / "from-n = 1" mechanism. Once a greedy sequence is shown to evolve,
from some index onward, as the least-greater-than map on a *fixed* periodic set `A`, Theorem 1
gives `a_{n+T} = a_n + L` (with `T = |A ∩ [0,L)|`) from that index onward, with no transient
internal to `A`.
