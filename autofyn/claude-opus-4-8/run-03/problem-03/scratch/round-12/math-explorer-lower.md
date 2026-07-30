## imo-2026-03 (LOWER wall scouting — genuinely new global mechanisms for MID-core)

### Setup recap (all certified, not re-derived here)
Work in units of `u`. Liu plays `C_n={1,2,...,2^n}`; residual case is a=0 (top piece `2^n`
shredded into `F` with `|F|≥2`, `ΣF=2^n`, each `≤2^{n-1}`), `B` any `≤(n-1)`-cut refinement of
the tail `C_{n-1}={1,...,2^{n-1}}` (`ΣB=2^n-1`, each `≤2^{n-1}`). `g=N_F-N_B` on `(0,2^{n-1})`.
`D(S)=μ{g odd}`, `∫g=1` (Lemma MID). MID-core: `μ{g odd}≥1` for `|F|≥3` (`|F|=2` and `0≤g≤1`
already closed). Equivalent CLIP `τ=0` face: `Σ_{F even rank}v ≤ Σ_{B odd rank}v`. Three families
DEAD per Rules: additive scalar potential, structured transport/Hall matching, termwise/prefix
monovariant.

---

### Framing (i): aggregate ballot/cycle-lemma on the reachable word (via ONE-REC recursion)

**What it is.** Read the descending merge of `F∪B` as a word `w∈{F,B}^m`; steps `e_i=±1`
(`+1` at F-rank), partial sums `S_i`, gap-lengths `w_i`. Certified: `D(S)=Σ_{i odd}w_i`,
`∫g=Σ_iS_iw_i=1`, and MID-core `⟺ Σ_ic_iw_i≥0`, `c_i=1[i odd]-S_i` (every `c_i` an even integer).
This is EXACTLY the `merge-interleave-pattern` slug's GAP-EXTR target and the `ballot-matching`
slug's residual (already registered, both still open — this is not a new object, it is the
existing residual re-approached). `Lemma ONE-REC` gives the reachability constraint: at each
dyadic scale `2^j` of `B`'s ladder, at most one fragment exceeds `2^{j-1}` (per-scale single
excursion) — this restricts which `(w, values)` are actually reachable from a genuine `C_n`
refinement, i.e. it constrains the vertex set of the feasible polytope, not the values directly.

**The genuinely new sub-idea to scout:** rather than trying to prove `Σc_iw_i≥0` by a *transport*
(refuted R11) or a *scalar running potential* (refuted R10), treat it as an LP: for FIXED reachable
word `w` (fixed sign pattern/rank-interleaving), `Σc_iw_i` is linear in the gap-lengths `w_i`, so
its minimum over the reachable-value polytope (cut-budget + ladder constraints) sits at a VERTEX.
`Lemma ONE-REC` + the cut-budget inequality `(|F|-1)+c_B≤n-1` cut out that polytope. If the vertex
set can be shown to coincide with the "canonical one-fragment-per-gap" telescoping layouts (which
are already PROVED, via `L2-telescope`, to give exactly `D(S)=1`), MID-core follows by a
finite-vertex argument — literally the SAME vertex-enumeration mechanism `breakpoint-vertex`
already uses for the UPPER wall (`Theorem VERT`, LP-vertex/hyperplane-arrangement rank argument,
reviewer-confirmed profile-independent there).

**Hard step.** Proving the vertex-characterization for the LOWER polytope (call it GAP-EXTR): that
every vertex of {reachable `(w,\text{values})` obeying ONE-REC + budget} is a canonical
one-fragment-per-gap interleave. This is NOT yet attempted with the LP-vertex machinery
specifically — prior attempts (ballot-matching) treated it as a *matching/transport* problem
(refuted), not an LP-vertex/finite-basis problem. It is a genuinely different technique from what
was refuted, but it is dangerously close in flavor to the already-open `GAP-REACH`/`GAP-EXTR` pair
in `merge-interleave-pattern.md` — an outliner picking this up should explicitly frame it as
"import breakpoint-vertex's Theorem-VERT machinery onto the lower polytope," not reinvent it, to
avoid duplicating registered-but-unclosed content.

**Refutation risk.** If the reachable-word polytope's vertex set is NOT confined to canonical
interleaves (i.e. some vertex has a "clumped" `F`-excursion violating the telescoping pattern),
this dies exactly like HALL-ENDPOINT did (credit/debit spread to non-adjacent scales). Should be
spot-checked on a small n (LP vertex enumeration via `scipy`/`cvxpy` on the actual finite
cut-budget polytope for n=3,4) BEFORE committing a builder round to it.

---

### Framing (ii): F-partition majorization vs. the FIXED dyadic ladder B

**Numeric investigation this round (new, not previously in the field).** I tested directly
whether Xiang spending cut-budget on `B` (instead of purely on the top piece `F`) can ever beat
the `B`-uncut value, and where the TRUE global minimizer of `D(S)` over the full 2-parameter
`(F,B)` search sits, respecting the exact cut-budget constraint `(|F|-1)+c_B≤n-1`.

- **n=4 and n=5, joint global optimization (scipy Nelder-Mead multistart over all `(cuts_on_F,
  c_B)` splits):** the TRUE global minimum `D=1.0000` (to numerical precision) is attained ONLY
  at `c_B=0` (`B` completely uncut = `C_{n-1}`) with all budget spent on `F` (`|F|=n`,
  `n-1` cuts) — i.e. the extremal/binding configuration is exactly the canonical interleave
  already known (`L2-telescope`), confirming (not new) that the floor-attaining case has `B`
  fixed.
- **But: for a FIXED `F`, spending a cut on `B` CAN strictly lower `D(S)` below `D(F,B_\text{uncut})`.**
  Budget-respecting adversarial search at n=5: 42.8% of sampled `(F, one extra cut on B)`
  configurations give `D(F,B_\text{cut}) < D(F,B_\text{uncut})` (by up to ~15% relative). None of
  the observed cut-B configurations went below the floor `D=1`, but they DO get closer to it than
  the same `F` with `B` uncut in some cases — cutting `B` is a real, sometimes-effective adversary
  move, not a wasted one.

**Conclusion — refutation risk for framing (ii) as literally stated.** The dispatch's premise "`B`
is pinned by the tight minimiser" is TRUE only for the exact extremal point, not as a WLOG
reduction over the whole search space. A pure majorization/rearrangement argument that compares
`F`'s ordered profile against a FIXED `B=C_{n-1}` therefore proves, AT BEST, only the `c_B=0` slice
of MID-core — it does not by itself handle the (empirically real, ~40%+ of instances) configurations
where Xiang also cuts `B`. To be a complete lower-bound proof, framing (ii) needs a SECOND,
separate ingredient: a monotonicity/exchange lemma showing "cutting `B` can lower `D` but never
below the `B`-uncut floor of `1`" (an unexplored, NOT yet stated or refuted claim — call it
**GAP B-MONO**). This is a genuinely new, concrete, checkable sub-target no prior round has framed:
`∀ F` (fixed, admissible), `∀` admissible `B`-refinement, `D(F,B) ≥ \liminf` over cut allocation
`= 1` — currently ONLY verified at the joint global optimum, not for each fixed `F` individually
(my per-`F` test only checked one extra cut, not exhaustive `B`-refinements).

**Corpus check.** No majorization/Karamata/Schur-convex crux entry is a close analogue for THIS
specific two-sided (F vs B, each independently cuttable) structure. The closest partial analogue
is `aimo-0287` (algebra, `double-counting`/majorization-order subtopic; New Zealand IMO-shortlist
style "strictly increasing sequence, subset closest to half" problem) — its exchange argument
("if `k∈X, k+1∉X`, compare `δ=a_{k+1}-a_k` against a shift `Δ`; case on `δ>Δ`, `δ<Δ`, `δ=Δ`") is
structurally similar in FLAVOR to the adjacent-fragment exchange step both `parity-measure` and
`induction-peel` have already invoked and left open — it is a genuine analogue of the *local
exchange move*, not of a majorization inequality with a fixed target sequence. It does NOT supply
a ready-made majorization/Karamata theorem for comparing an ordered value-profile against a fixed
superincreasing ladder; I did not find one in the corpus (`combinatorics/inequalities-SOS-and-
convexity` and `algebra/inequalities-SOS-and-convexity` subtopics were scanned — mostly cyclic-sum
AM-GM/Cauchy-Schwarz problems, not applicable to this alternating-sign, order-statistic structure).
**No strong crux match for framing (ii); report this honestly rather than force a citation.**

---

### Comparative assessment

- **Framing (i)** is the more structurally promising lead: it reuses the ALREADY-PROVED-elsewhere
  LP-vertex mechanism (`breakpoint-vertex`'s `Theorem VERT`), applied to a different (lower-wall)
  polytope, which is a genuinely different technique from the refuted matching/potential families
  (vertex-of-a-polytope, not transport-of-mass). Its risk is that it may just re-surface the
  already-registered-but-unclosed `GAP-EXTR`/`GAP-REACH` pair without new content — the outliner
  should treat this explicitly as "attempt GAP-EXTR via LP-vertex machinery," not as a fresh slug.
- **Framing (ii)** is NOT self-sufficient as literally stated (`B` fixed) — my numeric probe shows
  the "B pinned" premise holds only at the exact extremum, and cutting `B` is a real competing
  adversary move ~40%+ of the time (though it appears never to breach the floor `D=1` in samples).
  A viable version of framing (ii) needs to be posed as a TWO-PART argument: (1) majorization of
  `F` against fixed `B=C_{n-1}` (closes the `c_B=0` slice, matches `L2-telescope`), PLUS (2) a new
  monotonicity lemma **GAP B-MONO** (cutting `B` never drives `D` below `1`) that has not been
  attempted or refuted by any prior round. GAP B-MONO is itself a clean, checkable, genuinely new
  target — smaller in scope than full MID-core and worth an explorer/builder round on its own,
  independent of whether the majorization half succeeds.

### Cheap-kill candidates before committing a builder
- For framing (i): before assigning a builder, run a small explicit LP-vertex enumeration (n=3,4)
  on the lower polytope (feasible `(w,\text{values})` under ONE-REC+budget) via `scipy.optimize`
  or exact vertex enumeration, and check whether ALL vertices are canonical interleaves. This is
  a ~30-line, cheap, decisive check (analogous to the transport-family de-risking mandated in R11)
  that should happen FIRST, before any builder writes prose.
- For framing (ii)+GAP B-MONO: the numeric evidence above (42.8% of B-cuts help but seemingly never
  below floor 1) should be extended with an exhaustive adversarial search (not just "one extra cut")
  before trusting GAP B-MONO as true — my check was not exhaustive over multi-cut B refinements.

### Dead ends (confirmed, do not retry)
- Additive scalar potential (R10), structured transport/Hall matching (R11), termwise/prefix
  monovariant (R8) — all still dead, unaffected by this round's findings.
- Naive "B is fixed WLOG" as an unproved assumption — REFUTED as a general pointwise claim this
  round (42.8% of fixed-`F` instances at n=5 have cutting `B` strictly lower `D` than `B`-uncut).
  It is only true at the joint global optimum, confirmed at n=4,5 (`D=1.0000` exactly, `c_B=0`,
  `|F|=n`, matching the already-certified `L2-telescope` construction) — this is NOT new, it just
  reconfirms the known extremal construction.

### Small-case / intuition notes (conjecture, not proof)
- Conjecture GAP B-MONO: for any admissible `F` and any two `B`-refinements `B_1 ⊆_{\text{cuts}}
  B_2` (i.e. `B_2` refines `B_1` further), `D(F,B_2)` is not bounded below `D(F,B_1)` by more than
  is needed to stay `≥1` — i.e. `\min_B D(F,B) \ge 1` always, with the min possibly attained at
  `B` fully uncut OR partially cut depending on `F`. Numerically true on all samples so far
  (0 violations of `D≥1` in the ~20000-trial n=5 budget-respecting scan reported in
  `parity-measure-potential.md`/`ballot-matching.md`'s own scans, and 0 in the fresh joint-optimum
  search this round) but NOT proved.
- The vertex/LP-mechanism transfer (framing i) is a reasonable conjecture given how cleanly
  `Theorem VERT` worked for the analogous upper-wall polytope, but the lower polytope's combinatorics
  (interleaving of two independently-cut multisets under a shared budget) is more complex than the
  single-multiset reachable-set `R_i` used upstairs — treat the transfer as untested, not assumed.
