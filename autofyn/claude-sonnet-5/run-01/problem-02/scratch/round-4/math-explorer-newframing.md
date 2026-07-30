## imo-2026-02

### HEADLINE FINDING (verified numerically + symbolically to float precision): the shared Z≠0 gap has a clean closed-form trig resolution

The quantity `Z = aX + s(p²+q²)` (with `X=cq-ps`, `c=cosα, s=sinα`) that both `synthetic-angle-chase-aklastar` and `coordinate-groebner-elimination` need nonzero to divide through and conclude `myexpr=0` is **NOT an arbitrary function of (p,q,a,α)** — it depends on p,q,a **only through |AB| and the angle β:=∠ABC** (the actual angle of the triangle at B), and admits the exact trig identity (verified symbolically in sympy to ~1e-14, i.e. an algebraic identity, not a coincidence):

```
Z = |AB| · ( a·sin(β − α) + |AB|·sin(α) )
```//
where β = ∠ABC (angle between rays BA, BC at vertex B), a = BC, |AB| = AB.

**Why this closes the gap:** hypothesis (i) says α = ∠KBA, and the position hypothesis "K interior to triangle BMC" (BMC ⊆ ABC, with M on segment AB) forces ray BK to lie *strictly between* ray BA and ray BC — i.e. **0 < α < β < π** is forced directly by the stated interior-point hypothesis. Under this constraint, `sin(β−α) > 0` and `sin(α) > 0`, and `a, |AB| > 0`, so **Z > 0 identically** on the entire geometrically valid locus (not just "not of fixed sign on the ambient space" — on the *valid* locus it is strictly positive, provably, via one line of trig, no discriminant/Gröbner needed).

I verified this two ways:
1. Symbolically: `Z − |AB|·(a·sin(β−α) + |AB|·sin α) ≡ 0` (sympy, β=atan2(q,p), random substitution gives residual ~1e-14, i.e. an exact identity — this is really just `q cosα − p sinα = |AB| sin(β−α)` since (p,q) = |AB|(cos β, sin β)).
2. Numerically on the actual valid locus: sampled 40 random triangles + α with fsolve to find the true (T_K,T_L) satisfying hypotheses (ii),(iii), filtered to those where K is genuinely inside triangle BMC and L inside triangle BNC, and computed Z directly from its polynomial definition — **all 40 gave Z > 0** (range ~3 to ~36), zero negative hits, consistent with the trig proof above.

**This means the whole shared gap does NOT need a new framing to close — it needs exactly one geometric observation** (ray BK strictly between rays BA, BC ⟹ 0<α<∠ABC) plugged into the already-derived trig identity for Z. This is a *repair* to the existing coordinate approaches, not a rival framing, but it is the single most important finding this round: **the "Z≠0 needs the geometrically-constrained sub-locus" gap flagged as open in current.md is closeable in ~3 lines**, via:
(a) prove Z = |AB|(a sin(β−α) + |AB| sin α) as a trig identity (short, purely algebraic, done above);
(b) prove 0<α<β from "K interior to triangle BMC" (short synthetic argument: BMC ⊆ ∠ABC since M∈segment AB);
(c) conclude Z>0, divide, done.
Recommend the outliner route the `synthetic-angle-chase-aklastar` / `coordinate-groebner-elimination` builders to attempt exactly this closing move next round rather than the discriminant-of-A1 route mentioned in current.md (that route is unnecessary and more complex than this).

### Distinct openings explored (per dispatch, genuinely different framings)

1. **Power-of-a-point at M, N directly (no A* point)** — numerically confirmed the reformulation `OM=ON ⟺ pow(M,circle(AKL)) = pow(N,circle(AKL))` (this matches `isosceles-locus-direct`'s untested idea). I pushed further: since A,M,B are collinear (M is the midpoint of AB) and A,N,C are collinear, the "second intersection of line AM with circle(AKL)" is literally **the second intersection of line AB with circle(AKL)**, call it X₁; symmetrically line AC meets circle(AKL) again at X₂ (line AN = line AC). So `pow(M,ω)=MA·MX₁` (signed) and `pow(N,ω)=NA·NX₂` (signed), and since MA=MB, NA=NC (midpoint property), OM=ON reduces to `MB·MX₁ = NC·NX₂`. Numerically (same test triangle as headline finding) I located X₁≈(0.412,0.983) at parameter t≈0.683 along AB (from A) and X₂ at t≈0.622 along AC — **these do not coincide with K, L, or any other named point in a way I could detect in one example**, so this reformulation, while clean and true, does not obviously collapse further; I did not find a synthetic characterization of X₁, X₂ from the hypotheses. Verdict: legitimate alternative target (no A* needed at all), but currently no closing move found — would need a full round to chase; not clearly easier than the coordinate route now that the Z-gap has the closing move above.

2. **Trig-only (no Cartesian K,L) approach** — the headline finding above is itself a partial realization of this: Z, expressed via β=∠ABC, is a "trig-native" quantity. I did not find a way to eliminate T_K,T_L (the ray-length parameters) entirely from the argument — they seem structurally necessary since K,L's exact position (not just direction) matters for the final circumcenter computation. Not a full alternative route, but the successful trig reduction of Z suggests the same trick (expressing coordinate polynomials via the actual triangle angles B, C rather than raw p,q,a) may simplify other parts of the existing coordinate proof too — worth trying on `myexpr` itself.

3. **Complex-number approach** — not separately tested this round (time budget); given the headline finding closes the actual gap cheaply, I recommend not spending a round on a full complex-number rewrite unless the trig closing move (above) turns out to have a subtlety I missed.

4. **Load-bearing check on position hypotheses** — confirmed numerically (consistent with `synthetic-angle-chase-aklastar`'s own note) that the algebraic identity `myexpr = q1·A1+q2·B1` holds for *all* root branches of the two quadratics, not just the geometrically valid one — so the position hypotheses ("K inside ∠LBA", "L inside ∠ACK", "K inside △BMC", "L inside △BNC") are NOT needed for the OM=ON identity itself. They ARE needed for exactly one thing: establishing 0<α<β (and symmetrically for L,C,N) which is precisely what proves Z≠0 in the headline finding. So the position hypotheses are load-bearing — but only for the sign argument on Z, not for existence/uniqueness bookkeeping as previously assumed. This reframes what the position hypotheses are "for" in the whole proof, which the outliner should state explicitly.

### Cheap-kill candidates
- None further beyond the Z>0 trig identity above (which is itself the cheap kill for the shared gap).

### Knowledge-base entries to use
- **Synthetic toolkit** (KB line ~129-131): power of a point / concyclicity converse (used in opening 1), trig cevians, inversion — all already in play across the three live approaches.
- **Coordinates / complex / barycentric** (KB line ~137-140): "place coordinates to exploit symmetry" — the headline finding is exactly this in reverse: converting a coordinate polynomial (Z) back into the triangle's native angle β to get a sign argument, rather than a bare Gröbner/discriminant computation.

### Analogous past problems (cruxes)
- **None** — `crux_moves_documentation.md` states explicitly: "geometry — Not in the corpus yet; the problems DB includes geometry problems with solutions, but no geometry cruxes have been extracted." So no crux-corpus query is possible for this problem; do not force a match.

### Prior progress
See `current.md`: the reduction to `myexpr=0 ⟺ OM=ON`, the decoupling of hypotheses (ii),(iii) into quadratics `A1(T_L)=0`, `B1(T_K)=0`, and the polynomial identity `myexpr·Z = 2(q−T_K X)A1 + 2(T_L X'−q)B1` are all independently reviewer-verified and correct. The **only** open item, per current.md, is `Z≠0` on the valid locus — **this round's headline finding closes exactly that item** via `Z=|AB|(a sin(β−α)+|AB| sin α) > 0` given `0<α<∠ABC` (itself immediate from "K interior to △BMC").

### Dead ends (do not retry)
- `isosceles-locus-direct`'s literal idea was already cut by the outline-reviewer as empirically false in an earlier round (per current.md) — but the power-of-a-point-at-M,N-directly reformulation (opening 1 above) is a *different, valid* idea that I re-derived and numerically confirmed true (just not yet closed); don't conflate the two.
- The "isosceles branch-selection via symmetry-only" argument in `synthetic-angle-chase-aklastar` was abandoned as insufficiently rigorous (proving the swap-involution is the identity map is as hard as the original problem) — do not retry this.
- Ruled out by `inversion-at-a-collinearity`: literal spiral-similarity-center hypotheses for K,L relative to (B,N,C)/(C,M,B) — checked exactly false, don't retry.
- The discriminant-of-A1-forced-positive route mentioned in current.md as one of two proposed ways to close Z≠0: superseded/unnecessary now that the direct trig identity (headline finding) gives Z>0 in 3 lines; deprioritize in favor of the trig route.

### Small-case / intuition notes (labeled as conjecture where not fully proved)
- **Proved (short, symbolic + synthetic):** Z = |AB|·(a·sin(β−α) + |AB|·sin α) is an exact algebraic identity (verified via sympy substitution, residual ~1e-14 across 20 random points — this is a genuine trig identity, essentially q cosα − p sinα = |AB| sin(β−α), not a numerical coincidence).
- **Proved modulo the one-line synthetic fact "K ∈ int(△BMC) ⟹ 0<∠KBA<∠ABC":** Z > 0 on the entire geometrically valid locus. (The synthetic fact itself is essentially immediate: M lies on segment AB, so triangle BMC's angle at B, ∠MBC, literally equals ∠ABC=β; K in the interior of △BMC puts ray BK strictly between ray BM(=ray BA) and ray BC, i.e. 0<∠KBA<β. This should be stated and proved explicitly and rigorously in the outline, but it is not deep.)
- **Conjecture only (not pursued further, opening 1):** X₁ (second intersection of line AB with circle(AKL)) and X₂ (second intersection of line AC with circle(AKL)) may have a clean synthetic description in terms of K, L, or the hypotheses, but I did not find one in the time available — flagging for a future round only if the trig-Z closing move (headline finding) somehow fails to fully close the proof.
