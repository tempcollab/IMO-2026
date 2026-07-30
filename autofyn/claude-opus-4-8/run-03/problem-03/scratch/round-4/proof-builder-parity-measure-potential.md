# Build report — parity-measure-potential (imo-2026-03, round 4)

Status: **partial** (unchanged flag, but GAP U re-scoped with a genuine advance + a decisive
negative result). Answer CONFIRMED c(n)=2^n/(2^{n+1}−1); not re-derived.

## What I was asked to close
GAP U (upper bound, adaptive subset-cover feasibility): prove the mass-threshold subset-cover
disjunction is exhaustive over every sorted full-budget profile, profile-independently (not
spot-checks), and that each branch respects the residual piece-count bound.

## Outcome — two hard results

### 1. NEW closed region: `a₁ ≥ L/2` fully closed, profile-independently (Branch (2), whole-tail peel)
For a sorted full-budget profile `a₁≥…≥a_m`, sum `L`, with `L/2 ≤ a₁ ≤ c(k)L`: cut `a₁` into
the `m−1` tail values plus leftover `2a₁−L ≥ 0` (≤ k cuts; feasible since `Σ_tail = L−a₁ ≤ a₁`
iff `a₁ ≥ L/2`). Lemma P deletes all `m−1` cancelling pairs, leaving the **single piece** `2a₁−L`,
so `D = 2a₁−L` **exactly**. And `2a₁−L ≤ u_kL ⟺ a₁ ≤ c(k)L`, using `c(k)=(1+u_k)/2` (verified:
`(1+1/(2^{k+1}−1))/2 = 2^k/(2^{k+1}−1)=c(k)`). Combined with Branch (0) (bisect, `a₁≥c(k)L`), the
entire range `a₁ ≥ L/2` is closed for every `k≥1`. This is fully rigorous and profile-independent;
it upgrades the previous proven region (only `a₁≥c(k)L` + the `a₂≥c(k)L/2` strip). Since
`c(k)>1/2`, the strip `[L/2,c(k)L]` is nonempty and only Branch (2) fills it.

### 2. REFUTATION of the GAP U lever: the mass-threshold disjunction is NON-EXHAUSTIVE for `a₁<L/2`
I did NOT present a spot-check as a proof (per the reviewer's instruction) — I instead found a
**counterexample** proving the disjunction cannot be made exhaustive:

- `A = (0.44, 0.281, 0.279)`, k=2, full budget. Every threshold move is unavailable:
  Branch (0) needs `a₁≥c(2)=4/7≈0.571` (0.44 fails); Branch (2) needs `a₁≥L/2` (0.44 fails);
  `j=1` peel: size-1 sums `≤0.281 < θ_1=2/7≈0.2857`; `j=2` peel: only size-2 set sums
  `0.560 > a₁=0.44` (cap violated). No move in the disjunction exists.
- Yet true minimax `D = 0.002 ≤ 1/7` (direct minimax computation) — Xiang bisects `a₁` and wins,
  because the tail `{0.281,0.279}` near-cancels (`D=0.002`), far below the worst-case mass bound
  `u_1·0.56≈0.187` the threshold uses.
- **General diagnosis:** any reduction that bounds the post-peel residual by a function of its
  total *mass* alone cannot close `a₁<L/2`, because residual `D` depends on internal structure,
  not mass. A whole band (numerically `a₁∈[0.43,0.5)` with near-equal tail, k=2) defeats every
  mass threshold while being won by bisection. The subset-cover lever is therefore dead for
  `a₁<L/2`.

Verified computationally: `min_{≤2 cuts} D(0.44,0.281,0.279)=0.002`; also `(0.5,0.28,0.22)→0`,
`(0.44,0.28,0.28)→0`, dyadic `(4/7,2/7,1/7)→1/7` (extremal, tight). The minimax value ≤ u_k always
holds (the theorem is true); it is the *mass-threshold proof method* that fails, not the claim.

## Remaining gap (re-scoped, honest)
`a₁ < L/2` at full budget requires a **D-tracking** argument, not more subset-cover bookkeeping.
Two concrete routes already in the field: (i) import induction-peel's exact dominant-cut identity
`D_new = D_C − 2μ(E_R∩[0,p₂))` (its bisection case) to compute the top-cut residual's D exactly;
(ii) the smoothing/majorization framing. Recommend the outliner RETHINK GAP U toward these.

## Promotable lemmas (proposed for certification)
- **Whole-tail-peel closed region:** `L/2≤a₁≤c(k)L ⇒ D=2a₁−L≤u_kL` (proof above). Reusable in
  every upper-bound approach; profile-independent.
- **(Negative, record) Mass-threshold subset-cover is non-exhaustive for `a₁<L/2`** — witness
  `(0.44,0.281,0.279)`. Documents that no mass-only reduction closes the balanced regime; stops
  the field re-attempting subset-cover variants.

## Spec concerns
- The dispatched GAP U lever ("prove the subset-cover disjunction exhaustive with a
  profile-independent argument") is **provably false** as stated — the disjunction is
  non-exhaustive for `a₁<L/2`. I closed the part that IS true (`a₁≥L/2`) and refuted the rest
  rather than paper over it. This makes the upper wall in this approach a partial-with-hard-gap;
  the field should route GAP U's `a₁<L/2` regime to a D-tracking approach (induction-peel /
  smoothing), consistent with the reviewer's field-diversity note. Suggest CHANGES REQUESTED
  (real progress: `a₁≥L/2` closed) with the RETHINK hand-off for `a₁<L/2` recorded above.
