# Proof review — imo-2026-03, round 2

Reviewed three built approaches: `geometric-dominance-construction`,
`recursive-embedding-induction`, `universal-adversary-strategy`. Also read
`equalization-potential-bound.md` (unbuilt this round, context only) and all
`lemmas/*.md`. Independently re-derived and numerically stress-tested (exact
`fractions.Fraction` arithmetic, not floating point, thousands of random
trials each) every load-bearing identity claimed new this round, rather than
trusting the write-ups.

## Verification methodology and results

For each claimed new lemma, I wrote an independent Python script (exact
rational arithmetic) and checked the identity against random instances,
separately from how the builder verified it in-file:

- **Lemma F1** (`geometric-dominance-construction`): single-mark top-split,
  tail untouched — checked `oddrank({x,a}∪T_0) ≥ p_1` for `n=1..6`, 500
  random rational `a∈[0,p_1/2]` per `n`. No violation; minimum always
  exactly `p_1`. **Confirmed correct.**
- **Lemma DOM** (`universal-adversary-strategy`): `oddrank(B)=p_1` exactly
  when `p_1≥S`, arbitrary tail shape — checked 3000 random trials (random
  tail size 1–5, random tail values, random `p_1≥S`). Zero failures.
  **Confirmed correct, and correctly general** (works for any tail shape,
  not just the geometric one, as claimed).
- **Lemma HALVE** (`universal-adversary-strategy`): `oddrank(B)=p_1/2+oddrank(T')`
  when `p_1≥2p_2`, `T'` any refinement of the tail — checked 3000 random
  trials including randomized further splitting of tail elements. Zero
  failures. **Confirmed correct.**
- **Lemma G1 recursion** `c(n)=2λ_n c(n-1)` (`recursive-embedding-induction`):
  checked exactly for `n=1..7` against the closed form. All match.
  **Confirmed correct.**
- **The refuted Candidate Lemma's counterexample** (`recursive-embedding-induction`):
  recomputed `S={37/100,37/100,36/100}`, `T={73/200,71/200}` exactly;
  merged/sorted gives `74,74,73,72,71` (in units of `1/200`), odd-rank sum
  `218/200=109/100 < Σ(S)=110/100`. **Confirmed correct** — the "bound the
  merge by sums alone" candidate really is false, exactly as claimed, not a
  floating-point artifact.
- **Lemma S** (super-increasing identity): direct algebra check, correct
  finite geometric series computation, matches Lemma 2 as the `i=1` case.
  **Confirmed correct.**
- **Lemma G0** (full n=1 case, all k): re-derived by hand; the three
  order-type sub-cases the builder lists do exhaust all possibilities for
  `s_1≥s_2>0, s_1+s_2=2/3` merged with `1/3` (the "collapse to boundary
  point" claims in cases 2 and 3 are correct algebra: `s_1+s_2≥2/3` forced
  equality given the fixed sum). **Confirmed correct.**

No numerical or logical error was found in any of the newly claimed lemmas
across all three approaches. This is a genuinely positive result — three
independent builders each produced correct, verified new mathematics this
round, and none overclaimed (all self-report `Status: partial`, matching
reality).

## Per-approach verdicts

### `geometric-dominance-construction` — CHANGES REQUESTED (Status: partial, confirmed correct as stated)

**What's proved and verified:** Lemma S (uniform super-increasing identity,
correct, trivial extension of Lemma 2), the evenrank reformulation (correct,
trivial), and Lemma F1 (single-mark top-split, tail untouched, all `n` —
correct, verified independently). Combined with the already-certified
Proposition A, this closes `k=0` (all `n`) and `k=1` tail-untouched (all
`n`) of the lower bound.

**The gap, precisely:** `k≥2` (tail untouched) is only numerically pinned to
a "doubling family" of splits via a conjectured (unproven) recursive slack
identity `slack(k,n)=λ_n·slack(k-1,n-1)`; this identity is *not* proved
symbolically in general (only checked for `n≤5`), and even if proved would
only show one specific family attains `c(n)`, not that no other composition
beats it — the true minimization-over-all-compositions claim remains open.
Any `k≥1` with simultaneous tail-splitting is also open, and the builder
gives a genuine counterexample showing the naive extension of Lemma F1 fails
when the tail is refined beyond the legal mark budget (illustrative, not a
counterexample to any claimed theorem — correctly caveated as "not a legal
move" in the file). The upper bound over arbitrary configurations is
untouched by this approach.

**Verdict rationale:** real, verified progress (Lemma F1 genuinely extends
prior coverage from `k=0` only to `k∈{0,1}`); the self-reported `partial`
status is accurate — no overclaim. Route back to the builder to attack `k≥2`
directly (the "no split beats the doubling family" minimization claim is the
single most promising next target, since it is now a concretely stated,
bounded combinatorial claim, not vague).

### `recursive-embedding-induction` — CHANGES REQUESTED (Status: partial, confirmed correct as stated)

**What's proved and verified:** Lemma G0 (full `n=1` lower bound, both
`k=0` and `k=1`, every split — a complete result, not a hand-check; verified
correct), Lemma G1 (exact recursion `c(n)=2λ_n c(n-1)`, verified for
`n=1..7`), and — most valuable — a rigorous, independently-confirmed
counterexample refuting the "merge bounded by aggregate sums alone" Candidate
Lemma. This is a genuine negative result: it proves (not just observes) that
no purely-scalar induction-on-`n` argument via Lemma G1 can close the
remaining gap, which sharply reduces the search space for whoever attacks the
gap next (they must carry ordered/positional information through the
induction, not just totals).

**The gap, precisely:** general `k≥1` with simultaneous tail-splitting, for
`n≥2`, remains open; the upper bound over arbitrary configurations is not
attempted here at all (explicitly deferred to `universal-adversary-strategy`).

**Verdict rationale:** correct, non-overclaimed, and this round's negative
result (the counterexample) is exactly the kind of "genuinely new, reusable
information" the population needs — it forecloses one entire class of
future attempts rather than just failing quietly. Route back for a future
attempt that carries ordered/positional structure through an induction on
`n` (per the builder's own honest diagnosis), or pivot the builder to help
close `geometric-dominance-construction`'s `k≥2` gap since both approaches
now converge on structurally the same missing statement.

### `universal-adversary-strategy` — CHANGES REQUESTED (Status: partial, confirmed correct as stated)

**What's proved and verified:** Lemma DOM (fully general domination
construction, any tail shape, `p_1≥S` regime — verified correct by 3000
random exact-fraction trials) and Lemma HALVE (fully general halving
reduction identity, any tail shape, `p_1≥2p_2` regime — verified correct by
3000 random exact-fraction trials, including randomized further tail
refinement). These combine to give a complete, correct closure of `n=1` for
**every** possible Liu Bang configuration (not just the geometric one) — the
first result in the whole population that touches the arbitrary-configuration
upper bound at all. The three "dead end" write-ups (fixed-decrement Lemma J,
pure repeated-halving, and the `p_1 vs 2S` two-way switch) are each backed by
a specific falsifying numerical instance, correctly diagnosing why a static
single-threshold rule cannot work in general (confirmed plausible: the
claimed optimal counter-response splitting both `p_1` and a non-adjacent
`p_3` is a believable outcome of a genuine multi-piece optimization, though I
did not re-run `scipy` myself to reproduce that specific numeric instance —
it is used only as supporting diagnosis for an already-honest "not closed"
admission, not as a load-bearing step in any proof, so this does not affect
the verdict).

**The gap, precisely:** the general-`n` upper bound needs a genuinely
recursive combination of Lemma DOM and Lemma HALVE (deciding per-piece,
recursively, not via one static threshold) — not yet formulated or proved.

**Verdict rationale:** this is the most structurally important contribution
of the round: it is the *only* approach addressing the upper-bound half of
the minimax, which had been completely untouched by the population through
round 1. Lemma DOM and Lemma HALVE are both fully general, verified, and
reusable regardless of how the recursion is eventually closed. Route back to
continue building the recursive combination rule; this is now the natural
approach to own the whole upper-bound side of the problem.

## Consolidated summary — overall progress this round

No approach reaches `solved`; the true consolidated `Status` for
`imo-2026-03` remains **partial**, exactly as before, but substantively
narrower than at the end of round 1:

- The lower bound (Liu Bang's guarantee against the geometric construction)
  now has `k=0` (all `n`) and `k=1` tail-untouched (all `n`) fully closed,
  plus a full closure of `n=1` (all `k`, tail-splitting included). The
  remaining lower-bound gap is now precisely `k≥2` (tail untouched, pinned
  to one unproven minimization claim about a specific family) and any
  `k≥1` with simultaneous tail-splitting for `n≥2` — and a certified
  negative result rules out the most obvious shortcut (pure scalar
  induction on `n`) for closing it.
- The upper bound over arbitrary configurations — completely untouched
  through round 1 — now has two fully general, verified reduction lemmas
  (DOM, HALVE) and a full closure of `n=1`. The remaining gap is finding
  the correct recursive (not static) combination rule for general `n`.
- All three built approaches are honestly self-reported as `partial` with
  no overclaiming; I found no numerical or logical errors in any of the six
  new lemmas checked (Lemma S, F1, DOM, HALVE, G0, G1) or the one new
  negative result (the sums-alone counterexample) — every one of them
  reproduced correctly under independent exact-arithmetic testing.
- Three new lemma files certified this round:
  `lemmas/top-split-lemmas.md`, `lemmas/generalized-domination-and-halving.md`,
  `lemmas/merge-by-sums-counterexample.md`. `results/imo-2026-03/current.md`
  updated to reflect the consolidated `Status: partial` and the two
  precisely-narrowed open gaps.
- **Suggestion for next round:** the population has now cleanly split into
  two symmetric, well-posed combinatorial sub-problems — (1) proving a
  minimization-over-compositions/interleavings claim for the lower bound,
  and (2) proving a recursive-combination claim for the upper bound — both
  of the same underlying flavor (an order-type/interleaving argument beating
  a naive sums-only bound). A future round could productively try applying
  the same interleaving-casework technique that closed `n=1` and `k≤1`
  uniformly to both remaining gaps, since they are now structurally very
  close to each other despite belonging to different approaches.
