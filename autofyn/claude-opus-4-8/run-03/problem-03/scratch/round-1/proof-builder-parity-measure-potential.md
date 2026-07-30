# Build report — parity-measure-potential (imo-2026-03, round 1)

**Status: partial.** Answer c(n) = 2^n/(2^{n+1}−1) unchanged and confirmed for n≤4.

## What is now FULLY PROVEN (rigorous, ready to certify)
- **Lemma R (Reduction).** Claiming-game value = odd-rank sum; Liu total = (1+D)/2,
  D = Σ(−1)^{i+1}b_i. Proven by the recurrence V(S)=Σ−min_j V(S∖{b_j}) plus a componentwise
  monotonicity showing removing the largest minimises the remainder's odd-rank sum. Clean,
  complete. Shared by all three approaches — **propose certifying into lemmas/**.
- **Lemma I (Measure identity).** D = measure{ t : N(t) odd }. Complete (piece =
  ∫𝟙[t<b], swap sum/integral, alternating sum over top N(t) ranks). Corollary: even
  multiplicity everywhere ⇒ D=0. **Propose certifying.**
- **Lemma T (Toggle calculus).** A cut of s→(s_1≥s_2) toggles N-parity on [0,s_2)∪[s_1,s)
  (measure 2s_2); cumulative odd-set = O_0 △ ⨁E_i; |ΔD|≤2s_2. Complete. **Propose certifying.**

## Bounds
- **Lower bound: Case A proven** (top piece uncut ⇒ threshold band [2^n−1,2^n) has N=1 ⇒
  D≥u). **Case B is the gap** (cutting top piece; fragments dominate the sub-config — same
  interference as induction-peel's A1). GAP B2.
- **Upper bound: reduced, strategy is the gap.** I defined the greedy-match strategy and
  proved: it forces D=0 whenever Xiang keeps ANY spare cut, and D = (single leftover ℓ)
  only in the all-strict full-budget case m=n+1. So the entire upper bound collapses to
  "ℓ ≤ u" in that one case. **Then I proved greedy is INSUFFICIENT**: exact computation over
  20000 random partitions/​n gives greedy worst-case D = 0.0727(n3), 0.0344(n4), 0.0193(n5),
  0.0121(n6), each > u. Greedy meets u only for n≤2. So the correct Xiang strategy must be
  more adaptive than "match top two / halve if top dominates." GAP B3.

## Spec concerns (for the planner)
1. **The outline oversold both KEY gaps as "mechanical/attackable."** They are not
   mechanical. The lower bound is NOT just "write up the identity + one cut per scale":
   the per-cut leverage is |ΔD|≤2s_2 with s_2 up to 2^{n−1} (unnormalised), so there is NO
   uniform "≤const per cut" bound — the superincreasing cancellation argument (B2) is
   genuinely hard, and it is the SAME top-piece-fragment interference as induction-peel A1.
2. **Greedy-match (the natural B3 candidate the outline leaned on) is refuted for n≥3** by
   direct computation. Any next-round B3 attempt must NOT reuse "greedy/​match-top-two/​halve";
   the winning cut choice depends on piece ratios in a way greedy misses.
3. **Shared wall confirmed.** Both KEY gaps here coincide with induction-peel's A1/A2
   (top-piece peel/interference). Per the reviewer's own warning, if A and B both stall on
   this next round, seed a genuinely different framing for the upper bound (e.g. LP-duality /
   direct weight-function adversary bound), not another bookkeeping variant.
4. **Recursion 1/u_n = 2/u_{n−1}+1** (u_n = u_{n−1}/(2+u_{n−1})) strongly suggests the
   natural proof of BOTH bounds is a scale-recursion/​induction on n — which is exactly what
   this "no induction on n" framing forbids. The measure identity is a clean reformulation
   but does not by itself dissolve the recursion. Worth telling the outliner: the
   measure framework may need to import a light scale-induction to close B2/B3, or accept
   that its value-add is the foundational lemmas + Case A, with the hard directions owned by
   induction-peel.

## Files
- Proof: /home/agentuser/repo/results/imo-2026-03/approaches/parity-measure-potential.md
