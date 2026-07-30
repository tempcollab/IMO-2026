# Proof review: imo-2026-04 / denominator-valuation-necessity (round 5)

## Verdict: APPROVE
## True Status: solved

## Summary
The proof combines (a) the previously-certified sufficiency lemma
`lemmas/theta-180-over-n-forceable.md` ({180°/n : n≥2} ⊆ S, imported without
re-proof) with (b) this file's new necessity argument (S ⊆ {180°/n : n≥2}) to give
the complete characterization S = {180°/n : n integer ≥ 2}. After an adversarial
line-by-line check of the necessity argument and independent computer verification, I
find the proof correct and complete. `current.md` has been updated to Status `solved`
with the combined Full proof, and the Cleanliness Lemma has been certified into
`lemmas/integer-multiple-avoidance.md`.

## Line-by-line check of the load-bearing step: the Cleanliness Lemma

**Setup check.** T := 180°/θ, u := a/θ for angle a. Angle-sum invariant u_p+u_q+u_r=T
holds at every point of the game — trivially true since actual angles always sum to
180° and θ is fixed. Correct.

**Children formula.** A = {u_q, y1, u_r+u_p−y1}, B = {u_r, u_p−y1, u_q+y1}, for cut
vertex p split into y1 ∈ (0,u_p). This is the θ-unit rescaling of the cevian cut
formula in the already-certified `lemmas/cut-formula.md` (children
{q,x1,r+p−x1},{r,p−x1,q+x1}). Rescaling by 1/θ is a linear operation and preserves the
formula exactly. Correct, and correctly cites the dependency without re-deriving it
(cut-formula.md was certified round 2, and I additionally re-checked that its "x1
ranges over the entire open interval (0,p)" claim is used consistently: y1's legal
range (0,u_p) is exactly this, correctly imported).

**Four-case exhaustiveness.** Since u_q (in A) and u_r (in B) are non-integers by the
cleanliness hypothesis, "A unclean" reduces to "y1∈ℤ or u_p+u_r−y1∈ℤ" and "B unclean"
to "u_p−y1∈ℤ or u_q+y1∈ℤ". "Both unclean" is the disjunction of all 2×2=4
conjunctions — this is a correct, exhaustive distribution of two ORs, nothing missing.

**Case-by-case re-derivation (done independently from scratch, not following the
proof's own mod-1/residue framing, to cross-check):**
1. y1∈ℤ and u_p−y1∈ℤ ⟹ u_p = (u_p−y1)+y1 ∈ ℤ. Contradicts u_p∉ℤ (clean). ✓.
2. y1∈ℤ and u_q+y1∈ℤ ⟹ u_q ∈ ℤ. Contradicts u_q∉ℤ. ✓.
3. u_p+u_r−y1∈ℤ and u_p−y1∈ℤ ⟹ subtract ⟹ u_r∈ℤ. Contradicts u_r∉ℤ. ✓.
4. u_p+u_r−y1 = m1 ∈ ℤ and u_q+y1 = m2 ∈ ℤ ⟹ add ⟹ u_p+u_q+u_r = m1+m2 ∈ ℤ, i.e.
   T∈ℤ. Contradicts the standing hypothesis T∉ℤ. ✓ — **this is the only case that
   needs T∉ℤ**; the other three only need the cleanliness of the pre-cut triangle.

All four cases check out; my independent re-derivation matches the proof's own
(residue/mod-1-flavored) writeup exactly, including the correct handling of "adding
the two integer equalities to get T∈ℤ" in case 4 (verified: the two equalities share
the same real y1, so adding them algebraically cancels y1 and directly yields
u_p+u_q+u_r ∈ ℤ — no hidden step).

## Independent computational verification (not trusting the builder's own table)

I wrote fresh Python (not reusing the builder's script) with two tests:

1. **Random Monte Carlo** (200k trials, exact `fractions.Fraction`, random non-integer
   rational T, random clean triples, random rational y1): 0 counterexamples.
2. **Targeted exhaustive search** (stronger test): for ~17500 random clean triples
   with non-integer rational T, I enumerated the actual finite sets of exact
   integer-crossing y1-values in (0,u_p) for each of the four unclean conditions (not
   random sampling — exhaustive over all integers m in range) and checked all
   A-type/B-type pairs for coincidence. **0 double-unclean events found.**
3. **Control test**: re-ran the same targeted search with T forced to be an *integer*
   (all else unchanged) — found ~79000 double-unclean events out of 15706 valid
   triples tried. This confirms the T∉ℤ hypothesis is genuinely load-bearing (not a
   vacuous or unused assumption) — exactly as case 4 alone requires it.

This is strong independent corroboration of the Cleanliness Lemma beyond the algebra
alone.

## Necessity theorem (induction) check

- **Base case**: equilateral (60°,60°,60°) has u-values T/3 each. Clean since T/3∈ℤ
  ⟹ T=3(T/3)∈ℤ, contradicting T∉ℤ. Correct.
- **Inductive step**: Cleanliness Lemma guarantees a clean child exists at every move;
  Shan-Yu keeps it. Standard induction, correctly set up (checked at "top of loop"
  matching the problem's literal statement: win-condition check happens on the
  *current* T before Mulan's next cut).
- **Conclusion**: clean invariant maintained forever ⟹ no angle ever equals an integer
  multiple of θ, in particular never equals θ itself ⟹ game never terminates with a
  Mulan win ⟹ θ∉S (since S requires a *finite*-step guarantee). Matches the problem's
  literal win condition and S's definition — checked against the problem statement in
  `problems.jsonl` directly.

## Coverage / case-completeness check

- Uniformity over θ≤90° and θ>90°: T∈(1,2) (θ obtuse) contains no integers, so it's
  automatically covered by "T∉ℤ" with no separate case — verified this is not a
  vacuous claim: T∈(1,2) is a genuine subrange with T/3∈(1/3,2/3)⊂(0,1), trivially
  non-integer, consistent with (and reproducing, as remarked) `non-obtuse-invariant.md`.
- Uniformity over rational/irrational θ: the four-case argument uses only "is this
  specific real number an integer," valid for any real y1 without any genericity or
  algebraic-independence assumption — genuinely resolves the "wild x1" gap that
  earlier round-4 sub-approaches (referenced in the file, e.g.
  `backward-induction-transcendence`) got stuck on.
- Every legal move covered: cut-formula.md establishes y1 ranges over the entire open
  interval (0,u_p) for whichever vertex Mulan selects (any of the 3, by choice of
  which side she places P on) — matches the problem's literal rule ("point P... cut
  from P to the opposite vertex") with no omitted move type.
- Boundary values (T=1, T≤0) are excluded by the problem's own hypothesis 0°<θ<180°,
  correctly noted.

No hidden case gap found.

## Cross-check against certified sufficiency lemma

No contradiction: sufficiency proves {180°/n:n≥2}⊆S (including the n=7 witness);
necessity proves the complementary set is excluded from S. These are consistent by
construction (necessity's contrapositive is exactly "θ∈S ⟹ T∈ℤ, T≥2", i.e. θ=180°/n
for integer n≥2 — matching sufficiency's family exactly, no overlap or gap between the
two directions).

## Promotable lemmas — certification decision

- **Cleanliness Lemma (Integer-Multiple-Avoidance)**: CERTIFIED into
  `results/imo-2026-04/lemmas/integer-multiple-avoidance.md`. Self-contained
  (depends only on the already-certified `cut-formula.md`), no `sorry`/gaps, statement
  matches exactly what is proved (not overclaimed), independently re-verified both
  analytically and computationally.
- **Necessity Theorem**: folded directly into `current.md`'s Full proof rather than a
  separate lemma file (it's the problem's own necessity half, not a reusable
  sub-lemma for other problems).

## Actions taken
- `results/imo-2026-04/current.md`: Status set to `solved`; `## Full proof` written
  (combined sufficiency import + necessity argument + answer + verification); the
  `## Approaches tried` entry for `denominator-valuation-necessity` updated to record
  the round-5 verification.
- `results/imo-2026-04/lemmas/integer-multiple-avoidance.md`: created, certifying the
  Cleanliness Lemma.
- `record_outcome` called for `denominator-valuation-necessity`, round 5, outcome
  `verified-milestone`.

## Conclusion
This is a genuinely complete, correct solve of imo-2026-04. The answer
S = {180°/n : n ∈ ℤ, n ≥ 2} is proved in both directions and verified by concrete
instances (n=2,3,7). No further work is needed on this problem.
