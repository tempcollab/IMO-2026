## imo-2026-04

**Conflict resolution (done this round, verified independently with sympy):** The
"transfer move" lemma from `math-explorer-adversary.md` is ALGEBRAICALLY CORRECT
(re-derived: cutting the p-vertex with x1=r+p-θ, for spectator r<θ and p the larger
of the other two angles, gives A={q,p+r-θ,θ} containing θ directly, forcing B, and B
simplifies via p+q+r=180 to exactly {r,θ-r,180-θ}, independent of q). The hand-worked
θ=60° 2-move construction from that report checks out end to end (spectator = min
angle <60 exists unless equilateral; escape state is exactly {r,60-r,120}; bisecting
120 forces 60 into both children). So **θ=60° IS forceable — H2 ("only θ=90/2^k") is
REFUTED**, and the `math-explorer-characterization.md` genericity/algebraic-
independence necessity argument has a located bug: its "local lemma" only searched
one-move DOUBLE-HIT configurations (both children contain θ), and never considered
single-hit forced transitions (one branch is an instant win, forcing Shan-Yu into a
deterministic escape state) — these do not require "identity in y" / genericity at
all, since the instant-win branch removes Shan-Yu's choice regardless of how generic
the other angles are. This bug is documented in detail, with the correct/incorrect
mechanism spelled out, in `corrected-genericity-bound.md`.

What IS solid and reusable by every approach (re-verified this round, not just cited):
θ>90° impossible (non-obtuse invariant, closed under cevian cuts via the identity
(r+p-x1)+(q+x1)=p+q+r=180); θ=90° forceable in 1 move from any triangle (altitude-foot
double hit); bisection forces a/2 into both children unconditionally; the transfer
lemma (above) forces {r,θ-r,180-θ} or an instant win; composing these gives
θ=180°/((2^k+1)·2^j) forceable for all integers k,j≥0 (explicit finite, Shan-Yu-immune
construction). The EXACT upper characterization of forceable θ in (0°,90°] remains
open — computational evidence (from the adversary explorer, not yet hand-verified)
suggests it may be strictly larger than this family (e.g. 180/7°), but also not the
full interval (25°,40°,50°,70° not found forceable at search depth 12 in a restricted
move family, which is suggestive but not proof of impossibility).

dyadic-scaffold: new
Target: characterize S = {θ : Mulan can force θ}, established so far as a safe,
fully-verified partial result (not the full characterization).
Technique: direct algebraic bookkeeping of cevian-cut children (identity ★), invariant
method for necessity>90°, constructive/inductive family for sufficiency.
Skeleton: see approaches/dyadic-scaffold.md steps 1-9.
Key lemmas: identity ★ (sum of new angles =180 exactly); non-obtuse invariant closed
under cuts; transfer lemma escape formula B={r,θ-r,180-θ}; bisection double-hit.
Open gaps: exact S beyond {180/((2^k+1)2^j)} (delegated to sibling approaches); full
write-up of the "p chosen as larger non-spectator angle always valid" arithmetic.
Cases to cover: none additional (upper-bound θ>90 vs constructive family θ≤90 already
split).
Watch out for: boundary case θ=90 exactly in the validity arithmetic of step 7.

full-interval-hypothesis: new
Target: prove S = (0°,90°] exactly (Mulan wins for literally every θ up to 90°, no
exceptions).
Technique: extend the transfer lemma to a nested/adaptive two-level recursive
strategy, breaking out of the {r,θ-r,180-θ} fixed cycle via a richer closure rule than
plain bisection of 180-θ.
Skeleton: import dyadic-scaffold steps 1-7; reframe the escape state as a sub-game
with 180-θ as a fixed pinned constant; hand-verify the 180/7° computational witness
end-to-end; attempt a full recursive closure (candidate rules b1/b2); handle
irrational θ explicitly if H1 is claimed; report negative result if the recursion
provably does not close to the full interval.
Key lemmas: (imported) transfer/bisection/non-obtuse invariant; (to establish) nested-
recursion closure lemma — currently just a search procedure, not a proved lemma.
Open gaps: essentially everything past the imported lemmas — genuinely open research.
Cases to cover: rational vs irrational θ (an intrinsically rational construction
cannot alone prove H1 for irrational θ).
Watch out for: don't trust the depth-12 restricted search as proof of anything;
always re-derive by hand/sympy. Do not silently assume Shan-Yu is forced onto a
branch without checking the OTHER branch is truly an instant win.

corrected-genericity-bound: new (this IS the requested audit approach)
Target: produce a CORRECT necessity/upper-bound argument on S beyond θ>90°, using a
repaired genericity technique or a genuine closed invariant — or conclusively retire
genericity as a technique for this problem if unrepairable.
Technique: genericity/algebraic-independence (repaired to correctly enumerate BOTH
double-hit and single-hit forced-transition moves at every node), or a fallback
denominator/2-adic invariant analogous to the non-obtuse invariant.
Skeleton: state the audit finding (H2 refuted, with the located bug) as the opening
lemma; attempt the repair by re-enumerating all forcing mechanisms; try a genuine
closed invariant (e.g. denominator/prime-factor obstruction on rational-multiple-of-
180 angles) as a fallback necessity tool; if both fail, report the negative result
explicitly (a valid, useful outcome per CLAUDE.md).
Key lemmas: audit finding (θ=60° forceable via single-hit transfer, refuting the
double-hit-only local lemma) — DONE, re-verified with sympy this round. Repaired
bound / invariant — TBD, open.
Open gaps: steps 2-3 (repair attempt, invariant search) are fully open; may resolve
to "no necessity result found beyond θ>90°," which is itself valuable information.
Cases to cover: none (necessity-only approach).
Watch out for: don't repeat the double-hit-only restriction under a different name;
sanity-check any proposed invariant against ALL already-proven witnesses (60°,36°,
30°,20°,15°,...) before investing time formalizing it.

binary-word-invariant: new
Target: same characterization, via a distinct reformulation — model the game as a
monoid action on θ/180 alone (generators x↦x/2, x↦180-x), abstracting away the
triangle's other two angles, and characterize S as an orbit.
Technique: reformulate in another domain (knowledge_base.md heuristic) — abstract
number-theoretic orbit computation instead of triangle-geometry bookkeeping.
Skeleton: verify the orbit of 90 under {x/2,180-x} exactly reproduces dyadic-
scaffold's family (sanity check); hand-extract and verify the 180/7 witness
(resolves whether it's genuine or a search artifact — feeds every other approach);
if genuine, find and add the missing third generator (nested transfer) and
recompute the enlarged orbit; attempt to turn orbit-non-membership into an actual
impossibility proof (hardest, most uncertain step, flagged explicitly).
Key lemmas: orbit-reproduces-family sanity check (mechanism: g2 then repeated g1 is
literally transfer-then-bisect). Third-generator identification — TBD, conjectural.
Open gaps: everything past the sanity check in step 1; step 4 (orbit-non-membership
⟹ impossibility) may not be tractable and is the approach's biggest risk.
Cases to cover: rational vs irrational θ, same caveat as full-interval-hypothesis.
Watch out for: don't trust the depth-12 search's 180/7 result without hand-verifying
the actual witness path first (step 2) — this is the single highest-leverage check
in the whole field, since it discriminates between "family is exactly tight" and
"family needs a genuinely new generator," and several other approaches' direction
depends on its answer.

Build-set recommendation for this round: all four (dyadic-scaffold first — it is the
safest and most complete, should become `current.md`'s partial baseline immediately;
corrected-genericity-bound second — the audit is done, needs formal write-up as a
certifiable lemma; full-interval-hypothesis and binary-word-invariant third/fourth —
both hinge on hand-verifying the 180/7 witness, which should be prioritized early in
whichever builder(s) take these, since it's the single most informative unresolved
fact in the whole population).
