# imo-2026-03 — outline-reviewer report (round 7)

Terrain read: upper explorer (recursive-split fix, O2→subset-sum, greedy cascade),
lower explorer (vertex-level restatement (★), Mechanism A, exhaustive T_3/T_4
vertex enum 0 counterexamples). Both walls narrowed and concrete. The lower wall
gained a genuinely new object (the vertex-level restatement (★): `D=1` at a strong
breakpoint ⟹ `F=0`); the upper wall gained a load-bearing methodology fix
(recursive splits) but its proposed primary spine (greedy cascade) has a fatal
flaw (see §3).

I reproduced the load-bearing numerics with exact `Fraction` arithmetic:
- (★) verified on 15 non-dyadic vertices T_3+T_4 (cascade + split-tower +
  split-2tower types): all have D>1 (min 5/3), single surviving fragment
  (`F_pos` length 1), `1<v<2^{n−1}`, decomposition `D=(F−T)+2(t₊−f₋)` checks out
  (`decomp_check=True` all 15), mass-budget tight at 12/15. The "largest tower
  at + > frag + smaller" dominance FAILS exactly the 2 frag-at-+ cases — confirms
  the universal condition is `t₊−f₋>F`, not that dominance. (`mechanism_probe.py`.)
- **Greedy cascade FALSIFIED** on (12,4,3,2)/21 (n=3, compressed, large-top):
  the greedy (match a_2→4, then a_3→3, then a_4→2) leaves remainder 3, giving
  `D=3/21=1/7 > 1/15`. The explorer's achieving strategy (halve a_1+a_4) gives
  `D=1/21 ≤ 1/15`. So the greedy cascade is NOT a valid Xiang strategy.
  (`breakpoint_exact_enum.py` + direct Fraction recompute.)

---

## 1. Per-approach verdict

### tail-count — APPROVE (primary lower lead)

The vertex-level restatement (★) is a genuinely new object the face-level
framings missed. The load-bearing inference the dispatch asked me to check —
"does `D>1` at all non-dyadic VERTICES imply `D≥1` on the whole face by PL
convexity?" — is SOUND: `pl-breakpoint-minimum` (certified) says the GLOBAL min
of D over all ≤n-mark refinements is attained at a strong-breakpoint PL vertex
(standard PL-min-at-vertex fact: D is continuous piecewise-linear on the compact
refinement polytope; min of PL on a polytope is at a vertex of the PL
subdivision). A "tie face" is a cell where D is affine; its min is at a vertex of
that face = a PL vertex. So `D≥1` at all vertices ⟹ global min ≥1. The dispatch's
"global min on a tie face not a vertex" worry is moot — that case reduces to a
sub-vertex.

Non-circularity check (the dispatch's second worry): the decomposition
`D=(F−T)+2(t₊−f₋)` is the SAME algebra as round-5's spine sign-pattern framing,
but round-5's circularity was in the ARGUMENT (presupposing `S₊=F`, the
interleaving pattern), NOT the decomposition identity (which is just algebra).
Sub-step (d) tries to PROVE `t₊−f₋>F` from sort-order + mass-budget + tower-vs-
tower dyadic dominance, WITHOUT presupposing the pattern. The outline explicitly
forbids the circular spine sign-pattern/multi-swap framing and the fragment-vs-
tower superincreasing mechanism (correct — fragments aren't tower pieces). So the
spine is non-circular IF the builder does not smuggle in `S₊=F` as an assumption.

Hard steps (honestly flagged, buildable):
- **Sub-step (a) "at most one non-dyadic fragment survives at a vertex"** — the
  outline's argument ("two surviving non-dyadic groups ⇒ `nfree≥2` ⇒ face not
  vertex") is sketchy and needs rigor. Verified `F_pos` length 1 on the 15
  enumerated vertices, but this is a SUBSET (see caveat). The builder must prove
  it structurally, not just verify.
- **Sub-step (d) sign-forcing of `t₊−f₋>F`** — the universal condition (verified
  0/15). Two sub-cases (frag-at-− 13/15: need `t₊>2v`; frag-at-+ 2/15: need
  `t₊>v`). The outline correctly notes the "largest tower at + > frag+smaller"
  dominance FAILS 2/15 (I confirmed: exactly the frag-at-+ cases), so the builder
  must use the universal `t₊−f₋>F` condition. This is the genuine open core;
  the numerics confirm it's a real theorem (0/15), but the structural proof is
  unproved.

CAVEAT (★) is verified on a SUBSET of vertex types (cascade + split-tower +
split-2tower), NOT mixed types (e.g. "split top into 3 + split a tower"). The
builder must either prove (★) structurally for ALL vertex types (the sub-step d
aim) or extend the verification. Do not present the 15-vertex verification as
proof of (★) for general n.

Dead ends respected: spine sign-pattern/multi-swap (CIRCULAR, not retried),
fragment-vs-tower superincreasing (forbidden), mass-budget-as-sign-argument
(correctly noted as magnitudes not signs — sub-step d adds the sign step),
non-tower Liu configs (tower is unique maximizer). APPROVE.

### vertex-enum-n3 — APPROVE (with the completeness hard step flagged)

Legitimacy check (the dispatch's central question): is finite exhaustive vertex
enumeration a LEGITIMATE proof for fixed n=3? YES — IF `V_3` is PROVEN complete.
The round-2 rule forbids "exhaustive n≤6 grid numerics as a proof" — that rule
targets a CONTINUUM sample (grid), not a FINITE combinatorial exhaustion. The
PL-vertex set IS finite (combinatorial types × tie-structure set-partitions
with `sum=D_n`), and `pl-breakpoint-minimum` reduces the global min to vertices.
So a complete exact-Fraction enumeration over the full PL-vertex set IS rigorous
casework (KB "Casework / exhaustion"), not a grid heuristic. The distinction the
dispatch draws (covers ALL refinements exhaustively vs. a sample) is correct, and
the outline meets it IN PRINCIPLE — but NOT YET in the current enumeration.

Hard steps (load-bearing, buildable):
- **COMPLETENESS of `V_3` (hard step 1, make-or-break):** the current 64-vertex
  enum covers cascade + split-tower + split-2tower but MISSES mixed mark-
  distributions (e.g. "split top into 3 + split a tower"). The outline honestly
  flags this. The builder must (a) extend the enumeration to ALL mixed types
  (1,2,3 marks × all refinement types × all tie-structures with sum=15), and
  (b) PROVE `V_3` exhausts the PL-vertex set (every PL vertex is a tie-structure
  set-partition with sum=D_n, solved linearly — this is the soundness argument).
  Without completeness, the n=3 lower bound is NOT proved by this route.
- **Exact-Fraction soundness** — D is affine on each PL cell, so the vertex value
  IS the cell's min; computing at the vertex with exact arithmetic is rigorous
  (no rounding). Sound (PL affinity).
- **Origin-based classification** — classify fragments by ORIGIN (fragment vs
  tower piece), NOT value-type (round-5/6 bug). The outline correctly imports
  this. Hard-validate `sum(full)=D_n` at every vertex (the explorer caught a sum
  bug producing spurious `D=0`).

This is a certifiable milestone (`c(3)=8/15`, upper already certified) if
completeness closes — a real, tractable near-term result. Genuinely different
from tail-count (computational casework for fixed n vs general-n structural
lemma). The open gap (n≥4) is honestly noted (extend enumeration, or close the
structural (★) via tail-count). APPROVE.

### majorization-upper — CHANGES REQUESTED (greedy cascade spine FALSIFIED)

The greedy cascade primary spine is FALSIFIED by a concrete counterexample. I
verified with exact `Fraction` arithmetic:

**Counterexample (12,4,3,2)/21 (n=3, compressed, large-top):**
- Greedy cascade: split 12→{4,8} (match a_2=4), then 8→{3,5} (match a_3=3), then
  5→{2,3} (match a_4=2). All a_2..a_4 paired, remainder r_3=3. Multiset
  {4,4,3,3,3,2,2}, D = 4−4+3−3+3−2+2 = 3, D/21 = **1/7 > 1/15 = 1/D_3**. VIOLATION.
  (Stopping at n−1=2 marks also gives D=1/7.)
- The explorer's achieving strategy (halve a_1+a_4 → {6,6,4,3,1,1}) gives
  D=1/21 ≤ 1/15. So a valid strategy EXISTS, but it is NOT the greedy cascade.

**The monovariant claim is mathematically wrong.** The outline asserts "the
process terminates in ≤n−1 steps with a remainder r ≤ a_{n+1} (or 0)." But
`r_{n−1} = a_1 − (a_2+...+a_n) = a_1 − (1−a_1−a_{n+1}) = 2a_1 + a_{n+1} − 1`,
which for large a_1 is LARGE, not ≤ a_{n+1}. For (12,4,3,2)/21: r_{n−1}=5/21 >
a_{n+1}=2/21, and r_{n−1}=5/21 > 1/D_n=1/15. The remainder is not bounded by
a_{n+1} and exceeds the target. GAP-Greedy ("remainder never stuck in
(1/D_n, a_{k+1})") does not even cover this failure mode — the remainder is a
FINAL leftover that is simply too large, not "stuck between two a_i."

**The greedy cascade does NOT dodge the large-top regime** — it FAILS on it. The
outline's central claim ("the greedy MUST handle [the large-top regime] where
subset-sum is impossible") is contradicted by the counterexample. The 0-violations
numerics the explorer reported are for the FULL RECURSIVE SEARCH (which tries all
strategies), NOT for this specific greedy cascade. The greedy cascade is a
PHANTOM target — it is falsified by a concrete instance, like the V(n) IH and
3-mark cascade before it (round-5 rule).

**Verdict: CHANGES REQUESTED (not RETHINK)** — the approach is NOT dead. It has
accumulated certified progress (3 unconditional sub-cases all n, GAP-U2 narrowed
to compressed only, halving-always-a-nplus1). GAP-U2-compressed is an honestly-
open gap that needs attack. But the greedy cascade spine is CUT. The builder must:

1. **DROP the greedy cascade spine entirely** (steps 3–5). Do not build it; it is
   falsified. Do not attempt to "fix" the monovariant — `r_{n−1}=2a_1+a_{n+1}−1`
   is structurally large for large a_1, so no monovariant repair can bound r ≤
   a_{n+1}.
2. **Keep the recursive-split model fix** (step 2) — it is load-bearing and
   correct (the round-6 "violations" were a non-recursive search bug; the halving
   lemma + block-contribution-formula handle fragments).
3. **Pursue the subset-sum fallback (GAP-SubsetSum, step 6) for the
   a_1 ≤ 2^n/D_n regime** — honest, unproved, but a real target (multiset-equal-
   sums / Prouhet-Tarry-Escott density on bounded-spread values).
4. **For the large-top regime (a_1 > 2^n/D_n), pursue the ACTUAL achieving
   strategies** the explorer found (halve a_1+a_4 → D=a_2−a_3 type; reproduce
   a_2..a_k from a_1 then halve the rest; etc.) — these are ad-hoc witnesses and
   need a UNIFYING sufficient condition. Flag this as the genuine hard step
   (GAP-LargeTop). Do NOT collapse it into the greedy.
5. **Respect the parity obstruction** (target D=leftover≤1/D_n, not D=0) — kept.
6. **Respect dead ends** (O1, V(n) IH, 3-mark cascade, Max-bound, Schur,
   even-packing-as-bypass, perturbation-to-halving-region=O1) — all kept.

The approach stays in the build set (it is the ONLY upper-bound slug, and
GAP-U2-compressed must be attacked), but the builder works on GAP-SubsetSum +
GAP-LargeTop, NOT the greedy cascade.

---

## 2. Registrations performed

- `vertex-enum-n3` — REGISTERED cold-start (Elo 1500). New, genuinely-different
  lower framing (computational casework for fixed n=3, certifiable milestone
  c(3)=8/15 if completeness closes). `tail-count` and `majorization-upper` already
  registered; no copies requested this round.

---

## 3. Ranking comparisons + Elo snapshot

Comparisons (anchored to evidence — last outcomes, accumulated certified
progress, tractability of the open hard step):

- tail-count > vertex-enum-n3 — tail-count is general-n structural + 7 rounds of
  certified progress; the (★) is the strongest lower lead. vertex-enum-n3 is fresh,
  n=3-only, completeness unproven. Both have open hard steps but tail-count is
  further-reaching.
- majorization-upper > vertex-enum-n3 — majorization-upper has 3 unconditional
  sub-cases certified all n + GAP-U2 narrowed to compressed only; vertex-enum-n3
  is fresh with its milestone contingent on the completeness proof.
- vertex-enum-n3 > tower-induction — fresh tractable milestone (c(3)=8/15 in
  reach) vs stale converged-on-G1 (held since round 3).
- vertex-enum-n3 > even-packing-upper — fresh genuinely-different vs stale
  reframe-equivalent (not a bypass).
- vertex-enum-n3 > xor-overlap — tractable milestone vs G1-equivalent wall
  (GAP-X, honestly G1-equivalent by XOR-bound).
- vertex-enum-n3 > lp-dual-certificate — tractable milestone vs G1-equivalent wall
  (GAP-LP2, strong-duality-equivalent).
- vertex-enum-n3 > gaps-leftover — tractable milestone vs G1-equivalent wall
  (deficit-covering crux open).
- tail-count > majorization-upper — tail-count's (★) is a genuinely new verified
  object (0/15, the strongest lead in 7 rounds); majorization-upper's primary
  spine (greedy cascade) is FALSIFIED this round, leaving only unproved fallbacks.
- tail-count > tower-induction — strongest lower lead (new (★)) vs stale converged.
- tail-count > xor-overlap, > lp-dual-certificate — new (★) vs converged G1-
  equivalent walls.
- majorization-upper > even-packing-upper — primary active upper lead (despite
  greedy falsification, still the only upper slug with accumulated progress) vs
  stale reframe-equivalent.
- majorization-upper > xor-overlap, > tower-induction — active upper lead vs
  converged/stale lower walls.
- tower-induction = gaps-leftover (draw) — both converged lower framings, both
  G1-equivalent at the crux, both held.

**Resulting Elo snapshot (best-first):**
| slug | Elo | last outcome | note |
|---|---|---|---|
| tail-count | 1779 | partial (r6) | primary lower lead; (★) verified 0/15 (subset); sign-forcing open |
| majorization-upper | 1650 | advanced (r6) | greedy spine FALSIFIED; subset-sum + large-top fallbacks unproved |
| tower-induction | 1567 | advanced (r3) | held; converged on G1 |
| vertex-enum-n3 | 1559 | — (new) | cold-start; n=3 milestone if V_3 completeness closes |
| even-packing-upper | 1477 | partial (r6) | held; reframe-equivalent, not bypass |
| xor-overlap | 1467 | advanced (r5) | held; GAP-X G1-equivalent |
| gaps-leftover | 1437 | advanced (r3) | held; deficit-covering crux open |
| lp-dual-certificate | 1431 | advanced (r5) | held; GAP-LP2 G1-equivalent |
| self-similar | ~1426 | — | held (subsumed) |
| d-potential | ~1418 | verified-milestone (r1) | held (Φ circular) |
| balanced-configs | 1289 | — | retired |

Diversity note: the two lower build slugs (tail-count, vertex-enum-n3) diversify
by MECHANISM (general-n structural sign-assignment vs fixed-n computational
casework) and by SCOPE (general n vs n=3) — good, not a single-gap trap. The
upper slug (majorization-upper) is the only upper-bound line; its two fallback
hard steps (GAP-SubsetSum, GAP-LargeTop) are DIFFERENT quantities (subset-sum
density vs multi-piece-split unification), respecting the round-6 "open at most
ONE upper slug on the compressed sub-case" rule. The converged lower framings
(tower-induction, gaps-leftover, lp-dual, xor-overlap) are HELD per the round-5
"5 framings converged → retire all but the strongest mechanism" rule — they stay
ranked but stale, ready to revisit if (★) stalls.

---

## 4. Build set

Three builders, parallel (each owns its own approach file, no collision):
- `tail-count` — build Mechanism A: prove sub-step (a) (single-survivor rigor)
  and sub-step (d) (sign-forcing of `t₊−f₋>F`, universal not the failing
  dominance). Verify (★) on mixed vertex types too, or prove it structurally.
- `vertex-enum-n3` — extend enumeration to ALL mixed mark-distributions; PROVE
  `V_3` completeness (exhausts the PL-vertex set); hard-validate sum=D_n, classify
  by ORIGIN. Goal: certified milestone c(3)=8/15.
- `majorization-upper` — DROP the greedy cascade spine (falsified by
  (12,4,3,2)/21). Build GAP-SubsetSum (≤2^n/D_n regime) + GAP-LargeTop
  (multi-piece-split unification for a_1>2^n/D_n). Keep recursive-split model.

build set: tail-count, vertex-enum-n3, majorization-upper
