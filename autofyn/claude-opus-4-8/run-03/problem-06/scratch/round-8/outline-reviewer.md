# Outline Review — imo-2026-06, Round 8

Field of four (3rd collapse of the crux to ONE wall: ¬(FIN-Q) / crisp value inequality
"no minimal covering set containing a large prime realizes ≥ a_1"). The outliner correctly
put four GENUINELY DIFFERENT mechanisms on that one wall (transversal minimality / value
descent / value-difference counting / finite-state revisit). My job: keep the field diverse,
cut the parasitic, avoid the single-gap trap.

Numeric sanity (this round): greedy sim, a_1∈{15,35,99,231,105}, 400 terms each — **zero bad
terms** (CSP holds), consistent with ℰ-small-only and the crisp value inequality. So none of
the approaches rests on a false conjecture.

---

## minimal-cover-small-only — APPROVE (NEW, priority build)

**Whole attempt?** Yes — targets the full P6 claim via (CSP), gaps and all.

**Skeleton sound?** Verified. Steps 1,2,3,5 are gap-free from certified lemmas:
- Step 3 (C covering + finite ⟹ contains an edge C'∈ℰ): valid, self-dual clutter / DCC well-ordering.
- Step 5 closure: C'⊆[2,P_max] (the gap) ∧ C'⊆C ⟹ C'⊆C∩[2,P_max]=S(m_0); superset of a covering
  set is covering ⟹ S(m_0) covering, contradicting m_0 bad. **Logically valid, not circular.**
- Entry lever F1' checks out and is even cheaper than stated: C covering ⟹ C meets a_1's color P,
  and q∉P, so C∩P≠∅ (every large-prime edge also carries a prime of a_1). One line from "C covering."

**The gap (step 4, ℰ-small-only) — genuinely different mechanism, but crux-equivalent-or-STRONGER.**
Per the dispatch's explicit ask: ℰ-small-only *implies* the crisp value target (if no large-prime
minimal cover exists, none realizes ≥a_1), so it is at least as strong — it does NOT make the wall
disappear, it relocates it to a stronger, cleaner statement. The essential-witness monovariant is
NOT well-founded yet (primes are unbounded upward — the same "no downward quantity" difficulty that
has stalled every prior route). **However**, the payoff is real and is exactly the diversity mandate:
this is a *pure transversal* attack with **no value induction**, and it **bypasses Lemma 9's a_1-threshold
stall** entirely (the wall that killed value-descent for 3 rounds). It also survives Prop D honestly:
the §3 lever uses "a_1 is a term" (value-dependent), so it is not resurrected pure-Helly. Build it.

**What to change / watch (for the builder):**
- The monovariant MUST be strictly DOWNWARD well-founded (largest prime, |Q_C|, or ∏Q_C) — an
  upward-ascending q_k→∞ quantity stalls exactly as the refined star did. This is THE gap; do not
  hand-wave "then it follows."
- Cover |Q_C|≥1 in general (edge with several large primes), not just the singleton — GPC already
  superseded the singleton "Lemma A".
- Do NOT reintroduce value-descent here (that is covering-small-part-descent's lane) — keep it purely
  set-theoretic so the two remain independent bets.

## covering-small-part-descent — APPROVE (ADVANCE, top live carrier, Elo 1660)

**Whole attempt?** Yes, via (CSP). Steps 1–6 + Lemmas 6,7,8,9 gap-free/certified.

**Distinct from minimal-cover-small-only?** Yes, deliberately: it keeps the **crisp VALUE inequality**
target (min realization ≥a_1 impossible), NOT ℰ-small-only, and attacks by value descent (Lemma 9),
not transversal existence. Different top-level target AND different mechanism — no single-gap trap
with minimal-cover-small-only. Correct call by the outliner.

**Gap (step 7 / 6b):** the value inequality tying a_1 to the covering structure. New lever
(Realization-vs-a_1 via Window Purity + essential witnesses B_p each ≥a_1) is a legitimate continuation.
Caution for the builder: the red-n explorer showed RED_n and Window Purity add NO new leverage here
(Window Purity is strictly weaker than the E_n-emptiness the descent already uses); the essential-witness
value pressure is the only genuinely new ingredient — lean on that, not on re-deriving Window Purity.

## bounded-window-distinctness — APPROVE (NEW, diversity build) with a CHANGES-REQUESTED caveat

**Whole attempt?** Yes, via ¬(FIN-Q). Steps 1,2,3,5 gap-free.

**Genuinely distinct from the dead Σ1/p²?** Yes. The dead route was global capacity as the CLOSER;
here the certified C1–C3 are re-scoped LOCALLY only to feed the real new mechanism —
**distinctness-by-difference** (q>window-length divides ≤1 term in a value-window, else q|difference,
0<|diff|<q). That is a VALUE argument, not a density count, and it is the one surveyed lever touching
values rather than abstract set-covering. Step 3 is valid and NOT circular.

**Gap (step 4, window localization) — honest and structurally HARD; flag to the builder.** The witnesses
i∈W(r_0) live at arbitrarily large values (a_i→∞), so distinctness-by-difference only bites INSIDE a
bounded value-band, and clustering the infinite pool's new-prime contributors into such a band is
exactly what looks structurally false (they are spread over the unbounded sequence). Two specific
warnings:
- The foreign explorer proposed a cheap numeric pre-check of the clustering hypothesis, but note it
  **cannot be run**: no bad class is ever inhabited numerically (CSP holds on every seed), so there is
  no star config to observe — step 4 MUST be argued abstractly from Window Purity + linear growth, not
  validated empirically. The builder should not spend the round hunting for numeric confirmation.
- Do NOT conflate same-CLASS (differences are multiples of M, unbounded) with same-VALUE-WINDOW
  (differences < window length) — step 3 needs the value window; the outliner already flagged this.

This is the riskiest of the three built (its gap may be as hard as the wall), but it is a genuinely
new value-mechanism and the field needs the diversity — build it, gap stated honestly.

## window-purity-class-cycle — LIVE, NOT BUILT this round

**Not a fatal flaw**, but its ONLY new lever this round is to "import bounded-window-distinctness's
value-difference cap as the monovariant." That makes its Step-5 descent **parasitic on
bounded-window-distinctness's open gap** — building both would be the single-gap trap (they die
together on window localization). The foreign explorer independently confirmed the class-graph has NO
deterministic step map off the shelf (which large prime is used is not a function of the class), so
wpcc has no INDEPENDENT closing mechanism this round. Keep it live (Elo 1530) to pick up the
value-difference cap IF bounded-window-distinctness lands its gap; do not spend a builder on it now.
This mirrors round 7's convergence handling (wpcc / bad-residue-witness-index).

---

## Diversity note for the orchestrator

This is the **3rd collapse to one wall**. The three built approaches are genuinely far-apart
MECHANISMS on it — pure transversal (minimal-cover-small-only) / value descent
(covering-small-part-descent) / value-difference counting (bounded-window-distinctness) — which is
the correct response to the collapse. But be warned: minimal-cover-small-only's gap is
crux-equivalent-or-stronger and bounded-window-distinctness's clustering gap may be as hard as the
wall. If ALL THREE stall next round, the field will have exhausted transversal / value-descent /
value-difference framings; the round-9 outliner should NOT add a 4th reformulation of ¬(FIN-Q) — it
should attack the value inequality with a growth-RATE / recruitment argument (the red-n explorer's
"each new distinct connector q_k must appear as a factor of some term within a bounded window, costing
one slot per a_1-length window" is a not-yet-tried framing distinct from all four current mechanisms).
The RED_n / reduced-process-identity route is confirmed by its explorer to be only a *repackaging* of
the same disjunction (Case I = crisp value target, Case II = ¬(FIN-Q) star) — do NOT unpark it as a
fresh attack; at most certify the Case-I/II bifurcation as an organizing lemma.

## Ranking (updated this round)
covering-small-part-descent 1660 > window-purity-class-cycle 1530 ≈ minimal-cover-small-only 1524
> bounded-window-distinctness 1482. (Newcomers anchored against the established top carrier;
wpcc/bounded-window drawn as they share the value-difference gap.)

build set: minimal-cover-small-only, covering-small-part-descent, bounded-window-distinctness
