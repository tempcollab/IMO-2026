# Proof-reviewer — IMO 2026 P3 (imo-2026-03), Round 4

Reviewed 4 built approaches. **Problem remains `partial`**: neither the upper bound (GAP U) nor
the lower bound (GAP L) is fully proven for general n. Each approach advanced its wall by one
rigorous, verified sub-case; both residuals are honestly isolated (no overclaim in any of the four).
Certified spine (Lemma G, level-measure, cut-flip, IP) re-relied on, not re-litigated.

Independent checks I ran (`python3`, /tmp): (1) region-A residual `2ℓ₁−Σ < u_kΣ` over 2·10⁴
exact-Fraction/float Case-(iii-a) instances — 0 violations; (2) Lemma-T signed-sum identity
`D̃−1=Σψ(c_i)Δw_i` to 1e-7 and `maxc≤1 ⇒ D̃≥1` over 2·10⁴ random top/bottom splits — 0 violations;
(3) algebra `2c(k)−1=u_k`, `ψ(c)≥0⇔c≤1` re-derived by hand and by machine. All hold.

---

## 1. dyadic-discrepancy — VERDICT: CHANGES REQUESTED (Status: partial)
Scores: Correctness 5/5 · Rigor 4/5 · Progress 4/5.

Load-bearing new result = **Pivot Lemma (§4.6)**. I re-derived it from scratch: bisect the `m−1−|S|`
pieces not in `S` (IP-deleted), then pin `S` into the pivot in decreasing order; each pin legal since
`R_i−s_i = ℓ₁−(s₁+…+s_i) ≥ ℓ₁−sum(S) ≥ 0`; exactly `m−1` ops; final total `ℓ₁−sum(S)`. Correct.
Case (iii-a) closure: `S`=all others admissible iff `ℓ₁≥Σ/2`, residual `2ℓ₁−Σ`; since `ℓ₁<c(k)Σ`
and `2c(k)−1=u_k`, residual `<u_kΣ`, and `D≤`effective total gives `D<u_kΣ`. **Genuinely closes the
slab `Σ/2≤ℓ₁<c(k)Σ` for ALL n** (new — Case (i) only covered `ℓ₁≥c(k)Σ`). Verified numerically.

The recorded Status (`partial`) is correct and honest. GAP U reduced to (iii-b) `ℓ₁<Σ/2` (n≥3):
still open, correctly flagged as needing an adaptive pivot / strengthened potential, with the
pivot-into-ℓ₁-only route explicitly shown insufficient. Not solved (upper bound incomplete for n≥3).

**Gap to close:** RT(k) for `m=k+1`, `ℓ₁<Σ/2` (super-balanced), reach effective total `≤u_kΣ`.

## 2. dyadic-discrepancy-euclid — VERDICT: CHANGES REQUESTED (Status: partial)
Scores: Correctness 5/5 · Rigor 4/5 · Progress 3/5.

Closes the **same** region as the twin (region A `ℓ₁≥Σ/2`) via the accumulator schedule. I checked
Lemma 5.2: invariant `sum(rest)≤a` self-restores — after pinning `b` into `a`, for `x∈rest'`,
`x≤sum(rest')=sum(rest)−b≤a−b=a'`, so `a'` stays the max and `sum(rest')≤a'`. Termination in `≤m−1`
ops, final total `2ℓ₁−Σ` (each non-top piece absorbed once). Correct. Corollary 5.4 (`<u_kΣ` when
`ℓ₁<c(k)Σ`) is right. The empirical-gate refutations (pin-against-smallest, difference-tournament)
are correctly recorded as dead ends. Status `partial` honest; region B `ℓ₁<Σ/2` open.

**Note (for the outliner, not a defect):** this is the SAME closure as the twin's Pivot Lemma
(deterministic form vs subset form) with the SAME residual `ℓ₁<Σ/2`. Both GAP-U twins have now
bottomed out on the identical wall. Per the shared-gap rule this is a plateau signal — next round
should put ≥1 approach on GAP U (iii-b) from a genuinely different framing (e.g. the 2-adic recast),
not a third same-wall pin schedule.

**Gap to close:** GAP U-B, identical to the twin.

## 3. induction-recursion — VERDICT: CHANGES REQUESTED (Status: partial)
Scores: Correctness 5/5 · Rigor 4/5 · Progress 2/5.

New work: (R1) `D̃=∫1[M odd]`, `∫M=1`; (R2) Sufficient Lemma `|h|≤1 ⇒ D̃=∫h+2λ{h=−1}≥1`;
(R3) ±1 gradient + value-preserving exchange; (R4) obstruction `h(0⁺)=(a+1)−(n+b)≤1−2b`, so
`b≥2 ⇒ |h|≥3` near 0. I verified R1b (`∫h=2θ−(2θ−1)=1`), R2 algebra, and R4 arithmetic — all correct.
This is an **honest negative result**: the assigned exchange/degenerate-boundary route is PROVED
unable to close GAP-LB′ (interior-minimizer counterexample + fragment-count wall). No scalar-summary
fill smuggled in (that is refuted, correctly noted). Status `partial` correct; the gap is not closed,
only reformulated and its easy route killed — hence outcome recorded as `partial` (not `advanced`).

**Gap to close:** GAP-LB′ for `b≥2` — bound `2λ{h<0,h odd}` (the near-0 negative excursions) using
`Z`'s recursive dyadic cut-structure. Same wall as the telescope twin.

## 4. induction-recursion-telescope — VERDICT: CHANGES REQUESTED (Status: partial)
Scores: Correctness 5/5 · Rigor 5/5 · Progress 4/5.

Load-bearing new result = **Termwise Lattice Lemma T (§4)**. I re-derived the full chain: `M=N_Y−N_Z`,
`D̃=∫1[M odd]` (parity), merged descending order with `c_i=#T−#B`, `M=c_i` on `(w_{i+1},w_i)`, hence
`D̃−1=Σψ(c_i)Δw_i` with `ψ(c)=1[c odd]−c`. Checked `ψ(c)≥0⇔c≤1` (`ψ(1)=ψ(0)=0`, `ψ(≤0)≥−c≥0`,
`ψ(≥2)≤1−c<0`). So `maxc≤1 ⇒` all terms `≥0` (using `Δw_i≥0`) `⇒ D̃≥1`. **Correct and rigorous.**

Crucial guard check the orchestrator flagged: **this is NOT the refuted unconditional
`D̃≥sum(Y)−sum(Z)`.** Lemma T is CONDITIONAL on `maxc≤1`, a real termwise sign argument — no scalar
smuggling. The claim "every tight config has maxc≤1" is a numeric observation (not used in the
proof), so it does not inflate the result; the proof rigorously closes exactly the `maxc≤1`
sub-region. Verified numerically (identity to 1e-7; `maxc≤1⇒D̃≥1`, 0 violations). Structure Lemma
(recursive cut-tree of a dyadic response) also checked and correct. Status `partial` honest;
residual `maxc≥2` genuinely open.

**Gap to close:** GAP-LB′-run — `Σ_{c_i≥2}(c_i−1[c_i odd])Δw_i ≤ Σ_{c_i≤0}(1[c_i odd]−c_i)Δw_i`
(T-run deficit ≤ anchor surplus), via a two-level induction on `Z`'s cut-tree.

---

## Certified lemmas (round 4)
- **`lemmas/pivot-lemma.md`** — Pivot/accumulator lemma (residual `ℓ₁−sum(S)` in `m−1` ops; region-A
  closure `2ℓ₁−Σ<u_kΣ`). Admitted (both twins prove it; verified). Canonical form; subsumes the
  euclid accumulator.
- **`lemmas/termwise-lattice.md`** — Merged-order signed-sum identity `(♦)` + Termwise Lattice Lemma T
  (conditional on `maxc≤1`), with the unconditional version explicitly guarded as FALSE. Admitted.

Not separately certified (correct but subsumed / derivative): euclid accumulator Thm 5.3 (= Pivot
Lemma), Difference-function Sufficient Lemma R2 (correct; folded into the telescope reformulation
narrative — can be promoted later if reused), Fragment-count obstruction R4 (correct obstruction,
not a positive reusable lemma), Structure Lemma (correct; certify when the residual induction
actually consumes it).

## Bottom line
4× CHANGES REQUESTED. Problem `partial`. GAP U: only sub-case (iii-b) `ℓ₁<Σ/2` (n≥3) open. GAP L:
only residual `maxc≥2` open. WARNING to orchestrator: both GAP-U twins collapsed to one wall
(`ℓ₁<Σ/2`) and both GAP-L twins to one wall (`Z` cut-tree near 0). Two shared-gap plateaus — next
round should open ≥1 genuinely different framing per wall rather than a fifth same-wall variant.
