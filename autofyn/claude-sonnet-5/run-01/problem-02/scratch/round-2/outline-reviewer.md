## imo-2026-02 — outline review, round 2

### Shared reformulation check (applies to synthetic, inversion, coordinate-groebner)

The outline's headline reduction — for AB≠AC, `OM=ON ⟺ A* ∈ circle(AKL)`, where
`A* = A + (A' − A₀)` (A'=midpoint BC, A₀=foot of altitude from A) — is **not just asserted**: the
coordinate explorer derived it as an exact sympy symbolic identity, `det_concyclic(A,K,L,A*) =
(A'x − Ax)·myexpr` where `myexpr` is exactly `Re(O) − target` up to a nonzero denominator. I
re-derived the term counts/degrees independently (see below) and they check out. This part of the
reformulation is solid and each approach file cites it correctly. Good.

### Approach-by-approach verdicts

**synthetic-angle-chase-aklastar — CHANGES REQUESTED.**
- Technique is right (directed-angle chase is the standard tool for this kind of concyclicity, KB
  "Synthetic toolkit"), the reformulation is justified as above, and the skeleton correctly
  identifies the actual open content (step 5, closing `∠(AK,AL) ≡ ∠(A*K,A*L)`) rather than hiding
  it behind "it follows." Explorers already killed the tempting shortcuts (spiral-similarity
  centers at K/L, isogonality of AK/AL, AA* as bisector of ∠KAL) — good that the outline explicitly
  tells the builder not to retry these.
- **Gap in the isosceles fallback.** The outline's AB=AC handling ("swap B↔C, M↔N forces K↔L … so
  O lies on the axis") is not yet a proof. I checked: the three hypotheses ARE symmetric under
  swap B↔C,K↔L,M↔N,A-fixed (hyp1 is self-symmetric; the swap sends hyp2 to hyp3). But that only
  shows the *set* of valid (K,L) is closed under the swap — it does not by itself show a *given*
  valid (K,L) is fixed by the swap (i.e. K = reflect(L)), which is what's needed to put O on the
  axis. I numerically solved the isosceles case on a test triangle (A=(2,3),B=(0,0),C=(4,0)) at
  several α and from several different fsolve starting guesses — every solution found was in fact
  the mirror-symmetric one (K=reflect(L)) — consistent with the outline's claim, but this is only
  numeric evidence for uniqueness, not a proof that no asymmetric branch exists. **Required fix:**
  either prove that the isosceles case forces K=reflect(L) (e.g. via the 1-parameter-family
  structure — the family should collapse to the symmetric branch when AB=AC), or avoid the
  uniqueness question and directly re-derive OM=ON via the coordinate route (`myexpr=0`, which
  never degenerates at AB=AC per the coordinate explorer) for this one case as a fallback — flag
  this explicitly to the builder as an acceptable substitute if the symmetry argument doesn't close
  cleanly.

**inversion-at-a-collinearity — CHANGES REQUESTED.**
- Genuinely different formal target (linear collinearity vs 4-point concyclicity) and a legitimate
  KB technique (inversion). The base reformulation is inherited correctly. The listed risk (angle
  distortion under inversion away from the center) is real and correctly flagged as the main way
  this could go wrong — good that the outline warns the builder not to assume angles off-center are
  preserved.
- **Same isosceles gap as the synthetic approach** (identical fallback text, same missing
  uniqueness justification) — same required fix applies here.
- **Additional risk not fully priced in:** step 3/4 (translating all three hypotheses through the
  inversion-angle-distortion formula, then closing a Menelaus-type collinearity) is currently just
  "likely provable" — this is the single largest unclosed gap of the whole field and is more
  speculative than the coordinate route's mechanical fallback. Keep it in the population (it's a
  real alternate route, not a duplicate), but the builder should time-box this and fall back to
  reporting partial progress if the distortion-formula translation gets unwieldy, per the outline's
  own risk note.

**coordinate-groebner-elimination — APPROVE.**
- Sound and the most mechanically de-risked of the three: I independently reproduced the
  polynomial setup (bilinear cross/dot conditions e1, e2, and the degree-3-in-(tK,tL) target
  `myexpr`) with sympy and confirmed the term counts (e1: 48 terms, e2: 29, myexpr: 65) are large
  but tractable for a CAS — this is a real, checkable computation, not a hopeless blow-up.
- Correctly sidesteps the AB=AC degeneracy entirely (myexpr never divides by (Ax−A'x)), which is a
  genuine structural advantage over the other two approaches — no separate isosceles case needed.
  This should be highlighted, not just mentioned in passing.
- The rigor-rule reminder in the outline (must show explicit cofactors/resultant steps, not just
  "sympy says 0") is correctly present and should be enforced by the reviewer at build time.

**isosceles-locus-direct — RETHINK, correctly excluded from the outliner's build set.**
- The outliner's own outline flags this as the least-derisked approach and tells the builder to
  check the key mechanism "first" before investing further. I ran that check myself: for a scalene
  test triangle (A=(1.3,3.1), B=(0,0), C=(4,0)) I numerically solved for a valid (K,L), built
  circle(AKL), and found the **second intersection of line AM with circle(AKL)**. Result: this
  point is `X ≈ (0.269, 0.640)`, and it is **not** K, not L, not B, not M, not N (checked distances:
  all nonzero, none negligible — e.g. |X−K|≈0.33, |X−B|≈0.69, |X−M|≈0.99). Same negative result for
  the second intersection of line AN with circle(AKL). So the load-bearing idea of this approach —
  "hypothesis (iii) pins down the second intersection of AM with circle(AKL) as a nameable point" —
  is **empirically false**, not merely unverified. Since the entire mechanism (steps 3–4 of the
  skeleton) depends on identifying that point, this approach cannot be built as outlined.
- **Correct call by the outliner to exclude it from the build set.** Do not register it as an
  approach this round (it fails the "sound skeleton" bar — the named mechanism doesn't produce the
  claimed fact). If revisited later, it needs an entirely different way to compute pow(M,circle(AKL))
  that doesn't rely on identifying the second AM-intersection as a named point (e.g. via a length
  computation instead of a point-identification); as written, RETHINK.

### Diversity check (single-gap-trap)

All three build-set approaches ultimately target the same underlying algebraic fact (equivalent to
`myexpr=0` / "A,K,L,A* concyclic"), reached via different mechanisms — direct angle chase, inverted
angle chase, and pure algebra. This is a **moderate** diversity concern per CLAUDE.md: if the
"correct auxiliary idea" needed to close the concyclicity in the direct picture doesn't exist (i.e.
the fact genuinely requires more than base isosceles-angle substitution), the synthetic and
inversion approaches could both stall on the same underlying obstruction, just phrased two ways.
The coordinate-groebner-elimination approach is the field's real insurance policy here: it is
mechanical and does not depend on finding "the right" synthetic idea, so it should NOT be dropped
even if it looks less elegant. If both synthetic and inversion stall again next round on
essentially the same identity, the orchestrator should have the next outliner introduce a genuinely
different framing (e.g. trigonometric-form Ceva/Menelaus, or a moving-points/degrees-of-freedom
argument exploiting the confirmed 1-parameter family structurally) rather than a third variant of
the concyclicity chase.

### Ranking

Registered this round (first real round, cold-start Elo 1500 each): synthetic-angle-chase-aklastar,
inversion-at-a-collinearity, coordinate-groebner-elimination. isosceles-locus-direct was NOT
registered (RETHINK — its named mechanism is checked and false).

Comparisons submitted: coordinate-groebner-elimination beats inversion-at-a-collinearity (more
concrete, feasibility independently confirmed, no isosceles special-case needed); synthetic-angle-
chase-aklastar beats inversion-at-a-collinearity (same reformulation, less speculative closing
step — no inversion-angle-distortion risk); synthetic-angle-chase-aklastar and coordinate-groebner-
elimination drawn (both have a well-defined, non-trivial, but plausibly closeable remaining gap).
Resulting Elo: coordinate-groebner-elimination 1517, synthetic-angle-chase-aklastar 1514,
inversion-at-a-collinearity 1469.

build set: synthetic-angle-chase-aklastar, coordinate-groebner-elimination, inversion-at-a-collinearity
