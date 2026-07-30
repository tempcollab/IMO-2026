# Outline review — round 16 (imo-2026-03)

## universal-adversary-strategy (revise): peel-vs-halve two-branch closure of m=4 Case C

**Verdict: RETHINK.** The core Step 4 claim — "min(Strategy A, Strategy B),
each recursing into the already-proved exact m=3 theorem, closes Case C
for m=4 via a bounded ≤4-way algebraic case split" — is **false**, refuted
by an exact-`Fraction` counterexample constructed and hand-verified below.
This is not a nitpick on write-up quality; the outline's central mechanism
for this round does not work, so Step 4 cannot be built as planned. Do not
dispatch a builder on this outline; send it back to the outliner.

### 1. Citation check: Strategy A's cited lemma has the wrong (over-strict) hypothesis, but the underlying identity is still true — for the right reason

Lemma BLOCK-RECURSE, as literally certified (`lemmas/block-recurse.md`),
requires (for `j=1`) `r := p_1-t_1 < t_1`, i.e. `p_1<2t_1`. Case C alone
(`p_1<Σ(tail)`) does **not** guarantee this — e.g. `A=(2.9,1,1,1)` is Case C
(`2.9<3`) yet `p_1=2.9≥2=2t_1`, violating BLOCK-RECURSE's stated hypothesis.
I hand-verified that the peel identity `oddrank(B)=t_1+oddrank(W)` still
holds numerically even when `r≥t_1` (checked `A=(2.9,1,1,1)` directly: both
the literal merged-multiset computation and the formula give `3.9`,
matching). The reason: BLOCK-RECURSE's `j=1` case is exactly a special
case of the *already-certified, genuinely hypothesis-free* **Lemma
DOUBLE-INSERT** (`lemmas/double-insert.md`) — inserting the duplicate pair
`{t_1,t_1}` into *any* list `W` (not just one satisfying `r<t_1`) shifts
`oddrank` by exactly `+t_1`, unconditionally. So Strategy A's identity is
correct as an unconditional fact, but the outline's citation is wrong: it
should derive Strategy A directly from DOUBLE-INSERT (`v=t_1`, `T=W`), not
from BLOCK-RECURSE `j=1`, whose own stated hypotheses do not cover the full
Case-C range. **This is a fixable citation error (CHANGES REQUESTED-level
on its own)** — flag it for whichever round revisits this plan.

### 2. Fatal flaw: the outline's own description of "the exact m=3 theorem V_3" is incomplete, and even after correcting it, min(StratA,StratB) genuinely fails on a Case-C m=4 witness

The outline states `V_3(X) := min(TAIL-SNIP(X), BLOCK-RECURSE_1(X))` if `X`
is Case C, **else Lemma DOM(X)**. This 2-branch description omits **Case
A** of the certified `lemmas/ptbi-threshold-reduction.md` (`p_1≥c(m-1)Σ`:
peel-half+IH), which is essential — DOM alone is only valid in the middle
band `Σ/2≤p_1<c(m-1)Σ`; for `p_1≥c(m-1)Σ` DOM's achieved value (`=p_1`)
can badly exceed target. I confirmed this is load-bearing: using the
outline's literal 2-branch `V_3`, the witness `A=(990,989,502,8)/17-scale`
(`m=4`, Case C: `990<989+502+8=1499`) gives `min(StratA,StratB)=1484 >
target=c(3)·2489=19912/15≈1327.5` — a large, spurious "violation" caused
purely by the outline's incomplete `V_3`. Once `V_3` is corrected to the
**true 3-case theorem** (Case A/B/C, per `ptbi-threshold-reduction.md`),
this specific witness resolves fine (`StratA=1245≤1327.5`).

**However, even with the fully-corrected, 3-case `V_3`, I found a genuine,
exact counterexample where BOTH Strategy A (in every single-tail-element
variant: matching `p_1` to `t_1`, `t_2`, *or* `t_3`) and Strategy B fail:**

```
A = (1859, 931, 619, 611)   [sorted desc, Case C: 1859 < 931+619+611 = 2161]
Σ(A) = 4020,  target = c(3)·Σ = (8/15)·4020 = 2144   (exact)

StratA (match p1 to t1): leftover (928,619,611), V3 = 1230 (Case C, BLOCK-RECURSE_1)
  → StratA = 931 + 1230 = 2161  >  2144   (margin -17, exact)
StratA (match p1 to t2): value = 2161  (same, exact)
StratA (match p1 to t3): value = 2161  (same, exact)
StratB (halve p1):        leftover (931,619,611), V3 = 1230
  → StratB = 1859/2 + 1230 = 4319/2 = 2159.5  >  2144   (margin -15.5, exact)
```

All computed with exact `fractions.Fraction` arithmetic (no floating-point
involved) — reproducible via `/tmp/stress_m4_v2.py` and
`/tmp/stratA_general.py` in this container. A `scipy.optimize.
differential_evolution` search over the *true*, fully general 3-mark
game (enumerating which of the 4/5/6 current pieces gets split at each of
the 3 steps, with continuous split ratios) found the **true optimal value
is ≈2014, comfortably under the target 2144** — so Claim PTBI itself is
NOT violated here; only the outline's specific peel-vs-halve construction
fails to reach it. Tracing the winning strategy shows it splits a **tail
element** (`t_2=619`) to nearly-tie it with another tail element
(`t_3=611`) — i.e. it needs exactly the kind of **non-contiguous
tail-internal subset match** that Lemma SLACK-COVER (open since round 9,
proven unavoidable at `m=6` in round 15) supplies, not anything in the
peel/halve menu.

**Consequence:** the outline's central premise — "`m≥6` needs SLACK-COVER,
but `m=4` is closeable purely via peel-vs-halve + the certified `m=3`
theorem, no new existence question" — is **false**. `m=4` also needs at
least a bounded, tail-internal matching move; a genuinely new (if smaller,
possibly tractable) piece of content, not the "elementary algebra in
`p_1,t_1,t_2,t_3`" Step 4 promised. This is a load-bearing, pre-build catch
exactly of the kind this run's discipline (rounds 11, 12) has caught
before — the builder would have spent a round discovering this the hard
way otherwise.

### 3. What to tell the outliner next round

- Do not resubmit "peel-vs-halve alone closes m=4" — refuted by the exact
  witness `A=(1859,931,619,611)` above; record this as a **new dead end**
  for the whole-menu-avoids-SLACK-COVER framing at `m=4` specifically (it
  was previously known to fail only at `m=6`).
- A viable next step: since `m=4`'s tail has only 3 elements, the needed
  "tail-internal match" content may be **much smaller than general
  SLACK-COVER** (only finitely many candidate 2-of-3 or 3-of-3 tail
  matches, not an arbitrary subset-sum existence question) — worth
  attempting a bounded closed-form extension of `V_4` that also tries
  "tie `t_i` to `t_j` directly (no `p_1` involvement), then recurse on the
  remaining 2-element residual + `p_1`" as a third/fourth candidate
  strategy, reusing the already-certified DOUBLE-INSERT machinery. This is
  a legitimate, scoped next attempt — not a re-hash of the still-fully-open
  general SLACK-COVER question, but it does mean this round's promised
  "no new existence question" framing was wrong and must be corrected.
- Separately (independent of the above), fix the Strategy A citation
  (§1): derive it from Lemma DOUBLE-INSERT directly, not from
  BLOCK-RECURSE `j=1`, whose certified hypotheses don't cover full Case C.

## recursive-embedding-induction (advance, no new work)

**Verdict: APPROVE** (trivial). This is a pure Elo/no-op nomination for the
already fully-proved, certified lower bound (Lemma TREE-BOUND-MULTICLUSTER,
round 10) — out of scope for Case C, nothing to check, no regression risk.
No build needed this round (nothing to prove; re-verifying an already
gap-free, previously exhaustively-reviewed theorem burns a builder round
for zero new signal).

## Diversity note

The field is currently a single active line (universal-adversary-strategy)
attacking the sole open gap, plus one fully-closed sibling kept for Elo
bookkeeping. This round's finding reinforces, rather than changes, the
standing diagnosis: Case C (general `m≥4`) fundamentally needs some form of
tail-internal non-contiguous matching, now confirmed necessary even at the
smallest previously-hoped-avoidable case (`m=4`). If the next 1-2 rounds
also fail to make progress on a *scoped* (not general) `m=4` matching
argument, CLAUDE.md's diversity mandate should be invoked — a genuinely
different framing (not just another move added to the same menu) should be
opened, since the field has been circling this exact wall (contiguous menu
insufficiency) since round 9.

## Ranking

Compared `recursive-embedding-induction` (fully closed, gap-free, no
regression) against `universal-adversary-strategy` (still-open scope, this
round's specific plan refuted by an exact counterexample) as a **draw** —
both remain legitimate, valuable population members; the comparison only
clears staleness and lets Elo track relative completeness, not a real
head-to-head this round since no build occurred. No new approaches to
register this round (no new slug opened; the outliner's plan for
universal-adversary-strategy is rejected pre-build, so no
new/revised-and-approved content exists to register).

## build set: (none this round)

universal-adversary-strategy's outline is RETHINK — sent back to the
outliner with the concrete counterexample and the suggested scoped-matching
direction above. recursive-embedding-induction needs no rebuild (already
fully closed, no regression risk, confirmed by this review without
needing a builder). No approach is ready to build this round.
