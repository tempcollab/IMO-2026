## imo-2026-02 (lens: branch-selection gap for hypotheses (ii)/(iii))

### The gap, precisely restated
Both coordinate approaches (`synthetic-angle-chase-aklastar`, `coordinate-groebner-elimination`)
reduce hyp (ii) `∠LBK=∠LNC` to a polynomial `e1 := cross(L-B,K-B)·dot(L-N,C-N) − cross(L-N,C-N)·dot(L-B,K-B)`
(symmetrically `e2` for (iii)). Writing `θ1` = directed angle from ray `BL` to ray `BK`, `θ2` = directed
angle from ray `NL` to ray `NC` (fixed global orientation), `e1 ∝ sin(θ1−θ2)`, so **`e1=0` is the union
of two components: `θ1=θ2` (mod 2π) and `θ1=θ2+π` (mod 2π)**. The true hypothesis is the *unsigned*
equality `∠LBK=∠LNC`, i.e. `|θ1|=|θ2|`, which (since cos is injective on `[0,π]`) is equivalent to
`θ1=θ2` or `θ1=−θ2` — **a different second branch than the one `e1=0` algebraically contains**. So the
real content of the gap is: prove that on the geometrically valid locus (all five hypotheses + both
position constraints), the configuration lies on the `θ1=θ2` component of `{e1=0}`, not the
`θ1=θ2+π` component (the `θ1=−θ2` branch is automatically excluded — it isn't even a component of
`{e1=0}` — so "branch selection" here really means excluding one specific spurious component of the
polynomial variety, not choosing between two live geometric possibilities). This reframing matters:
it turns the problem from "which of two geometrically-plausible branches is real" into "prove an
inequality that kills the spurious algebraic branch," which is a more tractable target.

### Recommended mechanism (primary): same-sign-of-cosines discriminator
Since `θ1=θ2+π` forces `cos θ1 = −cos θ2` (i.e. `dot(L−B,K−B)` and `dot(L−N,C−N)` have **opposite**
sign, generically), while `θ1=θ2` forces `cos θ1=cos θ2` (**same** sign), the spurious branch is killed
by proving, from the position/interiority hypotheses alone (no reference to `e1=0` itself):
```
sign(dot(L−B,K−B)) = sign(dot(L−N,C−N))          [kills the spurious branch of e1=0]
sign(dot(L−C,K−C)) = sign(dot(B−M,K−M))          [kills the spurious branch of e2=0]
```
This is a **strictly weaker, more tractable claim** than pinning down the branch directly, and it is
exactly the same *flavor* of argument as the certified `interior-point-side-test` lemma (a sign/
same-side fact derived from barycentric positivity), so it is plausibly provable by the same toolkit —
except here it's a *dot*-product (cosine) sign, not a cross-product (side) sign, so it likely needs a
genuinely new lemma (e.g. bounding the relevant angles into a common half-range like `(−π/2,π/2)`
where cosine's sign is controlled by an inequality on distances, or via the law of cosines).

**I numerically stress-tested this discriminator** (not a proof, but far broader evidence than the
5-point check currently in the files): solved the *literal* unsigned-angle equations (ii),(iii) by
root-finding (independent of the polynomial `e1,e2` forms) for 4000 random `(a,p,q,α)` with `α` ranging
over `[0.02, 1.4]` (28× wider than the existing check's single `α=0.05`), keeping only the 1450 trials
where `K,L` came out strictly interior to `△BMC,△BNC` respectively. Result: **`sign(dot(L−B,K−B)) =
sign(dot(L−N,C−N))` held in all 1450/1450 valid configurations, zero exceptions** (and, separately,
this sign is *not* always positive — 31/1067 sampled cases had `dot(L−B,K−B)<0`, i.e. `∠LBK` obtuse —
so "always positive" would be false; it's specifically the *matching-sign* claim that's robust). This
is strong conjectural support that the same-sign discriminator is the right closed-form target, and
that a naive "always-positive" framing would fail as a lemma statement.

**What's still open:** I did not find (and did not attempt to find, per my scouting mandate) a
synthetic/algebraic proof of the same-sign claim itself. Candidate routes for the outliner:
(a) bound `θ1,θ2` both into `(−π/2,π/2)` (or some other common interval where sign of cosine is a
    priori fixed) using the interiority of `K,L` plus hypothesis (i)'s `α`-relations — would need an
    explicit angle-chasing bound, not just a side test;
(b) derive the sign of each dot product directly in the existing `(p,q,a,ca,sa,t_K,t_L)` coordinate
    system (the machinery is already built — `dot(L−B,K−B)` and `dot(L−N,C−N)` are already explicit
    polynomials in that system from the existing sympy setup) and try to certify the *product*
    `dot(L−B,K−B)·dot(L−N,C−N) ≥ 0` as a sum-of-squares / positivity fact on the valid parameter domain
    (defined by the barycentric-positivity inequalities for `K∈△BMC`, `L∈△BNC` already in use for the
    `Z>0` proof) — this reuses the exact coordinate infrastructure already certified, so is likely the
    lowest-effort path structurally, even though the positivity certificate itself is new work;
(c) a hybrid: use (i)'s established sign (`sinα>0`, `K` on `C`-side of `AB`) plus the "K inside ∠LBA"
    hypothesis to bound `θ1` (angle `∠LBK`) via `θ1 < ∠ABL` or similar chain, but this is only a
    sketch, not verified — flagged as more speculative than (a)/(b).

### Recommended mechanism (secondary, complementary not competing): encode the unused position hypotheses directly
`current.md`'s own "new bottleneck" note observes hyps "K inside ∠LBA" and "L inside ∠ACK" are not
encoded anywhere in the coordinate route beyond apparently being automatically implied. I confirm this
observation: the parametrization only uses `K` interior to `△BMC`/`L` interior to `△BNC` (via
barycentric positivity) and hypothesis (i) (via the rotation-sign lemma); nothing in the current chain
touches "K inside ∠LBA" or "L inside ∠ACK" at all. These are candidate *additional* algebraic
constraints (inequalities on `t_K,t_L,α,p,q,a`) that — if translated via the same cross-product
side-test style as the certified `interior-point-side-test` lemma, but applied to *angular sectors*
(ray `BK` betweeen rays `BL` and `BA`, tested via `sign(cross(BA,BK))=sign(cross(BA,BL))` and
`sign(cross(BL,BK))·sign(cross(BL,BA))<0`, i.e. the standard "ray between two rays" cross-product
criterion) — might directly force the same-sign discriminator above, or force the branch more
directly. I did not verify this reduction algebraically (out of scope for scouting), but flag it as
the more "principled" route since it uses the two hypotheses the problem literally states and the
population has flagged as currently idle — versus mechanism (primary) which is a discriminator found
by working backward from what distinguishes the two branches.

### Mechanism explicitly NOT recommended: continuity/connectedness (item 3 of dispatch)
Both existing files flag this as a possible route but note it's unproven. On reflection this is a
**weaker target than mechanism (primary)**, not just unproven: even if the configuration space of
valid `(a,p,q,α,t_K,t_L)` is shown connected and the branch is locally constant away from a
degenerate locus, one still needs (i) a rigorous connectedness proof (nontrivial — the domain is cut
out by several barycentric-positivity inequalities in 6 variables) and (ii) to rule out that the
"degenerate locus" (where `e1` changes branch, i.e. where `cos θ2=0` making the two branches coincide
locally) doesn't actually intersect the valid region, which is itself basically the same sign-fact as
mechanism (primary) but harder to state cleanly. I'd deprioritize this unless (primary)/(secondary)
both stall.

### Crux corpus check
Per `crux_moves_documentation.md`, **the corpus explicitly has no geometry cruxes yet** ("geometry —
Not in the corpus yet; the problems DB includes geometry problems with solutions, but no geometry
cruxes have been extracted"). So there is no subtopic to filter by and no analogous crux moves to
retrieve for this problem — confirmed by reading the documentation, not guessed. **Analogous past
problems (cruxes): none** — the corpus cannot help with this gap; do not spend more rounds querying
it for this problem.

### Knowledge-base entries
`knowledge_base.md` has no entry specific to "directed angle branch selection" (grepped for
`directed angle|orientation|branch|signed angle` — no hits). The relevant reusable technique already
in the population (not in `knowledge_base.md` proper, but certified in `results/imo-2026-02/lemmas/`)
is `interior-point-side-test.md` — recommend the outliner consider **promoting a new lemma** once
either mechanism above is closed (e.g. "same-sign-of-cosines from interior position" or "ray-
betweenness cross-product criterion") to `knowledge_base.md` for reuse, since branch-selection-for-
unsigned-angle-hypotheses is a generic geometry-with-coordinates issue that will likely recur.

### Prior progress (unchanged from current.md, restated for this lens)
`Z>0` gap fully closed (rounds 4). The cofactor identity `myexpr·Z = 2(q−T_KX)A1+2(T_LX'−q)B1` (or
the `2Z²·myexpr=...` fully-polynomial version) is verified exactly by CAS, unconditionally. The sole
remaining gap for the coordinate route is the branch-selection issue scouted here.

### Dead ends / cautions
- Treating "always positive" dot products as the target lemma is **wrong** — numerically refuted (31
  counterexamples to positivity out of 1067, i.e. `∠LBK` can be genuinely obtuse). The correct,
  numerically-robust target is the *matching-sign* claim, not positivity.
- The existing 5-point numeric check (all at `α=0.05`) is much weaker evidence than it might appear;
  my 1450-configuration sweep over `α∈[0.02,1.4]` is a substantially stronger (still non-proof)
  confirmation and should replace it as the population's working conjecture-support if a numeric
  citation is needed while the closed-form proof is pursued.
- Do not conflate this gap with the already-closed rotation-sign convention gap (K = B+T_K R(−α)(A−B)
  vs R(+α)) — that is a different, already-certified fact (`interior-point-side-test.md`). This
  report's gap is specifically about hyps (ii)/(iii)'s branch, one level "downstream" of that.

### Small-case / intuition notes (conjectural, numeric evidence only)
- Conjecture (strong numeric support, 1450/1450): `sign(dot(L−B,K−B)) = sign(dot(L−N,C−N))` and
  `sign(dot(L−C,K−C)) = sign(dot(B−M,K−M))` hold on every valid configuration satisfying all of the
  problem's hypotheses (interiority of K,L, hypothesis (i), and the literal unsigned angle equalities
  (ii),(iii)).
- Conjecture refuted: these dot products are not always positive individually (so `∠LBK`, `∠LNC` etc.
  can each be obtuse) — only their *pairwise sign match* is robust.
