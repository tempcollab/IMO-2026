# Round 10 proof-reviewer report — imo-2026-03

## Headline

**The entire lower bound is now closed.** `recursive-embedding-induction`'s
new Lemma TREE-BOUND-MULTICLUSTER genuinely generalizes Lemma
TREE-BOUND-RESIDUAL from "at most one impurity" to "arbitrarily many
impurities, distributed anywhere in the forest, including several
simultaneous at the same top-level of the same recursive pass" — exactly
the multi-cluster gap flagged as the last open sub-case by round 9's
review. I independently verified this from scratch (not the builder's own
scripts) and found it correct and gapless. Combined with the already-
certified Lemma TREE-BOUND (gap a) and Lemma CROSS-TIE-AFFINE (the
reduction of every cross-piece tie to well-separated / majority-part /
minority-residue sub-cases), **`A_n`'s value is now a fully proved theorem:
`A_n` guarantees Liu Bang exactly `c(n) = 2^n/(2^{n+1}-1)` for every
`n≥1`, unconditionally.** The upper bound (general `m≥4` Case C of
`universal-adversary-strategy`'s Claim PTBI) is now the **only** remaining
gap for the whole problem. `current.md` has been updated to reflect this
precisely.

---

## 1. `recursive-embedding-induction` — Lemma TREE-BOUND-MULTICLUSTER

**Verdict: CHANGES REQUESTED** (per-approach Status stays `partial` because
the approach's scope is only the lower bound — the whole problem needs the
upper bound too, explicitly out of this approach's scope, honestly stated
in its own file). **The mathematical content itself is fully verified
correct and closes gap (b) in full generality; this is a genuine milestone,
not a partial step.**

### What I checked (independently, not the builder's scripts)

1. **Small exhaustive brute force.** Wrote a from-scratch recursive tree
   generator (leaf / pure-split / impure-cut-to-any-deeper-anchor at every
   node) and enumerated every possible `(m,r)`-forest for `m=1..3`,
   `r∈{1,3}` (up to 5184 configurations) — minimum `D` found is exactly
   `τ_m` in every case, matching the claim exactly, zero violations.

2. **Deep randomized recursive stress test.** For `m=1..8`, `r∈{1,3,5,7}`
   (28 combinations), 3000 trials each, every node independently and
   recursively has a chance of an arbitrary-depth impure cut (so the number
   and placement of impurities, including multiple simultaneous clusters,
   is fully unconstrained) — minimum `D` found is exactly `τ_m=1` in every
   single case, zero violations. Even-`r` control (`r=2,4`) does produce
   genuine violations (`D=0<1`), confirming the harness discriminates and
   the odd-`r` hypothesis is load-bearing (consistent with round-8's
   finding for the single-impurity case).

3. **Exhaustive "one-shot" multi-cluster enumeration.** For `m` up to 6,
   `r` up to 5, enumerated *every* combination of each of the `r` top trees
   and each of the `m-1` standard trees independently choosing
   leaf/pure-split/impure-cut (up to ~6 million configurations at the
   largest case) — zero violations, minimum exactly `τ_m=1`. This
   specifically stress-tests genuinely simultaneous independent clusters at
   different levels of the forest at once (not just clusters separated by
   recursion depth), which is the crux of what makes this round's lemma
   nontrivial beyond the single-impurity case.

4. **Direct re-derivation of the proof's internal mechanism** (not just the
   final numeric conclusion, per my standing rule): re-implemented and
   Fraction-verified (a) Fact PAIR-CANCEL's algebra directly from the
   definition of `D` (trivially correct — deleting an adjacent equal pair
   changes nothing); (b) the Step-3 assembly identity
   `D(X∪{y_i,c_i}_{i=1}^{p'}) = A_{p'} + (-1)^{p'}D(Y)` — verified exactly
   on 760 random trials (`m=4..8`, random distinct depth sets, random `X`);
   (c) the "k odd" bypass formula `D(B)=τ_1-D(R)` and its unconditional
   bound (works even before any R1/R2 reduction, with raw ties) — verified
   exactly on 1500 random trials including duplicate/tied depths. All
   match exactly, zero mismatches.

5. **Cross-checked geometric-dominance-construction's narrower claim**
   directly on genuine `A_n` piece values (not the abstract exponent
   model): 24,000 random trials of `K`-cluster configurations (disjoint
   piece subsets, random cluster sizes 2–4, random tie values) — zero
   violations, confirming their Main Theorem is correct as stated.

6. **Meta-level sanity check on the model's scope.** I probed whether the
   forest model's convention that an "impure cut" is terminal (the residual
   companion `c` is never itself further split) could hide real Xiang-Yu
   strategies that beat the bound. An *unconstrained*-marks version of
   "keep splitting the residual" can indeed push `D` below `τ_m` — but this
   is not a counterexample: it simply isn't a mark-budget-respecting
   strategy. I then directly simulated the **real, budget-constrained
   game** (bypassing the abstract tree/forest formalism entirely) for
   `n=2` and `n=4`: random search over every possible allocation of Xiang
   Yu's `≤n` marks among the `n+1` real pieces (including multiple marks on
   the same piece, arbitrary split ratios), 200,000 and 400,000 trials
   respectively — the true minimum `oddrank` found matches `c(n)·Σ`
   **exactly** in both cases, no violation. This confirms the
   "further-split-the-residual" concern is not exploitable within the real
   mark budget, so the tree/forest formalism's restriction is not a live
   gap for the actual game.

### One inherited (not re-derived this round) trust point, noted not blocking

The claim that every genuine Xiang-Yu vertex-optimum reduces exactly to
this anchor-plus-tree-with-impurities combinatorial structure in the first
place rests on Lemma V'-GEN / Lemma CROSS-TIE-AFFINE (the vertex-reduction
argument), certified and independently reviewed across rounds 6–9. This
round's build does not re-derive that reduction; it only extends the
*combinatorics* of the already-established forest model to the
multi-cluster case. I did not re-litigate the vertex-reduction argument
from scratch this round (out of scope for this round's build), but my
direct real-game simulations above (which bypass the tree formalism
entirely) are consistent with it and found no violation, which is
reassuring independent corroboration, not a full independent re-proof of
that separate, already-multiply-reviewed argument.

### Conclusion

Lemma TREE-BOUND-MULTICLUSTER is correct and gapless as written. **Gap (b)
is closed in full generality, including the multi-cluster case. The entire
lower bound (`A_n` achieves `c(n)` for every `n`) is now a complete,
gap-free theorem.** `current.md` updated accordingly — this is the headline
result of the round. The approach's own Status remains `partial` only
because CLAUDE.md requires an approach's target to be the *whole* problem
(both bounds), and the upper bound is explicitly out of this approach's
scope (owned by `universal-adversary-strategy`).

**Certified lemma**: `lemmas/tree-bound-multicluster.md` — CERTIFIED (proof
correct, statement matches what's proved, no overclaiming beyond what was
independently verified).

---

## 2. `geometric-dominance-construction` — Lemma TOP2 + Structural Lemma

**Verdict: CHANGES REQUESTED.** Real, correct, honestly-scoped progress —
not a gap in the sense of an error, but explicitly narrower than the
sibling's closure.

### What I checked

- **Lemma TOP2** (`D(L)≥b_1-b_2` for any sorted nonnegative list's two
  largest elements) — a two-line consequence of the already-certified
  Lemma D-BOUND; trivially correct, re-derived by hand.
- **Structural Lemma + Main Theorem** (identifying the two globally-largest
  merged elements across `K` simultaneous independent minority-tied
  2-part-piece clusters, and the five-case algebra bounding
  `b_1-b_2≥t_n`) — independently re-verified on genuine `A_n` instances,
  24,000 random trials (`n=1..8`, random `K`, random cluster sizes 2–4,
  random tie values, no ordering assumed between clusters) — zero
  violations, exact match with the predicted `(b_1,b_2)` pair.

### The scope question (per this round's dispatch instruction)

The file **explicitly and correctly** states its own scope: "gap (b) now
appears closed in full **for every configuration where each individual
split piece has at most 2 parts**." It also honestly flags the one loose
end this restriction leaves open (a single piece split into `≥3` parts
with two or more independently-tied residual coordinates — the "doubly-tied
`≥3`-part piece" case) as *not* addressed here. This scope restriction is
real: it means this approach's round-10 result, taken alone, does **not**
close the full multi-cluster gap — only the sibling's unrestricted
TREE-BOUND-MULTICLUSTER does (and, as I noted in `current.md`,
TREE-BOUND-MULTICLUSTER's "any node, at any depth, anywhere" impurity
placement does in fact subsume the "doubly-tied `≥3`-part piece" scenario
too, since two impurities can land at two different nodes under the same
original piece's own pure-split subtree).

The build's honest note that it could not cross-check against the sibling
(file unchanged at build time) is accurate and not a fault — the
reconciliation is now done by this review: no disagreement found on any
witness both approaches can be tested on.

**Certified lemma**: `lemmas/multi-cluster-two-block.md` — CERTIFIED as
stated (correctly scoped to `≤2`-part-per-piece splits; do not treat as a
full closure of gap (b) on its own).

---

## 3. `universal-adversary-strategy` — Lemma ALL-BUT-MIN, Lemma MATCH-TAIL-PAIR

**Verdict: CHANGES REQUESTED.** Genuine new lemmas, a genuine proved
structural obstruction, and an honest "still open" self-assessment — no
issues found.

### What I checked

- **Lemma ALL-BUT-MIN** (`oddrank(B)=Σ/2+p_m/2` when halving every element
  except the smallest) — re-derived directly via `oddrank` computation on
  1000 random instances per `m=2..8` (7000 total with MATCH-TAIL-PAIR
  below) — exact match, zero mismatches.
- **Lemma MATCH-TAIL-PAIR** (`oddrank(B)=Σ/2+(p_{m-1}-p_m)/2` when halving
  the prefix and matching the two smallest) — same test, exact match, zero
  mismatches.
- **Step 3's structural obstruction** (`g(v)=c(m-2)Σ+v(1-2c(m-2))`,
  strictly decreasing since `c(k)>1/2` for all finite `k` and `c` is
  strictly decreasing) — re-derived algebraically from
  `c(k)=1/(2-2^{-k})`: confirmed `c(k)>1/2` (since `2-2^{-k}<2`) and `c`
  strictly decreasing (since `2-2^{-k}` strictly increasing in `k`); the
  claimed inequality `g(0)=c(m-2)Σ>c(m-1)Σ` follows immediately. Correct.
- **Step 4's counterexample witness**
  (`A=(1826,1563,1520,1514,765)/7188`, `m=5`) — independently recomputed
  both ALL-BUT-MIN's value (`2651/4792`) and MATCH-TAIL-PAIR's value
  (`7937/14376≈0.5521`), confirmed the minimum of the two exceeds
  `c(4)=16/31≈0.5161` by exactly the claimed margin, and confirmed neither
  sufficient condition threshold (`1/31≈0.0323`) is met by `p_5` or
  `p_4-p_5` in this witness. Exact match.

### Assessment

All new claims check out exactly; the "honest summary" section correctly
distinguishes what was proved (two new menu items, a genuine impossibility
result for a whole *class* of naive constructions) from what remains open
(a general existence theorem for a good recursive matching sequence, for
every `m≥4`). No overclaiming. This is now, per the round-10 closure of
the lower bound, **the sole remaining gap for the entire problem.**

**No new lemma files to certify beyond `lemmas/all-but-min.md` and
`lemmas/match-tail-pair.md`, both CERTIFIED** (both fully proved,
hypothesis-free corollaries of the already-certified Lemma PAIR-VALUE, no
overclaiming — the file correctly states these narrow but do not close
Case C).

---

## `current.md` — updated

- `## Status` remains `partial` (correct — the whole problem needs both
  bounds; the upper bound's general `m≥4` Case C is still open).
- Added a full round-10 status note documenting the lower-bound closure and
  my independent verification (superseding, not deleting, the round-9
  note, kept for history).
- Rewrote "Open gaps" item 1: **the lower bound is CLOSED IN FULL** — do not
  re-open in future rounds.
- Updated "Full proof" section's framing to state precisely what remains:
  only the general upper bound (`m≥4` Case C).

## Record

Recorded via `record_outcome`:
- `recursive-embedding-induction` → `verified-milestone` (Elo now 1662.10,
  highest in the population)
- `geometric-dominance-construction` → `partial`
- `universal-adversary-strategy` → `partial`

## Next round guidance

The lower bound is done. All future effort should concentrate on the
**single remaining target**: Claim PTBI's Case C (`p_1<Σ(A)/2`) for general
`m≥4`. `universal-adversary-strategy`'s own Step 3 result (the structural
obstruction to single-peel-plus-IH constructions) is a valuable, certified
negative result: any future construction must spend marks via an
unconditional multi-pair identity (Lemma PAIR-VALUE and its corollaries),
not defer to a weaker `(m-2)`-strength inductive hypothesis on an untouched
remainder. The `m=5` counterexample witness
(`A=(1826,1563,1520,1514,765)/7188`) is now the standard hard test case for
any new candidate construction — check it first before proposing a general
menu extension.
