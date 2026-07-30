# Build report — parity-measure-potential (round 2)

Status: **partial** (advanced; two localized gaps remain, both now sharp upper-bound-flavoured
inequalities on strictly smaller multisets).

## Closed / new this round
- **Upper bound** recast as clean strong induction UB(k) with the exact reduction threshold
  `2Σ_T ≥ L(1−u_k/u_{k−j}) = L·2^{k−j+1}(2^j−1)u_k`. Proved in full the **bisect branch**
  (`a₁≥c(k)L`) and **single-match branch** (`a₂≥c(k)L/2`), both via Lemma P. These fully
  solve **UB(1)** (n=1, c=2/3) end to end.
- **Lower bound** recast as strong induction on n. Proved the **top-scale dichotomy**: at most
  one final piece exceeds `2^{n−1}` (from superincreasing). Split into Case A (uncut top, done),
  a=1, a=0.
- **NEW exact identity (a=1):** `D(S) = f₁ − D(S_L)` where `f₁` is the unique piece `>2^{n−1}`
  and `S_L=S∖{f₁}`. Derived from Lemma I (`g_S = 1[t<f₁] ⊕ g_{S_L}`). Verified numerically
  exact. Reduces lower-bound a=1 to `D(S_L) ≤ f₁−1` (numerically TRUE and tight, margin→0).
- **Closed a=0 equal-bisection subcase:** `2^n→2^{n−1},2^{n−1}` cancels (Lemma P) ⇒ reduces to
  refinement of C_{n−1} ⇒ IH gives D≥1.
- Numeric confirmations: lower-bound min D = 1 (units u) for n≤5; identity exact;
  `D(S_L)≤f₁−1` holds with margin ≥0 (tight).

## Remaining gaps (all sharply localized)
- **GAP U** (upper crux, shared with induction-peel): subset-cover feasibility — balanced
  regime `a₁<c(k)L ∧ a₂<c(k)L/2` (first at k=2) needs a multi-pair `T` with `Σ_T∈[Lθ_j,a₁]`;
  proving existence is a knapsack-type disjunction.
- **GAP L1** (lower a=1): prove `D(S_L) ≤ f₁−1`. Upper-type inequality; needs cancellation of
  `2^n`'s sibling fragment `2^n−f₁` against the tail. Trivial `D(S_L)≤2^{n-1}` is short.
- **GAP L2** (lower a=0): top shredded into ≥3 all-`≤2^{n-1}` fragments; make Lemma-P
  cancelling-pair telescope into C_{n−1} exhaustive.

## Spec concerns
None new. Multiset reduction (Lemma R preliminary) and continuity/distinctness argument stand.
Answer c(n)=2^n/(2^{n+1}−1) confirmed; n=1 fully proved both directions in this file.

## Promotable lemmas (for reviewer to certify)
1. Dyadic top-scale dichotomy (≤1 piece >2^{n−1}).
2. a=1 splitting identity `D(S)=f₁−D(S∖{f₁})` when f₁ exceeds all other pieces.
3. Upper-bound peel threshold `2Σ_T ≥ L(1−u_k/u_{k−j})`.
