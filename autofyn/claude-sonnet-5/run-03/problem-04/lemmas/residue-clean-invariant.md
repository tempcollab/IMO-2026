## Residue-mod-θ Clean Invariant (Lemma A + Lemma B)

**Definitions.** Fix θ with ρ:=180/θ ∉ ℤ. Let g:ℝ→ℝ/ℤ, g(α) := (α/θ) mod 1; this is a group
homomorphism since α↦α/θ is a group isomorphism (ℝ,+)→(ℝ,+) and reduction mod 1 is the
canonical quotient ℝ→ℝ/ℤ. Call α θ-resonant if g(α)=0 (i.e. α is an integer multiple of θ;
in particular θ itself is θ-resonant, being 1·θ). Call a triangle (p,q,r) "clean" if none of
p,q,r is θ-resonant.

**Lemma A (one-move safety).** If (p,q,r) is clean and ρ∉ℤ, then for any split of any vertex
(WLOG p) at any x∈(0,p) — giving Child₁=(q,x,p+r-x), Child₂=(r,p-x,q+x) via the Master Cut
Formula — it is impossible for both children to be unclean.

*Proof.* Child₁'s inherited angle q, Child₂'s inherited angle r are non-resonant (clean
parent). Child₁ is unclean iff g(x)∈{0, g(p)+g(r)}; Child₂ is unclean iff
g(x)∈{g(p), -g(q)}. Both unclean forces one of: (1) 0=g(p), (2) g(q)=0, (3) g(r)=0 — all
impossible since p,q,r non-resonant — or (4) g(p)+g(r)=-g(q), i.e. g(p)+g(q)+g(r)=0, i.e.
g(p+q+r)=g(180)=ρ mod 1=0, i.e. ρ∈ℤ, excluded by hypothesis. All four cases impossible. ∎

**Lemma B (existence of a clean starting triangle).** For every θ∈(0,180) there is a
triangle (a₀,b₀,c₀), a₀+b₀+c₀=180, all positive, none θ-resonant. Construction:
a₀ := θ/√2 (so 0<a₀<θ<180, valid; a₀/θ=1/√2 irrational so a₀ non-resonant); pick
t ∈ I∖F where I=(0,(180-a₀)/θ) and F=ℚ∪{ρ-1/√2-k : k∈ℤ} (countable), set b₀:=tθ,
c₀:=180-a₀-b₀. Then b₀,c₀ non-resonant and all positive (algebra: t∉F rules out both
b₀ rational-ratio and c₀ resonance simultaneously).

**IMPORTANT — correct constant.** Use a₀ := θ/√2 (NOT √2·θ). The version a₀:=√2·θ, found
independently in `budget-partition-dimension.md`, is WRONG in general: for θ ≥ 180/√2 ≈
127.28°, a₀=√2θ ≥ 180°, an invalid angle. θ/√2 is always < θ < 180 for all θ in the valid
range, so it is the correct, fully general choice.

**Theorem (converse).** If ρ=180/θ∉ℤ, Shan-Yu starts from the clean triangle of Lemma B and,
at each of Mulan's moves, keeps a clean child (guaranteed by Lemma A). By induction every
triangle he ever holds is clean, hence never has an angle equal to θ — Mulan cannot force a
win in any finite number of moves.

**Verification.** Re-derived independently by the reviewer. Numerically checked Lemma A over
300,000 random (θ,p,q,r,x) with clean parent and ρ∉ℤ: 0 counterexamples. Numerically
confirmed the a₀=√2θ bug (fails for θ=128°,150°,170°,179° in the sample checked) and
confirmed a₀=θ/√2 is valid for all θ∈(0,180).

**Source.** Certified from `results/imo-2026-04/approaches/chip-double-force.md` (round 2),
which independently corrected the a₀ constant found in `budget-partition-dimension.md`.
