# proof-builder — breakpoint-vertex (Round 19)

Status: **partial** (consolidation/re-target; no gap closed, none claimed).

## What I did (narrow, per dispatch)

1. **Official re-target of the open residual.** Retired the caterpillar target `μ_{n+1} ≤ u_nL` and
   adopted the certified true target `min 𝓡(A) ≤ u_nL`, citing **Corollary R-UV** of **Lemma RL**
   (`results/imo-2026-03/lemmas/leftover-realizability.md`, CERTIFIED round 7).
   - Certified part (cited, NOT re-proved): a general nonnegative **differencing-TREE** value
     `ρ=|Σ_{i∈T}ε_i a_i|` over any nonempty `T` is Xiang-realizable as the single leftover in exactly
     `m−1=n` cuts (`|T|−1` MATCHes along the tree's internal nodes + `m−|T|` DELETEs), so
     `min 𝓡(A) ≤ u_nL ⟹ D ≤ u_nL`. This is general-tree, not caterpillar-only (ESF-2 was the
     caterpillar special case) — exactly the realizability the two new approaches needed licensed, and
     it is already discharged by RL.
   - Asserted part (bookkeeping only): `min 𝓡(A) ≤ μ_{n+1}` always (caterpillars are one tree
     topology), so the new target is weakly easier AND, by R-UV, equally sufficient. No new mathematics.
   - Scope caveat surfaced honestly: R-UV is a *sufficient* condition (converse R-COV' uncertified,
     unused). That is all the upper bound needs.

2. **Recorded the two R19 refutations** in the approach file with structural reasons:
   - completeness identity `μ_{n+1}=min 𝓡(A)` is FALSE — witness `(17,16,11,8,4)`: `μ=1`, `min 𝓡=0`
     (recomputed exact-Fraction with correct FGR dist-recursion + full tree search).
   - tree-min-divide-conquer DEAD — balanced full partition cannot drop pieces, can't reach the
     anchor-excluding tail minimiser; `9.30·u₄` on R18 witness, growing `2.70→2.92` on `A^{(4,5,6)}`.
   - signed-tree-invariant DEAD — `band_restart ≡ descKK`, reproduces the R18-dead `minpost=3/10=9.30·u₄`;
     band-landing is anchored at `a₁`; 9th dead anchored-walk relabeled.

3. **Stated current best honestly.** Boundary layer `a₁≥L/2−u_n/2` CLOSED by WTC; deep interior
   `a₁<L/2−u_n/2` OPEN with residual `min 𝓡(A) ≤ u_nL`; true minimiser is an anchor-EXCLUDING tail
   subset so no single object over the reachable-value set reaches it (9 dead mechanisms). Gap handed
   forward: needs a global existence (Steinitz/vector-balancing) argument or a sliver-local
   perturbation — out of this slug's framing.

## Evidence (exact-Fraction, NOT proof) — `/tmp/conf19.py`

`min 𝓡(A)` via memoized subset+tree `treeVals`; `μ` via FGR dist-recursion `μ_i=min(μ_{i-1},dist(a_i,R_{i-1}))`
(avoids the min-positive landmine that drops exact-0 cancellations). All `fractions.Fraction`, no float.

```
 family (Σ=1)                     n | min R(A)/u_n | mu_FGR/u_n
 {1/3,13/40,13/40,1/120,1/120}    4 |   0.0000     |  0.0000
 {30,25,20,15,10}/100             4 |   0.0000     |  0.0000
 A^(4)={16,8,4,3,2}/33            4 |   0.9394     |  0.9394
 A^(5)                            5 |   0.9692     |  0.9692
 A^(6)                            6 |   0.9845     |  0.9845
 A^(4) sliver (a1-=u/4)           4 |   0.6894     |  0.6894
 A^(5) sliver                     5 |   0.7192     |  0.7192
 A^(6) sliver                     6 |   0.7345     |  0.7345
```
`min 𝓡(A)/u_n ≤ 1` everywhere; asymptotically tight (approaches, never reaches 1 — VALLEY-TIGHT
respected). On structured `A^{(n)}` the caterpillar and tree minima coincide; they differ only on the
tie-rich integer witnesses. Evidence, not proof of the general inequality.

## Spec concerns

- The re-targeting is sound and de-risks any future `min 𝓡(A)` approach, but it is genuinely low-content:
  it closes NO gap. Status remains partial.
- **Shared-wall confirmed:** both R19 probes of `min 𝓡(A)` died at the covering-radius/anchored
  signature. The reachable-value object (`μ_{n+1}` / `min 𝓡(A)` / any single walk or partition over it)
  is the shared wall. Next round MUST field ≥1 UPPER approach that does NOT route through a single
  object over the reachable-value set — a global existence argument at the right exponential rate
  (`u_n∼2^{-n}`), or a bespoke sliver perturbation (explorer opening 4). No new UPPER lever exists in
  this slug's framing.
- LOWER stays HELD (12 dead levers) — no action here.

Files: `results/imo-2026-03/approaches/breakpoint-vertex.md` (updated), `/tmp/conf19.py` (confirmation).
