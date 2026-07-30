# Outline review — imo-2026-03 (Round 19)

All three nominated approaches are UPPER (LOWER correctly HELD: explorer confirmed SUFFIX-★ is the
12th dead lower lever, 33–42% failure growing with n). I ran the mandatory exact-`Fraction` gates
(`/tmp/gate19.py`, `/tmp/gate19b.py`) BEFORE ranking, per the dispatch. Both new mechanisms fail
decisively; only the low-risk consolidation advance survives.

## Certification check (target soundness) — PASS
- **R-UV is genuinely certified** (Corollary of Lemma RL, `leftover-realizability.md`): a general
  nonnegative differencing-tree value over any nonempty `T` is Xiang-realizable in exactly `m−1 = n`
  cuts (`|T|−1` MATCHes + `n+1−|T|` DELETEs), and `min R(A) ≤ u_nL ⟹ D ≤ u_nL`. So the pivot to
  targeting `min R(A)` directly is SOUND, and the "pivotal correctness check" (breakpoint-vertex
  step 2, tree realizability) is ALREADY discharged by RL — no new leap needed.
- Gate confirms `min R(A)/u_n ≤ 1` on every hard family (0, 0, 0.061, 0.031, 0.016 at the R18
  witness, 30-25-20-15-10, and A^{4,5,6}-deepened). Target is true with room to spare.

## breakpoint-vertex (ADVANCE) — CHANGES REQUESTED (build)
Verdict: sound but low-content. Steps 1–2 (`min R(A) ≤ μ_{n+1}` since caterpillars ⊆ trees; tree
value realizable in ≤n cuts) are correct and, per above, essentially already certified by RL/R-UV.
The advance is a legitimate consolidation — officially retire the caterpillar `μ_{n+1}` target and
adopt the certified `min R(A) ≤ u_nL` as the field's official residual — but it closes NO gap and
introduces no new mechanism. It is the only survivor and is worth one builder to (a) record the
re-targeting formally, and (b) record this round's two refutations (below) in the leader's file. It
must NOT attempt any anchored-walk/caterpillar-contraction closing lever (9th dead mechanism).

## tree-min-divide-conquer (NEW) — RETHINK (cut, not registered)
Gate FAILED. The central object — best over BALANCED disjoint splits `G₁⊔G₂` of the pieces (masses
within `2a₁`) of `min_{x∈T(G₁),y∈T(G₂)}|x−y|` — does NOT contract to `u_nL`:
```
   R18-witness (n=4): DCbest/u = 9.30      (true min R = 0)
   30-25-20-15-10   : DCbest/u = 0.0
   A^4-deepened     : DCbest/u = 2.697
   A^5-deepened     : DCbest/u = 2.846
   A^6-deepened     : DCbest/u = 2.922   (monotone GROWING, saturating ~3)
```
This is the covering-radius death signature (R12 two-cap saturated at 3–5·u_n). Root cause,
structurally identical to the R18 dead anchored walk: a split "of the pieces" is a FULL partition
that cannot DROP pieces, so it cannot reach a piece-EXCLUDING subset minimiser — on the R18 witness
the true `min R = 0` lives on `{13/40,13/40}` (drop 3 pieces), unreachable by any balanced full
partition, so DCbest saturates at 9.3·u_n. VALLEY-TIGHT kills any `C·u_n`, C>1; here C≈3–9. Dead.

## signed-tree-invariant (NEW) — RETHINK (cut, not registered)
Gate FAILED, and confirms the dispatch's exact suspicion. The "disjoint restart after band-landing"
is NOT a new object — `band_restart(A) ≡ descKK(A)` (the plain caterpillar/reflected walk) on every
family tested, and reproduces **exactly 9.30·u₄ on the R18 witness** = the R18-dead `minpost = 3/10`:
```
   R18-witness (n=4): band_restart/u = 9.300  ( = descKK, = R18 dead minpost)
   A^4/5/6-deepened : 2.697 / 2.846 / 2.922   (same growing saturation as D&C)
   excl-cancel n=4/5/6: 3.54 / 0.90 / 1.36    (generally >1)
```
The distinguishing claim ("a₁ consumed into `r`, disjoint restart, no re-inflation") is false: band-
landing is ANCHORED at a₁ (it sums survivors to cross a₁), so it forces a₁ into `r` and cannot see
the anchor-EXCLUDING tail minimiser `{13/40,13/40}` — the precise R18 root cause. It is the 9th dead
anchored-walk mechanism relabeled. Dead.

## Field assessment — the min R(A) target is now a SHARED WALL
Both new approaches were the two probes (counting / analytic) of the single `min R(A) ≤ u_nL`
target, and BOTH died at the gate on the same covering-radius/anchored signature. Per both approach
files' own watch-out (c) and the field-collapse rule: **the reachable-value object (`min R(A)` /
`μ_{n+1}` / any single walk or partition over it) is the shared wall.** Every "cheap" single-object
bound over it saturates at Θ(1)·u_n because `u_n ~ 2^{-n}` while any fixed-depth reflection resolves
only to Θ(2^{-depth}) — the explorer's exponential-rate mismatch. Next round the outliner MUST put
≥1 UPPER approach on the table that attacks the deep-interior upper bound from a framing that does
NOT route through a single object over the reachable-value set — a genuinely global existence
argument that exploits the full `2^{n+1}` search space at the right exponential rate (the standing
Steinitz/vector-balancing directive), or a bespoke perturbative argument confined to the `u_n/2`-wide
sliver (explorer opening 4), or a re-derivation off the reachable-value object entirely. LOWER stays
HELD (12 dead levers; only the untried, un-gated total-variation/transport formulation remains, and
it needs a cheap gate before any build).

## Ranking (this round)
breakpoint-vertex 1864 (live leader, certified core intact, stale cleared) > parity-measure-potential
1672 (partial, lower family stale) > reflected-walk-contraction 1580 (the anchored-walk object, this
round re-refuted at 9.3·u₄) > cross-scale-injection 1461 (SUFFIX-★, 12th dead lower lever). The two
cut approaches (tree-min-divide-conquer, signed-tree-invariant) are NOT registered — gate-refuted
before entry, so they do not pollute the pool.

build set: breakpoint-vertex
