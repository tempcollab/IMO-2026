## imo-2026-03 (R15 — ESCALATION field)

Context: LOWER wall has NO live vehicle after R14 (6 lower families dead). UPPER = first-gap
pigeonhole `μ_{n+1}=min_i dist(a_i,R_{i-1}) ≤ u_n`, TRUE and (VALLEY-TIGHT) asymptotically tight,
no uniform margin. I ran the two mandated cheap-kills this round; one lower lever DIED, the upper
lever passed a preliminary gate. Field below: 1 UPPER advance (new tight lever), 1 LOWER new-framing
probe (gated), 1 LOWER revise (records a decisive refutation, NOT built).

---

breakpoint-vertex: revise/advance (UPPER)
Target: for every n, minimax D = u_n = 1/(2^{n+1}−1) (whole claim); this slug owns Xiang forces D ≤ u_n.
Technique: two-region valley split = crude-with-margin DEEP + exact boundary-continuation of the
certified dominant formula D = 2a₁−L across a₁ = L/2. Genuinely respects VALLEY-TIGHT (margin used
ONLY where margin provably exists — deep valley — never uniformly).
Skeleton:
  1. Import certified whole-tail-peel: dominant regime a₁≥L/2 gives EXACT D = 2a₁−L, tight at a₁=L/2. — certified.
  2. Fix cutoff c≥1. DEEP region a₁ ≤ L/2 − c·u_n: whole-tail difference L−2a₁ ≥ 2c·u_n is tree-realizable; one MATCH of the top tail piece into it (or an interior even-cancellation, value 0) drops the reachable leftover below u_n WITH margin. — deep-region margin lemma.
  3. BOUNDARY layer L/2 − c·u_n < a₁ < L/2: leftover |2a₁−L| = L−2a₁ < c·u_n is already O(u_n); show Φ ≤ (L−2a₁) + correction(a₂,a₃) ≤ u_n, an EXACT continuation (no margin) tight at the family A^{(n)}. — boundary-continuation lemma.
  4. Regions overlap-cover the whole valley at the chosen c ⇒ Prop UV ⇒ upper bound. — by R-UV/FGR (certified).
Key lemmas (claim + mechanism):
  - Deep-region margin — because a₁ ≤ L/2 − c·u_n forces L−2a₁ ≥ 2c·u_n, so a bounded (1–2 move) reduction of the whole-tail signed leftover has u_n-slack to spare; VALLEY-TIGHT's no-margin family is boundary-layer (its a₁ is exactly ~u_n/2 below L/2), so it never enters the deep region.
  - Boundary-continuation — because D = 2a₁−L is the certified EXACT dominant value and is continuous across a₁ = L/2; in the valley its absolute value L−2a₁ is O(u_n) in the layer, and A^{(n)} (a₁ = 2^n/(2^{n+1}+1)) is the interpolant's fixed point giving Φ = u_n·(2^{n+1}−1)/(2^{n+1}+1).
Open gaps: step 3 correction term (the R14 tied face is 14-dim at n=4 — the continuation must be tight on the WHOLE face, not just A^{(n)}); the self-consistent cutoff c (steps 2+4).
Cases to cover: deep region; boundary layer; and confirm the two cover with no valley profile escaping (G3).
Watch out for: MANDATORY exact sympy/Fraction gate at n=3,4,5 BEFORE prose — (G1) deep margin bounded < 1 and NOT shrinking to 0 as n grows (structured+adversarial, not random — random misled R11); (G2) boundary interpolant ≤ u_n tight on A^{(n)} AND on {16,8,4,3,2}/33; (G3) overlap-cover. If G1 fails (deep margin → 0 with n), the split collapses to the full tight problem and the lever dies — report and STOP, no fake proof. Do NOT use the refuted mass-telescope (per-piece charge against Σaᵢ) for the deep bound; use a bounded-move argument.
  [Preliminary R15 cheap-kill, RANDOM valley, exact Φ: DEEP worst Φ/u_n = 0.559 (n=4) / 0.368 (n=5); BOUNDARY worst 0.730 / 0.326. Green light — margin deep, tight at boundary — but structured/exact gate still required.]

---

gen-func-transform: new (LOWER) — GATED escalation probe
Target: for every n, minimax D = u_n (whole claim); this slug owns Liu's guarantee D ≥ 1 on any ≤n-cut refinement of C_n (⟺ GAP MID-core μ{g odd} ≥ 1).
Technique: global Z-transform Z(z)=∫₀^L z^{g(t)}dt of the certified parity-measure, evaluated at z=−1 (roots-of-unity/character filter, crux aimo-0155). A genuinely different OBJECT from all 6 dead lower families (a transform of the whole config, not vertex/word/matching/running-potential).
Skeleton:
  1. Z(1)=L, Z'(1)=∫g=1 (Lemma MID b), Z(−1)=L−2μ{g odd} ⇒ MID-core ⟺ Z(−1) ≤ L−2. — Lemma MID + character identity.
  2. Two-band split of Z_n(−1) via certified ONE-REC/TB: B=F_B⊔B_B, top band (L/2,L), bottom band (0,L/2). — certified.
  3. [GATE — make-or-break] Z_n(−1) = Φ(F,F_B; Z_{n-1}(−1)|_{(0,L/2)}), a clean parity-controlled combining rule. — UNVERIFIED.
  4. IH Z_{n-1}(−1) ≤ L/2−2 + monotone Φ ⇒ Z_n(−1) ≤ L−2. — by step 3.
Key lemmas (claim + mechanism):
  - The step-1 identity is CERTIFIED-MID REPACKAGING by itself (closes nothing) — stated honestly.
  - The ONLY non-repackaging content is step-3 recursion — because dyadic self-similarity (ONE-REC/TB) MIGHT let the top-band character value combine multiplicatively with the sub-ladder transform; if it does NOT, the cross term is exactly the dead SPLIT cross-term μ(O_F∩O_B).
Open gaps: step 3 (the entire content). The R15 genfunc explorer could NOT find the recursion and flagged strong repackaging risk.
Cases to cover: the combining rule must hold for all two-band splits incl. non-canonical cross-group vertices (R14: minimizer need not be one-fragment-per-scale).
Watch out for: MANDATORY exact sympy gate FIRST — does Z_n(−1) obey a clean two-band recursion carrying the IH (test n=3,4,5 incl. tight {8,8,4,4,3,2,1,1} and cross-group F={6,6,4})? If NO → report refutation and STOP (repackaging of MID/TB, retire the slug). No fake proof. If bounding Z_n(−1) needs τ-derivative machinery it inherits the dead scalar-reserve κ-unbounded failure — check early.
  [HONEST assessment: this is a diversity bet because the LOWER wall has zero vehicles. Its value is a fast decisive gate, not an assumed proof. Reviewer may prefer to HOLD it if it judges the repackaging risk decisive; I open it so the empty wall has something concrete to test.]

---

induction-peel: revise (LOWER) — records a decisive REFUTATION; NOT nominated for build
Target: whole claim minimax D = u_n; this slug owns the recursive-peel route.
Outcome this round: the R15 recursion-explorer's merge/budget-domination lever for Case II (|F|≥3) —
"merge two top fragments, reallocate the freed cut to the tail, D never increases, induct down to the
solved |F|=2 floor" — was adversarially gated by me and DIED on two independent grounds:
  1. Per-config monotonicity FALSE: over n=3,4 (600 configs, ~600 reallocations/merge-pair) the claim
     "some merge+realloc gives D' ≤ D₀" fails 9.2% (worst excess 2.65); coarser n=3,4,5 sweep failed
     14.5%. The freed tail cut cannot reliably reverse merge's D-increase (round-8 fact: merge raises D).
  2. Structural: merging two fragments (each ≤2^{n-1}) generically yields F_i+F_j > 2^{n-1} = Case (I),
     whose residual is the still-OPEN critical band of (L⋆) — NOT the solved |F|=2 bisection. The
     reduction lands in the open case, doubly broken.
Recorded in §3.5 of the approach file as a dead end (7th dead lower lever). The global fact
"min_{Case II} D = 1 only in the |F|=2 limit" stays TRUE but is NOT provable by a local merge — it
needs the same still-open Gap-Interleaving exchange as the critical band. This slug has NO new closing
lever this round; keep it live (its certified machinery PEEL/SPLIT/ONE/TB/band-decomposition and the
proven sub-cases all stand), do NOT build the merge.

---

BUILD SET (nominations): breakpoint-vertex, gen-func-transform
- breakpoint-vertex — UPPER, boundary-continuation two-region lever; builder runs the exact gate
  G1/G2/G3 FIRST, then prose only if it passes.
- gen-func-transform — LOWER, builder runs the two-band recursion GATE FIRST; proves the combining
  inequality if YES, reports refutation and STOPS if NO (no fake proof).
Both are GATED: an escalation round should yield either an advance or a clean decisive refutation.
induction-peel is a RETHINK-recording (merge lever refuted), NOT built. The LOWER wall remains the
field's structural risk: if the gen-func GATE returns NO (likely, per explorer), next round MUST seed
a lower framing from a genuinely new object class — the transform, vertex-polytope, word, matching,
and potential objects are all now exhausted.
