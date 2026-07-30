# proof-reviewer — IMO 2026 P3 (imo-2026-03) — round 1

Conjectured answer `c(n) = 2^n/(2^{n+1}−1)`. Three approaches reviewed:
`tail-count`, `d-potential`, `tower-induction`. All three self-report `partial` and flag
the lower-bound case (b) (top piece split) and the general upper bound as open. The review
confirms this: **none is solved; all three are `partial`**. The shared certified lemmas
(Lemma 0, case-a, n=1 base, layer-cake identity) are admitted to the lemma cache.

## Independent verification performed

- **Lemma 0 (greedy = odd-index):** verified by full minimax game-tree search on 300
  random multisets (sizes 2–6), 0 mismatches. The lemma is TRUE.
- **Sign error found in `tail-count`'s Lemma 0 proof** (see below). The *conclusion*
  is correct; the *displayed formula* is wrong. Fixable; the certified lemma file uses
  `tower-induction`'s sign-correct proof.
- **n=1 base (both bounds):** verified `c(1)=2/3` — tower resists all 1-mark refinements
  (lower), and Xiang's halve-if-dominant / mark-nothing strategy caps every 2-piece Liu
  config (upper). Rigorous.
- **Case (a) (top unsplit → `D ≥ 1/D_n`):** verified for n=2,3,4. Rigorous; no IH needed.
- **Lower bound case (b) numerics:** re-ran with the *correct* (n+1)-piece tower
  `(2^n,…,1)/D_n`. 0 violations over 300k random refinements for n=2; 80k for n=3,4.
  Min odd-index = `2^n/D_n` exactly, attained at the "balanced-pairs" equality config.
  (An earlier buggy run used a truncated tower missing the `1` piece and produced fake
  violations — the approaches themselves use the correct tower.)
- **Equality config** `{2^{n-1},2^{n-1},…,2,2,1,1,1}/D_n`: odd-index = `2^n/D_n` exactly,
  confirming the answer is at most the target against the tower (but only against the
  tower — not a general upper bound).

---

## Approach `tail-count` — CHANGES REQUESTED (Status: partial)

**What holds (certified):**
- Lemma 0 (greedy = odd-index) — the *lemma* is true, but the *proof as written in this
  file has a sign error*: it displays `T_1 − T_j = a_1 + (a_3−a_2) + (a_5−a_4) + …` and
  justifies nonnegativity by "a_{2i+1} ≥ a_{2i}". BOTH are wrong: the correct formula is
  `T_1 − T_j = (a_1−a_2) + (a_3−a_4) + … + (a_{j−2}−a_{j−1})`, and descending gives
  `a_{2i−1} ≥ a_{2i}` (not `a_{2i+1} ≥ a_{2i}`). The conclusion `T_1 ≥ T_j` is nevertheless
  correct (verified independently). The certified lemma file `claim-game-odd-index.md`
  uses `tower-induction`'s sign-correct proof instead.
- Lemma 1 (layer-cake identity) — correct (Tonelli). Certified.
- Corollary 2 (`D = ∫(N mod 2)dt`) — correct. Certified.
- Lemma L-a (top unsplit, case a) — correct, no IH. Certified.
- n=1 base (both bounds) — correct. Certified.

**Gaps (honestly flagged, not silently hand-waved):**
- (L-b) Lower bound case (b), top piece split: OPEN. The crude `D_R ≤ largest rest piece`
  bound degenerates in the balanced-split regime `q ≈ 2^{n−1}/D_n` exactly where the
  minimum is attained; the needed finer estimate is itself the lower-bound statement for a
  smaller tower with a parity twist. Verified n ≤ 6, no general proof.
- (U) Upper bound general n: OPEN. The per-threshold parity cap is blocked by coupling of
  `N(t) mod 2` across thresholds (one mark re-sorts globally and flips parities on a long
  range of `t`). Only n=1 proved.

**Overclaim check:** Status honestly `partial`; no "proved" overclaim on the open gaps.
The one defect is the sign error in the Lemma 0 write-up (a proof bug, not a false lemma).

**Outcome recorded:** verified-milestone (Lemma 0 [fixable sign error noted], layer-cake
identity, D-integral, case-a, n=1 base all certified and importable; case-b + general
upper bound open).

---

## Approach `d-potential` — CHANGES REQUESTED (Status: partial)

**What holds (certified):**
- Lemma 0 (greedy = odd-index) — correct (exchange/backward-induction). The "removing an
  element from a descending list never increases the even-index sum" sub-claim is slightly
  hand-wavy in justification but is TRUE (verified: for p even,
  `old_even − new_even = a_p − D(tail) ≥ a_p − a_{p+1} ≥ 0`; for p odd, unchanged). Certified
  via `tower-induction`'s cleaner proof.
- Lemma R (closed-form recursion `1/r_n = 1 + 1/(2 r_{n−1})`, `r_n = 2^n/(2^{n+1}−1)`) —
  pure algebra, correct. Certified as `closed-form-answer.md`.
- n=1 base (both bounds) — correct. Certified.
- Lower bound Case A (top unsplit) — correct and even simpler than the other two
  approaches' version: the top piece alone `= 2^n/D_n` occupies an odd slot, so Liu's
  odd-index take `≥ a_1 = 2^n/D_n` directly. Certified.

**Gaps (honestly flagged):**
- Lower bound Case B (top split): OPEN. Verified n=2,3 (200k random refinements), no
  general proof. The approach correctly identifies this as the shared lower-bound crux
  and notes the `tail-count` framing is better placed to resolve it.
- General upper bound (n≥2): OPEN. The potential programme is **conditional** — it shows
  *if* a `Φ ≥ D` exists with the per-mark decay `1/Φ' ≥ 2/Φ + 1`, then the upper bound
  follows. But **no concrete `Φ` is exhibited**, and the natural candidate `Φ = D` is
  shown to be **circular** (witness `T_1`: `D` stays `1/3` under the optimal mark, but
  `2/D+1 = 7`). The approach honestly admits weighted-sum candidates (`Σ 2^{−i} a_i`,
  `Σ a_i/(1+a_i)`) were tested and fail (P2). This is the research question itself, not a
  fixable slip.
- The `−1` in `2^{n+1}−1` is traced to the additive `+1` per round in the recursion, but
  this lives at the *game-value* level, not a per-config decay of `D`. Pinning it to a
  concrete `Φ` = closing gap 2.

**Overclaim check:** Status honestly `partial`. The conditional programme is clearly
labelled conditional; no `Φ` is claimed to exist. The circularity of `Φ=D` is flagged,
not hidden.

**Outcome recorded:** verified-milestone (Lemma 0, closed form, n=1 base, case-A
certified; `Φ` circular / no candidate exists, case-B + general upper bound open).

---

## Approach `tower-induction` — CHANGES REQUESTED (Status: partial)

**What holds (certified):**
- Lemma 0 (greedy = odd-index) — the **cleanest** of the three proofs (sign-correct
  throughout, both parities settled via `payoff_j − D(S) = −2 Σ(a_{2i−1}−a_{2i}) ≤ 0`).
  There is a mid-derivation "wait" self-correction in the j-even branch, but it resolves
  correctly. Certified (this is the proof used in `claim-game-odd-index.md`).
- Lower bound case (a) (top unsplit): rigorous, no IH, `D(M) = A − D(R') ≥ A − total(R') = 1/D_n`. Certified.
- Lower bound sub-case (b-i) (equal split of top, one mark): closed **conditionally** on
  the IH for `n−1`. The two equal fragments `f_1=f_2=A/2` occupy positions 1,2; rest fills
  positions 3,…; `D(M) = D(R')`, and by IH `D(R') ≥ 1/D_{n−1}` in `T_{n−1}` units `= 1/D_n`
  in `T_n` units. NOTE: this is conditional on the (unproved) lower bound for `n−1`, so it
  is NOT a standalone certified lemma — it is a reduction, correct as far as it goes.
- n=1 base (both bounds): rigorous. Certified.

**Gaps (honestly flagged):**
- Lower bound sub-case (b-ii) (unequal one-mark split of top): OPEN. The fragment
  `f_2 < A/2` interleaves with the refined rest in a way the self-similar IH does not
  control (the merge `f_2 ∪ R'` is not a refinement of a smaller tower). Verified for n=2.
- Lower bound sub-case (b-iii) (≥2 marks on top, ≥3 fragments): OPEN. Same interleaving
  crux, harder. Equality config confirmed numerically; proof open.
- Upper bound dominant case (n≥2): OPEN. The recurrence through `c(n−1)` does not factor
  cleanly (`1/c(n) = 2−2^{−n}` is not a clean function of `1/c(n−1)` via halving); halving
  `L` interleaves with the rest.
- Upper bound non-dominant case (n≥2): OPEN. "Mark nothing" is too weak for near-equal
  configs (odd-index ≈ 1/2 + small, gap `2^n/D_n − 1/2 = 1/(2D_n)` is tiny). The naive
  "always halve the largest" dead end is correctly NOT revived here.

**Overclaim check:** Status honestly `partial`. The "sign-budget identity"
`D(M) = 1/D_n + 2(O_{R'} − E_F)` is correctly noted to be *equivalent to the lower bound*
(a reformulation, not a shortcut) — good honesty. The equal-split sub-case is conditional
on the IH, which is itself open; not overclaimed.

**Outcome recorded:** verified-milestone (Lemma 0 cleanest proof, case-a, n=1 base
certified; equal-split sub-case (b-i) conditionally closed; case (b-ii)/(b-iii) + general
upper bound open).

---

## Promotable lemmas — certification summary

Admitted to `results/imo-2026-03/lemmas/` (all sorry-free, statements correct, no
stronger than proved):

1. `claim-game-odd-index.md` — Lemma 0 (using `tower-induction`'s sign-correct proof;
   `tail-count`'s write-up has a fixable sign error, noted in the lemma file).
2. `tower-top-unsplit.md` — case (a), lower bound, all n, no IH.
3. `n1-base-both-bounds.md` — `c(1)=2/3`.
4. `layer-cake-odd-index.md` — odd-index = `∫⌈N/2⌉dt`.
5. `D-equals-parity-integral.md` — `D = ∫(N mod 2)dt`.
6. `closed-form-answer.md` — algebraic recursion `r_n = 2^n/(2^{n+1}−1)` (identity about
   the candidate, not a proof of the game value).

**Rejected:** `tower-induction`'s equal-split sub-case (b-i) is NOT certified as a
standalone lemma — it depends on the (unproved) lower bound for `n−1` (the IH). It is a
correct *reduction* but not an unconditional result.

---

## Goal Progress

**Status: partial.** No approach is solved; the conjectured answer `c(n)=2^n/(2^{n+1}−1)`
is numerically solid (verified n=1..4, equality config attained) but the two load-bearing
gaps are open in all three approaches.

**Best proven result so far:**
- Lemma 0 (claim game = odd-index sum, greedy optimal) — fully proven.
- Lower bound case (a): the tower resists refinement whenever Xiang leaves the top piece
  unsplit, for all n, with no IH (`D ≥ 1/D_n`).
- n=1 base: `c(1) = 2/3` (both bounds).
- Layer-cake identity + `D = ∫(N mod 2)dt` (structural language).
- Closed form `r_n = 2^n/(2^{n+1}−1)` (algebraic identity for the candidate).

**#1 gap to attack next round:** the **lower-bound case (b)** — prove that when Xiang
*splits* the tower's top piece `2^n/D_n` (arbitrary fragmentation: huge-fragment-plus-scrap,
balanced split, or many small fragments), the alternating sum stays `D ≥ 1/D_n`. This is
the shared wall of `tower-induction` (case b-ii/b-iii) and `tail-count` (L-b); `d-potential`
defers to it. The equal-split sub-case is conditionally closed (on the IH); the
unequal/multi-split is the crux. The `tail-count` framing (parity handled by the ceiling
structurally, not by fragile sorted-list IH) is the best-placed route per the
outline-reviewer. **Secondary gap:** the general upper bound (no approach has a real Xiang
strategy beyond n=1; the parity-coupling obstruction in `tail-count`, the absent `Φ` in
`d-potential`, and the non-factoring recurrence in `tower-induction` are all genuinely
open).
