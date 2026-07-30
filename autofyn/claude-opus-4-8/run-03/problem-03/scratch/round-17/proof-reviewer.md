# Proof-reviewer — imo-2026-03 (Round 17)

Two built slugs reviewed. No APPROVE; problem stays `partial`. No lemma certified (the one candidate
is a trivial corollary of an already-certified lemma). Both builders' self-recorded Status is HONEST
and matches my independent findings.

---

## scale-origin-layercake (LOWER, new) — Verdict: RETHINK  (Status: unsolved / dead-end)

Builder claim: the make-or-break per-(i,j) scale-of-origin cap `Σ_i α_{i,j} ≤ Σ_i β_{i,j}` is FALSE
(~50%), so the layer-cake × scale-of-origin lever is the 10th dead lower lever. **VERIFIED — the kill
is legitimate, not a mis-formulation and not a dressed tautology.**

Independent reconstruction (`/tmp/verify_scale.py`, exact `Fraction`, my own tagging code, n=4,5,6):
- **(★) holds:** `Σ_i μ{g≥2i} ≤ Σ_i μ{g≤1−2i}` — 0 failures / 330 refinements. Certified-true confirmed.
- **Tagging is loss-free:** `Σ_{i,j} α_{i,j} = LHS(★)`, `Σ_{i,j} β_{i,j} = RHS(★)` — 0 violations.
  So the bookkeeping is faithful (α always opened at a genuine B-value, β closed at one).
- **Per-scale cap `Σ_i α_{i,j} ≤ Σ_i β_{i,j}` is genuinely FALSE and worsens with n:**
  max-scale pick 12/93, 27/119, 48/118 (13% → 23% → **41%**); min-scale pick 21/93, 43/119, 57/118
  (23% → 36% → **48%**). Worst deficit 3 / 6 / 10 across n=4,5,6 — growing with n, consistent with the
  builder's "deficit up to ≈2^j" (my more restrictive budget gives lower rates than the builder's
  ~50%/9000, but the same growing-failure signature and the same conclusion).

The logic is sound: any scale-*local* cap family (both sides at the same scale j) summing to (★) must,
by telescoping over the level index i at fixed j, imply the per-scale statement — and that statement
is numerically false. Loss-free-but-strictly-false is a genuine refutation (the local aggregate is a
false STRENGTHENING of (★)), not a triviality. Cross-scale lending is real at the coarsest (scale)
granularity, so no level-shift/same-scale repair survives. The whole scale-of-origin lever is dead.

Route: RETHINK → back to the outliner. **10th dead lower lever.** The negative fact NO-SCALE-LOCAL-CAP
is correct as recorded; it is a dead-end record, not a promotable lemma (correctly not proposed for
certification). Do not re-open any per-(g-level, dyadic-scale-of-origin) local cell cap.

## breakpoint-vertex (UPPER, advance) — Verdict: CHANGES REQUESTED  (Status: partial, live leader)

Builder claims: (1) full-tree 2nd-moment probe DEAD (8th dead upper mechanism); (2) G1 refutes the
"0.34–0.56 margin" premise for the deep interior AS DEFINED; (3) G2 smoothing move non-monotone;
(4) sharpening `Φ ≤ min_{S⊆tail}|a₁−Σ_S|` localizes the crux. **All VERIFIED; WTC intact.**

- **G1 (VERIFIED, this changes the UPPER state).** `/tmp/verify_upper.py`, exact `Fraction`, full
  `Φ = min_{∅≠T} descKK(T)`. The tight family `A^{(n)}` sits exactly on the deep-interior boundary
  `a₁ = L/2 − u_n/2` with `Φ/u_n = (2^{n+1}−1)/(2^{n+1}+1) → 1`. Perturbing `a₁` just below the
  boundary into the deep interior: `Φ/u_n = 0.881 / 0.938 / 0.968 / 0.984` at n=3..6 (a₁ = bnd −
  u_n/1000). So the deep interior AS DEFINED (`a₁ < L/2 − u_n/2`) contains a `u_n/2`-wide near-boundary
  sliver where `Φ/u_n → 1` — as tight as the closed boundary layer. The outliner's non-shrinking
  0.34–0.56 margin holds only in the strictly-deeper `a₁ ≤ L/2 − u_n`; the extremal/margin lever has
  no margin to exploit in the sliver. G1 refutation is correct.
- **G2 (accepted).** The "shift mass to a₁" move decreasing Φ on ~80% of deep profiles is consistent
  with the certified R3/VALLEY-TIGHT non-monotonicity warnings; no monotone smoothing to the a₁-boundary.
  The refutation is sound (I did not re-run all 500-profile counts but the direction matches the
  reviewer-certified non-monotonicity of the minimax and my G1 spot-checks).
- **Full-tree 2nd moment probe (accepted DEAD, 8th mechanism).** Ratio growing with n is the same
  rare-needle failure that killed both fixed-order second moments; recorded dead, no prose shipped. OK.
- **Sharpening `Φ ≤ min_{S⊆tail}|a₁−Σ_S|` (VERIFIED, NOT a new certifiable lemma).** Holds 0 fails /
  832 profiles, but is strictly loose 551/832 = 66% of the time. It is a direct one-line corollary of
  certified Lemma WTC applied to `T = {a₁}∪S` (`descKK ≤ |2a₁−Σ_T| = |a₁−Σ_S|`), then minimized. It
  adds NO proof content beyond WTC and duplicates the band-landing idea. **Rejected for certification**
  — per the builder's own flag and the standing rule against certifying reformulations of certified
  lemmas. It is recorded as a useful reframing that narrows the residual, not a standalone lemma.

Net: the R17 deep-interior extremal/smoothing LEVER is dead, but the APPROACH stays live — WTC closes
the boundary layer exactly (intact), and the residual is now sharply localized to the near-boundary
sliver + the single-target subset-sum-density statement. Modest but genuine localization progress → the
gap to close: **prove `Φ ≤ u_nL` in the near-boundary sliver `a₁ ∈ (L/2−u_n, L/2−u_n/2)` where
`Φ/u_n → 1`, i.e. that some tail subset sum `Σ_S` lands within `u_nL` of `a₁` (an EXACT argument, no
margin available).** Do NOT re-attempt a margin/crude bound in the sliver (G1 proves it impossible),
nor any WTC-extension/single-anchor/constructive-selection bound (dead R16).

---

## Lemma certification
- Candidate "Corollary WTC-SUBSET" (`Φ ≤ min_{S⊆tail}|a₁−Σ_S|`): **REJECTED** — correct but a trivial
  one-line corollary of certified WTC (0 new proof content, strictly loose 66%); duplicates
  band-landing/WTC. Not admitted to `lemmas/`.
- No other lemma proposed. `lemmas/` unchanged (30 certified).

## Recorded outcomes
- scale-origin-layercake → dead-end (10th dead lower lever).
- breakpoint-vertex → partial (lever refuted, WTC intact, residual localized; stays live leader).

current.md `## Status` updated (stays `partial`; R17 summary added). No `## Full proof` written.
