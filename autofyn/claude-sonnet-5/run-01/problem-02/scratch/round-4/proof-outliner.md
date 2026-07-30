## imo-2026-02

synthetic-angle-chase-aklastar: revise
Target: OM=ON for every triangle ABC and every valid (K,L) satisfying hypotheses (i)-(iii) — the
whole problem, via the coordinate/myexpr route (this slug's chosen top-level framing: reduce to a
single scalar polynomial identity myexpr=0, no auxiliary A* point needed in the final write-up).
Technique: coordinate bash (Cramer's-rule circumcenter formula) + a directed-angle cross/dot
translation of hypotheses (ii),(iii) into two decoupled quadratics, closed by an explicit cofactor
identity myexpr·Z = 2(q−T_K X)A1 + 2(T_L X'−q)B1, PLUS (new this round) an elementary sign/positivity
argument that Z>0 unconditionally on the geometrically valid locus.
Skeleton (unchanged steps 0-4 already reviewer-certified; step 5 is new):
  0. OM=ON ⟺ O_x = (2p+a)/4 — elementary (M,N share height q/2, perp bisector of MN is vertical).
     [Already certified.]
  1. Circumcenter Cramer's-rule formula gives O_x − target = myexpr/D, D=2·cross(K−A,L−A)≠0 (A,K,L
     non-collinear since AKL is a genuine triangle). [Already certified.]
  2. Parametrize K = B + T_K·R(−α)(A−B), L = C + T_L·R(α)(A−C); hypothesis (i) automatic. [Certified.]
  3. Hypotheses (ii),(iii) as polynomial equations e1=T_K·A1(T_L,...), e2=T_L·B1(T_K,...) via the
     cross/dot directed-angle lemma; T_K,T_L>0 so (ii),(iii) ⟺ A1=0, B1=0. [Certified.]
  4. Cofactor identity: myexpr·Z = 2(q−T_K X)A1 + 2(T_L X'−q)B1 exactly, where X=cq−ps, X'=cq+s(p−a),
     Z=aX+s(p²+q²) — verified symbolically (reviewer-certified in round 2). Hence A1=B1=0 ⟹
     myexpr·Z=0.
  5. **NEW — close Z≠0 (in fact Z>0).** X = K_y/T_K where K_y is the y-coordinate of K. K is strictly
     interior to triangle BMC, which lies in the closed upper half-plane {y≥0} (B=(0,0), C=(a,0) on
     the x-axis; M=(p/2,q/2) has q>0) and touches y=0 only along edge BC. So K interior ⟹ K_y>0
     strictly (write K = λB+μM+νC, λ,μ,ν>0, λ+μ+ν=1 ⟹ K_y = μ·q/2 > 0). Since T_K>0, X = K_y/T_K > 0.
     Also α=∠KBA is a genuine unsigned angle of the configuration, α∈(0,π) (degenerate only if K∈line
     AB, excluded since K is a proper interior point of BMC, not on ray BA), so s=sin α>0. With a>0
     and p²+q²=|AB|²>0, Z = aX + s(p²+q²) is a sum of two strictly positive terms, hence Z>0.
     Therefore myexpr·Z=0 with Z≠0 gives myexpr=0, hence (step 0-1) OM=ON.
Key lemmas (claim + mechanism):
  - Cofactor identity myexpr·Z = 2(q−T_K X)A1 + 2(T_L X'−q)B1 — already certified (reviewer
    re-derived from scratch, round 2).
  - **Z>0 on the valid locus** — because K interior to △BMC forces K_y>0 (convex-combination
    argument: B_y=C_y=0, M_y=q/2>0, so any strict convex combination with positive M-weight has
    positive y), giving X=K_y/T_K>0, and α∈(0,π) (K not on line AB) gives sin α>0; Z is then a sum
    of two positive terms a·X and sin(α)·|AB|².
Open gaps: none structural remain if step 5 is written up rigorously and cleanly integrated with
steps 0-4 (which are already reviewer-certified) — this closes the whole approach. Builder must:
(a) restate/reprove the convex-combination fact "interior point of a triangle with two vertices on
a line has strict sign matching the third vertex" cleanly and generally (don't just wave at it);
(b) justify tK>0, i.e., K≠B, from the position hypotheses explicitly (K strictly interior to a
triangle not containing B on its boundary interior... actually simplest: K interior to △BMC and
B is a vertex, so K≠B trivially since interior points differ from vertices) — make this explicit;
(c) re-verify end-to-end that steps 0-4's polynomials (myexpr, e1, e2, A1, B1, Z) match exactly what
this file's certified version uses — do not silently reintroduce a sign/convention error since the
file's convention (K=B+T_K·R(−α)(A−B)) was locked in by a numeric construction check in round 2;
re-verify that check still applies, or redo it if any formula changed.
Cases to cover: none — step 5's argument is convention/sign-free w.r.t. AB=AC vs AB≠AC (works
identically at p=a/2), so no isosceles case split is needed anywhere in this approach.
Watch out for: don't accidentally use L-side facts (T_L>0, L interior to BMC-analog) to prove Z>0 —
the argument only needs the K-side hypothesis, so keep the proof minimal and don't over-claim
machinery it doesn't use. Also watch that "genuine unsigned angle α∈(0,π)" needs a one-line
justification (K∉ line AB) rather than being asserted as obvious.

coordinate-groebner-elimination: revise
Target: OM=ON for every triangle ABC and every valid (K,L) — same whole-problem target, via this
slug's own independent coordinate parametrization (tK,tL with cos α, sin α as separate symbols ca,sa
tied by ca²+sa²=1, rather than the rotation-operator R(θ) notation) and its own independently-derived
factorization e1=tK·const·g1(tL), e2=tL·g2(tK), closed via a two-step polynomial-division cofactor
identity D1·myexpr = D1·Q1·g1 + (QA+QB·tL)·g2.
Technique: coordinate bash + Gröbner-style two-variable polynomial division, closed by the same
underlying sign/positivity argument as above (D1 = 2·(a·X + sa·|AB|²) = Z is literally the same
quantity, confirmed identical in this file's own gap description — "D1 = 2·(a·X + sa·|AB|²) where
X = q·ca−p·sa is the y-component of the unit direction B→K").
Skeleton (steps 1-5 already reviewer-certified independently of the sibling approach; step 6 is new):
  1. OM=ON ⟺ Re(O)=(2p+a)/4 — elementary. [Certified.]
  2. Polynomial parametrization K=(tK(p·ca+q·sa), tK(q·ca−p·sa)), L symmetric; hypothesis (i)
     automatic by construction. [Certified.]
  3. e1 = tK·[|AC|²]·g1(tL,...), e2 = tL·g2(tK,...) — decoupling verified by direct expansion.
     [Certified.]
  4. myexpr := (p−a/2)cross(u,v) + Im(v)|u|² − Im(u)|v|² satisfies OM=ON ⟺ myexpr=0; never divides
     by (p−a/2), so no isosceles case split needed. [Certified.]
  5. Two-step polynomial division gives D1·myexpr = D1·Q1·g1 + (QA+QB·tL)·g2 exactly (D1 = tL²
     leading coefficient of g1). From g1=g2=0 (i.e. hypotheses (ii),(iii)), get D1·myexpr=0.
     [Certified — the division itself, mod ca²+sa²=1, was verified with zero remainder.]
  6. **NEW — close D1≠0 (in fact D1>0).** D1 = 2(a·X + sa·|AB|²) where X = q·ca − p·sa is exactly
     the y-coordinate of K divided by tK: K_y = tK·(q·ca−p·sa) = tK·X. Same argument as the sibling
     approach's step 5: K strictly interior to △BMC (which has B=(0,0), C=(a,0) and third vertex
     M=(p/2,q/2), q>0, so the triangle lies in the closed upper half-plane, touching y=0 only along
     BC) forces K_y>0 by convexity (K=λB+μM+νC, λ,μ,ν>0 summing to 1 ⟹ K_y=μq/2>0); since tK>0
     (K is an interior point, hence ≠ vertex B), X=K_y/tK>0. Also α=∠KBA∈(0,π) is a genuine
     angle (K∉line AB since K is interior to △BMC, not on ray BA), so sa=sin α>0. Hence
     D1 = 2(a·X + sa·|AB|²) is a sum of two positive terms (a>0, |AB|²>0), so D1>0.
     Substituting into step 5's identity: myexpr = 0 follows, so (step 1) OM=ON.
Key lemmas (claim + mechanism):
  - Two-step division cofactor identity — already certified.
  - **D1>0 on the valid locus** — identical mechanism to the sibling approach's Z>0 (D1 = Z up to a
    factor of exactly 2 in this file's own normalization, per its own gap note): K interior to △BMC
    ⟹ K_y>0 (convex combination sign) ⟹ X=K_y/tK>0; α∈(0,π) ⟹ sa>0; D1 is a sum of two positive
    terms.
Open gaps: none if step 6 is written up carefully (same caveats as the sibling approach: justify
tK>0 explicitly from "K is an interior point, hence not equal to vertex B", justify α∈(0,π) from
"K∉line AB").
Cases to cover: none — same as sibling, no isosceles split needed (myexpr never divides by p−a/2,
and the D1>0 argument doesn't depend on p=a/2 vs p≠a/2).
Watch out for: this file's own gap note in §6 suggested tying D1 to "the discriminant of g1" or
"handling the D1=0 locus separately" — BOTH of these routes are now unnecessary and should be
DROPPED in favor of the direct positivity argument above (per both explorer reports); don't let the
builder waste time re-deriving the discriminant route. Also: double check the sign convention
(ca,sa) used in THIS file's K,L parametrization exactly matches "X=K_y/tK" as claimed — this file
uses K=(tK(p·ca+q·sa), tK(q·ca−p·sa)) so K_y = tK(q·ca−p·sa) = tK·X literally by this file's own
definition of X; confirm this before invoking the argument, since the two sibling files use
slightly different rotation-sign conventions (R(−α) vs explicit ca,sa formula) and a mismatched
sign would invalidate the "sum of positives" step.

inversion-at-a-collinearity: advance (lower priority)
Target: OM=ON for every valid (K,L) via inversion centered at A turning "A,K,L,A* concyclic" into
"K*,L*,A*' collinear," plus a separate isosceles (AB=AC) branch-selection argument.
Technique: inversive geometry (cross-ratio realness ⟺ concyclic-or-collinear), reduction to a
collinearity chase in the inverted picture.
Skeleton: unchanged from current file — Lemmas 1-3 (inversion distance formula, similar-triangle
correspondence, cross-ratio/concyclicity-preservation) are reviewer-certified and reusable; the
open items are (a) translate hypotheses (i)-(iii), each anchored at a vertex ≠A, through the
inversion into a clean statement about K*,L*,A*' (the "up to eight sub-angle" bookkeeping flagged
as unresolved), and (b) for AB=AC, rule out the three non-symmetric root branches of the shared
quadratic Q(α,x) (currently only checked on 10 numeric samples).
Key lemmas: Lemmas 1-3 (certified). Decoupling lemma for the isosceles case (certified, elementary
expansion). No new lemma proposed this round.
Open gaps: (a) the full hypothesis-translation/collinearity chase (large, structurally unresolved —
this is a genuinely different mechanism from the coordinate approaches' cofactor identity, so it
does NOT benefit from this round's Z>0 finding at all); (b) general branch-selection proof for
AB=AC (still only numeric).
Cases to cover: AB=AC handled separately from AB≠AC by construction (this approach's stated design,
unlike the two coordinate approaches above which now need no case split at all).
Watch out for: this file's own note that its base-reformulation citation into
`synthetic-angle-chase-aklastar.md` is now stale (that file dropped the A*-concyclicity framework in
favor of the direct myexpr route) — the builder should re-derive "A,K,L,A* concyclic ⟺ OM=ON, for
AB≠AC" locally in this file (a short standard argument: A* is the reflection-type point making
AA*BC... a rectangle-derived point; the equivalence to OM=ON was established by the round-2
explorers) rather than citing a file that no longer contains it.
Priority note: since both sibling coordinate approaches now have a concrete, short (roughly one-page)
closing argument for their sole remaining gap, and this approach's remaining gaps ((a) and (b) above)
are each still substantial and unresolved after two rounds of dedicated effort, recommend the
outline-reviewer treat this as lower priority for this round's build set — build the two revised
coordinate approaches first; only include this slug in the build set if builder capacity remains,
since a second, independent framing reaching `solved` is valuable insurance (per CLAUDE.md's
single-gap-trap warning) in case a subtle error surfaces in the shared Z>0/D1>0 argument on review.

isosceles-locus-direct: no change (leave cut)
Target: n/a — remains RETHINK per round 2 outline-reviewer (its literal power-of-a-point-at-M,N idea
had an unverified, unclosed step). This round's newframing explorer independently re-derived the
power-of-a-point-at-M,N reformulation (opening 1 in its report) and confirmed it is TRUE but found no
synthetic characterization of the two secant second-intersection points X1,X2 — so the situation is
unchanged: a valid reformulation with no closing move. Given two other approaches are now close to
`solved`, do not force a revival of this slug this round; it stays in the population file as a
historical record only, not nominated for the build set.
