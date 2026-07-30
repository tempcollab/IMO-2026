## imo-2026-03 — lens: cut-top-rung leaf budget-trade

### Setup recap (from cut-top-rung-correction.md / ladder-length-deficient-induction.md)
Case II of `(P̂_m)`, sub-case IIb (top rung `ρ₁` cut, `a₁≥1`, all reds `≤θ`): exact identity (C)
`Δ(R,F') = Δ(R,F'') + ½θ + ½D̃(ρ₁) − I_S`, `I_S := λ(O_{ρ₁}∩O_W)`, `W=R⊎F''`. Need `Δ(R,F')≥0`,
i.e. `I_S ≤ Δ(R,F'') + ½θ + ½D̃(ρ₁)`. Budget: `a₀+a₁+Σ_{i≥2}a_i ≤ m`, so `a₀+b''≤m−a₁≤m−1` where
`b''=Σ_{i≥2}a_i` (cuts remaining in `F''`).

### Key numeric finding (the actual new resource, more precise than the approach file states)
The approach file (§4 Case IIb, §6) says "only the UPPER bound `(Q̂_{m−1})` on `Δ(R,F'')` is
inherited... a LOWER bound is needed" and treats this as fully open. **This undersells what is
already available: `(L̂B_{m−1})` — the full deficient lower bound, not just `(P̂_{m−1})` — applies
directly and exactly to `(R,F'')` on the leaf, with NO slack needed in the hypotheses:**
- `F''` is a budgeted refinement of `L_{m−1}`, cuts `b''=Σ_{i≥2}a_i`.
- Need `a₀+b''≤m−1`: TRUE because `a₀+a₁+b''≤m` and `a₁≥1`.
- Need every red `≤2^{m−1}=θ`: TRUE (case IIb hypothesis).
- Need `ΣR≤2^{(m−1)+1}=2^m`: TRUE (`(P̂_m)`'s own hypothesis `ΣR≤2^m`).
So `(L̂B_{m−1})` (which itself follows from `(P̂_{m−1})`, available by the outer induction on `m`)
gives, unconditionally on this leaf,
```
   Δ(R,F'') ≥ min(0, θ − ΣR).
```
**Verified 0 fails / ~70,000 exact-`Fraction` trials, m=2..5** (script `/tmp/probe4.py`,
`fail_LB=0` at every `m`) — the spent cut `a₁≥1` is EXACTLY what buys admissibility of
`(L̂B_{m−1})` here; this is a genuine, previously-unexploited consequence of "a₁≥1 spends budget."
This should be reported to the outliner as a **correction**, not just an opening: the "only Q̂ is
available" framing in the approach file is not accurate — L̂B_{m−1} is cleanly inheritable.

### But chaining it with the trivial `I_S≤D̃(ρ₁)` bound is NOT enough
Plugging the `(L̂B_{m−1})` estimate into (C) gives the "route bound"
`I_S ≤ min(0,θ−ΣR) + ½θ + ½D̃(ρ₁)`, tested against the trivial ceiling `I_S≤D̃(ρ₁)`. This FAILS
3–6% of trials (script `/tmp/probe4.py`: `fail_route` = 307/18335 (m=2) up to 1138/17731 (m=5)),
even though the TRUE `Δ(R,F')` is ALWAYS ≥0 on the same trials (`fail_final=0` throughout, matching
the approach's own numerics). So the obstruction is real: **two independently-taken bounds (a
floor on `Δ(R,F'')`, a ceiling on `I_S`) are provably too lossy; a JOINT/coupled bound is needed.**

Inspecting witnesses (script `/tmp/probe5.py`) where the route fails but truth holds: in every
witness, `ΣR>θ` (oversized reds) and the TRUE `Δ(R,F'')` sits far ABOVE the `(L̂B_{m−1})` floor
`min(0,θ−ΣR)` (e.g. true `Δ_pp=−0.68` vs floor `−2.56`; true `Δ_pp=−1.0` vs floor `−2.74`). So
**the leaf's hard sub-case is specifically `ΣR>θ`** (reds already oversized relative to the
`m−1` scale) — `(L̂B_{m−1})`'s bound is only tight near `ΣR≈θ`, and degrades linearly as
`ΣR−θ` grows, while the true `Δ(R,F'')` does not degrade nearly as fast. This points at a genuinely
NEW mechanism: bound `Δ(R,F'')` in the oversized regime using a REFINED estimate that also accounts
for `I_S` jointly (not the generic `(L̂B_{m−1})` floor) — e.g. peel one further big red or big blue
part before invoking the floor, or express `I_S` directly via `D̃(W)` (`I_S≤D̃(W)`, `D̃(W)=2Δ_pp+ΣR
−ΣF''`) and combine BOTH ceilings `I_S≤min(D̃(ρ₁),D̃(W))` — this is exact but circular (self-refers
to `Δ_pp`, which is what we're bounding); not yet tested as a genuine new closer.

### `ΣR≤θ` sub-case looks closeable now
When `ΣR≤θ`, `(L̂B_{m−1})` gives `Δ(R,F'')≥0` directly, so the route bound is
`I_S≤½θ+½D̃(ρ₁)`, which the trivial ceiling `I_S≤D̃(ρ₁)≤θ` ALREADY satisfies (since `D̃(ρ₁)≤θ`
⟹ `D̃(ρ₁)≤½θ+½D̃(ρ₁)`). **This half of case IIb (`ΣR≤θ`) is essentially closed already** by the
combination `(L̂B_{m−1})` + the trivial ceiling — worth having the outliner formalize this as a
sub-lemma (should reduce to zero failures once written precisely; confirm no edge case at
`ΣR=θ` exactly). The genuinely open residual is narrowed to **`ΣR>θ` (oversized reds)
specifically**, not the whole of case IIb.

### D̃(ρ₁) is NOT controlled by a₁ alone — cheap-kill against one natural conjecture
Tempting conjecture: "more cuts on the top rung (`a₁` large) forces `D̃(ρ₁)` (hence `I_S`) to
shrink." **FALSE as stated**: for any `r=a₁+1`, taking one part `θ−(r−1)ε` and `r−1` tiny parts
`ε` gives `D̃(ρ₁)→θ` as `ε→0`, regardless of `r` (verified exactly, `r=2..6`, `θ=8`:
`D̃(ρ₁)∈{7.998,…}` in all cases). So `a₁` gives **no direct leverage on `D̃(ρ₁)`'s ceiling** — its
only proven leverage is on the REMAINING budget for `(R,F'')` via `(L̂B_{m−1})`/`(Q̂_{m−1})`
admissibility (confirmed above), not on `ρ₁`'s own shape. Do not let a builder assume a₁-monotone
shrinkage of `D̃(ρ₁)` or `I_S` directly.

### The comb/interval structure of O_ρ₁ (unexplored opening, not tested numerically this round)
`ρ₁` sorted descending `p₁>…>p_r`: `O_{ρ₁}` is a union of exactly `⌊r/2⌋` intervals
`(p₂,p₁),(p₄,p₃),…` plus, if `r` odd, one extra interval `(0,p_r)`. So `a₁` controls the NUMBER
of "teeth" in `O_{ρ₁}` (`≈a₁/2`), even though it does not control their total measure. `I_S` is a
sum of per-tooth overlaps with `O_W`. This is a genuinely different, finer resource than the scalar
`D̃(ρ₁)` ceiling: an interval-by-interval (inclusion–exclusion / pigeonhole across `⌈r/2⌉` teeth)
charge against `O_W`'s own comb structure (which is itself constrained by `F''`'s budget
`b''≤m−1−a₀`) might succeed where the scalar route fails, exactly in the `ΣR>θ` residual. Not
numerically probed this round (time budget) — flag as the most promising unexplored mechanism.

### Distinct openings (summary, ranked by how close they already are)
1. **(closest) `ΣR≤θ` half of case IIb**: `(L̂B_{m−1})` (inherited, admissibility CONFIRMED by the
   spent cut `a₁≥1`) + trivial `I_S≤D̃(ρ₁)≤θ` already closes it. Formalize as a clean sub-lemma.
2. **`ΣR>θ` residual (the genuinely hard leaf)**: needs a bound on `Δ(R,F'')` (or jointly on
   `I_S`) that is sharper than the generic `(L̂B_{m−1})` floor in the oversized regime — the floor
   degrades in `ΣR−θ` faster than the truth does. Candidate mechanisms: (a) peel one more
   big/near-θ red from `R` before applying `(L̂B_{m−1})` (an `(A3)`-style further reduction inside
   `F''`'s own recursion, since `ΣR` up to `2θ` with parts `≤θ` means at most one red can itself be
   "large" relative to `θ/2`); (b) the comb/interval-teeth structure above, charging teeth of
   `O_{ρ₁}` against teeth of `O_W` directly rather than through a scalar `Δ_pp` intermediary.
3. **Comb/teeth invariant on `O_{ρ₁}`**: a₁ controls tooth COUNT not tooth MEASURE — a genuinely
   different lever than every prior scalar attempt (R14 NEG-lemma / R15 aggregate forms), worth a
   dedicated slug if (2) doesn't close cleanly.

### Candidate technique(s)
Continue the (P̂_m)/(Q̂_m)/(L̂B_m) mutual induction engine (already load-bearing, certified
machinery). The missing step is specifically a refined bound in the `ΣR>θ` regime of case IIb —
NOT a new global framework. Comb-structure interval counting (pigeonhole across `⌈r/2⌉` intervals)
is the concrete unexplored technique.

### Cheap-kill candidates
- `D̃(ρ₁)` is NOT a₁-monotone (confirmed above) — reject any sub-lemma assuming it is.
- `(L̂B_{m−1})` alone (without refinement) fails to close `ΣR>θ` — reject any builder claiming the
  generic floor suffices without further work; it must be SHARPENED specifically for `ΣR>θ`.
- The `ΣR≤θ` half is cheap to dispatch (2-line argument above) — don't spend a full slug on it,
  fold it into whichever slug attacks case IIb as a settled sub-case, concentrate builder effort on
  `ΣR>θ`.

### Knowledge-base entries to use
No new generic KB entry beyond what's already imported (this is deep in problem-specific
machinery); the relevant certified lemmas are all in `results/imo-2026-03/lemmas/`:
`cut-top-rung-correction.md` ((C), (A1)-(A3)), `base-slice-star.md` (the D̃-Lipschitz collapse
`(I4)` underlying `(L̂B_m)`), `top-peel-general.md` (MAXPEEL, (I3′)).

### Analogous past problems (cruxes)
Did not query the crux corpus this round (lens is a narrow problem-specific numeric probe of an
already-isolated leaf, not a fresh framing search) — the terrain here is fully internal to the
(P̂/Q̂/L̂B) engine built in R13-R15; no external analogy is likely to add leverage at this depth.
If the outliner wants a fresh far-apart slug (per the standing shared-gap rule), the comb/teeth
opening above (§ "comb structure") is the recommended target, not a corpus lookup.

### Prior progress
Current best = everything in `ladder-length-deficient-induction.md` through §5 (all uncut-top-rung
cases closed) plus §6's honest gap statement. This round's addition: (a) a CORRECTION — `(L̂B_{m−1})`
IS cleanly inheritable on the leaf (not just `(Q̂_{m−1})`, contra the approach file's §6 wording);
(b) the `ΣR≤θ` half of case IIb is essentially already closed by this + the trivial `I_S` ceiling;
(c) the residual is narrowed specifically to `ΣR>θ`; (d) `D̃(ρ₁)` is confirmed NOT a₁-monotone
(cheap-kill); (e) the comb/teeth structure of `O_{ρ₁}` flagged as the concrete unexplored lever for
the `ΣR>θ` residual.

### Dead ends (do not retry)
Confirmed avoided in this scouting: did not re-derive/re-attempt single-cut b→b−1 descent, WM-IH
inheritance, (NEG) Q≥S_π, scalar b-cutoff, π₀-fixed comparison, ABSORB engine, split-rung (I1′),
NEG-lemma value forms, independent-subgame decomposition, bottom-band/near-0 parity, GAP-IMR — none
of these were used; this round's probes stayed entirely within the certified (C)/(L̂B_{m−1}) engine
plus a fresh interval-count observation on `O_{ρ₁}`.

### Small-case / intuition notes (all CONJECTURE / numeric evidence, m≤5, exact Fraction, not proofs)
- `(L̂B_{m−1})` inheritance on the leaf: 0 fails / ~70,000 trials, m=2..5 — strong evidence it is a
  correct, genuinely usable (not just true-but-vacuous) fact.
- Naive route (L̂B_{m−1} + trivial I_S ceiling) fails 1.7–6.4% of trials, concentrated (100% of
  sampled failing witnesses) at `ΣR>θ` — strong evidence the hard case is specifically oversized
  reds, not the whole leaf.
- `D̃(ρ₁)` can be pushed arbitrarily close to `θ` for any `a₁≥1` via one dominant part + tiny
  fragments — exact witnesses given, not just numeric noise (this is a proof-level fact, trivial to
  verify: alternating sum of `{θ−(r−1)ε, ε,…,ε}` descending is `θ−(r−1)ε+(r−2)ε·(±)…→θ`).
