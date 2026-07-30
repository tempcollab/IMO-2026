# Build report — tie-structure-variational (imo-2026-03, round 1)

Status written to approach file: **partial**.
File: `results/imo-2026-03/approaches/tie-structure-variational.md`
Shared lemma written (lemmas dir was empty when I checked at 13:58 UTC): `results/imo-2026-03/lemmas/greedy-claiming.md` — full proof of the claiming-game value (odd-rank sum, via two termwise sub-lemmas + induction) and the multiset/Stackelberg reduction. Siblings should import, not re-prove. If a sibling raced me and the reviewer prefers their version, either is fine — certify one.

## What got proved this round (all in full rigor)

1. **Lemma G + Corollary R** (greedy claiming + reduction) — in `lemmas/greedy-claiming.md`.
2. **GAP T closed, and strengthened.** Replaced the outlined slide-to-tie iteration (cycling risk the outline-reviewer flagged) with a static LP/vertex argument: Xiang's value is affine on the cells of the tie-hyperplane arrangement; a minimizer exists at a cell vertex; with cut-count minimal among minimizers, ALL cuts are simultaneously pinned by Σm_j linearly independent equations of the forms "sub-piece = sub-piece" / "sub-piece = uncut piece", all sub-pieces positive (Lemmas V1–V3, Corollary V4 in §2–§3). No monovariant needed — nothing moves, nothing cycles. Degenerate/boundary replies are first-class: handled by the compactification (V1) and eliminated at the minimizer by cut-count minimality (V3).
3. **Layer-cake parity identity** (§4): Liu = 1/2 + Δ/2 with Δ = λ{t : #(pieces ≥ t) odd}. Independent derivation of the sibling's discrepancy identity; verified in exact arithmetic on 200 random multisets (check only).
4. **Mirror-ladder value** (§5): exact rank-by-rank computation, all n ≥ 1 (n = 1 case separate): the dyadic ladder concedes exactly 2^n/(2^{n+1}−1), so V(a*) ≤ c(n).
5. **n = 1 solved end-to-end through the pipeline** (§6): catalog for M ≤ 1 enumerated exhaustively from V3, V(a) = min(a₁, 1 − a₁/2), outer max gives c(1) = 2/3 — both bounds, fully rigorous, validating the framing.

## Remaining gaps (named in the file)

- **GAP C**: explicit, recursively organized enumeration of feasible pinned types for general n (finiteness is proved — V4; organization is not).
- **GAP M(a)**: ladder lower bound V(a*) ≥ c(n) — every pinned reply against the ladder gives ≥ 2^n u. Open. Recorded failed routes: parity-XOR induction on the top rung (the mirror reply's cancellation is exactly tight, no termwise bound); integrality of pinned sub-pieces (FALSE — 4 → 4/3·3 counterexample).
- **GAP M(b)**: outer bound V(a) ≤ c(n) for all a. Open, and confirmed to sit close to the induction sibling's A–D casework — per the kill criterion I did NOT duplicate that casework.

## Overlap / kill-criterion assessment (reviewer, please weigh in)

Not declaring dead-end yet: the round's genuinely variational asset — the Tie-Structure Lemma V2/V3 — is exactly what the siblings' lower-bound gaps (dyadic-recursion G1, discrepancy-halving GAP L) lack: it reduces "all Xiang replies against the ladder" to "pinned tie-system replies", for every partition, statically. Recommend certifying V2/V3 and Lemma D as field infrastructure regardless of this slug's fate. If next round §7a hits the same wall as G1/GAP L and §7b is only executable as the induction's casework, fold this slug into the siblings (donating V2/V3, Lemma D, Prop M) and retire it.

Spec concerns: none.
