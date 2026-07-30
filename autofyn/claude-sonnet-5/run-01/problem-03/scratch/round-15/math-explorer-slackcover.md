# Scouting report — Lemma SLACK-COVER (Case C, general m≥4)

Scouting only, per assignment — no proof attempted. Read `current.md` in
full, `approaches/universal-adversary-strategy.md` (rounds 8–14 in full,
including the "Round 14 build" section, lines ~2960–3280), `lemmas/pair-value.md`,
`lemmas/wf-c5.md`'s statement (via the file's own re-derivation), and the
crux corpus entries for `aimo-0063` (Hall-deficient-set-deletion) and
`aimo-0292` (strengthen-then-widen interval-covering induction).

## 1. Precise candidate statement for Lemma SLACK-COVER

The round-14 write-up correctly diagnoses that SLACK-COVER cannot be a
free-standing subset-sum covering lemma — it must be an inductive step
*inside* the same `(marks, |A|)` well-founded induction that `solve2`
already uses (Lemma WF-C5's order: lexicographic, `marks` primary). Here
is a precise statement compatible with that structure, phrased as the
exact inductive step the whole Claim PTBI induction needs at Case C:

**Lemma SLACK-COVER (candidate).** Let `A = (p_1 ≥ p_2 ≥ … ≥ p_m)` be
sorted descending, `m ≥ 2`, Case C (`p_1 < Σ(A)/2`), and let
`marks = m-1` (the real top-level budget). Write `T = tail(A)` (size
`m-1`). Then there exists a subset `S ⊆ T` (possibly empty; multiplicity
respected) with

```
cost(S) := |S| - [Σ(S) = p_1]      (the exact-tie boundary saves 1 mark,
                                     per the certified Lemma DOM-boundary-slack /
                                     PAIR-VALUE's SUBSET-DOM corollary)
```

such that, setting `r := p_1 - Σ(S) ≥ 0` and
`leftover := sort_desc((T \ S) ∪ ({r} if r>0 else ∅))` (size
`m' := (m-1-|S|) + [r>0] < m`, strictly smaller — this is the same
strict decrease already proved for Move 2 in Lemma WF-C5), we have

```
cost(S) ≤ marks   AND   Σ(S) + solve2(leftover, marks - cost(S)) ≤ c(m-1)·Σ(A).
```

That is: **some instance of the generalized (non-contiguous) Move 2 —
Lemma PAIR-VALUE's SUBSET-DOM corollary — by itself, closes Case C at
size `m`, given the strong induction hypothesis that `solve2` already
meets its target at every strictly smaller `(marks', |A|')` reached in
the well-order.** This is exactly a joint covering (existence of `S`)
+ recursive-value (the leftover's own `solve2` bound, invoked via IH)
statement, phrased so that "prove SLACK-COVER for size `m`" plugs
directly into "prove Claim PTBI for size `m`" via strong induction on
`|A|` (with `marks` always `= |A|-1` at any node reached by this specific
lemma's own recursive unfolding — note this is a *restriction* to the
"always spend the full budget" thread of the general `solve2` state
space, which is the thread Case C's construction actually needs; the
general well-foundedness proof for arbitrary `(marks,|A|)` pairs, already
proved, still applies to bound recursion depth).

A useful structural fact to attach to this statement (I derived and
spot-checked this arithmetic myself from the definitions above; it is
**not yet independently verified against `solve2`'s actual code output**,
so treat it as a lead, not a certified fact):

**Observation ("2-mark slack at the exact-tie boundary").** If the chosen
`S` hits `r=0` exactly (`Σ(S)=p_1`), then `cost(S)=|S|-1` and
`leftover`'s *own* natural top-level budget (if solved as an independent
instance of size `m'=m-1-|S|`) would be `m'-1 = m-2-|S|`, whereas the
marks actually available to it after paying `cost(S)` are
`(m-1)-(|S|-1) = m-|S|` — **exactly 2 more than its own "natural"
budget.** (In the generic `r>0` case, by contrast, `cost(S)=|S|` and the
marks left over, `(m-1)-|S|`, equal `leftover`'s natural budget
`m'-1=(m-|S|)-1` *exactly* — no slack.) If this arithmetic is confirmed
(a builder should re-derive it independently, e.g. against the
`(965,965,958,482)` witness where Move 0 fires — that is the `r=0`,
`|S|=1`-via-pre-existing-tie special case, giving `2` extra marks, matching
what round 14 reports: "leaving the sub-instance `(958,482)` with the
*full* `3`-mark budget" — the file's own account is consistent with a
"slack" interpretation, though it phrases it as Move 0 being free rather
than as this general phenomenon), it gives a concrete resource to spend:
whenever the natural exact-tie match slightly under-shoots what's needed,
there are 2 spare marks in the leftover recursion to spend on a
corrective secondary move (e.g., one extra Move-1 halving or Move-3
tail-snip beyond what the leftover's own naive IH-optimal path would use)
— this is a plausible mechanism for exactly the kind of "small correction"
the round-13/14 witnesses needed (e.g. `T=(0.20,0.15,0.12,0.08)`'s winning
construction independently halves `p_2=0.15` *in addition to* the
non-contiguous match, i.e. spends a second, independent move inside the
leftover — consistent with "slack being used," though this was not
derived from a `cost=2`-slack argument in the file, only observed
empirically).

## 2. Candidate proof techniques

**(a) A monotonicity-in-marks lemma, first (cheap, should be checked
before anything else).** Is `solve2(A, k)` non-increasing in `k`
(more marks never hurt Xiang Yu)? This should be nearly immediate: the
candidate set available at `marks=k` is not literally a subset of the one
at `marks=k+1` (different `k` may make different Move-2 costs newly
affordable), but every move legal at `marks=k` remains legal at
`marks=k+1` (the recursive call simply carries one more spare mark that
is never forced to be used — need to check `solve2`'s own base case /
menu never *requires* using all marks; from the `solve2` definition given
in the file, `min(candidates.values())` already includes the "do nothing
further" fallback `oddrank(A)` when no move's cost fits, so this should
go through by a straightforward induction on `|A|`). If proved, this
converts the "AND" in the candidate statement above into something much
easier to use: the IH only needs `solve2(leftover, marks-cost(S)) ≤
solve2(leftover, m'-1)` (i.e. spending *fewer* than leftover's own natural
budget is only counterproductive, never advantageous — actually the
inequality needed for the induction is the reverse: we want an upper bound
using the *available* marks, and by monotonicity `solve2(leftover,
marks-cost(S)) ≤ c(m'-1)Σ(leftover)` follows from the *strong IH at the
leftover's own natural budget* only when `marks-cost(S) ≥ m'-1` — this is
exactly where the "slack" observation in 1. matters: at the `r=0`
boundary there are 2 spare marks, i.e. `marks-cost(S) = m'+1 > m'-1`,
so monotonicity immediately gives the IH bound "for free" with margin to
spare; at the generic `r>0` boundary, `marks-cost(S)=m'-1` exactly, no
slack, so the plain IH suffices with no cushion). **This reframing turns
SLACK-COVER from "prove a covering+value AND" into "prove monotonicity
(cheap) + prove a pure covering existence statement (S exists with
`cost(S) ≤ marks` and `Σ(S) + c(m'-1)Σ(leftover) ≤ c(m-1)Σ(A)`)"** — the
second part is now a *scalar inequality in Σ(S) and the leftover's sum*,
not a recursive-value statement, which is a real simplification if
monotonicity holds. This is the single most promising concrete next step
for a builder to check first (cheap to verify numerically and to prove).

**(b) aimo-0292-style strengthen-and-widen induction, applied to the now
purely-algebraic covering statement from (a).** aimo-0292's technique
("strengthen the claim before inducting: replace the rigid boundary value
with an inequality and widen the free parameter's range," and "split the
achievable range into sums excluding vs. including the largest element,
shifted, so covering an interval reduces to two shifted copies
overlapping") transfers cleanly once the goal is the purely algebraic
statement in (a): peel the largest tail element `t_1=p_2`; the "exclude"
branch recurses with `S ⊆ T\{t_1}` on a smaller instance whose IH (by
induction on `m`) already supplies a valid `S`; the "include" branch
matches `t_1` and recurses on `T\{t_1}` with target `p_1-t_1` (needs the
IH generalized to *arbitrary* targets `p_1' ≤ p_1`, not just the specific
`p_1` of the original instance — this generalization, "widen the free
parameter," is exactly aimo-0292's move, and is the natural strengthening
to try: prove SLACK-COVER not just for `A`'s own `p_1`, but for the family
`{(p_1', T) : 0 < p_1' < Σ(T)/2\}` simultaneously, by induction on `|T|`).
The overlap condition then reduces to a single scalar gap check
(`t_1 ≤` some margin, playing the role of aimo-0292's `x_k ≤ (sum of
smaller blocks) + 2`), which is checkable directly from `t_1 ≤ p_1` (tail
elements are bounded by the max) combined with the `c(m-1)` recursion's
own algebraic identity `c(k-1)=c(k)/(2(1-c(k)))` (Lemma
THRESHOLD-REDUCTION, already certified) — this is the concrete place
`aimo-0292`'s crux move should be adapted (not cited) from scratch.
**This is the most concrete unexplored mechanism**; round 14's own
attempt at "the peel-largest-tail-element mechanism" got exactly this far
and stalled on "the value of the recursive leftover, not just its
achievable-sum coverage" — but that obstruction is precisely what
mechanism (a) above is designed to remove first. Try (a) before
re-attempting (b) as a value-only argument; if (a) succeeds, (b) becomes
a scalar induction, much more tractable than a value-aware one.

**(c) Exchange-argument fallback (if (a)/(b) stall).** The approach
already has a certified exchange-style argument (Fact 0's proof that
consecutive pairing maximizes sum-of-minima, via an "uncrossing" swap that
weakly improves) and Lemma TIE-NECESSARY (round 6, extremal-point
argument). A minimal-counterexample argument — take the `(marks,|A|)`-
minimal Case-C instance where no `S` satisfies the candidate statement,
and derive a contradiction by exhibiting an explicit exchange (swap one
element of a near-optimal `S` for another, using Fact-0's uncrossing
mechanism, generalized from "maximize sum of minima over a fixed multiset"
to "maximize sum of minima over a multiset with one free residual
`r=p_1-Σ(S)`") — is a second, structurally different lever from (a)/(b)
and worth keeping in reserve, since it reuses machinery already certified
in this same approach rather than adapting a fresh crux.

**Do not revisit:** non-constructive averaging/pigeonhole over the whole
Case-C family (proven dead 3 times: rounds 7–8, 11, 14) — anything
resembling "take an average bound over configurations and hope it beats
`c(m-1)`" is out. Also do not re-attempt "the mesh/covering bound alone"
(round 14 explicitly refutes this as insufficient with the
`(0.20,0.15,0.12,0.08)` witness) — any new attempt must engage the
*value* of the leftover, which is exactly what (a) is designed to make
tractable rather than avoid.

## 3. Is the m=8 non-termination a real obstruction, or implementation?

**Implementation, not mathematical**, with high confidence, for two
independent reasons:

1. The reference `solve2` script does an **exhaustive `2^{|tail|}`-subset
   search at every recursion level** (per the file's own description).
   Recursion depth can itself be `Θ(m)`, so the total work is not just
   `2^{m}` but closer to a *product* of per-level exponentials — a much
   worse blow-up than the raw `2^m` the "5-minute budget" framing suggests.
   This is a brute-force reference-checker design choice, not a fact about
   the underlying game.
2. **Memoization does not help this state space.** The recursion's states
   are `(marks, A)` where `A` is a real-valued (not small-integer) sorted
   tuple; after even one non-trivial split, the values in `A` are generic
   irrationals/awkward rationals that essentially never recur exactly
   across different branches of the exponential subset search. Memoizing
   on exact-value tuples therefore has a near-zero hit rate here — this
   explains why "memoization added" (round 14 explicitly reports trying
   this) still failed to terminate. A complexity fix via memoization alone
   is not promising; the real fix is algorithmic, not caching.

**Concrete algorithmic fixes for a future explorer/builder, in order of
effort:**
- **Do not brute-force subsets at all for a verification/witness check.**
  The round-12 explorer (`math-explorer-subsetmatch`) already *diagnosed
  the exact winning construction* for the `m=8` witness by hand: PARTIAL-
  DOM's ordinary contiguous prefix match (`S=\{p_2\}`, not any exotic
  subset — the brute-force-over-127-subsets search itself already showed
  the winning `S` is the trivial contiguous one) plus **one nested
  TAIL-SNIP inside the leftover's own recursion**. This is a fully
  explicit, short move sequence. Checking *this one candidate construction*
  by direct `Fraction` substitution is `O(m)` work, not `O(2^m)` — a
  builder should verify the `m=8` witness this way (evaluate the named
  construction directly) rather than re-running an exhaustive `solve2`
  search over it. This sidesteps the termination problem for that witness
  entirely and is consistent with "prove, don't (only) search" per
  CLAUDE.md's rigor rules.
- If a general proof needs to check many `m` values numerically (as a
  stress-test gate, not as the proof itself), restrict the candidate
  subset space searched to a **polynomial-size candidate family**: all
  contiguous prefixes (`O(m)` candidates, already what Lemma PARTIAL-DOM
  uses) plus "contiguous prefix with one element skipped near the
  boundary" (`O(m)` more candidates, motivated by every non-contiguous
  witness found so far — round 13's and round 14's witnesses both skip
  *exactly one* element, `0.15` in the `(0.20,0.15,0.12,0.08)` case).
  This turns the adversarial-gate stress test from exponential to
  polynomial per instance, and would likely let the `m=8` gate finish in
  well under a second instead of not terminating — worth implementing
  before the next gate run at any `m≥8`.
- If a genuinely general (not just bounded-skip) non-contiguous subset is
  ever needed at some larger `m`, that would be a real escalation in
  difficulty and worth flagging explicitly to the outliner as a new,
  sharper open question — but nothing on file yet demonstrates this is
  necessary; every witness found so far is closed by "prefix, or prefix
  skipping one element."

## 4. Concrete next steps for the proof-outliner

1. **Dispatch a builder to first prove/refute monotonicity of `solve2` in
   `marks`** (section 2(a) above) — cheap, and if true, immediately
   reduces the joint covering+value statement to a scalar covering
   inequality, which is a materially easier target than what round 14
   attempted directly. This should be step 1 of the next round's build,
   not the SLACK-COVER existence proof itself.
2. **Independently verify the "2-mark slack at exact-tie boundary"
   arithmetic** in section 1 against `solve2`'s actual code (not just my
   hand recomputation here) — if confirmed, it is a genuine new structural
   fact worth its own certified lemma name (e.g. Lemma EXACT-TIE-SLACK),
   reusable as the resource budget for whatever corrective move the
   induction ends up needing at the exact-match boundary.
3. **If (1) succeeds, attempt the aimo-0292-adapted peel-largest-element
   induction (section 2(b))** on the now-scalar covering statement — proved
   from scratch, not cited, per CLAUDE.md.
4. **For any numerical stress-testing at `m≥8`, do not re-run the
   exhaustive-subset `solve2` reference** — either hand-verify the
   already-diagnosed explicit construction (section 3, first bullet) or
   restrict the search to the polynomial candidate family (section 3,
   second bullet) so the gate actually terminates.
5. Keep `case-c-slack-covering`'s two certified lemmas
   (`lemmas/double-insert-match-value.md`,
   `lemmas/uniform-tail-margin-negative.md`) available as pruning facts,
   but do not revive one-level averaging in any new guise — three
   independent refutations (rounds 7–8, 11, 14) is conclusive for that
   mechanism specifically; the joint induction above is a genuinely
   different mechanism (constructive, not averaging), so it is not
   affected by that dead-end finding.
