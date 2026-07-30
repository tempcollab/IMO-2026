# Proof review — imo-2026-03 (round 7)

Problem: determine `c(n)` = Liu Bang's guaranteed total. Target answer
`c(n) = 2^n/(2^{n+1}−1)`, equivalently `D* = u_n := 1/(2^{n+1}−1)`.

**Headline: the general-n UPPER BOUND (open since round 1) is now genuinely, rigorously
proven for all n.** I re-derived the load-bearing step (Realizability + subset-sum pigeonhole)
from scratch and verified it end-to-end. The whole problem is still `partial` because the
lower-bound Case B (GAP L) is not closed.

---

## dyadic-discrepancy — Verdict: CHANGES REQUESTED — Status: partial (GAP U SOLVED)

**Upper bound (§4.7): CORRECT and COMPLETE for all n.** I attacked the load-bearing chain:

1. *Removal ops + Invisible-Pair Lemma.* IP (`D(R∪{v,v})=D(R)`) is correct: two equal pieces
   add an even amount `2·1[t<v]` to `N(t)` everywhere, so the odd-set is unchanged. Bisect /
   generalized-pin / free-delete each cost ≤1 cut and set aside one equal pair.
2. *Physical-decomposition remark.* The physical final multiset is `P = E ⊎ (one equal pair
   per op)`. Applying IP per pair gives `D(P)=D(E) ≤ total(E)` (pairing form `D≤b₁≤total`).
   This correctly closes the prose gap between "effective total" and the discrepancy the
   claiming phase actually faces — the pieces the reduction "deletes" are physically present
   as equal pairs, invisible regardless of later cuts. Sound.
3. *Realizability Lemma.* For any `ε∈{−1,0,1}^m\{0}`, Xiang reaches effective total exactly
   `|Σ ε_i ℓ_i|` in `≤ m−1` ops: bisect the zeros, then on the nonzero support repeatedly pin
   an opposite-signed pair (preserving the labelled signed sum) / free-delete equal pairs. Op
   count, pin legality (always cut the strictly larger, `a−b>0`), and the signed-sum invariant
   all check out.
4. *Subset-Sum Pigeonhole.* Among the `2^{n+1}` subset sums in `[0,Σ]`, the `2^{n+1}−1`
   consecutive gaps sum to `Σ`, so the min gap `≤ Σ/(2^{n+1}−1)=u_nΣ`; the two consecutive
   subsets `A≠B` give a nonzero `ε` with `|Σ ε_iℓ_i| = s_B−s_A ≤ u_nΣ`. Correct; `A≠B`
   always (consecutive sorted entries are distinct subsets even at a tie).
5. *Assembly.* Pick `ε` by pigeonhole, realize in `≤ n = m−1` cuts, `D=D(E)≤ total(E)=
   |Σε_iℓ_i| ≤ u_nΣ`. Legal `≤ n`-cut Xiang response. Sharp at dyadic (`min nonzero |Σε_i2^i|
   = 1 ⇒ u_n`).

**Independent verification (mine, exact `Fraction`):** simulated the ACTUAL physical Xiang
cut sequence (pigeonhole ε → realizability ops) on random `(n+1)`-piece partitions, `n=1..5`,
3000 each: true discrepancy `D(P) ≤ u_n` (worst ratio **0.9998**, tight at dyadic), `≤ n`
cuts, mass conserved `= Σ`, **0 violations**. The upper bound is real.

The builder's recorded status ("GAP U fully closed, overall partial") is **accurate** — no
overclaim. No refuted move (bisect-n-largest, myopic greedy, fixed schedule) is smuggled in;
the pigeonhole selects the globally optimal pattern, not any fixed first move, which is
exactly why it clears the round-4 (iii-b)/`k=4` obstruction.

*Why CHANGES REQUESTED not APPROVE:* this slug's file is a whole-problem attempt. It proves
the upper bound + lower-bound Case A, but **GAP L (lower-bound Case B) is open**, so the whole
problem is not solved. Remaining gap to close: the lower-bound Case B (owned by the induction
slugs). Scores — Correctness 10/10 (upper bound), Rigor 9.5/10, Progress: major (a
round-1 wall closed).

---

## dyadic-discrepancy-euclid — Verdict: CHANGES REQUESTED — Status: partial (GAP U SOLVED)

Same upper-bound result by an **independent route**: Theorem R (Abs-Difference Reachability),
`min Reach(U) = m*_±(U) = min_{ε∈{±1}^U}|Σ ε_i x_i|` — the minimum **all-signs** subset sum is
realizable by pinning `U` to a single coin in `|U|−1` pins — plus the same Subset-Sum
Pigeonhole (§B) and the trivial fewer-marks case (§F). §E op-budget accounting: `(n+1−s)`
bisects + `(s−1)` pins `= n` cuts exactly, never binding. The Theorem R sign-pairing induction
(`m*_±(U'')=m*_±(U)` via the constrained-min argument) is correct.

**Independent verification (mine):** Theorem R (`min Reach(U)=m*_±(U)`) — **0 mismatches**
over 500 random multisets (`|U|≤6`, exact arithmetic). *Caveat for the record:* the lemma
compares to `m*_±` (all ±1, no zeros), NOT `m*` (zeros allowed) — my first test wrongly used
`m*` and produced spurious mismatches; with the correct `m*_±` it is exact. On `U₀` = the
support of the global `{−1,0,1}` minimizer, all signs are nonzero, so `m*(x)=m*_±(U₀)` (§B
support argument) and Theorem R applies correctly.

Status accurate (upper bound closed, GAP L imported/open). This is a genuine but
**near-duplicate** framing of the dyadic twin (both = subset-sum pigeonhole + realizability).
For the population, keep ONE as the certified upper-bound owner; this twin is redundant now.
Scores — Correctness 10/10, Rigor 9.5/10, Progress: major (independent confirmation).

---

## induction-recursion-telescope — Verdict: CHANGES REQUESTED — Status: partial (GAP L open)

Leader on the lower-bound wall. New this round: the **exact threshold-split identity (△)**
`D̃(F) = (y₁−θ)⁺ + λ_{(0,θ)}(O_Y△O_Z)` (a genuine equality refinement of the round-2
inequality (★★); proof via `1[N_F odd]=1[t∈O_Y△O_Z]` and the half-total single-crosser fact —
correct), collapsing Case B to the **bounded-mass localized inequality (△⋆)**
`λ_{(0,θ)}{M odd} ≥ 1−β`. Plus a refuted reserve shape (§14: "Z's odd measure leads its even
measure from the top" is FALSE, surplus is bottom-inclusive/near-0). The certified Lemma T
(maxc≤1 core) stands. **GAP L residual `E(F) ≤ 2^n−1` ⇔ (♠≥0) ⇔ (△⋆) is NOT proven** — the
builder is honest about this. Real progress (sharper equivalent reductions, another dead-end
mapped), no overclaim. Remaining gap: prove the residual via Z's dyadic cut-tree by a global,
bottom-inclusive count-parity amortization (local matching, scalar/count summary of Z, and
top-down reserve of Z are all refuted). Scores — Correctness 10/10, Rigor 9/10, Progress:
incremental (residual sharpened, not closed).

---

## induction-recursion — Verdict: RETHINK — Status: partial→reframe (GAP L wall shared)

Same GAP-L wall via the budget-count reduction `O_B ≥ E_A`. This round drove it to exhaustion:
(E1) the natural **termwise** closure `|A_{2j}| ≤ |B_{2j−1}|` is **provably FALSE** (explicit
witness `n=4,a=b=2`), (E2) the tight `maxc≥2` boundary is isolated to `b≥1` near-tie configs,
and the builder **itself raises an ESCALATION FLAG** (E3): the framing is at the same wall as
telescope's Step-5 and needs a genuinely different framing, not a 4th attack on `O_B≥E_A`.
No gap closed; a natural sub-route is killed. Per CLAUDE.md this is a shared-gap plateau twin
that has bottomed out — send it back to the outliner to re-plan (RETHINK), keeping telescope as
the live GAP-L owner. The proved facts (super-level reduction, deficit budget/localization,
conservation) remain valid and are subsumed by telescope's cleaner equivalents. Scores —
Correctness 10/10 (what's written), Progress: negative-result only (framing dead-ended).

---

## Lemmas certified this round

- **`lemmas/upper-bound.md` (NEW, CERTIFIED):** the entire general-n upper bound
  `c(n) ≤ 2^n/(2^{n+1}−1)`, with its load-bearing sub-lemmas (Invisible-Pair, removal ops +
  physical decomposition, Realizability Lemma / Theorem R, Subset-Sum Pigeonhole). Reviewer-
  verified end-to-end. This is the upper-bound half of P3. Both twins prove it independently.
- Not separately certified (folded into the above, or already certified): pivot-lemma.md,
  termwise-lattice.md, greedy-claim.md, cut-flip.md stand as before.
- Telescope's (△) threshold-split identity and (♠) position-parity identity are correct and
  reusable, but I hold them uncertified this round pending their use in an actual GAP-L
  closure (they are equivalent restatements of the still-open residual, not a closure).

## Bottom line

Answer `c(n)=2^n/(2^{n+1}−1)` established as correct; **upper bound proven & certified for all
n**; problem status `partial` — the sole remaining wall is lower-bound Case B (GAP L). Next
round: point the GAP-L closure at telescope (global amortization through Z's cut-tree), reframe
induction-recursion, and consider merging the two now-redundant upper-bound twins.
