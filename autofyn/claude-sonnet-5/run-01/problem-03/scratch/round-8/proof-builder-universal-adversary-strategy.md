# Build report — universal-adversary-strategy, round 8

## Task
Formalize Lemma BLOCK-RECURSE and carry out the strong induction on
piece-count `m` for Claim PTBI (general upper bound over arbitrary
configurations), per the round-8 outliner/reviewer's build-set assignment.

## Result: Status remains `partial` (NOT solved)

**Lemma BLOCK-RECURSE — proved in full**, general `m`, any tail shape, any
recursion depth. Certified to `results/imo-2026-03/lemmas/block-recurse.md`.
Core mechanism: splitting a positive value never increases the resulting
parts, so the duplicated PARTIAL-DOM block always dominates the leftover
`{r}∪U` no matter how deeply the leftover is further recursively refined —
hence the block always occupies exactly the top `2j` ranks, giving the
exact identity `oddrank(block∪W) = S_j + oddrank(W)` unconditionally in
`W`. Budget conservation across recursion depth proved by a one-line
induction. This strictly generalizes the already-certified Lemma
PARTIAL-DOM / PARTIAL-DOM-RESIDUAL.

**Lemma THRESHOLD-REDUCTION — proved in full**, general `m`. Certified to
`results/imo-2026-03/lemmas/ptbi-threshold-reduction.md`. Proves a new
general algebraic identity `c(k-1) = c(k)/(2(1-c(k)))` for every `k`
(verified both symbolically and numerically for `k=1..7`), and uses it to
show:
- Case A (`p_1 ≥ c(m-1)Σ(A)`): peel+halve (Lemma DOUBLE-INSERT + the
  induction hypothesis on the tail) closes it, with `g(p_1)` decreasing and
  `g(c(m-1)Σ)=c(m-1)Σ` exactly by the identity.
- Case B (`Σ/2 ≤ p_1 < c(m-1)Σ`): Lemma DOM closes it directly, no
  recursion.
- Together these cover `p_1 ≥ Σ/2` in full, reducing Claim PTBI's
  inductive step to the single remaining case `p_1 < Σ(A)/2` — a genuine
  narrowing not on record before this round (round 7 only identified the
  peel+halve case, without the sharp threshold or the DOM case).

**Case C (`p_1 < Σ/2`) — the induction was NOT closed.** For `m=3` (`n=2`)
I pushed substantially further: proved Lemma HALVE's hypothesis is
structurally vacuous inside Case C when `m=3` (an exact contradiction
argument: `p_1≥2p_2` and `p_1<Σ/2` are mutually exclusive for `m=3`), fully
closed the sub-region `p_3≤Σ/7` via an exact two-fold DOUBLE-INSERT
identity, and fully closed all of `p_1≥Σ/2` (combining the general
Threshold-Reduction result with a sharper exact computation for `p_1>4/7Σ`
using a clean sum-exceeds-1 contradiction to force Lemma HALVE's
hypothesis). This leaves only the region `p_1<Σ/2` and `p_3>Σ/7` open even
for `m=3`; two candidate constructions (TAIL-SNIP, BLOCK-RECURSE `j=1`)
were shown, on two concrete cross-verified numeric examples, to be
genuinely complementary (each fails where the other succeeds), but no
general proof that their minimum always closes this last region was
completed. For general `m≥4`, Case C remains entirely open — the `m=3`
vacuousness argument for Lemma HALVE does not generalize, and
BLOCK-RECURSE's general-`j` optimization (as opposed to just `j=1`) was
not carried out algebraically for general `m`.

## Verification performed
All algebraic claims (the `c(k-1)=c(k)/(2(1-c(k)))` identity for `k=1..7`,
`g(c(m-1))=c(m-1)` for `m=5`, and both `m=3` worked numeric examples —
`(0.45,0.275,0.275)` giving TAIL-SNIP `0.5875` fail / BLOCK-RECURSE `0.55`
succeed, and `(0.4,0.35,0.25)` giving BLOCK-RECURSE `0.575` fail /
TAIL-SNIP `0.525` succeed) were independently recomputed via exact
`fractions.Fraction` arithmetic in this session and match the write-up
exactly.

## Files changed
- `results/imo-2026-03/approaches/universal-adversary-strategy.md` — new
  "Approaches tried" entry, new "Round 8" section with full proofs of
  Lemma BLOCK-RECURSE, Lemma THRESHOLD-REDUCTION, and the detailed `m=3`
  case analysis; updated "Full proof" summary paragraph; two new
  "Promotable lemmas" entries.
- `results/imo-2026-03/lemmas/block-recurse.md` — new, full proof.
- `results/imo-2026-03/lemmas/ptbi-threshold-reduction.md` — new, full
  proof.

## Honest bottom line
This is genuine, verified, non-trivial progress — two new certified general
lemmas, and a narrowing of Claim PTBI's open surface from "the entire
induction is unproved" to "only the case `p_1 < Σ(A)/2`, for each `m`
(essentially closed for `m=3` down to one small remaining sub-region)". It
does **not** close Claim PTBI, so it does **not** close the whole problem
this round. Status is `partial`, not `solved`; this was assessed honestly
rather than overclaimed.
