## imo-2026-03

Field of rival approaches, round 1 (fresh run — all three are `new`). All target the full claim: **c(n) = 2^n/(2^{n+1}−1)**, with both directions (Liu Bang's dyadic-ladder construction achieving it, AND a Xiang Yu reply capping every Liu placement at it). Conjecture is anchored: c(1)=2/3 hand-proved, c(2)=4/7 and c(3)=8/15 numerically exact-looking (15 and 8 sig figs), and I verified in exact rational arithmetic (n ≤ 7) the three identities the skeletons lean on: c(n) = c(n)/2 + c(n−1)(1−c(n)); a2 + c(n−1)(1−2a2) = c(n) at a2 = c(n)/2; and 1/2 + c(n)/2^{n+1} = c(n). No slug keeps the answer open — the evidence for the closed form is strong enough that an "answer-open" slug would waste a builder; if a bound refuses to close at the conjectured value, that is the signal to revisit.

Crux corpus: explorers found no genuine mechanical analogue; the closest echo is aimo-0117 ("play a dyadic sequence so the largest value exceeds the sum of all others") — I read its crux entries; the *super-increasing dominance* idea transfers as inspiration for the lower-bound accounting in all three slugs (each ladder rung exceeds the sum of all smaller rungs by exactly one unit), but its game mechanics don't, so no step cites it.

Shared infrastructure all three need: the **greedy-claiming lemma** (alternating-pick game on a sorted multiset ⇒ first mover gets the odd-rank sum; exchange argument) and the **multiset/Stackelberg reduction**. Recommend the first builder to touch any slug prove greedy-claiming rigorously and propose it for `lemmas/greedy-claiming.md` so the siblings import instead of re-prove.

---

dyadic-recursion-induction: new
File: results/imo-2026-03/approaches/dyadic-recursion-induction.md
Target: c(n) = 2^n/(2^{n+1}−1), both bounds.
Technique: strong induction on n; case split on Liu's largest piece a1; the tail after Xiang neutralizes the top is a scaled (n−1)-instance.
Skeleton:
  1. Greedy-claiming lemma — exchange argument (shared lemma).
  2. Multiset Stackelberg reduction — sizes only.
  3. Pair-collapse lemma: matched top pair (p,p) contributes exactly p to Liu — rank-shift parity.
  4. Lower bound: dyadic ladder resists every ≤n-cut refinement — induction on rungs via super-increasing property.
  5. Upper bound by induction: Case A (a1 ≥ c(n), a2 ≤ a1/2): bisect a1, bound a1/2 + c(n−1)(1−a1), decreasing in a1, = c(n) at a1 = c(n). Case B (a2 ≥ c(n)/2): shave a1 to match a2, bound a2 + c(n−1)(1−2a2), = c(n) at a2 = c(n)/2. Case C (1/2 ≤ a1 < c(n)): duplicate-and-remainder inside a1 gives Liu exactly a1. Case D (a1 < 1/2, a2 < c(n)/2): open — candidate strengthened hypothesis "cap ≤ max(a1, 1/2 + a1/2^{m+1})".
Key lemmas (claim + mechanism):
  - Recursion identity c(n−1)(1−c(n)) = c(n)/2 — because 2^{n−1}/(2^n−1) · (2^n−1)/(2^{n+1}−1) = 2^{n−1}/(2^{n+1}−1); verified exactly n ≤ 7. This makes Cases A and B close with zero slack.
  - Pair-collapse — deleting an adjacent matched pair shifts later ranks by 2, preserving parity.
  - Ladder surplus — 2^k exceeds the sum of all smaller rungs by exactly 1 unit, so an uncut rung leaves ≥ 1 unit of odd-rank surplus.
Open gaps: G0 (greedy lemma written rigorously), G1 (lower-bound induction accounting), G2 (Case D + remainder-interleaving bookkeeping in Case C).
Cases to cover: A/B/C/D exhaust (a1,a2) — shown in the file; also k < n+1 parts, Xiang using < n cuts, exact ties.
Watch out for: applying the c(n−1) tail bound when the top pair isn't actually top; ε-placements for exact copies; subgame move-order legitimacy (stated in file).

discrepancy-halving: new
File: results/imo-2026-03/approaches/discrepancy-halving.md
Target: same full claim.
Technique: potential-function / non-inductive reformulation. Exact identity Liu = 1/2 + Δ/2 where Δ = Σ(a_{2i−1}−a_{2i}) + a_{2n+1} (sorted, zero-padded). Theorem ⇔ minimax Δ = exactly one dyadic unit 1/(2^{n+1}−1).
Skeleton:
  1. Greedy lemma + reduction (shared).
  2. Discrepancy identity — Liu−Xiang telescopes over sorted pairs.
  3. Upper: Xiang forces Δ ≤ 1 unit against ANY partition — top-down match-or-bisect strategy; each cut at least halves the residual unpaired excess (halving lemma).
  4. Lower: any ≤n-cut refinement of the ladder has Δ ≥ 1 unit — pigeonhole (n cuts, n+1 rungs ⇒ one rung uncut) + super-increasing surplus, made global via a matching/flow accounting.
Key lemmas: halving lemma (each cut halves residual, tight at the ladder — that's the equality case); surplus lemma (uncut rung can only be paired against ≤ 2^k−1 units from below).
Open gaps: G0 (shared), GAP U (halving accounting stable under re-sorting), GAP L (global flow version of the surplus argument — per-rung accounting alone is unsound because an uncut small rung can pair with a sub-piece of a cut large rung).
Cases to cover: a1 ≥ 1/2 vs < 1/2; fewer parts/cuts; ties; all cut distributions over rungs.
Watch out for: NO integrality/parity-of-total shortcut — cuts are real-valued; matches broken by later insertions in the sorted order.

tie-structure-variational: new
File: results/imo-2026-03/approaches/tie-structure-variational.md
Target: same full claim.
Technique: variational/first-order over sorted vectors — no induction spine. Xiang's best reply to arbitrary a is piecewise-linear in cut positions ⇒ minimizer lies on tie strata ⇒ finite catalog of structured replies (duplicate-block, bisect, shave, hybrids) ⇒ V(a) = min of finitely many linear functionals ⇒ outer max_a min_i solved by rung-by-rung smoothing; unique equalizer = dyadic ladder (characterized by the two ties a1 = 2a2 and a1 = (1−a1) + a_{n+1}). Delivers construction and cap from one computation.
Skeleton: (1) shared lemmas; (2) compactness + piecewise-linearity; (3) tie-structure lemma via slope-±1 perturbation and a ties-count monovariant; (4) catalog exhaustiveness; (5) equalizing system + smoothing; (6) verify V(dyadic) = c(n) by the already-algebraically-verified mirror-ladder telescoping.
Key lemmas: tie-structure (nonzero slope ⇒ slide cut to nearest pattern boundary, Liu's take non-increasing); n=2 empirical signal that three distinct replies tie at 4/7 — the equalizer property is real.
Open gaps: G0, GAP T (perturbation with re-sorting), GAP C (catalog exhaustive), GAP M (smoothing beats every non-dyadic a).
Cases to cover: degenerate cuts (Xiang using fewer), equal Liu pieces (known bad — kill early via a catalog entry forcing ≈ 1/2), hybrid multi-piece cut distributions.
Watch out for: catalog blow-up — if it explodes, this collapses into the induction approach; keep it genuinely variational or let it die.

---

Recommendation for the outline-reviewer:
- Register all three; they share only the greedy-claiming lemma (deliberate — it's a settled-looking exchange argument, not a risky gap) and diverge in framing: recursive (A), potential/scalar (B), variational/structural (C).
- Priority order: **dyadic-recursion-induction** first (most concrete: three exact identities pre-verified, Cases A–C essentially mechanized, one well-scoped hard gap G2), then **discrepancy-halving** (cleanest reformulation, two symmetric hard gaps), then **tie-structure-variational** (highest risk, highest structural payoff).
- Suggested build set: dyadic-recursion-induction, discrepancy-halving, tie-structure-variational (3 builders). If capacity is 2, drop tie-structure-variational this round.
- First builder on any slug should certify `lemmas/greedy-claiming.md` (statement + exchange-argument proof) for the whole field.
- Dead ends to keep enforced (from explorers, already recorded in the files): c(n) = (n+1)/(2n+1) is refuted at n=2; equal/near-equal-piece Liu openings collapse to 1/2; no crux-corpus citation is load-bearing.
