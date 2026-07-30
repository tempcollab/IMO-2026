## imo-2026-03 — lens: the UPPER-BOUND wall (GAP U), all three approaches

### 0. Restating GAP U precisely, and checking the three framings agree
All three approaches (`parity-measure-potential` GAP U, `induction-peel` GAP U, `two-box-balancing`
GAP U) reduce the upper bound to the **same** claim, via the certified Lemmas R/M/T/P:

> For every sorted profile `a_1 ≥ … ≥ a_{n+1} ≥ 0`, `Σ = L`, with Xiang holding exactly `n`
> cuts (the **full-budget** case — `two-box-balancing`'s Lemma U0 disposes of `m ≤ n` for free,
> forcing `D = 0`), Xiang can choose a nonempty subset `T ⊆ {a_2,…,a_{n+1}}` (or split `a_1` into
> several targeted values, possibly matched partially) using `|T|=j` cuts so that after deleting
> the `j` cancelling pairs (Lemma P) the residual `(n+1-j)`-piece multiset of total `L-2Σ_T`, fed
> to Xiang's remaining `n-j` cuts, has value `≤ u_{n-j}(L-2Σ_T) ≤ u_nL`; equivalently
> `Σ_T ∈ [Lθ_j, a_1]`, `θ_j = u_n·2^{n-j}(2^j-1)` increasing in `j`.

This is **literally the same statement** in all three files — `parity-measure-potential` calls it
the "subset-cover feasibility" disjunction, `induction-peel` calls it the "balanced case /
early-stopping potential," `two-box-balancing` calls it "adaptive subset-match, m=n+1." Verified
they use the identical threshold arithmetic (`1-u_n/u_{n-j} = 2^{n-j+1}(2^j-1)u_n`). So there is
**no framing disagreement** to exploit here — the three approaches have already converged onto one
shared combinatorial core, which is the correct diagnosis of why it's stuck.

**New structural observation (not stated explicitly in any file): GAP U is self-similar/closed.**
A `j`-pair peel of a full-budget profile (`n+1` pieces, budget `n`) always lands in *another*
full-budget profile: `(n+1-j)` pieces with budget `(n-j)` satisfies `(n+1-j) = (n-j)+1` exactly.
So the induction never needs to leave the full-budget family (Lemma U0 handles the `m≤n`
boundary once and for all, and the `m=n+1` recursion only recurses into smaller `m=k+1`
instances). This means GAP U is *literally* a clean self-contained strong induction — worth
telling the outliner explicitly since none of the three files states the closure property.

### 1. Distinct openings

**(A) The subset-cover feasibility disjunction itself (currently pursued in all 3 files).**
Prove: for every full-budget profile, either `a_1 ≥ Lc(n)` (bisect, closes trivially) or there
exists `T` with `Σ_T ∈ [Lθ_{|T|}, a_1]`. This is a genuine knapsack/subset-sum-flavored covering
claim. It is *not yet reduced to a clean pigeonhole* by any approach — the difficulty is that
`θ_j` **increases** in `j` (harder to satisfy sum lower bound as you take more pieces), while
`Σ_T ≤ a_1` **caps** what's achievable, so there's a genuine max-over-`j`-of-(achievable-`Σ_T`)
vs-θ_j race. A clean argument would take, for each `j`, the top-`j` tail elements (`a_2,…,a_{j+1}`)
— the sum-maximizing choice of size `j` subject to `Σ ≤ a_1` isn't simply "the `j` largest" if
that overshoots `a_1`; the real greedy is "fill until you'd exceed `a_1`," i.e. **for the specific
`j*` where the greedy-fill first fits (from the `(4.3)`-style analysis in `induction-peel`),
check the resulting `r` against `θ_{j*}`.** No approach has verified this greedy-`j*` disjunction
is always sufficient in closed form — only spot-checked on 1–2 numeric examples per approach.

**(B) Majorization/smoothing: is dyadic the pointwise-worst Liu profile for `V(A) = min_Xiang D`?**
This is the "lp-dual-weight smoothing half" asked about. **I ran a fresh, independent numeric
check** (own code, not reused from round 2): for `n=2` (3 pieces, budget 2 cuts), an inner solver
that enumerates all ways to distribute 2 cuts among the 3 pieces, then for each allocation does
random+coordinate-descent refinement of the cut points to (approximately) globally minimize
`D` — i.e. an actual bilevel `max_A min_Xiang D` search, not just spot checks:
- On 13 structured test profiles (dyadic, the two live approaches' counterexamples, several
  skewed and near-uniform profiles): **the dyadic profile `(4/7,2/7,1/7)` is the unique one
  attaining `V = u_2 = 1/7` exactly; every other tested profile gives `V` strictly less**
  (e.g. `(0.5,0.28,0.22)→V≈0`, `(0.6,0.25,0.15)→V=0.1`, `(0.99,.005,.005)→V≈0`).
- A further random search over 60 Dirichlet-sampled 3-piece profiles found **zero violations**
  (max observed `V ≈ 0.119 < u_2 = 0.1429`, at a profile close in shape to dyadic).
This is **strong (but still only numeric/conjectural) evidence** that dyadic uniquely maximizes
`V(A)` over the full-budget simplex — consistent with round-2's independent (partial, timed-out)
bilevel search. **If provable**, a smoothing/exchange lemma ("perturbing any profile toward the
2:1 dyadic ratio pattern cannot decrease `V`") would close GAP U in one shot, replacing the whole
per-profile subset-cover casework. **Risk (unchanged from round 2's assessment, now with more
confidence in the premise but not the mechanism):** proving monotonicity of a minimax value under
adversary perturbation needs either (i) an explicit coupling of Xiang's optimal strategies before/
after the perturbation, or (ii) recasting `V` as an LP/game value with an envelope-theorem
argument. Nobody has produced this coupling yet — it is a **new** opening, not a continuation of
either dead branch.

**(C) Direct potential/monovariant on the toggle calculus (Lemma T), independent of subset-cover.**
Since `D_final = μ(O_0 △ ⊕E_i)` (certified Lemma T), an alternative to constructing an explicit
strategy is to exhibit a potential `Φ` on (current multiset, cuts remaining) such that (i)
`Φ(A, n) ≥ u_nL` is forced to be *achievable* by Xiang moves that decrease `Φ` monotonically
toward `u_nL` regardless of Liu's initial `A`, in the `⊕`-algebra directly (GF(2)-flavored). Not
developed by any approach; flagged in round-2 as opening 2, still open, no numeric progress this
round. Genuinely distinct from (A)/(B) in that it works in the "symmetric-difference of intervals"
language rather than the "sorted multiset + cancelling pairs" language.

**(D) Attack GAP U1 specifically (the dominant-but-`a_1>c(n)` cut-budget snag).** I rechecked the
arithmetic independently: bisecting `a_1` (1 cut) then deleting the equal pair by Lemma P leaves
`{a_2,…,a_{n+1}}` — **still `n` pieces** (nothing was removed from the tail) — with `n-1` cuts
remaining. Lemma U0 needs `m ≤ (budget)`, i.e. `n ≤ n-1`, which **fails by exactly one**. This
confirms (independently) the `two-box-balancing` file's own diagnosis — not a new finding, but I
verified it is not an off-by-one bookkeeping slip that a smarter cut order fixes: bisecting `a_1`
truly cannot both (a) create the cancelling pair for free structurally and (b) leave enough budget
for U0 on `n` residual pieces. So GAP U1 is real, and (as both `induction-peel` and
`two-box-balancing` note) is *subsumed* by the general subset-cover feasibility question (A) —
it is not an independent easier sub-case with its own shortcut; do not spend a separate round on
it in isolation.

### 2. Cheap-kill candidates
- **None found this round for a full kill.** Checked: parity/pigeonhole on subset count (`2^n`
  subsets of the tail vs. `n` thresholds `θ_j`) does not obviously force existence — the
  obstruction is a genuine sum-magnitude condition, not a counting one.
- **A useful reduction, not a kill:** by continuity of `D` in the piece lengths (Lemma M/I), the
  sup over Liu profiles of `V(A)` is attained in the closure, so WLOG-perturbation arguments
  (generic ratios, no coincidental exact subset-sum ties) are legitimate if the outliner wants to
  avoid boundary casework — flagged already by round-2, reconfirmed relevant here.

### 3. Knowledge-base entries to use
- **Invariants & monovariants** (combinatorics section) — for opening (C).
- **Extremal principle / exchange-smoothing arguments** — for opening (B); this is the same
  technique class as the crux `aimo-0146` below.
- **Hall's marriage theorem / SDR**, **Prouhet–Tarry–Escott / power-sum matching** — for
  formalizing opening (A)'s "does a feasible `T` always exist" as a covering/matching claim
  (already flagged by round-2; still the best KB fit for (A)).

### 4. Analogous past problems (cruxes) — new since round-2's scan
Filtered `combinatorics`+`algebra` for `extremal-principle` / `invariants-and-monovariants` with
keyword `smooth`/`majoriz`/`exchange` in `how_used` (round-2 only scanned `games-and-strategy`):
- **`aimo-0146`** (combinatorics, `extremal-principle` / `double-counting` /
  `invariants-and-monovariants`) — crux: *"Maximize a fixed weighted sum of a sorted nonnegative
  sequence under a sum constraint by exchange-smoothing weight toward the higher-coefficient
  positions until the free coordinates equalize and the tail drains, then enumerate the few
  surviving extremal profiles."* This is a **strong structural analogue for opening (B)**: our
  `D = Σ(-1)^{i+1}b_i` on the sorted final multiset is exactly a weighted sum of a sorted
  sequence with alternating ±1 weights under a fixed-sum constraint — the same shape `aimo-0146`
  smooths. The catch: in our problem the "sequence" being smoothed (the final multiset) is itself
  the outcome of an adversarial optimization (Xiang's response), not directly Liu's choice, so
  the smoothing has to be proven to survive taking the `min` over Xiang — `aimo-0146`'s argument
  doesn't have this extra minimax layer. Worth reading `past_problems_database.json` entry for
  `aimo-0146` for the exact mechanics of "smooth until equalized, then hand-check finitely many
  profiles" — that finite-profile endgame may be reusable once/if the smoothing direction is
  established here.
- **`aimo-0988`** (algebra, `inequalities-SOS-and-convexity`) — *"reduce a mean-of-n inequality
  to iterated two-variable smoothing... a balanced pairwise tournament telescopes."* Weaker
  analogy (pure algebra, no adversary), but the "iterated pairwise smoothing telescopes to a
  balanced/extremal profile" pattern is the generic shape opening (B) would need, so worth a
  glance for the telescoping bookkeeping technique.
- Reconfirm round-2's finding: **`aimo-0117`** (dyadic/superincreasing shape, already used for
  the lower bound) and **`aimo-0560`** ("replace the adversary with a pointwise-stronger
  surrogate") remain the best fits for opening (B)'s *mechanism*, not just its target profile —
  `aimo-0560` is precisely the "transfer a win against a surrogate down to all inputs" pattern
  opening (B) needs, i.e. treat dyadic as the surrogate for Liu, and show any actual Liu profile
  is pointwise weaker (Xiang does at least as well against it). No approach has yet attempted to
  adapt `aimo-0560`'s technical machinery (worth the outliner reading the full solution).
- No new corpus entry solves the exact "adaptive-cut minimax on a sorted alternating sum" shape;
  confirms round-2's conclusion that this problem has no close structural twin in the sampled
  corpus and the field must construct its own argument.

### 5. Prior progress (unchanged from current.md, restated for this lens)
Both bounds reduce to GAP U (upper) and GAP L (lower) via certified Lemmas R, M/I, T, P. Upper
bound is fully closed for: `m ≤ n` (Lemma U0, `D=0`); dominant `L/2 ≤ a_1 ≤ Lc(n)` (replicate-all,
`D=2a_1-L ≤ u_nL`, §4A of `induction-peel`, closed and tight at the dyadic boundary point). Open:
GAP U = balanced (`a_1<L/2`) **and** dominant-but-`a_1>Lc(n)` (GAP U1, shown above to be a special
case, not separately tractable). The single-cancelling-pair / greedy-match strategies are proven
(by counterexample, `n≥2`/`n≥3`) insufficient.

### 6. Dead ends (do not retry)
- **Greedy-match (top two only)** and **single cancelling-pair peel with threshold
  `max(a_1,2a_2)≥Lc(n)`** — proven insufficient by explicit counterexample at `n=2`
  (`(0.5,0.28,0.22)`) and shown (round-2) to leave large slack on the table (true minimax there is
  `≈0`, not merely "close to failing").
- **Bisect-`a_1`-then-invoke-Lemma-U0 for the `a_1>c(n)` dominant sub-case** — re-verified this
  round: fails the cut-count check by exactly one (`n` residual pieces vs. `n-1` residual budget).
  Not an independent gap; subsumed by (A).

### 7. Small-case / intuition notes (all conjectural; numeric evidence only)
- **Dyadic is (numerically, `n=2`) the unique global maximizer of `V(A)` among full-budget
  profiles**, attaining `V = u_n` exactly; every other tested and randomly-sampled profile gives
  strictly smaller `V`. This is new independent confirmation (own bilevel search, 13 structured +
  60 random profiles, zero violations) of round-2's partial finding — raises confidence in
  opening (B)'s premise, though the *mechanism* (a provable smoothing/exchange lemma) is still
  completely open.
- The subset-cover disjunction (A) succeeds on every hand-checked balanced example so far
  (`(0.5,0.28,0.22)` at `j=2`, matches the tail-sum exactly at the boundary `Σ_T=a_1`) — but no
  approach has produced a profile-independent proof that the greedy-fill `j*` always clears
  `θ_{j*}`; this remains the crux of opening (A) and is not yet reduced to a clean pigeonhole.
