## imo-2026-03 — LENS: GAP-P1′-a, the clean base-case inequality (★) Σ_{blue odd} ≥ Σ_{red even}

Scope: extremal base slice `b=0`, `F'=L={2^{n-1},…,2,1}` (uncut dyadic ladder, `ΣL=2^n−1`), `π_0`
any partition of `2^n` into `≤ n+1` parts. Target: `(★) Σ_{blue at odd rank} ≥ Σ_{red at even rank}`
in the descending merge of `π_0`(red) and `L`(blue); equivalently `I_n = Σ_{red even} − Σ_{blue odd} ≤ 0`.
All numerics below are exact `Fraction`, scripts in `/tmp/round-12/probe_*.py`.

### Headline: the RIGHT object is value-domination (weak majorization), not any positional charge/scan

- **NEW robust certificate — TOP WEAK-MAJORIZATION.** Let `BO` = multiset of blue-odd values,
  `RE` = multiset of red-even values (from the merged coloring). Sort each descending. Then for
  **every** prefix length `k`, `Σ_{top k of BO} ≥ Σ_{top k of RE}` (`BO` weakly majorizes `RE`).
  Verified with **0 failures**: exhaustive over all integer partitions `n≤6`, AND 280k random
  fractional `π_0` for `n≤8`, under BOTH tie-break conventions. This *implies* (★) (take `k`=all)
  and is strictly stronger. Equivalent Hardy–Littlewood–Pólya threshold form, also 0 failures:
  `∀t>0,  Σ_{v∈BO}(v−t)^+ ≥ Σ_{v∈RE}(v−t)^+`.
- **Why this dodges the refuted per-block charge (GAP-P1′-a's stated blocker).** The R11 dead charge
  `Σ_{red even} ≤ Σ_i⌈m_i/2⌉ b_i` is a *per-block, same-block* charge (51% fail). Weak majorization
  is a *global value-domination*: red-even mass is charged to blue-odd mass of ≥ value regardless of
  which ladder gap it sits in — exactly the "cross-block tail cancellation" the lens asks for,
  packaged as a majorization instead of an explicit injection.
- **Caveat (honest):** weak majorization is *stronger* than (★), so proving it is ≥ as hard in
  principle. Its value is that it (i) names the true mechanism (value-domination), (ii) has a
  standard toolkit (HLP / Karamata / doubly-substochastic transport), and (iii) may induct/smooth
  more cleanly than the raw scalar (★). The outliner should weigh proving weak-maj directly vs.
  using it only as the intended shape of an exchange argument (Opening B).

### Distinct openings

- **(A) Weak-majorization / HLP value-domination [strongest, NEW].** Prove `BO ≻_w RE`
  (descending partial sums, or the threshold form `Σ(v−t)^+`). The dyadic-dominance lever is
  `b_i = 2^{n-i} = 1 + Σ_{i'>i} b_{i'}` ("each rung = 1 + sum of all lower rungs") plus `m_0 ≤ 1`
  (at most one red exceeds `θ`, since two would sum `>2θ=2^n=Σπ_0`). Hard step: bound
  `Σ_{top k RE}` by the top-`k` blue-odd mass using this dominance at each threshold. This is a
  genuinely different top-level target from the R8–R11 profile/measure framings (those manipulate
  `M`; this compares two *value multisets*).

- **(B) Exchange-smoothing to the n+1 extremal profiles [strong, NEW structural handle].** The tie
  set `{D̃=1}` is EXACTLY, for every `n`, the `n+1` configs "`L` with one extra unit placed on one
  rung (or appended as a new part `1`)": e.g. `n=4`: `{9,4,2,1},{8,5,2,1},{8,4,3,1},{8,4,2,2},
  {8,4,2,1,1}` (verified `n≤6`). `D̃(π_0⊎L)=1+2(ΣBO−ΣRE)` is piecewise-linear in `π_0`'s parts under
  the fixed constraint `Σπ_0=2^n`. Opening: a unit/mass exchange that strictly lowers `D̃` whenever
  `π_0` is not one of these `n+1` profiles, descending to the minimum `=1`. This bypasses any charge
  entirely — it is a global monotone descent to a finite explicit extremal set.

- **(C) Abel/telescoping pairing of the signed merged sum [route b].** `D̃ = Σ_j(−1)^{j-1}w_j
  = Σ_{j odd}(w_j−w_{j+1})` over the descending merge. Pair consecutive merged elements so each
  intra-pair gap is a controlled non-positive/dominance term, leaving isolated boundary terms — the
  parity of the ladder's integer structure forces the leftover `≥1`. This is the summation-by-parts
  rearrangement the lens asks for; see the near-identical crux aimo-0388 below.

- **(C′) Induction on n peeling L's top rung θ=2^{n-1} [route c — UNCERTAIN, lower priority].** On
  `(0,θ)`, `N_L = 1 + N_{L'}`, `L'={2^{n-2},…,1}` the `(n−1)`-ladder. I did NOT find a clean
  recursion: `π_0` sums to `2^n` but `L'` lives at scale `2^{n-1}`, so the induction faces the same
  sum-doubling mismatch flagged for the general peel. Not refuted, but no working recursion found in
  this round — pursue only if A/B/C stall.

### Cheap-kill candidates (structural pruning to try first)
- `m_0 ≤ 1` (at most one red `>θ`) — already used above; keep it explicit, it pins the top of the merge.
- Parity: `D̃` is an integer for integer `π_0` (odd total `2^{n+1}−1`), so `D̃≥0 ⇒ D̃≥1` on the
  integer sublattice (Parity Lemma, certified) — but the residual is real-valued, so this only
  cheap-kills the integer probe, not the continuum.
- Dyadic dominance `b_i = 1 + Σ tail` is the one lever every route leans on — state it once as `(DOM)`.

### Candidate technique(s)
Hardy–Littlewood–Pólya weak majorization / Karamata; exchange-smoothing extremal principle;
Abel summation over a sorted merged sequence; dyadic "1 + tail" dominance.

### Knowledge-base entries to use
- **"Piecewise-concavity smoothing"** (Algebra section) — the "min of a piecewise-linear/concave
  functional is attained at a breakpoint / extremal profile" engine; directly powers Opening B.
- **"Invariants & monovariants"** and **"Induction: … structural"** (Combinatorics) — for B/C.
- **"Standard inequalities … equality cases pin the extremal configuration"** — the `n+1` tie
  profiles are the equality case to target.
(The KB has no explicit majorization/Karamata entry — worth the outliner citing HLP by name.)

### Analogous past problems (cruxes)
- **aimo-0146 [combinatorics, extremal-principle] — BEST match for Opening B.** Crux: "Maximize a
  fixed weighted sum of a sorted nonnegative sequence under a sum constraint by exchange-smoothing
  weight toward higher-coefficient positions until the free coordinates equalize and the tail
  drains, then enumerate the few surviving profiles." This is exactly "smooth `π_0` (fixed sum `2^n`)
  toward the `n+1` extremal tie profiles." The "enumerate the few surviving profiles" step maps 1-1
  onto our `n+1` tie configs.
- **aimo-0388 [combinatorics, telescoping-and-summation / extremal-principle] — BEST match for
  Opening C; structurally a baby-P3.** A coin 50-50 split minimizing `|val(A)−val(B)|`: crux "split
  a sorted sequence into two stacks by pairing consecutive elements so each pair's contribution is a
  non-positive gap, leaving isolated boundary terms," and "clustered extremes strain the balance,
  `2k−49` odd ⇒ `|diff|≥1`." This is an alternating signed sum over a sorted merge with a parity-forced
  `≥1` — the exact shape of `D̃=1+2(ΣBO−ΣRE)`.
- **aimo-0298 [combinatorics, extremal-principle] — the dyadic-dominance lever.** Crux "two gaps
  each ≥ the minimal scale sum to ≥ the next scale up" and the `2^{−r}` weighting — the geometric/
  dominance structure of `L`; adapt for `(DOM) b_i = 1 + Σ tail`.
- (Weaker) aimo-0003 [invariants-and-monovariants]: running `±1` tally reduced to adjacent
  transpositions — supports the exchange step of B, but the raw tally-minimum (ballot) route is
  dead here (see below).

### Prior progress (relevant to this lens)
(★-id) certified (`lemmas/ladder-interleaving-identity.md`); base case closed on `{M≤1}` (~88%),
the `(DIFF)` shell `|D̃(π_0)−D̃(L)|≥1`, and all `n=1`. `D̃(L)=(2^n−(−1)^n)/3`. Positive-layer bound
`P ≤ Σ_{k}y_{2k}` certified. The sole open residual of the base case is (★) on
`{M≥2 somewhere} ∩ {|D̃(π_0)−D̃(L)|<1}`.

### Dead ends (do NOT retry — verified THIS round for the ladder base case)
- **Per-block same-block charge** `Σ_{red even}≤Σ⌈m_i/2⌉b_i` — refuted R11 (51% fail); re-confirmed lossy.
- **Top-down positional reserve** (scan merge largest→smallest, blue-odd credit vs red-even debit):
  min prefix margin **grows negative** `= −3,−7,−15` for `n=4,5,6` (blue-first tie-break) — NOT a
  bounded buffer, DEAD. (Earlier note of "bounded deficit −1" was a script artifact of max-over-tiebreaks;
  corrected.)
- **Bottom-up positional reserve** (scan smallest→largest): min margin `= −2^{n-1}` — DEAD.
  ⇒ NO one-directional/positional scan certificate exists even for the ladder; the compensation is a
  value-reordering. This extends the R7/R9 reserve refutations to the extremal base case.
- **Termwise 1-1 domination** (k-th largest blue-odd ≥ k-th largest red-even): FAILS
  (e.g. `n=3, π_0=(2,2,2,2)`: `BO=[4,1]`, `RE=[2,2]`, `1<2`). Must use *partial-sum* (weak)
  majorization, not termwise — do not attempt a naive 1-1 value injection.

### Small-case / intuition notes (labeled: CONJECTURE unless said certified)
- CONJECTURE (strong, 0/all integer `n≤6` + 0/280k fractional `n≤8`): `BO ≻_w RE` (top weak
  majorization) ⇒ (★). This is the cleanest new opening.
- CERTAIN (enumeration `n≤6`): tie set `{D̃=1}` = exactly the `n+1` configs "`L` + one unit bumped
  onto one rung / appended"; number of ties `= n+1`. These are the only equality configs and the
  descent target for Opening B.
- Lever to state once for all routes: `(DOM) b_i = 2^{n-i} = 1 + Σ_{i'>i}b_{i'}`, and `m_0 ≤ 1`.
