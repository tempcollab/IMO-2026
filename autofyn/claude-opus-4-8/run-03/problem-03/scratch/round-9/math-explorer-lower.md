## imo-2026-03 (LOWER-WALL lens: aggregate ballot/cycle-lemma inequalities on ladder walks)

### Target recap
GAP MID-core / equivalently (Lemma OSR, certified): for admissible `a=0` refinement `S=F⊔B`
(`ΣF=2^n`, `ΣB=2^n−1`, `|F|≥3`), merge descending `v_1>…>v_m`, signs `e_i=+1` (F) / `−1` (B),
`S_k=Σ_{i≤k}e_i`. Need `Σ_{B odd rank}v_i ≥ Σ_{F even rank}v_i`, equivalently `D(S)≥1`. Certified
closed: `|F|=2`, and the one-sided walk cap `S_k≤1 ∀k` (Lemma OSR-cap, Abel summation with
`P_k=1[k odd]−S_k ≥0`). Residual: `max_k S_k≥2`, `|F|≥3`. Certified negative fact F1: the
INDEX-level prefix form fails on ~27% of refinements — no running monovariant on the merge order
works.

### Distinct openings surfaced this round
1. **(live, parity-measure) Dyadic Lemma-ONE recursion / aggregate compensation.** Still the
   primary lever assigned. Not closed; see new negative result below narrowing where it can live.
2. **(live, ballot-matching) Hall/transport certificate.** Recasts `Σc_iw_i≥0` as debit(overshoot)
   → credit(deficit) transport with a Hall feasibility condition keyed on dyadic scale (using
   Lemma ONE recursed to bound "≤1 F-fragment per scale-excursion"). Genuinely different mechanism
   (static feasibility certificate, no induction on `n`). GAP-HALL and GAP-TERMINAL both open.
3. **(live, merge-interleave-pattern) Reachable-word / extremal-vertex framing.** `D(S)=L_w(values)`
   linear in values for fixed interleaving word `w`; claims the minimum over the *reachable* word
   family sits at the canonical one-per-gap interleaving (telescoping value exactly 1). GAP-REACH
   (characterize reachable words from the ladder + budget) and GAP-EXTR (min is at that vertex) both
   open — this is an LP-vertex-style argument, distinct in kind from both 1 and 2.
4. **(new, this round — worth flagging) Double-counting/degree-bound certification of Hall's
   condition, rather than a general marriage argument.** See "Candidate technique" below — this
   is the concrete mechanism the corpus suggests for closing GAP-HALL specifically (ballot-matching's
   own writeup currently states GAP-HALL only as "the open content," with no concrete route to
   *verify* the Hall condition; the corpus pattern below is a plausible route).
5. **(new, scouted and REFUTED this round) Per-dyadic-gap localized compensation.** I tested
   whether the aggregate inequality already holds *locally within each dyadic gap* of `C_{n-1}`
   (i.e. `μ{g odd}` restricted to `(t_{k+1},t_k)` ≥ `∫g` restricted to the same gap, for every
   `k`) — a natural "coarser than index-prefix, finer than global" refinement that, if true, would
   let an inductive scale-by-scale argument close MID-core gap-by-gap without any cross-scale
   transport. **It is FALSE**: numerically, local (per-gap) violations occur in 20%–75% of sampled
   admissible refinements (rising with `n`; see Small-case notes), even though the GLOBAL
   inequality held with zero violations across all trials. So compensation is not just
   non-index-prefix-monotone (F1) but also non-scale-local: a debit incurred in one dyadic gap can
   be repaid by credit in a *different, non-adjacent* gap. This further narrows what kind of
   argument can work: it must be a genuinely global (whole-ladder) accounting, ruling out any
   "prove it gap-by-gap by induction on scale" plan, not just "prove it index-by-index."

### Cheap-kill candidates
- **DONE (this round): per-dyadic-gap local compensation — REFUTED** (see above; explicit
  numeric witness families exist at every `n=3..6` tested, use `python3` script pattern:
  generate `a=0` refinements with `|F|∈[3,n]`, cut tail `C_{n-1}` with `≤ n-|F|+1` extra cuts,
  compute `∫g` and `μ{g odd}` restricted to each gap `(2^{n-1-k},2^{n-2-k})` separately).
- Untested but cheap: check the SUFFIX (bottom-up, ascending-from-0) Abel form as an alternative
  monovariant, i.e. define `Q_k = Σ_{i>k} d_i` (coefficient sum "at or below" index k) and ask
  whether `Q_k≤0` always — this is NOT symmetric to `P_k≥0` since the `v_i` are not equally spaced
  and `Σd_i=P_m≤0` (Fact F2) makes the endpoint favorable; worth a quick numeric sweep before the
  builder invests, but note it inherits the same F1-style risk (a "credit early, debit late" bad
  case would violate it) — flag as a 10-minute check, not yet run.
- Fact F2 (certified, `S_m=|F|−|B|≤0`, i.e. more B than F in count) plus the *value*-scale
  asymmetry (`ΣB=2^n−1 > ΣF=2^n`... actually `ΣF>ΣB` by exactly 1) together pin the "just barely"
  nature of the inequality — any argument must use both the count deficit (`S_m≤0`, terminal
  descent) and the mass surplus (`∫g=1`) simultaneously; neither alone suffices (both were tried
  and are individually insufficient, per F2's own "necessary not sufficient" note).

### Candidate technique(s) — Hall's condition via bounded-degree double-counting
The corpus (see below) shows a recurring, concrete pattern for *proving* a Hall-type marriage
condition in an extremal combinatorics setting: instead of a general Hall/deficiency argument,
show the relevant bipartite graph is **regular or degree-bounded** and invoke the trivial
sufficient condition "if every debit-vertex has degree `≤ d` and every credit-vertex absorbs
`≥ d`-worth of debit-edges, Hall holds automatically" (aimo-0197's `3`-regular argument; aimo-0129's
degree-comparison via longest-length sticks). For GAP-HALL, this suggests: instead of proving Hall's
condition in general, show that **Lemma ONE recursed gives a hard degree bound** — e.g. "each
debit unit created at scale `2^{n-1-k}` can be charged to at most one specific later credit unit at
scale `2^{n-2-k}` (or coarser), and each credit unit absorbs at most a bounded number of debit
units" — turning GAP-HALL into a concrete counting statement rather than a general
marriage-theorem invocation. This is a genuinely new, corpus-suggested angle to hand the
ballot-matching builder (it does not remove the need to define the transport correctly, but gives a
template for how to *certify* feasibility once defined).

### Knowledge-base entries to use
Certified lemmas (import, don't re-prove): `reduction-odd-rank` (Lemma R), `measure-identity`
(Lemma M), `cancelling-pair` (Lemma P), `split-cross-term` (SPLIT), `top-scale-dichotomy` (Lemma
ONE), `mass-difference-reduction` (MID), `order-statistic-reformulation` (OSR),
`one-sided-walk-cap` (OSR-cap). `knowledge_base.md` itself — I did not find a named
general-purpose "ballot problem" or "cycle lemma" entry there generic enough to cite directly (the
combinatorial content here is bespoke to the dyadic-ladder structure); the general Hall's-theorem /
double-counting entries (if present in `knowledge_base.md`) are the right generic citation for the
GAP-HALL route — cite whichever KB entry names Hall's marriage theorem / bipartite matching, if one
exists (check `knowledge_base.md` directly for exact title before the builder cites it).

### Analogous past problems (cruxes)
- **aimo-0003** (`combinatorics/invariants-and-monovariants`) — genuinely related MECHANISM (not
  statement): a chord-inversion count is shown to equal `−(min value of a ±1 walk around a
  circle)`, proved by induction that deletes an "innermost matched pair" (a stable chord) and
  checks the walk-min changes by exactly the right amount. This is structurally the closest
  analogue to our `Σc_iw_i` ballot walk, but note our own Lemma P (`cancelling-pair`) is *already*
  this same "delete an innermost/cancelling matched pair" move — so this crux mainly *confirms*
  the field is using the right primitive move, it does not supply a new lever for the aggregate
  (non-prefix) part of the inequality specifically.
- **aimo-0129** and **aimo-0197** (`combinatorics/graph-theory-and-connectivity`) — both certify a
  Hall marriage condition via a **bounded/regular-degree double-counting** argument rather than a
  general deficiency argument. Best transferable technique for ballot-matching's GAP-HALL (see
  "Candidate technique" above); not a statement-analogue, a proof-technique analogue.
- **aimo-0298** (IMO scales, dyadic weight `w(S)=Σ2^{-r_S(x)}≤1`, minimal-gap-merge induction) —
  ALREADY TRIED and REFUTED as a lever for this exact gap (round 7, split-and-average monovariant
  fails ~28-45% of budget-enforced refinements; recorded dead end). Do not re-attempt in this form.
- No crux found that is a direct statement-analogue of "integer step function with fixed integral
  on a ladder has odd-parity-measure ≥ integral" — this really does look bespoke to the problem's
  dyadic/superincreasing structure, consistent with prior rounds' findings.

### Prior progress
See `results/imo-2026-03/current.md` / `approaches/parity-measure-potential.md` R8 section: Lemma
OSR + OSR-cap certified, sub-case `S_k≤1` closed, negative Fact F1 (prefix fails 27%) and F2
(`S_m≤0`, necessary-not-sufficient) established. `ballot-matching.md` and `merge-interleave-
pattern.md` both registered as skeletons (unsolved), sharing the same target with different
mechanisms, per the outliner's diversity mandate.

### Dead ends (do not retry)
- Prefix/running-deficit monovariant on the merge-order index (`P_k≥0` outside the `S_k≤1`
  sub-case) — RIGOROUSLY REFUTED, F1: fails on ~27% of admissible refinements (round 8, re-verified
  as still the load-bearing negative fact this round).
- Per-dyadic-gap LOCAL compensation (`μ{g odd}` ≥ `∫g` restricted to each individual gap
  separately) — NEWLY REFUTED THIS ROUND (20%–75% violation rate across `n=3..6`, worsening with
  `n`). Complements F1: rules out both an index-local AND a scale-local inductive/telescoping
  argument; only a genuinely whole-ladder (global) accounting can work.
- Pure-integral statement (`g` integer, `∫g=1` alone `⇒ μ{g odd}≥1`) — FALSE, `g≡2` on measure
  `1/2` counterexample (round 7, Lemma MID writeup).
- Per-gap single-O_B-interval invariant — REFUTED with explicit witness (round 7).
- aimo-0298 split-and-average monovariant — REFUTED (round 7, induction-peel).

### Small-case / intuition notes (all labeled conjecture/numeric, not proof)
- Global MID-core inequality (`D(S)≥1`) verified with **zero violations** across ~9,700 freshly
  generated budget-respecting `a=0` refinements this round (`n=3,4,5,6`, `|F|∈[3,n]`), consistent
  with all prior rounds' much larger samples (30000+). Strong conjectural confidence the statement
  is true; the difficulty is purely in finding the *proof mechanism*, not in the truth of the claim.
- The newly-tested per-gap-local violation rate GROWS with `n` (≈20% at `n=3` up to ≈75% at
  `n=6` in my sample), suggesting the "compensation distance" (how far across scales a debit's
  repaying credit can sit) grows with the ladder depth — consistent with why a naive scale-by-scale
  induction (mirroring the already-refuted `n`-induction attempts) keeps failing: the ladder's
  bottom scales can carry credit that repays debit incurred arbitrarily far up top, and vice versa.
  This is evidence (not proof) that any working argument needs a genuinely global potential/telescoping
  object over the WHOLE walk (matching the outliner's original mandate), and that neither
  index-local nor scale-local windows will suffice — the transport in ballot-matching's GAP-HALL,
  if it is to work, likely needs long-range (not nearest-scale) edges in its bipartite graph, which
  makes the "bounded local degree" Hall-certification pattern (aimo-0129/aimo-0197 style) harder to
  apply directly and may itself need adaptation (e.g. bound total degree summed over an entire
  suffix of scales, not per-scale).
