# Round 9 adversarial proof review — imo-2026-03 (IMO 2026 P3 stick-cutting game)

Reviewed all three built slugs: `recursive-embedding-induction`,
`geometric-dominance-construction`, `universal-adversary-strategy`.
Every claim below was independently re-derived with fresh, from-scratch
Python (exact `fractions.Fraction`), never by re-running the builders' own
scripts.

## 1. `recursive-embedding-induction` — Lemma TREE-BOUND-RESIDUAL

**Claimed:** gap (b) (cross-piece tied free coordinates) is now FULLY
closed via a third induction case (Case C) added to the certified
Sub-lemma ODD, using only the already-certified Lemma D-BOUND, closing
the "minority part of a 2-part-split piece tied at a deep external
anchor" residue. Also claims the round-9 plan's proposed "virtually fully
split" comparison mechanism was found FALSE (159/600 violations).

**Verification.** Re-implemented the forest-with-at-most-one-impurity
construction directly from the lemma's own definitions (independent of
the builder's scripts): `pure(e)` / `impure(e)` generators building every
achievable leaf-multiset of a binary-subdivision tree rooted at exponent
`e`, with at most one node in the whole `(m,r)`-forest allowed to make one
"impure" cut `τ_i→(τ_j, τ_i−τ_j)`. Exhaustively enumerated every tree
shape and every impurity placement for `(m,r) = (1,3),(2,3),(3,3),(4,3)`
(576–56,000 configurations depending on `m`): **minimum `D` found is
exactly `τ_m=1` in every case, zero violations.** This independently
confirms the lemma's induction step (Case C) is correct for the stated
scope.

**Finding (load-bearing).** The lemma's own hypothesis is "**at most one**
impure node in the entire forest," and the induction proof genuinely
relies on this (the remainder after peeling the top level again has ≤1
impurity only because the whole forest started with ≤1). **Neither the
lemma file nor the round-9 build report addresses or even flags the case
of two or more simultaneous, independent tie-clusters** (e.g. two
disjoint pieces each independently tied to a *different* external
anchor at once — a legitimate Xiang-Yu move using more of his budget).
I stress-tested this directly: for `n=2..6`, constructing configurations
with 2, 3, and 4 simultaneously-split pieces each tied (independently, at
different values) to an external anchor in its own minority range, over
dense grids (up to 24 points per free value, up to 21,875 configurations
checked) — **no violation of `D≥t_n` was found** (minimum values found
were comfortably above `t_n`, e.g. `17/16, 3/2, 4, 9/2, 55/6, ...` never
close to `1`). This is reassuring numerical evidence but **not a proof**
of the multi-cluster case, which is exactly the kind of case CLAUDE.md's
"no skipped cases" rule flags. **Verdict: the "gap (b) fully closed"
claim is over-broad; downgrade to "single-cluster case closed."**

## 2. `geometric-dominance-construction` — Lemma TWO-BLOCK

**Claimed:** an independent, second closure of the same gap (b) residue
sub-case via a direct two-block `D`-BOUND estimate (Lemma TWO-BLOCK, fully
general) plus a Structural Lemma identifying the two globally-largest
merged elements, for every `v` in the legal minority range (not just the
`D`-minimizing endpoint).

**Verification.** Independently re-implemented the construction from
scratch: for `n=1..6`, every subset `S⊆{0,...,n}` with `|S|≥2`, dense
`v`-grids (up to 50 points) within the legal minority range — `D≥t_n` in
every one of thousands of checked configurations, zero violations. This
is genuinely a different mechanism from `recursive-embedding-induction`'s
route (single shared `v` across an arbitrary subset `S`, vs. a
one-impurity forest), not circular, and not contradicting the sibling
route on any tested case (both reproduce the two cited numeric witnesses,
`n=4` symmetric two-minority tie and `n=6` external-anchor-snap,
exactly).

**Finding.** Same scope limitation as above: the Main Theorem is stated
for **one** shared tie-value `v` across **one** subset `S` — it does not
address two-or-more simultaneous independent clusters at different `v`
values, and (like the sibling file) does not flag this as a remaining
caveat. My multi-cluster stress test (shared with the sibling approach's
review) found no counterexample. **Verdict: same downgrade — closes the
single-cluster case; the multi-cluster case is an unaddressed, likely-true-
but-unproved residual gap.**

## 3. `universal-adversary-strategy`

### (a) `m=3` Case C, corrected `BLOCK-RECURSE_1` and 2-case algebra

**Claimed:** a round-8 labelling error is corrected (`L0={r,p3}`, not
`{p2,r}`), and the corrected closed form, combined with a 2-sub-case
algebraic argument (Sub-case B1: `p3≤2(p1−p2)`, giving `1−p1≤4/7`;
Sub-case B2: `p3>2(p1−p2)`, giving `p1+p3/2<4/7`), closes `m=3`'s Case C
(`p1<Σ/2`) in full, unconditionally.

**Verification.** Independently re-derived the corrected `BLOCK-RECURSE_1`
formula by directly simulating the actual construction (split `p1` into
`(p2,r)`, then apply the certified `n=1` result — "do nothing" or "halve
the max" — to the leftover `L0={r,p3}`), confirming
`oddrank(L0)=min(p3, p3/2+r)` and the two closed-form sub-cases match
exactly. Reproduced both worked examples exactly:
`(0.45,0.275,0.275)`: TAIL-SNIP `0.5875`, BLOCK-RECURSE₁ `0.55` (matches);
`(0.4,0.35,0.25)`: both `0.525` (matches the round-9 correction of the
round-8 error, which had wrongly given `0.575`). Ran a fresh 3,000-trial
exact-`Fraction` random search over `p1<1/2`: **zero violations** of
`min(TAIL-SNIP, BLOCK-RECURSE₁)≤4/7`; the extremal point
`(3/7,2/7,2/7)` gives exactly `4/7=4/7` for both candidates, matching the
claimed tight case. **`m=3`'s general upper bound is genuinely, fully
closed — no issues found.**

### (b) Lemma PAIR-VALUE and the `m=5` witness

**Claimed:** a new, general, hypothesis-free lemma (any decomposition into
tied pairs plus an unpaired remainder has `oddrank = Σ(pair values) +
oddrank(remainder)`, no domination/contiguity needed), whose SUBSET-DOM
corollary closes the concrete `m=5` falsifying witness
`A=(12,6,5,4,2)/29` (budget 4) via a genuinely non-prefix match (`p2` to
`{p4,p5}`, skipping `p3`), but does **not** establish general `m≥4` Case C.

**Verification.** Re-derived Lemma PAIR-VALUE's induction independently
and stress-tested with 5,000 random trials (small-integer values, forced
coincidences to stress the tie-insensitivity argument) — zero mismatches.
Independently recomputed the witness construction (match `p2↔{p4,p5}`,
`r=0` so 1 mark; halve `p1`, 1 mark; halve `p3`, 1 mark; 3 marks total
`≤4`): sorted final multiset `[6/29,6/29,4/29,4/29,5/58,5/58,2/29,2/29]`,
`oddrank = 1/2` exactly, beating `c(4)=16/31≈0.516` and beating the old
certified menu's best value on this witness (`15/29≈0.517>c(4)`, also
independently confirmed). **The file correctly and honestly does not
claim the general `m≥4` existence theorem is established** — this is an
accurate self-assessment, not overclaiming. **No issues found.**

## Overall assessment: what the lower bound vs. upper bound distinction
actually means here

Per the mandated check: the problem's target is
`c(n) = max_A min_B oddrank(B)`. The **lower bound** direction
(`c(n) ≥ 2^n/(2^{n+1}-1)`) requires exhibiting **one** configuration
(`A_n`) whose value against every Xiang-Yu response is `≥` the target —
this is exactly what `recursive-embedding-induction` /
`geometric-dominance-construction`'s gap (a)+(b) work establishes (modulo
the multi-cluster caveat above). The **upper bound** direction
(`c(n) ≤ 2^n/(2^{n+1}-1)`) requires the separate, universal claim that
**no** configuration `A` (geometric or not) lets Liu Bang do better — this
is `universal-adversary-strategy`'s target, and it is genuinely a
different, independent piece of work, not implied by or a byproduct of
the lower-bound closure. **"No other config beats `A_n`" is precisely
this separate upper-bound piece, not part of the lower bound**, and it
remains open for general `m≥4` even after this round's `m=3` closure.
`current.md`'s status language has been revised to state this precisely.

## Routing decisions (per CLAUDE.md's per-approach independent routing)

- **`recursive-embedding-induction` — CHANGES REQUESTED.** Genuine,
  independently-verified progress (Lemma TREE-BOUND-RESIDUAL correctly
  closes the single-cluster residue case), but the "gap (b) fully closed"
  claim is over-broad: the simultaneous-multiple-tie-cluster case is
  unaddressed. Next round: generalize the induction to multiple
  simultaneous impurities, or prove a WLOG single-cluster reduction.
- **`geometric-dominance-construction` — CHANGES REQUESTED.** Same
  reasoning as above; genuinely independent, correct route to the
  single-cluster case, same multi-cluster gap unaddressed.
- **`universal-adversary-strategy` — CHANGES REQUESTED.** `m=3`'s general
  upper bound is now genuinely fully solved (verified, no issues); general
  `m≥4` Case C remains open, honestly and correctly reported as such — a
  real, substantial, well-tooled remaining gap (Hall's-theorem existence
  question), not a flaw in what's claimed.

No approach reaches APPROVE this round (the overall problem is not fully
solved end-to-end by any one approach, and even the lower-bound-only
portion has the flagged multi-cluster caveat). No approach is RETHINK —
all three made genuine, independently-verified progress with no
correctness errors found (beyond the round-8 labelling bug that
`universal-adversary-strategy` itself already caught and fixed this
round).

`current.md` has been updated: Status remains `partial`; the round-9
entries for all three approaches are recorded under "Approaches tried";
the "Open gaps" and "Full proof" sections are revised to state precisely
that gap (b) is closed only for the single-cluster case (multi-cluster
flagged as the sharpest immediately-actionable open sub-question for next
round), and that the upper bound (general `m≥4`) remains the other fully
open piece. `record_outcome` was called for all three slugs
(`outcome=advanced` in each case, reflecting genuine certified progress).
