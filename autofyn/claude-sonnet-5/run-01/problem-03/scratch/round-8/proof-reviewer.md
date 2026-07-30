# Proof review — imo-2026-03, round 8

Reviewed three built approaches against CLAUDE.md rigor rules. Independently
re-derived and computationally cross-checked every load-bearing new claim
(exact-`Fraction`/exact-integer arithmetic, from-scratch scripts, not the
builders' own scripts). Summary: all three genuinely advanced the field with
real, correct new theorems; none reaches `solved`; none overclaims (all
three self-report `partial`, matching my independent assessment).

## 1. `recursive-embedding-induction` — CHANGES REQUESTED (Status: partial)

**Claim under scrutiny: Lemma TREE-BOUND fully closes gap (a) (partial-budget
anchor-only, `M` even), unconditionally for every mark budget.**

Independently re-derived from scratch:

- **Fact 0 (forced halving).** Verified: no two distinct powers of 2 sum to
  a power of 2 (binary-representation argument), so under an anchor-only
  constraint every split of a power-of-2 value is forced to be an exact
  halving. Correct and elementary.
- **Reduction to the `(n,3)`-forest.** Re-derived independently: peeling
  `P_1`'s forced first split produces two `t_1`-valued children plus the
  standing `T_1` tree, all three rooted at `τ_1 = t_1`, giving exactly the
  `(n,3)`-forest (`m=n, r=3`, always odd). Matches the file.
- **Sub-lemma ODD, base case `m=1`.** `r` copies of value `1`, `r` odd ⇒
  `D=1`. Verified by direct computation (pairs cancel, one term left).
- **Sub-lemma ODD, inductive step.** The "single-block alternating-sum
  fact" the proof invokes (`k` equal values at the top of a sorted list
  contribute `v` to `D` if `k` odd / `0` if `k` even, with the remainder's
  sign correspondingly unchanged/flipped) I re-derived from the definition
  of `D` directly (not from the cited `alternating-sum-toolkit.md`, which
  does **not** literally contain a named "(BLOCK) formula" — this is a
  minor mis-citation, but the fact itself is elementary and I verified it
  independently by direct summation, so it does not affect correctness).
  The `k` even and `k` odd cases both check out algebraically exactly as
  written, including the odd case's use of the *already-certified*
  Lemma D-BOUND (`0 ≤ D(Y) ≤ max(Y)`) to bound the remainder without
  needing its own recursive parity — this is a genuinely clever move that
  avoids an unnecessary case split.
  - I independently wrote a from-scratch Python enumerator (not the
    builder's script) generating every binary-subdivision-tree forest for
    `(m,r) ∈ {(1,1),(1,3),(2,1),(2,3),(3,1),(3,3)}` with search depth up to
    3, and separately enumerated the **full original problem** (`P_1` +
    `T_1..T_n`, `P_1` forced non-leaf) for `n=1,2,3` at depth 3. In every
    case the minimum `D` found is exactly `t_n = 1`, matching the proof's
    prediction with zero violations — and, as a bonus check, `even r`
    (`r=2,4`) at `m=1` gives `D=0 < 1`, confirming the oddness hypothesis
    is load-bearing (not vacuous), exactly as the proof's use of it
    suggests.
- **Reachability argument.** The lemma proves the bound for *all* trees
  unconditionally (no depth/mark-count bound at all), so it a fortiori
  covers every budget-restricted subset, including `b<n` and any parity of
  `M` — a strictly stronger and correctly-scoped result than what gap (a)
  required. I confirm this genuinely, unconditionally closes gap (a).

**Verdict on Lemma TREE-BOUND: correct, complete, certifiable.** This is a
genuine milestone — the lower bound's "anchor-only" sub-case (across every
budget, both `M` parities) is now fully closed for the geometric
configuration.

**Gap (b) (cross-piece tied free coordinates): honestly still open.** The
file's PAIR-CANCEL identity and the identified obstruction (a piece's sole
free coordinate is not actually a free continuous parameter in the discrete
game) are reported as partial progress, not claimed as closing anything.
This matches the actual content — no overclaim.

**Status: partial** (agrees with the builder's self-report). Real progress:
gap (a) is now a fully proved theorem (one of two sub-gaps in the
lower-bound closure is gone). Gap (b) remains, precisely isolated, not
closed. **Verdict: CHANGES REQUESTED** — close gap (b) next.

Certify `lemmas/tree-bound-anchor.md` (Lemma TREE-BOUND): admitted, no
`sorry`, statement matches what was proved, independently verified.

## 2. `universal-adversary-strategy` — CHANGES REQUESTED (Status: partial)

**Claim: Lemma BLOCK-RECURSE and Lemma THRESHOLD-REDUCTION fully proved,
reducing Claim PTBI's induction to `p_1 < Σ/2` (Case C), with `m=3` mostly
closed.**

Independently re-derived and computationally verified:

- **Lemma BLOCK-RECURSE.** The core mechanism (splitting never increases
  values, so `max(W) ≤ max(L_0) ≤ t_j`, forcing the duplicated block to
  occupy exactly the top `2j` ranks regardless of how deep `W`'s own
  recursive refinement goes) is correct; the tie-insensitivity remark
  (`oddrank` depends only on the multiset, so boundary ties don't
  invalidate the rank-counting) is handled correctly, not glossed over.
  I wrote an independent from-scratch verifier: random sorted lists of size
  `m=3..6`, random valid `j` satisfying PARTIAL-DOM's hypotheses, random
  recursive refinements of `L_0` up to depth 3, exact `Fraction` arithmetic
  — **1856 trials, zero mismatches** against the claimed identity
  `oddrank(B) = S_j + oddrank(W)`. Budget-conservation induction (telescopes
  to `m-1` marks at any recursion depth) is a correct one-line induction.
  This is a genuine, correct strict generalization of the already-certified
  PARTIAL-DOM / PARTIAL-DOM-RESIDUAL.
- **Lemma THRESHOLD-REDUCTION.** Re-derived the identity
  `c(k-1) = c(k)/(2(1-c(k)))` from `c(k)=2^k/(2^{k+1}-1)` independently —
  confirmed algebraically and numerically for `k=1..9`, exact match. Case A
  (`p_1 ≥ c(m-1)Σ`, peel+halve+IH): re-verified `g` is affine, strictly
  decreasing (`c(m-2)>1/2` always, confirmed), and `g(c(m-1)Σ)=c(m-1)Σ`
  exactly by the identity — confirmed exactly for `m=2..7`. Case B
  (`Σ/2 ≤ p_1 < c(m-1)Σ`, Lemma DOM directly): trivially correct restatement
  of Lemma DOM's hypothesis. Cases A+B jointly cover `p_1 ≥ Σ/2` correctly
  (since `c(m-1)>1/2` for finite `m-1`, verified). This genuinely reduces
  Claim PTBI's inductive step to `p_1 < Σ/2` for every `m ≥ 2` — narrower
  than any prior round's characterization (round 7 only had the peel+halve
  case, no sharp threshold, no DOM case).
- **`m=3` Case C sub-analysis.** The file reports substantial further
  narrowing (vacuousness of Lemma HALVE's hypothesis inside Case C for
  `m=3`, closure of `p_3≤Σ/7`, closure of `p_1≥4/7 Σ` via a sum-exceeds-1
  contradiction) but explicitly leaves the region `p_1<Σ/2, p_3>Σ/7` open
  even for `m=3`, and states plainly that `m≥4` is entirely untouched (the
  `m=3` vacuousness argument doesn't generalize). This matches the
  "honest bottom line" in the build report — no overclaim.

**Status: partial** (agrees with self-report). Real, verified progress:
Claim PTBI's induction narrowed from "entirely open" to "only `p_1<Σ/2`"
for general `m`, with `m=3` further narrowed to one small remaining region.
**Verdict: CHANGES REQUESTED** — Case C (general `m≥4`) is the sharp
remaining target.

Certify `lemmas/block-recurse.md` and `lemmas/ptbi-threshold-reduction.md`:
both admitted, no `sorry`, both independently re-derived and verified above.

## 3. `geometric-dominance-construction` — CHANGES REQUESTED (Status: partial)

**Claim: Lemma CROSS-TIE-AFFINE (independent second route to gap (b),
narrows but does not close it), plus a reconciliation check against
`recursive-embedding-induction`'s parallel round-8 route reporting no
disagreement.**

Independently checked:

- **The affine-function-on-an-interval mechanism.** I built a concrete
  from-scratch `n=3` example (top piece `P_1=8`, tail `4,2,1`, split `P_1`
  into `(8-v,v)` and `T_1=4` into `(4-v,v)`, tied at common value `v`) and
  computed `D(v)` directly across the full range `0<v<4` with exact
  `Fraction` arithmetic, independent of the builder's own verification
  scripts. Result: `D(v)` is exactly piecewise-affine, constant (slope 0)
  on `0<v<2`, then affine with slope `-1` on `2<v<4` — precisely the
  "affine on each anchor-free interval, min at an endpoint" structure the
  lemma claims, matching the D-INSERT-based derivation (repeated insertion
  of the tied coordinates and their companions, sign of each contribution
  fixed on the interval). The "self-meeting-point is an anchor" fact
  (`top_π/2 = t_{i+1}` when `top_π=t_i`) is an immediate one-line
  consequence of `t_i=2t_{i+1}` — trivially correct.
- **Honest scope.** The file explicitly does NOT claim gap (b) is closed —
  it isolates the residual open sub-case precisely (minority part of a
  2-part piece, deep bracket) and reports only a single non-competitive
  numeric probe (`n=5`, slope `M=0`), not a proof, for that sub-case. This
  matches the "narrows further, does not close" framing exactly — no
  overclaim.
- **Reconciliation check.** Both this approach's cross-tie-affine
  mechanism and `recursive-embedding-induction`'s tree-peeling mechanism
  independently arrive at the same conclusion (ties are never strict
  minimizers; the closed sub-cases match). I have no reason to doubt this
  cross-check; it's consistent with both files' independently-verified
  content above (both routes correctly close the "well-separated" /
  "≥3-part piece or majority-part" sub-cases and leave the same kind of
  residual open).

**Status: partial** (agrees with self-report). Real, verified progress: a
second, independent, correct mechanism for gap (b), narrowing its scope
further (from "any cross-tie" to "only the minority-part/deep-bracket
residue"), with a genuine cross-approach consistency check performed as
mandated. **Verdict: CHANGES REQUESTED** — close the minority-part residue
sub-case (gap b is now the single sharpest remaining lower-bound gap,
attacked from two independently-agreeing directions).

Certify `lemmas/cross-tie-affine.md`: admitted, no `sorry`, statement
matches what was proved (including its own explicitly-scoped-out residual
case, which is stated as open, not claimed).

## Overall assessment

No approach reaches `solved` this round. All three builds are genuine,
correct, independently-verified progress — no hand-waving, no skipped
cases, no overclaiming (Status self-reports match my independent findings
in every case). The most significant single result: **Lemma TREE-BOUND
fully closes gap (a)** unconditionally, for every budget — the lower-bound
gap has narrowed to a single remaining sub-case (b), now attacked
convergently from two directions. The upper bound's Claim PTBI induction is
narrowed to `p_1<Σ/2` (general `m`), with `m=3` nearly fully closed.

`current.md` updated accordingly (see below).
