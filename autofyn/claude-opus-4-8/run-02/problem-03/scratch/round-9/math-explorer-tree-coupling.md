## imo-2026-03 — lens: JOINT COUPLING between Y's and Z's cut-trees (GAP L)

Start 20:41 UTC. Target unchanged: `(△⋆)` `λ_(0,θ){M odd} ≥ ∫_(0,θ)M = 1−β`, `M=N_Y−N_Z`,
`θ=2^{n−1}`, `β=(y₁−θ)⁺`; equivalently `D̃≥1`, equivalently the unified §9 form `E(F)≤2^n−1`.
I did NOT attempt a proof; I mapped couplings and killed several with fresh numerics.

### The two objects, made precise (disambiguation the outliner needs)
Two different Y/Z splits float around; the operative one (the one `(△⋆)`/β use) is the **Case-B
split**, NOT the "Liu-ladder vs Xiang" split:
- **Y = fragments of the single top piece `2^n=2θ`** — an ARBITRARY partition into `a_0+1` parts,
  sum `2θ`. Y has **no internal dyadic tree**: it is a flat depth-1 star. Only `|Y|=a_0+1` and
  `sum=2θ` are structural; at most one part (`y₁`) exceeds `θ`.
- **Z = a ≤(n−1)-cut response to the `(n−1)`-dyadic `{1,…,2^{n−1}}`** — this is the one with the
  recursive cut-tree (Structure Lemma §5: `Z=⊎_{j≥0}Y'^{(j)}`, `Y'^{(j)}`=fragments of `2^{n−1−j}`,
  `Σa'_j≤n−1`). All parts `≤θ`, sum `2θ−1`, `|Z|=n+b` exactly (`n` base pieces + `b` cuts).
So the "two-tree coupling" is really **flat Y-star coupled to recursive Z-tree**, plus the exact
budget link `a_0+b≤n`. The genuinely symmetric two-tree picture only appears in the **unified §9
form**: `F=⊎_{j=0}^n π_j`, a simultaneous refinement of the FULL ladder `{1,…,2^n}` with `Σa_j≤n`
(here Liu's fixed dyadic comb vs Xiang's cut-vector `(a_0,…,a_n)`). That form is a distinct
top-level target and a cleaner arena for a joint induction — see Opening 1.

### Distinct openings (each a different attack, not a lens on one)
1. **Peel-the-top-scale JOINT INDUCTION on the unified form `E(F)≤2^n−1`** (avoids the Case-A/B
   split entirely). Write `F=π_0⊎F'`, `F'=⊎_{j≥1}π_j` = an `(n−1)`-refinement of `{1,…,2^{n−1}}`
   with budget `n−a_0≤n−1`; IH `E(F')≤2^{n−1}−1`. The coupling = how inserting `π_0`'s `a_0+1`
   fragments (total `2^n`) into the sorted `F'` shifts even/odd ranks. This is a two-tree
   (`π_0` vs `F'`) interleaving with a clean `+2^{n−1}` mass-injection budget. Different top-level
   target than `(△⋆)`; the induction lives on the FULL ladder, treating both players' trees
   symmetrically. NOT yet tried as an insertion/rank-shift induction (prior inductions were on
   `D(Z)` alone, i.e. down Z's tree only).
2. **Two-level RECURSIVE global charge down Z's tree.** Descend at `θ/2`: `Z=Y'^{(0)}⊎Z''`,
   `Z''`=response to `{1,…,θ/2}` in `(0,θ/2]`. Charge each high-`M≥2` (T-run) deficit against the
   ENTIRE lower sub-tree's surplus at once (global, telescoping), NOT one matched anchor (§10 killed
   per-anchor). Supplies the constant `1` per level via the dyadic `+1` dominance (largest dyadic
   piece exceeds the sum of all smaller ones by exactly `1` — aimo-0117/aimo-0019).
3. **Count-parity dyadic-band coupling** (bottom-inclusive, the band §14 says is load-bearing).
   Decompose `(0,θ)` into dyadic bands and read `N_Y` vs `N_Z` band-by-band, anchored by the exact
   two-tree budget identity `M(0⁺)=|Y|−|Z|=(a_0+1)−(n+b)≤1` (Invariant I) and `|Z|≥n`.
4. **Shadow/position-map coupling (aimo-0663 style).** Couple Xiang's actual cut-tree to a canonical
   reference tree (e.g. the pure-dyadic response, or the zigzag-extremal `D̃=1` family) by a
   position map, transferring the known `D̃=1` reference bound with a one-directional legality check.
   Speculative but genuinely different from every measure/sequential framing already pruned.

### 2–4 concrete joint invariants (state / what closes ½ / failure mode)
- **(I) Two-tree budget identity `M(0⁺)=|Y|−|Z|=(a_0+1)−(n+b)≤1`, `=1` iff `b=0,a_0=n`.** PROVABLE
  (cuts never merge ⇒ `|Z|=n+b` exactly; `a_0+b≤n`). GENUINELY joint & bottom-inclusive — reads both
  trees' cut-counts at height `0⁺`. Verified: `0/200000` configs have `M(0⁺)>1`. What it buys: the
  near-`0` band starts non-deficient (the §14 surplus band sits here). Does NOT close alone; it is
  the *seed/anchor* for Openings 2–3. **Use it — it is the one clean, proven, non-local budget fact
  that couples the two trees.**
- **(II) Threshold-survival dominations — DEAD in BOTH senses.** (a) count-survival
  `#{Z odd-pos>τ}≥#{Y even-pos>τ}` refuted §10 (21%). (b) I additionally tested the **mass**
  version `Σ_{Y even>τ}y ≤ Σ_{Z odd>τ}z` — **also fails, 28039/200000** (witness `n=6`,
  `Y_even=(12.92,0.87)`, `Z_odd=(10.96,5.04,1)`: single big `12.92` exceeds all `Z_odd`). Any
  "domination at every threshold τ," count or mass, in either direction, is DEAD. Do not retry.
- **(III) Monotone cumulative reserves — DEAD in BOTH scan directions.** Top-down refuted §14. I
  tested the **bottom-up** cumulative reserve `R(τ)=∫_0^τ(1[M odd]−M)≥0 ∀τ` (the "bottom-inclusive"
  hope) — **fails 33643/200000, worst `−22.4`**. Root cause, now confirmed from four angles:
  **deficits sit HIGH (Y stacks big parts near θ), surplus sits LOW (Z's small dyadic pieces reach
  near 0)**, so no monotone scan pairs them. The compensation is irreducibly NON-MONOTONE / global:
  a high deficit must draw surplus from BELOW it. This is the precise reason every single-tree
  profile and every one-directional coupling collapses.
- **(IV) Surviving shape (not refuted): a global telescoping charge across ALL scales at once** —
  the only coupling consistent with "deficit high, surplus low, both real." Concretely a
  strengthened JOINT IH read on the coupled tree (Opening 1 or 2), NOT a per-threshold or
  per-anchor statement. This is where the outliner should aim.

### Which look promising vs which collapse to a single-tree profile (dead)
- Promising & genuinely joint: **Opening 1 (rank-shift insertion induction on the unified ladder)**
  and **Invariant I (budget identity)**. Both read BOTH trees and neither is a static profile of
  `M`, so neither is caught by the R8 equivalence meta (which covered merged-order-measure,
  sequential-cut, and genfn framings of the FINAL multiset — see below).
- Collapses to single-tree (avoid): any survival/majorization domination (II), any monotone reserve
  (III), any per-anchor/per-run match (§10), any scalar/count summary of Z (§2), top-down reserve
  (§14). Also: a merged-order block/window tiling is CIRCULAR (merged-order-layer.md, §15).
- **Important scope note for the outliner:** `reserve-target-equivalence.md` proves *sequential-cut*
  reserves (functions of `(config,budget)` over Xiang's ordered cuts) are equivalent to the target.
  It does NOT cover a **static two-tree structural invariant** (a majorization/insertion-rank
  quantity read on the coupled `π_0`-vs-`F'` interleaving). Openings 1–2 are therefore NOT ruled out
  by that obstruction — worth stating explicitly so the outliner doesn't over-apply the pruning.

### Cheap-kill candidates (structural, before heavy work)
- Prove & deploy Invariant I (`M(0⁺)≤1`) — pure counting, one line.
- Dyadic `+1` dominance: `2^{n−1} = 1+2+…+2^{n−2}+1`, so each ladder piece exceeds the sum of all
  smaller ones by exactly `1` (aimo-0117/aimo-0019 crux). This is the arithmetic origin of the
  constant `1`; any successful argument must spend it once per... it is the natural `+1` supply.
- `|Z|≥n` and `|Y|≤n+1` (part-count caps from budget).

### Knowledge-base entries to use
- **Invariants & monovariants** (knowledge_base.md line 117, 191) — but note monotone reserves are
  refuted (III); the live use is a *global* charge, not a per-step monovariant.
- **Induction loading / strengthening the hypothesis** (line 227–228) — Opening 1/IV need a
  STRENGTHENED joint IH (plain `E(F')≤2^{n−1}−1` may not push through the insertion; load it).
- **Strong induction / no minimal counterexample** (line 185).
- **Dyadic-bucket / size-bound meta-strategy** (line 245) — Opening 3's band decomposition.

### Analogous past problems (cruxes)
- **aimo-0718** (combinatorics, invariants-and-monovariants): "bound a growing multiset by a
  fixed REFERENCE multiset of the same total that MAJORISES it for all time, sandwiching top/bottom
  coordinates." Directly analogous to Opening 4 / a two-tree majorization; adapt as "find a reference
  refinement (the zigzag-extremal or pure-dyadic response) that majorises F's even-rank profile."
- **aimo-0489** (combinatorics, induction-and-construction): "doubling recurrence by pairing each of
  the two forced boundary values of the last element with a value-preserving relabeling of the
  remaining prefix that maps back to a smaller instance." The `2θ=2·θ` doubling between scale 0 and
  scale 1 is exactly this shape — closest template for Opening 1's peel-and-halve induction.
- **aimo-0019** (combinatorics, invariants/games): "bound dyadic-length distinct pieces by twice the
  largest via geometric sum" + "amortized linear potential charging each frontier advance against the
  pieces it absorbs." The dyadic `+1` dominance and the global (not per-step) amortized charge of
  Opening 2. Read both cruxes.
- **aimo-0663** (combinatorics, games-and-strategy): "run a SHADOW game coupled to the real one by a
  position map; verify a ONE-directional legality implication per player, not a full automorphism."
  The template for Opening 4 (couple Xiang's tree to a reference tree).
- Secondary: **aimo-0287** (majorization/suffix-count order + prefix-count threshold constraints) and
  **aimo-0250** (interleave rising+falling into a zigzag) — the latter is literally the `D̃=1`
  extremal `T,B,T,B,…` family; useful as the equality/reference object.

### Prior progress (furthest correct)
`D̃≥1` proven on: `maxc≤1` region (Lemma T, certified), Case A (C3), `{y₁≥2^{n−1}+1}`, `{|h|≤1}`.
Exact reductions certified: `(△)`, `(△⋆)`, `(♠′)`, `(⊞)`, `(△△)`, Structure Lemma, Lemma H. Upper
bound fully done (do not touch). Residual is the single global inequality `(△⋆)`/`(♠≥0)`/`E(F)≤2^n−1`,
tie-attained at `n=4 Y=(8,3,3,2) Z=(8,2,2,2,1)` (true infimum `1`, non-strict). `0` violations over
`2·10⁵`+.

### Dead ends (do NOT retry — with reason)
- ALL merged-order / measure-profile / sequential-cut / genfn framings of the final multiset:
  proven equivalent to the target (R8, three certified lemmas). Off by exactly `½`.
- Per-anchor / per-run width-dominating injection (§10, 21% fail). Scalar/count summary of Z (§2,
  three counterexamples). Top-down reserve of Z (§14, 7306/4e5).
- **NEW this round (my probes):** mass-survival domination `Σ_{Y even>τ}≤Σ_{Z odd>τ}` (28039/2e5)
  and bottom-up cumulative reserve `∫_0^τ(1[M odd]−M)≥0` (33643/2e5). Together with §10/§14 these
  close the door on EVERY threshold-wise or monotone-scan coupling in either direction. The residual
  is irreducibly global/non-monotone (deficits high, surplus low).

### Small-case / intuition notes (labeled CONJECTURE)
- CONJECTURE (strong, from data): tight `D̃=1` configs have `M(0⁺)=|Y|−|Z|∈{0,1}` (2028/2060 tight
  samples), i.e. the zigzag-extremal family lives at the budget boundary `b=0` or strict alternation.
- CONJECTURE: the constant `1` is the dyadic `+1` dominance (`2^{n−1}=Σ_{<}2^k+1`) surviving one
  parity level; a correct proof spends it exactly once, via a JOINT strengthened IH on the coupled
  tree (Opening 1/2), not a static profile. This is consistent with all four refuted single-direction
  couplings failing for the same "high deficit / low surplus" reason.

Report written; probes at /tmp/probe_coupling.py, /tmp/probe_botup.py, /tmp/probe_maj.py.
