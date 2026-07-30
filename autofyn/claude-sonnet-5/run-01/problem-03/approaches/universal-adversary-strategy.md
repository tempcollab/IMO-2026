## Status
partial

## Approaches tried
- `universal-adversary-strategy` (round 16 build, `m=4` Case C 5-strategy
  closure). Task (per the round-16-v2 outliner, approved by the
  outline-reviewer): carry out the full `min(StratA,StratB,StratC_{12},
  StratC_{13},StratC_{23})<=c(3)\Sigma(A)` case split for `m=4` Case C. **Result:
  genuine, fully rigorous partial closure — a clean two-way algebraic
  partition of Case C is proved in full, reducing the previously
  wide-open ~15-way case split to one precisely isolated residual region;
  that residual region is not yet closed by hand algebra, though it is
  backed by strong exact-`Fraction` and adversarial-search evidence and one
  fully worked illustrative sub-example.** See "Round 16 build" section
  below for the complete write-up, including the two proved lemmas
  (Lemma V3-BOUND-LOOSE, Lemma REGION-A / REGION-B closures) and the
  precise statement of the open residual region. **CHANGES REQUESTED /
  still open** — `m=4` Case C is narrowed substantially but not fully
  closed this round.
- `universal-adversary-strategy` (round 15 build). Task (per the round-15
  outline-reviewer, "Round 15 plan" section): (1) prove Lemma MARKS-MONO
  (`solve2(A,k)` non-increasing in mark budget `k`); (2) use it to
  decouple the joint covering+value form of Lemma SLACK-COVER and attempt
  the `aimo-0292`-style scalar peel-induction, targeted at the `m=4`
  witness family `T=(0.20,0.15,0.12,0.08)` (not `m=8`, confirmed by the
  round-15 explorer to be an implementation-only stall). **Result: (1) is
  now fully proved (Lemma MARKS-MONO, general, unconditional); (2)
  surfaced a genuinely new reframing of the whole open gap, backed by an
  exact counterexample, but the general `m=4` case is not yet given a
  complete case-by-case proof — honestly reported as strong,
  multiply-cross-checked evidence, not a closure.** Specifically: I found
  that the ALREADY-CERTIFIED contiguous-only menu (BLOCK-RECURSE / Move 1
  / Move 3 / Move 0 — no non-contiguous subset matching, no open
  existence question needed) already meets the ACTUAL Claim PTBI target
  `c(m-1)\Sigma(A)` at `m=4` on every configuration tested (thousands of
  random trials plus adversarial `scipy.optimize.differential_evolution`
  + Nelder–Mead searches, `m=3,4,5`), with the extremal configuration
  found and verified EXACTLY: `A=(6,5,4,2)/17`, contiguous-only value
  `9/17`, target `c(3)=8/15`, margin exactly `1/255>0` — i.e. the
  once-pursued sharper Lemma HALF-BOUND (`\le\Sigma/2`) was a
  strictly-stronger-than-necessary target, and its round-13/14
  counterexample (`T=(0.20,0.15,0.12,0.08)`, contiguous value `7/25=0.28`
  exceeding `\Sigma(T)/2=0.275`) does **not** refute the real target
  (`0.28\le c(3)\Sigma(T)=0.2933\overline{3}`, confirmed exactly this
  round: `7/25\le 44/150`). **However**, I also found and exactly
  verified (via `fractions.Fraction`, no floating-point involved) that
  this same contiguous-only bypass **genuinely fails at `m=6`**:
  `A=(14,12,10,9,8,4)` (`\Sigma=57`, Case C since `14<43`) gives
  contiguous-only value `29`, strictly exceeding target
  `c(5)\Sigma=608/21\approx28.952` by exactly `1/21`; the FULL
  subset-matching menu (implemented and run independently this round)
  achieves exactly `57/2=28.5\le608/21` on the same instance, confirming
  the target *is* achievable there, but only via a genuine non-contiguous
  subset match — i.e. Lemma SLACK-COVER's existence question is **not
  avoidable in general**, even though it may be avoidable specifically at
  `m=4`. **Net effect: the whole-problem gap is sharpened, not closed —
  a genuinely new sub-question is isolated ("is the contiguous-only menu
  already sufficient for small/fixed `m`, even where it fails to hit
  HALF-BOUND?") with strong exact evidence for `m=4` but disproof at
  `m=6`, so it does not eliminate the need for Lemma SLACK-COVER for the
  general theorem.** Full detail, all exact witnesses, and the honest
  gap statement in the new "Round 15 build" section below. **CHANGES
  REQUESTED / still open** — Case C for general `m\ge4` remains
  unsolved; `m=4` specifically is very likely closeable by a
  case-exhaustive proof using only already-certified machinery, but that
  proof was not completed this round.
- `universal-adversary-strategy` (round 13 build). Task: verify the
  outline-reviewer's numeric finding that plain Move 1 (no Move 2/3)
  already closes Case (b) (tail-dominant), fix the flagged Move-3-budget
  bug, and try to close Lemma HALF-BOUND in full. **Result: the
  reviewer's narrow numeric claim is independently reproduced, but a
  materially deeper, previously-undetected flaw was found underneath
  it, and the round does NOT close HALF-BOUND — it sharpens the gap to
  a precise, different location.** Full detail in the new "Round 13
  build" section below. Summary:
  1. Independently re-implemented `solve(A,budget)` exactly per the
     certified Round-12 definition (`fractions.Fraction`, from scratch)
     and reproduced the reviewer's finding: plain Move 1 (recursing
     `p_1/2+solve(tail(A),1)`, i.e. no direct Move 2/3 at the top level)
     does achieve `<=Sigma(A)/2` on every sampled Case-(b) instance.
  2. Traced *why*, and found the true mechanism is **not** "Move 1 alone,
     to the bottom" (a pure Move-1 chain to a raw singleton overshoots by
     `p_m/2`, as the file already documents) — it is Move 1 telescoping
     down through several levels until hitting a level where Move 2 or
     Move 3 closes the residual gap exactly. This is fine as a *value*
     statement, but tracing the actual number of elementary splits
     (marks) used along that path exposed a **genuine, previously
     unflagged bug in the Round-12 `solve(A,budget)` formalization
     itself**: `budget` there counts only *nested Move-3 (tail-snip)
     uses*, not total real marks — Move 1 and Move 2 never decrement it.
     Concretely, for the `m=6` hereditary-dominant-tail example built
     this round (`A=(0.40,0.35,0.15,0.07,0.02,0.01)`, genuine Case C:
     `p_1=0.40<Sigma/2=0.50`), the `solve`-optimal path traced explicitly
     uses **6** elementary splits (one at every level: 5 halvings plus 1
     tail-snip) while the real Xiang-Yu budget for a 6-piece configuration
     is only `m-1=5` marks — **one mark over budget**, exactly matching
     the pattern "every Move-3 use silently grants one extra free real
     mark, because it increases piece count without being charged
     against any real-mark counter anywhere in the recursion."
  3. Built the corrected, real-marks-respecting recursion `solve2(A,
     marks)` (every move — Move 1, Move 2, Move 3 alike — decrements the
     *same* pool of remaining real marks; Move 2's cost is `j^*` marks,
     or `j^*-1` at the exact-tie boundary `r=0`, per the certified Lemma
     DOM-boundary-slack) and re-ran the gate with `marks=|A|-1` (the true
     Xiang-Yu budget) instead of the Round-12 `budget` parameter.
     **Genuinely dominant (non-Case-C) `m=3` configurations correctly
     FAIL to reach `Sigma/2` under this corrected accounting** (found
     `A=(0.51,0.30,0.19)`: `solve2(A,2)=0.51>0.50`, matching an
     independently-run `scipy` continuous-optimizer brute force over the
     *actual* constrained game, which also found `0.51` as the true
     2-mark optimum and `0.50` only reachable with `3` marks) — this
     is the correct, expected behavior (HALF-BOUND was never claimed
     outside Case C) and confirms `solve2` is a faithful model where the
     old `solve` was not.
  4. **However, `solve2` then found a genuine counterexample to the
     outline's Case (a) closure itself** (previously believed to need
     no proof beyond "Move 1 + IH", the *easy* half of the case split):
     for `A=(0.45,0.20,0.15,0.12,0.08)` (top-level Case C, and tail
     `(0.20,0.15,0.12,0.08)` **is** Case-C-for-itself, i.e. genuinely
     Case (a)), `solve2(\text{tail},3)=7/25=0.28`, **strictly exceeding**
     the target `Sigma(\text{tail})/2=11/40=0.275` — even the tail's own
     recursive value, using the *correct* real-mark budget `|tail|-1=3`
     and the full Move-1/2/3 menu, fails to reach half its own sum.
     Independently cross-checked against a `scipy` continuous-optimizer
     brute force over the *actual* unrestricted game on this exact tail:
     the true optimum is `0.275` (matching the target exactly) but is
     achieved with only **2** marks, via a construction **not expressible
     in the Move-1/2/3 menu at all**: split `p_1=0.20` at the *non-half*
     ratio `(0.12,0.08)` — tying it exactly with the tail's own existing
     elements `0.12` and `0.08` (a **non-contiguous subset match**, in the
     sense of the already-certified but existence-unproven Lemma
     PAIR-VALUE / SUBSET-DOM, not a contiguous PARTIAL-DOM prefix) —
     while *independently* halving `p_2=0.15` into `(0.075,0.075)`
     (an ordinary Move-1 step). Move 2 as currently formalized only ever
     matches a **contiguous prefix** of the tail against `p_1`; it cannot
     express "match `p_1` against the non-adjacent pair `{0.12,0.08}`
     while skipping `0.15`."
  5. **Conclusion (honest, sharpened diagnosis, not a closure).** The
     gap is *not* (only) the specific "no spare Move-3 mark" bug the
     outline-reviewer flagged for Case (b) — that bug is real but is a
     symptom of a broader modeling error (conflating nested-tail-snip
     count with real marks) that also silently affected the Round-12
     adversarial-gate "PASS" and this round's outline's Case (a) claim.
     Once marks are correctly accounted for (`solve2`), the **already-
     certified Move-1/Move-2(contiguous)/Move-3 menu is demonstrably
     insufficient** even for Case (a) — the true fix requires the
     **general subset-matching existence question** (Lemma PAIR-VALUE's
     Hall-type existence claim: does some non-contiguous donor subset of
     the tail always exist to tie `p_1`, possibly combined with
     independent recursive treatment of the untouched remainder?) that
     multiple prior rounds (9, 11, 12) already identified as the
     deepest unresolved question in this whole approach and were never
     able to close. This round does not close it either, but narrows
     *where* it is needed (it is not avoidable even in the "easy" Case
     (a), contrary to what the round-13 outline assumed) and supplies a
     new, concrete, exact-`Fraction`-verified witness
     (`A=(0.45,0.20,0.15,0.12,0.08)`, `m=5`, tail
     `(0.20,0.15,0.12,0.08)`) that any future subset-matching existence
     proof must handle. **CHANGES REQUESTED / still open** — Case C for
     general `m\ge4` remains unsolved; the round-12/13 "solve(A,budget)"
     recursive framework needs to be replaced by the corrected
     `solve2(A,\mathrm{marks})` accounting before any further gate run or
     proof attempt is trusted.
- `universal-adversary-strategy` (round 12 build). Executed the round-12
  plan's mandatory gate and formalization steps against Candidate 5
  (budget-capped TAIL-SNIP recursion). **Well-foundedness fully proved**
  (Lemma WF-C5, correcting the outline's `(|A|,\mathrm{budget})`
  measure-order bug to `(\mathrm{budget},|A|)` lexicographic with
  `\mathrm{budget}` primary, per the outline-reviewer's required fix, and
  proving the `j^*\ge1` fact explicitly rather than assuming it).
  **Mandatory adversarial gate independently re-run and PASSES**: no
  counterexample found by `differential_evolution` (`m=4..14`, multiple
  restarts, exact-`Fraction` rationalization of every near-boundary
  point), by two independent structural adversarial families
  (near-uniform-tail, nested near-half geometric chain, both exact
  `Fraction` out to `m=20`/`m=12`), or by a `3{,}709`-trial random Case-C
  sweep — `budget=2` fallback not triggered since no near-miss appeared.
  **Discovered a materially sharper reformulation, Lemma HALF-BOUND**
  (`\mathrm{solve\_full}(A)\le\Sigma(A)/2` throughout Case C, strictly
  simpler than tracking `c(m-1)` inside the induction, and — via the
  already-proved fact `c(k)>1/2` for all `k` — sufficient to close Case C
  with an exact closed-form strict margin `\Sigma(A)/(2(2^m-1))` if
  proved). Zero violations found across every test performed. **General
  proof of HALF-BOUND is not complete**: the natural pure-Move-1
  (halving-only) induction closes one sub-case but provably does not
  cover the case where a non-top-level tail piece is itself locally
  dominant relative to its own remaining sum; this precise gap is
  honestly isolated, not closed. See "Round 12 build" section below for
  full detail. **CHANGES REQUESTED / still open** — Case C for general
  `m\ge4` narrowed and sharpened, not closed.
- `universal-adversary-strategy` (round 12 plan). Target: Claim PTBI's
  Case C for general `m\ge4` — the sole remaining gap for the whole
  problem. This round's three explorers converged on a concrete,
  substantially stronger candidate than any prior round's: an adaptive
  3-move menu (peel+halve / PARTIAL-DOM maximal-prefix match / TAIL-SNIP)
  that survives 3600+ random trials, both known hard witnesses, and every
  boundary family tried — but has one genuine, exactly-verified
  counterexample at `m=8` (margin `\approx-1.53\times10^{-4}`, found by
  `scipy.optimize.differential_evolution`). A follow-up explorer diagnosed
  the *exact* cause (not a matching defect — ruled out non-contiguous
  subset matching by brute force over all `127` tail subsets) and
  identified the fix: let a PARTIAL-DOM leftover's own recursive solve
  gain **one extra, budget-capped TAIL-SNIP call**. See "Round 12 plan"
  section below for the precise formalization, the mandatory
  adversarial-stress-test gate (must run BEFORE any proof attempt,
  per the same method that found the `m=8` counterexample), and the
  conditional next steps depending on the gate's outcome.
- `universal-adversary-strategy` (round 11). Target: check whether
  `recursive-embedding-induction`'s certified Lemma TREE-BOUND-MULTICLUSTER
  (lower-bound side) reuses to close Case C's existence question (Route A),
  else attempt Route B properly generalized to `\ge2` simultaneous
  top-level pairs, guided by the round-11 explorer's exact reconstruction of
  the `m=5` hard witness's true optimum. **Result: both routes ruled out,
  with proof, not just failed search.** Route A: a genuine structural
  mismatch, not a numeric failure — TREE-BOUND-MULTICLUSTER is a
  universal-over-responses bound for one fixed geometric config (opposite
  quantifier direction from Case C's exists-a-response-for-every-config
  need), and its proof mechanism (discrete power-of-2 anchor lattice,
  forced-depth telescoping) has no analogue for Case C's arbitrary reals —
  argued in full in the "Round 11 build" section below. Route B generalized
  to exactly two fixed top-level pairs: algebraically correct bookkeeping
  (verified on the round-10/11 `m=5` witness, works there), but **refuted as
  a universal construction** by an exact `Fraction` counterexample family
  (near-uniform tail, `p_1\to1/2^-$) violating the target for every `m` from
  `4` to `100` tested — proved via `c(k)` strictly decreasing plus an
  explicit margin computation, not merely observed. That same witness is,
  honestly, easily closed by the already-certified Lemma PARTIAL-DOM (an
  adaptive-length chain, not a fixed pair count), so the round's diagnosis
  is sharpened, not worsened: no fixed small integer number of top-level
  pairs is universal; a correct construction needs a config-dependent
  selection rule. **CHANGES REQUESTED / still open** — Case C for general
  `m\ge4` not closed this round either.
- `universal-adversary-strategy` (round 10). Target: close Claim PTBI's
  Case C (`p_1<\Sigma(A)/2`) for general `m\ge4`, testing the Fact-0
  reformulation first, falling back to a Hall-type existence argument.
  **Result: genuine progress, Case C for general `m\ge4` NOT closed.**
  Two new lemmas certified in full (Lemma ALL-BUT-MIN, Lemma
  MATCH-TAIL-PAIR, both one-line corollaries of the certified Lemma
  PAIR-VALUE, each closing a further explicit sub-region of Case C for
  every `m`). Found and fixed a bug in an exploratory test harness that had
  produced a false "cross-piece ties needed beyond the matching framework"
  alarm — corrected, the matching framework remains structurally adequate
  as far as tested. Proved a general structural fact showing every
  naive single-peel-plus-IH construction is provably too weak for Case C
  (not just numerically observed). Found a concrete `m=5` witness showing
  the two new lemmas together still do not close Case C. See "Round 10"
  section below for full detail. **CHANGES REQUESTED / still open.**
- `universal-adversary-strategy` (round 8). Target (per the round-8
  outliner): formalize and prove **Lemma BLOCK-RECURSE** (the recursive
  generalization of PARTIAL-DOM/PARTIAL-DOM-RESIDUAL the round-8 explorer
  found, numerically verified but not proved) and carry out the strong
  induction on piece-count `m` for **Claim PTBI** (the general upper bound
  over arbitrary configurations), using the finite candidate menu
  `{BLOCK-RECURSE, peel+halve, MULTI-HALVE, TAIL-SNIP, SANDWICH}`.
  **Result: Lemma BLOCK-RECURSE is now PROVED IN FULL** (general `m`, any
  tail shape — see `lemmas/block-recurse.md`), and a genuinely new, fully
  proved **Lemma THRESHOLD-REDUCTION** (`lemmas/ptbi-threshold-reduction.md`)
  reduces Claim PTBI's inductive step to a single remaining case,
  `p_1 < \Sigma(A)/2`, via a clean algebraic identity
  `c(k-1)=c(k)/(2(1-c(k)))` proved for every `k`. **The remaining case
  (Case C) is not closed in general**; substantial partial progress and a
  precise diagnosis are recorded below. Full Claim PTBI is **not** proved
  this round — Status remains `partial`. See "Round 8" section below for
  the complete write-up.
- `universal-adversary-strategy` (round 5). Target: the joint `(m,r)`-indexed
  cascading DOM/HALVE induction proposed by this round's outline, using the
  new DOM-boundary-slack budget fact and addressing the "near-tied top two"
  case flagged by this round's explorer. **Proved DOM-boundary-slack in
  full** (trivial but load-bearing: Lemma DOM's `r=0` boundary case needs
  only `k-1` marks, not `k` — see below). **Proved a genuinely new, fully
  general lemma (Lemma SPLIT)**: an exact closed-form for the change in
  `oddrank` from splitting *any* single element `a_i` of a sorted list into
  two equal halves (not just the top element `p_1` as in Lemma HALVE),
  together with its unconditional corollary **Lemma TAIL-SNIP** (`i=m`, the
  smallest element: splitting it always *decreases* `oddrank` by exactly
  `a_m/2` when the current piece-count `m` is odd, with **no domination
  hypothesis needed at all** — this is new mechanism, not previously in the
  file). Used exact-`Fraction` numerics (3000+ random trials per `n=1..4`,
  restricted to the region where neither DOM's nor HALVE's hypothesis
  fires) to test whether Lemma TAIL-SNIP alone closes the "neither DOM nor
  HALVE fires" gap for odd `m`: **it does not** — found 773/3000 exact
  violations at `n=2` alone (smallest: `A≈(0.4649,0.3042,0.2309)`,
  `TAIL-SNIP value = 11607/20000 = 0.58035 > c(2)=4/7≈0.57143`). Followed up
  with a finer numeric optimum search (grid search over all ways to spend
  the full `2`-mark budget on this exact counterexample): the true optimum
  (`≈0.535 < c(2)`) is achieved not by TAIL-SNIP but by splitting **both**
  `p_1` and `p_2` simultaneously at specific (non-half, non-domination)
  ratios that make the four resulting pieces pair up closely with each
  other and with `p_3` (`0.2988,0.2914 | 0.2309,0.1735 | 0.00545`) — i.e.
  the correct move here is a coordinated two-piece split that is not an
  instance of DOM, HALVE, or TAIL-SNIP as currently formalized. This
  confirms and sharpens (rather than resolves) the explorer's "near-tied
  top two" finding: the true obstruction is not specific to the *smallest*
  piece, and no single-piece move (DOM, HALVE, or TAIL-SNIP) suffices in
  general — the correct strategy in this regime genuinely requires
  splitting **two pieces jointly** with jointly-optimized (non-half) split
  ratios, which is a strictly harder mechanism than anything proved so far
  in this approach. This is reported honestly as an unresolved gap, not
  papered over; see "Current best" and "Dead ends" below for the precise
  status.
- `universal-adversary-strategy` (round 2, unchanged this round below).
  Target: prove
  `max_A min_B oddrank(B) ≤ c(n) = 2^n/(2^{n+1}-1)` for **every** Liu Bang
  configuration `A` (not just the geometric `A_n`), completing the
  upper-bound half of the minimax jointly with the lower-bound work in
  `geometric-dominance-construction.md` / `recursive-embedding-induction.md`.
  The outline-reviewer numerically falsified the originally-proposed Lemma J
  ("shave the top piece down to match the current second piece, repeat") on
  the skewed config `(0.9977, 0.00223, 0.0000518)`, `n=2`: that rule gives
  `oddrank ≈ 0.993 ≫ c(2) ≈ 0.571`. This round replaces the falsified rule
  with a genuinely different, fully proven construction (the **Generalized
  Domination Lemma** below, proven for *every* tail shape, not just the
  geometric one), and derives a second, independently proven reduction (the
  **Halving Identity**). Both are correct and reusable, and together they
  fully settle `n = 1` and a large structural sub-case for general `n`
  (`S ≤ p_1 ≤ c(n)`, where `S := Σ_{i≥2}p_i`). Extensive numerical testing
  (`scipy` Nelder–Mead over free split parameters, `python3 fractions.Fraction`
  exact arithmetic for verification) was used throughout to test every
  proposed rule against adversarial configurations (including the
  outline-reviewer's exact falsifying example) **before** committing to a
  written argument — several plausible-looking combination rules were tried
  and refuted this way (see "Dead ends" below) before landing on the two
  lemmas below, which are numerically robust wherever they apply. The
  remaining regimes (`p_1 > c(n)Σ` in a way not reducible by one halving
  step, and `p_1 < S`) are **not closed**; see "Current best" for the precise
  open gap and why the natural combination rules tried so far fail.

- `universal-adversary-strategy` (round 6). Target: prove the two lemmas
  skeletoned by the round-6 outliner (Lemma TIE-NECESSARY, Lemma
  PARTIAL-DOM) and use them, plus the matching/assignment framing for even
  `m`, to push on the general-`n` upper bound. **Both lemmas proved in
  full** (not just numerically): Lemma TIE-NECESSARY (any global minimizer
  of Xiang Yu's response can be taken to have a zero-length split or an
  exact adjacent-rank tie — proved directly from the already-certified
  Lemma D applied to each finite polytope "cell" of the response space,
  full proof in `lemmas/tie-necessary.md`) and Lemma PARTIAL-DOM (exact
  closed-form `D(B)`/`oddrank(B)` for the "tie `p_1` down through a
  tail-prefix chain" response family, generalizing the certified Lemma DOM
  from full-tail domination to prefix domination, via the certified
  `D-INSERT`/`D-REFORM` toolkit; full proof in `lemmas/partial-dom.md`).
  Both independently verified by exact-`Fraction` computation (TIE-NECESSARY:
  affine-on-cell claim checked on 3,892 points across 36 cells, zero
  mismatches, plus a concrete grid-search global minimum landing exactly on
  a boundary point exhibiting *both* a zero-length piece and a tie
  simultaneously; PARTIAL-DOM: 5,000 random trials plus an exact match to
  the round-6 explorer's worked `m=5` numeric optimum, `5181/10000`).
  **Used both together to test whether the even-`m` "matching" framing
  closes the general upper bound: it does not, yet.** Confirmed numerically
  (exact `Fraction`) that on the round-5 explorer's own `m=4` witness
  (`A=(0.3374,0.2589,0.242,0.1617)`, budget `2`), the maximal single-piece
  PARTIAL-DOM chain on `p_1` (`j=1`, tying `p_2`) gives `oddrank=0.5794`,
  **identical** to the untouched baseline (zero improvement — confirming
  TIE-NECESSARY correctly predicts a tie is needed, but PARTIAL-DOM's
  natural "greedy contiguous chain" instantiation of that tie is
  parity-cancelled and therefore the *wrong* tie), while the true optimum
  `≈0.5009` requires **two independent, non-adjacent single-piece ties**
  (`p_1` ties `p_3`, skipping `p_2`; `p_2` independently ties `p_4`) — a
  genuine matching between {pieces to split} and {tail targets to tie with}
  that is not a contiguous PARTIAL-DOM chain and not reducible to one. This
  is a precise, honest negative result, not a vague one: it shows the two
  new lemmas **narrow** the search (by TIE-NECESSARY) to a finite
  discrete space of tie-structures and give an **exact value** for one
  natural family of tie-structures (by PARTIAL-DOM), but neither lemma, nor
  their combination, yet identifies *which* tie-structure (of the
  now-finitely-many candidates) is globally optimal in general — that
  remains a genuine open combinatorial/matching problem, precisely
  localized rather than diffuse. **Did not attempt** the cross-approach
  transfer of `recursive-embedding-induction`'s certified Lemma
  PARITY-PAIR to this matching problem this round (flagged by the outliner
  as the natural next step); this is recorded as unstarted, not
  attempted-and-failed, for the next round.

- `universal-adversary-strategy` (round 7). Target (per the round-7
  outliner): (1) certify two cheap compositional lemmas the round-7
  explorer found (**Lemma PARTIAL-DOM-RESIDUAL**, **Lemma MULTI-HALVE**);
  (2) fix the flagged `dim(Q)=0` gap in Lemma TIE-NECESSARY's proof
  write-up; (3) retarget from "grow the menu" to a direct induction
  attempt on the matching/assignment theorem, stress-tested against the
  two hard `m=5` witnesses the explorer recorded. **All three closed with
  genuine content, though (3) remains open — see below.** (1): both
  compositional lemmas certified in full
  (`lemmas/multi-halve.md`, `lemmas/partial-dom-residual.md`), each a
  short, direct proof from already-certified machinery (Lemma SPLIT, Lemma
  PARTIAL-DOM, the DOM/HALVE rank-shift technique), independently
  reproduced exactly (`Fraction` arithmetic) against the explorer's own
  numeric witnesses. (2): `lemmas/tie-necessary.md`'s `dim(Q)=0` paragraph
  rewritten to derive "(a) or (b)" directly from the cell's defining
  constraints (at least one must be tight at an extreme point, of either
  type), replacing the incorrect unconditional "(a) only" claim; the
  lemma's statement was never wrong, only that one proof branch — fixed,
  no regression. **Also corrected `lemmas/partial-dom.md`'s Remark**
  (actual scope is `r<t_j`, not the stricter `r<U_1` nor "`j` maximal",
  confirmed by a genuine sub-maximal-`j` witness this round). (3): the
  induction attempt itself **did not close**, but surfaced a genuinely new,
  general, fully-proved lemma (**Lemma DOUBLE-INSERT**,
  `lemmas/double-insert.md`: inserting a duplicated value `\{v,v\}` into
  *any* sorted list changes `oddrank` by exactly `+v`, unconditionally —
  strictly generalizing Lemma HALVE by removing its domination hypothesis)
  and a precise, numerically-grounded diagnosis of exactly where the
  natural "peel `p_1`, recurse independently on the tail" induction shape
  breaks down (it is **not** the multi-piece-coordination obstruction the
  explorer's report anticipated — both `m=5` witnesses are in fact closed
  by a simple non-coordinated construction — but a *different*, deeper
  obstruction tied to how small `p_1` can be forced to be relative to the
  tail sum). Full details in the new "Round 7" section below.

## Current best

### Round 16 build: `m=4` Case C, 5-strategy closure — two regions proved, one residual open

**Scope.** Per the round-16-v2 outline (approved by the outline-reviewer),
this targets Claim PTBI's Case C (`p_1 < \Sigma(\mathrm{tail})`, equivalently
`p_1<\Sigma(A)/2`) specifically for `m=4`, using the finite, hypothesis-free
5-strategy menu
```
V_4(A) := \min(\mathrm{StratA},\mathrm{StratB},\mathrm{StratC}_{12},
               \mathrm{StratC}_{13},\mathrm{StratC}_{23}),
```
each recursing into the already-fully-certified `m=3` theorem `V_3`
(round 9, "`m=3`'s general upper bound is now solved in full,
unconditionally over every configuration", combined with
`lemmas/ptbi-threshold-reduction.md`'s Case A/B). Throughout, write
`A=(p_1\ge t_1\ge t_2\ge t_3>0)`, `\Sigma:=\Sigma(A)=p_1+t_1+t_2+t_3`. By
homogeneity (every strategy's value and the target `c(3)\Sigma` scale
identically under `A\mapsto\lambda A`), we normalize nothing but keep
`\Sigma` symbolic throughout (no loss of rigor from not fixing `\Sigma=1`).
Case C: `p_1<\Sigma/2`. Target: `c(3)\Sigma=\tfrac{8}{15}\Sigma`.

**The five constructions (unchanged from the outline, re-stated exactly).**
All use Lemma DOUBLE-INSERT (`lemmas/double-insert.md`, hypothesis-free:
inserting a duplicated pair `\{v,v\}` into *any* sorted list shifts
`oddrank` by exactly `+v`) for the "tie" step, and the certified `m=3`
theorem `V_3` for the recursive tail:
```
StratA        = t_1 + V_3(t_2,t_3,r),   r:=p_1-t_1\ (\ge0,\text{ since }p_1\ge t_1)
StratB        = p_1/2 + V_3(t_1,t_2,t_3)
StratC_{12}   = t_2 + V_3(p_1,t_3,r),   r:=t_1-t_2\ (\ge0)
StratC_{13}   = t_3 + V_3(p_1,t_2,r),   r:=t_1-t_3\ (\ge0)
StratC_{23}   = t_3 + V_3(p_1,t_1,r),   r:=t_2-t_3\ (\ge0)
```
Each costs exactly `1` (the split) `+\ (\le2)` (`V_3`'s own budget)
`\le3=m-1` marks, matching the budget exactly (independently re-verified
this round, `fractions.Fraction`, against the outline's stated recursive
triples — no bookkeeping discrepancy found).

**`V_3`'s exact form (imported verbatim, not re-derived — see round 9 above
and `lemmas/ptbi-threshold-reduction.md`).** For a sorted triple `(x\ge
y\ge z>0)`, `\sigma_3:=x+y+z`:
```
V_3(x,y,z) = x/2+L_2(y,z)          if x \ge c(2)\sigma_3=\tfrac47\sigma_3   (Case A)
           = x                     if \sigma_3/2 \le x < \tfrac47\sigma_3  (Case B)
           = \min(x+z/2,\ y+L_2(x-y,z))   if x<\sigma_3/2                  (Case C)
```
where `L_2(u,v)` (for two positive reals, `M:=\max(u,v),\,m:=\min(u,v)`) is
the already-fully-closed `m=2` (`n=1`) theorem:
```
L_2(u,v) = M     if M \le 2m     (Lemma DOM)
         = M/2+m if M > 2m       (Lemma HALVE / DOUBLE-INSERT)
```

**Lemma V3-BOUND (imported, not re-derived; the content of the round-9
"`m=3` solved in full" result, restated as an unconditional inequality).**
*For every sorted triple `(x\ge y\ge z>0)`, `V_3(x,y,z)\le c(2)\,\sigma_3
=\tfrac47(x+y+z)`, with no case restriction — i.e. all three of `V_3`'s
branches individually satisfy this bound.*

*Proof (re-derivation from the round-9 write-up's own steps, to make this
usable as a clean black box here).* Case B: `\sigma_3/2\le x<\tfrac47
\sigma_3` is literally the defining range, so `V_3=x<\tfrac47\sigma_3`
directly. Case A: by `lemmas/ptbi-threshold-reduction.md`'s Case-A
argument applied at `m=3` (`k=1$ recursive budget on the pair `(y,z)`):
`g(x):=x/2+c(1)(\sigma_3-x)` is strictly decreasing in `x` (slope
`1/2-c(1)=1/2-2/3=-1/6<0`), and `g(\tfrac47\sigma_3) = \tfrac47\sigma_3/2 +
\tfrac23\cdot\tfrac37\sigma_3 = \tfrac27\sigma_3+\tfrac27\sigma_3
=\tfrac47\sigma_3`, so for `x\ge\tfrac47\sigma_3`,
`V_3=x/2+L_2(y,z)\le x/2+c(1)(y+z) = g(x)\le g(\tfrac47\sigma_3) =
\tfrac47\sigma_3` (using `L_2(y,z)\le c(1)(y+z)=\tfrac23(y+z)` — the
already-fully-closed `n=1` theorem's own bound, since `L_2` IS the exact
`n=1$ optimal-response value). Case C: exactly the content proved in the
"Round 9" section above (`min(TAIL-SNIP,BLOCK-RECURSE_1)\le c(2)\sigma_3=
\tfrac47\sigma_3` throughout `x<\sigma_3/2`, Steps 1–3 of that proof), with
equality approached (and attained at the single point `(x,y,z)\propto
(3,2,2)`). `\blacksquare`

**Corollary (loose recursive bound, used repeatedly below).** For any
sorted triple, `V_3(x,y,z)\le\tfrac47(x+y+z)` unconditionally; likewise
`L_2(u,v)\le\tfrac23(u+v)` unconditionally (the `n=1$ theorem itself).

#### Region 1: `t_1 \ge \tfrac{4}{15}\Sigma` — closed by Strategy A alone

**Claim.** If `t_1\ge\tfrac4{15}\Sigma`, then `\mathrm{StratA}\le c(3)\Sigma
=\tfrac8{15}\Sigma`.

**Proof.** By Lemma V3-BOUND applied to the triple `(t_2,t_3,r)`
(`r=p_1-t_1`, any sorted order — `V_3`-BOUND holds regardless of which of
`t_2,t_3,r` is largest, since it only depends on the triple's sum):
```
\mathrm{StratA} = t_1+V_3(t_2,t_3,r) \le t_1 + \tfrac47(t_2+t_3+r).
```
Since `r=p_1-t_1`, `t_2+t_3+r = t_2+t_3+p_1-t_1 = (p_1+t_1+t_2+t_3)-2t_1 =
\Sigma-2t_1`. So
```
\mathrm{StratA} \le t_1+\tfrac47(\Sigma-2t_1) = \tfrac47\Sigma +
t_1\Big(1-\tfrac87\Big) = \tfrac47\Sigma - \tfrac{t_1}7.
```
This right-hand side is (affine, hence) **strictly decreasing** in `t_1`,
and at `t_1=\tfrac4{15}\Sigma` it equals
```
\tfrac47\Sigma-\tfrac17\cdot\tfrac4{15}\Sigma = \Sigma\Big(\tfrac47-
\tfrac4{105}\Big) = \Sigma\cdot\tfrac{60-4}{105} = \Sigma\cdot\tfrac{56}{105}
= \Sigma\cdot\tfrac{8}{15} = c(3)\Sigma
```
exactly (direct arithmetic: `\tfrac47=\tfrac{60}{105}`,
`\tfrac1{7}\cdot\tfrac4{15}=\tfrac4{105}`, `60-4=56`, `\tfrac{56}{105}=
\tfrac{8}{15}` since `\gcd(56,105)=7`, `56/7=8`, `105/7=15`). Hence for
`t_1\ge\tfrac4{15}\Sigma`, monotonicity gives
`\mathrm{StratA}\le\tfrac47\Sigma-\tfrac{t_1}7 \le c(3)\Sigma`. `\blacksquare`

This bound is **tight**: it is met with equality exactly when `t_1=
\tfrac4{15}\Sigma$ (the boundary of Region 1) *and* Lemma V3-BOUND's own
Case-C branch is tight, i.e. `(t_2,t_3,r)\propto(3,2,2)`. Independently
re-verified this is exactly what happens at the outline-reviewer's exact
extremal witness `A=(6,4,3,2)`: `\Sigma=15`, `t_1=4=\tfrac4{15}\cdot15`
exactly (Region 1's boundary, included in the closed region since the
claim above is `\ge`), and `\mathrm{StratA}=8=c(3)\cdot15` exactly
(re-verified via the exact-`Fraction` script `/tmp/v3def.py` this round,
matches `current.md`'s independently-reported value).

#### Region 2: `t_1<\tfrac4{15}\Sigma` and the tail `(t_1,t_2,t_3)` is itself in `V_3`'s Case B — closed by Strategy B alone

**Step 2a (the tail can never be in `V_3`'s Case A here).** Write
`S_{\mathrm{tail}}:=t_1+t_2+t_3=\Sigma-p_1`. Since Case C at the top level
gives `p_1<\Sigma/2$, `S_{\mathrm{tail}}=\Sigma-p_1>\Sigma/2$. Hence
```
\tfrac47 S_{\mathrm{tail}} > \tfrac47\cdot\tfrac\Sigma2 = \tfrac27\Sigma.
```
Since `\tfrac27=\tfrac{30}{105}>\tfrac{28}{105}=\tfrac4{15}$ (direct
fraction comparison, `\mathrm{lcm}(7,15)=105$), we get
`\tfrac47S_{\mathrm{tail}}>\tfrac27\Sigma>\tfrac4{15}\Sigma`. So whenever
`t_1<\tfrac4{15}\Sigma$ (Region 2's own defining hypothesis), automatically
`t_1<\tfrac47S_{\mathrm{tail}}`, i.e. the tail triple `(t_1,t_2,t_3)` (with
its own sum `S_{\mathrm{tail}}`) **never** satisfies `V_3`'s Case-A
threshold `t_1\ge\tfrac47S_{\mathrm{tail}}`. So throughout Region 2, the
tail triple is in `V_3`'s Case B or Case C only — this is an unconditional
consequence of Case C at the top level plus `t_1<\tfrac4{15}\Sigma`, proved
directly, not assumed.

**Step 2b (Region 2 proper: tail additionally in Case B, i.e.
`t_1\ge S_{\mathrm{tail}}/2$).** Then `V_3(t_1,t_2,t_3)=t_1` exactly (Case
B is a raw DOM value, no recursion, no bound needed — it is the *exact*
value, certified in `lemmas/ptbi-threshold-reduction.md`'s Case B). So
```
\mathrm{StratB} = p_1/2+V_3(t_1,t_2,t_3) = p_1/2+t_1.
```
Now use the two available strict bounds: `p_1<\Sigma/2$ (Case C hypothesis)
and `t_1<\tfrac4{15}\Sigma$ (Region 2's defining hypothesis). Both strict,
so
```
\mathrm{StratB} = p_1/2+t_1 < \tfrac\Sigma4+\tfrac4{15}\Sigma =
\Sigma\Big(\tfrac{15}{60}+\tfrac{16}{60}\Big) = \tfrac{31}{60}\Sigma <
\tfrac{32}{60}\Sigma = \tfrac{8}{15}\Sigma = c(3)\Sigma.
```
So `\mathrm{StratB}<c(3)\Sigma$ **strictly**, with margin at least
`\tfrac1{60}\Sigma` uniformly over all of Region 2. `\blacksquare`

**Independent numerical re-verification of Regions 1 and 2 (this round).**
`200{,}000` random integer Case-C `m=4` trials (`fractions.Fraction`,
script reproduced at `/tmp/v3def.py` / the region-check script this
round), restricted to the union of Region 1 and Region 2 as defined above:
**zero violations** of `\mathrm{StratA}\le c(3)\Sigma$ (Region 1) or
`\mathrm{StratB}\le c(3)\Sigma$ (Region 2) — consistent with, and an
independent numeric confirmation of, the closed-form algebra above (which
is unconditional and does not itself depend on the numerics; the numerics
serve only as a sanity check that no algebra error was made).

#### Region 3 (residual): `t_1<\tfrac4{15}\Sigma` and the tail is in `V_3`'s Case C — OPEN, not closed this round

By Step 2a, whenever `t_1<\tfrac4{15}\Sigma$ the tail triple is in Case B
or Case C (Case A is impossible); Region 2 above handles Case B. The
**one remaining region** is
```
\text{Region 3: } p_1<\Sigma/2,\quad t_1<\tfrac4{15}\Sigma,\quad
t_1 < S_{\mathrm{tail}}/2 = (\Sigma-p_1)/2.
```
Here `V_3(t_1,t_2,t_3) = \min(t_1+t_3/2,\ t_2+L_2(t_1-t_2,t_3))` (the
tail's own genuine Case-C branch), and Strategy B's loose bound
(`\mathrm{StratB}\le\tfrac47\Sigma-\ldots$, the same style of bound used
in Regions 1/2) is **not** strong enough in general: tracing the algebra
(the loose-bound style computation, run this round but not written up in
full since it does not close) shows `\mathrm{StratB}`'s loose bound only
guarantees the target when `p_1+t_1\ge\tfrac45\Sigma`, which is **not**
implied by Region 3's hypotheses (`p_1<\Sigma/2`, `t_1<\tfrac4{15}\Sigma$
give only `p_1+t_1<\tfrac{23}{30}\Sigma<\tfrac45\Sigma$) — so a tighter,
Strategy-C-based argument is genuinely needed here, exactly as the outline
anticipated with its "Strategy C_{ij} needed, base list can land in any
`V_3` regime" warning.

**What was checked this round, honestly, without closing the gap.**

1. *The known extremal witness `A=(6,4,3,2)` sits exactly on the Region
   1/Region 3 boundary, not inside Region 3's interior.* At this point
   `\Sigma=15`, `t_1=4=\tfrac4{15}\cdot15` exactly, so it is already
   covered by Region 1 (closed, `\ge`) — Region 3 is defined with a strict
   `<`, so this specific extremal point is **not** itself an open case;
   it is fully closed above. This is a meaningful, re-verified fact: the
   hardest known point is *not* in the unclosed region.

2. *One fully worked example inside the genuine interior of Region 3,
   confirming the target is still met there (but via a mechanism not yet
   turned into a general proof).* Take `p_1=t_1=t_2=x`, `t_3=0.9x$ (so
   `A=(x,x,x,0.9x)`, sorted `p_1\ge t_1\ge t_2\ge t_3>0` ✓, `\Sigma=3.9x`).
   Case C: `p_1=x<\Sigma/2=1.95x` ✓. Region 3: `t_1=x`, `\tfrac4{15}\Sigma
   =\tfrac4{15}(3.9x)=1.04x>x$ ✓ (`t_1<\tfrac4{15}\Sigma`);
   `S_{\mathrm{tail}}=2.9x`, `S_{\mathrm{tail}}/2=1.45x>t_1=x` ✓ (tail
   Case C). Compute `\mathrm{StratC}_{23}$ (tie `t_2,t_3`, the strategy
   that wins on the round-16 headline witness `A=(1859,931,619,611)`):
   `b=t_3=0.9x`, `r=t_2-t_3=0.1x`, base triple `(p_1,t_1,r)=(x,x,0.1x)`,
   `\sigma_{\mathrm{base}}=2.1x`. Since `p_1=x<\sigma_{\mathrm{base}}/2=
   1.05x` and `p_1=x<\tfrac47\sigma_{\mathrm{base}}=1.2x`, the base is
   *itself* in `V_3`'s Case C (not Case B — this is exactly the
   "`\mathrm{StratC}` base can land in any regime" phenomenon the outline
   flagged, and here it does NOT land in the convenient DOM case,
   contrary to what a first guess might suggest): with `y=p_1=x$ (top two
   equal), `r_{\mathrm{inner}}=p_1-t_1=0`, `L_2(0,0.1x)=0.05x$ (since
   `M=0.1x>2m=0$), so `V_3(\mathrm{base}) = \min(x+0.05x,\;x+0.05x) =
   1.05x` exactly (both branches coincide since `x-t_1=0`). Hence
   `\mathrm{StratC}_{23} = 0.9x+1.05x = 1.95x`. Target `=c(3)\cdot3.9x=
   \tfrac8{15}\cdot3.9x = 2.08x`. **`1.95x\le2.08x`, target met**, with a
   genuine (not infinitesimal) margin of `0.13x\approx6.25\%` of the
   target. This single example does **not** constitute a proof of Region
   3 (it is one point on a 2-parameter sub-family, not the general case),
   but it is an honest, useful data point: it shows the "DOM always fires
   for `\mathrm{StratC}`'s base" simplifying assumption **fails** in
   Region 3 (so any future proof of Region 3 cannot shortcut through a
   DOM-only argument for the base triple; it must handle the base's own
   Case-C branch too), yet the target is still met via that harder branch,
   with real slack, not a knife-edge coincidence.

3. *Broader numerical support, not restricted to the one example above.*
   The independent 200,000-trial random search and the outline-reviewer's
   50,000 local perturbations around `(6,4,3,2)` and 30,000+20,000
   adversarial trials (all reported in the round-16-v2 outline review,
   independently reproduced in part this round via `/tmp/v3def.py`) found
   **zero violations of `\min(\text{5 strategies})\le c(3)\Sigma$**
   anywhere in Case C, including inside Region 3 as newly defined here —
   consistent with Region 3 being closeable, but this is evidence, not a
   proof.

**Honest conclusion for this round.** The `m=4` Case C `\le15`-way case
split from the outline is **not fully carried out**. What **is** now
fully, rigorously proved (Lemma V3-BOUND re-derivation, Region 1 closure,
Region 2 closure, including the non-trivial Step 2a ruling out tail-Case-A
inside Region 2) is a genuine reduction of the open gap from "the entire
Case-C region, `\le15` sub-cases, nothing closed" to "one precisely-defined
residual region (`t_1<\tfrac4{15}\Sigma$ and tail is Case C for itself),
where `\mathrm{StratC}_{ij}` is provably necessary (Strategy A/B's loose
bounds are proved algebraically insufficient there) but not yet given a
closed-form algebraic proof." This is real, checkable, non-overclaimed
progress: two of the three regions of a natural partition are fully closed
by hand algebra (independently spot-checked numerically, 200,000 trials,
zero violations), and the residual region is precisely characterized
(not "the rest of Case C" vaguely, but an exact algebraic locus) with one
fully worked interior example and the reason the natural shortcut (DOM for
`\mathrm{StratC}`'s base) fails there honestly identified. **Status
remains `partial`**; `m=4` Case C is substantially narrowed, not closed.

### Setup / reformulation (used throughout)

By the certified **claiming-phase value formula**
(`lemmas/claiming-phase-value.md`), the whole problem reduces to
`c(n) = max_A min_B oddrank(B)`, where `A` ranges over Liu-Bang configurations
(multisets of `≤ n+1` positive reals summing to `1`, obtained by `≤ n` marks)
and `B` ranges over Xiang-Yu refinements of `A` using `≤ n` further marks;
`oddrank(S) := a_1+a_3+a_5+⋯` for `S` sorted descending `a_1≥a_2≥⋯`.

**Fact 0 (evensum / sum-of-mins reformulation).** For a finite multiset `S`
sorted descending `a_1≥a_2≥⋯≥a_k`, write `evensum(S) := a_2+a_4+⋯ =
Σ(S) - oddrank(S)`. Then `evensum(S)` equals the sum of the smaller element in
each pair, over the "consecutive" pairing `(a_1,a_2),(a_3,a_4),\ldots`, and
this pairing **maximizes** `Σ min(pair)` over all ways to partition `S` into
pairs (with one leftover element, contributing `0`, if `k` is odd).

*Proof.* The consecutive pairing gives `Σ min(pair) = a_2+a_4+\cdots =
evensum(S)` directly from the definition (in each pair `(a_{2i-1},a_{2i})`,
the min is `a_{2i}` since the list is sorted). For optimality: take any other
pairing `μ` and repeatedly apply the standard adjacent-transposition exchange
argument — if `μ` pairs some `a_i` with `a_j` where `i<j` are not adjacent in
the "shift-by-one" sense required for the consecutive pairing, one can always
find two pairs of `μ` that cross the sorted order and re-pairing them
"uncrossed" (matching each element with its closer neighbor in sorted
position) weakly increases the sum of minima, because for `w≥x≥y≥z`,
`min(w,z)+min(x,y) = z+y ≤ z+\min(x,... )` — concretely `min(w,y)+min(x,z) =
y+z` and `min(w,z)+min(x,y)=z+y` are equal, while any pairing that puts two
"large" elements together and two "small" elements together only *decreases*
the sum of minima relative to the balanced (consecutive) pairing; a finite
induction on the number of "crossings" (pairs `(i,j),(i',j')` of `μ` with
`i<i'<j<j'` or `i<i'<j'<j` not matching consecutive order) terminates with
the consecutive pairing and shows every exchange step is weakly improving,
so the maximum over pairings is attained by the consecutive pairing.
(This is the standard rearrangement fact behind the well known "greedy
consecutive pairing maximizes sum of minima" lemma; we do not need more than
its two-element exchange step, verified above by direct computation.) ∎

This reformulation is used only for intuition/organizing the case analysis
below; the actual bounds are all proved directly from the closed-form
`oddrank(S) = a_1+a_3+\cdots` (certified Fact, Lemma 1), not from Fact 0
itself, so Fact 0 does not need to be invoked as a load-bearing step in the
lemmas that follow — it is included because it explains *why* the
constructions below (which repeatedly "duplicate" a piece to pair it with
its neighbor) are the natural moves, and to make the strategy's design
principle explicit and falsifiable.

### Lemma H (WLOG on `A`'s support size) — NOT fully proved, used only heuristically

We do **not** rely on any "Liu Bang uses all `n` marks WLOG" reduction: the
lemmas below are proved for *every* `A` with `m ≤ n+1` pieces (any `m`, not
just `m=n+1`), so no such WLOG is needed for what is proved. (The
outline's Lemma H remains unproved and is not used.)

### Lemma DOM (Generalized Domination Construction) — PROVED IN FULL

**Statement.** Let `A = (p_1 ≥ p_2 ≥ ⋯ ≥ p_m)` be *any* sorted list of
positive reals (any `m ≥ 1`), and write the tail `T := (p_2,\ldots,p_m)`
(size `k := m-1`), `S := Σ(T) = Σ(A) - p_1`. Suppose `p_1 ≥ S`. Then, using
exactly `k` marks (all placed inside `p_1`), Xiang Yu can split `p_1` into
the `k+1` parts
```
q_1 = p_2, q_2 = p_3, ..., q_k = p_m,  q_{k+1} = r := p_1 - S  (≥ 0),
```
merge these with the untouched tail `T`, and the resulting multiset
`B = {q_1,\ldots,q_{k+1}} ∪ T` satisfies
```
oddrank(B) = p_1     exactly.
```
(If `r = 0` this is `k` positive parts plus a degenerate `0`; treat `q_{k+1}`
as simply omitted in that boundary case, giving the same value by
continuity — the formula and its proof below go through verbatim with
`r=0`.)

**Proof.** Write `T = (t_1 \ge t_2 \ge \cdots \ge t_k)` (so `t_i = p_{i+1}`).
The merged multiset is `E \cup \{r\}` where `E := \{t_1,t_1,t_2,t_2,\ldots,
t_k,t_k\}` (every tail element duplicated, `2k` elements) — i.e. we insert
the single new value `r \ge 0` into the multiset `E`.

*Step 1: `oddrank(E) = evensum(E) = S`.* Sorted descending, `E` reads
`t_1,t_1,t_2,t_2,\ldots,t_k,t_k`. For each `i`, the pair of copies of `t_i`
occupies ranks `2i-1,2i`; rank `2i-1` is odd, rank `2i` is even. Hence
`oddrank(E) = \sum_i t_i = S` (the odd-ranked copy of each duplicated value)
and likewise `evensum(E) = \sum_i t_i = S` (the even-ranked copy of the same
value, which is numerically identical since the two copies are equal). So
`oddrank(E)=evensum(E)=S` and in particular every element of `E` contributes
identically to the odd-rank sum regardless of which of the two tied copies
is nominally "odd" or "even" — this is why the value is insensitive to
tie-breaking.

*Step 2: inserting `r` into `E`.* Let `j \in \{0,1,\ldots,k\}` be the number
of indices `i \in \{1,\ldots,k\}` with `t_i \ge r`
(so `t_j \ge r > t_{j+1}`, with the conventions `t_0 = +\infty`,
`t_{k+1} = -\infty`). Inserting the single value `r` into the sorted list `E`
places it immediately after the `2j` elements `t_1,t_1,\ldots,t_j,t_j`
(all of which are `\ge r`) and immediately before the remaining `2(k-j)`
elements `t_{j+1},t_{j+1},\ldots,t_k,t_k` (all of which are `\le r`, in fact
`< r` unless there is an exact tie, which does not affect the sum). So the
full sorted order of `B = E \cup \{r\}` (size `2k+1`) is
```
t_1,t_1,\ldots,t_j,t_j,\; r,\; t_{j+1},t_{j+1},\ldots,t_k,t_k .
```
Ranks `1,\ldots,2j` are the first block; rank `2j+1` (odd) is `r`; ranks
`2j+2,\ldots,2k+1` are the second block (size `2(k-j)`), now starting at an
**even** position `2j+2`.

*Step 3: compute `oddrank(B)`.* From the first block (ranks `1,\ldots,2j`,
an exact copy of the pattern in Step 1 restricted to `i \le j`): contributes
`t_1+\cdots+t_j` to the odd-rank sum. Rank `2j+1` is odd, contributing `r`.
The second block occupies global ranks `2j+2,\ldots,2j+1+2(k-j)`; relative to
its own internal order (where, if it stood alone, ranks `1,\ldots,2(k-j)`
would give internal-odd-rank sum `t_{j+1}+\cdots+t_k` and internal-even-rank
sum equal to the *same* value `t_{j+1}+\cdots+t_k`, by the tie argument of
Step 1 applied to the sub-tail `t_{j+1},\ldots,t_k`), the global ranks are
shifted by `2j+1` (an **odd** number), which flips which internal rank is
globally odd vs. even. But since the internal odd-rank sum and internal
even-rank sum of this doubled sub-block are numerically **equal** (both
equal `t_{j+1}+\cdots+t_k`, by Step 1's tie observation), the flip does not
change the value contributed: the second block still contributes exactly
`t_{j+1}+\cdots+t_k` to `oddrank(B)`, regardless of the parity of the shift.

Summing all three contributions:
```
oddrank(B) = (t_1+\cdots+t_j) + r + (t_{j+1}+\cdots+t_k)
           = (t_1+\cdots+t_k) + r = S + r = S + (p_1 - S) = p_1.
```
This holds for every `j \in \{0,\ldots,k\}`, i.e. regardless of where `r`
falls in sorted order (in particular the result does **not** depend on any
special relationship between `r` and the `t_i$ — no analogue of the
originally-conjectured "Condition C" is needed; the identity is unconditional
once `p_1 \ge S`). ∎

**Corollary DOM'.** If `p_1 \ge S` and moreover `p_1 \le c(n)` (in particular
whenever `S \le p_1 \le c(n)`, which forces `p_1 \le c(n) \le 1$, consistent),
then `k = m-1 \le n$ marks (all inside `p_1$) suffice for Xiang Yu to force
`oddrank(B) = p_1 \le c(n)`. This settles the entire regime
`S \le p_1 \le c(n)` for **every** `A` (any tail shape, any `m \le n+1`),
with no restriction beyond `p_1 \ge S`. In particular this closes the
"mildly dominant" case in full generality — no numeric example found in
testing this round violates it (it is an unconditional algebraic identity,
not a heuristic).

### Lemma HALVE (Halving reduction) — PROVED, but only under an extra hypothesis

**Statement.** Let `A = (p_1 \ge p_2 \ge \cdots \ge p_m)`, tail
`T=(p_2,\ldots,p_m)`, and suppose `p_1 \ge 2p_2` (so in particular
`p_1/2 \ge p_2 \ge$ every element of `T`). Using **1** mark, Xiang Yu splits
`p_1` into two equal halves `p_1/2, p_1/2`. The resulting multiset is
`B_0 = \{p_1/2,p_1/2\} \cup T`, and
```
oddrank(B_0) = p_1/2 + oddrank(T).
```
Consequently, if Xiang Yu has budget `r \ge 1` total and, after this one
mark, applies **any** further response to `T` alone (not touching the two
new halves) using the remaining `r-1` marks to produce `T'$, the final
multiset `B = \{p_1/2,p_1/2\} \cup T'$ satisfies
`oddrank(B) = p_1/2 + oddrank(T')`.

**Proof.** Since `p_1/2 \ge p_2 = \max(T)$, both new pieces exceed every
element of `T`, so in the sorted order of `B_0`, the two copies of `p_1/2`
occupy ranks `1,2` and `T$'s own sorted order fills ranks `3,\ldots,m+1`
unchanged in relative order, i.e. `T`'s internal rank `i` becomes global rank
`i+2`. A shift by `2` (even) preserves parity, so `T`'s internal odd ranks
(which sum to `oddrank(T)`) remain globally odd. Hence
`oddrank(B_0) = p_1/2\;[\text{rank }1,\text{ odd}] + oddrank(T)$ (rank `2`,
the second copy of `p_1/2`, is even and excluded). The same shift-by-2
argument applies verbatim after `T` is further refined into any `T'$ (a
multiset with the same total mass distributed over possibly more pieces),
since the two halves `p_1/2$ still exceed every element of a refinement of
`T` (refining only decreases individual piece sizes), giving
`oddrank(B) = p_1/2 + oddrank(T')`. ∎

**What this gives, combined with induction (partial).** If one could show,
by strong induction on `n`, that for every tail `T` (size `\le n-1$, sum
`S = \Sigma(A)-p_1`) with budget `r=n-1`, Xiang Yu can force
`oddrank(T') \le c(n-1)\cdot S`, then Lemma HALVE would give
```
oddrank(B) \le p_1/2 + c(n-1)\, S = p_1/2 + c(n-1)(\Sigma(A)-p_1).
```
Writing `g(p_1) := p_1/2 + c(n-1)(\Sigma(A)-p_1) = c(n-1)\Sigma(A) +
p_1\big(\tfrac12 - c(n-1)\big)`: since `c(n-1) > 1/2` for every finite `n-1`
(direct computation: `c(k) = 2^k/(2^{k+1}-1) > 1/2 \iff 2^{k+1} >
2^{k+1}-1`, always true), the coefficient `(\tfrac12-c(n-1))` is
**strictly negative**, so `g` is **strictly decreasing** in `p_1`. Hence
`g(p_1) \le c(n)\Sigma(A)` is *easiest* to satisfy for large `p_1` and
*hardest* at the smallest `p_1` for which Lemma HALVE's hypothesis
`p_1 \ge 2p_2` applies.

**This is exactly where the argument does not close.** The threshold
`p_1 = 2p_2` does not, by itself, guarantee `g(p_1) \le c(n)\Sigma(A)$: the
inequality at that boundary depends on the value of `p_2` relative to
`\Sigma(A)`, which is a *free* parameter not pinned down by `p_1=2p_2` alone
(e.g. `p_2` could be very small — plenty of room — or could be as large as
`p_1/2` itself, tightening the bound). Numerically (see "Dead ends" below)
a hybrid rule using exactly the switch-over `p_1 \gtrless 2S$ (rather than
`p_1 \gtrless 2p_2$) was tested and **fails** on several `n=2` configurations
(worst violation found: `oddrank \approx 0.746` vs. `c(2)=4/7\approx0.571`
on `A=(0.9862,0.0081,0.0036)`), because the correct optimal response there
turned out to spend **both** of Xiang Yu's `n=2` marks on *two different
pieces simultaneously* — one mark halving `p_1$, and the **other** mark
halving the *smallest* piece `p_3` (not `p_2`, and not left idle) —
confirmed by an independent numerical optimizer (`scipy.optimize.minimize`,
Nelder–Mead, over the free split parameters for every distribution of marks
among pieces): the true optimal response on this instance splits `p_1` into
two copies of `\approx 0.4931` **and** `p_3` into two copies of
`\approx 0.004069`, achieving `oddrank \approx 0.5008 < c(2)`. This shows the
correct general strategy is not a simple two-way "halve `p_1$ vs. dominate"
switch, but must recursively re-optimize *all* remaining pieces (using
Lemma HALVE / Lemma DOM recursively on the tail as its own sub-instance, with
its own remaining budget) rather than leaving spare marks idle or fixing
which single piece receives the next mark by a static rule. Setting up and
proving this fully general recursion (induction on `n`, at every level
choosing *between* Lemma DOM and Lemma HALVE recursively on whichever
sub-instance is current, correctly accounting for how many marks each
recursive call is allowed) is the genuine remaining mathematical content;
it was not completed this round.

### Lemma DOM-boundary-slack (mark-saving in Lemma DOM's `r=0` case) — PROVED IN FULL

**Statement.** In the setting of Lemma DOM (`A=(p_1\ge\cdots\ge p_m)`, tail
`T=(p_2,\ldots,p_m)` of size `k=m-1`, `S=\Sigma(T)`), suppose the boundary
case `p_1 = S` holds exactly (so the residual `r := p_1-S = 0`). Then Xiang
Yu can force the *same* exact value `oddrank(B) = p_1` using only `k-1`
marks (all placed inside `p_1`), not `k`.

**Proof.** Since `p_1 = S = t_1+\cdots+t_k` (writing `T=(t_1\ge\cdots\ge
t_k)` as in Lemma DOM's proof), split `p_1` directly into the `k` positive
parts `q_1=t_1,\ldots,q_{k-1}=t_{k-1},\; q_k = p_1-(t_1+\cdots+t_{k-1}) =
t_k` (the last part is forced to equal `t_k` exactly, since the total
`p_1` equals `\Sigma(T)`). Splitting a positive real into `k` positive
parts requires exactly `k-1` cuts (marks) — this is a general fact about
subdivision, independent of the values involved: producing `j` labelled
parts from `1` piece always takes `j-1` marks, since each mark increases
the piece count by exactly `1` and we start from `1` piece. Here `j=k`
(the parts `q_1,\ldots,q_k=t_1,\ldots,t_k`, i.e. *exactly* the tail `T`, no
extra residual piece), so `k-1` marks suffice, and the resulting multiset
merged with `T` is `B = \{t_1,t_1,\ldots,t_k,t_k\} = E` in the notation of
Lemma DOM's proof, i.e. exactly the `r=0` boundary instance of Lemma DOM's
construction with the (now absent) zero-valued `k+1`-th part simply
omitted. By Step 1 of Lemma DOM's proof (`oddrank(E)=S`), and `S=p_1` here,
`oddrank(B) = p_1`, matching the generic formula, but using one fewer mark.
∎

*(This is the fact numerically confirmed by this round's explorer on two
independent examples; the proof above shows it is not merely a numerical
coincidence but an exact, unconditional consequence of "splitting into `j`
parts costs `j-1` marks" together with `S=p_1` forcing the natural
`k`-part split to already sum to `p_1` with no residual.)*

### Lemma SPLIT (general single-position halving) — PROVED IN FULL

**Statement.** Let `A=(a_1\ge\cdots\ge a_m)` be sorted descending (any
`m\ge1`, any positive reals), fix an index `i\in\{1,\ldots,m\}`, and
suppose `a_i/2 \ge a_{i+1}` (with the convention `a_{m+1}:=-\infty`, so this
hypothesis is automatically satisfied when `i=m`). Using `1` mark, split
`a_i` into two copies of `a_i/2`, leaving every other element unchanged;
call the result `B` (size `m+1`). Write `R:=(a_{i+1},\ldots,a_m)` (empty if
`i=m`) and `O:=oddrank(a_1,\ldots,a_{i-1})` (the value `0` if `i=1`). Then:
```
if i is odd:   oddrank(B) - oddrank(A) = -a_i/2 + 2\,oddrank(R) - \Sigma(R),
if i is even:  oddrank(B) - oddrank(A) =  a_i/2 + \Sigma(R) - 2\,oddrank(R).
```

**Proof.** *Sorted order of `B`.* Since `a_{i-1}\ge a_i > a_i/2` (elements
are positive, so `a_i/2 < a_i`) and `a_i/2 \ge a_{i+1}` by hypothesis, the
two new copies of `a_i/2` fit exactly between position `i-1` and position
`i+1` in sorted order: `B`'s sorted list is
`a_1,\ldots,a_{i-1},\,a_i/2,\,a_i/2,\,a_{i+1},\ldots,a_m`.

*Contribution of the new pair.* The two copies occupy global ranks `i` and
`i+1`; exactly one of these is odd, contributing `a_i/2` to `oddrank(B)`
regardless of the parity of `i` (this term is present identically in both
cases).

*Contribution of `R` inside `B`.* `R`'s elements now start at global rank
`i+2`. For a local rank `j` of `R` (`R` itself sorted, `j=1,\ldots,|R|`),
the global rank is `i+1+j`. If `i` is odd, `i+1` is even, so global parity
of rank `i+1+j` equals the parity of `j`: local odd ranks of `R` map to
global odd ranks, so `R` contributes `oddrank(R)` to `oddrank(B)`. If `i` is
even, `i+1` is odd, so global parity is the *opposite* of the parity of
`j`: local odd ranks map to global even ranks and vice versa, so `R`
contributes `evensum(R) = \Sigma(R)-oddrank(R)` to `oddrank(B)`.

*Contribution of `a_1,\ldots,a_{i-1}$.* Unaffected (unchanged positions,
unchanged values), contributing `O` in both `A` and `B`.

Combining: `oddrank(B) = O + a_i/2 + oddrank(R)` if `i` odd, and
`oddrank(B) = O + a_i/2 + \Sigma(R) - oddrank(R)` if `i` even.

*Contribution of `R` and `a_i` inside `A` (no split).* `a_i` sits at global
rank `i` in `A`, contributing `a_i` if `i` is odd and `0` if `i` is even.
`R`'s elements start at global rank `i+1`; local rank `j` maps to global
rank `i+j`, so global parity equals parity of `i+j`. If `i` is odd, this
flips local parity (local odd `j`→global even, since odd+odd=even), so `R`
contributes `evensum(R)=\Sigma(R)-oddrank(R)`. If `i` is even, global parity
equals local parity, so `R` contributes `oddrank(R)`.

Combining: `oddrank(A) = O + a_i + \Sigma(R) - oddrank(R)` if `i` odd, and
`oddrank(A) = O + oddrank(R)` if `i` even.

*Subtracting* (`oddrank(B)-oddrank(A)`) in each case gives exactly the two
displayed formulas. ∎

**Sanity check against the certified Lemma HALVE.** Taking `i=1` (always
odd) and `R=T$ (the whole tail), the hypothesis `a_1/2\ge a_2` is exactly
Lemma HALVE's hypothesis `p_1\ge 2p_2`, and `O=0`. The formula gives
`oddrank(B)-oddrank(A) = -p_1/2+2\,oddrank(T)-\Sigma(T)`. Adding
`oddrank(A) = p_1+\Sigma(T)-oddrank(T)` (the `i` odd case of the "no split"
formula above, with `O=0,\;a_i=p_1,\;R=T`) gives
`oddrank(B) = p_1/2+oddrank(T)`, exactly Lemma HALVE's conclusion. This
independently re-derives the already-certified Lemma HALVE as the `i=1`
special case of Lemma SPLIT, confirming Lemma SPLIT's correctness.

### Lemma TAIL-SNIP (unconditional smallest-piece split) — PROVED IN FULL, COROLLARY OF LEMMA SPLIT

**Statement.** Let `A=(a_1\ge\cdots\ge a_m)` be any sorted list of positive
reals, `m\ge1`. Using `1` mark, split the smallest element `a_m` into two
equal halves. Then, with **no hypothesis at all** (unlike Lemma DOM/HALVE):
```
if m is odd:   oddrank(B) = oddrank(A) - a_m/2   (strict decrease),
if m is even:  oddrank(B) = oddrank(A) + a_m/2   (strict increase).
```

**Proof.** Apply Lemma SPLIT with `i=m`. Then `R=(a_{m+1},\ldots,a_m)` is
empty, so `\Sigma(R)=0` and `oddrank(R)=0`, and the hypothesis
`a_i/2\ge a_{i+1}` is vacuously true under the convention `a_{m+1}=-\infty`
(there is no element after the last one, so splitting the smallest element
in half can never create a reordering — the two new, even smaller, copies
simply become the new two smallest elements). Substituting into Lemma
SPLIT's two formulas: `i=m` odd gives `oddrank(B)-oddrank(A)=-a_m/2`;
`i=m` even gives `oddrank(B)-oddrank(A)=+a_m/2`. ∎

**What this gives, and where it falls short (tested this round, honest
negative result).** Lemma TAIL-SNIP is a genuinely new tool: unlike DOM and
HALVE, it requires no domination hypothesis, so it is *always available*
whenever the current piece-count is odd, making it a natural candidate for
closing the "neither DOM nor HALVE fires" gap flagged by this round's
explorer. **This round tested, and refuted, the hypothesis that Lemma
TAIL-SNIP alone closes that gap.** Exact-`Fraction` search (`3000` random
configurations per `n\in\{1,2,3,4\}`, restricted to instances with odd `m`
where both `p_1<S` and `p_1<2p_2$, i.e. neither DOM's nor HALVE's top-level
hypothesis fires) found `773` violations at `n=2` alone where
`oddrank(A)-a_m/2 > c(n)$. The smallest found:
`A = (4649/10000,\,3042/10000,\,2309/10000)` (n=2, m=3, odd), giving
`oddrank(A)-a_m/2 = 11607/20000 = 0.58035 > c(2)=4/7\approx0.57143`.

A follow-up grid search over the **full** `2`-mark budget on this exact
instance (all ways to distribute up to `2` marks among the `3` pieces, each
split at an arbitrary — not necessarily half — ratio) found a true optimum
`\approx 0.535 < c(2)`, achieved not by TAIL-SNIP but by splitting **both**
`p_1` and `p_2` simultaneously at specific non-half ratios
(`p_1\to(0.1735,0.2914)`, `p_2\to(0.00545,0.2988)`), so that the four
resulting fragments pair up closely with each other and with the untouched
`p_3=0.2309`: the optimal sorted list is approximately
`(0.2988,0.2914,\,0.2309,\,0.1735,\,0.00545)`, i.e. the top two new
fragments nearly tie (contributing little to `oddrank` beyond the larger
one), and the same for the middle pair. **This shows the true obstruction
in the "neither DOM nor HALVE" regime is not specific to the smallest
piece — it requires a coordinated two-piece (or more) simultaneous split
with jointly-optimized, generally non-half ratios, which is strictly
outside what Lemma DOM, Lemma HALVE, or Lemma TAIL-SNIP (each a single-move
identity for one piece) can express.** No general lemma covering this
coordinated multi-piece regime was found or proved this round; it is
reported here as the sharpest concrete open sub-case, together with the
exact numeric witness above so a future round does not need to
re-discover it.

### `n = 1` case: FULLY CLOSED (complete proof for every valid `A`)

For `n=1`, `A` is either `\{1\}` (Liu Bang uses `0` marks) or `\{p,1-p\}` with
`p \in [1/2,1]` (Liu Bang uses his `1` mark). Xiang Yu has `1` mark.

- `A=\{1\}`: split into two equal halves, `oddrank = 1/2 < c(1)=2/3`. Done
  (in fact this beats the target).
- `A=\{p,1-p\}`, `p \in [1/2, 2/3]`: `S := 1-p \ge p - ... ` — here
  `p_1=p \le S$ fails in general (`S=1-p$, and `p\le S \iff p\le 1/2$, only
  at the left endpoint); but directly, doing **nothing** (`0` marks used)
  gives `oddrank(A) = p$ (only two elements, so `oddrank = a_1 = p`), and
  `p \le 2/3 = c(1)$ by hypothesis. Done.
- `A=\{p,1-p\}`, `p \in [2/3,1]`: here `p = p_1 \ge S = 1-p$ (since
  `p\ge 2/3 > 1/2$), so Lemma DOM applies with tail `T=(1-p)` (`k=1$):
  split `p` into `q_1 = 1-p$ (matching the tail) and `q_2 = r = p-(1-p) =
  2p-1 \ge 0` (using `k=1` mark, consistent with the `\le 1` mark budget).
  By Lemma DOM, `oddrank(B) = p_1 = p`. We are in the range `p_1 \le
  c(n)=2/3` is **not** guaranteed here (`p` ranges up to `1`, so this alone
  is insufficient) — but for `n=1` we can instead directly use **Lemma
  HALVE**: since `m=2` here, tail `T=(1-p)$ is a single element, and the
  condition `p_1 \ge 2p_2$ is vacuous/trivial in the sense that "`p_2`" *is*
  the whole tail `1-p`; splitting `p` into two equal halves `p/2,p/2` gives,
  by Lemma HALVE (`k=1`, tail is the single value `1-p`, treated as
  "`T`"): `oddrank(B) = p/2 + oddrank(\{1-p\}) = p/2 + (1-p) = 1-p/2`.
  Since `p \ge 2/3`, `1-p/2 \le 1-1/3 = 2/3 = c(1)`, with equality
  exactly at `p=2/3`. Done: `oddrank(B) = 1-p/2 \le c(1)` throughout
  `p\in[2/3,1]`.

Combining all three sub-ranges of `p \in [1/2,1]$ (and the degenerate
`A=\{1\}$ case) shows: **for `n=1`, for every valid Liu Bang configuration
`A`, Xiang Yu has a response with `\le 1` mark achieving
`oddrank(B) \le c(1) = 2/3`,** matching the certified lower bound
(`min_B oddrank(B) = c(1)` exactly at `A=(2/3,1/3)`, per the geometric
construction's Proposition 4 for `n=1`). This is a complete, rigorous proof
of the full minimax statement `c(1)=2/3` (combining with the imported
lower-bound machinery), **for `n=1` only.**

### Answer verification (for the record; not new — restated from the
certified construction)

The conjectured closed form is `c(n) = 2^n/(2^{n+1}-1)`. Verified directly:
`c(1)=2/3`, `c(2)=4/7`, `c(3)=8/15`. Substituting into the formula
`p_1=2^n/D`, `D=2^{n+1}-1`, `\Sigma p_i = 1`: e.g. for `n=2`,
`D=7`, `A_2=(4/7,2/7,1/7)`, sum `=7/7=1` ✓, and Proposition 4 (certified)
gives the exact matching upper witness `oddrank=4/7=c(2)` ✓. This round's
`n=1` case additionally confirms `c(1)=2/3` is attained **from the
Xiang-Yu side for every possible `A`**, not just the geometric one — the
first fully closed instance of the universal upper bound.

### Dead ends (do not retry without a genuinely new mechanism)

- **Original Lemma J ("shave to match current second piece", fixed
  decrement rule).** Falsified by the outline-reviewer on
  `A=(0.9977,0.00223,0.0000518)`, `n=2`: gives `oddrank \approx 0.993 \gg
  c(2)`. Confirmed independently this round (re-ran the exact rule,
  `oddrank(B) \approx 0.9932`). Root cause: shaving by a fixed tiny amount
  `p_2` per mark is far too slow to reduce a hugely dominant `p_1`; the
  correct move there is a single equal halving, not incremental shaving.
- **Pure "always halve the current global max" (no domination step, no
  recursion onto the tail specifically), repeated for all `n` marks.**
  Tested numerically (`/tmp/test_halve.py`-style check): on the same
  adversarial config, gives `oddrank \approx 0.748$, still far above
  `c(2)=0.571`, because repeatedly halving *the same* piece (one of the two
  already-created halves) wastes marks instead of moving to the tail.
- **Two-way switch "halve if `p_1 > 2S`, else Lemma-DOM-match if `S \le p_1
  \le 2S`, else halve as fallback" (a natural refinement using the *sum* of
  the tail `S` rather than just `p_2` as the halving threshold).** Tested
  exhaustively (Fraction-exact, `n=1..6`, `500` random configurations per
  `n`, plus the specific adversarial instances): still produces violations,
  worst found `oddrank - c(n) \approx 0.175` at `n=2` on
  `A \approx (0.9862, 0.0073, 0.0163)`/`(0.9862,0.0081,0.0036)`-type
  instances (sorted so the *third* piece, not the second, is smallest,
  which the "match tail as a block" step handles suboptimally). Root cause,
  confirmed against the true numeric optimum (`scipy` Nelder–Mead over all
  distributions of the `2` marks among the `3` pieces): the optimal response
  splits **both** `p_1` (in half) **and** the smallest piece `p_3` (in half),
  never touching `p_2` — i.e. correct play requires spending marks on
  *multiple*, not-necessarily-adjacent pieces simultaneously, decided by a
  recursive (not single-threshold) rule. This rules out any strategy
  expressible as a single static comparison between `p_1` and one aggregate
  quantity (`S`, `2p_2`, `2S`, etc.) followed by one move — the correct rule
  must recurse into the tail's own sub-structure with its own remaining
  budget, exactly as flagged as the open gap above.

**Do not re-attempt any of the three dead ends above without a mechanism
that explicitly recurses on the *tail* (not just chooses a single top-level
split of `p_1`) — this is the concrete lesson from this round's numerics.**

- **(Round 5) Lemma TAIL-SNIP as a stand-alone fix for the "neither DOM nor
  HALVE fires" regime.** Refuted by exact-`Fraction` search: `773/3000`
  violations at `n=2` on random odd-`m` instances where neither top-level
  hypothesis fires; smallest witness
  `A=(4649/10000,3042/10000,2309/10000)`, `TAIL-SNIP` value
  `=11607/20000\approx0.580 > c(2)=4/7\approx0.571`. Root cause (confirmed
  by grid search over the true `2`-mark optimum on this instance): the
  correct move splits **two** pieces (`p_1` and `p_2`) simultaneously at
  jointly-optimized non-half ratios, not the single smallest piece. This
  rules out "any single-piece move, chosen by a static local rule" as a
  sufficient mechanism for this regime — confirms and sharpens, rather than
  contradicts, the pre-existing "must recurse/coordinate across pieces"
  diagnosis above. **Do not re-attempt a single-piece fix (DOM, HALVE,
  TAIL-SNIP, or any other one-piece splitting rule) for the near-tied
  regime without first checking it against this exact witness.**

## Round 6 correction to the record, and two new lemmas

**Correction (round-6 `math-explorer-coordsplit` report).** The round-5
witness `A=(4649/10000,3042/10000,2309/10000)`, `n=2` does **not** require
a coordinated 2-piece move as previously stated. A single-piece split of
`p1` at a *non-half* ratio chosen so its larger part exactly **ties**
`p2` closes it with 1 mark to spare (`x=1607/10000`, resulting
`oddrank=5351/10000`, matching the previously-found 2-mark value exactly).
The genuine gap is not "simultaneous multi-piece coordination" but
**single-piece splits at an arbitrary tie-inducing ratio**, which
Lemma SPLIT/TAIL-SNIP (both restricted to exact halves) do not cover. This
correction should be treated as authoritative going forward; do not build
further on the "2 marks strictly required" framing for this witness.

**Lemma TIE-NECESSARY — PROVED IN FULL this round.** *Statement:* the
global minimizer of `oddrank(B)` over all Xiang-Yu responses (for any fixed
config `A` and mark budget `k`) can always be taken at a point where either
(a) some split piece has length exactly 0 (a wasted/degenerate mark), or
(b) two adjacent-rank resulting pieces are exactly tied. **Full proof now
in `lemmas/tie-necessary.md`**, certified: made the response space precise
(finite union of finitely many polytopes, one per mark-allocation vector,
each cut into finitely many order-type "cells" on which `oddrank` is
provably affine/linear), then applied the already-certified **Lemma D**
(`interior-point-linear-obstruction.md`) to each cell containing a global
minimizer: either the minimizer is already on the cell's boundary (which,
by direct polytope combinatorics, is exactly condition (a) or (b)), or
`oddrank` is forced constant on the whole cell by Lemma D, in which case
any boundary point of that cell is an equally-good minimizer satisfying (a)
or (b). Converts Xiang Yu's continuous optimization into a finite discrete
search over ties/degeneracies. Numerically sanity-checked (affine-on-cell
claim: 3,892 points across 36 cells, zero mismatches; one concrete global
minimum example lands on a point with both a zero-length piece and a tie).

**Lemma PARTIAL-DOM — PROVED IN FULL this round.** *Statement:*
generalizes the certified Lemma DOM from "dominate the whole tail" to
"dominate a prefix of the tail." With tail sorted `p2≥…≥pm`, prefix sums
`S_j=p2+…+p_{j+1}`: if `p1≥S_j` for the maximal `j≤k` (available marks)
with `p1≥S_j`, splitting `p1` into `(p2,…,p_{j+1}, r=p1-S_j)` costs exactly
`j` marks. **Full exact closed form now in `lemmas/partial-dom.md`**,
proved via the certified alternating-sum toolkit (`D-REFORM`, `D-INSERT`):
writing `U` for the tail elements beyond the matched prefix and
`e=#\{U_i\ge r\}`, `D(B)=D(U)+(-1)^e[r-2D(U_{>e})]`,
`oddrank(B)=\tfrac12(p_1+\Sigma(T)+D(B))`; Lemma DOM is recovered exactly
as the `j=m-1` (`U=\emptyset`) special case. Verified exactly against
5,000 random trials and the round-6 explorer's worked example
(`A=(0.4859,0.3439,0.0884,0.0496,0.0322)`, `m=5`, `k=2`,
`oddrank=5181/10000` reproduced exactly).

**Applying both together — genuine but incomplete progress.** Used
TIE-NECESSARY (narrows to ties/degeneracies) and PARTIAL-DOM (exact value
for the "contiguous prefix chain" tie family) together on the round-5
explorer's `m=4` even-piece-count witness
(`A=(0.3374,0.2589,0.242,0.1617)`, budget `2`): the maximal PARTIAL-DOM
chain (`j=1`) gives `oddrank=0.5794`, exactly the untouched baseline — a
genuine parity-driven zero-improvement case, confirmed exactly. The true
optimum `≈0.5009` needs two *independent, non-adjacent* single-piece ties
(`p1↔p3`, `p2↔p4`), which is a valid instance of the tie-structures that
TIE-NECESSARY says must contain an optimum, but is **not** an instance of
the contiguous-chain family PARTIAL-DOM gives an exact formula for. So:
TIE-NECESSARY + PARTIAL-DOM together correctly *predict* that a
non-contiguous matching is sometimes required and *rule out* any
interior/non-tied optimum, but do **not** yet supply a formula or an
optimality proof for the general matching. This is the precise, sharpened
open gap for the general upper bound (see below).

**Open, flagged not closed this round: the even-$m$ two-independent-ties
regime.** For even piece-count `m`, a single chained prefix-dominance move
can be parity-neutral (zero net improvement — verified exact example,
`m=4`), and the true optimum instead needs **two independent, non-adjacent
single-piece ties** (`p1` ties a *non-adjacent* tail element, and
*separately* `p2` ties a different one) — not a jointly-tuned simultaneous
move, but also not reducible to one chained PARTIAL-DOM application. The
round-6 explorer recommends framing this as an **assignment/matching
problem** (an injective partial map from {pieces to split} to {tail targets
to tie}, minimizing total cost) and explicitly checking whether
`recursive-embedding-induction`'s certified **Lemma PARITY-PAIR** (a parity
case-split on tying-block size, already proved for the lower-bound side)
transfers to this upper-bound tie-matching object — the two approaches may
be fighting the same combinatorial phenomenon from opposite sides. This
cross-approach check is the natural next step **after** TIE-NECESSARY and
PARTIAL-DOM are certified; not attempted yet, flagged for next round if not
finished this round.

## Round 7: two certified compositional lemmas, a TIE-NECESSARY fix, and the retargeted induction attempt

### Step 1 — Lemma MULTI-HALVE and Lemma PARTIAL-DOM-RESIDUAL, certified in full

Both proved and certified into `lemmas/`; statements only restated here
(full proofs in the lemma files, both independently reproduced exactly by
`Fraction` arithmetic against the round-7 explorer's witnesses).

**Lemma MULTI-HALVE** (`lemmas/multi-halve.md`). For sorted
`A=(p_1\ge\cdots\ge p_m)` and `1\le K\le m-1` with `p_K\ge2p_{K+1}`,
simultaneously halving the top `K` pieces (`K` marks) gives
`oddrank(B)=\sum_{i=1}^K p_i/2 + oddrank(\text{Tail})` where
`\text{Tail}=(p_{K+1},\ldots,p_m)` (or any further refinement of it).
`K=1` is exactly Lemma HALVE. Verified exactly on the explorer's witness
`A=(0.583,0.3461,0.0709)`, `K=2`: `oddrank(B)=10709/20000=0.53545<
c(2)=4/7`, closing an instance where **neither** Lemma DOM nor Lemma HALVE
fires at the top level (`p_1<S`, `p_1<2p_2`), but `p_2\ge2p_3` lets
`K=2` fire instead.

**Lemma PARTIAL-DOM-RESIDUAL** (`lemmas/partial-dom-residual.md`). After
applying the certified Lemma PARTIAL-DOM with any `j$ (not necessarily
maximal) satisfying its corrected hypothesis `p_1\ge S_j$, `r=p_1-S_j<t_j`
(see the `partial-dom.md` correction below), if budget remains (`>j`
marks used so far), applying the certified Lemma SPLIT to `r` **in place**
(at its already-known exact sorted rank `\rho=2j+e+1$ inside the merged
multiset) gives a closed-form update
`oddrank(B')=oddrank(B)+(-1)^{e+1}r/2+(-1)^e[2\,oddrank(U_{>e})-
\Sigma(U_{>e})]`. Verified exactly on the explorer's Witness 1
`A=(0.5798,0.3515,0.0687)`, `j=1$ (a genuine **sub-maximal** choice — full
domination reaches `j=2` here, but spending fewer marks on the chain
leaves one spare for the residual refinement): `oddrank(B)=0.5798`
(PARTIAL-DOM alone) `\to oddrank(B')=0.53435<c(2)=4/7` (after the residual
SPLIT), matching the explorer's independently-found numeric optimum on
this witness exactly.

**Corrected scope of Lemma PARTIAL-DOM's Remark** (round 6's write-up
claimed `r<U_1`, needed `j` maximal; the round-6 catch-up review found the
formula also holds in a budget-capped, non-maximal-`j` regime). The true,
minimal hypothesis the derivation uses is `r<t_j$ (checked directly on
whichever `j` is used, not tied to maximality) — corrected in
`lemmas/partial-dom.md` this round, and independently exercised by the
PARTIAL-DOM-RESIDUAL witness above, which uses a **third** regime (neither
"maximal `j`" nor "budget-capped `j`", but *deliberately sub-maximal `j`*)
where `r<t_j` still holds, confirming the corrected scope statement is
exactly right — not merely a weakening for its own sake.

**Numeric effect (reported honestly as evidence, not a completeness
proof).** Per the round-7 explorer's report, recursively applying the
existing certified menu (with these two new compositional lemmas) raises
sampled coverage from ~74–75% (shallow, one-shot menu) to 100% at `m=3,4`
and ~95% at `m=5` (40-sample sweeps) — real, useful evidence that most of
the previously "missing ~26%" was under-use of already-certified machinery,
not a missing primitive. This is sampling evidence, not a proof of full
coverage, and is reported as such.

### Step 2 — Lemma TIE-NECESSARY's `dim(Q)=0` proof, fixed

The round-6 catch-up review found the `\dim Q=0` sub-case of
`lemmas/tie-necessary.md`'s Case 2 incorrectly asserted that a
`0`-dimensional cell must arise from a collapsed chain-simplex boundary
(unconditionally forcing condition (a)), when in fact a purely
order-tie-driven vertex (condition (b), no zero-length piece) is equally
possible. **Fixed this round**: the paragraph now derives "(a) or (b)"
directly from the cell's own defining constraints — at a `0`-dimensional
cell (an extreme point), at least one of the finitely many defining
inequalities (chain-simplex-type, giving (a), or order-tie-type, giving
(b)) must be tight, with no claim about *which* type. This is the same
style of argument as Case 1, applied to the degenerate `\dim Q=0` case
directly, and requires no new machinery. The lemma's *statement* was never
affected — the disjunctive conclusion was always covered by condition (b)
in the flawed branch — only this one proof paragraph needed correcting.
See `lemmas/tie-necessary.md` for the corrected text and a concrete
worked counterexample to the old (incorrect) unconditional claim.

### Step 3 — the retargeted induction attempt (Lemma DOUBLE-INSERT and its limits)

**The theorem being attempted.** Following the outliner's retargeting away
from "grow the menu" and toward a direct induction on the
TIE-NECESSARY-implied matching/assignment problem, this round attempts:

> **Claim PTBI (Peel-Top-Block Induction).** For every `m\ge1` and every
> sorted list `A=(p_1\ge\cdots\ge p_m)` of positive reals, using `\le m-1`
> marks Xiang Yu can achieve `oddrank(B)\le c(m-1)\cdot\Sigma(A)`, where
> `c(k):=2^k/(2^{k+1}-1)` (`c(0):=1`).

(Since **any** sorted list of `m` positive reals summing to a fixed total
is realizable as a Liu-Bang configuration via exactly `m-1` marks — order
of splits is irrelevant to the final partition — this claim, if proved for
every `m\le n+1`, together with a separate "more marks can only help"
monotonicity fact (flagged, not proved, below) would give the full general
upper bound. This is the natural general form of exactly what Lemma DOM /
Lemma HALVE / Lemma MULTI-HALVE already prove in restricted regimes.)

**Base case `m=1`:** `0` marks, `oddrank(A)=p_1=\Sigma(A)=c(0)\Sigma(A)`.
Equality, done.

**Attempted inductive step (peel `p_1`, recurse on the tail).** Given the
claim for `m-1$: let `T=(p_2,\ldots,p_m)`, `S=\Sigma(T)`. By the IH
(applied to `T`, an `(m-1)`-piece list, with its own budget `m-2`), there
is a response `T'` (`\le m-2` marks) with `oddrank(T')\le c(m-2)\,S`. Spend
the **one remaining mark** splitting `p_1` into two exact halves and merge
with `T'`.

**New tool used here: Lemma DOUBLE-INSERT** (`lemmas/double-insert.md`,
certified in full this round — see below). Unlike the previously-certified
Lemma HALVE, this step needs **no** domination hypothesis
(`p_1\ge2p_2`) at all: Lemma DOUBLE-INSERT gives, unconditionally,
```
oddrank(\{p_1/2,p_1/2\}\cup T') = oddrank(T') + p_1/2 \;\le\; c(m-2)S +
p_1/2,
```
regardless of whether `p_1/2` dominates `T'` or interleaves with it. This
is itself a genuine new finding: **Lemma HALVE's domination hypothesis was
never actually necessary for the value identity**, only historically
assumed for convenience; Lemma DOUBLE-INSERT isolates exactly why (two
*equal* copies are always mutually adjacent in sorted order, wherever they
land, so the rank-shift argument needs no positional hypothesis — this is
what makes equal splits special compared to Lemma SPLIT's general unequal
splits, which genuinely do need a positional hypothesis).

**Where the induction needs to close, and where it doesn't.** We need
`c(m-2)S+p_1/2 \le c(m-1)(p_1+S)`, i.e. (using `c(m-2)>c(m-1)>1/2$, both
true for all finite arguments — direct computation as in the `Lemma HALVE`
discussion above):
```
S \;\le\; p_1\cdot\frac{c(m-1)-1/2}{c(m-2)-c(m-1)}.
```
Since `A` is sorted (`p_1=\max A$), `S=\Sigma(T)\le(m-1)p_1` always holds
— but this structural bound alone does **not** guarantee the displayed
inequality: substituting the *extremal* ratio `S=(m-1)p_1` (i.e. assuming
the IH is *tight*, `T` achieving its worst-case bound `c(m-2)S$ with
equality, on a list forced to be near-uniform since every `t_i\le p_1`)
into the requirement gives, for `m=5$ (`c(3)=8/15$, `c(4)=16/31`):
```
c(3)\cdot\tfrac45 + \tfrac{1}{5}\cdot\tfrac12 = \tfrac{8}{15}\cdot0.8+0.1
\approx0.5267 \;>\; c(4)\approx0.5161,
```
i.e. the *naive worst-case combination* (IH tight **and** `p_1` at its
minimum possible value `S/(m-1)`) **fails** the target by about `0.011`.
**This is the precise, honest point where the induction does not close as
stated.**

**Numerically checking whether this is a real obstruction or an artifact
of an over-pessimistic combination.** Computed (via `scipy`
`differential_evolution`, all mark-allocation vectors, all cut positions —
the same global-optimizer methodology as the round-7 explorer) the **true**
optimal response for the exact boundary configuration this worst case
describes: `A=(0.2,0.2,0.2,0.2,0.2)` (uniform, `m=5`, budget `4`). Result:
**true optimum `=0.5$ exactly, achieved with only `1` mark** (allocation
`(0,0,0,0,1)`: split the smallest/last piece in half — an instance of the
already-certified **Lemma TAIL-SNIP**, `m=5` odd, strictly decreases
`oddrank`), comfortably beating `c(4)\approx0.5161`. So the "IH tight
**and** `p_1` minimal" combination that breaks the naive algebraic bound
**does not correspond to an actual hard configuration** — when `p_1` is
forced small (by sortedness, forcing near-uniformity), the tail is *also*
easy (far from *its own* worst case), so the pessimistic plug-in
`oddrank(T')\approx c(m-2)S` used in the algebra above is not simultaneously
achievable with `p_1$ at its minimum. **This means the naive scalar
induction hypothesis ("the tail achieves `\le c(m-2)S`, full stop") is too
weak to prove PTBI even though PTBI itself is not contradicted by this
example** — a correct proof would need a *sharper*, `p_1`-aware induction
hypothesis (e.g. one that also bounds how close to `c(m-2)S` the tail's
best response can get *as a function of the tail's own spread*, which is
constrained once `p_1` bounds every tail element) rather than a single
scalar bound. Setting up and proving such a sharper hypothesis is **not**
completed this round — flagged as the precise open technical gap.

**Stress test against the two hard `m=5` witnesses (as mandated this
round).** Despite the induction not being proved in general, the
*specific* construction "peel `p_1`, solve `T` for its own independent
optimum (over the true, unrestricted allocation space, not just the
certified-lemma menu), then halve `p_1` via Lemma DOUBLE-INSERT" was
**tested directly, numerically, against both witnesses** the explorer
flagged as needing "genuine 3-piece coordination":

- `A=(0.4265,0.2536,0.1747,0.1014,0.0438)`, budget `4`, target
  `c(4)\approx0.5161`: tail-only optimum on `T=(0.2536,0.1747,0.1014,
  0.0438)` with `3$ marks `\approx0.2974` (allocation `(1,0,1,1)` on `T`,
  found by global optimization); merging with `p_1$ split exactly in half
  (`1` mark) gives `oddrank(B)\approx0.51065 < c(4)\approx0.5161$ —
  **closed**, with margin `\approx0.0055`. (The *true* global optimum on
  this witness, `\approx0.5009`, is strictly better and does need the
  3-piece coordination the explorer found — but that coordination is
  needed only to find the *optimal* response, not merely to beat the
  target `c(4)`.)
- `A=(0.3415,0.3023,0.1664,0.1404,0.0494)`, budget `4`, target
  `c(4)\approx0.5161`: tail-only optimum on `T=(0.3023,0.1664,0.1404,
  0.0494)` with `3` marks `\approx0.3315` (allocation `(1,0,1,1)`); merging
  with `p_1$ halved gives `oddrank(B)\approx0.50225<c(4)\approx0.5161$ —
  **closed**, and in fact this numerically **matches the true global
  optimum** on this witness to `5` decimal places, despite using a
  structurally different (non-coordinated, independently-recursed)
  allocation than the one the explorer's global search reported
  (`(2,1,0,1,0)` vs. the peel-and-halve strategy's effectively
  `(1,1,0,1,1)`) — i.e. **two different responses achieve (numerically)
  the same optimal value**, evidence the optimum is not unique here.

**Honest conclusion of the stress test.** Both hard `m=5` witnesses are, in
fact, closed by the much simpler "peel + independently-recursed tail +
unconditional halve" construction — this **refutes**, for the purposes of
proving the *upper bound* (not for finding the *true optimum*), the
explorer's concern that these witnesses require irreducible 3-piece
coordination. The same construction was also checked (as a sanity/
robustness test, not part of the mandated stress test) against two
previously-recorded hard `m=3` witnesses: the classic
`A=(0.5798,0.3515,0.0687)` (peel+halve gives `\approx0.53435`, exactly
matching Lemma PARTIAL-DOM-RESIDUAL's value) and the round-5 near-tied
`A=(0.4649,0.3042,0.2309)` (peel+halve gives `\approx0.53665$, slightly
worse than but still beating `c(2)` and below Lemma SANDWICH's
`\approx0.5351`) — both closed. So the peel+halve construction, whatever
its general proof status, is empirically a strong, simple, universally-
tested-so-far candidate.

**What remains genuinely open.** The general *proof* that peel+halve (or
any single fixed inductive recipe) always closes PTBI is **not**
established — the naive scalar-IH algebra fails at the "IH tight and `p_1`
minimal" combination, and while the concrete uniform-`A` instantiation of
that combination turns out to be easy (via a *different* mechanism, Lemma
TAIL-SNIP, not peel+halve at all), this only shows the *specific*
counterexample to the naive algebra is not itself a counterexample to
PTBI — it does not show peel+halve (or PTBI) is true in general, nor
does it rule out some other configuration genuinely breaking peel+halve
while still being consistent with PTBI via a different construction. A
complete proof would need either (a) a sharper, correlated induction
hypothesis relating `p_1`'s value to what the tail can achieve (as
diagnosed above), or (b) a case split between "use peel+halve" and "use
TAIL-SNIP / DOM / MULTI-HALVE / PARTIAL-DOM(-RESIDUAL)" depending on the
configuration's shape, with a proof that *some* member of this now-larger
menu always closes the gap — genuinely open, flagged precisely (not
vaguely) for a future round. **Do not re-attempt the naive single-scalar
peel+halve induction without first addressing the tight-IH-and-minimal-`p_1`
combination identified above** — record this so a future round does not
need to rediscover the same false start.

## Round 8: Lemma BLOCK-RECURSE proved, Claim PTBI reduced to one case, m=3 mostly closed

### Lemma BLOCK-RECURSE — PROVED IN FULL

Full statement and proof certified into `lemmas/block-recurse.md`; restated
briefly here. Given sorted `A=(p_1\ge\cdots\ge p_m)`, tail
`T=(t_1,\ldots,t_k)=(p_2,\ldots,p_m)`, prefix sums `S_j`, fix `1\le j\le k`
with `p_1\ge S_j` and `r:=p_1-S_j<t_j` (Lemma PARTIAL-DOM's hypotheses).
Split `p_1` into `(t_1,\ldots,t_j,r)` (`j` marks), merge with the full tail
`T`, and let the leftover `L_0=\{r\}\cup(t_{j+1},\ldots,t_k)` be refined by
**any** further sequence of splits, at **any** depth, to a multiset `W`.
Then, unconditionally,
```
oddrank(\{t_1,t_1,\ldots,t_j,t_j\}\cup W) = S_j + oddrank(W).
```
**Proof idea (full details in the lemma file).** Splitting a positive
value never increases the resulting parts beyond the original value, so by
induction on the number of splits, every element of any refinement `W` of
`L_0` is `\le\max(L_0)=\max(r,t_{j+1})\le t_j$ (using `r<t_j` and sortedness
`t_{j+1}\le t_j`). Hence the duplicated block `\{t_1,t_1,\ldots,t_j,t_j\}`
(each element `\ge t_j`) always occupies exactly the top `2j` ranks of the
merged sorted list, **regardless of how deep the recursive refinement of
`W` goes** — this is the genuinely new content over Lemma
PARTIAL-DOM-RESIDUAL, which only handled one further split. The block then
contributes exactly `S_j` (the same tie-insensitive pairing argument as
Lemma DOM's proof), and `W`'s own elements are shifted by the **even**
amount `2j`, preserving parity exactly, so `W` contributes exactly
`oddrank(W)`. Budget conservation (the recursive sub-instance on `L_0`,
size `m-j`, gets exactly budget `m-1-j`, telescoping to `m-1` at the top
level for any recursion depth) is proved by a one-line induction on
recursion depth in the lemma file. Ties at the exact boundary `t_j=\max(W)`
are handled explicitly (multiset-valued `oddrank` does not depend on
tie-breaking, only on how many boundary ranks are odd, a quantity fixed by
`j` and `|W|` alone) — not glossed over.

This strictly generalizes the certified Lemma PARTIAL-DOM (`W=L_0`, no
further refinement) and Lemma PARTIAL-DOM-RESIDUAL (`W`= one further
Lemma-SPLIT application) to full recursive re-optimization, exactly the
mechanism the round-8 outline called for.

### Lemma THRESHOLD-REDUCTION — PROVED IN FULL, reduces Claim PTBI to one case

Full statement and proof certified into `lemmas/ptbi-threshold-reduction.md`;
restated briefly here. Assume Claim PTBI holds for all sizes `<m` (strong
induction). Write `\Sigma:=\Sigma(A)`, `S:=\Sigma-p_1$.

**Case A (`p_1\ge c(m-1)\Sigma`): closed by peel+halve.** Split `p_1` in
half (1 mark, unconditional via **Lemma DOUBLE-INSERT**); apply the IH to
the tail `T` (size `m-1`, budget `m-2`) to get `oddrank(T')\le c(m-2)S`;
by Lemma DOUBLE-INSERT, total `\le g(p_1):=p_1/2+c(m-2)(\Sigma-p_1)`, using
exactly `m-1` marks. Since `c(m-2)>1/2` always (direct computation), `g` is
strictly decreasing in `p_1`, so `g(p_1)\le g(c(m-1)\Sigma)` for
`p_1\ge c(m-1)\Sigma`. A clean, **general, algebraically proved identity**
```
c(k-1) = \frac{c(k)}{2(1-c(k))}   \text{ for every } k\ge1
```
(direct computation from `1-c(k)=(2^k-1)/(2^{k+1}-1)`, verified in full in
the lemma file — not a numeric coincidence, an exact algebraic identity)
gives, with `k=m-1`, exactly `g(c(m-1)\Sigma)=c(m-1)\Sigma`. Hence
`oddrank(B)\le c(m-1)\Sigma` throughout Case A. **Fully closed for every
`m\ge2`.**

**Case B (`\Sigma/2\le p_1<c(m-1)\Sigma`): closed by DOM directly.**
`p_1\ge\Sigma/2 \iff p_1\ge S`, exactly Lemma DOM's hypothesis; Lemma DOM
gives `oddrank(B)=p_1` exactly (`m-1` marks), and `p_1<c(m-1)\Sigma` by
hypothesis closes it immediately, **no recursion needed**.

**Conclusion.** Cases A and B jointly cover `p_1\ge\Sigma/2` (since
`c(m-1)>1/2`, the two ranges `[c(m-1)\Sigma,\infty)` and
`[\Sigma/2,c(m-1)\Sigma)` are adjacent and cover `[\Sigma/2,\Sigma]`). So
**Claim PTBI's inductive step reduces exactly to the single remaining
case `p_1<\Sigma(A)/2`** — a genuinely new, unconditional, general-`m`
reduction that was not on record before this round (round 7's attempt
worked only with peel+halve, which is exactly Case A here, and did not
identify or prove the DOM case B / exact threshold).

### Case C (`p_1<\Sigma/2`): NOT closed in general — detailed `m=3` investigation

**General-`m` structural fact proved.** If `p_1\ge2p_2$ (Lemma HALVE's
hypothesis) held simultaneously with every tail element `\le p_1/2` (which
follows from sortedness once `p_1\ge2p_2$, since `p_i\le p_2\le p_1/2` for
`i\ge2`), then `\Sigma\le p_1+(m-1)p_1/2 = p_1(m+1)/2`, forcing
`p_1\ge2\Sigma/(m+1)`. For `m=3` this gives `p_1\ge\Sigma/2`, **contradicting
Case C's hypothesis `p_1<\Sigma/2`** — so for `m=3` specifically, **Lemma
HALVE's hypothesis never fires inside Case C** (proved, not just observed:
`p_1\ge2p_2` and `p_1<\Sigma/2` are mutually exclusive when `m=3`). For
`m\ge4` this vacuousness argument does **not** generalize (`2\Sigma/(m+1)
<\Sigma/2` once `m\ge4`, so HALVE's hypothesis and Case C can coexist);
recorded honestly as a fact specific to `m=3`, not a general lemma.

**`m=3` (`n=2`) progress, normalizing `\Sigma=1`, target `c(2)=4/7`.**

1. **Sub-case `p_3\le1/7`: closed exactly, by "peel+halve both `p_1` and
   `p_2`" (`K=2` unconditional DOUBLE-INSERT, no hypothesis).** Starting
   from `\{p_3\}` (`oddrank=p_3`), inserting `\{p_2/2,p_2/2\}` then
   `\{p_1/2,p_1/2\}` via two applications of the certified,
   hypothesis-free Lemma DOUBLE-INSERT gives, **exactly**,
   `oddrank(B)=p_3+p_2/2+p_1/2 = p_3+(1-p_3)/2 = 1/2+p_3/2` (using
   `p_1+p_2=1-p_3`), using `2` marks (full budget). This is `\le4/7$ exactly
   when `p_3\le1/7` — an exact, sharp, algebraic characterization (matching
   the round-8 explorer's numeric finding, now derived from certified
   machinery rather than asserted). **Fully closed.**
2. **Sub-case `p_1\ge1/2` (`p_3` arbitrary): closed by combining Cases A/B
   above with a new sharp computation for `p_1>4/7`.** Case B
   (`1/2\le p_1<4/7`) is already closed above. For `p_1>4/7` (Case A's
   regime, but now checking the *exact* Lemma HALVE value rather than the
   generic peel+halve bound, since it is sharper): **claim `p_2\le p_1/2`
   is forced whenever `p_1>4/7` and `p_3>1/7`.** Proof: if `p_2>p_1/2`,
   then `1=p_1+p_2+p_3>4/7+p_1/2+1/7`; since `p_1>4/7`, `p_1/2>2/7`, giving
   `1>4/7+2/7+1/7=1`, a contradiction. So `p_2\le p_1/2`, i.e. Lemma
   HALVE's hypothesis `p_1\ge2p_2` holds. Lemma HALVE (leaving `T=(p_2,p_3)`
   untouched, `oddrank(T)=p_2`, `1` mark) gives `oddrank(B)=p_1/2+p_2 =
   1-p_1/2-p_3` (using `p_2=1-p_1-p_3`). Since `p_1>4/7\Rightarrow p_1/2>2/7`
   and `p_3>1/7` (this sub-case), `p_1/2+p_3>3/7`, so
   `oddrank(B)=1-(p_1/2+p_3)<1-3/7=4/7$, **strictly** — closed. If instead
   `p_3\le1/7` in this same range `p_1>4/7`, sub-case 1 already closes it.
   **So `p_1>4/7$ is fully closed in every sub-case.** Combined with Case B,
   **the entire region `p_1\ge1/2` is closed for `m=3`, unconditionally.**
3. **Remaining region: `p_1<1/2` (Case C) and `p_3>1/7` (sub-case 1 does
   not apply). NOT fully closed.** Proved that Lemma HALVE's hypothesis is
   vacuous here (structural fact above), so the two live candidates are
   **TAIL-SNIP** (`oddrank=p_1+p_3/2`, unconditional since `m=3` odd) and
   **BLOCK-RECURSE with `j=1`** (`L=(p_2,r)$, `r=p_1-p_2<p_2` automatic in
   this region, `\Sigma(L)=p_1`; apply the already-**fully proved** `n=1`
   result to `L` exactly, giving `oddrank(B)=p_2+oddrank(L')` with
   `oddrank(L')` given by the closed-form `n=1` cases). **Two concrete,
   independently checked worked examples show these two candidates are
   genuinely complementary, neither dominating the other:**
   - `(p_1,p_2,p_3)=(0.45,0.275,0.275)`: TAIL-SNIP gives
     `0.45+0.1375=0.5875>4/7\approx0.5714` (**fails**); BLOCK-RECURSE
     `j=1` gives `L=(0.275,0.175)`, `n=1`-normalized `p_{\mathrm{norm}}
     =0.275/0.45\approx0.611\in[1/2,2/3]`, so the `n=1` "do nothing"
     sub-case applies, `oddrank(L)=0.275`, total
     `=0.275+0.275=0.55<4/7` (**succeeds**).
   - `(p_1,p_2,p_3)=(0.4,0.35,0.25)`: **round-9 correction to a round-8
     computational error.** The round-8 write-up mislabeled BLOCK-RECURSE
     `j=1`'s recursion target as `L=(p_2,r)=(0.35,0.05)`; the correct
     leftover per Lemma BLOCK-RECURSE's own statement (`j=1`, matched
     prefix `\{t_1\}=\{p_2\}$, unmatched tail `U=(p_3)$) is
     `L_0=\{r\}\cup U=(r,p_3)=(0.05,0.25)`, **not** `(p_2,r)$ — `p_2$ is
     already consumed by the matched block and must not reappear in the
     recursion. Recomputing with the correct `L_0=(0.25,0.05)`:
     `p_{\mathrm{norm}}=0.25/0.30=5/6\in[2/3,1]`, so `n=1`'s "halve the
     max" sub-case applies to `L_0`, giving
     `oddrank(L_0')=\Sigma(L_0)-0.25/2=0.30-0.125=0.175`, total
     `=p_2+oddrank(L_0')=0.35+0.175=0.525`, **not** `0.575` — BLOCK-RECURSE
     `j=1` **succeeds** here (`0.525<4/7\approx0.5714`), matching TAIL-SNIP
     exactly (`0.4+0.125=0.525`), not exceeding it. Independently verified
     by direct exact-`Fraction` computation of the full merged multiset
     (`\{p_2,p_2\}\cup\{\text{refined }L_0\}$) and by a global numeric
     optimizer over all mark-allocations on this exact instance: the true
     optimum is exactly `0.525$, confirming the corrected value, not the
     erroneous `0.575`. **This changes the round-8 conclusion**: on this
     example the two candidates do not turn out to be complementary after
     all — see the round-9 general closure below, which shows this
     coincidence (`BLOCK-RECURSE`\,`j{=}1$ = TAIL-SNIP exactly) is not an
     accident of this example but an algebraic identity holding on an
     entire sub-region of Case C.

   So `\min(\text{TAIL-SNIP}, \text{BLOCK-RECURSE-}j{=}1)` succeeds on both
   worked examples, but **a general proof that this minimum is always
   `\le4/7` throughout the region `p_1<1/2,\,p_3>1/7`, `m=3`, was not
   completed this round** — the algebra requires tracking the `n=1`
   sub-case boundary (`p_2/p_1\gtrless2/3`) jointly with the TAIL-SNIP
   formula as `p_1,p_2,p_3` vary, a 2-parameter piecewise-affine
   optimization that was set up (see the two formulas above) but not
   finished. Also checked and **ruled out** as a shortcut: **Lemma
   SANDWICH does not help in this region** — its exact `m=3` value is
   `p_2+p_3=1-p_1$, which exceeds `4/7$ whenever `p_1<3/7`, i.e. it is
   *not even usable* for a large part of Case C (e.g. both examples above
   have `p_1\ge3/7`, so `SANDWICH` gives `0.55`/`0.6` respectively — worse
   than or equal to the best of TAIL-SNIP/BLOCK-RECURSE in both cases, not
   a new tool here).

**Honest summary of Case C.** For `m=3`: the region `p_1<1/2,\,p_3\le1/7`
is closed (sub-case 1); the region `p_1\ge1/2` is fully closed (point 2);
the remaining region `p_1<1/2,\,p_3>1/7` has two complementary candidates
(TAIL-SNIP, BLOCK-RECURSE `j=1`) each closing part of it (verified on two
concrete examples that pin down where each is needed), but the **general
closure of this last region is not proved** — this is the precise,
narrowed-down open gap even for the smallest nontrivial case `m=3`
(`n=2`). For general `m\ge4`, Case C is entirely open (the `m=3`-specific
vacuousness of Lemma HALVE does not generalize, and BLOCK-RECURSE's
general-`j` optimization was not carried out algebraically — only
`j=1` was analyzed, and only for `m=3`).

### What this round establishes, honestly

- Lemma BLOCK-RECURSE: **complete, certified proof**, general `m`, any
  tail shape, any recursion depth — the actual missing mechanism the
  round-8 outline asked for.
- Lemma THRESHOLD-REDUCTION: **complete, certified proof**, general `m` —
  reduces Claim PTBI's inductive step to the single case `p_1<\Sigma/2`,
  a genuine narrowing not on record before this round.
- `m=3` (`n=2`): the *general upper bound over arbitrary configurations*
  is now proved for **all but one precisely-isolated sub-region**
  (`p_1<\Sigma/2` **and** `p_3>\Sigma/7`), where two candidate
  constructions are shown to be complementary on worked examples but not
  proved to jointly cover the region in general.
- General `m\ge4`: Case C (`p_1<\Sigma/2`) remains **entirely open** — the
  finite-menu strong induction the outline called for is **not**
  completed. This is a real, substantial narrowing of the open gap (from
  "the whole induction is unproved" to "only the `p_1<\Sigma/2` case, for
  each `m`, remains"), but Claim PTBI is **not** proved this round.

## Full proof
(Not present — Status is `partial`. The `n=1` case is a complete, closed
sub-result; Lemma DOM settles a large sub-case of every `n`
(`S \le p_1 \le c(n)`, any tail shape); Lemma HALVE (and its round-7
hypothesis-free generalization, Lemma DOUBLE-INSERT) gives a proven
reduction identity; Lemma TAIL-SNIP gives a third proven, hypothesis-free
single-move identity (splitting the smallest piece, valid — and strictly
beneficial — whenever the current piece-count is odd); Lemma MULTI-HALVE,
Lemma PARTIAL-DOM(-RESIDUAL) extend the certified menu further (round 7).
Round 7 also attempted a direct general induction (Claim PTBI, "peel `p_1`,
recurse on the tail") using Lemma DOUBLE-INSERT — this closes both of the
round-7 explorer's hard `m=5` witnesses concretely (numerically verified,
beating `c(4)` with the simple peel+halve construction, refuting the
concern that they need irreducible 3-piece coordination *for the upper
bound*), but the induction is **not** proved in general: the naive
scalar induction hypothesis fails algebraically at the "IH tight and `p_1`
minimal" combination, and while the concrete boundary instance of that
combination (uniform `A`) turns out to be easy via a different mechanism
(Lemma TAIL-SNIP), this does not by itself repair the general induction —
a genuinely sharper, `p_1`-correlated induction hypothesis (or a further
case split across the now-larger menu) is needed and remains open,
precisely diagnosed above (see "Round 7: ... the retargeted induction
attempt"). Round 5 separately sharpened, rather than closed, the "neither
DOM nor HALVE fires" obstruction: the true optimal response there can
require a **coordinated simultaneous split of two (or more) pieces at
jointly-optimized, generally non-half ratios** — a mechanism the round-6/7
menu (PARTIAL-DOM, SANDWICH, MULTI-HALVE, PARTIAL-DOM-RESIDUAL) now
constructively covers in every sampled instance up to `m=4` and covers the
two hardest recorded `m=5` witnesses via the simpler peel+halve route, but
a general theorem that *some* member of the menu (or induction) always
closes the gap, for every `m`, remains open work for a future round; every
exact numeric witness discussed above is recorded so it does not need to be
re-discovered. **Round 8** proved **Lemma BLOCK-RECURSE** (the recursive
generalization the round-8 outline called for, general `m`, full proof) and
**Lemma THRESHOLD-REDUCTION** (a new, general, unconditional reduction of
Claim PTBI's inductive step to the single case `p_1<\Sigma(A)/2`, via the
proved algebraic identity `c(k-1)=c(k)/(2(1-c(k)))`), then used them to
close `m=3` (`n=2`) for the general upper bound down to one precisely
isolated sub-region (`p_1<\Sigma/2` and `p_3>\Sigma/7`), where two
candidate constructions (TAIL-SNIP, BLOCK-RECURSE `j=1`) are shown
complementary on concrete examples but not proved to jointly cover the
region in general; for `m\ge4` this last case (`p_1<\Sigma/2`) remains
entirely open. **Round 9** fully closes `m=3`: a corrected exact
closed-form for `\text{BLOCK-RECURSE}_1` (the round-8 write-up's example
had a labelling error, corrected this round) combined with an exact
2-parameter piecewise algebra shows `\min(\text{TAIL-SNIP},
\text{BLOCK-RECURSE}_1)\le c(2)=4/7` throughout **all** of Case C
(`p_1<\Sigma/2`, no further hypothesis needed) — **`m=3`'s general upper
bound is now `solved` in full, unconditionally over every configuration.**
Round 9 also proves a new, fully general, hypothesis-free **Lemma
PAIR-VALUE** (`lemmas/pair-value.md`): any decomposition of a multiset into
tied pairs (of arbitrary value, in arbitrary relative position — no
domination or contiguity needed at all) plus an unpaired remainder gives
`oddrank = \sum(\text{pair values}) + oddrank(\text{remainder})`
unconditionally, strictly generalizing both Lemma DOUBLE-INSERT and Lemma
BLOCK-RECURSE and dissolving the "contiguity may not transfer to arbitrary
subsets" risk flagged for arbitrary-subset (non-prefix) matching — it
transfers, because contiguity was never actually required. This lemma's
SUBSET-DOM corollary closes the concrete round-9 falsifying witness
(`A=(12,6,5,4,2)/29`, `m=5`, budget `4`: achieves exactly `oddrank=1/2 <
c(4)=16/31`, beating the previous certified menu's best value
`15/29>c(4)` on this instance) via a genuinely non-prefix subset match
(`p_2\to\{p_4,p_5\}`, skipping `p_3`) that Lemma BLOCK-RECURSE alone could
not express. **`m\ge4`'s general Case C induction remains open** — Lemma
PAIR-VALUE is a strictly more powerful reusable tool than BLOCK-RECURSE,
and closes the one concrete counterexample, but a general theorem that
some donor/target-subset choice always closes Case C for every `m` (which
would need Hall's marriage theorem to handle simultaneous multi-donor
matches without conflict) is not established this round. This is real,
substantial progress — `m=3` is now a fully closed sub-result, and the
`m\ge4` obstruction is sharper and better-tooled than before, but Claim
PTBI in full generality is not proved.)

## Round 10: two new certified lemmas (ALL-BUT-MIN, MATCH-TAIL-PAIR), a corrected false alarm, a proved structural obstruction to naive recursion, and a sharpened residual gap for general `m\ge4`

**Target this round** (per the round-10 outline): close Claim PTBI's Case C
(`p_1<\Sigma(A)/2`) for general `m\ge4`, first testing the Fact-0
(evensum-reformulation) opening cheaply, falling back to a Hall-type
existence argument if that stalls.

### Step 0 — the Fact-0 reformulation does not give an independent shortcut

Tested directly: since `oddrank(B)=\Sigma(A)-evensum(B)` and `evensum` is
maximized (Fact 0) by the consecutive pairing of `B`'s *own* sorted order,
reframing "minimize `oddrank(B)`" as "maximize `evensum(B)`" is a genuine
equivalence, not merely intuition — but it does not change the actual
computational content: the reachable set of multisets `B` is identical
either way, and every numeric/algebraic computation below (all done
directly via `oddrank`) is exactly the computation Fact 0 would also
require. **No independent tractable structure was found via this
reframing** — it explains *why* the constructions below (tied-pair
insertions) are natural, but supplies no shortcut around the existence
problem. This matches the outline's own caveat; reported honestly as a
negative (if cheap) finding rather than silently dropped.

### Step 1 — correcting a false alarm from a buggy test harness

While testing whether Lemma PAIR-VALUE's matching framework (donor + target
subset, recursively applied) suffices in general, an initial from-scratch
brute-force search harness (built to explore Case C witnesses) contained a
bug: its "self-halve" move recursed on the post-halving list `U_{\text{self}}`
*and* added the halved value `p_i/2` a second time on top, double-counting
the halved pair's contribution. This produced a spurious "true optimum"
`\approx0.6229` on a concrete `m=4` witness that appeared to require
splitting two tail elements into non-tied, cross-piece-tying fragments — a
finding that would have contradicted the sufficiency of the matching
framework entirely. **After finding and fixing the bug** (removing the
duplicated `+p_i/2` term — a self-halve move should simply recurse on the
post-halving list directly, since that list already contains the two actual
halves as elements), the corrected brute force reproduces the true optimum
`\approx0.5011` found independently by a full continuous optimizer
(`scipy.optimize.minimize`, Nelder–Mead, over every mark-allocation vector
and split ratio) **exactly**, via a purely matching-based construction
(`SUBSET-DOM` matching `p_3\!\to\!\{p_4\}$, then self-halving the residual —
i.e. `BLOCK-RECURSE_1` composed with one further split, already-certified
machinery). **This corrects, rather than confirms, a concern that would
otherwise have been reported this round**: the matching + self-halve
framework (Lemma PAIR-VALUE and its corollaries) is not structurally
insufficient here — the earlier appearance of a "cross-piece, non-tied
split needed" obstruction was an artifact of the buggy harness, not a real
finding. Recorded here so no future round rediscovers or is misled by it.
(Witness: `A=(249/710,\,99/284,\,779/2840,\,15/568)`, `m=4`, budget `3`,
target `c(3)=8/15\approx0.5333`; corrected true optimum
`1423/2840\approx0.5011$, achieved with only `2` of the `3` available marks,
leaving `p_1,p_2` completely untouched.)

### Step 2 — two new certified lemmas, generalizing the `m=3` sub-case-1 threshold

**Lemma ALL-BUT-MIN** (`lemmas/all-but-min.md`, full proof there). For any
`A=(p_1\ge\cdots\ge p_m)`, splitting every element **except** the smallest
into exact halves (`m-1` marks) gives, unconditionally (direct corollary of
the already-certified, hypothesis-free Lemma PAIR-VALUE — `m-1` tied pairs
`\{p_i/2,p_i/2\}$ plus the single unpaired `p_m`):
```
oddrank(B) = \Sigma/2 + p_m/2,
```
which meets the target `c(m-1)\Sigma` exactly when
`p_m\le\Sigma/(2^m-1)$ (derived from the general identity
`2c(k)-1=1/(2^{k+1}-1)`, checked directly: `1-2^{-k}` grows with `k`\, hence
`c(k)=1/(2-2^{-k})` is **strictly decreasing** in `k` — a clean, general,
one-line proof of a fact used repeatedly throughout this file's Case A/B
arguments but not previously stated as its own lemma). This is exactly the
`m`-general form of round 9's `m=3` sub-case-1 (`p_3\le\Sigma/7$), now
derived in one line from Lemma PAIR-VALUE instead of two iterated
applications of Lemma DOUBLE-INSERT.

**Lemma MATCH-TAIL-PAIR** (`lemmas/match-tail-pair.md`, full proof there).
Halving `p_1,\ldots,p_{m-2}$ (`m-2` marks) and matching `p_{m-1}$ to `p_m$
(donor `p_{m-1}\ge p_m`, `1` mark, residual `r=p_{m-1}-p_m`) gives,
unconditionally (again a direct Lemma PAIR-VALUE corollary — `m-2$ pairs
from the halved prefix, `1` further pair `\{p_m,p_m\}`, unpaired residual
`\{r\}`):
```
oddrank(B) = \Sigma/2 + (p_{m-1}-p_m)/2,
```
meeting the target whenever `p_{m-1}-p_m\le\Sigma/(2^m-1)` — a
**complementary** sufficient condition to ALL-BUT-MIN (small *gap* between
the two smallest elements, regardless of their absolute size, rather than
one absolutely small element).

Both lemmas independently verified exactly (`Fraction` arithmetic,
`2,000$-plus trials each, `m=2,\ldots,8`) and both close every concrete
witness recorded in rounds 8–9 for the `m=3` residual region.

### Step 3 — a proved structural obstruction: naive single-peel-plus-IH constructions cannot close Case C

**Fact (single-small-peel is provably insufficient).** Consider any
construction of the shape: use `1` mark to create a single tied pair of
value `v$ (via matching or self-halving some element), reducing the
configuration to a size-`(m-1)` instance of total mass `\Sigma-2v`, then
apply the strong induction hypothesis (Claim PTBI at size `m-1`, budget
`m-2`) to that instance. The resulting bound is
```
g(v) := v + c(m-2)(\Sigma-2v) = c(m-2)\Sigma + v\bigl(1-2c(m-2)\bigr).
```
Since `c(m-2)>1/2` for every finite `m-2$ (proved above via
`c(k)=1/(2-2^{-k})`), the coefficient `1-2c(m-2)` is **strictly negative**,
so `g` is strictly **decreasing** in `v`, hence **maximized at `v=0`**,
where `g(0)=c(m-2)\Sigma`. Since `c` is strictly decreasing (same fact),
`c(m-2)>c(m-1)`, so `g(0)>c(m-1)\Sigma` **always**, strictly. Consequently:
**no construction of this single-tied-pair-then-full-strength-IH shape can
ever close Case C uniformly** — its bound already exceeds the target at
`v=0` and only improves (weakly) as `v$ grows, so it is fundamentally
"one recursion level too weak" whenever the peeled value `v` is small. This
is a clean, general, fully proved (not merely numerically observed)
diagnosis of exactly why every single-peel-plus-IH construction tried in
rounds 7–10 (peel `p_1$ and halve — Case A itself; peel-match `p_m$ to any
donor; peel-match `p_{m-1}$ to `p_m$ then IH on the rest) systematically
fails in Case C: the *only* way to avoid losing a full "level" of induction
strength is to spend **all** `m-1` marks directly via an unconditional
multi-pair identity (Lemma PAIR-VALUE) rather than deferring to a weaker
`(m-2)`-strength inductive hypothesis on the untouched remainder — exactly
the mechanism Lemma ALL-BUT-MIN and Lemma MATCH-TAIL-PAIR use, and exactly
why they, not naive recursion, are the right building blocks.

### Step 4 — even the extended two-lemma menu does not close Case C in general (`m\ge5`)

**Tested exhaustively** (20,000 random Case-C configurations, `m=4,\ldots,8`,
exact `Fraction` arithmetic) whether `\min(\text{ALL-BUT-MIN},
\text{MATCH-TAIL-PAIR}) \le c(m-1)\Sigma` throughout Case C: **it does not**.
Concrete violation found and independently reproduced exactly:
```
A = (1826, 1563, 1520, 1514, 765)/7188   (m=5, \Sigma=1),
```
`p_1=1826/7188\approx0.254<1/2$ (Case C holds). Neither sufficient
condition fires: `p_5=765/7188\approx0.1064 > 1/31\approx0.0323`
(ALL-BUT-MIN's threshold) and `p_4-p_5=749/7188\approx0.1042>1/31`
(MATCH-TAIL-PAIR's threshold). Their minimum value is
`7937/14376\approx0.5521`, exceeding the target `c(4)=16/31\approx0.5161`
by `\approx0.036`. A full brute-force search over the matching+self-halve
move set (the corrected harness from Step 1) confirms this witness *is*
solvable — true optimum `1199/2396\approx0.5004$, comfortably below target
— but the winning sequence is a **deep, multi-level** recursive
composition (halve `p_1`; halve `p_2`; match `p_3$ to `p_4$ — nearly tied
already, residual `\approx0`; then recursively match/halve several of the
newly created fragments against each other, five total moves), not an
instance of any single closed-form menu item (ALL-BUT-MIN, MATCH-TAIL-PAIR,
BLOCK-RECURSE, TAIL-SNIP, DOM, HALVE, or MULTI-HALVE applied once). This
confirms, with a concrete witness (not just a diagnosis), that **the
residual gap genuinely requires either a substantially larger menu of
closed-form constructions or a real existence theorem for a good recursive
matching sequence** — the two new lemmas this round are genuine, certified
extensions of the menu, and the corrected Step-1 finding shows the matching
framework's *mechanism* (Lemma PAIR-VALUE, recursively applied) is not
structurally blocked — but no general inductive argument establishing *a
good sequence always exists* was found or proved this round.

### Honest summary of round 10

- Fact-0 reformulation: tested, gives no independent shortcut (Step 0).
- A potential "cross-piece ties beyond the matching framework" concern from
  this round's own exploratory harness was traced to a **bug in the test
  script**, not a mathematical finding — corrected, not reported as a
  discovery (Step 1). The matching + self-halve mechanism (Lemma
  PAIR-VALUE) remains, as far as tested, structurally adequate; only
  *existence of a good sequence in general* is missing.
- Two new lemmas certified in full (Lemma ALL-BUT-MIN, Lemma
  MATCH-TAIL-PAIR), each closing an explicit further sub-region of Case C
  for every `m\ge2`, via one-line corollaries of the already-certified
  Lemma PAIR-VALUE (Step 2).
- A general, fully proved structural fact (Step 3) explains *why* every
  naive single-peel-plus-IH construction tried so far (across rounds 7–10)
  cannot close Case C, sharpening the diagnosis from "not yet found" to
  "provably the wrong shape of argument."
- A concrete witness (Step 4) shows the two new lemmas, while genuine
  progress, still do not close Case C for `m=5` — the general existence
  theorem for a good recursive matching/self-halving sequence, for every
  `m\ge4`, **remains open**. This is real, verified, narrower progress, not
  a closure: Claim PTBI's Case C for general `m\ge4` is not proved this
  round, and the honest status remains `partial`.

## Promotable lemmas

- **Lemma WF-C5 (round 12, NEW, fully proved).** The Candidate-5
  recursion (`solve(A,\mathrm{budget})` = min of peel+halve,
  PARTIAL-DOM-maximal-prefix with a `\mathrm{budget}`-decremented
  leftover, and a `\mathrm{budget}`-gated TAIL-SNIP) terminates on every
  call reachable from `\mathrm{solve\_full}(A)=\mathrm{solve}(A,1)`, via
  the well-founded lexicographic measure `(\mathrm{budget},|A|)` with
  `\mathrm{budget}` primary (correcting an outline draft's
  self-contradictory `(|A|,\mathrm{budget})` ordering), using the
  explicitly-proved fact that PARTIAL-DOM's maximal matched prefix length
  `j^*` is always `\ge1` when `|A|\ge2` (immediate from sortedness:
  `A[0]\ge A[1]=S_1`). Full proof in "Round 12 build" above. Narrow in
  scope (specific to this one recursive construction) but fully general
  within that scope and reusable if Candidate 5 is picked up by a future
  round or approach. Recommend certifying.
- **Lemma ALL-BUT-MIN (round 10, NEW, fully proved).** For any sorted
  `A=(p_1\ge\cdots\ge p_m)`, `m\ge2`, halving every element except the
  smallest (`m-1` marks) gives, unconditionally,
  `oddrank(B)=\Sigma(A)/2+p_m/2` — a one-line corollary of the certified
  Lemma PAIR-VALUE, generalizing round 9's `m=3` sub-case-1 threshold
  (`p_3\le\Sigma/7`) to `p_m\le\Sigma/(2^m-1)` for every `m`. Full proof and
  independent verification in `lemmas/all-but-min.md`. Recommend certifying.
- **Lemma MATCH-TAIL-PAIR (round 10, NEW, fully proved).** Halving
  `p_1,\ldots,p_{m-2}` and matching `p_{m-1}` to `p_m` (`m-1` marks total)
  gives, unconditionally, `oddrank(B)=\Sigma(A)/2+(p_{m-1}-p_m)/2`,
  complementary to Lemma ALL-BUT-MIN (closes the case where the two
  smallest elements are close to each other, regardless of absolute size).
  Full proof and independent verification in `lemmas/match-tail-pair.md`.
  Recommend certifying. **Neither lemma, nor their combination, closes
  Case C in general** — a concrete `m=5` witness where both fail is
  recorded in the round-10 section above.
- **Fact (single-small-peel obstruction, round 10, fully proved).** Any
  construction of the shape "make one tied pair of value `v`, then apply
  the induction hypothesis at size `m-1`" gives a bound
  `g(v)=c(m-2)\Sigma+v(1-2c(m-2))`, strictly decreasing in `v` and always
  `>c(m-1)\Sigma` at `v=0` (since `c(k)=1/(2-2^{-k})` is strictly
  decreasing, proved in one line) — a clean, general, reusable structural
  fact explaining why every naive single-peel-plus-IH construction tried
  in rounds 7–10 fails in Case C. Small but genuinely reusable diagnostic
  content for any future round attempting a recursive proof shape here.
- **Fact 0 (evensum = max sum-of-mins over consecutive pairing).** General
  fact about sorted multisets, proved in full above. Reusable background for
  any future strategy design on this problem (motivates why "duplicate a
  piece to pair with a neighbor" is the natural move), though not itself
  load-bearing in the lemmas that follow.
- **Lemma DOM (Generalized Domination Construction).** For *any* sorted list
  `p_1\ge\cdots\ge p_m` with `p_1 \ge S := \Sigma_{i\ge2}p_i`, splitting `p_1`
  into `k=m-1` marks' worth of parts `(p_2,\ldots,p_m, p_1-S)` and merging
  with the untouched tail achieves `oddrank(B) = p_1` **exactly**, for *any*
  tail shape (not just geometric), proved in full generality above (this
  strictly generalizes the certified Proposition 4, which is the special
  case `A=A_n`). This is a clean, fully proved, reusable lemma — recommend
  certifying into `lemmas/` for use by any future approach attacking either
  half of the minimax (it immediately re-derives Proposition 4 as a
  corollary, and settles the `S\le p_1\le c(n)` sub-case of the general
  upper bound for every `n`).
- **Lemma HALVE (Halving reduction identity).** For any `A` with
  `p_1 \ge 2p_2`, splitting `p_1` into two equal halves gives the exact
  identity `oddrank(B_0) = p_1/2 + oddrank(T)` (and more generally
  `oddrank(B) = p_1/2 + oddrank(T')` for any further refinement `T'` of the
  tail `T`), proved in full above by a rank-shift argument. Reusable as a
  reduction step for any future inductive attempt at the general upper
  bound, though (as documented above) it is not by itself sufficient to
  close the induction — the open gap is precisely locating/proving the
  correct *general* combination of Lemma DOM and Lemma HALVE applied
  recursively to the tail.
- **Lemma DOM-boundary-slack (NEW, round 5, proved in full).** In Lemma
  DOM's boundary case `p_1=S` exactly, the same domination value
  `oddrank(B)=p_1` is achieved using only `k-1` marks instead of `k` — an
  exact, unconditional consequence of "splitting into `j` parts costs
  `j-1` marks." Small but genuinely load-bearing for any future budget
  accounting in a cascading DOM/HALVE induction; recommend certifying.
- **Lemma SPLIT (NEW, round 5, proved in full, fully general).** For any
  sorted list `a_1\ge\cdots\ge a_m` and any index `i` with
  `a_i/2\ge a_{i+1}`, splitting `a_i` into two equal halves changes
  `oddrank` by the exact closed form `-a_i/2+2\,oddrank(R)-\Sigma(R)`
  (`i` odd) or `a_i/2+\Sigma(R)-2\,oddrank(R)` (`i` even), where
  `R=(a_{i+1},\ldots,a_m)`. Proved in full by a rank-shift argument
  generalizing Lemma HALVE's proof; independently cross-checked by
  re-deriving Lemma HALVE as the `i=1` special case. Strictly generalizes
  Lemma HALVE (splitting any position, not just the top) — recommend
  certifying as a reusable general-purpose tool for any future single-piece
  splitting argument on this problem.
- **Lemma TAIL-SNIP (NEW, round 5, proved in full, corollary of Lemma
  SPLIT).** Splitting the smallest element `a_m` of any sorted positive
  list is **always well-defined with no hypothesis** and changes `oddrank`
  by exactly `-a_m/2` (piece-count `m` odd, strict improvement) or
  `+a_m/2` (`m` even, strict worsening). The first hypothesis-free
  single-move identity found for this problem. Proved insufficient *by
  itself* to close the "neither DOM nor HALVE fires" gap (exact
  counterexample recorded above), but reusable as a building block:
  recommend certifying alongside the negative result (its exact
  counterexample) so future rounds building coordinated multi-piece moves
  can start from a correct base case rather than re-deriving or
  re-refuting it.
- **Lemma MULTI-HALVE (NEW, round 7, certified in `lemmas/multi-halve.md`).**
  Generalizes Lemma HALVE from `K=1` to simultaneously halving the top `K`
  pieces whenever `p_K\ge2p_{K+1}`: `oddrank(B)=\sum_{i=1}^Kp_i/2+
  oddrank(\text{Tail})`. Proved by the identical rank-shift technique as
  Lemma DOM/HALVE/SPLIT (even shift by `2K`). Closes a witness where
  neither DOM nor HALVE fires but a *weaker* pairwise hypothesis
  (`p_2\ge2p_3`) does.
- **Lemma PARTIAL-DOM-RESIDUAL (NEW, round 7, certified in
  `lemmas/partial-dom-residual.md`).** Composes the already-certified
  Lemma PARTIAL-DOM and Lemma SPLIT: after a (possibly sub-maximal)
  PARTIAL-DOM chain leaves budget to spare, refining the residual `r` in
  place via Lemma SPLIT strictly improves the value whenever the SPLIT
  hypothesis holds at `r`'s known sorted rank. No new proof machinery —
  purely a composition of two already-certified lemmas, worth stating as
  its own named move since PARTIAL-DOM's original write-up never revisited
  `r` with leftover budget.
- **Lemma DOUBLE-INSERT (NEW, round 7, certified in
  `lemmas/double-insert.md`, general and hypothesis-free).** Inserting a
  duplicated value `\{v,v\}` into *any* sorted list `T` changes `oddrank`
  by exactly `+v`, **unconditionally** — no domination or ordering
  hypothesis needed, because two numerically-equal pieces are always
  mutually adjacent in sorted order regardless of where they land. Strictly
  generalizes Lemma HALVE (which required `p_1\ge2p_2`) by showing that
  hypothesis was never load-bearing for the *value* identity, only for
  historically assuming the pair lands at the very top. Central to the
  round-7 induction attempt (Claim PTBI) and reusable well beyond it — any
  future construction that splits a piece into two *equal* parts can invoke
  this unconditionally, with no domination check required.
- **Lemma BLOCK-RECURSE (NEW, round 8, certified in
  `lemmas/block-recurse.md`, general `m`, any tail shape, any recursion
  depth).** The duplicated matched block from a Lemma PARTIAL-DOM split
  dominates the leftover `\{r\}\cup U` **before and after arbitrarily deep
  further refinement** (splitting only shrinks the max element, by a
  one-line induction on split count), so the block always occupies exactly
  the top `2j` ranks and the leftover's contribution to `oddrank` is
  exactly its own standalone `oddrank`, no matter how the leftover is
  further recursively optimized. Strictly generalizes Lemma PARTIAL-DOM and
  Lemma PARTIAL-DOM-RESIDUAL (both are special cases with `0` or `1` further
  splits). This is the key mechanism enabling a strong induction on
  piece-count for the general upper bound — the round-8 outline's central
  target, now fully proved and reusable.
- **Lemma THRESHOLD-REDUCTION (NEW, round 8, certified in
  `lemmas/ptbi-threshold-reduction.md`, general `m`).** Proves a genuinely
  new, general algebraic identity `c(k-1)=c(k)/(2(1-c(k)))` for every `k`,
  and uses it to show peel+halve (via Lemma DOUBLE-INSERT + the induction
  hypothesis) unconditionally closes Claim PTBI's inductive step whenever
  `p_1\ge c(m-1)\Sigma(A)`, while Lemma DOM directly closes
  `\Sigma(A)/2\le p_1<c(m-1)\Sigma(A)` with no recursion at all — jointly
  reducing Claim PTBI's inductive step to the single remaining case
  `p_1<\Sigma(A)/2`, for every `m\ge2`. A clean, reusable reduction
  (previously round 7's induction attempt only identified the peel+halve
  case, without the sharp threshold or the complementary DOM case).
- **Lemma PAIR-VALUE (NEW, round 9, certified in `lemmas/pair-value.md`,
  fully general, hypothesis-free).** If a multiset decomposes into any
  number of exactly-tied pairs (of any values, in any relative position to
  each other and to the rest — no domination, no contiguity required)
  plus an unpaired remainder, `oddrank` equals the sum of the pair values
  plus `oddrank` of the remainder, unconditionally. Proved by a one-line
  induction (remove one adjacent tied pair at a time; the even
  rank-shift this induces preserves parity for everything else). Strictly
  generalizes both Lemma DOUBLE-INSERT (`k=1`) and Lemma BLOCK-RECURSE
  (`k` pairs restricted to the domination/contiguity case) — shows
  contiguity was never actually needed for the pairing-value identity.
  Its SUBSET-DOM corollary extends "split one piece to match a subset of
  the others" from sorted-prefix subsets (BLOCK-RECURSE) to **arbitrary**
  subsets with no extra hypothesis, closing the round-9 `m=5` falsifying
  witness (`A=(12,6,5,4,2)/29`, budget `4`: exact value `1/2<c(4)=16/31`,
  via matching `p_2` to `\{p_4,p_5\}`, skipping `p_3`) via a genuinely
  non-prefix match. The general theorem that some donor/subset choice
  always closes Case C for every `m` (which would need Hall's marriage
  theorem for simultaneous multi-donor matching) remains open — this
  lemma supplies the tool, not yet the general existence proof.

## Round 9 plan: two targets, a quick win and the real general-`m` obstruction

The round-9 `math-explorer-ptbi.md` scouting report **concretely falsified**
the existing certified menu (BLOCK-RECURSE + DOUBLE-INSERT + TAIL-SNIP,
applied at any recursion depth) at the exact witness
`A=(12,6,5,4,2)/29`, `m=5`, budget `4`: the menu's best achievable value is
`15/29`, but the true optimum is `1/2 < c(4)=16/31`, achieved by a
construction BLOCK-RECURSE cannot express (splitting `p_2` to match
`\{p_4,p_5\}` exactly, **skipping** the larger `p_3` — a non-prefix,
arbitrary-subset match). This is real gap-widening: treat it as the
sharp new obstruction statement, not the old vaguer "peel+halve might not
suffice" diagnosis.

**Target 1 (quick win): finish `m=3`'s residual Case C region.**
The region `p_1<\Sigma/2, p_3>\Sigma/7` is, per the explorer's 20,000-trial
+ fine-grid probe, closed by the *existing* certified menu
(`\min(\text{TAIL-SNIP}, \text{BLOCK-RECURSE }j=1)`) with zero violations
found — this is a bounded 2-parameter piecewise-affine optimization, not a
new construction. Skeleton: set up
`\min(\text{TAIL-SNIP}(A), \text{BLOCK-RECURSE}_{j=1}(A))` as an explicit
function of `(p_1,p_3)` (with `p_2=\Sigma-p_1-p_3`), fold in the `n=1`
sub-case boundary `p_2/p_1 \gtrless 2/3` (HALVE's hypothesis), and verify
by direct algebra (not just numerics) that the minimum of the two
candidates is `\ge c(2)\Sigma` on the whole region `p_1<\Sigma/2\wedge
p_3>\Sigma/7`. This should fully close `m=3` for every configuration.

**Target 2 (the real obstruction): Lemma SUBSET-DOM via Hall's theorem.**
Generalize Lemma BLOCK-RECURSE from matching a *prefix* `t_1,\ldots,t_j`
of the sorted tail to matching an **arbitrary subset** `T` of already-
present (untouched or already-recursed) values, cost `|T|` marks
(`|T|-1$ at the `r=0` boundary, per Lemma DOM-boundary-slack).
Skeleton:
1. State the target identity: for a piece `p_i` split into fragments
   reproducing an arbitrary subset `T` of the other pieces' current
   values (not necessarily a sorted prefix), `oddrank(\text{final}) =
   \Sigma(T) + oddrank(\text{leftover after recursing on the rest})` —
   BLOCK-RECURSE's proof needed the duplicated block to occupy a
   *contiguous* rank interval, which followed for free from `T` being a
   sorted prefix (`\max(W)\le t_j$); for general `T` this must be
   re-derived or the identity may fail (the `m=5` witness's own leftover
   `\{p_1,p_3\}` is **not** dominated by `\min(T)=p_5`, so contiguity is
   not automatic — this is the crux technical risk, honestly flagged, not
   yet resolved by any prior round).
2. Use **Hall's marriage theorem** (already in `knowledge_base.md`) to show
   a valid, budget-respecting assignment (which piece's fragments match
   which target subset) always *exists* whenever needed, viewing "pieces
   needing fragments" and "target values to reproduce" as the two sides of
   a bipartite matching — this is the mechanism to prove *existence* of a
   good move, not yet attempted by any live approach.
3. Re-derive the rank-occupancy claim for non-contiguous `T` directly (most
   likely via re-sorting the *full* final multiset and tracking parity of
   rank-runs, generalizing BLOCK-RECURSE's Steps 3–4 rather than assuming
   them) — this is the load-bearing new content; if it fails in general,
   report the failure honestly and narrow the claim (e.g. to `T` sets with
   at most one element strictly between two touched pieces) rather than
   asserting an unproved general identity.
4. Apply the resulting Lemma SUBSET-DOM to close Case C for `m=5` on the
   witness above first (as a concrete checkpoint matching the explorer's
   exact numbers), then attempt the general-`m` induction.

**Do not re-attempt**: potential-function/smoothing arguments for Case C
(structurally ruled out, `majorization-smoothing`'s non-concavity
obstruction); a static single-rule menu applied however deeply recursively
(now concretely falsified at `m=5`, not merely conjectured insufficient).

## Round 9: `m=3` Case C fully closed; Lemma PAIR-VALUE (SUBSET-DOM without contiguity)

### Target 1 — `m=3`'s residual Case C region: FULLY CLOSED

**Claim.** For `m=3`, every sorted `A=(p_1\ge p_2\ge p_3>0)`,
`\Sigma(A)=1`, with `p_1<1/2` (Case C), Xiang Yu can achieve
`oddrank(B)\le c(2)=4/7` using `\min(\text{TAIL-SNIP}(A),
\text{BLOCK-RECURSE}_{j=1}(A))`, with **no further hypothesis needed**
(the previously-open region was `p_1<1/2\wedge p_3>1/7`; the argument below
in fact closes all of `p_1<1/2`, a strictly larger region, subsuming the
already-closed `p_3\le1/7` sub-case too).

**Step 0 (both candidates are unconditionally available throughout Case
C).** TAIL-SNIP needs no hypothesis (`m=3` odd, certified). BLOCK-RECURSE
`j=1` needs `p_1\ge S_1=p_2$ (always true, sorted) and `r:=p_1-p_2<t_1=p_2`,
i.e. `p_1<2p_2`. The round-8 write-up already proved this is **automatic**
throughout Case C for `m=3`: if `p_1\ge2p_2` held, sortedness would force
`p_1\ge2\Sigma/(m+1)=\Sigma/2`, contradicting `p_1<\Sigma/2`. So both
candidates apply unconditionally on all of Case C.

**Step 1 (exact closed form for BLOCK-RECURSE `j=1`, corrected).** With
`r=p_1-p_2`, BLOCK-RECURSE `j=1` gives (Lemma BLOCK-RECURSE,
`S_1=p_2`, `L_0=\{r,p_3\}$ — **not** `\{p_2,r\}`, the round-8 labelling
error corrected above):
```
\text{BLOCK-RECURSE}_1(A) = p_2 + oddrank(L_0), \qquad L_0=\{r,p_3\}.
```
Throughout Case C (`p_1<1/2$, `\Sigma=1`), `r<p_3$ always: `r<p_3
\iff p_1-p_2<p_3 \iff p_1<p_2+p_3=1-p_1 \iff p_1<1/2`, exactly the Case C
hypothesis. So in `L_0`, `p_3$ is the larger element, `r$ the smaller, and
the certified `n=1` closed form (`universal-adversary-strategy.md`,
"`n=1` case") gives
```
oddrank(L_0) = \min\!\big(p_3,\; p_3/2+r\big)
```
(the two `n=1` sub-cases, "do nothing" vs. "halve the max", combine into
this single `\min` since the sub-case boundary `p_3=2r` is exactly where
the two formulas agree — direct check: at `p_3=2r`, both give `p_3`).
Substituting `r=p_1-p_2`:
```
\text{BLOCK-RECURSE}_1(A) =
\begin{cases}
p_2+p_3 = 1-p_1, & \text{if } p_3\le 2(p_1-p_2) \quad(\text{Sub-case B1}),\\[2pt]
p_1+p_3/2, & \text{if } p_3 > 2(p_1-p_2) \quad(\text{Sub-case B2}).
\end{cases}
```
**In Sub-case B2, BLOCK-RECURSE `j=1` equals TAIL-SNIP exactly**
(`p_1+p_3/2$ both), not merely coincidentally on isolated examples (as the
corrected round-8 example above illustrates) — it is this exact algebraic
identity. So
```
\min(\text{TAIL-SNIP},\text{BLOCK-RECURSE}_1)(A) =
\begin{cases}
\min(p_1+p_3/2,\ 1-p_1), & \text{Sub-case B1 } (p_3\le2(p_1-p_2)),\\
p_1+p_3/2, & \text{Sub-case B2 } (p_3>2(p_1-p_2)).
\end{cases}
```

**Step 2 (Sub-case B2: `p_1+p_3/2\le4/7` throughout).** Rewrite Sub-case
B2's condition using `p_2=1-p_1-p_3$: `p_3>2(p_1-p_2)=2(2p_1-1+p_3)
\iff p_1<(2-p_3)/4$. Two ranges of `p_3`:
- If `p_3\le2/7`: since `p_1<(2-p_3)/4`, `p_1+p_3/2 < (2-p_3)/4+p_3/2 =
  (2+p_3)/4 \le (2+2/7)/4 = 4/7`. Strict, so `<4/7` throughout.
- If `p_3>2/7`: sortedness (`p_2\ge p_3$) forces `p_1\le1-2p_3`, so
  `p_1+p_3/2 \le 1-2p_3+p_3/2 = 1-3p_3/2 < 1-3/7 = 4/7$ (strict, since
  `p_3>2/7`).

So `p_1+p_3/2<4/7` strictly throughout Sub-case B2 (the value `4/7$ is a
supremum, approached but not attained inside B2, consistent with B2 being
an open condition).

**Step 3 (Sub-case B1: `1-p_1\le4/7` throughout, i.e. `p_1\ge3/7`).**
Sub-case B1's condition is `p_1\ge(2-p_3)/4` (complement of B2). Two ranges
of `p_3` again:
- If `p_3\le2/7`: `(2-p_3)/4\ge(2-2/7)/4=3/7`, so `p_1\ge(2-p_3)/4\ge3/7`
  directly, giving `1-p_1\le4/7`.
- If `p_3>2/7`: sortedness forces `p_1\le1-2p_3<1-4/7=3/7`. Combined with
  B1's requirement `p_1\ge(2-p_3)/4`, and `(2-p_3)/4>1-2p_3$ exactly when
  `p_3>2/7$ (direct algebra: `2-p_3>4-8p_3\iff7p_3>2`), Sub-case B1's
  region (`p_1\ge(2-p_3)/4`) and the sortedness bound (`p_1\le1-2p_3`) are
  then **mutually exclusive** — Sub-case B1 is **empty** whenever
  `p_3>2/7`, so this range contributes nothing to check.

So `1-p_1\le4/7` throughout the (nonempty part of) Sub-case B1.

**Conclusion.** Combining Steps 2–3: `\min(\text{TAIL-SNIP},
\text{BLOCK-RECURSE}_1)(A)\le4/7` throughout **all** of Case C
(`p_1<1/2`), with equality approached (and, at the single boundary point
below, attained exactly) as `p_1\to3/7,\ p_2,p_3\to2/7`. **This fully
closes `m=3`'s previously-open region — indeed the entirety of Case C —
completing the general upper bound for `m=3` (`n=2`) unconditionally over
every configuration `A`.**

**Extremal check.** At `(p_1,p_2,p_3)=(3/7,2/7,2/7)$ (`p_1<1/2$ ✓, boundary
of both B1/B2): TAIL-SNIP `=3/7+1/7=4/7` exactly; BLOCK-RECURSE `j=1`
(`r=p_1-p_2=1/7$, `p_3=2/7=2r$, exact B1/B2 boundary) `=1-p_1=4/7` exactly
too. Both candidates equal `c(2)=4/7$ exactly at this point — matching
tightness, as expected for the extremal geometric-type configuration.

**Independent numerical verification.** Exact-`Fraction` random search,
`200{,}000` trials over `p_1<1/2` (uniform random sorted triples,
denominators up to `10^5`), zero violations of
`\min(\text{TAIL-SNIP},\text{BLOCK-RECURSE}_1)\le4/7`; maximum value found
`\approx0.571276`, approaching but never exceeding `4/7\approx0.571429`,
consistent with the proved supremum. The extremal point's exact equality
(`4/7=4/7=4/7`) independently re-verified by direct substitution.

**`m=3` general upper bound: now `solved` in full**, combining: `p_1\ge1/2`
(Cases A/B of Lemma THRESHOLD-REDUCTION, closed round 8) and `p_1<1/2`
(Case C, closed this round) — **every** sorted 3-piece configuration is
now covered, unconditionally, no gaps remaining for `m=3`.

### Target 2 — Lemma PAIR-VALUE: SUBSET-DOM without a contiguity hypothesis

**The falsifying witness (re-verified).** `A=(12,6,5,4,2)/29`, `m=5`,
budget `4`, target `c(4)=16/31\approx0.5161`. Confirmed exactly: the
existing certified menu (BLOCK-RECURSE + DOUBLE-INSERT + TAIL-SNIP, any
recursion depth) tops out at `15/29\approx0.5172>c(4)` on this witness
(re-derived independently this round), while the true optimum is
`1/2<c(4)`, achieved by splitting `p_2$ to exactly match `\{p_4,p_5\}`
(**skipping** `p_3`) — a non-prefix, arbitrary-subset match that Lemma
BLOCK-RECURSE cannot express (its hypothesis requires matching a *prefix*
`t_1,\ldots,t_j` of the sorted tail).

**New lemma, fully proved: Lemma PAIR-VALUE** (`lemmas/pair-value.md`).
*Statement:* if a multiset `B` decomposes into `k` **tied pairs**
`\{v_1,v_1\},\ldots,\{v_k,v_k\}$ (each pair two exactly-equal elements,
**anywhere** in `B`'s sorted order — no domination, no contiguity, no
relative-position hypothesis of any kind between the pairs or between the
pairs and the unpaired remainder `U`) plus an unpaired remainder `U`, then
**unconditionally**
```
oddrank(B) = oddrank(U) + \sum_{i=1}^k v_i.
```
*Proof (full detail in the lemma file):* induction on `k`. Two elements of
equal value are always mutually rank-adjacent in a sorted arrangement (no
differently-valued element can sit between two copies of the same value);
removing one such adjacent pair shifts every element below it down by
exactly `2` ranks (even, hence parity-preserving) and leaves every element
above it untouched, so `oddrank(B)=oddrank(B\setminus\text{pair})+v$
(exactly one of the pair's two adjacent ranks is odd, contributing `v`
regardless of which); apply the inductive hypothesis to the remaining
`k-1` pairs plus the same untouched `U`.

**Independently verified**, `40{,}000` exact-`Fraction` random trials total
(`20{,}000` with values drawn from a wide range, interleaving pairs and
unpaired elements in unpredictable relative order; `20{,}000` more from a
narrow range `\{1,\ldots,8\}` specifically to stress-test exact
coincidences between different pairs' values and between pair and unpaired
values), **zero mismatches** in every configuration tested.

**Why this resolves the round-9-flagged technical risk, rather than merely
routing around it.** The round-9 plan explicitly flagged: "BLOCK-RECURSE's
contiguity argument does NOT automatically transfer to arbitrary subsets
— this is a real technical risk... report honestly if the identity doesn't
hold for arbitrary subsets." Lemma PAIR-VALUE shows the identity **does**
hold for arbitrary subsets, because **contiguity was never actually
necessary** — Lemma BLOCK-RECURSE's domination hypothesis was sufficient
but not required, exactly analogous to how Lemma DOUBLE-INSERT showed
Lemma HALVE's domination hypothesis was never required for a *single*
pair. Lemma PAIR-VALUE is the common generalization of Lemma DOUBLE-INSERT
(`k=1`) and Lemma BLOCK-RECURSE (`k$ pairs, with the extra domination
hypothesis that happens to make them contiguous, an unnecessary special
case) — proved by the same one-line "adjacent pair, even shift" argument,
now shown to need no positional hypothesis at all.

**Corollary SUBSET-DOM** (stated in full in `lemmas/pair-value.md`):
splitting any element `p_i` to exactly reproduce an **arbitrary subset**
`T$ of the other current elements' values (not necessarily a sorted
prefix), with residual `r=p_i-\Sigma(T)\ge0`, gives
`oddrank(B)=\Sigma(T)+oddrank(U)` unconditionally, `U$ being the untouched
elements plus the residual, for **any** further recursive refinement of
`U`. This is Lemma BLOCK-RECURSE's conclusion with its contiguity
hypothesis (`r<t_j`) entirely removed.

**Closing the witness.** Apply SUBSET-DOM three times: match `p_2$ to the
non-prefix subset `\{p_4,p_5\}$ exactly (`\Sigma(T)=4/29+2/29=6/29=p_2`, so
`r=0`, costing `1` mark via the `r=0`-boundary saving, certified Lemma
DOM-boundary-slack); independently halve `p_1$ (`1` mark, a `k=1`
tied-pair instance of Lemma PAIR-VALUE, i.e. Lemma DOUBLE-INSERT) and halve
`p_3$ (`1` mark, likewise). Total `3\le4` marks. Now **every** element of
the resulting multiset is paired (`U=\emptyset`), so Lemma PAIR-VALUE
gives, exactly,
```
oddrank(B) = \frac{p_1}{2}+\frac{p_3}{2}+p_4+p_5 =
\frac{6}{29}+\frac{5}{58}+\frac{4}{29}+\frac{2}{29} = \frac{29}{58} =
\frac12.
```
Independently re-verified by direct exact-`Fraction` computation of the
full sorted `8`-element multiset
`(6/29,6/29,4/29,4/29,5/58,5/58,2/29,2/29)`: `oddrank=6/29+4/29+5/58+2/29
=29/58=1/2$, matching. Since `1/2 = 29/58 < 16/31 = c(4)$ (cross-multiply:
`29\times31=899 < 16\times58=928`), **this closes the falsifying witness**,
fixing the concrete gap the round-9 explorer found; the previous
best-menu value on this witness, `15/29\approx0.5172`, is strictly worse
than `c(4)`, and Lemma PAIR-VALUE's construction strictly beats it.

**What is and is not established.** Lemma PAIR-VALUE is a **fully general,
certified, hypothesis-free** structural fact about `oddrank`, strictly
generalizing Lemma DOUBLE-INSERT and Lemma BLOCK-RECURSE, and it
**concretely closes** the one falsifying witness that motivated this
round's Target 2. It does **not** by itself supply a general theorem that
some choice of donor element(s)/target subset(s) closes Case C (or Claim
PTBI's induction) for every `m` and every configuration — turning "some
good matching exists" into a theorem for the general induction would need
Hall's marriage theorem (`knowledge_base.md`) to handle **simultaneous,
non-conflicting multi-donor** matches (several pieces split at once,
matched to disjoint target subsets), which is a genuinely separate,
harder existence question not attempted in general this round — flagged
honestly as open, not closed. The general-`m` Case C induction (the
"main open gap" of the upper bound) remains open; what this round
establishes is (a) a strictly more powerful reusable tool
(Lemma PAIR-VALUE) than what BLOCK-RECURSE alone offered, with the
contiguity risk fully resolved rather than merely deferred, and (b) the
one concrete counterexample instance closed.

**Do not re-attempt**: assuming Lemma BLOCK-RECURSE's contiguity/
domination hypothesis is load-bearing for the pairing value identity — it
is not (Lemma PAIR-VALUE proves the identity unconditionally); any future
attempt at the general-`m` Case C induction should use Lemma PAIR-VALUE
directly (it strictly subsumes BLOCK-RECURSE, DOUBLE-INSERT, and — applied
iteratively — MULTI-HALVE) rather than re-deriving a contiguity-based
special case.

## Round 11 plan — the precise remaining sub-goal: Lemma MATCH-HALVE-EXISTS

**This is the ONLY remaining gap for the whole problem (see `current.md`):
Claim PTBI's Case C (`p_1<\Sigma(A)/2`), general `m\ge4`.** The lower bound
is fully closed and must not be re-opened. This section retargets Case C
after this round's three explorers (Hall's-marriage lens, construction
lens, alternative-framing lens) converged on a sharper, more precise
diagnosis than round 10 left it in.

### What the round-11 explorers established (read their full reports at
`/tmp/round-11/math-explorer-hall.md`, `-construction.md`, `-altframing.md`
before building)

1. **The round-10 hard witness's true optimum has now been exactly
   reconstructed**, not just numerically located. For
   `A=(1826,1563,1520,1514,765)/7188` (`m=5`, budget `4`,
   `c(4)=16/31\approx0.5161`), the true optimum
   `1199/2396\approx0.5004` is realized by the explicit 4-mark construction
   (winning allocation `(k_1,\ldots,k_5)=(1,0,1,0,2)`):
   ```
   match(p_1,p_2)  [residual r_1 = p_1-p_2 = 263/7188]
   match(p_3,p_4)  [residual r_3 = p_3-p_4 =   6/7188, left unpaired]
   match(p_5, r_1) [a cross-level Lemma PAIR-VALUE pair -- r_1 is not an
                    original piece, it only exists after the first move]
   self-halve(p_5 - r_1)  [Lemma DOUBLE-INSERT, unconditional]
   ```
   giving the exact sorted 9-element multiset (x7188)
   `1563,1563,1514,1514,263,263,251,251,6`, `oddrank=3597/7188=1199/2396`.
2. **A clean, exact counterexample proves "always match the two largest
   available values, recursively, never self-halve" is FALSE as a general
   rule** -- the naive greedy-matching cascade on the same witness gives
   `oddrank=1921/3594\approx0.5345>c(4)`, strictly above target. Self-halving
   the final residual is a *necessary*, structurally distinct move here, not
   a fallback used only when no partner exists. **Do not dispatch a builder
   on a pure-matching (no self-halve) existence theorem -- it is refuted.**
3. **A literal transplant of aimo-0063's Hall-deficient-set-deletion crux
   does not fit and should not be attempted again.** Its load-bearing
   ingredient is a fixed 0/1 compatibility graph plus a yes/no SDR question;
   Case C is a continuous exact-value subset/fragment-matching problem with
   no natural underlying bipartite graph (building one requires the split
   ratios as input, which are exactly the unknowns). Both explorers
   independently reached this same conclusion. **Do not spend a round
   building "the" Hall graph for this problem.**
4. **The closest structural analogue found in the crux corpus is
   `aimo-0292`** (peel the single largest block, solve the smaller instance,
   reattach, and use a per-block lower bound -- "each block `\ge1`" -- to
   guarantee the two covering intervals overlap with slack), not `aimo-0063`.
   This is a genuinely closer template than anything tried in rounds 7-10,
   but the adaptation is real, new work, not a copy: our tolerance is
   multiplicative (`c(m-1)\Sigma` vs. an achieved value), not the additive
   constant `2` of aimo-0292, and our moves are "split/match/self-halve", not
   "include/exclude a whole block."
5. **Round 10's Step 3 fact (`g(v)=c(m-2)\Sigma+v(1-2c(m-2))`, always
   `>c(m-1)\Sigma` at `v=0`) already proves that any construction of the
   shape "make ONE tied pair, then hand the rest to the bare `(m-2)`-strength
   induction hypothesis" is structurally insufficient -- one level of
   induction is provably not enough.** This is exactly why the correct
   `m=5` construction above needed **two simultaneous top-level pairs**
   (`p_1`-`p_2` and `p_3`-`p_4`) *before* any recursive/residual step, not
   one pair plus a bare IH call. Any new attempt must not reduce to a
   single-peel-then-bare-IH shape -- that shape is a proved dead end, not an
   unexplored one.

### Sub-goal for the next builder: Lemma MATCH-HALVE-EXISTS

> **Claim.** For every `m\ge4` and every sorted `A=(p_1\ge\cdots\ge p_m>0)`,
> `\Sigma(A)=1`, `p_1<1/2` (Case C), there is a way to spend `\le m-1` marks,
> expressible as a finite composition of (i) Lemma PAIR-VALUE matches
> (a piece, or a residual fragment created by an earlier move in the same
> construction, split to exactly tie another piece or fragment) and
> (ii) Lemma DOUBLE-INSERT self-halvings (splitting a piece or residual
> fragment into two exactly equal halves), applied in some finite sequence
> where later moves may act on fragments produced by earlier moves, such
> that the resulting multiset `B` satisfies `oddrank(B)\le c(m-1)`.

This is a precise existence statement -- not "some matching exists"
(Hall's yes/no), and not "any single named lemma applies" (the menu is
proved insufficient) -- it is "some finite-depth composition of the two
already-certified, hypothesis-free primitives (PAIR-VALUE-match,
DOUBLE-INSERT-self-halve) suffices," with the depth of composition
possibly growing with `m` (unknown -- flag this explicitly if discovered).

**Two concrete routes to try, in this order:**

**Route A (primary -- check for a direct reuse before inventing new
machinery).** `recursive-embedding-induction`'s certified
Lemma TREE-BOUND-MULTICLUSTER (`lemmas/tree-bound-multicluster.md`)
already proves, for the *lower*-bound side, a recursive-forest bound where
every top-level node is either a leaf, a "pure" 2-way split producing a
matched pair of subtrees, or an "impure" cut producing one forced residual
-- and the proof handles *arbitrarily many* such impure residuals occurring
simultaneously, at any recursion depth, all summing correctly against
`\tau_m`. **This is structurally the same recursive object as the
`match(p_1,p_2)+match(p_3,p_4)+match(p_5,r_1)+self-halve` pattern
found this round** -- pairs at one level, with residuals recursively fed
into deeper pairs/self-halves. Before writing a new existence proof from
scratch, the next builder's **first task** should be: precisely state the
upper-bound Case C existence claim as a forest/tree recursion in the same
language as TREE-BOUND-MULTICLUSTER (pieces <-> leaves, PAIR-VALUE matches
<-> pure splits, self-halves <-> a distinguished split type, residuals <->
impure cuts) and check, node by node, whether the *already-proved*
multiplier bound `\tau_m` (or its natural dual) forces
`oddrank(B)\le c(m-1)` directly, or whether the two recursions are only
superficially similar (different inequality direction, different
multiplier). **If they are genuinely the same structure, this could close
Case C by reusing already-certified machinery rather than inventing a new
proof** -- a high-value, cheap check to do first. If they are not the same
structure (a real possibility -- the lower-bound recursion bounds a
*minimum* achieved by an adversary choosing worst-case splits, while
Case C needs Xiang Yu, the *response*, to *achieve* a value, i.e. the
quantifiers may run the wrong way), report exactly where the disanalogy
breaks and fall back to Route B.

**Route B (fallback -- aimo-0292-style peel-and-reattach-with-slack,
adapted multiplicatively).** Following the round-11 Hall-lens explorer's
concrete recommendation: attempt an induction on `m` that peels **two**
elements at once (not one -- Step 3's fact rules out single-element peels)
by matching `p_1<->p_2` (Lemma PAIR-VALUE, residual `r=p_1-p_2\ge0`),
immediately **re-inserts** `r` into the size-`(m-1)` tail instance
`\{r\}\cup\{p_3,\ldots,p_m\}` (this is the aimo-0292 "reattach" step -- `r`
plays the role of the peeled-and-added-back element), and only *then*
invokes the induction hypothesis on this `(m-1)`-element instance with its
own `(m-2)`-mark budget. The open technical question, stated precisely by
the explorer and not yet answered: **does Case C's own hypotheses
(`p_1<\Sigma/2`, sortedness) supply a per-element or per-residual lower
bound analogous to aimo-0292's "every block `\ge1`", strong enough that the
reattached instance's IH bound plus the `p_2` pair-value already beats
`c(m-1)\Sigma`, avoiding the exact `g(v)` shortfall Step 3 proved for the
naive one-pair version?** Concretely: does
```
p_2 + c(m-1)( \Sigma - p_1 - p_2 + r ) = p_2 + c(m-1)(\Sigma-2p_2)
```
(matching `p_1`-`p_2`, budget `1` mark, then applying the FULL-STRENGTH
`c(m-1)` bound -- not the weaker `c(m-2)` -- to the reattached
`(m-1)`-element residual instance, since only `1` mark was spent and `m-2`
remain for an `(m-1)`-element tail) satisfy `\le c(m-1)\Sigma` for every
Case-C configuration? (Note this uses the *same-strength* IH `c(m-1)` on a
smaller instance, which is legitimate only if the reattached instance also
has `m-1` elements and `m-2` marks -- check the bookkeeping carefully; this
is exactly the aimo-0292 "reattach and recurse at only one lower index"
shape, potentially avoiding Step 3's "lose a full level" trap because the
reattached instance is `(m-1)`, not `(m-2)`, so the IH invoked is `c(m-1)`
at size `m-1` with `m-2` marks -- i.e. the *same* claim PTBI being proved,
one size down, not a weaker `c(m-2)` version.) If this algebraic check
fails on the round-10/11 witness (`A=(1826,1563,1520,1514,765)/7188`),
report the exact numeric gap and whether a second simultaneous pair
(mirroring the `m=5` construction's `p_3`-`p_4` pair) closes it.

**Either route, report honestly** if it does not close in the time
available -- a sharper diagnosis (e.g. "same structure as TREE-BOUND but
wrong inequality direction, here is exactly where" or "the reattach
bookkeeping in Route B requires depth `d(m)` growing like `\log m`,
unproven") is valuable progress and should be recorded as `partial`, not
forced into a false `solved`.

### Round 11 outline-review correction: Route B's IH-strength claim is WRONG as stated -- do not build it without fixing this first

**Route B's central claim -- that the reattached size-`(m-1)` instance
licenses the "full-strength" bound `c(m-1)`, not the weaker `c(m-2)` -- is
false, by Claim PTBI's own statement.** Claim PTBI says: for a list of size
`k`, using `\le k-1` marks, achieve `oddrank\le c(k-1)\Sigma`. The
reattached tail `\{r\}\cup\{p_3,\ldots,p_m\}` has size `m-1` (one element
`r$ plus `m-2` original tail elements). Applying Claim PTBI to *this*
instance (as an instance of size `m-1`, which is all the IH entitles you to
do) gives target `c((m-1)-1)=c(m-2)$, **not** `c(m-1)` -- exactly the
"weaker" bound Route B's write-up explicitly (and incorrectly) says it
avoids. There is no way to extract `c(m-1)` from a *size*-`(m-1)` instance
under Claim PTBI as proved; the index is determined by size alone, not by
how many marks happen to remain.

**Numerically confirmed this is not a bookkeeping nitpick -- it is exactly
Round 10's g(v) dead end, reproduced on the same witness.** Re-running
Route B's check with the *correct* IH bound `c(m-2)` (instead of the
claimed `c(m-1)`) on the round-10/11 hard witness
`A=(1826,1563,1520,1514,765)/7188` (`m=5`, so `c(m-2)=c(3)=8/15`,
`c(m-1)=c(4)=16/31`):
```
p_2 + c(3)(\Sigma-2p_2) = 18647/35940 \approx 0.51884 > c(4) = 16/31 \approx 0.51613.
```
**Fails**, by a margin (`\approx0.0027`) of the same size and sign as Round
10's Step 3 `g(v)` shortfall. (For reference, Route B's *literally-stated*
but erroneous `c(m-1)`-version gives `37815/74276\approx0.50911 < c(4)`,
which is why the write-up looked promising -- that pass used the wrong,
too-strong IH.) This is precisely Round 10's already-proven-insufficient
"one pair/peel, then bare `(m-2)`-strength IH" shape in different clothing
(match `p_1$-`p_2$ instead of halving `p_1`), and it fails for the same
structural reason: one top-level pairing before invoking the IH is not
enough, matching the round-11 explorer's own reconstruction of the true
`m=5` optimum, which needed **two** simultaneous top-level pairs
(`p_1$-`p_2$ *and* `p_3$-`p_4$) before any residual/self-halve step, not
one.

**Recommendation to the next builder: do not spend time on Route B as
literally written.** Either (a) treat this as confirming Route B is a dead
end unless generalized to match `\ge2` simultaneous top-level pairs before
invoking the IH (a strictly harder claim, not yet formulated precisely --
if attempted, state and check it against this same witness before writing
a full proof), or (b) prioritize Route A (the TREE-BOUND-MULTICLUSTER reuse
check), which does not have this error. This correction does not change
Case C's status (`unsolved`/open); it narrows which route is worth
building.

## Round 11 build: Route A ruled out (structural, not just numeric), generalized 2-pair Route B refuted by an exact witness, and a sharpened diagnosis

**Target this round:** the two routes left open by the round-11 outline
review. Route A (cheap reuse check of `recursive-embedding-induction`'s
certified Lemma TREE-BOUND-MULTICLUSTER, `lemmas/tree-bound-multicluster.md`)
first, then either Route B properly generalized to `\ge2` simultaneous
top-level pairs, or a fresh construction guided by the round-11 explorer's
exact `m=5` witness reconstruction. **Result: Route A does not transfer (a
structural, not merely numerical, mismatch — argued rigorously below); the
natural generalization of Route B to exactly two simultaneous top-level
pairs is also refuted, by an exact `Fraction` counterexample family valid
for essentially every `m\ge4`. Case C for general `m\ge4` is still open;
this round's contribution is two ruled-out routes plus a precise diagnosis
of what any working construction must do differently.**

### Route A: TREE-BOUND-MULTICLUSTER's mechanism does NOT transfer — full argument

Read `lemmas/tree-bound-multicluster.md` in full (already cited by the
outliner). Its statement: for the **fixed geometric configuration** with
anchor values `\tau_l=2^{m-l}` (i.e. exact powers of `2`), and for **every**
way Xiang Yu can build a forest response (any distribution of "impure cuts"
— splits that tie some other anchor value `\tau_j` in the configuration,
producing a companion residual — and "pure splits" — exact halvings), the
merged leaf multiset satisfies `D(B)\ge\tau_m` **unconditionally over the
response**. This is a **universal-over-responses** lower bound for **one
fixed, highly special `A`** (the geometric `A_n`), used on the lower-bound
side of the problem (`A_n` forces Liu Bang at least `c(n)`).

What Case C needs is the opposite shape in **every respect that matters**:

1. **Quantifier direction is reversed.** Case C needs: for **every**
   (arbitrary, non-geometric) `A` with `p_1<\Sigma(A)/2`, **there exists** a
   response `B` (built from `\le m-1` marks) with `oddrank(B)\le
   c(m-1)\Sigma(A)`. TREE-BOUND-MULTICLUSTER proves a **for-all-responses**
   statement about **one** `A`; Case C needs an **exists-a-response**
   statement about **every** `A`. These are not dual restatements of the
   same fact — one is a universal lower bound on the minimum (over `B`) for
   a single point of `A`-space, the other is a pointwise upper bound on the
   minimum (over `B`) for every point of `A`-space. Literally invoking
   TREE-BOUND-MULTICLUSTER's conclusion for the upper bound would say
   "no match/self-halve response can beat `\tau_m` against `A_n`" — if
   anything this is evidence **against** the hope that match/self-halve
   constructions are powerful (on `A_n` they are proved to be exactly as
   good as `\tau_m`, no better), not evidence that they suffice to reach
   `c(m-1)\Sigma` on a *general* `A`.

2. **The forced discrete "anchor spectrum" has no analogue in Case C.**
   TREE-BOUND-MULTICLUSTER's entire proof mechanism (Reduction R1: an
   impurity at depth `j=2` is literally indistinguishable from a pure
   split; Reduction R2: pairwise cancellation of impurities tied at the
   *same integer depth* `j`, via Fact PAIR-CANCEL; the Step-2 telescoping
   bound on sorted companion values `c_l=\tau_1-\tau_{j_l}`) is built
   entirely on the fact that in `A_n`, every reachable value is **exactly**
   one of finitely many anchors `\tau_1>\cdots>\tau_m`, so "which anchor did
   this cut tie" is a well-defined **integer** (`j\in\{1,\ldots,m\}`), and
   two impurities either land at the *same* integer depth (enabling
   R2's exact cancellation) or *different* integer depths (enabling the
   telescoping sum `\tau_1-\tau_j=\tau_2+\cdots+\tau_j`). In Case C, `A` is
   an **arbitrary** sorted list of positive reals with no anchor structure
   at all: a match in the `MATCH-HALVE-EXISTS` sense ties an arbitrary real
   value (another piece, or an earlier residual) — there is no discrete
   "depth" for two matches to coincide at, so Reduction R1 (vacuous — there
   is no distinguished `j=2` anchor to collapse into a pure split) and
   Reduction R2 (vacuous — "tied at the same depth" has no meaning without
   the anchor lattice) simply do not exist as available moves; the
   telescoping identity in Step 2 also has no analogue (it uses the
   *specific* numerical relation `\tau_1-\tau_j=\tau_2+\cdots+\tau_j`, valid
   only because every `\tau_l` is exactly half its predecessor — false for
   generic reals). **Concretely verified**: I attempted to write Case C's
   existence claim in the forest language exactly as the outliner asked
   (pieces ↔ leaves, PAIR-VALUE matches ↔ pure splits, self-halves ↔ a
   distinguished split type, residuals ↔ impure cuts) and found that the
   very first structural fact the lower-bound proof leans on — a fixed,
   finite, totally-ordered anchor set that every cut necessarily lands on
   — has no counterpart: residual values in Case C (e.g. `r_1=p_1-p_2` in
   the round-11 explorer's `m=5` reconstruction) are generic reals with no
   reason to coincide with any other piece or anchor, so the "R1/R2 collapse
   the impurity count down to a small distinct-depth set" step, which is
   the actual technical engine of the multi-cluster generalization, is not
   available.

**Conclusion (Route A): the resemblance flagged by the outliner is real
at the level of *move vocabulary* (both sides use "tie an existing value"
and "split into two equal halves" as their two primitive moves) but not at
the level of the *mechanism that makes the bound provable* (discrete
anchor lattice, forced-parity telescoping, and — most importantly — the
opposite quantifier direction). Route A does not close Case C, and no
partial transfer was found beyond the shared vocabulary. This is a
structural, not merely a failed-numerical-check, conclusion, so Route A
should not be revisited without a genuinely new bridging idea (e.g., some
way of discretizing a *general* configuration's values into an anchor-like
lattice before applying the machinery — not attempted, and not obviously
possible since Case C configurations are arbitrary reals by hypothesis).**

### Generalized Route B (exactly two simultaneous top-level pairs): also refuted, by an exact witness

Per the outline-review's correction, the *only* legitimate way to salvage
Route B is to generalize from one top-level match to **two** simultaneous
top-level matches before invoking the IH, so that the index bookkeeping is
honest. Concretely: match `p_1\leftrightarrow p_2` (residual
`r_1=p_1-p_2`) and, independently, `p_3\leftrightarrow p_4` (residual
`r_3=p_3-p_4`), reattach both residuals into the tail
`T''=\{r_1,r_3,p_5,\ldots,p_m\}` (size `m-2`), and apply the **already-legal**
strong-induction hypothesis at size `m-2` with its own budget `m-3` marks
(`\text{Claim PTBI at }k=m-2` licenses exactly `c(m-3)`, honestly, no
overclaiming): this gives, using `2` marks for the two matches and `\le m-3`
more for the tail,
```
oddrank(B) = p_2+p_4+oddrank(T'') \le p_2+p_4+c(m-3)\bigl(\Sigma(A)-2p_2-2p_4\bigr),
```
using exactly `2+(m-3)=m-1` marks total (the full budget), no index abuse.

**This is algebraically correct bookkeeping** (verified directly against
the round-10/11 hard witness
`A=(1826,1563,1520,1514,765)/7188`, `m=5`: exact-`Fraction` computation
gives `p_2+p_4+c(2)\bigl(\Sigma-2p_2-2p_4\bigr) = 1281397/2510676` after
simplification `\approx 0.51028 < c(4)=16/31\approx0.51613` — **it works on
this witness**, with margin `\approx0.0059`, though it does not reach the
true optimum `1199/2396\approx0.50042` found by the round-11 explorer,
since it uses a bare IH bound on the tail rather than the exact
match/self-halve construction).

**But it is not a universal construction — refuted by an explicit family of
counterexamples, valid for every `m` tested (`m=4,\ldots,100`).** Writing
`f(x,y):=x+y+c(m-3)(1-2x-2y)` (with `\Sigma=1`, `x=p_2,y=p_4`) and using
that `c(k)` is **strictly decreasing** in `k` (verified exactly:
`c(0)=1>c(1)=2/3>c(2)=4/7>\cdots\to1/2`, so in particular `c(m-3)>1/2`
always), `f` is **strictly decreasing** in `x+y` (coefficient
`1-2c(m-3)<0`), so the construction is hardest to satisfy exactly when
`p_2+p_4` is **smallest** relative to the configuration — i.e. when the tail
is close to **uniform** (all of `p_2,\ldots,p_m` nearly equal, so matching
adjacent pairs like `p_3\leftrightarrow p_4` costs a mark for an
almost-zero residual, wasting budget) rather than sharply decreasing.
Concretely, for `p_1=0.499` (Case C: `p_1<1/2`) and
`p_2=\cdots=p_m=(1-p_1)/(m-1)` (uniform tail), exact `Fraction` computation
gives:

| `m` | `c(m-1)\Sigma` (target) | `f` (2-pair route) | margin (target − f) |
|---|---|---|---|
| 4 | `0.53333` | `0.55533` | **−0.02200** (violated) |
| 5 | `0.51613` | `0.53564` | **−0.01951** (violated) |
| 6 | `0.50794` | `0.51997` | **−0.01204** (violated) |
| 8 | `0.50196` | `0.50566` | **−0.00370** (violated) |
| 10 | `0.50049` | `0.50152` | **−0.00104** (violated) |
| 20 | `0.5000005` | `0.5000017` | **−0.0000012** (violated) |

(all values exact `Fraction` arithmetic, script `/tmp/route_b2_check.py`;
the violation persists, shrinking but staying strictly negative, at every
`m` tested up to `100`). **This is a genuine, exact algebraic refutation,
not a numerical artifact**: the sign of the margin is forced by the
`f`-is-decreasing-in-`(x+y)` argument above together with `p_2+p_4\to0`
relative to `\Sigma` as the tail becomes uniform and `m` grows, while
`c(m-3)-c(m-1)` shrinks only like `2^{-m}$ — slower in the relevant regime
(checked directly, not just asymptotically) than `p_2+p_4` can be driven
down, so the fixed-two-pair construction is provably insufficient on this
family for every `m` tested.

**Important honesty check: this witness is not itself a new hard case for
Case C** — it is very close to Lemma DOM's boundary (`p_1=0.499`,
`S=\Sigma-p_1=0.501$, so `p_1<S` only barely), and directly checking (same
script) shows the **already-certified Lemma PARTIAL-DOM / BLOCK-RECURSE**
(matching *as much of the tail as the budget and the near-`S=p_1$ slack
allow*, not a fixed two pairs) closes it easily — a differential-evolution
/ Nelder-Mead search over all mark-allocations (`/tmp/true_opt_check2.py`)
finds the true optimum is `\approx1/2$ (comfortably under target),
achieved by spending nearly the **entire** budget subdividing `p_1` alone
(a many-way, non-half split of `p_1` that closely duplicates/matches the
tail's near-uniform value) — **not** by matching two fixed pairs. So this
witness kills the *specific fixed-shape* "exactly two top-level pairs"
construction as a **universal** template, without showing Case C itself is
harder here; it shows the correct move is an **adaptive-length** chain
(PARTIAL-DOM/BLOCK-RECURSE with a variable, config-dependent number of
matched elements) rather than a hard-coded count of `2`.

### Sharpened diagnosis for the next round

Combining this round's two negative results with round 11's exploratory
finding (the true `m=5` optimum needs **match(p_1,p_2) + match(p_3,p_4) +
match(p_5,r_1) + self-halve(p_5-r_1)`, i.e. *two* pairs there) and this
round's uniform-tail witness (needing a **long, adaptive-length**
PARTIAL-DOM-style chain instead of any fixed pair count): **no fixed
integer number of top-level pairs (one, per Route B literal; two, per
Route B generalized) is a universal construction for Case C.** The number
and *shape* of matches a correct construction needs is genuinely
config-dependent — sometimes exactly `2` disjoint pairs plus one
self-halve (the `m=5` witness), sometimes one long variable-length
PARTIAL-DOM chain absorbing almost the whole tail (the uniform-tail
witness) — so `MATCH-HALVE-EXISTS`, if true, is an honest *existence*
statement over a config-dependent composition, not a single parametrized
family provable by one clean induction step. This rules out (with proof,
not just failed search) the two most natural "fixed template" attempts and
narrows the open question to: is there a **selection rule** (a function
from `A` to a specific finite composition of matches/self-halves,
correctly indexed for the strong induction) that always works? This
remains open. **Do not re-attempt "match exactly `k` fixed top-level pairs
for some small constant `k`" without first checking it against both the
`m=5` witness (needs 2 pairs + self-halve) and the uniform-tail family
above (needs a long adaptive chain, not a fixed small `k`) — a single fixed
`k` cannot serve both.**

### Status

Case C for general `m\ge4` remains **unsolved**. This round's genuine
contribution: Route A is ruled out with a structural (not just numeric)
argument; the natural generalization of Route B (two fixed top-level
pairs) is ruled out with an exact `Fraction` counterexample family valid
for `m=4,\ldots,100`; and the combined evidence across three now-refuted
fixed templates (bare single peel+IH, two-fixed-pair peel+IH, TREE-BOUND
transfer) plus the two known hard witnesses gives a sharper target for the
next round: a *config-adaptive* selection rule (variable match-chain length
`j(A)` plus a decision of how much budget to reserve for a terminal
self-halve), not a fixed small menu item, guided by the two contrasting
witnesses recorded above.

## Round 12 plan — Candidate 5: budget-capped TAIL-SNIP recursion (gate FIRST, proof SECOND)

### Where this picks up

Round 12's three explorers ran a genuinely stronger candidate than any
prior round and diagnosed exactly why it still narrowly fails once
(`m=8`). The diagnosis has two independently-confirmed parts, and they
disagree with each other in a way that matters — read both before
building:

1. **`math-explorer-adaptive`**: found the base 3-move menu
   (`solve12` = peel+halve `\sqcup` PARTIAL-DOM-maximal-prefix, plus a
   top-level TAIL-SNIP move only available when `|A|` is odd — call this
   whole thing **Candidate 3**) survives 3600+ random trials (`m=4..15`),
   both known hard witnesses (`m=5` witness, near-uniform-tail family up
   to `m=40`), but has an exact `differential_evolution`-found
   counterexample at `m=8`:
   `A \approx (0.2117,0.1588,0.1410,0.1319,0.1232,0.0881,0.0748,0.0705)`,
   `c(7)\Sigma\approx0.50196078$, Candidate-3 value `\approx0.5021$,
   margin `\approx-1.53\times10^{-4}$ (exact-rational-confirmed, not
   floating noise). Tentatively guessed the fix needs non-contiguous
   subset matching (SUBSET-DOM).
2. **`math-explorer-subsetmatch`**: reproduced the `m=8` witness
   independently, then **refuted** the non-contiguous-subset-matching
   guess by brute force (all `127` nonempty subsets of the 7-element
   tail as donor matches for `p_1`; the winning subset is `T=\{p_2\}`,
   i.e. exactly the ordinary contiguous PARTIAL-DOM maximal prefix
   Candidate 3 already tries — the *subset choice* was never the
   problem). The actual defect: Candidate 3's Strategy-2 (PARTIAL-DOM)
   routes its leftover `U` (here `|U|=7`, odd) through the *restricted*
   `solve12` menu (no TAIL-SNIP access), deliberately, to avoid
   re-triggering TAIL-SNIP recursively. Letting `U` recurse through the
   *full* menu (`solve_full`, including TAIL-SNIP) closes `m=8` exactly
   (`p_2 + solve_full(U) = 0.5 < 0.50196...`), **but the unrestricted
   version is genuinely non-terminating** (confirmed: 2M+ recursive
   calls / 18s+ with no termination, even with memoization added, on a
   random `m=9` instance — this is real, not a hypothetical risk). A
   **budget-capped** version — thread an integer `budget` parameter,
   decremented only when TAIL-SNIP fires inside a nested call, with
   `budget=1` at the top (i.e. "a PARTIAL-DOM leftover's own recursive
   solve gets access to at most one extra TAIL-SNIP call anywhere in its
   own sub-recursion") — terminates cleanly and **still closes `m=8`
   exactly**, plus 523 random trials `m=4..12`, both known hard
   witnesses, and the near-uniform-tail family `m=4..20`.

**Call this fix Candidate 5** (per the dispatch's naming): Candidate 3's
menu, but with Strategy 2's (PARTIAL-DOM's) leftover recursion routed
through the full menu with a `budget`-capped nested TAIL-SNIP allowance,
`budget=1` at the top level, decrementing on each nested TAIL-SNIP use,
`0` disables TAIL-SNIP for that sub-call.

### Step 1 (MANDATORY, run before any proof attempt) — adversarial stress-test gate

Per CLAUDE.md's rigor rules and this run's established practice (the
*exact* method — `scipy.optimize.differential_evolution` minimizing the
margin `target - value` directly over the simplex restricted to Case C,
`p_1<\Sigma(A)/2` — is what originally found the `m=8` counterexample
against the un-capped menu; a smaller random/witness-only sample is not
sufficient evidence, as this round's own history shows: Candidate 3
looked fully universal against 3600+ random trials and 2 hard witnesses
before the optimizer found `m=8`).

**The builder's FIRST action must be:**
1. Implement Candidate 5 exactly (menu = peel+halve, PARTIAL-DOM with
   `budget`-capped-`solve_full` leftover recursion, top-level TAIL-SNIP
   when `|A|` is odd) with exact `fractions.Fraction` arithmetic
   throughout (no floats in the final verification, floats only for the
   optimizer's own search which then gets rationalized and re-checked
   exactly, exactly as `math-explorer-adaptive` did for the `m=8` find).
2. Run `differential_evolution` (or an equivalent global optimizer —
   basin-hopping / CMA-ES are acceptable substitutes if `scipy`'s
   variant is unstable) minimizing `target(m,A) - Candidate5(A)` over
   the Case-C simplex, for **every `m` from 4 to at least 12** (the
   un-capped menu's counterexample was at `m=8`; do not stop at one `m`
   — check a spread, since prior rounds' near-misses have appeared at
   different `m` each time).
3. For any candidate near-zero-or-negative margin the optimizer reports,
   rationalize to an exact `Fraction` (small denominator, as
   `math-explorer-adaptive` did) and re-verify the sign of the margin
   exactly — never trust the optimizer's floating output as the final
   verdict.
4. Also re-run `budget=2` if `budget=1` fails the gate, before
   concluding the whole "bounded TAIL-SNIP budget" mechanism is dead —
   the explorers only tested `budget=1`; `budget=2` (or a slowly growing
   `O(\log m)` budget) is a natural fallback to test cheaply in the same
   pass, per `math-explorer-subsetmatch`'s own explicit recommendation.

### Step 2a — IF Candidate 5 (`budget=1`, or `budget=2` if needed) survives the gate

Formalize as a precise strong-induction construction and attempt the
general proof:

**Exact recursive rule** (strong induction on `m = |A|`, `A` sorted
descending, `\Sigma:=\Sigma(A)`, Case C hypothesis `p_1<\Sigma/2`):

```
solve(A, budget):
  if |A| == 1: return A[0]
  candidates = {}
  # Move 1: peel + halve top piece (Lemma DOUBLE-INSERT, unconditional)
  candidates["halve"] = p_1/2 + solve(tail(A), budget)
  # Move 2: PARTIAL-DOM maximal-prefix match (Lemma BLOCK-RECURSE /
  #         PARTIAL-DOM-RESIDUAL), leftover recurses with ONE FEWER
  #         unit of TAIL-SNIP budget than the parent call
  j* = max j with p_1 >= S_j  (S_j = prefix-sum of tail, S_0 = 0)
  r  = p_1 - S_{j*};  leftover = sort_desc(tail[j*:] + ({r} if r>0 else {}))
  candidates["partial-dom"] = S_{j*} + solve(leftover, max(budget-1, 0))
  # Move 3: TAIL-SNIP (Lemma TAIL-SNIP) -- only legal/tried when |A|
  #         is odd AND budget > 0; splits smallest element into two
  #         halves (1 mark, unconditional decrease when |A| odd),
  #         continues with budget decremented by 1
  if |A| is odd and |A| >= 3 and budget > 0:
      A' = A with a_{|A|} replaced by two copies of a_{|A|}/2
      candidates["tail-snip"] = solve(A', budget-1)
  return min(candidates.values())

solve_full(A) := solve(A, budget=1)   # top-level entry point
```

**Induction hypothesis (exact statement to prove):** for every `m\ge1`
and every sorted Case-C-or-not configuration `A` with `|A|=m`, and every
`\mathrm{budget}\in\{0,1\}` reachable in the recursion tree from a
top-level call with `budget=1`,
`solve(A,\mathrm{budget}) \le c(m-1)\Sigma(A)` whenever the number of
marks the recursion actually uses is `\le m-1` (this must be checked as
part of the induction, not assumed — verify each branch's mark count:
`halve` uses `1+(\text{marks used by tail call})`, `partial-dom` uses
`j^*+(\text{marks used by leftover call})`, `tail-snip` uses
`1+(\text{marks used by the continuation})`; each of these must telescope
to `\le m-1` total, mirroring how Lemma BLOCK-RECURSE / Lemma
THRESHOLD-REDUCTION already track budgets for the existing menu items —
do not silently assume "using the recursive value bound also respects
the mark budget," verify it explicitly since the round-11 outline-review
caught exactly this class of bug before).

**Well-foundedness (CORRECTED this round — see "Round 12 build" section
below for the full fixed proof): the measure is `(\mathrm{budget},|A|)`
lexicographic with `\mathrm{budget}` PRIMARY, not `(|A|,\mathrm{budget})`
as an earlier draft of this plan stated** (that ordering is
self-contradictory: `tail-snip` *increases* `|A|` while decreasing
`budget`, so it cannot decrease a measure with `|A|` primary). Under the
corrected order: `halve` leaves `budget` unchanged and strictly decreases
`|A|` (decreases the secondary coordinate, ties the primary — still a
lex decrease); `partial-dom` strictly decreases `|A|` (via the `j^*\ge1`
fact proved below) and never increases `budget` (ties or decreases the
primary, always decreases the secondary — a lex decrease); `tail-snip`
strictly decreases `budget` (decreases the primary coordinate outright,
regardless of what happens to `|A|`). Both coordinates are bounded below
(`\mathrm{budget}\ge0`, `|A|\ge1`), so the order is well-founded. Full
proof, including the `j^*\ge1` fact, in "Round 12 build" below.

**Key lemmas needed, with mechanism:**
- **Lemma PAIR-VALUE** (already certified, `lemmas/pair-value.md`): every
  matching-into-tied-pairs decomposition has
  `oddrank = \Sigma(\text{matched values}) + oddrank(\text{unmatched})`
  — the algebraic backbone justifying that `candidates["partial-dom"]`
  and `candidates["tail-snip"]`'s claimed values are exactly what the
  recursive formula states (not just approximately, or only on average).
- **Lemma BLOCK-RECURSE** (already certified): the PARTIAL-DOM maximal
  prefix match is legal and its leftover computation is correct for any
  tail shape, at any recursion depth — the mechanism justifying Move 2's
  well-definedness.
- **Lemma THRESHOLD-REDUCTION** (already certified): supplies the
  target `c(m-1)\Sigma(A)` this induction must beat, and its identity
  `c(k-1)=c(k)/(2(1-c(k)))` is the tool for telescoping the recursive
  bound `solve(A,\cdot)\le c(|A|-1)\Sigma(A)\Rightarrow` the parent
  call's bound, exactly as it already does for the existing menu items
  — reuse this telescoping step for the new `budget`-indexed cases too,
  do not re-derive it.
- **NEW, to be proved this round — Lemma BUDGET-SUFFICES (the load-bearing
  new claim):** `budget=1` (or whatever constant the Step-1 gate confirms)
  is *always* enough — i.e. among the finitely many configurations where
  Move 1 and Move 2 alone (the `budget=0` menu, `=` old Candidate 3 with
  TAIL-SNIP only at the very top) fail to reach `c(m-1)\Sigma`, one extra
  nested TAIL-SNIP inside the PARTIAL-DOM leftover is always sufficient
  to close the gap. **The mechanism to prove this is NOT yet known** —
  the two explorers only established it empirically (523 random trials +
  known witnesses + the specific `m=8` case); if a proof is attempted,
  the natural strategy is to isolate *why* `m=8`'s witness needed exactly
  one nested TAIL-SNIP (near-uniformity forces the leftover `U` to be
  "hard" in the same way the original `A` was, so passing one unit of
  the same fix down one level suffices) and try to turn that into an
  inductive argument bounding how many levels of near-uniformity can
  stack — this is the actual open mathematical content of Case C, not a
  bookkeeping exercise, and may require the **Hall-deficient-set-deletion
  technique from crux `aimo-0063`** (iteratively remove a Hall-violating
  donor/target set and its neighborhood, repeat, to force a terminal
  matching nonempty) to handle the *general* subset-cover / donor-matching
  step rigorously (PARTIAL-DOM's maximal-prefix match is a special case
  of a donor covering a prefix-subset of targets; a fully general proof
  that some good match+snip combination always exists may need this
  deficiency-version argument rather than the ad hoc greedy-prefix
  construction alone, per `math-explorer-altframing`'s finding — this is
  a refinement *within* the matching framing, not a new approach).

### Step 2b — IF Candidate 5 fails the gate (a new counterexample is found)

Report honestly: **CHANGES REQUESTED, not a solved gap.** Record the
exact counterexample (rationalized `Fraction`, `m`, `A`, target, value,
margin) in this file under a new "Round 12 build" section, exactly in
the style of the `m=8` counterexample above, and do **not** force a
patch without re-running the gate on the patched version. If `budget=2`
also fails, record that too and flag for the next round's outliner
whether a slowly-growing (`O(\log m)`) budget is worth testing, or
whether the whole "bounded nested TAIL-SNIP" mechanism should be
retired in favor of a fresh selection-rule idea.

### Watch out for
- Do not let the builder skip Step 1 and jump straight to a proof
  attempt "because 523 random trials + 2 hard witnesses passed" — this
  exact overconfidence is what let Candidate 3 look universal for a full
  explorer report before the optimizer found `m=8`.
- Verify the well-foundedness argument explicitly (see above) — this is
  the class of bug (an unrestricted recursive move that looks
  terminating at first glance but isn't globally well-founded) that
  `math-explorer-subsetmatch` caught this round; a builder re-deriving
  the construction from scratch could easily reintroduce it if the
  `budget` parameter is not threaded through *every* recursive call
  (including Move 1's `halve` branch, which should also propagate
  `budget` unchanged, not silently reset it to `1`).
- If Lemma BUDGET-SUFFICES turns out to need `aimo-0063`'s technique,
  remember every borrowed crux step must be reproven from scratch here
  (per CLAUDE.md) — Hall-deficient-set-deletion is a hint to adapt, not
  a citation.

## Round 12 build

### Step 0 — well-foundedness, fully proved (fixing the outline's measure bug)

**Lemma WF-C5.** Define `solve(A,\mathrm{budget})` exactly as in the
recursive rule above. Then every call sequence reachable from a
top-level call `solve\_full(A)=solve(A,1)` terminates.

**Proof.** Order pairs `(\mathrm{budget},|A|)\in\mathbb Z_{\ge0}\times
\mathbb Z_{\ge1}` lexicographically with `\mathrm{budget}` primary:
`(\mathrm{budget}',|A|') \prec (\mathrm{budget},|A|)` iff
`\mathrm{budget}'<\mathrm{budget}`, or `\mathrm{budget}'=\mathrm{budget}`
and `|A|'<|A|`. This is a well-order on `\mathbb Z_{\ge0}\times
\mathbb Z_{\ge1}` (both coordinates bounded below, standard lexicographic
product of two well-orders). It suffices to show every one of the three
recursive calls a non-base-case invocation `solve(A,\mathrm{budget})`
(`|A|\ge2`) can make has strictly smaller measure than
`(\mathrm{budget},|A|)`.

- **Move 1 (`halve`)**: recurses as `solve(\mathrm{tail}(A),
  \mathrm{budget})`. Here `\mathrm{budget}` is unchanged and
  `|\mathrm{tail}(A)|=|A|-1<|A|`. Since the primary coordinate ties, the
  measure strictly decreases by the secondary coordinate. ✓.

- **Move 2 (`partial-dom`)**: recurses as `solve(\mathrm{leftover},
  \max(\mathrm{budget}-1,0))`. The new budget is
  `\le \mathrm{budget}$ always (it is `\mathrm{budget}` or
  `\mathrm{budget}-1`), so the primary coordinate never increases.
  *Sub-claim `j^*\ge1$ (needed to guarantee `|\mathrm{leftover}|<|A|`
  even when the primary coordinate ties, i.e. when `\mathrm{budget}=0`):*
  since `A` is sorted descending with `|A|\ge2`, `S_1=p_2\le p_1$, so
  `j=1` always satisfies the defining condition `p_1\ge S_j$ of the
  maximal-prefix search; hence `j^*\ge1` unconditionally whenever
  `|A|\ge2`. Consequently `|\mathrm{leftover}| = |A|-1-j^*+
  \mathbb 1[r>0] \le |A|-1-1+1 = |A|-1<|A|` (the leftover consists of the
  `|A|-1-j^*` untouched tail elements beyond the matched prefix, plus at
  most one residual element `r`, and `j^*\ge1` removes at least one
  element net). So: if `\mathrm{budget}=0` (primary ties, both before and
  after, since `\max(-1,0)=0`), the secondary coordinate strictly
  decreases by the `j^*\ge1` fact just proved; if `\mathrm{budget}\ge1`,
  the primary coordinate strictly decreases (`\mathrm{budget}-1<
  \mathrm{budget}`) regardless of `|\mathrm{leftover}|`. Either way the
  lexicographic measure strictly decreases. ✓.

- **Move 3 (`tail-snip`)**, only reachable when `\mathrm{budget}>0`:
  recurses as `solve(A',\mathrm{budget}-1)`. The primary coordinate
  strictly decreases (`\mathrm{budget}-1<\mathrm{budget}`, and this move
  is only ever taken when `\mathrm{budget}>0`, so `\mathrm{budget}-1\ge0`
  stays in the domain); this alone makes the lexicographic measure
  strictly decrease, **regardless of the fact that `|A'|=|A|+1>|A|`** —
  this is exactly the point the outline's original `(|A|,\mathrm{budget})`
  ordering got backwards, and exactly why `\mathrm{budget}` must be
  primary. ✓.

Since every recursive call strictly decreases a well-founded measure, and
`solve` returns immediately (no recursion) whenever `|A|\le1`, every call
sequence starting from `solve\_full(A)=solve(A,1)` reaches a base case in
finitely many steps: the measure starts at `(1,|A|)` and strictly
decreases at every step, so by well-foundedness of `\prec` it cannot
decrease infinitely often. `\blacksquare`

This closes the well-foundedness gap the outline-reviewer flagged,
including the explicit `j^*\ge1` fact the reviewer identified as
load-bearing and not stated in the original plan.

### Step 1 — mandatory adversarial gate: independently re-run, PASSES cleanly

I independently re-implemented `solve`/`solve\_full` from scratch (both a
float version for the optimizer and an exact `fractions.Fraction`
version for verification — scripts at `/tmp/gate_c5_v3.py`,
`/tmp/gate_c5_v4.py`, `/tmp/near_uniform_check.py`,
`/tmp/nested_check.py`, `/tmp/half_bound_check.py`,
`/tmp/half_bound_check2.py`) and ran the mandated gate:

- **`scipy.optimize.differential_evolution`** minimizing
  `\mathrm{margin}(A):=c(m-1)\Sigma(A)-\mathrm{solve\_full}(A)` over the
  Case-C region (`p_1<\Sigma(A)/2`, enforced by a steep penalty outside
  the region so the optimizer is pushed back into Case C), for **every
  `m` from `4` to `14`** (beyond the plan's minimum of `12`), each with
  multiple random restarts (3 seeds at `m\le12`, `popsize=18`,
  `maxiter=250`; 2 seeds at `m=13,14` for tractability, `popsize=14`,
  `maxiter=150`). **Result: the best (smallest) margin found at every
  tested `m` is strictly positive** — no counterexample at any `m` from
  `4` to `14`.
- For every `m`, I **rationalized the optimizer's near-boundary floating
  point solution to exact `Fraction`s and re-verified the margin's sign
  exactly**, per the mandate (never trust the optimizer's float output as
  the final verdict): every rationalized point reproduces the float
  margin to high precision and stays strictly positive.
- **The found worst-case margins follow an exact closed form**, confirmed
  by exact `Fraction` computation: `\mathrm{margin}(m) =
  c(m-1)-\tfrac12 = \dfrac{1}{2(2^m-1)}` (derivation: `c(m-1)-\tfrac12 =
  \tfrac{2^{m-1}}{2^m-1}-\tfrac12 = \tfrac{2\cdot2^{m-1}-(2^m-1)}
  {2(2^m-1)} = \tfrac{1}{2(2^m-1)}`), matching the optimizer's numeric
  output exactly for every `m=4,\ldots,14`
  (`1/30,1/62,1/126,1/254,1/510,1/1022,1/2046,1/4094,1/8190,1/16382,
  1/32766`) — i.e. `\mathrm{solve\_full}(A)=\tfrac12\Sigma(A)` exactly at
  every found worst case, for every tested `m`.
- **Two independent structural families reproduce this exact value**
  (not merely the optimizer's numerically-converged point): (i) the
  historically-hardest **near-uniform-tail family**
  (`p_1=0.499\Sigma`, or `0.4999\Sigma`, or the boundary `\Sigma/2` case
  itself — all three tested — with the remaining `m-1` pieces exactly
  equal), verified with exact `Fraction` for `m=4,\ldots,20`:
  `\mathrm{solve\_full}(A)=\Sigma/2` exactly, in every case, matching
  `c(m-1)-1/(2(2^m-1))` exactly; (ii) an independent **nested
  near-half-split geometric chain** (`p_i=(\tfrac12-\varepsilon)
  \cdot(\tfrac12+\varepsilon)^{i-1}$, `\varepsilon=1/1000`, structurally
  unrelated to the uniform-tail family), verified for `m=4,\ldots,12`:
  identical exact margins `1/30,\ldots,1/8190`. Two structurally
  different adversarial families converging to the *same* exact value
  is strong evidence this is the genuine extremal behavior at the
  `p_1\to(\Sigma/2)^-` boundary, not an artifact of one family's
  construction.
- **A separate large random sweep**, restricted to Case C
  (`p_1<\Sigma/2`, so it does not probe near the found extremal boundary
  specifically but samples the interior broadly): `3{,}709` random
  trials, `m=2,\ldots,12`, exact `Fraction` arithmetic — **zero
  violations of `\mathrm{solve\_full}(A)\le\Sigma(A)/2`** (a strictly
  stronger, cleaner claim than beating `c(m-1)\Sigma(A)` — see Step 2
  below).
- **`budget=2` was not needed**: since `budget=1` shows no near-miss (the
  smallest margin found, `1/16382` at `m=14`, is still an exact,
  robustly-reproduced positive rational, not a numerical artifact
  trending toward zero-crossing) — per the plan's own conditional
  ("test `budget=2` if `budget=1` shows any near-miss"), the fallback
  gate is not triggered. I flag this explicitly rather than skip it
  silently: the plan's trigger condition was checked and did not fire.

**Gate verdict: PASS.** No counterexample to Candidate 5 (`budget=1`) was
found by an independent from-scratch re-implementation of the exact
method that found the `m=8` counterexample against the uncapped menu,
run over a wider `m`-range (`4`–`14`, vs. the mandated minimum of `12`)
with multiple restarts, cross-checked against two structurally
independent adversarial families out to `m=20`, and a broad random sweep.

### Step 2 — a materially sharper reformulation found, not yet proved: Lemma HALF-BOUND

The gate's own output revealed something sharper than a bare pass: **at
every tested worst case (every `m` from `4` to `14`, both structural
families out to `m=20`, and the `3{,}709`-trial random sweep), the
achieved value never merely beats `c(m-1)\Sigma(A)` — it is bounded by
the much simpler quantity `\Sigma(A)/2`, and is exactly `\Sigma(A)/2` at
every found extremal point.**

**Conjectured Lemma HALF-BOUND.** For every `m\ge2` and every sorted
`A=(p_1\ge\cdots\ge p_m)` with `p_1<\Sigma(A)/2` (Case C),
`\mathrm{solve\_full}(A) = \mathrm{solve}(A,1) \le \Sigma(A)/2`.

**Why this would fully close Lemma BUDGET-SUFFICES / Claim PTBI's Case C,
if proved.** The certified fact `c(k)>1/2` for every finite `k`
(already established in this file's Lemma HALVE discussion: `c(k) =
2^k/(2^{k+1}-1) > 1/2 \iff 2^{k+1} > 2^{k+1}-1`, always true) gives, for
`k=m-1`, `c(m-1)\Sigma(A) > \Sigma(A)/2 \ge \mathrm{solve\_full}(A)`
whenever HALF-BOUND holds — i.e. Case C would be closed with a **strict**
margin `c(m-1)\Sigma(A)-\Sigma(A)/2 = \Sigma(A)/(2(2^m-1))>0` for every
`m`, exactly matching the gate's empirically-found exact worst-case
margins above. This is a strictly stronger and structurally simpler
target than the induction hypothesis originally proposed in the "Round 12
plan" section (`solve(A,\mathrm{budget})\le c(|A|-1)\Sigma(A)`, tracked
jointly over both values of `\mathrm{budget}`): HALF-BOUND needs no
reference to `c(\cdot)` inside the induction at all, only at the very
last step.

**Proof attempt (partial, does not close).** The natural approach is
strong induction on `m` via Move 1 (`halve`) alone: `\mathrm{solve}(A,b)
\le p_1/2+\mathrm{solve}(\mathrm{tail}(A),b)`, so if the tail satisfied
`\mathrm{solve}(\mathrm{tail}(A),b)\le \Sigma(\mathrm{tail}(A))/2 =
(\Sigma(A)-p_1)/2` by the inductive hypothesis, then `\mathrm{solve}(A,b)
\le p_1/2+(\Sigma(A)-p_1)/2 = \Sigma(A)/2` immediately, with **no need
for Move 2 or Move 3 at all**. This closes the sub-case where the tail is
*itself* in "Case C" relative to its own sum, recursively at every level
(`p_i < R_i/2` for every `i=1,\ldots,m-1`, `R_i:=p_i+\cdots+p_m` the
remaining sum at step `i`) — **but this sub-case is false in general**:
I verified directly (`half_bound_check2.py`) that dropping the Case-C
hypothesis at the *top* level alone already produces violations of
`\mathrm{solve\_full}(A)\le\Sigma(A)/2$ at `m=2` (as it must — a
dominant `p_1` genuinely needs `c(1)=2/3>1/2`, not `1/2`, confirming
`1/2` is only the right target under the Case-C hypothesis, not
unconditionally) — and more importantly, **a top-level Case-C `A` can
have a tail that is itself dominant** (i.e. `p_2 > \Sigma(\mathrm{tail})
/2$, meaning `p_2` alone exceeds half the remaining `m-1` pieces): e.g.
`A=(0.45,0.40,0.06,0.05,0.04)` has `p_1=0.45<\Sigma/2=0.5` (Case C) but
`p_2=0.40>\Sigma(\mathrm{tail})/2 = 0.55/2=0.275` (tail is not Case C
relative to itself). In this regime, pure repeated Move-1 halving does
**not** telescope to exactly `\Sigma/2` (a direct computation shows a
pure Move-1 chain overshoots to `\Sigma/2 + p_m/2`, since the very last
element is returned unhalved as the base case) — the gate's own
`3{,}709`-trial sweep confirms `\mathrm{solve\_full}` still achieves
`\le\Sigma/2` in this regime too, but the mechanism must be Move 2
(`partial-dom`) or Move 3 (`tail-snip`) doing the work there, not pure
Move 1, and I was **not able to complete an inductive argument covering
this second regime within this round's time budget**. This is the
precise, honestly-reported open gap: HALF-BOUND is true on every tested
instance (thousands of exact-`Fraction` trials across two structural
families and random sampling, zero violations) and, if true, gives a
strictly cleaner closure of Case C than the original plan, but its
general proof — specifically, handling the sub-case where a non-top-level
piece in the tail is itself locally dominant relative to its own
remaining sum — is not complete.

**Did not reach**: the `aimo-0063` Hall-deficient-set-deletion technique
was read and its mechanism understood (iteratively remove a
Hall-violating donor/target set and its neighborhood, using a universal
vertex to force the terminal match nonempty) but not yet needed or
applied — the obstruction found this round (the "tail locally dominant"
sub-case of HALF-BOUND) is not obviously a matching-existence question in
the sense that technique addresses; it may still be relevant to a full
proof of HALF-BOUND's second regime, but that connection is not
established.

### Verdict for this round

**Status remains `partial`.** Genuine, verified progress: (1)
well-foundedness of Candidate 5 is now fully and rigorously proved
(Lemma WF-C5, fixing the outline's measure-order bug and stating the
`j^*\ge1` fact explicitly, as the reviewer required); (2) the mandatory
adversarial gate was independently re-run at least as thoroughly as the
method that caught the `m=8` counterexample (wider `m`-range, multiple
restarts, two independent structural families, a large random sweep) and
**passes cleanly with no counterexample found**; (3) a materially
sharper, structurally simpler sufficient condition (Lemma HALF-BOUND:
`\mathrm{solve\_full}(A)\le\Sigma(A)/2` throughout Case C) was discovered
from the gate's own extremal points, which would close Case C with a
clean, closed-form strict margin `\Sigma(A)/(2(2^m-1))` if proved — but
its general proof is **not** complete, with the precise remaining
sub-case (tail locally dominant relative to its own sum) honestly
isolated rather than papered over. **Case C for general `m\ge4` is
narrowed and sharpened but still open.**

## Round 13 build: the outline-reviewer's Move-3-budget bug is a symptom
## of a deeper mark-accounting error; the corrected accounting reopens
## Case (a), sharpening the gap to a Hall-type subset-matching existence
## question

### Step 0 — reproducing the outline-reviewer's numeric claim

I independently re-implemented `solve(A,\mathrm{budget})` exactly per the
certified Round-12 definition (`fractions.Fraction`, from scratch,
memoized) and re-ran the reviewer's own test: sample Case-(b) instances
(`\mathrm{tail}(A)` NOT Case-C for itself, i.e. `p_2\ge\Sigma(\mathrm{tail}
(A))/2`), and check whether plain Move 1 (`p_1/2+\mathrm{solve}(
\mathrm{tail}(A),1)`, the unchanged-budget recursive call, no explicit
Move 2/3 invoked at the top level) already achieves `\le\Sigma(A)/2`.
**Confirmed: 0 failures**, matching the reviewer's `1729`-sample finding
exactly.

### Step 1 — tracing *why*, and finding a deeper problem

Tracing the winning move at every recursion level on the concrete
round-12 witness `A=(0.45,0.40,0.06,0.05,0.04)` (`m=5`) and on a new,
more adversarial "hereditarily dominant tail" witness I built this round,
`A=(0.40,0.35,0.15,0.07,0.02,0.01)` (`m=6`, sum `1`; verified `p_1=0.40<
\Sigma/2=0.50$ [Case C], and **every** suffix from `p_2` down to `p_5`
is non-Case-C relative to its own remaining sum — a chain of nested Case
(b) instances, not just one level), I found `\mathrm{solve\_full}(A)=1/2`
exactly (matching HALF-BOUND), achieved by a path that chains Move 1
three times, then Move 3 (tail-snip) once, then Move 1 twice more, then
an exact Move-2 boundary tie. **Counting the total number of elementary
splits (real marks) used along this path gives `6`** (one per move in the
chain above), **but the real Xiang-Yu budget for a `6`-piece configuration
is only `m-1=5` marks.** This is not a coincidence of this witness: it is
a structural consequence of how `\mathrm{solve}(A,\mathrm{budget})` is
defined — `\mathrm{budget}` there counts only *nested Move-3 (tail-snip)
uses* (as documented: "decremented only when TAIL-SNIP fires inside a
nested call"), while Move 1 and Move 2 never decrement any counter that
tracks real marks. Move 3 itself increases `|A|` by `1` (splitting the
smallest element into two), so **every Move-3 use silently grants the
recursion one extra real mark that is never charged against the `m-1`
budget Claim PTBI's induction actually needs.**

This means: the **outline-reviewer's specific "no spare Move-3 mark" bug
for Case (b)** (flagged this round) is a real instance of a *general*
modeling defect in the Round-12 `solve(A,\mathrm{budget})` recursion, not
an isolated slip in one proposed patch — the recursion as certified in
Round 12 (Lemma WF-C5) is well-founded and terminates, but it does **not**
correctly model "Xiang Yu has exactly `|A|-1` real marks," and so its
adversarial-gate "PASS" (Round 12) and this round's outline's Case (a)
claim ("closes trivially by Move 1 + IH, no budget spent below this
level") were **both evaluated against a recursion that can be strictly
more generous to Xiang Yu than the real game.**

### Step 2 — the corrected, real-marks-respecting recursion `solve2`

I built the corrected recursion, `\mathrm{solve2}(A,\mathrm{marks})`,
where a single pool of remaining real marks is decremented by **every**
move:
```
solve2(A, marks):
  if |A| <= 1 or marks == 0: return oddrank(A)   # no more splits possible
  candidates = {}
  if marks >= 1:
      candidates["move1"] = A[0]/2 + solve2(tail(A), marks-1)
  # Move 2: matching a maximal CONTIGUOUS prefix S_j of tail(A) against A[0]
  # costs j marks if the residual r=A[0]-S_j is > 0 (j matched values plus
  # 1 residual piece = j+1 parts from A[0], needs j cuts... wait: j matched
  # + 1 residual = j+1 parts needs j cuts) -- corrected cost model below.
  j*, S_{j*}, r = (as in Lemma DOM / PARTIAL-DOM)
  cost = j* if r > 0 else j*-1        # Lemma DOM-boundary-slack
  if marks >= cost:
      candidates["move2"] = S_{j*} + solve2(leftover, marks-cost)
  if |A| odd, |A| >= 3, marks >= 1:
      candidates["move3"] = solve2(tail-snip(A), marks-1)
  return min(candidates.values())      # oddrank(A) itself if no move fits
```
(Move 2's cost: creating the `j^*` matched parts plus the residual `r>0`
from `A[0]` is `j^*` cuts producing `j^*+1` pieces; at the exact boundary
`r=0` it is `j^*-1` cuts producing exactly `j^*` pieces — both already
established, this round only makes the cost explicit and charges it
against the *same* pool other moves use, instead of a separate untracked
counter.)

**Re-running the gate with `\mathrm{marks}=|A|-1`** (the actual Xiang-Yu
budget for an `m`-piece configuration):

- **Genuinely dominant, non-Case-C `m=3` configurations correctly now
  FAIL to reach `\Sigma/2`**, as they should (HALF-BOUND was never
  claimed there): `A=(0.51,0.30,0.19)` gives
  `\mathrm{solve2}(A,2)=0.51>0.50=\Sigma/2`. Independently cross-checked
  against a **from-scratch `scipy.optimize.minimize` (Nelder–Mead)
  continuous-parametrization brute force over the literal constrained
  game** (every way to distribute exactly `k` real marks among the `m`
  pieces, free — not necessarily half — split ratios, multiple random
  restarts per composition): the true `2`-mark optimum is also `0.51`
  exactly (`0.5099999999999999` to machine precision, confirmed
  rational), and `3` marks are needed to reach `0.5` exactly — confirming
  `\mathrm{solve2}` is a faithful model here, where the old `\mathrm{solve}`
  was not (the old recursion, using an untracked extra mark via a
  tail-snip-based path, incorrectly reported `0.5` reachable with only
  `\mathrm{budget}=1`, i.e. reported a value that requires `3` real marks
  as if it needed only `2`).

- **A genuine Case-(a) instance now fails to close via "Move 1 + IH"
  alone even with correct accounting** — this is the key new finding.
  Witness: `A=(0.45,0.20,0.15,0.12,0.08)` (`m=5`, `\Sigma=1`). Top level:
  `p_1=0.45<\Sigma/2=0.5` (Case C). Tail `T=(0.20,0.15,0.12,0.08)`,
  `\Sigma(T)=0.55`, `p_2=0.20<\Sigma(T)/2=0.275` — **`T` is genuinely
  Case-C for itself, i.e. this is Case (a)**, the sub-case the round-13
  outline claims "closes trivially by Move 1 + IH, no budget spent below
  this level." Computed exactly (`\mathrm{Fraction}`):
  `\mathrm{solve2}(T,|T|-1=3) = 7/25 = 0.28`, **strictly exceeding** the
  target `\Sigma(T)/2=11/40=0.275` — i.e. `T`'s own recursive value, using
  the correct real-mark budget `3` and the *full* Move-1/2/3 menu, does
  **not** reach half its own sum. So Move 1 + (the Move-1/2/3-menu IH on
  `T`) does **not** close Case (a) in general, once marks are correctly
  counted: the "IH" being invoked is a claim about `\mathrm{solve2}(T,
  |T|-1)`, and that claim is false for this `T` under the current menu.

- **Diagnosed the exact missing move** by an independent brute-force
  search over `T=(0.20,0.15,0.12,0.08)`, `\mathrm{marks}=2`
  (fewer than the nominal budget `3`, confirming there is slack): the
  true optimum is `0.275` exactly (`scipy` Nelder–Mead, rationalized),
  achieved by splitting `p_1=0.20` (of `T`) at the **non-half** ratio
  `(0.12,0.08)` — creating an **exact tie with the tail's own existing,
  non-adjacent elements `0.12` and `0.08`** — while *independently*
  halving `p_2=0.15` into `(0.075,0.075)` (an ordinary Move-1 step). This
  is a **non-contiguous subset match**: `p_1` is tied to the *subset*
  `\{0.12,0.08\}` of `T`'s tail, skipping over `0.15` entirely, not a
  contiguous prefix. Move 2 as currently formalized (Lemma
  PARTIAL-DOM / BLOCK-RECURSE) only ever matches a **contiguous prefix**
  of the sorted tail; it has no mechanism to skip an element and match a
  non-adjacent subset. This is *exactly* the already-certified but
  existence-unproven **Lemma PAIR-VALUE**'s general subset-matching
  regime (`lemmas/pair-value.md`, hypothesis-free value identity for
  *arbitrary* tied pairs/subsets, no contiguity needed) — the file has
  had this tool since round 9 but has never established a general
  existence theorem for *which* subset match always works (the Hall's
  marriage / donor-matching question flagged as open in rounds 9, 11, 12).

### Step 3 — honest conclusion: the gap is sharper and deeper, not closed

The outline-reviewer's specific "no spare Move-3 mark" complaint about
Case (b) is **correct but is a symptom, not the disease**: the disease is
that the Round-12 `\mathrm{solve}(A,\mathrm{budget})` recursion conflates
"nested tail-snip count" with "real marks used," silently granting one
extra real mark per Move-3 use. Correcting this (via `\mathrm{solve2}`)
does two things: (1) it correctly makes genuinely-dominant/non-Case-C
configurations fail to reach `\Sigma/2` (as they must), confirming the
corrected model is sound where the old one was too generous; but (2) it
also reveals that **even Case (a) — believed to be the easy half of the
outline's case split — is not closed by the current Move-1/Move-2
(contiguous-prefix)/Move-3 menu once marks are correctly accounted for**.
The fix requires exactly the long-flagged, still-unresolved **general
subset-matching existence question** for Lemma PAIR-VALUE: given `A`
Case C, does there always exist *some* subset `U` of `\mathrm{tail}(A)`
(not necessarily a prefix) whose sum, when matched against `p_1` (or
against a recursively-arising sub-instance's own top element), together
with independent halving of the untouched remainder, achieves the target
— using no more than the available real marks? This is not answered by
anything on file; it is the same open question rounds 9/11/12 already
identified as the deepest unresolved point in this whole approach,
now shown to be unavoidable even in Case (a), with a new, concrete,
exact-`\mathrm{Fraction}`-verified witness
(`A=(0.45,0.20,0.15,0.12,0.08)`, tail `(0.20,0.15,0.12,0.08)`) that any
future subset-matching existence proof must handle. **Lemma HALF-BOUND
is not proved this round, and the round-13 outline's proposed Case
(a)/(b) split does not close Case C as planned — both the Move-3-budget
bug (Case b) and a newly-found menu-insufficiency (Case a) are real,
open obstructions.** No claim of `solved` is made; Status remains
`partial`. **Recommendation for the next round: replace the
Round-12 `solve(A,\mathrm{budget})` formalization with the corrected
`\mathrm{solve2}(A,\mathrm{marks})` accounting given above before running
any further adversarial gate or proof attempt (any conclusion drawn
from the uncorrected `solve` — including the Round-12 "gate PASS" and
this round's outline's Case-(a) claim — should be treated as unverified
until re-checked under `\mathrm{solve2}`), and focus the next attempt
squarely on the Hall-type existence question for Lemma PAIR-VALUE's
general subset match (the `aimo-0063` Hall-deficient-set-deletion
technique flagged in Round 12 remains the most promising unexplored
tool for this).**

## Round 14 build

Target this round (per the round-14 outline/outline-review): (1) rebuild
the certified recursion with correct real-mark accounting (one shared
counter, cap `m-1`, every move charged); (2) add Move 0 (skip-if-tied) as a
genuine zero-cost move, checking ties **anywhere**, not just a top prefix;
(3) attack the subset-match existence question (Lemma SLACK-COVER) via a
from-scratch induction, not an import of `aimo-0292`'s bounded-mesh
argument; (4) make explicit how the covering induction interacts with the
recursive mark budget.

### (1)+(2): corrected `solve2(A,marks)`, fully proved, with Move 0 generalized

**Fully closed this round.** Defined `solve2(A,marks)` with a single real
mark counter `marks`, initialized to `|A|-1` at the top level and charged
exactly `1` per elementary split for every move (Move 1/halve, Move 3/tail
snip, Move 2/subset-match cost `|S|` or `|S|-1` at the exact-residual
boundary), plus a genuine zero-cost **Move 0** (skip-if-already-tied)
checking for an even-multiplicity tied run **anywhere** in the sorted array
(not restricted to a top prefix, correcting exactly the scope gap the
outline-reviewer flagged in the outline's Step 3/Move-0 description).

**New certified lemma: Lemma FREE-TIE-REDUCTION**
(`lemmas/free-tie-reduction-move0.md`). Statement: if a value `v` occurs
with even multiplicity `2j` anywhere in a sorted list `A` (necessarily a
contiguous run of ranks, by sortedness), then, deleting that run to obtain
`A'`, `\mathrm{oddrank}(A) = jv+\mathrm{oddrank}(A')` **exactly, at zero
cost, regardless of the run's position** — proved from scratch by pairing
up the `2j` consecutive ranks into `j` adjacent pairs (each pair straddles
exactly one odd and one even rank, independent of the run's starting
parity) and observing the prefix/suffix blocks retain identical parity in
`A` vs. `A'` (the deleted run has even length, so the parity shift across
it is `0 \bmod 2`). This strictly generalizes the tie-insensitivity
mechanism already used inside Lemma DOM's Step 1 and Lemma DOUBLE-INSERT
(`j=1` special case) to arbitrary even multiplicity, arbitrary position —
exactly the fix the outline-reviewer required (Move 0 as stated in the
outline only checked a top-prefix block; this version checks anywhere).

**Well-foundedness.** Re-verified explicitly (not assumed) that `(marks,
|A|)` lexicographic, `marks` primary, strictly decreases on every branch:
Move 0 leaves `marks` unchanged but strictly shrinks `|A|` (by `2j\ge2`);
every other move strictly decreases `marks` (by `1$, or by `\mathrm{cost}
\ge 1` for Move 2 — the only zero-cost sub-case of Move 2, `|S|=1,
r=0`, is exactly the situation `p_1=t_1$, which is already an
even-multiplicity tie caught for free by Move 0 first, so Move 2's own
cost is genuinely `\ge1` whenever it is separately invoked). This is
exactly the `(marks,|A|)` order used by the certified Lemma WF-C5, now
re-derived to explicitly include Move 0 as the outline mandated (Step 2 of
the outline, and the outline-reviewer's re-check item).

**Numerical verification (exact `fractions.Fraction`, from scratch, script
at `/tmp/solve2.py`, reproducible).** The corrected menu (Move 0 general +
Move 1 + Move 2 over *all* subsets of the tail, at every recursion level +
Move 3), with the corrected mark accounting, reaches:
- `A=(26,21,10)/57` (`m=3`): `solve2=31/57\approx0.5439 \le c(2)=4/7
  \approx0.5714$ ✓ (and `31/57` matches the round-13-reviewer's
  independently-computed true 2-mark-constrained optimum `31/57` exactly —
  this is the first time a *proved-move-menu* value, not just a numeric
  optimizer, has reproduced that exact figure).
- `T=(0.20,0.15,0.12,00.08)` (`m=4`): `solve2=11/40=0.275=\Sigma(T)/2$
  exactly, matching the round-13-reviewer's independently-found true
  optimum exactly — via a non-contiguous subset match (`p_1=0.20` matched
  to `\{0.12,0.08\}`, skipping `0.15`) exactly as the round-13 finding
  required; this confirms the general subset-match Move 2 (not restricted
  to contiguous prefixes) is what closes this witness.
- `A=(965,965,958,482)` (`m=4$, new round-14 witness): `solve2=1685=
  \Sigma(A)/2` exactly, well under `c(3)\Sigma(A)=5392/3\approx1797.3$.
  The winning sequence: Move 0 fires immediately (`965=965` is a
  pre-existing tie), banking `965` for **zero marks**, leaving the
  sub-instance `(958,482)` with the *full* `3`-mark budget untouched; that
  sub-instance is dominant (`958\ge482`) so halving both pieces (`2` of
  the `3` marks) gives `479+241=720`, total `965+720=1685`. **This
  confirms Move 0 is genuinely load-bearing**: every prior certified move
  menu (DOM/HALVE/TAIL-SNIP/PARTIAL-DOM/PAIR-VALUE, none of which check
  for a pre-existing free tie before spending a mark) would have wasted at
  least one mark "re-creating" a tie that already existed, and — while
  this particular witness is not proven to be a genuine counterexample to
  the OLD menu without Move 0 (not separately re-checked this round for
  time reasons) — it is exactly the scenario the round-14 hall-matching
  explorer flagged as the motivating case for adding Move 0, and the
  corrected menu handles it cleanly and provably.
- The round-12 `m=8` witness
  (`A\approx(0.2117,0.1588,0.1410,0.1319,0.1232,0.0881,0.0748,0.0705)`):
  **NOT evaluated this round** — the reference `solve2` implementation
  (exhaustive subset search over all `2^{|tail|}$ subsets at every
  recursion level, memoized) did not terminate within a 5-minute budget at
  `m=8`. This is a scalability limitation of the specific brute-force
  reference program, not a mathematical finding; it is recorded honestly
  as untested, not claimed positive or negative.

### (3)+(4): Lemma SLACK-COVER — attempted from scratch, **not closed**

**Why `aimo-0292`'s mechanism does not transfer (independently re-derived,
matching the outline-reviewer's flagged disanalogy).** `aimo-0292`'s
overlap argument needs a uniform lower bound on block weight to control the
"mesh" of achievable partial sums. Here, tail elements are unconstrained
positive reals — BUT they are not *entirely* unconstrained: every tail
element `t_i` of `A`'s tail satisfies `t_i \le p_1` (since `A` is sorted
descending and `p_1` is the max). This gives a genuine, from-scratch
analogue of the needed mesh bound: **taking the tail's elements in
descending order and forming prefix sums `s_0=0 < s_1 < \cdots < s_r =
\Sigma(T)`, each gap `s_k-s_{k-1}=t_k \le t_1 \le p_1`.** Since `\Sigma(T) >
p_1` (Case C), there is a unique `k$ with `s_{k-1} \le p_1 < s_k$ (or
`s_{k-1}=p_1$ exactly, the boundary case), and the residual gap
`p_1-s_{k-1} < t_k \le p_1$ is bounded — **but only by `p_1` itself**, not
by anything relative to `\Sigma(T)` or the target margin `c(m-1)\Sigma(A) -
p_1$. This bound is exactly what the certified, contiguous-prefix version
of Move 2 (PARTIAL-DOM) already uses (Lemma DOM-boundary-slack); it is
**not** new content, and it does **not**, by itself, control whether the
resulting merged value plus the recursively-solved leftover's value meets
`c(m-1)\Sigma(A)$ — that requires tracking the *recursive* value of the
leftover, not just the size of one residual gap. **This is exactly the
"mesh bound alone is not the missing ingredient" finding the round-13
witness already demonstrated**: on `T=(0.20,0.15,0.12,0.08)`, the
*contiguous* prefix match (`k=1`, matching `p_1=0.20$ to `\{0.15\}`,
residual `0.05`) is well within the mesh bound above, yet it provably fails
to reach the true optimum (`28>27.5`) — the true optimum needs skipping
past `0.15` entirely to hit the non-contiguous pair `\{0.12,0.08\}$
exactly. **So the open question is not "is some affordable subset close to
`p_1`" (that is answered, trivially, by the prefix-mesh bound above) — it
is "does an affordable subset exist whose resulting recursive value, after
paying its mark cost, meets the target," which is a strictly stronger,
value-aware statement that the size-only mesh argument cannot supply.**

**Explicit interaction with the mark budget (the outline-reviewer's second
flagged gap, addressed here explicitly, not left implicit).** In `solve2`
as defined above, choosing a subset match `S` at cost `\mathrm{cost}(S)=
|S|` (or `|S|-1` if exact) commits `\mathrm{cost}(S)` marks and the
recursive call on the leftover instance receives exactly `marks -
\mathrm{cost}(S)` remaining marks — this is a **single** shared induction
parameter, not a separate secondary budget for the "which subset" question:
the induction on `k=|T|$ that Lemma SLACK-COVER would need is not a
free-standing combinatorial induction on `T` alone, but must be indexed
jointly by `(marks,|T|)` exactly as the outer `solve2` recursion already
is — i.e., **Lemma SLACK-COVER, correctly stated, is not a separate lemma
proved once and then "plugged into" the `(marks,|A|)` induction; it would
have to be proved as an *inductive step inside* that same induction**,
with the inductive hypothesis available only at strictly smaller
`(marks,|A|)`, and the existence claim would need to quantify over "some
choice of `S` such that `\mathrm{cost}(S) \le marks` AND the induction
hypothesis applied to the exact leftover `(marks-\mathrm{cost}(S),
|A|-|S|-(\text{parity correction}))` yields a value meeting the target
when combined with `S`'s contribution." This is a materially different
(and harder) statement than a pure existence/covering claim on subset
sums alone — it is a statement about the *interaction* of a covering
choice with a value recursion, and no version of it was proved this
round.

**Honest status of Lemma SLACK-COVER: NOT PROVED.** No induction on `k=
|T|` closing the general existence claim was found this round. The
peel-largest-tail-element mechanism (mirroring `aimo-0292`'s "exclude
largest / include largest shifted" case split) was set up but the
"include" branch's overlap claim (that the shifted achievable range from
recursing on `T\setminus\{t_1\}$ with target `p_1-t_1` covers the gap left
by the "exclude" branch) could not be shown to hold in general once the
*value* of the recursive leftover (not just its achievable-sum coverage)
must also meet the target — this is exactly the gap identified above, not
resolved. **This is reported as the entire remaining content of the whole
problem, precisely isolated but not closed**, consistent with every prior
round's honest characterization (rounds 9, 11, 12, 13).

### Verdict

**Status: partial.** Real, certified new progress this round: (a) the
mark-accounting bug flagged in round 13 is now fully and correctly fixed
(`solve2`, well-foundedness re-proved including Move 0); (b) Move 0
(skip-if-tied) is proved in full generality (any position, not just a top
prefix) as Lemma FREE-TIE-REDUCTION, closing the outline-reviewer's scope
flag; (c) three known hard witnesses (including the new
`(965,965,958,482)`) are verified, with exact-fraction computation, to meet
the target under the corrected menu; (d) the interaction between the
subset-match existence question and the recursive mark budget is now made
fully explicit (it is a single joint induction, not two separable pieces),
addressing the outline-reviewer's second flagged gap directly rather than
leaving it implicit. Lemma SLACK-COVER (the general subset-match existence
theorem) remains **unproved** — the sole open gap for the whole problem,
now more precisely characterized: it is not a pure subset-sum covering
statement (the prefix-mesh bound already answers that trivially) but a
joint covering-plus-recursive-value statement, and no induction closing it
was found this round. The `m=8` witness was not re-tested (implementation
time-out, not a finding). No overclaiming: Status remains `partial`.

## Round 15 plan — joint-induction route for Lemma SLACK-COVER, via monotonicity-in-marks first

Per the round-15 `math-explorer-slackcover` scouting report, this is a
**revision of the same live approach**, not a new slug: the target
remains the whole problem's claim (`c(n)` determined and Claim PTBI's
adversary strategy proved optimal for every `n`), with the sole
remaining gap being Lemma SLACK-COVER inside Case C (`m\ge4`). This
round attacks that gap by a genuinely different mechanism than the three
already-refuted averaging/pigeonhole attempts (`case-c-slack-covering`,
`potential-averaging-bound`, `equalization-potential-bound`): a
**constructive joint induction**, adapted from `aimo-0292`'s
strengthen-and-widen interval-covering technique, on the `(marks,|A|)`
well-order `solve2` already uses (Lemma WF-C5).

**Restated target (Lemma SLACK-COVER, joint-covering-plus-value form).**
Sorted descending `A=(p_1,\dots,p_m)`, `m\ge4`, Case C
(`p_1<\Sigma(A)/2`), `marks=m-1`, `T=\mathrm{tail}(A)`. Show there exists
`S\subseteq T` (multiset-respecting) with cost `\mathrm{cost}(S)=|S|-
[\Sigma(S)=p_1]` such that, writing `r=p_1-\Sigma(S)\ge0` and
`\mathrm{leftover}=\mathrm{sort\_desc}((T\setminus S)\cup(\{r\}$ if
`r>0$ else `\emptyset))` (strictly smaller instance, size
`m'=(m-1-|S|)+[r>0]<m`), we have `\mathrm{cost}(S)\le marks` and
`\Sigma(S)+\mathrm{solve2}(\mathrm{leftover},marks-\mathrm{cost}(S))\le
c(m-1)\Sigma(A)`. This is the precise gap Round 14 isolated: not a pure
covering statement (the prefix-mesh bound from Round 14 already answers
existence-of-a-nearby-subset trivially) but a statement about the
*recursive value* of the leftover after paying the match's cost.

**Step 1 (gate, must be checked/proved before anything else): Lemma
MARKS-MONO — `solve2(A,k)` is non-increasing in `k`.** Every move legal
at budget `k` is legal at budget `k+1` (spending fewer than the full
budget is always an option in `solve2`'s own menu — need to confirm the
"do nothing further" fallback, `oddrank(A)` with no further moves, is
always in the candidate set regardless of `k`, so `\min` over a
weakly-larger candidate set at `k+1` can only be `\le` the value at
`k`). Prove this by induction on `|A|`, jointly with re-checking it
against every existing certified move (Move 0–3) to confirm none of them
*requires* using every mark. **If this holds**, it converts the "AND" in
the restated target above into something strictly weaker: the induction
only needs `\mathrm{solve2}(\mathrm{leftover},marks-\mathrm{cost}(S))\le
c(m'-1)\Sigma(\mathrm{leftover})`, which follows for free from the
strong IH at leftover's own natural budget `m'-1` **whenever**
`marks-\mathrm{cost}(S)\ge m'-1` — i.e. whenever there is no budget
*deficit* at the recursive call. The report's "2-mark slack at the
exact-tie boundary" observation (`r=0`: `marks-\mathrm{cost}(S)=m'+1`,
two more than needed; `r>0`: `marks-\mathrm{cost}(S)=m'-1$ exactly, no
slack) must be independently re-derived and re-verified against
`solve2`'s actual code (not just hand arithmetic) as part of this step,
and — if confirmed — named Lemma EXACT-TIE-SLACK.

**Step 2 (if Step 1 holds): scalar covering induction, aimo-0292-style.**
With Step 1 in hand, SLACK-COVER reduces to a *purely algebraic* covering
statement in `\Sigma(S)$ and `\Sigma(\mathrm{leftover})` (no recursive
value term), which can be attacked by peeling the tail's largest element
`t_1=p_2` and inducting on `|T|`, generalized ("widened," in
`aimo-0292`'s sense — this crux move is adapted here from scratch, not
cited as a proof step) to arbitrary targets `p_1'\le p_1$ simultaneously:
- **Exclude branch:** `S\subseteq T\setminus\{t_1\}`, handled by the IH
  on the smaller tail `T\setminus\{t_1\}` with the same target `p_1`.
- **Include branch:** match `t_1` and recurse on `T\setminus\{t_1\}` with
  reduced target `p_1-t_1`, using the IH at the widened target.
- The overlap condition reduces to a scalar gap check on `t_1$ (bounded
  by `t_1\le p_1`, the sorted-order bound already used by the certified
  contiguous Move 2 / Lemma DOM-boundary-slack) combined with the
  certified algebraic recursion identity `c(k-1)=c(k)/(2(1-c(k)))`
  (Lemma THRESHOLD-REDUCTION).
- **Test case, not `m=8`:** build and check this induction by hand
  against the small, already-diagnosed hard witness
  `T=(0.20,0.15,0.12,0.08)$ (`p_1=0.20`, needs the non-contiguous match
  `\{0.12,0.08\}$, skipping `0.15`) — per the round-15
  `math-explorer-termination` report, this `m=4` witness already
  contains the full structural difficulty (genuine non-contiguity) at a
  size cheap enough for exact hand/exhaustive-`2^3`-subset verification;
  do **not** spend effort getting the exhaustive-subset `solve2`
  reference to terminate at `m=8` — that witness's winning move was
  already shown (Round 12) to be an ordinary contiguous prefix match, so
  it tests nothing SLACK-COVER doesn't already get from the `m=4` witness,
  and the blow-up is a branching-factor/implementation issue, not a
  mathematical obstruction.

**Step 3 (fallback if Steps 1–2 stall): exchange/minimal-counterexample
argument**, reusing the already-certified Fact 0 uncrossing mechanism and
Lemma TIE-NECESSARY, generalized from "maximize sum-of-minima over a
fixed multiset" to "maximize sum-of-minima over a multiset with one free
residual `r=p_1-\Sigma(S)`" — a second, structurally different lever
that reuses this approach's own certified machinery rather than adapting
a fresh crux, kept in reserve.

**Explicitly out of scope for this round's build (do not re-attempt):**
non-constructive averaging/pigeonhole over the whole Case-C family
(refuted 3 times: Rounds 7–8, 11, 14) and "mesh/covering bound alone"
(refuted by the `m=4` witness, Round 14). Both remain closed dead ends;
the joint induction above is a different (constructive, value-aware)
mechanism and is not affected by those findings.

**Gaps this round must close, explicitly:** (i) Lemma MARKS-MONO
(monotonicity in `marks`) — prove or refute; (ii) Lemma EXACT-TIE-SLACK
— independently verify the 2-mark-slack arithmetic against `solve2`'s
actual code; (iii) if (i) holds, the scalar covering induction of Step 2
on the `m=4` witness, then generalized to all `m\ge4`. If (i) fails, the
restated target's "AND" cannot be decoupled and Step 2/3 must instead
attack the full joint (covering+value) statement directly — record
honestly which case obtains.

## Round 15 build

Executed the round-15 plan (Steps 1–2), against the precise pseudocode of
`solve2` as it has been described since round 14 (single real-marks pool,
candidate menu = Move 0 skip-if-tied / Move 1 halve-top / Move 2
subset-match top-vs-tail (contiguous prefix in the "contiguous-only"
sub-menu; arbitrary subset in the "full" menu) / Move 3 tail-snip, each
charged against the same `marks` counter, `min` taken over all legal
candidates). Two clarifications to the operational recursion were needed
and are recorded explicitly below (both harmless — neither changes any
previously-certified numeric value — but both are load-bearing for the
proofs that follow, so they are stated as part of the definition, not
silently assumed).

### Step 0 — two clarifications to `solve2`'s operational definition

**Clarification 1 (the "stop" candidate).** Every previous round's
pseudocode for `solve2(A,\mathrm{marks})` returns `oddrank(A)` only as a
*fallback* "if no move fits" (see the round-13 pseudocode's own comment).
For Lemma MARKS-MONO below to hold, "do nothing further, using `0` of the
remaining marks" must be an explicit, unconditional candidate in the
`min`, **whenever a move also fires** — not only when the candidate set
would otherwise be empty. I checked this is a harmless clarification, not
a silent change of any previously-reported value: re-running all
previously-certified witnesses (`(26,21,10)/57\to31/57`,
`T=(0.20,0.15,0.12,0.08)\to11/40`, `(965,965,958,482)\to1685`,
`(0.51,0.30,0.19)\to0.51`) with "stop" added as an always-present
candidate reproduces every value unchanged (Appendix script
`/tmp/check_contig2.py`, `/tmp/full_subset_solver.py`, both independently
written this round), because in every one of those cases some other move
already achieves a value `\le oddrank(A)`, so adding "stop" to the `\min`
never lowers it further. Going forward, `solve2(A,\mathrm{marks}) :=
\min\big(\{oddrank(A)\}\cup\{\text{value of every move legal at this
budget}\}\big)$ is the operative definition.

**Clarification 2 (splitting a lone remaining piece).** The base case
"`if |A|\le1`, return `oddrank(A)`" (present in every prior round's
pseudocode) incorrectly forbids splitting the sole remaining piece with a
mark. This is a genuine, previously-unnoticed bug: for a singleton
`\{v\}`, splitting it into `\{v/2,v/2\}` using `1` mark strictly decreases
`oddrank$ from `v` to `v/2` (a `2$-element list has `oddrank = a_1$ only,
so `oddrank(\{v/2,v/2\})=v/2<v`), i.e. this is a legal and often
beneficial move, not a terminal state. **Fixed**: the base case is now
"`if |A|=0` or `\mathrm{marks}=0`, return `oddrank(A)`" — `|A|=1` no
longer blocks recursion; Move 1 (halve the current top piece) is legal at
any `|A|\ge1`. This bug was caught precisely because it *broke* an early
attempt to verify MARKS-MONO/the `m=4` witness computationally (it made a
2-element sub-instance evaluate to a value strictly worse than reachable,
which is exactly the kind of error the mandated computational gate is
supposed to catch before any proof is trusted) — recorded here so no
future round reintroduces it.

Neither clarification changes the well-foundedness argument (Lemma
WF-C5/Move-0 termination, round 14): Clarification 1 adds no new
recursive calls (the "stop" candidate is a plain value, not a call);
Clarification 2 only removes a spurious early return, and Move 1 (the
only move enabled at `|A|=1`) still strictly decrements `\mathrm{marks}`
by `1`, so `(\mathrm{marks},|A|)$ lexicographic (marks primary) still
strictly decreases on every recursive call, exactly as WF-C5 requires.

### Step 1 — Lemma MARKS-MONO, PROVED IN FULL

**Statement.** For every finite list `A` of positive reals and every
integer `k\ge0`, `\mathrm{solve2}(A,k+1)\le\mathrm{solve2}(A,k)`.

**Proof.** By strong induction on the well-founded order `(k,|A|)` on
`\mathbb N\times\mathbb N$, lexicographic with `k` primary (this is a
different induction than WF-C5's own termination argument — WF-C5 shows
a *single* evaluation of `\mathrm{solve2}(A,\mathrm{marks})` terminates by
induction on the recursion's own decreasing measure; here we are proving
a *universally quantified* statement about the function's values at
*every* `(A,k)`, and we license strong induction on the auxiliary,
independently well-founded order `(k,|A|)$ of the free parameters — a
standard and valid technique, distinct from re-using WF-C5's induction
directly).

Fix `(A,k)`, and assume the **inductive hypothesis (IH)**: for every
`(A',k')` with `(k',|A'|)` lexicographically smaller than `(k,|A|)$ (i.e.
`k'<k`, or `k'=k` and `|A'|<|A|`), `\mathrm{solve2}(A',k'+1)\le
\mathrm{solve2}(A',k')`.

By Clarification 1, `\mathrm{solve2}(A,k) = \min\big(\{oddrank(A)\} \cup
\{\text{value}(\mu) : \mu\text{ a move legal at budget }k\}\big)$, where
each move `\mu$ (Move 0/1/2/3) is specified by a pair
`(\mathrm{cost}(\mu),A_\mu)` **depending only on `A`, not on the current
budget** (this is directly checkable from the menu: Move 0's target run,
Move 1's halved top, Move 2's maximal/chosen subset match and residual,
Move 3's snipped smallest element are all determined by `A`'s own sorted
values, never by how many marks remain — the budget only gates *whether*
a move is affordable, `\mathrm{cost}(\mu)\le k`, never *which* move or
*what* it produces), and `\text{value}(\mu) = c_\mu +
\mathrm{solve2}(A_\mu, k-\mathrm{cost}(\mu))$ for a fixed additive/
multiplicative constant `c_\mu` contributed by the move itself (e.g. `p_1/2`
for Move 1, `\Sigma(S)` for Move 2) that also does not depend on the
budget.

**Every move legal at budget `k$ (i.e. with `\mathrm{cost}(\mu)\le k$) is
also legal at budget `k+1$** (since `\mathrm{cost}(\mu)\le k\le k+1$), and
its recursive sub-call moves from `(A_\mu, k-\mathrm{cost}(\mu))$ at
budget `k` to `(A_\mu, k+1-\mathrm{cost}(\mu)) = (A_\mu,
(k-\mathrm{cost}(\mu))+1)$ at budget `k+1` — i.e. the **same** move, on
the **same** resulting sub-instance `A_\mu`, with its own remaining budget
bumped by exactly `1`. Two cases on `\mathrm{cost}(\mu)`:

- If `\mathrm{cost}(\mu)\ge1`: then `k-\mathrm{cost}(\mu) < k`, so the pair
  `(A_\mu, k-\mathrm{cost}(\mu))` has first coordinate strictly less than
  `k`, hence is lexicographically smaller than `(k,|A|)` regardless of
  `|A_\mu|` — the IH applies directly (with `k' = k-\mathrm{cost}(\mu) <
  k`), giving `\mathrm{solve2}(A_\mu,(k-\mathrm{cost}(\mu))+1) \le
  \mathrm{solve2}(A_\mu, k-\mathrm{cost}(\mu))`.
- If `\mathrm{cost}(\mu)=0` (only Move 0, by the well-foundedness
  discussion in the round-14 build: the one zero-cost sub-case of Move 2,
  `|S|=1,r=0`, is exactly a pre-existing tie already caught by Move 0
  first, so it is never separately invoked at cost `0`): then the
  sub-call is `(A_\mu, k)` at budget `k` and `(A_\mu, k)` at budget `k+1`
  &mdash; **but** `A_\mu \ne A` strictly (`|A_\mu|<|A|`, Move 0 removes a
  nonempty even-length run), so the pair `(k,|A_\mu|)` has the same first
  coordinate as `(k,|A|)` but a strictly smaller second coordinate, hence
  is lexicographically smaller than `(k,|A|)` — the IH applies again
  (with `A'=A_\mu`, `k'=k`), giving `\mathrm{solve2}(A_\mu,k+1) \le
  \mathrm{solve2}(A_\mu,k)`.

In both cases, `\text{value}(\mu)$ at budget `k+1` is `\le`
`\text{value}(\mu)` at budget `k` (same constant `c_\mu`, sub-call value
weakly smaller by the IH). Also, the "stop" candidate `oddrank(A)$ is
present, with the identical value `oddrank(A)`, at both budgets (it does
not depend on `k` at all).

Therefore every element of the candidate set at budget `k` has a
corresponding element in the candidate set at budget `k+1` (the same move,
or "stop") with a **weakly smaller or equal** value, so
```
\mathrm{solve2}(A,k+1) = \min(\text{candidates at }k+1) \;\le\;
\min(\text{candidates at }k) = \mathrm{solve2}(A,k).
```
This closes the inductive step, and (since `|A|=0` or `k=0` instances are
constant in `k$ — the base case, trivially non-increasing/equal — the
induction bottoms out correctly) proves the claim for all `(A,k)`. `\qed`

**Corollary (decoupling).** By Lemma MARKS-MONO, for the restated
Lemma SLACK-COVER target (a subset match `S` with cost `c\le
\mathrm{marks}` and leftover `L` of size `m'<m`), it suffices to exhibit
*any* `S` with `c\le\mathrm{marks}` and
`\Sigma(S)+c(m'-1)\Sigma(L)\le c(m-1)\Sigma(A)`, **provided**
`\mathrm{marks}-c\ge m'-1` (no budget deficit at the recursive call) —
in that case `\mathrm{solve2}(L,\mathrm{marks}-c)\le
\mathrm{solve2}(L,m'-1)\le c(m'-1)\Sigma(L)` by MARKS-MONO (more budget
than the leftover's own natural allotment can only help) composed with the
strong IH at the leftover's *natural* budget `m'-1`. This is exactly the
decoupling the round-15 plan predicted, and by the Lemma
EXACT-TIE-SLACK computation below, this "no deficit" proviso is met with
`2` marks to spare at the `r=0$ boundary and exactly met (no slack, but no
deficit either) at `r>0`, so the proviso is never violated by the
matching moves themselves — the remaining difficulty (below) is purely in
choosing `S` so the *scalar* covering inequality
`\Sigma(S)+c(m'-1)\Sigma(L)\le c(m-1)\Sigma(A)` holds, not in the budget
bookkeeping.

### Step 1(ii) — Lemma EXACT-TIE-SLACK, PROVED IN FULL (re-derived from
first principles, independent of any prior round's arithmetic)

**Statement.** Let `A=(p_1,\ldots,p_m)$ sorted descending, `m\ge2`, Case
C (`p_1<\Sigma(A)/2`), `\mathrm{marks}=m-1`, `T=\mathrm{tail}(A)`
(`|T|=m-1`). Let `S\subseteq T` (as a sub-multiset) with `\Sigma(S)\le
p_1`, `r:=p_1-\Sigma(S)$, and `L:=\mathrm{sort\_desc}\big((T\setminus
S)\cup(\{r\}$ if `r>0` else `\emptyset)\big)` (size `m' = (m-1-|S|)+[r>0]`).
Then:
- if `r>0`: `\mathrm{cost}(S)=|S|` and `\mathrm{marks}-\mathrm{cost}(S) =
  m'-1` **exactly** (no slack);
- if `r=0`: `\mathrm{cost}(S)=|S|-1` and
  `\mathrm{marks}-\mathrm{cost}(S) = m'+1$, i.e. **exactly `2` marks of
  slack** relative to `L`'s own natural budget `m'-1`.

**Proof.** Splitting `p_1` into `j` positive parts (any values, as long as
they sum to `p_1`) requires exactly `j-1` elementary cuts, since each cut
increases the piece count by exactly `1` and we start from the single
piece `p_1` — this is a general counting fact about subdivision,
independent of contiguity or of the values involved. Here we split `p_1`
into the `|S|` parts matching `S`'s elements exactly, plus (if `r>0`) one
further residual part of value `r`, i.e. `j=|S|+1` if `r>0` (giving
`\mathrm{cost}=|S|$), or `j=|S|` if `r=0` (no residual part needed, since
`\Sigma(S)=p_1` exactly; giving `\mathrm{cost}=|S|-1`). This proves the
two `\mathrm{cost}(S)` formulas directly (matching, not merely
re-deriving, the round-13/14 formula, but now justified purely by the
elementary "`j` parts needs `j-1` cuts" fact rather than by appeal to
Lemma DOM-boundary-slack's specific full-tail-domination proof, since
here `S` is an arbitrary sub-multiset, not necessarily the whole tail).

For the size/slack computation: `|L| = m' = (m-1-|S|) + [r>0]`.
- Case `r>0`: `m'=(m-1-|S|)+1=m-|S|`. Then `\mathrm{marks}-\mathrm{cost}(S)
  = (m-1)-|S| = m-1-|S|`. Compare to `L`'s natural budget `m'-1 =
  (m-|S|)-1 = m-1-|S|`. These are **equal** — exactly the claimed
  "no slack" fact.
- Case `r=0`: `m'=(m-1-|S|)+0=m-1-|S|`. Then
  `\mathrm{marks}-\mathrm{cost}(S) = (m-1)-(|S|-1) = m-|S|`. Compare to
  `L`'s natural budget `m'-1 = (m-1-|S|)-1 = m-2-|S|`. The difference is
  `(m-|S|)-(m-2-|S|) = 2` — exactly the claimed "`2`-mark slack." `\qed`

This confirms the round-15 plan's "2-mark slack at the exact-tie
boundary" observation, now derived directly from the elementary
subdivision-counting fact rather than from re-running `solve2`'s code, and
generalized to an *arbitrary* subset `S` (not only a contiguous prefix or
a full-tail match), so it applies uniformly to both the certified
contiguous menu and the still-open general subset-match question alike.

### Step 2 — the scalar covering attempt, and what it actually found

With MARKS-MONO and EXACT-TIE-SLACK in hand, the remaining content of
Lemma SLACK-COVER (for a fixed `A`, Case C, size `m$) is exactly: **does
there exist a subset match `S\subseteq T` with
`\Sigma(S)+c(m'-1)\Sigma(L)\le c(m-1)\Sigma(A)`?** I attacked this
directly for the `m=4$ family named by the outline (the
`T=(0.20,0.15,0.12,0.08)`-shaped instances, i.e. general `4`-element Case
C configurations `A=(p_1,t_1,t_2,t_3)`), first by hand (peeling `t_1`,
`aimo-0292`-style, exactly as Step 2 of the plan specifies) and then,
when the hand algebra did not close for one branch (documented below,
not hidden), by exhaustive computational cross-checking with two
independently-written, from-scratch exact-`Fraction` solvers
(`/tmp/check_contig2.py`, restricted to the **already-fully-certified**
contiguous-only menu — Move 0/1/3 plus BLOCK-RECURSE's contiguous-prefix
Move 2, no open existence question involved at all — and
`/tmp/full_subset_solver.py`, the full non-contiguous menu, for
comparison).

**The key finding: Lemma SLACK-COVER, as stated (a general non-contiguous
existence claim), is more than what is actually needed at `m=4`.** The
target that must be met is `\mathrm{solve2}(A,3)\le c(3)\Sigma(A) =
(8/15)\Sigma(A)$ — **not** the stronger, once-conjectured Lemma HALF-BOUND
target `\Sigma(A)/2`. The round-13/14 "counterexample"
(`T=(0.20,0.15,0.12,0.08)`, contiguous-only value `7/25=0.28$, exceeding
`\Sigma(T)/2=11/40=0.275`) refutes HALF-BOUND on this instance but **does
not** refute the actual target: `7/25=0.28 \le c(3)\Sigma(T) =
(8/15)(11/20) = 22/75 = 0.29\overline{3}`, confirmed exactly this round
(`7/25=21/75\le22/75`). This means the entire non-contiguous-matching
mechanism that Lemma SLACK-COVER was introduced to supply may be
**unnecessary at `m=4`** — the already-fully-certified contiguous-only
menu might already suffice for the *real* theorem, even on the instance
that was believed (rounds 13–14) to force a non-contiguous match.

**Evidence gathered this round for the `m=4` claim (strong, but NOT a
complete proof — reported honestly as such):**
1. **Exact extremal point found and verified.** A targeted adversarial
   search (`scipy.optimize.differential_evolution`, `15` random-seed
   restarts, `200`+ iterations each, `\mathrm{popsize}=30`, followed by
   Nelder–Mead local polishing to `10^{-12}` tolerance) converges, for
   `m=4`, to the configuration `A=(6,5,4,2)/17$ (a clean rational point,
   not an artifact of the search — confirmed by re-running the exact
   `Fraction` solver directly on it): Case C (`6<5+4+2=11`), contiguous-only
   `\mathrm{solve2}=9/17`, target `c(3)\Sigma=8/15`, **margin
   `=8/15-9/17=1/255>0`** — a small but strictly positive, exactly
   verified margin, not a boundary tie. (This is a genuinely new
   extremal witness, distinct from the round-13/14 witness
   `T=(0.20,0.15,0.12,0.08)`, whose own contiguous-only margin is the
   larger `22/75-21/75=1/75`.)
2. **No violation found in extensive further search.** `400` random
   Case-C `m=4$ instances (`fractions.Fraction`, random integer
   numerators/denominators, `/tmp/check_contig2.py`) plus `23`
   independent `differential_evolution` restarts across two separate
   scripts (`8` restarts in the first pass, `15` more in the focused
   re-run, different random seeds each time) followed by Nelder–Mead
   polishing found no configuration where the contiguous-only menu fails
   to meet `c(3)\Sigma(A)`; the same `400`-trial random search at `m=3,5`
   also found none (`m=3` is in any case already unconditionally closed
   in full by the certified Round 8–9 theorem, independent of this
   question). This is a solid but bounded amount of search, not an
   exhaustive check — stated precisely so it is not mistaken for more
   than it is.
3. **Hand-derived partial algebra.** I derived, for the sub-case `j^*=1`
   (i.e. `t_1\le p_1<t_1+t_2`, the case containing the extremal point
   above), the explicit strategy "match `t_1` against `p_1$ (cost `1`),
   then bound the `3`-element leftover by the **already-fully-certified**
   general `m=3` theorem (`c(2)\Sigma(\text{leftover})`, Rounds 8–9)" and
   computed its exact margin in closed form: `\text{target} -
   \text{this-strategy's value} = \tfrac{1}{105}\big(11t_1-4p_1-4t_2-4t_3\big)$,
   i.e. this *particular* single strategy meets the target **iff**
   `t_1\ge\tfrac{4}{15}\Sigma(A)`. I found this sufficient condition is
   **not implied** by sub-case `j^*=1`'s defining constraints alone (a
   limiting configuration `t_1=t_2=t_3\to c$, `p_1\to2c$ drives
   `t_1/\Sigma\to1/5<4/15`), so this one strategy is not by itself a
   universal proof — **but** `\mathrm{solve2}$ takes the `\min` over
   *all* candidate moves (not just this one), and I confirmed by direct
   computation that the specific configuration exhibiting this
   strategy's failure (`A=(1.9,1,1,1)`) is still comfortably closed by
   the full recursive minimum (`\mathrm{solve2}=2.45\le
   \mathrm{target}=2.6133\overline{3}$) via a *different* branch (plain
   Move 1 first, not the peel-`t_1$-then-bound-by-`m=3` strategy). This
   means a complete proof needs the full case tree (both `j^*=1` and
   `j^*=2$ top-level branches, each further branching into how the
   leftover 2- or 3-element instance is best handled), which was **not
   completed this round** — I traced enough of it to be confident no
   single clean sub-strategy covers every sub-case, but a full
   case-exhaustive closure remains future work.

**Crucially, this bypass does NOT generalize to arbitrary `m` — proved,
not just suspected, by an exact counterexample.** I built and exactly
verified (`fractions.Fraction`, `/tmp/check_contig2.py` vs.
`/tmp/full_subset_solver.py`, independent implementations) the following
`m=6` instance:
```
A = (14, 12, 10, 9, 8, 4),  \Sigma(A) = 57,  \text{Case C: } 14 < 43.
```
- **Contiguous-only menu** (Move 0/1/3 + BLOCK-RECURSE Move 2 — the
  already-fully-certified menu, no open existence question):
  `\mathrm{solve2}_{\mathrm{contig}}(A,5) = 29`.
- **Target:** `c(5)\Sigma(A) = \tfrac{32}{63}\cdot57 = \tfrac{608}{21}
  \approx28.952`.
- **`29 > 608/21`**: the contiguous-only menu **genuinely fails** to meet
  the target on this instance — a strict, exact violation
  (`29-608/21=1/21`), not a numerical near-miss.
- **Full (non-contiguous) subset-match menu**, independently implemented
  and run this round: `\mathrm{solve2}_{\mathrm{full}}(A,5) = 57/2 = 28.5
  \le 608/21$, margin `19/42>0` — the target **is** met, but only via a
  genuine non-contiguous subset match (verified by direct inspection of
  the winning branch: it is not reproducible by any contiguous-prefix
  choice, since the contiguous-only solver — searching the *same* move
  types minus non-contiguous Move 2 — provably cannot reach `28.5`).

**Conclusion for Step 2 (honest, not hedged).** The contiguous-only
bypass is a genuinely new, useful diagnostic tool — it shows the sole
remaining gap for the *whole* theorem is smaller than previously
characterized in one precise sense (HALF-BOUND was an unnecessarily
strong intermediate target, and dropping to the real target `c(m-1)\Sigma`
may make `m=4` (and by the same evidence, `m=5`) closeable with
**already-certified** machinery, no Hall-type existence theorem needed at
those sizes) — but it **does not eliminate Lemma SLACK-COVER's general
existence question**, which is now *proved* (not just suspected)
necessary for `m\ge6$ by the exact `A=(14,12,10,9,8,4)` counterexample
above. Since Claim PTBI must hold for **every** `m\ge4`, closing `m=4`
alone (even if completed) would not close the theorem; the general
subset-match existence question remains the sole open gap for the whole
problem. What this round adds is: (a) two new, fully proved lemmas
(MARKS-MONO, EXACT-TIE-SLACK) that correctly decouple the covering and
value parts of any future SLACK-COVER proof attempt; (b) a corrected,
harmless clarification to `solve2`'s own operational definition
(Clarifications 1–2 above), needed for MARKS-MONO to be provable and
catching a genuine latent bug (the `|A|=1` early-return); (c) a sharper,
two-sided characterization of exactly which sizes need the open existence
question (not needed, on current evidence, at `m=4,5`; proved needed at
`m=6`) — a strictly more precise map of the gap than any prior round
produced, though it is a map, not a proof.

### Verdict

**Status: partial**, unchanged. Lemma MARKS-MONO and Lemma
EXACT-TIE-SLACK are now fully proved and certified (general, not scoped
to any particular `m`). The attempted scalar covering induction (Step 2)
did **not** close Lemma SLACK-COVER, nor did it close the `m=4` case in
full generality (a genuine remaining case-tree gap, honestly reported,
not hand-waved) — but it did produce a rigorous, exact-`Fraction`-verified
finding that meaningfully re-maps the gap: the actual obstruction to
Claim PTBI is not present at `m=4,5` under the already-certified
contiguous-only menu (strong evidence, not a full proof) but is *proved*
present at `m=6` (exact counterexample). **No claim of `solved` is made
for any part of Case C.** The next round's most promising paths, in
order: (1) finish the `m=4$ case-exhaustive proof using only
already-certified machinery (the case tree is fully mapped above, just
not yet closed); (2) attack the genuine, now precisely-located `m=6`
(and presumably larger `m`) non-contiguous existence question directly,
using Lemma PAIR-VALUE plus a Hall-type argument, informed by the exact
`A=(14,12,10,9,8,4)` witness as the canonical hard test case (replacing
the `m=8` witness, which per this round's explorer was never load-bearing,
and possibly also replacing `T=(0.20,0.15,0.12,0.08)`, which this round
showed does *not* actually require non-contiguous matching for the real
theorem, only for the abandoned HALF-BOUND).


- **Lemma V3-BOUND (round 16, re-derivation of round 9's "`m=3` solved in
  full" as a clean unconditional inequality, fully proved).** For every
  sorted triple `(x\ge y\ge z>0)`, `V_3(x,y,z)\le c(2)(x+y+z)`, where
  `V_3` is the certified 3-case `m=3` theorem
  (`lemmas/ptbi-threshold-reduction.md` Cases A/B plus round 9's Case C
  closure). Proved directly from the three branches' own certified facts
  (Case A via `ptbi-threshold-reduction.md`'s own monotonicity argument
  applied at `m=3`; Case B trivial from its own defining range; Case C
  the round-9 theorem itself). Full proof in "Round 16 build" above.
  Reusable as a clean black-box bound for any future construction that
  recurses into `V_3` and only needs the loose `c(2)\sigma` bound rather
  than `V_3`'s exact case-by-case value. Recommend certifying.
- **Lemma m=4-REGION-A/REGION-B (round 16, NEW, fully proved).** For
  `A=(p_1\ge t_1\ge t_2\ge t_3>0)` in Case C (`p_1<\Sigma/2`, `\Sigma:=
  \Sigma(A)`): (a) if `t_1\ge\tfrac4{15}\Sigma`, then `\mathrm{StratA}
  := t_1+V_3(t_2,t_3,p_1-t_1) \le c(3)\Sigma`; (b) if `t_1<\tfrac4{15}
  \Sigma` and `t_1\ge(\Sigma-p_1)/2` (tail is `V_3`-Case-B, i.e. DOM, for
  itself), then `\mathrm{StratB}:=p_1/2+V_3(t_1,t_2,t_3)=p_1/2+t_1 <
  c(3)\Sigma` strictly, with uniform margin `\ge\Sigma/60`. Together these
  two facts prove `V_4(A)\le c(3)\Sigma` on the union of Region 1 and
  Region 2, an algebraically exact (not numerically-fitted) sub-region of
  `m=4` Case C, including the exact known extremal point `A=(6,4,3,2)`
  (which lies on Region 1's closed boundary `t_1=\tfrac4{15}\Sigma`).
  Full proof, including the non-trivial Step 2a (tail can never be
  `V_3`-Case-A once `t_1<\tfrac4{15}\Sigma`), in "Round 16 build" above.
  Independently spot-checked this round: `200{,}000` random Case-C
  trials restricted to Region 1 union Region 2, zero violations.
  Reusable by any future attempt to finish `m=4` Case C -- the residual
  open region (Region 3: `t_1<\tfrac4{15}\Sigma` and tail is `V_3`-Case-C
  for itself) is now the *only* remaining sub-case, precisely
  characterized rather than left as "the rest of a `\le15`-way split."
  Recommend certifying (both parts (a) and (b), each independently
  useful).

### Round 16 verdict

**Status: partial**, unchanged. The `m=4` Case C `\le15`-way case split
targeted by the round-16-v2 outline is genuinely narrowed -- two of its
regions (covering, in particular, the exact known extremal point
`A=(6,4,3,2)`) are now closed by fully rigorous, hand-checkable algebra,
independently spot-checked numerically (200,000 trials, zero violations)
-- but the residual Region 3 (`t_1<\tfrac4{15}\Sigma`, tail is
`V_3`-Case-C for itself) is honestly left open: Strategy A/B's loose
bounds are algebraically proved insufficient there, Strategy C_{ij} is
shown (via one fully worked interior example) to still meet the target
there but via a mechanism (the base triple's own `V_3`-Case-C branch, not
the simpler DOM branch) not yet turned into a closed-form general proof.
No overclaiming: `solved` is not claimed for `m=4` Case C, nor for the
whole problem. Next round's clearest path: finish Region 3 using
`\mathrm{StratC}_{23}` specifically (the empirically-winning strategy on
both the round-16 headline witness `A=(1859,931,619,611)` and the new
Region-3 interior example `A\propto(1,1,1,0.9)` worked above), tracking
its base triple `(p_1,t_1,t_2-t_3)`'s own `V_3`-regime as a further,
final case split (at most 3 more sub-cases, since the base is itself a
3-element list covered by the already-fully-certified `V_3`).

## Round 17 build: Region 3 closed in full — `m=4` Case C fully closed

**Scope.** Per the round-17 outline's GAP 1/2/3, this targets Region 3
exactly (`p_1<\Sigma/2`, `t_1<\tfrac4{15}\Sigma`, and the tail
`(t_1,t_2,t_3)` itself in `V_3`'s Case C), the one residual left open by
round 16. **Result: Region 3 is now fully, rigorously closed**, using only
`\mathrm{StratA}`, `\mathrm{StratB}`, `\mathrm{StratC}_{23}` (i.e.
`\mathrm{StratC}_{12}`, `\mathrm{StratC}_{13}` are proved dispensable, not
just empirically unnecessary — GAP 3 answered: dispensable). Combined with
`lemmas/m4-region-a-region-b.md` (Regions 1+2, round 16), **`m=4` Case C is
fully closed.** The two new certified lemmas doing the work —
`lemmas/v3-closed-form.md` and `lemmas/m4-region-c-closure.md` — are
summarized here; see those files for the complete proofs (reproduced in
full there, not abbreviated).

### The key new tool: `V_3` is exactly a min of ≤2 affine pieces on each branch

The round-16 write-up used `V_3`'s Case C form `\min(x+z/2,\,y+L_2(x-y,z))`
with `L_2` left as its own two-branch (DOM/HALVE) definition — this is what
made an exact (non-loose) bound on `\mathrm{StratB}`/`\mathrm{StratC}_{23}`
look like it needed an open-ended further case split (the round-17 outline's
framing of GAP 1/2). The actual fix (**Lemma V3-CLOSED-FORM**,
`lemmas/v3-closed-form.md`, proved in full by hand): substituting `L_2`'s
own two-branch definition into `V_3`'s Case C formula and simplifying shows
the `L_2`-dependence *cancels* — in both of `L_2`'s sub-branches, the
`y+L_2(x-y,z)` term collapses to **exactly** one of `\{y+z,\;x+z/2\}` (the
other of `V_3`'s own two terms), so
```
V_3(x,y,z) = \min(x+z/2,\;y+z)     \text{throughout Case C},
```
a clean two-affine-piece formula with *no* residual case split needed to
state it (only to prove the identity, and that proof is two lines: check
`L_2`'s DOM sub-branch gives `y+L_2=y+z` exactly, and its HALVE sub-branch
gives `y+L_2=x+z/2` exactly, matching the min's other term in each case).
The same substitution gives a matching two-piece form for Case A:
`V_3=\min(x/2+y,\,x/2+y/2+z)`. (Case B is already the raw value `x`, no
change.) This is the lemma that makes exact — not loose — closed forms for
`\mathrm{StratA}`, `\mathrm{StratB}`, `\mathrm{StratC}_{23}` tractable at
all; see `lemmas/v3-closed-form.md` for the full proof.

### `[GAP 1]` StratB's exact closed form

Region 3's own hypothesis puts the tail `(t_1,t_2,t_3)` in `V_3`'s Case C,
so by Lemma V3-CLOSED-FORM,
```
\mathrm{StratB} = \min\big(p_1/2+t_1+t_3/2,\;\; p_1/2+t_2+t_3\big)
```
**exactly** — not a loose bound. Cross-checked against the original
recursive definition over tens of thousands of exact-`Fraction` Region-3
trials, zero mismatches (script details in `lemmas/m4-region-c-closure.md`).
This closed form is **not universally `\le c(3)\Sigma`** on Region 3 — e.g.
at `A=(34/25,1,7/10,7/10)$ (scaled: `A=(136,100,70,70)`, `\Sigma=376`),
`\mathrm{StratB}=203>3008/15\approx200.53=c(3)\Sigma$, a genuine, exactly
verified violation (the outline's GAP 1 correctly anticipated this: the
loose bound "insufficient" diagnosis from round 16 survives even with the
exact formula — `\mathrm{StratB}$ alone is not universal on Region 3). This
is expected and does not block closure: Step 3 below shows `\mathrm{StratA}`
or `\mathrm{StratC}_{23}` always rescues wherever `\mathrm{StratB}` fails.

### `[GAP 2]` StratC_{23}'s exact closed form, base-regime tracked

Write `a:=p_1-t_1\ge0`, `c:=t_2-t_3\ge0`. `\mathrm{StratC}_{23}`'s base
triple `(p_1,t_1,c)` is always pre-sorted (`p_1\ge t_1\ge c`, since
`c\le t_2\le t_1`), and its own `V_3`-Case-C threshold works out to be
**exactly `a<c`** (`p_1<\sigma_C/2\iff p_1<t_1+c\iff p_1-t_1<c$). Both
regimes the round-17 explorer flagged as reachable are confirmed reachable
(witness `A=(937,457,390,142)`: `a=480>c=248`, base is Case B; witness
`A=(8,4,3,2)`: `a=4>c=1`, base is Case A — the explorer's own witness
labeling of `(8,4,3,2)` as "Case C" was rechecked this round and found to
be an error, corrected here). Exact closed forms (all via Lemma
V3-CLOSED-FORM):
```
a<c:   \mathrm{StratC}_{23} = \min(p_1+(t_2+t_3)/2,\; t_1+t_2)
a\ge c, p_1<\tfrac47\sigma_C:  \mathrm{StratC}_{23} = t_3+p_1     (base Case B)
a\ge c, p_1\ge\tfrac47\sigma_C: \mathrm{StratC}_{23} = \min(p_1/2+t_1+t_3,\;p_1/2+t_1/2+t_2)  (base Case A)
```
**Load-bearing observation:** in the `a<c` regime, `\mathrm{StratC}_{23}`'s
own formula already contains `t_1+t_2` as one of its two branches, and (Step
1 of `lemmas/m4-region-c-closure.md`) `\mathrm{StratA}=t_1+t_2` exactly
whenever `a\le c` too — so `\mathrm{StratC}_{23}\le\mathrm{StratA}$
throughout `a<c`, making `\mathrm{StratA}` provably redundant there (not
just unneeded in practice).

### `[GAP 3]` StratC_{12}/StratC_{13} are dispensable — proved, not just observed

The full case-exhaustive closure (Step 3 below) uses only `\mathrm{StratA}`,
`\mathrm{StratB}`, `\mathrm{StratC}_{23}` throughout Region 3 (and Regions
1/2 already used only `\mathrm{StratA}`/`\mathrm{StratB}`). Since the proof
never invokes `\mathrm{StratC}_{12}` or `\mathrm{StratC}_{13}`, they are
**proved dispensable on all of `m=4` Case C**, resolving GAP 3 in the
affirmative (matching the round-17 explorer's empirical finding, now backed
by a complete proof rather than a sampling argument).

### Full closure argument (summary — complete proof in `lemmas/m4-region-c-closure.md`)

1. **Lemma A-BASE-NOT-CASE-A** (new, proved in full by hand):
   `\mathrm{StratA}`'s base triple `\{t_2,t_3,a\}` is *never* in `V_3`'s
   Case A anywhere on Region 3 — a genuine two-line algebraic proof (split
   on whether `a` or `t_2` is the base's largest element; in each sub-case,
   Region 3's own `p_1<\Sigma/2` and `t_1<\tfrac4{15}\Sigma$ inequalities,
   combined with the ordering `t_1\ge t_2`, directly contradict the Case-A
   threshold). This collapses `\mathrm{StratA}`'s possible regimes from `3`
   (sort order) `\times3` (`V_3` branch) `=9` down to a clean 3-way split:
   `a\ge t_2` (base always Case C — Case B is *also* impossible there, by
   the same `a<t_2+t_3` fact used against Case A), `a\le c<t_2` (base Case
   B), and `c<a<t_2` (base Case C).
2. This gives a genuine **trichotomy** partitioning all of Region 3:
   Regime I (`a<c`), Regime `\mathrm{II_a}` (`a\ge t_2`), Regime
   `\mathrm{II_b}` (`c\le a<t_2`) — exhaustive since `c\le t_2` always.
3. On Regime I, `\mathrm{StratC}_{23}$ alone (its `a<c` closed form) already
   dominates `\mathrm{StratA}`, so only `\min(\mathrm{StratB},
   \mathrm{StratC}_{23})` needs checking. On `\mathrm{II_a}`/`\mathrm{II_b}`,
   `\mathrm{StratC}_{23}` further splits by its base's Case A/B threshold,
   giving **5 cells total** (Regime `\mathrm{II_b}`'s harmless internal
   `t_3\lessgtr a` tie inside `\mathrm{StratA}`'s own formula does not
   change which outer branch is active, so it does not add a 6th cell —
   both sub-branches were checked and give the same optimal vertex), each a
   rational polytope (Region 3's 3 defining inequalities `+` ordering `+`
   the cell's own regime conditions) on which every candidate strategy
   value is affine.
4. Each cell's worst case (`\max_{\text{cell}}\,[c(3)\Sigma-\min(\text{2–6
   affine candidates})]`) was computed as an exact linear program (auxiliary
   variable `m`, standard LP linearization of a min; optimum attained at a
   polytope vertex by the fundamental theorem of LP). All five exact
   optimal vertices were found to be `\ge0` (two are exactly `0`, attained
   only at points on Region 3's own excluded boundary `t_1=\tfrac4{15}
   \Sigma$ — one of them is the already-known extremal `A\propto(6,4,3,2)`,
   already closed with equality by Region 1; the other four are strictly
   interior to Region 3 with genuine positive slack, smallest being
   `1/15\cdot\Sigma` at the `A\propto(8,4,3,2)` all-5-tie witness). Every
   vertex was cross-checked by plugging the exact `Fraction` values back
   into the **original recursive** `\mathrm{StratA}`/`\mathrm{StratB}`/
   `\mathrm{StratC}_{23}` definitions (not just the derived affine
   formulas), confirming exact agreement.
5. Hence `\min(\mathrm{StratA},\mathrm{StratB},\mathrm{StratC}_{23})
   <c(3)\Sigma` strictly throughout the open Region 3. `\blacksquare`

### Independent numerical re-verification, this round

`>2{,}000{,}000` combined exact-`Fraction` random Region-3 trials across
several independently-written scripts (not reused between checks): **zero
violations** of `\min(\mathrm{StratA},\mathrm{StratB},\mathrm{StratC}_{23})
\le c(3)\Sigma`. A 20-restart `scipy.optimize.differential_evolution`
adversarial search directly on the true recursive functions (not the
closed-form affine pieces) found minimum slack `\approx-1.8\times10^{-15}$
(floating-point zero — no violation), converging to `A\propto(6,4,3,2)$,
consistent with the algebraic proof's own tight-boundary point. The 46,101-
trial exact-`Fraction` closed-form-vs-recursive-definition cross-check
(Step 1 of this section) found zero mismatches for all three strategies.

### Round 17 verdict

**Region 3 of `m=4` Case C: closed, in full, unconditionally.** Combined
with the round-16 closure of Regions 1+2 (`lemmas/m4-region-a-region-b.md`),
**`m=4` Case C is now fully closed** — every sorted `A=(p_1\ge t_1\ge t_2
\ge t_3>0)` with `p_1<\Sigma/2$ satisfies `V_4(A)\le c(3)\Sigma$ via the
3-strategy menu `\min(\mathrm{StratA},\mathrm{StratB},\mathrm{StratC}_{23})`
(`\mathrm{StratC}_{12}`, `\mathrm{StratC}_{13}` are proved unnecessary).
Combined with Case A/Case B of Claim PTBI at `m=4` (already closed via
`lemmas/ptbi-threshold-reduction.md`), **Claim PTBI is now fully proved for
`m=4`.** New certified lemmas this round: `lemmas/v3-closed-form.md`
(reusable `V_3` structural fact, independent of `m=4`) and
`lemmas/m4-region-c-closure.md` (the Region-3-specific closure, superseding
round 16's "open" verdict on Region 3).

**What is *not* claimed.** This does **not** close the problem in general.
`m=4` was always a fixed finite case within Claim PTBI's inductive
structure; general `m\ge5` (and in particular Lemma SLACK-COVER's proved
necessity at `m\ge6`, round 15) remains completely open, and the 5-strategy
(now 3-strategy) menu used here is `m=4`-specific — it does not obviously
generalize, since the number of `\mathrm{StratC}_{ij}`-style tie strategies
needed grows combinatorially with `m` (already flagged by the round-17
explorer's brief `m\ge5` note). `Status` for this slug is updated to
reflect `m=4` Case C's full closure but remains `partial` overall pending
general-`m` progress — see `current.md` for the reviewer's own status
determination.
