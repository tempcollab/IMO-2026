# Proof review — imo-2026-04, round 2

## Headline finding: the contradiction is resolved

`binary-word-invariant`'s claimed 8-move witness forcing θ=180°/7° is **genuine**.
`corrected-genericity-bound`'s "θ=180°/7° is NOT forceable" and
`full-interval-hypothesis`'s "the earlier witness was a search artifact" are both
**wrong**, and I located the precise flaw shared by both (see below).

I independently re-derived the raw cut formula from the problem statement (read from
`problems.jsonl`, `problem_id=imo-2026-04`), re-verified it symbolically, and then
hand-reconstructed `binary-word-invariant`'s entire 8-move sequence
(equilateral start → 2 bisections → 1 transfer → 5 shifts) using exact
`sympy.Rational` arithmetic, computing every intermediate triangle from scratch (not
trusting the builder's arithmetic table) and cross-checking both of Shan-Yu's branch
choices at the two bisection steps. Every move is legal (`x1 ∈ (0,p)` at each step,
including boundary checks) and Shan-Yu is genuinely forced at every non-bisection step
(his "safe" branch is the one lacking θ; I verified this explicitly for both bisection
branches at step 2, confirming they both funnel — via different but both-valid transfer
parameterizations — into the identical state `{15°, 75/7°, 1080/7°}`). The final state
`{1005/7°, 75/7°, 180/7°}` sums to 180° and contains θ=180/7° exactly. Full transcript
in my scratch computation (reproduced in `lemmas/theta-180-over-n-forceable.md`).

**The shift move is a real, correctly-derived primitive.** From `{p,q,r}` with `p>θ`,
setting `x1=θ` forces `B={p-θ, q+θ, r}` (A always contains θ literally). This is a
one-line consequence of the cut formula; I re-derived it independently from the raw
formula (not from the builder's write-up) and it checks out.

## The located flaw (shared by the two "180/7 impossible" approaches)

Both `corrected-genericity-bound` and `full-interval-hypothesis` build a closure /
monoid on the single "pure" (θ-affine, spectator-independent) quantity that survives a
transfer move, using only two generators:
- `corrected-genericity-bound`: (halve) `a↦a/2` and (reflect) `a↦V-a`.
- `full-interval-hypothesis`: (halve) `a↦a/2` and (cross-transfer) `a↦2a-180`.

**Neither includes the shift operation `a↦a-θ`** (subtracting the fixed target θ from
a big pure quantity — a completely different affine map from either "reflect" or
"cross-transfer"). This is exactly the "hidden restricted sub-monoid" failure mode
flagged in the dispatch brief: both proofs correctly analyze *their own* restricted
move family (their internal case-exhaustion is not itself wrong), but incorrectly
present the resulting impossibility as if it applies to the *actual* game, which
contains the shift move as a legal cut (any `x1=θ` with `p>θ`, a continuum-available
choice of cut point, not a contrived one).

Concretely: `corrected-genericity-bound`'s own §5 propagation lemma *lists* the shift's
defining formula (`x1=V`, forcing `B={r,p-V,q+V}`) as one of the "messy single-hit"
cases whose junk-coefficient propagation it claims to have accounted for — but its §3
closure computation `C(V)` never folds this generator in. Once it is added, `C(V)`
becomes exactly `{180/n : n≥2}`, not the strictly smaller `{180/((2^k+1)2^j)}` claimed.
`full-interval-hypothesis`'s mod-7 obstruction is real *within* its two-generator
monoid, but is silent about the shift move, which its own report acknowledges
("there could be some other move sequence not of this shape... We have not ruled that
out") — an honest hedge that turned out to be exactly the gap.

## Per-approach verdicts

### `dyadic-scaffold` — Status: **partial** (confirmed correct) — Verdict: **CHANGES REQUESTED**
Fully rigorous, gap-free as far as it goes: θ>90° impossible (non-obtuse invariant,
re-derived and checked), and `{180°/((2^k+1)·2^j)} ⊆ S` via bisection + transfer.
Every step checked directly against the cut formula; no hand-waving found. Superseded
in strength (not contradicted) by `binary-word-invariant`'s larger family — the
remaining gap is the same one it already honestly names: exact upper bound on
`S∩(0°,90°]`.

### `binary-word-invariant` — Status: **partial** (confirmed correct, strongest result this round) — Verdict: **CHANGES REQUESTED**
Discovers the shift move; proves `{180°/n : n≥2} ⊆ S` (strictly larger than
dyadic-scaffold's family) with a complete, Shan-Yu-immune construction for general n,
plus the θ=180/7° exact-fraction witness. I independently re-verified every algebraic
step and the full numeric witness — this holds up. Necessity (`S ⊆ {180/n}`) is
explicitly and honestly left open — Section 5's "junk-coefficient" heuristic is
correctly flagged as informal, not claimed proved. This is the round's real progress;
the remaining gap is exactly the necessity direction, which the sibling approach's
attempt at (see below) turns out to be fixable in principle but not fixed yet.

### `corrected-genericity-bound` — Status recorded as `solved`, **actual Status: unsolved (its central claim is false)** — Verdict: **RETHINK**
The claimed theorem `S = {180°/((2^k+1)·2^j)}` is **false**, refuted by an
independently-reproduced counterexample (θ=180/7° is forceable). The flaw is the
missing shift-generator in the §3 closure `C(V)`, detailed above. This is not a minor
gap — the paper explicitly claims `solved` and states the false conclusion as a boxed
final theorem with a "verification" section that asserts 180/7° is impossible; that
verification section is wrong. Two sub-results are independently correct and are
certified separately (see below): the §2 exhaustive double-hit dichotomy (matches
`dyadic-scaffold`'s and `binary-word-invariant`'s independently-derived versions
exactly), and the general "junk coefficients propagate without cancellation" fact of
§5 (true in isolation; the error is only in never applying it to a three-generator
closure that includes shift). Should not be advanced as-is; if re-attempted, redo §3's
closure with (halve, reflect, shift-by-θ) as the three generators and re-derive the
fixed-point set (this is very plausibly `{180/n : n≥2}` exactly, i.e. it may actually
*prove* `binary-word-invariant`'s conjecture if redone correctly — a promising next
step, not a dead framework).

### `full-interval-hypothesis` — Status: **unsolved** (as self-reported) — Verdict: **RETHINK**
Self-assessment was honest (`unsolved`, with an explicit caveat that its impossibility
result only covers its own restricted move family). Its round headline ("H1 very
likely false," "the 180/7 witness was almost certainly a search artifact") is now
refuted by the independently-verified construction, so this line of reasoning should
not be pursued further as framed. Its "cross-transfer" primitive is a real, legal move
but is not needed for (or a substitute for) the shift move; no further use for it was
identified. Its target hypothesis H1 (S = full interval (0°,90°]) remains neither
proved nor disproved by anything found so far, and is not evidenced by this round.

## current.md updated

`results/imo-2026-04/current.md` — Status: **partial**. Best established result now:
`{180°/n : n≥2} ⊆ S ⊆ (0°,90°]`, strictly stronger than the previously-recorded
dyadic-only lower bound, with the erroneous exact-characterization claim explicitly
retracted and the reason given. Next-step guidance recorded: repair
`corrected-genericity-bound`'s closure by adding the shift generator, or find a
θ genuinely outside `{180/n}` that is forceable.

## Lemmas certified into `results/imo-2026-04/lemmas/`

- `cut-formula.md` — the shared cevian cut formula and identity (★).
- `non-obtuse-invariant.md` — θ>90° impossible.
- `double-hit-primitives.md` — exhaustive classification of one-move double-hit forcing
  cuts (bisection at p=2V; altitude-foot at V=90°); this is the correct, salvaged part
  of `corrected-genericity-bound`'s §2.
- `transfer-and-shift-moves.md` — the transfer move (imported from `dyadic-scaffold`)
  and the shift move (new, from `binary-word-invariant`), both re-derived and checked
  directly against the cut formula by the reviewer.
- `theta-180-over-n-forceable.md` — the full construction proving `{180°/n:n≥2}⊆S`,
  including the reviewer-reproduced exact-fraction θ=180°/7° witness.

Not promoted: `corrected-genericity-bound`'s closure theorem (§3) and necessity
conclusion (§5) — both false as stated, per the flaw above.

## What next round should attack

The single highest-value move: repair `corrected-genericity-bound`'s closure
computation by adding the shift generator `a↦a-θ` alongside (halve) and (reflect), and
re-derive its fixed-point set rigorously (three-generator word problem on the affine
line, mod out by the constraint that intermediate values must stay valid triangle
angles in (0,180°)). If it comes out to exactly `{180/n : n≥2}`, combined with
`binary-word-invariant`'s certified sufficiency construction, this would close the full
problem: **S = {180°/n : n integer ≥2}**. This is the natural, most promising route to
`solved` next round — put an approach directly on this repair, not on further
constructive search.
