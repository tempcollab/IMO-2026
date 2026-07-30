## imo-2026-04 — Verification / arbitration report (resolves the round-1 conflict)

### 1. Master cut formula — independently re-derived, confirmed correct
Splitting vertex-angle `a` (other two `b`,`c`, `a+b+c=180`) at point P on the opposite side,
with `x1+x2=a`: Child1 = `(b, x1, a+c-x1)`, Child2 = `(c, a-x1, b+x1)`. Verified algebraically
(angle sums = 180, P-angles `a+c-x1` and `b+x1` are supplementary) and numerically on random
triangles. **Both prior reports used this correctly.**

### 2. Both prior conjectures are WRONG. The true answer (strong numerical evidence): **Mulan wins iff θ = 180°/n for some integer n ≥ 2** (θ ∈ {90°, 60°, 45°, 36°, 30°, 180/7°, 22.5°, 20°, 18°, ...} → 0).

This is neither "all θ≤90°" (explorer-gametheory) nor "θ=90/2^k dyadic" (explorer-extremal).
Both prior reports under-searched Mulan's move space: they restricted her to either pure
"chip exactly θ" forcing (gametheory) or a single doubling chain θ→2θ→4θ→...→90
(extremal). The real game allows mixed multi-branch strategies (e.g. one child hit θ directly,
the other child driven to 2θ, 3θ, etc., each of which is itself a bounded-move win) — this is
strictly richer and changes the answer.

**Method**: implemented an exact backward-induction / AND-OR minimax in Python (`good(state,
depth)`, memoized), where at each node Mulan may split any of the 3 vertices at a value `x1`
chosen from a *targeted* candidate set (values that make some resulting angle exactly `k·θ` for
integer `k`, `1≤k≤K`, plus `180−k·θ` variants) — justified because the recursive structure of
"forced win in d moves" is generated exactly by these exact-hit equations (I derived the depth-2
extension by hand first: solving the 2×2 "both children forced" system generalizes beyond the
θ,2θ case found by explorer-gametheory/extremal to give NEW triggers like "vertex = 3θ" and
"vertex = 4θ", found via `pair(x1=θ, x1=α−2θ) ⇒ α=3θ` etc. — algebra double-checked by hand and
matches the code's automatically-found witnesses).

**Key falsifying example (θ=60°, refuting BOTH prior conjectures' claim that Shan-Yu escapes /
that 60° is not dyadic-safe)**: from (20°,50°,110°) — the exact triangle explorer-extremal
simulated Shan-Yu surviving 500 rounds against a *greedy* Mulan — the exact minimax finds a
genuine 2-move forced win:
```
(20,50,110): split vertex a=20 (others 50,110) at x1=10
  -> C1=(10,50,120), C2=(10,60,110)   [C2 already contains θ=60 — win if Shan-Yu picks C2]
  C1=(10,50,120): split vertex c=120 (others 10,50) at x1=60
  -> C1'=(10,60,110), C2'=(50,60,70)  [BOTH contain θ=60 — Shan-Yu has no safe reply]
```
So explorer-extremal's greedy/heuristic 500-round simulation was NOT run against an optimal
Mulan; the "escape" it found is an artifact of a suboptimal search, not a real Shan-Yu win.
Similarly explorer-gametheory's claimed cycle for θ=180/7 under **pure exact-θ chip forcing**
is real (verified: that restricted subgame does cycle), but 180/7 is NOT actually a dead end —
the full minimax finds a win in 3 moves from every tested starting triangle including the ones
used in that cycle.

### 3. Numerical sweep — the θ=180/n pattern is sharp and robust
Tested `θ=180/n` for `n=2..10` against **6 structurally diverse starting triangles**
(generic (20,50,110), thin (1,2,177), equilateral (60,60,60), near-isosceles-right (89,89,2),
very thin (170,5,5), generic (33,77,70)): **every single one won**, at shallow depth (1–4 moves),
uniformly across ALL 6 triangles. Example: θ=90→1 move always; θ=60→2 moves (or 0 for
equilateral, trivially); θ=45→2 moves; θ=36→3; θ=30→3 (or 1 for equilateral); θ=180/7→3;
θ=22.5→3; θ=20→4 (or 0/2 for lucky triangles); θ=18→4.

Contrast: swept θ in [30°,90°] in 2.5° steps (K=8 target-multiples, depth ≤5) against the same
triangles — **the only θ values in that whole 24-point sweep that produced wins were exactly
30, 45, 50(partial/coincidental — 50 literally appears in one test triangle), 55(partial), 60,
90 — and of these only 30,45,60,90 (all of the form 180/n) won on EVERY triangle; 50 and 55 did
not** (55 failed on the (1,2,177) triangle at depth 5). All other θ (32.5, 35, 37.5, 40, 42.5,
47.5, 52.5, 57.5, 62.5, ..., 87.5) found **no win at all** on either test triangle, even after
pushing depth to 9 and enlarging the target-multiple set K to 20 for θ=40 and θ=70 specifically
(both remained "no win found").

**Exactness check** (rules out "θ near 60 also works", confirming the boundary is the exact
value 180/n, not an interval): perturbing away from θ=60 by even 0.5°–1° (θ=59, 59.5, 60.5, 61)
**killed the win on all 6 test triangles** (all `None` except one isolated accidental hit for
θ=59 on the (1,2,177) triangle specifically — an artifact of that one triangle's numbers, not a
general win, since the other 5 triangles all failed for θ=59). This sharp on/off pattern at
exactly `180/n` is strong evidence the true characterization is an equality condition
`n·θ=180`, not an inequality or a different discrete set (dyadic or otherwise).

### 4. θ>90°: confirmed dead (matches explorer-gametheory's rigorous invariant proof)
Swept θ=91,100,179 — no win found at any depth in the minimax, consistent with (and a nice
independent numerical check of) the fully-proved "keep all angles ≤90°" survival invariant from
explorer-gametheory (opening 2 in that report) — **that direction of the proof is solid and
should be kept as-is**.

### 5. Why 180/n structurally: the natural generalization of the θ=90 trick
θ=90 works because `a+b+c=180=2·90` lets Mulan force BOTH children to 90 in one universal move
(any triangle). For θ=180/n, `a+b+c=180=n·θ` — the total angle budget is an exact multiple of θ.
Conjecture (not proven, but the natural mechanism suggested by the depth-2/3 algebra above, e.g.
the "vertex=3θ" trigger requiring `3θ<180` i.e. relevant exactly when `n≥3` is achievable):
there is an explicit ≤(n−1)-move universal construction, generalizing the θ=90 one-mover, that
uses the exact divisibility `nθ=180` to always land on θ regardless of starting triangle. This
is THE most promising concrete algebraic target for the outliner: find the explicit n-move (or
`O(log n)`-move) construction. For the converse (non-multiples fail): the likely invariant is
some kind of "θ mod (180/gcd-type)" argument, or a linear-algebra/measure argument over the real
vector space spanned by θ that shows the reachable-angle set from a generic start, modulo the
constraint `a+b+c=180`, can never hit θ exactly unless `180/θ∈ℤ` — this needs real work but is a
well-defined, falsifiable target (unlike the vaguer "avoid a forbidding orbit" arguments in both
prior reports, which are now shown to be based on an under-searched move set).

### Candidate technique(s)
- Algebraic case analysis (2×2 / higher simultaneous-equation systems in x1) exactly as both
  round-1 explorers began, but must be pushed to depth ≥3 (not stopped at the "θ,2θ chain") to
  find the true trigger set — this is what breaks the resonance-cycle red herring.
- For the "180/n works" direction: induction on n, likely via an explicit peeling construction
  (split off a θ-sized wedge repeatedly) — needs a clean invariant like "current triangle has an
  angle that is a multiple of θ" as a progress measure, using up one "θ-unit" of the 180° budget
  per move.
- For the converse ("only 180/n works"): an invariant/monovariant on the θ-residues of the
  angles, or a dimension/genericity argument (the set of triangles from which a forced win exists
  is contained in a countable union of hyperplanes cut out by rational-coefficient equations in
  θ, which for generic irrational/non-180/n θ never contains an open set of starting triangles,
  and Shan-Yu picks his own starting triangle so can always dodge).
- knowledge_base.md: "Invariants & monovariants", "Induction" — same entries as round-1 reports
  flagged, but now aimed at proving/disproving θ=180/n rather than θ≤90 or θ=90/2^k.

### Cheap-kill candidates
- At most one angle ≥90° per triangle (still valid, underlies the θ>90 direction, keep it).
- **New cheap kill**: `180/θ ∉ ℤ ⇒ θ` should be conjectured NOT a Mulan win — before attempting
  any construction for a given θ, first check whether n=180/θ is a positive integer; if not,
  the outliner should not spend effort trying to force a win (matches all failed searches above).
- Equilateral start (60,60,60) is often a fast/degenerate win for θ dividing into its symmetric
  structure — not representative, don't use it as the sole test case (use asymmetric/thin
  triangles as done here) when sanity-checking any proposed universal construction.

### Knowledge-base entries to use
- "Invariants & monovariants", "Induction" (General Proof Methods) — as in both round-1 reports.
- "Synthetic toolkit: angle chasing" — underlies the master formula.

### Analogous past problems (cruxes)
No change from round-1 findings — no strong crux match exists for this specific cevian-cutting
game (both round-1 reports searched `combinatorics/games-and-strategy` thoroughly and found only
loose thematic echoes, e.g. `aimo-0236`'s dyadic-valuation flavor — but note that specific
"dyadic" flavor turned out to be a red herring for THIS problem, since the real answer is
`180/n` for all n, not powers of 2). Do not force the dyadic analogy.

### Prior progress
- θ>90°: **proven** Shan-Yu wins forever (explorer-gametheory's "keep all angles ≤90°"
  invariant) — solid, keep.
- θ=90°: **proven** Mulan wins in 1 move from any triangle — solid, keep.
- θ=180/n generally: **numerically very well supported** (uniform wins across 6 diverse
  triangles, n=2..10, sharp cutoff under 1° perturbation) but **not yet proven** — no explicit
  general-n construction has been written out, and no invariant has been proven for the converse.
  This is the actual open problem for the outliner.

### Dead ends (do not retry)
- **θ=90/2^k dyadic-only characterization** (explorer-extremal's conclusion) — refuted: θ=60°,
  30°, 180/7°, 22.5°(dyadic actually, fine), 36°, 20°, 18° all also win and are not of that form.
  Root cause: assumed Mulan's only tool is the single doubling chain θ→2θ→...→90; the minimax
  shows richer branching strategies exist.
- **"All θ≤90° wins" characterization** (explorer-gametheory's conclusion) — refuted: θ=32.5,
  35, 37.5, 40, 42.5, 47.5, 52.5, 57.5, 62.5, 65, 67.5, 70, 72.5, 75, 77.5, 80, 82.5, 85, 87.5
  (an extensive 2.5°-step sweep in (30°,90°)) all failed to produce ANY forced win even with
  generous search depth (up to 9) and enlarged target sets — strong evidence these are genuine
  Shan-Yu wins, not just search artifacts of an incomplete "pure chip forcing" strategy.
- **explorer-extremal's 500-round greedy simulation "showing" Shan-Yu escapes at θ=60°** — this
  is now known to be WRONG / an artifact of non-optimal (greedy, not full-minimax) play by the
  simulated Mulan; the exact same starting triangle (20,50,110) has an explicit 2-move Mulan win
  at θ=60°, shown above.
- **explorer-gametheory's θ=180/7 "provably cycles" claim** — technically true only for the
  *restricted* pure-exact-chip-forcing subgame (as they themselves flagged), and is NOT evidence
  against Mulan winning at 180/7 overall — she does win, in 3 moves, via the richer move set.

### Small-case / intuition notes
- **Conjecture** (very strong numerical support, exact-boundary behavior observed, NOT proven):
  Mulan can force a win in finitely many steps **iff θ = 180°/n for some integer n ≥ 2**, i.e.
  θ ∈ {90°, 60°, 45°, 36°, 30°, 180/7°≈25.71°, 22.5°, 20°, 18°, 180/11°, ...}. Equivalently:
  180/θ must be a positive integer ≥2.
- This is a countably infinite set accumulating at 0°, structurally resembling the "180/n"
  family that shows up in many circle/polygon partition olympiad results (a natural, clean,
  olympiad-plausible final answer — more so than either prior guess).
- The outliner's top priority: (a) construct an explicit finite-move universal strategy for
  general θ=180/n (generalize the 1-move θ=90 trick — likely by strong induction on n, peeling
  a θ-sized angle at a time, OR by a recursive "reduce n by finding two integers p+q=n, use
  θ target of pθ and qθ" divide-and-conquer, similar to how doubling worked for powers of 2 but
  now needs to work for ALL integers n, not just powers of 2 — this is a genuinely different,
  harder inductive step than either prior report's approach, but the 3θ/4θ triggers found here
  suggest the right building blocks: a state with an angle = kθ (k<n) is "(something like
  ⌈log2 k⌉ or fewer)-move away" from being fully forced); (b) prove the converse — Shan-Yu
  survives whenever n=180/θ is not an integer — likely via an argument that the "good" trigger
  set is always a subset of {kθ : k∈ℤ⁺, kθ<180} (established computationally above, worth trying
  to prove this closure claim rigorously by exhausting the finitely-many simultaneous-equation
  cases as I began doing by hand) combined with a genericity/avoidance argument for Shan-Yu:
  since 180 is not an integer multiple of θ, no angle of a "generic" (rationally independent)
  starting triangle can ever be forced to be exactly kθ using only the affine moves available.
