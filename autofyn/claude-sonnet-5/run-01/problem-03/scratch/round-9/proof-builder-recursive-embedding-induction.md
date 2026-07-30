# Build report: `recursive-embedding-induction`, round 9

## Target
Close gap (b)'s last remaining sub-case (cross-piece tied free coordinate
where the tie is the minority part of a 2-part-split piece, pinned at a
deep external anchor `t_j`, `j>i+1`, companion `c=t_i-t_j` generically
non-power-of-2) by extending Lemma TREE-BOUND's forest/tree-recursion
mechanism to "forced-residual" (non-anchor) leaves.

## Result: CLOSED IN FULL

**Gap (b) is now fully closed**, and with it, **Lemma PARITY-PAIR-GEN's
lower bound for the geometric configuration `A_n`** (`D(B)\ge t_n` for
every Xiang-Yu-reachable configuration, every `n\ge1`, every budget
`\le n`) **is a fully proved theorem** — no sub-case of this approach's
lower bound remains open. Combined with the already-certified upper-bound
tightness (Lemma 1–4 / Proposition 4, all prior rounds), `A_n`'s value is
exactly `c(n)`.

New certified lemma: `results/imo-2026-03/lemmas/tree-bound-residual.md`
(Lemma TREE-BOUND-RESIDUAL).

## The risky step: checked, and it failed as originally proposed — reported honestly

The round-9 plan's proposed mechanism ("domination via forest-extension":
compare the residual configuration directly to its "virtually fully
split" counterpart via one external inequality) was tested first, as
instructed. **It is false in general**: testing `D(X\cup\{y,c\}) \ge
D(X\cup\{τ_{i+1},\ldots,τ_j\})` against an unconstrained common background
`X` produced `159` violations out of `600` random exact-`Fraction` trials
(`/tmp/verify1.py`; e.g. background `\{8,1\}`, `D_{\text{residual}}=3 <
D_{\text{split}}=5`). So the plan's step 2, as a free-standing comparison
lemma, does not hold — the flagged risk was real.

**What actually works**: instead of comparing two separate configurations,
rerun Sub-lemma ODD's strong induction on `m` with one new case (Case C:
the impure node sits at the current top level). This new case is closed
directly by **two applications of the already-certified Lemma D-BOUND**
(no new machinery), using only that the residual `c=τ_1-τ_j` is always
`\ge τ_2` (hence a maximum of the relevant remainder) and elementary
geometric-anchor arithmetic (`τ_i=2τ_{i+1}`). Full proof in the new lemma
file.

## Verification performed (all exact `fractions.Fraction`, no floats)
1. `/tmp/verify1.py` — confirms the naive "virtually-split domination"
   claim is FALSE against unconstrained backgrounds (`159/600` violations).
2. `/tmp/verify3.py` — exhaustive enumeration of the full original
   `(n,3)`-forest problem with exactly one impurity allowed anywhere
   (every placement, every impure cut, every pure-shape combination for
   everything else), `n=2,3,4`: minimum `D` found is exactly `1=t_n`,
   **zero violations**.
4. `/tmp/verify_final.py` — large-scale randomized stress test, `n=2` to
   `12`, `17{,}876` trials, impurity at a uniformly random tree root at a
   uniformly random depth, every other tree independently randomly
   shaped: **zero violations**.
5. Reproduced this round's `math-explorer-crosstie.md`'s two hand-built
   numeric witnesses exactly (`n=4` symmetric two-minority tie, `D=11`;
   `n=6` external-anchor-snap residue with `c=14`, `D=43`) — both
   consistent with the new Lemma's derived (non-tight but always
   sufficient) quantitative bounds.

## Files changed
- `results/imo-2026-03/approaches/recursive-embedding-induction.md` —
  updated `## Status`, `Approaches tried`, `Full proof` placeholder, and
  appended a new `## Round 9 (this build): gap (b) CLOSED IN FULL` section
  with the complete writeup (the round-9 plan section is kept intact
  above it as the historical record, including the honest note that its
  proposed mechanism failed).
- `results/imo-2026-03/lemmas/tree-bound-residual.md` — new certified
  lemma (Lemma TREE-BOUND-RESIDUAL), extending
  `lemmas/tree-bound-anchor.md`'s Sub-lemma ODD with the forced-residual
  case, closing gap (b) in full.

## What remains open (honest scope)
The overall problem's Status stays `partial`: the "general upper bound
over all Liu Bang configurations" (ruling out non-geometric `A` beating
`c(n)`) is untouched by this approach and always was explicitly out of
its scope (belongs to `universal-adversary-strategy`). Everything this
approach owns — the lower bound for the specific geometric construction
`A_n` — is now complete.
