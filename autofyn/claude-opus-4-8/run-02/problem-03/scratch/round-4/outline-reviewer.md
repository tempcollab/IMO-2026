# Outline review — imo-2026-03 (IMO 2026 P3), Round 4

Context: answer, reduction `c(n)=(1+D*)/2` with `D*=u_n`, and the whole certified spine (Lemma G,
level-measure identity, Cut-Flip, Invisible-Pair, removal-ops + Residual-Total Theorem, threshold
block-decomposition (★)(★★)(◇◇)) are PROVEN and shared. n=1,2 fully solved. Two independent walls
remain — GAP U (upper bound / Xiang strategy) and GAP L (lower bound / Liu's dyadic) — each reduced
to a single precise residual research step. Both walls advanced in Round 3 (no proof-reviewer ran,
so the advances were never folded; I have folded them into the Elo this round: dyadic-discrepancy
and induction-recursion both rose off their round-1 ratings).

Structural note (not a defect): no single slug is a standalone whole solution because "determine c(n)"
inherently needs an upper bound AND a construction. The field correctly splits into two whole
sub-theorems (each slug owns one direction end-to-end + imports the shared certified spine). This is
the bound+construction decomposition the problem demands, NOT the single-gap-trap (the two walls are
independent theorems needing different objects — a Xiang strategy vs a Liu partition — not one proof
farmed out). To SOLVE, one upper twin and one lower twin must each close; diversifying each wall
across two distinct mechanisms is the right anti-plateau move.

The orthogonal explorer confirmed no genuinely different top-level framing exists (scale-invariance
≡ induction-recursion's recursion; surrogate-adversary ≡ dyadic-discrepancy's RT; the 2-adic recast
is unconstructed and near-circular). I concur — I do NOT force a cosmetic third framing this round.
Instead the two walls each get two distinct-mechanism twins. This is acceptable given the explorer's
diversity finding, but I flag for the orchestrator: if BOTH twins on a wall bottom out on the same
residual next round, that wall has truly collapsed to one obstruction and the orchestrator should
escalate the 2-adic recast (Candidate 3) as a genuine research assignment despite its circularity risk.

---

## dyadic-discrepancy — revise (GAP U, Case (iii) balanced regime) — APPROVE

Technique: Residual-Total induction closed by a **disjunctive reserve-buffer invariant** (aimo-0340
template) replacing the single fragile inequality.

- Right technique. The round-3 builder proved a rigorous obstruction: black-box single-move + RT(k−1)
  (and any max-total greedy) telescopes to `2/((k+1)(k+2)) > u_k` for k≥3. A strengthened IH that
  credits post-move balance is exactly the correct response, and aimo-0340 is a genuine structural
  match (cut-budget process, single survival inequality breaks at one transition, fixed by a
  two-clause invariant carrying a reserve). Load-bearing lemmas (post-move balance, reserve invariant)
  are each stated WITH a mechanism, not a bare label.
- Does NOT smuggle back the refuted routes: the skeleton explicitly avoids max-total greedy and the
  naive `W=2^{-#cuts}` standalone (off by ~2×, Finding 4), and the "watch out" list correctly pins
  the recursion factor at `1/(2+u_{k−1})`, not ½.
- Issues to close while building (CHANGES-REQUESTED-level, not blocking):
  1. Steps 3–4 (the exact second clause (b) + self-restoring transition) are the genuine research
     step — honestly labeled as such. The reserve clause must carry ACTIVE extra structure; if it
     degrades to plain greedy it telescopes above u_k at k=3. Verify the disjunction holds with
     EQUALITY on the dyadic boundary (dyadic is tight).
  2. The "slack sufficiency" fallback (Finding 2: 12–28% interior slack) is a legitimate cheaper
     target — but note the dyadic BOUNDARY has zero slack, so any non-tight bound must still be sharp
     at the Case-(i)/(iii) interface. Do not let the fallback quietly weaken the boundary case.

## dyadic-discrepancy-euclid — copy-of dyadic-discrepancy (GAP U, Case (iii)) — APPROVE (with a mandatory empirical gate)

Technique: an explicit deterministic **chained-pin / Euclidean-subtraction** Xiang schedule (pin
current largest against a small piece; continued-fraction-style decay of the top fragment) driving
residual total ≤ u_kΣ.

- Genuinely distinct from its source, not a near-duplicate: a CONSTRUCTIVE deterministic strategy vs
  a strengthened existence-IH. A concrete op-schedule is a different object and, if it works, more
  directly citable. The explorer's Finding 1 (solver traced pin(ℓ₁,ℓ₃)→pin(·,ℓ₄)→pin(·,ℓ₂), never a
  bisect) is real evidence this route differs in kind. Worth the parallel build — KEPT, not cut.
- It is NOT the refuted max-total greedy: it pins the top against a SMALL piece (removes only 2ℓ_min
  but does "long division" on the top), the opposite of peeling the largest chunk. The skeleton
  explicitly forbids reintroducing max-greedy. Good.
- MANDATORY gate before investing (blocking for this slug's build): the canonical pivot rule is NOT
  yet pinned down — Finding 1 is a SINGLE trace, and its optimal order was "pin against ℓ₃ first,"
  not strictly-smallest. The builder MUST first run `/tmp/round-4/rt_search.py` on many Case (iii)
  instances at k=3,4 to determine the correct deterministic pivot order empirically. If no single
  deterministic rule reproduces the solver's optimum across instances, this route has no fixed
  strategy to prove and should fall back to advancing the source twin. This is why it ranks just
  below its source.
- Steps 3–4 (the explicit (r_j, top_j) recurrence + "dyadic is the worst case for the chain") are the
  research step — honestly labeled. The "dyadic is the fixed point of the pin-recurrence" mechanism
  is stated and plausible; must be proven, not asserted.

## induction-recursion — revise (GAP L, doubly-balanced GAP-LB′) — APPROVE

Technique: Case-B induction closed by a **vanishing-fragment exchange** — at the D̃-minimum, push
the smallest top-fragment y_min→0, collapsing a top cuts to a−1, bottoming out at Case A.

- Right technique, not circular. Compactness+continuity gives an attained minimizer (D̃ is
  piecewise-linear on a compact simplex); the downward-a induction terminates at the PROVEN Case A.
  The only research step (the exchange lemma) is isolated and honestly labeled. Strong numerical
  support: every observed minimizer drives y_min→0.
- Correctly avoids the recorded dead ends: it does NOT invoke global monotonicity (refuted, Finding
  3 — f is jagged); the exchange is explicitly a LOCAL single-coordinate boundary argument, and the
  mechanism (y_min's contribution to the alternating level-sum is a boundary term of definite sign)
  is stated, not hand-waved. It does NOT rely on any scalar strengthening of Z.
- Issues to close while building:
  1. Case coverage: the exchange must handle y_min interior to Y's order vs y_min global-smallest,
     plus ties — flagged, must actually be executed for both.
  2. Watch (b): after y_min's mass is merged into the adjacent T-fragment, that fragment must stay in
     (0,θ] or the induction leaves the region. Watch (c): the a→a−1 reduction must not smuggle extra
     cut budget onto Z. Both are correctly flagged; the builder must verify, not assume.

## induction-recursion-telescope — copy-of induction-recursion (GAP L, GAP-LB′) — APPROVE

Technique: merged-order **head/tail telescoping** `D̃ = [sum(Y_head)−sum(Z_head)] + [tail alt-sum ≥0]`
closed by a **two-level joint induction on Z's recursive dyadic cut-tree** (Z=Y′⊎Z′ at θ/2) bounding
T-run mass.

- Genuinely distinct from its source: a merged-order signed-sum induction on Z's cut-tree, vs a
  compactness/exchange argument on the level-measure functional. The explorer explicitly listed these
  as two separate live sub-openings ((a) and (b)) worth a slug each. KEPT, not cut.
- CRITICAL — does NOT smuggle back the refuted scalar lower-bound: the explorer PROVED
  `D̃ ≥ sum(Y)−sum(Z)` is FALSE for a scalar-summarized Z (three counterexamples, probes 5–7,
  including full sum+bound+D_bot≥1 constraints). The skeleton's Step 4 sub-claim ("head covers
  Z-mass ≤ sum(Y)−1") is exactly the shape of that refuted claim IF taken as a free-standing
  two-multiset lemma — and the outline's "watch out (a)" explicitly forbids that: Step 5 MUST prove
  it via Z's recursive cut-tree, never as a bounded-multiset fact. This guard is correct and
  load-bearing; the builder must honor it or the approach is dead.
- Issues to close while building:
  1. Step 5 (bounded-T-run mass from Z's cut-tree) is THE research step; the explorer could not close
     it and warns this is precisely where a counterexample-style loss hides (a T-run of near-equal
     values contributes ~0, not its sum). The two-level joint induction must actively use that Z's
     dyadic anchors prevent long T-runs — this must be proven, not asserted.
  2. Case coverage: both leading-T,T merges (n=3, a=1,b=2, Y=(4,4)) and strict-alternation-then-tail
     (n=3, a=2,b=1) occur at minimizers; both must be covered. Keep every inequality equality-robust
     (D̃=1 is attained on the zigzag family).

---

## Twin verdicts (as requested)

Both copies earn their parallel build — each is a genuinely distinct mechanism on its wall, not a
near-duplicate that would double cost on the same idea:
- **dyadic-discrepancy-euclid**: constructive deterministic schedule vs strengthened IH — distinct.
  KEPT, but gated on the empirical pivot-rule verification (blocking) before the builder commits.
- **induction-recursion-telescope**: merged-order signed-sum induction on Z's cut-tree vs
  compactness/exchange — distinct, and explorer-endorsed as a separate sub-opening. KEPT.

Nothing doomed was smuggled in: the refuted scalar lower-bound fill and the refuted max-total greedy
are both explicitly excluded by the outlines. concavity-lp (dead/unregistered) and
potential-certificate (retired) were NOT resurrected; potential-certificate stays registered but
ranks at the bottom (retired/near-duplicate, loses to every live sibling).

## Ranking (folded this round; both R3 advances now reflected)

1. dyadic-discrepancy — 1598 (leader; advanced R3, reduced GAP U — the crux — to the single Case (iii))
2. dyadic-discrepancy-euclid — 1553 (twin; distinct constructive route, gated on empirical pivot check)
3. induction-recursion — 1516 (advanced R3, enlarged closed region, sharpened GAP-LB′)
4. induction-recursion-telescope — 1495 (twin; hardest residual step — T-run bound — but distinct)
5. potential-certificate — 1396 (retired near-duplicate; not built)

## Field-diversity note for the orchestrator

The field is well-separated ACROSS walls (upper vs lower) but each wall's two twins attack the SAME
residual (Case (iii) for U; GAP-LB′ for L) with different mechanisms. That is intended anti-plateau
insurance, not collapse. Watch for: if, after this round, both twins on either wall stall on the same
residual, that wall has genuinely collapsed to one obstruction — escalate the 2-adic recast
(Candidate 3) or a fresh framing rather than a third same-wall mechanism.

build set: dyadic-discrepancy, dyadic-discrepancy-euclid, induction-recursion, induction-recursion-telescope
