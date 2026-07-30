# Outline review — imo-2026-04, round 2

Reviewed: `dyadic-scaffold.md`, `full-interval-hypothesis.md`, `corrected-genericity-bound.md`,
`binary-word-invariant.md`. Context: the outliner's report resolved a conflict between two
round-1 explorers, confirming the "transfer move" lemma is algebraically correct and θ=60°
IS forceable, refuting the earlier "only θ=90/2^k" genericity claim. I independently
re-verified the core algebra with sympy (not just re-read the outliner's claim):

```
identity ★: (r+p-x1)+(q+x1) - (p+q+r) = 0                     [confirmed, 0]
transfer x1=r+p-θ: A = {q, p+r-θ, θ}   (contains θ directly)
                    B = {r, θ-r, p+q+r-θ} → {r, θ-r, 180-θ} after q=180-p-r  [confirmed]
```
This matches every approach's shared citation of the lemma. No approach misstates it.

## dyadic-scaffold — APPROVE

Whole-attempt: targets the full characterization S, states a proved partial (θ>90°
impossible; θ=180/((2^k+1)·2^j) forceable ∀k,j≥0) and honestly delegates the remaining
gap. Every step traces to a named mechanism (identity ★, non-obtuse invariant, bisection
double-hit, transfer lemma), not a bare "then it follows."

Checked myself, not just trusted:
- Identity ★ and the transfer-lemma output B={r,θ-r,180-θ} — confirmed via sympy above.
- Step 7's validity arithmetic (need p>θ-r for the transfer's non-spectator angle p):
  spectator r<θ, other two angles sum to 180-r, so max(p,q) ≥ (180-r)/2; need
  (180-r)/2 > θ-r ⟺ 180+r>2θ, true since θ≤90 ⟹ 2θ≤180<180+r (r>0 strictly, no
  degenerate triangle). Confirmed correct including at the θ=90° boundary — no hole.
- Non-obtuse invariant: identity ★ forces the two "new" angles to sum to 180°, so they
  can't both exceed 90° — sound, standard invariant-preservation argument (matches
  knowledge_base.md "Invariants & monovariants").

No case coverage issue: this approach explicitly does NOT claim the full characterization,
so there's no missing case, only an acknowledged open gap. This should become `current.md`'s
`partial` baseline as the outliner suggests — it's the only approach here with a fully
closed, hole-free argument top to bottom.

Minor ask for the builder: write out step 7's boundary-case arithmetic in full (already
sketched correctly above) rather than leaving it as a one-line parenthetical.

## corrected-genericity-bound — APPROVE (with a scope requirement)

The audit itself (θ=60° refutes the double-hit-only local lemma) is correct — I re-derived
it independently above and it matches. The diagnosis of the bug (the old argument only
enumerated double-hit configurations and never considered single-hit forced transitions,
which don't need "genericity in y" because the instant-win branch removes Shan-Yu's choice
regardless of the other angle's value) is the right fix and does not throw out genericity
as a technique wholesale, just repairs its enumeration — reasonable.

Concern: as scoped, this approach only ever produces the necessity half (an upper bound on
S). Per CLAUDE.md, a slug must be "a whole attempt ... end to end, not a sub-lemma," and
CLAUDE.md separately warns against splitting one proof across slugs where a shared *unproven*
gap kills both together. Here that trap does NOT apply, because the construction half it
would lean on (dyadic-scaffold's family) is already fully proved, not an open gap — reusing
a certified result is exactly what the `lemmas/` cache mechanism is for. Requirement for the
builder: if step 2 or step 3 yields a genuine invariant/bound, the approach's own "Full
proof" must explicitly combine it with the (cited, re-derivable) dyadic-scaffold construction
to state the complete characterization — don't stop at "necessity done, see sibling for the
rest." If no invariant is found, its deliverable is a documented negative result (valid
`partial`/`unsolved` per CLAUDE.md), not silence.

Sanity check to keep front and center (already flagged in the outline, good): any candidate
invariant must be checked against ALL currently-proven witnesses (60°,36°,30°,20°,15°,...)
before investing in formalizing it — a wrong invariant that blocks a proven-forceable value is
an instant refutation, cheap to catch early.

## binary-word-invariant — APPROVE

Genuinely different framing from the other three (abstracts the triangle entirely, working
only with the orbit of θ/180 under {x/2, 180-x}) — this is real diversity-of-thought, not a
technique variation on the same reduction. Step 1's consistency check (orbit of 90 under the
two generators reproduces dyadic-scaffold's family) is a correct and cheap sanity gate before
trusting the framing further; I re-derived the 60↔120 loop and the 2^k+1 divisibility
condition by hand and it matches dyadic-scaffold's family exactly.

The discriminating test built into the outline (is 1080/7 = 2^k·180/7, i.e. is 2^k=6? No) is
sharp and correctly identifies that under the two-generator monoid alone, 180/7 is NOT
reachable — meaning either the 180/7 computational witness is spurious, or a third generator
is needed. This is exactly the right question to resolve first, and the outline already says
so (step 2 before step 3+). Good.

Step 4 (turning orbit-non-membership into an actual impossibility proof) is honestly flagged
as the hardest, most uncertain part — appropriate, not oversold.

## full-interval-hypothesis — CHANGES REQUESTED

Sound target and correctly imports the proven lemmas, and correctly flags the
rational-vs-irrational θ split as a case that must not be silently dropped if H1 is claimed
(this is a real completeness requirement — CLAUDE.md requires the full claim, and θ ranges
over all reals in (0,180), not just rationals). No fatal flaw, but weakest of the four:

- Step 4's "candidate rules to test" (b1, b2) are vague placeholders, not mechanisms — no
  stated algebraic reason either rule would actually close the recursion. This is the
  "lemma named without its mechanism" pattern CLAUDE.md warns about, even though the outline
  itself labels it TBD rather than claiming it's already done (so it's not overclaiming, just
  underspecified).
- Overlaps substantially with binary-word-invariant's target (both are ultimately trying to
  find/rule out a "third generator" beyond bisect+transfer, both gated on the same 180/7
  witness verification). This is acceptable diversity for one round (different technique:
  direct triangle recursion vs. abstract orbit reformulation) but the builder should
  explicitly cross-check against binary-word-invariant's result on 180/7 rather than
  re-deriving it in isolation — if binary-word-invariant's step 2 already resolves the
  witness, full-interval-hypothesis should consume that result, not redo it.

Required change: do step 3 (hand-verify the 180/7 witness in exact fractions) FIRST, before
any attempt at step 4's general recursion — the outline already says to prioritize this, so
this is enforcing the outline's own stated order, not adding new scope. If the witness turns
out spurious, most of steps 4-5 become moot and the approach should report that finding
rather than continuing to search for a closure rule that isn't needed.

## Diversity assessment

Not a shared-wall collapse: dyadic-scaffold owns the safe constructive baseline;
corrected-genericity-bound attacks necessity via a repaired genericity/invariant technique;
full-interval-hypothesis attacks sufficiency via extended game-tree recursion within the
triangle-geometry framing; binary-word-invariant attacks the same question via full
abstraction into a number-theoretic orbit. Three distinct techniques (invariant hunting,
adaptive game recursion, algebraic reformulation) beyond the shared, already-proven
primitives (identity ★, transfer lemma, bisection) — acceptable diversity for this round.
The one real redundancy risk is the 180/7 witness verification being duplicated by two
approaches; flagged above with an instruction to share the result rather than fatal to either.

## Dead ends avoided

The only prior claim on record (the "S={90/2^k}" double-hit-only genericity argument) is
correctly retired: corrected-genericity-bound documents it under "Approaches tried" as a dead
end with the located bug, and no other approach here repeats it.

## Verdicts summary
- dyadic-scaffold: APPROVE
- corrected-genericity-bound: APPROVE (must present full combined characterization if its
  necessity result lands, not just the necessity half)
- binary-word-invariant: APPROVE
- full-interval-hypothesis: CHANGES REQUESTED (verify 180/7 first per its own stated order;
  replace vague b1/b2 placeholders with an actual mechanism once step 3 is done; consume
  binary-word-invariant's witness result rather than re-deriving independently)

build set: dyadic-scaffold, corrected-genericity-bound, binary-word-invariant, full-interval-hypothesis
