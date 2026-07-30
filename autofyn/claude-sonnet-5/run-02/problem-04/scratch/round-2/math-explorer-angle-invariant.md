## imo-2026-04

### Setup / notation established
Triangle T has angles (p,q,r), p+q+r=180°. A legal Mulan move: pick a vertex, say
the one with angle p (call it P), pick a point X on the OPPOSITE side (the side
joining the other two vertices Q,R, X strictly between them), cut PX. This splits
angle p into p1+p2=p (p1=∠QPX, p2=∠RPX, p1 ranges continuously and freely over the
whole open interval (0,p) as X ranges over the open segment QR — Mulan has full
real-number control over p1). The two children are:
  Option A ("keep Q side"): angles {q, p1, r+p-p1}
  Option B ("keep R side"): angles {r, p-p1, q+p1}
(new angle at X in A is 180-q-p1 = r+p-p1; in B it is 180-r-(p-p1)=q+p1; these two
new angles are supplementary and, more importantly, satisfy
  (r+p-p1) + (q+p1) = p+q+r = 180°           …(*)
exactly — this identity is the single most useful fact found.)
Shan-Yu then keeps A or B (his choice, made after seeing Mulan's p1).

### Distinct openings (rigorously verified, not just conjectured)

1. **Bisection lemma (state-independent, always works).** If Mulan sets p1=p2=p/2
   (bisect ANY current angle p), then BOTH Option A = (q, p/2, r+p/2) and Option B =
   (r, p/2, q+p/2) contain the angle p/2 explicitly. So Shan-Yu cannot avoid: after
   bisecting angle p, the surviving triangle is GUARANTEED to have an angle p/2,
   whichever child he keeps. (Direct algebra: this is the unique case "p1=θ" and
   "p−p1=θ" solved simultaneously, forcing p=2θ.)

2. **Full classification of 1-move "double hits."** I solved, exhaustively, for which
   target V and which p1 make BOTH Option A and Option B contain angle V (i.e. Mulan
   wins/sets up V unavoidably in one move). There are exactly two mechanisms:
   (a) **Local**: p = 2V (bisect an existing angle equal to 2V) — lemma 1 above,
       depends on the current triangle already having an angle 2V.
   (b) **Global/universal**: V = 90° *only*. Using (*), setting the two new-angle
       expressions equal to 90 simultaneously forces q+r+p = 180 = 2V automatically
       —independent of p,q,r! So **V=90° is forceable in ONE move from ANY current
       triangle** (as long as no angle already =90). No other value V has this
       triangle-independent property (checked all 4 sign combinations of the two
       linear conditions; the only other solutions degenerate to q=0 or r=0).
   Concretely for (b): pick P = the vertex with the LARGEST angle (only one angle
   can be ≥90°, so the other two, Q and R, are automatically <90°); drop the
   altitude from P to QR, foot H lands strictly inside QR (guaranteed since Q,R<90);
   both triangles PHQ and PHR have a right angle at H. This is literally the
   classical "foot of the altitude" fact, re-derived from the cevian-split algebra.

3. **Chained construction: θ = 90°/2^k is forceable for every k=0,1,2,…** Force 90°
   in move 1 (fact 2b, works regardless of the adversarial starting triangle), then
   bisect the guaranteed 90° angle (fact 1) to get 45° guaranteed in move 2
   regardless of Shan-Yu's choice, then bisect the guaranteed 45° to get 22.5° in
   move 3, etc. At every step only the *freshly guaranteed* angle is used (never an
   adversarial "other" angle), so this chain is completely immune to Shan-Yu's
   choices — a fully verified constructive proof that Mulan wins whenever
   θ ∈ {90°, 45°, 22.5°, 11.25°, …} = {90°/2^k : k≥0}.

4. **Impossibility for θ>90° (fully proved, clean invariant).** Claim: if a triangle
   is non-obtuse (all three angles ≤90°), then for *any* cevian cut of it, at least
   one of the two children is again non-obtuse. Proof: split angle p (≤90 given);
   the two "old-side" entries in each child are q,r (≤90 given) and p1,p-p1 (both
   <p≤90). The only entries that can exceed 90 are the two "new" angles
   r+p-p1 (child A) and q+p1 (child B); by identity (*) these sum to exactly
   p+q+r=180°, so at most one of them can exceed 90 — the child whose new angle is
   ≤90 is entirely non-obtuse, and it always exists. Hence Shan-Yu, starting from
   ANY non-obtuse initial triangle (e.g. equilateral, or any acute triangle — his
   choice), can always respond by keeping the non-obtuse child, maintaining "all
   angles ≤90°" forever. If θ>90°, this invariant means angle θ can NEVER appear —
   **Mulan cannot win for any θ>90°.** This is a complete, rigorous proof of
   necessity for the θ≤90° direction (modulo formalizing the initial-triangle choice
   and the induction, which is straightforward).

### Candidate technique(s)
- Direct algebraic tracking of the two children's angle triples (as above) — this
  *is* the real technique; no deep external theorem needed, just careful bookkeeping
  of the affine relations between old and new angles, exploiting the identity (*).
- Invariant/monovariant method (knowledge_base.md "Invariants & monovariants",
  "Invariant/monovariant" under General Proof Methods) — used for the θ>90
  impossibility (the "non-obtuse" invariant) and could plausibly be strengthened to
  rule out non-dyadic acute θ as well (open, see gap below).
- Induction / explicit finite construction (knowledge_base.md "Constructive vs.
  existence", "Induction") for the θ=90°/2^k family.

### Cheap-kill candidates
- The sum identity (*) — (new angle in A) + (new angle in B) = p+q+r = 180° exactly
  — is the single cheapest structural fact and should be the first thing any
  approach states; it immediately kills any attempted double-hit mechanism other
  than V=90° or V=p/2, and immediately proves the θ>90° impossibility.
- Parity/degree count: at most one angle of a triangle can be ≥90° — used to make
  the altitude trick always applicable (choose P = largest-angle vertex).

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics section) and "Invariant / monovariant"
  (General Proof Methods) — for the θ>90° non-obtuse-invariant impossibility proof.
- "Constructive / incremental" and "Constructive vs. existence" — for the θ=90/2^k
  explicit finite construction (need both an upper-bound/impossibility argument for
  the "only" direction and an explicit finite move-sequence for the "if" direction,
  exactly the CLAUDE.md rigor rule for "find all θ").
- "Synthetic toolkit" (Geometry section, altitude/right-angle facts) for the θ=90°
  one-move construction.
- Meta-Strategy: "solve a simpler / special case first" — θ=90 and θ>90 are the
  clean special cases that crack the problem; use them as anchors.

### Analogous past problems (cruxes)
Searched combinatorics/games-and-strategy (39 cruxes) and combinatorics/invariants-
and-monovariants in the corpus (crux_moves_documentation.md field names confirmed:
`technique`, `how_used`, `domain`, `subtopic`). No geometry cruxes exist in the
corpus (documented limitation — "geometry ... no geometry cruxes have been
extracted"), and this problem is a geometry/game hybrid, so nothing is a close
structural match. The closest *methodological* analogues (not close enough to be
true cruxes, but worth the outliner's awareness):
- `aimo-0236` (combinatorics, games-and-strategy): "maintain a two-phase invariant
  (stronger bound before the opponent moves, weaker bound after) that is
  self-restoring" — same flavor as our non-obtuse invariant (an invariant that
  survives one adversarial move because of a summation identity), but for a token
  game, not geometric. Worth a look if the outliner wants to tighten the θ>90 proof
  into the exact "before/after" induction format.
- `aimo-0521` (combinatorics, games-and-strategy): "track the full family of hidden
  states consistent with the information" — loosely analogous to the idea of
  tracking the *set* of angle-triples reachable, but not a real crux match.
No true crux match found; do not force one.

### Prior progress
None — workspace was empty at round start. This report IS the first substantive
progress.

### Dead ends (do not retry)
- Trying to find a *triangle-independent* (works from any starting shape) one-move
  double-hit for any target V ≠ 90°: proven impossible by exhaustive case analysis
  (see opening 2) — do not re-derive this, it's settled.
- Trying to use "genericity"/transcendence of Shan-Yu's chosen angles to block
  Mulan: does NOT work as a defense argument, because Mulan's split parameter p1 is
  a free real number chosen *after* seeing the actual current angles — she can
  always set p1 = θ − (known current angle) exactly, regardless of how "generic"
  that angle is. Any Shan-Yu defense must be a genuine closed invariant (like the
  non-obtuse set), not an appeal to algebraic independence.

### Small-case / intuition notes (labeled conjecture where not proved above)
- θ=90°: **proved** win in exactly 1 move, any starting triangle.
- θ=90°/2^k (k≥0): **proved** win in exactly k+1 moves, any starting triangle,
  fully adversary-immune construction.
- θ>90°: **proved** impossible (non-obtuse invariant, Shan-Yu picks any non-obtuse
  starting triangle and always keeps the non-obtuse child forever).
- θ acute but NOT of the form 90/2^k (e.g. θ=60°, θ=30°, θ=50°): **open / the key
  gap.** Two live hypotheses for the outliner to resolve:
  - **H1 ("θ≤90° all work")**: some more flexible adaptive (multi-branch, not
    immune-to-everything) strategy lets Mulan win for every acute θ too, using
    Shan-Yu's *revealed* angle values reactively (not just the immune bisection
    chain). This would make the final answer the clean interval 0<θ≤90°.
  - **H2 ("only θ=90/2^k")**: Shan-Yu has a (yet unfound) refined invariant, in the
    spirit of the non-obtuse one, that also blocks every acute θ not of that dyadic
    form — e.g. some invariant tied to which reals are reachable via the affine
    "new angle" maps from a well-chosen irrational/generic starting triangle
    (though the "dead end" above shows plain transcendence doesn't work — a
    correct invariant would have to be more structural, e.g. bounding *how many*
    times an exact hit can be engineered before Shan-Yu's residual continuum of
    choices exhausts Mulan's leverage).
  - Suggest the outliner/builder test θ=60° concretely as the deciding case (not
    of the dyadic-90 form, and a natural "nice" angle): try to either construct an
    explicit finite forcing sequence for θ=60°, or find an invariant blocking it.
    Resolving this one case very likely reveals the true general characterization.
