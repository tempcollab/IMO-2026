## imo-2026-03 — LOWER wall, CROSS-SCALE lens (R18)

### Setup recap (certified substrate, unchanged)
Lemma MID: `D(S)=μ{g odd}` on `(0,2^{n-1})`, `g=N_F-N_B`, `∫g=1`. Lemma CLIP: τ=0 face
`∫φ(g)=D(S)-1`. Residual (★): `Σ_{i≥1}μ{g≥2i} ≤ Σ_{i≥1}μ{g≤1-2i}`, true/tight (0/330 fails,
reviewer R17). 10 dead lower levers on record (scalar-reserve, transport/matching, prefix
monovariant, f-partition localisation, LP-dual/vertex-polytope (×2), transform/generating-
function, merge-domination (R7 aimo-0298 split-avg + R15 induction-peel merge/realloc),
domain-band parity count (R16), scale-of-origin layer-cake (R17)). No live LOWER vehicle.

### Direction (i): global level-index Abel/layer-cake identity — ALGEBRAIC CONTENT CHECKED, NO NEW LEVERAGE FOUND
Worked out the exact algebra of (★) in closed form. Writing `μ_m=μ{g=m}` (integer `m`):
```
Σ_{i≥1}μ{g≥2i} = Σ_{m≥2} ⌊m/2⌋ μ_m      (LHS)
Σ_{i≥1}μ{g≤1-2i} = Σ_{m≤-1} ⌊(1-m)/2⌋ μ_m  (RHS)
```
and since for integers `⌊m/2⌋ = -⌊(1-m)/2⌋` when `m≤-1`, one gets exactly
`∫⌊g/2⌋ = LHS - RHS`. Combined with the elementary identity `g = 2⌊g/2⌋ + [g odd]` (true for
all integers, including negative `g`, under floor division) and `∫g=1`:
`D = μ{g odd} = 1 - 2∫⌊g/2⌋ = 1 - 2·LHS + 2·RHS`, so `D≥1 ⟺ RHS≥LHS ⟺ (★)`.

**Conclusion: (★) is a literal algebraic rewriting of `D(S)≥1` via the floor-division parity
identity — not new content per se.** Any "Abel summation on the level index `i`" applied to
(★) alone just re-derives this same telescoping (I checked: summation-by-parts on the nested
sets `{g≥2i}` decreasing in `i` reduces back to exactly the `μ_m` layer-cake decomposition
above — no extra structural input enters unless a THIRD, independent object (dyadic-
realizability of the level sets, i.e. BLK/ONE-REC) is folded in). This matches and CONFIRMS
R17's own assessment that plain direction (i) has "no concrete mechanism for WHY level-1
deficits get repaid by deeper levels" — I now have the precise reason: the identity is a pure
rearrangement of terms, so it contains zero information beyond `∫g=1` + the odd/even split.
**R17's flagged "narrower conjecture" — that an `i=1` deficit `a_1-b_1` is always ≤ the total
`i≥2` surplus `Σ_{i≥2}(b_i-a_i)` — is algebraically IDENTICAL to (★) itself** (trivial
rearrangement: `Σ_i(b_i-a_i)≥0 ⟺ Σ_{i≥2}(b_i-a_i) ≥ a_1-b_1`). **This is not a new sub-target;
proving it requires exactly proving (★). Flag this so the outliner does not waste a round
"gating" it as if it were weaker — it is exactly as hard as MID-core.**

**Where direction (i) COULD still carry content:** only if the dyadic/ladder structure (BLK's
`≤n+2`-distinct-values, ONE-REC's per-scale `ΣG_j=2^j` mass identity) is used to constrain HOW
the level sets `{g≥2i}`/`{g≤1-2i}` are built from dyadic-gap intervals — i.e. this collapses
into direction (iii) of R17 (value-level × scale-of-origin), which is the one substantive
candidate, not a plain layer-cake identity. I did not find a way to make (i) alone (without
scale-of-origin or another independent structural input) carry content — treat it as
DEAD-ON-ARRIVAL as a standalone lever; a "level-only Abel identity" is a repackaging.

### Direction (ii): self-similar recursion `D(n)=D(n-1)/(2+D(n-1))` — merge-to-base landing site: NEW DECISIVE STRUCTURAL/NUMERICAL FINDING
Ran exact-`Fraction` experiments (Python, `n=4,5,6`, random admissible `a=0` refinements,
`|F|=k`) testing whether ANY 2-fragment merge of `F` (with `|F|=k`, `ΣF=2^n`, each fragment
`≤2^{n-1}`) can literally land in the "solved" `|F|=2` in-regime base.

**Rigorous structural fact (proved, not just observed): for `|F|=3`, merging ANY two of the
three fragments is essentially ALWAYS forced outside the `a=0` cap.** If `f_1,f_2,f_3` are the
three fragments (`Σ=2^n`, each `≤2^{n-1}`), then for any pair `{f_i,f_j}`, `f_i+f_j =
2^n-f_k ≥ 2^n-2^{n-1}=2^{n-1}`, with equality **iff** the omitted piece `f_k` is exactly
`2^{n-1}`. So generically (measure-zero exception) EVERY pairwise merge at `|F|=3` produces a
piece `>2^{n-1}`, landing in the OPEN critical/top-uncut band (Case A / `(L⋆)`), never in the
solved `|F|=2` regime. **This confirms, with a clean proof (not just the R15 numeric 9-14%
failure), that a direct one-step merge from `|F|=3` to `|F|=2` is structurally impossible in
general** — exactly the "critical band" obstruction flagged by the R15 outline-reviewer, now
with the precise reason.

**For `|F|=k≥4`, merging the two SMALLEST fragments always stays within the `a=0` cap**
(proved: sorted ascending `f_1≤f_2≤…≤f_k` summing to `T`, the minimum pairwise sum is at most
the average pairwise sum `2T/k` — since there are `C(k,2)` pairs, each element in `k-1` of
them, total pair-sum `=(k-1)T`, average `=2T/k` — and `2T/k≤T/2=cap` exactly when `k≥4`;
confirmed 100%/100%/100% at `k=4,5,6`, `n=6`, 500 trials each). So a merge chain CAN validly
walk `|F|: k→k-1→…→4→3` while staying in-regime — but is stuck at `3` (see above), never
reaching `2`.

**Monotonicity of `D` under this valid two-smallest merge is BADLY false** (exact-`Fraction`,
300 trials/cell, `n=4,5,6`, `k=4,5,6`, no reallocation): `D` **increases** on the merge
30–66% of the time (`k=4`: 54–66%; `k=5`: 30–53%; `k=6`: 31–56%), i.e. far worse than R15's
already-fatal 9–14% (which had reallocation). Adding an **existential** choice — best of ALL
`C(k,2)` pairwise merges that stay in-cap, still no reallocation — improves but does NOT
reach zero: fails 30% (`k=4`) → 8% (`k=5`) → 1.7–3% (`k=6`). **1.7% at `k=6` is still a
decisive counterexample rate for a claimed universal monotonicity lemma** — not sampling
noise (300 trials, multiple independent config seeds).

**Verdict: the merge/self-similar-recursion object family is DEAD-ON-ARRIVAL as a reduction
mechanism, for TWO independent reasons, not one:** (1) the target base case (`|F|=2`) is
structurally unreachable from the genuinely hard case `|F|=3` by any single admissible merge
(proved exactly, generic case), and (2) even where a valid in-regime merge exists (`|F|≥4`),
monotonicity of `D` fails at a rate (1.7–66%) far too high to rescue with a small correction
term — consistent with, and sharpening, R15's already-fatal 9.2–14.5% single-pair-with-
reallocation failure. **Do not re-propose ANY merge-based / "collapse to |F|=2" induction
step for the lower wall — this is the 11th dead lower mechanism, now with a rigorous proof of
why it cannot work (not just an empirical failure rate).** The self-similar recursion
`D(n)=D(n-1)/(2+D(n-1))` describes the ANSWER's closed form (from the extremal/upper-bound
construction — Xiang's bisection), not a reduction available on the lower-bound side; there is
no natural way to attach it to a general lower-bound induction on `|F|`.

### Cheap-kill / gate probes run (exact `Fraction`, n=4,5,6)
- (i) Algebraic identity check: `D=1-2·LHS(★)+2·RHS(★)` confirmed exactly by direct
  substitution on 10 hand-built configs (no failures) — this is an identity, always exact by
  construction, so a "gate" here just confirms the algebra, not new mathematical content.
- (ii) Pigeonhole: `|F|=3` two-of-three merge always `≥2^{n-1}` — proved algebraically, spot-
  checked 500 random `|F|=3` configs at `n=6`: 0/500 stayed within cap (matches the a.s.
  strict-inequality prediction).
- (ii) Pigeonhole: `|F|=k≥4` two-smallest merge stays within cap — proved algebraically
  (average-pair-sum argument), confirmed 500/500 (`k=4,5,6`, `n=6`).
- (ii) Monotonicity of `D` under two-smallest merge (no realloc): FAILS 30–66% (`k=4,5,6`,
  `n=4,5,6`, 300 trials/cell).
- (ii) Monotonicity under EXISTENTIAL best-of-all-pairs merge (no realloc): FAILS 1.7–37%,
  decreasing in `k` but never reaching 0 in 300-trial samples up to `k=6`.

### Knowledge-base entries relevant
- Fubini/layer-cake identity (already imported via MID/CLIP) — exhausted for direction (i)
  alone; no further KB entry found that supplies an independent "level-set rearrangement"
  tool beyond what MID/CLIP/BLK/ONE-REC already give.
- Averaging/pigeonhole ("some pair is below the mean") — the tool that makes the `k≥4`
  two-smallest-merge-stays-in-cap fact work; standard, not previously named in this problem's
  KB usage but elementary (no `knowledge_base.md` entry needed beyond generic pigeonhole).

### Analogous past problems (cruxes)
Re-confirms R17's finds as the best matches for the (still-open, still-untried-in-full)
value-level × scale-of-origin synthesis:
- **aimo-0127** (`double-counting`) — level-indexed tail-count sum with a structural
  (non-scalar) per-level cap, summing exactly to the fixed total. Same FORM as (★); the
  missing ingredient is a structural (not potential/scan) per-level cap for our `g`.
- **aimo-0009** (`size-bounding-and-descent`+`double-counting`) — self-referential index
  coupling (`a_{a_i}`) as the template for R17's direction (iii) (scale-of-origin as a second
  structurally-determined index). Still the most promising untried synthesis on the LOWER
  wall, per R17 — NOT re-tested this round (my dispatch was (i) plain-level and (ii) merge;
  both came back negative/repackaging, so (iii) remains the field's best untried lead).
- Searched `combinatorics`/`algebra` `extremal-principle` and `size-bounding-and-descent` for
  a merge/exchange-to-a-boundary-case crux analogous to my (ii) finding (aimo-0146, aimo-0261,
  aimo-0794, aimo-0950 all use merge/exchange-to-contradict-minimality patterns) — **none is a
  genuine analogue**: they all use merge as a REDUCTION VALIDITY device inside an extremal
  argument (assume minimal counterexample, merge to contradict), not as an induction step that
  must additionally preserve a numeric monovariant across a fixed base case. No forced match;
  do not cite these as templates.

### Prior progress
`results/imo-2026-03/current.md`: LOWER wall `partial`, 10 dead levers pre-this-round; UPPER
(breakpoint-vertex) is separate live leader untouched by this lens. Certified lemmas MID, CLIP,
BLK, ONE-REC, VERT-LOW stand and are unaffected by this round's findings (no new certifiable
lemma emerged — both probed directions are negative/DOA, not partial-progress claims).

### Dead ends (do not retry) — UPDATED
- All 10 prior dead levers (unchanged list, see current.md).
- **NEW (11th): merge / "collapse |F| toward 2" reduction family, ALL variants** (fixed-pair,
  two-smallest, existential-best-pair, with or without reallocation) — dead for two
  independent, now-rigorous reasons: (a) `|F|=3→2` is structurally unreachable by any single
  admissible merge (proved: pairwise sum `≥2^{n-1}` generically strict), (b) even where merge
  stays in-regime (`|F|≥4`), `D`-monotonicity fails at a rate (1.7% even in the best
  existential variant at `k=6`) too high for a clean theorem. Supersedes/sharpens R7's
  aimo-0298 split-average refutation and R15's fixed-pair-with-realloc refutation — do not
  revisit merge in ANY form as a lower-wall reduction vehicle.
- **Plain level-index-only Abel/layer-cake identity (i), standalone**: confirmed to be a pure
  algebraic rearrangement of `D≥1` with zero independent content (worked out exactly) — do not
  dispatch a builder to "try Abel summation on (★) alone"; any real progress needs BLK/ONE-REC
  folded in (i.e. must become R17's direction (iii), not (i)).
- R17's flagged "i=1-deficit-repaid-by-i≥2" narrower conjecture: shown here to be exactly
  equivalent to (★) (not a strictly easier sub-target) — do not gate it as if independent.

### Small-case / intuition notes (conjecture, not proof)
- The self-similar recursion `D(n)=D(n-1)/(2+D(n-1))` for the ANSWER is real and certified
  (closed form of `u_n`), but it lives on the UPPER/construction side (Xiang bisection), and I
  found no natural coupling of it to a lower-bound induction on `|F|` — the two "recursions"
  (answer's `n`-recursion vs. a hypothetical `|F|`-reduction) are different objects; conflating
  them was likely the source of past hope for a merge-based lower lever.
- The LOWER wall's only genuinely untried substantive lead, after this round's two negative
  results, is R17's direction (iii) (value-level `i` × dyadic-scale-of-origin `j` synthesis,
  aimo-0009-style self-referential cap) — recommend the outliner prioritize it, or accept the
  field needs a genuinely different top-level object (e.g. probabilistic/second-moment on `g`,
  or a direct induction on `n` using the WHOLE certified MID-core statement as the IH rather
  than trying to reduce `|F|`).
