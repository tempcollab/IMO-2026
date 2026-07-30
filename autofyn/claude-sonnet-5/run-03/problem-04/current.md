## Status
solved

## Approaches tried
- See approaches/chip-double-force.md, approaches/budget-partition-dimension.md,
  approaches/three-distance-avoidance.md for full history.
- Round 2: chip-double-force.md submitted a claimed complete two-directional proof
  (forward: explicit two-move state machine M1/M2 with Target/Shield/Growing bookkeeping;
  converse: residue-mod-θ clean-triangle invariant, Lemma A + Lemma B). Independently
  re-derived and adversarially checked by the proof-reviewer this round (see
  `/tmp/round-2/proof-reviewer.md` for the full line-by-line verification): the master cut
  formula, M1, M2, the full 4-step algorithm, Lemma A, and Lemma B were all re-derived from
  scratch and additionally checked by independent Python re-implementations (3600 random
  forward-algorithm trials across n=2..19, 0 failures; 300,000 random Lemma-A trials, 0
  counterexamples). One bug was found and fixed in transit: the sibling file
  budget-partition-dimension.md's own Lemma B used a₀:=√2·θ, which is an INVALID angle
  (exceeds 180°) for θ≳127.28°; chip-double-force.md independently uses the correct
  a₀:=θ/√2, which is valid for the entire range 0°<θ<180°. This bug does not affect
  chip-double-force.md's own proof (verified correct), but budget-partition-dimension.md's
  own converse write-up is not fully correct as stated (see its review). No other gaps
  found in chip-double-force.md. **Verdict: APPROVE — Status certified solved.**

## Current best
(superseded — see Full proof below.)

## Full proof

**Answer.** Mulan can guarantee a win in finitely many steps if and only if
θ = 180°/n for some integer n ≥ 2.

**Setup.** A "triangle" is an unordered triple of positive reals (p,q,r) with p+q+r=180.

**Master Cut Formula.** Let a triangle have vertex angles a (at A), b (at B), c (at C),
a+b+c=180°. Let P be a point on side BC, x=∠BAP∈(0,a). Cutting from P to A splits the
triangle into Child₁=(b,x,a+c-x) (triangle ABP) and Child₂=(c,a-x,b+x) (triangle ACP).
*Proof:* triangle angle sum in ABP gives the P-angle 180°-b-x = a+c-x (using a+b+c=180); in
ACP gives 180°-c-(a-x) = b+x. ∎ (Re-derived and independently verified by the reviewer.)

Write ρ:=180/θ; since 0<θ<180, ρ>1, so exactly one of ρ∈ℤ (automatically ρ≥2) or ρ∉ℤ holds.
It suffices to prove (⇐) ρ=n∈ℤ, n≥2 ⟹ Mulan wins; (⇒, contrapositive) ρ∉ℤ ⟹ Shan-Yu survives
forever.

**(⇐) Forward direction.** Two reusable moves, applied to a persistently-labelled state
(Target T, Shield S, Growing G; T+S+G=nθ):

- *General Chip Move (M1)*, precondition T>θ, no current angle=θ: cut the Target vertex at
  x=θ (master formula with a=T,b=G,c=S). Discard-branch=(G,θ,T+S-θ) always contains θ.
  Keep-branch=(S,T-θ,G+θ): if T≠2θ this contains no θ (S≠θ inductively, T-θ≠θ, G+θ≠θ since
  G>0) and is the unique safe continuation (Target'=T-θ, Shield'=S, Growing'=G+θ); if T=2θ,
  Keep-branch also contains θ (T-θ=θ) — both branches lose for Shan-Yu, terminal win.

- *Compensation Move (M2)*, precondition t<θ for one angle t of an (unlabelled) triple
  (t,u,w), t+u+w=nθ, no current angle=θ: not both u,w can be ≥(n-1)θ (else
  2(n-1)θ≤u+w<nθ ⟹ n<2, contradiction), so pick "keep-small"<(n-1)θ and split the other, s,
  at x₁=θ-t (valid: 0<x₁<s). Child_A=(t,θ-t,(n-1)θ), Child_B=(keep-small,s-θ+t,θ)
  (Child_B always contains θ). If n=2, (n-1)θ=θ so Child_A also contains θ — terminal win in
  one move. If n≥3, Child_A contains no θ and becomes the new labelled state
  Target:=(n-1)θ≥2θ, Shield:=t, Growing:=θ-t.

*Algorithm.* (1) if a starting angle already =θ, done. (2) else if some starting angle t<θ,
apply M2 to (t,u,w): ends the game (n=2) or yields Target=(n-1)θ (n≥3), go to (4). (3) else
all three angles >θ: designate one as Target, apply M1 repeatedly (Target strictly decreases
by θ, bounded below); either it hits exactly 2θ (terminal), or drops below θ for the first
time (this can only happen by skipping past — never landing exactly on — θ, since landing
on θ would require the immediately preceding Target to equal 2θ, which is caught first as
terminal); in the latter case treat the current triple as fresh and apply M2 (step 2), go to
(4). (4) if Target=(n-1)θ arose from M2 (n≥3): repeated M1 keeps Target an exact multiple of
θ, decreasing (n-1)θ,(n-2)θ,...,3θ,2θ, terminating in exactly n-2 further M1 applications
(the last one, at Target=2θ, is the terminal win).

Throughout: Shield is a fixed real value ≠θ from the moment it is designated (either one of
the three original angles, known >θ at that point, or a value t<θ produced by M2); Growing
only ever increases from a value that starts either >θ (untouched original angle) or in
(0,θ) (an M2 hand-off), and an increase of exactly θ from a value that was itself never
exactly θ cannot land exactly on θ. This gives, for every n≥2 and every starting triangle, a
fully explicit, deterministic-up-to-Shan-Yu's-forced-replies sequence of at most O(n) moves
after which Mulan wins, regardless of Shan-Yu's choices at each step (at every point he has
at most one non-immediately-losing reply, and taking the immediately-losing one ends the
game in Mulan's favor on the spot; taking the safe one continues the induction, which is
shown to terminate).

**(⇒) Converse direction.** Fix θ with ρ=180/θ∉ℤ. Define g:ℝ→ℝ/ℤ, g(α):=(α/θ) mod 1, a group
homomorphism (α↦α/θ is an isomorphism (ℝ,+)→(ℝ,+); reduction mod 1 is the canonical
quotient). Call α θ-resonant if g(α)=0 (θ itself is θ-resonant: θ=1·θ). Call a triangle
(p,q,r) "clean" if none of p,q,r is θ-resonant.

*Lemma A (one-move safety).* If (p,q,r) is clean and ρ∉ℤ, splitting any vertex (WLOG p) at
any x∈(0,p) — giving Child₁=(q,x,p+r-x), Child₂=(r,p-x,q+x) — cannot make both children
unclean. *Proof:* Child₁ unclean iff g(x)∈{0,g(p)+g(r)}; Child₂ unclean iff
g(x)∈{g(p),-g(q)}. Both unclean forces one of 0=g(p), g(q)=0, g(r)=0 (all impossible, parent
clean) or g(p)+g(r)=-g(q) i.e. g(p+q+r)=g(180)=ρ mod 1=0 i.e. ρ∈ℤ (excluded). ∎

*Lemma B (clean starting triangle exists for every θ∈(0,180)).* Take a₀:=θ/√2 (so
0<a₀<θ<180, and a₀/θ=1/√2 irrational, non-resonant). Let I=(0,(180-a₀)/θ) and
F=ℚ∪{ρ-1/√2-k : k∈ℤ} (countable); pick t∈I∖F (exists since I is uncountable), set
b₀:=tθ, c₀:=180-a₀-b₀. Then b₀,c₀>0 and both non-resonant (b₀/θ=t irrational; c₀=kθ would
force t=ρ-1/√2-k∈F, excluded). So (a₀,b₀,c₀) is clean. [Note: the constant must be θ/√2, not
√2·θ — the latter exceeds 180° for θ≳127.28° and is invalid; this was an error found in
budget-partition-dimension.md's independent derivation and confirmed absent here.]

*Theorem.* Shan-Yu starts from the clean triangle of Lemma B and, at each move, keeps a
clean child (Lemma A guarantees one exists). By induction every triangle he ever holds is
clean, hence never has an angle equal to θ, so Mulan's win condition is never triggered for
any sequence of her moves. ∎

**Boundary check (θ=90°, n=2).** Forward: M2 applied to any starting triangle (at least two
angles <90° always exist, since a triangle can have at most one angle ≥90°) gives a genuine
1-move win. Converse's Lemma A correctly fails to apply at ρ=2∈ℤ (its case-4 exclusion,
g(p)+g(q)+g(r)=ρ mod 1=0, holds exactly when ρ∈ℤ) — no contradiction; the dichotomy is
sharp.

**Verification of the answer (compute_and_prove requirement).** The answer θ=180°/n (n≥2
integer) is stated explicitly above and both directions are proved as full rigorous
arguments (the strongest form of "verification"). In addition: the entire forward algorithm
was independently re-implemented and simulated by the reviewer (3600 random trials spanning
n=2..19), 0 failures, confirming both the algebra and the termination bound; Lemma A's
4-case exhaustive check was independently re-derived algebraically and checked over 300,000
random trials, 0 counterexamples; the θ>90° special case (all-angles-≤90° invariant) was
separately verified as an independent cross-check, consistent with the general Lemma A/B
argument. This is a complete, gap-free proof of both directions.

## Promotable lemmas certified into results/imo-2026-04/lemmas/
- `master-cut-formula.md`
- `general-chip-move.md`
- `compensation-move.md`
- `forward-direction-theorem.md`
- `residue-clean-invariant.md` (Lemma A + Lemma B, with the a₀=θ/√2 vs √2·θ correction noted)
- `theta-gt-90-invariant.md` (special-case cross-check)
