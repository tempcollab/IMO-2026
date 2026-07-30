# Outline review — imo-2026-03, round 12

Answer CONFIRMED c(n)=2^n/(2^{n+1}−1), minimax D=u_n. Two open walls: LOWER MID-core (D(S)≥1 for
|F|≥3) and UPPER Covering claim (min R(A)≤u_nL in the balanced valley). Three whole families are
dead (scalar-reserve R10, structured-matching R11, dispersion-density R11). The field offers two
genuinely-far-apart LOWER mechanisms + one UPPER advance + retirement of the dead ballot vehicle.

---

## merge-interleave-pattern (LOWER, revise) — CHANGES REQUESTED (approve to build, with fixes)

Verdict: build it. The LP-vertex / active-constraint-rank mechanism is genuinely distinct from all
three dead lower families (transport, scalar potential, termwise monovariant), and it re-uses the
SAME machinery (breakpoint-vertex's Theorem VERT) that the reviewer already certified
profile-independent on the upper wall — so the technique is known to work on this problem's objects.
The mandated cheap-kill (enumerate vertices of the lower interleave polytope for n=3,4, verify the
minimum) directly de-risks the actual PROOF mechanism, not just the (already-known-true) claim. That
is the decisive reason it outranks its lower sibling for the build slot.

Fixable issues the builder MUST address:
- **GAP-EXTR is over-stated (skeleton step 4 / Key lemma).** "Every vertex of P_w is a canonical
  one-fragment-per-gap interleave whose value telescopes to exactly 1" cannot be literally true — D
  is not constant across words (Case (a) alone gives D=2^{n−1}), so not every vertex has value 1.
  The correct load-bearing claim is: over ALL reachable words w and ALL vertices of P_w,
  min L_w ≥ 1, with equality attained only at the canonical one-F-per-gap layouts. Restate GAP-EXTR
  as a lower bound at every vertex, not "every vertex is canonical."
- **Cheap-kill must test the right predicate.** The n=3,4 enumeration must check that NO vertex of any
  reachable P_w gives L_w = Σ_{i odd}w_i < 1 (and that the minimizers are the canonical interleaves).
  Testing only "all vertices are canonical" (as the current watch-out says) would falsely fail on
  every non-minimizing word. Gate: if any vertex yields L_w<1, this dies exactly like HALL-ENDPOINT
  (clumped excursion spread to non-adjacent scales) — record and retire. Do NOT write prose first.
- **GAP-REACH (step 2c) is load-bearing and only sketched.** The ONE-REC per-scale single-excursion
  constraints must be exhibited as explicit LINEAR inequalities in the gap-length vector, proven from
  the sum + ladder — not asserted. This is what makes P_w a genuine polytope; if these constraints
  are non-linear the vertex argument collapses.

Imports (R/M/TB/MID/OSR/CLIP/ONE-REC) are all certified — no re-derivation. Distinct polytope from
breakpoint-vertex's (interleave of two cut multisets vs single reachable set), different wall — not
the same gap, so no single-gap-trap double-up with the upper build.

---

## f-partition-majorization (LOWER, new) — CHANGES REQUESTED, but HELD from the build set

Verdict: register (done) and keep live in the population, but do NOT spend a builder on it this
round. Reasons:

- **The make-or-break GAP B-MONO's stated mechanism appears FALSE as written.** The skeleton
  justifies "min_B D(F,B)≥1" by claiming "a B-cut's effect on μ{g odd} has support in a single
  dyadic gap, so the min-B is at one aligned configuration." I checked this analytically: cutting a
  B-piece of length ℓ into (x, ℓ−x), WLOG x≤ℓ−x, changes N_B(t) by +1 on [0,x), 0 on [x,ℓ−x), −1 on
  [ℓ−x,ℓ). So g=N_F−N_B flips parity on TWO disjoint intervals — [0,x) near 0 AND [ℓ−x,ℓ) near ℓ —
  which generically lie in DIFFERENT dyadic gaps. The "single dyadic gap" localisation is not true in
  general, so the exchange step that was supposed to give the decomposition "teeth" does not obviously
  hold. This is precisely the collapse the explorer and outliner both flagged (GAP B-MONO risks being
  full MID-core restated).
- **Its cheap-kill only reconfirms the claim, not the proof.** The mandated "exhaustive multi-cut
  B-search, confirm min_B D≥1" (n=4,5) at best re-verifies a fact the field already knows numerically
  (explorer: 0 violations of D≥1). It supplies NO evidence the localisation mechanism works — unlike
  merge-interleave's cheap-kill, which de-risks the actual mechanism. So even a passing gate leaves
  the real gap wide open.
- **Building both lower slugs this round is the single-gap trap in disguise.** Both target MID-core
  D(S)≥1; f-partition's route currently reduces (via a broken localisation) toward full MID-core,
  which is exactly where merge-interleave's vertex argument also lands. The mechanisms are nominally
  far apart, but f-partition has no de-risked path yet, so pairing them risks two builders bottoming
  out on the same wall.

What to change before it earns a build slot (next round, via the outliner): repair or replace the
localisation mechanism for GAP B-MONO — the two-interval support of a B-cut must be handled honestly
(e.g. a genuine majorization/Schur argument on the joint (F,B) profile, or a proof that the two
parity-flips can only raise μ{g odd}), OR retire if it cannot escape being MID-core restated. The
c_B=0 majorization slice (Lemma MAJ) is fine as far as it goes but the explorer proved c_B=0 is NOT
WLOG (42.8% of one-cut B's strictly lower D at n=5), so MAJ alone is provably incomplete.

---

## breakpoint-vertex (UPPER, advance) — CHANGES REQUESTED (approve to build)

Verdict: build it. It is the live upper leader (now top of the field at Elo 1719 after de-throning
the dead-family parity-measure), with CONF and MD2 freshly certified, and GAP TWO-CAP builds directly
on those two lemmas. The two-cap covering-radius route is the least-explored surviving upper
direction; opening 1 (MATCH-two-smallest) was numerically REFUTED this round (fails 100%/99.5% at
n=2/3, exactly where induction starts) and is correctly off the table.

Issues the builder MUST address:
- **GAP TWO-CAP is UNVERIFIED and is the exact make-or-break.** R10 already refuted the one-cap
  covering-radius ≤ a_i/2 bound (saturates at a_{n+1}/2 ≫ u_n). The claim that using the second cap
  a_i≤a₂<β_nL at EVERY level (not just the top) makes the radius genuinely halve to u_nL is plausible
  but untested. HARD GATE (per the outliner and the R11 de-risking rule): numerically validate the
  exact recursion inequality c_i≤f(c_{i-1},a_i) telescoping to u_nL on random valley profiles n=2..7
  BEFORE any prose. Note the explorer's numerics (worst covering ratio 0.3–0.8) confirm the covering
  TARGET holds with margin, but say NOTHING about the recursion — that is the unverified content.
- **Step 4 (covering radius → nonempty-T value ≤ u_nL) must exclude T=∅ explicitly.** The explorer
  found the exact bug: including the "skip everything" branch falsely yields min=0 on 100% of trials,
  but T=∅ needs n+1 deletes with only n cuts — infeasible. The conversion must produce a NONEMPTY-T
  reachable value.
- **Do NOT lean on forced collisions / exact 0.** R11 killed the collision regime as a broad
  mechanism (exact 0 is measure-zero, 0/~8500 generic trials). The content must be a worst-case bound
  on a strictly-positive covering radius, with exact-0 folded in only as one easy tied boundary case —
  not elevated to a parallel mechanism. The outliner correctly incorporated this.

Different wall and different object from merge-interleave — no single-gap-trap with the lower build.

---

## ballot-matching (retire) — CONFIRMED

RETHINK stands (R11): the structured debit→credit transport/Hall mechanism is provably dead
(HALL-ENDPOINT 49% fail; GAP-TERMINAL premise S_m<0 false). Its defining mechanism is exactly what was
refuted, so there is no re-plan. Left in the population as dead-end (Elo now 1469); not built. Do NOT
rebuild parity-measure-potential either (Elo 1712 but its entire scalar-reserve family is dead).

---

## Field diagnosis (for the orchestrator)

- Stale-leader lock-in corrected: breakpoint-vertex (1719) is now the ranked leader over the
  dead-family parity-measure (1712); the ranking finally reflects that parity's mechanism is dead.
- Diversity: LOWER now has ONE de-risked live vehicle (merge-interleave, LP-vertex) plus ONE held
  reserve with a genuinely different framing (f-partition, majorization) — good separation, but note
  BOTH still terminate at MID-core D(S)≥1. If merge-interleave's cheap-kill fails, the lower wall has
  no de-risked vehicle left; next round the outliner must either repair f-partition's B-MONO
  mechanism or seed a fourth, structurally-different lower reformulation (the plateau NOTE in
  run_state flags this convergence risk).
- One vehicle per wall this round, per the single-gap-trap rule: merge-interleave (LOWER),
  breakpoint-vertex (UPPER).

build set: merge-interleave-pattern, breakpoint-vertex
