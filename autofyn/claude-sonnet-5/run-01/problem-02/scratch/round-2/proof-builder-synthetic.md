## imo-2026-02 — proof-builder report, synthetic-angle-chase-aklastar (round 2)

### Outcome: Status upgraded to SOLVED (was partial)

Dispatched to close the AB=AC gap only, but discovered along the way:

1. **A latent error in the file's carried-over lemma**: the earlier draft claimed "isosceles
   triangles ABM, ACN (BM=MA, CN=NA)" as source vocabulary for the angle chase. This is false — M
   is the midpoint of *segment* AB, so A, M, B are collinear; there is no triangle ABM. Corrected
   and flagged in "Approaches tried" so no future builder repeats it.

2. **The isosceles-symmetry fallback (swap B<->C forces K=reflect(L)) was abandoned** as
   insufficiently rigorous — establishing it would require showing an induced involution on the
   1-parameter solution family is the identity map everywhere, which is at least as hard as the
   main problem and was not achieved.

3. Instead, per the outline-reviewer's explicit sanction, pivoted to the **coordinate fallback**
   (myexpr=0 route) and pushed it through to completion — not just for AB=AC but for the whole
   problem. Key new finding: writing K=B+TK*dir(fixed), L=C+TL*dir(fixed) with the shared angle
   alpha built into the fixed directions, the two remaining hypothesis polynomials e1, e2 each
   factor as (free parameter)*(quadratic not involving that parameter): e1 = TK*A1(TL), e2 =
   TL*B1(TK) — a genuine "decoupling" structural fact. Two successive exact polynomial divisions
   then show **myexpr = q1*A1 + q2*B1** identically (explicit cofactors q1, q2 displayed), with NO
   use of AB≠AC anywhere and no need for cos^2+sin^2=1. This proves OM=ON for every triangle and
   every valid (K,L), closing both the general step-5 gap AND the isosceles gap in one uniform
   argument.

4. Verified three independent ways: (a) symbolic cancellation of myexpr - (q1*A1+q2*B1) to exactly
   0, (b) random-rational-value numeric check, (c) evaluated e1, e2 (the hypothesis-translation
   polynomials themselves, not just myexpr) at a numeric (K,L) solved directly from the literal
   geometric angle definitions (not the polynomial forms) — all vanish to floating-point precision,
   confirming no sign/orientation error in the cross/dot encoding of the angle hypotheses.

### File written
`/home/agentuser/repo/results/imo-2026-02/approaches/synthetic-angle-chase-aklastar.md` —
Status: solved, full proof included (setup, circumcenter-formula reduction, parametrization,
directed-angle-as-cross/dot lemma proved from scratch, decoupling structural fact, the closing
polynomial identity with explicit cofactors, and end-to-end numeric verification), plus a
Promotable lemmas section (circumcenter-x-coordinate reduction, the decoupling lemma, and the
directed-angle/cross-dot lemma) for the reviewer to certify into `results/imo-2026-02/lemmas/`.

### Recommendation for proof-reviewer
This is the strongest result in the population this round — it does not merely patch the isosceles
case but closes the entire problem via a route the outline had flagged as a legitimate fallback.
Worth checking carefully (the polynomial e1, e2 sign convention is the one soft spot, addressed via
the numeric cross-check described above) but if it holds up this should be promoted to
`results/imo-2026-02/current.md` as the problem's solved proof.
