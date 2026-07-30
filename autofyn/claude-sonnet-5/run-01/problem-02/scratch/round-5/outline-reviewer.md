## imo-2026-02 — outline review (round 5)

### Process discrepancy (flag before anything else)

`git diff` against the round-4 committed versions shows `synthetic-angle-chase-aklastar.md` and
`coordinate-groebner-elimination.md` are **byte-identical to round 4** — the "revised approach files"
the dispatch says the outliner produced were **not actually written to disk**. Everything below
("Ray-betweenness sign lemma", the citation fix, the `Status: solved → partial` header fix) exists
only in `proof-outliner.md`'s prose, not in the approach files themselves.

**This must be fixed before/while building.** Directive to both builders: treat `proof-outliner.md`'s
step-7 text as the actual content to merge into your approach file this round — do not silently build
on the stale on-disk file as if step 7 were already present. For `coordinate-groebner-elimination.md`
specifically, the on-disk header still literally reads `Status: solved` — the builder must not
re-emit that without redoing the work; per `run_state.md`'s explicit rule this file has overclaimed
solved twice already (rounds 2 and 4) and doing so a third time on an un-updated header would be a
serious lapse.

### Verifying the two candidate step-7 mechanisms

**(a) Ray-betweenness sign lemma + directed-angle ordering consequence.** I re-derived this from
scratch, independent of the outline's prose, in coordinates (`ray BA` along the reference axis,
`α`=clockwise angle to `BK`, `β`=clockwise angle to `BL`, both claimed in `(0,π)`):
- Condition (a) "K,L same side of line AB" ⟺ `sin α`, `sin β` same sign.
- Condition (b) "K,A same side of line BL" ⟺ `sign(sin(β−α)) = sign(sin β)`.
Combining, with `α,β∈(0,π)` (established from (a) plus the already-certified `sin α>0` fact): condition
(b) forces `sin(β−α)>0` and since `β−α∈(−π,π)` this is exactly `β>α`. I confirmed this by direct
cross-product algebra by hand *and* by a 200000-trial random numeric sweep (`python3`, no
counterexample) — the mechanism is **sound**: it does rigorously yield `0<α<β`, hence `θ1 = β−α ∈
(0,π)`, hence `sin θ1 > 0`, as claimed. This is genuine new content, not hand-waving; it correctly
reuses the same cross-product/bilinearity toolkit as the certified `interior-point-side-test.md` (a
close cousin, not literally the same lemma — the outline's phrasing "extends" is fair since the proof
technique is the same, but note it is technically a *new* lemma to write up and certify, not a direct
corollary of the existing file; the builder should write it as its own short lemma, citing the
existing one for the proof *style*).

One small labeling slip in the outline text: it attributes "K,L same side of line AB" (i.e., matching
rotational sense) to "Part (b)"; my derivation shows that fact actually follows from Part (a) of the
betweenness lemma, and Part (b) is what supplies the ordering `α<β`. Trivial to fix, does not affect
soundness — flag it for the builder so the write-up doesn't misattribute the step.

**Genuine, correctly-flagged remaining gap:** the outline itself is honest that this only pins the
`B`-vertex (resp. `C`-vertex) half of `θ1` (resp. `θ2`)'s range — the `N`/`M`-vertex half (needed to
combine into the actual branch of `e1=0` vs. its sign-flip) is *not* addressed by this mechanism, since
the position hypotheses are stated only for `K,L` relative to `B,C`, not `N,M`. This is correctly
scoped as still-open, not smuggled in as solved. Good.

**(b) Discriminator positivity certificate (fallback).** Correctly labeled speculative/fallback,
resting only on a numeric sweep (1450 configs) reusing the `Z>0`-style barycentric-positivity
machinery. The outline is appropriately careful to flag that *plain* positivity is false (31/1067
sampled `∠LBK` obtuse) and only the *matching-sign* claim survives sampling — this caveat is important
and correctly stated; do not let the builder round this up to "route (a) is a formality, we have (b)
as backup" — (b) is unproven and may not close.

Neither mechanism amounts to a circular step or a wrong technique; both are legitimate closed-form (or
honestly-labeled-numeric-fallback) attacks on the correct gap. No fatal flaw found.

### Diversity / single-gap-trap check (per CLAUDE.md)

`synthetic-angle-chase-aklastar` and `coordinate-groebner-elimination` remain, as flagged in prior
rounds, two expressions of essentially the same coordinate/cofactor core, and this round they converge
onto the *identical* remaining gap (step-7 branch selection) with the identical two candidate
mechanisms. If mechanism (a) cannot be extended to the `N`/`M` side and (b) does not yield a genuine
certificate, both siblings die together on the same wall. `inversion-at-a-collinearity` remains the
only population member not resting on this mechanism — its own obstruction (hypotheses (ii)/(iii) do
not translate under inversion-at-`A`) is structurally different and should stay in the build set purely
as a diversity hedge, per the CLAUDE.md single-gap-trap rule, even though it is currently furthest from
closing.

### Verdicts

- **synthetic-angle-chase-aklastar** — CHANGES REQUESTED. Technique and step-7 mechanism (a) are sound
  (independently re-verified above); required before further "solved" claims: (1) actually write
  the step-7 content (currently only in `proof-outliner.md`) into the approach file; (2) fix the
  Part(a)/Part(b) attribution slip; (3) do not claim step 7 closed until the `N`/`M`-vertex half of the
  branch argument is also closed in closed form — a partial closing of only the `B`,`C` side is real
  progress but is not a complete step 7.
- **coordinate-groebner-elimination** — CHANGES REQUESTED. Same step-7 target, but this file additionally
  needs its stale `Status: solved` header fixed to `partial` and the rotation-sign justification
  switched from its own numeric check to citing `interior-point-side-test.md`, per the outliner's plan
  — none of this is yet on disk. Given this file's history (two prior overclaims), the builder must not
  re-emit `Status: solved` this round unless step 7 is closed in full (both vertex sides, no numeric-only
  link) and independently re-derived from scratch, not copy-pasted from the sibling.
- **inversion-at-a-collinearity** — APPROVE (advance, unchanged). No revision needed; keep live as the
  population's only framing independent of the step-7 mechanism, per the diversity note above.

### Ranking

Registered slugs unchanged (all three already in the population from prior rounds; no new/copied slug
this round). Updated Elo via `update_ranking`: `synthetic-angle-chase-aklastar` (1554, has the more
rigorous existing proof surface and no un-mentioned gaps) > `coordinate-groebner-elimination` (1528,
correct algebra but a known overclaim risk and an un-synced revision plan) > `inversion-at-a-collinearity`
(1418, farthest from closing but valuable diversity hedge).

build set: synthetic-angle-chase-aklastar, coordinate-groebner-elimination, inversion-at-a-collinearity
