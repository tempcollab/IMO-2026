# imo-2026-03 — proof-outliner field (round 1)

## Problem & answer

Liu Bang marks ≤n points, Xiang Yu marks ≤n distinct points, stick cut into pieces, players alternate claiming (Liu first) maximizing own total. Find largest c(n) Liu guarantees.

**Conjectured answer (verified n=1,2,3 by exhaustive/grid):** `c(n) = 2^n / (2^{n+1} − 1)` (= 2/3, 4/7, 8/15, 16/31, …; → 1/2).

## Shared reduction (every approach imports this as Lemma 0)

**Lemma 0 (claim game = odd-index sum).** For a fixed multiset of pieces sorted descending `a_1 ≥ … ≥ a_m`, optimal play (Liu first, zero-sum, pick-any-piece) gives Liu exactly `a_1 + a_3 + a_5 + …` (odd-index sum). Equivalently `(1+D)/2` where `D = a_1 − a_2 + a_3 − …` is the alternating sum. Greedy "always take largest" is optimal for both.
- *Mechanism:* exchange argument — at any node, if the mover deviates from the largest piece `a_1` and takes `a_j < a_1`, the opponent immediately takes `a_1`; by backward induction the deviation never helps. Verified: full minimax matches odd-index sum on 3000+ random multisets.
- *Gap:* needs a clean induction proof (the builder writes it; it's standard but must be proven, not asserted).

**Consequence:** `c(n) = max_{Liu ≤n marks} min_{Xiang ≤n marks} [odd-index sum of sorted(final multiset)] = (1 + D*)/2`, where `D* = 1/(2^{n+1}−1)` is the target. Xiang's marks only REFINE Liu's pieces (split each into subpieces, then re-sort).

**KEY CORRECTED FACT (flagged for all approaches):** the naive "superincreasing ⇒ refinement can't drop odd-index sum below the top piece" lemma is **FALSE**. Counterexample: `{3,1}/4` (superincreasing, 3>1), split `3→1.5+1.5` gives `{1.5,1.5,1}/4`, odd-index = `1.5+1 = 0.625 < 0.75 = a_1`. The full dyadic TOWER `{2^n,…,2,1}` IS special (n=1,2,3 exhaustively verified to resist: odd-index ≥ `2^n/(2^{n+1}−1)` under every refinement). The lower-bound lemma must exploit the tower's self-similar structure, not a generic dominance inequality.

---

## Approach 1: `tower-induction` — new

**Framing.** The dyadic tower is the extremal Liu config; prove it resists refinement (lower bound) and that Xiang can match it for any config (upper bound), both by induction on n with a case split on whether Liu's largest piece dominates the rest.

**Lower-bound architecture.**
1. Liu places marks producing the tower `(2^n, 2^{n−1}, …, 2, 1)/(2^{n+1}−1)` (marks at cumulative sums `(2^k−1)/D`).
2. **Lemma L (tower resists refinement):** for the tower `T_n = (2^n,…,1)/D_n` (`D_n=2^{n+1}−1`), any Xiang refinement leaves odd-index sum `≥ 2^n/D_n`.
   - *Mechanism (induction on n, self-similarity):* the top piece `2^n` exceeds the entire rest (`2^n > 2^n−1 = sum of smaller`). Xiang's refinement either (a) leaves the top piece unsplit → it occupies slot 1 (odd) and the rest, being a rescaled copy of `T_{n−1}`, contributes `≥ 2^{n−1}/D_{n−1}` by IH after rescaling; or (b) splits the top piece into fragments. In case (b), every fragment `≥ 2^{n−1}` (the second piece) occupies a top slot; the sub-structure `T_{n−1}` among the remaining pieces still resists by IH. The tower's "each piece = 1 + sum of all smaller" pins the parity of how fragments interleave with the existing tower.
   - *Gap:* the exact inductive statement for case (b) — how fragments of the split top piece interleave with `T_{n−1}` and why the odd-index sum stays `≥ 2^n/D_n`. This is the load-bearing hard step. (n=1,2,3 case-checks confirm the boundary.)
3. Conclusion: Liu guarantees `≥ 2^n/D_n`.

**Upper-bound architecture.**
1. **Lemma U (induction on n, dominance case split).** For any Liu config (≤n+1 pieces summing to 1), Xiang has ≤n marks forcing odd-index sum `≤ 2^n/D_n`.
2. Let `L` = Liu's largest piece, `R = 1−L` (rest).
3. **Case (i): `L ≥ 2^n/D_n` (dominant).** Xiang splits `L`. Generalize the n=1 rule: split the dominant piece so its fragments + the rest give odd-index `≤ 2^n/D_n` (n=1: split `L≥2/3` into halves → `(1+L)/2 ≤ 2/3`? — re-derive the exact split). Use IH on the rest (≤n−1 marks) to bound the rest's odd-index contribution.
4. **Case (ii): `L < 2^n/D_n` (non-dominant).** All pieces `< 2^n/D_n`. Xiang marks nothing (or splits small pieces) and show odd-index sum `≤ 2^n/D_n` directly — *this is the wall* (see risk). For n=1 this works (2 pieces, odd-index = `L < 2/3`), but for large n with many pieces a direct count is too weak (could exceed target).
5. Recurrence `c(n) = 2^n/D_n` falls out of the IH `c(n−1) = 2^{n−1}/D_{n−1}` and the case split.

**Biggest risk.** Case (ii) of the upper bound: when no single piece dominates, the "mark nothing" response gives odd-index sum `≤ 2^n/D_n` is FALSE for many small equal pieces (odd-index can be `≈ 1/2 + small`, and `2^n/D_n → 1/2`, but for small n the gap `2^n/D_n − 1/2 = 1/(2D_n)` is tiny — needs a sharp bound, not a coarse one). The induction's "else" branch is the single wall.

**Gaps / hard steps (builder fills):**
- Lemma 0 (greedy = odd-index): clean exchange-argument proof.
- Lemma L (tower resists): the case-(b) inductive step for split top piece. *Hardest part of lower bound.*
- Lemma U case (ii): the non-dominant upper bound (may need a different sub-argument — pairing, or a weight bound borrowed from approach `d-potential`).

**Cases to cover:** n=1 (proven by hand, base case); inductive step n→n+1; both dominance cases.

**Watch out for:** the "naive halve-the-largest" Xiang strategy FAILS for near-equal Liu configs (recorded dead end) — the case split must route non-dominant configs to a different response. The `{3,1}/4` counterexample shows "superincreasing" alone is insufficient.

---

## Approach 2: `d-potential` — new

**Framing.** Work with the alternating sum `D = a_1 − a_2 + a_3 − …` (target `D* = 1/(2^{n+1}−1)`, since `c = (1+D)/2`). Find a weight/potential `Φ` on the sorted multiset that (a) upper-bounds `D`, (b) Liu can drive to `1/D_n` via the tower, (c) Xiang can reduce by a controlled factor per mark. The "base-2 place value" of the sorted list is the candidate `Φ`.

**Lower-bound architecture.**
1. Liu plays the tower. After Xiang's BEST response (split top piece into `{2^{n−1},…,2,1,1}/D_n`), the multiset is `{2^{n−1},2^{n−1},…,2,2,1,1,1}/D_n` (pairs + triple-1); `D = 1/D_n` exactly (verified). So `Φ ≥ D = 1/D_n` is attained — Liu forces `D ≥ 1/D_n`, i.e. `c ≥ 2^n/D_n`.
2. *Mechanism:* the tower saturates `Φ` — it is the config maximizing `min_{refine} Φ`, a fixed point of Xiang's reduction.

**Upper-bound architecture.**
1. Define `Φ(a_1,…,a_m) = Σ_{i} s_i a_i` for explicit signs/weights `s_i` (candidate: `s_i = (−1)^{i+1}` gives `D` itself; the nontrivial candidate is a *base-2 weighted* sum `Φ = Σ 2^{-i}·(stuff)` that dominates `D` and decreases cleanly under splits — the exact form is the gap).
2. **Lemma P1:** `Φ ≥ D` for every multiset (so bounding `Φ` above bounds `D`).
3. **Lemma P2 (one-mark decay):** for any multiset, Xiang has a mark making `Φ(new) ≤ Φ(old) − δ(Φ)` with a quantified decay; after ≤n marks `Φ ≤ 1/D_n`.
4. The dyadic denominator `D_n = 2^{n+1}−1` (not `2^n`) must emerge from the decay+initial bound. The doubled-1 terminal (three 1's in the equality config) is where the `−1` in `2^{n+1}−1` enters — pin this.

**Biggest risk.** Finding the exact `Φ` whose per-mark decay produces the denominator `2^{n+1}−1` (the naive "halving per mark" gives `2^n`, which is too strong and false for the tower). The potential must capture the residual `1/D_n` the tower holds. If `Φ = D` itself, the decay lemma is just "Xiang reduces D" restated — not progress.

**Gaps / hard steps:**
- Lemma 0 (shared).
- The definition of `Φ` and Lemma P1 (`Φ ≥ D`).
- Lemma P2 (one-mark decay with the exact `2^{n+1}−1` denominator). *Hardest step.*
- Verify the tower saturates `Φ` at `1/D_n`.

**Watch out for:** a potential that only yields `D ≤ 1/2^n` is useless (the tower achieves `1/D_n > 1/2^{n+1}`, so `1/2^n` is too strong/untrue). The `−1` correction is the crux.

---

## Approach 3: `tail-count` — new

**Framing.** Rewrite the odd-index sum as a threshold integral (layer-cake), inspired by the aimo-0127 crux (rewrite a weighted alternating total as a sum over thresholds of tail-counts, apply a per-threshold cap termwise).

**Identity (the spine):** For `N(t) = #{pieces of length ≥ t}`,
```
odd-index sum = ∫_0^∞ ceil(N(t)/2) dt.
```
*Reason:* pieces of length `≥ t` are the top `N(t)` pieces; `ceil(N(t)/2)` of them sit in odd positions.

**Lower-bound architecture.**
1. Liu plays the tower. Show that under any Xiang refinement, `∫ ceil(N(t)/2) dt ≥ 2^n/D_n` — i.e. Xiang cannot drive the integral below the tower value.
2. *Mechanism:* the tower's `N(t)` has a step structure with jumps at `t = 2^k/D_n`; splitting pieces can only `+1/−1` adjust `N(t)` in ranges, and the ceiling makes the integral decrease by at most the tower gaps. (This re-proves Lemma L in the `N(t)` language — distinct from `tower-induction`'s sorted-list induction.)

**Upper-bound architecture.**
1. For ANY Liu config, Xiang chooses marks so `∫ ceil(N(t)/2) dt ≤ 2^n/D_n`.
2. **Effect of one Xiang mark** (split piece `L` into `p≥q`, `p+q=L`): `N(t)` changes by `−1` on `t ∈ (p, L)` and `+1` on `t ∈ [0, q]`. The net change in `∫ ceil(N/2) dt` is
   - `−1` on `(p,L)` when `N(t)` is odd there (odd→even drops `ceil` by 1),
   - `+1` on `[0,q]` when `N(t)` is even there (even→odd raises `ceil` by 1).
3. Xiang picks the split making the `−1` ranges (odd `N`) outweigh the `+1` ranges (even `N`); telescope over ≤n marks to bound `≤ 2^n/D_n`.
4. The `2^{n+1}−1` denominator comes from the layer-cake of the tower: the threshold levels `2^k/D_n` and the parity structure of `N(t)` at each layer.

**Biggest risk.** The parity bookkeeping across interleaved `t`-ranges is intricate; `N(t)` is a step function and parities shift globally when one piece is split (resorting changes which pieces are "≥ t"). A clean per-threshold cap (as in aimo-0127) requires `N(t)`'s parity to be controllable mark-by-mark, which may not hold for arbitrary Liu configs.

**Gaps / hard steps:**
- Lemma 0 (shared).
- Prove the layer-cake identity rigorously (it's a standard tail-sum identity but must be justified).
- Lower bound in `N(t)` language: tower resists (distinct from `tower-induction`'s mechanism — this is the integral version).
- Upper bound: the parity-telescoping lemma (one-mark net change `≤ 0` after choosing the split), then summing over n marks to get `1/D_n`. *Hardest step.*

**Watch out for:** `N(t)` depends on the GLOBAL sorted order; splitting one piece reshifts parities at many thresholds simultaneously, so "per-threshold" control is not independent. The aimo-0127 crux had independent thresholds; here they're coupled.

---

## Approach 4: `self-similar` — new

**Framing.** The tower's self-similarity: the top piece `2^n/D_n` and the rest `(2^n−1)/D_n` which, rescaled by `D_n/(2^n−1)`, is exactly `T_{n−1}` with denominator `D_{n−1}=2^n−1`. This gives a recurrence for BOTH bounds by reducing the n-game to the `(n−1)`-game on the rest.

**Lower-bound architecture.**
1. Liu plays `T_n`. The top piece `2^n` exceeds the whole rest (`2^n−1`), so no fragment of a split top piece can be "buried" below the rest unless it is `< 2^{n−1}`; fragments `≥ 2^{n−1}` lock into the top slots.
2. **Lemma S (lower, self-similar):** `min_{Xiang} odd-index(T_n refined) = 2^n/D_n`. Split into: Xiang ignores the top piece → odd-index `≥ top + (rest bound)`; Xiang splits the top piece → the fragments dominate and the rest (rescaled `T_{n−1}`) resists by IH giving `≥ 2^{n−1}/D_{n−1}` in rescaled units `= (2^n−1)/D_n`, plus the top fragments' contribution, totaling `2^n/D_n`. (Numerical: tower rest-sum `(2^n−1)/D_n`, rescaled is `T_{n−1}`; IH gives rest odd-index `≥ 2^{n−1}/D_{n−1}`, and `2^{n−1}/D_{n−1} · (2^n−1)/D_n / ((2^n−1)/D_{n−1}) = 2^{n−1}/D_n`… — the builder fixes the scaling.)
3. Recurrence `c(n) = top piece = 2^n/D_n`.

**Upper-bound architecture.**
1. For ANY Liu config, Xiang reduces to the `(n−1)`-subgame. Identify Liu's largest piece `L` and the rest (sum `1−L`).
2. **Lemma S' (upper, self-similar):** Xiang spends one mark to split `L` (or its dominant fragment) so that Liu's odd-index take from `L`'s vicinity is `≤ L'` (controlled), and applies the `(n−1)`-strategy (IH) to the rest (rescaled), giving rest odd-index `≤ c(n−1)·(rescale)`.
3. Solve the recurrence `c(n) = L' + c(n−1)·(rescale)` with `c(n−1)=2^{n−1}/D_{n−1}` to get `c(n)=2^n/D_n`.

**Biggest risk.** The upper-bound reduction "the rest IS an `(n−1)`-subgame" is only literally true for the TOWER rest, not for an arbitrary Liu config's rest. For arbitrary configs the rest may not have tower structure, so IH-on-rest doesn't directly apply. This approach may prove the lower bound cleanly but stall on the upper bound (sharing `tower-induction`'s upper-bound wall). Mitigation: combine with an extremal argument (the tower is the worst case for Xiang — any non-tower config is easier) — but that extremal claim is itself hard and is approach `tower-induction`'s case (ii) in disguise.

**Gaps / hard steps:**
- Lemma 0 (shared).
- Lemma S (lower self-similar): the rescaling/induction. *Promising for the lower bound.*
- Lemma S' (upper): reducing an arbitrary config to the `(n−1)`-subgame. *Main wall — may fail for non-tower configs.*
- The extremal "tower is worst case" sub-lemma if Lemma S' stalls.

**Watch out for:** the rest of an arbitrary Liu config is NOT a rescaled tower; the self-similar reduction is exact only for the tower. Do not assume it transfer.

---

## Approach 5: `balanced-configs` — new

**Framing.** The odd-index sum is piecewise-linear in Xiang's mark positions; its minimum over the continuous action space is attained at a "balanced" config (a tie: two subpieces equal, or a subpiece equals an existing piece). This reduces Xiang's continuous optimization to finitely many combinatorial types of balanced refinements; verify each type gives odd-index `≤ 2^n/D_n`.

**Lower-bound architecture.**
1. Liu plays the tower; import Lemma L (tower resists) — OR re-prove via the same piecewise-linearity (the tower's resistance is that every balanced refinement still yields `≥ 2^n/D_n`; this is a finite type-check the builder does for general n by structural induction on the types).

**Upper-bound architecture.**
1. **Lemma B1 (extremal-at-ties):** for fixed Liu config and fixed "split pattern" (which Liu-pieces get how many Xiang marks), the odd-index sum is piecewise-linear in the mark positions; a minimum is at a breakpoint where some two subpieces are equal (or a subpiece hits a Liu-piece boundary value).
2. **Lemma B2 (finite types):** consequently the global minimum over Xiang's ≤n marks is attained at a balanced refinement — a multiset where every split produces equal halves or matches an existing piece. There are finitely many combinatorial types of such balanced refinements for each n.
3. **Lemma B3 (each balanced type ≤ target):** structurally verify, for every balanced refinement type, that the odd-index sum `≤ 2^n/D_n` (for the upper bound) and, for the tower, `≥ 2^n/D_n` (for the lower bound). The dyadic equal-halving pattern `{2^{n−1},2^{n−1},…}` is the extremal type (attains equality); all other balanced types are `≤` it.
4. The `2^{n+1}−1` denominator is the total of the extremal balanced tower.

**Biggest risk.** The number of balanced combinatorial types may explode with n; a structural (not exhaustive) argument is needed, and "all balanced types ≤ the dyadic one" is essentially the extremal claim that is the whole upper bound in disguise. If the type enumeration can't be made structural, this collapses into casework that only small n survives.

**Gaps / hard steps:**
- Lemma 0 (shared).
- Lemma B1 (extremal-at-ties): the piecewise-linearity + min-at-breakpoint argument (related to kb "Piecewise-concavity smoothing" / "min at a breakpoint").
- Lemma B2 (finite types): bounding the type count structurally.
- Lemma B3 (each type ≤ target): the structural comparison to the dyadic balanced type. *Hardest step; may be the upper bound restated.*

**Watch out for:** this is the riskiest framing — it risks reducing to a finite check that doesn't generalize. Keep it as a verification/scaffold for small n and a source of the extremal type, not the main upper bound.

---

## Field summary (slugs + one line each)

- `tower-induction` (new): dyadic tower resists refinement (lower) + induction on n with dominance case split (upper). Main line; wall = non-dominant upper-bound case.
- `d-potential` (new): alternating-sum `D` with a base-2 weight potential `Φ≥D` that Xiang decays per mark to `1/D_n`. Wall = the exact potential giving the `−1` in `2^{n+1}−1`.
- `tail-count` (new): odd-index sum `= ∫ceil(N(t)/2)dt`; Xiang's splits shift `N(t)` parity per threshold, telescoping to the bound (aimo-0127 crux adapted). Wall = coupled global parities.
- `self-similar` (new): tower rest rescales to `T_{n−1}`; recurrence `c(n)=top piece` for both bounds. Wall = upper bound for non-tower configs (rest is not a subgame).
- `balanced-configs` (new): piecewise-linearity ⇒ Xiang optimum at balanced (tie) refinements ⇒ finite types ⇒ structural check `≤` dyadic type. Wall = type explosion / extremal claim restated.

## Branching recommendation

None at round 1 (no existing approaches to copy). If `tower-induction`'s Lemma U case (ii) and `d-potential`'s Lemma P2 both survive round 2 with two viable sub-routes each, branch then.

## build set (recommendation)

`tower-induction`, `d-potential`, `tail-count`, `self-similar` (4 builders, one per slug — the four most distinct upper-bound mechanisms). Hold `balanced-configs` in reserve (riskiest; deploy next round if the upper bound stalls on all four). The outline-reviewer finalizes.
