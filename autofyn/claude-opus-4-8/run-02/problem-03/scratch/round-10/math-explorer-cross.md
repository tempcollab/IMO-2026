## imo-2026-03 — cross-leverage / unification lens (GAP-IMR vs GAP-P1)

### (a) Are GAP-IMR and GAP-P1 the same statement in two clothes?

**No — not literally, but they share the identical underlying obstruction.** Precise relation:

- **GAP-IMR** (`vertex-integrality-parity.md`) is a *single global* claim about the whole
  continuum polytope-union `Φ_n`: the global minimizer of `D̃` over all of `Φ_n` (integer AND
  fractional configs together) is attained at an integer point. If GAP-IMR is proved for a given
  `n`, it **immediately gives GAP L for that `n` in one shot** — no induction on `n`, no peeling,
  no casework needed: `μ = min_{Φ_n} D̃ = D̃(integer minimizer) ≥ 1` by the Parity Lemma, done.
- **GAP-P1** (`peel-scale-rank-induction.md`) is an *inductive* claim: assuming `D̃(F')≥1` for
  every `F'∈Φ_{n−1}` (IH, i.e. GAP L already holds one level down), show `D̃(π_0⊎F')≥1` on the
  residual `{|D̃(π_0)−D̃(F')|<1}` for every top piece `π_0`. This does not reference integrality of
  `F` or `F'` at all.

So logically, **either gap closing alone finishes the problem** — they are two independent
*sufficient* routes to the same target, not one restated as the other. Proving GAP-IMR makes the
whole peel machinery (Case A/B split, difference bound, Invariant I, GAP-P1) unnecessary; proving
GAP-P1 (for all `n`, closing the residual) makes GAP-IMR unnecessary. **Closing one does NOT
formally close the other as a corollary** — they are not inter-derivable in either direction from
what's certified so far.

However they **do bottom out on the identical combinatorial obstruction**, which is the real
cross-leverage finding: GAP-IMR's obstruction (§3.2 of `vertex-integrality-parity.md`) is that a
fractional tie-block `B` inside one dyadic *group* `π_j` cannot be integralized alone because its
group-sum `n_g·v` is fixed at a non-integer value; fixing it requires moving mass **into other
blocks of the same group**, i.e. a cross-block, same-scale coupling. GAP-P1's obstruction is that
the overlap term `λ(O_{π_0}∩O_{F'})` in the peel identity couples `π_0` (scale `j=0`) with `F'`
(scales `j≥1`) — a **cross-scale** coupling — and no static summary of `F'` suffices; the actual
witness (§7a) needing rejection is a multiset that is *not* a real dyadic refinement, i.e. one
that violates exactly the same "each scale's mass is a rigid constrained group-sum" structure that
GAP-IMR's obstruction describes. Both obstructions are instances of: **the dyadic Structure Lemma's
group-sum constraints `Σ(π_j)=2^{n−j}` tie the whole configuration together, so no local
(single-block / single-scale) argument can inject the missing `+1`.** This is the same wall
restated at two different granularities (whole-polytope vertex geometry vs. one induction step),
not the same theorem.

### (b)/(c) Can the Parity Lemma be pushed directly through the peel induction?

**Investigated and this is structurally blocked — worth flagging clearly so no builder wastes a
round on it.** The proposed combination needs "`F` is itself an integer/dyadic config when `F` is"
— but this premise is false in general. `Φ_n` is the union over **all real** feasible configs
(Xiang can cut at any real point, not just dyadic-rational ones); the peel induction's IH
`D̃(F')≥1` is stated and proved (where proved) for **every** real `F'∈Φ_{n−1}`, integer or not.
The Parity Lemma applies **only** to integer-part configs. So:

- If `F` (equivalently `F'`) happens to be integer, the Parity Lemma fires trivially and gives
  `D̃(F')` odd `≥1` — but this is already subsumed by the plain IH `D̃(F')≥1` (proved 7a to be
  insufficient anyway, since the residual counterexample witness itself has *non-dyadic* structure,
  independent of integrality — the witness `F'=(2.534,2.247,2.219)` is already fractional and
  fails for reasons of *shape*, not because it's non-integer).
- If `F'` is fractional (the generic case), the Parity Lemma simply does not apply, and there is no
  way to "push it through" the peel step without first knowing the residual's minimizer is integer
  — which is precisely GAP-IMR restricted to the residual sub-cell. So **using the Parity Lemma
  inside the peel induction presupposes exactly the fact GAP-IMR is trying to establish** (that the
  extremal/adversarial config is integer). This is a real, not superficial, circularity: you cannot
  invoke integer-total parity as a *finishing* device for GAP-P1 without first solving a
  GAP-IMR-shaped sub-problem for the residual region.
- The "residual forces near-integrality" idea in the prompt does not hold up: the residual
  `{|D̃(π_0)−D̃(F')|<1}` is a *measure-zero-adjacent but positive-dimensional* region of the
  continuum polytope, not a lattice-adjacent region; nothing in (PEEL)/(DIFF) forces integrality
  there. (Checked directly: the §7a rejected witness has `D̃(π_0⊎F')=0.146`, nowhere near an
  integer, and its rejection is on grounds of *not arising from real dyadic cuts* — a structural/
  combinatorial defect, unrelated to integer-vs-fractional.)

**Conclusion on (b)/(c): the combination does not work as stated.** The two lemmas cannot be
directly grafted; GAP-IMR would have to be proved (at least locally, on the residual) before the
Parity Lemma could contribute anything to GAP-P1, at which point GAP-IMR alone already finishes
the whole problem and the peel machinery becomes redundant scaffolding.

### What IS a productive cross-leverage opening (for the outliner)

Given (a)/(b)/(c), the one genuine synergy is **not** "run the Parity Lemma through the peel step,"
but: **use the peel decomposition (SD)/(PEEL)/(DIFF)/(Case A) as the *local* mass-transfer
mechanism that GAP-IMR's §3.3 says is missing.** GAP-IMR's own §3.3 identifies the needed proof
shape as "prove that at a global minimizer vertex every fractional tie-block is even, and the
union of even blocks can be re-split into integers using cross-block mass transfer that stays on
the optimal face." The peel machinery already supplies exactly a cross-scale mass-transfer
identity (`D̃(F)=D̃(π_0)+D̃(F')−2λ(O_{π_0}∩O_{F'})`) that operates scale-by-scale — this could be
repurposed **not** to prove `D̃(F')≥1` inductively, but to show that a scale-by-scale integer
rounding of a global minimizer preserves `D̃` (i.e., use (SD)/(DIFF) to bound how much `D̃` can
change under an integer perturbation of one scale's tie-block, keeping the group-sum fixed, and
show it cannot increase at a true minimizer). This is a genuinely different (not yet tried) use of
the certified peel identity — as a **perturbation/exchange-argument tool for GAP-IMR**, rather than
as an induction engine for GAP-P1. It is speculative (not verified numerically here) but is the
correct "combine the two certified lemmas" reading that survives scrutiny; it should be scouted,
not assumed, by whichever builder attacks it next.

### Recommendation to hand the outliner

- Do **not** dispatch a builder on "Parity Lemma finishes the peel residual directly" — shown above
  to be circular/structurally blocked.
- The two approaches remain genuinely independent routes; keep both alive, but the highest-value
  new move is: **retarget the peel identity (SD)/(DIFF), already certified, as the cross-block
  mass-transfer tool GAP-IMR's §3.3 needs**, i.e. a THIRD hybrid approach — "peel-as-exchange-
  argument-for-IMR" — distinct from both current slugs' framings (one is induction-on-n for D̃≥1
  directly, the other is an LP/vertex argument; the hybrid is an exchange argument on the *global*
  minimizer using the *local* peel identity to bound `D̃`'s change under scale-local integer
  rounding). This is a different top-level target (prove GAP-IMR by exchange, not prove GAP-P1 by
  induction) and should be logged as a new approach file, not a patch to either existing one.
- If this hybrid does not pan out quickly, the shared-wall signal from R9/R10 stands: seed a
  mechanism that avoids the odd-total-parity route entirely (2-adic valuation split N=N_++N_-,
  crux `aimo-0917`, or the shadow/position-map re-embedding, crux `aimo-0663` — see below).

### Knowledge-base entries
- `Piecewise-concavity smoothing` (kb.md line 20) — potentially relevant to the "global minimizer
  lands on an integer/boundary point" flavor of argument (smoothing/exchange to push extrema to
  extreme/lattice points) — worth checking against GAP-IMR's LP framing, not yet applied.
- No TU/network-flow/majorization entry exists in `knowledge_base.md` beyond what's already
  imported (checked via grep for "unimodular", "majoriz", "rearrange", "network flow",
  "exchange argument" — only the smoothing entry hit).

### Analogous past problems (crux corpus)
Filtered `combinatorics` × `coloring-and-parity`, `games-and-strategy`, `invariants-and-monovariants`
for "parity forces integrality/injects a +1 non-locally." Best candidates (already flagged in
`current.md`, independently re-verified as genuinely analogous in mechanism, not just subtopic):
- **`aimo-0917`** — crux "Define a potential as the count of a sign-labeling structure and preserve
  a chosen 2-adic residue... Split the invariant's count over the two possible responses as
  `N=N_++N_-`, so an odd-valuation total forces at least one branch to inherit that valuation."
  This is the closest real analog to "inject a `+1`/valuation constant non-locally": instead of an
  odd-*total*-parity argument (what the Parity Lemma does), it splits a count by *which branch of a
  choice* and uses Legendre/`S_2(n)` to force divisibility asymmetry. Directly suggests: split the
  GAP-L residual configs by an analogous branching (e.g. by `a_0` or by which dyadic scale absorbs
  the last unit of budget) and track a 2-adic valuation of a count, rather than the parity-of-total
  route both current approaches use. Genuinely different mechanism, not yet tried.
- **`aimo-0663`** — crux "run a shadow game coupled to the real one by a position map... verify a
  ONE-directional legality implication per player." Suggestive of a strategy-stealing/shadow-
  embedding route for GAP L (map a Case-B config to a reference `D̃=1` zigzag config via an explicit
  position map and show discrepancy can only increase), but this is a much looser analogy — the
  underlying games are combinatorially unrelated (path-coloring game vs. dyadic cutting game); flag
  as a weak analogy, worth a passing look only if the 2-adic route also stalls.
- No other corpus entry inspected (coloring-and-parity, 71 combinatorics cruxes scanned) matched
  the specific "odd total ⇒ integer discrepancy ⇒ ≥1" or "global LP-vertex integrality" mechanism;
  most are graph/tiling parity arguments on discrete boards, not continuum polytopes.

### Prior progress
As recorded in `current.md`: upper bound fully certified for all `n`
(`lemmas/upper-bound.md`); lower bound reduced to GAP L; GAP L reduced to two live, far-apart
partials (GAP-IMR, GAP-P1), both bottoming on cross-scale mass coupling as analyzed above. Four
certified lemma files: `parity-odd-total.md`, `peel-difference-bound.md` (this round's read
target), plus `greedy-claim.md`, `cut-flip.md`, `termwise-lattice.md`, `merged-order-layer.md`,
`reserve-target-equivalence.md`, `scale-parity-xor.md` (not re-verified this round, per assignment).

### Dead ends (do not retry)
- "Push the Parity Lemma directly through the peel step using F'/F integrality" — refuted above
  (structurally circular: requires GAP-IMR on the residual first; the residual counterexample
  witness fails on shape grounds unrelated to integrality).
- All R8 meta-refuted framings (merged-order tiling, sequential-cut potential, per-scale genfn) —
  still stand refuted, unaffected by this analysis.
- TU/B2 vertex-integrality core (R9) — still correctly deleted (fractional minimizing vertices
  exist at non-optimal cells).

### Small-case / intuition notes (conjecture, not proof)
- Numerically (both approach files, `n≤5`, exact `Fraction`) the global integer minimum of `D̃` is
  always exactly `1`, matching the target tightly — consistent across both framings.
- The obstruction pattern (fractional tie-blocks only at *non-optimal* cells for `n≤3`, per
  GAP-IMR §3.3) is suggestive that an exchange/smoothing argument (perturb toward integers,
  show `D̃` can't increase at the true optimum) is the right shape — but this is conjecture from
  small `n`, not yet attempted at the mechanism level.
