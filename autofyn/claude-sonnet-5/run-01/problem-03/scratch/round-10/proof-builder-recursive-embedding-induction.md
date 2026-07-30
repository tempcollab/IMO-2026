# Build report — recursive-embedding-induction, round 10

## Task
Generalize the certified Lemma TREE-BOUND-RESIDUAL (at most one impurity in
the whole forest) to arbitrarily many simultaneous, independent tie-clusters,
per the outliner's plan and `math-explorer-multicluster.md`'s diagnosis that
the genuine obstruction is `p≥2` impurities landing simultaneously at the
same top level of the same forest pass.

## Result: CLOSED IN FULL

New certified lemma: `results/imo-2026-03/lemmas/tree-bound-multicluster.md`
(Lemma TREE-BOUND-MULTICLUSTER). Proved by strong induction on `m`
(extending Sub-lemma ODD / TREE-BOUND-RESIDUAL's proof), with two new exact
reduction steps on the top-level impurities and a telescoping-anchor bound
closing the case that a naive repetition of the `p=1` argument does not
survive to (`p≥2` with tied companions, where the naive "largest companion
supplies the slack" mechanism degenerates to `A_p=0`).

**Key new content:**
1. **Reduction R1**: an impurity cut at depth `j=2` produces the identical
   two leaves a pure split would (`{τ_2,τ_2}`), so it is reclassified as
   pure — an exact, cost-free identity, not an approximation.
2. **Reduction R2 / Fact PAIR-CANCEL**: a short, self-contained, from-scratch
   proof that removing two *adjacent equal* entries from any sorted list
   changes the alternating sum `D` by exactly `0` (direct computation from
   the definition — a genuinely new elementary fact, not previously stated
   in this form in the lemma family, though closely related in spirit to the
   already-mentioned but never explicitly proved "PAIR-CANCEL" name from the
   round-8 approach history). Applied to cancel pairs of impurities tied at
   the same depth, reducing to impurities at pairwise **distinct** depths.
3. **Telescoping bound** (Step 2 of the lemma): using `τ_1-τ_j = τ_2+\cdots+τ_j`,
   shows the distinct-depth companion block's alternating sum `A_{p'}`
   satisfies `A_{p'}≥τ_2+τ_m` (`p'` odd) or `A_{p'}≥τ_m` (`p'` even, `≥2`) —
   closing every parity combination of (`k`=top-level leaf count, `p'`) via
   two applications of the already-certified Lemma D-BOUND, plus (in the
   `p'=0` case) the strong induction hypothesis itself, applied
   unconditionally, since a fully pure remainder `X` (at level `m-1`) is
   *exactly* an instance of the same general statement being proved.
4. The `k`-odd branch turned out to need **no reduction at all** — a direct
   application of D-BOUND to the whole remainder-plus-impurities list
   (bounding by the single deepest companion) closes it unconditionally,
   robust to any ties, for any `p≥0`, mirroring but slightly strengthening
   the `p=1` proof's structure.

**Verification performed (numerical, supporting not replacing the proof):**
- `28` `(m,r)` combinations (`m=1..7`, odd `r∈{1,3,5,7}`), fully unrestricted
  recursive random impurity placement (each node independently `20%` chance
  of an impure cut to a random deeper anchor), `2,000` trials each — zero
  violations, minimum `D` exactly `τ_m` throughout.
- Even-`r` sanity check: genuine violations found (`D=0<1` at `m=1,r=2`),
  confirming the test harness discriminates correctly.
- Targeted tied-depth `p=2` adversarial probe (`j_1=j_2`, the case flagged
  by this round's explorer as most likely to break a naive argument):
  `m=3..7`, all depths, `300` trials each — zero violations, exact match
  `D=1`.
- Targeted distinct-depth `p=2` probe: `m=4,5,6`, `r∈{3,5}`, all `k`
  parities, all depth pairs, `150` trials each — zero violations.

## What this completes

Combined with the already-certified `lemmas/cross-tie-affine.md` (reduces
every cross-piece tie to well-separated/self-meeting-point/minority-residue)
and `lemmas/tree-bound-anchor.md` (gap (a)), Lemma PARITY-PAIR-GEN's lower
bound is now **fully proved** for every `n`, every budget, and every number
of simultaneous tie-clusters — no open sub-case remains. Combined with the
already-certified Proposition 4 (exact-equality upper response), **`A_n`'s
value is exactly `c(n)` for every `n`, unconditionally** — the entire
lower-bound half of the minimax problem (this approach's whole scope) is
now a complete, gap-free theorem.

## What remains open (outside this approach's scope)

The separate "general upper bound over all Liu Bang configurations"
(showing no non-geometric configuration beats `A_n`) is untouched — owned
by `universal-adversary-strategy`, where it remains `partial` (general
`m≥4` Case C of that induction is the sharpest remaining open sub-problem
project-wide, as of round 9). The `recursive-embedding-induction` approach
file's overall `## Status` therefore remains `partial` (its stated Target
is the full two-sided determination of `c(n)`), but this round's work
closes its entire own contribution in full.

## Files touched
- `results/imo-2026-03/lemmas/tree-bound-multicluster.md` — new certified
  lemma (full proof, independent verification section).
- `results/imo-2026-03/approaches/recursive-embedding-induction.md` —
  updated `## Status` header comment, new `## Approaches tried` entry, new
  `## Round 10` detailed section at the end of the file.
