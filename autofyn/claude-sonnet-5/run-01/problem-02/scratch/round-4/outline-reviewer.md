# Outline review — round 4 — imo-2026-02

## Verification performed

I independently re-derived (fresh sympy, not trusting the outline's prose) the two revised approaches'
new closing step for the shared `Z>0` / `D1>0` gap. Key checks:

1. Rebuilt `K = B + T_K·R(-α)(A-B)`, `L = C + T_L·R(α)(A-C)` (synthetic file's convention) and
   `K=(tK(p·ca+q·sa), tK(q·ca-p·sa))` (groebner file's convention) from scratch, recomputed `e1`, and
   confirmed **`e1 = TK · A1(TL,...)`** with zero constant term in `TK` (decoupling holds) in both
   conventions — matches the certified round-2 lemma.
2. Confirmed **`K_y = T_K · X`** exactly, where `X = qc - ps` (synthetic) / `X = q·ca - p·sa` (groebner)
   — a clean symbolic identity (`sp.simplify(K_y - TK*X) == 0`), so the new step's central substitution
   is correct in both files.
3. Confirmed the leading-`T_L²`-coefficient identity: after dividing by the positive constant
   `|AC|² = (a-p)²+q²`, the leading coefficient of `A1` (synthetic) / `g1` (groebner) equals
   `Z/2 = (aX + sinα·(p²+q²))/2` exactly (verified both via full trig substitution and rational
   numeric substitution — exact zero difference). So **the formula `Z = aX + sinα·|AB|²` that the
   whole closing argument rests on is genuinely correct**, not just plausible.
4. **Bug found (coordinate-groebner-elimination only, cosmetic, not fatal):** the file's §3 explicit
   formula for `g1` (all three of its `tL^0, tL^1, tL^2` coefficients, including the one it calls
   `D1`) is uniformly **4× too large** compared to the actual `g1` obtained from the file's own `e1`
   definition (checked numerically at a random point: ratio = exactly 0.25 on all three coefficients,
   so it's a consistent scalar bookkeeping error, not a sign or structural error). Since the scale
   factor is a positive constant, this does **not** change the sign of `D1` nor the zero-locus of `g1`,
   so the closing argument's conclusion (`D1>0` ⟹ `myexpr=0`) is still valid — but the explicit
   polynomial displayed in the file is wrong as written and must be recomputed by the builder before
   the proof is finalized (a rigor rule: don't ship a displayed identity that doesn't match what a
   fresh derivation gives, even if the final conclusion survives).
5. **Real gap in both files' justification of `sin α > 0`** (not just a wording nitpick). Both outlines
   justify `α ∈ (0,π)` by "`K ∉ line AB` since `K` is interior to `△BMC`, not on ray `BA`" — but that
   parenthetical only rules out `α=0` (K on ray BA), not `α=π` (K on the *opposite* ray from B). Both
   values of `α` give `sin α = 0`, so the argument as literally stated only excludes one of the two
   failure modes. I checked this is still fixable and true: writing `K=λB+μM+νC` (λ,μ,ν>0, sum 1) and
   requiring `K` on line `AB` forces (via `K=t(p,q)` for some `t`) `ν·a·q=0`; since `a,q>0`, this forces
   `ν=0`, contradicting `ν>0`. So `K∉` the *full* line `AB` (both rays), hence `α∈(0,π)` strictly and
   `sin α>0` — but this full argument is not in either outline as written; only the weaker "not on ray
   BA" half is stated. This must be completed explicitly by the builder, not glossed as "K∉ line AB
   (obviously)".
6. The core convex-combination fact ("triangle with two vertices on a line has all interior points
   strictly on the third vertex's side") is standard (barycentric coordinates of interior points are
   all strictly positive) and I verified it applies correctly here: `B,C` on the x-axis, `M` strictly
   above (`q>0`), so `K` interior ⟹ `K_y=μq/2>0`. Sound.

**Conclusion: the mechanism is genuinely sound** (not a hand-wave-then-hope situation) — `Z>0`/`D1>0`
truly follows from `K` strictly interior to `△BMC` via `X>0` (from `K_y>0`, convex combination) and
`sin α>0` (from `K` off the full line `AB`, provable by the same convex-combination fact, not just
"not on ray BA"). Both outlines have this right in substance but under-justify the `sin α>0` half and
(groebner file only) display a numerically wrong intermediate polynomial. These are both fixable
within the current outline — no RETHINK needed.

## Per-approach verdicts

### `synthetic-angle-chase-aklastar` — CHANGES REQUESTED
- Step 5 (Z>0) mechanism verified sound (see above). Builder must:
  (a) fix the `sin α>0` justification to exclude *both* `α=0` and `α=π` (use the full-line
  barycentric argument above, not just "not on ray BA");
  (b) re-verify `T_K>0` is justified (interior point ≠ vertex B) — already fine, just make it explicit
  as the outline itself flags;
  (c) re-confirm the exact `myexpr·Z = ...` cofactor identity still matches this round's write-up
  (I independently re-derived the decoupling and the `Z` formula from this file's own conventions and
  both check out).
- No case split needed for AB=AC — confirmed, the identity never divides by `p-a/2`.

### `coordinate-groebner-elimination` — CHANGES REQUESTED
- Same Z>0/D1>0 mechanism, same fix needed to the `sin α>0` justification.
- **Additional required fix:** the explicit `g1` polynomial displayed in §3 (all three coefficients,
  including the displayed "`D1 = 2a·ca·q − 2a·p·sa + 2p²·sa + 2q²·sa`") is 4× too large versus a
  from-scratch recomputation from this file's own `e1` — a uniform scalar bookkeeping slip, not a sign
  or structural error, so the sign argument's conclusion survives, but the builder must recompute and
  redisplay the correct `g1`/`D1` (or explicitly note the normalization constant it dropped) before
  this can be called solved — a proof with a wrong displayed intermediate identity is not rigorous
  even if the final conclusion happens to be right.
- No case split needed for AB=AC — confirmed.

### `inversion-at-a-collinearity` — CHANGES REQUESTED (unchanged priority: lower)
- No new claims this round; still has two large open items (hypothesis-translation/collinearity chase,
  general branch-selection for AB=AC only checked on 10 numeric points). Genuinely different framing
  from the two coordinate approaches (inversive, not algebraic-elimination) — valuable for population
  diversity per CLAUDE.md's single-gap-trap rule, since if a subtle error surfaces later in the shared
  Z>0/D1>0 argument, this is the only approach not resting on it. Kept live but lower priority; not
  close to closing this round.
- Fix the stale cross-reference to `synthetic-angle-chase-aklastar.md`'s now-dropped A* framework — this
  file must re-derive "A,K,L,A* concyclic ⟺ OM=ON" locally rather than citing a section that no longer
  exists in the sibling file.

### `isosceles-locus-direct` — RETHINK (unchanged, left cut)
No change proposed this round; correctly left out of the build set.

## Diversity note (per CLAUDE.md)

The two leading approaches (`synthetic-angle-chase-aklastar`, `coordinate-groebner-elimination`) still
share the identical underlying algebraic wall (`Z=D1`, same formula, same closing mechanism) — this was
flagged as a moderate single-gap-trap risk in round 2 and remains true now that both share the identical
*fix* too. This is acceptable for this round because the shared mechanism has now been independently
verified correct by me from both files' own definitions, not merely "both got stuck the same way" — but
if either builder finds a genuine problem with the `sin α>0` argument or the interior-point convexity
fact during write-up, both approaches will fail together. `inversion-at-a-collinearity`'s continued
presence in the population (even at lower priority) is the correct hedge per CLAUDE.md; do not let it
drop out of the population entirely.

## Ranking

Registered: no new slugs this round (all three built approaches already registered from round 2).
Ranked head-to-head via `update_ranking`:
- `synthetic-angle-chase-aklastar` vs `coordinate-groebner-elimination`: draw (both now carry an
  equally strong, independently-verified closing mechanism with a comparable, fixable rigor gap each).
- Both beat `inversion-at-a-collinearity` (still far from closing, two large open items vs. one small
  fixable one for the coordinate pair).

Post-ranking Elo: `coordinate-groebner-elimination` 1531.8, `synthetic-angle-chase-aklastar` 1526.6,
`inversion-at-a-collinearity` 1441.7. All three `stale` flags cleared.

## Build set

Dispatch one builder per slug below, each told to close the specific gaps listed above (not just
restate the outline's step 5/6).

build set: synthetic-angle-chase-aklastar, coordinate-groebner-elimination, inversion-at-a-collinearity
