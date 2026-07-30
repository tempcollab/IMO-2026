# Proof-reviewer report — round 7, imo-2026-03

Reviewed all four round-7 builds independently: read each build report for
context, then re-derived/re-verified the actual approach and lemma files
from scratch (exact `fractions.Fraction` arithmetic in Python, no floats in
any final check), re-running or reconstructing every load-bearing numeric
claim rather than trusting the builder's self-report.

## 1. `recursive-embedding-induction` — CHANGES REQUESTED (Status: partial)

**Claims checked:**
- **Lemma PARITY-PAIR-GENERAL** (`lemmas/parity-pair-general.md`): drops the
  `c_i≥1` hypothesis from the certified Lemma PARITY-PAIR, proving `D(C)≥t_n`
  for any `c_1,...,c_n≥0` with `Σc_i` odd. Re-derived the induction
  independently (Case A/B on parity of `c_1`, using the same certified block
  formula and Lemma D-BOUND) — the proof is correct; the induction genuinely
  never needed `c_i≥1`. Independently exhaustively verified: wrote a
  from-scratch script, `n=1..6`, `c∈{0,...,4}^n`, **zero violations**
  (matches the builder's own 97,648-vector exhaustive check for `n=1..7`).
- **Lemma PARITY-PAIR-ANCHOR** (`lemmas/parity-pair-anchor.md`): closes the
  anchor-only sub-case for **every** full-budget (`b=n`) strategy, any `k`,
  any tail distribution — total piece count is always `2n+1` (odd,
  unconditional), so PARITY-PAIR-GENERAL applies directly. Verified the two
  structural facts (Fact 1: `P_1` must be split; Fact 2: `T_n` cannot be
  split anchor-exactly) and the worked `n=4` example independently:
  `D({4,4,4,4,4,4,4,2,1}) = 3 ≥ 1` ✓ (recomputed directly). The partial-budget
  gap (`M` even) is honestly and precisely flagged as open, with a correct
  counterexample showing the *abstract* parity-only statement is false in
  general (`n=2`, `c=(0,4)`: `D({1,1,1,1})=0 < 1` — independently
  reproduced), so the gap genuinely needs game-reachability tracking, not
  just a stronger abstract lemma. No overclaiming here.
- **Lemma V'-GEN, "well-separated" case**: the product-polytope
  decomposition (feasible region factors as `∏_π Q_π` since each split
  piece's own sum constraint is independent) plus per-piece LP-vertex
  reduction (reusing the already-certified Lemma V mechanism) is a
  legitimate, correctly-scoped argument — it is honestly restricted to the
  case where every free coordinate's sorted neighbors are anchors, and the
  genuinely-open cross-piece-tied case is precisely identified (not
  discovered to be false, just not yet closed) with the exact mechanism
  needed (shared multiplicity-2 block, analogous to PARITY-PAIR-GENERAL's
  Case A) named but not worked out.
- The peeling induction correctly reduces well-separated configurations to
  the anchor-only case with the same budget, so for full-budget,
  well-separated strategies, Lemma PARITY-PAIR-GEN **is** fully closed —
  this is real, not merely claimed, progress.

**Verdict:** Genuine new theorems, correctly proved, correctly scoped, no
hand-waving, two gaps stated precisely and narrowly rather than vaguely.
Status `partial` is accurate — Lemma PARITY-PAIR-GEN itself, and hence the
general lower bound, is not fully closed. **CHANGES REQUESTED** — re-dispatch
to close the two remaining gaps (partial budget; cross-piece ties).

## 2. `universal-adversary-strategy` — CHANGES REQUESTED (Status: partial)

**Claims checked, all independently verified exact:**
- **Lemma MULTI-HALVE** (`lemmas/multi-halve.md`): reproduced the witness
  `A=(0.583,0.3461,0.0709)`, `K=2` exactly — `oddrank(B)=10709/20000`,
  matching both the direct sort computation and the closed form.
- **Lemma DOUBLE-INSERT** (`lemmas/double-insert.md`): reproduced the
  unconditional identity `oddrank({v,v}∪T)=oddrank(T)+v` in 3,000 fresh
  random exact-`Fraction` trials (list sizes 0–6, arbitrary `v`) — **zero
  mismatches**, independent of the builder's own 2,000-trial check.
- **Lemma PARTIAL-DOM-RESIDUAL** (`lemmas/partial-dom-residual.md`):
  reproduced Witness 1 exactly (`A=(5798,3515,687)/10000`, `j=1`) — pre-split
  `oddrank(B)=2899/5000`, post-residual-split `oddrank(B')=10687/20000`,
  matching the claimed closed form exactly.
- **Lemma TIE-NECESSARY `dim(Q)=0` fix** (`lemmas/tie-necessary.md`): the
  new argument — at an extreme point of a polytope cell, at least one
  defining inequality (of either type) must be tight, since otherwise the
  point would be interior to a positive-dimensional region — is a standard,
  correct convex-polytope fact, correctly replacing the old, genuinely
  flawed unconditional-condition-(a) claim. The lemma's disjunctive
  statement is unaffected; only this proof branch changes.
- **Lemma PARTIAL-DOM Remark correction** (`lemmas/partial-dom.md`): the
  scope correction (`r<t_j`, not `r<U_1`) is exactly what Step 2 of the
  proof actually uses; verified algebraically against the
  PARTIAL-DOM-RESIDUAL witness, which is a genuine sub-maximal-`j` instance
  confirming the corrected scope (not the old, stricter one) is what's
  needed.
- **Task 3 stress test** (the load-bearing empirical claim this round):
  independently reproduced, via `scipy.optimize` + exact-`Fraction`
  re-verification, the "peel `p_1`, solve the tail independently for its own
  true optimum, then unconditionally halve `p_1`" construction on both
  mandated hard `m=5` witnesses:
  - `A=(4265,2536,1747,1014,438)/10000`: tail-only optimum `≈0.2974`
    (independently found by a from-scratch multi-start L-BFGS-B search,
    matching the builder's value and allocation shape exactly), full merged
    value `0.51065 < c(4)=16/31≈0.51613` — reproduced to the digit.
  - `A=(3415,3023,1664,1404,494)/10000`: tail-only optimum `≈0.3315`, full
    merged value `0.50225` — reproduced to the digit, matching the true
    global optimum on this witness.
  This genuinely refutes, **for the specific purpose of proving the upper
  bound** (not for finding the true optimum), the round-7 explorer's
  "irreducible 3-piece coordination" concern on these witnesses — a real,
  verified finding, correctly scoped (the build report is explicit that
  Witness 1's *true* optimum, `≈0.5009`, does still need coordination).

**Verdict:** Every certified claim checks out exactly; both write-up fixes
are correct; the honest open item (Claim PTBI's general induction) is
genuinely open, not glossed over. **CHANGES REQUESTED** — real progress, the
general upper-bound induction remains to be closed or replaced by a
completeness-proved case split.

## 3. `minimax-mixed-duality` — RETHINK (Status: partial → recommend
retirement/redirection)

**Numerics independently verified exact:**
- Witness 1's construction is subtler than a naive re-derivation suggests:
  a first attempt at reproducing it with `x=p_1/2` (midpoint split) gives
  `oddrank=0.53945`, which does **not** beat `c(4)`. The construction
  actually requires `p_1`'s split ratio to land in a specific narrow flat
  window (`x∈(0.40539,0.40961)` as a fraction of `p_1`); I independently
  confirmed this window is genuinely nonempty (algebraically: the two
  fragments must satisfy `p1a∈(p5,p3)` and `p1b∈(p3,p2)` simultaneously,
  giving a nonempty intersection `p1a∈(0.1729,0.1747)`) and reproduced the
  exact value `5009/10000` at a point inside it. This is a real, correctly
  reported construction, not a fluke — but it shows the claim needed more
  care to independently confirm than the build report's phrasing suggested.
- Witness 2's construction reproduced exactly (`2009/4000`).
- Lemma SANDWICH's hypothesis-check on both witnesses (fails on W1, holds
  but insufficient alone on W2, giving `5181/10000 > c(4)`) is correct.

**On the "second consecutive round with no independent leverage" question
(explicitly flagged for review):** the build report's own honest assessment
is correct and should be acted on. Every construction this approach found
this round is, by its own admission and by my independent check, an
explicit instance of `universal-adversary-strategy`'s discrete tie-search
(TIE-MIN-HALVE is a mechanical generalization of that approach's own
PARTIAL-DOM-RESIDUAL, just with the tie target widened to the global
minimum). No `A`-independent (or simply-parametrized) duality certificate
was found or is evidenced to exist — an informal Farkas/Positivstellensatz
attempt turned up nothing even for these two witnesses' local cells. This is
the second straight round (6, 7) the duality/minimax *framing itself* has
failed to produce anything beyond "more evidence for the same discrete
search."

**Verdict: RETHINK.** The approach *as set up* (seeking an LP/duality
shortcut around exact-minimizer casework) has now converged with
`universal-adversary-strategy` twice running with no independent leverage —
per CLAUDE.md's diversity rule, this should go back to the outliner: either
redirect to a genuinely different dual object (e.g. a global
Positivstellensatz-style certificate valid without case-splitting on `A`,
not yet attempted) or retire/merge this slug into `universal-adversary-
strategy` as a construction-contributor (TIE-MIN-HALVE is a legitimate,
if uncertified, addition to that approach's menu). Not treated as a failed
round — the numerics are correct and the honest self-diagnosis is exactly
right; the issue is strategic (population diversity), not correctness.

## 4. `relaxed-adversary-transfer` — RETHINK (Status: unsolved, clean dead
end)

**Claims checked, all independently verified exact:**
- **Theorem V-INF** (`V_∞(A)=1/2` for every configuration `A`): reproduced
  the "halve every piece" construction on all 5 of the file's test
  configurations (3 geometric: `A_1,A_2,A_3`; 2 non-geometric) — every case
  gives exactly `1/2`. Lemma PAIR-LB (the matching lower bound
  `oddrank(B)≥Σ(B)/2` via consecutive-pair sortedness) is a correct,
  elementary, self-contained argument — re-derived independently, no gaps.
- **The salvage attempt** ("halve `n` of `n+1` pieces, leave one whole"):
  reproduced the claimed failure on `n=1, A=(4/7,3/7)` — "halve `p_1`, leave
  `p_2`" gives `5/7`, exceeding `c(1)=2/3`, confirmed exactly.
- **The structural diagnosis** (three independent reasons the transfer fails:
  config-independence; the relaxed optimum needs `n+1` marks vs. the real
  budget of `n`; and, most importantly, `V_∞(A)` **lower**-bounds rather than
  upper-bounds `min_{B:≤n marks} oddrank(B)`, since a stronger — unlimited-
  mark — adversary can only achieve a value `≤` what a weaker, budget-limited
  adversary achieves) is logically sound: a good bound against a *strictly
  stronger* adversary carries no guarantee against a weaker one, which is
  exactly the wrong direction for this target (we need an upper bound on the
  real, budget-limited adversary's minimum).

**Verdict: RETHINK, cleanly recorded, not a failure of the round.** This is
exactly the kind of result CLAUDE.md's rigor rules ask for: a real, complete,
honestly-reported negative result (Theorem V-INF, proved both directions),
with a precise diagnosis of *why* the proof shape cannot work here, rather
than an unproven claim or a silently-abandoned attempt. The relax-the-
mark-budget mechanism is now ruled out for this problem; the slug should not
be re-attempted along this specific axis (the file itself correctly notes a
different relaxation axis — e.g. giving Xiang Yu foreknowledge, or a
continuous mixing-weight relaxation — is not ruled out by this finding, but
was not attempted and per the outline-reviewer's own scoping should not be
force-fit this round).

## Overall round-7 assessment

Genuine progress on both the lower-bound side (full-budget, well-separated
anchor-only case of the tail-refined lower bound is now completely closed —
a real narrowing, not incremental restatement) and the upper-bound side
(three new certified lemmas, two correctness fixes, and a stress test that
retires a specific "irreducible coordination" concern for two of the
hardest known witnesses). One approach (`minimax-mixed-duality`) has
converged with a sibling for two rounds running and should be redirected or
retired next round. One approach (`relaxed-adversary-transfer`) produced a
clean, complete, honestly-scoped negative result and should not be revived
along the same axis. `current.md` has been updated in full to reflect all
of the above; **Status remains `partial`** — neither the lower bound
(general `k<n`, two sub-cases open) nor the upper bound (general matching/
assignment optimality) is fully closed for arbitrary `n`.

## Outcomes recorded via `mcp__approach-ranker__record_outcome`
- `recursive-embedding-induction` — `partial`
- `universal-adversary-strategy` — `partial`
- `minimax-mixed-duality` — `dead-end` (with explicit RETHINK/retirement
  recommendation in the note)
- `relaxed-adversary-transfer` — `dead-end` (clean RETHINK, not a failed
  round)
