# Proof-builder report — bounded-diff-finite-state (round 1)

## Approach
`results/imo-2026-06/approaches/bounded-diff-finite-state.md` — bounded differences ≤ rad(a_1) ⇒ finite-state automaton on residues + stable small-support family ⇒ pigeonhole periodicity ⇒ lift to equality ⇒ from-n=1.

## What I proved (rigorous, complete)

1. **Bounded-difference lemma** (Lemma 1): `a_{n+1} - a_n ≤ R := rad(a_1)` for all `n ≥ 1`. Mechanism: the next multiple of `R` after `a_n` is divisible by every prime of `a_1`, and every past term shares a prime of `a_1` with it, so it is always admissible. Non-circular. **Proposed for `lemmas/bounded-difference.md`.**

2. **Universal small-prime lemma** (Lemma 2): every `a_n` is divisible by some prime of `a_1` (hence by a prime `≤ R`). Consequence: the small primes ever appearing, `S_0`, are contained in the fixed finite set `{primes ≤ R}`. **Proposed for `lemmas/universal-small-prime.md`.**

3. **Family-stabilization lemma** (Lemma 3): the small-prime-support family `F_n = {supp(a_i) ∩ S_0 : i ≤ n}` is monotone in the finite poset `2^{S_0}`, hence stabilizes at some `F` for `n ≥ N`. Then the small-prime admissible set `B = ∩_{σ∈F} ∪_{p∈σ} pZ` is fixed and `L_0`-periodic, `L_0 = ∏_{p∈∪F} p`, and `B ⊇ R·Z ≠ ∅`. Also `A_n ⊇ B` for `n ≥ N`, giving the one-sided bound `a_{n+1} ≤ min(B ∩ (a_n,∞))`.

4. **Cyclic-successor theorem** (Theorem 1): iterating `f(x) = min(B∩(x,∞))` on a fixed nonempty `L`-periodic set `B` gives `x_{k+T} = x_k + L` for all `k ≥ 0`, `T = |B mod L|`, a single cycle with **no pre-period**. Full proof via the cyclic ordering of residues. **Proposed for `lemmas/cyclic-successor.md`** (also targeted by `periodic-set-iteration`; merge if duplicate).

5. **Trivial Case A**: `a_1` even ⇒ `T=1, L=2`. Clean induction using consecutive-integer coprimeness (`gcd(a_n+1,a_n)=1` forces `a_{n+1} ≥ a_n+2`; `a_n+2` even hits all even past terms).

6. **Trivial Case B**: `a_1 = p^k` (prime power) ⇒ `T=1, L=p`. Pure-prime-power structure: candidates `a_n+1,...,a_n+(p-1)` are not divisible by `p`, hence coprime to `a_1 = p^k` and inadmissible; `a_n+p` is admissible.

7. **Conditional spine**: under Hypothesis B1 (greedy = cyclic successor on fixed `B` from `n=N`) Theorem 1 gives `a_{N+k+T}=a_{N+k}+L`; under B2 (`N=1`) this is from `n=1`.

## Gaps that remain (exact steps)

**[GAP: B1] — large-prime shortcuts / kernel stabilization.** After Lemma 3, the small-prime admissible set `B` is fixed, but the actual greedy `a_{n+1} = min(A_n ∩ (a_n,∞))` may use primes `> R` to land strictly below `min(B ∩ (a_n,∞))` (the inequality `a_{n+1} ≤ min(B∩...)` in (†) is one-sided). I could not prove equality.

**The skeleton's competing-candidate + Bertrand mechanism is INVALID as stated.** The sub-claim "the next multiple of a single kernel prime `p ≤ R` is `≤ a_n + p ≤ a_n + R`, a competing admissible candidate" is false: a multiple of a single `p` hits only past terms divisible by `p`, not every past term, so it is not generally admissible. Only the next multiple of `R` (all primes of `a_1` together) is universally admissible — and that gives Lemma 1, not B1. Bertrand's postulate (KB) guarantees a prime in a dyadic range but does not compare the sizes of two specific candidate integers hitting disjoint collections of past terms. Recorded in the approach file under "The gap" so it is not retried.

**[GAP: B2] — from-n=1 / empty pre-period.** Even granting B1, the stabilization index `N` of Lemma 3 is generally `> 1` (support family grows during the first few terms). Theorem 1 then gives periodicity from `n = N`, not `n = 1`. Extending to `n = 1` requires showing the early growth is consistent with the eventual cyclic-successor trajectory (equivalently, injectivity of the transition on reachable residues — the `bijection-from-n1` route's crux). Not proved. Free in trivial Cases A, B (induction handles `n=1` directly).

## Shared lemmas proposed for certification
- `results/imo-2026-06/lemmas/bounded-difference.md` — `a_{n+1}-a_n ≤ rad(a_1)`.
- `results/imo-2026-06/lemmas/cyclic-successor.md` — iterating least-greater-than on a periodic set ⇒ single cycle, `x_{k+T}=x_k+L` from `k=0`.
- `results/imo-2026-06/lemmas/universal-small-prime.md` — every `a_n` divisible by a prime of `a_1`.

## Self-assessed status
**partial.** The proof is complete and rigorous for trivial Cases A (even `a_1`) and B (prime-power `a_1`). For the hard case (odd `a_1` with ≥2 distinct prime factors, not collapsing to a common prime) the argument is complete modulo B1 and B2, both honestly flagged as unproved. The skeleton's B1 mechanism was found to be invalid as stated; I did not paper over it. The reusable lemmas (bounded-difference, cyclic-successor, universal-small-prime) are fully proved and should benefit the other routes regardless of whether B1/B2 close.
