# Approach: qlayer-charge-induction (close I_n≤0 for GENERAL F' directly; loaded IH = an inherited NUMERIC lower bound on F''s negative-layer sum Q, no majorization, no ladder reduction)

## Status
new (round 13) — the `b`-lift specialist, replacing the DEAD `coupled-cut-descent` (single-cut
co-varying descent RIGOROUSLY REFUTED at `n=5`, Prop REFUTE) and the DEAD `(WM)`-loaded-IH
inheritance (peel §11.5, numerically refuted for general `F'` this round). This route attacks the
whole reduced target `I_n≤0` for GENERAL `F'` at once — it does NOT go through the extremal ladder
base slice `(★)` and does NOT use weak majorization. Its object is the certified `(POS)/(Q)` layer
machinery, carried as a NUMERIC (not majorization) loaded IH inherited under one peel of `F'`.

## The whole claim this approach proves
GAP L (lower bound), closing the problem: `D̃(F) ≥ 1` for every dyadic-refinement final multiset `F`
under budget `Σa_j ≤ n`. With the certified upper bound this gives `c(n)=2^n/(2^{n+1}−1)`.

## Why this is FAR from the banned/dead routes
- NOT majorization / value-domination: carries a scalar numeric bound on a layer integral, not a
  prefix-sum relation (peel §11 `(WM)` refuted off the ladder this round — full and dyadic-threshold
  HLP both fail 477/12000, 1321/60000).
- NOT single-cut descent: no `b→b−1` move; induction on `n` via the certified peel, not on `b`
  (coupled-cut-descent refuted `n=5`).
- NOT a static scalar-summary of `F'`: the bound `Φ(F')` is DERIVED from `F'`'s recursive cut-tree
  origin (inherited peel-by-peel), not read off aggregate stats of the final multiset — this is
  exactly the "use `Σa_j≤n` non-locally via Z's recursive origin" the R8 meta demands. (The banned
  scalar-summary fills used only static aggregates of the final `Z`; see Watch-out.)
- NOT the GAP-IMR integrality route (dead) and NOT a top-down/bottom-up positional reserve (refuted).

## Technique (the spine)
Peel induction on `n` (`F = π_0 ⊎ F'`, `F'` a refinement of the `(n−1)`-ladder), reducing `D̃(F)≥1`
to the certified single inequality `I_n ≤ 0`, split as `I_n = P − Q` with
```
   P := Σ_{k≥1} λ{M ≥ 2k},      Q := Σ_{k≥1} λ{M ≤ −(2k−1)},      M = N_{π_0} − N_{F'} on (0,θ).
```
(`(FLOOR)`/`(LAYER)` certified.) Target `I_n≤0 ⟺ Q ≥ P`. The certified `(POS)` lemma already bounds
the positive side by `π_0` alone:
```
   (POS)   P ≤ Σ_{k=1}^{⌊(a_0+1)/2⌋} y_{2k}(π_0) =: S_π      (π_0's even-ranked parts only).
```
So it suffices to prove the **negative-layer lower bound** `Q(π_0,F') ≥ S_π` for EVERY partition
`π_0` of `2^n`. The negative layers `{M≤−(2k−1)} = {t: N_{F'}(t) ≥ N_{π_0}(t)+(2k−1)}` are where
`F'` out-counts `π_0` — a property that depends on `F'`'s count staircase `g=N_{F'}` (its recursive
dyadic origin), which is precisely what the peel-inherited IH will control.

## Skeleton
1. **Reduce.** By certified peel `(SD)/(PEEL)` + `(FLOOR)`: `D̃(F)≥1 ⟺ I_n = P − Q ≤ 0 ⟺ Q ≥ P`.
   By `(POS)`: `P ≤ S_π`. So the WHOLE lower bound reduces to
   ```
       (NEG)   Q(π_0,F') ≥ S_π    for every partition π_0 of 2^n into ≤ a_0+1 parts.
   ```
2. **Identify the loaded IH `Φ` (the design step).** Find an explicit numeric functional `Φ(F')` of
   the count staircase `g=N_{F'}` such that
   - **(a) worst-`π_0` sufficiency:** `Q(π_0,F') ≥ Φ(F')` and `Φ(F') ≥ max_{π_0} S_π`, so `(NEG)`
     holds for every `π_0`. [Candidate: `Φ(F')` = a weighted count of the "odd-count bands" of `g`,
     i.e. `∫_{(0,θ)} h(N_{F'}(t)) dt` for an explicit weight `h`, matching the even/odd threshold
     asymmetry `2k` vs `2k−1` that `(LAYER)` exposes as the source of the missing `½`.]
   - **(b) inheritance under one peel:** with `F' = π_1 ⊎ F''` (`π_1` a partition of `θ=2^{n−1}`,
     `F''` a refinement of the `(n−2)`-ladder), `Φ(F') ≥ (Φ(F'') contribution) + (π_1 contribution)`,
     so the level-`(n−1)` IH `Φ(F'') ≥ (its bound)` propagates to `Φ(F')`.
3. **Inheritance step.** Prove `(b)`: relate `N_{F'} = N_{π_1} + N_{F''}` on `(0,θ)` (level-set
   additivity, certified `(U2)`), and show the negative-layer functional `Q`/`Φ` splits sub-additively
   across the peel, with `π_1` supplying at least the extra even-part mass `S_π` gains at level `n`.
   The single unit of budget slack `n−(n−1)` (Invariant I: `M(0⁺)≤1`) is the exact non-local resource
   that closes the `½`.
4. **Base case `n=1`.** `F'={1}`, `π_0` a partition of `2`; `Q ≥ S_π` directly (`D̃(π_0⊎{1})≡1`).
5. **Conclude.** `(NEG)` for all feasible `(π_0,F')` ⇒ `I_n≤0` ⇒ `D̃(F)≥1` for all `n`.

## Key lemmas (claim + mechanism)
- **`(NEG)` reduction** — `D̃≥1 ⟺ Q ≥ P` (from certified `(FLOOR)`), and `P ≤ S_π` (certified
  `(POS)`), so the lower bound `⟺` a pure lower bound on the negative-layer sum `Q ≥ S_π`. Clean,
  imports only certified lemmas.
- **Loaded numeric IH `Φ(F')`** — an integral of an explicit weight of `g=N_{F'}` chosen so the
  positive `2k` / negative `2k−1` threshold asymmetry is absorbed. Its VALUE is inherited peel-by-peel
  from `F'`'s cut-tree, so it is a recursive (non-local) quantity, not a static aggregate. THIS is the
  open design object.
- **Peel sub-additivity of `Q`** — `N_{F'}=N_{π_1}+N_{F''}` (certified `(U2)`) ⇒ the negative-layer
  set of `F'` contains contributions from both `π_1` and `F''`; the IH controls the `F''` part, `π_1`
  (a partition of `θ`) supplies the increment matching `S_π`'s growth from level `n−1` to `n`.

## Open gaps
- **Identify `Φ` and prove `(a)`+`(b)` (steps 2–3)** — the entire crux. Concretely: (i) an explicit
  weight `h` with `Q(π_0,F') ≥ ∫ h(N_{F'})` for every `π_0` and `∫h(N_{F'}) ≥ S_π`; (ii) its
  inheritance under the peel `F'=π_1⊎F''`. This is honestly hard, but it is a genuinely different
  object from the ladder routes and stays inside the already-certified `(POS)`/`(LAYER)` machinery.
- **`Φ` must NOT be a static scalar-summary of the final multiset** (banned, refuted R3–R4) — it is
  admissible ONLY as a recursively-inherited quantity; the inheritance proof `(b)` is what certifies
  its non-locality. If `(b)` cannot be proven and `Φ` collapses to a static aggregate, this route
  RETHINKS.

## Cases to cover
- `n=1` base. Peel step for general `F'` (no `b`-slicing — `b` is subsumed by the `n`-induction).
- Case A (`a_0=0`) already closed unconditionally (certified §4) — the induction covers `a_0≥1`.
- Tie family (`I_n=0`): `(NEG)` holds with equality `Q=S_π` there — a correctness gate.

## Watch out for
- **The scalar-summary ban.** `Q ≥ (aggregate stat of F')` as a STANDALONE static bound is refuted
  (3 counterexamples R3–R4). Escape route: `Φ` must be justified by the peel-inheritance `(b)`, i.e.
  as a recursive functional of `F'`'s cut-tree, never as a summary of the final multiset. Flag this
  in the build; the inheritance step is what makes the route legitimate, not optional decoration.
- **`M(0⁺)≤1` alone is insufficient** (§9.3 decoy `D̃=0.146`): the IH must read the SHAPE of
  `g=N_{F'}`, not just its part-count. `Φ` must depend on the full staircase.
- **Do NOT reintroduce a top-down/bottom-up positional reserve** (refuted R7/R9): `Q` is a total
  negative-layer INTEGRAL proven by induction, not a pointwise running margin.
- Test any concrete candidate `Φ` first on the n=2 witness `π_0={4959/2500,5041/2500}`,
  `F'={3323/2500,1677/2500,1}` (which breaks `(WM)` but satisfies `(★)`), a 2-line `Fraction` filter.

## Imported (certified)
`lemmas/floor-half-reduction.md` (`(FLOOR)`/`(LAYER)`, general in `F'`),
`lemmas/positive-layer-localization.md` (`(POS)`: `P ≤ S_π`),
`lemmas/peel-difference-bound.md` (`(SD)/(PEEL)`, Invariant I, Case A), Lemma G, cut-flip,
upper-bound. Do not re-derive.
