# proof-reviewer — IMO 2026 P4 (Mulan's triangle game), round 1

**Answer (all three converge):** Mulan guarantees victory in finitely many steps ⟺ θ = 180°/n for some integer n ≥ 2 (θ divides 180°).

I independently re-derived every load-bearing step and ran numerical sweeps (M1 alignment for n∈{3,4,5,7,10,30}; the 2×2 taint casework for non-divisor θ∈{72,50,100,120,135,80,7,√5000}; M2 descent with bound ≤ n−1; the n=2 one-move win; Part A safe-set S closure for θ∈{91,100,120,135,150,179}; M2 same-vertex persistence). **All zero violations.** The shared infrastructure (cut formula, supplementary P-pair, M1, M2, 2×2 casework) is sound.

## Cut operation (independent derivation)

Triangle (A,B,C), Mulan cuts from P on side BC to vertex A, α = ∠BAP ∈ (0,A). Angle chase:
- Child 1 = △ABP = (α, B, 180−α−B) — preserves B.
- Child 2 = △ACP = (A−α, C, B+α) — preserves C.
Both sum to 180; the two fresh P-angles (180−α−B) and (B+α) are supplementary (sum 180). ✓ Verified.

## Load-bearing steps — re-derived and confirmed

**M2 (reduce/descent).** Angle mθ at vertex V (m≥2); cut to V with α=θ. Legality θ<mθ holds for m≥2. C1=(θ,B,180−θ−B) contains θ; C2=((m−1)θ, C, B+θ) carries (m−1)θ at the SAME geometric vertex V (V is a vertex of both children — the cut target persists). Positivity: (m−1)θ>0; C>0; B+θ<180 since B<180−mθ≤180−2θ; 180−θ−B>0 since B<180−2θ. Shan-Yu delays by keeping C2; level m→m−1 at V; at level 2 both children contain θ. Bound m−1, natural-valued strictly-decreasing potential. ✓ (numerically confirmed: max steps = n−1 exactly).

**M1 (alignment).** nθ=180, n≥3, no angle a multiple of θ. Largest angle A≥60≥θ; A=60 only if equilateral+n=3 (already won), so A>θ. Open interval (B, A+B) has length A>θ; multiples spaced θ apart ⟹ ∃ k with B<kθ<A+B (pigeonhole). k≥1 (kθ>B>0), k≤n−1 (kθ<180=nθ). α=kθ−B∈(0,A). P-angles: B+α=kθ and 180−kθ=(n−k)θ. Both positive multiples. All six child angles positive. ✓ (numerically: 0 failures across 1000 trials × 6 values of n).

**n=2 boundary (θ=90°).** Cut to largest A. If A=90 won. If A>90: B+C<90 ⟹ B,C<90. If A<90: acute. So B,C<90. β=90, α=90−B; legality α>0 (B<90), α<A ⟺ C<90 ✓. Both P-angles=90=θ. One move. ✓ (numerically: 0 failures / 10000).

**2×2 taint casework (exclusion crux).** Taint-free parent (A,B,C), B,C untainted. Both children tainted ⟹ witness per child ∈ {α-slot, P-slot}. Four cases:
1. α=k₁θ, A−α=k₂θ ⟹ A=(k₁+k₂)θ, A tainted (or ≥180 impossible). ✗
2. α=k₁θ, B+α=k₂θ ⟹ B=(k₂−k₁)θ, B>0⟹k₂>k₁⟹B tainted. ✗
3. 180−α−B=k₁θ, A−α=k₂θ ⟹ C=(k₁−k₂)θ, C>0⟹k₁>k₂⟹C tainted. ✗
4. 180−α−B=k₁θ, B+α=k₂θ ⟹ 180=(k₁+k₂)θ ⟹ θ=180/(k₁+k₂), a divisor. ✗
All contradict. At least one child taint-free; Shan-Yu keeps it. ✓ (numerically: 0 violations / 5000 trials × 8 non-divisor θ incl. irrational). Sub-families: irrational θ (case 4 needs θ∈ℚ), θ=180·p/q p>1 (case 4 needs p|q), θ>90 (F={θ}, case 4 forces θ≤90, cases 1–3 give angle≥2θ>180) — all handled. Initial taint-free triangle exists: F finite (⌊180/θ⌋ elements) even for irrational θ; finitely many forbidden lines can't cover the open 2-simplex. ✓

**Part A (equilateral-witness distinct exclusion, θ>90°).** S = {all angles ≤90}. Non-P angles of any child ≤90 (since <A≤90); only P-angles can exceed 90; P1+P2=180 ⟹ at most one exceeds 90 ⟹ at least one child ∈ S. Equilateral ∈ S, no angle = θ (≤90<θ). Genuinely geometric (not arithmetic-taint), a proper subset of the taint-free set, closed under the supplementary reflection. ✓ (numerically: 0 violations across 6 values of θ>90).

## Per-approach verdict

### lattice-descent — APPROVE (solved)

Both directions complete and rigorous. Inclusion: M1 alignment (pigeonhole) + M2 descent (natural-valued potential, same-vertex invariant, bound ≤ n−1) + n=2 one-move boundary. Exclusion: taint-free invariant, 2×2 casework (all four cases contradictory), explicit handling of irrational θ, p/q-rational θ with p>1, and θ>90°. Finite bound n−1 explicit. Every theorem named (pigeonhole/extremal, invariants/monovariants, induction/infinite descent, casework/exhaustion). The outline-reviewer's flagged gaps (M2 vertex invariant, M1 positivity, irrational-θ arm, θ>90°) are all closed in the written proof. No hand-waving found. This is the anchor.

### residue-monovariant — APPROVE (solved, with caveat)

The distinct Φ-monovariant crux is **honestly refuted** by the builder (recorded as a dead end with the structural reason: the interval (θ−Φ, Φ) is empty when Φ≤θ/2, so the only β decreasing both P-residues is r(β)=0 = the alignment move itself). The proof then stands on the fallback = M1 + M2 + 2×2 taint casework, which is complete and correct (identical structure to lattice-descent, verified above). The residue-sum identity is retained only as conceptual motivation, explicitly NOT load-bearing — no overclaiming. The proof as written is complete and rigorous; the distinct contribution is dead but that is a ranking matter, not a correctness gap. Caveat: this approach offers no proof-theoretic value beyond lattice-descent.

### equilateral-witness — APPROVE (solved)

Inclusion: M1 + M2 + n=2 (same solid proof). Exclusion: Part A (obtuse safe set S for θ>90°, genuinely independent geometric framing via the supplementary reflection, proven closed) + Part B (shared taint casework covering θ∈(0,90°]). The refuted "equilateral E alone is self-closed" crux is honestly recorded and correctly fixed by enlarging to S ⊋ {E}, with the explicit counterexample (θ=72°, α=48° ⟹ C1=(48,60,72) contains θ) admitted. Part A is a real distinct exclusion for the half-range (90°,180°), breaking the shared wall for that range. Complete and rigorous.

## Shared-wall note for the orchestrator

The exclusion direction shares the 2×2 taint casework across all three approaches (equilateral-witness adds an independent geometric route only for θ>90°). I verified this casework exhaustively by hand and by computation (0 violations across 8 non-divisor θ incl. irrational); the wall is solid. No flaw found that would sink all three.

## Lemmas certified

All three promotable lemmas from lattice-descent admitted into `results/imo-2026-04/lemmas/`:
- `reduce-move.md` (Lemma 1 / M2) — sorry-free, correct, not stronger than proved.
- `alignment-move.md` (Lemma 2 / M1) — sorry-free, correct.
- `taint-free-invariant.md` (Lemma 3) — sorry-free, correct, handles all θ sub-families.

## Verdicts

lattice-descent: APPROVE — complete rigorous proof both directions; all flagged gaps closed; verified independently by hand and computation.
residue-monovariant: APPROVE — distinct Φ-crux honestly refuted; fallback proof (M1+M2+casework) complete and correct; no overclaiming; redundant with lattice-descent.
equilateral-witness: APPROVE — inclusion solid; Part A obtuse safe set is a genuine independent exclusion for θ>90° (proven closed); Part B taint casework covers the rest; refuted E-alone crux honestly fixed.
