## Status
partial

## Approach: binary-word-invariant (round 2 rewrite)

Target: the problem's actual claim — determine exactly S = {θ ∈ (0°,180°) : Mulan can
force a win in finitely many moves against every Shan-Yu play}.

This round replaces the abstract-orbit sketch with a **complete classification of every
single-move "forcing" primitive available in the real game**, grounded directly in the
cut formula (not an assumed abstract generator set), and uses it to (a) build a
substantially larger and *fully verified* explicit constructive family than
`dyadic-scaffold`'s, (b) resolve the 180/7° computational witness definitively as
**genuine, with a hand-checked exact-fraction move sequence**, and (c) narrow the
necessity gap to one precisely stated, honestly unproven step.

### 0. Setup (shared cut formula, re-derived)

A triangle is an unordered angle-triple (p,q,r) with p+q+r=180°, all positive. A legal
Mulan move picks a vertex P (angle p) and a point X on the interior of the opposite side
QR, cutting PX. Writing x1 = ∠QPX ∈ (0,p) (this ranges over all of (0,p) as X ranges
over the open segment QR — continuity: as X→Q, x1→0; as X→R, x1→p; ∠PXQ and ∠PXR are
continuous, supplementary, and by IVT ∠QPX attains every value strictly between), the
two children are
  A = {q, x1, r+p−x1} (contains Q),  B = {r, p−x1, q+x1} (contains R).

**Identity (★):** (r+p−x1) + (q+x1) = p+q+r = 180°, i.e. the "new" angle in A and the
"new" angle in B are always supplementary. Verified symbolically:
`(r+p−x1)+(q+x1)−(p+q+r) = 0` (sympy `simplify`, confirmed in this round). This is the
single algebraic engine of everything below.

Shan-Yu, after Mulan's cut, discards one of {A,B}; being adversarial, if exactly one of
A, B contains θ, he discards the θ-containing one and keeps the other (he never
voluntarily hands Mulan the win). Only if **both** contain θ is he forced to lose in that
move ("double hit"); otherwise, if **neither** contains θ, he is free to pick either.

### 1. Necessity: θ > 90° is impossible (imported, re-verified)

By (★), if p,q,r ≤ 90°, at most one of the two candidate "new" angles (r+p−x1, q+x1)
can exceed 90° (their sum is 180°). So whichever child Shan-Yu is forced to consider,
at least one of A, B is still non-obtuse (all three angles ≤ 90°). Shan-Yu's strategy:
start with any non-obtuse triangle (e.g. equilateral) and, at every subsequent step,
always keep a non-obtuse child (one exists by the above, for **every** x1 Mulan might
choose, since the argument only used p,q,r ≤ 90 and (★), not any specific x1). By
induction the triangle is non-obtuse forever, so no angle >90° is ever produced, and in
particular θ > 90° never appears. Hence **θ ∈ S ⟹ θ ≤ 90°.** (This is
`dyadic-scaffold`'s Step 2, re-verified independently; reused here as a certified fact,
not re-derived from scratch beyond restating the one-line argument for
self-containedness.)

### 2. Exhaustive classification of single-move forcing primitives

Fix target θ ≤ 90° and a current triangle {p,q,r} (θ not already present). We ask: for
which x1 does θ end up in A, in B, or in both, as a function of x1? A's entries are
{q, x1, r+p−x1}; B's are {r, p−x1, q+x1}. Excluding the trivial cases q=θ or r=θ (θ would
already be present, contradicting "otherwise"), θ can appear in A only via x1=θ or
x1=r+p−θ (each valid iff it lies in (0,p)), and in B only via x1=p−θ or x1=θ−q (each
valid iff it lies in (0,p)).

**Double hit** (θ in both A and B for the same x1): solve the four pairings of
{θ, r+p−θ} = {p−θ, θ−q}:
- θ = p−θ ⟺ **p = 2θ**, x1 = θ. (*Bisection double-hit.*)
- θ = θ−q ⟺ q = 0: invalid (degenerate).
- r+p−θ = p−θ ⟺ r = 0: invalid (degenerate).
- r+p−θ = θ−q ⟺ r+p+q = 2θ ⟺ 180 = 2θ ⟺ **θ = 90°**, x1 = r+p−90 (equivalently 90−q).
  Valid (x1∈(0,p)) iff 0<r+p−90<p iff q<90 and r<90, i.e. the two angles *other than the
  cut vertex* are both acute — always achievable for at least one vertex of any triangle,
  since at most one angle can be ≥90° (cut from that vertex if it exists, else from any
  vertex). This is exactly the "foot of the altitude from the obtuse/any vertex" move.

No other pairing gives a valid double hit. So **the only single-move instant-win forcing
moves are**: (i) bisecting an angle equal to 2θ, and (ii) — only when θ=90° — cutting at
the foot of the altitude from a vertex whose other two angles are acute.

**Single-side forcing** (θ in exactly one of A, B, forcing Shan-Yu into the other,
non-trivial i.e. B or A does not identically already contain θ via q or r):
- x1 = θ (needs p>θ): A = {q, θ, r+p−θ} contains θ; Shan-Yu is forced into
  **B = {r, p−θ, q+θ}**. Call this the **shift move**: it requires only p>θ, and its
  output is p−θ (the cut angle drops by exactly θ) and q+θ (Mulan's chosen "receiver"
  gains exactly θ); r is untouched. By symmetry (using x1=p−θ instead) Mulan may equally
  force **A = {q, p−θ, r+θ}**, i.e. she freely chooses *which* of the two non-cut angles
  is the receiver.
- x1 = r+p−θ (needs θ−p<r<θ, i.e. spectator r<θ and p>θ): A={q, r+p−θ, θ} contains θ;
  Shan-Yu is forced into **B = {r, θ−r, q+r+p−θ}**. Using q+r+p=180 this simplifies to
  **B = {r, θ−r, 180−θ}** — independent of q entirely. Call this the **transfer move**
  (re-verified: sympy substitution of q=180−p−r into the raw output gives exactly
  `[r, θ−r, 180−θ]`). By the symmetric choice x1=θ−q (needs spectator q<θ, p>θ), Mulan
  may instead force **A = {q, θ−q, 180−θ}**, i.e. either non-cut angle may serve as the
  surviving "spectator."

These four families (double-hit bisection, double-hit altitude-for-90°, shift, transfer)
are the complete list of x1-values that make θ appear in at least one child; any other
x1 makes θ appear in neither A nor B, and Shan-Yu is then completely free to choose
either child (this is a genuine, if unavoidable, restriction of this classification's
reach on genuinely non-forcing moves — see the Necessity gap below).

### 3. Bisection is immune regardless of forcing

Setting x1 = p/2 in *any* triangle gives A = {q, p/2, r+p/2}, B = {r, p/2, q+p/2}: both
children contain p/2, so whichever Shan-Yu keeps, p/2 is present. This is not one of the
"forcing" families above (it need not involve θ at all) but is used as a building block:
it lets Mulan drive any chosen angle a down to a/2ⁿ for any n, and — as shown next — the
*other* surviving angle never shrinks below its pre-bisection value.

**Persistence lemma.** If Mulan bisects an angle s of the current triangle whose other
two angles are X and Y, then in *either* child, at least one angle is ≥ max(X,Y).
Proof: the children are {Y, s/2, X+s/2} and {X, s/2, Y+s/2}. In the first, the third
entry X+s/2 ≥ X. In the second, the first entry is X itself. So max(X,Y) is preserved
or increased. ∎ (Immediate induction: if X ≥ some bound b>θ before a bisection of a
*different* angle s, then after the bisection, some present angle is still ≥ b.)

### 4. Sufficiency: θ = 180°/n is forceable for every integer n ≥ 2

**Case n=2 (θ=90°).** From *any* starting triangle, at most one angle is ≥90°; cut from
a vertex whose other two angles are both <90° (such a vertex always exists — the
non-obtuse-of-the-remaining-two vertex, or any vertex if the triangle is non-obtuse) at
its altitude foot (Section 2, double-hit case θ=90°). Both children contain 90°
regardless of Shan-Yu's choice: forced win in exactly one move, from any start.

**Case n≥3 (θ=180/n ≤60°).** We give an explicit, finite, fully Shan-Yu-immune move
sequence from *any* Shan-Yu starting triangle.

*Step A — locate a big angle "for free."* Any triangle's largest angle is ≥60° (else
all three angles < 60° and their sum < 180°, contradiction). Since θ=180/n≤60°, this
largest angle p₀ satisfies p₀ ≥ 60° ≥ θ. If p₀ = θ exactly the game is already won (only
possible when θ=60°, n=3, i.e. the triangle is equilateral — an immediate win with zero
moves). Otherwise p₀ > θ strictly.

*Step B — manufacture a spectator, immune to Shan-Yu, while a big angle survives.*
Fix any *other* angle s₀ of the starting triangle (s₀ ≠ p₀; if the starting triangle is
equilateral with θ<60°=n≥4, this is impossible for the max-uniqueness reasoning above,
so just pick s₀ to be any one of the two non-maximal angles, or, in the fully symmetric
equilateral case, any angle other than the one designated p₀). Repeatedly bisect the
current descendant of s₀: s₀, s₀/2, s₀/4, …, s₀/2ᵏ, for k = ⌈log₂(s₀/θ)⌉+1, so that
s₀/2ᵏ < θ. By the bisection immunity (Section 3) this descendant is present after every
step regardless of Shan-Yu's choices, and by the Persistence Lemma (Section 3) some
angle ≥ p₀ ≥ 60° > θ is also present after every step (each bisection targets the
s₀-lineage, a *different* vertex from whichever vertex currently holds the surviving
big angle, so the Persistence Lemma applies at each step). After k bisections, Mulan has
forced (immune to all of Shan-Yu's k choices) a state with a spectator r := s₀/2ᵏ < θ and
a "big" angle P ≥ p₀ > θ simultaneously present.

*Step C — one transfer move.* Apply the transfer move (Section 2) with p=P>θ and
spectator r<θ: Shan-Yu is forced (else he loses immediately) into
**B = {r, θ−r, 180−θ}** exactly — independent of every other detail of the triangle.

*Step D — walk 180−θ down to θ by n−2 shift moves.* Starting from c₀ := 180−θ (with the
other two angles fixed as r and θ−r), repeatedly apply the shift move (Section 2) to the
current c-value, always designating "r" as the receiver (so θ−r is left untouched
throughout): after the i-th shift, the state is
  {r + iθ, θ−r, 180−θ−iθ} = {r+iθ, θ−r, 180−(i+1)θ}.
Each shift is valid provided the *pre-shift* c-value exceeds θ: we need
180−iθ > θ ⟺ i < n−1, i.e. valid for i = 1,…,n−2 (using θ=180/n). Performing exactly
m = n−2 shifts (i running 1,…,n−2, i.e. the k-th shift takes the state from
180−(k−1)θ… — indexing directly: after m shifts the third entry is 180−(m+1)θ) gives
final third entry 180 − (n−2+1)θ = 180 − (n−1)θ = 180 − 180(n−1)/n = 180/n = θ. Every
intermediate value used, 180−iθ for i=0,…,n−2, satisfies 180−iθ ≥ 180−(n−2)θ =
θ+180/n·... concretely 180−iθ > θ for all i ≤ n−2 as shown, so **every one of the n−2
shifts is valid**, and the final state contains θ exactly. (For n=3, m=1: a single
shift from {r,θ−r,120} to {r+60,θ−r,60} — exact match with the case θ=60°, previously
known.)

**Verified exact-fraction witness for θ=180/7 (n=7), resolving the outline's
discriminating test.** Start from the equilateral triangle {60,60,60} (a legitimate,
concrete Shan-Yu choice; the general argument above covers every other choice
identically). Bisecting one vertex gives (by the equilateral symmetry, both children
coincide) T₁={30,60,90}. Bisecting the 30°-angle gives, in either of Shan-Yu's two
choices, a spectator 15°<180/7 present alongside a big angle (105° or 90°/75° depending
on branch). Applying the transfer move (Section 2, Step C above) with spectator r=15
collapses **either** branch to the identical state
  T₂ = {15, 180/7 − 15, 180 − 180/7} = {15, 75/7, 1080/7}
(sum: 15+75/7+1080/7 = 105/7+75/7+1080/7 = 1260/7 = 180, ✓). Now perform 5 = n−2 shift
moves on the 1080/7-lineage, always receiving into the "15" slot:
```
c₀ = 1080/7                                     {15,        75/7, 1080/7}
c₁ = 1080/7 − 180/7 = 900/7,  receiver→15+180/7  {285/7,     75/7,  900/7}
c₂ = 900/7  − 180/7 = 720/7,  receiver→285/7+180/7 {465/7,   75/7,  720/7}
c₃ = 720/7  − 180/7 = 540/7,  receiver→465/7+180/7 {645/7,   75/7,  540/7}
c₄ = 540/7  − 180/7 = 360/7,  receiver→645/7+180/7 {825/7,   75/7,  360/7}
c₅ = 360/7  − 180/7 = 180/7,  receiver→825/7+180/7 {1005/7,  75/7,  180/7}
```
Each row sums to 1260/7=180 exactly (checked in this round with sympy `Rational`
arithmetic; c₅ = 180/7 = θ exactly, and every intermediate cᵢ (1080/7, 900/7, 720/7,
540/7, 360/7) exceeds θ=180/7, so every shift was valid). The final triangle
{1005/7°, 75/7°, 180/7°} contains θ = 180/7° exactly, after a total of 2 bisections + 1
transfer + 5 shifts = 8 fully Shan-Yu-immune moves. **This settles the outline's fork:
the 180/7° witness is genuine** (case (a) in the outline's fork — not a search artifact —
confirmed by an independent, hand-derivable, exact-fraction construction, not by
re-trusting the prior computational search), via a mechanism (the shift move) that
`dyadic-scaffold`'s construction did not use.

**Conclusion of Section 4:** S ⊇ {180°/n : n ∈ ℤ, n ≥ 2}. This strictly contains
`dyadic-scaffold`'s family {180°/((2^k+1)2^j)} (e.g. n=4,6,7,8,9,… are new: 45°=180/4 was
already dyadic, but 180/7° is new, and in general 180/n is dyadic exactly when n's odd
part is of the form 2^k+1 — so most n give genuinely new θ). Closure under θ↦θ/2 (proved
generally: if θ is forceable, reach it, then bisect once more — immune — to force θ/2)
maps 180/n to 180/(2n), already inside the same family, so this closure adds nothing new
— the family {180/n : n≥2} is already closed under halving.

### 5. Necessity: is S exactly {180°/n : n≥2}? (open gap, honestly stated)

**Conjecture:** S = {180°/n : n ∈ ℤ, n ≥ 2}.

Section 2 shows that the *only* single-move mechanisms that let Mulan force Shan-Yu's
hand (make progress he cannot block) are: double-hit bisection (needs an angle exactly
2θ present), the θ=90° altitude double-hit, the shift move (needs an angle >θ present,
no other condition), and the transfer move (needs a spectator <θ and a partner >θ). Any
*other* x1-value gives Shan-Yu a completely free choice between two triangles neither of
which contains θ. Restricting to strategies built purely from the four named primitives
(never taking a "free-choice" cut that doesn't force θ into at least one branch), the
reachable target set is generated exactly as in Section 4: transfer always "resets" to
the canonical family {r,θ−r,180−θ} independently of everything except θ and the chosen
spectator r (this erasure of q, and re-application within the canonical family, is a
genuine fixed point unless a shift is applied — verified: applying transfer again inside
{r,θ−r,180−θ} using 180−θ as the "big" angle and either r or θ−r as spectator reproduces
{r,θ−r,180−θ} exactly, since transfer's output third entry is 180−θ_target regardless of
which "big" angle was used); and shift only ever moves the canonical family's third
entry down through 180−θ, 180−2θ, 180−3θ, …, hitting θ exactly iff 180=(n)θ for an
integer n. So **within the primitive toolkit of Section 2, no θ outside {180/n} is
reachable** — this is a real (if informal) argument that the four primitives cannot
produce anything beyond the conjectured family.

**The remaining, unclosed gap** is ruling out genuinely adaptive strategies that use
"free-choice" cuts (x1 not forcing θ into either branch) as an intermediate step, relying
on a case split over Shan-Yu's free choice, each branch separately winnable by a
*different* follow-up strategy. Section 2's classification says such a cut cannot force
θ into either child *directly*, but it does not rule out that both possible children
could independently be winnable states for Mulan via different (possibly primitive-based)
continuations — a priori this could enlarge S beyond {180/n}.

A natural (but not fully rigorous) argument against this: pick Shan-Yu's initial two free
angles p₀, q₀ to be algebraically independent transcendentals over ℚ(θ) (e.g.
p₀=θ+π/1000, q₀=θ+e/1000 scaled to keep the triangle valid — any two "generic" reals
work). Every angle appearing after a sequence of moves is computed by an explicit field
formula in the previously-present angles and θ (this holds for the four named
primitives, whose outputs are visibly ℚ(θ)-affine-linear in the current angles), so
every angle ever present lies in the field K = ℚ(θ)(p₀,q₀), and — restricting to
primitive moves — the primitives' effect on which "p₀,q₀-degree" survives is controlled:
Section 4's construction shows the ONLY way to make an angle *independent of p₀,q₀*
(i.e., a pure ℚ(θ)-expression) is via a transfer move (which erases q, the leftover
"junk" angle, but leaves the spectator r itself still p₀,q₀-dependent in general); shift
moves preserve the "clean" (p₀,q₀-independent) status of whichever angle they are applied
to. Hence the *only* angle that ever becomes a pure ℚ(θ)-expression equal to θ itself
must come from a chain of shifts applied to the transfer's clean output 180−θ, which (as
computed) can only equal θ when 180/θ ∈ ℤ. This suggests any p₀,q₀-*dependent* branch of
the game (i.e., the spectator r, or any angle whose formula still involves p₀ or q₀
nontrivially) can never equal the *fixed, known* constant θ exactly, because a nonzero
p₀,q₀-linear (or, if free-choice cuts are allowed, a nonzero p₀,q₀-*rational function*)
combination cannot coincide with a specific algebraic value of θ for algebraically
independent transcendental p₀,q₀ — UNLESS its p₀,q₀-coefficients happen to be forced to 0
by the game dynamics, which is exactly what "clean" (transfer/shift-only) play achieves
and what free-choice cuts are not shown to preserve or avoid.

**What is missing to close this into a full proof:** a rigorous demonstration that (i)
Mulan gains nothing by ever choosing a "free-choice" x1 (one not in the four named
families) — equivalently, that WLOG an optimal Mulan strategy uses only primitive moves —
or (ii) a direct field/valuation-theoretic invariant (e.g. a well-defined "transcendence
degree over ℚ(θ) of the angle-difference from θ" that is provably non-decreasing, or
strictly positive and non-vanishing, under *every* legal cut, not just the four
primitives) showing Shan-Yu can always maintain "no present angle equals θ" by an
explicit pairing/potential argument valid against arbitrary x1. Neither (i) nor (ii) is
established here; this is the honest open gap. `corrected-genericity-bound` is attacking
a version of this necessity question independently and should be cross-checked against
the *exact* conjectured family derived here (not the smaller `dyadic-scaffold` family) —　
if its invariant is calibrated only against dyadic-scaffold's witnesses it will be too
weak (it must NOT rule out 180/7°, 180/4°, 180/9°, etc., all newly proved forceable here).

### Key lemmas (claim + mechanism) — new in this round

- **Exhaustive single-move forcing classification (Section 2):** the only x1-values that
  place θ in some child are x1 ∈ {θ, r+p−θ} (hits A) and x1 ∈ {p−θ, θ−q} (hits B); their
  four pairwise coincidences give exactly bisection-double-hit (p=2θ) and
  altitude-double-hit (θ=90°) as the double-hit cases, with the two singleton conditions
  (p>θ alone; p>θ and a spectator <θ) giving the shift and transfer moves respectively —
  proved by direct case-exhaustion of the linear system, not asserted.
- **Shift move:** {p,q,r}, p>θ ⟹ Mulan can force {p−θ, q+θ, r} (or, symmetrically,
  {p−θ, q, r+θ}), in one move, Shan-Yu having no escape — because x1=θ places θ literally
  in A, forcing Shan-Yu into B, and B's formula p−x1=p−θ, q+x1=q+θ is immediate
  substitution (verified with sympy).
- **Persistence lemma (Section 3):** bisecting an angle s of a triangle with other angles
  X,Y forces some present angle ≥ max(X,Y) into the surviving child regardless of choice —
  because the two children are {Y,s/2,X+s/2} and {X,s/2,Y+s/2}, and X (resp. Y) survives
  literally unchanged in the second (resp. first).
- **Sufficiency for θ=180°/n, all integers n≥2 (Section 4):** full explicit construction
  (pigeonhole for a free big angle, spectator manufacture via Persistence + bisection
  immunity, one transfer, n−2 shifts) — every step's validity checked algebraically, and
  the n=7 case additionally hand-verified with exact `sympy.Rational` arithmetic through
  a complete concrete move sequence from an explicit starting triangle.

### Open gaps

- Necessity (Section 5): S ⊆ {180/n : n≥2} is **not proved**. The obstruction is ruling
  out non-primitive ("free-choice") cuts as part of a genuinely adaptive, branching
  Mulan strategy. A transcendence-based heuristic is given but not made rigorous.
- The case θ irrational (θ/180 irrational): the constructive family only ever produces
  rational-multiple-of-180 angles (every primitive's output is a ℚ(θ)-affine combination
  of existing rational-in-θ,180 quantities, and hits exactly θ only via the integer
  relation 180=nθ), so **if the conjecture is correct, all irrational θ ≤ 90° are NOT
  forceable** — this claim inherits the same unproved necessity gap, not a separate one.

## Approaches tried
- Round 2: abandoned the purely abstract two-generator monoid {x/2, 180−x} sketched in
  round 2's outline (it does not model the real game: it omits the shift move entirely,
  which is why it wrongly appeared to exclude 180/7°). Replaced it with a **complete,
  exhaustive classification of the real cut formula's forcing primitives** (Section 2),
  discovered a fourth primitive (the *shift* move, x1=θ) beyond bisection and the
  previously-known transfer, and used it to prove a strictly larger constructive family
  S ⊇ {180°/n : n≥2} than `dyadic-scaffold`'s {180°/((2^k+1)2^j)}. Directly, rigorously,
  hand-verified (exact fractions, explicit move sequence) that 180°/7 is genuinely
  forceable — resolving the outline's discriminating test in favor of case (a)/(b) fused:
  the witness is real, and the "third generator" needed is the shift move, found and
  proved from the geometry itself (not guessed abstractly). Necessity remains open.

## Current best
**Proved:** θ ∈ S ⟹ θ ≤ 90° (imported/reverified). **Proved:** θ = 180°/n is forceable,
via an explicit finite Shan-Yu-immune construction, for every integer n ≥ 2 — this
strictly extends `dyadic-scaffold`'s family and rigorously confirms 180°/7° is forceable
(explicit 8-move witness in exact fractions given in Section 4). **Open:** whether S
equals {180°/n : n≥2} exactly (necessity gap, Section 5) — the candidate closed form for
S is now precisely stated and matches every known witness, but the upper bound is not
proved.

## Promotable lemmas

- **Cut identity (★)** — (r+p−x1)+(q+x1) = p+q+r = 180°, for a cevian cut from vertex p
  with parameter x1. Already shared with `dyadic-scaffold`; re-verified here.
- **Exhaustive forcing classification** — for a triangle {p,q,r} and target θ not already
  present, the only cevian cuts (values of x1) that place θ in at least one child are the
  four listed in Section 2, giving exactly two double-hit families (bisection at p=2θ;
  altitude foot at θ=90°) and two single-hit "forced transition" families (shift: any
  p>θ; transfer: p>θ with a spectator <θ). Proved in full in Section 2 by exhausting the
  linear system of coincidences among {θ, r+p−θ} (hits for A) and {p−θ, θ−q} (hits for
  B). Reusable by any approach analyzing this game's move structure.
- **Shift move** — from {p,q,r} with p>θ, Mulan forces {p−θ, q+θ, r} (receiver q of her
  choice) in one Shan-Yu-immune move. Proved in Section 2, re-verified with sympy.
- **Persistence lemma** — bisecting angle s of a triangle with other angles X,Y always
  leaves some present angle ≥ max(X,Y), regardless of Shan-Yu's choice. Proved in
  Section 3.
- **θ=180°/n forceable for every integer n≥2** — full explicit construction, Section 4,
  including a fully hand-verified exact-fraction 8-move witness for n=7 (θ=180/7°) from
  the equilateral start.
