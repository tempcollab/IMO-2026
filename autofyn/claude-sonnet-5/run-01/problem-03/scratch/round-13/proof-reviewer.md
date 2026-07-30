# Proof-reviewer report — round 13 (imo-2026-03)

Reviewed builds: `universal-adversary-strategy` (main) and
`universal-adversary-strategy-exact-tie` (new this round). One
builder report (`proof-builder-universal-adversary-strategy.md`) was
present in `/tmp/round-13/`; the second (`exact-tie`'s) was not saved to
disk, so I reviewed its work directly from the committed approach file
`results/imo-2026-03/approaches/universal-adversary-strategy-exact-tie.md`
(311 lines, self-contained, git-tracked) instead, per the standing rule
of reconstructing lost reports from the raw file changes.

## Headline finding (independently re-derived from scratch, not reusing
## either builder's code)

Both builds independently discovered the same root problem: **the
Round-12 certified `solve(A,budget)` recursion (Lemma WF-C5) does not
faithfully model Xiang Yu's true mark budget.** `budget` only counts
nested Move-3 (tail-snip) uses; Move 1 and Move 2 never decrement any
real-mark counter, and Move 3 itself increases `|A|` by 1 without being
charged. I independently confirmed this with three from-scratch checks
(my own Python, exact `fractions.Fraction`, plus `scipy` continuous
optimization over the literal constrained game — no code copied from
either builder):

1. **Reimplemented `solve(A,budget)` from scratch** (the certified
   Round-12/WF-C5 specification) and reproduced `solve_full((26,21,10))
   = 57/2 = 28.5 = Σ(A)/2` exactly, confirming the "apparent identity"
   both this round's explorer and the `exact-tie` builder found is a
   real fact about this specific recursion. Traced the winning move
   path with my own debug instrumentation: `move3(snip 10) → move1(halve
   26) → move1(halve 21) → move2(jstar=1, r=0, free tie)`. **Counting
   real elementary splits: 3 marks used, against a true budget of
   `m-1=2`.**
2. **Independently verified the TRUE 2-mark-constrained game value** for
   `A=(26,21,10)` via an exhaustive-over-allocation-pattern `scipy`
   search (both topologically distinct 2-mark patterns on 3 pieces: one
   piece split into 3 parts, or two different pieces each split once;
   many random restarts plus a `differential_evolution` cross-check to
   rule out local-optimum artifacts). **The true value is exactly `31`,
   not `28.5`.** This independently confirms `universal-adversary-
   strategy-exact-tie`'s refutation of the sharper "exact identity"
   conjecture (`solve_full(A)=Σ(A)/2` throughout Case C) is correct.
   Note `31 ≤ c(2)Σ(A) = 228/7 ≈ 32.57` — Claim PTBI's actual (weaker)
   target is untouched by this witness.
3. **Independently verified the second, sharper finding** (`universal-
   adversary-strategy`'s main build: the bug also reopens Case (a),
   previously assumed trivial). Witness `A=(0.45,0.20,0.15,0.12,0.08)`,
   tail `T=(0.20,0.15,0.12,0.08)`. I built my own exhaustive `scipy`
   search over every mark-allocation composition (0 to 3 marks split
   among `T`'s 4 pieces, continuous ratios, hundreds of random restarts
   per composition) and found **the TRUE 3-mark-constrained value of `T`
   is exactly `27.5 = Σ(T)/2`** (achieved by `20→(12,8)` — a
   non-contiguous exact tie against `T`'s own existing elements `12,8`,
   skipping `15` — plus `15→(7.5,7.5)`, using only 2 of 3 marks). This
   is important: **it does NOT refute HALF-BOUND on this witness** (the
   true value exactly meets the target `≤ Σ/2`). What it does refute is
   the *sufficiency* of the certified move-menu: I independently
   reimplemented the correctly mark-capped but menu-restricted
   `solve2(A,marks)` (contiguous-prefix-only Move 2, per the
   builder's spec) and got `solve2(T,3)=28 > 27.5` — confirming the
   menu itself (even with correct mark accounting) cannot express the
   non-contiguous match needed, so a proof via this menu is genuinely
   insufficient, even though the underlying claim still holds.

## Consequence: Round 12's "adversarial gate PASS" is retracted as
## evidence

Round 12's gate checked `solve_full(A) ≤ c(m-1)Σ(A)` using the uncapped
`solve` recursion. Since granting the minimizing player (Xiang Yu) more
moves than he truly has can only make the computed value smaller or
equal to the true, correctly-capped value, **a "PASS" of that gate
establishes nothing about the real game — it bounds a strictly
easier-for-Xiang-Yu surrogate, the wrong direction for certifying the
theorem.** This is a genuine methodological invalidation of Round 12's
headline conclusion (not a minor bookkeeping slip), and I have written it
explicitly into `current.md` with a "do not cite" instruction for future
rounds.

**What is NOT affected:**
- **Lemma WF-C5 itself stands, unmodified.** I re-read its file
  (`lemmas/wf-c5.md`): it only proves the abstract recursion terminates
  (a well-founded lex-order argument), and never claims to model real
  marks. That correctness/faithfulness gap is a separate, additional
  fact this round discovered, not a flaw in WF-C5's actual proved
  content.
- **The entire lower bound** (Lemma TREE-BOUND-MULTICLUSTER, round 10)
  and **`m=3`'s fully-solved upper bound** (round 9) are untouched — no
  part of this round's finding concerns them.
- On every witness tested this round with a properly capped model,
  Claim PTBI's actual (weaker) target still holds (`31≤228/7`;
  `27.5≤27.5` exactly). No counterexample to the real theorem has been
  found — only to the round-12 evidentiary claim and to the sharper
  "exact identity" conjecture.

## Verdicts

### `universal-adversary-strategy` (main) — CHANGES REQUESTED

Status: `partial` (correctly self-reported, no overclaiming). Real,
independently-confirmed progress: correctly diagnosed that the outline-
reviewer's narrower "Case (b) Move-3 budget" complaint is a symptom of a
general defect, and found it also breaks Case (a). Built the corrected
`solve2(A,marks)` model (properly mark-capped, though still restricted to
the old contiguous-prefix Move-2 menu — I independently confirmed this
restriction is itself insufficient on the `T` witness, exactly as the
builder reports). No new certifiable lemma this round (correctly not
claimed as one — the builder explicitly says the `solve2` accounting is
diagnostic, not a standalone theorem). Case C for general `m≥4` remains
open. This is valuable negative/diagnostic progress narrowing what the
eventual proof must contain (the Hall-type subset-matching existence
theorem, unavoidable even in Case (a)) — routed CHANGES REQUESTED, not
RETHINK, since the framing (casework + menu extension) is still sound,
just incomplete.

### `universal-adversary-strategy-exact-tie` (new) — CHANGES REQUESTED

Status: `partial` (correctly self-reported). Assigned to prove a sharper
identity via a Hall-type existence route; instead found and rigorously
refuted the identity itself, on the correctly-capped model, with a
concrete witness confirmed by two independent methods internally
(menu-restricted DP + unrestricted continuous optimizer) and by me
independently from scratch (matching `31` exactly). Proved Lemma
NONNEG-EXCESS (a genuinely correct, if narrowly useful, fact about the
uncapped recursion) — I independently re-derived the induction and
stress-tested it (3000 random trials, minimum excess found exactly `0`,
matching). Honestly scoped: explicitly does not claim to refute or close
Claim PTBI itself, and correctly notes the real target still holds on
its witness. This is a valuable, population-pruning negative result
(rules out the sharper identity as a viable route) plus a genuine,
serious discovery (the round-12 gate's invalidity) that benefits every
other approach in the population. Routed CHANGES REQUESTED (real
progress, not a dead end — the underlying weaker theorem remains a live,
undisproven target, and the approach's Hall's-theorem framing itself is
not shown unworkable, just not yet executed).

## Lemma certification

- **CERTIFIED**: `lemmas/nonneg-excess-uncapped-recursion.md` (new file
  I wrote this round, formalizing `universal-adversary-strategy-exact-
  tie`'s Lemma NONNEG-EXCESS). Statement correct as proved, `sorry`-free,
  independently re-verified (3000-trial stress test, zero violations).
  Certified with an explicit, prominent scope warning: it is a fact
  about the specific *uncapped* `solve(A,budget)` recursion only, not
  about the true mark-capped game value — flagged so no future round
  mistakes "excess ≥ 0" for evidence about the real game.
- The "mark cost of peel+snip+auto-tie" fact and the corrected `solve2`
  model are useful diagnostic constructions but are NOT certified as
  standalone lemmas this round — `solve2` itself is demonstrably not a
  faithful model of the true game (it can report a value exceeding the
  target even when the true value meets it, due to menu insufficiency),
  so certifying it as "the corrected recursion" would risk exactly the
  kind of trust-without-verification error this round's finding is about.
  Recommend any future round that reuses `solve2` treats a "PASS" as
  valid evidence (properly capped menu-restricted values are provable
  upper bounds on the true value, so `solve2(A,marks) ≤ target ⟹ true
  value ≤ target` is a valid direction) but a "FAIL" as inconclusive
  (menu insufficiency, not necessarily a real counterexample) — this
  asymmetry is exactly what happened on the `T` witness and should be
  written up as a lemma once the general subset-matching menu extension
  is built, not before.

## `current.md` updates made

- Added a full Round-13 review block at the top of `## Status`,
  explaining the bug, its independent confirmation, and the retraction
  of Round 12's gate-PASS claim as evidence, with an explicit "do not
  cite" instruction for future rounds. Clarified WF-C5 is unaffected.
- Added Round-13 entries to `## Approaches tried` for both slugs,
  summarizing what each found, what I independently confirmed, and the
  precise (corrected) interpretation of the `T`-witness finding (menu
  insufficiency, not a HALF-BOUND refutation).
- Updated the "Open gaps" / Case C section with an explicit Round-13
  correction paragraph retracting the round-12 gate PASS, clarifying the
  `solve2`-vs-true-value asymmetry, and re-stating the sharpest concrete
  next target (the Hall-type subset-matching existence theorem for Lemma
  PAIR-VALUE, now confirmed unavoidable even in Case (a)).
- Overall `## Status` remains `partial` (Case C, general `m≥4`, is still
  the sole open gap for the whole problem) — no regression, but a
  significant, necessary correction to what evidence actually supports.

## Recommendation for round 14

Focus squarely on the Hall-type general subset-matching existence
theorem for Lemma PAIR-VALUE (flagged since round 9, now confirmed
unavoidable even in the "easy" Case (a)) — this is the actual crux, not a
bookkeeping detail. Any future numeric "gate" must use a properly
mark-capped model and must not treat a menu-restricted "FAIL" as a
genuine counterexample without first checking the true unrestricted
optimum (as both builders and I did this round). Do not resurrect the
round-12 gate-PASS claim in any form without first re-running it under a
correctly capped model.
