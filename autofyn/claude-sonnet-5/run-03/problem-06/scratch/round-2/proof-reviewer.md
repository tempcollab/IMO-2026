# Proof review — imo-2026-06, round 2

Reviewed: `antichain-signature-closure.md`, `dense-signature-vanishing.md`, `dilworth-antichain-bound.md`.
All independently re-derived/re-simulated (not just read), per the round-1 rule that builder-reported
numbers must be reproduced from scratch.

## 1. `antichain-signature-closure` — Verdict: **CHANGES REQUESTED** (Status: `partial`, matches
builder's self-report)

**What I checked and reproduced independently (Python, from-scratch simulation, not the builder's
code):**
- $a_1=2310$: exact untruncated antichain reaches size **268 at $n=893$**, then **collapses to size
  1 at $n=894$** where $a_{894}=4096=2^{12}$. Exact match to the file's claim.
- All of $a_1,\dots,a_{894}$ are even (0 odd terms) — exact match.
- **353** growth events in the first 893 terms — exact match (I computed 354 over 900 terms, 353
  restricted to the first 893, matching the file's "353 growth events before the eventual collapse").
- $a_1=15$: antichain stabilizes at $\{\{2,3\},\{2,5\},\{3,5\}\}$ — consistent with the outline-
  reviewer's earlier independent check.

All headline computational claims check out exactly. Good discipline by this builder.

**Correctness of the mathematical content:**
- Lemma 2 (exact CRT validity criterion, two-directional iff) — re-derived from scratch: correct,
  no gap. This is a genuine strengthening over the old truncated-$P$ machinery: because $P^*$ is
  built from the exact prime factorizations of the fixed eventual generators (not truncated by
  $\le L_0$), sufficiency and necessity really do collapse into one statement. Verified.
- **Absorption Lemma** (Lemma 4) — re-derived from scratch: correct, self-contained induction, no
  gap. Certified to `lemmas/absorption-lemma.md`.
- **Self-closing sufficiency** (Lemma 5) — re-derived from scratch: correct, follows directly from
  Constraint Domination. Certified to `lemmas/self-closing-antichain-sufficiency.md`.
- **Negative diagnosis of the "witness-debt charging" argument** — re-derived the counting argument
  myself: correct. The per-step budget is $O(\log a_n)$, which is $n$-dependent (grows since
  $a_n\to\infty$), so summing gives $O(N\log N)$, not a finite bound; the $a_1=2310$ data (268 live
  generators vs. $\log a_{893}\approx14.5$) is a genuine, checked numerical witness that the naive
  charging shape cannot work. This is a real, useful negative result, correctly scoped (not
  overclaimed as ruling out *all* charging arguments, only the one shape sketched).
- **Sanity check against the round-1 trap**: I verified that (unlike the refuted `|Q|<∞` target)
  Antichain Stabilization is *not* contradicted by the theorem's own conclusion — if the sequence is
  eventually periodic with shift $L$, the defining behaviour is eventually periodic, which forces the
  live-generator antichain to be eventually periodic/finite-state too. So this is a legitimate open
  target, not a disguised false claim.

**Gap found by me, not previously flagged in this file or by the outline-reviewer:** Lemma 3 cites
`lemmas/periodicity-given-no-escape.md` with $P:=P^*$ (built from the eventual generator set). That
lemma's *stated* hypothesis is $\mathrm{primes}(a_1)\subseteq P$. I checked whether $P^*$ actually
satisfies this: **it need not.** If $\mathrm{primes}(a_1)$ itself later gets dominated by a strictly
smaller generator, $P^*$ (built only from the surviving eventual generators' primes) can omit some
prime of $a_1$. I then checked the actual proof body of `periodicity-given-no-escape.md` line by
line: it never uses $\mathrm{primes}(a_1)\subseteq P$ anywhere in the derivation (only $G\ne\emptyset$
and No-Escape are used), so the hypothesis is vestigial and the result almost certainly still holds
for $P^*$ — but as written, the citation "applies verbatim" is not literally justified, since the
cited lemma's stated hypothesis is not verified to hold. This is a real, if likely-fixable, rigor gap
that should be patched next round (either verify $P^*\supseteq\mathrm{primes}(a_1)$ directly, or
restate the periodicity lemma without the unused hypothesis). It does **not** touch the paper's real
open gap (Antichain Stabilization itself is still fully open for general $a_1$).

**Verdict rationale:** genuine progress (two new certified lemmas + a checked negative diagnosis +
a cleaner combinatorial target), but the central claim (Antichain Stabilization / self-closing
reachability) remains unproved for general $a_1$, plus the hygiene gap above. `partial` is the correct
Status (matches the builder's own claim). CHANGES REQUESTED: close self-closing reachability, and
patch the $P^*\supseteq\mathrm{primes}(a_1)$ citation gap.

## 2. `dense-signature-vanishing` — Verdict: **RETHINK** (true Status: `unsolved`, builder's
self-reported `partial` is an overclaim)

**What I checked:** reproduced the disproof of Proposition 3 from scratch (independent simulation of
$a_1=15$'s first 60 terms and all $\binom{60}{2}=1770$ pairs): **exactly 1510 violations** of
$(j-i)\mid a_j-a_i$, matching the file's number exactly, including the specific $i=1,j=3$
counterexample cited ($a_3-a_1=5$, $j-i=2$, $2\nmid5$).

This negative finding (the literal `aimo-0680` transplant fails) is rigorous — not merely asserted,
but backed by an exact, reproducible computation and a correct structural diagnosis of *why* it must
fail (the greedy recursion's defining rule changes at every step, unlike a fixed iterated map $f$).
Good, honest population hygiene.

**Proposition 4** (any repaired/localized identity is "no easier" than the shared wall): the forward
direction (No-Escape $\Rightarrow$ the identity is available for free) is a valid, correctly-derived
implication. The converse/main claim ("cannot be manufactured from below without first essentially
proving determinism") is a **reasoned but only semi-formal diagnostic**, not a fully formalized
impossibility theorem — it surveys the two facts available from certified machinery and argues
neither suffices, which is defensible but not airtight against every conceivable identity. The file
itself hedges this appropriately ("This is a genuine, checked negative result... not... asserted",
but still labeled a "diagnosis"), so it is not overclaimed as a proof — good.

**Why I downgrade the file's self-reported Status from `partial` to `unsolved`, and the verdict from
CHANGES REQUESTED to RETHINK:** Per the file contract, `partial` requires "a correct reduction or a
proven key lemma" toward the theorem. Propositions 1–2 are one-line corollaries of already-certified
facts (the builder itself, in "Promotable lemmas," says they "do not warrant a separate lemma file"
and carry "no independent reuse value"). Propositions 3–4 are negative/diagnostic only — they rule
out a mechanism, they do not advance a proof of the theorem. Nothing in "Current best" is new positive
progress toward the actual claim. This is the same situation as round 1's `monovariant-telescoping`
(a rigorously-established dead end for a specific mechanism, valuable as documented history per
CLAUDE.md's "record everything" rule, but not `partial` progress toward the theorem itself, and the
approach itself — the literal transplant — cannot become a proof). RETHINK routes it back to the
outliner for a genuinely different mechanism if a fourth approach is wanted; the negative result stays
recorded in `current.md` and this file so it is not re-attempted.

## 3. `dilworth-antichain-bound` — Verdict: **CHANGES REQUESTED** (Status: `partial`, matches
builder's self-report)

**What I checked and reproduced independently:**
- Re-simulated PC (P-Confinement) for $a_1\in\{15,105,6,210,2310\}$ up to 400 terms: **zero
  violations** in every case, matching the builder's broader 13-value, 1200-term check. Confirms the
  claim as far as tested.
- **Re-derived Steps A–D of the PC $\Rightarrow$ Theorem proof line by line from scratch**, treating
  it as the load-bearing new claim (per instructions, held to full certification rigor since it is
  proposed as a reusable lemma):
  - Step A ($R'_n=\min(R_n)$): correct — standard finite-poset "descend to a minimal element" argument,
    both inclusion directions verified.
  - Step B (reduce $G$'s defining condition to checking only true generators): correct, follows
    directly from Step A.
  - Step C (translate to the real validity condition via PC + Constraint Domination): correct.
  - Step D (No-Escape): correct — minimality of $y_{n+1}$ plus Step C rules out any valid candidate
    strictly between $a_n$ and $y_{n+1}$, and $a_{n+1}\le y_{n+1}$ was already certified, giving
    equality.
  - **Crucially**, this file uses $P=\{\text{primes}\le L_0\}$ throughout (same as
    `core-signature-pigeonhole`), which genuinely satisfies `periodicity-given-no-escape.md`'s stated
    hypothesis $\mathrm{primes}(a_1)\subseteq P$ (true by definition of $L_0=\mathrm{rad}(a_1)$) — so,
    unlike `antichain-signature-closure`, there is **no hypothesis-mismatch gap** here. This chain is
    genuinely zero-gap as claimed.
- Certified this reduction to `lemmas/pc-implies-theorem.md`.

**Assessment of PC vs. the shared wall (per the dispatch's specific question):** the file itself
proves (informally but correctly, and I re-checked the argument) that **PC $\Rightarrow$ Antichain
Stabilization** (via the same Step A machinery — if PC holds, the true generator sets always lie in
$2^P\setminus\{\emptyset\}$, so the already-certified pigeonhole chain argument for $R_n$ applies to
$R'_n=\min(R_n)$ too). This means PC is *stronger*, not an independent/easier target — it is the same
wall restated with the "generators never use large primes" framing instead of "the antichain
eventually stops growing." The builder is honest about this ("apparently of comparable difficulty...
I do not claim it is strictly easier"). I agree with this self-assessment. The value of this approach
is architectural (a single, clean, checkable hypothesis with a zero-secondary-gap payoff), not a
weaker target.

**Also correctly diagnosed as dead**: the originally-assigned Dilworth/chain-covering-by-window
mechanism, for the same underlying reason ($O(\log a_n)$ budget is $n$-dependent) that sank the
charging argument in `antichain-signature-closure` and the outline's original sketch — I agree this
is the same obstruction appearing a second time under a different technique label, consistent with
the outline-reviewer's prediction.

**Verdict rationale:** real new, fully certified reduction (cleaner than `antichain-signature-closure`'s,
with no citation-hygiene issue), but PC itself is unproved and — per the builder's own honest
admission, which I've independently confirmed — is not an easier route around the shared wall.
`partial` is correct. CHANGES REQUESTED: prove PC (or equivalently, self-closing reachability) for
general $a_1$.

## Lemmas certified this round

- `results/imo-2026-06/lemmas/absorption-lemma.md` — Prime-power absorption (from
  `antichain-signature-closure`). Fully re-derived, correct, no gap.
- `results/imo-2026-06/lemmas/self-closing-antichain-sufficiency.md` — Self-closing antichain
  $\Rightarrow$ permanent stabilization (from `antichain-signature-closure`). Fully re-derived,
  correct, no gap.
- `results/imo-2026-06/lemmas/pc-implies-theorem.md` — P-Confinement $\Rightarrow$ full theorem (from
  `dilworth-antichain-bound`). Fully re-derived step by step (Steps A–D), correct, no gap; notably
  free of the hypothesis-mismatch issue found in the sibling approach's citation of the same
  downstream periodicity lemma.

Not certified: `antichain-signature-closure`'s Lemma 2/Corollary/Lemma 3 chain as a single promotable
unit — Lemma 2+Corollary alone is correct and could be certified on request, but Lemma 3's citation of
`periodicity-given-no-escape.md` has the unaddressed $P^*\supseteq\mathrm{primes}(a_1)$ gap described
above, so I am not certifying the full chain as "zero-gap" until that is patched (a one-line fix is
likely, but per CLAUDE.md's certification bar — "no `sorry`, statement correct and no stronger than
proved" — an unverified hypothesis citation does not clear the bar as currently written).
`dense-signature-vanishing`: no lemmas proposed by the builder, none certified (Propositions 1–2 are
trivial corollaries not worth a separate file; Propositions 3–4 are negative/diagnostic, not reusable
positive building blocks, per the builder's own correct assessment).

## `results/imo-2026-06/current.md`

Updated (I own this file): `## Status` remains `partial`; `## Approaches tried` extended with all
three round-2 verdicts and their exact reproduced numbers; `## Current best` now lists both live
zero-secondary-gap reductions (Route 1 via `antichain-signature-closure`'s self-closing sufficiency,
Route 2 via `dilworth-antichain-bound`'s PC); cross-cutting diagnosis updated to flag that the
antichain-family wall has now been hit twice under different technique dressings (charging argument,
Dilworth chain-covering) and that the one attempted genuinely-independent framing this round
(`dense-signature-vanishing`) is now a confirmed dead end, per the orchestrator's "break a shared-gap
plateau" guidance — next round should prioritize either a new technique for self-closing/PC
reachability specifically, or a wholly different top-level framing not going through
antichains/signatures at all.

## Ranking

Recorded outcomes via `record_outcome`: `antichain-signature-closure` → `partial` (real progress, two
lemmas closed, stuck on stabilization + found a new citation gap), `dense-signature-vanishing` →
`dead-end` (mechanism refuted rigorously, true Status downgraded to unsolved), `dilworth-antichain-bound`
→ `partial` (new clean zero-gap reduction certified, PC itself remains the same wall restated, not an
easier bypass).
