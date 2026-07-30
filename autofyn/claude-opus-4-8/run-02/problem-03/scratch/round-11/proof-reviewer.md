# Proof-reviewer — Round 11 (imo-2026-03, GAP L / lower-bound Case B)

Upper bound is DONE/certified — not re-reviewed. Both slugs target GAP L (`I_n:=∫_{(0,θ)}⌊M/2⌋≤0`,
`D̃=1−2I_n`, `M=N_{π_0}−N_{F'}`). Neither claims a full solve. All numerics below were reproduced
independently by me with exact `Fraction`/integer arithmetic.

---

## Slug 1: peel-scale-rank-induction

**Verdict: CHANGES REQUESTED. Status: partial.** (Builder's recorded Status `partial` is CORRECT.)

### Load-bearing new claim re-derived: the ladder-interleaving identity `(★-id)` — HOLDS

Independently re-derived §10.2. With `D̃(G)=Σ_j s_j w_j` (`s_j=(−1)^{j−1}`, Lemma G) and colour sign
`τ_j=+1` red / `−1` blue, the colour sum is `Σ_j τ_j w_j = Σπ_0−ΣL = 2^n−(2^n−1) = 1` exactly (C).
Subtracting, `D̃−1 = Σ_j(s_j−τ_j)w_j`, and `s_j−τ_j ∈ {0,−2,+2,0}` for red-odd / red-even /
blue-odd / blue-even respectively, giving
`D̃(π_0⊎L) = 1 + 2(Σ_{blue odd} − Σ_{red even})`. **Correct.** Tie-break-independent (D̃ and (C) both
are). My check: `0` mismatches of `(★-id)` AND of the FLOOR consistency `I_n=Σ_{red even}−Σ_{blue odd}`
over `3·10³` random `π_0` per `n=1..6`, exact `Fraction`. The identity is a clean, genuinely new,
fully-proven restatement of the extremal base case → **CERTIFIED** as
`lemmas/ladder-interleaving-identity.md`.

### Is the base case `D̃(π_0⊎L)≥1` PROVEN for every partition? NO.

- §10.3 (`M≤1` ⇒ `⌊M/2⌋≤0` pointwise ⇒ `I_n≤0`): **correct, rigorous.** Closes ≈88%.
- §10.4 (`(DIFF)` shell, exact `D̃(L)=(2^n−(−1)^n)/3`): **correct, rigorous.** I verified the closed
  form (1,1,3,5,11,21 for n=1..6).
- §10.5 (`n=1` identically `D̃=1`): **correct.**
- **GAP-P1′-a (OPEN, real gap):** the residual cross-block ladder-dominance form of `(★)` where both
  `M≥2` somewhere and `|D̃(π_0)−D̃(L)|<1`. The builder is HONEST that the naive per-block charge
  `Σ_{red even}≤Σ_i⌈m_i/2⌉b_i` is insufficient (its sufficient condition fails ≈51%) and that a
  cross-`k` tail-cancellation argument is missing. The rank-parity formula `rank(b_i)=i+P_i` is
  correct. But `(★)` itself is NOT proved on the residual — only asserted true (min `D̃=1`
  numerically, which I confirmed for all integer partitions `n≤6`).
- **GAP-P1′-b (OPEN, real gap):** reduction of general `b` to `b=0` is not attempted; the builder
  correctly records that the pointwise per-cut monovariant holding `π_0` fixed is FALSE (~30%
  violations), so it must be a slice-max statement in which `π_0` co-varies — unproven.

**Assessment.** Real, bankable progress: a new certified identity plus reduction of the extremal base
case to ONE combinatorial inequality, closed on two large regions + all `n=1`. Two explicit,
correctly-flagged gaps remain (GAP-P1′-a base-case dominance; GAP-P1′-b reduction-to-base). No
overclaim. Scores — Correctness 10/10 (everything written is valid); Completeness 5/10 (base case
core + reduction-to-base open); Progress: significant (cleanest base-case form to date).

**Precise remaining gap (whole problem):** prove `(★) Σ_{blue odd} ≥ Σ_{red even}` on the residual
via cross-block ladder-dominance (GAP-P1′-a), AND lift `b=0` to all feasible `b` as a slice-max
statement (GAP-P1′-b). Until both close, GAP L — and the problem — stays open.

---

## Slug 2: allocation-vertex-corner

**Verdict: RETHINK. Status: unsolved (as an engine).** (Builder's recorded Status `partial` overstates
it — the route's engine is refuted; the whole-problem contribution is a single surviving lemma + an
honest negative. As a *route to GAP L* it is unsolved and must return to the outliner.)

### Honest negative re-verified: `φ(b)` pruning has NO separating power — CORRECT

I reproduced both exact ties (integer, exact):
- `b=2`: `n=4`, `a=(1,2,0,0,0)`, `F={8,8,5,4,2,2,1,1}`, `ΣF=31=2^5−1`, alt-sum
  `8−8+5−4+2−2+1−1=1` ⇒ `D̃=1`, `I_n=0`. Valid dyadic refinement, budget `Σa_j=3≤4`.
- `b=3`: `n=4`, `F={8,8,3,3,2,2,2,2,1}`, `D̃=1`, `I_n=0`.

So the tie set `{I_n=0}` is reached at `b∈{0,2,3}`; a `φ(b)` negative for `b≥1` is impossible, and no
`n`-independent `b`-cutoff isolates the tie. The refutation is **correct and decisive** — the engine
(Step 2) is dead. Closing `I_n=P−Q≤0` still needs `Q≥P`, governed by `F'`'s recursive cut-tree — the
field's shared wall — which this allocation route does not escape.

### Surviving lemma re-derived: Positive-Layer Localization — HOLDS

`{M≥2k}⊆{N_{π_0}≥2k}=(0,y_{2k})` (measure `y_{2k}`, empty unless `π_0` has `≥2k` parts), `y_{2k}≤y_2≤θ`,
so `P=Σ_k λ{M≥2k} ≤ Σ_{k=1}^{⌊(a_0+1)/2⌋} y_{2k}`. **Rigorous.** My check: `0` violations, tight, over
`5000` feasible peels per `n=2..5`, exact `Fraction`. → **CERTIFIED** as
`lemmas/positive-layer-localization.md`. It controls only the positive layers (`π_0` side); the
matching `Q` lower bound is exactly the open wall.

**Assessment.** Correctness of what's written: 10/10 (both the refutation and the lemma are valid).
As a route: the engine cannot work as set up (refuted) → RETHINK; the slug goes back to the outliner.
The Positive-Layer Localization Lemma is banked for reuse (it is the clean FLOOR-language form of the
banked round-6 even-rank deficit bound, tied to `a_0`).

---

## Summary

- **peel-scale-rank-induction:** CHANGES REQUESTED / partial. Certified `(★-id)`. GAP-P1′-a
  (cross-block dominance of `(★)`) and GAP-P1′-b (slice-max reduction of `b`) remain open.
- **allocation-vertex-corner:** RETHINK / unsolved-as-engine. `φ(b)` engine refuted (exact ties
  `b=2,3`). Positive-Layer Localization Lemma certified and banked.
- **Whole problem: partial.** Upper bound certified; the sole open wall is GAP L, now pinned to the
  single inequality `(★) Σ_{blue odd}≥Σ_{red even}` on the extremal slice (base-case dominance +
  reduction-to-base). No APPROVE this round.
- **Lemmas certified this round:** `lemmas/ladder-interleaving-identity.md`,
  `lemmas/positive-layer-localization.md`.
