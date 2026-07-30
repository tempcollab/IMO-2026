# math-explorer (upper-maxbound lens) — IMO 2026 P3, round 4

**Route:** the Max-bound crux `a_1 < 2a_2 ∧ a_3 > a_1/2` and the two-variable IH. All numbers exact-`Fraction`-verified unless noted.

---

## HEADLINE FIND: the Max-bound conjecture `D* ≤ M/2^n` is FALSE

The round-3 conjecture `D* ≤ M/2^n` (M = a_1, the largest piece), which the `majorization-upper` slug built its whole spine on, is **falsified** by an exact-`Fraction`-verified counterexample:

> **Config `(7,6,5,3)/21`** (n=3): `D* = 1/21 ≈ 0.047619`, `M/8 = (7/21)/8 = 1/24 ≈ 0.041667`. **Ratio = 8/7 ≈ 1.1429.** VIOLATION (exact).

This config is squarely in the crux regime: `a_1 = 7/21 < 2·(6/21) = 12/21` ✓ and `a_3 = 5/21 > (7/21)/2 = 3.5/21` ✓. The breakpoint-justified optimizer (Lemma B1) with exact `Fraction` arithmetic confirms `D* = 1/21` (achieved by pairing all three large pieces against each other: split `a_1 → {5/21, 2/21}`, split `a_2 → {5/21, 1/21}`, split `a_3 → {1/7, 2/21}`; three canceling pairs `5/21, 1/7, 2/21` at positions 1-6, residual `1/21 = a_1 - a_2` at position 7).

**A whole family** of violations exists (11 found by integer-partition scan, D=8..80, all exact-verified):
- `(7,6,5,3)/21`: ratio 8/7 (cleanest, smallest denominator)
- `(22,19,16,10)/67`: ratio 12/11
- `(15,13,11,6)/45`: ratio 16/15
- `(23,20,17,11)/71`: ratio 23/22

The pattern: configs `(p, q, r, s)/D` with `p, q, r` forming a near-arithmetic-progression and `s` small. The violation ratio is `D/s` or similar; it is **bounded** (worst 8/7) but real.

**CRUCIALLY: the actual upper-bound target `D* ≤ 1/D_n = 1/15 ≈ 0.0667` is NOT violated by any of these.** `D* = 1/21 = 0.0476 < 0.0667 = 1/15`. So the answer `c(n) = 2^n/(2^{n+1}-1)` is still correct; only the Max-bound *conjecture* (a sufficient but not necessary lemma) is wrong. The Max-bound overshoots the target by exactly the margin that makes it false.

**Implication for `majorization-upper`:** the MB-Dom (dominant case) reduction is still valid (it only uses pairing + the IH, and dominant configs don't produce the violation). But MB-Pair and the whole `D* ≤ M/2^n` framing must be **replaced**. The two-variable IH `f(M, M_2, n)` candidate from round 3 is the right path, with the explicit form identified below.

---

## THE REPLACEMENT: `V(n) = M_2 / 2^{n-1}` (second-largest-piece bound)

> **Conjecture V(n).** *For every n ≥ 1 and every multiset `L = (a_1 ≥ a_2 ≥ … ≥ a_m)` of positive reals (any m ≥ 2), Xiang has ≤ n marks with `D* ≤ M_2 / 2^{n-1}`, where `M_2 = a_2` is the second-largest piece.*

**Evidence (exact + float, breakpoint-justified optimizer, Lemma B1):**
- n=3: 0 violations over 800+ configs (400 random + 300 crux + known Max-bound violators + tower). Worst ratio 0.889.
- n=4: 0 violations over 60 random + 40 crux. Worst ratio 0.46.
- n=5: 0 violations over 20 random. Worst ratio 0 (trivial for small m).
- **TIGHT at the tower `T_n`**: `M_2(T_n) = 2^{n-1}/D_n`, so `M_2/2^{n-1} = (2^{n-1}/D_n)/2^{n-1} = 1/D_n = target`. Ratio exactly 1.000 at n=3,4,5. **The tower is the unique equality case** (same as Max-bound was).

**Why V(n) is the right replacement for Max-bound:**
- Max-bound `M/2^n` fails because `a_1` (the largest) can be close to `a_2` (crux), making `a_1/2^n` too small.
- V(n) uses `a_2` (the second-largest), which is always ≤ `a_1` but still captures the tower exactly.
- After Xiang's pairing move `a_1 → {a_2, a_1-a_2}` (two copies of `a_2` cancel at positions 1,2), the rest has max `a_3 ≤ a_2 = M_2`. So `V(n) ≤ Max-bound(n-1)` applied to the rest — V(n) is **weaker** than the Max-bound at the lower level, which is why it survives where the Max-bound fails.

---

## V(n) + certified factorization = FULL UPPER BOUND

The key closure: V(n) combined with the certified above-threshold factorization (regimes A/B1, round-2 reductions U2/U3) closes the full upper bound `D* ≤ 1/D_n`:

- **Above-threshold** (`M ≥ 2^n/D_n`): certified factorization U2 (dominant, halving) / U3 (non-dominant, pairing). `D* ≤ 1/D_n`. CLOSED (conditional on `W(n-1)`, the `(n-1)`-target IH — which V provides).
- **Below-threshold** (`M < 2^n/D_n`):
  - If `a_2 ≥ 2^{n-1}/D_n`: this is regime B1 (non-dominant above the `a_2`-threshold). Certified factorization U3. `D* ≤ 1/D_n`. CLOSED.
  - If `a_2 < 2^{n-1}/D_n`: V(n) gives `D* ≤ M_2/2^{n-1} < (2^{n-1}/D_n)/2^{n-1} = 1/D_n`. **STRICT.** CLOSED.

So V(n) only needs to be **proved for below-threshold configs with `a_2 < 2^{n-1}/D_n`** (small second-largest). In this regime, `a_2` is small, so the rest after pairing has small max and the IH is closer to closing (though the simple pairing IH still overshoots — see below).

**V(n) is piece-count-free** (same as Max-bound was): any multiset with second-largest `M_2`, any piece count.

---

## The inductive structure of V(n) — what works and what doesn't

**V(3) is PROVABLE from the certified n=2 Max-bound.** Pair `a_1 → {a_2, a_1-a_2}` (1 mark, two `a_2`'s cancel at positions 1,2). The rest `rest' = {a_3, a_4, …, a_1-a_2}` has max `a_3 ≤ M_2`. Apply the **certified n=2 bound** (`n2-upper-bound-complete`, which proves the Max-bound `D* ≤ max/4` for n=2): `D(rest', 2 marks) ≤ a_3/4 ≤ M_2/4 = V(3)`. ✓ This is rigorous for n=3.

**V(n) for n ≥ 4: the simple pairing IH does NOT close.** The natural induction `V(n) ← V(n-1)` via pairing fails:
- After pairing, `rest'` second-largest `M_2(rest') = max(a_4, a_1-a_2)`.
- Need `M_2(rest')/2^{n-2} ≤ M_2/2^{n-1}`, i.e. `M_2(rest') ≤ M_2/2`.
- This fails in 37% of crux configs (e.g. `a_1-a_2 > a_2/2` when `a_1 > 3a_2/2`, or `a_4 > a_2/2`).
- When it fails, the V(n-1) bound on the rest OVERSHOOTS the V(n) target.
- But the **actual** `D(rest', n-1 marks)` is well below the V(n) target (worst ratio 0.71 when the IH condition fails). The slack is real; the IH can't see it.

**2-mark IH also fails:** pairing `a_1` and `a_3` (2 marks, reduce to n-2 game) gives worst ratio 2.70 (much worse). The pairing cascade is suboptimal for the IH.

**The actual optimal Xiang strategy in the crux** (traced for `(7,6,5,3)/21` and the other violators) is a **3-mark pairing cascade**: pair `a_1` against `a_3`, pair `a_2` against `a_3`, then split `a_3` — creating three canceling pairs and leaving residual `= a_1 - a_2`. The residual is always `a_1 - a_2` in these worst cases, which is bounded by `M_2` (since `a_1 - a_2 < a_2` in the non-dominant case). But formalizing this cascade as a clean induction is the open step.

---

## Candidate forms for the two-variable IH — full scan results

Tested 17 candidate forms `f(M, M_2, a_3, n)` over 400+ configs (n=3, random + crux + known violators + tower). Results (0 violations = bound holds; tower ratio = f at tower vs target 1/D_n):

| candidate | violations | worst ratio | tower ratio | notes |
|---|---|---|---|---|
| **`M_2/2^{n-1}`** | **0** | 0.889 | **1.000** | **WINNER** — tight at tower, holds everywhere |
| `(M+M_2)/2^n` | 0 | 0.667 | 0.667 | holds but loose at tower |
| `(2M-M_2)/2^n` | 0 | 0.852 | 0.667 | holds but loose at tower |
| `max(M/2^n, M-M_2)` | 0 | 0.838 | 0.250 | holds but very loose at tower |
| `(M-M_2)+M_2/2^n` | 0 | 0.571 | 0.300 | holds, loose |
| `M/2^n` (Max-bound) | **1+** | 1.143 | 1.000 | **FALSE** (the killed conjecture) |
| `(M-M_2)/2^{n-2}` | 47 | 2.000 | — | fails badly |
| `max(M/2^n, (M-M_2)/2^{n-2})` | 1 | 1.143 | — | fails (includes Max-bound) |

**`V(n) = M_2/2^{n-1}` is the unique clean form** that is both tight at the tower (ratio 1.000) and has 0 violations. No other tested form achieves both.

---

## Optimal Xiang move in the crux (traced)

For the worst crux configs, the optimal 3-mark strategy (n=3) is:
1. Split `a_1 → {a_3, a_1-a_3}` (fragment matches `a_3`)
2. Split `a_2 → {a_3, a_2-a_3}` (second copy of `a_3`)
3. Split the original `a_3 → {a_4, a_3-a_4}` (or halve, or match another piece)

Result: three canceling pairs `a_3, a_4, (a_1-a_3+a_2-a_3)` at positions 1-6, residual at position 7. For `(7,6,5,3)/21`: residual = `1/21 = a_1 - a_2`. The residual is always small (bounded by `a_1 - a_2 < a_2 = M_2`).

**No single fixed move achieves the bound** (confirmed round-3 finding): sometimes pair, sometimes halve, depending on the ratio vector. The move is adaptive.

---

## Alternative framings orthogonal to Max-bound (scouted)

1. **Direct residual characterization:** `D* = (sum of unpaired residuals after optimal pairing)`. The residual is governed by `a_1 - a_2` in the crux, and `a_1 - a_2 < M_2`. This is the `D = ∫(N(t) mod 2)dt` picture (the `D-equals-parity-integral` lemma). The crux asks to prove the unpaired-interval measure ≤ `M_2/2^{n-1}`. This is a **measure-theoretic** framing that escapes the single-IH-overshoot problem — but it requires characterizing the optimal pairing globally, which is hard.

2. **Mutual recursion `W(n) + V(n)`:** W(n) = Max-bound for DOMINANT configs (proved, MB-Dom). V(n) = M_2-bound for ALL configs (conjecture). V(n) ← W(n-1) when the rest after pairing is dominant (50% of crux cases); V(n) ← V(n-1) when non-dominant (the failing 50%). The mutual recursion closes the dominant-rest cases; the non-dominant-rest cases need either a 2-level step or a direct argument. This is the cleanest formal structure.

3. **Min-max LP dual:** the game is a zero-sum game; `D*` is the value. The dual would be a fractional covering/packing on the piece-structure. Not developed — the LP would be infinite-dimensional (continuous marks), but the breakpoint structure (Lemma B1) discretizes it. Potential escape from the IH overshoot, but not scouted deeply.

---

## Distinct openings (for the outliner)

1. **Replace Max-bound with V(n) = M_2/2^{n-1}** in `majorization-upper`. Prove V(3) from the certified n=2 bound (rigorous). Mark V(n≥4) as a conjecture with the mutual W/V recursion as the inductive structure. The closure V(n) + certified factorization = full upper bound is clean.

2. **Prove V(n) via the mutual recursion `W(n) + V(n)`**: W(n) for dominant (proved MB-Dom), V(n) for all. The hard step: when the rest after pairing is non-dominant, prove V(n) ← V(n-1) closes. Numerics say the actual D(rest) is 0.71x the V(n) target even when the IH condition fails — the slack is there but the IH misses it. Attack via a 2-level step or a direct residual bound.

3. **Direct residual-integral attack**: `D = ∫(N(t) mod 2)dt`. Prove the unpaired measure ≤ `M_2/2^{n-1}` directly, bypassing the IH entirely. The breakpoint structure (B1) makes this a finite combinatorial problem.

4. **Characterize the optimal pairing cascade**: in the crux, Xiang pairs the 3 large pieces against each other (3 marks), leaving residual `= a_1 - a_2 ≤ M_2`. Formalize: after pairing all pieces ≥ M_2/2 against each other, the residual is bounded. This is a **pairing/matching** argument on the top pieces, not a recursive IH.

---

## Cheap-kill candidates

- **m ≤ 3 crux at n=3:** Xiang drives D to 0 (3 marks, halve each piece — verified exactly). So the crux is only hard for m ≥ 4 (tail after top-3). This is a **size reduction**: configs with `m ≤ n` and all pieces ≥ M/2 are trivial (halve each, D=0). The hard configs have a tail of small pieces.
- **The Max-bound violators are all near-tower**: `(7,6,5,3)/21 ≈ T_3/1.4` — they are close to the tower in structure. The violation is small (ratio 8/7). This suggests the bound can be patched with a small correction term.

---

## Knowledge-base entries to use

- `n2-upper-bound-complete` (certified n=2 Max-bound — the BASE for V(3))
- `pl-breakpoint-minimum` (B1 — justifies breakpoint-only optimizer)
- `claim-game-odd-index` (Lemma 0)
- `D-equals-parity-integral` (residual-integral framing for the direct attack)
- `parallel-halving-saturates-tower` (equality witness — V is tight at tower)
- `frontier-recursion` (tower closed form, verifies tower ratio = 1.000)
- MB-Dom (`max-bound-dominant`, REDUCTION) — the dominant-case W(n), still valid

## Analogous past problems (cruxes)

Not searched this round (focused on numerics). The structure is game-theoretic (alternating draft + adaptive refinement), unusual for the crux corpus. The pairing-cascade residual bound is closest to a **matching/covering** argument.

## Prior progress

- Max-bound conjecture **FALSIFIED** (exact counterexample `(7,6,5,3)/21`, ratio 8/7). The `majorization-upper` spine must be revised.
- MB-Dom (dominant case) still valid. MB-Pair must be revisited (it was conditional on the Max-bound IH, which is now false at level n-1 for n≥4).
- n=1,2 certified and complete. V(3) provable from n=2.

## Dead ends (do not retry)

- **Max-bound `D* ≤ M/2^n`** — FALSE (exact counterexample). Do not attempt to prove it. The `majorization-upper` approach's spine is broken; replace with V(n).
- **Majorization/Schur-convexity** — killed round 3 (D* not Schur-convex).
- **Simple pairing IH for V(n)** — fails 37% of crux cases (M_2(rest') > M_2/2). The actual D(rest') is below the target (0.71x), but the IH bound overshoots. Do not frame the V(n) proof as "pair a_1, apply V(n-1)."

## Small-case / intuition notes (CONJECTURES, not proved)

- V(n) = M_2/2^{n-1} is **conjectured** (0 violations n=3,4,5; tight at tower). V(3) is **provable** from the certified n=2 bound. V(n≥4) is the open step.
- The optimal crux strategy is a 3-mark pairing cascade leaving residual `= a_1 - a_2` (conjectured, traced for all 11 Max-bound violators).
- The Max-bound violators are all near-tower configs with a small tail piece (ratio D*/(M/2^n) ≤ 8/7, bounded). The bound V(n) absorbs them (ratio D*/(M_2/2^{n-1}) ≤ 0.67 for the worst violator).
- **The full upper bound `D* ≤ 1/D_n` is NOT violated by any config tested** (3000+ configs n=2,3,4,5). The answer `c(n) = 2^n/(2^{n+1}-1)` stands.

---

## Single best next step for a builder

**Revise `majorization-upper`**: replace the Max-bound spine with **V(n) = M_2/2^{n-1}**. Prove V(3) rigorously from the certified n=2 bound (pair `a_1`, apply `n2-upper-bound-complete` to rest). State the closure: V(n) + certified factorization → `D* ≤ 1/D_n` for all n (with V(n) as the conjecture for n≥4, and the mutual W/V recursion as the inductive structure). Record the Max-bound counterexample `(7,6,5,3)/21` explicitly as the reason the Max-bound is dropped. Mark the V(n≥4) proof as the open GAP.
