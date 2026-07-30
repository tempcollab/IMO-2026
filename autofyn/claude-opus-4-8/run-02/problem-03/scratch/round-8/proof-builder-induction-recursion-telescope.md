# Build report — induction-recursion-telescope (Round 8)

**Status: partial** (GAP L still open; assigned tiling mechanism refuted).

## Assignment
Close GAP L Case B (`D̃≥1` ⇔ `(△⋆)` ⇔ `E(F)≤2^n−1`) via a greedy bounded-window
nonnegative-block **TILING** of the merged descending order `Σ_iψ(c_i)Δw_i≥0` (crux aimo-0626),
as a NET block-domination (not the refuted §10 1-1 injection), with a two-sided budget-bounded window.

## Outcome: the assigned tiling mechanism is REFUTED as a local certificate (rigorous, §15 of the file)

Three findings, all rigorous and numerically checked (`2·10⁵`/`10⁵` residual configs, `n≤6`):

1. **The tiling is circular.** A partition of `{1..m}` into consecutive blocks each of nonneg
   `ψ(c_i)Δw_i`-sum exists **iff** the total `Σ≥0` — take the single block `[1,m]`. So "a nonneg
   block tiling exists" is logically equivalent to the target and carries no independent content.
   The device is non-trivial ONLY with a *bounded local* window certificate (the aimo-0626 setting).

2. **No bounded/one-sided local certificate exists.** Both-directional greedy minimal-window tiling
   fails on `222/2·10⁵` residual configs. Minimal witness (`n=3`):
   `Y=(3.382,2.553,2.065)`, `Z=(4,1.042,1,0.958)`, merged `s=(+1.237,0,0,−2.046,0,0,+1.916)`.
   The lone deficit `s_4=−2.046` exceeds EACH adjacent surplus (`1.237<2.046`, `1.916<2.046`); its
   only nonneg window is the whole list. So the certifying "block" is non-local — the compensating
   surplus for a single depth-2 excursion is split across both sides and must be gathered at once.
   This is the direction-trap in sharpest form and it is fatal to any bounded-window tiling.

3. **Budget bounds height, not window.** Lemma H: `maxc≤|Y|=a_0+1` (proved; `0/10⁵`). Caps the
   excursion depth but not the window length or block sign — does not localize the certificate.

4. **All measure forms restate `D̃≥1`.** Identity `(△△)`: `∫(⌊M^+/2⌋−⌈M^-/2⌉)=½∫M−½D̃` (proved;
   `0/10⁵`). Hence layer/summed/`(♠≥0)`/`(△⋆)` are pure measure-algebra restatements; the trivial
   layer bound yields only `D̃≥0` (off by `½`). The residual `½` — the equality-attaining content —
   must be injected by the dyadic budget `Σa_j≤n` NON-locally; a reshuffle of the profile `M`
   (which is all a tiling is) cannot supply it.

## What is proved this round (promotable)
- Lemma H (`maxc≤a_0+1`), fully proved.
- Identity `(△△)`, fully proved — pins the circularity of the measure forms.
- Negative result: no local tiling certificate; minimal witness recorded. Cache to stop retries.

## Spec concern (important for the orchestrator)
The assigned mechanism does not and cannot close GAP L as a local tiling. This joins matching (§10),
scalar-summary (§2), top-reserve (§14) as refuted merged-order routes. Recommend RETIRING the
merged-order block/window/matching family for the residual. The two sibling slugs
(`cut-sequence-potential` — sequential exact-toggle amortized monovariant; `even-rank-doublecount` —
static scale-graded double-count) are the live hope precisely because they can inject `Σa_j≤n`
non-locally, which `(△△)`/§15 prove the merged-order measure forms cannot. If both also stall, the
field should escalate to a fourth framing that routes through neither the merged-order reduction nor
the static `E(F)≤2^n−1` inequality (per the outline-reviewer's escalation note).

## Honesty
No overclaim: GAP L remains open. The round's value is a rigorous elimination of the bounded-window
tiling family plus the `(△△)` circularity result, which together redirect the field.
