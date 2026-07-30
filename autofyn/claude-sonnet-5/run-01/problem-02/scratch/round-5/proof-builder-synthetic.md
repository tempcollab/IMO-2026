## imo-2026-02 — synthetic-angle-chase-aklastar (round 5)

Closed the last open gap (directed-angle branch selection for hypotheses (ii),(iii)) in full, closed
form, no numerics load-bearing. File rewritten: `results/imo-2026-02/approaches/synthetic-angle-chase-aklastar.md`.
Status changed `partial` -> `solved`.

Mechanism used: proved a new general **ray-betweenness sign lemma** (Lemma A) — if P is interior to
the convex angle ∠RVQ (intersection of the two bounding half-planes, the standard definition), then
sign(cross(P-V,Q-V)) = sign(cross(R-V,P-V)) — proved from scratch via a directed-angle case split
(σ=±1), generalizing the certified `interior-point-side-test.md` from one line to a two-line angular
sector.

Applied it twice:
- Vertex B, using "K inside ∠LBA" (V=B,R=A,Q=L,P=K): gives cross(L-B,K-B)>0.
- Vertex C, using "L inside ∠ACK" (V=C,R=A,Q=K,P=L): gives cross(L-C,K-C)>0.

Then closed the previously-open "N/M-vertex half" (the part the outline/outline-reviewer explicitly
flagged as not yet addressed) via two *new applications* of the already-certified
`interior-point-side-test.md` lemma, on edges not previously used in this file:
- Edge NC of triangle BNC, off-vertex B: gives cross(L-N,C-N)>0 (via cross(C-N,B-N)=-qa/2<0, computed
  directly and exactly).
- Edge MB of triangle BMC, off-vertex C: gives cross(B-M,K-M)>0 (via cross(B-M,C-M)=qa/2>0).

All four cross products strictly positive places all four directed angles θ1,θ2,θ1',θ2' strictly in
(0,π). Combined with the trivial fact that a directed angle already in (0,π) equals its own unsigned
magnitude, the literal *unsigned* hypotheses (ii) ∠LBK=∠LNC and (iii) ∠LCK=∠BMK translate into exact
directed-angle equalities θ1=θ2, θ1'=θ2' — no branch ambiguity survives, no continuity/connectedness
argument needed, no numeric check needed. This directly gives e1=0, e2=0 for the specific (unflipped)
polynomials already used in the rest of the chain (cofactor identity, Z>0, all previously certified),
completing the proof.

Verified all four new sign facts (F1's two entries, plus the two new interior-point-side-test
applications) both by hand-derivation (shown in the file) and by a fresh independent numeric spot-check
across the file's existing five diverse configurations (all consistent, all strictly positive as
predicted) — the numeric check is now a confirmation only, not a proof step.

Result: `results/imo-2026-02/approaches/synthetic-angle-chase-aklastar.md` now presents a complete
rigorous proof, Status `solved`, ending in ∎, with an explicit "Full proof" section per the file
contract. Promotable lemmas section lists the new Ray-betweenness sign lemma and the (trivial but
load-bearing) "unsigned angle = |directed angle|" fact as candidates for certification into
`lemmas/`.
