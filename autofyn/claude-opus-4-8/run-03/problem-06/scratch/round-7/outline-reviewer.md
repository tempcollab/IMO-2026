# Outline Review — imo-2026-06, Round 7

Field: 2 NEW (window-purity-class-cycle, lex-rewrite-descent), 2 ADVANCE (covering-small-part-descent,
bad-residue-witness-index). All import the certified scaffold; none re-proves it. No approach secretly
routes through the proven-dead closures (static covering/Helly — Prop D barrier; global Σ1/p² capacity —
capacity RETHINK; aimo-0016 — proven non-transplanting). Gate constraints satisfied.

I independently sanity-checked the new load-bearing lemma **Window Purity** on a_1∈{15,35,99,231}: every
integer strictly inside a gap (a_n,a_{n+1}) fails gcd>1 with some term of the whole sequence — 0 violations.
It is in fact definitional from ENUM (the terms are exactly the increasing enumeration of E_∞∩[a_1,∞), so no
E_∞-element lies strictly between consecutive terms) and clause (c) supplies "covering ⟹ ∈E_∞". Certifiable
as claimed. Good.

---

## window-purity-class-cycle (NEW) — CHANGES REQUESTED, BUILD (mandated dynamics surface)

Verdict: the technique is right and this is the mandated GREEDY-DYNAMICS framing (spine uses how a_{n+1} is
chosen — the open gap (a_n,a_{n+1}) — not a static E_∞/covering fact). It is **not circular**: Step 5's two
closes (5a)/(5b) are honestly flagged UNPROVEN, and the outliner explicitly forbids the two circular traps
(q* floor does NOT itself give the descent; the symmetric bad-partner ascent gives no strict descent). The
skeleton is sound end-to-end: Step 1 (import FIN-W reduction, gap-free), Step 2 (Window Purity, certifiable
now), Step 3 (import certified star pigeonhole), Step 4 (single-sided-harmless ⟹ mutual/cyclic), Step 5
(finite class-graph must revisit — valid pigeonhole), Step 6 (contradiction). This is a whole end-to-end
attempt at the actual theorem, not a fragment.

Issues to close while building:
- **Step 4 "single-sided witnessing is harmless" is DERIVED-not-certified.** The builder must re-derive it
  from the certified Reduction Lemma (finite Q_rel bookkeeping) BEFORE relying on it — do not import it as a
  hypothesis. This is the same unverified claim bad-residue-witness-index leans on; certifying it here is a
  concrete deliverable for the whole field.
- **Step 5 is the real gap** — deliver, at minimum, (i) Window Purity as a certified cached lemma and (ii)
  the Step-4 mutual/cyclic reduction as a certified sharpening of the wall, EVEN IF (5a)/(5b) stay open. Do
  not overclaim a close that isn't extracted. For (5a) the strict prime DESCENT must be produced, not asserted
  from the q* floor. Respect the numeric caveat: "one hub blocks a whole window" is REFUTED — Step 5b must
  allow several blocking predecessors per interior integer.

## lex-rewrite-descent (NEW) — CHANGES REQUESTED, BUILD (genuine diversity)

Verdict: a genuinely different framing (constructive active rewrite / exchange operator on a lex-minimal bad
config), far from the FIN-W and value-ascent framings, and clear of every dead route. Not circular: Step 3(i)
uses REAL clause (c) (primes(A′) contains a covering set ⟹ A′ is a term) — a legitimate realizability use,
not the forbidden "peeled cofactor compatible with all earlier" hypothesis. The strict-descent asymmetry is
anchored to q*'s non-symmetric minimality (Lemma A), the exact lever the symmetric value-ascent lacked.

Issues:
- **Step 3 is the whole difficulty and is UNBUILT.** The existence of a covering-preserving, (q*,k)-lowering
  operator is entirely open. The builder MUST do the small-case operator search (a_1∈{99,231,1155}) FIRST and
  report honestly if no operator is found — this is an unverified transplant, expected to spend the round
  locating (or falsifying) the operator, not assuming it.
- Heed the flagged trap: dividing out a prime is not free (primes(A/r) may lose covering and fail clause (c));
  the rewrite must ADD a compensating covering prime. Do NOT reuse the symmetric bad-partner relation as the
  descent.

## covering-small-part-descent (ADVANCE) — CHANGES REQUESTED, BUILD (value/local-capacity framing)

Verdict: legitimate advance with two genuinely fresh ingredients ((A) local hub-cover, (B) Window Purity), so
it is not merely re-holding the partial. Distinct framing (value well-ordering + LOCAL finite-capacity on one
hub — explicitly never the dead global Σ1/p² sum). (6a) stays closed (Lemma 6); it targets only (6b).

Issues:
- The round-5 caveat stands and the outliner repeats it honestly: the missed-color-vs-|Q(h)| count does NOT
  obviously overflow (a bad term may miss ONE color with |Q(h)|=1). The builder must FIND the overflow or
  report it doesn't close — no hand-waved count.
- Regardless of whether (6b) closes, **local hub-cover (A) should be delivered as a certified reusable
  local-capacity lemma** (primes(h) covering while S(h) is not ⟹ the finite Q(h) jointly covers W(h mod L_0)).

## bad-residue-witness-index (ADVANCE) — CHANGES REQUESTED, NOT BUILT this round (diversity)

Verdict: the outline itself is sound, but this round it has **converged onto window-purity-class-cycle's
framing** — both attack the FIN-W star via the SAME three ingredients (single-sided-harmless ⟹ mutual/cyclic,
plus Window Purity), differing only in the closing tool (Lemma B window-cap vs. class-graph revisit/descent).
Per the shared-gap / diversity mandate, building both would be two variations of one framing hitting the same
wall together. window-purity-class-cycle is the mandated carrier of this framing and additionally certifies
the single-sided-harmless reduction that bad-residue-witness-index also needs, so I keep bad-residue-witness-
index LIVE (already registered, Elo 1521, stale cleared) but out of the build set. It re-enters when the
mutual/cyclic wall moves or it is re-framed genuinely far.

---

## Diversity assessment (report to orchestrator)

The build set spans **three distinct framings**, deliberately kept apart:
1. window-purity-class-cycle — greedy DYNAMICS / FIN-W mutual-cyclic class-graph (mandated).
2. lex-rewrite-descent — constructive foreign-technique active rewrite (no dynamics, no pigeonhole).
3. covering-small-part-descent — value well-ordering + LOCAL hub-capacity.

reduced-process-identity (Elo top, 1628) stays PARKED per standing rule — its advance adds no new closing
mechanism; keep it to import the eventual crux closure, do not spend a build slot re-holding the partial.
The two FIN-W carriers (window-purity, bad-residue) have converged; if window-purity-class-cycle's mutual/
cyclic close also stalls, next round should NOT field a fourth FIN-W variant — push a fourth genuinely
distinct framing instead.

## Ranking (Elo after this round)
reduced-process-identity 1628 (parked) · covering-small-part-descent 1627 · **window-purity-class-cycle 1568
(NEW)** · bad-residue-witness-index 1521 · **lex-rewrite-descent 1483 (NEW)** · cofactor 1478 · minimal-
linking-prime-extremal 1453 · large-prime-capacity-counting 1360 (dead) · difference-sequence-squeeze 1340.
(enum-covering-primes not in this sample; unchanged ~1597.) All stale flags on sampled approaches cleared.

build set: window-purity-class-cycle, lex-rewrite-descent, covering-small-part-descent
