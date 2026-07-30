# proof-builder report — `relaxed-adversary-transfer` (round 7, first build)

## Task recap

New slug per this round's outliner (Candidate 1, `aimo-0560` surrogate-
adversary import): attack the general-`n` upper bound over **arbitrary**
Liu Bang configurations by relaxing Xiang Yu to unlimited marks, solving
that relaxed game, then attempting a truncation/rounding transfer down to
the real `≤n`-mark game. Mandatory gate: solve the `∞`-mark relaxation
exactly on 2–3 small configs (incl. geometric `A_n`, `n=2,3`) *before*
attempting the truncation lemma; if the relaxed optimum is degenerate,
report a dead end honestly rather than forcing a proof.

## What was done

1. Set up the relaxed value `V_∞(A) := inf` over all finite refinements of
   `A` with unboundedly many splits, of `oddrank(B)`.
2. Ran the mandated cheap numeric gate first, exact `fractions.Fraction`
   arithmetic, no floats: computed `oddrank` of "split every piece into two
   exact halves" for the geometric configs `A_1, A_2, A_3` and two
   non-geometric configs. All five gave exactly `1/2`.
3. Generalized this to a full proof, not just numerics: **Theorem V-INF**,
   `V_∞(A) = 1/2` for *every* finite configuration `A` and *every* `n`,
   proved two-sided: (a) `oddrank(B) ≥ Σ(B)/2` for any finite multiset `B`
   by a direct pairing/sortedness argument (Lemma PAIR-LB, elementary, self
   contained — pair up consecutive sorted elements, each pair's difference
   is `≥0`); (b) `1/2` is attained (not just approached) by splitting every
   piece of `A` into two exact halves, using exactly `r` marks where `r` is
   the number of pieces of `A` (one more than Xiang Yu's real budget when
   `A` comes from `n` Liu Bang marks, since then `r = n+1`).
4. Diagnosed **why this kills the transfer step**, per the gate's
   honest-stop instruction, rather than forcing a truncation lemma:
   - `V_∞` is completely independent of `A` — it discards exactly the
     information (`A`-dependence) that the target theorem needs.
   - It requires `r = n+1` marks, i.e. **exactly one more** than Xiang Yu's
     real budget — the relaxation doesn't approximate the real game, it
     needs a strictly larger, fixed budget increment to reach its optimum.
   - It bounds the real `n`-mark value from the **wrong side**:
     `V_∞(A) ≤ min_{B: ≤n marks} oddrank(B)` (relaxed adversary is only
     stronger), so `V_∞` is a *lower* bound on the quantity we need to
     upper-bound — a surrogate-adversary transfer in the `aimo-0560` style
     requires the opposite relationship (a harder surrogate's *guarantee*
     transferring to the easier real game), which doesn't apply here
     because relaxing the adversary's budget makes the adversary strictly
     *stronger*, not weaker, so a good bound against the strong adversary
     says nothing useful about the weak one.
   - Checked explicitly against the outline-reviewer's convergence caveat:
     this does **not** converge with `universal-adversary-strategy`'s or
     `minimax-mixed-duality`'s discrete tie-search target — the degenerate
     relaxed optimum is a single `A`-independent universal move, not a
     configuration-dependent finite tie-structure, so there is no shared
     load-bearing content to flag as overlapping.
5. As a natural follow-up (not required by the gate, but the obvious next
   question), tested the most natural finite salvage — "halve `n` of the
   `n+1` pieces, leave one whole" (uses exactly the real budget `n`) —
   against both the geometric config (where it happens to reproduce `c(n)`
   exactly, a coincidence already covered by the existing Proposition 4
   construction) and against random non-geometric configs (`n=1,...,4`,
   thousands of exact-`Fraction` trials): it **fails badly** in general
   (e.g. `n=1`, `A=(4/7,3/7)`: best achievable is `5/7 > c(1)=2/3`),
   confirming there's no cheap fix hiding in this construction and that any
   real fix would require exactly the per-configuration casework the other
   approaches already do.

## Outcome

**Dead end, reported honestly** — this is a genuine negative result, not a
non-attempt: Theorem V-INF is a complete, correctly proved theorem (both
directions), and the diagnosis of why it can't be transferred is structural
(three independent reasons: config-blindness, budget off-by-one, wrong-
direction inequality), not "we ran out of time." Per CLAUDE.md's rigor
rules this is written up as `unsolved` with the negative result recorded
under "Approaches tried" and "Current best," not oversold as `partial`
progress toward the target theorem (it makes zero progress toward proving
`c(n)` is the right bound; it only rules out one proof mechanism).

No lemma files were added to `results/imo-2026-03/lemmas/` — Theorem V-INF
and Lemma PAIR-LB are local to this dead approach and not imported by, nor
useful to, any other live approach's target this round, so per the "shared
cache" purpose of `lemmas/` (importable by other approaches) they are kept
inline in `approaches/relaxed-adversary-transfer.md` rather than promoted.

## File written

`results/imo-2026-03/approaches/relaxed-adversary-transfer.md` — Status
`unsolved`, full writeup of Theorem V-INF (with Lemma PAIR-LB), the exact
numeric verification (5 configs, `Fraction` arithmetic), and the three-part
structural diagnosis of why the transfer step cannot work, plus the
"halve-all-but-one" salvage attempt and its counterexample.

## Recommendation for next round

Retire this slug from active build slots — the mechanism (relax the mark
*budget*) is structurally ruled out for this target, not just this round's
attempt. If a future round wants to revisit the surrogate-adversary idea,
it would need a genuinely different axis of relaxation (not the mark
count) to avoid re-deriving the same degenerate `1/2` value — no such
alternative axis was identified this round, and per the outline-reviewer's
instruction not to re-open plain mixing-over-the-named-menu, none is
proposed here.
