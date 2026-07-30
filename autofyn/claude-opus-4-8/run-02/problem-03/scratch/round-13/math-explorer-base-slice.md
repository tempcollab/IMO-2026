## imo-2026-03 — LENS: closing (★) Σ_blue-odd ≥ Σ_red-even on the extremal base slice b=0

Scope per dispatch: terrain report only (no proof attempt). All numerics below exact `Fraction`,
scripts in `/tmp/probe{1..9}.py`.

### Route comparison: which is genuinely closer?

- **peel-scale-rank-induction §11 (weak majorization / HLP).** Status: names the right mechanism
  (value-domination, not per-block charge) and has a clean equivalent reformulation `(HLP)`
  `∀t: ∫_t^∞(N_BO(s)-N_RE(s))ds ≥ 0` via the "self-similar truncation" view (§11.2, correct — every
  top-truncation `P_t` is itself a merge of a red sub-multiset with a blue sub-ladder-suffix, so the
  same shape recurs at every `t`). But it bottoms out at the *identical* unproved step as before: "the
  odd-rank rungs surviving in `P_t` carry ≥ the even-rank red mass surviving in `P_t`, uniformly in
  `t`" (§11.4) — this is just (★) restated for every truncation, not a proof of it. No actual charging
  function or induction is exhibited. **It has not advanced past stating the target more strongly.**
- **ladder-abel-pairing.** Status: essentially the *same* open step from the opposite direction —
  "re-pair the alternating sum by rung so each odd rung's gap absorbs its whole lower even-red tail"
  (step 3) is again asserted, not built. No telescoped inequality is written down; "parity of `ΣL`
  odd forces the residual ≥0" is not yet a derivation (parity alone gives only integrality, not
  sign — see Dead ends below).
- **Verdict:** both routes are at the *same* place — they have correctly identified that the missing
  ingredient is "one odd rung dominates its whole lower tail, so charge the tail's red-even mass to
  it," but neither has written the actual charging/telescoping argument. Neither is closer in substance;
  they differ only in packaging (global tail-sum inequality vs. a partial-fraction/pairing rewrite of
  the same sum). This round I did NOT find a way to advance either as stated — see the NEW opening
  below instead, which is a genuinely different structural route that already produces two proven
  building-block identities.

### NEW opening (D): peel-the-top-rung recursive induction on (★) itself, generalized to deficient totals

This is a structural induction on the ladder length `m` (not on the peel-scale recursion already in
use for the whole GAP L problem — this is a *second*, nested induction living entirely inside the
base slice). It produces two **exact, unconditional, numerically 0-violation identities** that split
`(★)` into two branches by whether `π_0` has a part `> θ`:

**Generalized Ladder Lemma (NEW, conjectured, 0/32000 exact-`Fraction` violations, m=1..8).**
For the ladder `L_m = {2^{m-1},…,2,1}` and ANY red multiset `R` with `≤ m+1` parts and
`ΣR ≤ 2^m` (not necessarily `=2^m`!), `Σ_{blue odd} ≥ Σ_{red even}` in the descending merge.

This *generalizes* (★) (which is the case `ΣR = 2^m` exactly) to allow a **deficient** total. The
generalization is exactly what makes an m-induction close cleanly:

- **Branch 1 (some red `y_1 > θ=2^{m-1}`; at most one such red since `2θ ≥ ΣR`).** PROVEN identity
  (probe3, 0/18000 mismatches): removing the pair `{y_1, θ}` from the merge changes NEITHER `BO` nor
  `RE` — the pair occupies ranks 1 (red, odd, contributes 0) and 2 (blue, even, contributes 0) and
  everything below keeps its rank parity. The reduced config is red multiset `R\{y_1}` (total
  `ΣR - y_1 ≤ 2θ-θ=θ=2^{m-1}`, part count `≤ m`) against ladder `L_{m-1}`. **This is exactly the IH
  of the Generalized Ladder Lemma one level down** — a clean, closed induction step, no gap.
- **Branch 2 (no red `>θ`, so `θ` is the top element, rank 1, blue, odd).** PROVEN identity (probe9,
  0/6793 mismatches, verified independent of total): `BO = θ + BE'`, `RE = RO'`, where `BE',RO'` are
  the blue-EVEN and red-ODD sums (not blue-odd/red-even!) in the merge of the SAME reds against
  `L_{m-1} = L_m\{θ}` — removing one (odd-rank) element flips the parity of every later rank, so the
  roles of "odd" and "even" *swap* for the remainder. Target `(★)` becomes `θ + BE' ≥ RO'`, i.e.
  `RO' - BE' ≤ θ`. This is a genuinely NEW inequality — a **complementary-parity** statement, not an
  instance of the same-shape IH. It needs its own bound: since `BE'+BO'=ΣL_{m-1}=θ-1` and
  `RO'+RE'=ΣR`, it rearranges to `BO' - RE' ≤ 2θ - 1 - ΣR`, i.e. an UPPER bound on the very quantity
  the IH only lower-bounds. **This is the real open content of opening (D)** — a two-sided
  (upper-and-lower) strengthened IH is needed for Branch 2, exactly mirroring the general GAP-L
  pattern (need matching `Q≥P`, both directions) but now localized to a clean, self-contained,
  purely-about-the-ladder recursion with NO reference to `F'`'s cut-tree.

**Why this is a genuinely different opening from (A)/(C).** It is neither value-domination
(majorization) nor a rung-by-rung Abel pairing of the *whole* sum — it is a two-branch case split
that peels ONE rung (`θ`) and reduces exactly (Branch 1) or produces a dual complementary-parity
target (Branch 2), both purely combinatorial identities already proven with 0 violations. It is
self-contained (does not import the peel-scale induction's `F'`/dyadic-cut-tree machinery at all —
lives entirely inside `π_0` vs. a ladder) and gives the outliner two concrete proven lemmas plus one
sharply isolated open two-sided inequality (an UPPER bound on `BO'-RE'` in terms of `ΣR`), which is
narrower and more tractable-looking than the diffuse "tail-charge uniformly in t" of routes A/C.

### Cheap-kill / structural notes
- `m_0 ≤ 1` generalizes cleanly to the deficient-total lemma (two reds `>θ` sum `>2θ≥ΣR`).
- Without BOTH constraints (part count `≤ m+1` AND total `≤ 2^m`) the statement is FALSE: unconstrained
  total (probe5/6) fails ~40-60%, and unconstrained part count even with total `≤2^m` fails ~3.4%
  (probe8) — both constraints are load-bearing, not artifacts. Any induction/charging argument MUST
  track both simultaneously.
- The Branch-2 open target `BO' - RE' ≤ 2θ-1-ΣR` shows the upper bound gets HARDER (RHS smaller) as
  `ΣR→2θ` (the un-deficient, hardest case) — consistent with (★) being tight exactly at `ΣR=2^m`.

### Answer to the dispatched probing questions

- **Cross-block tail-cancellation mechanism / why (DOM) makes majorization plausible:** `(DOM)
  b_i = 1+Σtail` means each rung's value exceeds the sum of every smaller rung; combined with `m0≤1`,
  this is precisely the classical "largest exceeds sum of rest" dominance (crux aimo-0298, aimo-0917)
  that make a GREEDY top-down value assignment safe — it's why WEAK (partial-sum, sorted-by-value)
  majorization survives while POSITIONAL (rank-indexed, unsorted) domination fails. Partial-sum
  majorization of {BO} vs {RE} (sorted descending, prefix sums) tested directly: **0 failures** over
  18k (probe1, integer+fractional, n=2..7) and 0 more failures under an adversarial search that
  clusters reds just below each rung to try to maximize RE mass (probe2, n=2..9, 2000 configs/n). It
  robustly holds. Termwise (unsorted, k-th BO value vs k-th RE value by original position) is
  confirmed FALSE (n=3, π_0=(2,2,2,2): BO=[4,1], RE=[2,2], 1<2) — re-verified this round, matches R11.
- **Can the Abel/parity closer be made global?** I found no construction this round that escapes the
  "restate the target as a pairing/telescope, still unproved" trap for routes (A)/(C) — see Route
  comparison above. The genuinely new leverage this round is opening (D)'s two proven peel identities,
  which sidestep the "prove a global charge in one shot" difficulty by turning it into an ordinary
  two-branch induction on ladder length, at the cost of introducing a dual complementary-parity target
  in Branch 2.
- **Third framing (not on ban list):** opening (D) above qualifies — it is a direct
  cut-tree-flavored structural induction on `(★)` itself (peeling the top ladder rung, not on `F'`'s
  cut tree, and not reserved aimo-0917's game-invariant mechanism). The reserved aimo-0917 2-adic
  N=N_++N_- split (crux corpus, `invariants-and-monovariants`/`p-adic-valuation`) is a genuinely
  different mechanism (parity of a COUNT of sign-labelings, not of a value sum) but I found no natural
  translation of `(★)`'s value inequality into a countable "labeling" set this round — flag as
  still-unexplored, lower priority than (D) given (D) already has two proven lemmas.

### Candidate technique(s)
Two-branch case split + induction on ladder length (top-rung peel), generalizing (★) to allow a
deficient red total; HLP/weak majorization (routes A); Abel/summation-by-parts rung pairing (route C).

### Knowledge-base entries to use
- "Piecewise-concavity smoothing" / extremal-principle entries (as R12 explorer noted) — for
  routes A/B.
- No direct KB entry for "peel one extreme element, induct on residual with a role-swap by parity" —
  this is closest to standard induction-with-strengthened-hypothesis (KB "Induction: structural"),
  but the complementary-parity role-swap (Branch 2) is a distinctive move worth naming explicitly if
  the outliner adopts opening (D).

### Analogous past problems (cruxes)
- **aimo-0298** [dyadic dominance] — still the best match for `(DOM)`, reused across all three
  openings.
- **aimo-0917** [invariants-and-monovariants / p-adic-valuation] — the `N=N_++N_-` split-by-response
  mechanism (an odd/valuation-forcing count splits when one item is removed) is structurally
  reminiscent of opening (D)'s Branch-2 role-swap (removing the top element flips which half of the
  merge is "odd"), but it's a count-invariant not a value-sum, so treat as a loose structural analogy,
  not a literal template.
- **aimo-0388** — as R12 noted, best match for route (C)'s Abel pairing; not newly advanced this
  round.

### Prior progress (relevant to this lens)
(★-id) certified; base case closed on `{M≤1}` (~88%), `(DIFF)` shell, all `n=1`. Positive-layer bound
certified. NEW this round (unreviewed, not yet certified): the Generalized Ladder Lemma's two branch
identities (probe3, probe9, both 0 violations) — present to the outliner as candidate lemmas for a
NEW approach or as reinforcement of peel-scale-rank-induction §10.6/§11, not yet promoted.

### Dead ends (do NOT retry)
- Per-block same-block charge (51% fail, R11).
- Top-down / bottom-up positional reserve scans (margins → −2^{n-1}/−(2^{n-1}), R11/R12).
- Termwise 1-1 domination (FALSE, n=3 witness above).
- Unconstrained-total or unconstrained-part-count versions of the ladder lemma (this round,
  probes 5/6/8): dropping EITHER the total-≤2^m or part-count-≤m+1 constraint breaks it badly
  (12703/32000 and 724/21000 failures respectively) — any induction must track both jointly.

### Small-case / intuition notes (CONJECTURE unless stated proven)
- CONJECTURE (0/32000, m=1..8): Generalized Ladder Lemma (deficient-total (★)) holds.
- PROVEN (0 violations, exact identities, this round): Branch-1 pair-removal identity (probe3);
  Branch-2 role-swap identity `BO=θ+BE'`, `RE=RO'` (probe9), independent of total.
- CONJECTURE (0/18000 + 0/2000-adversarial-per-n): weak/partial-sum majorization `BO ≻_w RE` holds
  robustly, resists adversarial clustering at rungs — reconfirms R12's finding, no new
  counterexample found despite a targeted adversarial search different from R12's.
