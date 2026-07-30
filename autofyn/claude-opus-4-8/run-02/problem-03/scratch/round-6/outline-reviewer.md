# Outline review — imo-2026-03 (IMO 2026 P3), round 6

Field: 4 live slugs, 2 per wall, each a distinct closing MECHANISM for that wall's single
residual. potential-certificate stays retired (correctly). No new slug proposed, no branch/copy
requested — the two "revise (repoint)" fates keep their existing slugs. All 4 avoid every banked
dead end and each is a whole attempt at its bound direction end-to-end (shared spine + all cases,
differing only on the residual closer), so no single-gap-split trap. Verified the outliner's
critical numbers: the tie config Y=(8,3,3,2), Z=(8,2,2,2,1) gives altsum exactly 1 (non-strict
target is correct — no universal strict slack); and the Euclid one-shot pigeonhole gap c(k)Σ/(2k)
exceeds u_kΣ for k≥3 (ratio 1.33 at k=3 → 5.3 at k=6), which sharpens that slug's load-bearing risk
(see below).

---

## induction-recursion-telescope — APPROVE (GAP L leader)

Sound. The reserve-carry IH `P*(n)` is the right shape: a scalar `altsum(Z)≥1` is provably
insufficient (3 recorded counterexamples), and the per-scale local reserve `R_Z(τ)` carried down
Z's dyadic cut-tree is exactly the "per-scale certificate that survives interleaving" the explorer
identified (structural match to crux aimo-0493's per-dyadic-scale tag). The tie-normalization
precision fix (Step 3) is correctly folded in: canonical Y-before-Z tie-break, prove (♦) is
tie-break-invariant, push the exact-tie boundary `y₁=θ` into the already-closed region, target
non-strict `D̃≥1` with equality tracked. This directly obeys the run_state rule "no universal strict
slack — infimum is exactly 1 at ties." Mechanism for every named lemma is stated. Spine = certified
Lemma T machinery + the Structure Lemma (§5, flagged for promotion to lemmas/).

Load-bearing gap (correctly isolated as THE remaining GAP-L gap): Step 5 — proving `P*(n)` closes
under the Structure-Lemma descent at θ/2, i.e. each T-run's width-weighted deficit is dominated by
the matched anchor subtree's banked reserve. Watch item: the match must be WIDTH-weighted, not
count-weighted (near-equal T-runs have tiny internal width / near-0 deficit) — the outliner flagged
this. Cases (a)–(d) are complete and disjoint. Build it.

## induction-recursion — APPROVE, with a diversity caveat (GAP L, repoint to budget-count)

The repoint is legitimate, NOT cosmetic. The prior exchange/difference-function `h` route is
genuinely dead (fragment-count obstruction `h(0⁺)≤1−2b≤−3` for b≥2, re-confirmed airtight by the
explorer this round). The swap-in — a one-shot global combinatorial budget count (run peaks vs
Z-anchors, both bounded by `a+b≤n`) on the (♦) form — is a different proof STRUCTURE from
telescope's recursive descent: one is a single global pigeonhole, the other a level-by-level
recursion. That satisfies the round-4 memory rule (two distinct mechanisms on one residual when no
orthogonal top-level route exists).

Caveat the builder must respect, and the orchestrator should watch: both GAP-L slugs ultimately
target the SAME inequality — "T-run deficit ≤ anchor surplus" (width-weighted). The mechanisms to
PROVE it differ (recursion vs global count), but if that inequality itself is the wall, both die
together. This is the shared-wall risk the plateau rule warns about. Acceptable for one round
because the two proof mechanisms are genuinely distinct, but if BOTH stall on the width-weighted
domination next round, escalate: the field will have collapsed and GAP L needs a genuinely
different framing, not a third mechanism for the same inequality. Step 4 (the width-weighted count)
is the gap; the outliner correctly forbids a pure run-vs-anchor count ignoring widths (refuted by
the near-equal-run counterexample) and requires the Structure Lemma for anchor heights (scalar/count
summary of Z refuted). Build it, but keep it on a short leash.

## dyadic-discrepancy — APPROVE (GAP U leader)

Sound and the strongest line in the field. Pin-top-2 is the only GAP-U opening with real empirical
legs (0/1058 broad, 1/1117 tight-residual per the explorer). Crucially, the outliner does NOT
propose the refuted naive splice: it explicitly records that `u_{k−1}·(Σ−2ℓ₂)` reduces algebraically
to Case (ii) and fails 100% on the residual, and instead demands a genuine two-parameter potential
`ψ(k,β)` (β = top fraction) with `ψ(k,c(k))=u_k`, non-increasing on β<1/2, and a verified recursion
into `ψ(k−1,β′)`. That is the correct "post-merge remainder improves" content the explorer said must
be supplied. The k=4 near-miss (ratio 1.039 at parts≈[0.483,0.168,0.151,0.117,0.081]) is flagged as
a mandatory build obligation — reproduce via gate2d_residual_region.py and prove the chosen escape
branch (pin-top-3, or a secondary (iii-b) split) kills it; the outliner bars submitting bare
single-pin-top-2. Cases complete (dominant / balanced-top / still-balanced + near-miss + ℓ₁=ℓ₂ free
pair). Gap = Step 2 (define/verify ψ). Build it.

## dyadic-discrepancy-euclid — APPROVE, with a sharpened load-bearing warning (GAP U, repoint to Euclidean difference-coin)

The repoint away from the accumulator schedule (a near-duplicate of the twin's Pivot Lemma closure)
to a CONSTRUCTIVE Euclidean difference-coin descent is genuinely far apart in framing from
pin-top-2's inductive potential: one exhibits an explicit legal op-sequence reaching a single
reachable effective total ≤u_kΣ, the other induces on a potential. Good — this is what the plateau
rule wants for the GAP-U wall. The outliner correctly bars the two refuted detours: no global
mesh-coverage bound (mesh not globally ≤u_kΣ, gaps up to 2× just outside the window) and no
region-restricted concavity/LP (37–42% violations). Only a single constructive reachable point is
claimed. The near-equal-pair base case is grounded in the explorer's actual (iii-b) optima.

SHARPENED WARNING (make this explicit to the builder). I verified the constant: the one-shot gap
pigeonhole `Σ(ℓ_i−ℓ_{i+1}) < c(k)Σ/2` over k gaps gives a gap `< c(k)Σ/(2k)`, and
`[c(k)Σ/(2k)] / u_kΣ = 2^{k−1}/k`, which is 1.33 at k=3, 2 at k=4, 3.2 at k=5. So the single-gap
pigeonhole does NOT reach u_kΣ for k≥3 — the "just find a small consecutive gap" base is provably
insufficient on its own. The slug therefore LIVES OR DIES on the ITERATED subtractive descent
(replace two largest coins P≥p by P−p, repeat) driving the residual strictly below the finest gap
WITHIN the ≤k op budget. That is exactly the outliner's flagged open gap (Step 3 + op-budget
accounting), and it is the real risk: a subtractive Euclidean chain on reals can take many steps and
overrun k ops. The builder MUST bound the chain length against the budget, not just assert
termination. Treat this as CHANGES-REQUESTED-grade difficulty: build it as the diversity bet on the
GAP-U wall, but if the op-budget bound can't be produced, this slug is the first to cut next round.

---

## Field diversity note (for the orchestrator)

Both walls now run the SAME pattern: two distinct mechanisms attacking one shared residual, and on
each wall the two mechanisms share a common target inequality (GAP L: "T-run deficit ≤ anchor
surplus"; GAP U: "reach ≤u_kΣ on ℓ₁<Σ/2"). This is the correct response to the R4 plateau flag while
no orthogonal top-level route exists (explorer confirmed none). But it is one round of runway: if
next round the two GAP-L mechanisms both stall on the width-weighted domination, or the two GAP-U
mechanisms both stall on ℓ₁<Σ/2, the field has genuinely collapsed to one wall per bound and the
outliner must be told to seed a genuinely different framing for that residual — not a third
mechanism for the same inequality.

## Ranking (Elo after this round's head-to-head)

dyadic-discrepancy 1634 > induction-recursion-telescope 1519 > dyadic-discrepancy-euclid 1535 >
induction-recursion 1474. (Note: euclid 1535 sits just above telescope 1519 by Elo, but I ranked
telescope ABOVE euclid head-to-head this round — telescope is the closer-to-solved, cleanly-specified
GAP-L leader with certified Lemma T, whereas euclid's repoint carries the proven one-shot-pigeonhole
constant obstruction; their ratings are converging accordingly.) potential-certificate untouched
(retired, not sampled). No new registrations, no copies.

build set: induction-recursion-telescope, induction-recursion, dyadic-discrepancy, dyadic-discrepancy-euclid
