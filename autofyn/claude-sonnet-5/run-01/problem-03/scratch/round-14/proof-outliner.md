## imo-2026-03

### Context recap (do not re-derive, just reuse)
Entire lower bound closed (Lemma TREE-BOUND-MULTICLUSTER, round 10). `m=3`
upper bound fully closed (round 9). The ONLY remaining gap for the whole
problem: Claim PTBI's Case C (`p_1<Σ(A)/2`) for general `m≥4`. Round 13
found and the reviewer confirmed a real mark-bookkeeping bug in the
certified `solve(A,budget)` recursion (Lemma WF-C5's termination itself is
fine, but the value function silently over-credited Xiang Yu one mark via
uncharged Move 3). Round 14's three explorers:
- **recursion-accounting**: built and ran a correctly-accounted
  `solve2(A,marks)` (single real-mark pool, every move charged). Confirmed
  non-contiguous subset-matching is genuinely needed, and — new finding —
  needed at *every* recursive level (traced explicitly on the `m=8`
  witness: the match fires one level down, after an ordinary contiguous
  match already happened, not at the top level). This means round 12's
  "subset choice was never the problem at m=8" finding was itself
  contaminated by the old accounting bug and should be treated as
  unverified.
- **hall-matching**: found no viable fixed/mechanical matching template
  closes Case C universally; found a clean new witness
  `A=(965,965,958,482)` (`m=4`) where the two top elements are *already
  exactly tied* and every tested template wastes marks halving them anyway
  — the correct response is "skip the free tie, spend the whole budget on
  the tail." This is a small, concrete, previously-missing zero-cost move.
  Also flagged `aimo-0292` (subset-sum *interval/slack-covering* induction,
  not Hall/SDR) as a closer structural analog than `aimo-0063`.
- **altframing**: 5th go/no-go check, confirmed STAY (casework/matching is
  correct); found the "extremal-config-interpolation" idea reduces exactly
  to the already-3×-dead `majorization-smoothing` (V is concave, not
  convex — max can sit in a polytope interior, no vertex-forcing argument
  exists) — do not re-open under any name. Flagged (but did NOT validate)
  an LP/weak-duality inequality-only idea as untested, not ready for a slug.

### universal-adversary-strategy: revise
Target: `max_A min_B oddrank(B) ≤ c(m-1)Σ(A)` for every Liu Bang
configuration `A` with `m` pieces, `m≥4`, in Case C (`p_1<Σ(A)/2`) — the
whole remaining upper-bound gap. (Recall: `m=3` and the entire lower bound
are DONE — do not re-touch.)

Technique: strong induction on `(marks, |A|)` (single real-mark counter,
lexicographic, `marks` primary — reusing the corrected well-foundedness
argument the recursion-accounting explorer gave, a one-parameter
simplification of certified Lemma WF-C5) via a corrected, fully
mark-faithful recursive value function `solve2(A, marks)`, combined with
an *inductive* (not one-shot) existence argument for the subset-match move.

Skeleton:
  1. **Rebuild the recursion with correct real-mark accounting.** Define
     `solve2(A, marks)` exactly per the recursion-accounting explorer's
     spec: ONE shared counter `marks`, initialized to `|A|-1` at the top
     level, decremented by the true physical cut-count of every move:
     - Move 0 (**skip-if-tied**, cost 0): if the current top `2k` elements
       already form `k` exact ties (`a_1=a_2, a_3=a_4,\ldots`), recurse on
       the untouched remainder with the FULL remaining budget, banking the
       tied pairs' contribution for free. This is the new move the
       hall-matching explorer's `(965,965,958,482)` witness shows is
       load-bearing and was missing from every prior certified menu
       (DOM/HALVE/TAIL-SNIP/PARTIAL-DOM/PAIR-VALUE all unconditionally
       spend a mark to *create* a tie; none checks for a pre-existing free
       one first).
     - Move 1 (halve `p_1`): cost 1 — as before (certified Lemma HALVE /
       SPLIT).
     - Move 2 (subset-match, possibly non-contiguous): for a subset `S`
       of the tail with `Σ(S)≤p_1`, cost `|S|` (`|S|-1` if the residual
       `r=p_1-Σ(S)=0` exactly, per certified Lemma DOM-boundary-slack) —
       by Lemma PAIR-VALUE (already certified, hypothesis-free, no
       contiguity needed).
     - Move 3 (tail-snip smallest element): cost 1, `|A|` odd, `|A|≥3` —
       as before (certified Lemma TAIL-SNIP / SPLIT).
     Mandatory gate before any proof attempt: re-run the adversarial
     search (`differential_evolution`, `m=4..14`) against `solve2` with
     the FULL menu (Moves 0-3) and confirm zero counterexamples to
     `solve2(A,|A|-1) ≤ c(m-1)Σ(A)` throughout Case C — by hand/tool
     verification, not assumed. — by `builder`/computational check.
  2. **Prove well-foundedness of `solve2`.** Single-counter measure
     `marks`, strictly decreasing on every move (Move 0 doesn't recurse at
     all on a strictly smaller `|A|` — it must be formalized as an
     immediate value return for the tied block plus one recursive call on
     the remainder at the SAME `marks` but smaller `|A|`, so termination
     needs the pair `(marks,|A|)` lex with `marks` primary, exactly as in
     WF-C5, NOT `marks` alone — the recursion-accounting explorer's claim
     that "termination is on marks alone" undersells Move 0's zero-cost
     recursion and must be corrected in the skeleton). — by adapting
     certified Lemma WF-C5's argument with the added Move-0 case.
  3. **Attack the subset-match existence question as an INDUCTION, not a
     one-shot claim, per the `aimo-0292` adaptation.** Reformulate: instead
     of requiring `solve2` to find one globally-existing exact subset
     `S⊆tail` with `Σ(S)=p_1` (or close via residual), prove a *slack*
     statement by induction on `|tail|`, mirroring `aimo-0292`'s
     "remove the largest element, split the achievable-sum range into
     'excludes it'/'includes it' shifted copies, show they overlap"
     mechanism:
     **Lemma SLACK-COVER (target statement to prove).** For any sorted
     tail `T=(t_1\ge\cdots\ge t_k)` and any target `p_1` with
     `0<p_1<\Sigma(T)`, there exists a subset `S\subseteq T` (possibly
     using the residual-boundary convention of Lemma DOM-boundary-slack)
     with `|Σ(S)-p_1|` small enough, and `|S|` cheap enough (in marks),
     that the resulting `solve2` value on the combined instance
     (matched block plus recursively-solved leftover, using the
     remaining budget) meets `\le c(m-1)\Sigma(A)`. Proof attempt: strong
     induction on `k=|T|` — peel off `t_1` (the largest tail element,
     mirroring `aimo-0292`'s "remove the largest block" step): either
     `t_1` itself, or a subset avoiding it, is affordable and closes the
     gap (excludes case); or matching `t_1` plus a sub-selection from
     `T\setminus\{t_1\}$ shifted by `t_1` closes it (includes case);
     show the two cases' achievable-value ranges overlap using the same
     "later elements are individually small relative to remaining total"
     argument `aimo-0292` uses, adapted from "hit every integer `r` in a
     window" to "achieve `oddrank\le` target within the recursively
     available mark budget." — this is the open gap; do not claim it
     proved, only give the precise reduction and the analogy to formalize.
  4. **Combine Steps 1-3 into the strong induction proving Claim PTBI's
     Case C**, structured on `(marks,|A|)`: base cases `|A|\le3` (closed —
     `m=3` fully solved, round 9); inductive step invokes Move 0 first
     (free ties banked), then Lemma SLACK-COVER (Step 3) to select the
     match, then the induction hypothesis on the strictly smaller
     `(marks',|A|')` leftover instance.
  5. State and verify the final answer `c(n)=2^n/(2^{n+1}-1)` is
     unaffected by anything in this round (already verified, round 1) —
     restate only as the closing sentence once Case C is closed, not
     re-derive.

Key lemmas (claim + mechanism):
  - **Lemma DOM-boundary-slack, Lemma PAIR-VALUE, Lemma TAIL-SNIP, Lemma
    HALVE/SPLIT** — all already certified, reused verbatim as Moves 1-3's
    justification; no re-proof needed.
  - **Move 0 (skip-if-tied) value identity** — because a pre-existing
    exact tie contributes its odd-rank value for free regardless of
    which copy is "nominally" odd (same tie-insensitivity mechanism as
    Lemma DOM's Step 1: two equal values split across adjacent ranks
    contribute the shared value to `oddrank` regardless of tie-breaking) —
    NEW, small, should be proved and certified this round (cheap, mostly
    a corollary of the existing tie-insensitivity argument already used in
    Lemma DOM/HALVE's proofs).
  - **Lemma SLACK-COVER** (the real open gap) — because (conjectured
    mechanism, adapted from `aimo-0292`) the achievable-value range of
    "exclude the largest tail element from the match" and "include it,
    shifted" overlap whenever the remaining tail elements are collectively
    small relative to what's left to cover — this is the load-bearing new
    idea to attempt, not yet proved.

Open gaps: Lemma SLACK-COVER (the existence argument) is the entire
remaining content of the whole problem. Also: prove the Move-0 value
identity and re-verify well-foundedness with Move 0 included (small but
must not be skipped, per the WF-C5 precedent of a subtle measure bug).

Cases to cover: within Lemma SLACK-COVER's induction, both the "exclude
largest" and "include largest (shifted)" branches must be shown to jointly
cover every possible target `p_1<\Sigma(T)`; do not assume WLOG one branch
always suffices without checking the boundary where neither individually
does (this is exactly the kind of gap `aimo-0292`'s original proof handles
via the overlap argument — re-derive it here, don't just cite it).

Watch out for: (a) do NOT reuse round 12's "the m=8 witness's winning
subset is the contiguous prefix" claim as settled — round 14's
recursion-accounting explorer showed it does not survive re-accounting;
re-verify from scratch under `solve2` before relying on any specific
witness's traced move sequence from before round 13. (b) the free-tie
Move 0 must be checked to not break well-foundedness (it's a zero-cost
move — confirm it strictly decreases `|A|` at the same `marks`, so
`(marks,|A|)` lex still works, exactly flagged in Step 2 above). (c) any
mark-count claim for a proposed construction must be sanity-checked by
literally counting cuts and confirming it never exceeds `|A|-1` (the
one-line check that would have caught the round-12/13 bug).

### universal-adversary-strategy-exact-tie: retire (no build this round)
Its assigned target (the sharper identity `solve_full(A)=Σ(A)/2` exactly
throughout Case C via Hall's-theorem/exact-cover) is now proved FALSE in
general (witness `A=(26,21,10)`, true value `31\ne28.5`) — a clean,
complete, reviewer-confirmed negative result, not a stuck gap needing
re-planning. Its only remaining potential content (re-deriving the
existence question for the weaker, correct target `\le c(m-1)\Sigma(A)`)
is now identical to `universal-adversary-strategy`'s own Step 3
(Lemma SLACK-COVER) — continuing to build it in parallel would just
duplicate that work under a different name (the same convergence failure
mode that killed `minimax-mixed-duality` and `case-c-secondary-
extremality`). Its two certified contributions (Lemma NONNEG-EXCESS, the
`m`-vs-`|A|-1` mark-cost fact) stay in the shared lemma cache, importable
by the primary approach if useful. Do not rebuild this slug without a
genuinely new mechanism distinct from Step 3 above.

### case-c-slack-covering: new
Target: the same whole-problem claim as `universal-adversary-strategy`
(Claim PTBI's Case C, general `m\ge4`) — a **genuinely separate attempt**
at Lemma SLACK-COVER itself, run in parallel as a second, independent
route to the single hardest remaining gap (justified per CLAUDE.md's
"copy when two viable ways exist for the same gap" — here the two ways are
(i) `universal-adversary-strategy`'s exact-subset-match-with-Move-0 route,
gap-filled by adapting `aimo-0292`'s specific overlap mechanism, vs.
(ii) reformulating the whole induction to avoid ever needing to *identify*
the optimal subset at all — an inequality-only argument).

Technique: **weak-duality / non-constructive existence**, avoiding
identifying the optimal matching subset. Instead of constructing a witness
subset `S` explicitly (as the primary approach's Step 3 does), bound
`solve2`'s value from above using an averaging/counting argument over
*all* affordable subsets simultaneously (a Markov/counting-style bound: if
the *average* value over some natural family of affordable matches already
meets the target, existence of at least one good one follows without
construction) — genuinely different proof shape from Step 3's explicit
overlap-interval construction, even though both attack the same lemma.

Skeleton:
  1. Fix Case-C `A`, tail `T`. Define the family `F` of "cheap" matches:
     all subsets `S\subseteq T` with `|S|\le` some budget-determined cap.
  2. Compute (or bound) the AVERAGE of `solve2`'s resulting value over a
     natural, easy-to-analyze sub-family of `F` (e.g. all size-`j` prefixes
     shifted by a free rotation, or all size-`j` subsets containing a fixed
     small pivot) — this is a finite, computable average, not the full
     `2^k` family, chosen to admit closed form.
  3. If the average over this sub-family is `\le c(m-1)\Sigma(A)`, at least
     one member of the sub-family achieves the target (pigeonhole on the
     average) — existence without construction. — by the standard
     averaging/pigeonhole principle (`knowledge_base.md`, extremal /
     double-counting techniques).
  4. If the average argument fails on some sub-family, try the next
     candidate sub-family (rotate the pivot, widen `j`) — this is where
     the real work is: finding an averaging family whose mean provably
     clears the bound. This is NOT guaranteed to exist; the mandatory
     first check is a numeric feasibility gate (compute the true
     average over 2-3 candidate families on the known hard witnesses —
     `A=(26,21,10)`, `T=(20,15,12,8)`, `m=8` witness, `(965,965,958,482)`
     — BEFORE any proof write-up) exactly per the standing "mandatory
     numeric gate before commit" rule.

Key lemmas (claim + mechanism):
  - **Averaging-existence lemma (to attempt)**: if `E_{S\in\text{family}}
    [\text{solve2-value}(S)]\le c(m-1)\Sigma(A)`, some `S` in the family
    achieves `\le` the average — because the minimum of a finite set is
    `\le` its mean, elementary pigeonhole, no new machinery.
  - The real content is finding/computing a *provably-clearing* averaging
    family — this is the open gap, symmetric in difficulty to Lemma
    SLACK-COVER but via a structurally different (non-constructive)
    mechanism.

Open gaps: the entire lemma (no averaging family has been shown to clear
the bound yet — this slug starts from the numeric feasibility gate, not
from a half-finished proof).

Cases to cover: none yet (gate-first).

Watch out for: the SAME failure mode that killed `potential-averaging-
bound` (round 5) — averaging over budget-blind, fixed candidate
strategies that ALL individually overshoot cannot produce an average
below target. The averaging family here MUST include Move 0 (skip-if-
tied) as an option, or it will provably fail on the `(965,965,958,482)`
witness exactly as every fixed template did in round 14's hall-matching
report. Run the numeric gate against that exact witness FIRST — if the
averaging family that includes Move 0 still fails there, this whole
approach should be downgraded/retired quickly (do not sink further rounds
into it without an early positive signal), per the round-11
convergence-failure precedent (`case-c-secondary-extremality`,
`minimax-mixed-duality`).
