# Scouting report: Claim PTBI's Case C (`p_1 < Σ(A)/2`), general `m ≥ 4`

**Lens assigned:** the one remaining upper-bound gap after Lemma
THRESHOLD-REDUCTION — `universal-adversary-strategy`'s Claim PTBI, Case C.
Scouting only; no proof attempted.

## 1. Exact statement of what Case C requires

Recall the setup from `results/imo-2026-03/lemmas/ptbi-threshold-reduction.md`
and `approaches/universal-adversary-strategy.md` (round 8):

**Claim PTBI.** For every `m≥1` and sorted `A=(p_1≥⋯≥p_m)` of positive reals,
using `≤ m-1` marks Xiang Yu can force `oddrank(B) ≤ c(m-1)Σ(A)`, where
`c(k)=2^k/(2^{k+1}-1)`.

Lemma THRESHOLD-REDUCTION (certified) already closes:
- **Case A** (`p_1 ≥ c(m-1)Σ`): peel+halve (unconditional Lemma DOUBLE-INSERT)
  + IH on the tail, via the identity `c(k-1)=c(k)/(2(1-c(k)))`.
- **Case B** (`Σ/2 ≤ p_1 < c(m-1)Σ`): Lemma DOM directly, `oddrank(B)=p_1`.

**Case C** (`p_1 < Σ/2`) is what remains, for every `m≥4` entirely open, and
for `m=3` narrowed to the sub-region `p_1<Σ/2 ∧ p_3>Σ/7` (the sub-case
`p_3≤Σ/7` is closed exactly by "peel+halve both `p_1` and `p_2`", giving
`oddrank=1/2+p_3/2≤4/7`, and `p_1≥Σ/2` is Case A/B). The tools available as
given (certified) lemmas: BLOCK-RECURSE (split `p_1` to exactly match a
**prefix** `t_1,…,t_j` of the sorted tail, `j` marks, then recurse
arbitrarily deep on the leftover `{r}∪U`, giving the unconditional identity
`oddrank(block∪W) = S_j + oddrank(W)`), THRESHOLD-REDUCTION's peel+halve, and
the older menu (DOM, HALVE, MULTI-HALVE, TAIL-SNIP, DOUBLE-INSERT, SANDWICH,
PARTIAL-DOM(-RESIDUAL)).

## 2. Numerical experiments — the key finding

I coded an exact-`Fraction` recursive "menu" evaluator implementing exactly
the certified moves available today (do-nothing; unconditional equal-halve
of any one piece via DOUBLE-INSERT, recursing on the rest with budget−1;
BLOCK-RECURSE at every prefix-length `j`, recursing on the leftover; and
TAIL-SNIP), applied **recursively at every level** (not just once), and
swept it against random and adversarially-optimized configurations in Case C.

- **`m=3`, region `p_1<1/2, p_3>1/7`:** 20,000 random trials + a 200×200 fine
  grid near the boundary — **zero violations** of `c(2)=4/7`. This is strong
  evidence that `m=3`'s remaining sub-case is *already* closed by the
  existing certified menu (TAIL-SNIP vs. BLOCK-RECURSE `j=1`, i.e. exactly
  the two candidates the file already identified) — the file's own
  diagnosis ("two complementary candidates, general algebra not finished")
  looks like a genuine, closable algebra gap, not a missing construction.
  Recommend: **attack `m=3`'s remaining region first as a stepping stone**;
  it is very likely a pure 2-parameter piecewise-affine algebra exercise
  (track `min(TAIL-SNIP, BLOCK-RECURSE-j=1)` as a function of `(p_1,p_3)`
  with the `n=1` sub-case boundary `p_2/p_1≷2/3` folded in — exactly as the
  file already set up, just not finished).
- **`m=4`:** 10,000+3,000 random trials, plus a `scipy.differential_evolution`
  adversarial search (many restarts) over the full Case-C region — **zero
  violations found**, best adversarial "violation" was actually negative
  (menu beats target by margin ≥0.0039 at the worst point found). `m=4`
  looks closable by the existing prefix-only menu too, empirically.
- **`m=5`: a genuine, exact violation of the existing (prefix-only) menu.**
  Adversarial search (`differential_evolution` + Nelder–Mead polish) converged
  to the exact rational witness
  ```
  A = (12, 6, 5, 4, 2)/29        (p_1=12/29 < Σ/2 = 1/2, so genuinely in Case C)
  ```
  Exact-`Fraction` check: the existing recursive menu (do-nothing / DOUBLE-INSERT
  halve / BLOCK-RECURSE at every prefix `j`, recursed to arbitrary depth /
  TAIL-SNIP) achieves only `15/29 ≈ 0.51724`, while the target is
  `c(4)=16/31≈0.51613` — **a violation of exactly `1/899`**. This is not
  numerical noise: reproduced exactly with `fractions.Fraction`.
- **But the true optimum on this exact witness is `1/2` (verified two
  independent ways):** a full mark-allocation-and-cut-ratio global search
  (all allocations `(k_1,…,k_5)` with `Σk_i≤4`, `differential_evolution`
  over cut ratios per allocation) finds optimum `0.500000…` at allocation
  `(1,1,1,0,0)`, and directly sorting the resulting 8-piece multiset by hand
  confirms `oddrank = 29/58 = 1/2` **exactly**. The construction:
  - split `p_1` into two exact halves (`6/29,6/29`) — ordinary HALVE/DOUBLE-INSERT;
  - split `p_3` into two exact halves (`5/58,5/58`) — ordinary HALVE/DOUBLE-INSERT;
  - **split `p_2` into two fragments that exactly equal `p_4` and `p_5`**
    (`p_2 = p_4+p_5` exactly: `6=4+2` in units of `1/29`), **skipping `p_3`**.
  This only costs `1+1+1=3` marks total (`1` mark spare out of budget `4`).

  The third move is the load-bearing new phenomenon: it is a DOM-style
  "match a target sub-multiset exactly" move, but the target `{p_4,p_5}` is
  **not a prefix of the sorted tail below `p_2`** — it *skips* `p_3`, which is
  larger than both `p_4` and `p_5`. This is exactly the kind of move
  BLOCK-RECURSE (by construction restricted to a contiguous prefix `t_1,…,t_j`
  of the *sorted* tail) cannot express: BLOCK-RECURSE's proof crucially uses
  that everything in the untouched leftover is `≤ t_j = \min(T)` (sortedness
  of a *prefix*); here the leftover `{p_1,p_3}` is **not** dominated by
  `\min\{p_4,p_5\}=p_5` — `p_1,p_3` are much larger. I hand-verified the
  final multiset directly (not via any unproven recursive shortcut) to make
  sure this isn't an artifact of a buggy formula: sorted descending in
  58ths, `12,12,8,8,5,5,4,4` → `oddrank=12+8+5+4=29`, i.e. `29/58=1/2`.

  I also built a generalized ("arbitrary subset, not just prefix") version
  of the menu and confirmed it *recovers* `1/2` on this witness — i.e. the
  fix is naturally expressible as "generalize BLOCK-RECURSE's prefix `T` to
  an arbitrary subset of the tail", composed with independent HALVE moves on
  the untouched pieces. (I did **not** attempt to prove this generalized
  move's underlying rank identity in the case where the block does *not*
  dominate the recursively-processed leftover — see §5, this is exactly the
  open technical content.)

## 3. Is `m=3`'s narrower remaining sub-case a stepping stone?

Yes, and it looks strictly *easier* in kind than the general problem: the
numerics above show `m=3`'s open region is closed by the existing menu with
no need for the new "skip a tail element" mechanism (there is no room to
skip anything when the tail has only 2 elements — skipping the *only*
candidate to match reduces to TAIL-SNIP or standard BLOCK-RECURSE `j=1`,
which are exactly the two candidates already on record). So closing `m=3`
does **not**, by itself, reveal the general-`m` induction step — the
`m=5` witness shows the *real* obstruction (arbitrary-subset matching) only
shows up once the tail has ≥3 elements to choose from after peeling the top
piece, which `m=3`'s reduced case cannot exhibit. Closing `m=3` would remove
the last confusion about "is the current menu even sufficient for small
cases" but the general-`m` induction step needs the subset-matching
generalization regardless.

## 4. Relevant techniques

- **Hall's marriage theorem / SDR**, already in `knowledge_base.md` (lines
  122–125: "a bipartite graph with parts `X,Y` has a matching saturating `X`
  iff Hall's condition holds"). This looks like the natural tool to formalize
  the generalized move: view each "piece to be split" as needing to select a
  disjoint sub-multiset of "target pieces to reproduce," and use a
  Hall-type / greedy-exchange argument to show a valid, budget-respecting
  assignment achieving `≤c(m-1)Σ` always exists. This has not been tried by
  any live approach yet (round 6 flagged "matching/assignment" framing for
  the even-`m` **lower**-bound tie-necessary problem, and this is now shown
  to be relevant to the **upper**-bound Case C too, for odd `m` — a genuine
  connection between the two open gaps that is worth flagging to the
  outliner).
- **Exchange-argument style** (the "consecutive pairing maximizes sum of
  mins" Fact 0, already proved in `universal-adversary-strategy.md`) is the
  right conceptual frame for *why* matching a piece's fragment to an
  existing value is good: it creates an exact tie, and Fact 0 says the
  globally best pairing of the final multiset (whichever it turns out to be)
  is exactly the consecutive one — a construction that *manufactures* ties
  with existing values is trying to force the consecutive-pairing structure
  onto favorable value-pairs.
- **Potential-function / convexity approaches**: already ruled out
  structurally by `majorization-smoothing` (a genuine non-concavity
  obstruction, min of an affine and a strictly convex piece) — do not
  re-attempt a smooth potential-function argument for Case C; the
  obstruction is combinatorial (matching structure), not analytic.

## 5. Promising vs. dead-end assessment

**Promising, concrete next step:** formalize "Lemma SUBSET-DOM" — splitting
piece `p_i` into fragments that exactly reproduce an **arbitrary subset**
`T` of the other (untouched or already-recursed) pieces' values, not
necessarily a sorted-order prefix, cost `|T|` marks (`|T|-1` at the `r=0`
boundary, as in DOM-boundary-slack), composed with independent HALVE/DOM
moves on whatever pieces are left untouched. The key open technical point
(**not resolved this round**): BLOCK-RECURSE's rank-identity proof needs the
duplicated block to occupy a contiguous rank interval, which followed for
free from sortedness when `T` is a prefix; for an arbitrary subset `T` this
need **not** hold (as the `m=5` witness shows — the leftover `{p_1,p_3}`
is *not* dominated by `T={p_4,p_5}`'s minimum), yet the construction still
achieved the exact claimed value on direct computation. Whether the exact
identity `oddrank(final) = Σ(T) + oddrank(leftover-after-recursion)` still
holds *unconditionally* for arbitrary `T` (not just when the block
dominates), or only holds for this specific witness by a coincidence of
values, is the precise mathematical question a builder needs to resolve
next — I did not attempt a general proof, only confirmed the *value* by
direct brute-force sorting on one witness.

**Dead ends / not promising:**
- Any single fixed static rule (peel+halve, DOM-vs-HALVE threshold, or the
  existing prefix-only BLOCK-RECURSE menu applied however deeply
  recursively) is now **concretely falsified** for general `m` by the exact
  `(12,6,5,4,2)/29` witness at `m=5` — this supersedes the round-7/8 "naive
  scalar IH fails algebraically but no concrete PTBI-level counterexample
  found" status: **there is now a concrete witness where the entire
  currently-certified menu (not just the naive algebraic bound) provably
  falls short of the target**, by exactly `1/899`. This should be recorded
  as the sharp new obstruction, superseding the vaguer "peel+halve might not
  suffice in general" diagnosis.
- Potential-function / smoothing arguments: already ruled out structurally
  (see above); do not re-attempt.
- A pure `m=3`-style "vacuity of HALVE's hypothesis" argument does **not**
  generalize past `m=3` (the file already notes this; my numerics confirm
  the true obstacle at `m≥5` is a genuinely different, subset-matching
  phenomenon, not a hypothesis-vacuity argument at all).

## 6. Concrete artifact for the next round

Exact witness to build/test against, falsifying the current menu (not just
the naive algebraic bound) for Case C at `m=5`:
```
A = (12/29, 6/29, 5/29, 4/29, 2/29),  budget = 4,  target c(4) = 16/31
Existing certified menu (best over do-nothing / DOUBLE-INSERT-halve /
  BLOCK-RECURSE at every prefix j / TAIL-SNIP, recursed to any depth):
  15/29 ≈ 0.51724  >  16/31 ≈ 0.51613   (violates by exactly 1/899)
True optimum: 1/2, via halving p_1, halving p_3, and splitting p_2 into
  two fragments exactly equal to p_4 and p_5 (skipping p_3) — NOT expressible
  as a prefix-match.
```
Recommend the next outliner/builder round target: (a) finish `m=3`'s
remaining algebra (low-risk, likely mechanical) as a confidence-building
stepping stone, and (b) open a genuinely new sub-approach or task formalizing
Lemma SUBSET-DOM (arbitrary-subset matching generalization of BLOCK-RECURSE)
with a Hall's-theorem-style existence argument for a valid matching that
always closes Case C — this is the real missing primitive, not a sharper
scalar induction hypothesis.
