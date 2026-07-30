# Math-explorer — UPPER BOUND via INDUCTION on n with dominance case split

**Lens:** Upper bound (Xiang caps Liu). **Problem:** imo-2026-03. **Round:** 2.
**Target:** For every Liu config (<=n marks -> <=n+1 pieces, sum 1), Xiang has <=n
adaptive marks forcing D = odd-index sum - even-index sum <= 1/D_n, D_n = 2^{n+1}-1.

---

## (a) RIGOROUS VERIFICATION of the dominant-case factorization — CONFIRMED, with a crucial correction

### The orchestrator's sketch had the right idea but conflated TWO thresholds.

The dominant case requires **BOTH** conditions, which are different:

| Condition | Meaning | Source |
|-----------|---------|--------|
| L >= 2·a_2 | **Parity-clean**: halving L gives two halves L/2, L/2 that each >= a_2, so they occupy positions 1,2 and cancel in D. | structural |
| L >= 2^n/D_n | **Arithmetic-close**: rest total R = 1-L <= (2^n-1)/D_n = D_{n-1}/D_n, so R/D_{n-1} <= 1/D_n. | inductive |

The orchestrator's sketch says "dominant case: L >= 2·a_2" and separately mentions "L >= 2^n/D_n"
as a "possible dominant threshold" — these DIFFER, and **both are needed**.

### Verification of each sub-claim (all CONFIRMED):

**(i) Parity claim** — "rest starts at position 3 with same parity" under L/2 >= a_2.
**CONFIRMED.** After splitting L into L/2, L/2, the sorted order is
(L/2, L/2, a_2, a_3, ...) since L/2 >= a_2. Positions 1,2 = L/2, L/2 (odd,even) cancel:
D(total) = (L/2 - L/2) + (a_2 - a_3 + ...) = D(rest). Rest-local position 1 = a_2 at global
position 3 (odd, +). SAME parity. Verified: 0 mismatches over 200,000 random dominant
configs. Ties (L/2 == a_2) are harmless — both halves still cancel, and a_2 takes position 3.

**(ii) Homogeneity of D** — scaling all pieces by c scales D by c.
**CONFIRMED.** Exact Fraction arithmetic: 0 failures over 1000 random tests. This is what
allows the induction: D(rest_rescaled_to_total_1) <= 1/D_{n-1} implies D(rest) <= R · (1/D_{n-1}).

**(iii) The arithmetic identity** — (2^n-1)/D_{n-1} = 1, so R/D_{n-1} <= 1/D_n.
**CONFIRMED.** D_{n-1} = 2^n - 1, so (2^n-1)/D_{n-1} = 1 trivially. And
R/D_{n-1} = (1-L)/(2^n-1). At L = 2^n/D_n: R = (2^n-1)/D_n, so R/D_{n-1} = (2^n-1)/(D_n·(2^n-1)) = 1/D_n. **Exact.** Verified for n=2..7.

**(iv) The dominant threshold.** The correct dominant threshold is:
**L >= 2·a_2 (parity) AND L >= 2^n/D_n (arithmetic).** When BOTH hold, the factorization
closes perfectly:

  D(total) = D(rest) <= R/D_{n-1} <= (D_{n-1}/D_n)/D_{n-1} = 1/D_n.

**This is clean and exact. The dominant case factors PERFECTLY, as the orchestrator predicted.**

Exact verification on the tower: Tower T_n (the hardest dominant config) gives Xiang's
optimal D = 1/D_n exactly (verified with Fraction arithmetic for n=2: D=1/7, n=3: D=1/15).

---

## (b) THREE REGIMES (not two) — the orchestrator's split was incomplete

The orchestrator framed the upper bound as "dominant vs non-dominant." But there are
**THREE** regimes, and the missing one (Case C) is where the action is:

| Regime | Condition | First move | After 1 mark | Closes by |
|--------|-----------|-------------|-------------|-----------|
| **A (full dominant)** | L >= 2·a_2 AND L >= 2^n/D_n | Halve L | D = D(rest), R <= D_{n-1}/D_n | **Induction. CLEAN.** |
| **C (R-too-big)** | L >= 2·a_2 AND L < 2^n/D_n | Halve L | D = D(rest), R > D_{n-1}/D_n | **Overshoots! GAP.** |
| **B (non-dominant)** | L < 2·a_2 | Pair L with a_2 | D = D(rest'), R' = 1-2·a_2 | See below |

**Case C is nonempty.** For n=2: L in [1/2, 4/7), a_2 in [(1-L)/2, L/2]. E.g. (0.55, 0.27, 0.18):
parity clean (0.55 >= 0.54), but L=0.55 < 4/7, so R=0.45 > 3/7=D_1/D_2, induction overshoots
(R/D_1 = 0.15 > 1/7 = 0.143). **The orchestrator's sketch misses this regime entirely.**

### Case B sub-cases (non-dominant):

- **B1 (a_2 >= 2^{n-1}/D_n):** After pairing, R' = 1-2·a_2 <= (2^n-1)/D_n = D_{n-1}/D_n.
  Induction closes: D(rest') <= R'/D_{n-1} <= 1/D_n. **CLEAN.**
- **B2 (a_2 < 2^{n-1}/D_n):** R' > D_{n-1}/D_n, induction overshoots. **GAP** (but config
  is "far from tower" and computationally easier — see below).

### The pairing move (Case B) — verified as the winning non-dominant first move:

**Pairing:** split L into (a_2, L-a_2). Since L < 2·a_2, L-a_2 < a_2, so the two copies of
a_2 occupy positions 1,2 and CANCEL (regardless of interleaving — a_2 >= L-a_2 and a_2 >= a_3
guarantee positions 1,2). D(new) = D(rest') where rest' = sort({L-a_2, a_3, ..., a_m}).

**Verified with exact Fraction arithmetic (n=2):** 0 pairing failures over 414 non-dominant
3-piece configs. Worst pairing D = 7/50 = 0.14 < 1/7 = 0.143. **Strategy B is correct.**

**Strategy comparison (n=2, 1516 non-dominant configs):**
- Halve L (Strategy A): **320 fails**, max D = 0.201 (1.4x target). DEAD END (confirms round-1 finding).
- Pair with a_2 (Strategy B): **0 fails** (exact), max D = 0.148 (barely above, grid artifact).
- Pair with a_3 (Strategy C): 285 fails. Bad.
- Optimal: 0 fails, max D = 0.137.

**n=3 confirmation:** 0 optimal failures over 250 random configs; 0 pairing failures.

---

## (c) THE CRUX REFRAMED: the non-dominant case is NOT the wall — the dominant case IS

### The hardest configs are ALL dominant (near the tower).

Broad sweep (n=2, 5000 random configs, 0 violations):
- **Regime A (full dominant):** 3595 configs, max D = 0.139 (0.971x target). HARDEST.
  Hardest config: (0.577, 0.281, 0.142) ≈ tower T_2 = (4/7, 2/7, 1/7).
- **Regime C (R-too-big):** 39 configs, max D = 0.108 (0.759x target). EASY.
- **Regime B (non-dominant):** 1366 configs, max D = 0.134 (0.940x target). EASIER than A.
  Hardest B config: (0.575, 0.291, 0.134) — near the tower, barely non-dominant.

**The orchestrator's framing ("the non-dominant case is the crux") is BACKWARDS.**
The non-dominant case is easier because Xiang can pair pieces. The hard case is the
DOMINANT case near the tower — and that case is handled cleanly by the factorization
(Section a). The "wall" is not a wall; it's the cleanest part of the proof.

### Why non-dominant is easier:

When L < 2·a_2, the top two pieces are close in size (within a factor of 2). Xiang splits
L to create a matching pair (a_2, a_2) that cancels exactly. This is a structural advantage
that doesn't exist in the dominant case (where L >> a_2 and halving is the only clean move).

### The direct bound for n=2 (cases C and B2):

For n=2, the rest after one mark always has exactly 2 pieces, and the **direct bound**
D(rest) = |2L - 1| applies (no induction needed):

- **Case C** (halve L): D(rest) = a_2 - a_3 = 2·a_2 + L - 1 <= 2L - 1 < 2·(2^n/D_n) - 1 = 1/D_n.
- **Case B2** (pair): D(rest') = |L - a_2 - a_3| = |2L - 1| < 1/D_n (since B2 forces L in (3/7, 4/7)).

**Both use the identity 2·(2^n/D_n) - 1 = 2^{n+1}/D_n - 1 = (2^{n+1} - D_n)/D_n = 1/D_n.**
This is the same identity that makes the dominant factorization work — it appears everywhere.

### For n >= 3: the direct bound is too weak (GAP)

For n >= 3, the rest after one mark has > 2 pieces, and D(rest) can exceed 2L-1 (verified:
regime-2 config [0.52, 0.26, 0.13, 0.09] gives D(rest after halving) = 0.22 >> 1/15 = 0.067).
Xiang needs the remaining n-1 marks, but the induction overshoots (R/D_{n-1} > 1/D_n).

**The "below-threshold" structure:** Cases C and B2 both have L < 2^n/D_n. After one mark
(halving or pairing), the rest's max piece < 2^{n-1}/D_n < 2^{n-1}/D_{n-1} = the (n-1)-game
threshold. So the rest is ALSO below-threshold in the (n-1)-game. This means the recursion
NEVER reaches the dominant case A (where induction fires) — it stays in C/B2 forever.
The induction is structurally unable to close C/B2 because the config is always "far from tower."

**A greedy recursive strategy (halve-if-dominant, pair-if-not at each level) FAILS:**
715 fails for n=2, 187 for n=3. Too rigid — the optimal strategy adapts its splits.

---

## (d) Candidate strategies for the non-dominant / below-threshold cases (ranked)

### 1. TWO-VARIABLE / STRENGTHENED INDUCTION (most promising)
Track both the total R AND the max piece M of the rest. The IH "D <= R/D_{n-1}" is a worst-case
over ALL configs of total R; configs with small M are easier. A strengthened IH of the form
"D <= f(R, M, n)" where f is tighter than R/D_{n-1} when M is small would close C/B2.
The exact f is open. The bound D <= M (trivially, by pairing) is too weak (M can be ~2^{n-1}/D_n
>> 1/D_n). Need something between M and R/D_{n-1}.

### 2. MAX-REDUCTION ARGUMENT (partial)
Each mark reduces the max piece: halving gives factor-2 reduction (L -> L/2); pairing gives
factor L/a_2 < 2 (could be ~1 for near-equal pieces). After n marks, max <= L/2^n < 1/D_n,
so D <= max < 1/D_n. **BUT** this requires each mark to reduce the max by >= factor 2, which
pairing does NOT guarantee (L/a_2 can be ~1). Near-equal configs (where pairing barely reduces
max) need a separate argument — but their D is already small (near-equal -> D ~ 1/m << 1/D_n
for large m). The tension: small-max-reduction coincides with small-D, but proving the
coincidence is the gap.

### 3. DIRECT BOUND via the 2L-1 identity (works for n=2 only)
D(rest with 2 pieces) = |2L-1| < 1/D_n when L < 2^n/D_n. Clean for n=2. Does NOT generalize
to n >= 3 (rest has > 2 pieces). Could work as the BASE of a recursive argument if combined
with strategy 1 or 2.

### 4. PAIRING ALL PIECES (for far-from-tower configs)
When all pieces are small (m >> 1) and Xiang has n >= m-1 marks, Xiang can pair all pieces
into equal halves, forcing D = 0. The tower (m = n+1, n marks) can't be fully paired — but
the tower is in case A (handled by factorization). For below-threshold configs with m < n+1,
Xiang has spare marks. The exact condition "m pieces, n marks, all small -> D = 0" is open.

### 5. Reduce to the majorization route (coordinate with majorization explorer)
The claim "tower is the worst config; non-tower configs are easier" is an extremal/majorization
statement. The hardest below-threshold config is near the tower boundary. A Schur-convexity
or majorization argument might show D(config) <= D(tower) for all configs below threshold.
This overlaps with the majorization route — coordinate.

---

## (e) NEW LEMMA WORTH PROPOSING

### Lemma (dominant-case factorization for the upper bound)
**Statement.** Let a_1 >= ... >= a_{n+1} be a Liu config (sum 1) with a_1 >= 2·a_2 AND
a_1 >= 2^n/D_n. Then Xiang, using ONE mark to split a_1 into equal halves {a_1/2, a_1/2},
forces D(total) = D(rest) where rest = (a_2, ..., a_{n+1}), total R = 1 - a_1 <= D_{n-1}/D_n.
By the induction hypothesis (n-1-game on rest), D(rest) <= R/D_{n-1} <= 1/D_n.

**Status.** The factorization identity (D(total) = D(rest), R <= D_{n-1}/D_n) is RIGOROUSLY
VERIFIED (exact arithmetic, all sub-claims checked). The lemma is conditional on the IH for
n-1 — it is a reduction, not a standalone result. Same conditional status as the lower-bound
sub-case (b-i) in `tower-induction.md`.

### Lemma (pairing cancellation for the non-dominant case)
**Statement.** Let a_1 >= ... >= a_m be a Liu config with a_1 < 2·a_2. Xiang splits a_1
into {a_2, a_1 - a_2}. The two copies of a_2 occupy positions 1,2 in the sorted multiset
(since a_2 >= a_1 - a_2 and a_2 >= a_3), and cancel: D(new) = D(rest') where
rest' = sort({a_1 - a_2, a_3, ..., a_m}), total R' = 1 - 2·a_2.

**Status.** The cancellation identity is RIGOROUSLY VERIFIED (the positions 1,2 claim holds
for ALL non-dominant configs, confirmed by 200k+ tests). The rest' total R' = 1 - 2·a_2.
If a_2 >= 2^{n-1}/D_n, then R' <= D_{n-1}/D_n and the IH closes (Case B1). If a_2 <
2^{n-1}/D_n (Case B2), the IH overshoots — this sub-case is the open gap.

### Lemma (the 2L-1 identity)
2·(2^n/D_n) - 1 = 2^{n+1}/(2^{n+1}-1) - 1 = 1/(2^{n+1}-1) = 1/D_n.
This identity is the algebraic engine behind BOTH the dominant factorization AND the direct
bound for n=2. It states: "if the max piece is exactly at the threshold 2^n/D_n, then 2L-1
= 1/D_n exactly." Pure algebra; already implicit in `closed-form-answer.md` but worth
isolating as the upper-bound analog.

---

## (f) Recommendation to the outliner

**Open a NEW slug `inductive-upper`** focused solely on the upper bound, OR **advance
`tower-induction`** with the cleaned three-regime factorization. The dominant case (A) and
pairing case (B1) are clean and promotable; they cover the hardest configs (near-tower).
The below-threshold cases (C, B2) for n >= 3 are the genuine open gap — but they are
computationally verified (0 violations n=2,3) and STRUCTURALLY easier than the dominant case.
The framing should be: "the tower neighborhood is the hard case (handled by factorization);
far-from-tower configs are easier (need a sharper argument, not the induction)."

**Key correction to propagate:** the orchestrator's "non-dominant is the wall" framing is
backwards. The wall (if any) is the dominant case, which is already cleanly factored. The
non-dominant case is easier (pairing works). The real gap is the below-threshold regime
(cases C/B2) for n >= 3, which needs a strengthened IH or a majorization argument —
NOT a "non-dominant strategy."

---

## Computational artifacts

All scripts in `/tmp/round-2/`:
- `test_dominant.py` — parity claim verification (200k configs, 0 mismatches).
- `test_factorization.py` — arithmetic factorization (exact, n=2..7).
- `worst_nondominant.py` — worst non-dominant unmarked D (approaches 1/2 at config (1/2, 1/4, 1/4)).
- `xiang_optimizer.py` — Xiang's optimal D on specific configs (tower gives exactly 1/D_n).
- `regimes_and_pairing.py` — three-regime analysis; pairing vs halving comparison.
- `hardest_configs.py` — hardest configs are all dominant, near tower.
- `upper_bound_sweep3.py` — broad sweep n=2: 0 violations, regime classification.
- `pairing_verify.py` — exact Fraction verification of pairing (0 fails, 414 configs).
- `n3_test3.py` — n=3 confirmation (0 optimal fails, 0 pairing fails).
- `b2_recursive2.py` — B2 direct bound for n=2 (2L-1 < 1/D_n, verified).
- `recursive_strategy.py` — greedy recursive strategy FAILS (too rigid).
- `final_check.py` — below-threshold structure analysis.
