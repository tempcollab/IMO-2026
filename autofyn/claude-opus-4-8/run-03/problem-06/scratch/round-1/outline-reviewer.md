# Outline review — imo-2026-06 (IMO 2026 P6), round 1

Fresh population, four rival framings. I independently verified the flagship reduction
numerically on all six seeds a_1 ∈ {15,35,77,105,143,255}: the sequence equals the increasing
enumeration of E_∞ from a_1 (`enum==seq? True` in every case), and the relevant-prime set
R ⊆ primes(a_1)∪{2,3} in every case (e.g. a_1=77→R={2,7,11}, a_1=255→R={2,3,5,17}). The
reduction and the isolation of the gap are honest.

## enum-covering-primes — APPROVE (flagship)
The core reduction is genuinely rigorous, not hand-waved:
- **Step 1** (every term ∈ E_∞): correct — for i≠j the defining rule gives gcd(a_i,a_j)>1 in whichever
  direction the larger index was chosen, gcd(a_i,a_i)=a_i>1, so each a_j is compatible with the whole
  sequence. Sound.
- **Step 2** (sequence = increasing enumeration of E_∞): the load-bearing new idea, and it checks out.
  Uses E_∞ ⊆ E_n in the correct direction: any compatible m in (a_n,a_{n+1}) would lie in E_n and beat
  the greedy minimum, contradiction; a_{n+1} ∈ E_∞ by Step 1. This kills the transient and delivers the
  "for every n" (from n=1) strengthening for free. Verified numerically.
- **Step 3** (covering characterization, restriction to R): correct; membership depends only on
  primes(m)∩R via the minimal-covering-subset argument. The outliner's warning that the "≥2 of the core
  primes" predicate is FALSE is correct and important — builder must use the covering condition, not ≥2.
- **Step 4** (periodicity + counting): correct once R is finite — L=∏R squarefree, m∈E_∞ depends only on
  m mod L, enumeration of a mod-L-periodic set advances by L every T=#residues steps from n=1.

**The sole gap, Lemma F (R finite), is correctly isolated and is the genuine crux of the problem.** The
outliner is honest that the stated mechanism (a large-prime witness in a minimal covering set can always
be replaced by a small prime, using syndeticity gap ≤ a_1 + "every term divisible by a prime of a_1") is
a *proposed* mechanism, not a proof. That is the whole difficulty of P6 and where the builder must spend
its effort. The conjectured explicit form R ⊆ primes(a_1)∪{2,3} is a useful target but the builder should
be told the *finiteness alone* suffices for Step 4 — do not over-commit to the exact form if the general
finiteness argument is cleaner. Build.

Issues to close while building (Lemma F): (a) prove no prime exceeding maxfactor(a_1) is relevant;
(b) prove only finitely many small primes are recruited. The replacement/syndeticity mechanism must be
made rigorous — it is currently a sketch.

## density-bounded-recruitment — APPROVE (second crux attack, distinct mechanism)
Imports the *proven* covering-periodicity endgame (enum-covering Steps 3–4) and attacks the SAME
finiteness crux by a genuinely different mechanism: term density ≥ 1/a_1 (bounded gaps) vs. a large prime
q covering only density ≤ 1/q of terms, so q cannot be forced into the covering family. This is exactly
the CLAUDE-mandated "second independent attack on the one true crux" — different tool (analytic
density/Bertrand) from enum-covering's combinatorial minimal-covering witnesses. The "too sparse to be
forced" step is a real, honestly-flagged gap: sparsity of q-multiples does not by itself forbid a single
witness term from being irreplaceable, so the builder must convert density into an actual replacement/
non-relevance argument. Technique is plausible and worth a shot. Build.

## finite-state-window — CHANGES REQUESTED (keep for framing diversity)
The only framing that avoids E_∞ entirely (automaton state + pigeonhole), so it protects the field from
collapsing to one framing. Two gaps, both hard and honestly stated: G1 (recruited-prime set Q finite) is
essentially the same finiteness fact as Lemma F, and G2 (state-determinism / forward propagation) fights
the fact that the greedy rule depends on *all* earlier terms — unbounded memory. The outliner correctly
warns that the corpus propagation skeleton (aimo-0079) is a single reindex, far weaker than needed, and
that G2 must stay independent of the covering characterization or the approach collapses into
enum-covering. G2 is under-specified — no concrete mechanism yet for why a finite recorded state
determines the next term against unbounded memory. Build to explore the independent framing, but the
builder must supply a real G2 mechanism, not a bare "by determinism."

## difference-sequence-squeeze — CHANGES REQUESTED (registered, NOT built this round)
Distinct object (gap sequence d_n) and distinct wall (a manufactured divisibility for an aimo-0680-style
squeeze). The most speculative: the outliner itself flags R2 as "make-or-break" and "not guaranteed by
analogy — if none exists, record dead end." Since round-1 builder effort is better spent on the two crux
attacks plus the independent automaton framing, this stays in the population for later sampling but is not
in the build set. Not doomed enough to cut — it is a legitimately different framing worth keeping.

## Diversity assessment
The field does not collapse to one wall. enum-covering and density-bounded-recruitment share the E_∞/
covering endgame but attack the finiteness crux by different mechanisms (combinatorial vs analytic);
finite-state-window and difference-sequence-squeeze attack different objects (automaton state; gap
sequence) with different walls (propagation; squeeze divisibility). Note for the orchestrator: three of
four approaches ultimately need "finitely many relevant/persistent primes" — if all crux attacks stall on
finiteness for 2+ rounds, next round should seed a framing that does not route through prime-finiteness at
all.

## Ranking (Elo after this round)
enum-covering-primes 1546 > density-bounded-recruitment 1515 > finite-state-window 1485 >
difference-sequence-squeeze 1454.

build set: enum-covering-primes, density-bounded-recruitment, finite-state-window
