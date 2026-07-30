# imo-2026-03 — lower-bound 5th-framing scout (round 5)

Lens: find a GENUINELY 5th framing of the lower-bound G1 wall, far from the four
converged framings (PL/variational `tail-count`, block/spine `tower-induction`,
gaps/leftover `gaps-leftover`, LP/Farkas `lp-dual-certificate`).

## (1) The wall restated

Liu plays the dyadic tower `T_n = (2^n, 2^{n-1}, …, 2, 1)` (tower units, total
`D_n = 2^{n+1}−1`). Target: `D = a_1 − a_2 + a_3 − … ≥ 1` for EVERY `≤ n`-mark
Xiang refinement. Equivalently (Xiang-take form): Xiang's even-index mass
`≤ D_{n−1} = 2^n − 1` (= below-top tower mass), i.e. **Liu always captures `≥ 2^n`
= the top piece's worth.** The open sub-case G1: Xiang uses `≥ 3` marks with `≥ 1`
unbalanced (non-dyadic) split. Four framings converge on this wall; the shared
obstruction is the GLOBAL SORT / interleaving — a fragment's sign (position
parity) is a global functional of the whole sorted multiset, so per-fragment or
per-level rules do not compose (the V-shape: after `8→5+3`, the second split is
V-shaped, rebalancing INCREASES `D`).

## (2) Candidate angles — computation + obstruction

### (a) Absorption invariant / exact-potential induction on mark count

**Approach.** Seek a quantity `Q(config)` with `Q(T_n) = 1` such that every
single Xiang split changes `Q` by a predictable signed amount whose cumulative
sum is always `≥` the loss, giving `Q(refined) ≥ 1`. The `d-potential` attempt
set `Φ ≥ D` and went circular; the candidate here must be an EXACT invariant or a
one-sided bound with a clean per-split budget.

**Concrete candidate tested.** Split the top `2^n → F` (fragments) and refine the
below-top `T_{n−1} → R`. The layer-cake integral gives `D = ∫(N mod 2)dt` with
`N = N_F + N_R`. Using `(a+b) mod 2 = (a mod 2)+(b mod 2)−2(a mod 2)(b mod 2)`:

  `D = D_F + D_R − 2·C`,   `D_F = ∫(N_F mod 2)dt`, `D_R = ∫(N_R mod 2)dt`,
  `C = ∫(N_F mod 2)(N_R mod 2)dt` (overlap of the two odd-parity regions).

`D_F` is the standalone alternating sum of the top-fragments; `D_R` is the
standalone `D` of the below-top refinement. I tested the sufficient condition
`D_F ≥ 2C` (which with `D_R ≥ 1` by IH would give `D ≥ 2C+1−2C = 1`).

**Computation (`xor_decomp.py`, `xor_induct.py`, exact `Fraction`).**
- The XOR identity `D = D_F + D_R − 2C` is EXACT: 0 failures over 6000+ random
  refinements of `T_3, T_4, T_5`. Verified on the unsplit tower
  (`F={2^n}`: `C = D_R`, `D = 2^n − D_R = D(T_n)` ✓).
- `D_F ≥ 2C` holds for 0/5000 RANDOM tower-refinement configs, BUT FAILS at
  breakpoint (tie/minimizer) configs: 10/78 pairs (T_3), 543/2196 pairs (T_4).
  Worst deficit `D_F − 2C = −6` at `F={9,3,3,1}`, `R={8,2,2,1,1,1}` (T_4).
- At minimizers `(D=1)`, `D_F < 2C` is common; the slack `D_R > 1` compensates.
  So `D_F ≥ 2C` is too strong; the EXACT needed bound `D_F + D_R ≥ 2C + 1` is
  just `D ≥ 1` restated (circular).

**Obstruction.** No clean EXACT invariant `Q` exists: the per-split budget
`D_F − 2C` can be NEGATIVE (the top-fragments' odd-parity region overlaps the
below-top odd-parity region by MORE than half of `D_F`). The "1" margin is NOT
absorbed locally by the top split; it requires the below-top tower structure.
`D_F ≥ 2C` fails at exactly the extremal (minimizer) configs where it is needed.

### (b) Different Liu config

**Approach.** Is the tower really the easiest to prove? Search for a near-tower
Liu config (still `≤ n` marks, still min `D = 1`) with cleaner refinement
structure.

**Finding.** DEAD END. Run-state establishes (round 1–2): the tower is the UNIQUE
worst Liu config — `n=2` non-tower configs let Xiang drive `D` to 0. Any config
with min `D > 1` (more slack) gives a LARGER `c(n)`, contradicting the (proved
for `n≤3`) upper bound `c(n) ≤ 2^n/D_n`. So only the tower (or another exact-
equality config, of which the tower is unique) attains the tight bound. There is
no "easier near-tower" config with `D ≥ 1` to prove against.

### (c) Partition / dominance-order lattice theorem

**Approach.** `D` = alternating sum of the sorted partition. A refinement `μ` of
the tower partition `λ` has `μ ≺ λ` (μ majorized by λ). Is there a lattice
theorem giving `D(μ) ≥ 1` for refinements of the staircase `(2^{n−1},…,2,1)`?

**Finding.** DEAD END. `D` is NOT monotone in the refinement/majorization order.
Single-split refinement is non-increasing (slope `0` or `−2`, `single-split-top-
lower-bound`), but MULTI-split refinement can INCREASE `D` (the V-shape:
`8→5+3` then `5→2.5+2.5` gives `D=2 > 1`, an INCREASE from the tie `D=1`).
`rebalanced ≻ unbalanced` yet `D(rebalanced) > D(unbalanced)`: `D` is neither
Schur-convex nor Schur-concave under refinement. No standard lattice-monotonicity
theorem (Karamata, Muirhead, dominance-order) applies. (Already refuted for the
upper-bound majorization route in round 3; confirmed here for the lower-bound
refinement direction.)

### (d) Generating-function / roots-of-unity / polynomial

**Approach.** Encode the sorted partition as `P(x) = Σ_k p_k x^k`; then
`D = P(−1)` (evaluation at the order-2 root of unity). Tower polynomial
`T_n(x) = Σ_{k=0}^n 2^{n−k} x^k`, `T_n(−1) = (2^{n+1}+(−1)^n)/3 ≥ 1`. Does a
coefficient-positivity or root-of-unity lemma give `D ≥ 1` under refinement?

**Finding.** NOT genuinely new. The encoding `D = P(−1)` is correct, but a
refinement (splitting a piece and re-sorting) is NOT a clean polynomial operation
on `P`: the new positions depend on the global sort, so the monomial
`V·x^j` is replaced by `f·x^a + (V−f)·x^b` with `a,b` determined by interleaving.
Decomposing `P(−1) = Σ_t P_t(−1)` by tower-piece bins (= `Σ_t y_eq[t]·2^{n−t}`,
the signed tower-value sum) IS EXACTLY the LP-dual objective of framing 4
(`lp-dual-certificate` GAP-LP2). The polynomial angle is the LP-dual angle in
disguise; it offers no new positivity lemma beyond strong duality (which is
G1-equivalent, per the round-4 reviewer correction).

### (e) Topological / parity (Sperner / Tucker / Borsuk-Ulam / discrete fixed-point)

**Approach.** The GAP-C claim "the min-level set `{D=1}` is star-shaped to a
dyadic vertex" is a CONNECTIVITY claim on the PL (breakpoint) complex. A
Sperner-lemma / discrete-fixed-point argument: color breakpoint vertices by
their tie-type; Sperner gives an odd-parity fully-colored simplex = a dyadic
vertex in the min-level set.

**Finding.** Suggestive but NO concrete coloring found. The breakpoint polytope
vertices (tie configs) would need a Sperner-proper boundary coloring whose
"fully-colored" simplex corresponds to a dyadic endpoint — but the PL complex of
refinements is not a simplex with the standard Sperner boundary, and the relevant
parity is GLOBAL-position-parity (the obstruction itself), not a local label.
This is a SUB-DIRECTION of GAP-C (a possible proof mechanism for the
star-shaped-transport claim), not a genuinely-new top-level framing. It shares
GAP-C's wall.

### (f) XOR / overlap decomposition (NEW — the lead 5th framing)

Discovered while testing angle (a). This is the genuinely-5th framing.

**Identity (EXACT, proved algebraically).** Split the refinement into
top-fragments `F` (mass `2^n`, from splitting the top piece) and below-top
pieces `R` (mass `2^n−1`, a `≤ (n−1)`-mark refinement of `T_{n−1}`). With
`N(t) = N_F(t) + N_R(t)` and `(a+b) mod 2 = (a mod 2)+(b mod 2)−2(a mod 2)(b mod 2)`:

  **`D = D_F + D_R − 2·C`**,   `C = ∫_0^{2^n} (N_F mod 2)(N_R mod 2) dt`.

- `D_F = ∫(N_F mod 2)dt` = standalone alternating sum of the top-fragments (a
  function of `F` ALONE, independent of `R`).
- `D_R = ∫(N_R mod 2)dt` = standalone alternating sum of the below-top pieces
  = `D` of a `≤ (n−1)`-mark refinement of `T_{n−1}`. **By strong induction on
  `n`, `D_R ≥ 1`** (the IH is G1 itself at size `n−1`; base `n=1`: `D_R=1`).
- `C` = the OVERLAP (correlation) of the two odd-parity regions — a genuinely
  different object from the global sort/interleaving. It is a PRODUCT of two
  `{0,1}`-valued step functions, decoupled in source.

**Why this is genuinely different from all four converged framings.**
- vs PL/variational: no piecewise-linear geometry of `D` in cut coordinates; the
  object is an integral CORRELATION, not a PL function.
- vs block/spine: no adjacent-equal-pair cancellation or spine sign-bookkeeping;
  `C` is a real-valued overlap measure, not a parity-vector recursion.
- vs gaps/leftover: no per-pair gap charging against tower levels; `C` couples
  two parity REGIONS, not pairs of positions.
- vs LP/Farkas: the dual objective `Σ_t y_eq[t]·2^{n−t}` is a signed tower-value
  sum (a STATIC certificate); `C` is a DYNAMIC overlap depending on BOTH `F`
  and `R`, with a clean inductive reduction.

**Induction.** `G1(n)` reduces to `G1(n−1)` + an overlap bound:
`D = D_F + D_R − 2C ≥ 1 ⟺ C ≤ (D_F + D_R − 1)/2`. With `D_R ≥ 1` (IH), it
suffices to bound `C` by a DECOUPLED function of `F` and `R` separately. The
trivial bounds: `C ≤ min(D_F, D_R)` (sub-measure), and by AM-GM / Cauchy-Schwarz
`C ≤ √(D_F·D_R)`, giving `D ≥ (√D_F − √D_R)^2 ≥ 0` — only the trivial `D ≥ 0`
(gaps-leftover Lemma G2). The "1" needs tower structure.

**The concrete hard step (the new lemma).** The R-odd region is dyadic-
structured ONLY when `R` is the unsplit tower or a dyadic refinement (verified:
T_2 unsplit odd on `[0,1]∪[2,4]`; T_3 unsplit odd on `[1,2]∪[4,8]`). Once `R`
is a NON-dyadic refinement (the G1 hard case of `R`), the R-odd region is NOT
dyadic (only ~37%/29%/24% of refined R have purely-dyadic odd regions for
T_2/T_3/T_4; counterexample `R={5/8,15/8,3/2,2,1}` has odd region
`[0,5/8]∪[1,3/2]∪[15/8,2]`). So a "dyadic-misalignment lemma" (bound `C` by
exploiting dyadic structure of R-odd) covers only the EASY sub-case (R
unsplit/dyadic, already closed by `dyadic-refinement-lower-bound`); the hard
case (non-dyadic R) has a non-dyadic R-odd region, and the overlap bound there
is G1(n−1)-equivalent. The genuine hope: the overlap `C` (a CORRELATION of two
parity functions, decoupled in source) admits a bound via a DIFFERENT mechanism
than global-position-parity — e.g. a Cauchy-Schwarz/AM-GM sharpened by the tower
mass identity `2^n = D_{n−1}+1`, or a recursive expansion where the overlap
terms telescope. The standard CS/AM-GM bound gives only `D ≥ 0` (trivial); the
"1" needs a structural input not yet identified.

**Computation summary.**
- Identity exact: 0 failures / 6000+ trials (T_3,T_4,T_5). Unsplit tower:
  `C = D_R`, `D = 2^n − D_R = D(T_n)` ✓.
- Base `n=1`: `F = {f, 2−f}`, `R = {1}`. `D_F = 2f−2`, `C = f−1` (for `f>1`),
  so `D_F = 2C` EXACTLY, `D = 2C + 1 − 2C = 1`. TIGHT at the base. ✓
- `D_R ≥ 1` confirmed: min `D_R` over `≤ (n−1)`-mark refinements of `T_{n−1}`
  is exactly `1` (the IH holds at the base; the induction reduces `n` by 1).
- Bound `D ≥ 1` (=`D_F + D_R − 2C ≥ 1`) holds with 0 violations (it is `D ≥ 1`,
  already known); the open question is whether the DECOUPLED overlap bound on
  `C` (the dyadic-misalignment lemma) is provable.

**Obstruction.** The overlap bound `C ≤ (D_F + D_R − 1)/2` is, as a STATEMENT
about `D`, G1-equivalent (it IS `D ≥ 1`). The genuine novelty is the OBJECT `C`
(a correlation of two separately-structured parity functions, one dyadic) and
the INDUCTION `G1(n) → G1(n−1) + overlap`. The decoupled dyadic-misalignment
lemma is the make-or-break step; it is NOT yet proved, and the numerics do not
reveal a clean decoupled bound `C ≤ g(D_F, D_R)` with `g` independent of the full
`F,R` structure (the max-`C`-per-`D_R` data is irregular). So this framing, like
the LP-dual, is a genuinely-different ATTACK ANGLE, not a shortcut.

## (3) Ranked recommendation

**1. XOR / overlap decomposition (angle (f)) — TURN INTO A SLUG.** Genuinely-5th
framing, far from the four converged. One-sentence skeleton: *Prove the exact
identity `D = D_F + D_R − 2C` (algebraic, from `(a+b) mod 2`); apply strong
induction on `n` so `D_R ≥ 1` (R refines `T_{n−1}` with `≤ n−1` marks); the hard
step is a decoupled bound on the overlap `C = ∫(N_F mod 2)(N_R mod 2)dt` (a
correlation of two separately-structured parity functions, NOT a global-sort
object) by `(D_F + D_R − 1)/2`.* The identity + induction + base case (`n=1`:
`D_F = 2C` exactly, `D = 1`) are PROVED; only the overlap bound is open. HONEST
caveat: for non-dyadic R (the G1 hard case of R), the R-odd region is NOT
dyadic, so a "dyadic-misalignment" path covers only the already-closed sub-
case; the overlap bound for non-dyadic R is G1(n−1)-equivalent (like GAP-LP2).
The angle's value is a DIFFERENT ATTACK SURFACE (a correlation/overlap, not a
global-position-parity or PL geometry) and a clean inductive reduction
`G1(n) → G1(n−1) + overlap`; it is NOT a shortcut. Worth one slug because it
may expose decoupled structure the four converged framings cannot see, and
because its base case is provably tight.

**2. Angle (e) topological/Sperner — NOT a new slug, but fold as a sub-direction
of `tail-count` GAP-C.** A Sperner-type coloring of the breakpoint polytope is a
possible PROOF MECHANISM for the star-shaped-transport claim (GAP-C), not a
rival top-level framing. No concrete coloring found this round; record as a
fallback within GAP-C, not a standalone approach.

**Dead ends (do not retry as lower-bound framings):**
- (b) different Liu config — tower is the unique equality config, no easier near-tower.
- (c) dominance/majorization lattice — `D` not monotone under refinement (V-shape).
- (d) polynomial/root-of-unity — `D = P(−1)` is the LP-dual objective in disguise.
- (a) exact-absorption invariant `D_F ≥ 2C` — fails at minimizers (543/2196 T_4);
  the exact invariant is circular.

## Knowledge-base entries to use
- **Invariants & monovariants** (the XOR `D = D_F + D_R − 2C` is an exact
  decomposition, not a monovariant, but the induction `G1(n)→G1(n−1)` is a
  monovariant-style reduction on `n`).
- **Piecewise-concavity smoothing / breakpoint minimum** (`pl-breakpoint-minimum`:
  the min is at a breakpoint; the XOR overlap `C` is also a PL function of the
  cuts, so the same breakpoint reduction applies to `C`).
- **Pigeonhole / extremal principle** (the dyadic-misalignment lemma may reduce
  to a pigeonhole on dyadic intervals: the F-odd region, a union of `≤ n+1`
  intervals from splitting `2^n`, overlaps the `⌈n/2⌉`-many dyadic R-odd
  intervals; a counting/measure bound).
- **Hall's marriage theorem / SDR** (a matching reformulation of the overlap:
  charge each F-odd interval to a dyadic R-odd interval — the gaps-leftover
  charging, now on REGIONS not positions; may sharpen the dyadic-misalignment).

## Analogous past problems (cruxes)
- **`aimo-0019`** (paintful dyadic game) — crux: "Maintain a linear potential
  bounding cumulative resource by a constant times progress, proved by amortized
  induction that charges each frontier advance against the pieces it absorbs"
  + "Bound a family of dyadic-length pieces of pairwise distinct sizes by twice
  the largest, via the geometric sum of distinct negative powers of two." WHY
  analogous: a covering game on the line with dyadic-length pieces where a linear
  potential + dyadic geometric dominance proves the resource bound. The XOR
  framing's `D = D_F + D_R − 2C` is a linear-potential decomposition with the
  same dyadic-geometric dominance flavor; the "charge each advance against
  absorbed pieces" is the overlap `C`.
- **`aimo-0156`** (frog hops, dyadic step sizes) — crux: "Hops of size a
  multiple of `2^m` keep position fixed modulo `2^m`" (modular/residue invariant)
  + "Rewrite a weighted sum of counts as a sum of cumulative tail partial sums
  (Abel summation)" + "achieve extremal by splitting into evens/odds, each a
  scaled copy of the smaller instance (self-similar)." WHY analogous: the
  dyadic-residue-class invariant and the self-similar split-into-evens/odds are
  the SAME structures as the tower's self-similarity and the XOR decomposition's
  dyadic R-odd region. The Abel-summation rewrite (weighted sum = cumulative
  tails) is the layer-cake `D = ∫(N mod 2)dt` in discrete form.
- **`aimo-0131`** (funny subsets, `x+y` a power of 2) — crux: "Trap a pairwise
  sum strictly between two consecutive powers of two to force it to equal the
  unique power of two in that gap." WHY analogous: the dyadic-dominance margin
  `2^n > 2^n − 1` (the "1") is the same "consecutive powers of two" gap trapping;
  the self-similar restriction to `B_n` (the lower half) is the induction
  `G1(n) → G1(n−1)`.

## Prior progress
- 24 certified lemmas (see `current.md`). Lower bound closed for: case (a)
  top-unsplit, (b-i) single-split, (b-ii-dyadic) all-balanced, 2-split
  top-fragment, even-group strong breakpoints (2 independent proofs),
  block-condition cells (GAP-B telescoping mass identity), spine-3 cascade
  (GAP-A), clean types (LP-dual). `n=1` fully proved; `n=2,3` lower PARTIAL
  (GAP-C open). The XOR framing IMPORTS all of these as the inductive base
  (`D_R ≥ 1` for the below-top refinement is exactly the closed sub-cases at
  size `n−1`).

## Dead ends (do not retry)
- (b) different Liu config: tower is the unique equality config (run-state).
- (c) majorization/dominance lattice on refinements: `D` not monotone (V-shape).
- (d) `D = P(−1)` polynomial: = LP-dual objective (framing 4) in disguise.
- (a) `D_F ≥ 2C` exact-absorption sufficient condition: fails 543/2196 at T_4
  breakpoint minimizers (worst deficit `−6`); exact invariant is circular.

## Small-case / intuition notes (labeled CONJECTURE)
- CONJECTURE: the XOR identity `D = D_F + D_R − 2C` combined with strong
  induction on `n` (`D_R ≥ 1`) and a dyadic-misalignment lemma on `C` closes G1.
  Verified: identity exact (6000+ trials, 0 failures); `D_R ≥ 1` at base
  (min `D_R = 1` for `T_{n−1}` refinements); `D ≥ 1` holds (0 violations, all
  `n≤5`). NOT proved: the decoupled dyadic-misalignment lemma.
- CONJECTURE (weaker, PARTIALLY REFUTED): the R-odd region of a tower refinement
  is a union of dyadic intervals `[2^k, 2^{k+1}]`. REFUTED for general
  refinements: only ~37%/29%/24% of refined R have purely-dyadic odd regions
  (T_2/T_3/T_4); counterexample `R={5/8,15/8,3/2,2,1}` has odd region
  `[0,5/8]∪[1,3/2]∪[15/8,2]`. The dyadic structure holds ONLY for unsplit/dyadic
  R (= the already-closed sub-case). So the "dyadic-misalignment lemma" is NOT
  the clean path; the overlap bound for non-dyadic R is the genuinely open step
  and is G1(n−1)-equivalent. The XOR framing is a different attack ANGLE, not a
  shortcut — same logical status as GAP-LP2.
