## Status
partial

*(Round 17 review — HEADLINE: `m=4` Case C is now FULLY CLOSED, hence
Claim PTBI is fully proved for `m=4`. Whole problem remains `partial`
only because general `m\ge5` is still entirely open (untouched this
round) — no overclaiming.

**`universal-adversary-strategy` (round 17 build, Region 3 closure).**
Independently re-verified from scratch (fresh Python, exact
`fractions.Fraction`, several independently-written scripts, plus an
adversarial `scipy.optimize.differential_evolution` search on the true
recursive (non-closed-form) functions):

- **Lemma V3-CLOSED-FORM** (`lemmas/v3-closed-form.md`): every branch of
  `V_3` is a min of `\le2` affine pieces — in particular Case C collapses
  to `V_3=\min(x+z/2,\,y+z)` with the `L_2`-sub-branch dependence
  cancelling exactly. I independently reproduced the two-line proof by
  hand (both `L_2` sub-branches checked to give the *other* outer-min term
  exactly, not just a bound) and confirmed it computationally against the
  original recursive `V_3`/`L_2` definitions over 200,000 random triples:
  **zero mismatches.** Correct, and reusable.
- **Lemma A-BASE-NOT-CASE-A** (`lemmas/m4-region-c-closure.md`):
  `\mathrm{StratA}`'s base triple `\{t_2,t_3,p_1-t_1\}` is never in
  `V_3`-Case-A on Region 3. I independently re-derived both sub-case
  chains of inequalities by hand (they check out algebraically exactly as
  written) and confirmed computationally over 300,000 Region-3 trials:
  **zero violations.**
- **Exact (non-loose) closed forms for `\mathrm{StratA}`,
  `\mathrm{StratB}`, `\mathrm{StratC}_{23}` on Region 3** — I independently
  re-implemented all three closed forms from the write-up and checked them
  against the original recursive definitions over 400,000 Region-3 trials:
  **zero mismatches** (exact equality, not merely an upper bound). Also
  independently reproduced the genuine `\mathrm{StratB}$-alone
  counterexample `A=(136,100,70,70)` (`\mathrm{StratB}=203>3008/15\approx
  200.53`) — confirming `\mathrm{StratB}` really is insufficient alone, so
  the 3-strategy `\min` is load-bearing, not decorative.
- **The foundational Region-1/2/3 partition (round 16's Step 2a: tail
  never `V_3`-Case-A when `t_1<\tfrac4{15}\Sigma`)** — re-checked this
  round since Region 3's validity depends on it: 200,000 trials, zero
  violations.
- **Regime I dominance** (`\mathrm{StratC}_{23}\le\mathrm{StratA}` whenever
  `a<c`) — independently confirmed, zero violations over 7,636 sampled
  Regime-I trials.
- **All 5 LP-vertex-cell table values reproduced exactly** with
  `fractions.Fraction`, including membership/boundary-exclusion: Cell I
  vertex `(20,12,11,2)`, slack `1$, correctly excluded (on the
  `t_1=\tfrac4{15}\Sigma` boundary); `\mathrm{II_a}`+C23-B vertex
  `(12,6,5,2)`, slack `1/3`, interior; `\mathrm{II_a}`+C23-A vertex
  `(8,4,3,2)`, slack `1/15`, interior (the known all-5-tie witness);
  `\mathrm{II_b}`+C23-B vertex `(6,4,3,2)`, slack `0`, correctly excluded
  (Region-1/3 boundary, already closed with equality by Region 1);
  `\mathrm{II_b}`+C23-A vertex `(8,5,4,3)`, slack `1/6`, interior. All
  exact, all match the write-up's table to the fraction.
- **Global adversarial check**: a 30-restart
  `scipy.optimize.differential_evolution` search directly on the true
  recursive `\min(\mathrm{StratA},\mathrm{StratB},\mathrm{StratC}_{23})`
  vs. `c(3)\Sigma`, penalized to stay in Region 3, found minimum slack
  `\approx-2\times10^{-16}` (floating-point zero — no violation),
  converging exactly to the normalized point `(0.4,0.267,0.2,0.133)
  \propto(6,4,3,2)`, matching the algebraic proof's own tight boundary
  point exactly. No counterexample found anywhere in Region 3.

**No gaps, sign errors, or skipped cases found.** The trichotomy
(`a<c`, `a\ge t_2`, `c\le a<t_2`) is exhaustive and (up to a harmless
shared boundary point) disjoint, using only the elementary fact
`0\le c\le t_2`; each of the resulting 5 cells is a genuine rational
polytope on which every candidate is affine, and the claimed LP optimum
at each cell's vertex is `\ge0` (checked exactly). Combined with the
already-independently-verified round-16 closure of Region 1 `\cup`
Region 2 (`lemmas/m4-region-a-region-b.md`, re-cross-checked this round
for partition consistency, no regression), **`m=4` Case C is fully and
rigorously closed**, and with it Case A/B (already closed via
`lemmas/ptbi-threshold-reduction.md`), **Claim PTBI is fully proved for
`m=4`.** `\mathrm{StratC}_{12}`/`\mathrm{StratC}_{13}` are proved (not just
observed) dispensable throughout `m=4` Case C.

**Verdict: CHANGES REQUESTED** (per the file-contract routing: this is a
`verified-milestone`, but the *approach's* own ultimate target is the whole
problem, which is still `partial` since general `m\ge5` — in particular
Lemma SLACK-COVER's proved-necessary-at-`m\ge6` non-contiguous subset
matching machinery — is completely untouched this round, honestly not
attempted, not claimed). This is major, certified progress: the entire
`m=4` case of Claim PTBI, which had been the run's focus since round 12,
is now closed in full.

**`vertex-reduction-on-adversary` (round 17, scoped feasibility check).**
Builder's honest-negative-result self-assessment independently confirmed
correct: for Region 1/2, the vertex/LP framing is a faithful but purely
notational restatement of `lemmas/m4-region-a-region-b.md` (same
monotonicity argument, same boundary arithmetic dressed in polytope-vertex
language) — it produces zero new inequalities and closes zero new
territory; its one genuine contribution (the "nested vertex, not flat
vertex" observation, correctly showing `(6,4,3,2)` is the intersection of
an outer facet with an *inner* recursive cell's own extremal vertex, not a
vertex of one flat LP) is a valid structural refinement, not new leverage.
For Region 3/general `m`, the report is correctly inconclusive rather than
falsely optimistic: no argument is given (or found) that the nested-cell
count stays small as the recursion deepens, so the approach would have to
carry out essentially the same casework `universal-adversary-strategy` did
directly — and this same round, Region 3 *was* closed directly by that
route (see above), independently confirming the vertex framing supplied no
shortcut. This is not stale or missing a real opportunity; it is a
correct, well-scoped negative result. **Verdict: RETHINK** — no
independent proof leverage found in either the closed (Region 1/2) or
still-relevant-in-principle (Region 3/general `m`, now moot for Region 3)
parts of its scope; any future revival needs a genuinely different
collapse argument (e.g. a proof the cell count stays polynomial, not
exponential), not a relabeling of existing casework.

**Current best (updated this round): `m=4` Case C is fully and
unconditionally closed — Claim PTBI is fully proved for `m=4`.** General
`m\ge5` remains the sole open gap for the whole problem (Lemma SLACK-COVER
proved necessary at `m\ge6`, round 15; the `m=4`-specific 5-(now
3-)strategy menu used here does not obviously generalize, since the number
of tie-strategies needed appears to grow combinatorially with `m`, per both
this round's and round 17's explorer notes). Overall Status remains
`partial`, not `solved`, pending general-`m` progress.)*

*(Round 16 review — CHANGES REQUESTED for `universal-adversary-strategy`
(the sole slug built this round; `recursive-embedding-induction` was
advanced unchanged by the outline-reviewer, no build, no regression, no
review needed). Whole problem remains `partial`; Case C for general
`m\ge4` is still the sole open gap. **This round targeted `m=4` Case C
specifically** (the round-16-v2 outline's `\le15`-way case split of the
5-strategy menu `V_4(A)=\min(\mathrm{StratA},\mathrm{StratB},
\mathrm{StratC}_{12},\mathrm{StratC}_{13},\mathrm{StratC}_{23})`) and made
real, fully rigorous partial progress, independently re-verified from
scratch (exact `fractions.Fraction`, ~300,000 random Case-C trials, plus a
complete hand re-derivation of every algebraic step, not just a numeric
re-run):

- **Lemma V3-BOUND** (re-derivation of the already-certified round-9
  "`m=3` solved in full" result as a clean, unconditional inequality
  `V_3(x,y,z)\le c(2)(x+y+z)` for every sorted triple) — re-derived
  independently branch-by-branch (Case A via `ptbi-threshold-reduction.md`'s
  own monotonicity argument at `m=3`, Case B trivial, Case C the already
  fully-certified round-9 closure) and confirmed with 200,000 random-integer
  trials, zero violations. **Certified**, `lemmas/v3-bound.md`.
- **Lemma m=4-REGION-A/REGION-B**: a genuine, algebraically exact (not
  numerically-fitted) two-region partition-and-closure of part of `m=4`
  Case C. Region 1 (`t_1\ge\tfrac4{15}\Sigma`): `\mathrm{StratA}\le
  \tfrac47\Sigma-\tfrac{t_1}7`, strictly decreasing, hitting `c(3)\Sigma`
  exactly at `t_1=\tfrac4{15}\Sigma` — I independently re-derived this
  affine bound by hand and confirmed it is *exactly* tight at the known
  extremal witness `A=(6,4,3,2)` (`\Sigma=15`, `t_1=4=\tfrac4{15}\cdot15`,
  `\mathrm{StratA}=8=c(3)\cdot15` exactly, reproduced independently).
  Region 2 (`t_1<\tfrac4{15}\Sigma` and the tail is `V_3`-Case-B/DOM for
  itself): includes a genuinely non-trivial sub-lemma (Step 2a: the tail
  can *never* be `V_3`-Case-A once `t_1<\tfrac4{15}\Sigma`, proved via the
  chain `\tfrac47S_{\mathrm{tail}}>\tfrac27\Sigma>\tfrac4{15}\Sigma`, which
  I independently re-derived and confirmed exactly) plus a clean strict
  bound `\mathrm{StratB}=p_1/2+t_1<\tfrac{31}{60}\Sigma<c(3)\Sigma`, margin
  `\ge\Sigma/60` uniformly. I independently re-implemented `V_3`, `L_2`,
  `\mathrm{StratA}`, `\mathrm{StratB}` from scratch and ran 300,000 random
  Case-C trials, classified exhaustively and disjointly into Region 1 /
  Region 2 / Region 3 (by construction: `t_1\ge\tfrac4{15}\Sigma$ else
  `t_1\ge S_{\mathrm{tail}}/2$ else neither) — **zero violations** in
  Region 1 (199,320 trials) and Region 2 (1,069 trials; narrow region, small
  natural sample, still zero violations). Also independently reproduced the
  two named witnesses exactly: `A=(6,5,4,2)/17` gives
  `\mathrm{StratA}(6,5,4,2)=9\le\tfrac{136}{15}` (Region 1), and
  `A=(1859,931,619,611)` gives, via the full 5-strategy `\min`,
  `\mathrm{StratC}_{23}=2014\le2144` (this witness lies in **Region 3**, not
  Region 1/2 — confirmed by direct computation, `t_1=931<1072=\tfrac4{15}
  \Sigma$ and `t_1=931<1080.5=S_{\mathrm{tail}}/2`). **Certified**,
  `lemmas/m4-region-a-region-b.md`, explicitly scoped as covering only
  Region 1 `\cup` Region 2, NOT the residual Region 3.
- **Region 3 (residual, `t_1<\tfrac4{15}\Sigma` and tail is `V_3`-Case-C for
  itself): honestly reported as OPEN, correctly not overclaimed.** The
  builder's write-up explicitly shows Strategy B's loose bound is
  algebraically insufficient here (needs `p_1+t_1\ge\tfrac45\Sigma`, not
  implied by Region 3's own hypotheses, which only give `p_1+t_1<
  \tfrac{23}{30}\Sigma<\tfrac45\Sigma`) — I independently re-checked this
  chain of inequalities and confirmed it. One fully worked interior example
  (`A\propto(1,1,1,0.9)`, i.e. `A=(10,10,10,9)`) is given, showing
  `\mathrm{StratC}_{23}=19.5\le20.8=c(3)\cdot39$ (target) with a genuine
  `6\%` margin, via a mechanism (the base triple `(p_1,t_1,t_2-t_3)` landing
  in `V_3`'s own Case-C branch, not the simpler DOM branch, since the
  builder shows the "DOM always fires for the base" shortcut is FALSE in
  general in this region) not yet turned into a closed-form general proof —
  I independently reproduced this exact worked example
  (`\mathrm{StratC}_{23}(10,10,10,9)=39/2`, target `104/5`, `39/2\le104/5`
  exactly) and reproduced the full 5-strategy `\min` over 49,737 randomly
  sampled Region-3 trials with **zero violations** (consistent with, but
  short of proving, Region 3 being closeable). **No proof of Region 3 was
  completed this round; `solved` is correctly not claimed for `m=4` Case C
  or for the whole problem.**

**What I independently verified is airtight and load-bearing (all reproduced
from scratch, none merely re-run from the builder's own script):** the
`V_3` case formulas as imported (matching `lemmas/ptbi-threshold-reduction.md`
Cases A/B and the round-9 Case C closure exactly, cross-checked line by
line); the `\mathrm{StratC}_{12},\mathrm{StratC}_{13},\mathrm{StratC}_{23}`
formulas as stated in the build (each costs `1+(\le2)\le3=m-1` marks, no
bookkeeping discrepancy found); the exact Region 1/Region 2/Region 3
partition is disjoint and exhaustive of `m=4` Case C (confirmed by direct
classification, no gap, no double-counting); every claimed numeric witness
value reproduces exactly.

**Verdict: CHANGES REQUESTED.** Two new lemmas certified (V3-BOUND,
m=4-REGION-A/REGION-B), genuine narrowing of the `m=4` Case C `\le15`-way
case split down to one precisely-characterized residual region (Region 3),
with the known hardest witness `A=(6,4,3,2)` shown to sit exactly on the
already-closed Region 1 boundary (not in the open residual). No
overclaiming: Region 3 is honestly left open, and general `m\ge5` is
entirely untouched this round (not attempted, not claimed). Next round's
clearest path: close Region 3 via `\mathrm{StratC}_{23}` (empirically the
winning strategy on both the round-16 headline witness and the new interior
example), tracking the base triple's own `V_3`-regime as a further (at most
3-way) sub-case split — then separately re-attack general `m\ge5`, which
this round's `m=4`-specific 5-strategy menu does not address.)*

*(Round 15 review — CHANGES REQUESTED for `universal-adversary-strategy`,
RETHINK for `defect-hall-deficiency`. Whole problem remains `partial`; Case C
for general `m\ge4` is still the sole open gap, now sharpened by two
independently re-verified, exact facts and a new negative result narrowing
the search on the "different-mechanism" side.

**`universal-adversary-strategy` (round 15 build).** I independently
re-derived and re-verified from scratch (fresh Python, `fractions.Fraction`
exact arithmetic, two independently-written recursive solvers — one
restricted to the certified contiguous-only menu, one implementing the full
non-contiguous subset-match menu):
- **Lemma MARKS-MONO** (`solve2(A,k)` non-increasing in mark budget `k`) —
  the inductive proof (strong induction on the auxiliary well-founded order
  `(k,|A|)`, using that every move legal at budget `k` is also legal at
  `k+1` with the same cost and a weakly-smaller-or-equal recursive value by
  the IH) is correct as written. I additionally reproduced it empirically
  (260 random trials, `m=2..6`, both the contiguous-only and the full
  menu, checking `solve2(A,k)` is non-increasing in `k` for every `k`):
  zero violations.
- **Lemma EXACT-TIE-SLACK** (matching a subset `S` of the tail costs
  `|S|` marks if the residual `r>0`, `|S|-1` if `r=0` exactly, giving
  `2`-mark slack at the recursive call in the `r=0` case and none in the
  `r>0` case) — re-derived directly from the elementary "splitting into `j`
  parts costs `j-1` cuts" fact; the arithmetic checks out exactly for both
  cases.
- **The `m=4` extremal witness, exactly reproduced.** `A=(6,5,4,2)/17`:
  Case C (`6/17<1/2`), contiguous-only `solve2(A,3)=9/17`, target
  `c(3)\cdot1=8/15`, margin `=8/15-9/17=1/255>0` — I reproduced this exact
  value independently with my own from-scratch recursive solver (matches
  to the exact fraction, not merely numerically close).
- **The `m=6` counterexample, exactly reproduced.** `A=(14,12,10,9,8,4)`
  (`\Sigma=57`, Case C since `14<28.5`): contiguous-only `solve2(A,5)=29`,
  target `c(5)\cdot57=608/21\approx28.952`, so `29>608/21` — a genuine,
  exact violation (`1/21`), confirmed by my own independent solver. The
  full non-contiguous menu reaches exactly `57/2=28.5\le608/21` on the same
  instance (also independently reproduced), confirming Lemma SLACK-COVER's
  general non-contiguous existence question genuinely *is* unavoidable for
  `m\ge6`, even though (per the strong, but incomplete, `m=4` evidence)
  it may not be needed at `m=4`.
- **What is honestly NOT closed.** No case-exhaustive proof that the
  contiguous-only menu meets the real target at every `m=4` configuration
  was completed — the builder's own write-up traces one natural strategy
  (`j^*=1` branch, peel-`t_1`-then-bound-by-certified-`m=3`-theorem) and
  shows it is *not* by itself universal (fails its own sufficient condition
  on a limiting family), though the specific failing configuration is still
  closed by a different branch of the `\min`. This is correctly reported as
  a gap, not papered over. Case C for general `m\ge4` remains open.

**Verdict: CHANGES REQUESTED.** Two new, fully general, independently
re-verified lemmas (MARKS-MONO, EXACT-TIE-SLACK), plus two exact,
independently-reproduced witnesses that sharply re-map (not close) the
remaining gap: the general subset-match existence question (Lemma
SLACK-COVER) is now *proved* necessary at `m=6` and not yet proved
unnecessary or provable at `m=4`. No overclaiming; `solved` is correctly
not claimed for any part of Case C.

**`defect-hall-deficiency` (round 15, mandated Step-0 gate).** Attacked
Lemma SLACK-COVER via a defect-Hall/König-deficiency bipartite-matching
encoding, a genuinely different mechanism from the three already-refuted
averaging/pigeonhole routes. I independently re-derived its central
structural fact from Case C's own defining inequality: `p_1<\Sigma(A)/2`
forces `\Sigma(\mathrm{tail}(A))=\Sigma(A)-p_1>\Sigma(A)/2>p_1` strictly,
always — so a covering subset of the tail for `p_1` always exists by a
trivial greedy argument (largest-first, must succeed before the tail is
exhausted since its sum exceeds `p_1`), checked and confirmed on all three
mandated witnesses (uniform-tail family, `T=(0.20,0.15,0.12,0.08)`,
`A=(1826,1563,1520,1514,765)/7188`). This makes any *permissive* Hall/König
encoding vacuous (deficiency identically `0`, no leverage on which subset
meets the actual value target) and a *restrictive* (contiguous-only)
encoding's Hall-witness demonstrably the wrong choice value-wise — I
independently reproduced the concrete counterexample (`fractions.Fraction`,
matching prior rounds' certified computation exactly): tail
`(0.20,0.15,0.12,0.08)`, contiguous match value `7/25=0.28`, strictly
exceeding `\Sigma(T)/2=11/40=0.275`. Both horns of the dichotomy are
correctly, rigorously ruled out — this is a genuine structural dead end for
the Hall/König-deficiency framing specifically (the underlying question is
a numeric subset-value optimization, not a cardinality/reachability
question), not a math error, and the approach correctly stopped at its own
mandated Step-0 gate rather than proceeding on an unverified premise.
**Verdict: RETHINK** (the builder's own honest self-diagnosis, independently
confirmed correct) — this specific mechanism is exhausted; any future
attack on Lemma SLACK-COVER needs a genuinely different tool.

Net effect: **Case C for general `m\ge4` remains the sole open gap for the
whole problem.** Nothing previously closed is reopened. The gap is now
mapped more precisely than before: proved *necessary* (non-contiguous
subset matching, i.e. full Lemma SLACK-COVER) at `m=6`; strong exact
evidence, but no full proof yet, that it is *avoidable* at `m=4` using
only already-certified machinery; the defect-Hall/König mechanism is now
ruled out as a route to closing it, in either of its two natural
encodings.)*

*(Round 14 review — CHANGES REQUESTED for `universal-adversary-strategy`,
RETHINK for the new `case-c-slack-covering`. Whole problem remains
`partial`; the sole open gap (Case C, general `m\ge4`) is not closed
this round either, but real, independently-confirmed progress was made
on both sides.

**`universal-adversary-strategy` (round 14 build).** Rebuilt the
budget-capped recursion (`solve2(A,marks)`) with a single shared
real-mark counter (cap `m-1`, every move — Move 0/1/2/3 alike —
charged correctly), fixing the round-13 mark-accounting bug. I
independently re-verified from scratch:
- **Lemma FREE-TIE-REDUCTION (Move 0)** — CORRECT, certified in full
  (`lemmas/free-tie-reduction-move0.md`). I wrote my own from-scratch
  exact-`Fraction` check (20,000 random trials, even-multiplicity tied
  runs of random length `2j` at random positions in random arrays) and
  found zero violations. The proof itself (pairing the `2j` consecutive
  ranks into `j` adjacent pairs, each straddling exactly one odd/even
  rank regardless of starting parity; even-length run means no parity
  shift for the surrounding blocks) is correct and genuinely
  positionally general (not just a top-prefix special case).
- **`solve2`'s well-foundedness** — re-derived and confirmed: `(marks,
  |A|)` lexicographic, `marks` primary, strictly decreases on every
  branch (Move 0: `marks` unchanged, `|A|` strictly drops by `2j\ge2`;
  every other move: `marks` strictly drops by `\ge1`). I independently
  reimplemented `solve2` myself (not reusing the builder's script) and
  hit exactly the subtlety the write-up flags: a naive Move-2 branch
  with `|S|=1,r=0` (cost `0`) is a literal *no-op* (reproduces the same
  multiset with the same `marks`, since `p_1=t_i` already gives an
  even-multiplicity tie) and causes infinite recursion unless explicitly
  excluded in favor of Move 0 — confirming the write-up's remark that
  this sub-case "is already covered by Move 0" is not just a comment but
  load-bearing for termination; once excluded (as the write-up's design
  intends), my independent reimplementation reproduced the builder's
  claimed values **exactly** on all three witnesses:
  `A=(26,21,10)/57 → 31/57` (matches the round-13 true-optimum figure
  exactly), `T=(0.20,0.15,0.12,0.08) → 11/40 = \Sigma(T)/2` exactly (via
  the non-contiguous match), and `A=(965,965,958,482)/3370 → 1685/3370 =
  \Sigma(A)/2` exactly (Move 0 firing for free on the pre-existing tie).
  All three are comfortably `\le` their respective `c(m-1)\Sigma(A)`
  targets.
- **The `m=8` witness — genuinely untested, not a false claim.** I
  attempted my own independent computation and it also did not
  terminate within several minutes (the exhaustive `2^{|tail|}`-subset
  Move-2 search is exponential and does not scale to `m=8` without a
  smarter algorithm). This is an honestly-reported implementation
  limitation, not an overclaim — the builder correctly flagged it as
  "NOT evaluated" rather than silently omitting it or claiming a pass.
  **Per CLAUDE.md's rigor rules, this is an acceptable way to report an
  untested case** (distinguish "we have proved X" from "we conjecture
  X"): it does not block the `partial` verdict, but it does mean the
  general Lemma SLACK-COVER (subset-match existence, now correctly
  identified as a joint covering+value statement, not a pure covering
  statement) remains the sole open item for the whole problem, and no
  claim beyond `partial` is warranted. **Verdict: CHANGES REQUESTED.**
  Real progress (mark-accounting bug fixed, Move 0 generalized and
  certified, three-witness re-verification), sole remaining gap sharply
  isolated (Lemma SLACK-COVER, an inductive joint covering+value
  statement, not solvable by a pure subset-sum mesh bound as shown this
  round).

**`case-c-slack-covering` (round 14, new slug, first build).** Built a
one-level averaging/pigeonhole family `UB_i := c(m-2)\Sigma +
(1-2c(m-2))t_i` from the certified Lemma DOUBLE-INSERT (via a new
corollary, Lemma DOUBLE-INSERT-MATCH-VALUE, now certified —
`lemmas/double-insert-match-value.md`, independently re-verified by me,
5000 random trials, zero violations of the exact value identity). I
independently re-derived, symbolically with `sympy` (not reusing the
builder's script), the claimed worst-case margin at the uniform-tail
boundary:
```
margin(m) = c(m-1) - UB_1(m) = (2^m(3-m)-2) / (2(2^m-2)(2^m-1)(m-1))
```
— my own symbolic simplification matches this closed form **exactly**
(`sympy.simplify` gives a zero difference), and matches the builder's
numeric table exactly at `m=4` (`-1/70`) and `m=8` (`-641/453390`). The
sign argument (denominator positive for `m\ge2`; numerator
`\le -2^m-2<0` for every integer `m\ge4`) is elementary and I verified
it holds for `m=3..12` numerically as well. **This is a genuine, exact
algebraic refutation of the entire one-level-averaging-plus-coarse-IH
family for every `m\ge4`, not a numerical near-miss** — certified as a
reusable pruning fact (`lemmas/uniform-tail-margin-negative.md`).

**Verdict: RETHINK, not merely CHANGES REQUESTED.** This is not a case
of "the math is wrong" — every step (Step 0's exact value identity,
Step 1's trivial averaging-existence lemma, Step 2's domination-by-min
observation, Step 4's algebraic margin) is correct and I independently
reproduced all of it. The reason for RETHINK is the same
convergence-failure pattern already established twice in this run
(`minimax-mixed-duality`, rounds 6-8; `case-c-secondary-extremality`,
round 11): the approach's own analysis shows that **any repair of the
refuted mechanism collapses into exactly the same multi-level
recursive matching content (`Lemma SLACK-COVER`) that
`universal-adversary-strategy` is already independently pursuing and
has not yet closed** — the builder's own write-up says this explicitly
("reduces to exactly the same multi-level recursive matching machinery
... eliminating any independent proof leverage this route would
supply"). An approach whose entire premise (a genuinely distinct route
to Case C) is refuted, with the builder's own diagnosis showing no
repair can avoid duplicating the sibling approach's still-open content,
offers no independent path forward and should return to the outliner
for a fundamentally different framing (per the CLAUDE.md diversity
mandate — a bypass in the same framing hits the same wall). The two
lemmas it produced (DOUBLE-INSERT-MATCH-VALUE, and the uniform-tail
margin negative fact) are certified and retained as reusable
pruning/building-block facts for whichever approach continues to attack
Case C, but the slug itself is not worth rebuilding without a genuinely
new mechanism (not a variant of one-level match+IH averaging).

Net effect: **Case C for general `m\ge4` remains the sole open gap for
the whole problem.** Nothing previously closed is reopened (lower
bound, `m=3`, `m=1` fully general, WF-C5's termination content, and now
also `solve2`'s corrected accounting and Lemma FREE-TIE-REDUCTION all
stand). The gap is now precisely: prove the general subset-match
existence theorem (Lemma SLACK-COVER / PAIR-VALUE) as a joint
covering-plus-recursive-value statement inside the `(marks,|A|)`
induction — a pure size-only mesh/covering argument is proven
insufficient (round 14), and a one-level averaging shortcut is now also
proven insufficient (round 14) — the correct proof must engage with the
recursive *value* of the leftover, not just its achievable-sum
coverage.)*

*(Round 13 review — CHANGES REQUESTED for both builds; corrects a serious
methodological error in Round 12's headline claim, but does NOT reopen
anything already fully closed (the entire lower bound, `m=3`'s upper
bound, and Lemma WF-C5's actual content — termination — all still
stand). Both round-13 builders (`universal-adversary-strategy` and
`universal-adversary-strategy-exact-tie`) independently discovered the
SAME root problem and I independently re-verified it from scratch with
my own fresh Python (exact `fractions.Fraction`, plus `scipy` continuous
optimization over the literal constrained game, not reusing either
builder's code):

**The critical finding, confirmed correct: Round 12's certified
`solve(A,budget)` recursion (Lemma WF-C5) does *not* correctly model
"Xiang Yu has exactly `|A|-1` real marks."** Its `budget` parameter only
counts *nested Move-3 (tail-snip) uses*; Move 1 and Move 2 never
decrement any real-mark counter, and Move 3 itself increases `|A|` by 1
without being charged for it. I independently reproduced this exactly:
for the witness `A=(26,21,10)` (`m=3`), I reimplemented `solve(A,1)`
completely from scratch and got `solve_full(A)=57/2=28.5=\Sigma(A)/2`
exactly (confirming the round-13 explorer's "apparent identity" finding
is a real fact about this specific recursion, not a builder error) — but
tracing the actual winning move sequence, it uses **3 elementary splits**
(`tail-snip` then `halve` then `halve` then a free 0-mark tie), i.e. `|A|
= 3` real marks, while the true available budget is `m-1=2`. **I then
independently verified, via an from-scratch exhaustive-over-mark-
allocation-pattern `scipy` continuous optimizer (both "one piece split
into 3 parts" and "two different pieces each split once" patterns, many
random restarts plus `differential_evolution` cross-checks), that the
TRUE 2-mark-constrained game value for this witness is exactly `31`, not
`28.5`.** This refutes `universal-adversary-strategy-exact-tie`'s
targeted sharper conjecture (the "exact identity"
`solve_full(A)=\Sigma(A)/2` throughout Case C) — confirmed correct. Note
`31 \le c(2)\Sigma(A) = 228/7 \approx 32.57`, so Claim PTBI's actual
(weaker) target is untouched by this witness.

**Consequence for Round 12's "mandatory adversarial gate PASS":** that
gate checked `solve_full(A) \le c(m-1)\Sigma(A)` using the *uncapped*
`solve` recursion, which (since Move 3 grants an uncounted extra mark)
gives Xiang Yu strictly MORE power than he truly has. Since more power
for the minimizing player can only make `solve_full(A)` smaller or equal
to the true, correctly-capped game value, **a "PASS" of the round-12 gate
establishes nothing about the true game value — it is evidence about a
strictly easier-for-Xiang-Yu, over-generous surrogate, in the WRONG
direction to certify the actual theorem.** This is a genuine
methodological invalidation of Round 12's headline conclusion, not a
minor bookkeeping slip: **the round-12 "gate PASS" must be treated as
RETRACTED as evidence for Claim PTBI's Case C; it should not be cited or
relied upon by any future round.** (Lemma WF-C5 itself is UNAFFECTED and
remains correctly certified — re-read its file directly: it only proves
the abstract recursion terminates, and never claims to model the true
mark-capped game; that modeling gap is precisely what this round
discovered and is a separate, additional fact.)

**Second, independent confirmation the bug is not confined to Case (b):**
`universal-adversary-strategy`'s main build found the same root defect
generalizes to Case (a) (previously assumed to close "trivially" via
Move 1 + IH). Witness `A=(0.45,0.20,0.15,0.12,0.08)`, tail
`T=(0.20,0.15,0.12,0.08)` (`\Sigma(T)=0.55`, genuinely Case-C-for-itself).
I independently re-verified via an exhaustive-over-mark-allocation-
composition `scipy` search (every way to distribute up to 3 marks among
`T`'s 4 pieces, continuous split ratios, hundreds of random restarts per
pattern) that **the TRUE 3-mark-constrained value of `T` is exactly
`27.5 = \Sigma(T)/2`** (achieved by splitting `p_1=20\to(12,8)` — an exact
non-contiguous tie against `T`'s own existing elements `12,8`, skipping
over `15` — plus independently halving `p_2=15\to(7.5,7.5)`, using only 2
of the 3 available marks). **This does NOT refute HALF-BOUND or Claim
PTBI on this witness — the true value exactly meets the target.** What it
refutes is the SUFFICIENCY of the current certified move-menu
(Move 1/halve, Move 2/contiguous-prefix-match only, Move 3/tail-snip): I
independently reimplemented the properly-mark-capped `solve2(A,marks)`
using this restricted (contiguous-prefix-only) menu and got
`solve2(T,3)=28 > 27.5`, confirming the menu itself — even with correct
mark accounting — cannot reach the true optimum here, because the true
optimum needs a **non-contiguous subset match** (`p_1` tied to `{12,8}`,
skipping the intervening `15`), which none of the certified lemmas
(BLOCK-RECURSE, PARTIAL-DOM, DOM, HALVE, TAIL-SNIP) can produce — only
the still-existence-unproven, hypothesis-free Lemma PAIR-VALUE (certified
since round 9 but with no general Hall-type existence theorem) covers
this move shape.

**Net effect on the open gap:** Case C for general `m\ge4` remains open,
and is now understood MORE PRECISELY (not more badly) than after round
12: the actual missing piece was never "does Candidate 5 pass a gate" —
it is, and always was, the Hall-type general subset-matching existence
question for Lemma PAIR-VALUE (flagged since round 9, reiterated rounds
11-12) — this round shows that question is unavoidable even in the
"easy" Case (a), not just the originally-suspected regimes. No
regression: nothing previously airtight (lower bound, `m=3`, WF-C5's
actual termination content) is touched. **Certified this round:**
`lemmas/nonneg-excess-uncapped-recursion.md` (Lemma NONNEG-EXCESS,
independently re-derived and stress-tested by me, 3000 random trials,
minimum excess found exactly `0`) — narrowly scoped explicitly as a fact
about the *uncapped, now-known-unfaithful* `solve(A,budget)` recursion,
not the true game value; flagged so no future round mistakes it for
evidence about the real game.

Both builds routed **CHANGES REQUESTED**: real, valuable, independently-
confirmed negative/diagnostic progress; no `solved` claim by either
builder (correctly not overclaimed); Case C remains the sole open gap for
the whole problem, now more sharply (and more honestly) characterized.
Full detail in the new "Round 13 build" sections of
`approaches/universal-adversary-strategy.md` and
`approaches/universal-adversary-strategy-exact-tie.md`.)*

*(Round 12 review — CHANGES REQUESTED, real progress, gap remains open.
`universal-adversary-strategy`'s round-12 build (Candidate 5,
budget-capped TAIL-SNIP recursion) was independently re-verified from
scratch by the proof-reviewer:

1. **Lemma WF-C5 (well-foundedness) — independently re-derived and
   CONFIRMED CORRECT, certified** (`lemmas/wf-c5.md`). The measure
   `(budget,|A|)` lexicographic with `budget` primary (not `|A|` primary
   as an earlier outline draft had it) is the right fix — reviewer
   independently re-derived why: `tail-snip` increases `|A|` while
   decreasing `budget`, so only a `budget`-primary order can register it
   as a decrease. The `j*≥1` sub-claim (needed for Move 2 to decrease the
   secondary coordinate when `budget=0`) is immediate from `A` sorted
   descending (`A[0]≥A[1]=S_1`) — reviewer confirmed this one-line fact
   and additionally reproduced clean termination on thousands of random
   test instances with an independent from-scratch Python
   implementation (after fixing an unrelated bug in the reviewer's own
   test harness: for `m=2`, Case C `p_1<Σ/2` is vacuous since sorted
   descending forces `p_1≥p_2≥Σ/2` always — a harness artifact, not a
   flaw in the proof or the recursion).
2. **Mandatory adversarial gate — independently re-run, CONFIRMED PASS.**
   Reviewer's own `scipy.optimize.differential_evolution` sweep,
   `m=4..12`, found the exact same worst-case margins the builder
   reports (`1/30, 1/62, ..., 1/4094`, i.e. `1/(2(2^m-1))` exactly,
   matching to machine precision at every `m` tested) — strong
   independent corroboration, not just a re-run of the builder's own
   script. Reviewer also independently confirmed the builder's flagged
   witness `A=(0.45,0.40,0.06,0.05,0.04)` (tail locally dominant
   relative to its own remaining sum): `solve_full(A) = 1/2` exactly
   (matching `Σ/2`), while a pure Move-1-only (halve-every-piece) chain
   overshoots to `13/25 = 0.52 > 1/2`, confirming Move 2/3 genuinely do
   load-bearing work in this regime and the gap is real, not a
   near-miss.
3. **Lemma HALF-BOUND — honestly reported as unproved, correctly not
   overclaimed.** The builder's own "Verdict for this round" explicitly
   states Status remains `partial` and Case C remains open; no
   overclaiming found. The one flagged open sub-case (a non-top-level
   piece in the tail becomes itself locally dominant relative to its own
   remaining sum, so repeated Move-1 halving alone cannot telescope to
   exactly `Σ/2`) is a real, precisely-isolated gap — reviewer
   independently reproduced the overshoot computation above confirming
   it is not a red herring.

**Case C for general `m≥4` remains open. The whole problem remains
`partial`** — this closes neither Case C nor the whole problem, contrary
to what a looser reading might suggest; the builder never claimed
`solved` and the reviewer's independent checks found no gap in what
*was* proved (WF-C5) and no unfounded claim in what was *not* proved
(HALF-BOUND). Certified `lemmas/wf-c5.md` this round. See
`approaches/universal-adversary-strategy.md`, "Round 12 build" section,
for full detail.)*

*(Round 11 review — no status change; both routes tried this round
against general-`m≥4` Case C are correctly ruled out, narrowing the search
rather than closing it. **`universal-adversary-strategy`** tested two
things: (i) reusing the just-certified Lemma TREE-BOUND-MULTICLUSTER
(lower-bound side) for Case C's existence question — I re-read the lemma
statement myself and confirm the builder's diagnosis: it is a
universal-over-Xiang-Yu-responses bound against one fixed geometric
configuration `A_n`, the opposite quantifier shape from what Case C needs
(exists-a-response, for every arbitrary configuration), and its proof
engine depends on a discrete power-of-2 anchor lattice (Reductions R1/R2,
telescoping) that has no analogue when residuals are generic reals — Route
A is a genuine structural dead end, not a numeric near-miss; (ii) the
natural fix to the round-10/11 induction-hypothesis bookkeeping error, a
construction matching exactly 2 disjoint top-level pairs
(`p_1\!\to\!p_2`, `p_3\!\to\!p_4`) before invoking the strong IH at size
`m-2`. I independently re-derived and re-ran this exact construction with
`fractions.Fraction` arithmetic (script reproduced fresh at
`/tmp/route_b2_check.py`): it meets the target on the known hard `m=5`
witness `A=(1826,1563,1520,1514,765)/7188` (margin `≈0.00585`, exactly
reproducing the builder's number), but **fails for every `m` from 4 to 100**
on the near-uniform-tail family `p_1=0.499`, tail uniform (e.g. `m=6`
margin `≈-0.01204`, `m=20` margin `≈-1.2×10^{-6}`, still strictly
negative) — confirmed exactly, not approximately. I also independently
confirmed (Nelder-Mead search, `/tmp/true_opt_check2.py`) that this same
uniform-tail witness is *not* a genuine obstruction: the already-certified
Lemma PARTIAL-DOM (spending nearly the whole budget subdividing `p_1`
alone) reaches `≈0.5`, comfortably under target. Verdict: no fixed small
integer number of top-level pairs is a universal Case-C construction;
both routes this round are correctly reported negative results, not false
progress. Routed **CHANGES REQUESTED** — real, if negative, progress
(narrows what any future fixed-template construction must satisfy), gap
remains open. **`case-c-secondary-extremality`** ran its mandated cheap
feasibility gate (does a secondary tie-count statistic distinguish the
true optimal response among all global minimizers, on the same `m=5`
witness) before building any exchange machinery. I independently
reproduced the two key numeric claims from scratch with exact
`Fraction` arithmetic (script `/tmp/round-11/verify_gate.py`): Construction
A (match/match/match/self-halve chain, 4 tied pairs + 1 singleton) and
Construction B (three independent self-halves, 3 tied pairs + 3 singletons)
both evaluate to the *exact same* `oddrank = 1199/2396`, and this is not
numerical coincidence — I re-derived both value formulas symbolically and
confirmed they reduce to the identical expression
`p_1/2+p_2/2+p_3+p_5/2`. So the candidate secondary statistic (tied-pair
count) does narrowly prefer the correct branch on this one test (4 vs 3
pairs), but only because the two competing constructions are provably
value-equivalent by direct algebra — meaning any general proof that
"the tie-maximal response meets the target" would still have to establish
the same closed-form bound `p_1/2+p_2/2+p_3+p_5/2\le c(4)\Sigma` that
`universal-adversary-strategy`'s Routes A/B are already trying to prove.
This is the exact convergence failure mode (`minimax-mixed-duality`'s
fate) CLAUDE.md's diversity rule and this slug's own risk section
flagged in advance. Routed **RETHINK** — the builder's own recommendation,
independently confirmed correct.)*

*(Round 10 review — HEADLINE: the entire lower bound is now closed. New
Lemma TREE-BOUND-MULTICLUSTER (`recursive-embedding-induction`,
`lemmas/tree-bound-multicluster.md`) generalizes Lemma TREE-BOUND-RESIDUAL
from "at most one impurity" to "arbitrarily many impurities, distributed
anywhere in the forest, including several landing simultaneously at the
same top-level of the same recursive pass" — precisely the multi-cluster
gap the round-9 review flagged as the last open sub-case. I independently
re-verified this from scratch, not just numerically but by re-deriving the
proof's own internal mechanism: (1) exhaustive brute-force enumeration for
small `(m,r)` (`m≤3`) with a from-scratch tree generator, zero violations;
(2) large-scale randomized recursive stress test with every node
independently and recursively having a chance to be an arbitrary-depth
impure cut (`m=1..8`, `r∈{1,3,5,7}`, 3000 trials each) — minimum `D` found
is exactly `τ_m` in every case, and the even-`r` control shows genuine
violations (confirming the harness discriminates and `r` odd is
load-bearing); (3) an *exhaustive* (not sampled) enumeration allowing every
one of the `r` top trees and every one of the `m-1` standard trees to
independently choose leaf/pure-split/any-depth-impure-cut in one shot
(`m` up to 6, `r` up to 5, up to 6 million configurations at the largest
case) — zero violations, confirming the bound is robust to many
*simultaneous* independent clusters, not just clusters separated by
recursion depth; (4) direct algebraic re-derivation and Fraction-exact
numerical confirmation of every intermediate identity the proof uses
(Fact PAIR-CANCEL, the Step-3 assembly identity
`D(X∪{y_i,c_i})=A_{p'}+(-1)^{p'}D(Y)`, and the "k odd" bypass formula
`D(B)=τ_1-D(R)`) — all reproduce exactly, on hundreds to thousands of
random instances each, zero mismatches. I also stress-tested a meta-level
concern (whether the "impure cut is terminal — the residual companion is
never itself further split" modeling choice could hide real Xiang-Yu
strategies that beat the bound): an *unconstrained*-marks version of this
does show `D` can be driven arbitrarily low, but a **direct simulation of
the real, budget-constrained game** (not the abstract forest model) for
`n=2` and `n=4` — random search over every possible allocation of Xiang
Yu's `≤n` marks among all `n+1` real pieces, including multiple marks on
the same piece, hundreds of thousands of trials each — found the true
minimum `oddrank` matches `c(n)·Σ` **exactly**, no violation, confirming
the "further-split-the-residual" concern is not exploitable within the
real mark budget and is not a live gap. **Conclusion: Lemma
TREE-BOUND-MULTICLUSTER's proof is correct and gapless as written, closing
gap (b) in full generality. Combined with the already-certified Lemma
TREE-BOUND (gap a) and Lemma CROSS-TIE-AFFINE (the reduction to well-
separated / majority-part / minority-residue sub-cases), `A_n`'s value is
now a fully proved theorem: `A_n` guarantees Liu Bang exactly `c(n) =
2^n/(2^{n+1}-1)` for every `n≥1`, unconditionally — the entire LOWER BOUND
half of the problem is closed.** The one inherited (not re-derived this
round) trust point is the original vertex-reduction argument (Lemma
V'-GEN / Lemma CROSS-TIE-AFFINE, certified across rounds 6–9) that
establishes every genuine Xiang-Yu optimum reduces to this
anchor-plus-tree-with-impurities combinatorial structure in the first
place; this was reviewed and re-verified in prior rounds and not
re-litigated here, and my own direct real-game simulations (budget-
respecting, arbitrary splits, not restricted to the tree formalism) are
consistent with it finding no violation.

Separately: `geometric-dominance-construction`'s round-10 Lemma TOP2 +
Structural Lemma (`lemmas/multi-cluster-two-block.md`) independently
proves the SAME multi-cluster closure but honestly scoped only to
configurations where **every split piece has at most 2 parts** — correctly
and explicitly flagged by the builder as narrower than an unrestricted
closure, and (per this round's dispatch) not cross-checked against the
sibling at build time since the sibling's file had not yet been updated.
I independently re-verified this narrower result too (24,000 random
trials using genuine `A_n` piece values, zero violations) — it is
correct as stated, but it is `recursive-embedding-induction`'s
TREE-BOUND-MULTICLUSTER (unrestricted to any number of parts per piece,
including pieces with several independently-tied residual coordinates)
that is the operative, stronger claim actually closing the lower bound in
full; geometric-dominance-construction's result is a valuable independent
cross-check of the ≤2-part sub-case, not an independent full closure.

`universal-adversary-strategy`'s round-10 work (Lemma ALL-BUT-MIN, Lemma
MATCH-TAIL-PAIR, both independently re-verified exactly by direct
`oddrank` computation on hundreds of random instances; the `g(v)`
structural-obstruction algebra re-derived and confirmed; the `m=5`
counterexample witness `A=(1826,1563,1520,1514,765)/7188` independently
recomputed to reproduce `7937/14376≈0.5521 > c(4)=16/31` exactly) is
correct and honestly reported as still open for general `m≥4` Case C — no
issues found.

**Upper bound (general `m≥4` Case C) is now the ONLY remaining gap for the
whole problem.** The lower bound (`A_n` achieves `c(n)`) is fully proved;
what remains is showing no *other* (non-geometric) Liu Bang configuration
lets him do better than `c(n)`.

Prior (round 9) review note, superseded above but kept for history: builders' claim that gap (b) is "fully closed" is
accepted for the single-cluster case, independently re-derived from
scratch (fresh Python re-implementations of both TREE-BOUND-RESIDUAL's
forest-with-one-impurity construction and TWO-BLOCK's two-largest-element
estimate, exhaustive/dense-grid, zero violations). **However, both proofs,
as written, explicitly cover only ONE residual/tie-cluster in the whole
configuration** — TREE-BOUND-RESIDUAL's induction hypothesis is "at most
one impure node in the entire forest"; TWO-BLOCK's Main Theorem covers one
shared tie-value `v` across one subset `S`. Neither file argues (or even
flags) that the true vertex-optimum can be WLOG reduced to at most one
such cluster; a configuration with **two or more simultaneous,
independent** tie-clusters (different tie values, disjoint piece sets) is
not covered by either written proof. My own stress test (2–4 simultaneous
independent minority-tied splits, `n` up to 6, dense grids, exact
`Fraction`) found **no violation** — `D` stayed comfortably above `t_n` in
every case — so the underlying claim is very likely true, but this is
numerical evidence, not a proof, and the gap should not yet be treated as
airtight. Routed **CHANGES REQUESTED** for both approaches this round;
next round should either generalize the induction to multiple
simultaneous impurities or prove a WLOG single-cluster reduction.
Separately, re-verified `universal-adversary-strategy`'s `m=3` Case C
closure and Lemma PAIR-VALUE from scratch — both check out exactly, no
issues found; `m≥4` Case C is honestly and correctly left open. Full
review: see reviewer notes recorded via `record_outcome`, round 9.)*

## Approaches tried
- `universal-adversary-strategy` — round 17: closed Region 3 of `m=4`
  Case C in full (Lemma V3-CLOSED-FORM + Lemma A-BASE-NOT-CASE-A collapse
  it to a 3-regime/5-cell exact rational LP-vertex closure using only
  `\mathrm{StratA}`/`\mathrm{StratB}`/`\mathrm{StratC}_{23}`). Combined
  with round 16's Region 1+2 closure, **`m=4` Case C is fully closed and
  Claim PTBI is fully proved for `m=4`.** Independently re-verified in
  full this round (see Status note above): both new lemmas re-derived by
  hand and stress-tested (200k/300k trials, zero violations), all three
  exact closed forms cross-checked against the recursive definitions
  (400k trials, zero mismatches), all 5 LP-vertex values reproduced
  exactly, adversarial `differential_evolution` search found no
  counterexample. General `m\ge5` untouched, honestly not claimed.
  **verified-milestone / CHANGES REQUESTED** (whole-problem `Status`
  stays `partial`).
- `vertex-reduction-on-adversary` — round 17, first (and, per this
  review, likely only) build: scoped feasibility check of a vertex/LP
  reduction framing on Region 1/2 (already closed) plus a sketch for
  Region 3/general `m`. Confirmed to be a correct but purely notational
  restatement of the existing Region 1/2 proof (no new inequality, no new
  territory), with an honestly inconclusive (not falsely optimistic)
  outlook for Region 3/general `m` that this round's direct closure of
  Region 3 (above) has now made moot. Independently re-verified — the
  builder's own negative self-assessment is correct. **RETHINK** —
  dead-end for this specific framing.
- `universal-adversary-strategy` — round 16: targeted `m=4` Case C's
  5-strategy menu specifically (`V_4(A)=\min(\mathrm{StratA},
  \mathrm{StratB},\mathrm{StratC}_{12},\mathrm{StratC}_{13},
  \mathrm{StratC}_{23})`). Proved Lemma V3-BOUND (loose `\le c(2)\sigma_3`
  bound on the certified `m=3` theorem) and Lemma m=4-REGION-A/REGION-B (a
  clean two-region algebraic closure of part of `m=4` Case C, including the
  known extremal witness `A=(6,4,3,2)` exactly on Region 1's boundary).
  Both independently re-verified and certified this round (see Status note
  above, `lemmas/v3-bound.md`, `lemmas/m4-region-a-region-b.md`). Residual
  Region 3 (`t_1<\tfrac4{15}\Sigma`, tail is `V_3`-Case-C for itself) is
  honestly left open — Strategy A/B's loose bounds proved algebraically
  insufficient there, one worked interior example shows the target is still
  met via `\mathrm{StratC}_{23}`'s harder (non-DOM) branch, but no general
  proof. General `m\ge5` untouched this round. **CHANGES REQUESTED.**
- `universal-adversary-strategy` — round 13: diagnosed that the round-12
  outline-reviewer's flagged "no spare Move-3 mark" bug (Case b) is a
  symptom of a *general* mark-accounting defect in the certified
  `solve(A,budget)` recursion (Move 1/2 never decrement real marks, Move
  3 grants an uncounted extra one) — independently reproduced by the
  reviewer exactly. Built the corrected `solve2(A,marks)` (single real-
  marks pool). Found this reopens Case (a) too (previously assumed
  trivial): witness `A=(0.45,0.20,0.15,0.12,0.08)`, tail
  `T=(0.20,0.15,0.12,0.08)`, `solve2(T,3)=7/25=0.28>\Sigma(T)/2=0.275`
  under the certified (contiguous-prefix-only) move menu — independently
  reproduced by the reviewer (`solve2(T,3)=28` vs. true 3-mark optimum
  `27.5`, confirmed via exhaustive `scipy` search). **Reviewer clarifies:
  this does NOT refute HALF-BOUND on this witness — the TRUE game value
  is exactly `27.5=\Sigma(T)/2` (found by the reviewer's own from-scratch
  search, achieved by a non-contiguous match `20\to(12,8)` plus an
  independent halving of `15`) — it refutes the SUFFICIENCY of the
  current certified move-menu (contiguous-prefix Move 2 only) for
  *proving* Case (a), not the underlying claim itself.** Real progress:
  correctly and precisely re-locates the missing piece (Hall-type
  non-contiguous subset-matching existence for Lemma PAIR-VALUE) as
  unavoidable even in Case (a). **CHANGES REQUESTED.**
- `universal-adversary-strategy-exact-tie` — new round 13. Assigned to
  prove the sharper conjectured identity `solve_full(A)=\Sigma(A)/2`
  exactly throughout Case C via a Hall's-theorem/exact-cover route.
  **Result: found and proved the identity is FALSE for the true,
  correctly mark-capped game** — witness `A=(26,21,10)` (`m=3`, true
  budget `2` marks): the certified (uncapped) `solve(A,1)` recursion
  computes `28.5=\Sigma/2` exactly via a construction using `|A|=3`
  physical marks (one over the true `m-1=2` budget); properly capped, the
  reviewer independently confirmed (fresh `scipy` search over both 2-mark
  allocation patterns, cross-checked with `differential_evolution`) the
  TRUE value is `31\ne28.5`. Proved Lemma NONNEG-EXCESS (`e(A,budget)\ge0`
  for the uncapped recursion, any `A`, any `budget$) — independently
  re-derived and stress-tested by the reviewer (3000 random trials, min
  excess exactly `0`), certified with an explicit scope caveat (a fact
  about the uncapped recursion, not the true game). Correctly notes
  `31\le c(2)\Sigma(A)=228/7\approx32.57`, so Claim PTBI's real target is
  untouched by this witness. Honestly scoped throughout: does not claim
  to refute or close Claim PTBI itself. **CHANGES REQUESTED** (its
  assigned sharper-identity target is refuted with a rigorous, reviewer-
  confirmed negative result — valuable population-pruning progress, not a
  dead end, since the underlying weaker theorem is untouched and the
  approach surfaced a genuine defect the whole population needed found).
- `universal-adversary-strategy` — round 12: built Candidate 5 (budget-
  capped TAIL-SNIP recursion). Proved and certified Lemma WF-C5
  (well-foundedness, `lemmas/wf-c5.md`, independently re-verified).
  Independently re-ran the mandatory adversarial gate — confirmed PASS
  (no counterexample `m=4..14`, two structural families to `m=20`, a
  large random sweep, all independently reproduced by the reviewer with
  a fresh `differential_evolution` implementation matching the exact
  claimed margins `1/(2(2^m-1))`). Discovered but explicitly did NOT
  prove a sharper sufficient Lemma HALF-BOUND
  (`solve_full(A)≤Σ(A)/2` throughout Case C) — the one open sub-case
  (tail locally dominant relative to its own remaining sum) is real,
  independently reproduced by the reviewer, not a red herring. Honestly
  reported as `partial`, no overclaiming. **CHANGES REQUESTED** — real
  progress (WF-C5 closed, gate re-confirmed, gap sharpened to
  HALF-BOUND's one sub-case) but Case C for general `m≥4` remains open.
- `universal-adversary-strategy` — round 11: tested reuse of Lemma
  TREE-BOUND-MULTICLUSTER for Case C (Route A) and a properly-generalized
  2-simultaneous-top-level-pair construction (Route B). Both ruled out
  with proof, independently re-verified (see Status note above) — Route A
  a structural quantifier/mechanism mismatch, Route B refuted by an exact
  `Fraction` near-uniform-tail counterexample family for `m=4..100`. CHANGES
  REQUESTED, Case C for `m≥4` remains the sole open gap.
- `case-c-secondary-extremality` — round 11: ran its mandated feasibility
  gate on the `m=5` hard witness; found the candidate secondary statistic
  (tied-pair count) only "passes" because the two competing constructions
  are algebraically value-equivalent, giving no independent leverage —
  independently re-verified exactly (see Status note above). RETHINK, per
  the builder's own honest self-diagnosis.
- `recursive-embedding-induction` — worked (partial). **Round 9: Lemma
  TREE-BOUND-RESIDUAL extends TREE-BOUND with a third induction case for
  one forced-residual leaf, independently re-derived from scratch (fresh
  Python forest generator, exhaustive `m=1..4,r=3`) and confirmed
  `D≥τ_m` in every case — the "minority part of a 2-part-split piece tied
  at a deep external anchor" residue sub-case is correctly closed for the
  single-cluster case.** The round-9 build's own claim that this
  "virtually fully split" comparison mechanism was found FALSE
  (`159/600` violations) is a correctly-reported negative result, not
  load-bearing — the actual closure reruns the induction with a new case
  instead, using only the already-certified Lemma D-BOUND. **Reviewer
  caveat (round 9, CHANGES REQUESTED): the claim "gap (b) fully closed"
  is over-broad as written** — the lemma's induction hypothesis is
  explicitly "at most one impure node in the entire forest," and does not
  extend to two-or-more simultaneous independent tie-clusters (disjoint
  pieces each tied to a *different* external anchor at once); this
  multi-cluster case is not addressed or even flagged in the lemma file.
  My own stress test (2–4 simultaneous independent minority splits, `n`
  up to 6, dense grids, exact `Fraction`) found no violation, so the
  underlying claim is very likely true, but this is numerical evidence,
  not a proof — next round should either generalize the induction to
  multiple simultaneous impurities or prove a WLOG single-cluster
  reduction before gap (b) is treated as unconditionally closed. **Round
  8: gap (a) FULLY CLOSED, unconditionally for every mark budget.** New certified
  Lemma TREE-BOUND (`lemmas/tree-bound-anchor.md`) reframes anchor-only
  strategies as binary-subdivision-tree forests (forced halving: no two
  distinct powers of 2 sum to a power of 2), proves a general "forest"
  sub-lemma `D(m,r)≥τ_m` for odd `r` by strong induction on `m`
  (the key new structural fact: every genuine tree split produces children
  in pairs, so the remainder's top-level multiplicity is *automatically*
  odd at every recursion level — the missing reachability information the
  abstract vector formalism lacked). This closes the partial-budget,
  `M`-even sub-case left open by `lemmas/parity-pair-anchor.md`, and more
  strongly, works for any budget whatsoever. **Independently reviewer-
  verified**: from-scratch Python enumeration of every `(m,r)`-forest for
  `m=1..3` and the full original anchor-only problem for `n=1,2,3`
  (depth-3 search), zero violations, minimum `D` exactly `t_n` in every
  case; also confirmed the odd-`r` hypothesis is load-bearing (even `r` at
  `m=1` gives `D=0<1`). Certified. **Gap (b) (cross-piece tied free
  coordinates): genuine partial progress, not closed.** New PAIR-CANCEL
  identity (a 2-way cross-tie's net contribution to `D` is exactly `0`)
  plus a precisely-identified remaining obstruction (a piece's sole free
  coordinate is not a genuinely free continuous parameter in the discrete
  game — needs a discrete-move argument, not completed this round).
  Honestly reported as open. **CHANGES REQUESTED.** Prior rounds:
  independently verified new Lemma PARITY-PAIR-GENERAL (`lemmas/parity-pair-
  general.md`, strictly generalizes the certified Lemma PARITY-PAIR by
  dropping the "every anchor appears" hypothesis `c_i≥1`, proved by the
  identical strong induction — re-derived and exhaustively cross-checked,
  `n=1..6`, zero violations) and Lemma PARITY-PAIR-ANCHOR
  (`lemmas/parity-pair-anchor.md`, closes the anchor-only sub-case of the
  tail-refined lower bound **unconditionally for every full-budget strategy**
  — total piece count is always `2n+1`, odd, so PARITY-PAIR-GENERAL applies
  directly; worked `n=4` example independently recomputed, `D=3≥1` ✓). Also
  proves Lemma V'-GEN (multi-free-coordinate vertex reduction) in the
  "well-separated" case (product-polytope decomposition into independent
  per-piece LP-vertex problems, reusing the certified Lemma V mechanism) —
  a valid, correctly-scoped argument. Two precisely-isolated gaps remain,
  honestly flagged, not hand-waved: (a) partial-budget anchor-only
  strategies (`M` even — the abstract parity statement is provably false in
  general, so this needs game-reachability, not just abstract combinatorics);
  (b) cross-piece tied free coordinates (two free coordinates from different
  split pieces, no anchor between them — mechanism identified, not worked
  out). This is genuine, verified progress narrowing the remaining
  lower-bound gap; **CHANGES REQUESTED**, not yet closing Lemma
  PARITY-PAIR-GEN. Prior rounds:
  the same reduction/construction; fully closes `n=1` (all `k`); derives
  `c(n)=2λ_n c(n-1)`; proves the alternating-sum toolkit (D-REFORM, D-BOUND,
  D-INSERT, V'). **Round 5: Lemma L (the reduced combinatorial claim for the
  `k=n`, tail-untouched, pure-anchor sub-case) fully PROVED for every `n`**
  via Lemma PARITY-PAIR (independently re-derived and verified by the
  reviewer, 1,000,000+ trial cross-check). **Round 6: no proof produced.**
  The round-6 build (report lost to the interrupted round, file edit
  verified directly against the diff) only added a *skeleton/plan* section
  for the assigned target, Lemma PARITY-PAIR-GEN (`k=2` tail-refined) —
  Case A is restated from already-existing Claim-★ work, Case B (the odd
  tying-block case, the genuinely new content) is explicitly flagged as not
  worked out. No new theorem was proved this round; status is unchanged
  from round 5. Remaining gaps (honestly and precisely stated): (a) the
  "one free coordinate" vertex case of Lemma V' — **now closed, see
  `geometric-dominance-construction` below**; (b) extending from "tail
  untouched" (`k=n` only) to general `k<n` with the tail simultaneously
  adversarially refined (unchanged, fully open, still only a plan); (c) the
  upper bound over arbitrary configurations (out of scope for this
  approach).
- `geometric-dominance-construction` — worked (partial). **Round 9:**
  Lemma TWO-BLOCK (fully general, no geometric structure) plus a
  Structural Lemma identifying the two globally-largest merged elements
  closes the same minority-part/deep-bracket residue sub-case as
  `recursive-embedding-induction`'s round-9 route, but via a direct
  two-block `D`-BOUND estimate at the tie value itself — independently
  re-derived and stress-tested from scratch (exact `Fraction`, `n=1..6`,
  dense `v`-grids), zero violations, genuinely different mechanism from
  the sibling approach's forest/tree route (mandatory reconciliation
  check: no disagreement on any tested witness). **Reviewer caveat (round
  9, CHANGES REQUESTED): same scope limitation as the sibling approach**
  — the Main Theorem covers only ONE shared tie-value `v` across one
  subset `S` (one cluster); it does not address two-or-more simultaneous
  independent tie-clusters at different values, and this is not flagged
  in the file. My own multi-cluster stress test found no counterexample,
  but this is numerical evidence, not proof — flagged for next round
  alongside the sibling approach's identical gap. **Round 8:**
  second, independent route to gap (b) (cross-piece tied free coordinates).
  New certified Lemma CROSS-TIE-AFFINE (`lemmas/cross-tie-affine.md`): for
  `k≥2` mutually tied free coordinates from distinct split pieces, `D` is
  affine in the shared tie value on each anchor-free interval (via repeated
  D-INSERT), so an interior tie is never a strict local minimizer — the
  minimum sits at an interval endpoint. Also proves the "self-meeting-point
  is an anchor" fact (`top_π/2` is always itself an anchor, one line from
  `t_i=2t_{i+1}`), which resolves the tie in the "majority part of a
  2-part piece" and "≥3-part piece" sub-cases (the latter reproducing
  `recursive-embedding-induction`'s already-closed well-separated case as
  `k=1`). **Independently reviewer-verified**: built an independent `n=3`
  cross-tie example from scratch (exact `Fraction`), confirmed `D(v)` is
  exactly piecewise-affine (constant on one anchor-free interval, slope
  `-1` on the next) with the minimum at the endpoint, matching the lemma
  exactly. **Honest residual gap, narrower than before**: when the tied
  coordinate is the *minority* part of a 2-part piece in a bracket deeper
  than that piece's own halving level, the winning endpoint can leave the
  companion at a non-anchor residue value — not resolved this round (one
  non-competitive `n=5` numeric probe only). **Reconciliation check
  performed as mandated**: compared against `recursive-embedding-
  induction`'s parallel round-8 tree-peeling route to the same gap — no
  disagreement, both independently reach the same closed sub-cases.
  **CHANGES REQUESTED.** Prior rounds: worked (partial, genuine milestone
  round 6). Proves `k=0` (Proposition A), `k=1` tail-untouched (Lemma
  F1), and `k≤1` with simultaneous tail-splitting (unconditional `n≤2`,
  conditional on M(n-1) for general `n`). Claim ★ proved FALSE for `s≥3`.
  Round 5: exact exchange-move formula (Lemma X) and certified move-traps
  ruling out the bounded-width single-exchange mechanism; imports Lemma L
  by reference from `recursive-embedding-induction`. **Round 6: proves the
  "one free coordinate" vertex case of Lemma V' in full, for every `n≥1`**
  (`lemmas/lemma-V-prime-free-coordinate.md`), by composing the certified
  Lemma D-INSERT (affineness of `D` in the free coordinate on each
  anchor-bracket interval) with Lemma PARITY-PAIR applied unconditionally at
  both bracket endpoints (each endpoint is automatically a valid
  pure-anchor `m=n+1` instance, `n+m=2n+1` always odd, no dependence on the
  dropped value constraint), plus an integrality argument ruling out the
  `(0,t_n)` bracket. **Independently re-derived and hand-verified by the
  reviewer this round** on concrete `n=3` examples (both the `j=0`
  unbounded-bracket case and an interior-bracket convex-combination case),
  matching the file's own exhaustive `18,283`-point computational check —
  **this closes Proposition K (the `k=n`, tail-untouched sub-case of the
  lower bound) completely, for every `n≥1`, not merely its pure-anchor
  part.** Its unique remaining scope is `k<n` with the tail simultaneously
  refined (owned by `recursive-embedding-induction`, not attempted here).
- `universal-adversary-strategy` — worked (partial). **Round 9: `m=3`'s
  general upper bound is now `solved` in full, unconditionally over every
  configuration** — independently re-derived and re-checked from scratch:
  the corrected closed form for `BLOCK-RECURSE_1` (`L0={r,p3}`, fixing a
  round-8 labelling bug that had used `{p2,r}`), the full Case-C algebra
  (`min(TAIL-SNIP,BLOCK-RECURSE_1)≤4/7` throughout `p_1<1/2`), and a
  fresh 3,000-trial exact-`Fraction` random search over `p_1<1/2` (zero
  violations) all reproduce exactly — including both worked examples
  (`0.5875/0.55` and the round-9-corrected `0.525/0.525`) and the extremal
  point `(3/7,2/7,2/7)` giving `4/7=4/7` exactly. Also proves new, fully
  general Lemma PAIR-VALUE (`lemmas/pair-value.md`, hypothesis-free value
  identity for arbitrary tied pairs, no contiguity needed) —
  independently re-verified (5,000 random trials) and its SUBSET-DOM
  corollary's construction on the falsifying witness
  `A=(12,6,5,4,2)/29` independently recomputed to give exactly
  `oddrank=1/2<c(4)=16/31` (beating the old menu's `15/29>c(4)`), matching
  the file's claim exactly. **Correctly and honestly does NOT claim
  general `m≥4` Case C is closed** — the Hall's-theorem existence question
  for a general donor/subset match remains genuinely open, precisely as
  reported. No errors found this round. **CHANGES REQUESTED** (general
  `m≥4` still open). **Round 8:** proves
  Lemma BLOCK-RECURSE (`lemmas/block-recurse.md`, general `m`, any tail
  shape, any recursion depth — splitting a value never increases the
  resulting parts, so the duplicated PARTIAL-DOM block always occupies
  exactly the top `2j` ranks no matter how deeply the leftover is further
  recursively refined, giving `oddrank(block∪W)=S_j+oddrank(W)`
  unconditionally in `W`; strictly generalizes PARTIAL-DOM /
  PARTIAL-DOM-RESIDUAL) and Lemma THRESHOLD-REDUCTION
  (`lemmas/ptbi-threshold-reduction.md`, general `m` — a new algebraic
  identity `c(k-1)=c(k)/(2(1-c(k)))` combined with peel+halve+IH closes
  `p_1≥c(m-1)Σ`, and Lemma DOM directly closes `Σ/2≤p_1<c(m-1)Σ`, together
  reducing Claim PTBI's inductive step to the single case `p_1<Σ(A)/2` for
  every `m≥2`). **Independently reviewer-verified**: BLOCK-RECURSE's
  identity checked with a from-scratch exact-`Fraction` randomized
  verifier, 1856 trials (random `m=3..6`, random valid `j`, random
  recursive refinements to depth 3), zero mismatches; THRESHOLD-REDUCTION's
  algebraic identity and the `g(c(m-1)Σ)=c(m-1)Σ` boundary computation
  independently re-derived and confirmed exactly for `k,m=1..9`. For `m=3`
  specifically, further narrows the remaining case `p_1<Σ/2` down to
  `p_3>Σ/7` (small residual region; general `m≥4` remains fully open in
  this case). **CHANGES REQUESTED.** Prior rounds: worked (partial).
  Proves Lemma DOM
  (generalized domination, any tail shape) and Lemma HALVE (halving
  reduction, any tail shape); fully closes `n=1` for every configuration.
  Round 5: Lemma DOM-boundary-slack, Lemma SPLIT, Lemma TAIL-SNIP; refutes
  TAIL-SNIP-alone on `A=(4649,3042,2309)/10000`, `n=2`. **Round 6: proves
  two new lemmas, plus a correction to the round-5 record.** *Correction:*
  the round-5 witness above does **not** need a coordinated 2-piece move —
  a single-piece split of `p_1` at a non-half tie-inducing ratio closes it
  with 1 mark to spare (independently confirmed this round: `minimax-mixed-
  duality`'s Lemma SANDWICH gives the same value, `0.5351`, by a different,
  more general single-mark construction — cross-checked and consistent).
  **Lemma TIE-NECESSARY**: proved and independently checked this round —
  **the interior/`dim(Q)≥1` branch (via the certified Lemma D) is sound**,
  but **the `dim(Q)=0` branch's proof is flawed**: it claims a 0-dimensional
  cell must arise from a collapsed chain-simplex boundary (forcing condition
  (a), a zero-length piece), but a 0-dim cell can equally arise purely from
  independent order-tie constraints (condition (b)) with no zero-length
  piece at all — a concrete scenario (e.g. two independent ties pinning a
  2-mark, single-piece-split polytope to a point) shows this. **The lemma's
  disjunctive conclusion "(a) or (b)" still holds** (condition (b) covers
  the gap), so the *certified statement* survives, but the write-up needs a
  correction to the `dim(Q)=0` case before being fully airtight — flagged
  for next round, not blocking. **Lemma PARTIAL-DOM**: proved in full and
  **independently re-derived and hand-verified by the reviewer this round**
  on the exact `m=5` witness (`A=(4859,3439,884,496,322)/10000`, `j=2`,
  budget-capped case) — reproduces `oddrank=5181/10000` exactly by direct
  computation, confirming the closed-form `D(B)=D(U)+(-1)^e[r-2D(U_{>e})]`
  even in the "budget-capped, `r≥U_1`" regime the file's own Remark
  under-claims coverage of (the actual requirement is `r<t_j`, not the
  stricter `r<U_1` the Remark states — a minor scoping imprecision, not an
  error). Applying both lemmas together correctly (and honestly) shows the
  even-`m` "two-independent-ties" regime is not yet closed by either lemma
  or their combination. **Round 7: two new certified lemmas plus two write-up
  fixes, all independently verified.** Lemma MULTI-HALVE
  (`lemmas/multi-halve.md`, simultaneous top-`K` halving) and Lemma
  PARTIAL-DOM-RESIDUAL (`lemmas/partial-dom-residual.md`, composes
  PARTIAL-DOM with SPLIT on the residual) both reproduce their claimed
  witness values exactly (`Fraction`-verified independently:
  `10709/20000` and `10687/20000`). Lemma DOUBLE-INSERT
  (`lemmas/double-insert.md`, hypothesis-free generalization of Lemma HALVE:
  inserting a duplicated value always changes `oddrank` by exactly `+v`,
  unconditionally) independently re-verified by 3,000 fresh random exact
  trials, zero mismatches. The Lemma TIE-NECESSARY `dim(Q)=0` proof gap
  (flagged last round) is now correctly fixed — replaced with a standard
  "at least one defining inequality must be tight at an extreme point"
  argument, giving (a) or (b) directly with no false unconditional claim.
  Lemma PARTIAL-DOM's Remark scope correction (`r<t_j`, not `r<U_1`) checks
  out algebraically. **Task 3 (retargeted matching/assignment induction,
  Claim PTBI):** the general induction is honestly **not** closed (the naive
  scalar IH fails algebraically at the "IH tight, `p_1` minimal"
  combination), but the mandated stress test — "peel `p_1`, solve the tail
  independently for its own true optimum, then unconditionally halve `p_1`
  via Lemma DOUBLE-INSERT" — was independently reproduced (via `scipy`
  optimization + exact `Fraction` merge) on both mandated hard `m=5`
  witnesses, matching the claimed values `0.51065` and `0.50225` exactly.
  This genuinely refutes the round-7 explorer's "irreducible 3-piece
  coordination needed" diagnosis **for the purpose of proving the upper
  bound** (though the true optimum on Witness 1 does still need
  coordination). Real, verified progress; the general upper-bound induction
  remains open. **CHANGES REQUESTED.**
- `minimax-mixed-duality` — new round 6. Opened per the
  outline-reviewer's shared-gap-plateau rule to attack the upper bound via
  minimax/LP duality over Xiang Yu's mixed strategy space, a genuinely
  different proof shape from every other live approach. **First build pass:
  the LP-duality framing itself did not yield a shortcut** (honestly
  diagnosed: "find good mixing weights" reduces to the same casework
  `universal-adversary-strategy` is already doing). However the mandated
  exploratory numeric search surfaced a genuinely new, general, correctly
  proved construction: **Lemma SANDWICH** (`lemmas/sandwich-split.md`,
  1-mark straddle-split of `p_1` for odd piece-count `m`, hypothesis
  `p_1<p_2+p_m`), **independently re-derived and hand-verified by the
  reviewer this round** by direct rank-shift computation and exact
  substitution on the `A=(4649,3042,2309)/10000` witness (reproduces
  `oddrank=0.5351` exactly, matching and superseding
  `universal-adversary-strategy`'s round-5 two-piece-coordination finding on
  the same witness — a genuine, useful correction, not a duplicate). Even-`m`
  and full menu-coverage (only ~74% of a sampled `m=3` space covered by
  `{DOM,HALVE,TAIL-SNIP,SANDWICH}`) remain honestly open. **Round 7: gate
  check against the two mandated hard `m=5` witnesses succeeded numerically
  (both exact-value claims, `5009/10000` and `2009/4000`, independently
  reproduced — Witness 1's construction needs locating the correct
  flat-direction window for `p_1`'s split ratio, confirmed genuinely
  nonempty), but the underlying duality-certificate technique produced
  **no independent proof leverage for the second consecutive round** (6 and
  7): every construction found reduces to an explicit instance of
  `universal-adversary-strategy`'s own discrete tie-search (the proposed,
  uncertified Lemma TIE-MIN-HALVE is a mechanical generalization of that
  approach's PARTIAL-DOM-RESIDUAL). No `A`-independent dual certificate was
  found or evidenced to exist. **This is a genuine, well-documented
  convergence, not a failed round** — the file itself recommends evaluation
  for retirement/merge. **RETHINK**: per CLAUDE.md's diversity rule, this
  framing needs either a genuinely new dual object next round or should be
  retired/folded into `universal-adversary-strategy` as a
  construction-contributor rather than kept alive as a nominally-independent
  proof shape that has stopped producing independent leverage.
- `relaxed-adversary-transfer` — new this round (round 7), per the
  outline-reviewer's plateau-break instruction to put a genuinely different
  framing on the table: relax Xiang Yu's mark budget to unlimited, solve the
  relaxed game exactly, attempt to transfer down. **Result: a rigorous,
  complete dead end, correctly reported as such rather than forced into
  `partial`.** Theorem V-INF (`V_∞(A)=1/2` for every configuration `A`,
  proved both directions — Lemma PAIR-LB for the lower bound, an explicit
  "halve every piece" construction for the upper bound) independently
  re-verified exactly on 5 configurations (3 geometric, 2 non-geometric),
  matching `1/2` in every case. The three-part structural diagnosis
  (config-independence; the relaxed optimum needs `n+1` marks, one more than
  the real budget; and critically, `V_∞` **lower**-bounds — not
  upper-bounds — the real `≤n`-mark value, the wrong direction for this
  target) is correct: relaxing the adversary's budget makes it strictly
  *stronger*, so a bound against the relaxed adversary says nothing useful
  about the real, weaker one. The natural salvage ("halve `n` of the `n+1`
  pieces, leave one whole") was independently re-verified to fail on
  `n=1, A=(4/7,3/7)` (`5/7 > c(1)=2/3`, reproduced exactly). **RETHINK,
  cleanly recorded**: this is not a failure of the round's build effort but
  a legitimate negative result ruling out the relax-the-mark-budget
  mechanism entirely; the slug should not be re-attempted along this axis.
- `potential-averaging-bound` — worked (partial; round 5). Tests, per
  the outline-reviewer's mandatory feasibility gate, whether averaging two
  simply-defined "cascading DOM/HALVE" candidates can bound Xiang Yu's true
  optimum without exact-minimizer casework. **Result: the gate fails.**
  Built three natural candidate strategies (cascade-DOM, cascade-HALVE,
  always-halve) and found an exact-fraction counterexample
  (`A=(1/3,1/3,1/3)`, `n=2`) where **every** candidate (and hence every
  pairwise average) gives `2/3 > c(2)=4/7`, even though the true optimum
  (using only 1 of the 2 available marks) is `1/2 < c(2)`. Independently
  re-derived and verified exactly by the reviewer (all three candidate
  computations reproduce `2/3` exactly; the true 1-mark response gives
  `1/2` exactly). Diagnosed the root cause: every tested candidate is
  budget-blind (always spends a mark when a local hypothesis fires, never
  "stops early"), and averaging two candidates that are both individually
  forced above the bound cannot produce an average at or below the bound.
  Produced one small reusable lemma (dual-objective shift under an untouched
  maximum). **Assessment (this round):** this is real, verified negative
  progress — not a dead end in the strict sense (no proof that *no* pair of
  simply-defined candidates can ever work), but the file's own diagnosis
  shows that repairing it would require a "budget-aware" candidate whose
  definition already resolves the same optimal-stopping decisions that
  `universal-adversary-strategy`'s direct casework is built to make — i.e.
  a genuine fix would likely collapse this approach into a duplicate of that
  one. Kept as `partial` (not downgraded to `RETHINK`) this round because
  the impossibility argument is a plausibility diagnosis from 3 tested
  candidates, not a structural proof of impossibility (unlike
  `majorization-smoothing`'s genuine convexity-obstruction proof); but
  flagged for the next round: if a further attempt at a "budget-aware third
  candidate" also collapses into duplicating `universal-adversary-strategy`,
  this approach should then be retired as duplicative per the CLAUDE.md
  diversity rule, not kept alive indefinitely as a near-copy.
- `majorization-smoothing` — RETHINK / dead-end, confirmed rigorously
  (round 4, unchanged this round). Structural non-concavity obstruction
  (min of an affine and a genuinely convex piece) proved, not just a bare
  numeric counterexample. Kept as a documented negative result only; not
  revived this round (correctly not re-attempted).
- `equalization-potential-bound` — stagnant since round 1 (conditional
  impossibility argument, not independently closed). Not touched this
  round.

## Current best
Shared foundation (certified, see `lemmas/`): Lemma 1 (claiming-phase
value), geometric configuration facts (top-piece domination,
self-similarity, Proposition 4), interior-point linear obstruction,
top-split lemmas (Lemma S, Lemma F1), generalized domination and halving
(Lemma DOM, Lemma HALVE), merge-by-sums counterexample, insertion and
abstract reduction (Lemma I, Claim ★ `s≤2` + `s≥3` counterexample),
alternating-sum toolkit (D-REFORM, D-BOUND, D-INSERT, V'),
concavity-failure-and-n2-k1-value.

**Round 5, all independently reviewer-verified:**
- `lemmas/parity-pair-lemma-L.md` — Lemma PARITY-PAIR and Lemma L, fully
  proved for every `n`: the `k=n`, tail-untouched, pure-anchor sub-case of
  the lower bound.
- `lemmas/exchange-move-and-trap.md` — Lemma X and a certified negative
  result (move-traps ruling out bounded-width single-exchange-move).
- `lemmas/split-and-tail-snip.md` — Lemma DOM-boundary-slack, Lemma SPLIT,
  Lemma TAIL-SNIP, and a certified negative result (TAIL-SNIP alone
  insufficient for the "neither DOM nor HALVE" regime).
- `lemmas/dual-objective-shift.md` — small general reusable fact.

**NEW this round (round 6), all independently reviewer-verified (this
catch-up review), except where flagged:**
- `lemmas/lemma-V-prime-free-coordinate.md` — **Lemma FC (the "one free
  coordinate" vertex case of Lemma V'), fully proved for every `n≥1`**,
  composing the certified D-INSERT and PARITY-PAIR lemmas. **Combined with
  Lemma L, this fully closes Proposition K** (the `k=n`, tail-untouched
  lower-bound sub-case) — the single biggest advance of the round.
- `lemmas/sandwich-split.md` — **Lemma SANDWICH, fully proved**: a new,
  general, hypothesis-`p_1<p_2+p_m` single-mark straddle-split for odd
  piece-count configurations, independently verified, strictly outside the
  DOM/HALVE/TAIL-SNIP menu and superseding a round-5 "needs 2 coordinated
  marks" diagnosis on the same witness.
- `lemmas/tie-necessary.md` — Lemma TIE-NECESSARY, converts Xiang Yu's
  optimization to a finite search over ties/degeneracies. **The stated
  disjunctive conclusion is correct and reusable, but the `dim(Q)=0`
  sub-case of the proof needs a fix** (see "Approaches tried" above) —
  flagged, not blocking, since condition (b) already covers that branch.
- `lemmas/partial-dom.md` — Lemma PARTIAL-DOM, fully proved and
  independently verified (including in the "budget-capped" regime its own
  Remark had flagged as unverified — confirmed to work there too).

**NEW this round (round 7), all independently reviewer-verified:**
- `lemmas/parity-pair-general.md` — **Lemma PARITY-PAIR-GENERAL, fully
  proved**: strictly generalizes Lemma PARITY-PAIR by dropping the `c_i≥1`
  hypothesis (allows some anchor values to be entirely absent from the
  merged multiset), same induction technique, exhaustively re-verified
  `n=1..6`.
- `lemmas/parity-pair-anchor.md` — **Lemma PARITY-PAIR-ANCHOR, fully proved
  for every `n≥1` and every full-budget anchor-only strategy** (any `k`, any
  tail distribution) — closes the anchor-only sub-case of the tail-refined
  lower bound whenever Xiang Yu spends his entire budget. Partial-budget
  case (`M` even) precisely isolated as open, not closed.
- `lemmas/multi-halve.md` — **Lemma MULTI-HALVE, fully proved**: simultaneous
  top-`K` halving, strictly generalizing Lemma HALVE.
- `lemmas/double-insert.md` — **Lemma DOUBLE-INSERT, fully proved**:
  hypothesis-free generalization of Lemma HALVE (duplicated-value insertion
  changes `oddrank` by exactly `+v`, unconditionally).
- `lemmas/partial-dom-residual.md` — **Lemma PARTIAL-DOM-RESIDUAL, fully
  proved**: mechanical composition of PARTIAL-DOM and SPLIT, closes a
  concrete previously-open witness.
- `lemmas/tie-necessary.md` — `dim(Q)=0` proof gap **fixed** (statement
  unchanged, now airtight).
- `lemmas/partial-dom.md` — Remark scope **corrected** (`r<t_j`, not
  `r<U_1`).

The conjectured answer `c(n) = 2^n/(2^{n+1}-1)` remains numerically confirmed
for small `n`, `n=1` is fully closed both directions, the lower bound's
`k=n` sub-case (tail-untouched, every vertex type) is a genuine closed
theorem for every `n`, the tail-refined lower bound's anchor-only,
full-budget, well-separated sub-case is fully closed (round 7), and — new
this round (round 8) — the anchor-only sub-case is now closed
**unconditionally for every budget** (Lemma TREE-BOUND, subsuming the
round-7 full-budget-only result).

**NEW this round (round 8), all independently reviewer-verified:**
- `lemmas/tree-bound-anchor.md` — **Lemma TREE-BOUND, fully proved**:
  every anchor-only strategy (any budget, any `M` parity) satisfies
  `D(B)≥t_n`, via a binary-subdivision-tree reachability argument (forced
  halving of powers of 2) and a "forest" sub-lemma with automatic odd
  top-level multiplicity at every recursion depth. **Fully closes gap (a)**
  (partial-budget anchor-only, `M` even) — strictly more than requested.
- `lemmas/block-recurse.md` — **Lemma BLOCK-RECURSE, fully proved**:
  general `m`, any tail shape, any recursion depth — the duplicated
  PARTIAL-DOM block always occupies the top `2j` ranks regardless of how
  deeply the leftover is further recursively refined, giving
  `oddrank(block∪W)=S_j+oddrank(W)` unconditionally. Strictly generalizes
  PARTIAL-DOM / PARTIAL-DOM-RESIDUAL.
- `lemmas/ptbi-threshold-reduction.md` — **Lemma THRESHOLD-REDUCTION,
  fully proved**: a new algebraic identity `c(k-1)=c(k)/(2(1-c(k)))`
  combined with peel+halve+IH and Lemma DOM together reduce Claim PTBI's
  inductive step to the single case `p_1<Σ(A)/2`, for every `m≥2`.
- `lemmas/cross-tie-affine.md` — **Lemma CROSS-TIE-AFFINE, fully proved**:
  a second, independent route to gap (b) — `D` is affine in a cross-piece
  tied value on each anchor-free interval, so an interior tie is never a
  strict local minimizer; plus the "self-meeting-point is an anchor" fact.
  Narrows gap (b) to a precisely-isolated minority-part/deep-bracket
  residue sub-case, cross-checked against `recursive-embedding-induction`'s
  independent tree-peeling route to the same gap (no disagreement found).

**NEW this round (round 9), independently reviewer-verified from scratch
(fresh re-implementations, not the builders' own scripts), with one
caveat flagged below:**
- `lemmas/tree-bound-residual.md` — **Lemma TREE-BOUND-RESIDUAL**: extends
  Sub-lemma ODD with a third induction case for one forced-residual leaf.
  Reviewer independently re-implemented the forest-with-one-impurity
  construction from the lemma's own definitions and exhaustively checked
  `m=1..4,r=3`: `D≥t_m` in every case, confirming the closure for the
  single-cluster minority-tie residue.
- `lemmas/two-block-residue-close.md` — **Lemma TWO-BLOCK + Structural
  Lemma**: an independent, direct two-block `D`-BOUND route to the same
  residue sub-case. Reviewer independently rebuilt the configuration space
  from scratch (`n=1..6`, dense `v`-grids, exact `Fraction`): `D≥t_n` in
  every sampled case, no disagreement with the sibling route.
- `lemmas/pair-value.md` — **Lemma PAIR-VALUE** (`universal-adversary-
  strategy`): hypothesis-free tied-pair value identity. Reviewer
  independently re-verified by 5,000 fresh random trials (arbitrary
  interleaving, forced value coincidences) — zero mismatches — and
  independently recomputed the `m=5` witness construction
  (`A=(12,6,5,4,2)/29`) to reproduce `oddrank=1/2<c(4)` exactly.
- **`universal-adversary-strategy`'s `m=3` Case C closure**: reviewer
  independently re-derived the corrected `BLOCK-RECURSE_1` closed form and
  reran the full algebra plus a fresh 3,000-trial exact-`Fraction` search
  over `p_1<1/2` — zero violations, extremal point exact. `m=3`'s general
  upper bound is genuinely `solved` in full.

**Reviewer caveat on gap (b) (round 9, load-bearing — see "Open gaps"
below): both TREE-BOUND-RESIDUAL and TWO-BLOCK, as written, cover only a
single tie-cluster/impurity in the whole configuration; the simultaneous-
multiple-cluster case is not addressed by either proof and was not flagged
by either builder.** The reviewer's own stress test (2–4 simultaneous
independent minority-tied splits, `n` up to 6, dense grids) found no
violation, but this is numerical evidence, not a proof — gap (b) is
**not yet unconditionally closed**, downgraded from the builders'
"fully closed" claim pending a multi-cluster generalization or a proved
WLOG single-cluster reduction.

**Open gaps, revised after round-10 review — LOWER BOUND NOW FULLY CLOSED:**
1. **Lower bound, general case — CLOSED IN FULL (round 10).** Proposition K
   (`k=n`, tail untouched) fully closed (round 7). Gap (a) [partial-budget
   anchor-only] fully closed (round 8). **Gap (b) [cross-piece tied free
   coordinates], including the multi-cluster case flagged open by round 9's
   review, is now fully closed** by `recursive-embedding-induction`'s new
   Lemma TREE-BOUND-MULTICLUSTER (`lemmas/tree-bound-multicluster.md`),
   independently re-verified this round (see Status note above — proof
   mechanism re-derived, not just the numeric conclusion). **"`A_n`'s value
   equals `c(n)` for every `n≥1`" — the overall minimax lower bound,
   `c(n) ≥ 2^n/(2^{n+1}-1)`, obtained from the single configuration `A_n`
   — is now a fully proved, gap-free theorem. Do not re-open or re-attempt
   this gap in future rounds.**
2. **Upper bound over arbitrary (non-geometric) Liu Bang configurations,
   general `n≥2`** — this is the separate, unconditionally-still-open
   piece establishing `c(n) ≤ 2^n/(2^{n+1}-1)` (no configuration beats
   `A_n`); it is **not** subsumed by gap (b)'s closure, which concerns only
   the lower-bound instance `A_n`. `n=1` fully closed (Lemma DOM/HALVE),
   and — new this round — **`m=3` (`n=2`) is now fully closed
   unconditionally** (Case A/B via Lemma THRESHOLD-REDUCTION, round 8; Case
   C via the corrected `BLOCK-RECURSE_1`/`TAIL-SNIP` algebra, round 9,
   independently reviewer-verified). The casework toolkit now includes DOM,
   HALVE, MULTI-HALVE, PARTIAL-DOM, PARTIAL-DOM-RESIDUAL, TAIL-SNIP,
   SANDWICH, DOUBLE-INSERT, BLOCK-RECURSE, and the new hypothesis-free
   Lemma PAIR-VALUE (strictly generalizing BLOCK-RECURSE to arbitrary,
   non-prefix subset matches). **General `m≥4` Case C remains fully
   open** — Lemma PAIR-VALUE's SUBSET-DOM corollary closes the one known
   concrete falsifying witness but a general existence theorem (which
   donor/subset match always works, needing Hall's marriage theorem for
   simultaneous non-conflicting multi-donor matches) is not established.
   **Round 12: sharpened, still open.** Candidate 5 (budget-capped
   TAIL-SNIP recursion) is well-founded (Lemma WF-C5, certified) and
   passes an extensive independently-reproduced adversarial gate
   (`m=4..14`+, two structural families to `m=20`, thousands of random
   trials — reviewer independently reran with a fresh implementation,
   matched exactly). The sharper sufficient target Lemma HALF-BOUND
   (`solve_full(A)≤Σ(A)/2` throughout Case C) is strongly evidenced
   (zero violations, every test) but its proof is NOT complete — the
   next builder should attack exactly the "tail locally dominant"
   sub-case (a non-top-level piece exceeds half its own remaining sum,
   so repeated Move-1 halving alone overshoots; Move 2/3 must do the
   work but no inductive argument covers this yet), possibly via the
   Hall-deficient-set-deletion technique from crux `aimo-0063` as the
   round-12 plan flagged but did not reach.
   **Round 13 CORRECTION (important, read before reusing anything above):
   the "adversarial gate PASS" reported in round 12 is RETRACTED as
   evidence for Claim PTBI.** It checked `solve_full(A)≤c(m-1)Σ(A)` using
   the *uncapped* `solve(A,budget)` recursion, but that recursion's
   `budget` parameter does not track Xiang Yu's true total mark count
   (Move 1/2 never decrement it, Move 3 grants an uncounted extra mark) —
   independently confirmed by the reviewer (witness `A=(26,21,10)`: the
   recursion's winning path uses `3` real marks against a true budget of
   `2`). Since more moves for the minimizing player (Xiang Yu) can only
   make the computed value smaller or equal, a "PASS" against the
   over-generous recursion is evidence in the WRONG direction and proves
   nothing about the true, correctly mark-capped game. **Lemma WF-C5
   itself is unaffected** (it only proves termination, never claimed to
   model real marks). The sharper HALF-BOUND identity is furthermore
   independently REFUTED on the corrected model (same witness: true
   2-mark value is `31≠28.5=Σ/2`) — though Claim PTBI's actual (weaker)
   target `≤c(2)Σ=228/7≈32.57` still holds there. **Do not cite the
   round-12 gate PASS in any future round; any future numeric sweep must
   use a properly mark-capped model** (either an exhaustive per-witness
   continuous optimizer, as the reviewer used this round, or a corrected
   recursion — but note even the "corrected" `solve2` with the current
   contiguous-prefix-only Move 2 menu is *itself* an underestimate of
   Xiang Yu's true power in general: it can report a value exceeding the
   target [as it did on witness `T=(0.20,0.15,0.12,0.08)`, `28>27.5`] even
   though the true optimum meets the target exactly via a non-contiguous
   subset match `solve2`'s menu cannot express — so a `solve2` "failure"
   is not evidence the theorem is false, only that the menu is
   insufficient to prove it). **The real missing piece, now confirmed
   unavoidable even in the "easy" Case (a), remains exactly the long-
   flagged (rounds 9/11/12) Hall-type general subset-matching existence
   theorem for Lemma PAIR-VALUE** — this is the sharpest, most concrete
   target for round 14.
3. **`minimax-mixed-duality`'s duality-certificate framing** has produced no
   independent proof leverage for two consecutive rounds and is flagged for
   the outline-reviewer to either redirect to a genuinely new dual object or
   retire/merge into `universal-adversary-strategy`.

## Full proof
(Not present — Status is `partial`: the lower bound is now a complete,
gap-free theorem (round 10, see Status note above), but the general upper
bound over arbitrary Liu Bang configurations — general `m≥4` Case C of
`universal-adversary-strategy`'s Claim PTBI induction — remains open.
Round 9's main advances, all
independently reviewer-verified from scratch: gap (b)'s minority-part/
deep-bracket residue sub-case is closed for the single-cluster case by two
independent mechanisms (Lemma TREE-BOUND-RESIDUAL, Lemma TWO-BLOCK) — but
the reviewer identifies and flags a genuine, narrower residual gap neither
builder addressed: **the simultaneous-multiple-tie-cluster case is not
covered by either written proof**, so gap (b), and hence the full lower
bound `c(n)≥2^n/(2^{n+1}-1)` via `A_n`, is not yet unconditionally closed
(strong numerical evidence it holds, no proof yet). Separately,
`universal-adversary-strategy`'s general upper bound is now fully closed
for `m=3` (`n=2`), independently re-verified exactly; general `m≥4` Case C
remains fully open, with a new, more powerful, hypothesis-free tool (Lemma
PAIR-VALUE) in hand but no general existence theorem. Round 8's main
advances: **gap (a) of the lower bound is now fully closed** (Lemma
TREE-BOUND, unconditional for every mark budget). Round 7's main advances:
the anchor-only, full-budget, well-separated sub-case of the tail-refined
lower bound is fully closed (PARITY-PAIR-GENERAL + PARITY-PAIR-ANCHOR +
V'-GEN well-separated + peeling induction); the upper-bound casework
toolkit grew by three more certified lemmas (MULTI-HALVE, DOUBLE-INSERT,
PARTIAL-DOM-RESIDUAL) plus two write-up fixes, and a stress test refutes a
"3-piece coordination" concern on the two hardest known witnesses for the
purposes of the upper bound (though not for the true optimum).
`relaxed-adversary-transfer` is a rigorous, cleanly-recorded dead end
(RETHINK) — the relax-the-mark-budget mechanism is structurally ruled out.
`minimax-mixed-duality` has converged with
`universal-adversary-strategy` for a second consecutive round with no
independent leverage, and is flagged for redirection or retirement next
round; the matching/assignment question for the upper bound remains the
sharpest open sub-problem.)
