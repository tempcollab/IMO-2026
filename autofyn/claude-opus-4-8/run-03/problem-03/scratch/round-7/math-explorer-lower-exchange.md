## imo-2026-03 — LENS: lower-bound exchange crux (GAP L2-exch)

Target inequality (in the a=0 / balanced regime, both live approaches agree on the exact
statement): S = F ⊔ B, F = fragments of the top scale (sum 2^n, ≥2 parts, all ≤2^{n-1}),
B = a ≤(n-1)-cut refinement of the tail ladder C_{n-1}={2^{n-1},...,1}, both O_F,O_B ⊆
[0,2^{n-1}). Need
  μ(O_F ∩ O_B) ≤ (D(F)+D(B)-1)/2   … equivalent to D(S) ≥ 1,
binding only when |D(F)-D(B)|<1 and D(F)>0 (the "balanced overlap" band). This is the
*same* combinatorial fact induction-peel's Gap-Interleaving Lemma (GAP L2, critical band of
(L⋆) + Case II |F|≥3) attacks by rearrangement/adjacent-pair exchange — two independent
derivations of one wall.

### Distinct openings

1. **Strengthen the induction hypothesis from a scalar to a structural statement.**
   The current proof only feeds `D(B) ≥ 1` (a number) into the SPLIT master inequality via
   the crude cap `μ(O_F∩O_B) ≤ min(D(F),D(B))`. That cap is tight only when one odd-set is
   (nearly) contained in the other — it throws away *where* O_B lives. But B is not an
   arbitrary set with `D(B)≥1`: it is itself a refinement of a superincreasing ladder, so by
   the SAME top-scale dichotomy (Lemma ONE) applied one level down, O_B has constrained
   structure (e.g. at most one "large" excursion near the top of its own ladder, recursively).
   **Opening:** carry a stronger IH — not just `D(B)≥1` but something like "the odd-set O_B,
   when read against the dyadic gaps `(2^{n-2-i}, 2^{n-1-i})` induced by C_{n-1}'s own
   recursion, occupies at most one atom per gap" (a structural interleaving invariant). This
   would let you bound `μ(O_F∩O_B)` gap-by-gap rather than via the global min-cap, closing the
   balanced band directly. This is a genuinely different lever from "prove the single scalar
   inequality by a clever trick" — it says the master inequality as stated may be UNCLOSABLE
   from `D(B)≥1` alone, and the fix is upstream (a richer IH), not downstream (a sharper
   overlap lemma).

2. **Merge-sort / rank-parity argument treating F and B symmetrically (not via SPLIT at all).**
   D(S) is the alternating sum over the descending merge of F and B. Directly track, as you
   merge two sorted lists, how the "current running sign" flips; this is a two-pointer /
   patience-sort style argument (cf. KB's Monotone-Subsequence toolkit, Dilworth/ES flavor,
   though the analogy is inexact) rather than the measure-integral route. Concretely: define
   the interleaving PATTERN of F vs B in the merged order as a binary string; D(S) is a
   fixed linear functional of the pattern and the values. The claim "D(S)≥1" should reduce to
   a claim about which patterns are *reachable* given the cut-budget constraint
   `(|F|-1)+c_T≤n` — i.e. a pattern-counting / extremal-pattern argument, potentially cleaner
   than tracking measures of unions.

3. **A genuine potential/monovariant exchange, modeled on the crux corpus's "closest-pair
   merge" technique (aimo-0298).** aimo-0298 (IMO 2022-ish "scales" problem) proves a global
   weight bound `Σ 2^{-r_S(x)} ≤ 1` by strong induction: find the two elements at the MINIMAL
   scale gap, show removing/merging them can only be safe (any other pair at distance >1 apart
   in sorted order has larger scale), and induct on `|S|`. The technique — order the reals,
   find the closest (in a dyadic-scale sense) adjacent pair, merge/delete it, and show the
   potential is monotone — is structurally the closest crux to our "adjacent-atom exchange"
   (slide a fragment across one tail atom `t_k`, track `μ(O_F∩O_B)` monotonically toward
   canonical). It is a genuine hint for how to *write* the exchange step rigorously as an
   induction on the number of "out-of-place" fragments (a well-founded monovariant), rather
   than trying to prove the inequality as a static optimization. Recommend the outliner or
   builder read `aimo-0298`'s full solution (`past_problems_database.json`, `problem_id
   aimo-0298`) for the induction-on-minimal-scale-pair pattern.

4. **Attack via the interleaving being an LP / rearrangement extremal problem with the
   "gap-occupancy" already identified in induction-peel's §3.3** (below-insertion /
   above-insertion canonical layouts, exact telescoping to `f₁-1` and `1` respectively). Both
   live approaches already have the EXACT value at the conjectured extremum (proven identity,
   not conjecture); what's missing is only that this is a minimum/maximum over the admissible
   set. A rearrangement-inequality-style argument (KB: "Standard inequalities" / rearrangement)
   applied to the *pairing* of F-fragments against tail gaps could show any deviation from
   "one fragment per gap, just outside it" can only move D in the unsafe direction — but this
   needs the *adjacent swap* lemma made precise (what happens to D when you move one F atom
   from gap k to gap k+1, or merge two atoms in one gap) — precisely GAP L2 as already stated,
   just packaged as a rearrangement inequality rather than a raw "exchange lemma."　

### Candidate technique(s)
- Structural/inductive strengthening of the IH (not just scalar D(B)≥1) — most promising,
  attacks the actual gap in the master-inequality route rather than just polishing it.
- Merge-pattern / interleaving-pattern combinatorics (finite pattern space, cut-budget as a
  constraint on reachable patterns) — a genuinely different top-level target from "prove one
  inequality," reduces to a pattern-counting extremal claim.
- Potential-function induction modeled on aimo-0298's minimal-scale-pair merge (rearrangement
  / monovariant / adjacent-transposition family in KB and crux corpus).
- Rearrangement inequality (KB "Standard inequalities") repackaging of the exchange lemma.

### Cheap-kill candidates
- None found that dispatch the whole gap cheaply. But a useful PRUNE for builders: **the
  crude cap `μ(O_F∩O_B) ≤ min(D(F),D(B))` is provably not tight enough** — the known
  counterexample-to-the-cap-only-route is `D(F)=D(B)=1` giving true `D(S)=2` (cap gives 0);
  so any attempted proof that tries to sharpen ONLY the cap (without using more structure
  of O_B/O_F) is very likely to fail the same way induction-peel's naive per-cut bound
  `|ΔD|≤2s₂` failed (flagged as "too loose" in both approach files). Don't retry naive
  per-cut/per-atom toggle summation without a monovariant.
- Parity/size check: `|F|≥2` and `Σ F = 2^n` with each fragment `≤2^{n-1}` forces `|F|≥2`
  always (Lemma ONE); the `|F|=2` case is fully closed (both approaches), so the true
  residual content is strictly `|F|≥3`. Any proposed proof should explicitly reduce to
  `|F|≥3` and should degenerate correctly to the known `|F|=2` closed case as a check.

### Knowledge-base entries to use
- **"Standard inequalities" / rearrangement** (Algebra & Polynomials section) — for opening 4.
- **Induction (ordinary/strong), infinite descent** (General Proof Methods) — the natural
  frame for opening 1 and 3 (strengthen IH; induct on a monovariant).
- **Invariants & monovariants** (Combinatorics section) — exactly the mechanism needed for
  the adjacent-atom exchange (opening 3).
- **Monotone Subsequences: Erdős–Szekeres, Dilworth, Patience Sort** — loosely analogous
  machinery for opening 2 (merge-pattern / two-pointer arguments on sorted sequences), though
  the fit is not exact; worth checking if the (I_p,D_p) coordinate trick has any translation
  to "position in F-merge vs B-merge," but this is speculative, not a confirmed match.

### Analogous past problems (cruxes)
- **`aimo-0298`** (IMO Shortlist "scales" problem, domain=combinatorics,
  subtopic=extremal-principle). Crux: define weight `w(S)=Σ_x 2^{-r_S(x)}` over a finite
  real set with a dyadic "scale" function `D(x,y)=⌊log2|x-y|⌋`; prove `w(S)≤1` by strong
  induction on `|S|`, picking the pair at MINIMAL scale (necessarily sorted-adjacent, since
  two gaps each ≥ the minimal scale sum to at least the next scale up — a superincreasing-type
  argument essentially identical in flavor to our "at most one final piece exceeds 2^{n-1}"
  Lemma ONE), merging/deleting that pair, and showing the potential is monotone under the
  merge. **This is the single best structural analogue in the corpus**: same dyadic/scale
  bookkeeping, same "closest pair in sorted order" reduction, same style of potential-function
  induction that GAP L2-exch needs. Genuinely worth reading in full (`past_problems_database
  .json`, `problem_id: aimo-0298`) before attempting the exchange step.
- No other crux in the corpus (searched combinatorics/algebra subtopics
  games-and-strategy, invariants-and-monovariants, extremal-principle, plus keyword search
  over technique/how_used for "alternating sum," "interleav-," "cutting," "stick," "merge,"
  "rearrangement," "adjacent transposition") is a close structural match to a *claiming game
  on stick fragments with a parity/alternating-sum payoff*. `aimo-0340` (IMO pearls-cutting
  problem, two colored strings repeatedly bisected) shares the "ceiling/floor halving,
  propagate a length gap through matched halvings" flavor superficially, but its game
  mechanics (fixed cutting rule each round, not an adversarial minimax over cut placement)
  are different enough that I would call it suggestive, not analogous — flag it only as a
  secondary read if opening 3 stalls.

### Prior progress
Both live approaches (`induction-peel`, `parity-measure-potential`) have independently
reduced the ENTIRE lower bound's residual content to this one inequality (or its
rearrangement-flavored twin, the Gap-Interleaving Lemma). Concretely:
- The SPLIT master inequality `D(S) ≥ |D(F)-D(B)|` is proved and certified (file
  `lemmas/split-cross-term.md` underlies it), closing the whole `|D(F)-D(B)|≥1` subregime,
  incl. ALL even-multiplicity/doubling fragmentations (`D(F)=0`).
- The extremal value (=1) is computed EXACTLY (not just numerically) two ways: the attained
  cascade construction, and the "canonical interleaving" merged-telescope identity
  `Σg_k − Σt_k = 2^n-(2^n-1) = 1`. So the target floor is verified exact, not conjectural.
- `induction-peel`'s Lemma PEEL + band decomposition (3.1) gives the exact identity reducing
  Case I to `D(S') ≤ f₁-1`ᵂ (=GAP L1, the dual/upper-flavored twin of this same crux), with
  the trivial regime (`w≤2^{n-1}-1`) fully closed, leaving only a width-one critical band.
- Both `|F|=2` sub-cases (Case II induction-peel, equal-bisection parity-measure) are fully
  closed via IH `D(T)≥1`/`D(B)≥1` and Lemma HALF/U0(a) (even multiplicity ⇒ D=0).

### Dead ends (do not retry)
- **Mass-threshold / subset-cover reductions** (from the upper-bound side, GAP U) are
  REFUTED by a rigorous counterexample `(0.44,0.281,0.279)` — not directly this gap, but the
  same underlying lesson applies here: bounding a residual `D` by a function of *measure/mass
  alone* (rather than its internal odd-set structure) is a proven-insufficient lever. The
  crude cap `μ(O_F∩O_B)≤min(D(F),D(B))` is exactly this kind of measure-only bound, and it is
  known to fail exactly where `D(F)≈D(B)` (verified: `D(F)=D(B)=1` case, true `D(S)=2`, cap
  route gives only `0`). Any attempted fix that stays purely in "bound `μ(O_F∩O_B)` by some
  function of `D(F)`,`D(B))` alone, with no reference to *where* the odd sets sit relative to
  the ladder `t_k`" is very likely to hit the same wall.
- **Per-cut/per-move toggle-measure summation `|ΔD|≤2s₂`** (Lemma T) — explicitly flagged in
  both approach files as "too loose, doesn't see the budget." Confirmed by both independent
  derivations; do not resubmit as-is.
- Round-3's "budget-monotonicity ⇒ WLOG single top cut" — already refuted with an explicit
  counterexample (minimiser puts ALL n cuts on top, interleaving construction, D=1 exactly);
  this is recorded and should not be revisited.

### Small-case / intuition notes (all labeled conjecture/numerics, not proof)
- My own quick numeric probe of the raw inequality WITHOUT enforcing the cut-budget
  constraint `(|F|-1)+c_T≤n` produced apparent "violations" with `D(S)<1` (e.g. found
  `D(S)≈0.483`). On inspection this was an artifact of an invalid (over-budget) refinement in
  my test harness, not a real counterexample — a useful cautionary note: **any builder writing
  a numeric verifier for GAP L2-exch MUST explicitly enforce `(|F|-1)+c_T≤n-1` (one level
  down) or the checker will manufacture false counterexamples.** Both approach files' own
  verified-zero-failure claims (round 6, 3×10^5 samples) presumably do enforce this, but it's
  worth an explicit sanity re-check by the next builder given how easy it is to get wrong.
- The reported tight case `D(F)=D(B)=1`, `D(S)=2` (not `1`) shows the true inequality is
  NOT tight along the "cap" route — i.e. the minimum of D(S) is not approached by pushing
  `μ(O_F∩O_B)` to its cap `min(D(F),D(B))`; conjecturally the true worst case (D(S)=1 exactly)
  occurs at a specific interleaved configuration (the canonical layout in opening 4), and any
  correct proof of GAP L2-exch must be tight exactly there, with `D(F)=D(B)=1, D(S)=2` case
  being comfortably non-binding (`D(S)=2≥1`) — consistent with, not contradicting, the target.
