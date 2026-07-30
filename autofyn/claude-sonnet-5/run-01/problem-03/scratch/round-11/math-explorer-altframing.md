# Explorer report (lens: alternative proof technique for Case C, m≥4)

## Scope of this report

Per assignment: look for a genuinely different PROOF TECHNIQUE (not a variant
of the current matching/casework mechanism) that could close Claim PTBI's
Case C (`p_1<Σ(A)/2`) for general `m≥4` in `universal-adversary-strategy`.
Did NOT attempt the proof. Queried `crux_moves_documentation.md`'s corpus
(`past_crux_moves_database.json`, 2434 cruxes) across `combinatorics` and
`algebra`, filtering `extremal-principle`, `games-and-strategy`,
`invariants-and-monovariants`, `induction-and-construction`,
`graph-theory-and-connectivity` (Hall/matching), plus keyword sweeps
(`exchange`, `Hall`, `matching`, `smoothing`, `threshold`, `adversary`,
`potential function`, `SDR`, `assignment problem`).

## What Case C actually is, precisely (so "different technique" means something)

By round 8–10's work, Case C is now a clean, isolated statement: for every
sorted `A=(p_1\ge\cdots\ge p_m)`, `\Sigma=1`, `p_1<1/2`, Xiang Yu (budget
`\le m-1` marks) must exhibit *some* way to partition some elements/fragments
into exactly-tied pairs (Lemma PAIR-VALUE, fully general and hypothesis-free)
so that `oddrank(\text{remainder}) + \sum(\text{pair values}) \le c(m-1)`.
Lemma PAIR-VALUE has already removed every geometric/contiguity obstruction
from the *value formula* — what's missing is a **pure existence theorem**:
for every `A` in Case C, some valid pairing/matching achieves the bound. Two
partial constructions (ALL-BUT-MIN, MATCH-TAIL-PAIR) close large sub-regions;
a concrete `m=5` witness shows they don't jointly cover everything.

This reframes the open gap as: **"does a good donor/subset matching always
exist?"** — an existence question over a finite (but `m`-growing) space of
matchings, subject to a numeric threshold, not just "some matching exists"
(which would be Hall's theorem's usual yes/no). This distinction matters for
judging whether Hall's theorem is really the right tool (see below).

## Candidate techniques found in the crux corpus

1. **Defect/maximal-deficient-set Hall's theorem** (`aimo-0063`, `aimo-0341`,
   graph-theory-and-connectivity / induction-and-construction). Technique:
   when a naive bipartite matching might not saturate one side, take a
   *maximal* Hall-deficient set, delete it and its neighborhood, and apply
   Hall's theorem to the survivors, using an extra "universal" vertex/fact
   to force the terminal matching nonempty. This is exactly the mechanism
   `universal-adversary-strategy`'s own round-9 write-up already named as
   the missing tool ("Hall's marriage theorem for simultaneous multi-donor
   matches") — so it is not a new discovery, it's confirmation that the
   already-identified target tool is a real, previously-used olympiad
   pattern. **Caveat, load-bearing**: Hall's theorem alone proves *existence
   of a valid matching*, not that a valid matching *achieves a numeric
   threshold* `\le c(m-1)\Sigma`. Case C needs the latter. A pure Hall
   argument would need to be paired with a value bound on whichever matching
   Hall's deficiency-argument produces — this is a real technical gap, not
   just bookkeeping, and no crux in the corpus combines Hall's theorem with
   a *value*-threshold condition of this kind (all matching examples found
   are pure existence/counting, e.g. `aimo-0129`, `aimo-0197`, `aimo-0336`).
   **Verdict: this is the natural completion of the CURRENT framing, not a
   different one** — it's the same matching mechanism, just finishing the
   existence step that rounds 9–10 already flagged as unattempted.

2. **Exchange-smoothing on a rank-weighted sum under a sum constraint**
   (`aimo-0146`, `combinatorics/extremal-principle` +
   `invariants-and-monovariants`). Technique: given `A(x) = \sum a_i x_i`
   over a sorted sequence `x_1\ge\cdots\ge x_n\ge0` with `\sum x_i` fixed and
   *increasing* coefficients `a_i`, repeatedly move a unit of mass from a
   lower-coefficient index to a higher-coefficient one whenever doing so
   strictly increases (or, for a bound, one shows it cannot decrease) the
   objective — this forces the extremal configuration into a small,
   enumerable family of canonical profiles ("top block within 1 of each
   other, tail capped"), which are then checked by hand. **Why this is
   genuinely different from the current framing**: `oddrank(B)` for a fixed
   piece-count *is* exactly a rank-weighted sum (weight 1 on odd positions,
   0 on even), so this technique's shape matches the objective almost
   perfectly — but the free variables here (how each Liu-Bang piece is
   split, i.e. Xiang Yu's continuous split ratios) are the "positions"
   being moved, not amounts of a single homogeneous resource. A
   smoothing/exchange argument would need to show: starting from an
   arbitrary Xiang-Yu response, some local "shift mass from an even-ranked
   fragment to an odd-ranked one" move is always available and weakly
   improves `oddrank`, until a canonical form (a specific finite family of
   tie-patterns) is reached — this is a genuinely different *proof
   mechanism* (continuous smoothing to a canonical extremal point, not
   naming a menu of discrete lemmas and casing on which applies).
   **However**: this is very close in spirit to `majorization-smoothing`
   (already RETHINK'd, round 4) and to `potential-averaging-bound` (RETHINK,
   round 5) — both found that `oddrank` as a function of split ratios is
   **not concave** (it's a genuine min/pointwise-min-like object across
   cells, an affine-on-cell-but-not-globally-concave function per Lemma
   TIE-NECESSARY / Lemma D), so a naive continuous smoothing argument that
   assumes "moving mass toward the odd ranks always weakly helps" is exactly
   the kind of claim `majorization-smoothing`'s non-concavity obstruction
   already rules out in general. A finer version restricted to a fixed
   combinatorial cell (where `oddrank` genuinely *is* affine, by
   TIE-NECESSARY) could still work, but that is once again the same
   cell-by-cell case analysis the current approach already does — not
   independent leverage, just the same machinery in exchange-argument
   language.

3. **Extremal principle with a secondary maximality criterion, forcing
   canonical structure via contradiction** (`aimo-0438`,
   `combinatorics/extremal-principle`: "among all optimal configurations,
   select one maximizing a secondary alignment statistic, then show any
   local deviation admits an edge-count-preserving exchange that strictly
   increases the statistic, contradicting maximality"). This is a
   genuinely different *proof shape* from anything tried so far on Case C:
   instead of building an explicit construction (DOM/HALVE/PAIR-VALUE) and
   checking it beats the threshold, one would argue *by contradiction*: take
   a globally optimal Xiang-Yu response for a fixed `A`, choose among all
   optimal responses one maximizing some secondary statistic (e.g. number
   of exactly-tied pairs, or total mass moved to odd ranks), and derive a
   structural property (e.g. "some specific pair must be tied") that a
   maximal response must have, purely from a swap-argument, without ever
   naming which construction achieves it. This is close to what Lemma
   TIE-NECESSARY already does (any minimizer can be taken at a tie/zero
   boundary) — so the *shape* is not new to this problem, but a **second
   layer** of secondary-maximality argument (maximize, among tied-optimal
   responses, some structural count) has not been tried, and could
   potentially pin down *which* tie-structure is forced without needing
   Hall's theorem's full generality. This is the most promising genuinely
   different angle found, but it is speculative — no worked instance in the
   corpus matches this problem's specific "weighted alternating sum" payoff
   closely enough to transplant a concrete lemma, only the general shape.

4. **LP/minimax duality.** Already tried twice by `minimax-mixed-duality`
   (rounds 6–7) and RETIRED: found, on two independent hard witnesses, that
   any candidate dual certificate collapses to "the same explicit
   tie-structure search," with no `A`-independent shortcut. This is not
   worth re-attempting as a *different* framing per that file's own
   documented conclusion; nothing in this round's corpus search surfaced a
   duality technique not already tried and refuted there.

5. **Relaxed-adversary transfer.** Already tried and RETHINK'd
   (`relaxed-adversary-transfer`, round 7): structurally the wrong direction
   (relaxing Xiang Yu's budget makes the relaxed value a *lower* bound on
   the real value, the wrong side of the inequality needed), config-blind,
   off-by-one in budget. Correctly ruled out, not revivable along this
   exact axis; no crux found this round suggests a different relaxation axis
   (e.g. relaxing Liu Bang's side, or an LP relaxation of the discrete
   matching) that would avoid the same wrong-direction problem, though this
   was not exhaustively checked.

6. **Potential-function / monovariant induction with a cleverer invariant
   than "oddrank".** Searched `invariants-and-monovariants` broadly
   (combinatorics + algebra + number_theory `games-and-strategy`); found
   many game-invariant cruxes (pairing/mirroring strategies, parity
   invariants, valuation-based monovariants for combinatorial games:
   `aimo-0077`, `aimo-0236`, `aimo-0631`) but none whose invariant shape
   (a single scalar tracked across discrete legal moves in a turn-based
   game with a fixed number of "moves" per side) obviously transplants to
   Case C's actual structure, which is a **one-shot optimization** (Xiang
   Yu picks his whole response at once, not a multi-round alternating game)
   over a continuous polytope with combinatorial cell structure — the
   "monovariant across turns" shape doesn't match this payoff structure.
   `majorization-smoothing`'s non-concavity finding already forecloses the
   most natural potential-function candidate (a weighted linear functional
   of the sorted values) for exactly this problem.

## Honest verdict

**A framing switch is not clearly warranted; the casework/matching
framing (Lemma PAIR-VALUE + an existence theorem for the matching) is very
likely the right one, and the two candidates below are refinements of it,
not alternatives to it:**

- The multi-donor Hall's-theorem existence argument (candidate 1) is not a
  new framing — it is precisely the tool round 9's own write-up already
  named as needed and unattempted (`crux_moves_documentation.md` confirms
  it is a real, previously load-bearing olympiad pattern, `aimo-0063` /
  `aimo-0341`), but it only proves *a* matching exists, not that the
  matching's *value* clears the threshold — that half still needs new
  content specific to this problem's payoff (oddrank), and is the genuine
  remaining work, not a framing question.
- The secondary-maximality extremal argument (candidate 3, `aimo-0438`-style)
  is the one candidate in this search that is a genuinely different *proof
  shape* (contradiction via a second layer of extremality, rather than
  exhibit-and-check) and has not been tried on Case C. It is speculative —
  no directly transplantable crux exists for this exact payoff shape — but
  it is worth a try next round precisely because it's structurally distinct
  from both the matching-construction approach and the two already-refuted
  "different framings" (duality, relaxed-adversary).
- Every other alternative framing actually tried so far
  (`minimax-mixed-duality`, `relaxed-adversary-transfer`,
  `majorization-smoothing`, `potential-averaging-bound`) has a *specific,
  structural* reason it fails (non-concavity, wrong-direction inequality,
  no independent duality leverage found in two rounds) — these are not
  "not yet found the right idea," they are proven obstructions to those
  particular mechanisms. Retrying any of them without a new mechanism would
  repeat documented dead ends.

**Recommendation for next round**: do not force a wholesale framing switch.
Either (a) push the current framing's missing half — a Hall-type existence
argument for the multi-donor matching, PAIRED with an explicit value bound
on whichever matching the deficiency-argument produces (this is the
precise, well-defined remaining gap, not vague), or (b) as a genuinely
distinct secondary attempt (not a replacement), try the
extremality-with-secondary-criterion proof shape from candidate 3 — pick,
among all globally optimal Xiang-Yu responses to a fixed `A` in Case C, one
maximizing a secondary statistic (e.g. number of tied pairs, or total
`\Sigma` fraction moved into tied pairs), and attempt a swap-contradiction
to force a canonical, provably-sufficient tie-structure directly, without
first establishing existence via Hall's theorem. If both stall again next
round on the same obstruction, that would be the point to escalate to a
genuinely alien framing (e.g. reformulating Case C as a flow/LP problem
over fragment-to-target assignment with an explicit objective, rather than
matching + Hall) — not yet, since neither (a) nor (b) has been tried.
