# Round 10 build report — geometric-dominance-construction

## Task
Generalize the certified TWO-BLOCK mechanism (`lemmas/two-block-residue-close.md`,
single-cluster minority-role residue closure) to K≥2 simultaneous, independent
tie-clusters, per `/tmp/round-10/proof-outliner.md`'s plan (nested threshold
peeling `v_1>...>v_K`).

## Result: full proof achieved, via a simpler mechanism than the outline planned

The outline's planned "K-fold nested threshold peel" mechanism has a genuine
subtlety it didn't fully resolve (peeling the whole list at threshold `v_1`
does not cleanly isolate cluster 1, since a majority part belonging to some
*other* cluster can easily exceed `v_1`). Rather than repair that plan, I
found a strictly simpler, hypothesis-free replacement:

- **Lemma TOP2**: for any sorted nonnegative list, `D(L) ≥ b_1 - b_2` where
  `b_1,b_2` are its two globally largest elements. This is a 2-line
  consequence of the already-certified Lemma D-BOUND (no threshold/Y-Z split,
  no parity case-split needed at all — strictly simpler than Lemma TWO-BLOCK).
- A generalized **Structural Lemma** identifying the two globally-largest
  elements of a K-cluster merged configuration, for *any* K, with *no*
  ordering assumption between the clusters' tie values.
- Combining these, the **Main Theorem**: `D(B) ≥ t_n` for every `n≥1`, every
  `K≥1`, every disjoint collection of minority-role 2-part tie-clusters, any
  choice of tie values. The proof reduces to a **fixed 5-case analysis**
  (independent of K) — the only new case beyond K=1 is "pieces 0 and 1 owned
  by two different clusters," closed by the same load-bearing fact used in
  K=1's analogous case (whichever cluster owns a piece must contain a second,
  ≥2-indexed member, forcing its tie value below t_2/2).

All of this is proved in full (not just numerically), and cross-checked
against 16,000 randomized instances (`n=1..8`, random `K` up to
`⌊(n+1)/2⌋`, random cluster sizes 2-4, random tie values) with zero
violations and zero mismatches in the structural-lemma prediction
(`/tmp/verify_kcluster.py`).

Certified new lemma file: `results/imo-2026-03/lemmas/multi-cluster-two-block.md`.

## Cross-check against sibling (recursive-embedding-induction)

Per the dispatch instruction, this round was scoped primarily as a
cross-check task. At the time this build ran, `recursive-embedding-induction.md`
was unchanged since the round-9 commit (no completed general theorem existed
in the repo to compare against) — I could not verify/cross-check against a
sibling result that didn't yet exist. I reported this honestly in the
approach file and flagged it for the reviewer/next round to reconcile once
the sibling's parallel round-10 work lands.

## Honest remaining scope

Combined with all previously-certified facts (Lemma CROSS-TIE-AFFINE,
Lemma TREE-BOUND, recursive-embedding-induction's well-separated closure),
gap (b) of Lemma V'-GEN now appears closed in full for the case where every
individual split piece has at most 2 parts. The one remaining, honestly
un-addressed loose end (same as flagged in round 9, NOT a multi-cluster
question, not attempted this round): a single piece split into ≥3 parts
with more than one of its own coordinates independently tied at different
values ("doubly-tied ≥3-part piece"). I noted (but did not verify) that this
scenario may be structurally impossible at a genuine vertex at all, given
the per-piece LP-vertex property underlying Lemma V'/V'-GEN — this is left
for the sibling approach or a future round to confirm, not claimed here.

## Files changed
- `results/imo-2026-03/approaches/geometric-dominance-construction.md` —
  updated Status/Approaches-tried/Current-best entries, appended full
  "Round 10" section with complete proof, appended Promotable-lemmas entry.
- `results/imo-2026-03/lemmas/multi-cluster-two-block.md` — new certified
  lemma file (Lemma TOP2, Structural Lemma general-K, Main Theorem), full
  proofs and verification detail.

## Status
Setting approach Status to `partial` (unchanged) — the overall problem
(both bounds, all approaches) is still not fully solved; this round's work
is a genuine, complete closure of one specific sub-gap (the multi-cluster
generalization) within this approach's lower-bound contribution, not a
solve of the whole problem. Recommend the proof-reviewer independently
re-verify Lemma TOP2 and the Structural Lemma (both short, checkable by
hand) and cross-check against recursive-embedding-induction's parallel
round-10 result if/when available.
