## imo-2026-02 (lens: alternative framing to sidestep the branch-selection wall)

### Summary verdict up front
Directed angles mod 180° do **not** structurally eliminate the branch-selection gap — it is
intrinsic to the problem, not an artifact of the coordinate route. But the investigation below
identifies a concrete, provable mechanism (a side-test lemma using the *position* hypotheses
"K inside ∠LBA" / "L inside ∠ACK") that is the natural non-numeric way to close the gap, and it
reuses machinery the population has already certified (not a new framework, but the right next
move). Spiral similarity, checked numerically, does **not** apply to hypothesis (ii)/(iii) in the
naive "two-angle SAS-similarity" form — ruled out below with data. Trig-Ceva/unsigned-magnitude
framing is a genuine alternative worth flagging but is essentially equivalent in difficulty to the
already-proposed "cosine-squared" reformulation in `current.md`, i.e. not a new framing so much as
a variant of the existing algebraic route.

### 1. Directed angles mod 180° — does it dodge the branch issue? (Answer: no, but clarifies it)

**Why it looks tempting.** The standard payoff of `∠(XY,ZW)` mod 180° notation (see
`knowledge_base.md`'s Geometry section, "Synthetic toolkit" — angle chasing, concyclicity converse)
is that concyclicity criteria (`X,Y,Z,W` concyclic iff `∠(XZ,YZ)=∠(XW,YW)`) and chase steps compose
*without configuration case-splits*: you never need to know which side of a line a point falls on to
combine two angle facts. This is exactly the kind of case-split the coordinate approaches' rotation-
sign lemma (`interior-point side test`, already certified in `synthetic-angle-chase-aklastar.md`)
had to prove by hand.

**Why it does not solve the actual gap here.** The problem's hypotheses (ii),(iii) are equalities of
*unsigned ray-angles* (`∠LBK=∠LNC ∈[0°,180°]`, angle between two specific rays from a vertex — not
between two lines). Converting `∠LBK=∠LNC` (unsigned, ray-based) into a directed-angle-mod-180°
statement `∠(BL,BK) ≡ ±∠(NL,NC) (mod 180°)` is a **two-way ambiguous step**: reversing either ray
changes the ray-angle to its supplement but changes nothing about the *line* through it, so the
correspondence between "which of the two rays from B is meant" and "which sign the directed angle
takes" is precisely the same fork the coordinate route hits as `e1=0` vs. `e1`-negated. I verified
this is not merely a notational worry — it is the same fork in different clothing: writing out
`∠(BL,BK)` and `∠(NL,NC)` symbolically, `e1` (as defined in the sibling files) is literally
proportional to `sin(θ1−θ2)` where `θ1,θ2` are these two directed angles (see the Appendix in
`inversion-at-a-collinearity.md`... actually in `synthetic-angle-chase-aklastar.md`'s Appendix) — so
switching to `∠(·,·)` notation from the start reproduces `e1` (up to the same sign choice), it does
not avoid defining it.

**What directed angles DO buy, concretely.** If the outliner builds a *fully synthetic* directed-
angle chase (no coordinates at all) from (i)-(iii) straight to "A,K,L,A* concyclic" (Lemma 0's target,
already proved in `inversion-at-a-collinearity.md` for `AB≠AC`), every *intermediate* step of that
chase (concyclicity transfers, inscribed-angle equalities) would be config-independent — so the
population would only need to fix the sign **once**, at the point where the unsigned hypotheses (i)-
(iii) are first translated into directed form, rather than worrying about sign consistency through a
multi-step chase. That single translation step is exactly where the position hypotheses ("K inside
∠LBA", "L inside ∠ACK", "K interior to △BMC", "L interior to △BNC") must be invoked — this is a
genuine reduction of the problem's *scope* of branch-selection work (from "keep signs straight
through the whole argument" to "fix one sign per hypothesis at the start"), even though it's not a
full dodge.

**Concrete, checkable lead for fixing that one sign (new this round, not in either coordinate file).**
The position hypothesis "K inside ∠LBA" should pin `sign(cross(L−B,K−B))` directly, by the identical
side-test mechanism already certified as the "Interior-point side test" lemma
(`synthetic-angle-chase-aklastar.md`, Promotable lemma 3): "K inside ∠LBA" means ray `BK` lies between
rays `BL` and `BA`, i.e. `K` and `A` are on the same side of line `BL` — which should give
`sign(cross(L−B,K−B)) = sign(cross(L−B,A−B))`, a *betweenness* fact provable the same way the
rotation-sign lemma was (writing "between the rays" as a convex-cone condition), not numerically. I
spot-checked this on 3 of the population's own sample configurations:

| config (a,p,q,α) | cross(BL,BA) | cross(BL,BK) | same sign? |
|---|---|---|---|
| (4,1.3,3.1,0.05) | 6.445 | 2.721 | yes (both +) |
| (5,−1.5,2.0,0.05) | 4.621 | 1.634 | yes (both +) |
| (3,2.8,0.5,0.05) | 1.052 | 0.309 | yes (both +) |

This is consistent with the conjectured betweenness fact (and is the kind of fact that should be
provable in closed form, exactly parallel to the already-certified interior-point side test, since
"K inside ∠LBA" is a convex-cone/betweenness statement just like "K interior to △BMC"). **This is my
top recommendation for closing the gap without a new framework**: extend the certified side-test
lemma to a directed-betweenness form and apply it to hypotheses (ii),(iii)'s position qualifiers
directly, rather than to the rotation parametrization only. I did not attempt the proof (out of
scope for this report) — this is a lead, not a result.

### 2. Spiral similarity — checked and largely ruled out for (ii)/(iii) directly

Hypothesis (ii) `∠LBK=∠LNC` gives only **one** of the two angle equalities SAS-similarity would need
to conclude `△LBK ∼ △LNC` (spiral similarity centered at L taking B→N, K→C) — the classical spiral-
similarity lemma (uniqueness of the spiral center; `knowledge_base.md` names "spiral similarity" in
the Synthetic toolkit list but has no detailed lemma text) requires *two* matching angles, or an
equal-ratio side condition, neither of which is given or an obvious consequence of the other
hypotheses. I tested this directly: on 5 of the population's sample configurations, computed the
*second* angle a full similarity `△LBK∼△LNC` would require (`∠BLK` vs `∠NLC`, and `∠LKB` vs `∠LCN`)
— **these differ by 55°–169° across the samples, wildly not equal.** So `△LBK` and `△LNC` are *not*
similar under this correspondence; there is no spiral similarity centered at `L` sending `B→N,K→C`.
This rules out the naive "package hypothesis (ii) as a spiral similarity" idea as stated — it is a
genuine dead end, not an unexplored opening. (I did not test other point/segment pairings — e.g. a
spiral similarity relating `(B,K)` to `(N,C)` centered elsewhere, or one derived jointly from (i)+(ii)
— but the immediate, most natural reading fails cleanly.) Do not pursue "spiral similarity as a direct
translation of (ii) or (iii)" without a different pairing; if revisited, first search for *which*
pair of points a spiral similarity could relate using both (ii) and (iii) jointly (untested here, out
of time budget).

### 3. Trig-Ceva / pure-unsigned-magnitude framing

This is essentially the "cosine equality reformulation" already flagged as an open next-step option
in `current.md`/`synthetic-angle-chase-aklastar.md` (`E_1 := [dot(L−B,K−B)]²|L−N|²|C−N|² −
[dot(L−N,C−N)]²|L−B|²|K−B|² = 0`, likewise `E_2`) — squaring the cosine-equality kills the sign
ambiguity by construction (cosine injective on `[0,π]`), at the cost of a higher-degree polynomial
system whose decoupling/cofactor identity has **not yet been re-derived**. This is a legitimate,
already-identified route, not a new framing per se — I did not find anything beyond what's already
in `current.md`'s "Concrete next step (b)". Flag it as still open and doable, but not this report's
novel finding.

### Knowledge-base entries relevant
- Geometry / Synthetic toolkit (angle chasing, concyclicity converse, spiral similarity, inversion) —
  `knowledge_base.md` lines ~127-138. No detailed spiral-similarity-uniqueness lemma text exists in
  the KB; if the outliner wants to use it rigorously, it must be stated and proved from scratch
  (SAS-similarity + uniqueness of similarity ratio, standard but not pre-supplied).
- No dedicated "directed angles mod 180°" lemma exists in `knowledge_base.md` either — it's referenced
  only implicitly via "angle chasing" and "concyclicity converse." Any directed-angle argument would
  need its case-independence properties stated and used carefully (as the sibling files already do
  informally with cross/dot ↔ sin/cos identities).

### Crux corpus
Per `crux_moves_documentation.md`: **geometry has no cruxes extracted yet** ("Not in the corpus yet;
the problems DB includes geometry problems with solutions, but no geometry cruxes have been
extracted."). So there is no analogous crux to retrieve for this problem — confirmed by reading the
documentation, not guessed. No geometry subtopic list exists to query against.

### Prior progress (context, not new)
`Z>0` is fully closed (rigorous, not numeric) in both coordinate approaches. The sole shared gap
across the whole population (all 3 live approaches) is the directed-angle branch selection for
hypotheses (ii),(iii) — confirmed genuinely intrinsic to the problem (see §1), not a coordinate-route
artifact, since the inversion approach independently hits the same kind of sign ambiguity in its own
isosceles-case decoupling ("branch-selection numeric evidence, not proof" for the isosceles case).

### Dead ends (do not retry)
- Naive spiral similarity centered at L sending `(B,K)→(N,C)` as a direct translation of hypothesis
  (ii) alone: **numerically refuted** (second angle mismatch of 55°-169° across 5 samples, see §2).
- "Switch to directed-angle mod 180° notation" as a way to *avoid* fixing a sign for (ii),(iii): does
  not work — the ambiguity re-appears identically when converting the unsigned hypothesis into
  directed form (see §1); it only reduces *scope* of sign-tracking, not the need for it.

### Recommendation for the outliner
Do not open a wholesale new framework. Instead, add (or extend an existing approach with) a targeted
lemma: prove the **directed-betweenness side test** — "K inside ∠LBA" ⟹
`sign(cross(L−B,K−B)) = sign(cross(L−B,A−B))`, and symmetrically for "L inside ∠ACK" — using the same
convex-cone/betweenness technique that already closed the rotation-sign gap (certified as the
"Interior-point side test" lemma). This is a *closed-form* target, directly checkable against the
population's own sample data (see table in §1, 3/3 consistent), and is the most direct non-numeric
route to close the shared gap without introducing a rival framework that would fragment the
population's shared, already-certified lemmas (`circumcenter-x-coordinate-reduction`,
`ray-parametrized-angle-decoupling`, `interior-point side test`). If pursued, this should be built as
a revision/extension of `synthetic-angle-chase-aklastar` (or a close cousin), not a wholly new slug,
since it reuses that file's coordinate setup and lemma directly.
