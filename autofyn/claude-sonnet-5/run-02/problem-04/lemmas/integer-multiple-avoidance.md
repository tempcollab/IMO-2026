# Lemma: Integer-Multiple-Avoidance Invariant (Cleanliness Lemma)

**Setup.** Fix θ ∈ (0°,180°), set T := 180°/θ. For an angle value a occurring in the
game, write u := a/θ ("θ-units"). Any triangle's three current values u_p, u_q, u_r
satisfy u_p + u_q + u_r = T at every point of the game. Call such a triangle *clean* if
none of u_p, u_q, u_r is an integer.

**Statement.** Suppose T ∉ ℤ. If the current triangle is clean, then for every legal
cut (cut vertex p, split value y1 ∈ (0, u_p), giving children
A = {u_q, y1, u_r+u_p−y1}, B = {u_r, u_p−y1, u_q+y1} per `cut-formula.md`), at least
one of A, B is again clean.

**Proof.** u_q (inherited by A) and u_r (inherited by B) are non-integers by
hypothesis, so:
- A unclean ⟺ y1 ∈ ℤ or u_p+u_r−y1 ∈ ℤ;
- B unclean ⟺ u_p−y1 ∈ ℤ or u_q+y1 ∈ ℤ.

Both unclean requires one of 4 simultaneous conjunctions (exhaustive by distributing
the two ORs):

1. y1 ∈ ℤ and u_p−y1 ∈ ℤ ⟹ u_p = (u_p−y1)+y1 ∈ ℤ. Contradicts u_p ∉ ℤ.
2. y1 ∈ ℤ and u_q+y1 ∈ ℤ ⟹ u_q = (u_q+y1)−y1 ∈ ℤ. Contradicts u_q ∉ ℤ.
3. u_p+u_r−y1 ∈ ℤ and u_p−y1 ∈ ℤ ⟹ subtracting, u_r ∈ ℤ. Contradicts u_r ∉ ℤ.
4. u_p+u_r−y1 ∈ ℤ (= m1) and u_q+y1 ∈ ℤ (= m2) ⟹ adding,
   u_p+u_q+u_r = m1+m2 ∈ ℤ, i.e. T ∈ ℤ. Contradicts the hypothesis T ∉ ℤ.

All four cases are impossible, so no single real y1 can make both A and B unclean;
hence at least one is clean. ∎

**Verification.** Independently re-derived and computer-checked by the proof-reviewer
(round 5): (a) a targeted exact-`Fraction` search enumerating every actual integer-
crossing value of y1 ∈ (0,u_p) for ~17500 random clean triples with non-integer
rational T found zero double-unclean events; (b) the same search re-run with T forced
to be an *integer* (all else unchanged) found ~79000/15706 double-unclean events,
confirming the T∉ℤ hypothesis is load-bearing (case 4 only) and not vacuous.

**Use.** Combined with the equilateral start (clean whenever T∉ℤ, since T/3∈ℤ would
force T∈ℤ) and induction, shows: if T=180°/θ ∉ ℤ, Shan-Yu can keep the triangle clean
forever, so θ is never hit and θ ∉ S. See `results/imo-2026-04/current.md` for the
full necessity argument and the combined characterization S = {180°/n : n ≥ 2}.

**Source.** `denominator-valuation-necessity.md` (round 4 build), certified by
proof-reviewer round 5.
