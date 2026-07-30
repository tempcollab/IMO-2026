# Proof-builder report — `universal-adversary-strategy`, round 7

## Summary

All three assigned tasks addressed. Two cheap compositional lemmas
certified in full (Lemma MULTI-HALVE, Lemma PARTIAL-DOM-RESIDUAL), the
flagged `dim(Q)=0` gap in Lemma TIE-NECESSARY's proof fixed, and the
retargeted induction attempt on the matching/assignment theorem produced
one genuinely new, general, fully-proved lemma (Lemma DOUBLE-INSERT) plus
a precise (not vague) diagnosis of where the induction fails, backed by
concrete numeric stress tests against both hard `m=5` witnesses. Status
remains `partial` — the general upper-bound induction is not closed — but
this is real, verified progress, not a repeat of prior rounds' findings.

## Task 1 — cheap compositional lemmas (both certified in full)

- **`lemmas/multi-halve.md`** — Lemma MULTI-HALVE: simultaneously halving
  the top `K` pieces whenever `p_K≥2p_{K+1}` gives
  `oddrank(B)=Σ_{i=1}^K p_i/2 + oddrank(Tail)`. Direct rank-shift proof
  (even shift by `2K`), identical technique to the already-certified
  DOM/HALVE/SPLIT family. Verified exactly (`Fraction`) against the
  explorer's witness `A=(0.583,0.3461,0.0709)`, `K=2`:
  `oddrank=10709/20000=0.53545<c(2)=4/7`.
- **`lemmas/partial-dom-residual.md`** — Lemma PARTIAL-DOM-RESIDUAL:
  composes the certified Lemma PARTIAL-DOM and Lemma SPLIT, applying SPLIT
  to PARTIAL-DOM's residual `r` at its already-known exact sorted rank.
  No new proof machinery. Verified exactly against the explorer's Witness
  1 `A=(0.5798,0.3515,0.0687)`, `j=1` (a genuine sub-maximal choice):
  `oddrank(B)=5798/10000\to oddrank(B')=10687/20000=0.53435<c(2)`.

Both independently reproduced the explorer's numeric findings to the exact
fraction, not merely approximately.

## Task 2 — Lemma TIE-NECESSARY `dim(Q)=0` fix

Rewrote the flawed paragraph in `lemmas/tie-necessary.md`: the old text
incorrectly claimed a `0`-dimensional cell must arise from a collapsed
chain-simplex boundary (unconditionally forcing condition (a)). The fixed
version derives "(a) or (b)" directly from the cell's own defining
constraints — at an extreme point, at least one of the finitely many
defining inequalities (of either type) must be tight, with no claim about
which type. Added a concrete worked counterexample to the old claim (two
independent order-ties pinning a 2-mark single-piece polytope to a point,
no zero-length piece anywhere) directly in the lemma file. The lemma's
statement was never wrong; only this proof branch needed correcting — no
regression to the certified status.

Also corrected `lemmas/partial-dom.md`'s Remark per the catch-up review:
actual scope is `r<t_j` (checked directly, not tied to `j` being maximal),
not the stricter `r<U_1`. Exercised by the PARTIAL-DOM-RESIDUAL witness
above, which uses a *third*, previously undocumented regime (deliberately
sub-maximal `j`, chosen to leave budget for the residual refinement).

## Task 3 — retargeted induction attempt (open, but real progress)

Attempted **Claim PTBI**: for every sorted `A` of `m` pieces, `≤m-1` marks
give `oddrank(B)≤c(m-1)Σ(A)`. Base case trivial. Inductive step ("peel
`p_1`, recurse independently on the tail, halve `p_1`") uses a genuinely
new lemma discovered this round:

**Lemma DOUBLE-INSERT** (`lemmas/double-insert.md`, certified in full):
inserting a duplicated value `{v,v}` into *any* sorted list changes
`oddrank` by exactly `+v`, **unconditionally** — no domination hypothesis
needed at all. This strictly generalizes Lemma HALVE (whose `p_1≥2p_2`
hypothesis turns out never to have been necessary for the value identity,
only for the historical assumption that the pair lands at the top).
Verified by 2,000 exact-`Fraction` trials, zero mismatches.

Plugging this into the induction, the required inequality
`c(m-2)S+p_1/2 ≤ c(m-1)(p_1+S)` **fails algebraically** at the "IH tight
and `p_1` at its structurally-forced minimum `S/(m-1)`" combination (e.g.
`m=5`: naive bound `≈0.5267 > c(4)≈0.5161`). Checking this exact boundary
configuration numerically (`A` uniform, `m=5`) shows the *true* optimum
there is `0.5` (via Lemma TAIL-SNIP, 1 mark) — i.e. the pessimistic
combination that breaks the algebra does not correspond to an actual hard
instance, but this alone does not repair the general induction (the naive
scalar IH is provably too weak; a sharper, `p_1`-correlated IH is needed
and not constructed this round — precisely diagnosed, not closed).

**Stress test against the two mandated `m=5` witnesses**: computed
(`scipy.optimize.differential_evolution`) that the simple "peel + recurse
independently on the tail (full allocation search) + unconditionally halve
`p_1` via Lemma DOUBLE-INSERT" construction closes **both**:
- `A=(0.4265,0.2536,0.1747,0.1014,0.0438)`: `≈0.51065 < c(4)≈0.5161`
  (margin `0.0055`).
- `A=(0.3415,0.3023,0.1664,0.1404,0.0494)`: `≈0.50225 < c(4)≈0.5161`,
  numerically matching the true global optimum to 5 decimal places despite
  using a different (non-coordinated) allocation.

This **refutes, for the purposes of proving the upper bound** (not for
finding the true optimum), the menu-coverage explorer's concern that these
witnesses require irreducible 3-piece coordination — a genuinely different,
simpler construction suffices. Sanity-checked further against two
previously-recorded hard `m=3` witnesses (both closed too). Status remains
honestly `partial`: the general theorem is not proved, and the precise
remaining gap (a sharper induction hypothesis, or a menu-based case split
with a completeness proof) is stated exactly, not vaguely, so a future
round does not need to re-discover any of this round's findings.

## Files touched

- `results/imo-2026-03/approaches/universal-adversary-strategy.md` —
  updated in place (new round-7 "Approaches tried" bullet, full "Round 7"
  section, updated "Full proof" summary, updated "Promotable lemmas").
- `results/imo-2026-03/lemmas/multi-halve.md` — new, certified.
- `results/imo-2026-03/lemmas/partial-dom-residual.md` — new, certified.
- `results/imo-2026-03/lemmas/double-insert.md` — new, certified.
- `results/imo-2026-03/lemmas/tie-necessary.md` — `dim(Q)=0` proof fixed,
  Status note updated; statement unchanged.
- `results/imo-2026-03/lemmas/partial-dom.md` — Remark's stated scope
  corrected (`r<t_j`, not `r<U_1`/"`j` maximal").

Did not touch `current.md` (reviewer-owned per CLAUDE.md).
