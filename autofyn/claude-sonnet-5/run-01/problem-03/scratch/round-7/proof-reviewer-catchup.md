# Catch-up proof-review — imo-2026-03, round 6 (interrupted round, independent review)

Round 6 was interrupted before any review happened. Four builders edited their
approach files; only one report (`minimax-mixed-duality`) survived at
`/tmp/round-6/`. This review independently re-derives and verifies **all
four** updated approaches directly from the committed diff (`git show
108eee8`), with no reliance on the lost builder reports beyond the one that
survived (used only as context, not as ground truth).

## Verdicts

| Approach | Verdict | Status set |
|---|---|---|
| `recursive-embedding-induction` | **CHANGES REQUESTED** | `partial` (unchanged from round 5 — no proof this round) |
| `geometric-dominance-construction` | **CHANGES REQUESTED** (genuine milestone: Proposition K fully closed) | `partial` |
| `universal-adversary-strategy` | **CHANGES REQUESTED** | `partial` (one lemma proof needs a fix, doesn't invalidate the lemma) |
| `minimax-mixed-duality` | **CHANGES REQUESTED** | `partial` (first pass, real new lemma) |

None reach APPROVE — the overall problem (`c(n)=2^n/(2^{n+1}-1)`, both
directions, all configurations) is far from complete. None are RETHINK — every
one of the four either proved something correctly or (in
`recursive-embedding-induction`'s case) merely stalled without introducing any
false claim.

---

## 1. `recursive-embedding-induction` — CHANGES REQUESTED

**What the round-6 diff actually contains.** Checked via
`git diff 108eee8^ 108eee8 -- .../recursive-embedding-induction.md`: the only
change is a new section "Round 6 target: Lemma PARITY-PAIR-GEN (skeleton,
scoped to k=2 first)". It restates the target statement, sketches "Case A
(even tying block)" as already covered by prior Claim-★ work, and explicitly
labels "Case B (odd tying block)" — the actual new content needed — as **not
worked out** ("This is the genuinely open part"). No proof, no lemma, no
computation appears in the diff. The file's own top-of-file "Approaches
tried" bullet list was **not** updated to claim any round-6 result (consistent
with there being none).

**Assessment.** This is honest — nothing is overclaimed — but it is also not
progress: the "builder" for this slug (report lost) produced a plan, not a
proof. Since Lemma FC (see #2 below) now closes the *only* other open piece
of the `k=n` sub-case, this approach's Lemma PARITY-PAIR-GEN (`k<n`,
tail-refined) is now the single remaining piece of the entire lower-bound
gap. No regression, no error — but no advance either. `partial`, unchanged
from round 5.

---

## 2. `geometric-dominance-construction` — CHANGES REQUESTED (real milestone)

**Claim.** Round 6 proves the "one free coordinate" vertex case of Lemma V'
(`lemmas/lemma-V-prime-free-coordinate.md`), which — combined with the
already-certified Lemma L (pure-anchor case) and Lemma V' (vertex reduction)
— fully closes **Proposition K**: for every `n≥1` and every partition
`S=(s_1≥...≥s_{n+1}>0)` of `2t_1` into `n+1` positive parts, `D(S∪T)≥t_n`,
i.e. `oddsum(S∪T)≥c(n)`. This is the `k=n`, tail-untouched sub-case of the
lower bound.

**Independent verification performed.** I did not just read the proof; I
hand-computed two concrete instances at `n=3` (`t=(4,2,1)`, `2t_1=8`) from
scratch and checked every step of the argument against them:

- **`j=0` case** (`x` above the top anchor `t_1`): `a=(0,0,3)`, giving
  `x=5`. Direct computation: `S∪T` sorted `= 5,4,2,1,1,1,1`,
  `D = 5-4+2-1+1-1+1 = 3 ≥ t_3=1`. ✓. Checked the file's `D_0 - 2τ(r) +
  (-1)^{r+1}x` decomposition reproduces `3` exactly (`D_0=2`, `r=1`,
  `f(x)=x-D_0=5-2=3`). ✓. Checked the endpoint bound `f(t_1)=2≥1` via the
  incremented vector `a^{(1)}=(1,0,3)` (an `m=n+1=4` pure-anchor PARITY-PAIR
  instance) directly. ✓.
- **Interior-bracket case** (`1≤j≤n-1`): `a=(0,2,1)`, giving `x=3`,
  bracket `(t_2,t_1)=(2,4)`. Direct computation: `S∪T` sorted `=
  4,3,2,2,2,1,1`, `D=4-3+2-2+2-1+1=3≥1`. ✓. Checked the affine-interpolation
  claim: `f(t_1)=2`, `f(t_2)=4`, and `x=3` is the midpoint (`λ=0.5`) of
  `t_2,t_1`, so `f(x)` should `=0.5·4+0.5·2=3` — matches the direct
  computation exactly. ✓. Checked both endpoint values against their
  respective incremented pure-anchor vectors (`a^{(1)}=(1,2,1)`,
  `a^{(2)}=(0,3,1)`), confirming each is a valid `m=n+1=4` PARITY-PAIR
  instance with `n+m=7` odd (automatic, as claimed — no dependence on the
  dropped value constraint). ✓.

Every step of the proof mechanism (D-INSERT affineness on a fixed-rank
interval, snap-to-endpoint producing a genuine pure-anchor PARITY-PAIR
instance, convexity combining the two endpoint bounds, the integrality
argument ruling out the vacuous `(0,t_n)` bracket) checks out exactly on
both hand-worked examples. The proof composes only already-certified lemmas
(D-INSERT, PARITY-PAIR, V') with no new unproven machinery — this is a
clean, correct, complete argument for the stated claim.

**Minor note (not a defect):** in the `j=0` case-writeup, the phrase "`f(t_1)`
was established in Step 3" slightly overloads notation (Step 3's generic
bound is stated for `f(t_j)` and `f(t_{j+1})` at general `j`; for `j=0` the
relevant bound is the `f(t_{j+1})` one specialized to `j=0`, i.e. `f(t_1)` via
`a^{(1)}`). The substance is correct — verified above — the notation is just
slightly loose in one clause. Not a correctness issue.

**Verdict rationale.** This is a genuine, correct, complete closure of
Proposition K (both the pure-anchor part from round 5 and the free-coordinate
part from round 6) — analogous in significance to round 5's closure of
Lemma L. Recorded as a `verified-milestone` outcome in the ranker. The
approach remains `partial` overall since the tail-refined `k<n` case and the
general upper bound are out of its scope / still open.

---

## 3. `universal-adversary-strategy` — CHANGES REQUESTED

Two new lemmas, `lemmas/tie-necessary.md` (Lemma TIE-NECESSARY) and
`lemmas/partial-dom.md` (Lemma PARTIAL-DOM), plus a correction to the round-5
record about the `A=(4649,3042,2309)/10000` witness (superseded by
`minimax-mixed-duality`'s Lemma SANDWICH — cross-checked below, consistent).

### Lemma PARTIAL-DOM — verified correct, no issues found

Hand-checked the file's own headline example in full, exactly:
`A=(4859,3439,884,496,322)/10000`, `j=2`, budget `k=2`. Note this instance is
**budget-capped**, not domination-maximal: true domination would allow
`j=3` (`p_1=4859 ≥ S_3=4819`), but only `2` marks are available, so `j=2` is
used and `r=p_1-S_2=536 > U_1=496` — i.e. this example actually falls
**outside** the "`r<U_1`" scope the file's own Remark claims is required for
the certified formula.

- Direct construction: split `p_1` into `(3439,884,536)`, merge with full
  tail `(3439,884,496,322)`. Sorted: `3439,3439,884,884,536,496,322`.
  `oddrank` (ranks 1,3,5,7) `= 3439+884+536+322 = 5181`. Matches the claimed
  `5181/10000` exactly.
- Via the closed form: `D(B)=D(U)+(-1)^e[r-2D(U_{>e})]` with `U=(496,322)`,
  `e=0` (no `U_i≥r=536`): `D(U)=174`, `D(B)=174+536-2·174=362`. Then
  `oddrank=(p_1+Σ(T)+D(B))/2=(4859+5141+362)/2=5181`. Matches exactly.

So the formula is verified correct **even in the case the file's own Remark
says was "not separately written up or verified this round."** On inspection,
the actual requirement for the derivation (Step 2) is `r < t_j` (r stays
below the *duplicated block*, not below all of `U`) — here `r=536<t_j=884`,
so the derivation's real hypothesis holds fine even though `r>U_1`. This
means the Remark under-states the lemma's true scope (it should say `r<t_j`,
not the stricter `r<U_1`) — a minor imprecision in the write-up's stated
caveat, not an error in the certified lemma itself, and not something that
needs fixing before certification (if anything, the certified formula is
*more* general than claimed).

**Verdict: certify as-is; recommend a one-line correction to the Remark's
stated scope** (replace "`r<U_1`" with "`r<t_j`") for the next round, but this
is not blocking.

### Lemma TIE-NECESSARY — genuine flaw found in one proof branch; conclusion survives

The overall statement (any global minimizer of `oddrank(B)` can be taken to
satisfy condition (a) zero-length split or (b) an adjacent-rank tie) is true
and the main argument (Case 1: boundary point; Case 2, `dim(Q)≥1`: apply the
certified Lemma D to force `oddrank` constant on `Q`, then any boundary point
also minimizes) is sound and correctly uses the already-certified Lemma D.

**But the `dim(Q)=0` sub-case of Case 2 is argued incorrectly.** The proof
claims: "a 0-dimensional cell of a product-of-chain-simplices arrangement is
automatically a point at which every chain-simplex coordinate is pinned to an
anchor... forces every sub-piece to have length 0" — i.e. it asserts a
0-dimensional cell must arise from a collapsed *chain-simplex boundary*
constraint, unconditionally giving condition (a).

This is false in general. A cell `Q` is cut out by **both** chain-simplex
boundary constraints **and** order-tie constraints (adjacent-rank equalities).
A 0-dimensional cell can arise from `k` independent order-tie constraints
alone, with **no** chain-simplex boundary active — e.g., with 2 marks spent
inside a single piece `p_1` (a 2-dimensional polytope), two independent ties
(the first sub-piece ties `p_2`, and the third sub-piece ties `p_3`) pin the
polytope to a single point with **no** zero-length sub-piece anywhere — this
is a legitimate 0-dimensional cell satisfying only condition (b), not (a).

This does **not** invalidate the lemma's conclusion, because the lemma's
statement is a disjunction — "(a) **or** (b)" — and a pure-tie vertex still
satisfies (b). So the theorem as stated remains true; only the specific
justification offered for this one branch is incorrect (it over-asserts (a)
specifically, when only "(a) or (b)" is actually guaranteed). This is a real
rigor defect (an unjustified/false intermediate claim, contrary to the
CLAUDE.md "no hand-waving" rule) that should be fixed before the lemma is
treated as airtight, even though the headline statement survives.

**Verdict: keep certified (the true content — the disjunction — is
established by the sound parts of the proof: Case 1 covers all boundary
points, including pure-tie ones; the `dim(Q)=0` sub-case's own boundary is
itself just the point `Q=\{x^*\}$, so falling back on Case-1-style facet
reasoning directly also closes it correctly, without needing the incorrect
"must be (a)" claim at all). Recommend the next round rewrite the
`dim(Q)=0` paragraph to conclude "(a) or (b)" directly from the cell's
defining constraints (exactly as in Case 1, since a 0-dim cell's definition
already includes both constraint types) rather than asserting (a)
specifically.**

### Combining the two lemmas — no overclaiming found

The file correctly and precisely reports that TIE-NECESSARY + PARTIAL-DOM
together do **not** close the even-`m` "two-independent-ties" regime
(verified exact numeric example on `A=(0.3374,0.2589,0.242,0.1617)`, `m=4`:
the maximal PARTIAL-DOM chain gives no improvement over baseline, `0.5794`,
while the true optimum `≈0.5009` needs a non-contiguous matching). This is
consistent with `lemmas/partial-dom.md`'s own "What this does and does not
close" section. No overclaiming.

---

## 4. `minimax-mixed-duality` — CHANGES REQUESTED

New approach, first build pass. Reviewed the surviving builder report and
independently re-derived the headline result.

### Lemma SANDWICH — verified correct

Statement: for sorted `A=(p_1≥...≥p_m)`, `m` odd, `p_1<p_2+p_m`: splitting
`p_1` (1 mark) into `x∈(max(p_3,p_1-p_m),p_2)`, `y=p_1-x` gives
`oddrank(B)=p_2+p_3+p_5+...+p_m` exactly, independent of `x` in that range.

Checked on the exact witness `A=(4649,3042,2309)/10000` (`m=3`): hypothesis
`p_1=4649<p_2+p_3=5351` holds; interval for `x` is `(2340,3042)`. Picked
`x=2500` concretely: `y=2149`. Sorted `B`: `p_2=3042` (rank 1), `x=2500`
(rank 2), `p_3=2309` (rank 3), `y=2149` (rank 4, `m+1=4` even, excluded).
`oddrank(B)=3042+2309=5351=0.5351`, matching the claimed formula and the
file's stated value exactly. Also checked
`oddrank(B)-oddrank(A)=p_2-p_1=3042-4649=-1607`, and directly
`oddrank(A)=p_1+p_3=4649+2309=6958`, `6958-1607=5351`. Consistent.

This construction genuinely beats and supersedes the round-5
`universal-adversary-strategy` diagnosis that this exact witness needs a
2-piece coordinated move (it doesn't — 1 mark suffices via a different
single-piece move) — cross-checked and consistent with
`universal-adversary-strategy`'s own round-6 correction citing the same
value. Good cross-approach consistency.

### Honest scope

The file correctly reports (not overclaimed): the LP-duality/mixed-strategy
framing itself gave no shortcut over direct casework this round; even-`m` is
untested (explicitly flagged as inconclusive, not claimed either way); the
4-candidate menu `{DOM,HALVE,TAIL-SNIP,SANDWICH}` covers only ~74% of a
sampled `m=3` configuration space, with the remaining ~26% spot-checked
(not proved) to still satisfy the target via constructions not yet in the
menu.

**Verdict: genuine new lemma, no defects found, honestly scoped.**

---

## Summary of actions taken

- Recorded round-6 outcomes via `mcp__approach-ranker__record_outcome` for
  all four approaches (`recursive-embedding-induction`: `partial`;
  `universal-adversary-strategy`: `partial`; `minimax-mixed-duality`:
  `partial`; `geometric-dominance-construction`: `verified-milestone`).
- Updated `results/imo-2026-03/current.md`: rewrote all four "Approaches
  tried" bullets to reflect the true round-6 state (including the
  `recursive-embedding-induction` non-progress and the TIE-NECESSARY proof
  defect), and rewrote "Current best" / "Open gaps" / "Full proof" to
  reflect that **Proposition K is now fully closed** (Lemma L + Lemma FC),
  narrowing the entire lower-bound gap down to the single tail-refined
  `k<n` case (Lemma PARITY-PAIR-GEN, still only a plan, not a proof).
- Did **not** touch `lemmas/*.md` files themselves — TIE-NECESSARY and
  PARTIAL-DOM remain certified as filed (PARTIAL-DOM with a suggested, non-
  blocking scope-note correction; TIE-NECESSARY with a suggested, non-
  blocking proof-writeup correction for the `dim(Q)=0` branch). Both
  lemmas' actual mathematical content is correct and safe to build on.

## Recommendation for round 7

1. **The lower-bound gap is now entirely `Lemma PARITY-PAIR-GEN` (`k<n`,
   tail simultaneously refined)** — `recursive-embedding-induction`'s own
   target, still unattempted beyond a plan. This should be the top
   priority; Case B (odd tying block) of the round-6 skeleton is the
   genuinely hard part and needs a real builder pass, not another skeleton.
2. `universal-adversary-strategy` should fix the `dim(Q)=0` paragraph of
   `lemmas/tie-necessary.md` (low effort, does not change the lemma's
   truth) and correct `lemmas/partial-dom.md`'s Remark's stated scope
   (`r<t_j` not `r<U_1`).
3. `minimax-mixed-duality` and `universal-adversary-strategy` should
   coordinate: SANDWICH (odd `m`, single-mark) and PARTIAL-DOM/TIE-NECESSARY
   (any `m`, matching-based) are attacking the same menu-coverage gap from
   different angles — worth checking whether SANDWICH is itself a special
   instance of a more general tie-structure TIE-NECESSARY already predicts.
