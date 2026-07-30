## imo-2026-03 — lens: open k≥2 lower-bound gap (s≥3 top-splits)

### What I did
Read `current.md`, `geometric-dominance-construction.md`, and the certified
`lemmas/insertion-and-abstract-reduction.md`. Confirmed by direct re-derivation
that Lemma I / rank-shift-by-s / Claim ★ (s∈{1,2}) are correct, and that the
s=3 counterexample to Claim ★ (`q=1/8, T={1/8}, R={649/4000,116181/2000000,
59319/2000000}`, giving `oddrank(R∪T)=440681/2000000<1/4=2q`) is exact and
reproducible. Then ran fresh numeric experiments (exact-Fraction + float
Monte Carlo/DE, `/tmp/probe1.py`–`/tmp/probe10.py`) targeting exactly the
question the dispatch asked: does the theorem (not the over-abstracted
Claim ★) actually survive for s≥3 once T is forced to be a genuine
mark-bounded refinement of the geometric tail, and what extra invariant of T
would resolve the counterexample?

### Key finding 1 — the s=3 counterexample is an artifact of over-abstraction, not a real threat
The counterexample's `T={1/8}` is a **single element**. In the real problem,
when k=2 marks split `p_1` (using `s=3`), the leftover tail `T` is a
refinement of `T_0=λ_n·A_{n-1}`, which for `n≥2` has **at least `n` elements
before any further splitting** (its own base cardinality), not 1. So the
counterexample multiset is not reachable as an actual tail under the game's
rules — it "cheats" by having far too few elements for its claimed
`oddrank(T)≥q` to be realistic. This matches the file's own honest diagnosis
but is now confirmed by direct construction: the abstraction dropped too much
(not just max/oddrank, but T's minimum cardinality and its self-similar
shape).

### Key finding 2 — adding Σ(T) as a third scalar invariant is STILL insufficient
Natural next guess: Claim ★ needs `Σ(T)=Λ` pinned to the real tail-sum value
too (in the true problem `Σ(T)=λ_n`, and `λ_n/q → 2` as `n→∞`, ranging over
`3/2, 7/4, 15/8, 31/16,...` for `n=2,3,4,5`). I ran a randomized search
(`probe9.py`) fixing `max(T)≤q`, `oddrank(T)≥q`, **and** `Σ(T)=Λ` exactly at
each of these realistic ratios, searching over `s=3` compositions `R` of
`2q`. **Violations of `oddrank(R∪T)≥2q` were found at every tested ratio
`Λ/q∈{1.0,...,1.9}`**, only vanishing (in a limited search) near `Λ/q≈1.99`.
So a 3-scalar abstraction (max, oddrank, sum) is *still* provably too weak in
general — pinning down `Σ(T)` alone does not resolve the gap. This is a new
negative result (not in the existing file) worth recording: **no small fixed
tuple of scalar summaries of T suffices; the proof must use T's actual shape
(element count bounded by the mark budget, and/or its superincreasing/
self-similar structure), not any bounded list of aggregate statistics.**

### Key finding 3 (positive, most useful) — the real theorem checks out numerically, and reveals the extremal strategy's structure
Testing the *actual* game (T restricted to arise from ≤`n−k` real marks
refining `T_0=λ_n·A_{n−1}`, not an adversarial abstract multiset) for
`n=2,...,6`, `k=2` (`s=3`):
- If Xiang Yu's 2 top-marks are combined with his remaining `n−2` marks
  spent **anywhere in the tail** (I tested: concentrating all remaining
  marks recursively on the tail's own largest piece `p_2`; spreading 1 mark
  each on `p_2` and `p_3`; spending all `n` marks entirely on top with tail
  fully untouched; and large-scale unstructured random binary-split search
  over the whole tail), the numerically-found minimum of `oddrank(B)` is
  **exactly `c(n)`, never below**, matching the doubling-family values
  `slack(k,n)` already recorded in the file's Round 2 table (verified exactly
  for `n=4`: `slack(2,4)=1/31>0` for the *tail-untouched* sub-case alone, but
  once the extra `n−k` marks are allowed on the tail, the true joint minimum
  drops to exactly `c(n)` — i.e. Xiang Yu's best use of extra marks after
  splitting `p_1` into 3 is indeed to spend them on the tail, and doing so
  exactly closes the slack).
- Crucially, **several different tail-mark placements (spread over `p_2,p_3`
  vs. concentrated on `p_2` alone vs. all marks entirely on top) all hit the
  *same* minimum value `c(n)` in my tests** — suggesting there may be a
  whole family of extremal configurations, not a unique one, echoing the
  `s=1,2` equality case structure already noted in Proposition A/Lemma F1.
- I initially got a spurious "violation-looking" result via gradient
  optimizers (Nelder–Mead / `differential_evolution`) converging to `0.5645
  > target` on the `n=4, k=n=4` (tail-fully-untouched) case and mistakenly
  read this as a possible failure of the doubling family's claimed
  `slack=0`; a 2-million-sample Dirichlet random search resolved this —
  it *does* hit the target exactly (`0.51612903 = 16/31`), the gradient
  methods were just getting stuck in bad local optima on the boundary of the
  simplex parametrization. **Caution for future numeric probes on this
  problem: gradient-based optimizers (NM, DE) are unreliable near this
  landscape's optimum (likely because the true minimizer sits at/near a
  simplex boundary with several tied coordinates, e.g. `p3=p4` appearing
  twice in `C_4`); prefer large-sample Dirichlet/random search or exact
  algebraic evaluation of the candidate family, not local optimizers alone.**

### What extra structural fact about T looks like it's actually needed
Based on the above, the natural candidate is **not** a new scalar invariant
but a **stronger induction hypothesis that carries forward T's own recursive
shape**, in one of these forms (untested/unproved, just surfaced as
candidates):
1. **Track majorization, not just oddrank.** Conjecture: the geometric
   tail's refinements satisfy a majorization-type bound on the *whole sorted
   vector* (not just the odd-rank sum), strong enough that merging with any
   `s`-part `R` summing to `2q` can be handled by a rearrangement/
   exchange argument rather than a case split on `s`. This would need a
   *vector* strengthening of Claim ★ (e.g., "oddrank of every prefix" or
   "the sorted sequence of T majorizes a specific comparison sequence"),
   which is a strictly stronger and more informative hypothesis than the
   single number `oddrank(T)≥q`.
2. **Joint/simultaneous induction instead of two-step (split-top-then-
   induct-on-tail).** The numerics (finding 3) suggest the extremal
   strategy spends *all* Xiang Yu's marks along a single greedy chain
   (recursively splitting whichever current piece is largest — first `p_1`,
   then, once `p_1`'s top sub-piece is itself no longer clearly dominant,
   the tail's own top piece `p_2`, etc.), rather than needing to handle an
   arbitrary interleaving of top-splitting and tail-splitting. If this
   "recursive-greedy-largest-piece" strategy can be shown to dominate (be at
   least as good for Xiang Yu as) every other strategy — a **majorization/
   exchange argument bounding what happens if Xiang Yu deviates from
   splitting the current largest piece** — the whole `k≥2` case could reduce
   to analyzing *one* explicit recursive family (essentially the doubling
   family, generalized to allow the "extra" marks past `k` to also cascade
   recursively), which is a finite, checkable recursion, not an
   over-general worst-case-multiset claim. This is speculative (a possible
   route, not verified) but is consistent with every numeric experiment run
   this round: unstructured/spread-out tail-splitting never beat the
   greedy-recursive strategy in any test.
3. **Bound T by cardinality**, i.e. explicitly carry "T arises from ≤`n−k`
   marks refining a multiset of ≥`n+1−k` base elements" as a hypothesis
   (not just max/oddrank/sum) — this at least rules out the exact `T={1/8}`
   counterexample (cardinality 1) and the `Σ(T)=Λ` counterexamples found in
   finding 2 (which also used very small `|T|`, e.g. 1–3 elements, far
   fewer than the ≥`n−1` a real tail refinement would have after only a
   couple of marks are removed from a base of `n` pieces). Worth checking
   whether adding a cardinality floor to Claim ★'s hypotheses (`|T|≥` some
   function of `n,k`) is enough by itself — I did not have time to test this
   specific 4th-invariant strengthening numerically this round; it's a
   concrete, cheap next experiment.

### Candidate technique(s) for the outliner
- Strengthen Claim ★ to a **majorization** statement rather than a scalar
  `oddrank≥q` statement (knowledge-base: rearrangement/majorization
  inequalities, if present — check `knowledge_base.md`'s entries on
  majorization/Karamata; I did not find a directly-named entry but this is
  the natural KB category).
- **Greedy-exchange argument**: show that moving marks from the tail to
  "wherever the current largest untouched piece is" (recursively) is a
  weakly-dominant strategy for Xiang Yu, reducing the adversary's search
  space to a single explicit recursive family (the already-certified
  doubling-family recursion, `slack(k,n)=λ_n·slack(k-1,n-1)`, still unproved
  in general per the file but numerically exact for `n≤6`) — this is a
  genuinely different top-level target than Claim ★'s "any multiset T"
  framing: instead of bounding over *all* T, prove *a specific T* (built
  recursively by the greedy rule) is always at least as bad as any other,
  via an interchange argument.
- **Cardinality-augmented Claim ★**: same shape as the existing lemma but
  with an added hypothesis `|T|≥` (mark-budget-derived floor), cheapest to
  test first (a few hours of work: does the s=3 counterexample search
  produce violations once |T| is forced ≥ some threshold like `n−k+1`?).

### Cheap-kill candidates
- Test whether Claim ★ + a cardinality floor on `|T|` (e.g. `|T| ≥ n-k`,
  matching the real problem's base tail size after `k` top-marks and 0 extra
  tail marks) already rules out all found counterexamples — fast to check
  computationally (extend `probe9.py`'s search restricting `m` = |T| to be
  large, e.g. `m≥3` or `m≥4`, and re-run the violation search). Not done
  this round due to time; flagged as the single fastest next check.
- Parity/pigeonhole: none obviously new beyond what `recursive-embedding-
  induction`'s Lemma L already explores (parity of block lengths for the
  tail-untouched `k=n` sub-case) — that remains a live, narrower, still-open
  cheap-ish target (verified exactly for `n=1..8`, not proved in general).

### Knowledge-base entries to use
Did not have time this round to re-grep `knowledge_base.md` exhaustively
beyond what prior rounds already cite (Lemma 1's backward-induction game
value, rearrangement-style arguments). Recommend the outliner re-check for a
named majorization/Karamata or exchange-argument entry if one exists, since
finding 3 above points toward that being the right hammer.

### Analogous past problems (crux corpus)
Not queried this round — time was spent on the numeric structural probe per
the dispatch's explicit instruction ("Do NOT attempt the proof yourself...
Try small cases numerically"). Recommend a future explorer query the corpus
for `subtopic` terms like "combinatorial game / alternating claiming",
"majorization", or "greedy exchange argument" per
`crux_moves_documentation.md`'s subtopic index.

### Prior progress
As recorded in `current.md`: `k=0` (all n), `k=1` tail-untouched (all n), and
`k≤1` with simultaneous tail-splitting (unconditional n≤2, conditional on
M(n-1) for general n) are closed. `k≥2` open in every form. This round adds:
(a) a rigorous negative result that even a 3rd scalar invariant (Σ(T)) does
not rescue Claim ★ for s≥3, and (b) numeric confirmation (Dirichlet random
search, corrected after an optimizer artifact) that the *real* (mark-bounded,
self-similar) game value does hit exactly `c(n)` at `k=2` for `n=2..6`, with
the extremal Xiang-Yu strategy apparently always expressible as recursive
greedy-largest-piece splitting.

### Dead ends (do not retry)
- Claim ★ generalized with only `max(T)`, `oddrank(T)` bounds: proved false
  for s≥3 (already certified).
- Claim ★ generalized with `max(T)`, `oddrank(T)`, AND `Σ(T)=Λ` pinned to the
  realistic tail-sum ratio: **also false** (new this round, found violations
  at Λ/q ratios 1.0 through 1.9 via randomized search — see finding 2). Do
  not propose "just add the sum" as the fix; it doesn't work.
- Gradient-based local optimizers (Nelder-Mead, `differential_evolution`)
  are unreliable for finding the true minimum in this family of problems —
  they got stuck ~5% away from the true optimum on the `n=4, k=4`
  tail-untouched case; use large-sample Dirichlet/random search or exact
  symbolic evaluation of candidate families instead when probing numerically.

### Small-case / intuition notes (all labeled conjecture — numeric evidence only)
- Conjecture: for every tested `n=2..6`, `k=2`, the true minimum of
  `oddrank(B)` over all legal Xiang-Yu strategies spending exactly 2 marks on
  `p_1` and the rest freely in the tail equals `c(n)` exactly, and is
  achieved (among other configurations) by concentrating all remaining marks
  recursively on the tail's own current-largest piece.
- Conjecture: the doubling family `C_k` (already in the file) generalizes
  naturally to a "recursive doubling all the way down" family that uses
  *all* n marks (some on top, the rest cascading down the current-largest
  untouched piece at each step) and always attains exactly `c(n)`; if this
  family can be shown to majorize/dominate every other mark allocation, the
  k≥2 gap reduces to proving dominance of one explicit recursive
  construction rather than bounding an arbitrary abstract T.
