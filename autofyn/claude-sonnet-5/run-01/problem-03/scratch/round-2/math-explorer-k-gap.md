## imo-2026-03 — scouting the k≥1 (top-piece-split) gap

### Setup used for probing
Against `A_n = {p_1,...,p_{n+1}}`, `p_i = 2^{n+1-i}/(2^{n+1}-1)`, I let Xiang Yu
spend `k` of his `n` marks splitting `p_1` into `k+1` continuous parts and the
remaining `n-k` marks distributed (in every combinatorial pattern, for small
`n`) among the `n` tail pieces `p_2,...,p_{n+1}`, each split into further
continuous parts. For each `(n,k,tail-cut-pattern)` I minimized `oddrank(B)`
over all continuous split ratios with `scipy.optimize.minimize` (Nelder–Mead,
many random restarts, since `oddrank` is only piecewise-linear/non-smooth).
For `n=2,3` I enumerated *all* integer compositions of the remaining cuts
among the tail pieces (feasible exhaustively at this size); for `n=4` I used a
handful of representative compositions plus even spreads. Code:
`/tmp/explore_k.py`, `/tmp/explore_k2.py` (kept on disk, not part of the repo).

### Main finding: k≥1 never helps Xiang Yu below c(n) — and k=0 is *not* the hardest case
For every `n ∈ {2,3,4}` and every `k = 1,...,n` tested, the numerically found
minimum of `oddrank(B)` equals `c(n)` **exactly** (differences ~1e-7,
consistent with floating-point noise around an exact equality, not a real
gap). No configuration with `k≥1` ever produced `oddrank(B) < c(n)`.

Crucially, **`k=0` (Proposition A's case, top untouched) is strictly worse for
Xiang Yu** than every `k≥1` case, not merely tied:
```
n=2: c(n)=0.571429   k=0 best=0.642857 (diff +0.0714)   k=1 best=0.571429 (diff 0)   k=2 best=0.571429 (diff 0)
n=3: c(n)=0.533333   k=0 best=0.633333 (diff +0.100)    k=1..3 best=0.533333 (diff 0)
n=4: c(n)=0.516129   k=0 best=0.629796 (diff +0.114)    k=1..4 best=0.516129 (diff 0)
```
So the true worst case for Liu Bang (the minimizing Xiang-Yu response) is
*always* achieved with `k≥1` — Proposition A proves a correct but **slack**
inequality for a case that is never tight. The already-proved `k=0` case does
NOT degenerate-cover the general case; the open `k≥1` gap is where the real
extremal behavior lives, and any proof of the reduction must engage it
directly rather than treat it as a lesser add-on.

### Structure of the flat optimum (evidence for the right technique)
For every tested `k` from 1 to `n`, the minimum value is the *same* constant
`c(n)` — a whole family of distinct Xiang-Yu strategies (different `k`,
different tail-cut patterns) all achieve equality simultaneously. Inspecting
an explicit optimal solution (n=3, k=1, cuts on tail pieces 1 and 3):
Xiang Yu's optimizer converged to splitting `p_1` into **exactly two equal
halves**, each equal to `p_2` (since `p_1 = 2p_2` exactly in the geometric
config). That is, splitting the top piece in half doesn't create an
arbitrary new value — it reproduces an extra copy of `p_2`, i.e. it uses the
doubling identity `p_i = 2p_{i+1}` to fold the top-split case back into the
same combinatorial shape as Proposition 4's construction (which uses k=n).
This is strong evidence that **the whole family of k≥1 optimal responses are
just different "depths" of the same self-similar halving construction**, not
independent phenomena requiring separate case analysis.

### Candidate technique to close the gap
This flatness (many distinct k achieving the exact same value c(n), all via
the doubling relation p_i=2p_{i+1}) points away from a brute per-k case split
and toward a **mark-fungibility / reduction lemma built on self-similarity
(Lemma 3, already certified in `lemmas/geometric-configuration-facts.md`)**:

- Show that splitting `p_1` with any `k≥1` marks can be *simulated or
  dominated* by an equivalent response that instead treats one mark as
  "moved" into the tail's self-similar copy of `A_{n-1}` (since
  `p_1 = 2p_2` and the tail is exactly `λ_n · A_{n-1}`, Lemma 3), reducing a
  k-mark top-split-plus-tail-split response at level n to an (k-1)-mark (or
  equivalent) response purely within a rescaled level-(n-1) problem.
- This would let a **strong induction on n** (already the spine of
  `recursive-embedding-induction`) absorb the k≥1 case uniformly instead of
  needing an ad hoc combinatorial argument for "how many marks touch the
  top": the inductive step handles "one mark spent, wherever it is spent"
  as a single unit via the doubling identity, rather than branching on
  top-vs-tail.
- Concretely: try to prove a **potential-function decomposition**
  generalizing Proposition A's clean identity
  `oddrank(B) = p_1 + evensum(T)` (k=0 case) to
  `oddrank(B) - c(n) = (nonnegative sum of terms indexed by unused
  "halving slack")`, i.e. an exact telescoping/invariant argument (in the
  spirit of Lemma 3's self-similarity) rather than a fresh inequality per k.
  The fact that equality is hit on a whole manifold of strategies (not an
  isolated point) is itself evidence that the right proof is an **identity**
  (algebraic invariant that's ≥0 termwise) rather than a strict-inequality
  argument via majorization/rearrangement over generic (non-doubling)
  configurations.

Rearrangement/majorization (à la `majorization-smoothing`'s Lemma C
concavity idea) remains a secondary candidate but the doubling-identity
evidence here is more specific and more likely to give a short, clean
argument than a general concavity/KKT calculation, which that approach's own
report flags as unfinished, substantial, and possibly requiring a large case
enumeration if concavity fails.

### Cheap-kill / sanity checks
- Parity/domination check confirms Prop A's k=0 bound is real but never
  binding — so it should NOT be presented as "the hard case is settled,
  k≥1 is a technicality." Flag this explicitly to the outliner: the current
  framing in `current.md` risks under-stating how central k≥1 is.
- No configuration tested gave `oddrank(B) < c(n)` for ANY k (0 through n),
  which is additional numeric support (beyond the reviewer's n=1,2,3
  differential_evolution checks already in `lemmas/`) that
  `min_B oddrank(B) = c(n)` exactly for `A_n`, extended now to n=4 and to the
  k≥1 sub-case specifically, which had not been separately checked before.

### Population / prior work context
- `sample_approaches` returns the same 3 approaches noted in `current.md`
  (`geometric-dominance-construction`, `recursive-embedding-induction`,
  `equalization-potential-bound`), all marked `stale: true` (Elo predates
  this round's findings) — no new approach has appeared in the ranker yet
  besides `majorization-smoothing.md` (present as a file, not yet ranked/
  reviewed — appears to be a fresh unsolved draft from this round proposing
  the concavity/smoothing route discussed above).
- Dead ends: none newly found here. `equalization-potential-bound`'s
  "dead-end" claim was already flagged by the reviewer as conditional on the
  still-open lower bound — my probing doesn't resolve that, just confirms
  the lower-bound conjecture numerically once more.

### Summary for the outliner
- k≥1 does NOT help Xiang Yu beat c(n) (strong numeric evidence, n=2,3,4,
  exhaustive-for-size search over combinatorial cut patterns + continuous
  optimization).
- k=0 is strictly suboptimal for Xiang Yu, not merely a boundary case —
  the real minimax action is in k≥1, so the proof must directly handle it,
  not lean on Prop A as covering "most of" the difficulty.
- The optimal k≥1 responses observed are literal instances of the doubling
  identity `p_i = 2p_{i+1}` folding a top-split back into extra copies of
  `p_2`, matching the self-similar structure already certified in Lemma 3 —
  strongly suggesting the fix is a **self-similarity-based reduction/
  induction lemma that treats top-splits and tail-splits as fungible marks**,
  building on (not replacing) `recursive-embedding-induction`'s spine, rather
  than a brand-new majorization/concavity argument (the latter is plausible
  but flagged by its own author as unfinished and possibly heavy).
