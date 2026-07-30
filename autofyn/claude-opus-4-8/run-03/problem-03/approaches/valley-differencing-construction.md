## Status
unsolved (new — round 8 skeleton; UPPER valley by explicit construction, not counting)

## Approach: valley-differencing-construction (framing I — Xiang's cuts given by an explicit sorted-differencing chain with a DELETE-repair prefix; constructive, existential-free)

Target (the whole claim): for every positive integer n the largest c Liu can guarantee is
c(n)=2^n/(2^{n+1}−1), equivalently minimax D=u_n=1/(2^{n+1}−1).

**Why far from the field.** breakpoint-vertex and subset-sum-pigeonhole both attack Prop UV
*existentially* — VERT vertex-enumeration or a pigeonhole over the achievable family — and the
explorer (upper lens, round 8) confirmed those two are the SAME tree-realizable-subset-sum object
in two languages. This approach instead **exhibits Xiang's response by an explicit algorithm** and
bounds its leftover directly, never counting subsets or invoking a vertex theorem. It is the
constructive dual of RL/VS's own machinery (a nonnegative differencing tree), turned into a
concrete recipe with a proven overshoot bound. Distinct route: construction + induction on the
number of surviving pieces, not existence.

Imports (certified, no re-proof): Lemmas R, M/T, P, DM (elementary-reductions), U0, RL
(leftover-realizability), whole-tail-peel, Reduction R-UV.

### Reduction (imported, exact)
By R/M the game is scalar minimax of D over refinements. By U0(c) the upper bound is nontrivial
only at full budget m=n+1. By whole-tail-peel the range a₁≥L/2 is closed. By Reduction R-UV
(certified) the residual valley {m=n+1, a₁<L/2, a₂<β_nL, β_n=2^{n−1}/(2^{n+1}−1)} holds iff
min 𝓡(A) ≤ u_nL, where 𝓡(A) is the achievable-leftover set of ≤n-move DELETE/MATCH sequences,
and by Lemma RL every element of 𝓡(A) is a **nonnegative differencing-tree value** on a subset T.

### The construction (the distinct content)
Sort A descending: a₁≥a₂≥…≥a_{n+1}. Xiang plays the following **subset-prefix + sorted-difference**
recipe, all moves legal DELETE/MATCH (each one cut):

1. **DELETE-repair prefix.** Choose an index set to DELETE (drop) so that the surviving subset T
   is *balanced-coverable*: define the running remainder r starting at a₁ and greedily MATCH r with
   the next surviving piece (r ← |r − a_j|), processing survivors in descending order. DELETE a
   piece a_j at the moment it would make the remainder *increase past* the current running bound
   (i.e. when a_j is too small to help drive r down and would only be wasted). Concretely: keep a_j
   iff a_j ≤ r_current; DELETE it otherwise is WRONG (large pieces must be kept) — the correct rule
   is the mirror of Karmarkar–Karp with the size hypotheses: keep every piece while r > 0 and DELETE
   only the terminal tail once r has been driven below u_nL.
2. **Sorted-difference chain.** On the survivors, run r₁=a₁, r_k=|r_{k−1} − a_k| (a left-deep
   nonnegative differencing tree = MATCH the running remainder with the next survivor). This is
   tree-realizable (Lemma RL), so the final r is a legal leftover ρ∈𝓡(A).
3. **Output.** ρ = final remainder ≤ u_nL, giving a legal ≤n-cut Xiang response with D=ρ≤u_nL
   (Reduction R-UV).

### Why it should work (mechanism, using BOTH valley hypotheses)
- **a₁<L/2 drives r to 0.** Since a₁ < a₂+…+a_{n+1}, the total of the rest exceeds a₁, so the
  descending-difference chain cannot get "stuck positive": the remainder is repeatedly reduced and
  crosses below every surviving piece's scale. (aimo-0796's sequential-append discrepancy bound
  gives the crude ρ < max survivor; the valley needs the sharp bound below.)
- **a₂<β_nL sharpens the overshoot.** The extremal dyadic profile a_i=2^{n+1−i}/(2^{n+1}−1) is the
  model: the descending cascade 2^n−2^{n−1}−…−1 telescopes to exactly 1=u_n·(2^{n+1}−1), i.e. the
  chain leftover is exactly u_nL, tight. The claim to prove is that pushing a₂ below β_nL (and a₁
  below L/2) can only *decrease* the chain leftover relative to this dyadic tight case — a
  monotone/telescoping overshoot bound by induction on the number of survivors.

## Round 10 revision — scope narrowed to NEAR-UNIFORM; greedy chain replaced by simultaneous pairing

The R8 greedy sorted-difference chain (GAP-CHAIN) is REFUTED (single-pass overshoot up to 7.5×, R9).
Re-plan: narrow this slug to the NEAR-UNIFORM valley only (all n+1 pieces within an explicit factor-≈2
band — the residual case breakpoint-vertex delegates), and replace the sequential chain with an
explicit SIMULTANEOUS even-cancellation pairing: sort descending, MATCH adjacent pairs
(a₁,a₂),(a₃,a₄),…; the narrow band forces every |a_{2i−1}−a_{2i}| ≤ (band ratio −1)·a_{2i} ≤ u_nL, the
many near-0 differences even-cancel (Lemma U0 mechanism), and the ≤1 leftover odd piece is DELETEd
within budget, giving reachable value 0 or ≤u_nL. Make-or-break lemma INTERLEAVE-CANCEL: in a factor-≈2
band the sorted-adjacent pairing residual telescopes ≤u_nL (adjacency in a sorted narrow band minimizes
each pairwise gap, matching the dyadic cascade's tight u_nL). This is a SIMULTANEOUS pairing, NOT a
sequential chain — do not resurrect the greedy chain. Stays far apart from breakpoint-vertex
(existential two-level search): this is the explicit constructive dual for the near-uniform tail.

## Open gaps
- **GAP-CHAIN (make-or-break).** Prove the sorted-difference chain leftover ρ satisfies ρ≤u_nL for
  every full-budget valley profile, choosing the DELETE-repair subset in closed form. The crude
  aimo-0796 bound ρ<a₂ is off by up to 2^{n−1} (since a₂ can be ≈2^{n−1}u_nL=β_nL), so a genuine
  telescoping bound is required, not the sequential-append lemma alone. The induction should track,
  after subtracting the first k survivors, r_k ≤ (remaining survivor-sum) with an h-scale
  telescoping matching the dyadic cascade; the DELETE-repair must be specified as a function of how
  far A is from dyadic. This is the exact constructive analogue of Prop UV; equivalent to it, but
  attacked by an explicit algorithm rather than pigeonhole/enumeration.
- **GAP-DELETE-RULE.** Pin down the DELETE set precisely (which small pieces, how many) so the chain
  is well-defined and budget-legal (≤n cuts total: |T|−1 MATCHes + (n+1−|T|) DELETEs = n). Step 1's
  rule above is stated loosely and must be made deterministic and proven correct.

## Lower bound
Imported from the certified reduction + TB; the lower exchange is carried by the lower slugs
(parity-measure-potential / ballot-matching), not this approach's contribution.

## Approaches tried
- (round 8, new) registered as skeleton. Constructive sorted-differencing + DELETE-repair recipe
  laid out; the sharp telescoping overshoot bound (GAP-CHAIN) and the DELETE rule (GAP-DELETE-RULE)
  isolated. Genuinely far from breakpoint-vertex (existential vertex enumeration) and
  subset-sum-pigeonhole (existential counting): this is an explicit algorithm with a proven bound.

## Current best
Import of the full certified reduction (R/M/U0/whole-tail-peel/R-UV/RL); upper valley reduced to a
constructive statement: an explicit sorted-difference chain on a DELETE-repaired subset leaves
ρ≤u_nL. The dyadic cascade (telescoping to exactly u_nL) is the tight model to generalize;
GAP-CHAIN + GAP-DELETE-RULE open.
