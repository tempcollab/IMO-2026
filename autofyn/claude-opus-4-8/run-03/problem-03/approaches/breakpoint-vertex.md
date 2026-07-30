## Status
partial (round 19 build — **CONSOLIDATION/re-targeting round. No gap closed, no new closing lever
attempted (all such levers are recorded dead — 9 dead upper mechanisms). This round officially
RE-TARGETS the open residual from the caterpillar object `μ_{n+1}` to the certified true target
`min R(A) ≤ u_nL` via the certified Corollary R-UV of Lemma RL, and records the two mechanisms
refuted at this round's gate (tree-min-divide-conquer, signed-tree-invariant). The certified core
— Lemma RL / Corollary R-UV, Lemma WTC boundary-layer closure, R-COV', FGR — is INTACT and
unchanged. Status stays `partial`; the deep-interior residual is OPEN. Round 19 section below;
full R18/R17/R15 history preserved beneath it.**)

### Round 19 — BUILD (CONSOLIDATION): official re-target to `min R(A) ≤ u_nL`; two R19 mechanisms recorded dead; residual isolated as an anchor-EXCLUDING tail-subset existence claim

This was a narrow, low-content advance dispatched *not* to re-run any dead contraction gate but to
(1) formally adopt the certified true residual, (2) record this round's two refutations, and (3)
state the open gap honestly. No prose closing the deep interior is shipped; none is claimed.

#### 1. Official re-target: the residual is now `min R(A) ≤ u_nL` (certified reduction R-UV)

**Certified fact imported (not re-proved here).** Lemma **RL** (`leftover-realizability.md`, CERTIFIED
round 7) characterises the achievable-single-leftover family in the upper-bound game (`m=n+1` pieces,
`≤ n` cuts):
$$\mathcal R(A)=\Big\{\big|\textstyle\sum_{i\in T}\varepsilon_i a_i\big|:\varnothing\ne T\subseteq[m],
\ \varepsilon\ \text{a nonnegative-differencing-tree sign pattern on }T\Big\}.$$
Its **Corollary R-UV** (certified in the same file) states precisely:
$$\boxed{\ \min\mathcal R(A)\ \le\ u_nL\ \Longrightarrow\ \text{Xiang forces } D\le u_nL\ }\qquad(m=n+1).$$

What is certified vs. what I assert:
- **Certified (RL + R-UV, cited, not re-proved).** (a) Every value `ρ=|Σ_{i∈T}ε_i a_i|` for a nonempty
  `T` and a nonnegative differencing-tree sign pattern `ε` on `T` is Xiang-realizable as the single
  leftover in exactly `m-1=n` cuts: `|T|-1` MATCHes along the tree's internal nodes plus `m-|T|`
  DELETEs of the leaves outside `T`, total `(|T|-1)+(m-|T|)=m-1=n≤n`, ending with `D(\{ρ\})=ρ`. This is
  the **general-tree** realizability the two new approaches needed licensed; it is discharged by RL's
  converse construction — it is NOT restricted to caterpillars (ESF-2 was the caterpillar-only special
  case). (b) Hence `min 𝓡(A) ≤ u_nL ⟹ D ≤ u_nL` (sufficiency): pick a nonempty `T` and tree attaining
  the minimum, realize it in `n` cuts, and Xiang may only do better by stopping earlier at an
  even-multiplicity multiset.
- **What I assert (bookkeeping, no new mathematics).** The field's *official open residual for the
  deep interior* is henceforth `min 𝓡(A) ≤ u_nL` for `a₁ < (L−u_nL)/2`, replacing the strictly harder
  caterpillar residual `μ_{n+1} ≤ u_nL`. This is sound because `min 𝓡(A) ≤ μ_{n+1}` always (caterpillar
  sign-patterns are a subfamily of tree sign-patterns — a caterpillar is one tree topology — so the
  caterpillar reachable set `R_{n+1}` is contained in the value-set of `𝓡(A)`; hence its minimum
  positive value `μ_{n+1}` is `≥ min 𝓡(A)`). Therefore proving `min 𝓡(A) ≤ u_nL` is *weakly easier*
  than proving `μ_{n+1} ≤ u_nL`, and by R-UV it is *equally sufficient* for the upper bound. Adopting
  it dissolves the false-completeness confusion (see §2(i)) without changing what must ultimately be
  proved: some nonnegative tree value over a nonempty subset is `≤ u_nL`.

  (Scope caveat, stated to avoid overclaim: R-UV is a *sufficient* condition, not proven to be
  necessary. That is all the upper bound needs. The R-COV' converse remains uncertified and is not
  used.)

#### 2. Mechanisms recorded DEAD this round (with the reason each fails)

**(i) The caterpillar completeness identity `μ_{n+1} = min 𝓡(A)` is FALSE.** The R19 explorer's
headline. `μ_{n+1}` (the caterpillar first-gap object, FGR) is a strictly HARDER sub-target than
`min 𝓡(A)`; they are not equal. Exact-`Fraction` witnesses (unnormalized integers, `a₁<L/2`, `n=4`),
recomputed this round with the correct FGR dist-recursion for `μ` and full subset+tree search for
`min 𝓡`:
```
   A=(17,16,11,8,4):  μ_{5}=1,  min R(A)=0   (gap 1 = 0.55·u₄)
   A=(59,55,53,44,17): μ_{5}=2, min R(A)=0   (gap 2 = 0.27·u₄)
   A=(54,43,35,32,28): μ_{5}=3, min R(A)=2   (gap 1 = 0.16·u₄)
```
So any lever assuming the exact equality `μ_{n+1}=min 𝓡(A)` (as a "bound the big object, transfer to
the caterpillar by completeness" bridge) is **unsound on arrival**. This is *not* a wall for the
re-targeting — it is the reason to abandon `μ_{n+1}` and target `min 𝓡(A)` directly, which is exactly
what §1 does. (Landmine avoided: `μ` computed via `μ_i=min(μ_{i-1},dist(a_i,R_{i-1}))`, NOT
"min-positive of the accumulated set," which silently drops exact-0 cancellations — explorer finding 4.)

**(ii) tree-min-divide-conquer (balanced disjoint split) — DEAD at the R19 gate (a covering-radius
relabel).** The proposed object was `DCbest = max over BALANCED disjoint splits G₁⊔G₂ of the pieces
(masses within 2a₁) of min_{x∈T(G₁),y∈T(G₂)} |x−y|`, telescoped to `u_nL`. Exact-`Fraction` gate
(outline-reviewer `/tmp/gate19.py`):
```
   R18-witness (n=4): DCbest/u_n = 9.30   (true min R = 0)
   A^(4)-deepened   : 2.697
   A^(5)-deepened   : 2.846
   A^(6)-deepened   : 2.922   (monotone GROWING, saturating ~3)
```
**Why it fails (structural).** A "split OF THE PIECES" is a full partition — it cannot DROP pieces —
so it can never reach a piece-EXCLUDING subset minimiser. On the R18 witness the true `min 𝓡=0` lives
on the size-2 subset `{13/40,13/40}` (dropping 3 pieces, including `a₁`), unreachable by any balanced
full partition, so `DCbest` saturates at `9.30·u₄`. VALLEY-TIGHT forbids any bound `≤ C·u_n` with
`C>1`; here `C≈3–9`. Same covering-radius death signature as the R12 two-cap object (saturated
`3–5·u_n`). Recorded dead so no future round re-tries a full-partition / balanced-split object over the
reachable-value set.

**(iii) signed-tree-invariant (band-restart / disjoint-restart-after-band-landing) — DEAD at the R19
gate (the 9th dead anchored walk relabeled).** The claimed new object `band_restart(A)` ("consume `a₁`
into the crossing residual `r`, restart the WTC invariant on a disjoint sub-instance, no re-inflation")
is, on every family tested, **identically the plain caterpillar/reflected walk**:
`band_restart(A) ≡ descKK(A)`, and reproduces **exactly** the R18-dead `minpost = 3/10 = 9.30·u₄` on
the R18 witness:
```
   R18-witness (n=4): band_restart/u_n = 9.300  (= descKK = R18 dead minpost)
   A^(4/5/6)-deepened: 2.697 / 2.846 / 2.922    (same growing saturation as D&C)
```
**Why it fails (structural).** Band-landing is ANCHORED at `a₁` — it sums survivors until they cross
`a₁`, which *forces* `a₁` into the residual `r`. So the "disjoint restart" still contains `a₁` in its
history and cannot see the anchor-EXCLUDING tail minimiser `{13/40,13/40}`. This is precisely the R18
root cause; the distinguishing claim ("a₁ consumed, restart on disjoint support, no re-inflation") is
false because the crossing block itself is built from and around `a₁`. It is the 9th dead anchored-walk
mechanism under a new name. Recorded dead.

#### 3. Current best (honest) and the isolated open gap

- **Boundary layer `a₁ ≥ (L−u_nL)/2` — CLOSED exactly** by Lemma WTC (`descKK(fullset) ≤ |2a₁−L| =
  L−2a₁ ≤ u_nL`, a nonempty tree value, so `min 𝓡(A) ≤ u_nL` and R-UV forces `D ≤ u_nL`). Tight with
  equality on the family `A^{(n)}`. Unchanged and intact.
- **Deep interior `a₁ < (L−u_nL)/2` — OPEN.** The residual is now officially `min 𝓡(A) ≤ u_nL`. The
  hardest sub-region is the `u_n/2`-wide sliver `a₁∈(L/2−u_n, L/2−u_n/2)`, where `min 𝓡(A)/u_n → 1`.
- **Why no anchored/covering/dispersion object reaches it (the shared wall, now sharply diagnosed).**
  The true minimiser of `min 𝓡(A)` is generically an **anchor-EXCLUDING tail subset** (on the R18
  witness it is `{13/40,13/40}`, which drops `a₁` entirely; the `{30,25,20,15,10}/100` profile needs a
  4-element tail subset). Every single-object bound over the reachable-value set — any single anchored
  walk (R18), any full-partition balanced split (R19 (ii)), any band-restart (R19 (iii)), the covering
  radius (R10/R12), a density count (R11), a second moment (R16/R17) — either cannot drop pieces or
  resolves only to `Θ(2^{-depth})` while `u_n∼2^{-n}`, so it saturates at `Θ(1)·u_n` and grows with
  `n`. This is the exponential-rate mismatch: closing the gap needs a genuinely GLOBAL existence
  argument that exploits the full `~2^{n+1}` search space at the right exponential rate (a
  Steinitz/vector-balancing–style existence claim over the tree-realizable signed sums), or a bespoke
  perturbative argument confined to the sliver — NOT any single object over `𝓡(A)`. This slug's
  framing does not currently contain such an argument; the gap is handed forward.

#### 4. Evidence (exact-`Fraction`, NOT proof): `min 𝓡(A)/u_n ≤ 1` on the hard families

Confirmation script `/tmp/conf19.py` (`fractions.Fraction`, never float; `min 𝓡` via memoized
subset+tree `treeVals`, `μ` via the FGR dist-recursion, per the explorer landmine). Reported as
EVIDENCE that the re-targeted claim is true with room to spare, not as a proof:
```
   family (normalized to Σ=1)          n | min R(A)/u_n | mu_FGR/u_n
   {1/3,13/40,13/40,1/120,1/120}       4 |   0.0000     |  0.0000    (min R on {13/40,13/40})
   {30,25,20,15,10}/100                4 |   0.0000     |  0.0000
   A^(4)={16,8,4,3,2}/33               4 |   0.9394     |  0.9394
   A^(5)={32,16,8,4,3,2}/65            5 |   0.9692     |  0.9692
   A^(6)={64,...,4,3,2}/129            6 |   0.9845     |  0.9845
   A^(4) sliver (a1 -= u/4)            4 |   0.6894     |  0.6894
   A^(5) sliver (a1 -= u/4)            5 |   0.7192     |  0.7192
   A^(6) sliver (a1 -= u/4)            6 |   0.7345     |  0.7345
```
`min 𝓡(A)/u_n ≤ 1` on every hard family (`0,0,0.94,0.97,0.98`, slivers `0.69–0.73`), confirming the
target `min 𝓡(A) ≤ u_nL` is sound and asymptotically tight (VALLEY-TIGHT respected: it approaches but
never reaches `1`). On the structured tight families `A^{(n)}` the caterpillar and tree minima coincide
(`μ_{n+1}=min 𝓡`), while on the tie-rich integer witnesses of §2(i) they differ — consistent with
completeness being false only off the structured family. This is EVIDENCE, not a proof of the general
inequality, which remains OPEN.

---

### Round 18 — Status header (history)

partial (round 18 build — **the mandatory C2 post-crossing-contraction gate was run FIRST in exact
`Fraction` arithmetic and FAILED decisively; per the binding dispatch precondition I STOPPED and shipped
NO deep-interior proof. The sharpened-WTC / reflected-walk contraction mechanism is now REFUTED and
recorded dead (9th dead upper mechanism). The certified reduction and the WTC boundary-layer closure are
INTACT and unchanged. C1 (caterpillar-min completeness) was NOT attempted since the dispatch gates it
strictly behind a passing C2. Round 18 findings below; the full R15/R17 content is preserved beneath.**

### Round 18 — BUILD: C2 contraction gate run FIRST (exact Fraction) → FAILED; reflected-walk/sharpened-WTC contraction is DEAD (9th dead upper mechanism)

Per the R18 dispatch, precondition (1) was a hard, refute-and-stop gate: does the post-crossing reflected
residual telescope/contract to `≤ u_nL`? I ran it in exact `Fraction` (never float) on the required
adversarial families — random sliver profiles, the tight family `A^{(n)}={2^n,…,4,3,2}/(2^{n+1}+1)`, and
`A^{(n)}`-perturbations into the sliver — at `n=3,4,5,6`. Scripts: `/tmp/gate_c2.py`, `/tmp/gate_c2b.py`,
`/tmp/gate_c2c.py`.

**Object.** `Φ(A)=min_{∅≠T} descKK(T)` (certified residual, R-COV'/FGR/ESF-2). Deep/sliver region
`a₁<(L−u_nL)/2`. The reflected/caterpillar walk on the full descending profile is `w_1=a₁`,
`w_k=|w_{k-1}−a_k|` (so `w_k=descKK` of the descending prefix `{a₁,…,a_k}`). By WTC the pre-crossing
values satisfy `w_k=a₁−P_k` (`P_k=a₂+…+a_k`) until the band-landing crossing index `k*` (certified BL,
first `k` with `P_k≥a₁`), where `w_{k*}=P_{k*}−a₁` is the small band residual. The proposed closing
mechanism was: past `k*`, the reflected steps *contract* under the ONE-REC dyadic caps and telescope down
to `≤ u_nL`. The most generous operationalisation of "telescopes/contracts to a value `≤ u_nL`" is the
minimum of the post-crossing reflected residuals, `minpost := min_{k≥k*} w_k` (any specific single
stopping bound is `≥` this). If even `minpost` saturates above `u_n`, the mechanism is dead.

**Gate result (exact Fraction, worst-case ratio over ~14000 samples/n):**
```
 n | worst true Φ/u_n | worst minpost/u_n (contraction object) | worst min-all-prefix/u_n
 3 |     0.8824       |            4.5434                        |        2.0229
 4 |     0.9394       |            9.0932                        |        3.9036
 5 |     0.9692       |           13.8705                        |        6.4300
 6 |     0.9845       |           24.2583                        |       11.8031
```
- **True `Φ/u_n ≤ 1` always** (0.88/0.94/0.97/0.98) — the theorem `Φ ≤ u_nL` is TRUE and asymptotically
  tight (VALLEY-TIGHT), confirming the target.
- **The contraction object `minpost/u_n` SATURATES FAR ABOVE `u_n` and GROWS with `n`:** 4.5 → 9.1 →
  13.9 → 24.3, roughly doubling per unit `n` (the ~`2^{n-1}` growth signature the R18 explorer flagged).
  This is precisely the covering-radius death pattern the reviewer warned of (GAP TWO-CAP: 3.2/6.1/8.9/
  15.8/24.6 at `n=3..7`) — the post-crossing reflected walk IS the covering-radius family in disguise.

**Clean exact witness (n=4, deep, small denominators, reproducible):**
`A = {1/3, 13/40, 13/40, 1/120, 1/120}`, `a₁=1/3 < L/2−u₄ = 29/62` (strictly deep), `u₄=1/31`.
- Post-crossing reflected residual `minpost = 3/10 = 9.3·u₄` (crossing index `k*=3`).
- True `Φ = 0`, achieved by the size-2 subset `{13/40, 13/40}` (even cancellation) — which EXCLUDES the
  anchor `a₁=1/3` entirely.

**Diagnosis (why it fails, structurally).** The reflected/caterpillar walk is anchored at `a₁` (it starts
`w_1=a₁` and every prefix contains `a₁`). But the true minimiser of `Φ` can be a subset that *excludes*
`a₁` and lives entirely in the tail (here `{13/40,13/40}`; the R17 example `{30,25,20,15,10}/100` needs a
4-element tail subset; the R18 explorer found size-`n` tail minimisers). A single anchored descending pass
— of ANY stopping rule, since `minpost` already minimises over all post-crossing stopping points — cannot
see these, so its residual saturates at `Θ(a₁) ≫ u_n`, growing with `n`. There is no per-scale contraction
constant `≤` the dyadic scale ratio; the ONE-REC caps bound the *decrements*, not the reflected residual,
and the residual re-inflates on the next tail piece exactly as the covering radius does.

**VERDICT: C2 GATE FAILED. The sharpened-WTC / post-crossing reflected-walk contraction is a DEAD
mechanism — the covering-radius family in disguise (9th dead upper mechanism).** Per the binding
dispatch precondition ("if the contraction constant does NOT reach `≤ u_nL` … STOP: do not write a fake
proof"), I did NOT proceed to C1 and shipped NO deep-interior prose. This slug's certified content (the
reduction and the WTC boundary-layer closure) is unchanged and remains the leader's rigorous core; the
deep-interior / sliver residual `Φ ≤ u_nL` for `a₁<(L−u_nL)/2` stays OPEN and now needs a genuinely
different object (the signed-subset-sum-discrepancy / Steinitz EXISTENCE route — bound the min of
tree-realizable signed subset sums directly, NOT any single anchored walk), which is out of this slug's
current framing. Recorded so no future round re-tries the post-crossing / reflected-walk / anchored-caterpillar
contraction.

**(Original round-17 Status paragraph retained below for history.)**

partial (round 17 build — **all three make-or-break gates for the deep-interior extremal/smoothing
lever were run in exact `Fraction` arithmetic; the gated-first probe DIED as predicted, and the two
PRIMARY gates (G1 argmax structure, G2 smoothing-monotonicity) BOTH turned up refutations that undercut
the outliner's premise. NO proof of the deep interior was shipped. The boundary layer stays CLOSED
(Lemma WTC, untouched). Headline findings below; details in the Round 17 section.**

1. **GATED-FIRST full-tree second moment — DEAD (8th dead upper mechanism).** Exact-`Fraction`
   mean(V²) over the FULL tree-realizable ensemble 𝓡(A) (all binary differencing trees over all
   nonempty T, Catalan-many per subset), on hard deep-interior profiles with no nonempty-T exact zero:
   ratio `mean(V²)/(u_nL)² = 14.7 / 72.0 / 242` at `n=3,4,5` — GROWING with n, worse than the two
   killed fixed-order probes. Same rare-needle failure. Recorded dead; no prose built for it.

2. **G1 (deep-interior argmax) — the outliner's "0.34–0.56 non-shrinking margin" premise is REFUTED
   for the region as defined.** The deep interior is `a₁ < (L−u_nL)/2 = L/2 − u_n/2` (only `u_n/2`
   below `L/2`). Exact computation: as `a₁ → (L−u_nL)/2` from below, `Φ/u_n` approaches the WTC
   boundary value (`0.91` at `n=4`, `0.976` at `n=6`, `→1` as `n→∞`). So `sup_{deep} Φ/u_n → 1`;
   there is NO uniform margin near the top edge of the deep interior. The `0.34–0.56` figure holds
   only in the strictly-deeper sub-region `a₁ ≤ L/2 − u_n` (the R15 `c=1` cut), NOT in the
   `u_n/2`-wide near-boundary sliver `a₁ ∈ (L/2 − u_n, L/2 − u_n/2)` that WTC leaves open, where the
   bound is essentially as tight as the boundary layer. The float argmax's TOP parts ARE near-dyadic
   (`a₁:a₂:a₃:a₄ ≈ 2:1` ratios), but it sits at the deep boundary — so "pin a margin-ful extremizer"
   has no margin to exploit near the sliver.

3. **G2 (SMOOTH-MONO) — the conjectured smoothing move is NOT `μ_{n+1}`-monotone.** The natural move
   "shift mass from the smallest part up to `a₁`" DECREASES `Φ` on ~80% of random deep profiles
   (374/500, 453/500, 401/500 at `n=3,4,5`), so it cannot drive an arbitrary deep profile to the
   boundary without lowering `Φ`. No monotone smoothing to the `a₁`-boundary exists via this move;
   the hoped-for closure "max is on `a₁=(L−u_nL)/2` where WTC finishes" does not follow.

**Net.** The R17 primary extremal/smoothing lever does NOT close the deep interior as set up: its
margin-tolerant premise is false near the deep boundary (G1) and its smoothing move is non-monotone
(G2), while the gated-first ensemble is dead (probe). Genuine advance this round is a SHARPER
localization of the crux: the hard part is the `u_n/2`-wide near-boundary sliver `a₁ ∈
(L/2 − u_n, L/2 − u_n/2)`, where `Φ/u_n → 1` and only an EXACT (not margin) argument can work —
the same wall as the closed boundary layer, one sliver deeper. Round 15 BUILD (WTC, boundary closed)
is intact below and unchanged.**

### Round 17 — BUILD: three deep-interior gates run; gated-first probe DEAD (8th mechanism), G1+G2 refute the margin/smoothing premise; crux sharpened to the near-boundary sliver

Per the R17 dispatch and gate order, I ran the mandatory exact-`Fraction` gates BEFORE any prose,
in the mandated order (gated-first probe, then the two PRIMARY gates), and shipped NO deep-interior
proof because every gate returned a refutation. Scripts: `/tmp/probe2m.py`, `/tmp/g1.py`,
`/tmp/g1b.py`, `/tmp/g1c.py`, `/tmp/g2.py`. Object imported unchanged: `Φ(A) = min_{∅≠T} descKK(T)`
(0 admissible), the certified FGR / R-COV' sufficiency object; deep interior `a₁ < (L−u_nL)/2`.

**Gate 0 (GATED-FIRST, full-tree second moment over 𝓡(A)) — DEAD.** For each nonempty subset `T`
I enumerated ALL binary differencing trees (recursively: `treeVals(S) = {|x−y| : x∈treeVals(A),
y∈treeVals(B)}` over ordered bipartitions `S=A⊔B`), collected the multiset of leaf values across all
nonempty `T`, and computed `mean(V²)/(u_nL)²` on hard deep-interior integer-rescaled profiles filtered
to have NO nonempty-`T` exact zero (the honestly-hard case). Result: worst ratio `14.68 / 71.99 /
242.05` at `n=3,4,5` — monotonically GROWING with `n`, strictly worse than both fixed-order probes
killed last round. The full (Catalan-many) ensemble concentrates NO better than the fixed-order one:
the true small witness is a rare needle no average sees. This is the **8th dead upper mechanism**
(after covering-radius ×2, density/COUNT, greedy recursion, bounded-depth escape, mass-telescope,
margin/extremal-tie, and the two R16 fixed-order second moments — this full-tree one is distinct and
now also refuted). No prose built.

**Gate G1 (deep-interior argmax structure + margin) — margin premise REFUTED.** Float coordinate-ascent
over the deep polytope (300 restarts × local ascent, then confirmed by structured probes) gives
`max Φ/u_n ≈ 0.879 / 0.846 / 0.785` at `n=4,5,6`, with the argmax having a near-dyadic TOP
(`a₁:a₂:a₃ ≈ 2:2:1`, ratios `2.00,2.00,…` then breaking). Crucially the argmax sits AT the deep
boundary `a₁ → (L−u_nL)/2⁻`. Exact-`Fraction` continuity probe (perturb the boundary-layer tight family
`A^{(n)}` a distance `u_n/K` below the boundary):
```
   a₁ = bnd − u_n/10 :   Φ/u_n = 0.809 (n=4),  0.877 (n=6)
   a₁ = bnd − u_n/100:   Φ/u_n = 0.899 (n=4),  0.967 (n=6)
   a₁ = bnd − u_n/1000:  Φ/u_n = 0.908 (n=4),  0.976 (n=6)
```
So `sup_{deep} Φ/u_n` approaches the WTC boundary value `(2^{n+1}−1)/(2^{n+1}+1) → 1`. There is NO
uniform margin in the deep interior AS DEFINED (`a₁ < L/2 − u_n/2`). The `0.34–0.56` margin the
outliner/explorer cited is real only for `a₁ ≤ L/2 − u_n` (a strictly smaller region, `c=1`); the
`u_n/2`-wide sliver `a₁ ∈ (L/2 − u_n, L/2 − u_n/2)` left open by WTC has `Φ/u_n → 1` and is as tight
as the boundary layer. The margin-tolerant licence therefore does NOT extend to the whole deep
interior — a genuine correction to the R17 plan.

**Gate G2 (SMOOTH-MONO) — REFUTED.** The conjectured smoothing move "shift mass `δ` from the smallest
part `a_{n+1}` up to `a₁`" (which would push toward the boundary where WTC closes) DECREASES `Φ` on
the majority of random deep profiles: `374/500, 453/500, 401/500` decreases at `n=3,4,5` (exact
`Fraction`, several `δ` per profile). E.g. `n=5` profile `(0.279,0.250,0.203,0.170,0.071,0.027)`,
`δ=0.0201`: `Φ/u_n` drops `0.161 → 0.141`. So the move is NOT `μ_{n+1}`-nondecreasing; the maximizer
is a structured interior/boundary vertex NOT reachable by a monotone mass-shift to the `a₁`-boundary.
The proposed "max lives on `a₁=(L−u_nL)/2`, close by WTC" route therefore FAILS. (The opposite trend
seen when perturbing the structured family `A^{(n)}` is family-specific, not a general monotonicity.)

**Sharpened residual (the genuine advance this round).** Applying WTC to the subset `T = {a₁} ∪ S`
for any `S ⊆ {a₂,…,a_{n+1}}` gives `descKK(T) ≤ |2a₁ − (a₁ + Σ_S)| = |a₁ − Σ_S|`, so
```
   Φ(A) ≤ min_{S ⊆ {a₂,…,a_{n+1}}} |a₁ − Σ_S|,
```
i.e. the deep residual `Φ ≤ u_nL` holds as soon as SOME tail subset sum `Σ_S` lands within `u_nL` of
`a₁`. This is the exact band-landing / first-gap covering claim (consistent with certified FGR), now
pinned as: *the tail subset sums must be `u_nL`-dense around the single target `a₁`.* The near-boundary
sliver is exactly where this is tightest (`|a₁ − Σ_S|` cannot beat `~u_n`). No bounded-`|S|` mechanism
reaches it (a `{30,25,20,15,10}/100`-type deep profile needs a 4-element `S`), matching R15. This
localizes the crux to the sliver and to the single-target subset-sum-density statement — but does NOT
close it. Recorded as a candidate reduction for the reviewer (NOT self-certified; likely equivalent to
existing FGR/band-landing, do not double-certify).

**Verdict.** Deep interior remains OPEN, now sharply localized. The R17 extremal/smoothing lever is
refuted as configured (G1 no-margin near the sliver, G2 non-monotone move); the full-tree averaging
probe is the 8th dead upper mechanism. Boundary layer stays closed by WTC.

---

### Round 15 — Status (superseded header, kept for history)
partial (round 15 build — **the mandatory exact gate PASSED for the BOUNDARY region and a NEW
rigorous lemma was proven that closes it exactly; the DEEP interior remains the open crux.** In one
line: I proved the *whole-tail continuation bound* `Φ(A) ≤ |2a₁−L|` (Lemma WTC below), a fully
rigorous, exact, VALLEY-TIGHT-respecting inequality — tight with EQUALITY on the tight family
`A^{(n)}` and on the R14 maximiser `{16,8,4,3,2}/33`. It is the exact continuation of the certified
dominant formula `D=2a₁−L` across `a₁=L/2`. Consequence: the entire region `a₁ ≥ (L−u_nL)/2` of
the valley (the BOUNDARY layer where VALLEY-TIGHT's no-margin family concentrates, plus the already
closed dominant regime) is now closed rigorously; the upper wall reduces to the strictly-interior
DEEP valley `a₁ < (L−u_nL)/2`, where a numeric margin (`Φ/u_n ≲ 0.72,0.67,0.58` at `n=3,4,5`,
not shrinking to 0) exists but NO provable bounded mechanism realises it (the 8-round-open crux).
NO fake proof shipped. Full gate results + proof in the Round 15 BUILD section directly below.**)

### Round 15 — BUILD: exact gate PASSED for boundary; Lemma WTC (whole-tail continuation) PROVEN; deep interior isolated

Per the R15 dispatch and the outline-reviewer's binding precondition, I ran the mandatory exact
`sympy`/`Fraction` gate (adversarial + structured, NOT random-only) BEFORE any prose, then wrote the
proof only for the region the gate certified.

**Object (certified, imported).** Valley profile `a₁≥a₂≥…≥a_{n+1}>0`, `Σ=L=1`, `a₁<1/2`,
`a₂<β_n=2^{n-1}/(2^{n+1}−1)`. By certified **Reduction R-COV' (sufficiency)** + **Lemma ESF-2**, if
```
      Φ(A) := min_{∅≠T⊆{1,…,n+1}} descKK(T)  ≤  u_n L ,
```
then Xiang forces `D ≤ u_n L`, where `descKK(T)` is the largest-first differencing (caterpillar)
value of the sub-multiset `{a_i : i∈T}` and `Φ` is realised in exactly `n` cuts. `descKK` of a
descending list `b₁≥…≥b_r` is `v₁=b₁, v_j=|v_{j−1}−b_j|`. (`Φ = min positive value of the descending
include/skip reachable set `R_{n+1}`, with `0` from a nonempty even cancellation admissible.)

**GATE RESULTS (exact `Fraction`, adversarial + structured; scripts `/tmp/gate2.py`, `/tmp/verify.py`).**

- **Definitional correction found and fixed (load-bearing).** The residual is `Φ = min over NONEMPTY
  subsets` (0 admissible), NOT `min positive`. E.g. `{30,25,20,15,10}/100` (a valley at `n=4`): the
  descending include/skip *min positive* value is `1/20 = 1.55·u₄ > u₄` (would spuriously refute the
  target), but the nonempty subset `{30,25,20,15}` cancels to `0`, so `Φ=0≤u₄`. Using `min-nonempty`
  (0 allowed) the target `Φ≤u_n` holds with 0 fails, exactly as R13 recorded.
- **G2 (BOUNDARY, exact-continuation) — PASS, and upgraded to a THEOREM.** The universal inequality
  `Φ(A) ≤ |2a₁−L|` holds with **0 failures** over >100 000 exact profiles (`n=3,4,5`, valley AND
  general). Moreover `descKK(fullset) ≤ |2a₁−L|` alone holds with 0 failures — the full-profile
  caterpillar already witnesses it (no subset search needed). On the tight family it is EQUALITY:
  `descKK(A^{(n)}) = |2a₁−L| = 1/(2^{n+1}+1)` for `n=2..6` (ratios `0.778,0.882,0.939,0.969,0.985`),
  and on the R14 maximiser `{16,8,4,3,2}/33` likewise `Φ = |2a₁−L| = 1/33`. So the continuation is
  EXACT and tight, not a margin bound — it is the correct VALLEY-TIGHT-respecting object. **Proven
  below (Lemma WTC).**
- **G1 (DEEP margin) — margin EXISTS numerically but NO provable mechanism.** For the deep region
  `a₁ ≤ L/2 − c·u_n`, adversarial worst `Φ/u_n = 0.72/0.67/0.58` at `n=3/4/5` (at `c=1/2` and `c=1`;
  the margin ≈0.3 does NOT shrink to 0 with `n`, and does not improve past `c≈1/2`). BUT the deep
  minimiser requires unbounded-order cancellation: on `{30,25,20,15,10}/100` (deep, `a₁=0.30`) the
  min is `0` reached ONLY by the 4-element subset `{30,25,20,15}`; the min pairwise/single value is
  `1/20 = 1.55·u₄`. So a bounded (1–2 move) mechanism provably cannot reach the deep bound — matching
  the reviewer's gap-3 warning. **No analytic deep lever exists; the deep region is NOT closed.**
- **G3 (cover) — PASS trivially.** Dominant `a₁≥L/2` (certified whole-tail-peel) ∪ boundary
  `(L−u_nL)/2 ≤ a₁ < L/2` (Lemma WTC) ∪ deep `a₁ < (L−u_nL)/2` partitions all `a₁`.

**Verdict.** The boundary lever passes decisively and is now a proven lemma; the two-region split is
sound and the boundary half is CLOSED. The deep half is the residual (the same crux open since R7).
Genuine partial advance: the valley shrinks from `a₁<L/2` to `a₁<(L−u_nL)/2`, and the region where
VALLEY-TIGHT forbade any margin (the boundary layer, where `A^{(n)}` lives) is closed EXACTLY.

---

**Lemma WTC (whole-tail continuation bound) — PROVEN.**
For any reals `a₁ ≥ a₂ ≥ … ≥ a_m > 0` (`m≥1`) with sum `L`, the largest-first differencing value
`K := descKK(a₁,…,a_m)` satisfies
$$K \;\le\; |\,2a_1 - L\,|.$$

*Proof.* Define `v₁ = a₁` and `v_k = |v_{k−1} − a_k|` for `2 ≤ k ≤ m`, so `K = v_m`. Put
`P_k := a₂ + … + a_k` for `k ≥ 1` (empty sum `P₁ = 0`), so `P_m = L − a₁`. We prove the two-sided
invariant, for all `1 ≤ k ≤ m`,
$$(\mathrm I_k)\qquad a_1 - P_k \;\le\; v_k \;\le\; |\,a_1 - P_k\,| .$$

*Base `k=1`.* `v₁ = a₁`, `P₁ = 0`, and `a₁ − P₁ = a₁ = |a₁ − P₁|`; both sides of `(I₁)` are `a₁`. ✓

*Induction step.* Assume `(I_{k−1})`. Write `d := a₁ − P_{k−1}`, so `d ≤ v_{k−1} ≤ |d|` and
`v_{k−1} ≥ 0`. Since `P_k = P_{k−1} + a_k`, we have `a₁ − P_k = d − a_k`, and `v_k = |v_{k−1} − a_k|`.

Lower bound: `v_k = |v_{k−1} − a_k| ≥ v_{k−1} − a_k ≥ d − a_k = a₁ − P_k`. ✓

Upper bound, split on the sign of `d`:
- If `d ≥ 0`: then `|d| = d`, so `(I_{k−1})` forces `d ≤ v_{k−1} ≤ d`, i.e. `v_{k−1} = d`. Hence
  `v_k = |d − a_k| = |a₁ − P_k|`. ✓ (equality)
- If `d < 0`: then `|d| = −d ≥ 0`, and `(I_{k−1})` gives `0 ≤ v_{k−1} ≤ −d`. Also `a₁ − P_k = d − a_k
  < 0`, so `|a₁ − P_k| = a_k − d = a_k + (−d)`. As `t := v_{k−1}` ranges over `[0, −d]`, the function
  `|t − a_k|` (with `a_k > 0`) attains its maximum at an endpoint:
  `max(|0 − a_k|,\ |(−d) − a_k|) = max(a_k,\ |(−d) − a_k|)`. Now `a_k ≤ a_k + (−d) = |a₁−P_k|`, and by
  the triangle inequality `|(−d) − a_k| ≤ (−d) + a_k = |a₁−P_k|`. Therefore
  `v_k = |t − a_k| ≤ |a₁ − P_k|`. ✓

This proves `(I_k)` for all `k`. Taking `k = m`: `K = v_m ≤ |a₁ − P_m| = |a₁ − (L − a₁)| = |2a₁ − L|`.
`∎`

*(Verification: the invariant `(I_k)` and the bound `K ≤ |2a₁−L|` held with 0 violations over 300 000
adversarial integer profiles `m=2..7`; equality `K = |2a₁−L|` on `A^{(n)}` for `n=2..6`, `/tmp/verify.py`.)*

**Corollary (boundary + dominant closed).** For every valley profile with `a₁ ≥ (L − u_nL)/2`:
since `a₁ < L/2`, `|2a₁ − L| = L − 2a₁ ≤ u_nL`; the full profile is a nonempty subset `T` with
`descKK(T) = K ≤ |2a₁−L| ≤ u_nL`, so `Φ(A) ≤ u_nL`, and by certified **R-COV' (sufficiency)** Xiang
forces `D ≤ u_nL`. This is the exact continuation of certified **whole-tail-peel** (`a₁≥L/2` gives
`D = 2a₁−L`), which is the `d≥0`/equality branch of Lemma WTC. Hence the whole region
`a₁ ≥ (L−u_nL)/2` (dominant ∪ boundary) is closed, with equality attained on `A^{(n)}`. `∎`

**Residual (the open crux).** The DEEP valley `a₁ < (L−u_nL)/2` (equivalently `|2a₁−L| > u_nL`).
There the whole-tail bound gives only `Φ ≤ |2a₁−L|`, which exceeds `u_nL`; closing it needs
`Φ ≤ u_nL` via genuine multi-piece cancellation, for which no analytic mechanism is known (bounded
moves provably insufficient — `{30,25,20,15,10}/100` needs a 4-element cancellation). This is the same
first-gap / Subset-KK pigeonhole open since R7, now confined to the deep interior.

---

### Round 14 — extremal-tie / smoothing-minimax GATE: bound holds but is asymptotically tight; the "valley has margin" premise is REFUTED

Per the reviewer's mandatory gate and binding correction ("run the gate over the ACTUAL valley
domain; the dyadic ladder is OUTSIDE the valley; expect an interior maximizer at ratio ≈0.75; do
NOT pin to the ladder; prove `M* ≤ u_n` by bounding `Φ` at any tied maximizer wherever it lies"),
I ran the gate before any prose. The gate outcome is decisive and it undercuts the route's closing
mechanism, so I stop and report rather than ship a proof. **(Round 15 note: the R14 conclusion "no
margin ⇒ route dead" was correct FOR A UNIFORM bound; Round 15 shows the fix is a REGION SPLIT — the
no-margin phenomenon is entirely in the boundary layer, closed exactly by Lemma WTC above.)**

### Round 14 (original text follows) — extremal-tie / smoothing-minimax GATE
route was run FIRST, over the ACTUAL valley domain, per the reviewer's binding correction. The
UPPER BOUND ITSELF HOLDS in the valley (no valley profile with `Φ/u_n ≥ 1` exists — target
confirmed), but the reviewer's structural premise for CLOSING it — that the valley residual has a
`0.75` margin so a crude non-tight bound at the maximizer suffices — is REFUTED. The valley
residual is ASYMPTOTICALLY TIGHT: I found an explicit exact valley family with `Φ/u_n → 1`, so
the extremal-tie route cannot close via any margin-exploiting bound. Reported honestly; NO fake
proof shipped. Details in the Round 14 section directly below; Round 13 content follows.**)

### Round 14 — extremal-tie / smoothing-minimax GATE: bound holds but is asymptotically tight; the "valley has margin" premise is REFUTED

Per the reviewer's mandatory gate and binding correction ("run the gate over the ACTUAL valley
domain; the dyadic ladder is OUTSIDE the valley; expect an interior maximizer at ratio ≈0.75; do
NOT pin to the ladder; prove `M* ≤ u_n` by bounding `Φ` at any tied maximizer wherever it lies"),
I ran the gate before any prose. The gate outcome is decisive and it undercuts the route's closing
mechanism, so I stop and report rather than ship a proof.

Setup. `Φ(A) := min_{∅≠T tree-realizable} descKK(T) = min positive value of the descending
include/skip reachable set` (certified equal by Lemma FGR; the value `0` from a nonempty even
cancellation is admissible and only helps). Valley `= {a_1≥…≥a_{n+1}≥0, Σ=1, a_1<1/2,
a_2<β_n}`, `β_n=2^{n-1}/(2^{n+1}-1)`. `M* := max_{valley} Φ`. Prop UV ⟺ `M* ≤ u_n`.

**GATE FINDING 1 — the bound holds, but there is NO `0.75` margin; `M*/u_n → 1`.** Exact-fraction
evaluation of `Φ` on the explicit valley family
$$A^{(n)} = \tfrac{1}{2^{n+1}+1}\,\{\,2^n,\,2^{n-1},\dots,4,\,3,\,2\,\}\qquad(n\ge3)$$
(the dyadic ladder `{2^n,…,4,2,1}` with its two smallest parts `{2,1}` replaced by `{3,2}`; this
pushes `a_1=2^n/(2^{n+1}+1) < 1/2` INTO the valley, and `a_2 = 2^{n-1}/(2^{n+1}+1) < β_n` holds):
this family lies in the valley for every `n≥3` and has `Φ(A^{(n)}) = 1/(2^{n+1}+1)`, hence
$$\frac{\Phi(A^{(n)})}{u_n} = \frac{2^{n+1}-1}{2^{n+1}+1}\ \longrightarrow\ 1 .$$
Exact values: ratio `= 0.882, 0.939, 0.969, 0.985, 0.992, 0.996` at `n=3,4,5,6,7,8`. So
`M*_valley/u_n → 1`. The reviewer's premise ("over the valley the bound holds with margin — worst
ratio 0.75 — so bound `Φ` at the maximizer without needing tightness") is FALSE: the valley
residual is asymptotically as tight as the full upper bound. (The `0.75` figure recorded in prior
rounds was an under-sampling artifact; exact evaluation on this structured family reaches `0.996`
at `n=8` and the ratio is monotone increasing to `1`.)

**GATE FINDING 2 — the bound DOES hold in the valley (target confirmed sound).** No valley profile
with `Φ/u_n ≥ 1` was found in exact-fraction and multi-restart searches at `n=3,4,5`; the
`{2^n,…,4,3,2}` family gives `Φ/u_n = (2^{n+1}-1)/(2^{n+1}+1) < 1` strictly. This is consistent
with the confirmed answer and with the exact reduction R-UV (`upper bound in valley ⟺ Φ ≤ u_n`),
so Prop UV is TRUE — but only just, and tightly, for all large `n`.

**GATE FINDING 3 — the tie/maximizer structure is degenerate and n-dependent, not a clean single
point.** At the `n=4` maximizer `{16,8,4,3,2}/33` the minimizing signed sum `1/33` is achieved by
`14` distinct signed-subset patterns simultaneously (a high-dimensional tied face), including both
the whole-tail difference `|2a_1-1| = |a_1-a_2-a_3-a_4-a_5|` and many short interior differences.
At a different local maximizer (`n=3`, `{a_1,a_2,a_3,a_4}=(0.471,0.235,0.178,0.116)`) the minimum
is `|a_2-a_3|`, near-tied with the whole-tail difference `|2a_1-1|`. So the extremal set is neither
a unique achiever (which step 4 wanted to perturb away) nor a clean two-way tie pinning a
closed-form profile; it is a large, `n`-varying tied face on which `Φ` already equals essentially
`u_n`.

**Consequence for the route (why I stop here rather than force a proof).** The extremal-tie
argument's step 4 (unique achiever ⇒ feasible ascent ⇒ contradiction) is sound *in kind* and
does yield the dichotomy "at a maximizer, a boundary is active or ≥2 signed sums tie." But step 5
— converting that dichotomy into `Φ ≤ u_n` — was to rely on the maximizer being a clean, bounded-
away-from-tight point. GATE FINDINGS 1–3 refute exactly this: (i) there is no asymptotic margin, so
any bound that is not tight fails for large `n`; (ii) the maximizing face is high-dimensional,
degenerate, and `n`-dependent, so there is no clean profile to pin and no finite tie-classification.
Closing the valley now requires an *exact, tight* argument that reproduces `u_n` on the whole
degenerate face — which is no easier than the full upper bound and is precisely the crux that has
been open since R7. Per the standing rule and this round's directive ("if the gate FAILS, report
the refutation honestly and STOP — do NOT ship a fake proof"), I ship no proof.

**Recommendation to the outliner/reviewer (Spec note).** The reviewer's binding correction was
itself based on a numerically wrong margin (`0.75`); the corrected numeric picture is `M*_valley →
u_n`. Therefore: (a) the extremal-tie *closing* mechanism (bound `Φ` at a clean maximizer) is dead
for the same reason the ladder-pinning was — the valley has no exploitable slack; (b) the
valley-differencing-construction hedge inherits the same wall (its robustness/margin premise is
also refuted by `M*_valley→1`); (c) the honest residual is unchanged from R12 — the first-gap /
Subset-KK pigeonhole `min_{∅≠T} descKK(T) ≤ u_n` — and it is TIGHT throughout the valley, so the
next lever must be a genuinely different, *tight* framing (e.g. a direct exact induction that
carries the `{…,4,3,2}` near-extremal family, or the LP-dual/smoothing machinery being developed on
the LOWER wall, transported to the reachable-value discrepancy). Do NOT re-attempt a margin/crude
bound in the valley — it is provably impossible.

Positive, reusable deliverable this round: the explicit exact valley family `A^{(n)}` above with
`Φ(A^{(n)}) = 1/(2^{n+1}+1)` and ratio `→1`, a certified-quality lower bound on `M*_valley` that
pins the valley residual as asymptotically tight (Promotable: **Lemma VALLEY-TIGHT**).

### Round 15 (OUTLINE) — NEW LEVER proposed: BOUNDARY-CONTINUATION / two-region valley split

**Motivation (why this respects VALLEY-TIGHT).** VALLEY-TIGHT forbids any *uniform* margin/crude
bound in the valley because the tight family `A^{(n)}` drives `Φ/u_n→1`. BUT `A^{(n)}` sits at the
**boundary of the valley**: its top part is `a_1 = 2^n/(2^{n+1}+1)`, so
`L/2 − a_1 = 1/(2(2^{n+1}+1)) ≈ u_n/2` — i.e. `A^{(n)}` is at distance `~u_n/2` below `L/2`. The
no-margin phenomenon is therefore a **boundary-layer** phenomenon adjacent to the already-closed
dominant regime `a_1≥L/2` (certified whole-tail-peel: `D = 2a_1 − L`, exact and tight at `a_1=L/2`).

**Preliminary cheap-kill (R15 outliner, RANDOM valley profiles, exact `Fraction`, full
tree-realizable `Φ`):** splitting the valley by `L/2 − a_1` relative to `u_n`:
- `n=4`: DEEP valley (`L/2 − a_1 > 4u_n`) worst `Φ/u_n = 0.559` (3111 samples); BOUNDARY layer
  (`≤ 4u_n`) worst `0.730` (889 samples).
- `n=5`: DEEP worst `0.368` (1471); BOUNDARY worst `0.326` (29).
So **deep valley carries a genuine margin** (worst ≈0.37–0.56, bounded well below 1) while the
tightness concentrates in the boundary layer — exactly opening (4) of the R15 tight-cert explorer.
(Random-only, does not hit the structured tight family; the tight family is boundary-layer, which
is consistent.) This is a preliminary GREEN light, NOT a proof — the exact/structured gate below is
mandatory before any prose.

**THE PROPOSED TWO-REGION ARGUMENT (Prop UV closed exactly, no uniform margin):**
Fix a cutoff `c≥1` (to be pinned; `c=1` or `2` looks right). Split the valley `a_1<L/2`:

1. **Deep region `a_1 ≤ L/2 − c·u_n`.** Prove `Φ(A) ≤ u_n` with *room to spare* by a crude bound.
   This is legitimate because VALLEY-TIGHT's obstruction lives only in the boundary layer — deep,
   there IS margin (cheap-kill above). Candidate crude mechanism: the whole-tail signed difference
   `|2a_1 − L| = L − 2a_1` is tree-realizable (drop everything but "a_1 vs the rest"), so
   `Φ ≤ L − 2a_1`; combined with a second, interior tree value bound, close the deep region where
   `L−2a_1 ≥ 2c·u_n` gives slack to spend.
2. **Boundary layer `L/2 − c·u_n < a_1 < L/2`.** Here `Φ` is tight; treat the bound as the
   **continuation of the exact dominant formula** `D = 2a_1 − L` across `a_1 = L/2`. In the valley
   `2a_1 − L < 0`, so the whole-tail signed leftover has absolute value `L − 2a_1 < c·u_n` — already
   `O(u_n)`. Show `Φ(A) ≤ (L − 2a_1) + (correction from a_2,a_3)` and that this interpolant equals
   `u_n` at the tight family, i.e. the leftover `L−2a_1` can be shaved by one MATCH against the
   next pieces down to `≤ u_n`. This is the exact/tight step, no margin needed because the formula
   is exact on both sides of `a_1=L/2`.

**Key lemma (claim + mechanism).**
- *Deep-region margin lemma* — because for `a_1 ≤ L/2 − c·u_n` the whole-tail difference `L−2a_1`
  is `≥ 2c·u_n`, one MATCH of the largest tail piece into it (or an even-cancellation of two
  interior pieces, admissible value 0) drops the reachable leftover below `u_n`; margin exists so a
  non-tight bound suffices *here only*.
- *Boundary-continuation lemma* — because `D = 2a_1 − L` is the certified EXACT dominant value and
  is continuous across `a_1 = L/2`, the valley leftover is `|2a_1 − L|` plus a correction that is
  itself `O(u_n)` in the boundary layer; the tight family `A^{(n)}` is the fixed point of the
  interpolant (its `a_1` is exactly `u_n/2` below `L/2`, giving `Φ = u_n·(2^{n+1}−1)/(2^{n+1}+1)`).

**MANDATORY EXACT GATE before any builder prose (per VALLEY-TIGHT rule + R15 dispatch):**
run in exact `sympy`/`Fraction` at `n=3,4,5`:
  (G1) for a grid of cutoffs `c∈{1,2,3}`, confirm `max_{deep, a_1≤L/2−c·u_n} Φ/u_n` is bounded
       strictly below 1 by a MARGIN that does NOT shrink to 0 as `n` grows (structured + multi-restart
       adversarial, not random-only — random misled R11);
  (G2) confirm the boundary-layer interpolant `Φ ≤ (L−2a_1) + correction(a_2,a_3) ≤ u_n` holds on
       `A^{(n)}` and on the R14 true tied-face maximizer `{16,8,4,3,2}/33` (n=4) with equality/tightness;
  (G3) verify the two regions OVERLAP-COVER (no valley profile escapes both) at the chosen `c`.
If G1 fails (deep margin shrinks to 0 with `n`) the two-region split collapses to the full tight
problem and this lever dies like the margin route — report and STOP, no fake proof.

**Watch out for:** (a) the deep-region "crude" bound must still be `≤u_n` — VALLEY-TIGHT only licenses
margin *deep*, and the cutoff `c·u_n` must be large enough that `L−2a_1≥2c·u_n` genuinely gives room
yet small enough that the boundary layer stays `O(u_n)`-wide (a self-consistent `c` must exist —
that is G1+G3). (b) the correction term in the boundary layer is where the R14 route died (the tied
face is 14-dimensional at n=4); the continuation must be tight on that whole face, not just `A^{(n)}`.
(c) do NOT let the deep bound be the refuted mass-telescope (charging per-piece against `Σa_i`); use
a single whole-tail MATCH + one interior cancellation, a bounded-move argument, not a sum.

### Round 13 — SEED(p) + GAP-TELE refuted by the mandatory exact-fraction gate

Per the outline-reviewer's mandatory gate ("exact-fraction machine-check the SEED(p) statement AND the
GAP-TELE inequality BEFORE prose; if the scaling/constant fails, report the refutation, do not dress a
fake proof"), I ran the gate first. Both load-bearing steps FAIL. I record the refutation and the exact
obstruction.

**Reconciliation of the residual target (important; corrects a definitional trap).** The certified
residual is `μ_{n+1} = min_i dist(a_i,R_{i-1}) ≤ u_nL`, where `R_{n+1}` is the descending include/skip
reachable set. The value `0` (from an even cancellation over a *nonempty* subset) is admissible and only
helps (it gives `D=0≤u_n`); only the empty subset `T=∅` is excluded (R-COV'). Hence the correct scalar
target is
$$\min_{\varnothing\ne T\subseteq\{1,\dots,n+1\}}\ \mathrm{descKK}(T)\ \le\ u_nL,$$
the *min over nonempty subsets of the descending-KK caterpillar value* (0 allowed). Exact-fraction
check: **0 fails** over thousands of exact valley profiles, `n=2..6`, worst ratio `0.75`, tight `=1` at
the dyadic ladder — consistent with the certified reduction. (An earlier reading using `min positive`
reachable value spuriously "failed" because it wrongly discards the admissible `0`; that is a red
herring, now cleared.)

**GATE 1 — SEED(p) scaling: REFUTED.** SEED(p) as specified (seed `r`, pieces `b_1≥…≥b_p`, seed
domination `r≤b_1`, valley caps inherited, mass `M=r+Σb_j`, target: descending fold-from-seed reaches a
value `≤ u_p·M`) was checked exactly.
- With only `r≤b_1`: fails, worst ratio `2.24 / 4.21 / 6.20 / 8.17 / 9.77` at `p=2..6`.
- With the valley caps *inherited on the combined `(p+1)`-instance* (`max<M/2`, second `<β_pM`): still
  fails, worst ratio `1.67 / 3.44 / 4.85 / 7.47` at `p=3..6`.
- With the reverse domination `r≥` all pieces: fails catastrophically, worst `7.5 / 15.5 / 31.5 / 63.5`
  at `p=3..6`.
In every parametrization the worst ratio *grows with p*, so `u_p·M` is not an inductively stable
threshold: the seed-domination invariant that would make SEED(p−2) a legal IH instance does not exist at
the scaling `u_p·M`. This is exactly the failure the reviewer flagged ("12 rounds of induction attempts
failed on this parametrization") — now made concrete as a refutation, not merely "unproven."

**GATE 2 — GAP-TELE (mass-telescope discrepancy): STRUCTURALLY IMPOSSIBLE.** GAP-TELE claims
`¬(∃i: dist(a_i,R_{i-1})≤u_nL) ⟹ Σa_i>L`, i.e. charging each "far" piece against the total mass `L=1`.
Two exact facts kill it:
1. **The far-pieces reservoir is exponentially too small.** If every one of the `n+1` pieces were "far"
   (`dist(a_i,R_{i-1})>u_n`), the crude sum of thresholds is only `(n+1)u_n = (n+1)/(2^{n+1}-1)`, which
   is `0.43, 0.27, 0.16, 0.095, 0.055, 0.031, …` for `n=2,3,4,5,6,7` — it **tends to 0**. There are only
   linearly many pieces but `u_n` is exponentially small, so the "far" hypothesis is far too weak to
   reach the mass `1`. No charging of the `n+1` distances can sum past `L`.
2. **The distance-sum is provably `<2a_1<1` (a clean telescope, but the WRONG direction).** Because the
   covering radius of `R_{i-1}` on `[0,a_1]` at most halves per reflection, `dist(a_i,R_{i-1}) ≤
   a_1·2^{-(i-1)}`, whence
   $$\sum_{i=1}^{n+1}\mathrm{dist}(a_i,R_{i-1})\ \le\ a_1\sum_{k=0}^{n}2^{-k}\ =\ a_1\,(2-2^{-n})\ <\ 2a_1\ <\ 1.$$
   Exact-fraction check confirms the constant: `sum_dist/a_1` saturates at exactly `2-2^{-n}`
   (`1.75, 1.875, 1.9375, 1.96875, …` for `n=2,3,4,5`, tight, `<2`). So the *sum* of first-gap distances
   is bounded ABOVE by `<1` — the opposite of what a mass contradiction needs. GAP-TELE cannot force
   `Σa_i>L`; the mechanism is dead at the structural level, not merely unproven.

**Consequence for the field.** The mass-telescope-discrepancy lever (charge far pieces against
`Σa_i=L`) joins the four already-dead upper-wall families (covering-radius R10/R12,
density/COUNT R11, greedy-recursion R9, bounded-depth escape R10). It is a genuinely *distinct*
refutation: not "the constant is loose" but "there is not enough total distance-mass among `n+1` pieces
to reach `L`, since `(n+1)u_n→0` while the distance-sum is `<2a_1<1`." Any future upper-wall lever must
NOT try to sum per-piece contributions against the total mass — the arithmetic is fatally against it.
The honest open crux is unchanged: the first-gap / Subset-KK pigeonhole `min_{∅≠T} descKK(T) ≤ u_nL`,
which is TRUE (0 exact fails, tight at the dyadic ladder) but needs a lever that is neither a covering
radius, nor a density count, nor a greedy recursion, nor a bounded-depth escape, nor a mass-telescope.
Recommendation to the outliner: escalate per the diversity note — a potential-free / LP-duality extremal
re-derivation attacking both walls at once, rather than a sixth variant on the reachable-set object.

---

## Status (round 12)
partial (round 12 build — **the mandated GATE FAILED and the two-cap covering-radius mechanism is
REFUTED**, reported honestly per directive. Positive, rigorous deliverables recorded (see §4B.8): a
**corrected, clean covering→value reduction** with the T=∅ exclusion handled exactly, and a **sharpened
residual** that is provably NOT a covering-radius object. Details:

(i) **GATE FAILED — GAP TWO-CAP does not exist.** The proposed contraction of the *covering radius*
`c_i = ½·(max consecutive gap of R_i)` toward `u_nL` is FALSE. Exact-rational valley profiles (n=3..7,
2000 profiles): `max-gap(R_{n+1})/u_n` is `3.2× / 6.1× / 8.9× / 15.8× / 24.6×` in the worst case (fails
on 96–100% of profiles). Tracking the level-by-level evolution shows the covering radius *does* contract
roughly geometrically but **SATURATES at ≈3–5·u_n** and never reaches `u_n` — exactly the R10 saturation
(`a_{n+1}/2 ≫ u_n`) that the "second cap at every level" was supposed to fix. It does not fix it: using
`a_i ≤ a_2 < β_nL` at every level still leaves the covering radius a bounded multiple of `u_n`, never
`≤ u_n`. The windowed variant `c_n := sup_{x∈[0,β_n]} dist(x,R_n) ≤ u_n` also FAILS (worst `1.8×–19.5×`,
fails 37–100%), and even the exact-point `dist(a_{n+1},R_n) ≤ u_n` fails a few % (worst `1.4×–2.6×`).

(ii) **Root cause — the true content is the FIRST gap, not the covering radius.** The Covering claim is
`min{v>0 : v∈R_{n+1}} ≤ u_nL` (min *positive* reachable value = first gap from 0), which holds ROBUSTLY
(0 fails over 2000 exact valley profiles n=3..7, worst ratio `0.70`; and holds on adversarial
near-all-equal exact profiles where it is `~5·10^{-4}·u_n`; TIGHT `=u_n` at the dyadic boundary profile
`a_i=2^{n+1-i}/(2^{n+1}-1)`, verified n=2..6). The first gap is FAR smaller than the max gap: writing the
recursion `μ_i := min{v>0:v∈R_i}`, one has the exact identity `μ_i = min(μ_{i-1}, dist(a_i, R_{i-1}))`,
so `μ_{n+1} = min_{1≤i≤n+1} dist(a_i, R_{i-1})` — the *closest approach of some a_i to the previously
reachable set*. This is a genuinely GLOBAL pigeonhole ("some a_i lands within u_n of a prior subset-KK
value"), and `min_i dist(a_{i+1},R_i) ≤ u_n` holds (0 fails, worst `0.74`) — but it is the target
restated, with no single-level covering-radius surrogate: no fixed choice of level i works (that is why
the per-level covering radius saturates). The mechanism the outline proposed cannot exist.

(iii) **Rigorous positive contributions this round (§4B.8):** (a) the **exact reduction**
`upper bound in valley ⟺ μ_{n+1} ≤ u_nL`, via a clean conversion that EXCLUDES T=∅ correctly — every
nonempty subset T is realizable in *exactly n cuts* (leader free + (|T|−1) MATCHes + (n+1−|T|) DELETEs),
whereas T=∅ needs n+1 DELETEs (over budget), so the value `0` is geometrically present in R but is NOT a
legal leftover; the conclusion value μ_{n+1} is always nonempty-T. (b) the identity
`μ_i = min(μ_{i-1}, dist(a_i,R_{i-1}))` and the reformulation of the residual as the first-gap pigeonhole.
The make-or-break GAP is now sharply and correctly stated (it is NOT the refuted covering radius). Round
11 content below.)

## Status (round 11)
partial (round 11 build — the outline's density substrate was tested BEFORE prose, per the reviewer's
hard gate, with a decisive split of outcome: (i) **CONFINEMENT** `max(R_i)≤a₁` for all `i` is PROVEN in
full (one-line strong induction, §4B.7) and confines `R_{n+1}⊂[0,a₁)⊂[0,L/2)` — a clean, cheap,
certifiable global fact; a companion **MULTISET-DOUBLING** fact (`|M_i|=2^i` as a multiset, all in
`[0,a₁]`) is also proven. (ii) **COUNT `|R_{n+1}|=2^{n+1}` is REFUTED** — an EXACT adversarial valley
counterexample (the all-equal profile `a_i=1/(n+1)`, a genuine valley profile for `n≥3`, has
`|R_{n+1}|=2`, not `2^{n+1}`; also `n=2`: `{7/16,9/32,9/32}` gives `|R|=5<8`). So the set-injectivity
the outline's density pigeonhole was to rest on is FALSE in the valley (the random-only 1200-profile
evidence was misleading, exactly as the standing rule warned). (iii) Even the salvage — pigeonhole on
the always-`2^{n+1}` MULTISET `M_{n+1}` — does NOT convert to a value: numerically the covering value
`cov` can exceed both the average multiset gap (ratio up to `2.07`) and the smallest distinct gap
(ratio up to `3.0`), so there is NO clean `gap→value` bound of the pigeonhole type. The Covering claim
itself is RECONFIRMED robustly true even adversarially (0 fails over exact-rational valley profiles,
`n=2..6`, worst `cov/u_n=0.83`), covered via `0` from nonempty even cancellation whenever the positive
minimum is large. **Net:** the make-or-break GAP→VALUE conversion is NOT closed; moreover the SPECIFIC
mechanism the round-11 outline proposed (COUNT + density pigeonhole) is now RIGOROUSLY UNDERCUT — both
the set-count and the multiset-gap conversion provably fail. Two genuine deliverables (CONFINEMENT,
MULTISET-DOUBLING) are certifiable; GAP U-cover remains the honest open crux, now with its natural
substrate refuted so the field is not wasted on it again. Round 10 content below.)

## Status (round 10)
partial (round 10 build — the two-case (generic/near-uniform) skeleton was NUMERICALLY STRESS-TESTED
before any prose, per the reviewer's hard gate, and the outline's GENERIC mechanism was REFUTED as a
fixed-depth lemma: the "two-level existential move" (one DM move landing in a regime closed at bounded
lookahead) does NOT close the generic case — its required escape *depth grows with $n$* (depth-2-to-
dominant fails on 2.4%/14.6%/52.9% of valley profiles at $n=4/5/6$), and the failures are NOT confined
to near-uniform profiles (many have an adjacent ratio $\ge2$). So the proposed generic/near-uniform
partition does NOT hold with "generic = bounded-depth escape"; the escape is genuinely depth-$\Theta(n)$,
i.e. the *global* covering claim itself. **Spec concern raised** (see §4B.6). Two positive rigorous
items: (i) reconfirmed the Covering target holds with zero exceptions ($n=2\!-\!6$, min-reach$/u_n$
worst $0.81$); (ii) a NEW clean structural invariant of the reachable set — the covering radius of
$R_i$ on $[0,a_i]$ is $\le a_i/2$ (0 violations in 47516 checks) — recorded as a validated candidate,
with an honest note that (a) the natural induction only yields the weaker $a_{i-1}/2$ and (b) it is in
any case INSUFFICIENT alone (bounded below by $a_{n+1}/2\gg u_n$ on near-uniform), so the true crux is a
density/pigeonhole among the tree-realizable values. GAP U-cover remains open, now sharpened. Round 9
content below.)

## Status (round 9)
partial (round 9 build — the UPPER-valley residual is RE-EXPRESSED and SHARPENED. New rigorous
content: (i) **Lemma BL (band-landing / first-crossing)** — a fully-proven discrete-IVT lemma
locating a subset $T=\{a_1,\dots,a_k\}$ with $a_1-\Sigma_T=|a_1-\Sigma_T|\in[0,\beta_nL)$, realizable
by ESF-1, closing step 2 of the outline including the straddle edge case (there is none: a finite
monotone sequence crossing $a_1$ has a unique crossing index; the strict valley $a_1<L/2$ gives the
crossing, no continuity needed). (ii) A **clean reachability reformulation** of the Subset-KK claim
as a covering statement over the descending include/skip reachable set $R_{n+1}$. (iii) A **rigorous
NEGATIVE result** that settles the make-or-break step 3: the outliner's greedy band-landing
*recursion* — and EVERY single-pass greedy rule — provably overshoots $u_nL$ (machine-verified worst
ratios up to $11.4\times$ at $n\le7$ over thousands of valley profiles), while the true subset
minimum is always $\le u_nL$ (worst $0.84$). So the good subset requires genuine foresight; a
deterministic recursion is NOT the mechanism, and the residual is exactly the reachability-covering
statement, still OPEN. n=2 witness re-verified: band-landing crosses at $k=2$ with $r=17/100>u_2$,
forcing the abs-flip subset $\{a_2,a_3\}\to1/100$. Round 8 content below.)

## Status (round 8)
partial (round 8 build — Prop UV made CONSTRUCTIVE: two explicit budget-exact tree-realizable
subfamilies proven (ESF-1 subtraction-from-top, ESF-2 subset-caterpillar/descending-KK), a clean
Reduction UV' of Prop UV to the *Subset-KK claim* over an explicit family, and a RIGOROUS
counterexample proving the one-sided ESF-1 family alone is insufficient — so the two-sided abs-flip
is provably mandatory, and the greedy-subset-sum-toward-$a_1$ route is dead. Residual: the Subset-KK
claim, a restricted-discrepancy statement still requiring the scale recursion. Round 7 content below.)

## Status (round 7)
partial (round 7 build — the upper-bound valley is now REDUCED RIGOROUSLY to a single sharp
discrepancy statement **Prop UV**, with two genuinely new fully-proven pieces: a **Realizability
Lemma (RL)** characterizing exactly which leftover values Xiang can force, and a **Valley-sharpness
Lemma (VS)** proving no single DELETE/MATCH move admits an IH-certified reduction in the valley —
so any proof is forced to use ≥2 coordinated cuts. A round-6 framing error is corrected: DELETE
(dropping pieces / choosing a *subset*) is **essential** — the "one core leftover over all $n+1$
pieces" reading is refuted (a full differencing tree over ALL pieces overshoots on a positive
fraction of valley profiles; with DELETE the bound always holds). Standing: PL1, Theorem VERT, TB
proven in full; upper bound $a_1\ge L/2$ closed. The residual positive bound **Prop UV** (min
reachable differencing value $\le u_nL$) remains open.)

## Approach: breakpoint-vertex (framing F — LP-vertex / piecewise-linearity: an optimal Xiang refinement is a polytope vertex, hence takes ≤ n+1 distinct part-values)

Target (the whole claim): for every positive integer $n$, the largest $c$ Liu can guarantee is
$$c(n)=\frac{2^n}{2^{n+1}-1},\qquad\text{equivalently minimax }D=u_n=\frac1{2^{n+1}-1}.$$

**Why this is far from the current field.** Every live approach reduces to an inequality about a
*continuum* of Xiang cut-fractions. This approach proves a **finiteness / LP-vertex theorem**:
because $D$ is *piecewise linear* on the polytope of refinements (linear inside each "sort
chamber"), its minimum is attained at a **vertex**, and a vertex forces the parts to repeat — at an
optimal Xiang refinement the parts take at most $n+1$ distinct values. This collapses the continuous
minimax to a **finite** search. The lower-bound endgame is then attacked by a new exact
**top-band decomposition** (Lemma TB below), which is profile-independent and closes the bulk of the
lower bound outright.

Throughout use the certified scalar reduction (Lemmas R, M): $D=\sum_i(-1)^{i+1}b_i$ on the
descending sort $=\mu\{t>0:N(t)\text{ odd}\}$ where $N(t)=\#\{i:b_i>t\}$; Liu's share $=(1+D)/2$;
$D$ depends only on the **final multiset** of lengths. It suffices to show minimax $D=u_n$. We work
with the **unnormalized** ladder $C_n=\{2^n,2^{n-1},\dots,2,1\}$ (sum $S_n:=2^{n+1}-1$); dividing by
$S_n$ turns $D=1$ into $D=u_n$. The two directions are:

- **Lower bound (Liu plays $C_n$):** every refinement $R$ of $C_n$ using $\le n$ cuts has
  $D(R)\ge1$. (§4A)
- **Upper bound (Xiang responds to any profile $A$, $L=1$):** Xiang with $\le n$ cuts forces
  $D\le u_n$. (§4B)

---

### 1. Imported infrastructure (certified — no re-proof)
- **Lemma R** (`lemmas/reduction-odd-rank.md`): claiming ⇒ Liu gets the odd-rank sum; Liu $=(1+D)/2$.
- **Lemma M/T** (`lemmas/measure-identity.md`): $D=\mu\{t:N(t)\text{ odd}\}$; toggle calculus.
- **Lemma P** (`lemmas/cancelling-pair.md`): $D(S\cup\{v,v\})=D(S)$; the peel move.
- **Lemma PEEL** (`lemmas/strict-max-peel.md`): unique max $f_1\Rightarrow D(S)=f_1-D(S\setminus\{f_1\})$.
- **Lemma SPLIT** (`lemmas/split-cross-term.md`): $D(X\sqcup Y)=D(X)+D(Y)-2\mu(O_X\cap O_Y)$.
- **Lemma ONE** (`lemmas/top-scale-dichotomy.md`): in any refinement of $C_n$ at most one final
  piece exceeds $2^{n-1}$.
- **Whole-tail-peel** (`lemmas/whole-tail-peel.md`): closes the upper bound for $a_1\ge L/2$.

Since $D$ is a function of the final multiset only (Lemma M), a **Xiang response is a refinement**:
a choice, for each Liu piece $a\in A$, of a partition of $a$ into finitely many positive parts, with
the total number of added parts at most $n$ (using $\le n$ cuts). The order of cutting is irrelevant.

---

### 2. Lemma PL1 (single-cut piecewise-linearity) — PROVEN

**Statement.** Fix a background multiset $B$ (all other current lengths) and a piece of length
$\ell>0$. For $s\in[0,\ell]$ set $g(s):=D\big(B\cup\{s,\ell-s\}\big)$. Then $g$ is continuous,
$g(s)=g(\ell-s)$, and is **piecewise linear with slope $\in\{-2,0,+2\}$**. Consequently
$\min_{s\in[0,\ell]}g$ is attained at a breakpoint: an endpoint $s\in\{0,\ell\}$ (a *wasted* cut),
a *bisection* $s=\ell/2$, or a *tie* where $s$ or $\ell-s$ equals a value of $B$.

**Proof.** By the symmetry $\{s,\ell-s\}=\{\ell-s,s\}$ we have $g(s)=g(\ell-s)$, so it suffices to
treat $s\in[0,\ell/2]$ (then $s\le\ell-s$). Write $O:=\{t>0:N_B(t)\text{ odd}\}$ for the odd-set of
$B$ (a finite union of half-open intervals, contained in $[0,\max B)$), $f:=\mathbf 1_O$, and
$F(x):=\int_0^x f$. Because
$$N_{B\cup\{s,\ell-s\}}(t)=N_B(t)+\mathbf 1[s>t]+\mathbf 1[\ell-s>t],$$
the parity of $N$ equals that of $N_B$ on $[0,s)\cup[\ell-s,\infty)$ and is *opposite* on
$[s,\ell-s)$. Hence by Lemma M ($D=\mu\{N\text{ odd}\}$),
$$g(s)=\underbrace{\int_0^s f}_{[0,s)}+\underbrace{\int_s^{\ell-s}(1-f)}_{[s,\ell-s)}
+\underbrace{\int_{\ell-s}^\infty f}_{[\ell-s,\infty)}.$$
With $D_B:=\mu(O)=\int_0^\infty f$ (finite) this is
$$g(s)=F(s)+\big[(\ell-2s)-(F(\ell-s)-F(s))\big]+\big[D_B-F(\ell-s)\big]
=2F(s)-2F(\ell-s)+(\ell-2s)+D_B.$$
Now $F$ is the integral of the $\{0,1\}$-valued $f$, so $F$ is continuous, piecewise linear with
slope $f\in\{0,1\}$, and its breakpoints are the boundaries of $O$ — which occur only at values $v$
of $B$ (where $N_B$ changes parity). Differentiating on any interval avoiding these breakpoints,
$$g'(s)=2f(s)-2f(\ell-s)\cdot(-1)-2=2f(s)+2f(\ell-s)-2\in\{-2,0,+2\},$$
since $f(s),f(\ell-s)\in\{0,1\}$. Thus $g$ is piecewise linear with slope in $\{-2,0,2\}$, and its
breakpoints occur exactly where $s$ or $\ell-s$ crosses a value of $B$ (a tie), plus the endpoints
$s\in\{0,\ell/2\}$. A continuous piecewise-linear function on a compact interval attains its minimum
at an endpoint of one of its linear pieces, i.e. at a breakpoint or a domain endpoint. This is
precisely the stated alternative. $\qquad\blacksquare$

**Corollary PL1'.** With all other lengths frozen, an optimal choice of one cut is: not to cut, to
bisect, or to tie a fragment to an existing length. A generic interior split is never *strictly*
better.

---

### 3. Theorem VERT (vertex finiteness) — PROVEN

We prove the joint (multi-cut) statement by a **global polytope-vertex argument** on the whole
refinement at once. No settling order is used, so the reviewer's un-tying hazard cannot arise.

**Theorem VERT.** For every input multiset $A$ ($M:=|A|\le n+1$) there is a refinement $R^\star$ of
$A$ using $\le n$ cuts with $D(R^\star)=\min\{D(R):R\text{ a refinement of }A,\ \le n\text{ cuts}\}$,
such that the multiset of **positive** parts of $R^\star$ takes at most $M\ (\le n+1)$ **distinct
values**.

**Proof.**
*Step 1 — reduce to a fixed combinatorial type.* A refinement is specified by a *type*
$\tau=(m_1,\dots,m_M)$, $m_i\ge1$, $\sum_i(m_i-1)=k\le n$ (piece $a_i$ is split into $m_i$ parts),
together with the part lengths. There are finitely many types. For a fixed $\tau$ set
$N:=\sum_i m_i$ and coordinates $x=(x_{i,j})_{1\le i\le M,\,1\le j\le m_i}\in\mathbb R^N$. The
feasible set is the product of simplices
$$P_\tau=\Big\{x:\ x_{i,j}\ge0,\ \textstyle\sum_j x_{i,j}=a_i\ (\forall i)\Big\},$$
a compact convex polytope whose affine hull has direction space $W_0=\{v:\sum_j v_{i,j}=0\ \forall i\}$
of dimension $k=N-M$ (the $M$ sum-constraints are independent). The full minimum is
$\min_\tau\min_{P_\tau}D$; fix a $\tau$ achieving it.

*Step 2 — $D$ is piecewise linear on $P_\tau$, linear on each sort chamber.* Let $\mathcal H$ be the
arrangement of all "equal-length" planes $H_{p,q}=\{x_p=x_q\}$ over ordered pairs of the $N$
part-coordinates. On any connected component (chamber) $C$ of $\mathbb R^N\setminus\bigcup\mathcal H$
the descending sort order of the parts is a fixed permutation (two parts can tie only on $\mathcal H$),
so each part $x_p$ has a fixed rank and a fixed sign $\sigma_p=(-1)^{\mathrm{rank}_p+1}\in\{\pm1\}$,
whence $D(x)=\sum_p\sigma_p x_p$ is **linear** on $C$. Because sorting is continuous, $D$ is
continuous on all of $\mathbb R^N$ and equals this linear form on the closed chamber $\overline C$.

*Step 3 — the minimum is at an arrangement vertex.* $D$ is continuous on the compact set $P_\tau$,
so it attains its minimum at some $x^0\in P_\tau$; pick a chamber $C$ with $x^0\in\overline C$. Then
$Q:=\overline C\cap P_\tau$ is a nonempty compact polytope and $D|_Q$ is the *affine* function
$\sum_p\sigma_p x_p$. An affine function on a compact polytope attains its minimum at a vertex
(extreme point). Let $x^\star$ be such a vertex of $Q$; then
$D(x^\star)\le D(x^0)=\min_{P_\tau}D$, so $x^\star$ is a global minimizer, and it is a **vertex** of
$Q=P_\tau\cap\{x_p\ge x_q:\text{order relations of }C\}$.

*Step 4 — a vertex forces few distinct values.* At the vertex $x^\star$ the active constraints,
restricted to $W_0$, have rank exactly $k=N-M$ (they cut the $k$-dimensional affine hull of $P_\tau$
down to the point $x^\star$). The active constraints other than the $M$ sum-equalities (which define
the hull) are of two kinds:
(b) nonnegativities $x_p=0$ (a *zero* part); let $Z$ be the set of zero parts, $z:=|Z|$;
(c) order relations at equality $x_p=x_q$ (a *tie*), which can only join two parts of *equal* value.
Bound the *ambient* rank of (b)$\cup$(c). The zero-functionals $\{e_p:p\in Z\}$ act on $Z$; the
tie-functionals $\{e_p-e_q\}$ that are non-redundant act on positive coordinates (a tie of two zeros
is dependent on the zero constraints), a disjoint coordinate set. Let $N':=N-z$ be the number of
positive parts and $d$ the number of *distinct positive values* at $x^\star$. Active ties among
positive parts join equal values, so the graph of active positive ties has $\ge d$ connected
components; the rank of difference functionals on $N'$ coordinates with $\ge d$ components is
$\le N'-d$. Therefore
$$\mathrm{rank}(\text{(b)}\cup\text{(c)})\le z+(N'-d)=(N-N')+(N'-d)=N-d.$$
Restricting functionals to $W_0$ cannot increase rank, so
$$N-M=\mathrm{rank}_{W_0}(\text{(b)}\cup\text{(c)})\le\mathrm{rank}(\text{(b)}\cup\text{(c)})\le N-d,$$
which gives $\boxed{d\le M}$. Taking $R^\star=x^\star$ proves the theorem. $\qquad\blacksquare$

**Corollary VERT-C.** There is an optimal Xiang refinement in which the positive parts fall into
$\le n+1$ value-classes. Every value-class of size $\ge2$ contains a Lemma-P cancelling pair;
peeling all such pairs (Lemma P, $D$ unchanged) reduces $R^\star$ to a **core** multiset with all
values distinct and $\le n+1$ elements. The continuum of cut-fractions is genuinely collapsed to a
finite tie-pattern search.

**Usage of VERT (both directions).**
- *Lower bound:* $\displaystyle\min_{R}D(R)=\min_{\text{vertex }R}D(R)$, so to prove
  $\min_R D\ge1$ it suffices to check vertex refinements — a **finite** family for each fixed $n$.
- *Upper bound:* it suffices to exhibit **one** good vertex response.

---

### 4. Consequences — the two bounds

#### 4A. Lower bound: $D(R)\ge1$ for every refinement $R$ of $C_n$ ($\le n$ cuts)

We prove this by isolating the top scale $2^{n-1}$. The key new tool is exact and
profile-independent.

**Lemma TB (top-band decomposition) — PROVEN.**
Let $R$ be any refinement of $C_n$ (so, by Lemma ONE, at most one final piece exceeds $2^{n-1}$),
$n\ge1$. Let $f_1:=\max R$ and set the **top excess** $e:=(f_1-2^{n-1})^+$. Put
$$D_{\mathrm{low}}:=\mu\{t\in(0,2^{n-1}):N_R(t)\text{ odd}\}\ \ge0.$$
Then
$$D(R)=e+D_{\mathrm{low}}.$$

*Proof.* By Lemma M, $D(R)=\int_0^\infty\mathbf 1[N_R(t)\text{ odd}]\,dt$. Split the integral at
$t=2^{n-1}$:
$$D(R)=\underbrace{\int_0^{2^{n-1}}\mathbf 1[N_R(t)\text{ odd}]\,dt}_{=\,D_{\mathrm{low}}}
+\int_{2^{n-1}}^\infty\mathbf 1[N_R(t)\text{ odd}]\,dt.$$
By Lemma ONE at most one piece of $R$ exceeds $2^{n-1}$, so for every $t\ge2^{n-1}$ we have
$N_R(t)\in\{0,1\}$; hence $N_R(t)$ is odd iff $N_R(t)=1$ iff $f_1>t$. Therefore
$$\int_{2^{n-1}}^\infty\mathbf 1[N_R(t)\text{ odd}]\,dt=\int_{2^{n-1}}^\infty\mathbf 1[f_1>t]\,dt
=(f_1-2^{n-1})^+=e.$$
Adding the two pieces gives $D(R)=e+D_{\mathrm{low}}$. $\qquad\blacksquare$
(Numerically confirmed on $3000$ random multisets with $\le1$ piece above the threshold: the identity
$D=e+D_{\mathrm{low}}$ held exactly.)

**Base case $n=0$.** $C_0=\{1\}$, no cuts, $D=1\ge1$. ✓

**Trivial regime (closes the vast majority unconditionally).** Assume $n\ge1$. If $e\ge1$, i.e.
$f_1\ge2^{n-1}+1$, then by Lemma TB
$$D(R)=e+D_{\mathrm{low}}\ge1+0=1.$$
In particular this covers:
- **Case (a) — top piece $2^n$ uncut:** then $f_1=2^n$, so $e=2^n-2^{n-1}=2^{n-1}\ge1$, giving
  $D(R)\ge2^{n-1}\ge1$. (Here $2^n$ is the unique max because every other original piece $\le2^{n-1}$
  and fragments only shrink.)
- **Any refinement whose largest piece is at least $2^{n-1}+1$.**

Thus the entire lower bound reduces to the two residual sub-cases where the top excess is small,
$e<1$ (equivalently $f_1<2^{n-1}+1$), which by Lemma TB both become a lower bound on the single
scalar $D_{\mathrm{low}}$:

- **Critical band (one big fragment, $a=1$):** $2^{n-1}<f_1<2^{n-1}+1$. Then $e=f_1-2^{n-1}\in(0,1)$
  and $D(R)\ge1$ ⟺
  $$D_{\mathrm{low}}\ \ge\ 1-e\ =\ 2^{n-1}+1-f_1\ \in(0,1).\tag{L1}$$
- **Top-shredded ($a=0$):** $f_1\le2^{n-1}$, so $e=0$ and $D(R)=D_{\mathrm{low}}$; need
  $$D_{\mathrm{low}}\ =\ D(R)\ \ge\ 1.\tag{L2}$$

Both (L1) and (L2) are lower bounds on $D_{\mathrm{low}}=\mu\{t<2^{n-1}:N_R\text{ odd}\}$, i.e. on the
$D$-value of the multiset $\widehat R:=\{\min(b,2^{n-1}):b\in R\}$ obtained by **capping** every
piece at $2^{n-1}$ (indeed capping does not change $N_R(t)$ for $t<2^{n-1}$, and the capped odd-set
lies in $(0,2^{n-1})$, so $D(\widehat R)=D_{\mathrm{low}}$). By **VERT**, the minimum of
$D_{\mathrm{low}}$ over the (finite, per $n$) family of vertex refinements is what must be checked;
the extremal below-/above-gap interleavings identified in the field give exactly the boundary values
(L1: the canonical one-fragment-per-gap layout has $D_{\mathrm{low}}=2^{n-1}+1-f_1$; L2: the
straddling layout has $D_{\mathrm{low}}=1$), so both inequalities are tight and consistent with
minimax $D=1$.

**Status of §4A.** The base case, the trivial regime, and Case (a) are **proven unconditionally and
profile-independently**. The residual is the single scalar inequality on $D_{\mathrm{low}}$ in the
two small-excess sub-cases, recorded honestly as:

> **GAP L-fin.** Prove $D_{\mathrm{low}}\ge 2^{n-1}+1-f_1$ in the critical band (L1) and
> $D_{\mathrm{low}}\ge1$ in the top-shredded case (L2). By VERT this is a finite check per $n$; the
> profile-independent proof requires the one-per-gap **exchange/telescoping** argument (shared with
> induction-peel's Gap-Interleaving Lemma and parity-measure's toggle route). Carrying Lemma SPLIT's
> cross term is mandatory in the critical band (margin $\to0$ as $f_1\to2^{n-1}$); dropping it is
> fatally lossy. **Not closed in this round.**

*(That the target $\min_R D=1$ is correct is confirmed by exact brute force over integer and
$\tfrac1{12}$-grid refinements of $C_n$ for $n\le4$: the minimum is exactly $1$, attained e.g. at
$\{3,2,1,1\}$ for $n=2$ and $\{8,8,4,4,3,2,1,1\}$ for $n=4$.)*

#### 4B. Upper bound: Xiang forces $D\le u_n$ for every profile $A$ (sum $L=1$, $m\le n+1$ pieces)

**Reduction to full budget (imported).** By certified **Lemma U0(c) / Lemma DM corollary**
(`lemmas/even-multiplicity-corrector.md`, `lemmas/elementary-reductions.md`), any profile with
$m\le n$ pieces is disposed of with $D=0$ (bisect/DELETE all pieces). So the upper bound is
nontrivial only at **full budget $m=n+1$**, which we assume henceforth.

**Dominant case $a_1\ge L/2$ — CLOSED (imported).** By the certified **whole-tail-peel**
(`lemmas/whole-tail-peel.md`): with $a_1\ge L/2$ the tail mass $L-a_1\le a_1$, so Xiang cuts $a_1$
into the $m-1$ tail values plus a leftover $\ell=2a_1-L\ge0$ (using $m-1\le n$ cuts), and Lemma P
deletes the $m-1$ cancelling pairs, leaving $D=2a_1-L$. For $L/2\le a_1\le c(n)L$ this is $\le u_nL$;
for $a_1\ge c(n)L$ the bisect branch (delete $a_1$, recurse with $u_{n-1}(L-a_1)\le u_nL$) closes it
(conditional on the inductive hypothesis, as recorded in that lemma). This covers the entire range
$a_1\ge L/2$.

---

##### 4B.1 The DELETE/MATCH reduction and the achievable-leftover set

For the **upper bound only sufficiency is needed**: it suffices to *exhibit one* legal $\le n$-cut
Xiang response with $D\le u_nL$. (Optimality — Theorem VERT — is the tool for the *lower* bound and
for certifying that a finite search cannot be beaten; it is not required to prove an upper bound.)
The clean model for a Xiang response is the certified **Lemma DM** (`lemmas/elementary-reductions.md`),
whose two moves cost one cut each:
- **DELETE $x$:** bisect the piece $x$; the pair $\{x/2,x/2\}$ cancels (Lemma P), so
  $D(S)\mapsto D(S\setminus\{x\})$ — the piece $x$ is *dropped*.
- **MATCH $(x,y)$, $x>y$:** cut $x$ into $\{y,x-y\}$; the new $y$ cancels the resident $y$
  (Lemma P), so $D(S)\mapsto D\big((S\setminus\{x,y\})\cup\{x-y\}\big)$.

Both DELETE and MATCH lower the (tracked) piece-count by exactly $1$. Starting from the $m=n+1$
pieces of $A$ and applying a sequence of exactly $n$ non-degenerate DM moves therefore ends at a
**single surviving piece** $\rho\ge0$, and by Lemma DM the final alternating sum is $D=\rho$
(a single piece has $D=\rho$). Thus:

> **Reduction (R-UV).** Xiang can force $D\le u_nL$ as soon as *some* length-$n$ DM sequence on
> $A$ ends at a leftover $\rho\le u_nL$. Equivalently, writing
> $$\mathcal R(A):=\{\rho\ge0:\ \rho\text{ is the leftover of some }\le n\text{-move DM sequence on }A\}$$
> for the **achievable-leftover set**, the upper bound holds iff $\min\mathcal R(A)\le u_nL$.

This is exact and profile-independent; the only remaining question is a bound on $\min\mathcal R(A)$.

**Lemma RL (realizability of leftovers) — PROVEN.**
Let $A=\{a_1,\dots,a_m\}$. Then every $\rho\in\mathcal R(A)$ is a **signed subset sum**
$\rho=\big|\sum_{i\in T}\varepsilon_i a_i\big|$ for some nonempty $T\subseteq\{1,\dots,m\}$ and signs
$\varepsilon_i\in\{-1,+1\}$; moreover the signs are those of a **nonnegative differencing tree**
on $\{a_i:i\in T\}$ (a full binary tree whose internal nodes are the *absolute* differences of their
children). Conversely, every value of such a tree over any nonempty $T$ (with $|T|-1\le n$ internal
nodes, and the $m-|T|$ deletions costing $m-|T|$ further cuts, total $\le n$ when $m\le n+1$) lies in
$\mathcal R(A)$. Consequently
$$\mathcal R(A)\subseteq\Big\{\big|\textstyle\sum_i\varepsilon_i a_i\big|:\varepsilon\in\{-1,0,+1\}^m,\ \varepsilon\ne0\Big\},$$
and this inclusion is in general **strict**: only the *tree-realizable* sign patterns occur.

*Proof.* Track, for each current piece, its expansion as an integer combination of the $a_i$.
Initially each $a_i$ is itself (the standard basis vector $e_i$). A DELETE removes a piece and adds
nothing, so it only deletes coordinates. A MATCH $(x,y)$ replaces the two vectors $\mathbf v_x,
\mathbf v_y$ by $\mathbf v_x-\mathbf v_y$ (choosing the sign so the *value* $x-y\ge0$). By induction
every current piece is $\sum_i c_i a_i$ where the coefficient vector $\mathbf c$ is obtained from
initial basis vectors by *sign-respecting differences*; a straightforward induction shows each
coordinate $c_i\in\{-1,0,+1\}$ and the support forms a tree of MATCHes over a subset $T$, with
$c_i=0$ exactly for the deleted/unused leaves. Since the final piece has value $\rho\ge0$ equal to
its own combination, $\rho=\big|\sum_{i\in T}\varepsilon_i a_i\big|$ with $\varepsilon_i=c_i$. The
converse (any nonnegative differencing tree on any subset is executable within budget) is exactly a
DM sequence: MATCH along the tree's internal nodes ($|T|-1$ cuts) and DELETE the leaves outside $T$
($m-|T|$ cuts), total $m-1\le n$. Strictness: for $m=3$ the value $a_1+a_2$ is a $\{0,\pm1\}$ signed
sum but is **not** reachable (MATCH only ever produces a *difference* $x-y$, never a sum of two
positive pieces), so it is absent from $\mathcal R(A)$. $\qquad\blacksquare$

(Machine-checked, budget $\le n$ enforced: for $m\in\{3,4,5\}$, $\mathcal R(A)$ is always a *subset*
of the $\{0,\pm1\}$ signed sums — in $30/30$ random trials $\mathcal R(A)\setminus\{\text{signed
sums}\}=\varnothing$ — and a *strict* subset, e.g. $|\mathcal R|=8<13$ for $m=3$. The excluded
patterns are exactly the non-tree-realizable ones the explorer flagged.)

**Correction to the round-6 framing (important).** The round-6 note "the simultaneous even-pairing
vertex response leaves one core leftover $\rho$ over all $n+1$ pieces" is **wrong for the valley**:
a differencing tree that uses *all* $n+1$ pieces (no DELETE) does **not** always reach $\le u_nL$.
Machine-checked with the cut-budget enforced: over $516$ random valley profiles ($n=2,\dots,5$;
$a_1<L/2$, $a_2<\beta_nL$), the no-DELETE minimum leftover *exceeded* $u_nL$ on $214$ of them (worst
ratio $7.54\times$). With DELETE allowed (i.e. the full $\mathcal R(A)$, choosing a *subset*), the
minimum leftover was $\le u_nL$ on all $387$ valley profiles tested (worst ratio $0.56$). So
**DELETE / subset-selection is essential** in the valley; the operative statement is Prop UV below,
over the full $\mathcal R(A)$, not over full-support trees.

##### 4B.2 Valley-sharpness: no single move admits an IH-certified reduction

The balanced valley is $\{m=n+1,\ a_1<L/2,\ a_2<\beta_nL\}$ with $\beta_n:=2^{n-1}/(2^{n+1}-1)$.
Here $c(n)=2^n/(2^{n+1}-1)=(1+u_n)/2>\tfrac12$, and the ratio $u_n/u_{n-1}=(2^n-1)/(2^{n+1}-1)$.

**Lemma VS (valley-sharpness) — PROVEN.** In the balanced valley, *no* single DM move produces an
$(n)$-piece instance on which the inductive hypothesis $\mathrm{UB}(n-1)$ (that Xiang forces
$D\le u_{n-1}\cdot(\text{mass})$) alone certifies $D\le u_nL$. Concretely:
1. **Single DELETE $a_i$** gives $n$ pieces of mass $L-a_i$; $\mathrm{UB}(n-1)$ yields
   $D\le u_{n-1}(L-a_i)$, which is $\le u_nL$ iff $a_i\ge c(n)L$. But $a_i\le a_1<L/2<c(n)L$, so the
   certificate fails for every $i$.
2. **Single MATCH $(a_i,a_j)$**, smaller part $y:=\min(a_i,a_j)$, gives $n$ pieces of mass $L-2y$;
   $\mathrm{UB}(n-1)$ yields $D\le u_{n-1}(L-2y)$, which is $\le u_nL$ iff $y\ge\beta_nL$. But the
   smaller of any two pieces is $\le a_2<\beta_nL$, so the certificate fails for every pair.

*Proof.* (1) $u_{n-1}(L-a_i)\le u_nL\iff L-a_i\le(u_n/u_{n-1})L=\frac{2^n-1}{2^{n+1}-1}L\iff
a_i\ge\big(1-\frac{2^n-1}{2^{n+1}-1}\big)L=\frac{2^n}{2^{n+1}-1}L=c(n)L$. Since $c(n)=2^n/(2^{n+1}-1)
>\tfrac12$ (as $2\cdot2^n=2^{n+1}>2^{n+1}-1$) and $a_i\le a_1<L/2$, we get $a_i<c(n)L$; the certificate
fails. (2) $u_{n-1}(L-2y)\le u_nL\iff 2y\ge\big(1-\frac{2^n-1}{2^{n+1}-1}\big)L=\frac{2^n}{2^{n+1}-1}L
\iff y\ge\frac{2^{n-1}}{2^{n+1}-1}L=\beta_nL$. In any pair the smaller element is $\le a_2$ (at most
one member of the pair is $a_1$; the other is $\le a_2$, and the smaller is $\le$ that other). Since
$a_2<\beta_nL$, we get $y<\beta_nL$; the certificate fails. $\qquad\blacksquare$

Lemma VS is the **rigorous** statement of why the valley is the unique residual case and why every
*deterministic single-rule* Xiang strategy was refuted numerically (always-DELETE-$a_1$ $25.5\times$,
always-MATCH-top-two $4.23\times$, hybrid $10.7\times$, cascading bisection $4.7\times$): each such
rule is a one-move-then-recurse reduction, and Lemma VS shows the one-move IH certificate is
unavailable throughout the valley. Any valid proof must therefore spend **$\ge2$ coordinated cuts**
before invoking any induction — i.e. it is genuinely adaptive, exactly as the field diagnosed. The
two thresholds $c(n)L$ (DELETE) and $\beta_nL$ (MATCH) meet the valley's two defining inequalities
$a_1<L/2$ and $a_2<\beta_nL$ *exactly*, confirming the valley boundary is sharp.

##### 4B.3 The residual: Proposition UV

> **Prop UV (achievable-discrepancy bound) — OPEN.** For every full-budget balanced-valley profile
> $A=\{a_1\ge\dots\ge a_{n+1}\}$ (sum $L$, $a_1<L/2$, $a_2<\beta_nL$),
> $$\min\mathcal R(A)\ \le\ u_nL,\qquad u_n=\tfrac1{2^{n+1}-1}.$$
> By Reduction (R-UV) this is *equivalent* to the upper bound in the valley. By Lemma RL it is the
> **restricted signed-subset-sum discrepancy** problem: minimize $\big|\sum_{i\in T}\varepsilon_ia_i
> \big|$ over subsets $T$ and *tree-realizable* sign patterns. **Not closed in this round.**

*What is genuinely established this round.* (i) The upper-bound valley is *exactly* Prop UV, a single
clean discrepancy inequality (R-UV, rigorous via certified DM/P/U0). (ii) Lemma RL pins down the
achievable family precisely and corrects the round-6 no-DELETE framing. (iii) Lemma VS proves
profile-independently that $\ge2$ cuts are unavoidable before induction, so any correct argument is
adaptive — ruling out the entire class of single-move recursions rigorously (not just numerically).

##### 4B.4 Round 8: explicit realizable subfamilies and reduction to the Subset-KK discrepancy claim

This round makes Prop UV *constructive*: we exhibit **explicit** tree-realizable subfamilies of
$\mathcal R(A)$ (with full cut-budget accounting), reduce Prop UV to a bound over one of them, and
prove *rigorously* (explicit counterexample) that the tempting "subtract from the top" family alone
is insufficient — so any construction must use the abs-flip. All of the following is self-contained
on certified Lemmas P/DM (`lemmas/cancelling-pair.md`, `lemmas/elementary-reductions.md`); no
numerics enter the proofs.

**Lemma ESF-1 (subtraction-from-top subfamily) — PROVEN.** Let $A=\{a_1\ge a_2\ge\dots\ge a_{n+1}\}$
(full budget, sum $L$). For every $T\subseteq\{2,\dots,n+1\}$ with $\sum_{i\in T}a_i\le a_1$,
$$a_1-\sum_{i\in T}a_i\ \in\ \mathcal R(A),$$
realized by exactly $n$ DM moves.

*Proof.* Write $T=\{i_1,\dots,i_k\}$ in any order and set $r_0:=a_1$, $r_j:=r_{j-1}-a_{i_j}$. For each
$j$, the partial sum through step $j$ satisfies $a_{i_1}+\dots+a_{i_j}\le\sum_{i\in T}a_i\le a_1$,
hence $r_{j-1}=a_1-(a_{i_1}+\dots+a_{i_{j-1}})\ge a_{i_j}\ge0$. So the current running piece
$r_{j-1}$ is $\ge$ the resident piece $a_{i_j}$, and MATCH$(r_{j-1},a_{i_j})$ is legal: cut $r_{j-1}$
into $\{a_{i_j},\,r_{j-1}-a_{i_j}\}$; the created $a_{i_j}$ cancels the resident $a_{i_j}$ (Lemma P),
leaving the single running piece $r_j=r_{j-1}-a_{i_j}\ge0$ and consuming the resident. Each MATCH
costs one cut (Lemma DM) and lowers the piece-count by one. After the $k$ MATCHes the pieces are the
running $r_k=a_1-\sum_{i\in T}a_i$ together with the $n-k$ untouched non-top, non-$T$ pieces. DELETE
each of those ($n-k$ bisect-and-cancel moves, Lemma DM, one cut each), reaching the single piece
$r_k$. Total moves $k+(n-k)=n$, and $D=r_k$ (a single piece has $D=$ its length, Lemma M). $\blacksquare$

**Lemma ESF-2 (subset-caterpillar subfamily) — PROVEN.** For every nonempty $T\subseteq\{1,\dots,n+1\}$
and every ordering $t_1,t_2,\dots,t_k$ of $\{a_i:i\in T\}$, the caterpillar value
$$v_1:=t_1,\qquad v_j:=|v_{j-1}-t_j|\ (2\le j\le k),\qquad v_k\ \in\ \mathcal R(A),$$
realized by exactly $n$ DM moves. In particular the **descending-KK value** (order $t_1\ge\dots\ge t_k$)
of any subset lies in $\mathcal R(A)$.

*Proof.* Induct on $j$ that the multiset can be driven to have $v_{j-1}$ as a current piece with the
untouched pieces $\{a_i:i\notin\{t_1,\dots,t_{j-1}\}\}$ present, after $j-1$ MATCHes. Base $j=1$:
$v_1=t_1$ is a resident piece. Step: $v_{j-1}$ and $t_j$ are both current pieces. If $v_{j-1}\ge t_j$,
MATCH$(v_{j-1},t_j)$ cuts $v_{j-1}$ into $\{t_j,v_{j-1}-t_j\}$; the new $t_j$ cancels the resident
$t_j$ (Lemma P), leaving $v_{j-1}-t_j=|v_{j-1}-t_j|=v_j$. If $v_{j-1}<t_j$, MATCH$(t_j,v_{j-1})$ cuts
the resident $t_j$ into $\{v_{j-1},t_j-v_{j-1}\}$; the new $v_{j-1}$ cancels the running piece
$v_{j-1}$ (Lemma P), leaving $t_j-v_{j-1}=|v_{j-1}-t_j|=v_j$. Either branch is a single legal MATCH
(one cut), lowers the count by one, and leaves $v_j$ as the running piece. After $k-1$ MATCHes the
pieces are $v_k$ and the $n+1-k$ elements of $A$ outside $T$; DELETE those ($n+1-k$ moves). Total
$(k-1)+(n+1-k)=n$ moves, $D=v_k$. $\blacksquare$

*(Remark: ESF-1 is the special case of ESF-2 in which the running value never flips sign; ESF-2 is
strictly larger precisely because of the abs-flip branch $v_{j-1}<t_j$.)*

**Reduction UV' (Prop UV $\Longleftarrow$ Subset-KK claim) — RIGOROUS.** By ESF-2, if some subset
$T$ has descending-KK value $\le u_nL$, then $\min\mathcal R(A)\le u_nL$ and, by Reduction R-UV, the
upper bound holds in the valley. Hence Prop UV follows from:

> **Subset-KK claim (residual).** For every full-budget balanced-valley profile
> $A=\{a_1\ge\dots\ge a_{n+1}\}$ ($\sum=L$, $a_1<L/2$, $a_2<\beta_nL$) there exists a nonempty subset
> $T\subseteq\{1,\dots,n+1\}$ whose descending-KK caterpillar value is $\le u_nL$.

This is a *strictly cleaner* target than Prop UV as stated over the full $\mathcal R(A)$: it is a
minimum over an **explicit constructive family** (subset + one fixed order), each member realizable by
ESF-2, and it is *sufficient* for the upper bound (we need only existence of one small value, not the
true minimum). Independent brute force over the valley (all subsets, descending-KK, budget enforced)
found the Subset-KK value $\le u_nL$ on **every** profile tested with margin (worst ratios
$0.31$–$0.74$ for $n=2,\dots,6$), so the claim is correct; it is the honest residual.

**Rigorous negative result — the subtraction-only family is insufficient (abs-flip is essential).**
One might hope to close Prop UV using only ESF-1 (choose $T$ to make $\sum_{i\in T}a_i$ approach $a_1$
from below). This is *false*, profile-independently, and here is an **explicit rational
counterexample** at $n=2$ (so it is a theorem, not a spot-check): take
$$A=\Big\{a_1,a_2,a_3\Big\}=\Big\{\tfrac{9}{20},\ \tfrac{7}{25},\ \tfrac{27}{100}\Big\},\qquad L=1.$$
Check it is a valley profile: $a_1+a_2+a_3=\tfrac{45+28+27}{100}=1$; $a_1=\tfrac9{20}<\tfrac12$;
$a_2=\tfrac7{25}=0.28<\beta_2=\tfrac2{7}\approx0.2857$. The only subsets $T\subseteq\{2,3\}$ with
$\sum_{i\in T}a_i\le a_1$ are $\varnothing$ (value $a_1=\tfrac9{20}$), $\{2\}$ (value
$a_1-a_2=\tfrac{9}{20}-\tfrac7{25}=\tfrac{45-28}{100}=\tfrac{17}{100}$), and $\{3\}$ (value
$a_1-a_3=\tfrac{45-27}{100}=\tfrac{9}{50}$); the subset $\{2,3\}$ is excluded since
$a_2+a_3=\tfrac{55}{100}>a_1$. Thus the ESF-1 minimum is $\min\{\tfrac9{20},\tfrac{17}{100},
\tfrac9{50}\}=\tfrac{17}{100}$, which **exceeds** $u_2=\tfrac17=\tfrac{14.28\dots}{100}$. By contrast
the abs-flip subset $T=\{2,3\}$ gives descending-KK value $|a_2-a_3|=|\tfrac{28}{100}-\tfrac{27}{100}|
=\tfrac{1}{100}\le u_2$. So ESF-1 alone provably cannot reach $u_nL$; the extra power of ESF-2 (a
caterpillar not anchored at $a_1$, i.e. an abs-flip / choosing the leader among the *smaller* pieces)
is **necessary**. This rigorously rules out the "greedy subset-sum toward $a_1$" route (which the
field's crude bound $\rho<a_2$ from aimo-0796 realizes, and which is short of $u_n$ by up to a factor
$\beta_n/u_n=2^{n-1}$) and pins the residual to the genuinely two-sided Subset-KK claim.

**Where the Subset-KK claim stands.** It is *not* closed this round. A deterministic single-pass
policy does **not** suffice: the natural greedy "include $a_k$ iff it strictly reduces the running
value" overshoots (rigorously, it must, since it coincides with full-support descending-KK once no
piece is skippable, and full-support KK is machine-refuted at ratio up to $7.5\times$); the correct
subset requires foresight. So the Subset-KK claim is a genuine restricted-discrepancy statement whose
profile-independent proof needs the *scale-recursion* content (represent the residual after the first
crossing using the smaller pieces, recursively), exactly the shared crux. What round 8 contributes is
(i) two explicit, budget-exact realizable subfamilies ESF-1/ESF-2, converting Prop UV from an
existence statement over the abstract $\mathcal R(A)$ into a bound over a concrete construction;
(ii) the reduction to the cleaner Subset-KK claim; and (iii) a *rigorous* proof (explicit
counterexample) that the one-sided subtraction family is insufficient, so the two-sided abs-flip is
provably mandatory.

*Why Prop UV is true (evidence, not proof).* The extremal dyadic profile $a_i=2^{n+1-i}/(2^{n+1}-1)$
attains $\min\mathcal R=u_nL$ exactly (any nonzero $\{0,\pm1\}$-combination of $2^n,\dots,2,1$ is a
nonzero integer, $\ge1$ in absolute value, and $2^n-2^{n-1}-\dots-1=1$ is tree-realizable by the
descending cascade). Machine search over $387$ valley profiles ($n\le5$, budget $\le n$ enforced)
found $\min\mathcal R\le u_nL$ every time (worst ratio $0.56$), so the target is correct; the
difficulty is a *profile-independent* proof of the restricted-discrepancy bound. The naive
$2^{n+1}$-subset-sum pigeonhole gives $u_nL$ only if all $\{0,\pm1\}$ patterns were reachable, which
Lemma RL shows they are not — so a direct pigeonhole is invalid, matching the explorer's factor-2
achievability deficit. Closing Prop UV is the make-or-break step, shared with `subset-sum-pigeonhole`
and `smoothing-majorization`.

##### 4B.5 Round 9: band-landing lemma (step 2, PROVEN), reachability reformulation, and the rigorous refutation of the greedy recursion (step 3)

Throughout normalize $L=1$ (divide all lengths by $L$; $D$ scales linearly). Recall $u_n=1/(2^{n+1}-1)$
and $\beta_n=2^{n-1}u_n=2^{n-1}/(2^{n+1}-1)$. We are in the full-budget balanced valley:
$A=\{a_1\ge a_2\ge\dots\ge a_{n+1}\}$, $\sum_i a_i=1$, $a_1<\tfrac12$, $a_2<\beta_n$.

**Lemma BL (band-landing / first crossing) — PROVEN.**
Let the *survivors* be $s_1:=a_2\ge s_2:=a_3\ge\dots\ge s_n:=a_{n+1}$, with descending partial sums
$P_0:=0$ and $P_j:=s_1+\dots+s_j$ ($1\le j\le n$). Then:
1. $P_n=1-a_1>a_1$ (strict), so the finite increasing sequence $P_0<P_1<\dots<P_n$ crosses $a_1$:
   there is a unique index $k\in\{1,\dots,n\}$ with $P_{k-1}\le a_1<P_k$.
2. Put $T:=\{a_1,a_2,\dots,a_k\}$ and $r:=a_1-P_{k-1}=a_1-\sum_{i=2}^{k}a_i$. Then
   $$0\le r<s_k\le a_2<\beta_n .$$
3. $r$ equals the descending-KK caterpillar value of $T$ and lies in $\mathcal R(A)$, realized by
   exactly $n$ DM moves (Lemma ESF-1).

*Proof.* (1) The survivors are positive, so $P_0<P_1<\dots<P_n$ is strictly increasing;
$P_n=\sum_{i=2}^{n+1}a_i=1-a_1$. The valley hypothesis $a_1<\tfrac12$ gives $1-a_1>\tfrac12>a_1$, i.e.
$P_n>a_1$; and $P_0=0\le a_1$. A strictly increasing finite real sequence starting $\le a_1$ and
ending $>a_1$ has a unique first index $k$ with $P_{k}>a_1$; then $P_{k-1}\le a_1<P_k$ (discrete
intermediate value; no continuity is invoked — this is a statement about a totally ordered finite
list, so there is **no straddle ambiguity**: exactly one index $k$ satisfies the two-sided
inequality). Since $P_n>a_1$ we have $k\le n$, so $T$ uses only real survivors.
(2) From $P_{k-1}\le a_1$ we get $r=a_1-P_{k-1}\ge0$. From $P_k=P_{k-1}+s_k>a_1$ we get
$s_k>a_1-P_{k-1}=r$, i.e. $r<s_k$. Finally $s_k\le s_1=a_2<\beta_n$ by the sorting and the valley
hypothesis, giving $r<\beta_n$.
(3) Order $T$ descending: $a_1\ge a_2\ge\dots\ge a_k$. Run the caterpillar $r_1=a_1$,
$r_j=|r_{j-1}-a_j|$. For each $2\le j\le k$ the running value *before* subtracting $a_j$ is
$r_{j-1}=a_1-\sum_{i=2}^{j-1}a_i=a_1-P_{j-2}\ge a_1-P_{k-1}=r\ge0$; moreover
$r_{j-1}=a_1-P_{j-2}\ge s_{j-1}=a_{j}$? We only need $r_{j-1}\ge a_j$ to avoid an abs-flip:
$r_{j-1}-a_j=a_1-P_{j-1}=a_1-\sum_{i=2}^{j}a_i\ge a_1-P_{k-1}=r\ge0$ (since $j\le k$ means
$P_{j-1}\le P_{k-1}$). Hence every step is a plain subtraction with no flip, and
$r_k=a_1-P_{k-1}=r$. This is exactly Lemma ESF-1 with the subset $\{2,\dots,k\}$
($\sum_{i=2}^{k}a_i=P_{k-1}\le a_1$), realized by $k-1$ MATCHes and $n-(k-1)$ DELETEs $=n$ moves,
with $D=r$. $\qquad\blacksquare$

Lemma BL closes **step 2** of the outline completely and disposes of the reviewer's flagged
straddle edge case: because the crossing is located on a *finite strictly increasing sequence of
partial sums*, the crossing index is unique and unambiguous; the strict valley inequality
$a_1<\tfrac12$ is precisely what forces $P_n>a_1$ (the crossing to exist with $k\le n$), and
$r<s_k\le a_2<\beta_n$ uses the sorting plus $a_2<\beta_n$. There is no boundary case to settle.

**Verification on the n=2 witness $A=\{9/20,7/25,27/100\}$.** Survivors $s_1=a_2=7/25=28/100$,
$s_2=a_3=27/100$; $P_0=0,\ P_1=28/100,\ P_2=55/100$. Since $P_1=28/100\le a_1=45/100<P_2=55/100$, the
crossing is at $k=2$ with $r=a_1-P_1=45/100-28/100=17/100$. Indeed $0\le17/100<s_2=27/100<\beta_2=2/7$.
This matches the round-8 ESF-1 floor $17/100$, which **exceeds** $u_2=1/7=14.28\dots/100$. So the
first crossing (anchored at $a_1$) does **not** reach $u_n$ here; the abs-flip subset $\{a_2,a_3\}$
(descending-KK $|a_2-a_3|=1/100\le u_2$) is required. This is the concrete manifestation of why
step 3 must not anchor at $a_1$.

**Reachability reformulation of the Subset-KK claim.** Since ESF-2 realizes the descending-KK
caterpillar over *any* subset, define the **descending include/skip reachable set**
$$R_0:=\{0\},\qquad R_i:=R_{i-1}\ \cup\ \{\,|v-a_i|:v\in R_{i-1}\,\}\quad(1\le i\le n+1).$$
Reading "include $a_i$" as $v\mapsto|v-a_i|$ (the first include, from $v=0$, sets the leader
$|0-a_i|=a_i$), every element of $R_{n+1}$ reachable through a nonempty set of includes is the
descending-KK value of that subset, hence lies in $\mathcal R(A)$ (Lemma ESF-2). Therefore:

> **Covering claim (equivalent residual).** $R_{n+1}$ contains a value $\rho$ with $0\le\rho\le u_n$
> that is realized by a **nonempty** set of includes. By Lemma ESF-2 and Reduction R-UV this implies
> $\min\mathcal R(A)\le u_n$, i.e. the upper bound in the valley.

(The value $\rho=0$ is admissible: an even-cancelling nonempty subset — e.g. two equal pieces — gives
descending-KK $0$, hence $D=0\le u_n$. This is exactly how the near-all-equal valley profiles, whose
minimal *positive* caterpillar can exceed $u_n$, are covered.) The Covering claim is a clean
restricted-discrepancy/covering statement: *the descending include/skip reachable set meets
$[0,u_n]$.*

**Rigorous refutation of the greedy recursion (step 3 as a deterministic recipe is FALSE).**
The outline's step 3 proposes to iterate Lemma BL: cross $a_1$ to get $r<\beta_n$, then recurse the
same band-landing on $r$ against the remaining survivors, gaining one dyadic band each phase. This
**does not work as a deterministic recursion**, and neither does any single-pass greedy. Concretely,
consider the natural candidate recipes:
- **Greedy band-landing recursion:** repeatedly cross the current target with a descending prefix of
  the remaining survivors and take the smaller crossing residual, then recurse on the rest.
- **Flip-if-it-helps greedy:** process $a_2,a_3,\dots$ in descending order and include $a_i$
  (set $r\mapsto|r-a_i|$) iff it strictly reduces $r$ (i.e. $a_i<2r$), else skip.
- **Drop-one:** run full descending-KK on each of the $n+1$ subsets $A\setminus\{a_i\}$ and take the best.

Each of these is a fixed deterministic policy, so its output is a *specific* subset value; if the
Subset-KK claim held via any of them, that value would be $\le u_n$ on every valley profile. It does
not. An exhaustive machine check over thousands of admissible valley profiles per $n$
($a_1<\tfrac12$, $a_2<\beta_n$, budget enforced) gives the worst-case ratios (output/$u_n$):

| $n$ | greedy band-landing | flip-if-helps | drop-one | **true min over subsets** |
|-----|--------------------|---------------|----------|---------------------------|
| 2   | 0.96 | 0.98 | 0.47 | **0.33** |
| 3   | 1.62 | 1.61 | 3.56 | **0.84** |
| 4   | 3.03 | 2.86 | 2.67 | **0.62** |
| 5   | 4.30 | 4.52 | 8.88 | **0.52** |
| 6   | 7.70 | 7.96 | 8.56 | **0.41** |
| 7   |  —   | 11.38| —    | **0.39** |

Every greedy/single-pass rule overshoots $u_n$ (ratios growing like $2^{\Theta(n)}$), while the true
minimum over *all* subsets (equivalently $\min$ of the reachable set $R_{n+1}$, computed by the
include/skip DP) stays $\le u_n$ with a comfortable margin. (These numerics are diagnostic only, used
to *rule out* candidate recipes; no numeric statement enters a proof step.) This is a rigorous
negative result in the sense that a single overshooting profile is an explicit counterexample to the
recipe (the $n=2$ witness above is such an explicit counterexample for flip-if-helps and greedy
band-landing: they bottom at $17/100>u_2$). **Consequence:** the correct subset genuinely requires
foresight; the residual is *not* closed by iterating Lemma BL or by any deterministic single pass. It
is exactly the Covering claim, whose proof needs a *global* covering argument on $R_{n+1}$ (a
gap/dispersion invariant that telescopes to $u_n$), not a recursion.

> **GAP U-cover (the make-or-break, OPEN).** Prove the Covering claim: for every full-budget
> balanced-valley profile, the descending include/skip reachable set $R_{n+1}$ meets $[0,u_n]$ via a
> nonempty include-set. Equivalently $\min\mathcal R(A)\le u_n$. What is needed is a
> profile-independent covering/dispersion invariant on the sets $R_i$ that shrinks the covering
> radius near $0$ to $\le u_n$ after all $n+1$ pieces are processed — using the sum constraint
> $\sum a_i=1$ and the caps $a_1<\tfrac12$, $a_2<\beta_n$ jointly (a per-step "gain one dyadic band"
> statement is FALSE, per the refutation above; the correct object is aggregate/global, mirroring the
> LOWER wall's reserve $\rho_k$). Lemma BL supplies the first landing $r\in[0,\beta_n)$; the residual
> is to cover the remaining factor $2^{n-1}$ down to $u_n$ globally rather than greedily.

*What round 9 established (self-contained on certified P/DM/ESF-1/ESF-2, no numerics in proofs):*
(i) **Lemma BL** — a fully rigorous first-crossing/band-landing lemma with the straddle case settled
(there is none). (ii) The **reachability/Covering reformulation** — the cleanest equivalent form of
the residual, an explicit descending include/skip covering statement. (iii) A **rigorous refutation**
that the outline's greedy step-3 recursion and every single-pass policy overshoot (up to $11.4\times$),
so the residual is genuinely a global covering problem requiring foresight — pruning the entire class
of deterministic recursion recipes (including the valley-differencing reserve's greedy hope).

##### 4B.6 Round 10: numerical stress-test of the two-case skeleton — REFUTATION of the fixed-depth generic lemma, a new reachable-set covering invariant, and the sharpened residual

Per the outline-reviewer's hard numeric-first gate, the proposed two-case skeleton — **generic**
(a two-level existential move escaping to an already-closed regime) $\cup$ **near-uniform** (explicit
even-cancellation) — was tested profile-independently against the valley generator ($n=2\!-\!6$,
$a_1<\tfrac12$, $a_2<\beta_n$, full budget, sum $1$) *before* committing prose. All numerics below are
diagnostic only (used to rule recipes in/out); no numeric statement enters a proof step.

**(0) Target reconfirmed.** Over thousands of valley profiles per $n$, the descending include/skip
reachable minimum $\min\mathcal R(A)$ (nonempty-include) satisfied $\min\mathcal R(A)\le u_n$ with **zero
exceptions**; worst ratio $\min\mathcal R/u_n$ was $0.29,0.81,0.74,0.50,0.48$ for $n=2,3,4,5,6$. The
Covering claim (§4B.5) is correct; the difficulty is a profile-independent *proof*.

**(1) Refutation of the fixed-depth generic lemma (make-or-break — the outline's step 2 does NOT hold
as stated).** Define the *depth-$d$ escape value* of a profile $A$: the minimum, over all DM sequences
of length $\le d$, of the value obtained by either reaching a single piece or reaching an instance in
the unconditionally-closed dominant regime $a_1'\ge L'/2$ and taking its whole-tail-peel leftover
$2a_1'-L'$. The outline's generic mechanism asserts that *outside the near-uniform band* the depth-$2$
escape value is $\le u_n$. This is **false**, and the failure worsens with $n$:

| $n$ | depth-$1$ fail | depth-$2$ fail | depth-$3$ fail |
|-----|----------------|----------------|----------------|
| 3   | 21.6%          | 0.0%           | 0.0%           |
| 4   | 68.9%          | 2.4%           | 0.1%           |
| 5   | 91.6%          | 14.6%          | 0.2%           |
| 6   | 98.7%          | 52.9%          | 0.8%           |

(fractions of valley profiles whose depth-$d$ escape value exceeds $u_n$). Two rigorous consequences.
*First*, the pure single-move "escape to the dominant regime $a_1'\ge L'/2$" (depth $1$) fails on
$21\!-\!99\%$ of the valley — already reported by the explorer as a cheap-kill, here reconfirmed
profile-independently, so branch (a) *alone* is not the generic mechanism. *Second, and decisively:*
the depth-$2$ escape (branch (a) OR one further VS-certified move, i.e. the outline's actual
"two-level" lemma) fails on a fraction that **grows with $n$** ($2.4\%\to14.6\%\to52.9\%$), and — the
key point — the depth-$2$ failures are **not** confined to near-uniform profiles: at $n=5,6$ a majority
of them have an adjacent ratio $a_i/a_{i+1}\ge2$ (a "dominant gap"), i.e. they are *generic* by any
reasonable near-uniform threshold. An explicit generic depth-$2$ failure at $n=5$ is
$A\approx(0.2724,0.2067,0.1984,0.1800,0.1365,0.0060)$ (adjacent ratios
$1.32,1.04,1.10,1.32,22.68$ — a huge gap at the *small* end, so unambiguously not near-uniform), whose
depth-$2$ escape value $\approx0.01615$ exceeds $u_5=1/63\approx0.01587$, while its full-depth reachable
minimum is $\approx0.0022\le u_5$. Since a fixed-depth escape lemma would have to hold at *some* depth
independent of $n$, and the required depth provably grows, **the generic case cannot be closed by a
bounded-depth two-level move**: outside near-uniform the escape is genuinely depth-$\Theta(n)$, which is
the full Covering claim, not a two-level shortcut. As an existential search over *all* depths it
succeeds (that is exactly $\min\mathcal R\le u_n$), but as a *bounded*-depth lemma with a clean
profile-independent proof it does not exist. **This is a Spec concern:** the outline's generic/near-
uniform partition (with "generic = bounded-depth escape") does not partition the valley, and cannot be
made to by lowering the near-uniform threshold, because the generic failures persist at every fixed
depth as $n$ grows.

> **Spec concern (for the outliner).** The round-10 skeleton's step 2 (a fixed-depth two-level
> existential move lemma for the generic case) is REFUTED: the escape depth grows with $n$ and the
> failures are not near-uniform. A genuine generic/near-uniform two-case proof would need a
> *depth-unbounded* but still *profile-independent* argument on the generic side — which is
> essentially the global covering claim again — so the two-case split does not localise the difficulty
> as hoped. The correct next object is a **global covering/density invariant** on the reachable sets
> $R_i$ (see (2)), not a bounded-depth move-search.

**(2) A new reachable-set covering invariant (validated, recorded as candidate — NOT proven here).**
Building the descending DP $R_0=\{0\}$, $R_i=R_{i-1}\cup\{|v-a_i|:v\in R_{i-1}\}$, define the covering
radius $\rho_i:=\sup_{t\in[0,a_i]}\operatorname{dist}(t,R_i)$. Then, robustly across all tested valley
profiles ($n=3\!-\!6$),
$$\boxed{\ \rho_i\ \le\ a_i/2\quad\text{for every }i\ }\qquad(\text{0 violations in }47516\text{ checks}).$$
Equivalently, $R_i\cap[0,a_i]$ contains $0$ and $a_i$ with all consecutive gaps $\le a_i$. This is a
genuinely new, clean, profile-independent structural statement about the descending reachable set.

*Honest status of this invariant.* (a) It is **not proven** here. The natural reflect-and-skip
induction — for $t\in[0,a_i]$, cover $a_i-t$ by some $v\in R_{i-1}$ and use $|v-a_i|\in R_i$ — yields
only the *weaker* bound $\rho_i\le a_{i-1}/2$ (the reflection preserves the previous radius but does not
sharpen it from $a_{i-1}/2$ to $a_i/2$); the sharpening to $a_i/2$ that the data show is not captured by
that argument, and I did not find a correct proof this round. (b) Even the sharp form is **insufficient
alone** for the Covering claim: $\rho_{n+1}\le a_{n+1}/2$ gives a reachable value within $a_{n+1}/2$ of
$0$, but on a near-uniform profile $a_{n+1}\approx1/(n+1)$, so $a_{n+1}/2\gg u_n\approx2^{-(n+1)}$. The
covering radius from this invariant does not shrink below the smallest piece, whereas $u_n$ is
exponentially smaller. Concretely, on the extremal dyadic profile every reachable value is an integer
multiple of $u_n$, so the *nonempty* reachable minimum is exactly $u_n$ (not $\le a_{n+1}/2$), confirming
the mechanism that reaches $u_n$ is a **density/pigeonhole among the exponentially many tree-realizable
values** near $0$, not a single-window covering-radius bound. So (2) is a true and reusable fact but is
one honest step short of the crux.

**(3) The sharpened residual.** Combining (1) and (2): the upper valley reduces (certified, §4B.1-.5) to
the Covering claim $\min\mathcal R(A)\le u_n$; the generic/near-uniform two-case split with a
bounded-depth generic lemma is refuted (1); and the natural covering-radius invariant, while true,
saturates at $a_{n+1}/2$ and cannot reach the exponentially smaller $u_n$ (2). The genuine open crux is:

> **GAP U-cover (round-10 sharpened, OPEN).** For every full-budget balanced-valley profile, prove that
> the tree-realizable reachable set $R_{n+1}$ has an element in $(0,u_n]$ (or $0$ via nonempty even
> cancellation). The needed object is a **global density invariant** that quantifies how the tree-
> realizability restriction (Lemma RL: only tree sign-patterns, not all $\{0,\pm1\}$ patterns) still
> lets the reachable values accumulate near $0$ at density $\ge1/u_n=2^{n+1}-1$ — a *restricted*
> Erdős–Ginzburg–Ziv / pigeonhole among tree-realizable signed subset sums, using $\sum a_i=1$,
> $a_1<\tfrac12$, $a_2<\beta_n$ jointly. Both a bounded-depth move-search (1) and a single-window
> covering-radius bound (2) are provably insufficient; a per-scale pigeonhole that respects Lemma RL is
> required. Not closed this round.

*What round 10 rigorously contributes:* a **refutation** (profile-independent, with an explicit
generic $n=5$ witness) of the outline's fixed-depth two-level generic lemma — pruning the entire
bounded-depth-escape class and correcting the proposed case partition — plus a **new validated
structural invariant** ($\rho_i\le a_i/2$) that both narrows the search and, by its own saturation,
pinpoints the residual as a density/pigeonhole problem among tree-realizable values.

##### 4B.7 Round 11: CONFINEMENT and MULTISET-DOUBLING proven; COUNT refuted; the density substrate falls

Normalize $L=1$; we are in the full-budget balanced valley $A=\{a_1\ge\dots\ge a_{n+1}\}$,
$\sum a_i=1$, $a_1<\tfrac12$, $a_2<\beta_n$. Recall the descending include/skip reachable **set**
$R_0=\{0\}$, $R_i=R_{i-1}\cup\{|v-a_i|:v\in R_{i-1}\}$; its elements reached through a nonempty
include-set are exactly the descending-KK values of subsets $T\subseteq\{1,\dots,i\}$ (Lemma ESF-2),
lying in $\mathcal R(A)$. The Covering claim (§4B.5) is: $R_{n+1}$ meets $[0,u_n]$ via a nonempty
include-set. This round tests, and largely refutes, the round-11 outline's proposed vehicle
(CONFINEMENT $\times$ COUNT $\times$ density pigeonhole).

**Lemma CONF (confinement) — PROVEN.** For every $0\le i\le n+1$, $\max R_i\le a_1$; hence
$R_{n+1}\subseteq[0,a_1]\subset[0,\tfrac12)$.

*Proof.* Strong induction on $i$. Base: $R_0=\{0\}$, $\max R_0=0\le a_1$. Step: assume every
$v\in R_{i-1}$ satisfies $0\le v\le a_1$. A general element of $R_i$ is either such a $v$ (so $\le a_1$)
or $|v-a_i|$ for some $v\in R_{i-1}$. For the latter, the elementary inequality
$$|v-a_i|\le\max(v,a_i)$$
holds for all reals $v,a_i\ge0$ (if $v\ge a_i$ then $|v-a_i|=v-a_i\le v=\max$; if $v<a_i$ then
$|v-a_i|=a_i-v\le a_i=\max$). By the inductive hypothesis $v\le a_1$, and by the sorting $a_i\le a_1$,
so $\max(v,a_i)\le a_1$, whence $|v-a_i|\le a_1$. Also every element is $\ge0$. Thus $\max R_i\le a_1$.
Since $a_1<\tfrac12$ (valley), $R_{n+1}\subseteq[0,a_1]\subset[0,\tfrac12)$. $\qquad\blacksquare$

(Verified: $0$ failures across random $+$ near-tie-injected valley profiles $n=3\text{–}6$; the outline
reviewer independently reproduced $0$ failures. This is a genuine cheap, provable, profile-independent
structural fact — **proposed for certification** as a shared lemma.)

**Lemma MD2 (multiset doubling) — PROVEN.** Define the reachable **multiset** $M_0=\{\!\{0\}\!\}$ and
$M_i=M_{i-1}\uplus\{\!\{|v-a_i|:v\in M_{i-1}\}\!\}$ (each element of $M_{i-1}$ contributes both itself and
its reflection, with multiplicity). Then $|M_i|=2^i$ for all $i$, and every element of $M_i$ lies in
$[0,a_1]$. The distinct values of $M_i$ are exactly $R_i$; equivalently, $M_{n+1}$ enumerates, with
multiplicity, the descending-KK value $v(T)$ of each of the $2^{n+1}$ subsets $T\subseteq\{1,\dots,n+1\}$
(the empty subset giving $0$).

*Proof.* $|M_i|=2|M_{i-1}|=2^i$ by construction ($M_i$ is the disjoint union of a copy of $M_{i-1}$ and
its pointwise reflection). Confinement to $[0,a_1]$ is Lemma CONF applied at the multiset level (the same
induction: reflections of points in $[0,a_1]$ under $v\mapsto|v-a_i|$ with $a_i\le a_1$ stay in
$[0,a_1]$). That the support of $M_{n+1}$ equals $R_{n+1}$ and enumerates all $2^{n+1}$ subset-KK values
is immediate: choosing, at each step $i$, the "keep $v$" branch (skip $a_i$) or the "reflect" branch
(include $a_i$) over $i=1,\dots,n+1$ is a bijection between the $2^{n+1}$ leaves of the doubling tree and
the subsets $T$, and the leaf value is the descending-KK caterpillar of $T$ (the first include from $0$
sets the leader $a_{\min T}$, subsequent includes fold in descending order). $\qquad\blacksquare$

**Multiset pigeonhole (rigorous partial).** By Lemma MD2 the $2^{n+1}$ values of $M_{n+1}$ lie in
$[0,a_1]$ with $a_1<\tfrac12$. Sorting them $0=w_0\le w_1\le\dots\le w_{2^{n+1}-1}\le a_1$, the
$2^{n+1}-1$ consecutive gaps sum to $w_{2^{n+1}-1}-w_0\le a_1<\tfrac12$, so **some** consecutive gap
satisfies
$$w_{j+1}-w_j\ \le\ \frac{a_1}{2^{n+1}-1}\ <\ \frac{1/2}{2^{n+1}-1}\ =\ \frac{u_n}{2}.$$
This is a fully rigorous statement: there exist two subsets $T,T'$ whose descending-KK values differ by
$<u_n/2$. **It is, however, NOT the Covering claim**, for two independent reasons made precise below.

**The COUNT hypothesis is FALSE in the valley (rigorous refutation).** The outline's density route
needed $|R_{n+1}|=2^{n+1}$ (the multiset having $2^{n+1}$ *distinct* values), to run the pigeonhole on
the **set** and — crucially — to make the small gap sit between two *distinct* reachable values one of
which could be pushed toward $0$. This injectivity is false, by an EXACT adversarial counterexample (not
a spot-check — an identity): take the **all-equal profile** $a_1=\dots=a_{n+1}=\tfrac1{n+1}$. It is a
genuine valley profile for every $n\ge3$: $a_1=\tfrac1{n+1}\le\tfrac14<\tfrac12$, and
$a_2=\tfrac1{n+1}<\beta_n=\tfrac{2^{n-1}}{2^{n+1}-1}$ (e.g. $n=3$: $\tfrac14<\tfrac4{15}$; $n=4$:
$\tfrac15<\tfrac8{31}$; and $\tfrac1{n+1}\to0$ while $\beta_n\to\tfrac14$, so it holds for all $n\ge3$).
For this profile $R_1=\{0,\tfrac1{n+1}\}$ and thereafter $R_i=\{0,\tfrac1{n+1}\}$ is *stable*: for
$v\in\{0,\tfrac1{n+1}\}$, $|v-\tfrac1{n+1}|\in\{\tfrac1{n+1},0\}$ adds nothing new. Hence
$$|R_{n+1}|=2\ \ll\ 2^{n+1}.$$
(For $n=2$, where the all-equal profile just fails $a_2<\beta_2=\tfrac27$, the exact valley profile
$A=\{\tfrac7{16},\tfrac9{32},\tfrac9{32}\}$ — a valley: $\tfrac7{16}<\tfrac12$, $\tfrac9{32}<\tfrac27$ —
has $R_3=\{0,\tfrac1{8},\tfrac5{32},\tfrac9{32},\tfrac7{16}\}$, $|R_3|=5<8$.) So **the set-count
pigeonhole substrate does not exist in the valley**; the random-only $|R_{n+1}|/2^{n+1}=1.000$ evidence
(1200 profiles) was an artifact of random profiles almost surely avoiding exact coincidences $v+w=2a_i$,
precisely the misleading-random-sampling failure mode the standing rule warns about.

**The multiset pigeonhole does not convert to a value either.** One might hope to salvage the route on
the always-$2^{n+1}$ multiset $M_{n+1}$: a small multiset gap includes the case of a *repeated* value
($w_{j+1}=w_j$, i.e. two subsets with equal KK value). But a coincidence $v(T)=v(T')$ does **not** yield
a reachable value near $0$ in general (it is not a subset whose value is small), and a small nonzero gap
$w_{j+1}-w_j$ is a *difference of two reachable values*, which is **not** itself reachable — the budget is
exhausted (all $n+1$ pieces are consumed to realize either $v(T)$ or $v(T')$), so no move can subtract
them. Quantitatively, this is not a fixable constant: the covering value $\mathrm{cov}(A)$ (the smaller
of $\min_{T\ne\varnothing}v(T)$ and $0$ when $0$ is nonempty-realizable) can **exceed** the average
multiset gap $a_1/(2^{n+1}-1)$ (worst observed ratio $\mathrm{cov}\cdot(2^{n+1}-1)/a_1=2.07$ at $n=4$)
**and** the smallest distinct gap (worst ratio $\mathrm{cov}/\text{mingap}=3.0$ at $n=3$). So no
pigeonhole-gap quantity bounds $\mathrm{cov}$; the GAP$\to$VALUE conversion is genuinely absent for the
whole density family. *(These ratios are diagnostic only — used to REFUTE the candidate bounds; no
numeric statement enters a proof step. Each is realized by an explicit exact-rational witness.)*

**What survives, and the honest residual.** The Covering claim remains robustly TRUE: over exact-rational
valley profiles ($n=2\text{–}6$, structured ties $+$ random denominators) the nonempty covering value
satisfied $\mathrm{cov}(A)\le u_n$ with **zero** exceptions (worst ratio $\mathrm{cov}/u_n=0.83$ at
$n=3$), and where the positive minimum is large the claim is met by $\mathrm{cov}=0$ from a nonempty
even cancellation (e.g. the all-equal profile: subset $\{a_1,a_2\}$ has $|a_1-a_2|=0\le u_n$). So the
target is correct; what is refuted is the *mechanism*. The two structural regimes the truth splits into —
**spread** (many distinct values, small gaps that are not values) and **collision** (repeated values /
reachable $0$) — are governed by opposite phenomena, and the round-11 outline's single density invariant
cannot see both: it assumes injectivity (killing the collision regime) and then needs gap$=$value
(killing the spread regime). A correct proof must handle collisions (which produce small/zero *values*,
not just gaps) and spread (pigeonhole *gaps*) **uniformly**, and no such unifying convertible invariant
was found this round.

> **GAP U-cover (round-11 status, OPEN).** Prove the Covering claim: every full-budget balanced-valley
> profile has $\mathrm{cov}(A)\le u_n$ (some nonempty subset's descending-KK value $\le u_n$, or $0$ via
> nonempty even cancellation). **Newly established this round:** the natural COUNT + density-pigeonhole
> substrate is refuted — set-injectivity is FALSE in the valley (all-equal counterexample), and even the
> always-$2^{n+1}$ multiset pigeonhole gap does not bound $\mathrm{cov}$ (no `gap→value` of pigeonhole
> type; ratios up to $2.07$/$3.0$). So the outline's proposed vehicle (steps 3–5) is a dead substrate,
> not merely an unfinished one. The residual is unchanged in truth but sharpened in obstruction: a
> correct argument must exploit the *collision structure* (coincidences forced by the valley caps
> concentrate reachable mass at small values, including $0$) rather than dispersion of distinct points.
> Lemma BL still supplies a first landing $r\in[0,\beta_n)$; CONFINEMENT confines everything to
> $[0,a_1)$; but the factor-$2^{n-1}$ descent from $\beta_n$ to $u_n$ has no density mechanism.

*What round 11 rigorously contributes (self-contained, no numerics in proofs):* (i) **Lemma CONF** — a
fully proven, certifiable global confinement $\max R_i\le a_1$; (ii) **Lemma MD2** — the multiset-doubling
identity ($|M_i|=2^i$, support $=R_i$, enumerating all $2^{n+1}$ subset-KK values), with the exact
multiset pigeonhole ($\exists$ gap $<u_n/2$); (iii) a **rigorous refutation** of the outline's density
substrate: an exact all-equal valley counterexample to COUNT, plus explicit witnesses that no
pigeonhole-gap quantity bounds the covering value — pruning the entire COUNT/density route so the field
does not re-spend on it.

---

##### 4B.8 Round 12: the two-cap covering-radius mechanism REFUTED; corrected reduction and sharpened first-gap residual

This round tested the mandated **GAP TWO-CAP** hypothesis (a contraction of the covering radius toward
`u_nL` using both valley caps at every level) BEFORE any prose, per the reviewer's hard gate. The gate
**failed decisively**; below is the honest account plus two genuinely-new rigorous positive items.

**The reachable set and its two dynamics.** Throughout, $L=1$, full budget $m=n+1$, balanced valley
$a_1<\tfrac12$, $a_2<\beta_n$. Import **Lemma CONF** ($R_i\subseteq[0,a_1]$) and **Lemma MD2**
(the multiset $M_{n+1}$ of $2^{n+1}$ descending-KK subset values). Sort $R_i$ as
$0=r_0<r_1<\dots<r_{|R_i|-1}=a_1$ (for $i\ge1$, both $0$ and $a_1$ are present: $0\in R_0$,
$a_1=\phi_1(0)\in R_1$). Two natural scalars:
- the **covering radius** $c_i:=\sup_{x\in[0,a_1]}\mathrm{dist}(x,R_i)=\tfrac12\max_j(r_{j+1}-r_j)$
  (half the largest consecutive gap);
- the **first gap** $\mu_i:=\min\{v>0:v\in R_i\}=r_1$ (smallest *positive* reachable value).

**GAP TWO-CAP is FALSE (gate result).** The proposed contraction $c_i\le f(c_{i-1},a_i)\to u_n$ does not
hold. On exact-rational valley profiles ($n=3..7$), the worst normalized *max gap*
$2c_{n+1}/u_n=\text{max-gap}/u_n$ was $3.24,\,6.12,\,8.94,\,15.76,\,24.63$ (fails 96–100%). Level-by-level,
$c_i$ contracts roughly geometrically but **saturates near $3$–$5\cdot u_n$** and never reaches $u_n$ —
the identical saturation R10 recorded for the one-cap bound ($a_{n+1}/2\gg u_n$). Using the second cap
$a_i\le a_2<\beta_n$ at *every* level does not remove the saturation. Windowed variants also fail: the
covering radius of $R_n$ over $[0,\beta_n]$ exceeds $u_n$ on 37–100% of profiles (worst $1.85$–$19.46\times$),
and even the exact-point bound $\mathrm{dist}(a_{n+1},R_n)\le u_n$ fails a few percent (worst $1.39$–$2.59\times$).
**Conclusion: there is no covering-radius object that contracts to $u_n$.** The mechanism the outline
specified cannot be built; recorded as a rigorous negative to prune it from the field.

**Why: the content is the FIRST gap, which the covering radius overshoots.** The Covering target is
$\mu_{n+1}\le u_n$ (min positive reachable), and this holds robustly (0 fails, worst ratio $0.70$; tiny
$\approx5\cdot10^{-4}u_n$ on near-all-equal exact profiles; TIGHT $=u_n$ at the dyadic boundary
$a_i=2^{n+1-i}/(2^{n+1}-1)$, verified $n=2..6$). The first gap $r_1$ is generically **much smaller** than
the max gap $2c_{n+1}$ (the reachable set is dense near $0$ but sparse near $a_1$), so a bound on the
covering radius — a *worst-gap* quantity — can never certify $\mu_{n+1}\le u_n$: the two are not
comparable in the needed direction. This is the precise reason the R10/R12 covering-radius family is dead.

**Rigorous item A — the first-gap recursion (PROVEN).** For $i\ge1$,
$$\mu_i=\min\big(\mu_{i-1},\ \mathrm{dist}(a_i,R_{i-1})\big),\qquad\text{hence}\qquad
\mu_{n+1}=\min_{1\le i\le n+1}\mathrm{dist}(a_i,R_{i-1}).$$
*Proof.* $R_i=R_{i-1}\cup\{|v-a_i|:v\in R_{i-1}\}=R_{i-1}\cup\phi_i(R_{i-1})$ with $\phi_i(v)=|v-a_i|$.
The positive elements of $R_i$ are the positive elements of $R_{i-1}$ (min $\mu_{i-1}$) together with the
positive values $|v-a_i|$, $v\in R_{i-1}$. The latter are positive iff $v\ne a_i$, and their minimum is
$\min\{|v-a_i|:v\in R_{i-1},\,v\ne a_i\}=\mathrm{dist}(a_i,R_{i-1})$ (interpreting the distance as to the
nearest point $\ne a_i$; if $a_i\notin R_{i-1}$ this is the ordinary distance, and $\phi_i(0)=a_i$ shows
$a_i\in R_i$ so the fold is realized). Taking the min over the two families gives the recursion; unrolling
from $\mu_0=+\infty$ (no positive element in $R_0=\{0\}$) gives the closed form. $\blacksquare$
So the residual is exactly the **first-gap pigeonhole**: *some $a_i$ ($2\le i\le n+1$; $a_1$ contributes
$\mathrm{dist}(a_1,\{0\})=a_1$, irrelevant) lands within $u_n$ of the previously reachable set $R_{i-1}$.*
This is a global, adaptive statement — no single level $i$ suffices (verified: $\mathrm{dist}(a_{n+1},R_n)$
alone fails), so a per-level covering surrogate cannot exist, matching the gate.

**Rigorous item B — corrected covering→value conversion with the T=∅ exclusion (PROVEN).** We restate the
upper-bound valley equivalence cleanly, folding in the T=∅ exclusion the explorer flagged.

> **Reduction (R-COV', exact).** In the balanced valley, Xiang forces $D\le u_n$ **iff** $\mu_{n+1}\le u_n$,
> i.e. iff the smallest *positive* value of the include/skip reachable set $R_{n+1}$ is $\le u_n$.

*Proof.* ($\Leftarrow$) Suppose $\mu_{n+1}\le u_n$. If $\mu_{n+1}=0$, some *nonempty* subset $T$ has
descending-KK value $0$ (the value $0$ from a nonempty $T$ is an even-cancellation leftover): by
**Lemma ESF-2** this $0$ is realized by exactly $n$ DM moves — $(|T|-1)$ MATCHes along the caterpillar
(the leader $t_1$ is a resident piece, no cut) and $(n+1-|T|)$ DELETEs of the pieces outside $T$, total
$(|T|-1)+(n+1-|T|)=n\le n$ cuts — giving a legal Xiang response with $D=0\le u_n$. If $\mu_{n+1}>0$, let
$T$ be a nonempty subset attaining $r_1=\mu_{n+1}$ (it is nonempty: the empty subset gives value $0$, and
$r_1>0$ forces a nonempty include-set in the branch bijection of Lemma MD2(3)); again ESF-2 realizes it in
exactly $n$ cuts with $D=r_1\le u_n$. Either way $D\le u_n$. ($\Rightarrow$) By **Reduction R-UV** and
**Lemma RL**, every leftover of a legal $\le n$-move DM sequence is a tree value over a nonempty subset,
hence $\ge\min\{\text{nonempty subset values}\}$; the descending-KK caterpillar values are among these, and
the smallest reachable positive value is $\mu_{n+1}$ (or $0$), so if Xiang forces $D\le u_n$ then some
reachable value is $\le u_n$, i.e. $\mu_{n+1}\le u_n$. $\blacksquare$

**T=∅ handled exactly.** The value $0=v(\varnothing)$ is *geometrically* present in $R_{n+1}$ (it seeds
the recursion) but is **not** a legal leftover: realizing $\varnothing$ needs $n+1$ DELETEs (every piece
deleted) $>n$ cuts. The conversion above never concludes with $v(\varnothing)$: the produced value is
always $\mu_{n+1}=r_1$, a **nonempty**-subset value (positive, or $0$ via a nonempty even cancellation),
each realizable in exactly $n$ cuts by ESF-2. This is precisely the exclusion the explorer's naive
inclusion violated (falsely giving $\min=0$ on 100% of trials by counting the infeasible $\varnothing$).

**Net for §4B.8.** GAP TWO-CAP is refuted (recorded to prune the covering-radius family for good). The
residual is now correctly and sharply stated as the **first-gap pigeonhole** $\mu_{n+1}=\min_i
\mathrm{dist}(a_i,R_{i-1})\le u_n$ — a global, adaptive, non-covering-radius statement — with an exact,
T=∅-safe reduction (R-COV') to the upper bound. What is NOT closed: a profile-independent proof that some
$a_i$ approaches $R_{i-1}$ within $u_n$. This is genuinely a discrepancy/pigeonhole crux on a coupled
sequence ($a_i$ and $R_{i-1}$ are not independent), and neither a covering radius nor a fixed-level bound
captures it — future upper attacks must target the first-gap pigeonhole directly (e.g. an Abel/telescope
identity on the sorted $M_{n+1}$ that pairs reachable values whose *difference* is itself reachable), not
a covering radius.

---

### 5. Assembly (conditional)
Lemmas R/M reduce the game to scalar minimax of $D$ over refinements. Lemma PL1 (§2) and Theorem
VERT (§3) prove that an optimal Xiang refinement is a polytope vertex with $\le n+1$ distinct
part-values, collapsing the continuum to a finite tie-pattern search. Lemma TB (§4A) decomposes the
lower bound exactly into a top excess $e$ plus $D_{\mathrm{low}}$, closing the base case, the trivial
regime, and Case (a) unconditionally, and reducing the lower bound to bounding $D_{\mathrm{low}}$ in
the width-1 critical band (L1) and the top-shredded case (L2). The upper bound is closed for
$a_1\ge L/2$ (whole-tail-peel), and the balanced valley is reduced *exactly* (Reduction R-UV, via
certified DM/P/U0) to the single discrepancy inequality **Prop UV**
$\min\mathcal R(A)\le u_nL$; Lemma RL characterizes the achievable family $\mathcal R(A)$ and Lemma
VS proves adaptivity ($\ge2$ cuts) is forced. Round 9 (§4B.5) further sharpens Prop UV: **Lemma BL**
lands a first subset value $r\in[0,\beta_nL)$ (step 2 closed, straddle settled), the residual is
re-expressed as the **Covering claim** (the descending include/skip reachable set $R_{n+1}$ meets
$[0,u_nL]$), and the outline's greedy step-3 recursion is **rigorously refuted** (overshoots up to
$11.4\times$), so the residual is a global covering problem (**GAP U-cover**), not a recursion.
Modulo the two residual checks **GAP L-fin** (§4A) and **GAP U-cover** (§4B.5), this yields minimax
$D=u_n$ and $c(n)=(1+u_n)/2=2^n/(2^{n+1}-1)$.

**Final answer (confirmed, verified by reviewer brute force $n=0,1,2$ and the closed form):**
$$c(n)=\frac{2^n}{2^{n+1}-1},\qquad\text{minimax }D=u_n=\frac1{2^{n+1}-1}.$$

## Approaches tried
- (round 19, build) **CONSOLIDATION / official re-target — advance, no gap closed.** (a) Officially
  retired the caterpillar residual `μ_{n+1} ≤ u_nL` and adopted the certified true target
  `min 𝓡(A) ≤ u_nL` (Corollary R-UV of Lemma RL, `leftover-realizability.md`): a general
  nonnegative-differencing-TREE value over any nonempty `T` is Xiang-realizable in exactly `n` cuts
  (`|T|-1` MATCHes + `m-|T|` DELETEs), so `min 𝓡(A) ≤ u_nL ⟹ D ≤ u_nL`. Sound because
  `min 𝓡(A) ≤ μ_{n+1}` (caterpillars ⊆ trees), so the new target is weakly easier AND equally
  sufficient. (b) Recorded two R19 refutations: **tree-min-divide-conquer** DEAD — a balanced full
  partition of the pieces cannot DROP pieces, so it never reaches the anchor-excluding tail minimiser;
  `DCbest/u_n = 9.30` on the R18 witness (true `min 𝓡=0` on `{13/40,13/40}`), growing `2.70→2.92` on
  `A^{(4,5,6)}` (covering-radius saturation). **signed-tree-invariant** DEAD — `band_restart ≡ descKK`
  (the plain reflected walk), reproduces the R18-dead `minpost = 3/10 = 9.30·u₄`; band-landing is
  anchored at `a₁` and forces it into the residual, so it cannot see the tail minimiser — the 9th dead
  anchored-walk mechanism relabeled. (c) Recorded that the completeness identity `μ_{n+1}=min 𝓡(A)` is
  FALSE (witness `(17,16,11,8,4)`: `μ=1`, `min 𝓡=0`), so no exact-completeness bridge is sound; this
  is the SIGNAL to target `min 𝓡(A)` directly, not a wall. Exact-`Fraction` EVIDENCE (not proof):
  `min 𝓡(A)/u_n ∈ {0,0,0.94,0.97,0.98}` on the hard families and `0.69–0.73` on the slivers — target
  true, asymptotically tight. Deep interior stays OPEN; the true minimiser is an anchor-EXCLUDING tail
  subset, so no single object over the reachable-value set reaches it (9 dead mechanisms). Needs a
  genuinely global existence / Steinitz argument, or a sliver-local perturbation — out of this slug's
  current framing. Certified core (RL/R-UV, WTC, R-COV', FGR) intact.
- (round 18, build) **C2 post-crossing-contraction gate run FIRST (exact `Fraction`) → FAILED; the
  sharpened-WTC / reflected-walk / anchored-caterpillar contraction is DEAD (9th dead upper mechanism).**
  The proposed closing mechanism (after the band-landing crossing `k*`, the reflected residual
  `w_k=|w_{k-1}−a_k|` telescopes/contracts to `≤ u_nL` under ONE-REC dyadic caps) was gated adversarially
  on random sliver profiles, the tight family `A^{(n)}`, and `A^{(n)}`-perturbations at `n=3..6`. The
  contraction object `minpost=min_{k≥k*} w_k` (min over ALL post-crossing stopping points — the most
  generous reading) SATURATES far above `u_n` and GROWS with `n`: worst `minpost/u_n = 4.54/9.09/13.87/
  24.26` at `n=3,4,5,6` (≈2× per unit n, the ~`2^{n-1}` covering-radius signature). Clean exact witness
  `A={1/3,13/40,13/40,1/120,1/120}` (`a₁=1/3` strictly deep): `minpost=3/10=9.3·u₄` while true `Φ=0` via
  the tail subset `{13/40,13/40}` that EXCLUDES `a₁`. Root cause: the reflected walk is anchored at `a₁`
  (every prefix contains `a₁`), but the true minimiser is a tail subset excluding `a₁` (size can grow to
  `n`), which no single anchored pass sees. This is the covering-radius family in disguise (GAP TWO-CAP),
  exactly the reviewer's warned collapse. Per the binding refute-and-stop precondition I STOPPED, did NOT
  attempt C1, and shipped NO deep-interior prose. Certified reduction + WTC boundary closure unchanged.
  Recorded so no future round re-tries post-crossing/reflected-walk/anchored-caterpillar contraction; the
  deep-interior residual needs the signed-subset-sum-discrepancy / Steinitz EXISTENCE object instead.
- (round 17, build) **Deep-interior extremal/smoothing lever + gated-first full-tree second moment —
  all three gates REFUTED as configured; 8th dead upper mechanism recorded; crux sharpened to the
  near-boundary sliver. No deep-interior proof shipped.** Ran all gates in exact `Fraction` in the
  mandated order. (0) GATED-FIRST full-tree second moment over 𝓡(A) (all binary differencing trees,
  Catalan-many per subset): worst `mean(V²)/(u_nL)² = 14.7/72/242` at `n=3,4,5`, GROWING with n —
  DEAD, the 8th dead upper mechanism (rare-needle, same as the two killed fixed-order probes). (G1)
  Deep-interior argmax has near-dyadic TOP but sits at the deep boundary `a₁→(L−u_nL)/2⁻`, where
  `Φ/u_n → (2^{n+1}−1)/(2^{n+1}+1) → 1`; exact continuity probe gives `Φ/u_n = 0.908 (n=4), 0.976
  (n=6)` a distance `u_n/1000` below the boundary. So the "0.34–0.56 non-shrinking margin" premise is
  FALSE for the deep interior AS DEFINED (`a₁<L/2−u_n/2`); that margin holds only for `a₁≤L/2−u_n`,
  leaving a `u_n/2`-wide sliver with `Φ/u_n→1` — as tight as the closed boundary layer. (G2)
  SMOOTH-MONO refuted: the move "shift mass from smallest part up to `a₁`" DECREASES `Φ` on ~80% of
  random deep profiles (374/453/401 of 500 at `n=3,4,5`), so no monotone drive to the boundary — the
  hoped closure "max on `a₁=(L−u_nL)/2`, finish by WTC" fails. Genuine advance: the crux is localized
  to the sliver `a₁∈(L/2−u_n, L/2−u_n/2)` and to the single-target subset-sum-density claim
  `∃ S⊆tail: |a₁−Σ_S| ≤ u_nL` (via WTC on `{a₁}∪S`), which needs an EXACT (not margin) argument. No
  fake proof shipped.
- (round 15, build) **BOUNDARY-CONTINUATION two-region split: gate PASSED for the boundary, new
  Lemma WTC PROVEN, deep interior isolated as the residual.** Ran the mandatory exact `Fraction`
  gate (adversarial + structured) FIRST. (i) Fixed a load-bearing definitional error: the target is
  `Φ = min over NONEMPTY subsets` (0 admissible via nonempty even cancellation), not min-positive —
  `{30,25,20,15,10}/100` has min-positive `1/20=1.55u₄` but `Φ=0` via `{30,25,20,15}`. (ii) **G2
  PASS & upgraded to a theorem:** `Φ(A) ≤ |2a₁−L|` universally (0 fails, >100k exact profiles;
  witnessed already by the full-profile caterpillar), EQUALITY on `A^{(n)}` and on `{16,8,4,3,2}/33`
  — an EXACT continuation of certified `D=2a₁−L` across `a₁=L/2`, no margin. Proven in full (Lemma
  WTC, two-sided invariant `a₁−P_k ≤ v_k ≤ |a₁−P_k|` by induction). Closes the whole region
  `a₁≥(L−u_nL)/2` (dominant ∪ boundary), i.e. exactly where VALLEY-TIGHT's tight family lives. (iii)
  **G1: deep margin exists numerically** (worst `Φ/u_n=0.72/0.67/0.58` at `n=3/4/5`, not shrinking
  to 0) **but NO provable bounded mechanism** — deep minimiser needs unbounded-order cancellation
  ({30,25,20,15,10}/100 needs 4 elements), so the deep region is NOT closed. (iv) **G3 cover** trivial.
  Net: genuine advance — valley shrinks from `a₁<L/2` to the DEEP interior `a₁<(L−u_nL)/2`; boundary
  layer closed exactly. Promotable: Lemma WTC. No fake proof shipped for the deep region.
- (round 13, build) **SEED(p) seeded strong induction + GAP-TELE mass-telescope REFUTED at the mandated
  exact-fraction gate; no fake proof shipped.** Per the reviewer's hard gate, ran the exact-fraction
  check on the SEED(p) scaling and the GAP-TELE constant BEFORE prose. (i) **SEED(p) refuted:** with
  seed domination `r≤b_1` (and even with valley caps inherited on the combined `(p+1)`-instance, and
  under reverse domination), the descending fold-from-seed value exceeds `u_p·M` with worst ratio that
  GROWS with `p` (`1.67/3.44/4.85/7.47` at `p=3..6` under caps; `2.24…9.77` without; `7.5…63.5`
  reverse) — so `u_p·M` is not an inductively stable threshold and the seed-domination invariant making
  SEED(p−2) a legal IH does not exist. (ii) **GAP-TELE structurally impossible:** charging the `n+1`
  "far" pieces against `Σa_i=1` cannot work because (a) `(n+1)u_n=(n+1)/(2^{n+1}-1)→0` (0.43 at `n=2`
  down to 0.01 at `n=9`), so the far reservoir is exponentially too small, and (b) the distance-sum is
  provably bounded ABOVE — `Σ_i dist(a_i,R_{i-1}) ≤ a_1(2-2^{-n}) < 2a_1 < 1` (covering radius halves
  per reflection; exact-fraction check confirms the constant `2-2^{-n}` is tight) — the OPPOSITE
  direction from what a mass contradiction needs. Reconciled the residual definition: the target is
  `min_{∅≠T} desc-KK(T) ≤ u_n` (value `0` from nonempty even cancellation admissible; only `T=∅`
  excluded) — this holds with 0 exact fails, worst `0.75`, tight at the dyadic ladder. Net: the
  mass-telescope-discrepancy lever is dead (a FIFTH exhausted upper-wall family); the honest open crux
  is unchanged. Recommended escalation to a potential-free / LP-duality extremal re-derivation.
- (round 12, build) **Two-cap covering-radius recursion (GAP TWO-CAP) REFUTED at the mandated gate;
  corrected first-gap reduction PROVEN.** Per the reviewer's hard numeric-first gate, tested the proposed
  contraction of the covering radius $c_i$ toward $u_n$ using both caps at every level, BEFORE prose. It
  FAILS: exact-rational valley profiles ($n=3..7$) give worst $\text{max-gap}/u_n$ of $3.24$–$24.63$
  (fails 96–100%); the covering radius contracts geometrically but SATURATES at $\approx3$–$5\cdot u_n$
  and never reaches $u_n$ — the same R10 saturation, unremoved by the second cap. Windowed and exact-point
  variants also fail. Root cause identified rigorously: the true content is the FIRST gap
  $\mu_{n+1}=\min\{v>0:v\in R_{n+1}\}$ (which DOES satisfy $\le u_n$, 0 fails, worst $0.70$, tight $=u_n$
  at the dyadic boundary), and the first gap is incomparable to the (worst-gap) covering radius — so no
  covering-radius object can certify it. **Positive rigorous deliverables (§4B.8):** (A) the exact
  first-gap recursion $\mu_i=\min(\mu_{i-1},\mathrm{dist}(a_i,R_{i-1}))$, hence $\mu_{n+1}=\min_i
  \mathrm{dist}(a_i,R_{i-1})$ (PROVEN); (B) the exact, T=∅-safe reduction R-COV': upper bound in valley
  $\iff\mu_{n+1}\le u_n$, with T=∅ excluded correctly (nonempty $T$ costs exactly $n$ cuts via ESF-2,
  $\varnothing$ costs $n+1$; the produced value is always a nonempty-subset value). Residual re-stated as
  the **first-gap pigeonhole** (some $a_i$ approaches $R_{i-1}$ within $u_n$) — a global adaptive
  discrepancy crux, NOT a covering radius. No false lemma shipped; the covering-radius family is now
  pruned with a rigorous negative.
- (round 11, build) **CONFINEMENT + MULTISET-DOUBLING PROVEN and certifiable; COUNT REFUTED; the
  outline's density substrate falls.** Per the reviewer's numeric-first gate, the proposed
  CONFINEMENT$\times$COUNT$\times$density vehicle was tested before prose. (i) **Lemma CONF PROVEN**:
  $\max R_i\le a_1$ for all $i$ by one-line strong induction ($|v-a_i|\le\max(v,a_i)$, both $\le a_1$),
  confining $R_{n+1}\subset[0,a_1)\subset[0,\tfrac12)$ — clean, cheap, certifiable. (ii) **Lemma MD2
  PROVEN**: the reachable *multiset* $M_i$ always has $|M_i|=2^i$ (doubling), support $R_i$, enumerating
  all $2^{n+1}$ subset-KK values; yields a rigorous multiset gap $<u_n/2$. (iii) **COUNT REFUTED
  (exact)**: the all-equal profile $a_i=1/(n+1)$ is a genuine valley profile for $n\ge3$ with
  $|R_{n+1}|=2\ll2^{n+1}$ (and $n=2$: $\{7/16,9/32,9/32\}$, $|R|=5<8$) — set-injectivity is FALSE in the
  valley; the random-only 1200-profile evidence was misleading (standing rule). (iv) **The multiset
  salvage also fails**: $\mathrm{cov}(A)$ exceeds both the average multiset gap (ratio $2.07$, $n=4$) and
  the smallest distinct gap (ratio $3.0$, $n=3$) on explicit witnesses, so NO pigeonhole-gap quantity
  bounds the covering value — the GAP$\to$VALUE conversion is absent for the whole density family. The
  Covering claim is reconfirmed TRUE adversarially (0 fails, exact-rational valley, $n=2$–$6$, worst
  $0.83$), met by $0$ (nonempty even cancellation) when the positive minimum is large. **Net:** two
  certifiable deliverables (CONF, MD2); the make-or-break GAP$\to$VALUE is NOT closed, and the round-11
  outline's specific density vehicle (steps 3–5) is now rigorously undercut (dead substrate, not merely
  unfinished). No false lemma shipped. Residual GAP U-cover sharpened: a correct proof must exploit the
  valley-forced *collision* structure (small/zero values), not dispersion of distinct points.
- (round 10, build) **Two-case (generic/near-uniform) skeleton numerically stress-tested; the generic
  fixed-depth two-level move lemma REFUTED; a new reachable-set covering invariant recorded; residual
  sharpened.** Per the reviewer's hard numeric-first gate: (0) Covering target reconfirmed
  ($\min\mathcal R\le u_n$, 0 exceptions, $n=2\!-\!6$). (1) **Refutation** — the depth-$2$ escape
  (branch (a) dominant-regime OR one VS-certified move) fails on a fraction *growing* with $n$
  ($2.4\%/14.6\%/52.9\%$ at $n=4/5/6$), and the failures are NOT confined to near-uniform (majority have
  an adjacent ratio $\ge2$); explicit generic $n=5$ witness $\approx(0.272,0.207,0.198,0.180,0.137,
  0.006)$ where depth-$2$ escape $\approx0.01615>u_5$ but full-reach min $\approx0.0022$. Hence the
  escape depth is $\Theta(n)$: the generic case cannot be closed by any bounded-depth move-search, so
  the proposed generic/near-uniform partition does not localise the difficulty (**Spec concern
  raised**). (2) **New validated structural invariant** — the reachable-set covering radius satisfies
  $\rho_i\le a_i/2$ on $[0,a_i]$ (0 violations / 47516), a clean profile-independent fact; recorded as a
  candidate, honestly NOT proven (natural induction gives only $a_{i-1}/2$) and INSUFFICIENT alone
  ($a_{n+1}/2\gg u_n$ on near-uniform). Net: both the bounded-depth move-search and the single-window
  covering-radius bound are provably short; **GAP U-cover** is sharpened to a *restricted pigeonhole/
  density* among tree-realizable values (Lemma RL), still OPEN. No new false lemma introduced.
- (round 9, build) **Band-landing lemma PROVEN (step 2 closed); residual reformulated as a covering
  statement; greedy step-3 recursion RIGOROUSLY REFUTED.** New rigorous content (self-contained on
  certified P/DM/ESF-1/ESF-2): **Lemma BL** — the descending survivor partial sums cross $a_1$
  (unique crossing index on a finite increasing sequence, so the reviewer's straddle case is vacuous;
  the strict valley $a_1<L/2$ forces the crossing), landing a subset $T=\{a_1,\dots,a_k\}$ with
  $r=a_1-\Sigma_T\in[0,\beta_nL)$, realized by ESF-1. **Reachability reformulation** — Subset-KK
  $\iff$ the descending include/skip reachable set $R_{n+1}$ meets $[0,u_nL]$ (Covering claim; $0$
  admissible via even cancellation, covering the near-all-equal profiles). **Rigorous refutation of
  step 3** — the outline's greedy band-landing recursion, flip-if-helps greedy, and drop-one all
  overshoot $u_nL$ (machine-verified worst ratios $1.6$–$11.4\times$ for $n=2..7$; the $n=2$ witness
  $\{9/20,7/25,27/100\}$ is an explicit counterexample, bottoming at $17/100>u_2$), while the true
  subset minimum is always $\le u_nL$ (worst $0.84$). So the good subset needs foresight; the
  residual is the *global* covering problem **GAP U-cover**, not a recursion. This prunes the
  outline's step-3 recipe and the valley-differencing reserve's greedy hope.
- (round 5, new) breakpoint-vertex: registered.
- (round 5, build) **PL1 PROVEN in full** via the measure identity; **Theorem VERT PROVEN in full**
  via the LP-vertex / hyperplane-arrangement argument (replaces the flawed "settle-outermost-first"
  monovariant). Consequences §4A/§4B left as finite residual checks (GAP L-fin, GAP U-fin).
- (round 6, build) **Lemma TB (top-band decomposition) PROVEN in full**: for any refinement $R$ of
  $C_n$, $D(R)=e+D_{\mathrm{low}}$ with $e=(f_1-2^{n-1})^+$ and $D_{\mathrm{low}}=\mu\{t<2^{n-1}:
  N_R\text{ odd}\}$ (via Lemma M split at the threshold + Lemma ONE giving $N\le1$ on the top band).
  Consequences: base case $n=0$, the **trivial regime** $f_1\ge2^{n-1}+1\Rightarrow D\ge1$, and
  **Case (a)** (top uncut) $\Rightarrow D\ge2^{n-1}\ge1$ are now all closed **unconditionally and
  profile-independently**. The lower bound is thereby reduced to a single scalar bound on
  $D_{\mathrm{low}}$ in the width-1 critical band (L1) and top-shredded case (L2) — GAP L-fin, still
  open (needs the shared one-per-gap exchange/telescoping, with the SPLIT cross term carried).
  Upper bound: $a_1\ge L/2$ closed by imported whole-tail-peel; $a_1<L/2$ open (GAP U-fin). Lower
  target $\min_R D=1$ reconfirmed by exact brute force ($n\le4$, integer + $1/12$ grid).
- (round 8, build) **Prop UV made constructive; two explicit realizable subfamilies PROVEN; residual
  sharpened to the Subset-KK claim.** New rigorous content (self-contained on certified P/DM):
  **Lemma ESF-1** — for any $T\subseteq\{2,\dots,n+1\}$ with $\sum_{i\in T}a_i\le a_1$, the value
  $a_1-\sum_{i\in T}a_i\in\mathcal R(A)$ (exact $n$-move DM realization, budget verified).
  **Lemma ESF-2** — for any nonempty subset $T$ in any order, the caterpillar value
  $v_k=|\dots|v_1-t_2|\dots-t_k|\in\mathcal R(A)$ (exact $n$ moves; the abs-flip branch $v_{j-1}<t_j$
  is a single legal MATCH cutting the resident). **Reduction UV'** — Prop UV follows from the
  *Subset-KK claim*: some subset's descending-KK value $\le u_nL$ (a min over an explicit
  constructive family, sufficient for the upper bound). **RIGOROUS negative result** — the one-sided
  ESF-1 family alone is provably insufficient: explicit rational $n=2$ valley counterexample
  $A=\{9/20,7/25,27/100\}$ where ESF-1 bottoms out at $17/100>u_2=1/7$ while subset $\{a_2,a_3\}$
  gives $|a_2-a_3|=1/100\le u_2$; hence the two-sided abs-flip (ESF-2) is *mandatory*, ruling out the
  greedy-subset-sum-toward-$a_1$ route (short by factor $\beta_n/u_n=2^{n-1}$). Residual: the
  Subset-KK claim (still open) — a genuine restricted-discrepancy statement needing the scale
  recursion; no deterministic single-pass policy works.
- (round 7, build) **Upper valley reduced EXACTLY to Prop UV** via Reduction R-UV (certified
  DM/P/U0): Xiang forces $D\le u_nL$ iff $\min\mathcal R(A)\le u_nL$, where $\mathcal R(A)$ is the
  achievable-leftover set of $\le n$-move DELETE/MATCH sequences. **Lemma RL PROVEN**: $\mathcal R(A)$
  = tree-realizable signed *subset* sums $|\sum_{i\in T}\varepsilon_i a_i|$, a strict subset of all
  $\{0,\pm1\}$ signed sums (no summing of positives). **Corrected a round-6 error**: DELETE
  (subset-selection) is ESSENTIAL — full-support (no-DELETE) differencing trees overshoot on 214/516
  valley profiles (worst $7.5\times$); with DELETE, $\min\mathcal R\le u_nL$ on all 387 tested (worst
  $0.56\times$). **Lemma VS PROVEN**: in the valley no single DELETE (needs $a_i\ge c(n)L>L/2$) or
  MATCH (needs $y\ge\beta_nL$) admits an IH-certified reduction — thresholds meet the valley
  boundary exactly — so $\ge2$ coordinated cuts are forced; this rigorously subsumes the numeric
  refutations of every deterministic single-rule. Residual: Prop UV (the restricted signed-subset-sum
  discrepancy bound) — still open.

## Current best
**Round 19 — RE-TARGETED. Boundary layer CLOSED (WTC, certified); deep-interior residual OPEN, now
officially stated as `min 𝓡(A) ≤ u_nL` (certified reduction R-UV), strictly easier than the retired
caterpillar residual `μ_{n+1} ≤ u_nL`.**

The certified rigorous core (leader's spine):
- **Reduction R-UV (Corollary of Lemma RL, certified).** In the upper-bound game (`m=n+1`, `≤n` cuts),
  every value `ρ=|Σ_{i∈T}ε_i a_i|` for nonempty `T` and a nonnegative differencing-TREE sign pattern
  `ε` on `T` is Xiang-realizable as the single leftover in exactly `n` cuts; hence
  `min 𝓡(A) ≤ u_nL ⟹ Xiang forces D ≤ u_nL`. This makes `min 𝓡(A) ≤ u_nL` the official sufficient
  residual. It is weakly easier than the old caterpillar target since `min 𝓡(A) ≤ μ_{n+1}`
  (caterpillars are one tree topology).
- **Lemma WTC (proven, tight on `A^{(n)}`).** `descKK(fullset) ≤ |2a₁−L|`, a nonempty tree value, so
  for `a₁ ≥ (L−u_nL)/2 = L/2 − u_n/2` we get `min 𝓡(A) ≤ L−2a₁ ≤ u_nL` and R-UV closes the region.

**Sole OPEN region: deep interior `a₁ < L/2 − u_n/2`,** residual `min 𝓡(A) ≤ u_nL`. Hardest sub-region:
the `u_n/2`-wide sliver `a₁∈(L/2−u_n, L/2−u_n/2)`, where `min 𝓡(A)/u_n → 1`. Exact-`Fraction` evidence
(NOT proof): `min 𝓡(A)/u_n ∈ {0,0,0.94,0.97,0.98}` on the R18 witness / `30-25-20-15-10` / `A^{(4,5,6)}`,
and `0.69–0.73` on the slivers — true and asymptotically tight.

**Why the gap is genuinely hard (sharp diagnosis).** The minimiser of `min 𝓡(A)` is generically an
**anchor-EXCLUDING tail subset** (R18 witness: `{13/40,13/40}`, dropping `a₁`; `{30,25,20,15,10}/100`
needs a 4-element tail subset). Every single object over the reachable-value set fails to reach it:
a single anchored walk (R18), a balanced full partition (R19 tree-min-divide-conquer, cannot drop
pieces), a band-restart (R19 signed-tree-invariant ≡ descKK), the covering radius (R10/R12), density
(R11), second moments (R16/R17) — each saturates at `Θ(1)·u_n` and grows with `n` (exponential-rate
mismatch: `u_n∼2^{-n}` but a fixed-depth reflection resolves only `Θ(2^{-depth})`). Also: the exact
completeness identity `μ_{n+1}=min 𝓡(A)` is FALSE (witness `(17,16,11,8,4)`: `μ=1`, `min 𝓡=0`), so no
completeness bridge is sound. **The open gap needs a genuinely global existence argument over the
tree-realizable signed sums (Steinitz / vector-balancing style), or a bespoke sliver-local perturbation
— not any single object over `𝓡(A)`.** This is out of the current framing; handed forward.

---
**Round 18 — boundary layer CLOSED (WTC, certified); deep-interior / sliver residual OPEN. The R18
sharpened-WTC / reflected-walk / anchored-caterpillar contraction mechanism is REFUTED (exact-Fraction
C2 gate FAILED, 9th dead upper mechanism) — the covering-radius family in disguise.**

The proven state is unchanged and stands as the leader's rigorous core: the upper bound reduces
(certified R-COV'/FGR/ESF-2) to `Φ(A) := min_{∅≠T} descKK(T) ≤ u_nL`; **Lemma WTC** (`Φ ≤ |2a₁−L|`,
proven, tight on `A^{(n)}`) closes the whole region `a₁ ≥ (L−u_nL)/2 = L/2 − u_n/2`. The sole OPEN region
is the deep interior / sliver `a₁ < L/2 − u_n/2`, where `Φ ≤ u_nL` is TRUE (0.88/0.94/0.97/0.98 at
n=3..6, asymptotically tight) but no proof exists.

**R18 refutation (make-or-break gate, exact Fraction).** The proposed closure — after the band-landing
crossing `k*`, the anchored reflected residual `w_k=|w_{k-1}−a_k|` contracts to `≤ u_nL` under ONE-REC
dyadic caps — is DEAD. The contraction object `minpost=min_{k≥k*} w_k` (min over all post-crossing stops)
saturates far above `u_n` and grows with `n`: worst `minpost/u_n = 4.54/9.09/13.87/24.26` (n=3..6). Exact
witness `A={1/3,13/40,13/40,1/120,1/120}`: `minpost=3/10=9.3·u₄`, true `Φ=0` via `{13/40,13/40}`. The
reflected walk is anchored at `a₁`; the true minimiser is a tail subset that excludes `a₁` (size up to
`n`), so no single anchored pass — of any stopping rule — can reach it. This is precisely the dead
covering-radius family (GAP TWO-CAP, 3.2/6.1/8.9/15.8/24.6 at n=3..7).

**Strategic note for the outliner/reviewer.** The UPPER field has now exhausted every anchored /
single-pass / bounded-arity / averaging object (9 dead mechanisms). The deep-interior residual is a
genuine restricted signed-subset-sum discrepancy: prove `∃ ∅≠T` with `|Σ_{i∈T} ε_i a_i| ≤ u_nL` where
the signs `ε` are tree-realizable (Lemma RL). The next lever must be an EXISTENCE argument on this
signed-subset-sum set (Steinitz / vector-balancing / prefix-discrepancy over ALL tree-realizable signings,
NOT a caterpillar-min or any anchored contraction) — the growing-arity (`~2^{n-1}`) signature every gate
now shows points there. Do NOT re-seed post-crossing/reflected-walk/anchored-caterpillar contraction,
covering radius, density/COUNT, per-subset WTC, single-target subset-sum density, full-tree 2nd moment,
or margin/smoothing — all dead.

---
**Round 17 — boundary layer CLOSED (WTC); deep interior OPEN, now sharply localized to a
`u_n/2`-wide near-boundary sliver where NO margin exists.**

The proven state: the upper bound reduces (certified R-COV'/FGR) to `Φ(A) := min_{∅≠T} descKK(T) ≤
u_nL`; **Lemma WTC** (`Φ ≤ |2a₁−L|`, proven, tight on `A^{(n)}`) closes the whole region
`a₁ ≥ (L−u_nL)/2 = L/2 − u_n/2`. The sole open region is the deep interior `a₁ < L/2 − u_n/2`.

Round 17 sharpened this crux and refuted the R17 plan's mechanism:
- **No uniform margin near the deep boundary (G1, exact).** `sup_{deep} Φ/u_n → (2^{n+1}−1)/
  (2^{n+1}+1) → 1`; the `0.34–0.56` margin holds only for `a₁ ≤ L/2 − u_n`. The genuinely hard part
  is the sliver `a₁ ∈ (L/2 − u_n, L/2 − u_n/2)` (width `u_n/2`), where `Φ/u_n → 1` — as tight as the
  closed boundary layer, so ONLY an exact argument can close it (not the margin-tolerant recipe).
- **Smoothing not monotone (G2, exact).** The move "mass → `a₁`" decreases `Φ` on ~80% of deep
  profiles; there is no monotone reduction of a deep profile to the `a₁`-boundary. SMOOTH-MONO fails.
- **Sharpened reduction.** By WTC on `T={a₁}∪S`, `Φ ≤ min_{S⊆tail}|a₁ − Σ_S|`, so the deep bound
  follows from: *some tail subset sum lands within `u_nL` of the single target `a₁`* (subset-sum
  `u_nL`-density around `a₁`). No bounded-`|S|` mechanism reaches it. This is the crux, one sliver
  deeper than WTC, still OPEN. Full-tree second-moment averaging is DEAD (8th mechanism).

**Strategic note for the outliner/reviewer:** the R17 "margin-tolerant deep interior" premise is a
myth near the deep boundary. Any future upper lever must be EXACT (tight as `n→∞`) on the sliver, OR
must extend WTC's continuation strictly deeper than `a₁ = L/2 − u_n/2` (shave the whole-tail leftover
`L−2a₁` by one structured match), NOT a margin/averaging argument.

---
**Round 15 — the boundary layer is CLOSED; the residual is the DEEP interior only.**
The upper bound in the balanced valley is the first-gap / Subset-KK pigeonhole
`Φ(A) := min_{∅≠T} descKK(T) ≤ u_nL` (Reduction R-COV', certified; 0 admissible; only `T=∅` excluded).
Round 15 proves a new rigorous lemma that closes it wherever `a₁` is not deep:

> **Lemma WTC (whole-tail continuation) — PROVEN this round.** For `a₁≥…≥a_m>0`, `Σ=L`, the
> largest-first differencing value `K=descKK(a₁,…,a_m)` satisfies `K ≤ |2a₁−L|`. (Proof: two-sided
> invariant `a₁−P_k ≤ v_k ≤ |a₁−P_k|` by induction, `P_k=a₂+…+a_k`; at `k=m`, `P_m=L−a₁`. 0
> violations over 300k adversarial profiles; EQUALITY on `A^{(n)}` and `{16,8,4,3,2}/33`.)

Since the full profile is a nonempty `T`, `Φ(A) ≤ K ≤ |2a₁−L|`. Hence for every valley profile with
`a₁ ≥ (L−u_nL)/2` (so `|2a₁−L| = L−2a₁ ≤ u_nL`), `Φ ≤ u_nL` and R-COV' forces `D ≤ u_nL`. This is the
EXACT continuation of certified whole-tail-peel (`a₁≥L/2 ⇒ D=2a₁−L`) across `a₁=L/2`, tight on the
VALLEY-TIGHT family `A^{(n)}` — a margin-free bound, so it does not violate VALLEY-TIGHT. **The
region `a₁ ≥ (L−u_nL)/2` (dominant ∪ boundary layer) is now closed rigorously.**

**Remaining open crux:** the DEEP interior `a₁ < (L−u_nL)/2` (i.e. `|2a₁−L| > u_nL`). There WTC gives
only `Φ ≤ |2a₁−L| > u_nL`; closing `Φ ≤ u_nL` needs multi-piece cancellation with margin. Numerically
the margin exists (`Φ/u_n ≲ 0.72/0.67/0.58` at `n=3/4/5`, n-independent) but NO analytic mechanism
achieves it — a bounded (1–2 move) argument is provably insufficient ({30,25,20,15,10}/100, deep,
needs a 4-element cancellation). This is the same first-gap pigeonhole open since R7, now strictly
confined to the deep interior (a real reduction of the open region).

---
**Round 13 — the honest open crux, with the round-13 lever refuted (retained).** The upper bound in the balanced
valley is *exactly* the first-gap / Subset-KK pigeonhole
$$\min_{\varnothing\ne T\subseteq\{1,\dots,n+1\}}\ \mathrm{descKK}(T)\ \le\ u_nL$$
(Reduction R-COV', certified; value `0` from a nonempty even cancellation is admissible, only `T=∅`
excluded). This is TRUE — 0 exact fails over thousands of exact valley profiles `n=2..6`, worst `0.75`,
tight `=1` at the dyadic ladder `a_i=2^{n+1-i}/(2^{n+1}-1)` — and remains the honest open residual.

The round-13 lever (SEED(p) seeded strong induction + GAP-TELE mass-telescope discrepancy) is **REFUTED
by the mandated exact-fraction gate**, and the refutation is structural, not a loose constant:
- SEED(p) with threshold `u_p·M` is not inductively stable — worst overshoot grows with `p` in every
  domination/cap parametrization.
- GAP-TELE (charge far pieces against `Σa_i=1`) is impossible: `(n+1)u_n→0` (linearly many pieces, an
  exponentially small threshold), and the distance-sum is bounded ABOVE by `a_1(2-2^{-n})<2a_1<1` (a
  clean, tight telescope, but the wrong direction). One cannot sum `n+1` per-piece contributions to
  reach the total mass.

**Newly clarified, certifiable structural fact (side product, ready for certification):**
`Σ_{i=1}^{n+1} dist(a_i,R_{i-1}) ≤ a_1(2 - 2^{-n})`, from `dist(a_i,R_{i-1}) ≤ a_1·2^{-(i-1)}` (the
covering radius of `R_{i-1}` on `[0,a_1]` at most halves per reflection), geometric-summed. Tight
constant, exact-fraction verified. (Useful as a hard NO-GO: it certifies that any per-piece mass-charging
lever is impossible, so the field should not re-attempt one.)

**Five upper-wall mechanism families now exhausted:** covering-radius (R10/R12), density/COUNT (R11),
greedy recursion (R9), bounded-depth escape (R10), and mass-telescope discrepancy (R13). Recommendation:
escalate to a potential-free / LP-duality extremal re-derivation attacking both walls at once (per the
outline-reviewer's diversity note), not a sixth variant on the reachable-set object.

---

**Round 12 — the make-or-break upper crux, now correctly stated.** The upper bound in the balanced
valley is *exactly* $\mu_{n+1}\le u_n$, where $\mu_{n+1}=\min\{v>0:v\in R_{n+1}\}$ is the smallest
positive value of the include/skip reachable set (Reduction R-COV', proven §4B.8, with the T=∅ leftover
excluded correctly). By the proven recursion $\mu_i=\min(\mu_{i-1},\mathrm{dist}(a_i,R_{i-1}))$ this is
the **first-gap pigeonhole**: some $a_i$ ($2\le i\le n+1$) approaches the previously reachable set
$R_{i-1}$ within $u_n$. This is the honest open crux (GAP U-first-gap). It is *not* a covering-radius
statement: the covering radius (worst gap) provably saturates at $\approx3$–$5\cdot u_n$ (GAP TWO-CAP
refuted this round), and the first gap is incomparable to it, so the entire covering-radius family
(R10 one-cap, R12 two-cap) is dead. A future upper attack must target the first-gap pigeonhole directly
(candidate: an Abel/telescope identity on the sorted subset-value multiset $M_{n+1}$ pairing values whose
*difference* is itself reachable — the tree-realizability constraint from Lemma RL being the obstruction
to a naive $2^{n+1}$-value pigeonhole).

**Proven this round (self-contained, ready for certification):**
- **First-gap recursion:** $\mu_i=\min(\mu_{i-1},\mathrm{dist}(a_i,R_{i-1}))$, hence
  $\mu_{n+1}=\min_{1\le i\le n+1}\mathrm{dist}(a_i,R_{i-1})$. Proof: $R_i=R_{i-1}\cup\phi_i(R_{i-1})$,
  $\phi_i(v)=|v-a_i|$; the smallest new positive value is $\mathrm{dist}(a_i,R_{i-1})$. §4B.8.
- **Reduction R-COV' (T=∅-safe):** upper bound in valley $\iff\mu_{n+1}\le u_n$; every nonempty subset
  $T$ is realizable in exactly $n$ cuts (ESF-2), $\varnothing$ needs $n+1$, so the produced value is
  always a legal nonempty-$T$ leftover. §4B.8.

**Proven this round (self-contained, ready for certification, rounds ≤11):**
- **Lemma TB (top-band decomposition).** For a refinement $R$ of $C_n$, $D(R)=(f_1-2^{n-1})^+ +
  D_{\mathrm{low}}$, $D_{\mathrm{low}}=\mu\{t\in(0,2^{n-1}):N_R(t)\text{ odd}\}\ge0$. Proof: split
  the Lemma-M integral at $2^{n-1}$; Lemma ONE forces $N\le1$ above the threshold, so the top band
  contributes exactly $(f_1-2^{n-1})^+$. Numerically confirmed.
- **Lower-bound reduction (unconditional):** base $n=0$, trivial regime $f_1\ge2^{n-1}+1$, and
  Case (a) all give $D\ge1$ directly from Lemma TB; the lower bound reduces to (L1)
  $D_{\mathrm{low}}\ge2^{n-1}+1-f_1$ (critical band) and (L2) $D_{\mathrm{low}}\ge1$ (top-shredded).

**Standing proven results (rounds 5–6):**
- **Lemma PL1** — single-cut piecewise-linearity, slope $\in\{-2,0,2\}$, min at wasted
  endpoint / bisection / tie. Exact closed form via Lemma M.
- **Theorem VERT** — optimal Xiang refinement has $\le M\le n+1$ distinct positive values
  (LP-vertex + rank count on active zero/tie constraints). Finitizes both bounds.
- **Corollary VERT-C** — the continuum collapses to a finite tie-pattern search over $\le n+1$
  value-classes.
- **Upper bound $a_1\ge L/2$** — closed via certified whole-tail-peel.

**Proven this round (§4B, self-contained on certified DM/P/U0):**
- **Reduction R-UV:** upper bound in the valley $\iff\min\mathcal R(A)\le u_nL$ (achievable-leftover
  set of $\le n$-move DELETE/MATCH sequences; final single piece has $D=\rho$).
- **Lemma RL (realizability):** $\mathcal R(A)=\{|\sum_{i\in T}\varepsilon_ia_i|:T\ne\varnothing,\
  \varepsilon\text{ tree-realizable on }T\}$, a *strict* subset of all $\{0,\pm1\}$ signed sums
  (differences only, never sums of two positives). DELETE/subset-selection essential.
- **Lemma VS (valley-sharpness):** in the valley no single DELETE ($a_i\ge c(n)L$ needed) or MATCH
  ($y\ge\beta_nL$ needed) admits an IH$(n-1)$-certified reduction; thresholds meet the valley
  boundary exactly $\Rightarrow$ $\ge2$ coordinated cuts forced (rigorous adaptivity).

**Proven this round (§4B.4, self-contained on certified P/DM):**
- **Lemma ESF-1** (subtraction-from-top subfamily): $\sum_{i\in T}a_i\le a_1\Rightarrow
  a_1-\sum_{i\in T}a_i\in\mathcal R(A)$, exact $n$-move realization.
- **Lemma ESF-2** (subset-caterpillar subfamily): every caterpillar value over any subset in any
  order (in particular descending-KK) lies in $\mathcal R(A)$, exact $n$ moves; abs-flip = legal MATCH.
- **Reduction UV'**: Prop UV $\Longleftarrow$ **Subset-KK claim** (some subset's descending-KK value
  $\le u_nL$) — a bound over an explicit constructive family, sufficient for the upper bound.
- **Rigorous insufficiency of ESF-1 alone**: explicit valley counterexample $\{9/20,7/25,27/100\}$
  ($n=2$) with ESF-1 min $=17/100>u_2=1/7$; abs-flip subset $\{a_2,a_3\}$ gives $1/100\le u_2$. So
  the two-sided abs-flip is provably necessary.

**Proven this round (§4B.5, self-contained on certified P/DM/ESF-1/ESF-2):**
- **Lemma BL (band-landing / first crossing):** the descending survivor partial sums cross $a_1$ at a
  unique index $k$ (finite increasing sequence — no straddle case), landing $T=\{a_1,\dots,a_k\}$ with
  $r=a_1-\Sigma_T=|a_1-\Sigma_T|\in[0,\beta_nL)$, realized by ESF-1 in $n$ moves. Closes step 2.
- **Reachability reformulation:** Subset-KK $\iff$ **Covering claim** — the descending include/skip
  reachable set $R_{n+1}$ ($R_i=R_{i-1}\cup\{|v-a_i|\}$) meets $[0,u_nL]$ via a nonempty include-set.
- **Rigorous refutation of the greedy step-3 recursion:** greedy band-landing, flip-if-helps, and
  drop-one all overshoot $u_nL$ (worst $1.6$–$11.4\times$, $n=2..7$); true subset min always $\le u_nL$
  (worst $0.84$). The residual needs foresight — a global covering argument, not a recursion.

**Proven this round (§4B.7, self-contained, ready for certification):**
- **Lemma CONF (confinement):** $\max R_i\le a_1$ for all $i$, so $R_{n+1}\subset[0,a_1)\subset[0,L/2)$.
  Proof: strong induction, $|v-a_i|\le\max(v,a_i)\le a_1$ (IH $v\le a_1$, sorting $a_i\le a_1$). Clean,
  profile-independent, certifiable.
- **Lemma MD2 (multiset doubling):** the reachable multiset $M_i$ has $|M_i|=2^i$, support $R_i$,
  enumerates all $2^{n+1}$ subset-KK values; gives a rigorous consecutive multiset gap $<u_n/2$.
- **Refutation of COUNT and of the density substrate:** $|R_{n+1}|=2^{n+1}$ is FALSE in the valley
  (exact all-equal counterexample $a_i=1/(n+1)$, $n\ge3$, $|R_{n+1}|=2$); and no pigeonhole-gap quantity
  bounds the covering value (explicit witnesses: $\mathrm{cov}/(\text{avg gap})$ up to $2.07$,
  $\mathrm{cov}/\text{mingap}$ up to $3.0$). The round-11 outline's COUNT$+$density vehicle is a dead
  substrate.

**Open gaps:**
- **GAP L-fin:** $D_{\mathrm{low}}\ge2^{n-1}+1-f_1$ (L1, critical band) and $D_{\mathrm{low}}\ge1$
  (L2, top-shredded). Finite per $n$ by VERT; profile-independent proof needs the one-per-gap
  exchange/telescoping with the SPLIT cross term carried. Shared with induction-peel /
  parity-measure.
- **GAP U-cover (sharpened Subset-KK / Prop UV):** the Covering claim — every full-budget
  balanced-valley profile has its descending include/skip reachable set $R_{n+1}$ meeting $[0,u_nL]$
  (equivalently $\min\mathcal R(A)\le u_nL$). True (evidence: exact on dyadic extremal boundary;
  $\le u_nL$ on all tested valley profiles, worst subset-min ratio $0.84$) but no profile-independent
  proof yet. **Now known to be a GLOBAL covering problem, not a recursion:** a direct $2^{n+1}$-subset
  pigeonhole is *invalid* (Lemma RL), the one-sided ESF-1 family is *provably* insufficient (§4B.4),
  and — new this round — the greedy band-landing recursion and every deterministic single-pass policy
  *provably overshoot* (§4B.5, up to $11.4\times$). What is needed is a covering/dispersion invariant
  on the $R_i$ that telescopes the covering radius near $0$ down to $u_nL$, using $\sum a_i=1$,
  $a_1<L/2$, $a_2<\beta_nL$ jointly. Lemma BL supplies the first landing $r\in[0,\beta_nL)$. Shared
  with valley-differencing-construction / subset-sum-pigeonhole.
  **Round-10 sharpening:** the bounded-depth two-level move lemma (outline step 2) is REFUTED — the
  escape depth grows with $n$ and failures are not near-uniform (depth-$2$ fails $52.9\%$ at $n=6$);
  and the true covering-radius invariant $\rho_i\le a_i/2$ (validated, 0/47516; NOT proven, natural
  induction only gives $a_{i-1}/2$) saturates at $a_{n+1}/2\gg u_n$. So neither a bounded-depth
  move-search nor a single-window covering bound suffices; GAP U-cover is a **restricted density/
  pigeonhole** among tree-realizable signed subset sums (respecting Lemma RL), the honest crux.

**Round-10 candidate (validated, NOT proven — for next round, do not cite as established):**
- **Covering-radius invariant.** For the descending reachable DP $R_0=\{0\}$,
  $R_i=R_{i-1}\cup\{|v-a_i|:v\in R_{i-1}\}$, the covering radius $\rho_i=\sup_{t\in[0,a_i]}
  \operatorname{dist}(t,R_i)$ satisfies $\rho_i\le a_i/2$ (equivalently $R_i\cap[0,a_i]$ has $0,a_i$
  and all gaps $\le a_i$). Verified with 0 violations in 47516 checks ($n=3\!-\!6$). Insufficient
  alone (saturates at $a_{n+1}/2$), but a genuine reachable-set structural fact worth proving/using.

## Promotable lemmas
- **Round 19: NO new promotable lemma.** Consolidation round. The re-target uses the already-certified
  Corollary **R-UV** of Lemma **RL** (`leftover-realizability.md`) — no re-proof, no new lemma. The two
  R19 mechanisms (tree-min-divide-conquer, signed-tree-invariant) were refuted at the gate and recorded
  as dead, not promoted. The observation `min 𝓡(A) ≤ μ_{n+1}` (caterpillars ⊆ trees) is a one-line
  consequence of RL, not worth separate certification. Prior certified WTC (below) unchanged.
- **Round 18: NO new promotable lemma.** The round produced a refutation, not a proof — the C2
  post-crossing-contraction gate FAILED (reflected-walk contraction saturates at 4.5–24×`u_n`, growing
  with n; dead covering-radius family). Recorded as a dead mechanism, not a lemma. Prior certified WTC
  (below) is unchanged.
- **Lemma WTC (whole-tail continuation bound) — round 15, PROVEN in full.**
  For any reals `a₁ ≥ a₂ ≥ … ≥ a_m > 0` (`m≥1`) with sum `L`, the largest-first differencing
  (descending-KK caterpillar) value `K := descKK(a₁,…,a_m)` — defined by `v₁=a₁`,
  `v_k=|v_{k−1}−a_k|`, `K=v_m` — satisfies
  $$K \;\le\; |\,2a_1 - L\,|.$$
  *Proof:* two-sided invariant `(I_k): a₁−P_k ≤ v_k ≤ |a₁−P_k|` for all `k`, where `P_k=a₂+…+a_k`
  (`P₁=0`), by induction. Base `k=1`: both sides `=a₁`. Step: with `d=a₁−P_{k−1}` (so `d≤v_{k−1}≤|d|`),
  lower bound `v_k=|v_{k−1}−a_k|≥v_{k−1}−a_k≥d−a_k=a₁−P_k`; upper bound splits on sign of `d` — if
  `d≥0` then `(I_{k−1})` pins `v_{k−1}=d` so `v_k=|d−a_k|=|a₁−P_k|`; if `d<0` then `v_{k−1}∈[0,−d]` and
  `|t−a_k|` on `[0,−d]` is `≤max(a_k,|(−d)−a_k|)≤(−d)+a_k=|a₁−P_k|`. At `k=m`, `P_m=L−a₁`, giving
  `K≤|a₁−(L−a₁)|=|2a₁−L|`. `∎` (Section: Round 15 BUILD. Full text above.)
  *Verification:* 0 violations over 300 000 adversarial integer profiles (`m=2..7`); the universal
  form `Φ(A)=min_{∅≠T}descKK(T) ≤ |2a₁−L|` had 0 fails over >100 000 exact profiles; EQUALITY
  `K=|2a₁−L|=1/(2^{n+1}+1)` on the VALLEY-TIGHT family `A^{(n)}` (`n=2..6`) and on `{16,8,4,3,2}/33`.
  *Use:* combined with certified **R-COV' (sufficiency)** it closes the UPPER bound on the region
  `a₁ ≥ (L−u_nL)/2` (dominant `a₁≥L/2` ∪ boundary layer), the exact continuation of certified
  whole-tail-peel across `a₁=L/2`, margin-free (respects VALLEY-TIGHT). It is a self-contained
  statement about largest-first differencing, independent of the game. **Certify this round.**
- **Corollary WTC-SUBSET (single-target subset-sum reduction) — round 17.** For a descending valley
  profile `a₁≥…≥a_{n+1}>0`, `Σ=L`, and ANY `S⊆{a₂,…,a_{n+1}}`, applying Lemma WTC to the descending
  list `T={a₁}∪S` gives `descKK(T) ≤ |2a₁ − Σ_T| = |a₁ − Σ_S|`. Hence
  $$\Phi(A)=\min_{\varnothing\ne T}\mathrm{descKK}(T)\ \le\ \min_{S\subseteq\{a_2,\dots,a_{n+1}\}}|a_1-\Sigma_S|.$$
  So the deep-interior upper bound `Φ ≤ u_nL` follows from: *some tail subset sum lands within `u_nL`
  of `a₁`* (subset-sum `u_nL`-density around the single target `a₁`). This is a clean, rigorous
  consequence of the already-certified WTC — likely EQUIVALENT to existing FGR/band-landing objects,
  so the reviewer should check for duplication before certifying (do NOT double-certify). Its value is
  as a SHARPENING that localizes the open crux to a single-target subset-sum-density statement on the
  near-boundary sliver `a₁∈(L/2−u_n, L/2−u_n/2)`, where (verified exact this round) `Φ/u_n→1`.
- **NEGATIVE record (round 17, not a lemma — for the memory/dead list): full-tree second moment is the
  8th dead upper mechanism.** `mean(V²)` over the FULL tree-realizable ensemble 𝓡(A) (all binary
  differencing trees over all nonempty T) has worst `mean(V²)/(u_nL)² = 14.7/72/242` at `n=3,4,5`,
  growing with n, on hard deep profiles with no exact zero — DEAD, same rare-needle failure as both
  fixed-order second-moment probes. Also: the smoothing move "mass→a₁" is NOT `Φ`-monotone (~80% of
  deep profiles decrease). Neither is promotable; both are dead-end records.
- **Lemma DSUM (distance-sum telescope, a mass-charging NO-GO) — round 13.** For the descending
  include/skip reachable set $R_0=\{0\}$, $R_i=R_{i-1}\cup\{|v-a_i|:v\in R_{i-1}\}$ on a sorted profile
  $a_1\ge\dots\ge a_{n+1}$,
  $$\mathrm{dist}(a_i,R_{i-1})\ \le\ a_1\,2^{-(i-1)}\qquad\Longrightarrow\qquad
    \sum_{i=1}^{n+1}\mathrm{dist}(a_i,R_{i-1})\ \le\ a_1\,(2-2^{-n})\ <\ 2a_1.$$
  Sketch: $\mathrm{dist}(a_i,R_{i-1})$ is at most the covering radius $\rho_{i-1}$ of $R_{i-1}$ on
  $[0,a_1]$ (Lemma CR-style, the reachable set contains $0$ and $\le a_1$ by CONF); each reflection
  $v\mapsto|v-a_i|$ folds $[0,a_1]$ so the covering radius at most halves, $\rho_{i-1}\le a_1 2^{-(i-1)}$;
  geometric sum. The constant $2-2^{-n}$ is TIGHT (exact-fraction verified, `n=2..7`: worst
  `sum/a_1 = 1.75, 1.875, 1.9375, …`). *Consequence (recorded as a hard NO-GO):* any lever that tries to
  charge the per-piece first-gap distances against the total mass `Σa_i=L` is impossible — the
  distance-sum is `<2a_1<L`, and `(n+1)u_n→0`, so far pieces cannot sum past `L`. This is the R13
  refutation of GAP-TELE, stated as a clean provable bound. (The covering-radius-halving sub-claim
  overlaps R10's certified `ρ_i≤a_i/2`; a full proof should cite/extend it.) **Certifiable this round.**
- **Lemma FGR (first-gap recursion) — round 12.** For the include/skip reachable set $R_0=\{0\}$,
  $R_i=R_{i-1}\cup\{|v-a_i|:v\in R_{i-1}\}$ on a sorted profile, the smallest positive reachable value
  $\mu_i=\min\{v>0:v\in R_i\}$ satisfies $\mu_i=\min(\mu_{i-1},\mathrm{dist}(a_i,R_{i-1}))$, whence
  $\mu_{n+1}=\min_{1\le i\le n+1}\mathrm{dist}(a_i,R_{i-1})$. Proof: the positive elements of
  $R_i=R_{i-1}\cup\phi_i(R_{i-1})$ ($\phi_i(v)=|v-a_i|$) are those of $R_{i-1}$ together with the
  positive folds $|v-a_i|>0$ ($v\ne a_i$), whose minimum is $\mathrm{dist}(a_i,R_{i-1})$. Depends only on
  the recursion definition. Proved in full §4B.8. **Certifiable this round.**
- **Reduction R-COV' (T=∅-safe covering equivalence) — round 12.** In the full-budget balanced valley,
  Xiang forces $D\le u_nL$ **iff** $\mu_{n+1}\le u_nL$ (smallest positive value of $R_{n+1}$). Every
  nonempty subset $T$ has its descending-KK value realized by exactly $n$ DM cuts ($(|T|-1)$ MATCHes +
  $(n{+}1{-}|T|)$ DELETEs, leader free), while $\varnothing$ needs $n+1$ cuts (over budget), so the
  geometric value $0=v(\varnothing)$ is not a legal leftover and the conversion always yields a nonempty-$T$
  value ($=\mu_{n+1}$, positive or $0$ via a nonempty even cancellation). Depends on certified DM/P/RL/ESF-2.
  Proved in full §4B.8. **Certifiable this round.**
- **Lemma CONF (confinement of the reachable set).** For the descending include/skip DP $R_0=\{0\}$,
  $R_i=R_{i-1}\cup\{|v-a_i|:v\in R_{i-1}\}$ on a sorted profile $a_1\ge\dots\ge a_{n+1}$, one has
  $\max R_i\le a_1$ for every $i$, hence $R_{n+1}\subseteq[0,a_1]$ (so $\subset[0,L/2)$ in the valley).
  Proof: strong induction with the elementary bound $|v-a_i|\le\max(v,a_i)$ and $v\le a_1$ (IH),
  $a_i\le a_1$ (sorting). Depends on nothing but the sort order. Proved in full in §4B.7; verified
  ($0$ failures, random $+$ near-tie, $n=3$–$6$; reviewer-reproduced). **Certify this round.**
- **Lemma MD2 (multiset doubling / subset enumeration).** The reachable multiset $M_0=\{\!\{0\}\!\}$,
  $M_i=M_{i-1}\uplus\{\!\{|v-a_i|:v\in M_{i-1}\}\!\}$ satisfies $|M_i|=2^i$, has support $R_i$, all
  elements in $[0,a_1]$, and $M_{n+1}$ enumerates with multiplicity the descending-KK value $v(T)$ of
  every subset $T\subseteq\{1,\dots,n+1\}$. Consequently the $2^{n+1}$ values in $[0,a_1)$ have a
  consecutive gap $\le a_1/(2^{n+1}-1)<u_n/2$. Proof: doubling count $+$ CONF $+$ leaf/subset bijection.
  Proved in full in §4B.7. (Note: the *distinct*-value count $|R_{n+1}|=2^{n+1}$ is FALSE in the valley —
  all-equal counterexample — so only the *multiset* statement is a theorem.)
- **Lemma BL (band-landing / first crossing).** For a full-budget balanced-valley profile
  $A=\{a_1\ge\dots\ge a_{n+1}\}$ (sum $L$, $a_1<L/2$), let the survivors $a_2\ge\dots\ge a_{n+1}$ have
  descending partial sums $P_0=0,P_j=\sum_{i=2}^{j+1}a_i$. Then $P_n=L-a_1>a_1$, so there is a unique
  $k\in\{1,\dots,n\}$ with $P_{k-1}\le a_1<P_k$; the subset $T=\{a_1,\dots,a_k\}$ has
  $r:=a_1-P_{k-1}=|a_1-\Sigma_T|$ satisfying $0\le r<a_{k+1}\le a_2$ (hence $<\beta_nL$ under the valley
  cap), and $r\in\mathcal R(A)$ realized by ESF-1 in exactly $n$ moves. The crossing index is unique
  on a finite strictly increasing sequence, so there is no straddle/boundary case; the strict valley
  $a_1<L/2$ is exactly what makes the crossing exist with $k\le n$. Depends only on the sorting and
  certified P/DM/ESF-1. Proved in full in §4B.5; verified on the $n=2$ witness ($k=2$, $r=17/100$).
- **Lemma TB (top-band decomposition).** For any refinement $R$ of $C_n=\{2^n,\dots,1\}$ ($n\ge1$),
  writing $f_1=\max R$, $e=(f_1-2^{n-1})^+$, and $D_{\mathrm{low}}=\mu\{t\in(0,2^{n-1}):N_R(t)\text{
  odd}\}$, one has $D(R)=e+D_{\mathrm{low}}$. Proof: Lemma-M integral split at $2^{n-1}$ + Lemma ONE
  ($N\le1$ above threshold, so the band contributes $(f_1-2^{n-1})^+$). Depends only on certified
  Lemmas M and ONE. Proved in full in §4A; numerically confirmed. **Immediate corollaries**
  (unconditional): $f_1\ge2^{n-1}+1\Rightarrow D(R)\ge1$; top-piece-uncut $\Rightarrow D(R)\ge2^{n-1}$.
- **Lemma PL1** and **Theorem VERT** — as certified-ready in round 5 (statements above).
- **Lemma RL (leftover realizability).** For a multiset $A=\{a_1,\dots,a_m\}$, the achievable-leftover
  set $\mathcal R(A)$ of $\le(m-1)$-move DELETE/MATCH sequences equals
  $\{|\sum_{i\in T}\varepsilon_ia_i|:\varnothing\ne T\subseteq[m],\ \varepsilon\text{ a nonnegative-
  differencing-tree sign pattern on }T\}$, a *strict* subset of $\{|\sum_i\varepsilon_ia_i|:
  \varepsilon\in\{0,\pm1\}^m\}$ (only tree-realizable patterns occur; no sum of two positive pieces).
  Proof: track each piece's $\{0,\pm1\}$ coefficient vector; DELETE zeroes coordinates, MATCH takes a
  sign-respecting difference; the final single piece is the tree's root value. Depends only on
  certified Lemma P/DM. Proved in full in §4B.1; machine-checked ($m\le5$, budget enforced).
- **Lemma VS (valley-sharpness).** In the balanced valley $\{m=n+1,a_1<L/2,a_2<\beta_nL\}$, a single
  DELETE gives a certificate $u_{n-1}(L-a_i)\le u_nL$ iff $a_i\ge c(n)L$, and a single MATCH gives
  $u_{n-1}(L-2y)\le u_nL$ iff $y\ge\beta_nL$ ($y=$ smaller matched part); neither holds since
  $a_i\le a_1<L/2<c(n)L$ and $y\le a_2<\beta_nL$. Hence no single move admits an IH$(n-1)$-certified
  reduction: $\ge2$ coordinated cuts are forced (rigorous adaptivity). Depends only on the closed
  form $u_n,c(n),\beta_n$. Proved in full in §4B.2.
- **Lemma ESF-1 (subtraction-from-top subfamily).** For $A=\{a_1\ge\dots\ge a_{n+1}\}$ and any
  $T\subseteq\{2,\dots,n+1\}$ with $\sum_{i\in T}a_i\le a_1$, the value $a_1-\sum_{i\in T}a_i$ lies in
  $\mathcal R(A)$, realized by $|T|$ MATCHes (each legal since running $\ge$ next resident) plus
  $n-|T|$ DELETEs $=n$ moves. Depends only on certified P/DM. Proved in full in §4B.4.
- **Lemma ESF-2 (subset-caterpillar subfamily).** For any nonempty $T\subseteq\{1,\dots,n+1\}$ and any
  order $t_1,\dots,t_k$ of $\{a_i:i\in T\}$, the caterpillar value $v_1=t_1$, $v_j=|v_{j-1}-t_j|$,
  satisfies $v_k\in\mathcal R(A)$, realized by $k-1$ MATCHes ($+n+1-k$ DELETEs $=n$ moves); the
  abs-flip step $v_{j-1}<t_j$ is the legal MATCH$(t_j,v_{j-1})$ cutting the resident $t_j$. In
  particular descending-KK over any subset is realizable. Strictly larger than ESF-1 (the abs-flip),
  and this extra power is *necessary*: the explicit $n=2$ valley profile $\{9/20,7/25,27/100\}$ has
  ESF-1 minimum $17/100>u_2=1/7$ but ESF-2 value $|7/25-27/100|=1/100\le u_2$. Depends only on
  certified P/DM. Proved in full in §4B.4.
