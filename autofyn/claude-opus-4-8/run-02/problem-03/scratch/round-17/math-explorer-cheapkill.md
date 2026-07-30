## imo-2026-03 — CHEAP-KILL of the two R16-logged speculative directions

Scope: per dispatch, this report ONLY cheap-kills the two speculative directions flagged by the
R16 proof-reviewer, on the sole open wall — the cut-top-rung, oversized-red leaf `ΣR>θ`
(Case IIb-2, `(P̂_m)` induction step, `ladder-length-deficient-induction.md` §6) and its
`(Q̂)`-mirror Case IIa. No new far-apart slug is proposed here (per dispatch, that is only opened
if the primary route looks stuck; the primary comb-geometry route is still live per §6/§7 of the
approach file and is not this report's job).

### DIRECTION 1 — discrete ±1-jump run-length recast of `M` — **DEAD** (reproduces R8 meta)

**Precise reading tested.** Any statistic built only from the *combinatorial* run-length /
breakpoint-count structure of the ±1 step function `N_{ρ₁}(t)−N_W(t)` (equivalently the
comb-tooth count `⌈r/2⌉` of `O_{ρ₁}` vs. the breakpoint count `|W|` of `O_W`), i.e. any statistic
that is a function of `(r, |W|)` alone (ignoring the actual real-valued widths / positions), was
tested for separating power.

**Witness (exact `Fraction`, same `(r,|W|)=(2,3)` class, `m=2`, `θ=2`).**
- Config A (near-zero): `ρ₁={1987/1000, 13/1000}`, `F''={1}`, `R={1989/1000, 153/125}`
  → `Δ(R,F') = 13/1000` (razor-close to the wall).
- Config B (comfortably positive): `ρ₁={119/100, 81/100}`, `F''={1}`, `R={1241/1000, 447/500}`
  → `Δ(R,F') = 229/250 ≈ 0.916`.

Both configs have identical `r=2` (teeth count `⌈r/2⌉=1`) and identical `|W|=3` breakpoint bound
— i.e. **identical run-length/count profile** — yet `Δ` ranges over `[0.013, 0.916]` on this one
profile class. A broader sweep (`6000` random oversized-leaf configs, `m∈{2,3}`) confirms this is
systematic, not cherry-picked: grouping by `(r,|W|)` gives spreads of `Δ` up to `2.99` within a
single count-class (e.g. `(r,|W|)=(3,4)`: `Δ∈[0.014, 3.0]` over `765` configs). **Verdict: any
statistic depending only on run-length/breakpoint COUNTS carries zero separating power** — it
cannot distinguish the razor-tight configs (`Δ→0`) from the slack ones. This is exactly the R8
meta ("every static profile of the final multiset is equivalent to the target" / "no reshuffle of
the profile `M` can close GAP L") reproduced on the current leaf: the discrete run-length recast
throws away the magnitude information that the identity `(C)`/`(†)` genuinely needs, and any
non-vacuous bound built from it collapses to either the target itself (if it retains full
magnitude data — a mere relabeling of `I_S`) or a vacuous/false bound (if it retains only counts,
as shown above). **DEAD. Do not seed.**

### DIRECTION 2 — red-side MAXPEEL / red-peel (I3′) applied to `W` on the oversized-red leaf — **DEAD**, with one clarifying finding

**What was tested.** The certified `(I3′)` (`top-peel-general.md`) only requires "`Z`'s parts all
`< y=max R`" — NOT `y>θ`. So `(A3)` (`y=max R>θ`) is a special case of a strictly more general
available move: peel `y=max(R)` whenever `y` exceeds every part of `F'` (in particular whenever
`y>max(ρ₁)=p₁`, which can happen even when `y≤θ`, i.e. `θ≥y>p₁` — exactly the "apply the peel to
the red side of the oversized-red leaf" idea).

**Identity check.** Generalized peel `Δ(R,F') = (2^m−1−ΣR₀) − Δ(R₀,F')` (`R₀=R∖y`) holds exactly
whenever `y>max(F')`: `0` fails / `1460` random oversized-leaf trials, `m∈{2,3,4}`, confirmed also
by hand-derivation (it is literally `(A3)`'s own proof via `(I3′)`, which never used `y>θ`, only
`y>max(F')`).

**Why it still dies.** After peeling, `1375/1375` (100%) of the trials where this generalized peel
lands `ΣR₀≤θ` — i.e. exactly onto the ALREADY-CLOSED `(IIb-1)` leaf — the peel identity
`Δ(R,F')=(2^m−1−ΣR₀)−Δ(R₀,F')` needs an **UPPER** bound on `Δ(R₀,F')` to produce a **lower** bound
on `Δ(R,F')` (subtraction flips the direction). But `(IIb-1)` only proved a LOWER bound
(`Δ(R₀,F')≥½(θ−D̃(ρ₁))>0`); the only available UPPER bound on a cut-top-rung leaf is the weak
`(Q̂_m)`-branch noted in the approach file itself as "off by `2^m`" (§5, "the `ΣR>2^m` cut-top-rung
branch of `(Q̂_m)` is open — same wall"), and it is vacuous every single time it was tried
(`1375/1375`).

**Explicit witness** (`m=2`, `θ=2`): `ρ₁={3/2,1/2}`, `F''={1}`, `R={5/2,1/2}` (`ΣR=3>θ`, `a₀=1`).
`y=5/2>p₁=3/2`, generalized peel applies (`0`-fail identity check: `Δ(R,F')=1`, RHS recomputed `=1`
✓). `R₀={1/2}`, `ΣR₀=1/2≤θ`. The only available upper bound `Δ(R₀,F')≤2^{m+1}−1−ΣR₀=13/2` gives
`Δ(R,F') ≥ (2^m−1−ΣR₀) − 13/2 = 5/2 − 13/2 = −4`, vacuous (true value `Δ(R,F')=1`).

So the generalized red-peel is a *genuine, valid* generalization of `(A3)` (worth banking as a
minor observation: `(A3)` need not require `y>θ`, only `y>max(F')`), but it does **not** supply new
leverage on the oversized-red leaf — it re-routes to exactly the `(Q̂_m)`-mirror wall (Case IIa,
already flagged open in the approach file, §5 remark) rather than bypassing it. **DEAD as an
independent closer; do not seed as a slug.** The one-line observation ("A3 generalizes to
`y>max(F')`, not just `y>θ`") can be folded into the existing leader's bookkeeping if useful, but
it changes nothing about which leaf is open.

### Net verdict for the outliner

Both R16-logged speculative directions are cheap-killed with exact-`Fraction` witnesses. **Neither
opens a new route.** The sole live lever remains the per-tooth comb-geometry charge described in
`ladder-length-deficient-induction.md` §6 (bound `Σ_teeth λ(tooth∩E_W) + λ(E∩O_W) ≥ ΣR−2θ+1` via the
budget-limited breakpoint count of `O_W`, `≤2m−a₁` — genuinely using both the comb structure of
`O_{ρ₁}` AND the budget, not a scalar summary). Do not open filler slugs this round; if the primary
comb-geometry route (already assigned) also stalls, the next genuinely-far framing to consider
(not attempted here, out of this report's scope) would need to leave the `Δ(R,F')`
peel-and-recurse family entirely — e.g. a direct two-sided (both teeth-meet AND teeth-miss)
double-counting argument across `O_{ρ₁}` and `O_W` simultaneously, rather than any further
single-sided peel or profile recast.

### Knowledge-base / lemma pointers (unchanged, for the outliner's reference)
- `lemmas/top-peel-general.md` (MAXPEEL, I3′) — used above; confirmed its scope does NOT include
  `y≤max(F')` peels (no valid identity exists there without further structure) and, per this
  report, its `y>θ` hypothesis in `(A3)` can be weakened to `y>max(F')` but this buys nothing new.
- `lemmas/cut-top-rung-correction.md` (C),(A1),(A2),(A3) — imported, not re-derived.
- `lemmas/floor-half-reduction.md` — the FLOOR identity `D̃(F)=1−2∫⌊M/2⌋` is the rigorous ancestor
  of "Direction 1"; it already reduces GAP L to a single scalar `I_n≤0`, and R8–R11 already proved
  every profile/merged-order/genfn reshuffle of that `M` is either circular or vacuous. Today's
  witness reconfirms this on the current cut-top-rung leaf's local `M=N_{ρ₁}−N_W`.

### Dead ends (confirmed/reconfirmed this round, do not retry)
- Any statistic of `(r,|W|)` (teeth-count vs. breakpoint-count) alone as a certificate for
  `Δ(R,F')≥0` on the oversized leaf — spread up to `2.99` within one count-class (this report).
- Red-side peel of `R` down through the leaf via `(I3′)`/generalized-`(A3)` when it lands back on
  the closed `ΣR₀≤θ` leaf — needs an upper bound on `Δ(R₀,F')` that only the vacuous `(Q̂_m)`
  weak branch supplies (`1375/1375` vacuous, this report). This is the same wall as the file's
  own Case IIa / "`(Q̂_m)` `ΣR>2^m` cut-top-rung branch" — not a bypass.
