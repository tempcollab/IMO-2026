# Proof-builder report v2 — w-descent-rsmooth (round 3, post-patch)

## Headline
**SOLVED.** Applied the reviewer-specified one-case-split patch to Lemma 2, re-verified the entire proof end-to-end across `a_1 ∈ {15,35,77,91,105,135,175,187,221,385}` (including the purely-smooth regime), and confirmed the descent survives the `r' = r` equality case. No remaining gaps.

File: `/home/agentuser/repo/results/imo-2026-06/approaches/w-descent-rsmooth.md` (Status: solved).

## The patch (Lemma 2, one-case-split)
- **Case 1 (b is k-smooth, no prime > a_1):** take `x = b`. Trivially `k ≤ x ≤ b` (equality), k-smooth, similar to b. This is the **base case** — nothing to strip. It carries the whole argument in the purely-smooth regime (`a_1 ∈ {175, 221, 385}`), where NO greedy term ever has a big prime and Case 2 never fires.
- **Case 2 (b has a big prime q > a_1):** the existing strip + inflate-by-minimal-power construction, anchored by `a·q ≤ b`, unchanged. Gives `x < b` (strict).

The conclusion is `x ≤ b` (equality in Case 1, strict in Case 2), which is **deliberate and sufficient**.

## Why the descent survives `r' = r` (the reviewer's stated worry)
The reviewer asked: "if b is k-smooth, x=b is NOT < b — does the descent break?" **No.** The minimal-counterexample descent needs `r' ≤ r`, NOT `r' < r`. The strict decrease that powers the contradiction is `max(r, r') = r < a ≤ max(a, b)` — the inequality `r < a` comes from the **move** `a ⟶ r` (Corollary 1.2, `a ∉ G` ⟹ ∃ good `r < a` coprime to `a`), which is **independent of whether `r' = r` or `r' < r`**. The minimality is on `max(a, b)`; the similar pair `(r, r')` has `max(r, r') = r < a ≤ max(a, b)`, strictly smaller, regardless of the `r'`-vs-`r` relationship. In the purely-smooth regime, Case 1 always fires (`r' = r`), and the descent reduces to: pick minimal counterexample `(a, b)`; move `a ⟶ r`; find a common small prime `p'` of `r` (= `r'`) and `b` (both in G, distinct-or-equal, Cor 1.1 / trivial); similarity forces `p' | a` and `p' | r`, contradicting `gcd(a, r) = 1`. Uniform across both regimes.

## Edge cases verified
- **`r' = b` case:** r' k-smooth ⟹ b k-smooth; b ≥ k ≥ 2 has a small prime; "common prime of r', b" = any prime of r' (=b); small since r' k-smooth. Works.
- **`r' ≠ b` case:** Cor 1.1 gives `gcd(r', b) > 1`, a common prime `p'`; `p' | r'` and r' is k-smooth ⟹ `p'` small. Works.
- **`r = k` case (move target is a_1 itself):** take any prime of k; `p | k, p | r = k`, small. Lemma 2 applies to r. Works.
- **Move existence (Cor 1.2):** verified `r < a` holds for every bad `a` across all 10 a_1 (including purely-smooth 175/221/385). 0 failures.

## Sigma-periodicity consistency
The reviewer corrected the round-2 `sigma-periodicity` lemma's `T'` formula in place (it dropped a factor of `p` when `p | T, p ∤ L`); corrected to `T' = T · ∏_{p ≤ R, p ∤ L} p`. **This proof does not depend on sigma-periodicity** — periodicity is proved directly via similarity + CRT (Part IV), without the v_p/sieve framework. The lemma is mentioned only in the non-load-bearing "B1' subsumed" remark. So the round-2 bug and correction do not affect this proof. (Noted in the file.)

## Computational verification (Python/sympy)
All across `a_1 ∈ {15,35,77,91,105,135,175,187,221,385}`:
- **Lemma 1 (characterization G = H):** 0 mismatches, n ≤ 300.
- **Lemma 2 (patched, with case-split):** 0 failures on every greedy term (first 300 terms). Includes the purely-smooth regime (175/221/385: Case 1, `x = b`, carries everything) and the big-prime regime (15/35/77/91/105/135/187: Case 2 when `b` has a big prime, Case 1 when `b` is k-smooth).
- **Similarity theorem:** 0 violations (uniform G-status within each small-prime signature), n ≤ 800.
- **Lemma 2 outputs in G (by similarity, directly confirmed):** 0 failures — every `x` produced lies in G (within computed range).
- **Move `r < a` (Cor 1.2):** verified for every bad `a` in all regimes, 0 failures.
- **`r' ≤ r` (Lemma 2):** verified in all regimes, 0 failures.

## Status: SOLVED
The proof is complete and rigorous for every `a_1 > 1`:
1. Lemma 1 (greedy-set characterization) — proved.
2. Lemma 2 (s-substitution, with case-split) — proved, patched.
3. Similarity theorem (minimal-counterexample descent) — proved, descent survives `r' = r`.
4. Periodicity (similarity + CRT + Theorem 1, cited) — `a_{n+T} = a_n + P` from `n = 1`, with `P = ∏(primes ≤ a_1)`, `T = |R|`.

B1' AND B2 are both closed (similarity is stronger than B1' and gives periodicity from n=1 directly via Theorem 1's no-pre-period property). No open gaps.

## Promotable lemmas (proposed for certification)
- **Greedy-set characterization** (Lemma 1): `n ≥ a_1` ∈ G iff coprime to none of the smaller G-elements.
- **s-substitution lemma** (Lemma 2, patched): for `b ≥ a_1` with a small prime, ∃ k-smooth `x` similar to `b` with `a_1 ≤ x ≤ b` (Case 1: `x = b` if b k-smooth; Case 2: strip + inflate if b has a big prime).
- **Similarity theorem** (Part III): the crux — two integers ≥ a_1 divisible by the same primes ≤ a_1 have the same G-membership.
