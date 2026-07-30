# Proof-reviewer — imo-2026-03, round 18

## Approach reviewed: `breakpoint-vertex` (UPPER)

### Verdict: CHANGES REQUESTED — Status: partial (approach stays live; C2 sub-lever dead)

Builder's recorded Status (`partial`, C2 gate FAILED, no new prose) is **correct and not overclaimed**.
This is an honest gate-failure + no-fake-proof, which is the required behaviour. I APPROVE nothing
(the problem is not solved), and I confirm the mechanism death independently.

---

## Independent verification (exact `Fraction`, my own script — not the builder's)

Re-derived the load-bearing witness from scratch:

- **`u_4 = 1/31` confirmed** as `1/(2^{n+1}−1)` with `n=4`; equivalently `2^n/(2^{n+1}−1) = 16/31 = c(4)`.
- **Witness `A = {1/3, 13/40, 13/40, 1/120, 1/120}`**: `L = 1` exactly, `a₁ = 1/3`. Deep-region bound
  `(L−u_nL)/2 = 15/31`; `1/3 = 20.67/62 < 30/62 = 15/31`, so **`A` is genuinely deep** (strictly interior,
  WTC vacuous). ✓
- **True `Φ = 0`**: my exhaustive min over all 31 nonempty subsets of `descKK` returns `0`, achieved by
  subset `{13/40, 13/40}` (indices 1,2), which **excludes the anchor `a₁ = 1/3`**. `descKK(13/40,13/40) = 0`
  by one even cancellation — trivially DM-tree-realizable (one cut cancels the equal pair; the remaining
  three pieces DELETEd within the `n=4` budget, per certified R-COV'/ESF-2). ✓
- **Anchored reflected walk**: full descending walk `w = [1/3, 1/120, 19/60, 37/120, 3/10]`. Band-landing
  crossing at `P = 13/40+13/40 = 13/20 ≥ a₁` (builder's `k*=3`, my loop index 2 — pure indexing offset,
  same point). **`minpost = min_{k≥k*} w_k = 3/10`**, ratio `= (3/10)·31 = 93/10 = 9.3·u_4`. ✓

So the gate failure is **real, not an artifact**: the anchored post-crossing residual saturates at
`9.3·u_4` while the true minimiser is `0`, attained by a tail-only subset that no `a₁`-anchored pass can
reach. The `minpost/u_n` growth (4.5/9.1/13.9/24.3 at n=3..6) is the covering-radius signature and matches
the already-dead GAP TWO-CAP (3.2/6.1/8.9/15.8/24.6). Confirmed the same dead family in disguise.

**Root cause is structural, so the mechanism is dead as a class, not as a parametrisation.** `minpost`
already minimises over *all* post-crossing stopping points of the anchored walk, so no "smarter stopping
rule" survives — the failure is that every prefix of the anchored walk contains `a₁`, whereas the true
minimiser (`{13/40,13/40}`; cf. R17 `{30,25,20,15,10}/100` needing a 4-element tail subset) can exclude
`a₁` entirely. This is the anchor-excluding-tail root cause the dispatch asked me to test — it is
**genuine**. Any single `a₁`-anchored descending pass is therefore provably insufficient. Correctly the
**9th dead upper mechanism**.

Minor note (does not affect verdict): the clean witness gives `9.3·u_4`, slightly *above* the reported
random-sample worst `9.0932` — consistent (the constructed adversarial point simply beats the random
sweep), and only strengthens the refutation. Not a contradiction.

## Certified core — untouched and intact

I confirm the builder shipped no new prose and touched none of the certified content. Lemma **WTC**
(whole-tail continuation, `descKK ≤ |2a₁−L|`, boundary layer `(L−u_nL)/2 ≤ a₁ < L/2` closed exactly),
**R-COV'** (sufficiency), **FGR**, **ESF-2** all stand as previously certified. No new promotable lemma
was flagged this round, so nothing to certify/reject. The answer `c(n) = 2^n/(2^{n+1}−1)` is unchanged.

## Scores

- **Correctness:** high — the negative result is exact-arithmetic-verified and I reproduced it
  independently; no false claim shipped.
- **Completeness/rigor:** the round is a rigorous *refutation*, not a proof; honestly recorded. No
  hand-waving, no skipped case, no overclaim. The problem itself remains unsolved.
- **Progress:** modest but real — prunes a live-looking lever (the sharpened-WTC/reflected-walk
  contraction) as the covering-radius family in disguise, preventing future rounds from re-treading it.

## True Status: partial — precise open residual

Deep-interior / near-boundary sliver residual **`Φ(A) = min_{∅≠T} descKK(T) ≤ u_nL` for
`a₁ < (L−u_nL)/2`** remains OPEN. The residual is asymptotically tight (VALLEY-TIGHT, `Φ/u_n → 1` in the
sliver), so only an *exact* argument can work, and it must be an object that sees **tail-only subsets
excluding `a₁`** — no anchored walk / covering-radius / caterpillar contraction can (proven dead ×several).

## Routing rationale (CHANGES REQUESTED vs RETHINK)

I rule **CHANGES REQUESTED**: the *approach* `breakpoint-vertex` is not fatally broken — it carries a
certified reduction and the exact WTC boundary closure (permanent, genuine advance), and remains the Elo
leader. Only the C2 reflected-walk **sub-lever** died. Because no builder move remains *within the current
anchored/contraction framing*, the CHANGES-REQUESTED instruction to the next round must route the
deep-interior residual to the **outliner for a genuinely different object** — the Steinitz /
vector-balancing / signed-subset-sum **existence** bound over all tree-realizable signings (Lemma RL):
prove `∃ ∅≠T` with `|Σ_{i∈T} ε_i a_i| ≤ u_nL`, an existence statement that can land on a tail-only
subset. Do **NOT** re-seed any anchored-caterpillar / post-crossing-reflected-walk / covering-radius
contraction — proven dead as a class. This matches the plateau-break call (9 dead upper mechanisms all
sharing the anchored/aggregate wall → need a genuinely new framing).

## Goal Progress (for Eval History)

- Leader `breakpoint-vertex` Elo **1847.3** (expanded 11, selected 8; last_outcome dead-end, stale).
- Open residual (precise): deep-interior/sliver `min_{∅≠T} descKK(T) ≤ u_nL` for `a₁ < (L−u_nL)/2`;
  tight (`Φ/u_n → 1`), needs an existence/discrepancy object over tree-realizable signings, not an
  anchored walk.
- Upper wall: boundary layer CLOSED (WTC); 9 upper mechanisms now dead. Lower wall: no live vehicle.
- No APPROVE this round. Status remains **partial**.
