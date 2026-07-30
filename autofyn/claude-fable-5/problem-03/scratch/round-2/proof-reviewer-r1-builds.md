# Proof review — round 1 builds of imo-2026-03 (reviewed round 2)

Problem: stick game, `compute_and_prove`, answer_type `expression`. Conjectured answer across the field: **c(n) = 2^n/(2^{n+1}−1)** (matches n=1 hand proof 2/3; my independent n=2 outer-optimization grid is consistent with 4/7, ladder attains Δ = 1/7 exactly).

## Approach: discrepancy-halving

**Builder's recorded Status: partial — CORRECT, not an overclaim.** The file cleanly separates "proved" from "open" and its self-assessment survives adversarial review.

**Load-bearing step identified and independently re-derived: Theorem L (the complete lower bound).** This is the round's headline. I checked it three ways:

1. **Hand re-derivation of the tree/mass argument.** (a) Pairing identity (★): Δ = Σ consecutive-pair gaps, with the phantom 0 correctly converting a trailing +p_m — checked. (b) Edge/vertex count: m = n+1+C, C ≤ n; m even ⟹ m ≤ 2n ⟹ q = m/2 ≤ n < n+1 vertices; m odd ⟹ q = (m+1)/2 ≤ n+1 < n+2 vertices (with ⊥) — checked, including the parity step. (c) Since every component has #edges ≥ #vertices − 1 and totals give #edges < #vertices, a tree component T exists; deg ≥ 1 everywhere forces |T| ≥ 2 — checked (a single-vertex component would contradict its own vertex's positive degree; a loop makes edges ≥ vertices, so T is loop-free). (d) Partner argument: every fragment of the top-mass rung r of T pairs via an edge of T (edges incident to r lie in r's component) with a piece homed in T∖{r}; no partner is a fragment of r (loop), distinct fragments give distinct pairs hence distinct partners; Σ partners ≤ mass(T∖{r}) ≤ 2^0+⋯+2^{r−1} = 2^r − 1; so Σ(f_i − π(f_i)) ≥ 1 and Δ ≥ Σ gaps over those distinct pairs ≥ 1 (all other gaps ≥ 0) — checked. No integrality used; edge cases (C = 0, endpoint marks, ties in sorting, phantom) all handled.
2. **Numeric attack.** Nelder–Mead minimization of Δ over ALL cut allocations against the ladder, n = 1, 2, 3: minimum found is exactly u = 1/(2^{n+1}−1) every time, never below. The bound is sharp (mirror reply), so any slack would have shown.
3. **Supporting identities.** Identity 1, Identity 2 (threshold), Lemma 3 (tied-pair invariance): re-proved by hand; correct.

Minor blemish, not a gap: one garbled sentence in Step 3 ("distinct labels < ... distinct labels different from r") — the intended and correct statement is "every other vertex of T has smaller mass, hence is ⊥ or a rung k < r"; I wrote the clean version into the certified lemma file.

**Upper bound (Claim U(m)).** The reduction chain (zero-padding, the bisect/match/free-retire move process, Δ(final) = Δ(A_end) via tied-pair invariance, U(n+1) ⟹ c(n) ≤ 2^n/(2^{n+1}−1)) is rigorous. Case 1 (a₁ ≥ 2^{m−1}β) and Case 2 with a₁ > a₂ (a₂ ≥ 2^{m−2}β): algebra re-checked, correct. The file is admirably honest that Case 2's a₁ = a₂ tie sub-case and Case 3 (middle) are OPEN — and its own counterexample to the naive greedy is real: I verified by exhaustive move search that on (5,3,3,2)/13 greedy leaves 1/13 > β = 1/15 while the optimum is Δ = 0 (cut 5 → 3+2). U(m) itself passed an exhaustive-search check on 60 random integer multisets (m = 3..5): zero failures — the claim looks true, only unproven in the middle case.

**Scores.** Correctness: 10/10 (everything asserted as proved is proved). Completeness: 7/10 (upper-bound middle case + tie sub-case open). Progress: major — the entire lower bound of an IMO P3-level problem is closed and certified, and the whole problem is reduced to one clean finite claim, U(m) middle case.

**True Status: partial. Verdict: CHANGES REQUESTED.** Exact remaining gap: Claim U(m), Case 3 (a₁ < 2^{m−1}β, a₂ < 2^{m−2}β, m ≥ 3) plus the a₁ = a₂ branch of Case 2. Suggested attack (from the file, endorsed): the tail-min invariant Δ ≤ min_{1≤j≤m} T_j/(2^j−1) (T_j = sum of j smallest active pieces), equalized at the ladder and consistent with all numerics; or a lookahead match rule creating double ties. Nothing else stands between this approach and solved.

## Approach: tie-structure-variational

**Builder's recorded Status: partial — CORRECT.**

Verified claims:
- **Lemma G + Corollary R** (in `lemmas/greedy-claiming.md`): Sub-lemmas 1–2 re-derived (the termwise rank-comparison is exact: rank shifts by one across the deleted index, and counts of odd ranks match); Claims A/B induction sound; exactness from the two complementary guarantees. Brute-forced the game value on 200 random rational multisets with ties and zeros: perfect agreement. **CERTIFIED.**
- **Tie-Structure Lemma V1–V3 + Corollary V4**: checked V1's compactification (degenerate cuts ↔ zero sub-pieces ↔ fewer cuts, both inclusion directions), V2's cell decomposition (constant weak order per cell ⟹ f affine per cell; LP vertex principle; classification of active constraints into forms (i)–(iii) — the constant/identically-zero comparisons are correctly excluded from 𝒜*), V3's cut-count-minimality elimination of form (i) (the needed inequality min over smaller D_{m″} ≥ V(a) follows from the zero-cut padding embedding). Sound, and genuinely static — the cycling risk flagged at outline stage is gone. **CERTIFIED** as `lemmas/tie-structure.md`.
- **Lemma D** (layer-cake parity): correct; the ⌈N/2⌉ − N/2 = ½·1[odd] step checked; agrees with the sibling's Identity 1–2 (">" vs "≥" is a null set). Certified inside `lemmas/threshold-identity.md`.
- **Proposition M** (mirror-ladder value): rank bookkeeping re-checked by hand and in exact arithmetic for n = 1..8 — Liu gets exactly 2^n u. Correct.
- **§6, n = 1 end-to-end**: catalog enumeration for M ≤ 1 is exhaustive given V3; V(a) = min(a₁, 1 − a₁/2); outer max = 2/3 at (2/3, 1/3). Correct — c(1) = 2/3 fully proved by this route.
- Recorded dead ends (parity-XOR, integrality of pinned replies) are genuine and well-documented; the 4 → 4/3·3 counterexample is right.

**Scores.** Correctness: 10/10. Completeness: 5/10 (its own GAP M(a) is only closed via the sibling's certified ladder-resists; GAP C and GAP M(b) open). Progress: strong on infrastructure; weaker as a standalone route — its §8 self-assessment is candid that M(b) risks duplicating the induction casework.

**True Status: partial. Verdict: CHANGES REQUESTED** — with a routing note for the outline-reviewer: GAP M(a) is now moot (import `ladder-resists`); what remains proprietary to this slug is GAP C + GAP M(b). If those cannot advance beyond the siblings' framing next round, execute the fold-in its own §8 prescribes (retire the slug, keep the certified lemmas). Alternatively, its certified V4 catalog could serve the upper bound: a pinned-type route to U(m)'s middle case would be a genuinely different attack than the move-process induction.

## Not reviewed as a build

- **dyadic-recursion-induction** — outline-stage skeleton only (builder interrupted, no build report, file unchanged since 13:51). Not judged; no outcome recorded; its Elo stands.

## Lemma certifications (all held to the sorry-free bar)

- `lemmas/greedy-claiming.md` — **CERTIFIED** (stamp added to the file).
- `lemmas/threshold-identity.md` — **CERTIFIED**, created (Identities 1–2 + tied-pair invariance + zero-padding; merges both builders' equivalent derivations).
- `lemmas/ladder-resists.md` — **CERTIFIED**, created (Theorem L in full, cleaned prose; the entire lower bound, importable as a black box — it subsumes gaps G1 / GAP L / GAP M(a) across the field).
- `lemmas/tie-structure.md` — **CERTIFIED**, created (V1–V4 statement + proof pointer + the no-integrality caution).

## current.md

Created (reviewer-owned): Status **partial**; conjectured answer c(n) = 2^n/(2^{n+1}−1); lower bound proved and certified; problem reduced to Claim U(m) middle case + tie sub-case. No `## Full proof` (not solved).

## Outcomes recorded

- discrepancy-halving: `advanced` (round 1) — lower bound certified; single gap remains.
- tie-structure-variational: `advanced` (round 1) — infrastructure certified; own gaps overlap siblings.

## For next round

The single highest-value target in the field: **Claim U(m), middle case (+ a₁ = a₂ sub-case)** in discrepancy-halving. It is numerically true on every instance tested and would immediately finish the problem with answer c(n) = 2^n/(2^{n+1}−1).

verdict: discrepancy-halving = CHANGES REQUESTED
verdict: tie-structure-variational = CHANGES REQUESTED
