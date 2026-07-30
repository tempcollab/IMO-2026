# Proof Reviewer — Round 6 — IMO 2026 P3 (`imo-2026-03`)

Three approaches reviewed: `majorization-upper`, `even-packing-upper` (NEW), `tail-count`. Each independently. All three: **CHANGES REQUESTED** (partial) — real progress on each, but load-bearing gaps remain.

---

## 1. `majorization-upper` — CHANGES REQUESTED (partial)

### Headline claim: `halving-always-a-nplus1` — VERIFIED, CERTIFY

**Claim:** For ANY strictly-decreasing m=n+1 Liu config (a_1 > ... > a_{n+1}), halving a_1,...,a_n (n marks, leaving a_{n+1}) gives D = a_{n+1}. No bottom-dominance hypothesis.

**Independent verification:** 0 violations / 20000 exact-`Fraction` trials (n=2..6, random strictly-decreasing integer configs), INCLUDING 495 trials with edge case a_i = 2·a_{n+1}. Explicit edge-case configs (4,2,1)/7, (6,2,1)/9, (8,2,1)/11, (6,4,2,1), (10,4,2,1), (8,6,2,1), tower T_3, T_4, near-equal (100,99,98,97,96) — ALL give D = a_{n+1}. ✓

**Re-derivation of the proof (sound):**
1. Refined multiset: {a_1/2, a_1/2, ..., a_n/2, a_n/2, a_{n+1}} (2n+1 pieces). ✓
2. Strictly-decreasing ⟹ a_1/2 > ... > a_n/2 pairwise distinct. ✓
3. Every value v ≠ a_{n+1} appears exactly 2 times (even) — UNLESS a_i/2 = a_{n+1} (a_i = 2·a_{n+1}), in which case a_{n+1} appears 1+2 = 3 times. Strictly-decreasing ⟹ at most one such i. So a_{n+1} multiplicity is 1 (k=0) or 3 (k=1), both ODD. ✓
4. All blocks above the a_{n+1}-block are even-sized (all v ≠ a_{n+1} have even multiplicity) ⟹ sum of preceding pieces is EVEN ⟹ a_{n+1}-block starts at position 1+even = ODD. ✓ (This holds regardless of WHERE a_{n+1} sits in the sorted order — blocks below it don't affect its starting position.)
5. Block-contribution formula (certified): even block contributes 0; odd block (2k+1) at odd start contributes +v. ✓ (Independently verified: size-3 at odd positions gives +v, size-2 at any position gives 0.)
6. D = 0 + a_{n+1} = a_{n+1}. ✓

**Edge case a_i = 2·a_{n+1} handled explicitly:** multiplicity 3 (odd), size-3 block at odd start: 2 plus-signs, 1 minus-sign, net +1·a_{n+1}. ✓ Verified on (4,2,1)/7 (a_2=2=2·1), (6,2,1)/9, etc.

**The bottom-dominance hypothesis IS unnecessary** — the block-grouping argument works on any sorted order, not just the "adjacent-pair" presentation of the round-5 proof. This generalizes `bottom-dominant-halving`.

### Corollary: region closure (a_{n+1} ≤ 1/D_n CLOSED for all n)

D* ≤ a_{n+1} for ALL strictly-decreasing m=n+1 configs ⟹ whenever a_{n+1} ≤ 1/D_n, halving gives D = a_{n+1} ≤ 1/D_n directly. ✓ This closes the a_{n+1} ≤ 1/D_n region unconditionally for all n, regardless of bottom-dominance. This is a genuine advance — it subsumes the non-bottom-dominant sub-case (a) of GAP-U2 whenever a_{n+1} ≤ 1/D_n, and narrows GAP-U2 to ONLY the compressed case (a_{n+1} > 1/D_n).

### O1 (split-bottom + exact-pair-rest) — DEAD (confirmed)

The outline-reviewer proved exact pairing is IMPOSSIBLE for (5,3,2)/10 (n=2) for ALL x ∈ (0, 1/D_n] and all 9 split/pairing patterns. The "pairing feasibility as a PL function of x" is a category error (discrete 0/1 indicator, IVT cannot apply). The builder correctly drops O1 and does not retry it. ✓

### GAP-U2-compressed (OPEN, honestly flagged)

The compressed case (a_{n+1} > 1/D_n, strictly-decreasing m=n+1) remains open. The halving bound D = a_{n+1} > 1/D_n overshoots. O2 (split-LARGE-to-match-MEDIUM) and bounded-spread pigeonhole are honest candidate mechanisms, both bottoming on the same unproved subset-sum/piece-matching existence. Verification (0 violations over 6000+ trials n=4, exhaustive n=2) supports the claim but is verification-not-proof. The parity obstruction (2n+1 odd ⟹ D ≠ 0 with n marks) is correctly noted — the compressed case can only yield D = small leftover ≤ 1/D_n, never D = 0 via n marks. ✓

**No overclaims found.** The builder correctly distinguishes "proved" (halving lemma, region closure) from "conjecture/verification" (compressed case). The Status is `partial` and matches reality.

### Scores
- Correctness: 9/10 (halving lemma proof sound; O1 dead correctly; gap honestly flagged)
- Completeness: 7/10 (region closure is real; compressed case open)
- Progress: 8/10 (closes a_{n+1} ≤ 1/D_n for all n — a genuine narrowing of GAP-U2)

### Verdict: CHANGES REQUESTED (partial). The halving lemma is a certifiable milestone; GAP-U2-compressed remains open.

---

## 2. `even-packing-upper` — CHANGES REQUESTED (partial, NEW)

### Claim 1: Even-position reframe (D = 1 − 2E) — CORRECT, CERTIFY

D = O − E, O + E = T = 1 ⟹ D = 1 − 2E, E = (1−D)/2. Xiang minimizes D ⟺ maximizes E. The upper bound D* ≤ 1/D_n ⟺ E* ≥ (2^n−1)/D_n. Trivially correct from Lemma 0 and total = 1. ✓

### Claim 2: Tower tightness E*(T_n) = (2^n−1)/D_n "PROVED both directions" — OVERCLAIM on lower direction

**Upper direction (halving packs E ≥ (2^n−1)/D_n):** CORRECT. By `parallel-halving-saturates-tower`, D(halving) = 1/D_n against T_n, so E = (1−1/D_n)/2 = (2^n−1)/D_n. Verified for n=1..5. ✓

**Lower direction (Xiang cannot pack E > (2^n−1)/D_n against T_n):** NOT PROVED. This requires D*(T_n) ≥ 1/D_n — the TOWER LOWER BOUND. The builder claims "the certified dyadic lower bound ... establishes that against T_n, EVERY ≤ n-mark Xiang refinement gives D ≥ 1/D_n" and "for the TOWER specifically the lower bound D(T_n) ≥ 1/D_n is certified closed." **This is FALSE.** GAP-C (non-dyadic multi-split k≥3 breakpoints of T_n) is the OPEN gap in the tower lower bound — it is the main open problem on the lower side, documented extensively in `tail-count` and `current.md`. The builder conflates "the lower bound for T_n" (which IS GAP-C, open) with a hypothetical "certified closed" status. The parenthetical "the tower's self-similar structure forces D ≥ 1 at every breakpoint" is the unproved GAP-C(i) claim, not a certified result.

**Impact:** The "E*(T_n) = (2^n−1)/D_n exactly" and "equivalently D*(T_n) = 1/D_n" statements are only HALF-proved (upper direction only). The lower direction is GAP-C-open. This overclaim must be corrected. However, it does NOT affect the upper bound approach's main correctness — the upper bound only needs D* ≤ 1/D_n (the upper direction), not equality.

### Claim 3: `halving-underpacks-compressed` — CORRECT, CERTIFY

By `halving-always-a-nplus1` (certified this round), halving gives D = a_{n+1}, so E_halve = (1−a_{n+1})/2. In the compressed case (a_{n+1} > 1/D_n), E_halve < (1−1/D_n)/2 = (2^n−1)/D_n. Verified for n=2..5. ✓ This correctly explains why halving closes the a_{n+1} ≤ 1/D_n region but not the compressed region.

### Claim 4: GAP-U2-packing ⟺ GAP-U2-compressed — CORRECT but a RESTATE

The equivalence E* ≥ (2^n−1)/D_n ⟺ D* ≤ 1/D_n is trivial algebra (E = (1−D)/2). The "mechanism" (exhibit marks creating ties/pairings with small leftover) is IDENTICAL to GAP-U2-compressed. The builder honestly acknowledges: "the even-packing lens REFRAMES the crux as a packing-density question but does NOT bypass it: the load-bearing step is the same piece-matching / tie-creation existence." The outline-reviewer correctly flagged this. The even-packing lens is a REFRAME, not a genuinely different mechanism.

### Verification table (Part IV) — CORRECT

Spot-checked (5,3,2)/10 (n=2): D* = 0 IS achievable using 1 mark (split a_1=1/2 → {3/10, 1/5}, refined = {3/10, 3/10, 1/5, 1/5}, D = 0, 4 pieces even count). The parity obstruction only applies with exactly n marks (2n+1 odd); using ≤ n−1 marks gives even count, D = 0 possible. The outline-reviewer's D = 1/1750 was for a different (suboptimal) 2-mark strategy. The table is correct. ✓

### Assessment of genuine-difference

The even-packing approach is essentially a RESTATE of `majorization-upper`'s results in E-language. The reframe is trivial. The diagnostic follows from the halving lemma. The tower tightness upper direction is `parallel-halving-saturates-tower` restated. GAP-U2-packing is GAP-U2-compressed restated. The only new insight is the diagnostic (why halving fails for compressed configs), which is a minor restatement. The scaffolding lemmas are correct but thin.

### Scores
- Correctness: 7/10 (reframe + diagnostic correct; tower tightness lower direction OVERCLAIMED)
- Completeness: 5/10 (core gap is a restate of GAP-U2-compressed; no genuinely new attack)
- Progress: 4/10 (reframe + diagnostic are minor scaffolding; no advance on the crux)

### Verdict: CHANGES REQUESTED (partial). Reframe and diagnostic are sound scaffolding; tower tightness lower direction must be downgraded to "upper direction only, lower direction = GAP-C-open"; the core gap is a restate of GAP-U2-compressed.

---

## 3. `tail-count` — CHANGES REQUESTED (partial)

### Headline claim: Mass-budget breakpoint inequality T ≥ 3F − 1 — VERIFIED, CERTIFY

**Claim:** At a breakpoint of T_n (cascade type, all n marks split top 2^n), T ≥ 3F − 1 where F = surviving non-dyadic fragment mass, T = surviving tower mass.

**Independent re-derivation (sound):**
1. Top mass 2^n partitioned among fragments. At a breakpoint, every fragment value appears ≥ 2 times. ✓
2. Surviving non-dyadic values w_i (odd count ≥ 3): each consumes c_{w_i}·w_i ≥ 3w_i. Total ≥ 3F. ✓ (Non-dyadic values can only tie other top fragments — tower pieces are all powers of 2.) ✓
3. Non-surviving non-dyadic (even count ≥ 2): consume ≥ 0. ✓
4. Dyadic values 2^k appearing d_k times: consume d_k·2^k. For d_k odd (≥1): 2^k not in spine (count 1+d_k even), contributes d_k·2^k ≥ 2^k. For d_k even (≥0): 2^k in spine, contributes ≥ 0. So Σ d_k·2^k ≥ (2^n−1) − T (non-surviving tower mass). ✓
5. Total: 2^n ≥ 3F + (2^n−1) − T ⟹ T ≥ 3F − 1. ✓

**Verification:** 0 violations across all T_3 cascade breakpoints (1/24 grid, 58 unique breakpoints). Tightness examples match: {7/3,7/3,7/3,1} gives T=6=3·(7/3)−1 (tight); {4/3,4/3,4/3,4} gives T=3=3·(4/3)−1 (tight). ✓

### Corollary 15a (block condition sufficiency) — CORRECT as conditional

Block condition (all F at +) + D=1 ⟹ F=T+1 ⟹ T ≥ 3(T+1)−1 = 3T+2 ⟹ T ≤ −1, contradiction ⟹ F=0 (spine dyadic, D≥1 by §8). ✓ Correct as a CONDITIONAL result (conditional on the block condition).

### Corollary 15b (continuity rules out "all F at −") — CORRECT

If block condition holds with all fragments at − on an adjacent cell, D = 2S_+ − D_n ≤ 2(2^n−1) − D_n = −1 on that cell. A cell with D ≤ −1 on its interior cannot have D = 1 at its boundary vertex by PL continuity. ✓

### Does it advance "balance ⟹ block"? — NO, not directly

The mass-budget inequality constrains MAGNITUDES (T vs F) but not SIGNS. The "balance ⟹ block" step (from S_+ = 2^n to all-fragments-at-+) is about the sign assignment, which the mass-budget doesn't address. The inequality narrows the search space (any counterexample must have F > 0 AND block condition failing) but doesn't bridge the gap. The builder honestly acknowledges: "The step we CANNOT prove: at a D=1 breakpoint, the block condition holds on (at least one) adjacent cell."

### 0/523 block-condition verification — CORRECTLY classified

The round-5 "failures" were a misclassification bug (classifying by value-type: power-of-2 vs not, instead of by ORIGIN: fragment of top 2^n vs tower piece below). A fragment of the top can be a power of 2 (e.g., 4 from splitting 8→4+4); value-type classification would misclassify it as a "tower piece." The round-6 origin-based classification is the CORRECT one. I verified: 0 block-condition failures at all D=1 breakpoints found (1/24 grid, T_3 cascade). The 0/523 across T_3/T_4/T_5 (from the explorer's corrected script) is a verification result, honestly labeled as such.

### Outline-reviewer flag: superincreasing mechanism insufficient — CONFIRMED

The outline-reviewer correctly flagged that bare superincreasing (2^k > sum of smaller 2^j) constrains tower-vs-tower only, not fragment-vs-tower. The mass-budget inequality does NOT use superincreasing — it uses the breakpoint structure (each non-dyadic fragment must tie another, forcing ≥ 2 copies, ≥ 3 for survivors) and mass counting. This is a genuinely different mechanism from superincreasing, but it still doesn't close the gap.

### F > 0 ⟹ D > 1 — verified

Across all T_3 breakpoints found, whenever F > 0, D > 1 always (minimum D = 5/3 at {4/3,4/3,4/3,4}). No counterexample with F > 0 and D ≤ 1. ✓ (But this is verification-not-proof.)

### Scores
- Correctness: 9/10 (mass-budget inequality proof sound; corollaries correct; circularity honestly flagged)
- Completeness: 6/10 (narrows GAP-C(i) but doesn't close it; "balance ⟹ block" still open)
- Progress: 5/10 (new certified constraint, but the core gap is unchanged)

### Verdict: CHANGES REQUESTED (partial). The mass-budget inequality is a genuine new certified constraint; GAP-C(i)-balance-implies-block remains open.

---

## Lemma certifications

### CERTIFY (4 new lemmas, total 35):

32. **`halving-always-a-nplus1`** (`majorization-upper`, Part IV-bis) — For ANY strictly-decreasing m=n+1 config, halving a_1..a_n gives D = a_{n+1}. Proved (parity/block-grouping, edge case a_i=2·a_{n+1} handled). Generalizes `bottom-dominant-halving`. Closes a_{n+1} ≤ 1/D_n for all n. Verified 0/20000.

33. **`even-position-reframe`** (`even-packing-upper`, Part I) — D = 1−2E, E = even-position sum; Xiang minimizes D ⟺ maximizes E. Upper bound D* ≤ 1/D_n ⟺ E* ≥ (2^n−1)/D_n. Trivially correct from Lemma 0.

34. **`halving-underpacks-compressed`** (`even-packing-upper`, Part III-A) — Halving gives E_halve = (1−a_{n+1})/2; in compressed case (a_{n+1} > 1/D_n), E_halve < (2^n−1)/D_n. Follows from `halving-always-a-nplus1`. Diagnostic.

35. **`mass-budget-breakpoint-inequality`** (`tail-count`, §15) — At a breakpoint of T_n (cascade type), T ≥ 3F−1. Proved (mass budget: each non-dyadic survivor appears ≥ 3 times). Corollary: block condition + D=1 ⟹ F=0. Honest caveat: constrains F but doesn't prove block condition without it.

### REJECT:

- **`tower-even-packing-tight`** (`even-packing-upper`, Part II) — REJECTED as stated. The builder claims "E*(T_n) = (2^n−1)/D_n PROVED both directions." The UPPER direction is correct (halving achieves it, = `parallel-halving-saturates-tower` restated). The LOWER direction (E*(T_n) ≤ (2^n−1)/D_n) requires D*(T_n) ≥ 1/D_n = the TOWER LOWER BOUND, which is GAP-C-OPEN. The claim "for the TOWER specifically the lower bound D(T_n) ≥ 1/D_n is certified closed" is FALSE. Reject the lemma as stated; the upper direction is already covered by `parallel-halving-saturates-tower`.

---

## Overall assessment

Round 6 produced one genuine certifiable milestone (`halving-always-a-nplus1`, closing the a_{n+1} ≤ 1/D_n region for all n) and one genuine new constraint (`mass-budget-breakpoint-inequality`, narrowing GAP-C(i)). The even-packing approach is a clean reframe but its core gap is a restate of GAP-U2-compressed, and its tower-tightness lower direction is overclaimed. Two walls remain:
- **Lower (GAP-C/G1):** narrowed but not closed — the mass-budget inequality constrains F but doesn't force the block condition.
- **Upper (GAP-U2-compressed):** narrowed to the compressed case (a_{n+1} > 1/D_n) — O1 dead, O2/bounded-spread open, no proof.

A solve needs BOTH closed. Neither is close to closing this round.
