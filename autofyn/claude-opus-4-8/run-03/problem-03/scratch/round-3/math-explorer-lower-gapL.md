## imo-2026-03 — lens: LOWER-BOUND wall, GAP L / B2 / SL (Xiang cuts the top dyadic piece)

### Setup recap (confirmed correct, matches current.md and all three approaches)
Liu's dyadic construction, integer units of `u_n`: pieces `{1,2,4,...,2^n}`, sum `2^{n+1}-1`.
Need: for any ≤n Xiang cuts, `D ≥ 1`. Case A (top piece never cut) is fully proved via
Lemma M (`N(t)=1` odd on `[2^{n-1},2^n)`). Case B (Xiang cuts the top piece `P=2^n` at least
once) is open in all three live approaches under different names (GAP L / GAP B2 / Sub-lemma
SL's "imperfect top cut" branch) — same mathematical obstruction in all three: the fragments
of P dominate the tail in the global sort, so the residual is not cleanly the order-(n-1)
dyadic instance, and no approach has closed the general (non-bisection) top cut.

I re-verified round 2's numeric finding (min D = 1 exactly for n=1,2,3, flat across the choice
of first-cut fraction on the top piece) with an independent random-search script; confirmed
again with n=4. This is strong evidence the claim is TRUE and TIGHT — not a dead end to route
around.

### Main new finding this round: an EXACT toggle identity for cutting the current max piece
(this is the substantive result of this exploration — a candidate to close GAP L directly,
not just another framing of the obstruction)

**Setup.** Let `C = {p} ∪ R` be any current configuration where `p` is strictly the largest
piece (`p > max(R)`). By the "single dominant piece" identity (already discovered
independently in `parity-measure-potential` as their `(LB-id)`, `D(S)=f₁−D(S_L)`):
```
D_C = p − D_R.
```
Now suppose Xiang cuts `p` into `p1 ≥ p2` (`p1+p2=p`). Applying Lemma T's toggle calculus
(`E = [0,p2) ∪ [p1,p)`) *combined with* the dominance structure of `p` over `R`, I derived —
and verified both numerically (35 random trials, `n=2..4`, exact match to `1e-9`) and
symbolically (sympy, exact algebraic match) — the identity
```
D_new = D_C − 2·μ( [0,p2) ∩ E_R ),      E_R := {t : N_R(t) is even}  (complement of O_R).
```
Equivalently `D_new = p − 2p2 − D_R + 2μ(O_R ∩ [0,p2))`. I confirmed by direct symbolic
computation (order `p1 > x1 > x2 > p2`, tail `R={x1,x2}`) that this identity is exact, not
approximate — this should be provable in general by the same band-splitting argument used for
Lemma M/T (see derivation below), not just a numerical coincidence.

**Derivation sketch (not full proof, but the mechanism, so the outliner/builder can verify
quickly):** for `t ≥ max(R)`, only `p` can exceed `t`, contributing `N(t)=1[t<p]`. For `t <
max(R)` (`< p` too), `N_C(t) = 1 + N_R(t)` (p always counts), so `O_C` restricted to `[0,
max(R))` is exactly `E_R` there (parity flips because of the `+1`). After the cut, on
`[p1,p)` (⊆ toggle set `E`, length `p2`) the old-odd band flips to even; on `[max(R),p1)`
(untouched, still odd, only `p1` counts); on `[0,p2)` (⊆ `E`) parity flips relative to the OLD
state there, i.e. new-odd = `E_R ∩ [0,p2)` becomes... (sign bookkeeping as in the derivation)
gives the stated closed form. **This is exactly the quantitative form of "cutting a scale
costs that scale":** the *only* way Xiang's cut can lower `D` is by "eating into" the region
where `R`'s own count was already even (`E_R`) — capturing precisely the earlier informal
diagnosis in all three approach files ("fragments of P dominate the tail") as a hard number.

**Why this is a promising opening (not yet a full proof):**
- It converts the vague "coupling" language of GAP L / SL into an *exact recursive value
  formula* usable step by step in a strong induction — no coupling MAP or shadow game needed;
  a real strong induction can literally recompute `D` after each Xiang cut via this identity.
- Because `R` at the moment of the *first* cut on the top piece is the exact, known, UNCUT
  dyadic-(n-1) tail `{2^{n-1},...,1}`, `O_R` (hence `E_R`) is explicitly computable in closed
  form (it is the alternating band structure already used to compute the uncut values
  `D_m = (2^{m+1}+(-1)^m)/3`), so `μ(E_R ∩ [0,p2))` is an explicit piecewise-linear function of
  `p2` — a genuinely tractable object, not an abstract coupling.
- Caveat / what remains: this identity gives `D` right *after Xiang's first cut*, when
  `R` is still untouched; Xiang has `n-1` more cuts to spend on the residual `{p1,p2}∪R`, and
  those further cuts are NOT covered by a single application of the identity — they require
  either (a) reapplying the same identity recursively at each subsequent cut (turning the whole
  problem into an exact but branching recursion — feasible as a strong-induction skeleton, since
  each cut always targets *some* current max piece relative to *some* current rest, and the
  identity applies whenever the cut is on the current global max), or (b) bounding the *worst
  case* over all continuations using this identity as the base step plus the induction
  hypothesis (LB(n-1)) applied *after* algebraically accounting for the cross term
  `μ(O_R∩[0,p2))`. I did not attempt to close this — that is proof-outliner/builder work — but
  the reduction is now much sharper than "prove a coupling map exists."

### Distinct openings
1. **Exact toggle-identity strong induction (NEW, this round).** Use the identity above as the
   engine of an induction on `n`: after Xiang's cut on the top piece (`p2` chosen by Xiang), the
   value is `D_C − 2μ(E_R∩[0,p2))` with `R` the *known* uncut dyadic-(n-1) tail; then bound the
   remaining `n-1` cuts' effect on the residual `{p1,p2}∪R` — possibly by re-deriving a second
   application of the SAME identity (now with a different dominant piece, e.g. `p1` if
   `p1 > max(R)` still holds) or by falling back to LB(n-1) once the residual is shown to
   dominate a genuine order-(n-1) instance. This is the most concrete, checkable new lead.
2. **Direct measure-toggle "cost accounting" (as posed by the dispatch).** Assessed: the naive
   version ("Xiang's cut can erase at most its own fragment's odd-measure") is TRUE but not by
   itself sufficient — the identity above shows the erasure is exactly `2μ(E_R∩[0,p2)) ≤ 2p2`,
   matching Lemma T's generic bound, but the *equality* form (not just the inequality) is what
   makes progress possible, since `μ(E_R∩[0,p2))` is computable from the known dyadic structure
   of `R`, not just crudely bounded by `p2`.
3. **Strong induction (peel the top scale) vs. coupling map.** The exact identity strongly
   favors strong induction over a coupling map: a coupling map needs to be *constructed and its
   monotonicity proven* (an existence argument), whereas the identity is already an equality —
   no construction needed, only algebra to propagate it through the recursion. Recommend the
   outliner prioritize induction-peel / the SL framing (two-box-balancing) over
   parity-measure-potential's dual "D(S_L) ≤ f₁−1" framing for closing this specific gap, though
   note (§GAP L1 in parity-measure-potential) that inequality IS an instance of the same
   identity: `D(S)=f₁−D(S_L)` is the `p2→0` degenerate case of the general dominant-piece
   identity above (`R` there is `S_L`, `p` is `f₁`).
4. **Piece-count / cut-budget monotonicity (cheap-kill, confirms round-2 finding).** Spending
   `k≥2` cuts fragmenting the top piece before touching the tail leaves only `n-k` cuts for the
   tail, and by monotonicity of `L(n-1)` in budget (fewer cuts ⇒ weakly larger minimum `D`),
   this is never advantageous for Xiang relative to spending exactly 1 cut on top — verified
   numerically this round (forced-2-cuts-on-top search matches free search, does not go below
   `D=1`). This suggests the outliner can restrict attention to "Xiang spends exactly one cut on
   the top piece" (the SL framing already does this) as WLOG optimal, though a fully rigorous
   monotonicity lemma (`L` is non-increasing in budget) should be stated and proved — it looks
   easy (a strategy with fewer cuts is a restriction of one with more) and is probably already
   implicit but not explicitly certified as a lemma; worth promoting.

### Candidate technique(s)
The exact dominant-piece toggle identity (opening 1/2) is the standout candidate — it is
provable algebra (verified numerically + symbolically), not an existence claim, and directly
operationalizes "cutting a scale costs that scale." Combine with strong induction (opening 3)
and the cut-budget monotonicity cheap-kill (opening 4) to justify restricting to the
single-top-cut case before invoking the identity.

### Cheap-kill candidates
- Cut-budget monotonicity (`L(n-1, budget=b)` non-increasing... i.e. non-decreasing as budget
  decreases): reduces "how many cuts Xiang spends on the top piece" analysis to `=1` WLOG.
  Should be stated as an explicit lemma (looks straightforward: a `k`-cut strategy on a
  `b`-budget game is also a valid strategy for a `b'≥b` budget game by wasting extra cuts as
  no-ops — wait, actually the direction needed is: MORE budget can only help Xiang (weakly lower
  D_min), i.e. `L` is non-increasing in budget. This is immediate: Xiang can always ignore extra
  cuts. So `L(residual, n-1-extra) ≥ L(residual, n-1)`, formalizing why over-cutting the top is
  never better.) Recommend certifying this as a one-line promotable lemma.
- Piece-count parity (from round 2, opening 3 there): `D=0` needs even total piece count;
  cheap sanity filter, not a closer.

### Knowledge-base entries to use
No problem-specific dyadic-game KB entry exists; the reusable machinery is the
approach-agnostic certified lemmas already in `lemmas/` (R, M/I+T, P). The new dominant-piece
identity above is a natural candidate for `lemmas/dominant-cut-identity.md` if the outliner
adopts it (it generalizes and sharpens both `parity-measure-potential`'s `(LB-id)` and
`two-box-balancing`'s SL Case A/perfect-bisection computations into one closed-form tool).

### Analogous past problems (cruxes)
Reaffirming round 2's findings (I did not re-run the corpus query fresh this round, since
round 2's `math-explorer-lower-coupling.md` already did a careful subtopic-filtered search of
`games-and-strategy` / `invariants-and-monovariants` / `processes-and-algorithms` and found no
exact match, only technique-shape analogues):
- **aimo-0019** — amortized potential / resource-accounting induction (paint-game, dyadic
  intervals). Best match for framing the exact-identity-driven induction (opening 1) as an
  amortized argument if the single-step identity needs to be chained across multiple cuts.
- **aimo-0663** — one-directional coupling/shadow-game inequality. Less essential now that an
  EXACT identity (not just an inequality) is available for the first cut; still relevant if the
  chaining across further cuts ends up needing an inequality rather than exact recursion.
- No corpus problem literally matches "alternating-sum-of-sorted-parts with a cut budget."

### Prior progress
See `current.md`, `induction-peel.md` (§3 Case (b), GAP L), `parity-measure-potential.md`
(§LOWER BOUND, GAP L1/L2), `two-box-balancing.md` (§2, Sub-lemma SL, GAP L). All three
independently isolate the identical obstruction. This round's contribution is the exact
closed-form identity that operationalizes it — a genuinely new tool, not previously in any
approach file or in `lemmas/`.

### Dead ends (do not retry)
- Naive strengthening of the "superincreasing" induction hypothesis to survive an arbitrary top
  cut (round 2 finding, reconfirmed not revisited this round but no new evidence against it):
  bisection produces a residual that is not superincreasing relative to the tail; do not
  re-attempt this exact IH strengthening.
- "1 cut kills 1 dyadic band" naive pigeonhole (round 2): false, a cut's toggle set spans
  multiple bands. The new exact identity supersedes this — it correctly accounts for
  multi-band toggle effects via `μ(E_R∩[0,p2))` rather than a per-band count.

### Small-case / intuition notes (conjectural / numerical, confirmed this round)
- Re-verified (independent random-cut search, n=1..4): minimax `D` on the dyadic input is
  exactly `1` (in integer units), matching `u_n`, and the extremal Xiang strategy set is flat
  (many first-cut fractions on the top piece all lead to eventual `D=1`), consistent with round
  2's finding — favors the exact-identity/induction route (opening 1) over trying to
  characterize a unique optimal line.
- New: verified the exact toggle identity `D_new = D_C − 2μ(E_R∩[0,p2))` numerically (35
  trials, `n=2,3,4`, random cut fractions) and symbolically (sympy, 2-element tail case) — this
  is the most load-bearing new fact from this exploration and should be handed to the outliner
  as a candidate lemma, not merely a heuristic.
- Numerically re-confirmed (forced 2-cuts-on-top vs 1-cut-then-free vs free search, n=3):
  spending extra cuts fragmenting the top piece never beats spending exactly one, consistent
  with the cut-budget monotonicity cheap-kill (opening 4).
