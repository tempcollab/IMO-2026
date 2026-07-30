## imo-2026-04 — outline review (round 1)

Conjectured answer (all three explorers): Mulan wins ⟺ θ = 180°/n (n ≥ 2 integer).
Verified by me: (i) the 2×2 taint casework has NO violation for non-divisor θ ∈ {72,50,100,120,135,80,7} (50k trials each); (ii) M1+M2 wins 200/200 random triangles for θ ∈ {90,60,45,36,30,180/7,180/5} with step counts ≤ n−1; (iii) the cut formula and the supplementary P-pair (β, 180−β) are arithmetically consistent. The shared infrastructure is sound.

The outliner's shared-wall warning is **correct and confirmed by computation**: the exclusion of lattice-descent, residue-monovariant, AND equilateral-witness all reduce to the same 2×2 taint casework. I additionally found that equilateral-witness's *distinct* exclusion crux (E self-closed under the reflection) is **false** — see below. So the field's exclusion diversity is weaker than it appears: only euclidean-needle offers a genuinely different exclusion framing, and it is the leakiest (compute explorer: (1,35,144) not safe for θ=72°).

---

### lattice-descent — APPROVE

Both directions sound; this is the anchor.

**Inclusion (M1 alignment + M2 descent):** verified. M1: cut to largest angle A ≥ 60° ≥ θ = 180/n; interval (B, A+B) has length A > θ (strict unless equilateral n=3, already won), so pigeonhole gives kθ ∈ (B, A+B); set α = kθ−B; both P-angles become kθ and (n−k)θ. Whichever child Shan-Yu keeps carries a multiple; M2 descends it. M2: the tracked multiple sits at the *cut vertex* A, which is a geometrically fixed vertex of C2 = ((m−1)θ, C, B+θ); Mulan re-cuts the same vertex with α=θ; level m → m−1 → … → 1. The vertex never needs "relocating" — it is the same point — so the outliner's flagged "tracked-vertex commitment" gap is overstated: it is a one-line invariant ("always cut the vertex that currently carries the largest multiple of θ"). I traced the angle bookkeeping: after j M2-steps the kept child has angle (m−j)θ at A and the other two angles are positive and sum to (n−m+j)θ, so positivity holds throughout. Bound ≤ 1 + (n−2) = n−1. Confirmed by 200/200 sim.

**n=2 boundary (θ=90°):** clean. Cut to largest angle A; β=90° lies in (B, A+B) because B<90 (since A≥60 and if A<90 then B≤A<90; if A>90 then B<90) and A+B=180−C>90 (C<90). Both P-angles = 90°. One move.

**Exclusion (2×2 taint casework):** verified sound. I checked each of the four cases by hand AND computationally (no violation for 7 non-divisor θ). The key subtlety — that "tainted in both slots" doesn't break the argument — is handled: pick any witness slot per child; each of the 4 (witness_C1 × witness_C2) pairs yields a linear relation A=(k1+k2)θ, B=(k2−k1)θ, C=(k1−k2)θ, or 180=(k1+k2)θ, the first three contradicting the parent's taint-freedom directly, the fourth forcing θ=180/n. The initial triangle exists because the forbidden set {kθ} is finite for every θ>0 (incl. irrational θ). Correct.

**Gaps (minor, builder closes while building):**
- Write the M2 tracked-vertex invariant in one line (it is trivial — see above; do NOT over-formalize into a fake difficulty).
- Positivity check for M1: state 1 ≤ k ≤ n−1 ⇒ kθ, (n−k)θ ∈ (0,180) and all six child angles positive.
- Irrational-θ arm of the 4th case: state (k1+k2)θ=180° has no solution because 180/θ∉ℚ.
- θ>90°: confirm excluded (the 4th case forces θ=180/(k1+k2)≤90 for k1+k2≥2).

No cuts. Register.

### residue-monovariant — CHANGES REQUESTED

**Distinct contribution:** a direct residue potential Φ = max(r(A),r(B),r(C)) bypassing the M1 alignment move. Genuinely different inclusion framing — keep alive.

**Crux (Φ strictly decreases for BOTH children under Mulan's best move):** unproved, and the outliner/invariant-explorer both flag it as "conjectural in detail." This is the single most likely fatal gap in the field. The supplementary pairing controls the two *fresh* P-residues (r(β) and θ−r(β) when θ|180) but each child also inherits a *fixed* preserved angle whose residue Mulan cannot move. Whether Mulan can always drive max-residue down on BOTH sides simultaneously is non-obvious and may be false (Shan-Yu keeps the non-improving child). I did not find a counterexample by hand for θ=180/n, but I could not prove it either — it is a real gamble.

**Fallback:** if Φ-decrease fails, the inclusion collapses to the M1 alignment move (lattice-descent). The exclusion IS the 2×2 casework (shared wall, stated honestly). So in the worst case this approach = lattice-descent. That is an acceptable fallback but kills the approach's distinctness.

**Also under-specified:** "strictly decreases" on a continuous residue box does not give a finite bound. The builder MUST naturalize Φ into a natural-valued co-rank (e.g. a lattice-point count under Φ, or the level of the largest residue in units of θ/n) — a real-valued decrease alone is insufficient for "finitely many steps" (rigor rule).

**Action:** register; build; the builder must either prove the Φ-decrease lemma (with the natural-valued co-rank) or convert to the alignment move early rather than late. Do not hand-wave the decrease.

### equilateral-witness — CHANGES REQUESTED

**Distinct contribution:** a self-reproducing safe set via the supplementary reflection β↔180−β (crux aimo-0262 template) as an exclusion framing independent of the taint casework. This is the field's best shot at breaking the shared exclusion wall — *if* it can be made to work.

**CRUX REFUTED as stated.** The outline's Step 4 claims "for every non-divisor θ, no single cut from E=(60,60,60) produces θ in either child." This is FALSE. I verified directly: for θ=72°, cutting E to a vertex with α=48° gives child C1=(48,60,72) — which contains 72°=θ. (General formula: α=120°−θ makes C1's P-angle = θ whenever 60°<θ<120°; and α=θ makes C1's α-slot = θ whenever θ<60°.) So E is NOT self-closed under one move. The θ=120° template works only because 120° happens to be unreachable from E's α-range (0,60)∪{60}; it does not generalize.

**What survives:** E is still a valid *starting point* for Shan-Yu's strategy, because the 2×2 casework guarantees Mulan cannot taint BOTH children from a taint-free parent — so when α=48° taints C1, Shan-Yu discards C1 and keeps C2=(12,60,108), which is taint-free. But that is exactly lattice-descent's exclusion (the taint-free set), not a distinct reflection-based one. So the approach's distinct exclusion collapses to lattice-descent unless the builder finds a *genuinely different* closed set S⊇{E} that is NOT the full taint-free set.

**Action:** register; build; the builder must EITHER (a) exhibit a reflection-closed family S⊇{E} that is strictly smaller/richer than the taint-free set and prove its closure under ALL β (not just lattice β — the compute explorer showed lattice-closure is insufficient: (1,35,144) is not safe for θ=72°), OR (b) honestly concede the exclusion = lattice-descent's casework and contribute only the (shared M1+M2) inclusion. If (a) is impossible, this approach should be RETHINK'd next round.

### euclidean-needle — CHANGES REQUESTED (weak; deferred from build set)

**Distinct contributions:** (1) needle-attraction inclusion (drive to a thin needle, then Euclidean-extract θ); (2) δ-blocks-Euclid exclusion (thin-needle safe set with large angle ≡ 180 mod θ).

Both cruxes are under-proved and one is empirically refuted in its naive form:
- **Needle-phase termination** (the load-bearing lemma) is unproved: no natural-valued decreasing potential is given, and "both children lexicographically thinner" is asserted without a rank. The ε>0 reality (P≠vertex) is unresolved. This is a genuine gap, not a formalization issue.
- **δ-blocks-Euclid exclusion is leaky** (compute explorer explicitly: (1,35,144) is NOT safe for θ=72°, so "all thin needles" is not closed). The outliner admits the fallback is the 2×2 casework = lattice-descent.

**Convergence risk:** the inclusion is a strictly harder route to the same result as M1 (which already solves inclusion in one shot from any triangle); the exclusion degrades to lattice-descent. In the limit this approach IS lattice-descent on both directions. Per CLAUDE.md's single-gap-trap warning, this is the closest approach to lattice-descent of the four.

**Action:** register (it is not a dead end — the Euclidean framing is sound in principle and empirically validated; a clever potential might exist); but DO NOT build this round. Builder effort is better spent on the three far-apart approaches. Revisit only if the field stalls and a genuinely different inclusion framing is still wanted; if the needle-phase potential cannot be found next round, RETHINK.

---

### Shared-wall assessment (for the orchestrator)

The exclusion direction is the field's shared wall: lattice-descent, residue-monovariant, and equilateral-witness all bottom out on the 2×2 taint casework (verified sound, so the wall is solid — but if a flaw were later found, three approaches die together). Only euclidean-needle offers a different exclusion framing, and it is the leakiest. **Recommendation for next round:** dispatch an explorer to find a genuinely independent exclusion route (e.g. a direct closed-safe-set construction for a specific non-divisor θ family — θ>90° is the cleanest sub-case: prove E is closed for ALL θ∈(90°,180°), which prunes half the range without the taint casework). The easy θ>90° sub-case: no θ=180/n exceeds 90°, and from E a single cut keeps all child angles in (0,120)∪{60}, so θ>120° is unreachable in one move; the (90°,120°) slice needs the reflection. This is a concrete independent exclusion target.

---

### Registered approaches (all four new, none cut — none are RETHINK; all survive with CHANGES except lattice-descent which is APPROVE)
- lattice-descent — APPROVE — registered
- residue-monovariant — CHANGES REQUESTED — registered
- equilateral-witness — CHANGES REQUESTED — registered
- euclidean-needle — CHANGES REQUESTED — registered (deferred from build set)

### Ranking (pairwise, anchored to evidence: verified-both-directions > unproved-crux-distinct-inclusion > refuted-crux-distinct-exclusion > convergent-two-crux)
- lattice-descent > residue-monovariant (verified both directions vs one unproved crux + shared exclusion)
- lattice-descent > equilateral-witness (verified vs refuted E-crux + shared inclusion)
- lattice-descent > euclidean-needle (verified vs two unproved cruxes incl. leaky exclusion)
- residue-monovariant > equilateral-witness (live unproved inclusion crux vs refuted exclusion crux; residue keeps a distinct inclusion, equilateral's distinct exclusion is refuted)
- residue-monovariant > euclidean-needle (one unproved crux with distinct inclusion vs two cruxes incl. empirically-refuted exclusion + harder-than-M1 inclusion)
- equilateral-witness > euclidean-needle (distinct exclusion idea still alive after rework vs leaky exclusion that is empirically refuted + convergence-prone inclusion)

### Build set (three far-apart approaches: canonical anchor + alternative-inclusion bet + alternative-exclusion bet; euclidean-needle deferred as too close to lattice-descent)

build set: lattice-descent, residue-monovariant, equilateral-witness
