# Proof-reviewer — round 5 (imo-2026-03)

Build set reviewed: `geometric-dominance-construction`, `recursive-embedding-
induction`, `universal-adversary-strategy`, `potential-averaging-bound`. Every
load-bearing claim below was independently re-derived from scratch (not just
read) with exact `Fraction`/integer arithmetic in Python, not the builders'
own scripts, per standing memory rule.

---

## 1. `recursive-embedding-induction` — the headline claim: Lemma PARITY-PAIR / Lemma L

**This is the single most important claim of the round and I verified it in
full, independently, from scratch.**

Setting: `t_i = 2^{n-i}` (`i=1..n`), nonnegative integers `a_1,...,a_n`,
`c_i = a_i+1`, block-parity formula for the alternating sum `D` of the merged
sorted list of blocks. **Lemma PARITY-PAIR**: for `n+m` odd (`m=Σa_i`, no
constraint on `Σa_it_i`), `D ≥ t_n = 1`. **Lemma L** is the special case
`m=n+1` (`n+m=2n+1` always odd).

**Independent re-derivation performed:**
1. Wrote a from-scratch brute-force enumerator (exhaustive for `n=1..8`,
   `a_i` up to budget 6, plus random sampling `n=1..12`, 10,000+ trials per
   `n`) computing `D` by direct sort-and-alternate (not the block formula) and
   checking `D≥1` whenever `n+m` odd. **Zero violations, 1,000,000+ total
   trials.**
2. Independently re-derived the *case-split relation itself* — not just the
   final inequality — by building, for random `n,a`, the full list and the
   fresh-indexed remainder list (levels `n` and `n-1`), and checking
   `D = D'` when `c_1` even and `D = t_1 - D'` when `c_1` odd, against direct
   recomputation of both `D` and `D'` from their own definitions. **24,000
   trials, zero mismatches.** This confirms the mechanism the induction relies
   on (not just its numeric conclusion).
3. Hand-checked the algebra of both cases against the write-up: Case A's
   parity-transfer condition `(n-1)+m' = (n+m)-1-a_1` = odd−1−odd = odd
   (checks out); Case B's use of the already-certified Lemma D-BOUND
   (`0≤D(Y)≤max(Y)`, `n≥2` guarantees remainder nonempty) and the numeric
   chain `t_1-t_2=t_2≥t_n=1` for `n≥2` (checks out, `t_2=2^{n-2}` and equality
   exactly at `n=2`).

**Verdict on this claim: correct, complete, no gap.** This is a genuine proof
of Lemma L for every `n`, not a numerically-verified conjecture — the
write-up's own honesty about this (explicitly not claiming Lemma L as proved
in the round-3/4 sections, then explicitly claiming it as proved this round
with the new mechanism) matches what I independently confirmed.

**What this closes / does not close.** Combined with the already-certified
Lemma V' (vertex-reduction), this closes the "pure-anchor vertex" part of
Proposition K's `k=n`, tail-untouched sub-case, for every `n`. It does **not**
close: (a) Lemma V's "one free coordinate" vertex case (honestly flagged,
concrete not vague — a plausible extension is sketched but unverified); (b)
`k<n` with the tail simultaneously refined (unchanged, fully open); (c) the
upper bound (out of scope here).

**Overclaim check.** File's Status header says `partial` — correct, not
overclaiming (it does not claim the whole theorem, only Lemma L). The
"Round 5" section is explicit about the narrower remaining gaps.

**Verdict: CHANGES REQUESTED. Status: partial.** This is major, correct,
independently-verified progress (Lemma L closes a sub-case open since round
1), but the theorem as a whole remains open (items (a),(b),(c) above).

---

## 2. `geometric-dominance-construction` — exchange-move Lemma X and move-trap negative result

**Lemma X (exact effect of the elementary move `(+1,-3,+2)` on `D`).**
Re-derived from scratch symbolically (matching the write-up's own algebra,
which the file honestly notes needed an in-place correction during the
build) and independently verified: 10,000+ random exact-integer trials
(`n` up to 12, random legal move positions), comparing the predicted
`ΔD=(-1)^{a_{i-1}+1}(-1)^{C_{i-2}}t_i` against full direct recomputation of
`D` before/after. **Zero mismatches.**

**Move-trap claim (`n=5, a=(0,2,4,0,0), D=11`).** I independently
re-implemented the check from scratch: confirmed `a` is feasible
(`Σa_i=6=n+1`, `Σa_it_i=32=2t_1`), confirmed `D=11` by direct sort-and-
alternate, then exhaustively enumerated **all** `C(5,3)=10` index triples and
**both** directions of the elementary move at each (20 candidate moves
total), checking feasibility (all coordinates `≥0`) and `D`-value. **Result:
confirmed exactly — every legal resulting vector has `D≥11`, no strict
decrease. This is a genuine, exhaustively-verified move-trap, not a
sampling artifact.** Also confirmed the claimed width-2 escape
`(0,2,4,0,0)→(1,0,3,2,0)`, `D:11→7`.

**Is this "exhaustive, not sampled" as claimed?** Yes, confirmed — my
re-implementation used the same exhaustive `C(n,3)` enumeration
independently, not the builder's script, and matches exactly.

**Overclaim check.** The approach honestly reports this as a *negative*
result (the exchange mechanism does not work in bounded-width form) and
correctly imports Lemma L by reference from the sibling approach rather than
re-claiming it. Status header `partial` — correct.

**Verdict: CHANGES REQUESTED. Status: partial.** Genuine, rigorously verified
negative result (rules out an entire proof strategy, valuable for future
rounds) plus a correct, reusable exact identity (Lemma X); does not itself
close any part of the remaining gap, but is honest about that and correctly
coordinates with the sibling approach rather than duplicating its (now
successful) effort.

---

## 3. `universal-adversary-strategy` — Lemma DOM-boundary-slack, SPLIT, TAIL-SNIP, and the coordinated-split counterexample

**Lemma DOM-boundary-slack.** Trivial but correctly stated mark-counting fact
(`j` labelled parts from one piece cost `j-1` marks); no error found.

**Lemma SPLIT.** Re-derived and independently verified: 11,000+ random
exact-`Fraction` trials (`m` up to 8, random valid split index `i` satisfying
`a_i/2≥a_{i+1}`), comparing the two claimed closed forms (`i` odd / `i` even)
against direct computation of `oddrank(B)-oddrank(A)`. **Zero mismatches.**
Also confirmed the claimed reduction to the certified Lemma HALVE at `i=1`.

**Lemma TAIL-SNIP and its refuting counterexample.** Recomputed exactly:
`A=(4649/10000, 3042/10000, 2309/10000)`, `oddrank(A)=3479/5000`, TAIL-SNIP
value (split `a_3` in half) `= oddrank(A)-a_3/2 = 11607/20000 = 0.58035`,
compared against `c(2)=4/7≈0.571429`. **Confirmed: `0.58035 > 4/7`, an exact
violation, not a numerical artifact.** Also confirmed the "true optimum uses
1 mark, not 2" logic is consistent (not directly re-verified the specific
non-half two-piece optimum to full precision, since that computation is
explicitly non-load-bearing exploratory diagnosis, not a proof step — per
standing memory rule, decoration/diagnosis is not held to the same bar as a
load-bearing claim).

**Overclaim check.** Status header `partial` — correct; the file is explicit
that the "neither DOM nor HALVE" regime remains unresolved and that
TAIL-SNIP is refuted as a standalone fix, not silently papered over.

**Verdict: CHANGES REQUESTED. Status: partial.** Real, verified new general
lemma (SPLIT) plus a correctly-executed and honestly-reported negative result
(TAIL-SNIP insufficient) that sharpens, rather than closes, the known "near-
tied top two" obstruction from this round's explorer.

---

## 4. `potential-averaging-bound` — the feasibility-gate counterexample

**Independently recomputed the central counterexample exactly:**
`A=(1/3,1/3,1/3)`, `n=2`.
- `always-halve`, budget 2: round 1 gives `(1/3,1/3,1/6,1/6)`, `oddrank=1/2`;
  round 2 gives `(1/3,1/6,1/6,1/6,1/6)`, `oddrank=2/3`. **Confirmed exactly**
  (`2/3` matches the write-up).
- `cascade-DOM`/`cascade-HALVE`: at level 0 neither hypothesis fires
  (`1/3<2/3` for both DOM's `p_1≥S` and HALVE's `p_1≥2·max(T)=2/3`); falls
  through to `evenmin-cascade` on `(1/3,1/3)`, where the DOM-boundary
  equality `p_1'=S'=1/3` fires, giving `evenrank=1/3`; total `1/3+1/3=2/3`.
  **Confirmed by direct hand-check of the recursion, matches the write-up.**
- `2/3 > 4/7 = c(2)` — confirmed exactly (`2/3=14/21 > 12/21=4/7`).
- **The true optimum (1 mark, not 2): split one `1/3` into two `1/6`s,
  giving `(1/3,1/3,1/6,1/6)`, `oddrank=1/2 < 4/7`.** Confirmed exactly.

**Is "Status: partial" (not a dead RETHINK) the right call?** I agree with
the builder's self-assessment, with one caveat for next round. The
distinction from `majorization-smoothing` (which *was* correctly ruled
`RETHINK`/dead) is real: majorization-smoothing's Step 0 produced a
**structural mathematical proof** that the whole technique's premise (global
concavity of a min of an affine and a genuinely convex piece) is impossible
in principle, for *any* refinement. Here, only three *specific* natural
candidates were tried and refuted; the write-up's own "no candidate can work"
argument is a plausibility diagnosis (both named strategies are individually
forced above the bound, so no average of them can clear it), not a proof
that *no* simply-defined pair of strategies could ever work. That keeps this
at `partial`, not `RETHINK`, this round. However, the file's own honest
conclusion — that a genuine fix ("budget-aware" candidate) would necessarily
re-implement the same optimal-stopping decisions `universal-adversary-
strategy`'s casework already makes — means that if next round's attempt
lands in the same place (a "fix" that is really just a relabeled copy of the
sibling approach's casework), it should then be retired as duplicative per
CLAUDE.md's diversity rule, not kept alive as a near-copy indefinitely. I
flagged this explicitly in `current.md`.

**Promotable lemma check.** "Dual-objective shift under an untouched
dominant element" — checked, correct, short, general, no gap; certified (it
overlaps in mechanism with existing certified facts, noted in the lemma
file, but is a legitimately reusable standalone statement).

**Verdict: CHANGES REQUESTED. Status: partial** (matches the file's own
header, not downgraded to RETHINK this round — see caveat above for the
condition under which it should be downgraded next round).

---

## Summary of verdicts

| Approach | Verdict | Status |
|---|---|---|
| `recursive-embedding-induction` | CHANGES REQUESTED | partial (Lemma L now fully proved — major advance) |
| `geometric-dominance-construction` | CHANGES REQUESTED | partial (rigorous negative result, no net gap closure) |
| `universal-adversary-strategy` | CHANGES REQUESTED | partial (new lemma + sharpened negative result) |
| `potential-averaging-bound` | CHANGES REQUESTED | partial (feasibility gate correctly failed; not yet a dead end) |

No `APPROVE` this round — the theorem is not yet solved. No `RETHINK` this
round — every approach produced genuine, verified content (positive lemmas
or rigorous negative results), none is fatally broken as currently scoped
(though `potential-averaging-bound` is flagged as at risk of becoming
duplicative next round if its fix collapses into casework).

## Actions taken
- Updated `results/imo-2026-03/current.md` in full (Status, Approaches
  tried, Current best, open gaps) to reflect all four round-5 builds.
- Certified four new lemma files (all independently re-verified above):
  - `results/imo-2026-03/lemmas/parity-pair-lemma-L.md` (Lemma PARITY-PAIR,
    Lemma L — the round's headline result)
  - `results/imo-2026-03/lemmas/exchange-move-and-trap.md` (Lemma X, the
    move-trap negative result)
  - `results/imo-2026-03/lemmas/split-and-tail-snip.md` (Lemma
    DOM-boundary-slack, Lemma SPLIT, Lemma TAIL-SNIP, the TAIL-SNIP
    counterexample)
  - `results/imo-2026-03/lemmas/dual-objective-shift.md` (small general
    reusable fact)
- Called `record_outcome` for all four approaches: `recursive-embedding-
  induction` → advanced; `geometric-dominance-construction` → partial;
  `universal-adversary-strategy` → partial; `potential-averaging-bound` →
  partial.

## Notes for next round
- **The single biggest development this round is that Lemma L is now a
  fully proved theorem** — this closes a gap that has been open since round
  1 and should reshape the ranking. `recursive-embedding-induction`'s next
  natural target is the "one free coordinate" vertex extension (narrow,
  concretely scoped) and then `k<n` with tail-refinement.
- `geometric-dominance-construction`'s exchange-argument route to `k≥2` is
  now confirmed not to be a bounded-width shortcut; its unique remaining
  value is extending the doubling-family conjecture to `k<n` with the tail
  simultaneously refined, which needs a version of Lemma V' generalized to a
  variable (not fixed) tail — not yet attempted by any approach.
- `universal-adversary-strategy`'s "neither DOM nor HALVE fires" regime now
  has a precise, reproducible witness requiring a coordinated two-piece
  move; the natural next lemma to attempt is a "Lemma PAIR-SPLIT" (jointly
  optimizing two simultaneous half-splits), generalizing Lemma SPLIT.
- `potential-averaging-bound` should either find a genuinely non-duplicative
  "budget-aware" candidate next round, or be retired as duplicative of
  `universal-adversary-strategy` — do not let it linger as a near-copy.
- Both remaining halves (lower bound: `k<n` tail-refined; upper bound:
  coordinated two-piece regime) are now structurally similar again (both
  need to reason about *simultaneous* multi-piece adversarial moves, not a
  single dominant piece) — worth flagging to the next outliner as a
  potential unifying angle, as was done for the (now-resolved) `k=n` crux.
