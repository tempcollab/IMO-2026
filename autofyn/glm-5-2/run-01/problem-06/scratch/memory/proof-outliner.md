# proof-outliner role memory

Lessons learned (round 1, imo-2026-06).

## ALWAYS
- ALWAYS: verify the modulus empirically before committing a finite-state framing. The natural modulus for imo-2026-06 is NOT `∏_{p≤rad(a_1)}p` (periodicity mod that is FALSE) — it is `L = ∏(kernel primes)`, and `L` is always a multiple of `rad(a_1)` but strictly smaller than the all-small-primes product. The state must use L (the kernel product), which requires identifying the kernel (B1). (round 1)
- ALWAYS: when seeding a field, explicitly check whether the framings share one underlying gap (a "stabilization river"). If they do, include at least 1-2 routes that GAMBLE on avoiding that river via a different mechanism (compactness, injectivity, abstract-theorem-factorization), even if those are high-variance. (round 1)
- ALWAYS: distinguish "next multiple of rad(a_1)" (valid candidate) from "a_n + rad(a_1)" (NOT necessarily a multiple of rad(a_1), may be invalid). The clean bounded-diff lemma uses the former. (round 1)

## NEVER
- NEVER: claim "the set of primes dividing some a_n is finite" — for this problem it is FALSE (free-rider primes unbounded: every prime q divides some a_n that is also divisible by a kernel prime). The stabilizing object is the minimal-hitting-set family / kernel, not the full prime support. (round 1)
- NEVER: use "a_n + rad(a_1)" as the guaranteed-valid candidate — it is the next MULTIPLE of rad(a_1) strictly greater than a_n that is valid. (round 1)

Lessons learned (round 2, imo-2026-06).

## ALWAYS
- ALWAYS: when a "stabilization river" gap collapses to a single clean claim (here B1' = "the true greedy = the small-prime-only greedy"), re-examine whether the crux is really ONE mechanism or whether multiple DISTINCT mechanisms can attack that single claim. Single-claim ≠ single-mechanism: a field can still be a single-gap trap if every slug attacks the one claim via the same mechanism. Diversify the MECHANISM on the crux claim, not just the framing. (round 2)
- ALWAYS: before keeping a borrowed crux move (e.g. aimo-0678's min-of-failing-set monovariant + reduce-mod-lcm), verify the crux's load-bearing step transfers by testing the analog object empirically first (e.g. does the candidate monovariate `w_n = min{m>a_n : m∉B_n}` actually stay above `a_n+R`?); flag the slug as probe-and-retire-if-fails when the transfer is uncertain. (round 2)
- ALWAYS: when a route is folded/retired, record its ONE salvageable idea and which live slug already carries it (here König's "finite-state⇒eventually-periodic" = bounded-diff-finite-state's conditional spine) so the next outliner does not re-open it as "new." (round 2)

## NEVER
- NEVER: trust a monovariant on the minimal-hitting-set family `M_n` without testing it on the worst-case trajectory (here `a_1=385`: `|M_n|` rises 3→9 before falling; `#disjoint-pairs` rises 3→12 on step 1) — `(|M_n|, Σ|h|, #disjoint-pairs)` are ALL non-monotone under the greedy. The valid stabilization argument is the finite-universe pigeonhole over `P_R`, NOT a measure on `M_n`. (round 2)
- NEVER: let two spacing-mechanism slugs both ride on the same unproved covering-bound refinement without flagging the coupling — if the shared sub-move is refuted, both die together (re-creating the single-gap trap at the mechanism level). Flag the coupling explicitly for the reviewer. (round 2)

Lessons learned (round 3, imo-2026-06).

## ALWAYS
- ALWAYS: when retiring a slug whose name has become misleading (e.g. `hitting-set-monovariant` after the monovariant was dropped), prefer OPENING a fresh honestly-named slug that IMPORTS the certified salvage (closure lemma) over REVISING in place under the stale name — the ranker re-ranks every round so the Elo reset is cheap, and a misleading name misleads the reviewer. (round 3)
- ALWAYS: before grafting a "new lever" onto a live CHANGES-REQUESTED slug, check whether the lever is genuinely new or a re-label of the exhausted mechanism. The spacing/v_p/covering cluster is EXHAUSTED — re-advancing those slugs with the same mechanism is a no-op; route the new mechanism (cross-intersection / (W)-descent) through FRESH slugs and LEAVE the exhausted ones as certified-spine (their lemmas stay importable). (round 3)
- ALWAYS: when two sibling slugs share a sub-gap (here conjecture (W) = "every σ*-class has an R-smooth term", shared by `cross-intersecting-anchor` GAP A and `w-descent-rsmooth`), flag the coupling BUT keep both if they attack it by genuinely different mechanisms (stabilized-family cross-intersection vs per-term s-substitution descent) — two mechanisms on one sub-gap is acceptable diversity, not a single-gap trap. (round 3)
- ALWAYS: when an approach has TWO viable fillings of the SAME gap where one is independent and the other is coupled to a sibling's crux (here B2 path α depends on `cross-intersecting-anchor` GAP B, path β is independent), recommend a COPY twin so both run in parallel — the independent path is the fallback if the sibling's crux fails. (round 3)

## NEVER
- NEVER: claim the direct aimo-0030 size bound "`s > a_{j-1}`" (the R-smooth rewrite lands in the greedy window) for imo-2026-06 — it is EMPIRICALLY FALSE (`s ≤ a_{j-1}` in 0/33 counter-cases; the s-substitution NEVER gives a direct window contradiction). The contradiction must come from a late-arrival induction, not a size landing. (round 3)
- NEVER: claim "the first term of each σ*-class is R-smooth" — it is FALSE (counterexample `a_1=135`: class `{2,3}` first term `138=2·3·23`). The correct weak form is conjecture (W): every class has SOME (possibly late) R-smooth term. (round 3)
- NEVER: conflate "every `h∈M'_∞` hits `σ(a_1)`" with "`M'_∞` is pairwise cross-intersecting" — two sets can each hit `σ(a_1)` disjointly. Cross-intersection is strictly stronger and is the actual crux (B). (round 3)
