# Build report: universal-adversary-strategy (round 10)

## Target
Close Claim PTBI's Case C (`p_1 < Sigma(A)/2`) for general piece-count
`m >= 4` (the sole remaining gap in the upper-bound half of the minimax,
`m=3` already fully solved and not re-attempted).

## Result: Status remains `partial`. Case C for general `m>=4` is NOT closed
this round, but real, certified progress was made.

### What was done
1. **Fact-0 (evensum reformulation) tested and found to give no
   independent shortcut** — it is a genuine equivalence but computes over
   exactly the same reachable-multiset space as the direct `oddrank`
   approach, so it supplied no new tractable structure. Reported honestly
   as a negative (cheap) finding, per the outline's own instruction to
   test this first.
2. **Found and fixed a bug in my own exploratory brute-force search
   harness.** The bug (a self-halve move's recursive case double-counted
   the halved value) initially produced a spurious "true optimum" that
   looked like it required cross-piece, non-tied splits beyond the
   Lemma-PAIR-VALUE matching framework — which would have been a serious
   negative finding contradicting round 9's toolkit. After fixing the bug
   and cross-checking against an independent `scipy` continuous optimizer,
   the corrected true optimum on the same witness is achieved by a purely
   matching-based construction (already-certified machinery). This
   corrects what would otherwise have been a misleading report.
3. **Proved two new, fully general lemmas**, both one-line corollaries of
   the already-certified Lemma PAIR-VALUE:
   - **Lemma ALL-BUT-MIN** (`lemmas/all-but-min.md`): halving every element
     except the smallest gives `oddrank(B) = Sigma/2 + p_m/2` unconditionally,
     closing Case C whenever `p_m <= Sigma/(2^m-1)`. Generalizes round 9's
     `m=3` sub-case-1 threshold (`p_3<=Sigma/7`) to every `m`.
   - **Lemma MATCH-TAIL-PAIR** (`lemmas/match-tail-pair.md`): halving the
     top `m-2` elements and matching the two smallest gives
     `oddrank(B) = Sigma/2 + (p_{m-1}-p_m)/2`, closing Case C whenever the
     two smallest elements are close together, complementary to ALL-BUT-MIN.
4. **Proved a general structural fact** ("single-small-peel obstruction"):
   any construction of the shape "make one tied pair, then apply the
   induction hypothesis at size `m-1`" gives a bound that is provably worse
   than the target already at the boundary value `v=0`, because
   `c(k) = 1/(2-2^{-k})` is strictly decreasing. This is a clean, fully
   proved (not numerical) explanation for why every naive single-peel-plus-IH
   construction tried across rounds 7-10 fails in Case C.
5. **Found a concrete `m=5` witness** (`A = (1826,1563,1520,1514,765)/7188`)
   showing that even the extended two-lemma menu (ALL-BUT-MIN,
   MATCH-TAIL-PAIR) does not close Case C in general — the true optimum
   (`1199/2396`, comfortably below target) requires a deep, multi-level
   recursive sequence of matches/self-halves, not a single closed-form
   formula. This sharpens, rather than closes, the remaining gap.

### What remains open
A general existence theorem — that *some* sequence of matches/self-halves,
within budget `m-1`, always achieves `oddrank(B) <= c(m-1)*Sigma(A)` for
every configuration with `p_1 < Sigma(A)/2` and every `m >= 4` — is still
not established. This is the precise, honestly reported open gap.

## Files touched
- `results/imo-2026-03/approaches/universal-adversary-strategy.md` (Status
  unchanged: `partial`; new "Round 10" section, new "Approaches tried"
  entry, two new Promotable lemmas entries).
- `results/imo-2026-03/lemmas/all-but-min.md` (new, proposed for
  certification).
- `results/imo-2026-03/lemmas/match-tail-pair.md` (new, proposed for
  certification).
- `/tmp/memory/proof-builder.md` (two new rules appended, about the
  self-halve double-counting bug and the c(k)-strictly-decreasing
  impossibility-proof technique).

## Recommendation for next round
The residual gap (`p_1 < Sigma/2`, both ALL-BUT-MIN's and MATCH-TAIL-PAIR's
thresholds failing) needs either: (a) a genuinely larger menu of
closed-form PAIR-VALUE-based constructions (e.g. a 3-or-more-level
generalization of MATCH-TAIL-PAIR), or (b) an actual existence/induction
argument for why *some* matching sequence always works — the corrected
Step-1 finding shows the matching+self-halve mechanism itself is not
structurally blocked, only the general existence proof is missing. Do
**not** re-attempt "single-tied-pair-then-apply-IH" constructions without
first checking them against the round-10 Fact (Step 3 above) — that whole
construction shape is now proven insufficient in general.
