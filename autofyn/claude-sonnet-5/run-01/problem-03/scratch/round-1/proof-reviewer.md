# Proof review — imo-2026-03, round 1

Reviewed all three built approaches against `problems.jsonl` (imo-2026-03,
`task: compute_and_prove`, `answer_type: expression` — so a proof requires
both the closed-form answer stated and both directions, upper and lower
bound, proven), `CLAUDE.md`'s rigor rules, and independent computation
(Python: exact `Fraction` brute force of the alternating-claim game value,
and `scipy.optimize.differential_evolution` searches over Xiang Yu's cut
placements) to re-derive the load-bearing claims from scratch rather than
trust the write-ups.

Independent verification performed:
- Re-derived Lemma 1 (claiming-phase value = odd-rank sum) by brute-force
  backward induction vs. the closed form, 200 random trials, multisets of
  size 0–6, exact rational arithmetic — **no mismatches, confirmed correct.**
- Re-derived the `n=1` exact value function `V(p1,p2) = min(p1, p2+p1/2)`
  (claimed in `equalization-potential-bound.md`) by brute-force search over
  all of Xiang Yu's split choices — **confirmed exactly** (diff ~1e-16 over
  30 random configurations).
- Re-derived Proposition 4 (`recursive-embedding-induction.md`: Xiang Yu's
  explicit `n`-mark response against the geometric config `A_n` achieves
  `oddrank(B) = c(n)` exactly) by exact `Fraction` computation for
  `n = 1,...,6` — **confirmed exactly in every case.**
- Numerically searched (via `differential_evolution` over all ways to
  distribute Xiang Yu's marks and split points, `n=2` exhaustively via three
  strategy classes, `n=3` via full enumeration of mark-distributions across
  the 4 pieces) whether any Xiang Yu response beats `c(n)` against the
  geometric configuration `A_n`, and whether any non-geometric Liu Bang
  configuration achieves a higher guaranteed value than `A_n` (30 random
  configs tested for `n=2`) — **in every test, `c(n) = 2^n/(2^{n+1}-1)` held
  and was not beaten**, strong (though not itself a proof) confirmation the
  target answer is correct.

## 1. `geometric-dominance-construction.md`

**Verdict: CHANGES REQUESTED. True status: `partial`** (matches the
builder's own self-report — no overclaim here).

What is genuinely proven, checked line by line:
- **Lemma 1** (claiming-phase value formula) — correct; independently
  verified computationally (above). The write-up has one clunky moment
  ("wait, checking indices carefully...") but the underlying parity/rank-shift
  argument is sound and the conclusion matches brute force exactly.
- **Lemma 2** (top-piece domination, `p_1 = top > Σ(tail)`) — trivial,
  correct algebra (finite geometric series identity), re-verified by hand.
- **Proposition A** (`k=0` lower-bound sub-case: if Xiang Yu's cuts avoid the
  top piece entirely, `oddrank(B) ≥ top`) — the argument (no element of a
  nonnegative multiset can exceed the multiset's own sum, hence `top` is the
  unique max and rank shifts push `evensum(tail) ≥ 0` onto the bound) is
  correct and complete, no case-split needed. Genuinely a clean, non-trivial
  proof, not a restatement of the trivial fact it sounds like.

**The gap, precisely.** The "Missing Lemma" (top-touched sub-case, `k ≥ 1`
marks land inside the top piece, tail possibly also refined) is honestly
flagged as open — not proven, only supported by numeric search at `n=2`. This
IS the hard part of the lower bound (the `k=0` case is comparatively easy,
as the builder itself notes: for `n ≥ 2` it never gives a tight bound). Step
3 (the matching adversary strategy for an *arbitrary*, non-geometric Liu Bang
configuration — the upper-bound half `c(n) ≤ 2^n/(2^{n+1}-1)`) is not
attempted at all this round.

No hand-waving found beyond what's explicitly flagged as open. The "Consequence" claim that piece order along the stick doesn't matter is stated and briefly justified (correctly — claiming and cutting only ever act on the current multiset of pieces, not their spatial arrangement).

## 2. `recursive-embedding-induction.md`

**Verdict: CHANGES REQUESTED. True status: `partial`** (matches self-report).

What is genuinely proven:
- **Lemma 1** — same statement/proof as approach 1, independently re-derived;
  correct (computationally verified, see above).
- **Lemma 2, Lemma 3 (self-similarity)** — short, correct algebra; Lemma 3's
  claim that the tail of `A_n` is an exact scaled copy of `A_{n-1}` checks
  out by direct substitution.
- **Hand-check of "Lemma B" at `n=2`** — the exhaustive order-type casework
  (7 regions, 3 vacuous by contradiction, 4 non-vacuous all giving
  `oddrank ≥ 4/7`) is carried out in full and is correct; I independently
  re-derived the same minimum (`4/7`) via `differential_evolution` over the
  full continuous split space at `n=2`, matching exactly. This gate check is
  genuine, not rubber-stamped.
- **Proposition 4** (general-`n` exact-equality construction) — this is the
  approach's strongest new result: a clean, fully general (not just spot-
  checked) proof that Xiang Yu can always force Liu Bang down to exactly
  `c(n)` against `A_n`. I re-verified this by exact computation for
  `n = 1,...,6`, all exact matches. This is real, certifiable progress
  (already certified into `lemmas/geometric-configuration-facts.md`).
- **`k=0` sub-case of the general lower bound** — proven in full generality,
  essentially the same argument as Proposition A above (both approaches
  converged on the identical clean proof independently — good cross-check).

**The gap, precisely, same shared wall as approach 1:** the general `k ≥ 1`
lower bound (Xiang Yu splits the top piece by `k` marks *and possibly also*
refines the tail with the remaining `n-k` marks, for arbitrary `n` and `k`)
is not closed — only the `n=2`, `k=n` (tail untouched) special case is
hand-verified. The upper bound over arbitrary (non-geometric) `A` is
explicitly out of scope this round and untouched. This is honestly and
precisely stated in "Open gaps," not glossed over.

**Diversity note for the orchestrator:** both live constructive approaches
now sit on the *exact same* unclosed step (general interleaving-domination
for `k ≥ 1`, simultaneous tail-splitting). Per `CLAUDE.md`'s "shared-gap
plateau" guidance, if this persists past round 2–3, a genuinely different
framing (e.g. an explicit exchange/majorization argument treating the merged
multiset directly, rather than case-splitting on how Xiang Yu allocates
marks) should be introduced — not just another patch attempt on the same
casework shape.

## 3. `equalization-potential-bound.md`

**Verdict: CHANGES REQUESTED (revised down from the builder's implied
"settled dead end").** **True status: `partial`** — real, certifiable
structural progress (Lemma D, Lemma E), but the headline claim ("proved
impossible in general, with a complete argument") is **overclaimed**: it
rests on an unproven premise.

Lemma D (interior maximum of a linear functional forces it constant on the
polytope) and Lemma E (the ordered simplex `Δ_n` is `n`-dimensional and the
geometric point is a strict interior point, via the standard `V_k` vertex
description) are both re-derived by hand and are **correct, standard,
self-contained polytope facts** — no gap in either.

**The load-bearing step I re-derived myself and found broken:** the
impossibility chain is
```
c(n) = V(p*) ≤ Σw_i p*_i ≤ max_A Σw_i p_i = c(n)
```
which needs `V(p*) = c(n)` **exactly** (not just `≤`) to force every
inequality to equality and hence force `p*` to be a maximizer of the linear
functional, which is where Lemma D bites. The file asserts this fact is
"computed directly... not in dispute," citing "the other approaches' Lemma
2/3." But checking those approaches directly: Lemma 2/3 (top-piece
domination, self-similarity) do **not** establish `V(p*) = c(n)` — only
Proposition 4 (`≤ c(n)`, an explicit witness) and the `k=0` sub-case
(part of `≥ c(n)`, but not the full statement) are proven, and the general
`k ≥ 1` case of `V(p*) ≥ c(n)` is the **exact open gap** both other
approaches explicitly flag as unsolved this round. So the premise this
approach treats as "not in dispute" is, in fact, in dispute — it is the
central unresolved claim of the whole problem.

Concretely: if it turned out (hypothetically) that some clever Xiang Yu
`k≥1` strategy beats `c(n)` against `A_n`, i.e. `V(p*) < c(n)` strictly, the
equality chain above collapses and Lemma D no longer applies — the
"impossibility" argument would no longer even be well-formed. (My own
numerics strongly suggest `V(p*) = c(n)` is in fact true for `n=1,2,3`, so
the conclusion is very likely correct — but "very likely true premise" is
not the same as "proved," and `CLAUDE.md` explicitly requires distinguishing
proved from conjectured.)

This is a real gap, not a fatal flaw in the *mechanism*: Lemma D/E are sound
and reusable (certified), and once the shared `k≥1` gap is closed by either
of the other two approaches, this argument becomes a legitimate, fully
rigorous corollary establishing that no linear/LP shortcut exists. Until
then, the "confirmed dead end" claim should be read as conditional. I am
recording this as `partial` progress (a real, certified structural fact) with
an identified logical gap, rather than accepting the builder's stronger
"unconditionally settled negative result" framing.

The `n=1` exact value function `V(p_1,p_2)=min(p_1,p_2+p_1/2)` (full case
analysis of Xiang Yu's one cut) is independently re-verified by brute force
(above) and is correct — a genuinely useful, self-contained base case,
certified for reuse.

## Certified lemmas (written this round)

- `results/imo-2026-03/lemmas/claiming-phase-value.md` — Lemma 1, shared
  foundation of all three approaches, reviewer-verified by brute force.
- `results/imo-2026-03/lemmas/geometric-configuration-facts.md` — Lemma 2,
  Lemma 3, Proposition A, Proposition 4, all reviewer-verified.
- `results/imo-2026-03/lemmas/interior-point-linear-obstruction.md` —
  Lemma D, Lemma E, certified as standalone facts, with an explicit caveat
  attached documenting the open dependency flagged above.

## `current.md` updated

Overall population `Status: partial`. No approach reaches `solved` this
round; the two constructive approaches share one precisely-identified open
gap (general `k≥1` lower bound against the geometric config, plus the
entirely-untouched upper bound over arbitrary configurations), and the LP
approach's negative result is real but conditional on that same gap. See
`results/imo-2026-03/current.md` for the full write-up.

## Verdicts summary
- `geometric-dominance-construction` — CHANGES REQUESTED (Status: partial)
- `recursive-embedding-induction` — CHANGES REQUESTED (Status: partial)
- `equalization-potential-bound` — CHANGES REQUESTED (Status: partial;
  builder's "unsolved / confirmed dead end" framing is accurate on "does not
  solve the problem" but overclaims on "unconditionally confirmed" — the
  gap is that `V(p*)=c(n)` is assumed, not proven, in this round's population)
