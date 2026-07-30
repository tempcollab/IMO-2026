# Lemma PARITY-PAIR-ANCHOR (round 7, `recursive-embedding-induction`)

**This is Step 1 of round 7's target (Lemma PARITY-PAIR-GEN).** It closes
the "anchor-only" sub-case of the tail-refined lower bound **for
full-budget strategies** (Xiang Yu spends all `n` of his marks), and
precisely isolates — rather than closes — the remaining "partial-budget"
sub-case. Builds on the newly-certified `lemmas/parity-pair-general.md`
(Lemma PARITY-PAIR-GENERAL, Lemma ZERO-DROP).

## Setting

Fix `n ≥ 1`, the geometric configuration `A_n` with top piece
`P_1 = 2t_1 = 2^n` and tail `T = (T_1,...,T_n)`, `T_i = t_i := 2^{n-i}`.
Xiang Yu has a budget of `≤ n` marks, which he distributes among `P_1` and
the `T_i` (a mark placed inside a piece cuts it; `k` marks placed inside
one piece, with no two marks at the same point, produce exactly `k+1`
sub-pieces of that piece, by the problem's own cutting rule — this holds
regardless of where inside the piece the marks fall). Write `b_0` for the
number of marks spent on `P_1` and `b_i` for the number spent on `T_i`
(`i=1,...,n`); `b := b_0 + Σ_i b_i ≤ n`.

**Definition (anchor-only strategy).** A strategy is *anchor-only* if every
resulting positive-length piece (from splitting `P_1` and/or any `T_i`) has
value in the fixed lattice `{t_1,...,t_n}`. (Pieces of value exactly `0`
cannot literally arise from a cut at an interior point with two *distinct*
marks — see the closing remark — but the definition, together with Lemma
ZERO-DROP, is stated to also harmlessly cover the limiting/degenerate
bookkeeping case where a "wasted" mark is modelled as contributing a
`0`-length piece.)

**Definition (full budget).** An anchor-only strategy uses *full budget* if
`b = n` exactly.

## Two structural facts

**Fact 1 (`P_1` must be split).** In any anchor-only strategy, `b_0 ≥ 1`.

*Proof.* If `b_0 = 0`, `P_1` remains as one piece of value `2t_1 = 2^n`,
which is not in `{t_1,...,t_n} = {2^{n-1},...,2^0}` (it strictly exceeds
`t_1`), contradicting anchor-only. ∎

**Fact 2 (`T_n` cannot be split anchor-exactly).** In any anchor-only
strategy, `b_n = 0`, and `T_n` contributes exactly one copy of `t_n = 1` to
the merged multiset.

*Proof.* A genuine split of `T_n` (`≥ 2` positive resulting parts) has all
parts summing to `t_n = 1` and each part strictly less than `t_n` (since
each of `≥ 2` positive parts is less than the whole). But every anchor
value is `≥ t_n = 1`, so no anchor value is `< t_n`: no anchor-exact
genuine split of `T_n` exists. Hence `T_n` is untouched (`b_n = 0`), and
contributes its own value `t_n` once. ∎

## Main theorem (full-budget case)

**Theorem.** For every `n ≥ 1` and every anchor-only Xiang-Yu strategy that
uses **full budget** (`b = n`), the resulting merged multiset `B` (`P_1`'s
parts ∪ `T_1`'s parts ∪ ⋯ ∪ `T_n`'s parts, with any `0`-length parts
dropped) satisfies `D(B) ≥ t_n = 1`, i.e. `oddsum(B) ≥ c(n)` (via the
certified Lemma D-REFORM).

**Proof.** Let `c_i` (`i=1,...,n`) be the total multiplicity of value `t_i`
in `B` (summed over contributions from `P_1`'s split and from whichever
`T_j`'s were split and happened to produce a level-`i` part, plus `T_i`'s
own contribution of `1` if `T_i` was left untouched). By construction `B`
is *exactly* the multiset "`c_i` copies of `t_i`, `i=1,...,n`" — every
piece present has a value in `{t_1,...,t_n}` by the anchor-only hypothesis,
so `B` has no other kind of element.

The total number of resulting pieces is `(n+1) + b` (one mark always adds
exactly one piece, starting from the `n+1` base pieces `P_1,T_1,...,T_n`),
so with `b = n`,
```
M := Σ_{i=1}^n c_i = |B| = (n+1) + n = 2n+1,
```
which is **odd for every `n`**, unconditionally. Lemma PARITY-PAIR-GENERAL
(`lemmas/parity-pair-general.md`) therefore applies directly — with no
constraint that every `c_i ≥ 1` (Fact 2 guarantees `c_n ≥ 1` automatically,
but intermediate `c_i`, `1 ≤ i ≤ n-1`, may genuinely be `0`; see the worked
example below) — giving `D(B) ≥ t_n`. ∎

### Worked example confirming genuine gaps occur (and are handled)

`n=4` (`t=(8,4,2,1)`, `P_1=16`). Strategy: split `T_1` (`=8`) once
(`→{4,4}`, using `T_1`'s natural halving, so `T_1` contributes *no* copy of
`t_1=8`); split `P_1` using `3` marks into `{4,4,4,4}` (four copies of
`t_2=4`, avoiding `t_1` entirely — a valid anchor-exact partition of `16`
into parts `≤ 4`); leave `T_2,T_3,T_4` untouched. Total marks: `1+3=4=n`,
full budget. Merged `B = {4,4,4,4} ∪ {4,4} ∪ {4} ∪ {2} ∪ {1} = {4×7, 2, 1}`
(`9 = 2n+1` elements). Here `c_1 = 0` (value `t_1=8` is **entirely absent**
— this is exactly the kind of configuration the *original* Lemma
PARITY-PAIR, which requires `c_i≥1` for all `i`, does not cover) yet
`c_2=7, c_3=1, c_4=1`, `M=9` odd. Direct computation: sorted `B =
(4,4,4,4,4,4,4,2,1)`, `D = 4-4+4-4+4-4+4-2+1 = 3 ≥ t_4 = 1` ✓, matching
Lemma PARITY-PAIR-GENERAL's prediction and confirming that the
generalization (not the original restricted lemma) is genuinely what is
needed here. (Verified with exact integer arithmetic.)

## Remaining gap: partial-budget anchor-only strategies (`b < n`)

The theorem above is stated **only** for `b = n`. If Xiang Yu uses `b < n`
marks in an anchor-only way, the resulting `M = (n+1)+b < 2n+1`, and its
parity now depends on `b`: `M` is odd iff `b ≡ n (mod 2)`. When `M` is odd,
Lemma PARITY-PAIR-GENERAL still applies directly and gives `D(B) ≥ t_n` (so
partial-budget strategies with the "right" mark-parity are already covered
by the theorem's proof verbatim, without change). **When `M` is even**
(`b ≢ n mod 2`), Lemma PARITY-PAIR-GENERAL's hypothesis fails and gives no
information; this is a genuine, currently open sub-case.

This gap is **not** a defect of Lemma PARITY-PAIR-GENERAL (that lemma is
proved in full generality, and is *tight*: the abstract combinatorial
statement "`M` even ⟹ `D≥t_n`" is **false** in general — e.g. `n=2`,
abstract `c=(0,4)` gives `M=4` and `D({1,1,1,1}) = 0 < t_n = 1`). What
prevents this from being a counterexample to the *theorem* is that
`c=(0,4)` is **not game-reachable** at `n=2`: achieving `c_1=0` requires
`P_1` to skip `t_1` entirely, which by the same counting argument as the
worked example above needs `≥3` marks on `P_1` alone, exceeding the total
budget `n=2`. So closing the partial-budget case requires tracking the
game's specific *mark-cost* structure (which `(c_1,...,c_n)` vectors with
`M<2n+1` are actually reachable within `b≤n-1` additional marks beyond the
mandatory one on `P_1`), not merely the abstract parity condition —
genuinely more than "bookkeeping."

**Evidence the gap is benign (not a proof).**
- A direct hand-argument (worked above, and generalizable) shows that
  *killing* any single anchor value `t_i` (`i<n`) entirely from `B` has a
  minimum mark cost that grows with how far below `t_1` the skip needs to
  reach, and the mandatory `≥1`-mark cost on `P_1` is already "spent" in
  every anchor-only strategy — so cheap partial-budget strategies (small
  `b`) structurally cannot produce many simultaneous gaps.
- A randomized simulator (`/tmp/verify_game.py`, `n=1,...,6`, `30,000`
  trials each, budget used chosen adaptively and independently truncated
  at each step with probability `0.3` to generate genuine partial-budget
  instances) found **zero violations**: the minimum observed `D` over all
  trials (mixing full- and partial-budget anchor-only strategies) was
  always exactly `t_n=1`, attained at (or extending toward) the
  full-budget canonical configuration, never below it.
- Every partial-budget example checked by hand (round 6/7 exploration, and
  the `n=2,4` extension chains recorded in
  `recursive-embedding-induction.md` round 7 section) shows `D` *decreasing
  monotonically* as more marks are spent, bottoming out exactly at `t_n` at
  full budget — consistent with a conjectural **extension-monotonicity**
  principle ("splitting one more anchor-exact level can only
  decrease-or-preserve `D`"), which if proved in general would immediately
  close the partial-budget case by reducing it to the already-proved
  full-budget theorem (any partial-budget config extends to *some*
  full-budget config with `D` no larger, and that full-budget value is
  `≥ t_n` by the theorem, so the partial-budget value is too). **This
  monotonicity principle is not proved this round** — an attempted direct
  proof via the certified block formula (tracking how `D` changes under
  `c_j → c_j-1, c_{j+1} → c_{j+1}+2`) showed the sign changes propagate to
  *every* higher-indexed block with an odd count, not just a bounded local
  region, so the naive per-block accounting does not obviously bound the
  net change; a genuine proof (or a counterexample) is left open for the
  next round.

## Status

**Certified for full budget (`b=n`), for every `n≥1`** — a complete,
unconditional theorem, not merely a numerically-checked claim. **Open for
partial budget with `M` even** — precisely isolated (not vaguely "open"):
the abstract parity-only argument provably cannot be strengthened (a
genuine combinatorial counterexample exists), so any fix must use
game-reachability directly; numerical evidence (randomized search, zero
violations) and a plausible but unproved monotonicity principle are
recorded above as the concrete lead for the next round.
