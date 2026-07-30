## imo-2026-03 — lens: LOWER-BOUND wall, GAP MID-core

### Key new structural fact found this round (not previously recorded)

Encode the merge of F∪B in strictly descending order as v_1>v_2>...>v_m (m=|F|+|B|),
label e_i=+1 if v_i∈F, −1 if v_i∈B, and S_i=Σ_{j≤i} e_i (S_0=0) the partial sum ("walk").
Then on the interval (v_{i+1},v_i) (length w_i:=v_i−v_{i+1}), g≡S_i, so
- D(S) = Σ_{i odd} w_i,   ∫g = Σ_i S_i w_i  ( = ΣF−ΣB = 1, reproved by Abel swap Σ_i S_i w_i
  = Σ_j e_j v_j = ΣF−ΣB, consistent with Lemma MID(b) ).

**Crucial fact:** because every step e_i=±1, S_i ≡ i (mod 2) ALWAYS — a completely general
walk fact, independent of the F/B/ladder structure. Hence {t : g(t) odd} = ⋃_{i odd}(v_{i+1},v_i)
is exactly the set of ODD-RANK gaps of the merged multiset S=F⊔B. So **D(S)=Σ_{i odd}w_i is
literally the alternating sum of order statistics of the full multiset S** — i.e. Lemma MID's
"g odd" set is identical to the direct odd-rank set from Lemma R/M applied to S itself. Lemma
MID's part (a) is therefore NOT new leverage beyond Lemma R — it is a re-derivation of the same
alternating-sum fact, dressed in F/B language. The genuinely new content of Lemma MID is only
part (b), ∫g=1, a distinct identity (Σ_i S_i w_i = 1).

**Consequence: GAP MID-core is exactly the inequality**
  D(S) − ∫g = Σ_i c_i w_i ≥ 0,  where c_i := 1[i odd] − S_i.
Since S_i≡i (mod2), c_i is always EVEN, and: for i odd, c_i=1−S_i (≥0 iff S_i≤1); for i even,
c_i=−S_i (≥0 iff S_i≤0). **This is NOT termwise nonnegative in general** — I built an explicit
example (n=3, F={3.4,2.6,2}, B={4,1.05,1,0.95}, budget 3=n) where the walk overshoots (S_4=2>1,
giving a negative term −1.9 at i=4) yet the deficit is exactly repaid by excess at i=1 and i=7
(terms +1.2 and +1.9), net D−∫g=1.2>0. Checked numerically consistent (D=2.2, ∫g=1.0 exactly).

So GAP MID-core is a genuine **ballot/cycle-lemma-flavored claim about a ±1 walk weighted by
gap lengths**: excursions of S_i above the baseline 1[i odd] must be "repaid" by dips below it
elsewhere, and this repayment is forced by the fact that the walk MUST end very negative
(S_m=|F|−|B|, and |B|≥n while |F|≤n, and B's sum ladder structure forces |B| large relative to
|F| — this is exactly where the superincreasing/ladder property of B, i.e. Lemma ONE recursed,
must enter). This is a materially different, more tractable shape of the gap than "prove an
abstract measure inequality" — it is now an explicit **signed-walk / partial-sum inequality**
amenable to induction on the walk's length or on n via peeling the LARGEST element (v_1) and
recursing (the walk-prefix framing is naturally inductive: peeling v_1 removes one B or F label
from the front and reduces to the same shape of problem on the residual walk, with adjusted
target R.H.S.).

### (i) Is there a clean route?

- **Pure integral / abstract version is FALSE** (already established: g≡2 on measure 1/2 is a
  counterexample) — reconfirmed by my analysis: the walk-overshoot argument needs the ladder
  structure, not just ∫g=1.
- **A natural sufficient-but-not-necessary condition** S_i≤1[i odd]+0 for ALL i is false in
  general (see counterexample), so a naive "the walk never runs 2 ahead" claim will not work
  as stated — but it may still be TRUE that the walk cannot run 2 ahead **and stay there past
  a full dyadic gap of B** (i.e. w_i>0 at the moment of overshoot must be compensated by a
  positive-length interval immediately after where the walk drops back), which is exactly a
  finer version of the ladder-recursion idea (Lemma ONE recursed) the field has already flagged.
- **A monovariant via Lemma ONE recursed** is plausible: define the partial deficit function
  Δ(i) := Σ_{j≤i}(1[j odd]−S_j)w_j and try to show Δ(i) ≥ −(something controlled by the ladder
  scale currently being crossed), inductively peeling from i=1 (top) downward through each
  dyadic scale of C_{n-1}, using that at most one B-piece can exceed each dyadic threshold
  (Lemma ONE) to bound how far S_i can run ahead before the next B-crossing forces it back down.
  This is NOT closed — it is a genuine, structurally promising lever, distinct from both
  approaches' current framings, that should be tried.
- **Reachable-word framing (merge-interleave-pattern)** is essentially the SAME object viewed
  combinatorially (w = the label word FBBFF..., GAP-REACH ≈ characterizing which walks/words are
  reachable, GAP-EXTR ≈ minimizing D(S) over reachable words). My walk analysis gives a concrete
  reformulation of GAP-EXTR as: minimize Σ_{i odd}w_i subject to Σ_i S_iw_i=1 and the ladder/
  reachability constraints on (S_i, w_i) — i.e. GAP-EXTR is LITERALLY GAP MID-core restated. So
  merge-interleave-pattern and parity-measure-potential's residual gap are now PROVABLY the same
  scalar inequality, just in different notation (word vs. g-function) — good to flag to the
  outliner so they aren't developed as if independent; but the reachable-word combinatorial
  language (GAP-REACH: ≤1 F-letter per dyadic gap of B) may be the more tractable vehicle for
  actually doing the induction, since it exposes the ladder constraint directly as "at most one
  F insertion per B-gap," which is the natural handle for an inductive peel from the top scale.

### (ii) Corpus analogue

Searched crux corpus (domain-filtered combinatorics/number_theory, subtopics
invariants-and-monovariants, pigeonhole, coloring-and-parity, games-and-strategy, plus free-text
scan for "ballot", "cycle lemma", "running maximum", "excursion", "partial sum", "random walk").
**No genuine analogue found.** The closest hits are generic monovariant-tracking cruxes
(`aimo-0121`: track a running maximum as a monovariant, bound move-count by its total required
rise — same *flavor* of "bound something by tracking the walk's excursions" but on a totally
different problem, not a signed-measure/parity walk) and various "parity of a completely additive
statistic" cruxes (`aimo-0274`, `aimo-0580`) which are not about weighted occupation time of a
walk. Conclusion: **no corpus crux directly transfers**; the ballot-lemma/cycle-lemma shape is a
useful mental model but not literally instantiated in the corpus for this problem.

### (iii) Which approach is the better vehicle, and hardest sub-step

- **parity-measure-potential** currently owns Lemma MID and is well-positioned to state and
  attack GAP MID-core directly in the g/walk language (my c_i decomposition slots right into its
  existing measure-calculus style). This is probably the vehicle of least friction since MID is
  already certified there.
- **merge-interleave-pattern** is unsolved/skeleton but offers the more natural inductive
  handle (GAP-REACH's "≤1 F-letter per B-gap" is exactly the constraint needed to control how
  far S_i can run ahead of baseline before the next B-label forces it down). If the walk-peel
  induction is pursued, this framing may make the induction cleaner to write, since the
  reachability constraint is already isolated as a named open sub-gap (GAP-REACH) rather than
  buried in measure-calculus.
- **Hardest sub-step (either vehicle):** proving the walk cannot sustain S_i>1[i odd] (mod 2's
  even-excess) for a length exceeding what the NEXT ladder-forced B-crossing pays back — i.e.
  quantifying "at most one F excess per dyadic scale of B" into a genuine inequality
  Σ_{j∈ overshoot interval} w_j ≤ (compensating deficit later), profile-independently over ALL
  admissible (F,B) with |F|≥3. This is exactly GAP MID-core / GAP-EXTR; it requires strong
  induction using Lemma ONE recursed (peeling the top dyadic scale of B each step), analogous in
  STRUCTURE (not content) to a cycle-lemma argument, but no template exists in the KB or corpus —
  it must be built from scratch.

### Candidate technique(s)
Induction on n via peeling the top dyadic scale (Lemma ONE recursed), reformulated as a signed
±1-walk weighted-occupation-time inequality (new framing surfaced this round); alternatively the
reachable-word/GAP-REACH characterization as the combinatorial vehicle for the same induction.

### Cheap-kill candidates
- Check whether the "at most one F-fragment can lie strictly inside a given dyadic gap of B'
  top scale" claim (GAP-REACH, restricted to the TOP scale only, which Lemma ONE already gives)
  is enough by itself, by testing the walk-overshoot bound on more numeric examples at n=4,5
  with |F| large (5–8 fragments) — a cheap way to see if a single-scale argument suffices or if
  multi-scale coordination is really needed. (Not run this round due to time budget; flag for
  next round's builder as a fast numeric probe before committing to a heavy induction.)
- None found that fully resolves the gap without real work.

### Knowledge-base entries to use
Certified lemmas only (no separate `knowledge_base.md` generic entry directly matches a
ballot/cycle-lemma template): Lemma M (measure identity), Lemma ONE (top-scale dichotomy,
the key structural input to recurse), Lemma MID (mass-difference reduction, already certified,
whose part (a) I've shown is equivalent to the direct odd-rank fact and part (b) is the
genuinely new ∫g=1 identity).

### Analogous past problems (cruxes)
None found that is a genuine analogue (see (ii) above); closest tangential hit `aimo-0121`
(invariants-and-monovariants: running-maximum monovariant bounding a count by required rise) —
same generic "bound via tracking a walk's excursions" flavor but not a real match; do not force it.

### Prior progress
Lemma MID certified (parity-measure-potential): D(S)=μ{g odd}, ∫g=1, reduces L2/GAP-L2 exactly
to GAP MID-core for |F|≥3 (|F|=2 and 0≤g≤1 already closed). merge-interleave-pattern registered
as skeleton (GAP-REACH + GAP-EXTR), unsolved, not yet built. This round's finding: GAP MID-core
and GAP-EXTR are the SAME inequality in two notations; and MID's part (a) is a re-derivation of
Lemma R/M (no new leverage), so the only genuinely new fact from MID is ∫g=1 — the real residual
work is the walk-overshoot/ballot inequality Σc_i w_i≥0, not yet proved anywhere in the field.

### Dead ends (do not retry)
- Pure-integral version "∫g=1 ⇒ μ{g odd}≥1" — FALSE (g≡2 on measure 1/2), reconfirmed.
- Outliner's "O_B meets each dyadic gap in ≤1 interval" invariant — FALSE (explicit witness in
  Lemma MID file), reconfirmed by re-reading, do not resurrect.
- The naive termwise-sufficient condition "S_i ≤ 1[i odd] for all i" — FALSE (my own
  counterexample this round, S_4=2 at n=3 example above); do NOT propose this as the lemma to
  prove — it is not true and the correct claim needs the compensating-deficit (aggregate) form.

### Small-case / intuition notes (conjectural, numerically checked this round)
- Verified by hand (n=3, F={3.4,2.6,2}, B={4,1.05,1,0.95}): D(S)=2.2, ∫g=1.0 exactly,
  D−∫g=1.2>0, with an intermediate walk overshoot (S_4=2) that is NOT locally compensated but
  IS compensated in aggregate by the earlier/later terms — supports the "aggregate ballot"
  picture over any termwise-positivity picture.
- Conjecture (not proved): the compensation is forced by B's superincreasing ladder structure
  ensuring |B| grows fast enough, and the correct inductive invariant should track, at each
  dyadic scale threshold τ=2^{j}, the running deficit Σ_{v_i>τ} c_i w_i and show it is bounded
  below by 0 minus a term that vanishes as more of the ladder is peeled — this is speculative
  and NOT attempted further (per instructions, stopping here without developing the induction).
