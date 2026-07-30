## imo-2026-04 (top-down characterization lens)

**Bottom line / best guess:** θ ∈ {90°/2^k : k = 0,1,2,…} = {90°, 45°, 22.5°, 11.25°, …}
is the true and complete answer. I independently re-derived this (matching sibling
report's H2), but I also found a genuinely new **necessity argument** (a
genericity/transcendence + countability argument) that goes well beyond the sibling's
open question and, I believe, closes gap H1 vs H2 in favor of H2. This is still not a
fully complete rigorous writeup (see Gaps below), but it is much stronger than
small-case evidence — treat it as a near-complete proof sketch for the outliner to
formalize, not a mere conjecture.

### The new necessity argument (this is the main new content of this report)

**Setup.** Track a current triangle's angles as affine expressions in Shan-Yu's two
free initial parameters (p0,q0) (r0 = 180−p0−q0). Every cevian cut produces two
children whose angle-triples are again affine (integer-coefficient) expressions in
(p0,q0) and in Mulan's chosen split parameter t — this is exactly the identity (*)
mechanics the sibling report set up.

**Key local lemma (verified in sympy, see Method below).** Suppose the current
triangle has one angle pinned to a KNOWN CONSTANT c (i.e. an expression not
involving the "free" parameter y) and the other two angles are (y, 180−c−y) for a
still-generic affine y. Then, over **all three choices of which vertex to cut**, and
**all algebraic ways to solve "θ appears in both children" (2 equations, 1 unknown
t, requiring the resulting condition to hold as an IDENTITY in y — i.e. for every
value y could possibly take, not a coincidence for one specific y)**, the only
solutions are:
  - θ = c/2  (bisect the known angle — the sibling's lemma 1)
  - θ = 90°  (the universal altitude trick, independent of c — the sibling's lemma 2b)
  - θ = c    (trivial, already present)

I verified this exhaustively with sympy (script below) for a symbolic constant `c`
and symbolic generic `y`, across all 3 cut-vertex choices and all 3×3 entry pairings
— **no other θ formula ever appears.** Moreover, whichever of {c/2, 90} is chosen,
the resulting child triangle is again of the exact same shape (one new pinned
constant, plus two entries that are still literally ±y + const, i.e. still
non-constant affine in y — "generic" is preserved). So the lemma re-applies at every
depth: **the set of constants Mulan can ever force this way is exactly the closure
of {90} under c ↦ c/2, i.e. {90/2^k : k ≥ 0}.**

**Why "identity in y" is the right requirement, not just "true for the actual y".**
This is the subtlety I had to resolve (my own initial approach was too hasty here).
Shan-Yu picks the ENTIRE initial triangle (p0,q0) before play begins, adversarially,
knowing θ and knowing Mulan's full strategy (a — possibly infinite-depth-in-principle
— binary decision tree, branching on Shan-Yu's A/B choice at each node). At any
single node, a "double-hit" condition that is not an identity in y is merely a
polynomial equation in (p0,q0); it fails for all but finitely many "bad" values.
Since Mulan's full strategy tree is a binary tree, it has only **countably many
nodes**, hence only **countably many "bad" polynomial conditions** across the whole
strategy (one finite set of bad conditions per node — non-identity coincidences that
would let θ sneak in by luck rather than by forced identity). A countable union of
proper algebraic subvarieties of the 2-dimensional parameter region {(p0,q0):
0<p0,q0,p0+q0<180} cannot cover it (uncountability / Baire category), so **Shan-Yu
can choose (p0,q0) avoiding every single one of these countably many bad
conditions simultaneously.** Against such a choice, θ can appear in the triangle
at any node of Mulan's tree **only if it is one of the identity-forced values** —
and by the local lemma above, the closure of identity-forced values is exactly
{90/2^k}. Hence if θ ∉ {90/2^k}, θ never appears against this Shan-Yu choice, so no
finite (or even infinite, since it never appears at any node) strategy of Mulan's
succeeds — **Mulan cannot force θ.**

This argument subsumes and generalizes the sibling's "non-obtuse invariant" for
θ>90° (that's really the θ=90/2^k-only-below-90 fact together with the countable-
genericity idea applied to a slightly different invariant) but is derived
completely independently via a top-down "what values are ever hittable-by-forcing"
approach rather than a monotone invariant.

### Method (verification, not scratch code — I ran this to check the claim)

I used `sympy` to symbolically compute, for a triangle (c, y, 180−c−y) with `c`
symbolic-constant and `y` symbolic-generic, and for each of the 3 possible
cut-vertices, the two children's angle-triples, then for each of the 3×3 pairs of
entries (one from each child) solved "entry_A(t) = θ" for t, substituted into
entry_B(t) = θ, and required the resulting equation to vanish **identically in y**
(all polynomial coefficients in y zero) — solving the resulting system for θ in
terms of c. Every one of the 3 configurations × 9 entry-pairs yields only
θ ∈ {c/2, 90, c}. (Full output reproduced: config "cut at c-vertex" → θ=c/2 or
θ=90; "cut at y-vertex" (both side-orderings) → θ=90 or θ=c (trivial).) This is a
mechanical/exhaustive check, not a proof by itself, but it is strong computational
evidence that the local lemma is exactly right (no missed case), since the case
space (3 vertices × 3×3 entries = 27 sub-cases) was covered completely by the
symbolic solve.

### Distinct openings for the outliner

1. **The bisection+altitude chain construction** (already in sibling report) — proves
   sufficiency for θ = 90/2^k. Keep as-is.
2. **NEW: genericity/countability necessity argument** (this report) — aims to prove
   necessity for ALL θ ∉ {90/2^k}, not just θ>90°. This is a genuinely different
   top-level target from the sibling's "non-obtuse invariant" (which only rules out
   θ>90°): it's a transcendence-degree / countable-bad-set argument that, if
   formalized, closes the whole problem in one stroke (covers θ>90° as a special
   case too — for θ>90°, it's even easier: 90 is the max identity-forceable value
   less than or equal to it in the {90/2^k} chain, and 90<θ trivially unreachable).
3. **Reduction to a cleaner invariant for write-up**: instead of the raw
   countability/Baire argument (correct but perhaps non-elementary for a contest
   writeup), consider recasting as: "choose p0, q0 algebraically independent over
   Q(θ)" (transcendence basis argument) — this is the standard olympiac-friendly way
   to phrase "avoid a countable union of proper subvarieties," and only requires the
   existence of two reals algebraically independent over Q(θ) forming a valid
   triangle, which is elementary (cardinality of algebraic numbers is countable, so
   generic reals work).

### Candidate technique(s)
- Transcendence-degree / algebraic-independence argument (this is the technique to
  cite for necessity) — I did not find this named explicitly in knowledge_base.md;
  it is closest in spirit to "Constructive vs. existence" and general
  "Invariant/monovariant" entries but is really its own technique (an "adversary
  genericity" argument). The outliner should state it from scratch, citing
  transcendence/algebraic-independence of reals over Q as the underlying fact
  (standard, doesn't need a KB citation beyond stating it).
- Induction on the "one pinned constant, rest generic" triangle shape, driven by the
  exhaustive local lemma above.

### Cheap-kill candidates
- The local lemma computation above is itself a cheap, fully mechanical kill of any
  hope for "extra" forceable θ beyond 90/2^k — recommend the outliner treat this as
  settled (do not re-search for exotic double-hits; the symbolic sweep was
  exhaustive over vertex choice and entry pairing).
- Sanity check: at c=90/2^k for large k, c/2 keeps halving toward 0 but never
  produces any θ outside the {90/2^k} lattice — no accumulation-point subtlety since
  the problem only asks about a single fixed θ>0, and any given θ either is exactly
  90/2^k for some finite k or is not.

### Knowledge-base entries to use
- No entry in knowledge_base.md directly names "genericity/transcendence adversary
  argument" — flag this as a technique the outliner must develop from first
  principles (cite: algebraic numbers are countable, hence a "generic" choice of two
  reals is algebraically independent over any fixed countable field — elementary
  fact, doesn't need external citation beyond stating it clearly).
- "Invariant/monovariant" (General Proof Methods) — still applicable to the θ>90°
  sub-case via the sibling's cleaner "non-obtuse" invariant, which is a good
  elementary special case to keep in the writeup even if the general genericity
  argument subsumes it (it's a much simpler self-contained argument for that one
  case and a good warm-up/base case).
- "Constructive vs. existence" — for the sufficiency chain (90/2^k construction).

### Analogous past problems (cruxes)
No new search performed beyond sibling's (already reported: no true crux match in
the corpus; geometry cruxes don't exist in the corpus per crux_moves_documentation.md
limitations, and this is a geometry/game hybrid). Defer to sibling report's finding:
`aimo-0236`, `aimo-0521` are loosely analogous (invariant-based games) but not true
matches.

### Prior progress
Sibling's report (`/tmp/round-2/math-explorer-angle-invariant.md`) already
established: sufficiency for θ=90/2^k (full construction), impossibility for θ>90°
(non-obtuse invariant), and left θ≤90°, θ∉{90/2^k} (e.g. θ=60°) as the open
question. This report's contribution: a candidate general necessity argument
(genericity/countability) that, if it holds up under formalization, resolves that
open question in favor of "only θ=90/2^k works" — i.e. **θ=60° should be
IMPOSSIBLE for Mulan**, contrary to the "clean interval (0,90]" hypothesis H1.

### Dead ends (do not retry)
- Don't bother searching for a single-move double-hit target value other than
  {c/2, 90, c} from a "one pinned constant + one generic" state — exhaustively ruled
  out by the sympy sweep in this report.
- Don't try to defend H1 (all θ≤90° work) via an oblivious/non-adaptive multi-step
  scheme that doesn't rely on new identities — any such scheme reduces to the same
  local lemma at each step and is covered by the impossibility argument.
- (Repeating sibling's note) Don't try to use "Mulan sees the actual numbers so she
  can always solve for t exactly" as a defense of extra power — that's true LOCALLY
  (any one branch), but the genericity argument shows it can't be leveraged into a
  double-hit that avoids the identity requirement, because Shan-Yu picks the
  triangle first and can dodge any finite (or countable) list of non-identity
  coincidence conditions.

### Small-case / intuition notes
- θ=60°: my argument suggests (conjecturally, pending full formalization) that
  Mulan CANNOT force θ=60° — Shan-Yu picks an initial triangle with p0,q0
  algebraically independent over Q, and 60 is never among the identity-forced
  values {90,45,22.5,...}, and by the countability argument no coincidence can
  bail Mulan out. This directly contradicts the naive "θ≤90° all work" guess (H1);
  I recommend the outliner adopt **H2 as the target answer**: θ ∈ {90°/2^k : k≥0}.
- The construction direction (sufficiency) is solid (sibling's proof). The main
  remaining work for a `solved` status is formalizing the necessity direction
  cleanly — I'd suggest structuring it as: (1) elementary non-obtuse invariant for
  θ>90° (simple, self-contained, already done by sibling); (2) for 0<θ≤90°,
  θ≠90/2^k, use the algebraic-independence argument in this report, with the local
  lemma's exhaustive case-check written out by hand (not code) as a finite,
  checkable-by-a-human case analysis (27 sub-cases, but really only 3 essentially
  distinct configurations by symmetry — cut-at-pinned-vertex vs cut-at-generic-
  vertex, the two generic-vertex orderings being symmetric).
