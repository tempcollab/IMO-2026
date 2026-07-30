# Outline review — round 12 — imo-2026-03

## Scope

Only one slug is in the round-12 outline: `universal-adversary-strategy`,
"Round 12 plan — Candidate 5: budget-capped TAIL-SNIP recursion". Target:
close Claim PTBI's Case C (`p_1<Σ(A)/2`) for general `m≥4`, the sole
remaining open gap in the whole problem (lower bound fully closed since
round 10; `m=1,2,3` of the upper bound fully closed).

## Verdict: `universal-adversary-strategy` — CHANGES REQUESTED (proceed to build with two fixes flagged below; not a RETHINK)

The plan is well-specified, correctly scoped (whole-problem target, not a
sub-lemma), builds only on already-certified lemmas (PAIR-VALUE,
BLOCK-RECURSE, THRESHOLD-REDUCTION), and does not repeat any recorded
dead end (Route A / Route B of round 11, the non-contiguous-subset-match
guess refuted this round by `math-explorer-subsetmatch`'s exhaustive
127-subset check, `minimax-mixed-duality`, `relaxed-adversary-transfer`,
`case-c-secondary-extremality`). I independently re-implemented Candidate
5 from scratch in Python (`fractions.Fraction`, exact arithmetic) to
check the three specific things the dispatch asked me to verify.

### 1. Is the mandatory Step 1 adversarial gate well-specified and as strong as the method that caught `m=8`?

Yes. It specifies the exact same tool
(`scipy.optimize.differential_evolution` or an equivalent global
optimizer), the exact same target (`target(m,A) - Candidate5(A)`
minimized over the Case-C simplex), an explicit range (`m=4` to at least
`12`, not stopping at one `m` — correctly learned from this round's own
history, where Candidate 3 passed 3600+ random trials and 2 hard
witnesses before the optimizer alone found `m=8`), a mandatory
exact-`Fraction` rationalization step before trusting any near-zero
margin, and an explicit fallback (`budget=2`) if `budget=1` fails. This
is not weaker than the method that found `m=8` — it is the same method,
applied over a wider `m` range. The "Watch out for" section explicitly
warns the builder not to skip Step 1 on the strength of the 523-trial +
2-witness pass, citing the exact failure mode that bit Candidate 3. I
independently re-verified the plan's claimed `m=8` result myself
(script below): Candidate 5 gives `oddrank=1/2` exactly on the
(rationalized) `m=8` witness the plan cites, against target `128/255 ≈
0.5019608` — margin `≈0.00196`, closing the previously-negative
Candidate-3 margin (`≈-1.53e-4`). This reproduces the plan's central
empirical claim exactly, giving confidence the Step 1 gate description
is accurate, not aspirational.

### 2. Is the well-foundedness argument (lexicographic `(|A|, budget)` measure) actually sound?

**Not quite as literally stated — a real but easily-fixable spec bug,
not fatal.** The plan states the measure is `(|A|, budget)` lexicographic
with `|A|` as the *primary* decreasing coordinate ("with budget as the
primary decreasing coordinate whenever `|A|` does not decrease" — this
phrasing is self-contradictory: it can't be both `|A|`-primary and, in
the one case that actually needs it, budget-primary). Concretely:
`tail-snip` **increases** `|A|` by 1 while strictly decreasing `budget`.
Under a literal `(|A|,budget)` lex order with `|A|` primary, `tail-snip`
does **not** decrease the measure (the primary coordinate goes up) — the
correct measure is `(budget, |A|)` lexicographic with **budget primary**:
`halve` (budget unchanged, `|A|` ↓) and `partial-dom` (budget
non-increasing, `|A|` ↓) both decrease it on the secondary/primary
coordinate as appropriate, and `tail-snip` (budget strictly ↓, `|A|` ↑)
decreases it on the primary coordinate regardless of the secondary. This
is well-founded (budget bounded below by 0, `|A|` bounded below by 1)
under the corrected order, but not under the order as literally written.

I also checked the second load-bearing fact this well-foundedness
argument silently needs and that the plan does not state explicitly:
**`partial-dom`'s `j* ≥ 1` always**, so `|A|` strictly decreases on
every `partial-dom` call *regardless of budget* (this matters because if
`budget=0`, `max(budget-1,0)=0` doesn't decrease, so `partial-dom` must
carry its own termination guarantee independent of budget). This holds
because `A` is sorted descending so `A[0] ≥ A[1] = S_1`, forcing
`j*≥1` unconditionally when `|A|≥2`. I verified this by direct
argument and by a 2000-trial randomized check (zero violations) — it is
true, but the plan does not state it as an explicit fact the
well-foundedness proof depends on; the builder should state and prove it
(one line) alongside the corrected measure.

I additionally stress-tested termination empirically: Candidate 5 on 30
random configurations `m=4..12`, `budget=1`, all completed instantly, no
runaway recursion — consistent with (but not a substitute for) the
corrected formal argument above.

**Required fix for the builder:** restate the measure as
`(budget, |A|)` lexicographic, budget primary; add the explicit `j*≥1`
lemma (or an equivalent one-line sortedness fact) as part of the
well-foundedness proof, not just asserted. This is a specification
error in the outline, not in the underlying mechanism — Candidate 5
itself terminates correctly, only the *written measure* in the plan is
mis-ordered. Not fatal, but must be fixed before the builder writes the
formal induction, since a wrong measure statement would let a reviewer
later flag it as an unjustified claim.

### 3. Is skipping a second diversity slug this round justified?

Agree with the outliner. This is the 4th consecutive go/no-go check
(rounds 7, 9, 10, 11, now 12) on alternative framings, and every
concrete alternative tried in this run's history (concavity/smoothing,
LP/mixed duality, secondary-extremality, ∞-mark relaxation) has a
*structural* obstruction, independently re-verified by this reviewer in
prior rounds — not a stalled search that a fresh framing would unstick.
`case-c-secondary-extremality`'s round-11 RETHINK in particular showed
*why* a structurally different proof shape converges to the same
closed-form question `universal-adversary-strategy` already owns
(the two competing constructions are provably value-equivalent by
algebra) — this is evidence the remaining gap is genuinely a single
precise combinatorial fact (Lemma BUDGET-SUFFICES / the general
donor-matching existence question), not evidence of an unhealthy
single-line collapse. The one new lever found this round
(Hall-deficient-set-deletion from crux `aimo-0063`) is correctly folded
into Step 2a's mechanism list as a refinement within the existing
framing rather than spun into a same-wall-later sibling slug. I concur
this is the right call for this round. **Caveat for the record:**
Case C at general `m≥4` has now been the single blocking gap for
rounds 10, 11, and 12 with no closure; if round 12's build again fails
to close it (Step 2b) or leaves Lemma BUDGET-SUFFICES's general proof
open, round 13's outliner should be told explicitly to open at least
one approach that attacks the donor/matching existence question via a
different combinatorial tool than Hall-deficient-set-deletion (e.g. a
direct entropy/potential-function argument on the tie structure, or an
extremal-configuration/compactness argument bounding how many
near-uniform "hard" sub-configurations can nest), rather than running a
5th go/no-go check on the same rejected list of framings.

## Other approaches in the population

Not built this round (per dispatch); left untouched by the outliner as
instructed. Ranking updated below to reflect last-round outcomes and
anchor the newcomer's history: `recursive-embedding-induction` and
`geometric-dominance-construction` (lower bound fully closed,
`verified-milestone`/`partial` respectively) rank above
`universal-adversary-strategy` (still open on Case C); `universal-
adversary-strategy` ranks above the two RETHINK/dead-end approaches
(`case-c-secondary-extremality`, `minimax-mixed-duality`) and above the
stagnant, conditionally-overclaimed `equalization-potential-bound`.

## Verification scripts

`/tmp/check_c5.py` — independent from-scratch re-implementation of
Candidate 5 (`solve`/`solve_full`), exact `Fraction` arithmetic:
reproduces the plan's `m=8` witness closure (`value=1/2` vs
`target=128/255`, margin `≈0.00196`) and confirms `j*≥1` always
(2000-trial randomized check, zero violations) and clean termination on
30 random `m=4..12` instances.

## Actions taken

- No new slug registered (none opened this round).
- No copy requested (no branch proposed).
- Ranked the field via `update_ranking` (recursive-embedding-induction >
  universal-adversary-strategy > case-c-secondary-extremality;
  universal-adversary-strategy > minimax-mixed-duality;
  universal-adversary-strategy > equalization-potential-bound;
  geometric-dominance-construction > case-c-secondary-extremality),
  clearing stale flags.

build set: universal-adversary-strategy
