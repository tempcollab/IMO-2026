## imo-2026-03

Round 1 — no prior approaches existed (fresh workspace). Four rival approaches
opened below, all targeting the full claim: determine c(n) with a complete proof
(Liu Bang's ≥ c(n) strategy AND Xiang Yu's ≤ c(n) adversary strategy). Conjectured
answer, independently converged on by all three explorers: **c(n) = 2^n / (2^{n+1} − 1)**.

All four approaches share one already-proven building block found independently by
all three explorers — the **claiming-phase reduction (Lemma 1)**: for a fixed
piece-length multiset sorted descending a_1≥a_2≥...≥a_m, the alternating claim
subgame's forced value for the mover is a_1+a_3+a_5+... (odd-rank sum), proved by
strong induction (see math-explorer-gamevalue.md for the complete proof — the
builder of the first-built approach should write this up cleanly and propose it as
`results/imo-2026-03/lemmas/claiming-phase-value.md` for reuse by all others).
This reduces the ENTIRE problem to a two-stage adversarial interval-cutting
optimization; every approach below builds on this reduction and does not re-derive
it from scratch.

---

geometric-dominance-construction: new
Target: c(n) = 2^n/(2^{n+1}−1) for all n, with full Liu Bang construction and
matching Xiang Yu adversary proof for ARBITRARY Liu Bang configurations.
Technique: Direct construction (explicit geometric-ratio-1/2 marking) + explicit
adversary strategy, tied by strong induction on n and a "top piece dominates the
sum of the rest" argument (crux move adapted from aimo-0117, Jesse & Tjeerd stone
game: dyadic sequence where the top term exceeds the sum of the rest forces a
dominance outcome regardless of how the rest is split).
Skeleton:
  1. Import Lemma 1 (claiming-phase value).
  2. Liu Bang marks n points giving pieces x_i = 2^{n+1-i}/(2^{n+1}-1),
     i=1..n+1 (geometric ratio 1/2) — by explicit construction.
  3. Prove Liu Bang's guarantee ≥ 2^n/(2^{n+1}-1) against ANY Xiang Yu response,
     via the domination fact x_1 > Σ_{i≥2} x_i (geometric series identity) plus
     a case analysis on how Xiang Yu distributes his n cuts across the top piece
     vs. the geometric tail.
  4. Prove Xiang Yu's adversary strategy caps Liu Bang at ≤ 2^n/(2^{n+1}-1) for
     ANY Liu Bang configuration (not just the geometric one) — via a
     cut-concentration dominance lemma (Xiang Yu never loses by moving a cut
     from a smaller piece to the current largest piece) plus an explicit optimal
     in-piece split.
  5. Combine matching bounds.
Key lemmas:
  - Top-piece domination: x_1 = 2^n/(2^{n+1}-1) exceeds Σ_{i≥2}x_i =
    (2^n-1)/(2^{n+1}-1) — because Σ_{i=2}^{n+1} 2^{n+1-i} = 2^n - 1 < 2^n
    (geometric series sum).
  - Cut-concentration dominance (OPEN) — moving a cut onto the largest piece
    weakly helps Xiang Yu, by a swap/exchange argument on the odd-rank-sum
    functional (not yet proven, numerically observed only).
Open gaps: full case analysis in step 3 (how the guarantee survives arbitrary
cut distributions across the tail); the cut-concentration dominance lemma in
step 4 (currently only numerically observed); the exact inductive recursion
linking c(n) to c(n-1) inside the dominated top piece.
Cases to cover: Xiang Yu spending 0,1,...,n cuts on the top piece (all
distributions); Xiang Yu using fewer than n effective (non-degenerate) cuts.
Watch out for: do not assume concentration-on-one-piece is optimal for Xiang Yu
without proving it; piece order along the physical stick is irrelevant to the
claiming value (state this explicitly, easy to smuggle in unjustified).

---

equalization-potential-bound: new
Target: same as above.
Technique: Potential-function / weighting (LP-duality-flavored) UPPER BOUND
argument that bounds Liu Bang's guaranteed value directly via a rank-dependent
"worst-case discount" weight, without pinning down Xiang Yu's exact optimal
response combinatorially — generalizes the explicit n=1 crossing computation
g(x)=max(1-x,x/2) to a general weighted-rearrangement argument. Deliberately a
different route from the domination/induction approaches: seeks ONE global
inequality rather than a case-split.
Skeleton:
  1. Import Lemma 1.
  2. Define V(A) = min over Xiang Yu refinements of oddrank(B); reformulate the
     bound via a rank-dependent weighting w_i such that oddrank(B) ≤ Σ w_i p_i
     for ANY configuration A and ANY Xiang Yu response, with weights depending
     only on rank i, not on the actual values p_i.
  3. Derive the weights from the n=1 exact solve (effective coefficient 1/2 on
     the bisected top piece) and conjecture w_i = 2^{-i} generalizing to all n.
  4. Solve the resulting one-shot linear/rearrangement optimization
     max Σ w_i p_i s.t. Σp_i=1 to recover the geometric configuration as the
     maximizer, PROVIDED the weights can be shown to be fixed functions of rank
     independent of the configuration (the central technical risk — see below).
  5. Matching lower bound via the same geometric construction, justified as the
     fixed point of the weight-recursion.
Key lemmas:
  - Per-piece worst-case discount w_i (OPEN, central) — Xiang Yu can force
    piece originally at rank i down to (in aggregate) w_i·p_i by recursively
    bisecting contested pieces, mirroring the n=1 halving mechanism.
  - Fixed-point uniqueness of the geometric configuration under the
    weight-recursion — by contraction/geometric-decay analogy.
Open gaps: whether the discount decomposes additively/linearly across pieces at
all given Xiang Yu's SHARED budget of n cuts (a real risk of overcounting Xiang
Yu's power if treated as independent per-piece discounts — this could make the
whole approach's upper bound invalid, not just incomplete); validity of treating
weights as fixed functions of rank rather than configuration-dependent.
Cases to cover: Xiang Yu spreading 1 cut across n pieces vs. concentrating n
cuts on 1 piece vs. any intermediate distribution — the budget coupling must
handle all of these.
Watch out for: if the budget-coupling overcounting issue cannot be fixed, mark
this approach dead-end explicitly rather than silently patching it; keep
"original rank i" and "final sorted rank after Xiang Yu's split" notationally
distinct throughout.

---

recursive-embedding-induction: new
Target: same as above, PLUS an independent derivation/check of the recursion
c(n) = g(c(n-1)) (a check on whether the conjectured closed form is even
correct, not just an alternative proof route to a fixed target).
Technique: Strong induction on n via an explicit structural game-reduction:
prove Xiang Yu's budget concentrates on Liu Bang's single largest piece (Lemma
A, shared with geometric-dominance-construction), then prove a self-duality
(Lemma B) showing the sub-problem "split one piece with k cuts to minimize its
contribution to the opponent's odd-rank share, against a fixed tail" is governed
by the same geometric-halving structure as the ORIGINAL maximization problem —
reducing c(n) to a genuine 2-term recursion in c(n-1), derived structurally
rather than guessed-and-verified.
Skeleton:
  1. Import Lemma 1.
  2. State Lemma A (adversary-budget concentration): Xiang Yu's n marks are
     optimally spent entirely inside Liu Bang's single largest piece.
  3. State Lemma B (self-dual splitting sub-problem): the "split-to-minimize"
     sub-problem faced by Xiang Yu when attacking one piece against a fixed
     tail is structurally identical (up to rescaling) to the original
     "construct-to-maximize" problem — giving a recursion for c(n) via c(n-1).
  4. Derive the exact recursion algebra (currently NOT nailed down — the central
     gap) and verify base cases c(0)=1 (trivial, no marks ⇒ one piece), c(1)=2/3
     (already proven exactly).
  5. Solve the recursion, confirm (or refute) it matches 2^n/(2^{n+1}-1).
Key lemmas:
  - Lemma A (shared with geometric-dominance-construction) — OPEN.
  - Lemma B (self-dual splitting sub-problem) — OPEN, the single biggest
    unknown; mechanism (conjectured): duality between "construct to maximize
    your own odd-ranks" and "split to minimize the opponent's odd-ranks," both
    governed by the identical extremal geometric structure.
Open gaps: Lemma A (shared); Lemma B and the exact recursion algebra — if this
duality fails even at n=2 by hand-check, this approach's Step 3 should be marked
a confirmed dead end.
Cases to cover: verify the sub-problem's own cut budget doesn't secretly
interact with the tail beyond simple merging into the sorted list.
Watch out for: HIGH RISK / HIGH PAYOFF — builder should hand-check Lemma B
concretely on n=2 BEFORE investing in the general proof; if it fails even there,
report precisely which sub-case broke rather than patching around it.

---

majorization-smoothing: new
Target: same as above.
Technique: Global smoothing/exchange argument on the CONTINUOUS configuration
space (both players' choices as real vectors), using local perturbation /
first-order (KKT-style) stationarity conditions plus a concavity argument for
GLOBAL optimality — genuinely different from the other three: no induction on
n, no explicit "who attacks which piece" case-split, no configuration-dependent
weight-recursion. Self-contained; does NOT import Lemma A or Lemma B from the
other approaches.
Skeleton:
  1. Import Lemma 1; reformulate as Liu Bang picking p=(p_1,...,p_{n+1}) on the
     simplex, Xiang Yu picking a refinement using ≤n total splits to minimize
     the odd-rank sum.
  2. Lemma C: for fixed p, Xiang Yu's best response, as a function of p, is a
     MIN of finitely many piecewise-linear-in-p functions (one per
     combinatorial "attack type"), hence V(p) is CONCAVE — established via an
     explicit first-order/directional-derivative analysis of the odd-rank-sum
     functional under piece-split perturbations.
  3. Given concavity, apply standard KKT/Lagrange theory on the simplex: any
     stationary point of V is the GLOBAL max (concave function on convex
     compact set) — this is the approach's main selling point, avoiding the
     case-enumeration burden of the induction-based approaches.
  4. Solve the stationarity system explicitly (Lemma D) to show it forces
     p*_i/p*_{i+1}=2 for all i, recovering the geometric sequence, matching the
     n=1 exact crossing computation g(x)=max(1-x,x/2).
  5. If concavity (Lemma C) fails to hold cleanly, fall back to explicit
     region-by-region case enumeration (flagged as a more laborious contingency).
Key lemmas:
  - Lemma C (concavity of V) — OPEN but promising; mechanism: V is a min over
    finitely many linear-in-p functionals (one per Xiang Yu attack type), and a
    min of linear functions is concave — PROVIDED the inner optimization over
    continuous split ratios within each attack type is resolved first (needs
    care, flagged explicitly as a subtlety, not a free assumption).
  - Lemma D (stationarity solves to geometric sequence) — OPEN, expected to
    telescope via the same halving mechanism as the n=1 case.
Open gaps: Lemma C's concavity (the subtle two-level minimax collapse into a
single concave function of p needs genuine verification, not assertion); the
explicit derivation of V(p) and its stationarity system (substantial
computation, not yet done); the fallback case-enumeration if concavity fails.
Cases to cover: fallback region-by-region enumeration of Xiang Yu's response
types if Lemma C fails.
Watch out for: do not assert "V is a min of linear functions hence concave"
without first resolving the INNER optimization over continuous split
parameters within each fixed combinatorial type — verify this reduction
carefully, it's the easiest place to introduce a silent error.

---

Summary for outline-reviewer: 4 approaches on the table, all targeting the full
claim end-to-end. Two (`geometric-dominance-construction`,
`recursive-embedding-induction`) share the open Lemma A (cut-concentration
dominance) and pursue induction/construction; two (`equalization-potential-bound`,
`majorization-smoothing`) pursue non-inductive global arguments (weighted LP-style
vs. continuous concavity/smoothing respectively) and are framed to be robust even
if Lemma A turns out to be false or hard. This spread covers: (a) the direct
"nail the exact construction+adversary" route, (b) a recursion-first route that
independently double-checks the conjectured closed form, (c) a weighting/LP route,
(d) a calculus/concavity route. Recommend builders start on
`geometric-dominance-construction` (most concrete, highest chance of a checkable
partial result this round — Lemma 1 write-up + top-piece domination is immediately
provable) and `recursive-embedding-induction`'s Lemma B hand-check at n=2 (cheap,
high information value: confirms or refutes the whole recursive-duality idea
early). The other two are higher-risk/higher-payoff and can run in parallel.
