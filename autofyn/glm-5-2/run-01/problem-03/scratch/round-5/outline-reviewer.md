# Round 5 outline-reviewer — imo-2026-03

## (1) Fidelity check per approach (overclaim flags)

### tail-count — REVISE (close GAP-C via mass-balance + spine sign-pattern lemma)
**Verdict: APPROVE.** Faithful to the nosaddle explorer report; no overclaims.

- **Mass-balance lemma (the "3-line proof"):** Verified rigorous. On a block-condition cell, `D = 2S₊ − D_n`; `D = 1 ⟺ S₊ = (D_n+1)/2 = 2^n` (confirmed: `(2^{n+1}−1+1)/2 = 2^n` for all n). If all top-fragments at −: `S₊ ≤ 2^n−1 < 2^n ⟹ D ≤ −1`, so `D ≠ 1`. If all at +: `S₊ = 2^n + (tower mass at +)`, so `S₊ = 2^n ⟺` all tower pieces at −. This is a clean, n-independent argument — certifiable NOW. No overclaim.
- **Spine identity `F = T + 1`:** Verified rigorous. Total mass `D_n` odd ⟹ paired mass even (each pair `2v`) ⟹ spine mass `S = F+T` odd ⟹ `D = 1 ⟺ S₊ = (S+1)/2 = (2T+2)/2 = T+1 = F`. So `S₊ = F` is FORCED. Sound.
- **Single-swap argument:** Verified rigorous. Swapping one fragment `v` (at +) with one tower `t` (at −) preserves `D = 1` iff `t = v`; `t` is a power of 2, `v` is not. Impossible. ✓
- **Multi-swap (GAP-C-hard, the load-bearing unproved step):** HONESTLY flagged. The outline admits the naive value-type argument FAILS in isolation (`3 = 2+1` — confirmed: a non-power fragment CAN equal a tower subset). The obstruction must come from breakpoint structure (fragments arise from splitting powers of 2, tying their values to the tower). Verified 0/523 but NOT proved. This is correctly labeled "verification-not-proof" and marked as THE open gap. No overclaim.
- **Watch out (b) — spine vs full config level:** Correctly noted. The all-top-+/all-below− pattern operates at the SPINE level (after pair cancellation), NOT the full-config level (impossible for split-tower types). Faithful to the explorer's dead-end note.

No issues. The mass-balance lemma is certifiable immediately; the spine sign-pattern lemma is the genuine closer with a concrete proof sketch (single-swap done, multi-swap open).

### majorization-upper — REVISE (direct adaptive strategy; phantom crux)
**Verdict: CHANGES REQUESTED.** The "phantom crux" insight is SOUND and verified, but GAP-U1 (the stated hard step) is mis-identified — it is either trivial or false-as-stated, and the real hard step is elsewhere.

- **Phantom-crux claim — VERIFIED SOUND.** I computed `D*` (breakpoint-restricted, exact `Fraction`) for n=4 configs:
  - Crux `(7,6,5,3,1)/22`: `D* = 0`. ✓
  - Non-dominant tower-tail `(14,8,4,2,1)/29` (`a_1 < 2^n`): `D* = 0`, NOT `1/29`. ✓ (halving gives `1/29` but the pair cascade does better)
  - Tower perturbations `(16,9,4,2,1)/32`, `(16,8,5,2,1)/32`, `(16,8,4,3,1)/32`: all `D* = 0`. ✓
  - Dominant tower-tail `(17,8,4,2,1)/32`, `(20,...)/35`, `(24,...)/39`: `D* = 1/S ≤ 1/31`. ✓
  The crux regime and non-tower configs have `D* = 0`; the tower is the unique tight config. Dropping the `V(n)←V(n−1)` IH is correct — the IH was chasing a phantom.

- **GAP-U1 mis-identified (the issue).** The outline states: "prove `a_{n+1} ≤ 1/D_n` for the bottom-dominant tower-tail family, i.e. `S ≥ D_n`." This is problematic:
  - For **dominant** tower-tail (`a_1 ≥ 2·a_2 = 2^n`): `S = a_1 + (2^n−1) ≥ 2^n + (2^n−1) = D_n`. This is **trivial** — not a hard step. `D* = 1/S ≤ 1/D_n` follows immediately from the halving strategy.
  - For **non-dominant** tower-tail (`a_1 < 2^n`, i.e. `a_1 ∈ [2^{n−1}, 2^n)`): `S < D_n`, so `a_{n+1} = 1/S > 1/D_n`. The claim "prove `a_{n+1} ≤ 1/D_n`" is **FALSE** here — the halving bound exceeds the target. But `D* = 0` (pair cascade), so the upper bound still holds via a different strategy. The outline conflates the halving upper bound (`D = a_{n+1}`) with `D*` itself.

- **The real hard step** is GAP-U2 (prove `D* = 0` or `≪ 1/D_n` for non-dominant configs via the pair-matching cascade) + GAP-U3 (`m ≤ n ⟹ D = 0`). Both are conjectures from computation (3000 trials, worst ratio 0.52), NOT proofs. The pair-matching cascade has no proof — only numerical support. The outline does flag GAP-U2 and the conjectural status, but mis-labels GAP-U1 as "the hard step" when it is trivial (dominant) or inapplicable (non-dominant).

- **Phantom-of-a-phantom check:** The explorer does NOT merely show `D*` is small relative to a loose `V(n)` bound — it shows `D* = 0` or `D* = 1/S ≤ 1/D_n` directly (exact computation). The phantom-crux claim is honest, not a phantom-of-a-phantom. The issue is purely the hard-step identification.

**Required changes for the builder:**
1. Reframe GAP-U1: for dominant tower-tail (`a_1 ≥ 2^n`), `S ≥ D_n` is trivial; `D* = 1/S ≤ 1/D_n` by halving. State this as a 2-line lemma, not "the hard step."
2. Promote GAP-U2 to the PRIMARY hard step: prove `D* = 0` (or `≪ 1/D_n`) for non-dominant configs (`a_1 < 2^n` tower-tail, non-tower-tail bottom-dominant, non-bottom-dominant) via the pair-matching cascade. This is currently a conjecture — it must be PROVEN, not assumed.
3. Do NOT conflate halving's `D = a_{n+1}` (an upper bound on `D*`) with `D*` itself.
4. GAP-U3 (`m ≤ n ⟹ D = 0`) is a conjecture (verified n=4); prove it, don't assume it.

### xor-overlap — NEW (5th lower framing)
**Verdict: APPROVE.** Genuine 5th framing; identity non-circular; hard gap honestly G1-equivalent.

- **XOR identity `D = D_F + D_R − 2C`:** Verified exact (algebraic from `(a+b) mod 2 = (a mod 2) + (b mod 2) − 2(a mod 2)(b mod 2)`). The explorer verified 0 failures / 6000+ trials. Non-circular — it is a direct consequence of bilinearity of the parity product.
- **Base case n=1:** Verified tight. `F = {f, 2−f}`, `R = {1}`. `D_F = 2f−2`, `C = f−1` (for `f ≥ 1`), so `D_F = 2C` exactly, `D = 2C + 1 − 2C = 1`. Confirmed for 9 values of `f` (1.1 to 1.9). ✓
- **Induction `G1(n) → G1(n−1) + overlap`:** Clean. `D_R` is the standalone `D` of a `≤ (n−1)`-mark refinement of `T_{n−1}`; by strong IH, `D_R ≥ 1`. The reduction is well-formed.
- **Overlap bound (GAP-X, the hard step):** HONESTLY G1-equivalent. The outline explicitly states: trivial bounds (`C ≤ min(D_F, D_R)`, `C ≤ √(D_F·D_R)`) give only `D ≥ 0` (the trivial G2 bound); the "1" needs tower structure not captured by generic inequalities; the exact bound `D_F + D_R ≥ 2C + 1` is `D ≥ 1` restated (circular). The `D_F ≥ 2C` sufficient condition FAILS at minimizers (543/2196 T_4 breakpoints, worst deficit −6) — the outline warns against this route. No overclaim.
- **G1-equivalent, not a shortcut:** Faithfully marked. The value is a different attack surface (correlation/overlap of two decoupled parity functions, with a clean inductive reduction) and a provably tight base case — not a difficulty reduction.
- **Diversity check:** Genuinely far from all four converged framings (no PL geometry, no pair cancellation, no per-pair charging, no static LP certificate). Satisfies the plateau-break mandate.

Registered as a new approach (cold-start Elo 1500).

### lp-dual-certificate — REVISE (fix LP-2 sign error; reframe GAP-LP2)
**Verdict: APPROVE with CHANGES REQUESTED notes.** The sign-error fix is a required correctness step; the reframing is sound; but the outline itself flags sign-convention uncertainty.

- **Sign-error fix:** Correctly identified. The round-4 LP-2 mountain direction was flipped (nonneg should be nonpos); the interleaved T_2 demo was infeasible (obj 2 vs actual min 1, verified scipy); the narrow sub-class had wrong parity (`k` odd → `k` even). The outline correctly mandates fixing this BEFORE any new feasibility claim. GAP-LP1 (clean types) is unaffected (`y_ub = 0`, sign irrelevant) and stands certified.
- **Reframing (GAP-LP2 = spine sign-pattern lemma in LP language):** Sound by strong duality. The dual certificate `y_eq[fragment-bin] = +1, y_eq[tower-bin] = −1` IS the spine's sign assignment; objective `(Σ fragments) − (Σ towers) = 1`; `dual ≥ 1 ⇔ min D ≥ 1`. Correct.
- **Rival mechanism:** LP feasibility (Farkas/separating hyperplane) is genuinely different from tail-count's combinatorial multi-swap subset-sum. Both attack the same closing lemma from different proof mechanisms — acceptable diversity, NOT a single-gap trap.
- **Sign-convention uncertainty (the issue):** The outline's key lemma itself stumbles: `"d_k = (−1)^k − y_eq[b(k)] ≥ 0 — because the spine interleaves... d_k = −1 − 1 = −2 < 0... wait, sign needs care."` The outline flags its own uncertainty. The builder MUST verify the exact sign convention after the fix before claiming feasibility.
- **Family of sign-patterns:** Correctly noted that only 0–3% of odd types admit a single uniform cert; the feasibility lemma needs a FAMILY of sign-patterns, not one.
- **G1-equivalent:** Honestly marked (not a shortcut, per the round-4 rule).

**Required changes for the builder:**
1. Fix the LP-2 sign error FIRST (mountain direction, parity, infeasible example). No feasibility claim before this is settled.
2. Verify the exact sign convention rigorously — the outline's own stumbles show this is error-prone.
3. The feasibility lemma needs a family of sign-patterns (not one uniform cert).

### tower-induction, gaps-leftover — HOLD
Correctly held. Their open gaps (G2-odd, deficit-covering) are now recognized as the same spine sign-pattern lemma that tail-count and lp-dual attack this round. Building them would risk a three-slug single-gap trap. If both rival mechanisms stall, revive tower-induction's spine-value arithmetic as a third mechanism next round.

### d-potential, self-similar, balanced-configs — HOLD/RETIRED
No change. Certified sub-results harvested.

---

## (2) Registration decision for xor-overlap

**REGISTERED.** `xor-overlap` is a genuine 5th lower-bound framing (exact XOR identity + strong induction on n), far from all four converged framings. The identity is non-circular (algebraic, verified 6000+ trials); the base case is provably tight (`D_F = 2C`, `D = 1`); the hard gap (decoupled overlap bound) is honestly G1-equivalent. It satisfies the plateau-break mandate (≥1 genuinely-different framing in the build set). Registered at cold-start Elo 1500.

---

## (3) Head-to-head ranking with reasoning

Field after ranking (Elo): tail-count (1730) > tower-induction (1597) > majorization-upper (1544) > xor-overlap (1524) > lp-dual-certificate (1486) ≈ gaps-leftover (1486).

Key comparisons and reasoning:
- **tail-count > tower-induction:** tail-count has the direct-close lead (mass-balance lemma certifiable NOW as a 3-line proof; spine sign-pattern verified 0/523 with a concrete single-swap proof sketch). tower-induction is HELD with no new progress this round; its G2-odd is now recognized as the same spine lemma tail-count attacks. tail-count is closer to closing G1 than any prior round.
- **tail-count > majorization-upper:** tail-count's mass-balance lemma is rigorous and certifiable immediately; majorization-upper's stated hard step (GAP-U1) is mis-identified (trivial for dominant, false-as-stated for non-dominant). Different walls, but tail-count's lead is more solid.
- **tail-count > xor-overlap:** tail-count is closer to closing (certifiable sub-lemma + verified spine lemma); xor-overlap is cold-start with a G1-equivalent gap. But xor-overlap's framing is genuinely further from the converged wall.
- **tower-induction > majorization-upper:** tower-induction has certified S1/S2/S3 scaffolding and no mis-step this round; majorization-upper has a sound phantom-crux insight but a mis-identified hard step (GAP-U1) and an unproved pair cascade (conjecture from 3000 trials).
- **majorization-upper > lp-dual-certificate:** majorization-upper's phantom-crux insight is verified sound (D*=0 for non-tower, exact computation); lp-dual is correcting a sign error (a real setback). Both are REVISE, but majorization-upper's reframing is a net positive (cleaner strategy, no IH) while lp-dual's is a corrective fix.
- **majorization-upper ≈ xor-overlap (draw):** different walls (upper vs lower); both sound but incomplete. majorization-upper has verified computation; xor-overlap has a tight base case and exact identity. Neither has a proof of its hard step.
- **tower-induction ≈ xor-overlap (draw):** tower-induction has established scaffolding (S1/S2/S3 certified); xor-overlap has a genuine new framing with tight base case. Different strengths at similar levels.
- **lp-dual-certificate ≈ xor-overlap (draw):** both attack the lower wall from different mechanisms. lp-dual has certified GAP-LP1 (clean types); xor-overlap has exact identity + tight base case but no certified sub-result yet. Similar logical status.
- **xor-overlap > gaps-leftover:** xor-overlap is a fresh framing with momentum (exact identity, tight base); gaps-leftover is HELD with no new progress (same wall, stalled).
- **lp-dual-certificate > gaps-leftover:** lp-dual has a certified sub-result (GAP-LP1) and a corrective reframing this round; gaps-leftover is stalled.

**Shared-wall flag (tail-count + lp-dual on the spine sign-pattern lemma):** Both aim at the SAME closing lemma (spine sign-pattern) from different proof mechanisms (combinatorial multi-swap subset-sum vs LP feasibility/Farkas). This is acceptable diversity (rival PROOF MECHANISMS for one lemma, not a single-gap trap) — but if BOTH stall on the same lemma for 3 rounds, retire one. The outliner correctly holds tower-induction and gaps-leftover (which share the same wall) to avoid a four-slug single-gap trap.

---

## (4) Build set

`build set: tail-count, majorization-upper, xor-overlap, lp-dual-certificate`

Four builders, one per slug, in parallel:
- **tail-count** (ADVANCE — certify the mass-balance lemma immediately; attempt the multi-swap subset-sum proof for the spine sign-pattern lemma, the G1-closer).
- **majorization-upper** (REVISE with CHANGES — reframe GAP-U1 as trivial for dominant tower-tail; promote GAP-U2 to primary hard step; PROVE the pair-matching cascade for non-dominant configs, don't assume it; prove GAP-U3 m≤n⟹D=0).
- **xor-overlap** (NEW — prove the XOR identity rigorously; establish the tight base case; attempt the decoupled overlap bound on C).
- **lp-dual-certificate** (REVISE — fix the LP-2 sign error first; verify sign convention rigorously; reframe GAP-LP2 as LP-feasibility witness of the spine lemma; attack via Farkas).
