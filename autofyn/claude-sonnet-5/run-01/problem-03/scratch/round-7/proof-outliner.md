# Proof-outliner report — round 7 (imo-2026-03)

Ranker standings read via `sample_approaches` (k=8): live field
`recursive-embedding-induction` (Elo 1626.6, stale), `universal-adversary-strategy`
(1550.2, stale), `geometric-dominance-construction` (1571.0, stale,
last_outcome `verified-milestone` — Proposition K fully closed round 6),
`minimax-mixed-duality` (1500.0, stale). Dead/near-dead, not revived:
`potential-averaging-bound` (1447.7), `majorization-smoothing` (1424.3),
`equalization-potential-bound` (1380.2).

`current.md` confirms (catch-up review) Proposition K — the `k=n`,
tail-untouched lower-bound sub-case — is **fully closed for every `n`**
(Lemma L + Lemma FC together). The two remaining gaps are now sharply
isolated:

1. **Lower bound, general `0≤k<n` with the tail simultaneously refined**
   (Lemma PARITY-PAIR-GEN) — `recursive-embedding-induction`'s gap.
2. **Upper bound, arbitrary Liu Bang configurations, general `n≥2`**
   (menu-coverage / matching-assignment optimality) —
   `universal-adversary-strategy` / `minimax-mixed-duality`'s gap.

`geometric-dominance-construction` has no open target of its own left this
round (its owned sub-case, Lemma V', is closed) — not re-nominated for the
build set unless the reviewer/outline-reviewer wants a fresh assignment;
left live at its current Elo, no new work proposed for it here.

---

## 1. `recursive-embedding-induction` — advance (multi-free-coordinate vertex reduction for PARITY-PAIR-GEN)

**Target this round.** Replace the round-6 "Case A / Case B" skeleton
(hedged, Case B an unworked black box) with the paritypairgen explorer's
sharper strategy: (a) close the anchor-only sub-case in full generality as
an immediate corollary of the *existing, unmodified* Lemma PARITY-PAIR, and
(b) attack the genuinely free-coordinate content by a **peeling induction on
the number of simultaneously-free coordinates**, built entirely from
already-certified tools (Lemma D-INSERT, Lemma FC's affine-interpolation
argument). This replaces "Case A/Case B" as the organizing split; the new
organizing axis is *anchor-only vs. some coordinates free*, not *even vs.
odd tying block*.

### Step 1 (cheap, should close outright this round): anchor-only closure for all `k`, all tail distributions

**Claim.** If every split Xiang Yu makes (on `p_1` and/or on any tail piece
he chooses to refine, in any combination, using any `k≤n` marks total)
lands exactly on the fixed lattice `{0,t_n,...,t_1}` (`t_i:=p_{i+1}`), then
regardless of *which* piece produced each anchor copy, the merged multiset
is `T∪{t_i with multiplicity a_i}` for some `(a_1,...,a_n)` with
`Σa_i = n+1` — i.e. literally an instance of the object Lemma PARITY-PAIR
already governs (Lemma PARITY-PAIR needs only `n+m` odd and places no
constraint on `Σa_i t_i` or on which original piece supplied which copy).
Since `n+(n+1)=2n+1` is always odd, Lemma PARITY-PAIR applies unconditionally.

**Proof obligation for the builder.** This is largely already proved by
Lemma PARITY-PAIR as certified — the only new content is the *bookkeeping*
step: verify explicitly that (i) every self-similar geometric piece, when
split exactly at its own natural half-point, reproduces an existing anchor
value one level down (this is Lemma 3, already certified — write out the
one-paragraph induction that "any anchor-exact split, from any piece,
however the marks are distributed, always lands in `{0,t_n,...,t_1}`"), and
(ii) the total anchor count is always `n+1` regardless of the split
distribution (immediate: `n` marks always produce `n+1` final pieces from
`p_1`'s original `n+1`-piece decomposition... more precisely from the whole
`A_n`, `|A_n|+k = (n+1)+n$ wait — check exactly: total pieces after Xiang
Yu's `k` marks starting from `n+1`-piece `A_n$ is `n+1+k`; the builder must
re-derive the exact multiplicity bookkeeping for the *general* case (not
just `k=n`) directly from Lemma PARITY-PAIR's generalized statement, which
already drops the `Σa_i t_i` constraint and works for any `m` with `n+m$
odd — the builder needs the parity check for the *specific* `m` that arises
here, not just `m=n+1`). **De-risk:** the explorer's exact `n=4` witness
(`a=(1,1,2,0)`, `k=2$ tail-refined, `D=t_4$ exactly) is a ready-made
worked example — reproduce it in the writeup as the concrete sanity check.

**Expected outcome:** a genuine, general, provable closure — this is not
speculative, it is "assemble already-certified Lemma PARITY-PAIR + Lemma 3
correctly," and should be written up as a complete lemma this round
(tentative name: **Lemma PARITY-PAIR-ANCHOR**), closing the entire
anchor-only sub-case of PARITY-PAIR-GEN for every `k` and every tail
distribution — strictly stronger than the round-6 skeleton's `k≤2` hedge.

### Step 2 (the real target): multi-free-coordinate vertex reduction

**Conjecture to prove (Lemma V'-GEN, generalizing the certified Lemma V').**
At the true minimizer of `D` over the joint polytope where Xiang Yu
simultaneously chooses how to split `p_1` and any subset of tail pieces,
**the number of simultaneously-free (non-anchor) coordinates is bounded by
the number of distinct pieces split** — i.e. at most one free coordinate
*per split piece*, not one globally.

**Proof strategy (concrete, from the explorer's Finding 3 — attempt this
directly, don't re-derive from scratch):**
- Lemma V' (certified, `lemmas/lemma-V-prime-free-coordinate.md`) proves the
  single-free-coordinate case for `p_1$ alone by a vertex argument on
  `{s: Σs_i = 2t_1}` with box constraints per coordinate. **Generalize the
  same argument to the joint polytope**: each split piece contributes its
  own independent linear equality (its parts sum to its own fixed value),
  so the joint feasible region is a product-like polytope cut by one
  equality per split piece; the same "vertex of a box-with-one-equality has
  ≤1 interior coordinate" fact applies *per equality*, giving ≤1 free
  coordinate per piece. This is very likely a direct, mechanical
  generalization of Lemma V's own proof (per that file's own remark that it
  never essentially used fixed-tail-ness) — the builder's job is to check
  this claim explicitly, not assume it.
- **Peeling induction.** Given a minimizer with `≥1` free coordinates, pick
  one free value `x` (in whichever piece it lives), fix everything else,
  and apply **Lemma D-INSERT exactly as Lemma FC already does**: `D` is
  affine in `x` alone on the anchor-bracket it currently occupies, so push
  `x` to whichever endpoint doesn't increase `D` (this is the *same* step
  Lemma FC certified for the single-piece case — reuse it verbatim, the
  argument doesn't care which piece `x` lives in). This strictly decreases
  the free-coordinate count (or leaves `D` unchanged, in which case move to
  the boundary point, matching Lemma FC's own boundary-snap handling).
  Repeat until zero free coordinates remain, landing in the anchor-only case
  closed by Step 1.
- **Well-founded induction on total free-coordinate count** (finite, since
  each piece contributes at most `(marks spent on it)` coordinates, all
  bounded by `k≤n`) — the builder must set this up explicitly as the
  induction's formal measure, not just describe it informally.

**Honest gaps to flag, not paper over (per the explorer's own caveats):**
(a) Lemma V'-GEN itself is unproved — a genuine new proof obligation, even
if it looks like a direct generalization; (b) the explorer did **not** find
(nor rule out) a genuine *two-simultaneous-truly-independent* free
coordinate at a sharp vertex (only a flat-face artifact at `n=4`) — if the
builder's peeling step ever needs to handle two free coordinates
interacting inside the *same* anchor bracket simultaneously, that is new
content beyond "one at a time," and must be either proved handleable by the
same one-at-a-time argument (moving one coordinate at a time while holding
the other fixed is still valid even if both are eventually free — check this
explicitly) or flagged as a further gap.

### Where Candidate 3 (pigeonhole liveness) fits

The altframing explorer's Candidate 3 (component-counting pigeonhole,
`aimo-0663`) is **not** a substitute for the peeling induction above — fold
it in only as a **fallback tactic** if the peeling induction stalls on a
specific sub-question: *does Liu Bang's configuration always have enough
"room" (untied anchor brackets) left for the peeling argument to terminate
without being forced into a degenerate all-tied configuration when Xiang Yu
concentrates marks adversarially?* If the builder hits that specific
obstruction, attempt Candidate 3's pigeonhole framing (count intervals cut
by Xiang Yu's marks vs. marks Liu Bang/the induction has "used up") as a
targeted patch — but do not open it as a parallel proof strategy; it should
only appear as a lemma inside this approach's file if actually needed.

**Deliverable for this round's builder:** Lemma PARITY-PAIR-ANCHOR (Step 1,
should close completely), plus a genuine attempt at Lemma V'-GEN and the
peeling induction (Step 2) — even if Step 2 doesn't close, a precise
statement of Lemma V'-GEN with a real proof attempt (not just "likely
generalizes") is real progress, continuing this approach's pattern of
narrowing the gap precisely each round.

---

## 2. `universal-adversary-strategy` — advance (certify cheap lemmas, fix TIE-NECESSARY, retarget away from menu-growth)

**Target this round**, per the menucoverage explorer's findings:

### Step 1: certify two cheap compositional lemmas (mechanical, should close outright)

- **Lemma PARTIAL-DOM-RESIDUAL (a.k.a. "PARTIAL-DOM + residual-refine").**
  After applying the certified Lemma PARTIAL-DOM to get `(j,r)` (residual
  rank `r` known exactly), if budget `>j` remains, apply the certified
  Lemma SPLIT to `r` *in place*, recursively, using `r`'s already-known
  sorted rank inside the merged multiset. **This composes two already-
  certified lemmas — no new proof machinery.** Worked witness to reproduce
  in the writeup: `A=(0.5798,0.3515,0.0687)`, `m=3`, budget 2 — PARTIAL-DOM
  `j=1` gives residual `r=p1-p2`, then SPLIT halves `r`, giving exact
  optimum `≈0.53435<c(2)=0.5714` (explorer's Witness 1, re-derive exactly
  with `Fraction`, not the float approximation).
- **Lemma MULTI-HALVE (cascade/multi-HALVE).** Generalizes the certified
  Lemma HALVE (`K=1`) to simultaneously halving the top `K` pieces whenever
  `p_K≥2p_{K+1}`: sorted order is
  `p_1/2,p_1/2,...,p_K/2,p_K/2,` then the tail from `p_{K+1}`; each pair
  occupies one odd + one even rank contributing `p_i/2` once each to
  `oddrank`, and the tail shifts down by the even number `2K`, preserving
  parity. **Proof is a direct rank-shift argument, same technique as
  DOM/HALVE/SPLIT** — write it out fully (the explorer's proof sketch is
  correct in substance; the builder must make it rigorous, checking the
  sortedness claim `p_1/2≥...≥p_K/2≥p_{K+1}` explicitly follows from
  `p_1≥...≥p_K$ and the hypothesis `p_K≥2p_{K+1}`). Worked witness:
  `A=(0.583,0.3461,0.0709)`, `m=3`, budget 2, `K=2` — needs only
  `p_2≥2p_3` (strictly weaker than HALVE's own `p_1≥2p_2` hypothesis),
  optimum `≈0.53545<c(2)$ (explorer's Witness 2).

Both are short, mechanical, and high-value (recursive use of the existing
menu alone already lifts `m=3$ coverage from ~74% to ~92% per the
explorer's reproduction; these two additional lemmas close `m=3,4` to 100%
on sampled sweeps — record this coverage improvement honestly in the file,
flagged as *numerical evidence*, not a proof of completeness, since sampling
≠ exhaustive).

### Step 2: fix the flagged TIE-NECESSARY write-up gap

Round 6 found the `dim(Q)=0` branch of Lemma TIE-NECESSARY's proof is
flawed (wrongly claims a 0-dim cell must come from a collapsed chain-simplex
boundary; pure independent-tie vertices also give `dim(Q)=0` without a
zero-length piece). The disjunctive conclusion "(a) or (b)" still holds
(condition (b) covers the gap) — this round, **rewrite the `dim(Q)=0` case
proof correctly**: a 0-dimensional cell of the arrangement is pinned down by
`k` independent tight constraints among {order-ties, zero-length pieces},
and the two ways this can happen are exactly conditions (a) (a collapsed
simplex-boundary / zero-length piece) and (b) (a purely tie-driven vertex,
no zero-length piece) — prove the dichotomy is exhaustive directly (any
0-dim vertex is cut out by `k$ tight linear constraints from the finite list
{`s_i=s_{i+1}`, `s_i=t_j`, `s_i=0`}; partition these into "involves a
`s_i=0`" (⟹(a)) vs. "all order-ties, no zero" (⟹(b))). This is a bookkeeping
fix, not new mathematics — should close this round.

### Step 3: retarget from "grow the menu" to "prove the matching/assignment theorem"

Per the menucoverage explorer's headline finding — the `m=5` residual needs
genuine **3-piece** simultaneous coordination (up from 2 at `m=4`), with two
recorded exact witnesses (`A=(0.4265,0.2536,0.1747,0.1014,0.0438)`, optimal
allocation `(1,0,1,2,0)`; `A=(0.3415,0.3023,0.1664,0.1404,0.0494)`, optimal
allocation `(2,1,0,1,0)`, both budget 4, target `c(4)=16/31$) — **do not
chase move #7/#8 this round.** Reframe the open problem explicitly as: given
Lemma TIE-NECESSARY's finite discrete search over tie-structures/matchings,
**prove by induction on `n` (or on `m`) that some member of that discrete
search always achieves `≤c(n)`**, using MULTI-HALVE and PARTIAL-DOM-RESIDUAL
as base mechanisms *inside* the inductive step rather than as terminal named
moves capping out at fixed `K`. Concretely: set up the induction hypothesis
as "for the `(m-1)`-piece / `(n-1)`-mark sub-game obtained by peeling off the
top piece (or top tied block), the discrete search already has a witness
`≤c(n-1)`" and show how to lift that witness one level, using the
self-similar structure (Lemma 3) the way `recursive-embedding-induction`
already does on the lower-bound side. **This is a genuine new proof attempt,
not guaranteed to close this round** — record honestly whatever partial
progress results (e.g. does the induction go through for the "peel the top
tied block" step at least in the `k=1$ base case newly recorded this round?).
Use the two `m=5$ witnesses above as the stress test: if the inductive
argument can be checked to correctly produce a `≤c(4)$ witness on both, that
is strong evidence the induction shape is right even before a fully general
proof is complete.

---

## 3. `minimax-mixed-duality` — advance (different technique on the same retargeted theorem)

Rather than duplicate `universal-adversary-strategy`'s direct casework
induction, `minimax-mixed-duality` should continue in its own distinct
proof shape — an LP/duality-style argument — but now aimed precisely at the
**same retargeted theorem** (the matching/assignment optimum is always
`≤c(n)`), since round 6 diagnosed that "find good mixing weights over the
*existing named menu*" collapses into the same casework; the fix is not to
abandon the mixed-strategy framing but to apply it to the **general
discrete search** (all of Lemma TIE-NECESSARY's tie-structures), not to a
fixed finite list of named moves.

**Concrete task this round:**
- Take the two hard `m=5` witnesses recorded by the menucoverage explorer
  (`A=(0.4265,0.2536,0.1747,0.1014,0.0438)`, budget 4, and
  `A=(0.3415,0.3023,0.1664,0.1404,0.0494)`, budget 4) — both need genuine
  3-piece coordination with non-tie, non-half ratios. **Attempt a duality
  certificate**: exhibit dual weights/multipliers (a weighting over ranks or
  pieces) such that the *value* of any Xiang-Yu response is bounded below by
  `c(n)` as a weighted-sum identity, independent of which specific
  tie-structure Xiang Yu picks — i.e. look for the "invariant that doesn't
  care about the discrete choice," analogous to how Lemma D-REFORM's
  alternating sum `D(B)` sidesteps casework on the lower-bound side. This is
  exploratory — the mandated cheap gate is: **first check numerically
  whether a fixed dual weighting reproduces `c(n)` exactly as a lower bound
  on the two `m=5` witnesses above** (and on 1-2 of the already-closed
  `m=3,4` cases, as a sanity check) before committing to a general proof.
- If the duality-certificate search stalls (as the round-6 mixing-weights
  attempt did), **honestly diagnose why** (as round 6 did) rather than
  force a write-up — a second honest "this framing doesn't shortcut the
  casework, here's precisely why" is still useful signal, especially if it
  differs from round 6's diagnosis (round 6 found "same casework"; this
  round should check specifically whether the obstruction is the same one
  or a new one tied to the 3-piece-coordination witnesses).
- Certify Lemma SANDWICH's odd-`m` scope explicitly against the new `m=5`
  witnesses (both are odd `m$... check: `m=5` is odd, `A$ has 5 pieces — 
  confirm whether SANDWICH's hypothesis `p_1<p_2+p_m` holds or fails on
  these two witnesses, and if it fails, record that as the reason SANDWICH
  alone doesn't cover them — closing the loop on why the existing menu
  entry doesn't already handle these cases).

---

## 4. NEW approach: `relaxed-adversary-transfer` (Candidate 1 — surrogate/relaxed-adversary transfer)

**Opened this round** per the altframing explorer's Candidate 1 and the
CLAUDE.md diversity mandate — the field of live approaches
(`recursive-embedding-induction`, `geometric-dominance-construction`,
`universal-adversary-strategy`, `minimax-mixed-duality`) all share one
mechanism on the upper-bound side: enumerate Liu Bang / Xiang Yu
configuration types and exhibit a matching named move per type
(DOM/HALVE/SANDWICH/PARTIAL-DOM/MULTI-HALVE/...). This new slug attacks the
upper bound with a structurally different technique: **relax the game,
solve the relaxation in closed form, then transfer down**, adapted from
`aimo-0560`'s gardener–lumberjack surrogate-adversary trick
(`games-and-strategy`, crux corpus).

**Target.** The upper bound: for every Liu Bang configuration `A`
(`n+1` pieces, from `≤n` marks) there exists a Xiang Yu response `B`
(`≤n` further marks) with `oddsum(B)≤c(n)`.

**Proof skeleton (mandated cheap/exploratory gate first, per the explorer's
own risk flag):**

1. **Define the `∞`-mark relaxation.** Same game, but Xiang Yu may split any
   piece arbitrarily many times, at arbitrary ratios (unboundedly many
   marks, or equivalently a continuum of cuts). Call the relaxed optimal
   value `V_∞(A) := inf_{B: \text{any refinement of } A} \operatorname{oddsum}(B)`.
2. **Cheap gate (do this before anything else, this round): solve `V_∞(A)`
   in closed form, or at least numerically, on 2–3 concrete small
   configurations (`n=2,3`, including both the geometric configuration
   `A_n` and at least one non-geometric configuration).** Plausible
   mechanism: with unlimited splits, Xiang Yu can, in the limit, split every
   piece into infinitesimal parts, making `oddsum→Σ(A)/2` (the "fully
   diffuse" limit) or some other clean closed form pinned by a
   symmetry/convexity argument — **do not assume this; compute it.** If
   `V_∞(A)` numerically comes out *below* `c(n)` for the geometric
   configuration `A_n` itself (recall `V_∞` is an infimum over *more*
   options than the real `n`-mark game, so `V_∞(A_n)≤c(n)` is expected/
   required — if it's strictly below, that already tells you how much
   "slack" the truncation step has to recover), record the exact numbers.
3. **If the relaxation is numerically clean, attempt the truncation/
   transfer lemma:** show the `∞`-mark optimal (or near-optimal) response
   can always be realized, or approximated with *zero* asymptotic loss
   relative to `c(n)`, using at most `n` marks — plausibly by showing the
   `∞`-mark optimum is actually achieved (not just approached) at a
   **finite** configuration already (e.g. an anchor-tie structure exactly
   like Lemma TIE-NECESSARY's discrete search), in which case the "∞-mark"
   framing is really a proof that the discrete search is complete, giving a
   *fresh, independent argument* for exactly the same target
   `universal-adversary-strategy` is chasing by direct induction — a useful
   cross-check even if it doesn't independently close the gap.
4. **Honest stop condition:** if the `∞`-mark relaxation's optimum needs
   genuinely unboundedly many splits to approach for some configurations
   (i.e. `V_∞(A) < $ the true `n`-mark optimum by an amount that doesn't
   shrink as more marks are allowed, for some fixed small `n`), the
   transfer step fails and this approach should say so plainly and pivot
   internally (e.g. to a *bounded-relaxation* version, `k`-mark relaxation
   for `k$ moderately larger than `n`, rather than full `∞`) rather than
   force a false transfer claim.

**Do not re-open plain LP/mixed-strategy duality over the *existing named
menu*** — that is `minimax-mixed-duality`'s round-6 territory and was
diagnosed to collapse into the same casework. This slug's distinguishing
mechanism is relax-the-game-then-round-down, not mix-the-known-moves; the
builder should state this distinction explicitly in the file to avoid the
outline-reviewer flagging it as a duplicate.

**Build-set recommendation:** include this new slug in this round's build
set specifically to execute Step 2 (the cheap numeric gate) — do not let the
first build attempt jump straight to the truncation lemma before the gate
result is in hand, mirroring the discipline that produced Lemma SANDWICH
from `minimax-mixed-duality`'s own mandated exploratory phase.

---

## Summary: build set recommended for round 7

- `recursive-embedding-induction` — Lemma PARITY-PAIR-ANCHOR (should close)
  + Lemma V'-GEN / peeling induction attempt (real progress expected, may
  not fully close).
- `universal-adversary-strategy` — certify PARTIAL-DOM-RESIDUAL and
  MULTI-HALVE (should close), fix TIE-NECESSARY's `dim(Q)=0` writeup
  (should close), retarget to the matching/assignment induction theorem
  (exploratory, partial progress expected).
- `minimax-mixed-duality` — duality-certificate attempt on the general
  discrete search, gated by the cheap numeric check against the two
  recorded `m=5` witnesses; honest diagnosis either way.
- `relaxed-adversary-transfer` (**new**) — cheap numeric gate on the
  `∞`-mark relaxation first; truncation lemma only if the gate result
  supports it.

`geometric-dominance-construction` — no new target this round (its owned
sub-case is fully closed); not included in the build set unless the
outline-reviewer wants to reassign it (e.g. as a second pair of hands on
Lemma V'-GEN, given its proven track record on exactly this kind of
vertex-reduction argument via Lemma FC).
