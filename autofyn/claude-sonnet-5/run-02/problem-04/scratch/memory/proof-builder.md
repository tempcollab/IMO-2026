ALWAYS: when a lemma's validity arithmetic has a boundary case (e.g. θ=90° exactly in a
transfer-move inequality), write out that boundary substitution explicitly in the proof
text rather than leaving it as "true whenever θ≤90" — reviewers will flag it as a hidden
case even when the inequality is genuinely non-degenerate there (round 2, imo-2026-04).

ALWAYS: when chaining several "adversary-immune forcing" moves (each guarantees a target
value appears in the kept child regardless of which child the adversary keeps) into a
multi-stage construction (e.g. spectator-creation -> transfer -> bisection -> halving
closure), explicitly define "immune-forceable" once and prove each primitive lemma has
that property, then argue the composite sequence inherits it by induction on move count
— this avoids silently needing to track the adversary's actual choice history (round 2,
imo-2026-04).

NEVER: claim "θ forceable ⟹ θ/2 forceable" by informally "running the same strategy and
bisecting once more" without addressing why the intermediate target value (θ) appearing
mid-sequence doesn't end the game early against the WRONG target — resolve this by
noting the real game only stops at the true final target, so an intermediate waypoint
value appearing is harmless (round 2, imo-2026-04).

ALWAYS: when asked to "hand-verify a computational witness" for a specific numeric
value, don't trust a naive BFS/closure search over exact fractions as proof of
non-reachability — infinite move families (e.g. repeated bisection x->x/2) never
produce an empty frontier, so a loop that "breaks when frontier is empty" silently
never breaks and the reported "closure size" is just wherever the depth cap stopped;
switch to an algebraic argument (e.g. track the composition as an affine map and find a
modular/order-of-an-element obstruction) which is both correct and gives a genuine
proof, not a bounded numerical hint (round 2, imo-2026-04).

NEVER: assume a per-round dispatch note that a sibling approach "may have already
resolved X in parallel" means you can skip verifying X yourself — sibling files may
still show placeholder/unsolved content when you check (parallel timing), so redo the
verification independently and just note the cross-check attempt, rather than blocking
on or silently trusting an unfinished file (round 2, imo-2026-04).

ALWAYS: when a "genericity" necessity argument was refuted for ignoring single-hit
forced transitions, repair it by tracking an algebraic-independence invariant through
EVERY move type (not just re-restricting to double-hits): represent every reachable
quantity as a Q-affine combination of {1, target, adversary's chosen transcendentals},
show every legal move propagates the nonzero/zero status of the adversary-transcendental
coefficients without ever cancelling them to zero, then conclude only the "coefficient-
free" (pure target-relation) values can ever equal the target — this correctly captures
single-hit moves (which need no genericity to execute) while still blocking them from
ever producing a win, giving a genuine closed-form necessity proof in one round instead
of an open research gap (round 2, imo-2026-04).

ALWAYS: before trusting an abstract "generator set" sketch from an outline (e.g. a
2-generator monoid on a game's parameter), re-derive the FULL exhaustive case-split of
the real move formula (here: solve for every x1 that places the target in either child
of a cevian cut) rather than adopting the outline's assumed generators as-is — round 2
imo-2026-04 found a missing third primitive ("shift": x1=θ, needs only p>θ, no spectator
condition) this way, which strictly enlarged the provable forceable set (180/n for ALL
n≥2, not just dyadic-related n) and rigorously confirmed a witness (180/7) the outline
only flagged as suspicious.

ALWAYS: for necessity in a "cut a triangle, adversary discards" game with a fixed
target theta, try normalizing all angles by theta (u = angle/theta, sum = T = 180/theta
constant) and look for an invariant of the form "no angle's normalized value is an
integer" preserved via a mod-1 residue argument on the cut parameter y1 — this handles
literally ARBITRARY real y1 (no genericity/transcendence/wild-x1 casework needed at
all) because "is a specific real number an integer" is well-defined regardless of its
algebraic nature; the four possible "both children hit an integer" coincidences reduce
to algebraic identities that force T integer, closing necessity in one clean lemma
where three sibling approaches (genericity/transcendence-degree machinery) were stuck
on an open wild-x1 gap for multiple rounds (round 4, imo-2026-04).

NEVER: assume an outline's proposed invariant (e.g. "odd part of denominator divides
odd part of theta's denominator") is the only tractable route just because it's the one
handed down — spend 10-15 min searching for a structurally simpler invariant from
first principles (here: integer-vs-non-integer in theta-units beats 2-adic/odd-part
bookkeeping) before committing to formalizing the outline's harder conjecture; a
simpler true invariant is worth more than a hard-to-derive one (round 4, imo-2026-04).
