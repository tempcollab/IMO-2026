# Proof review — round 14, imo-2026-03

Problem: for each n, determine c(n) (Liu Bang / Xiang Yu stick game).
Conjectured/certified answer c(n) = 2^n/(2^{n+1}-1). Lower bound and
upper-bound Case A/B are fully closed in prior rounds; the sole remaining
gap is Claim PTBI's Case C (p_1 < Sigma(A)/2) for general m>=4, attacked
this round by two builds.

## Build 1: `universal-adversary-strategy`

**Claims reviewed:** (a) corrected real-mark-accounting recursion
`solve2(A,marks)` replacing the buggy round-12/13 `solve(A,budget)`;
(b) new Lemma FREE-TIE-REDUCTION (generalized zero-cost Move 0, any
even-multiplicity tied run anywhere in the array); (c) well-foundedness
of `solve2` re-derived via `(marks,|A|)` lex, `marks` primary; (d) three
witnesses (m=3, m=4 non-contiguous-match, m=4 pre-tied) reproduce the
true known optimum exactly; (e) round-12 m=8 witness untested (timeout);
(f) Lemma SLACK-COVER (general subset-match existence) attempted, not
closed — correctly re-characterized as a joint covering+recursive-value
statement, not a pure size-only mesh/covering claim.

### Independent re-verification (from scratch, not reusing builder code)

- **Lemma FREE-TIE-REDUCTION.** Wrote my own exact-`fractions.Fraction`
  script: 20,000 random trials, even-multiplicity tied runs of random
  length `2j` inserted at random positions in random sorted arrays,
  checking `oddrank(A) = j*v + oddrank(A')` exactly. **Zero violations.**
  The proof mechanism (pair up the `2j` consecutive ranks into `j`
  adjacent pairs, each straddling exactly one odd/even rank regardless
  of the run's starting offset parity; the removed even-length block
  causes no parity shift for the surrounding blocks) is correct and
  genuinely position-independent — it is a real strict generalization
  of Lemma DOM's Step 1 / Lemma DOUBLE-INSERT (both special cases),
  not a relabeled restatement. **Certified as-is** (file already present
  at `lemmas/free-tie-reduction-move0.md`, correctly written).

- **`solve2`'s correctness and well-foundedness.** I reimplemented
  `solve2` completely independently (my own script, not the builder's
  `/tmp/solve2.py`). On first attempt I hit exactly the subtlety the
  write-up's Remark flags: the Move-2 sub-case `|S|=1, r=0` (cost `0`)
  is a literal *no-op* — it reproduces the identical multiset with the
  identical `marks` value (because `p_1=t_i` already means an
  even-multiplicity tie exists, so "matching" against it just
  reconstructs the same array), which causes true infinite recursion in
  a naive implementation unless explicitly excluded in favor of Move 0.
  This confirms the write-up's claim ("Move 2's own cost is genuinely
  >=1 whenever it is separately invoked") is load-bearing for
  termination, not decorative — good that the write-up flagged it, and
  it should be read as an explicit exclusion in the recursion's
  definition, not merely a remark. Once I added this exclusion (which
  is exactly what the well-foundedness proof already assumes), my
  independent implementation reproduced the builder's exact claimed
  values on all three witnesses:
  - `A=(26,21,10)/57`: `solve2 = 31/57`, matching the round-13
    reviewer's independently-computed true 2-mark game value exactly.
  - `T=(0.20,0.15,0.12,0.08)`: `solve2 = 11/40 = Sigma(T)/2` exactly,
    via the non-contiguous match `{0.12,0.08}` skipping `0.15`.
  - `A=(965,965,958,482)/3370`: `solve2 = 1685/3370 = Sigma(A)/2`
    exactly, via Move 0 firing for free on the pre-existing tie
    `965=965`.
  All three are comfortably below their `c(m-1)Sigma(A)` targets. This
  independently confirms both the corrected accounting and the specific
  numeric claims — not just a re-run of the builder's own script.

- **m=8 witness — untested claim.** I independently attempted my own
  computation on the round-12 m=8 witness and it also failed to
  terminate within several minutes (naive exhaustive `2^{|tail|}`-subset
  Move-2 search is exponential in the tail size at every recursion
  level). This is a genuine scalability limitation of the brute-force
  reference implementation, not a mathematical finding either way. Per
  CLAUDE.md's rigor rule ("distinguish proved from conjectured; never
  present an unproven claim as established"), the builder's honest
  "NOT evaluated this round" framing is the correct way to report this
  — it does not inflate the Status, and does not by itself block a
  `partial` verdict. It does mean no claim beyond `partial` is
  warranted, which is exactly what was claimed.

- **Lemma SLACK-COVER diagnosis.** The write-up's argument that
  `aimo-0292`'s bounded-mesh technique gives only a size-only bound
  (residual gap `< t_k <= p_1`), and that this is insufficient because
  the round-13 witness `T=(0.20,0.15,0.12,0.08)` already satisfies the
  mesh bound via the *contiguous* match yet still fails to reach the
  true optimum, is a correct re-derivation of a fact already established
  in round 13 (re-verified, not re-litigated here); the further
  observation that the existence claim must be proved as an inductive
  step jointly indexed by `(marks,|A|)` (not a free-standing
  subset-sum covering statement) is a sound structural point, correctly
  reported as unproved.

### Verdict for `universal-adversary-strategy`

**Status: partial** (matches the builder's own self-report; not an
overclaim). **Verdict: CHANGES REQUESTED.** Real, independently
confirmed progress this round: the round-13 mark-accounting bug is
genuinely fixed; Lemma FREE-TIE-REDUCTION is a new, correctly proved,
certifiable lemma; three hard witnesses are independently reproduced
exactly under the corrected accounting. The sole remaining gap for the
whole problem is Lemma SLACK-COVER (general subset-match existence,
now correctly understood as a joint covering+value statement) — precisely
isolated, not closed.

## Build 2: `case-c-slack-covering` (new slug)

**Claims reviewed:** built a one-level averaging/pigeonhole family
`UB_i = c(m-2)*Sigma + (1-2c(m-2))*t_i` from a new corollary of the
certified Lemma DOUBLE-INSERT (Lemma DOUBLE-INSERT-MATCH-VALUE); showed
the averaging step is dominated by the deterministic choice `i=1` (since
`c(n)>1/2` for all n makes `UB_i` strictly decreasing in `t_i`); passed
3 witnesses (last one, `(965,965,958,482)`, only by margin `1/4718`);
then derived, in closed form via `sympy`, a strictly negative margin at
the uniform-tail boundary for every integer `m>=4`.

### Independent re-verification (from scratch)

- **Step 0 exact value identity.** Wrote my own exact-`Fraction` script:
  5000 random trials (list sizes 2–7, arbitrary index `i`), checking
  `oddrank(A after matching p_1 to t_i) = t_i + oddrank(REST_i)` exactly.
  **Zero violations.** This is indeed a direct, correct corollary of the
  already-certified Lemma DOUBLE-INSERT (re-read that lemma's file
  directly: statement and proof both check out as cited).

- **The negative margin (the decisive claim).** Independently re-derived
  the exact symbolic expression for `margin(m) = c(m-1) - UB_1(m)` at
  the uniform-tail boundary using my own from-scratch `sympy` script
  (not the builder's). `sympy.simplify(mine - claimed) = 0` — an exact
  symbolic match, not merely numeric agreement at sampled `m`. My own
  numeric table for `m=3..12` also matches the builder's exactly at
  `m=4` (`-1/70`) and `m=8` (`-641/453390`). The sign argument
  (denominator `2(2^m-2)(2^m-1)(m-1) > 0` for `m>=2`; numerator
  `2^m(3-m)-2 <= -2^m-2 < 0` for every integer `m>=4`) is elementary and
  I confirmed it algebraically myself — this is a genuine, exact,
  unconditional proof for every integer `m>=4`, not a numerical
  near-miss at a handful of sampled points.

- **Is this a clean refutation of the whole mechanism, or does it admit
  a fix?** Every individual step is correct (verified above). The
  builder's own Step 2 shows averaging over the family is *provably*
  dominated by the single best member `UB_1` (mean >= min is trivial,
  and here the family is monotone so the min has a closed form) — so
  there is no room to "improve" the averaging step itself; the only way
  to fix the construction is to change the family (multi-level matching
  or a value-aware leftover bound), which the builder's own diagnosis
  shows collapses into exactly the still-unsolved Lemma SLACK-COVER
  content that `universal-adversary-strategy` already owns. I checked
  this claim of "no independent leverage" is not asserted lightly: the
  write-up explicitly traces why (a coarser `c(m-2)*Sigma` bound on the
  leftover throws away exactly the information a genuine fix would need,
  and the leftover at the uniform-tail boundary is itself
  near-worst-case for the same reason recursively). This is a genuine
  structural impossibility proof for the one-level-averaging family
  (true for any weighting/refinement scheme within that family), not
  merely "we tried some candidates and they failed" — it meets the bar
  from prior-round guidance (proof-reviewer memory) for distinguishing a
  true structural dead end from an ordinary negative diagnosis.

### Verdict for `case-c-slack-covering`

**True Status: I set this to `unsolved`/dead** (overriding the builder's
self-reported `partial`) **for the purposes of continuing this specific
slug** — not because any step is wrong (every step independently
re-verified correct), but because the approach's entire premise (a
route to Case C structurally distinct from `universal-adversary-
strategy`'s explicit construction) is refuted by the builder's own
analysis: any repair reduces to duplicating the sibling approach's
still-open Lemma SLACK-COVER content, so it offers zero independent
proof leverage going forward. This is the same convergence-failure
pattern already established twice in this run for `minimax-mixed-
duality` (rounds 6-8) and `case-c-secondary-extremality` (round 11),
both of which were correctly routed RETHINK for exactly this reason
(per proof-reviewer memory: distinguish a genuine "structural
impossibility true for any refinement" from "we tried N candidates and
failed" — this is the former). **Verdict: RETHINK.** The two lemmas
produced (Lemma DOUBLE-INSERT-MATCH-VALUE and the uniform-tail-margin
negative fact) are independently verified correct and are certified
into `lemmas/` as reusable pruning/building-block facts for whichever
approach continues to attack Case C — they are not wasted, but the slug
itself should not be rebuilt without a genuinely new mechanism (not a
variant of one-level match+IH averaging).

## Lemma certification actions taken this round

- `lemmas/free-tie-reduction-move0.md` — **certified** (already present,
  independently re-verified, no changes needed).
- `lemmas/double-insert-match-value.md` — **newly certified** (written
  this round from the builder's Step 0, independently re-verified).
- `lemmas/uniform-tail-margin-negative.md` — **newly certified** (written
  this round from the builder's Step 4, independently re-verified
  symbolically).

## current.md

Updated `results/imo-2026-03/current.md` with a new "Round 14 review"
section at the top (Status remains `partial` for the whole problem),
documenting both verdicts and the independent re-verification detail
above, and reaffirming the sole open gap: Lemma SLACK-COVER (general
subset-match existence, as a joint covering+recursive-value statement
inside the `(marks,|A|)` induction) for Claim PTBI's Case C, general
`m>=4`.

## Recommendation for round 15

- Continue `universal-adversary-strategy` on Lemma SLACK-COVER directly
  (the joint covering+value induction), reusing the now-certified Lemma
  FREE-TIE-REDUCTION and Lemma DOUBLE-INSERT-MATCH-VALUE.
- Do not rebuild `case-c-slack-covering`'s one-level averaging mechanism;
  if a new "distinct route" approach is wanted, it must engage the
  leftover's recursive *value*, not just a size-based covering/mesh
  bound or a single-match-plus-generic-IH average — both are now proven
  insufficient (round 13's mesh finding + round 14's averaging-margin
  finding).
- Getting `solve2` to actually terminate at `m=8` (a smarter
  implementation — e.g. pruning subsets that cannot beat the current
  best bound, or restricting to contiguous+one-hole matches first) would
  let a future round close the empirical loop on the round-12 witness;
  this is an implementation task, not new mathematics, but worth doing
  before the next proof attempt to remove the last piece of untested
  numeric doubt.
