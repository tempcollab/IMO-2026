# Certified lemma: the general-n upper bound (GAP U) — c(n) ≤ 2^n/(2^{n+1}−1)

Certified round 7 (proof-reviewer). Independently verified end-to-end (see below).
Proved in `approaches/dyadic-discrepancy.md` §4.5–4.7 and, by an independent route,
in `approaches/dyadic-discrepancy-euclid.md` §A–§G. Rests only on the previously
certified spine (`greedy-claim.md` = Lemma G + level-measure identity, `cut-flip.md`).

## Statement

Let `u_n = 1/(2^{n+1}−1)`. For every Liu partition of a length-`Σ` segment into
`m ≤ n+1` positive pieces, Xiang has a response using `≤ n` cuts (marks) after which the
final piece multiset `P` has discrepancy `D(P) := Liu − Xiang = 2·(Liu total) − Σ ≤ u_n·Σ`.
Hence `D* = max_Liu min_Xiang D ≤ u_n`, and by the reduction (§0, Lemma G)
`c(n) = (1 + D*)/2 ≤ (1 + u_n)/2 = 2^n/(2^{n+1}−1)`.

This is the **upper-bound half** of P3. (The matching lower bound `D* ≥ u_n` — Liu's
dyadic partition — is Case A (certified) plus GAP L Case B, still open.)

## Load-bearing sub-lemmas (all certified with this file)

1. **Invisible-Pair Lemma (IP).** For any multiset `R` and `v>0`, `D(R ∪ {v,v}) = D(R)`
   (two equal pieces add `2·1[t<v]`, an even amount, to `N(t)` at every threshold, so the
   odd-set `O = {t : N(t) odd}` is unchanged; `D = λ(O)` by the level-measure identity).

2. **Removal ops (each ≤ 1 cut), preserving "final D = discrepancy of the current effective
   multiset":** *bisect* `ℓ` → `{ℓ/2,ℓ/2}` (an invisible pair, deletes `ℓ`); *generalized pin*
   `b` into `a` (`a>b`) → cut `a` into `{b, a−b}`, the pair `{b,b}` is invisible, leaving
   `a−b`; *free-delete* an existing equal pair (0 cuts). Because IP applies to the **final**
   physical multiset, each op's set-aside equal pair is invisible regardless of later cuts.

3. **Physical-decomposition remark.** The physical final multiset is `P = E ⊎ (⋃_s {v_s,v_s})`,
   one equal pair per op, where `E` is the effective multiset. Applying IP once per pair gives
   `D(P) = D(E) ≤ (total of E)` (pairing form `D ≤ b₁ ≤ total`).

4. **Realizability Lemma (dyadic §4.7).** For any `ε ∈ {−1,0,+1}^m \ {0}`, Xiang using
   `≤ m−1` removal ops reaches an effective multiset of total exactly `|Σ_i ε_i ℓ_i|`.
   (Bisect the zero-coordinates; on the nonzero support repeatedly pin an opposite-signed pair
   / free-delete equal pairs, preserving the labelled signed sum.)
   **Equivalent form — Theorem R (euclid §D):** `min Reach(U) = m*_±(U) := min_{ε∈{±1}^U}|Σ ε_i x_i|`,
   the minimum all-signs sum is realizable by pinning `U` to a single coin in `|U|−1` pins.

5. **Subset-Sum Pigeonhole.** Among the `2^{n+1}` subset sums of an `(n+1)`-piece partition
   of `Σ`, two consecutive sorted values differ by `≤ Σ/(2^{n+1}−1) = u_n·Σ`. Their symmetric
   difference gives a nonzero `ε ∈ {−1,0,1}^{n+1}` with `|Σ ε_i ℓ_i| ≤ u_n·Σ`.

**Assembly.** Pick `ε` by the pigeonhole; realize it in `≤ n` ops (= `≤ n` cuts) by
Realizability; then `D = D(E) ≤ (total of E) = |Σ ε_i ℓ_i| ≤ u_n·Σ`. If `m ≤ n`, bisect
all pieces (`≤ n` cuts) for `D = 0`. Fewer Liu marks only remove Liu options.

## Sharpness

On Liu's dyadic partition `ℓ_i = 2^i u_n`, every nonzero `{−1,0,1}` combination has
`|Σ ε_i 2^i| ≥ 1`, so the minimal nonzero signed sum is exactly `u_n`; the pigeonhole
bound is attained with equality, matching the lower-bound target. So `u_n` is sharp.

## Independent verification (proof-reviewer, round 7)

- End-to-end simulation of the ACTUAL physical Xiang cut sequence (pigeonhole ε → realizability
  ops), exact `Fraction` arithmetic, random `(n+1)`-piece partitions, `n = 1..5`, 3000 each:
  true discrepancy `D(P) ≤ u_n` (worst ratio `0.9998`, tight at dyadic), `≤ n` cuts, mass
  conserved `= Σ`. 0 violations.
- Theorem R (`min Reach(U) = m*_±(U)`): 0 mismatches over 500 random multisets (`|U| ≤ 6`),
  exact arithmetic. (Note: the bound is `m*_±`, all-signs — NOT `m*` with zeros allowed.)

## No refuted move is used

The proof does NOT use "bisect the n largest," myopic per-cut greedy, "cut only the top
piece," or any fixed schedule (all refuted). It selects the globally optimal `{−1,0,1}`
pattern via pigeonhole and realizes it constructively — genuinely non-myopic.
