## Status
solved

## Approaches tried
- Direct chip-and-double-force induction on n = 180/θ (this approach), round 1: forward
  direction sketched with two lemmas (Double-Forcing, Chip-Reduction) but the inductive
  hand-off between them was written as informal "iterate the move," which the outline-reviewer
  showed (by literal implementation) can loop forever if the target/shield/growing roles are not
  pinned down explicitly.
- **Round 2 (this update).** Rebuilt the forward direction from scratch as a single explicit,
  persistent state machine on a triple (Target, Shield, Growing) with two named moves (General
  Chip Move, Compensation Move), each with a fully written algebraic derivation and an explicit
  invariant showing Shield is literally constant and Growing is literally monotonic, so there is
  no possible infinite loop — the induction is now on the strictly decreasing real quantity
  Target, which forces termination. Independently re-verified the master formula and both moves'
  algebra symbolically (see below) and ran a full simulation of the exact stated algorithm
  (not a hand-wavy "iterate") over 660 random (n, triangle) pairs for n = 2..12: **0 failures**,
  confirming both correctness and termination of the literal algorithm as written. This closes
  the forward-direction gap flagged by the reviewer.
- **Round 2 new converse progress.** (1) Proved completely, from scratch, the θ>90° sub-case of
  the converse (Shan-Yu maintains "all angles ≤ 90°" forever, a clean invariant-lemma proof,
  algebra checked). This was previously only cited as "solid" from another approach's report; it
  is now proved here in full as part of this approach's self-contained argument. (2) For the
  harder remaining case (0°<θ<90°, 180/θ∉ℤ), replaced the round-1 "pure/impure linear
  independence" sketch (which the reviewer flagged as only checked for one move type at depth 1)
  with a different, more structural framework: showing that the set of starting triangles from
  which Mulan has a forced win in ≤ d moves is, for every finite d, a **finite union of lines**
  in the 2-dimensional triangle-simplex — UNLESS a depth-and-pattern-dependent resonance equation
  in θ alone (not in the triangle's angles) happens to hold, in which case that pattern
  contributes the *entire* simplex. The θ=90° (n=2) universal 1-move win is exhibited as exactly
  one instance of such a resonance. This is a cleaner, more promising mechanism, but classifying
  *all* possible resonance equations across all depths and proving they reduce exactly to
  "180/θ ∈ ℤ" is not complete on its own — but see the next bullet, which closes the whole
  converse by a cleaner route instead of finishing this one.
- **Gap closed this round via a cleaner mechanism (residue mod θ).** Rather than pushing the
  line-counting framework further, I found (and independently derived and numerically verified,
  ~200,000 random trials, 0 failures) a single clean global invariant that resolves the converse
  completely, uniformly for ALL θ with 180/θ∉ℤ (including θ>90°, so it subsumes the separate
  θ>90° invariant lemma above as a special case): track the homomorphism g(α) = (α/θ) mod 1 ∈
  ℝ/ℤ and call a triangle "clean" if none of its three angles has g=0 (i.e. none is an integer
  multiple of θ). A one-move case-check (4 sub-cases, all excluded using only that the parent is
  clean and 180/θ∉ℤ) shows Mulan can never force both children of any move to be simultaneously
  unclean — so Shan-Yu, starting from an explicit clean triangle constructed below, can always
  reply so as to keep a clean triangle forever, and a clean triangle never has an angle equal to
  θ. This argument applies verbatim at every depth and every move type (no per-move-type or
  per-depth gap, unlike the round-1 pure/impure sketch or the line-counting framework above),
  closing the converse completely. Full derivation below. Status is now `solved`.

## Current best

**Target claim.** Mulan can force a win in finitely many steps if and only if
θ = 180°/n for some integer n ≥ 2.

**Master cut formula** (elementary — exterior angle / triangle angle sum). Let a triangle have
vertex angles a (at A), b (at B), c (at C), a+b+c=180°. Let P be a point on side BC, and let
x = ∠BAP ∈ (0,a), so ∠CAP = a-x. Cutting from P to A splits the triangle into ABP and ACP. In
ABP the angles are (at B: b, at A: x, at P: 180-x-b); since a+b+c=180 gives 180-b=a+c, this
P-angle equals a+c-x. In ACP the angles are (at C: c, at A: a-x, at P: 180-(a-x)-c); since
180-c=a+b, this equals b+x. So:
  Child₁ = ABP = (b, x, a+c-x)  (keeps vertex B's angle b unchanged)
  Child₂ = ACP = (c, a-x, b+x)  (keeps vertex C's angle c unchanged)
Both children exist simultaneously for a fixed choice of x (equivalently, of P); Shan-Yu keeps
whichever he prefers and the other is discarded. This was re-derived here from the exterior-angle
/ angle-sum theorem and independently checked with random numeric triangles (script in this
session, see "Verification" below).

### Forward direction (θ=180/n ⟹ Mulan wins): complete, explicit, bounded-move construction

We use only two reusable, fully-derived moves, always applied to a *labelled* current state
(which vertex plays which role — this labelling is exactly the "persistent bookkeeping" the
reviewer required).

**Move M1 (General Chip Move).** State: a triangle with three *designated* roles — Target
(angle T), Shield (angle S), Growing (angle G), T+S+G = nθ, T > θ, no current angle = θ. Mulan
cuts the Target vertex at the point P for which x = θ measured from the Growing-vertex side (this
is a specific, well-defined point since 0<θ<T, and this choice is fully in Mulan's control: she
designated the Shield/Growing labelling at some earlier moment and simply keeps cutting off θ
from the same side each time). Concretely, apply the master formula with a=T, b=G, c=S:
  Discard-branch = (G, θ, T+S-θ)     — this ALWAYS contains angle θ exactly (the "x" slot), for
                                        every value of T,S,G, so this branch is never a survivable
                                        choice for Shan-Yu.
  Keep-branch    = (S, T-θ, G+θ)     — Shield S is untouched, Target drops to T-θ, Growing rises
                                        to G+θ.
*Case T ≠ 2θ:* the Keep-branch has no angle equal to θ: S ≠ θ (Shield's value never changes once
fixed, and it was ≠θ at the moment it was designated — justified below by induction on the whole
procedure), T-θ ≠ θ (since T≠2θ by hypothesis of this case), and G+θ ≠ θ (since G>0, always, as
every angle is positive). So this is a genuine safe reply for Shan-Yu, and since the discard
branch always loses, he is *forced* to take it (any rational player avoids an immediate loss when
a safe alternative exists). The move is deterministic: new state is (Target'=T-θ, Shield'=S,
Growing'=G+θ), same roles carried forward.
*Case T = 2θ:* Keep-branch = (S, θ, G+θ) — now contains θ as well (T-θ=θ). Both branches contain
θ. Shan-Yu has no reply avoiding an immediate angle-θ; the game ends, Mulan wins, in this one
move. This is the **terminal** application of M1.

Algebra of M1 checked symbolically and numerically (script `/tmp/check.py`, "Chip move algebra
OK", 2000 random trials).

**Move M2 (Compensation Move).** State: a triangle with angles (t,u,w), t+u+w = nθ, t<θ, no
current angle = θ (this is a *fresh* unlabelled triple — used once, to bootstrap M1's labels).

*Claim:* not both of u,w are ≥ (n-1)θ. Proof: if both were, then u+w ≥ 2(n-1)θ; but also
u+w = nθ-t > nθ-θ = (n-1)θ, and u+w<nθ (as t>0); the two bounds give
2(n-1)θ ≤ u+w < nθ, so 2(n-1) < n, i.e. n<2, contradicting n≥2. So at least one of u,w is
< (n-1)θ; call it "keep-small" (relabel if necessary) and call the other "s" (the vertex to be
split).

Split vertex s at x₁ = θ-t. Validity: x₁>0 since t<θ; x₁<s since s+t = nθ-(keep-small) >
nθ-(n-1)θ = θ, i.e. s > θ-t = x₁. Apply the master formula with a=s, b=t, c=keep-small:
  Child_A = (t, θ-t, s+keep-small-θ) = (t, θ-t, nθ-θ) = (t, θ-t, (n-1)θ)
    [using s+t+keep-small = nθ, so s+keep-small-θ = (nθ-t)-θ, and then adding/removing t:
     s+keep-small-x₁ = s+keep-small-θ+t = (s+t+keep-small)-θ = nθ-θ = (n-1)θ.]
  Child_B = (keep-small, s-θ+t, t+x₁) = (keep-small, s-θ+t, θ)  [since t+x₁=t+θ-t=θ exactly]
Child_B always contains θ exactly — Shan-Yu avoids it if it is not already a certain loss he
prefers over Child_A, but since Child_A does not (generically) also contain θ, Child_B is simply
a losing branch. Two sub-cases:
- If n=2: (n-1)θ = θ, so Child_A = (t,θ-t,θ) ALSO contains θ. Both branches lose for Shan-Yu —
  the game ends, Mulan wins, in this one move (this is the n=2 "any acute-enough angle" 1-move
  win, and subsumes what would otherwise be a separate base case).
- If n≥3: Child_A = (t, θ-t, (n-1)θ) has no angle equal to θ (t≠θ given; θ-t=θ would need t=0,
  impossible; (n-1)θ=θ would need n=2, excluded here). Shan-Yu is forced to Child_A. We now
  *designate* Target := (n-1)θ (the third coordinate), Shield := t, Growing := θ-t (an arbitrary
  but fixed choice of which of the two small angles is "shield" — either choice is valid, we fix
  one). Since n≥3, n-1≥2, so Target = (n-1)θ ≥ 2θ > θ: M1 is applicable next.

Algebra of M2 checked symbolically and numerically (script `/tmp/check.py`, "Compensation move
algebra OK", 2000 random trials).

**Full algorithm and termination (strong induction on the value of Target / on n).**
Given any starting triangle (a,b,c), a+b+c = nθ, n≥2 an integer:
1. If some starting angle already equals θ: Mulan has already won (0 moves).
2. Otherwise, if some starting angle t<θ: apply M2 directly to (t, u, w) (the other two). By the
   case analysis above this ends the game immediately (n=2) or produces a labelled state with
   Target = (n-1)θ, an exact integer multiple of θ, Shield = t, Growing = θ-t (n≥3). Go to step 4.
3. Otherwise, all three starting angles are >θ (they cannot equal θ by step 1, and none is <θ by
   assumption of this branch). Designate any one of the three, say the first, as Target, and the
   other two as Shield, Growing (arbitrary fixed choice). Apply M1 repeatedly: since Target is a
   fixed positive real number decreasing by exactly θ at each application, and each application
   is checked against the terminal condition Target=2θ (ending the game immediately if reached),
   this process must terminate in one of two ways after finitely many steps (Target starts
   ≤ nθ, so at most ⌈(nθ)/θ⌉ = n applications are possible before Target ≤ θ):
   - it hits exactly Target=2θ at some step: terminal win, done; or
   - it reaches a step where the *current* Target value (before applying M1) is < θ for the
     first time (this must happen since Target decreases by the fixed amount θ each step and
     starts finite): stop M1, and now treat the *current labelled triple* (Target, Shield,
     Growing) as a fresh unlabelled triple (t,u,w) with t = Target < θ, and go to step 2's
     procedure, i.e. apply M2 to it. (Growing is safe throughout this phase: Growing_new =
     Growing_old+θ > θ ≠ ... in fact Growing only ever *increases* from a positive starting value,
     so it is always >0 and, once increased at least once, >θ; if never increased it is the
     original designated angle, which is >θ by the case-3 hypothesis (all three starting angles
     >θ) — either way Growing is never equal to θ during this phase, since it never equals a
     value forced to be exactly θ by the recursion: an increase of θ from a positive value can
     equal θ only if the value before the last increase was 0, impossible. Shield is likewise
     safe: it is fixed at one of the three original angles, all of which are >θ ≠ θ automatically
     in case 3.)
4. If Target = (n-1)θ was produced by M2 (n≥3): apply M1 repeatedly. Since Target is now an
   *exact* integer multiple of θ, subtracting θ at each M1 application keeps it an exact integer
   multiple: (n-1)θ, (n-2)θ, ..., 3θ, 2θ. It never overshoots or undershoots (each step is an
   exact subtraction of θ from an exact multiple of θ), so it reaches exactly 2θ after precisely
   (n-1)-2 = n-3 applications, and the (n-2)-th application (at Target=2θ) is the terminal,
   game-ending move. Throughout, Shield=t is untouched and (by t≠θ, fixed at the moment of M2)
   safe forever; Growing = θ-t, θ, 2θ, ... increases from θ-t (which is in (0,θ), so ≠θ) and each
   subsequent value is θ-t+kθ for k≥1, which is >θ, hence also ≠θ. (Formally: θ-t+kθ=θ would need
   t=kθ; but t<θ and k≥1 forces kθ≥θ>t, contradiction; so no term of this sequence equals θ.)

This gives, for every integer n≥2 and every starting triangle, an explicit, fully-labelled,
deterministic-for-Shan-Yu (he never has more than one non-immediately-losing reply, until the
final terminal move where he has none) sequence of at most O(n) moves after which the game ends
with Mulan winning. Finiteness (all that CLAUDE.md / the problem requires — "in finitely many
steps," not a minimal count) is established.

**End-to-end verification of the literal algorithm.** I implemented steps 1–4 exactly as
written above (not a paraphrase) in Python and ran it over n=2..12, 60 random starting triangles
each (660 trials total): **0 failures**, every trial terminates with Mulan winning, well within
the claimed O(n) move bound (script `/tmp/check2.py` in this session). This directly answers the
outline-reviewer's concern: the algorithm as stated, with the Target/Shield/Growing roles fixed
and threaded through explicitly (never "re-searched from scratch"), provably terminates because
Target is a strictly-decreasing real-valued potential function bounded below, and the two moves
(M1, M2) are the *only* moves ever invoked — there is no ambiguity or possibility of looping.

### Converse direction (Shan-Yu survives when Mulan cannot force θ): partially complete

**Sub-case θ>90°: complete, self-contained proof.**

*Invariant Lemma.* If a triangle has all three angles ≤90°, then for **any** cut Mulan makes
(any vertex a with others b,c≤90°, any x∈(0,a)), at least one of the two children
Child₁=(b,x,a+c-x), Child₂=(c,a-x,b+x) again has all three angles ≤90°.

*Proof.* Since a+c-x and b+x are the two P-angles of a straight cut, they sum to
(a+c-x)+(b+x) = a+b+c = 180. Hence at most one of them exceeds 90° (if both did, their sum would
exceed 180). Two cases:
- a+c-x ≤ 90°: then Child₁ = (b, x, a+c-x) has b≤90° (given), x<a≤90° (given a≤90°, and x<a),
  and a+c-x≤90° (this case's hypothesis) — all three ≤90°.
- a+c-x > 90°: then (from the supplementary-sum fact) b+x < 90° (strictly, since the sum is
  exactly 180 and one term exceeds 90 the other is strictly below), so Child₂ = (c, a-x, b+x) has
  c≤90° (given), a-x<a≤90° (given a≤90, x>0), and b+x<90° — all three ≤90°.
In either case at least one child is entirely ≤90°. ∎ (Algebra checked numerically, 20000 random
samples, script in this session, 0 violations.)

*Theorem.* If θ>90°, Shan-Yu wins (survives forever): he starts with any triangle all of whose
angles are ≤90° (e.g. equilateral 60°-60°-60°, which also trivially has no angle equal to θ since
60°<90°<θ), and at every one of Mulan's moves he applies the Invariant Lemma to pick a child that
again has all angles ≤90°(possible by the Lemma, regardless of Mulan's choice of vertex and x).
Since every angle in every triangle that ever occurs is ≤90°<θ, no angle can ever equal θ, so the
game never stops with a win for Mulan — it continues forever. ∎

**General case 180/θ∉ℤ (all of 0°<θ<180° with ρ:=180/θ not an integer): COMPLETE via a residue
invariant.** This single argument covers the whole converse (it also re-proves θ>90° above, as a
special case, uniformly — since for θ>90°, ρ=180/θ<2 and ρ>1, so ρ is automatically not an
integer).

**Definition.** For a nonzero real θ, define g : ℝ → ℝ/ℤ by g(α) = (α/θ) mod 1 (the class of α/θ
in ℝ/ℤ). Since α ↦ α/θ is an additive-group isomorphism (ℝ,+)→(ℝ,+) (as θ≠0) and reduction mod 1
is the canonical quotient homomorphism ℝ→ℝ/ℤ, the composite g is a **group homomorphism**:
g(α+β)=g(α)+g(β) and g(-α)=-g(α) for all real α,β. Call α **θ-resonant** if α is an integer
multiple of θ, i.e. g(α)=0; otherwise **non-resonant**. Call a triangle (p,q,r) (p+q+r=180, all
>0) **clean** if none of p,q,r is θ-resonant. Note θ itself is θ-resonant (=1·θ), so a clean
triangle never has an angle equal to θ.

**Lemma A (one-move safety).** Suppose (p,q,r) is clean and 180/θ∉ℤ. If Mulan splits vertex p
(WLOG, by symmetry of the three vertices) at any x∈(0,p), producing
Child₁=(q,x,p+r-x) and Child₂=(r,p-x,q+x) (master formula applied to vertex p, other two q,r),
then it is impossible for both children to be unclean.

*Proof.* Child₁'s angle q is inherited unchanged from the clean parent, hence non-resonant; so
Child₁ is unclean iff one of its two *new* angles, x or p+r-x, is resonant, i.e.
g(x)=0 or g(p+r-x)=g(p)+g(r)-g(x)=0, i.e. g(x) ∈ {0, g(p)+g(r)}.
Similarly Child₂'s angle r is inherited (non-resonant), so Child₂ is unclean iff
g(p-x)=g(p)-g(x)=0 or g(q+x)=g(q)+g(x)=0, i.e. g(x) ∈ {g(p), -g(q)}.
If both children were unclean, g(x) would lie in {0,g(p)+g(r)} ∩ {g(p),-g(q)}, forcing one of:
1. 0 = g(p) — impossible, p is non-resonant (parent clean).
2. 0 = -g(q), i.e. g(q)=0 — impossible, q is non-resonant.
3. g(p)+g(r) = g(p), i.e. g(r)=0 — impossible, r is non-resonant.
4. g(p)+g(r) = -g(q), i.e. g(p)+g(q)+g(r) = 0 in ℝ/ℤ.
For case 4: since g is a homomorphism, g(p)+g(q)+g(r) = g(p+q+r) = g(180) = (180/θ) mod 1 =
ρ mod 1, which is 0 in ℝ/ℤ exactly when ρ∈ℤ — excluded by hypothesis (ρ∉ℤ). So case 4 is also
impossible. All four cases are impossible, so it is never true that both children are unclean —
at least one is clean. ∎

*Verification.* Re-derived and checked independently by direct random simulation (not just the
sibling budget-partition-dimension.md's own check): 199,999 random (θ,p,q,r,x) with (p,q,r) clean
and ρ non-integer, testing directly whether "Child₁ unclean AND Child₂ unclean" ever holds — **0
occurrences** (script run in this session).

**Lemma B (existence of a clean starting triangle, for every θ).** For every θ∈(0,180) there
exists a triangle (a₀,b₀,c₀), a₀+b₀+c₀=180, all positive, with none of a₀,b₀,c₀ θ-resonant.

*Proof.* Set a₀ := θ/√2, so 0<a₀<θ<180 (a valid positive angle less than 180), and
a₀/θ = 1/√2 is irrational, hence a₀ is non-resonant. Let
I := {t∈ℝ : 0<t<(180-a₀)/θ}, a nonempty open interval (nonempty since a₀<180). Let
F := ℚ ∪ {ρ - 1/√2 - k : k∈ℤ}, a countable subset of ℝ (countable union of countable sets). Since
I is an interval it is uncountable, so I∖F ≠ ∅; pick t∈I∖F and set b₀ := tθ. Then:
- b₀>0 and a₀+b₀=(1/√2+t)θ<180 (since t<(180-a₀)/θ), so c₀:=180-a₀-b₀>0: genuine triangle.
- b₀/θ=t is irrational (t∉ℚ⊆F), so b₀ is non-resonant.
- c₀ is non-resonant: if c₀=kθ for integer k, then 180-a₀-b₀=kθ ⟹ ρθ-θ/√2-tθ=kθ ⟹
  t=ρ-1/√2-k, contradicting t∉F (F excludes exactly these values for every integer k).
Hence (a₀,b₀,c₀) is clean. ∎

**Theorem (converse, general case).** If ρ=180/θ∉ℤ, Shan-Yu wins (survives forever): he starts
with the clean triangle (a₀,b₀,c₀) of Lemma B, and at every move, of the (at least one, by Lemma
A) clean child(ren) produced, he keeps a clean one.

*Proof.* By induction on the number of moves played, the triangle Shan-Yu holds is always clean:
base case is Lemma B; inductive step, if the current triangle is clean and Mulan makes any legal
move (any vertex, any split value), Lemma A guarantees at least one child is clean, and Shan-Yu
keeps it. Since every triangle Shan-Yu ever holds is clean, none of its angles is ever
θ-resonant, and in particular none is ever equal to θ (θ=1·θ is θ-resonant). So the game's win
condition is never triggered, for any sequence of moves by Mulan — she cannot force a win in any
finite number of steps. ∎

This completes the converse for every θ with 180/θ∉ℤ, uniformly (no split into θ>90° / θ<90°
sub-cases needed — though the θ>90° Invariant Lemma proved earlier stands as an independent,
simpler cross-check for that special case, consistent with this general result).

**(Retained for the record, not needed for the final proof.)** Below is round-2's
line-counting framework, developed before the residue-mod-θ mechanism above was found; it is
superseded by the complete argument above and is kept only as additional context /
cross-verification (e.g. it independently identifies θ=90° as the unique "whole-simplex
resonance" at depth 1, consistent with Lemma A excluding exactly ρ∈ℤ).

*Framework.* Represent a triangle
state by (a,b) with c=180-a-b (a,b>0, a+b<180) — a point of the open 2-simplex Δ. Define
L₀ = {(a,b,c)∈Δ : a=θ or b=θ or c=θ}, a union of 3 line segments in Δ. Define, for d≥1,
L_d = L₀ ∪ {states from which Mulan has a single cut, at some vertex, with some x, such that
BOTH resulting children lie in L_{d-1}}. By definition, "Mulan forces a win from state σ within
d moves" is equivalent to σ ∈ L_d, and "Mulan can force a win in some finite number of moves" is
equivalent to σ ∈ L := ⋃_{d≥0} L_d.

*Key structural fact, established for d=0,1 and the mechanism explained in general (not yet
fully proven for all d — this is the gap).* Suppose L_{d-1} is a **finite union of lines** in Δ
(true for d=1, since L₀ is 3 lines). Fix a vertex to cut (say vertex a, others b,c) and a pair of
defining linear conditions, one from a line ℓᵢ of L_{d-1} applied to Child₁=(b,x,a+c-x) and one
from a line ℓⱼ applied to Child₂=(c,a-x,b+x). Each condition is a single linear equation in x
(with coefficients depending affinely on a,b,c); generically (i.e. when the coefficient of x does
not vanish) it determines x as an affine function x=f_i(a,b,c) resp. x=f_j(a,b,c). Requiring both
simultaneously forces f_i(a,b,c)=f_j(a,b,c), a linear equation in (a,b,c) (equivalently, using
a+b+c=180, in the 2 free coordinates (a,b)). Two possibilities after simplification:
  (α) the (a,b)-dependence does *not* cancel: this is a genuine line in Δ, contributing (a
      sub-segment of) one more line to L_d;
  (β) the (a,b)-dependence *cancels entirely*, leaving a pure equation in θ alone (no a,b,c),
      e.g. for the pairing "x=θ" (from Child₁'s middle slot) together with "a+c-x=θ" (from
      Child₁'s last slot, i.e. asking Child₁ itself to already be a double-hit): eliminating x
      gives a+c=2θ — a genuine LINE (not vacuous) unless further paired with additional
      structure. But for the specific pairing appearing in the n=2 universal win (identified in
      the Compensation Move derivation above): pairing "b+x=θ" (Child₂'s last slot) with
      "a+c-x=θ" (Child₁'s last slot) forces, after eliminating x (x=θ-b from the first, so
      a+c-(θ-b) = a+b+c-θ = 180-θ), the condition 180-θ=θ, i.e. **θ=90°** — a condition on θ
      ALONE, independent of (a,b,c): when it holds, this single pairing certifies EVERY
      (a,b,c)∈Δ (with b<θ, which is always satisfiable) as an immediate 1-move win, matching the
      Invariant/Theorem proven directly above for n=2. This confirms mechanism (β) is exactly
      what produces "whole-simplex" wins, and exhibits θ=90° (n=2) as one concrete instance.

*What is proven:* d=0 (L₀, 3 lines) and the d=1 case worked out in full generality above (every
pairing at d=1 is classified as case (α), giving a line, or case (β), giving either the empty
contribution or, only when θ=90° exactly, the whole simplex — I verified by direct case
enumeration over the 3×3 pairings at d=1, for a general vertex choice, that θ=90° is the *only*
value of θ for which any d=1 pairing degenerates to case (β) with a satisfiable condition; all
other θ produce only lines at d=1).

*What is NOT yet proven (the gap):* that this dichotomy continues at every depth d≥2 — i.e. that
(i) L_d remains a finite union of lines whenever no case-(β) resonance has fired, and (ii) EVERY
possible case-(β) resonance condition, at every depth and for every pairing/targeting pattern
(there are finitely many patterns at each depth, but their number can grow with d, and the
algebra of eliminating x across d nested applications of the master formula, i.e. eliminating
d successive split-variables x₁,...,x_d, is more involved than the single-elimination done above
for d=1), reduces to an equation of the exact form "mθ=180 for some positive integer m ≤ (a bound
depending on d)" — and no *other* accidental resonance in θ (e.g. some resonance that would hold
for a θ not of the form 180/m) ever occurs. The depth-2/3 "3θ, 4θ trigger" patterns found
numerically by the verification explorer (math-explorer-verify.md, section 2) are *consistent*
with this — every trigger found was an exact integer multiple of θ — but a full inductive proof
covering all depths and all pairing patterns has not been written out. If this classification is
established, the converse would follow immediately: whenever 180/θ∉ℤ, no depth ever produces a
case-(β) resonance, so every L_d is a finite union of lines, so L = ⋃L_d is a countable union of
lines (countably many finite sets of lines, one set per depth), which is a Lebesgue-measure-zero
(and nowhere dense) subset of the 2-dimensional simplex Δ; Shan-Yu, who chooses the starting
triangle FIRST and freely, simply picks any (a₀,b₀)∈Δ avoiding this countable union of lines
(possible since Δ is uncountable and a countable union of lines cannot cover it, e.g. take a₀ to
be any positive transcendental number smaller than 90 with a₀+b₀<180 for a further generic choice
of b₀ avoiding the at-most-countably-many resulting linear constraints on b₀ given a₀) — from
this starting triangle Mulan can never force θ in any finite number of moves.

This is a genuinely different and more structural mechanism than round 1's pure/impure
linear-independence sketch (which the reviewer correctly flagged as checked only for one move
type at depth 1); it is not yet a complete proof, but it isolates the *exact* single remaining
lemma needed (the resonance-classification claim above) rather than leaving the whole converse
diffuse.

## Full proof

**Answer.** Mulan can guarantee a win in finitely many steps if and only if
θ = 180°/n for some integer n ≥ 2.

**Setup.** Throughout, a "triangle" is an unordered triple of positive reals (p,q,r) with
p+q+r=180. The master cut formula (derived above from the exterior-angle/angle-sum theorem):
splitting the vertex of angle a (other two b,c) at x∈(0,a) yields the two possible child
triangles Child₁=(b,x,a+c-x) and Child₂=(c,a-x,b+x); Shan-Yu keeps one, discards the other.
Write ρ := 180/θ; since 0<θ<180 we always have ρ>1, so exactly one of the following holds:
ρ∈ℤ (automatically ρ≥2, since ρ>1) or ρ∉ℤ. These two cases are exhaustive and mutually
exclusive, so it suffices to prove: (⇐) ρ=n∈ℤ, n≥2 ⟹ Mulan wins; (⇒, contrapositive) ρ∉ℤ ⟹
Shan-Yu survives forever.

**(⇐) Forward direction.** Proved in full in "Current best" above via the General Chip Move
(M1) and Compensation Move (M2), assembled into the 4-step algorithm. Summary of the argument:
(1) if the starting triangle already has an angle =θ, done; (2) if some starting angle t<θ,
Compensation Move M2 (using the identity that not both of the other two angles can be ≥(n-1)θ,
proved via the inequality 2(n-1)θ ≤ u+w < nθ ⟹ n<2) either wins in one move (n=2) or produces an
exact-multiple vertex (n-1)θ; (3) if all starting angles are >θ, repeated General Chip Moves
(each: cut the Target vertex at x=θ, which always makes the discard-branch contain θ exactly and
the keep-branch (Shield unchanged, Target-θ, Growing+θ) the unique safe reply unless Target=2θ,
in which case both branches contain θ and the game ends) decrease Target by θ each move until
either Target=2θ (terminal win) or Target first drops below θ, reducing to case (2); (4) from an
exact multiple-of-θ Target=(n-1)θ (n≥3), repeated General Chip Moves keep Target an exact
multiple, terminating in exactly n-3 further moves plus 1 terminal move when Target=2θ. Every
move is fully specified (which vertex, which split value, which of the two non-target angles is
"Shield" vs "Growing"), Shield is proved to be safe forever (fixed real value, ≠θ from the moment
it is set), Growing is proved to be safe forever (strictly increasing from a positive value,
crosses θ at most once and never lands on it exactly by construction), and Target is a strictly
decreasing real-valued potential bounded below by 0, so the whole procedure terminates in a
finite (O(n)) number of moves for every starting triangle. (Full algebraic derivation of M1, M2,
and the algorithm's termination is in "Current best" above; the literal algorithm was
additionally end-to-end simulated over 660 random trials, n=2..12, 0 failures.)

**(⇒) Converse direction.** Proved in full above via the residue homomorphism g(α)=(α/θ) mod 1
∈ ℝ/ℤ: a triangle is "clean" if none of its three angles is θ-resonant (an integer multiple of
θ). Lemma A shows that whenever a clean triangle is cut (any vertex, any split value) and ρ∉ℤ,
it is impossible for both children to be unclean (a 4-case exhaustive algebraic check using only
that g is a group homomorphism, that the parent's three angles are non-resonant, and that
g(180)=ρ mod 1 ≠0 since ρ∉ℤ). Lemma B exhibits, for every θ, an explicit clean starting triangle
(a₀,b₀,c₀)=(θ/√2, tθ, 180-θ/√2-tθ) for a suitably generic t. Shan-Yu starts from this triangle
and, at each of Mulan's moves, keeps a clean child (guaranteed to exist by Lemma A); by induction
on the move count, every triangle he ever holds is clean, so no angle he ever holds equals θ, so
the game's win condition is never triggered — Mulan cannot force a win in any finite number of
moves, for any strategy she uses.

**Verification of the answer.** Both directions were checked algebraically (derivations above,
using only the elementary master cut formula and, for the converse, the elementary fact that
α↦(α/θ) mod 1 is a group homomorphism ℝ→ℝ/ℤ) and numerically: the forward algorithm was
simulated end-to-end (660 trials, n=2..12, 0 failures) and Lemma A's exhaustive case analysis was
checked by direct random simulation (≈200,000 trials, 0 counterexamples) and, in the sibling
approach that first found this mechanism, by an additional adversarial root-enumeration check
(100,000 trials, 0 failures). The boundary case θ=90° (n=2, ρ=2∈ℤ) is consistent on both sides:
the forward construction gives a genuine 1-move universal win, and the converse's Lemma A
correctly fails to apply (case 4 of its proof, g(p)+g(q)+g(r)=g(180)=ρ mod 1=0, is exactly the
excluded case precisely when ρ∈ℤ), so there is no contradiction at the boundary — it is a sharp
dichotomy. ∎

## Promotable lemmas

- **Master Cut Formula** (re-derivation from the exterior-angle/angle-sum theorem): stated and
  proved in "Current best" above. Reusable by any approach to this problem.
- **General Chip Move Lemma (M1)**: given a labelled triangle state (Target T>θ, Shield S,
  Growing G, T+S+G=nθ, no current angle =θ), cutting the Target vertex at x=θ (measured from the
  Growing side) produces a discard-branch that always contains θ and a keep-branch
  (S, T-θ, G+θ) that is Shan-Yu's unique safe reply whenever T≠2θ, or is itself a second
  θ-containing branch (terminal win) when T=2θ. Proved in full above, algebra verified
  numerically (2000 trials, 0 failures).
- **Compensation Move Lemma (M2)**: given an unlabelled triangle (t,u,w), t+u+w=nθ (n≥2 integer),
  t<θ, no current angle=θ, Mulan can split one of u,w (whichever is <(n-1)θ, guaranteed to exist)
  at x=θ-t to produce a branch containing θ exactly and a branch equal to either (t,θ-t,θ)
  [n=2, itself already a second θ-hit, terminal] or (t,θ-t,(n-1)θ) [n≥3, a fresh labelled state
  with an exact multiple-of-θ Target]. Proved in full above, algebra verified numerically (2000
  trials, 0 failures).
- **Forward Direction Theorem**: for every integer n≥2 (θ=180°/n) and every starting triangle,
  the explicit algorithm (steps 1–4 above, built only from M1 and M2) forces a Mulan win in a
  finite (O(n)) number of moves. Proved in full above; the literal algorithm was additionally
  end-to-end simulated (660 trials, n=2..12, 0 failures).
- **θ>90° Survival Invariant Lemma**: if a triangle has all angles ≤90°, then any single master-
  formula cut leaves at least one child with all angles ≤90°; hence for θ>90°, Shan-Yu starting
  from any all-≤90° triangle (e.g. equilateral) and always choosing such a child survives
  forever. Proved in full above, algebra verified numerically (20000 trials, 0 violations). (Now
  subsumed by Lemma A/B below, which cover all θ with 180/θ∉ℤ uniformly, but retained as an
  independent, simpler cross-check for the θ>90° special case.)
- **Lemma A (residue-mod-θ one-move safety)**: if (p,q,r) is a triangle with none of p,q,r an
  integer multiple of θ, and ρ=180/θ∉ℤ, then for any split of any vertex at any valid cut point,
  at least one resulting child has no vertex angle that is an integer multiple of θ (in
  particular none equal to θ). Proved in full above by an exhaustive 4-case check via the
  homomorphism g:ℝ→ℝ/ℤ, g(α)=α/θ mod 1; algebra independently checked numerically (≈200,000
  random trials, 0 counterexamples, this session). This is the central engine of the converse
  direction.
- **Lemma B (existence of a clean/non-resonant starting triangle)**: for every θ∈(0,180) there is
  a triangle with no angle an integer multiple of θ, explicitly (θ/√2, tθ, 180-θ/√2-tθ) for
  suitable t avoiding a countable forbidden set. Proved in full above.

These items together constitute a complete, gap-free proof of both directions of the target
characterization: Master Formula + M1 + M2 + Forward Direction Theorem prove "if
θ=180°/n (n≥2 integer) then Mulan wins"; Lemma A + Lemma B prove "if 180/θ∉ℤ then Shan-Yu
survives forever" (which, combined with ρ=180/θ>1 always holding, is exactly the complementary
case to the forward direction). The θ>90° Invariant Lemma is a proved, independent special-case
cross-check of the converse. Status: solved.
