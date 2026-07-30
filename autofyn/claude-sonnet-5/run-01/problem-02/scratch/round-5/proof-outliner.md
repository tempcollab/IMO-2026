## imo-2026-02

synthetic-angle-chase-aklastar: revise
Target: OM=ON for every triangle ABC satisfying all 5 hypotheses (i)-(iii) plus the two position
hypotheses ("K inside ∠LBA", "L inside ∠ACK") and K,L strictly interior to △BMC,△BNC resp.
Technique: coordinate/synthetic hybrid (already established): reduce OM=ON to `myexpr=0`, parametrize
K,L via hypothesis (i) with a rigorously-fixed rotation sign (certified, `interior-point-side-test.md`),
decouple hyps (ii),(iii) into `A1=0,B1=0`, close via the unconditional cofactor identity
`myexpr·Z = 2(q-T_K X)A1 + 2(T_L X'-q)B1` and `Z>0` (both fully closed, keep verbatim). This round's
revision targets ONLY the one remaining gap: the directed-angle branch selection for `e1,e2`.
Skeleton (unchanged steps 1-6 from current file, kept as-is; NEW step 7 replaces the numeric 5-point
check):
  1. Base reduction OM=ON ⟺ myexpr=0 — Cramer's rule circumcenter formula (certified, keep).
  2. Parametrize K=B+T_K R(-α)(A-B), L=C+T_L R(α)(A-C), T_K,T_L>0 — rotation sign forced by
     interior-point-side-test.md (certified, keep).
  3. sin α>0, α∈(0,π) strictly — barycentric argument (certified, keep).
  4. Hyps (ii),(iii) as polynomial e1,e2 via the cross/dot-sin(θ1-θ2) identity — keep, but the sign
     convention picked for e1,e2 is now justified by step 7 below instead of the 5-point numeric table.
  5. Decoupling e1=T_K·A1, e2=T_L·B1 (certified, `ray-parametrized-angle-decoupling.md`) — keep.
  6. Cofactor identity myexpr·Z = 2(q-T_K X)A1+2(T_L X'-q)B1, and Z>0 (certified) ⟹ myexpr=0 — keep.
  7. **NEW — branch selection, closed-form.** Prove directly from the position hypotheses (not
     numerically) that the specific unflipped e1,e2 (not their sign-negations) are forced.
Key lemmas (claim + mechanism) for the new step 7:
  - **Ray-betweenness sign lemma** (extends `interior-point-side-test.md` to angular sectors, not just
    half-planes): if ray BK lies strictly between rays BA and BL (i.e. "K inside ∠LBA", a convex angle
    since α,∠ABL ∈(0,π)), then simultaneously (a) K and L lie on the same side of line AB — i.e.
    sign(cross(A-B,K-B)) = sign(cross(A-B,L-B)) — and (b) K and A lie on the same side of line BL —
    i.e. sign(cross(L-B,K-B)) = sign(cross(L-B,A-B)). Mechanism: this is exactly the two-line
    "wedge/sector" test for a ray inside a convex angle < π (standard: a ray is between two other rays
    from the same vertex, both spanning less than π, iff it is simultaneously on the same side as each
    bounding ray relative to the *other* bounding line) — same cross-product bilinearity toolkit as the
    certified lemma, just applied to two lines through B instead of one line through B,C.
    Symmetrically for "L inside ∠ACK" at vertex C: sign(cross(A-C,L-C))=sign(cross(A-C,K-C)) and
    sign(cross(K-C,L-C))=sign(cross(K-C,A-C)).
  - **Directed-angle ordering consequence.** Fix the global rotational sense already pinned by step 2/3
    (directed angle from ray BA to ray BK is exactly -α, i.e. clockwise, since sin α>0). Part (b) of the
    betweenness lemma above forces the directed angle from ray BA to ray BL to have the *same sign*
    (also clockwise, call it -β, β:=∠ABL∈(0,π)) and, because K is strictly between A and L on that
    rotational sweep, 0<α<β. Hence the directed angle θ1 from ray BL to ray BK equals (-α)-(-β)=β-α,
    which lies strictly in (0,π) — this alone pins sin θ1>0, i.e. rules out θ1∈(-π,0) as a possibility,
    a genuine sign fact not previously available. This is new content step 7 contributes beyond the
    numeric table: it converts "K inside ∠LBA" into a hard inequality on θ1's range, using the vertex-B
    betweenness data that the population has not yet encoded.
  - **Discriminator route (fallback/complement if the θ2 side at N resists the same direct argument,
    since N is not a vertex of either position hypothesis):** per this round's branchselect explorer,
    numerically confirmed on 1450/1450 broadly-swept valid configs (α∈[0.02,1.4], not just α=0.05):
    sign(dot(L-B,K-B)) = sign(dot(L-N,C-N)) and sign(dot(L-C,K-C)) = sign(dot(B-M,K-M)). If the direct
    θ1,θ2-range argument above cannot be closed for the N/M vertices (which lack a stated position
    hypothesis), fall back to certifying this matching-sign fact as a positivity computation in the
    existing (p,q,a,c,s,T_K,T_L)-coordinate system, reusing the exact barycentric-positivity domain
    already built for the Z>0 proof (K=λB+μM+νC, L=λ'B+μ'N+ν'C, λ,μ,ν,λ',μ',ν'>0) — i.e. substitute
    those barycentric forms into dot(L-B,K-B)·dot(L-N,C-N) [as polynomials in the positive barycentric
    weights and T_K,T_L,c,s] and attempt a sum-of-products-of-positive-terms decomposition, the same
    style of certificate that closed Z>0.
Open gaps: step 7 is NOT yet proven — this is the target for this round's builder. Two candidate
closing mechanisms given above (direct betweenness/angle-range argument at B and C; discriminator
positivity certificate reusing existing machinery) — the builder should attempt (a) first since it
uses the literally-stated position hypotheses and is the most "principled," falling back to (b) if
the N,M-vertex half resists. Do NOT claim solved unless one of (a)/(b) is closed as a genuine
closed-form (not numeric) argument for BOTH e1's branch and e2's branch (the M-vertex analogue).
Cases to cover: none additional beyond the existing AB=AC-uniform treatment (myexpr never divides by
p-a/2, so no isosceles case split is needed anywhere in this route, including step 7 — the betweenness
argument at B,C is symmetric and does not distinguish AB=AC).
Watch out for: (1) do not silently reuse the discriminator's "always positive" framing — the
branchselect explorer explicitly refuted plain positivity (31/1067 sampled cases had ∠LBK obtuse),
only the *matching-sign* claim is robust; (2) the θ1-range argument above only directly controls the
B,C-vertex side of θ1 — it does NOT yet address θ2 (vertex N for e1, vertex M for e2), since the
position hypotheses are stated only for K,L relative to B,C, not N,M; closing θ2's range (or the full
matching-sign claim) is the actual remaining work, not a formality; (3) keep the "unconditional, no
AB=AC case-split" property of the whole chain intact — do not introduce a case split at step 7.

coordinate-groebner-elimination: revise
Target: same as above (OM=ON, full problem).
Technique: same coordinate spine (Groebner-style elimination / cofactor-identity route), independently
re-derived polynomial identities `2Z²·myexpr=(Z·P1)g1+(Z·QA+QB)g2`, `Z>0` — both certified and
confirmed exact by CAS this round's predecessor. This file currently still says "Status: solved" at
its header — **that is stale/incorrect**; current.md's reviewer downgraded it to partial because (a)
the rotation-sign convention was only checked numerically here (the sibling now has it certified via
`interior-point-side-test.md` — this file should switch to *citing* that certified lemma instead of
its own numeric check, not re-deriving it), and (b) this file did not even address the branch-selection
gap for (ii),(iii). Revision: fix the Status header to `partial`, cite `interior-point-side-test.md`
for the rotation-sign piece (drop the numeric-only justification), and add the identical step-7
branch-selection target as `synthetic-angle-chase-aklastar` (same lemma, same two candidate mechanisms
— this file's contribution should be to independently re-verify whichever mechanism the sibling closes,
using its own g1,g2/D1-based polynomial forms as a cross-check, since it is a genuinely different
polynomial parametrization route even though it shares the same underlying geometric facts — this is
NOT a single-gap-trap merge, per run_state's round-4 rule: keep both slugs live so a subtle error in
one doesn't hide behind the other).
Skeleton: identical structure to synthetic-angle-chase-aklastar's 7 steps, expressed in this file's own
g1,g2,D1 notation (D1=2Z after the constant normalization already established); step 7 is the same
open target.
Key lemmas: same two candidates as above (betweenness/angle-range at B,C; discriminator positivity
certificate) — this file should attempt an independent re-derivation in its own coordinate variables
as a cross-check once the sibling proposes a mechanism, rather than inventing a third mechanism.
Open gaps: step 7 (branch selection), identical to the sibling. Also must correct the stale `Status:
solved` header this round regardless of step-7 progress.
Cases to cover: none additional (same AB=AC-uniform property).
Watch out for: do not re-claim "solved" without independently re-deriving step 7's closing argument
from scratch in this file's own notation (per run_state's explicit rule: this file has overclaimed
"solved" twice before — round 2 and round 4 — both times caught by the reviewer re-deriving from
scratch; do not let a third overclaim happen by copy-pasting the sibling's step 7 without independent
verification).

inversion-at-a-collinearity: advance
Target: same (OM=ON, full problem), via inversion centered at A reducing to "K*,L*,A*' collinear."
Technique: unchanged — inversive/cross-ratio route, structurally independent of the coordinate cofactor
machinery (does not share the branch-selection gap's mechanism, though it hits an analogous sign issue
in its own isosceles-case decoupling per its file). Nominate as-is for continued build: its own honest
open gaps (translating hyps (ii),(iii) through the inversion — flagged as a genuine structural
obstruction, not just unsolved) are unrelated to this round's branch-selection focus, so no outline
revision needed. Keep live per CLAUDE.md's single-gap-trap diversity guidance: if step 7 above turns
out to be wrong for both siblings, this is the population's only framing not resting on that mechanism.
Skeleton / key lemmas / open gaps: unchanged from the current file (Lemma 0 base reformulation
certified; Lemma 2 hypothesis-(i) translation certified; hyps (ii),(iii) translation and the closing
collinearity chase remain open, diagnosed as a genuine obstruction of this framing, not merely
unattempted).
Cases to cover: none new this round.
Watch out for: do not let this approach's own isosceles branch-selection sub-question be conflated with
the coordinate siblings' step-7 gap — current.md already correctly notes these are different questions
(this file's is moot for the overall problem since the sibling's identity is unconditional; the
siblings' step-7 is the one actually blocking a full proof).
