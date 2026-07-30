# Proof-reviewer — Round 8 (imo-2026-03, GAP L)

Context: upper bound already certified (`lemmas/upper-bound.md`) — not re-reviewed. Only open
wall is GAP L (lower bound, Case B) ⇔ `(△⋆)` `λ_{(0,θ)}{M odd}≥1−β` ⇔ `E(F)≤2^n−1`. Three
far-apart framings attacked it; each reports a partial + a structural negative. I verified every
load-bearing claim independently (algebra re-derived from scratch; numerics reproduced).

Independent verifications run: base value `D̃(F_0)=(2^{n+1}+(−1)^n)/3` = 1,3,5,11,21 for n=1..5 ✓;
`(⊞)` scale-XOR identity 0/20000 mismatches over random refinements ✓; telescope minimal witness
c=(−1,0,1,2,1,0,−1), s=(+1.237,0,0,−2.046,0,0,+1.916), Σs=1.107=D̃−1 ✓; `(△△)` and `R^*`
admissibility re-derived by hand ✓.

---

## Slug 1: induction-recursion-telescope — VERDICT: CHANGES REQUESTED (Status: partial)

Correctness ✓ / Rigor ✓ / Progress: sharpened + eliminated a family (net negative but valuable).

Verified claims:
- **Circularity of the tiling (§15a).** A partition of `{1..m}` into consecutive nonneg-sum
  blocks exists iff the total `Σs_i≥0` (single block `[1,m]`). Correct and trivial — the device
  is content-free unless blocks are certified by bounded *local* windows. Sound.
- **No local window certificate (§15b).** Minimal witness reproduced exactly: the sole deficit
  `s_4=−2.046` strictly exceeds each adjacent surplus (`1.237`, `1.916`), so its only nonneg
  window is the full list. Rigorous elimination of the bounded-window family.
- **Lemma H `maxc≤|Y|` (§15c).** Correct (negative count `≥0`). Trivial but true.
- **Identity `(△△)` `∫(⌊M⁺/2⌋−⌈M⁻/2⌉)=½∫M−½D̃` (§15d).** Re-derived independently:
  `⌊k/2⌋=k/2−½1[k odd]`, `⌈k/2⌉=k/2+½1[k odd]`, and `1[M⁺ odd]+1[M⁻ odd]=1[M odd]` pointwise.
  Exact. This correctly proves every layer/summed/`(♠)`/`(△⋆)` form is a pure measure-algebra
  restatement of `D̃≥1` (trivial bound → `D̃≥0`, off by ½).

No overclaim: file honestly marks partial, GAP L open. The Status in the approach file (`partial`)
is CORRECT. This slug owns the certified `(△)/(△⋆)` machinery and is the leader on the wall; the
merged-order block/window/matching family is now fully eliminated (matching, scalar, top-reserve,
tiling). Keep live to advance on `(△⋆)` by a non-local argument through Z's cut-tree — NOT another
merged-order reshuffle. → CHANGES REQUESTED.

Certified this round: `lemmas/merged-order-layer.md` (Lemma H + `(△△)` + cached tiling-negative).

## Slug 2: cut-sequence-potential — VERDICT: RETHINK (Status: unsolved as an engine)

Correctness ✓ / Rigor ✓ / Progress: a proven structural obstruction (kills a whole family).

- **Reserve⇔Target Equivalence Theorem (§2).** Re-derived independently. The DP recursion
  `minreach(P,b)=min(D̃(P), min_{P→P'} minreach(P',b−1))` is correct; the value-function reserve
  `R^*(P,b)=D̃(P)−minreach(P,b)` satisfies (R0)–(R3), and (⇒) is telescoping. The theorem is
  genuinely PROVEN (not hand-waved). It is a standard amortized-potential/value-function argument,
  applied correctly.
- **Per-cut law `ΔD̃=λ(S)−2λ(S∩O)` with `S=[0,x)∪[L−x,L)`.** Direct consequence of the certified
  Cut-Flip toggle set (odd indicator XOR `1_S`). Correct.
- Coarse-reserve and summed-magnitude refutations (`R^*` not a function of `(D̃,b)`; `R^*(F_0,b)`
  strictly concave `0,6,8,10,10` at n=4) are correct numeric evidence, consistent with the theorem.

The Equivalence Theorem shows the sequential monovariant is **logically equivalent** to GAP L —
no independent leverage. As an *independent engine* the approach is fatally broken (provably no
easier than the target). Builder's own recommendation is RETHINK; I concur. The approach's
recorded Status (`partial, RETHINK-leaning`) understates it — the correct routing is RETHINK
(back to outliner; the sequential-count/potential family is pruned). The proven theorem is the
banked value. → RETHINK.

Certified this round: `lemmas/reserve-target-equivalence.md`.

## Slug 3: even-rank-doublecount — VERDICT: RETHINK (Status: unsolved for the genfn mechanism)

Correctness ✓ / Rigor of the identity ✓ / Progress: a new clean reformulation, mechanism dead.

- **`(⊞)` scale-parity XOR identity (§2, Lemmas 2.1–2.2).** Re-derived and numerically verified
  (0/20000). `E=∫⌊N/2⌋`, `O=∫⌈N/2⌉` via `w_{2k}=λ{N≥2k}`; `D̃=∫1[N odd]=∫⊕_j 1[N_j odd]` since
  `N=Σ_j N_j`; roots-of-unity `½∫(1−∏_jσ_j)` since `1[N odd]=½(1−(−1)^N)`. Fully correct and
  reusable. Genuinely game-free/measure-free and keeps every scale separate.
- **Genfn-mechanism failure (§3).** The non-additivity `∫⊕_j s_j ≠ Σ_j∫s_j` is correct (concrete
  all-uncut check: `Σ_j D̃_j=2^{n+1}−1 ≠ (2^{n+1}+(−1)^n)/3`). The front-loaded dichotomy
  (prefix-budget-ok slice has `min D̃=4/8/9`; every near-tight config front-loaded) is honest
  empirical evidence — NOT a proven impossibility theorem, but a legitimate cheap-kill that the
  per-scale genfn identity cannot close the bound.

Note (honesty caveat for the meta-conclusion): unlike slugs 1–2 whose obstructions are *proven
theorems* (`(△△)` circularity; Equivalence Theorem), this slug's mechanism-failure is
*empirical* (cheap-kill), not a proof of impossibility. The reformulation `(⊞)` is proven; the
"genfn can't close it" is a well-supported RETHINK signal, correctly not overclaimed as a theorem.
The genfn mechanism as set up is dead → RETHINK (re-plan around `(⊞)` as a covering/discrepancy
framing, not a per-scale identity). → RETHINK, `(⊞)` preserved.

Certified this round: `lemmas/scale-parity-xor.md`.

---

## Meta-conclusion assessment
The claim "a whole class of framings (merged-order measure, sequential-count, genfn) is provably
equivalent to GAP L and cannot inject the budget non-locally" is:
- **Rigorously established** for the merged-order measure family (`(△△)` + tiling circularity)
  and the sequential-cut family (Reserve⇔Target Equivalence Theorem). Both PROVEN.
- **Empirically established (not a theorem)** for the scale-graded genfn — the reformulation
  `(⊞)` is proven, but its non-closure is a cheap-kill, not an impossibility proof.

Collectively this correctly directs next round toward framings that use Z's recursive dyadic
cut-tree ORIGIN with the budget `Σa_j≤n` entering non-locally (covering argument on the `s_j`
from `(⊞)`, two-level joint induction across scales, or a strategy-stealing route bypassing the
merged-order reduction). Three lemmas certified into `lemmas/`.

Routing summary:
- induction-recursion-telescope → CHANGES REQUESTED (partial; leader, keep live on `(△⋆)`)
- cut-sequence-potential → RETHINK (unsolved engine; sequential family pruned by proven theorem)
- even-rank-doublecount → RETHINK (unsolved genfn mechanism; `(⊞)` preserved to seed a new framing)
