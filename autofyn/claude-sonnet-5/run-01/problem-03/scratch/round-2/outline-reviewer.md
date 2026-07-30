# Outline review — imo-2026-03, round 2

Context checked: `results/imo-2026-03/current.md` (partial), all four existing
approach files (`geometric-dominance-construction`, `recursive-embedding-induction`,
`equalization-potential-bound`, `majorization-smoothing`), `/tmp/round-2/proof-outliner.md`,
`/tmp/memory/run_state.md` Rules (in particular the explicit standing rule to never
re-run majorization-smoothing's falsified concavity claim), and `knowledge_base.md`.
Ran numeric checks (Python) on the new `universal-adversary-strategy` mechanism.

## majorization-smoothing — RETHINK (cut again)

**Verdict: RETHINK.** This is the exact violation the standing rule warns about.
I diffed the current `approaches/majorization-smoothing.md` against what round-1's
outline-reviewer rejected: **the file is byte-for-byte unchanged.** Lemma C
("Xiang Yu's optimal response is a min of finitely many linear functionals of
`p`, hence `V(p)` is concave") is still presented as the approach's entire
selling point — the mechanism that makes Step 4 (global optimality) "nearly
free." Round 1's outline-reviewer numerically falsified exactly this claim
(`n=2`, `p1=(0.7,0.2,0.1)`, `p2=(0.34,0.33,0.33)`, midpoint `(0.52,0.265,0.215)`:
`V(mid)=0.52 < (0.55+0.50)/2=0.525`, reconfirmed with 5x more optimizer
restarts — a clean, well-converged counterexample, not noise). The outliner's
round-2 report labels this approach "advance" and tells the builder to
"prioritize verifying (or refuting) Lemma C's concavity claim first" — i.e.
it asks the builder to re-open a question that is already closed (refuted).
The file itself still calls Lemma C "OPEN but likely TRUE," which is false:
it is open only in the sense that no one has written the disproof into the
file, but the disproof already exists and is on record in `/tmp/memory/run_state.md`
Rules and in round 1's report. Per the standing rule, this must be cut again,
not advanced. If the outliner wants a genuinely different global/variational
framing next round, it must NOT lean on concavity of `V(p)` at all (e.g., a
weaker property like quasi-concavity along specific line segments, or an
entirely different global argument) — and must show it has actually checked
the new claim against the existing counterexample point before proposing it.

I am not registering `majorization-smoothing` (it was never registered after
round 1's RETHINK, correctly, per the registration tool's own semantics) and
I am not including it in the build set.

## geometric-dominance-construction — CHANGES REQUESTED (revise, as proposed)

Right technique still (top-piece domination + doubling identity), and the
revision (Lemma F: fold the `k>=1` case into a single induction on `k` via the
`p_1=2p_2` doubling identity) is a sound *shape* of argument — not hand-waved,
the outline correctly identifies the concrete mechanism (exchange/merge-
monotonicity) rather than just labeling the gap "done by symmetry."

Issues to fix while building:
- The outline itself flags the real risk (re-verifying Lemma F numerically at
  another small `n` and calling it done) — keep this as a hard gate on the
  builder: the induction step must be a genuine general argument on `k`
  (moving one mark from tail to top cannot decrease `oddrank(B)` below the
  `k-1` bound), not a growing case enumeration.
- "Simultaneous tail-splitting" (remaining `n-k` marks spent adversarially on
  the tail at the same time as the `k` top marks) must be handled inside the
  same inductive step, not bolted on afterward — the outline says this but the
  actual mechanism for combining the two mark streams isn't spelled out yet;
  push the builder to make this explicit, not implicit in "combine."

## recursive-embedding-induction — CHANGES REQUESTED (revise, as proposed)

Independent, legitimately different decomposition of the *same* gap (induct
on `n` via the self-similar rescaling `tail(A_n)=λ_n·A_{n-1}`, rather than on
`k`). This is a fine hedge — if the exchange argument on `k` (sibling
approach) stalls, the rescaling-identity route is a real alternative, not a
duplicate slice of one proof (each independently completes the whole
target end to end, importing but not depending on the other).

Issues to fix:
- Lemma G's core claim — that the rescaling identity `oddrank(B) = c(n) +
  λ_n·(oddrank_{n-1}(B') - c(n-1))`-type decomposition holds for the FULL
  range of possible splits of `p_1` (not just the specific optimal doubling
  split found numerically) — is exactly the crux and is explicitly marked
  open. Good that the outline says so plainly; the builder must derive the
  decomposition as an identity/inequality that holds for *every* split, not
  merely verify it holds at the split Proposition 4 already uses.
- Base case `n=0,1` should be written out explicitly in the final proof, not
  just referenced as "already available from explorer hand computations."

## universal-adversary-strategy — CHANGES REQUESTED (new; register, do not approve as-is)

Genuine diversity: this is the first approach to attack the untouched
upper-bound-over-arbitrary-`A` half of the problem, and its top-level target
(`max_A min_B oddrank(B) ≤ c(n)` for every `A`, not just the geometric one) is
a different overall claim than the other three, which all fix `A=A_n`. Good
technique choice in spirit (fixed-responder-rule template, per crux
`aimo-0560`), and Lemma H (full-mark-budget WLOG) is plausible and cheap.

**However, I ran a numeric check on Lemma J (the core "shave top piece down to
match the second-largest piece" universal rule) and it is falsified as
stated:**

```
n=2, c(2) = 4/7 ≈ 0.5714
A = (0.9977, 0.00223, 0.0000518)   (a valid, if extreme, Liu Bang config)
Applying the "shave p1 to p2" rule twice (using both of Xiang Yu's marks):
  round 1: (0.9955, 0.00223, 0.0000518)
  round 2: (0.9932, 0.00223, 0.0000518)
oddrank(B) = 0.9932 + 0.0000518 ≈ 0.9932  >>  c(2) = 0.5714
```

The fixed rule as literally described in the outline (spend marks shaving the
top piece down to match the current second-largest piece, repeat) does **not**
cap `oddrank(B)` at `c(n)` for skewed configurations — here Xiang Yu clearly
has a far better response (e.g. splitting the giant piece more aggressively,
not by an amount equal to the tiny second piece), so the specific mechanism
in Lemma J is wrong as a universal rule, even though the overall claim
(some Xiang Yu response achieves `≤ c(n)` for this `A`) is almost certainly
still true.

This is exactly the same failure mode CLAUDE.md and the standing rule warn
about for majorization-smoothing: a plausible-sounding mechanism asserted as
the whole selling point, refuted by a concrete instance. The difference here
is the outline was honest that Lemma J is "not yet proven, only motivated by
analogy," and it partially anticipates the problem via Lemma I ("cheap-kill:
configs far from `c(n)`'s `p_1` are easy") — but Lemma I is not actually
derived (no quantitative bound is stated), so as written there is no proof
that the regime where Lemma J's specific rule applies actually covers all of
simplex minus an easily-handled region. My counterexample lives exactly in
the gap between "Lemma I's promised cheap kill" and "Lemma J's specific rule"
— neither currently covers it.

**Required before building further:** the builder must either (a) make Lemma
I's cheap-kill quantitative and prove it actually disposes of configurations
like my counterexample (e.g. by a direct bound showing any config with `p_1`
above some explicit threshold trivially yields `oddrank(B) ≤ c(n)` via a
*different*, simpler Xiang Yu response — likely "just cut `p_1` into
`n+1` roughly-equal pieces," not the shave rule), or (b) generalize Lemma J's
rule itself to be adaptive (e.g. spend more than one mark per iteration when
`p_1` is far above `p_2`, cutting proportionally rather than by a fixed
`p_1-p_2` amount) and re-derive the induction against my counterexample
concretely before claiming the general case. Either way, Lemma J as currently
stated is not usable and must be revised, not merely "double-checked" — this
is CHANGES REQUESTED, not RETHINK, because the overall target and the
fixed-responder-rule *template* are sound and there is an evident fix
(adaptive rule / quantitative cheap-kill); the specific stated rule is what's
wrong.

Register this approach (done below) since its target is real, distinct
diversity and worth pursuing with the fix.

## equalization-potential-bound — no change (not in build set), correctly held

Outliner's plan (keep alive, no new work, explicit conditional-negative-result
framing, reuse Lemma D/E as background for the new approach's cheap-kill) is
appropriate given the still-open lower bound it depends on. No issues.

## Diversity assessment

`geometric-dominance-construction` and `recursive-embedding-induction` are
twin attacks on the *same* central gap (k>=1 lower bound against the geometric
config) via different induction variables (`k` vs `n`) — legitimate parallel
hedges per the outliner's own reasoning, not the single-gap-trap CLAUDE.md
warns about, since each independently completes the whole claim end to end
and imports (doesn't split) the shared lemma base. But flag for next round:
if BOTH stall again on Lemma F/G, that confirms this is a genuine wall in the
geometric-construction framing itself (not an artifact of one induction
choice), and the population will then need a lower-bound approach with a
framing genuinely unlike "geometric config + doubling identity" — e.g. a
direct minimax/LP-duality certificate for the specific geometric point,
independent of induction on `n` or `k` altogether.

`universal-adversary-strategy` is real, needed diversity (first approach on
the upper-bound-over-arbitrary-`A` half) but its core lemma needs a concrete
fix before it can close anything — track this closely; don't let a second
round pass with the same falsified specific rule re-asserted.

## Verdicts summary
- geometric-dominance-construction — CHANGES REQUESTED (build: close Lemma F)
- recursive-embedding-induction — CHANGES REQUESTED (build: close Lemma G)
- universal-adversary-strategy — CHANGES REQUESTED (build: fix Lemma J per
  counterexample above before/while proving it)
- equalization-potential-bound — no change, not built this round
- majorization-smoothing — RETHINK, cut again (unchanged file, still relies
  on the numerically-falsified concavity claim; not registered, not built)

Ranking updated via `mcp__approach-ranker__update_ranking` (draw between the
two geometric-construction twins; both beat the new, still-flawed
universal-adversary-strategy; universal-adversary-strategy beats
equalization-potential-bound, which remains the weakest live approach).
`universal-adversary-strategy` newly registered via
`mcp__approach-ranker__register_approach`.

build set: geometric-dominance-construction, recursive-embedding-induction, universal-adversary-strategy
