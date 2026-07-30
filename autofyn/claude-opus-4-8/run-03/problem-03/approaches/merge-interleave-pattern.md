## Status
partial

## Approaches tried
- (round 14) LP-DUAL / same-group exchange-smoothing (sparse Farkas certificate) revision. Ran the
  MANDATED n=5 gate FIRST (scipy HiGHS + exact hand-check of the load-bearing coefficient identity).
  RESULT: the CLAIM holds (min L_T = 1 at n=3,4,5, NO sub-1 vertex — GAP-EXTR now confirmed at n=5),
  but the proposed MECHANISM is REFUTED on BOTH mandated gate conditions:
    (i) the sparse dual pattern "±1 equality multipliers + a single order-inequality with multiplier
        2" is NOT uniform (extracted duals vary: some 1 order-slack ×2, some 4 order-slacks ×1, some a
        box multiplier) and is RIGOROUSLY IMPOSSIBLE for the mandated non-canonical n=4 witness
        F={6,6,4}, tail level-3 split {3,3,2}, sorted {6,6,4,4,3,3,2,2,1}: the witness is box-interior,
        so by complementary slackness every certifying dual has zero box multipliers; coefficient
        matching then forces Σ_g y_g rhs_g = 1 AND Σ_g y_g|g| = [m odd]; the ±1 solution of the first
        (unique by binary rep: y_F=+1, y_tail=−1) gives Σ y_g|g| = |F|−|B| = −3 ≠ 1. Contradiction.
    (ii) "every box-free vertex has ≤ one odd block" is FALSE — up to 5 odd blocks occur (n=5),
        including at TIGHT L_T=1 vertices. Clean counterexample: n=4, F={6,6,4}, level-3 split {4,4},
        sorted {6,6,4,4,4,4,2,1}, box-free, L_T=1, block sizes [2,4,1,1] = TWO odd singleton blocks
        {2},{1} (also refutes "odd residual pinned to value 1": one odd block has value 2).
  DIAGNOSIS: certificate-existence is (strong LP duality) LOSS-FREE EQUIVALENT to GAP-EXTR — a
  reframing, not a reduction. The only lever would have been a uniform provable multiplier pattern;
  both handles (sparse dual; odd-block collapse) are dead. The LP-dual vehicle joins the dead lower
  families. Outcome: PARTIAL — claim de-risked to n=5, mechanism refuted, one rigorous structural
  lemma (DUAL-CHAR) extracted. Per hard constraints, no fake prose shipped.
- parity-measure-potential lineage / word-encoding skeleton (round 7) — registered; two open steps
  (GAP-REACH, GAP-EXTR) isolated.
- (round 12) LP-VERTEX / active-constraint-rank revision. Ran the MANDATED cheap-kill FIRST:
  exhaustive vertex/LP enumeration of the lower interleave polytope for n=3 (5 F-types × all words)
  and n=4 (21 F-types × all words). RESULT: global min D = 1 exactly for both, NO vertex with
  L_w < 1 — the cheap-kill PASSES (GAP-EXTR holds for n ≤ 4). Established rigorously the vertex
  REDUCTION (Theorem VERT-LOW: MID-core min over the continuum = min over a finite explicit set of
  block-structured extreme points) and the block-structure bound (≤ n+1 distinct positive values at a
  vertex; rigorous bound n+3). REFUTED two would-be shortcuts to GAP-EXTR: D is NOT constant across
  words (Case (a) gives D=2^{n-1}) and D is NOT always integral at vertices (132 non-integer vertices
  found at n=3, all with D>1). GAP-EXTR for general n (every vertex has D ≥ 1) is loss-free equivalent
  to MID-core and remains the honest open crux. Outcome: PARTIAL — rigorous reduction + de-risked
  mechanism (n≤4 confirmed), general-n vertex bound open.

## Current best
**MID-core recast as a finite vertex-minimisation, rigorously (Theorem VERT-LOW below), with the
mechanism de-risked to n≤4 by exhaustive computation (min D = 1, no clumped vertex).** The general-n
vertex bound GAP-EXTR is the remaining gap; it is loss-free equivalent to MID-core (μ{g odd}≥1 for
|F|≥3), so this route sharpens the target to "every block-structured extreme point of P_T has
alternating value ≥ 1" but does not by itself close it. The integrality and constant-value shortcuts
are refuted (non-integer vertices exist; D varies across words).

The answer is **c(n) = 2^n/(2^{n+1}−1)**, minimax **D = u_n = 1/(2^{n+1}−1)** (field-confirmed).

---

### Imports (certified, no re-proof)
Lemmas **R** (claiming game ⇒ Liu = (1+D)/2, D = Σ(−1)^{k+1}v_k over descending pieces), **M**
(D = μ{t: N_S(t) odd}), **TB** (top-band decomposition; closes f₁ ≥ 2^{n-1}+1 and Case (a)),
**MID** (`mass-difference-reduction`: reduces the a=0 lower bound to MID-core, and gives
D(S)=μ{g odd}, ∫g=1), **ONE / ONE-REC** (`top-scale-dichotomy`, `recursed-dyadic-dichotomy`:
per-scale single excursion), **OSR** (`order-statistic-reformulation`). These reduce the whole lower
bound D(S) ≥ 1 to:

> **MID-core (residual).** Let S = F ⊔ B with F the fragments of the top piece 2^n (each in
> (0, 2^{n-1}], ΣF = 2^n, |F| ≥ 3) and B a refinement of the tail ladder C_{n-1}={2^0,…,2^{n-1}}
> using c_B cuts (each piece in (0, 2^{n-1}], ΣB = 2^n−1), subject to the cut budget
> (|F|−1) + c_B ≤ n. Then D(S) = Σ_k (−1)^{k+1} v_k ≥ 1, where v_1 ≥ … ≥ v_m are the sorted pieces
> of S, m = |F| + |B|.

(|F|=2 and the trivial/top-uncut regimes are closed by the imports; |F| ≥ 3 is the entire residual.)

### The combinatorial type and its polytope
A **combinatorial type** is T = (|F|, (k_0,…,k_{n-1}), σ) where k_j ≥ 1 is the number of fragments of
the tail piece 2^j (so Σ_j (k_j−1) = c_B), and σ is a word: a linear order on the labelled pieces
{the |F| F-fragments; the k_j fragments of each 2^j} that is consistent with descending value and, WLOG,
descending within each group. There are finitely many types for each n.

Fix T. Introduce a variable v_i ≥ 0 for each labelled piece (m variables). Impose the LINEAR
constraints:
- **(E) group sums:** Σ_{i∈F} v_i = 2^n and, for each j, Σ_{i ∈ group j} v_i = 2^j. [n+1 equalities.]
- **(O) order:** v_{σ(1)} ≥ v_{σ(2)} ≥ … ≥ v_{σ(m)}. [m−1 inequalities.]
- **(C) cap/box:** 0 ≤ v_i ≤ 2^{n-1} for every i.

Call the feasible set **P_T**. It is a compact polytope (bounded by the box (C), cut out by finitely
many linear inequalities). Note **ONE-REC is not an extra facet**: two fragments of group j each
> 2^{j-1} would sum to > 2^j = Σ group j, so "at most one fragment of group j exceeds 2^{j-1}" is
already IMPLIED by (E)+positivity — it constrains which words σ are *realisable* but adds no binding
inequality inside a fixed realisable P_T. (This corrects the outline's step-2c: the ladder single-excursion
is an automatic consequence, not a separate linear constraint.)

By certified Lemma R (and M), on P_T the functional D coincides with the **linear** functional
$$L_T(v) \;=\; \sum_{\text{pos odd}} v_{\sigma(\text{pos})} \;-\; \sum_{\text{pos even}} v_{\sigma(\text{pos})},$$
the alternating sum in the descending order fixed by σ.

Every admissible MID-core refinement lies in P_T for exactly one type T, and conversely every point of
P_T with all coordinates positive and pairwise-consistent is such a refinement. Hence the set of all
admissible refinements is the union, over the finitely many types T, of (the positive part of) P_T.

### Theorem VERT-LOW (rigorous vertex reduction)
> min{ D(S) : S an admissible MID-core refinement } ≥ min_T min_{v ∈ vert(P_T)} L_T(v),
> and each inner minimum is attained at a **vertex** of P_T.

*Proof.* L_T is a linear functional on the nonempty compact polytope P_T, so it attains its minimum
over P_T at an extreme point (vertex) of P_T — the **Fundamental Theorem of Linear Programming**: a linear
functional that is bounded below on a nonempty polyhedron attains its minimum at a vertex whenever the
polyhedron has one, and a compact polytope always does. (Standard; the same profile-independent
LP-vertex fact certified as Theorem VERT in the breakpoint-vertex approach on the upper wall.) The admissible refinements form
a subset of ⋃_T P_T (their positive parts), and D = L_T there; therefore
min D ≥ min_T min_{P_T} L_T = min_T min_{vert(P_T)} L_T. ∎

Because for a *lower* bound we may enlarge the feasible region to the whole (closed) polytope P_T —
including its degenerate boundary points with zero-length coordinates — VERT-LOW is safe: if every
vertex has L_T ≥ 1, then every genuine refinement has D ≥ 1. Thus MID-core is **equivalent** to:

> **GAP-EXTR.** For every type T and every vertex v of P_T, L_T(v) ≥ 1.

### Block-structure of vertices (rigorous, bounded distinct values)
> At a vertex of P_T the m coordinates take at most n+3 distinct values (hence ≤ n+2 distinct
> positive values). Numerically the sharp bound is n+1.

*Proof.* A vertex is a point where m linearly independent constraints are active. The n+1 equalities
(E) are always active; their rows have pairwise-disjoint supports (each labelled piece lies in exactly
one group), so they have rank exactly n+1. The remaining ≥ m−(n+1) active constraints come from the
tight order relations (O) and the box faces (C). Partition the m positions into p maximal blocks of
equal value; then exactly m−p of the order relations v_{σ(k)}=v_{σ(k+1)} are tight. The box supplies
at most two more active independent constraints (v=2^{n-1} on the top block, v=0 on the bottom block).
Hence the active rank is ≤ (n+1)+(m−p)+2. For a vertex this must equal m, forcing
(n+1)+(m−p)+2 ≥ m, i.e. **p ≤ n+3**. Excluding a possible zero block leaves ≤ n+2 distinct positive
values. ∎

So GAP-EXTR is a statement about a FINITE, explicit family of block-structured configurations (each
with ≤ n+1 distinct dyadic-group-summed values) — a genuine sharpening of the target.

### Cheap-kill (MANDATED, run FIRST — decisive, exhaustive for n = 3, 4)
For n = 3 (5 F-types) and n = 4 (21 F-types), for every type T and every word σ, the minimum of
L_T over P_T was computed exactly by linear programming (scipy HiGHS). RESULT:

- **Global min L_T = 1.000000 for both n = 3 and n = 4; NO vertex has L_T < 1.** GAP-EXTR holds for
  n ≤ 4. The minimum is attained at canonical one-fragment-per-gap layouts, e.g. n=3:
  F = {4,3,1}, B = {4,2,1} (tail uncut), sorted {4,4,3,2,1,1}, D = 4−4+3−2+1−1 = 1.
- **No clumped sub-1 vertex** — the refutation branch (a clumped F-excursion spread to non-adjacent
  scales, the HALL-ENDPOINT failure mode) does **not** occur. The route is not refuted.
- Two shortcuts to GAP-EXTR are **refuted** (recorded so no round retries them): D is NOT constant
  across words (Case (a) alone gives D = 2^{n-1}), and D is NOT always an integer at a vertex (132
  non-integer vertices at n=3, all with D > 1) — so GAP-EXTR cannot be reduced to "D ∈ ℤ_{>0}".

### Attainment (tightness — matches the answer u_n)
The bound D ≥ 1 is tight. Take B = C_{n-1} uncut and F = {2^{n-1}, 2^{n-2}, …, 2, 1, 1} (sum
2^{n-1}+…+1+1 = (2^n−1)+1 = 2^n, |F| = n+1 ≥ 3, F-cuts = n, c_B = 0, budget n ≤ n). The merged
descending multiset is 2^{n-1},2^{n-1},2^{n-2},2^{n-2},…,2,2,1,1,1: every value 2^{n-1},…,2 occurs
twice (a +x,−x cancelling pair at consecutive odd/even positions) and the value 1 occurs three times
(positions 2n−1,2n,2n+1 contribute 1−1+1 = 1). Hence D = 1 exactly, so min D = 1 and the lower bound
is sharp, confirming minimax D = u_n and c(n) = 2^n/(2^{n+1}−1). (This construction is also the tight
UPPER witness: Xiang forces D down to 1.)

### R14 update — LP-dual/sparse-Farkas MECHANISM refuted (claim de-risked to n=5)
The n=5 gate was run. **GAP-EXTR is now confirmed at n=5** (min L_T=1, no sub-1 vertex). But the
LP-dual vehicle proposed to PROVE it is dead:

- **DUAL-CHAR (rigorous, box-free chain-certificate characterization).** For a box-free type T, a
  Farkas certificate of L_T≥1 using only the (E) equalities and the (O) order chain exists iff there
  are reals y_g with (A) Σ_g y_g·rhs_g = 1, (B) Σ_g y_g·|group g| = [m odd], and (C) the chain
  prefix-sums z_k := Σ_{l=1}^k (s_l − y_{g(l)}) ≥ 0 for all k, where s_l=(−1)^{l+1} and rhs_F=2^n,
  rhs_j=2^j. *Proof.* On P_T write L_T(v)−1 = Σ_g y_g(eq_g−rhs_g) + Σ_{k=1}^{m-1} z_k(v_{σ(k)}−v_{σ(k+1)}).
  Matching the coefficient of the piece at position k gives s_k = y_{g(k)} + z_k − z_{k−1} (z_0=z_m:=0);
  the constant gives −1 = −Σ y_g rhs_g, i.e. (A). Solving the chain, z_k = Σ_{l≤k}(s_l−y_{g(l)}); the
  position-m equation is the telescoped total Σ_k s_k = Σ_g y_g|g|, i.e. [m odd]=Σ_g y_g|g| = (B).
  Feasibility (z_k≥0) is (C). ∎ *This is a correct reusable fact but is loss-free equivalent to
  GAP-EXTR, so it does NOT close it — no free lunch.*

- **Refutation R14a (±1 equalities impossible).** The mandated non-canonical n=4 witness
  F={6,6,4}, tail level-3 split {3,3,2}, sorted v*={6,6,4,4,3,3,2,2,1}, L_T=1, is strictly
  box-interior (all 0<v_i*<8=2^{n-1}). By LP complementary slackness every certifying (=optimal) dual
  has zero box multipliers, so DUAL-CHAR applies. rhs_g are the distinct powers {2^0,…,2^4}; Σ ±2^k=1
  has the UNIQUE ±1 solution y_F=+1, y_tail=−1 (the positively-signed rhs must sum to 2^n, only {2^n}=F
  qualifies since 1+…+2^{n−1}=2^n−1<2^n). That y gives Σ y_g|g| = |F|−|B| = 3−6 = −3 ≠ [9 odd]=1,
  violating (B). Hence NO ±1-equality certificate exists — the outline's stated multiplier form is
  impossible. (The true optimal dual here is y=e_{L0} with four order-slacks ×1 at k∈{1,3,5,7}:
  L_T−1 = (v_9−1)+Σ_{k∈{1,3,5,7}}(v_k−v_{k+1}).)

- **Refutation R14b (odd-block collapse impossible).** Box-free vertices with ≥2 odd blocks occur,
  including at L_T=1. Explicit: n=4, F={6,6,4}, level-3 split {4,4}, sorted {6,6,4,4,4,4,2,1},
  box-free, L_T=6−6+4−4+4−4+2−1=1, block sizes [2,4,1,1] — two odd singletons {2},{1}. The
  "≤1 odd block / residual pinned to value 1" gate-conjecture is dead.

- **Consequence.** The LP-dual/exchange-smoothing vehicle joins the dead LOWER families (no uniform
  provable multiplier pattern; the dual is a reframing of GAP-EXTR). Retire it for the LOWER wall.
  Next framing must NOT be a restatement of "min L_T over the vertex polytope." Candidates flagged
  (both undes-risked): (a) dyadic-scale induction on D=μ{g odd}, ∫g=1 tracking odd-block mass across
  scales via ONE-REC as a STRUCTURAL fact; (b) aimo-0493-style dyadic-tagging bound on co-occurring
  odd blocks.

### The open gap
- **GAP-EXTR (open, general n):** every vertex of every P_T has L_T ≥ 1. It is loss-free equivalent to
  MID-core, so the vertex reduction does not automatically close it; it sharpens it to a bound on the
  alternating sum at each block-structured extreme point (≤ n+1 distinct dyadic values), which must
  still be proven using the dyadic ladder. Confirmed for n ≤ 4 by the exhaustive cheap-kill; the
  general-n argument (an inductive/telescoping bound over the block levels, exploiting that at a vertex
  the group sums pin the block values to the superincreasing ladder) is not yet in hand.
- **GAP-REACH — CLOSED as originally posed:** the ONE-REC per-scale single-excursion is an automatic
  consequence of (E)+positivity, not a separate constraint; it restricts realisable words but P_T is a
  genuine polytope regardless. (Outline step 2c corrected.)

### Watch out (recorded for next round)
- The vertex reduction is a rigorous *reframing*, not a closure: the residual GAP-EXTR is exactly
  MID-core. Its value is (i) a de-risked mechanism (n≤4 confirmed, no clumped vertex), (ii) a finite
  explicit target (block-structured extreme points, ≤ n+1 dyadic block-values), (iii) two dead
  shortcuts eliminated (integrality, constant-value). A future round should attack GAP-EXTR by an
  induction over the block levels / dyadic scales at a vertex, NOT by a monovariant, transport, or
  scalar-reserve (all dead).
- Do NOT re-attempt the integrality shortcut (non-integer vertices exist) or the "every vertex is
  canonical value-1" claim (false — D varies across words).

## Full proof
Not present — Status is `partial`. GAP-EXTR (general-n vertex bound) is the open step; the reduction,
block-structure lemma, cheap-kill (n≤4), and tight attainment are complete and rigorous.

## Promotable lemmas
- **Lemma DUAL-CHAR (box-free chain-certificate characterization) — NEW R14, rigorous.** For a
  box-free type T, a Farkas certificate of L_T≥1 from (E)+(O) exists iff ∃ reals y_g with
  (A) Σ_g y_g rhs_g = 1, (B) Σ_g y_g|g| = [m odd], (C) z_k := Σ_{l≤k}(s_l−y_{g(l)}) ≥ 0 ∀k. Proven
  in full above by coefficient matching + telescoping. NOTE: loss-free equivalent to GAP-EXTR (does
  not close it); its value is the two forced identities (A),(B) that make the ±1 refutation R14a
  airtight. (Certify as a structural fact / dead-mechanism record, not as a lower-bound closer.)
- **Refutation R14a (rigorous):** no certifying dual with y_g∈{±1} exists (proof via complementary
  slackness at the box-interior n=4 witness + binary uniqueness of Σ±2^k=1 + identity (B)).
  Kills the outline's ±1-equality/single-order-×2 mechanism.
- **Refutation R14b (rigorous):** box-free L_T=1 vertices with ≥2 odd blocks exist (explicit n=4
  witness {6,6,4,4,4,4,2,1}). Kills the odd-block-collapse gate-conjecture.
- **Theorem VERT-LOW (vertex reduction for MID-core).** For each n, MID-core (D(S) ≥ 1 for the residual
  band |F| ≥ 3) is equivalent to: over the finitely many combinatorial types T (= word σ + tail
  grouping), every vertex of the polytope P_T (variables = piece values; constraints (E) group sums,
  (O) descending order fixed by σ, (C) box 0 ≤ v_i ≤ 2^{n-1}) satisfies the linear alternating
  functional L_T(v) = Σ_{odd}v − Σ_{even}v ≥ 1. *Proof:* linear functional on a nonempty compact
  polytope attains its min at a vertex; admissible refinements ⊆ ⋃_T P_T with D = L_T. Proven in full
  above (rigorous; independent of GAP-EXTR).
- **Block-structure lemma.** At a vertex of P_T the values take ≤ n+3 distinct values (≤ n+2 positive),
  by an active-constraint rank count against the n+1 group-sum equalities. Proven in full above.
- **MID-core is tight (attainment D = 1).** Explicit family B = C_{n-1}, F = {2^{n-1},…,2,1,1} realises
  D = 1 for every n via cancelling pairs plus a triple-1 residue. Proven in full above (confirms
  minimax D = u_n).
