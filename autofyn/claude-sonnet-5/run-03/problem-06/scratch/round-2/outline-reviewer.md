## imo-2026-06 — Round 2 outline review

Verified independently by simulation (not just taking the outline's word):
- `python3` check on `a1=15`: the exact (untruncated) antichain of minimal prime-sets over 300
  terms stabilizes to exactly 3 generators (`{3,5},{2,3},{2,5}`) and stays flat — consistent with
  `antichain-signature-closure`'s claim that this object stabilizes in the cases we can check
  quickly.
- `python3` check on `a1=2310` (`rad=2310`): over 800 terms the antichain is still *growing*
  (243 live generators at term 800, monotonically climbing in the tail sampled), confirming the
  outline's own caveat that stabilization is not fast and not monotone in general, and that the
  "peaks then collapses" phenomenon it describes is a real, nontrivial dynamic that has not been
  proved to terminate — this is exactly the open gap, not yet resolved by either computation or
  argument.

### antichain-signature-closure (revise of core-signature-pigeonhole) — CHANGES REQUESTED (build)

Sound skeleton. Steps 1–2 are the already-certified `gap-bound` and `constraint-domination`
lemmas, unchanged. Step 4's claim — that once the antichain's *generator set* is fixed, the CRT
residue set built from those generators' exact prime sets is both necessary and sufficient — is
correctly derived from `constraint-domination` and does genuinely remove a proof step that the old
`core-signature-pigeonhole`/`growth-bound-density` framing needed: the old approach had to prove
sufficiency (easy, done) *and separately* rule out escapes via primes outside a truncated
`P={primes≤L0}` (the open "No-Escape" lemma) — two different claims bridged only by an inequality.
Here, because the antichain is built from the *exact*, untruncated prime factorizations of the
actual generator terms (not truncated by a size bound), "hits the CRT set" and "is C_true-valid" 
are the *same* statement by construction once the antichain is fixed — sufficiency and necessity
collapse into one lemma. This is a real architectural simplification, not cosmetic.

That said — per the orchestrator's flag — this is **not** a new framing. The outline itself says
"same overall spine ... as core-signature-pigeonhole," and `current.md`'s round-1 cross-cutting
diagnosis already identified "does a fixed finite covering pattern eventually suffice" as the
single shared obstruction behind `growth-bound-density`'s antichain gap, `core-signature-pigeonhole`'s
No-Escape, and (in refuted form) `monovariant-telescoping`'s `|Q|<∞`. Antichain Stabilization is a
cleaner *restatement* of that same wall (one lemma instead of two), not evidence the wall is
weaker. My a1=2310 simulation shows the antichain climbing past 240 generators with no sign of
having peaked in 800 terms — the "spends factorization budget" charging mechanism sketched in the
outline is plausible but genuinely unfinished; there's a real risk this stalls exactly where
No-Escape stalled. Approve for building (it is architecturally the strongest available reduction
and the CLAUDE.md gap-mechanism bar is met: a stated charging mechanism, not a bare label), but
flag explicitly: if the charging argument stalls again this round, treat that as round-2-of-3
evidence the wall needs a genuinely different top-level object, not a third relabeling of the same
finite-covering-pattern claim.

Watch-outs to hold the builder to (already correctly flagged by the outliner, repeat them because
they are easy to violate under time pressure): (1) do not conflate stabilization with monotonicity
— confirmed non-monotone by my own simulation, not just claimed; (2) the charging scheme must count
*growth events*, not net antichain-size change, since a single index can collapse many generators
at once; (3) `P*` is only well-defined after `N*` is fixed — do not let the builder pre-define it.

### dense-signature-vanishing (new) — APPROVE (build)

This is the genuinely different mechanism the field needs. It reuses only the *cheap, already-
certified* truncated-P signature stabilization as a partitioning device (not as the closing
argument), then tries to force eventual-linear behavior on each recurring class via a
pigeonhole + bounded-divisibility-forces-vanishing trick borrowed from crux `aimo-0680`. Crucially
it does not require ruling out escapes for individual pairs and does not require the untruncated
antichain to ever stabilize — it is a structurally independent route to the same conclusion, not a
relabeling of the shared wall. The single open step (manufacturing a divisibility identity
analogous to `aimo-0680`'s $d\mid f^d(m)-m$ for *this* recursion) is honestly flagged as not yet
derived, with an explicit warning against just asserting the analogy — good outline hygiene. Sound
technique per the knowledge base's finite-difference/pigeonhole patterns; worth building. One
caution for the builder: the outline itself notes the explorer's numerical check of gap
boundedness for signature classes was inconclusive (300–580 out of 800 terms) with a slow
simulator — re-verify with a faster bitmask simulator before leaning on any boundedness claim, and
if boundedness turns out false, report that as a concrete dead end for this specific mechanism
rather than silently degrading the argument.

### dilworth-antichain-bound (revise/replace of covering-construction-induction) — CHANGES REQUESTED (build, lower priority)

Whole end-to-end attempt (reuses steps 1–2, then 4–6, of `antichain-signature-closure`), so it is
not a fragment split across slugs. However it targets the *identical* Key Lemma
(Antichain Stabilization) that `antichain-signature-closure` needs — it is a different *technique*
(Dilworth chain-covering vs. charging) for the same open claim, not a different top-level claim.
Per CLAUDE.md's warning ("approaches that only differ in technique are too close ... hit the same
wall and fail together"), this pairing is riskier for diversity purposes than the outline's framing
suggests — it should be counted as a technique-variant within the antichain family, not as an
independent third framing (only `dense-signature-vanishing` is). It is still worth building because
a genuinely different proof technique for a shared hard lemma is legitimate hedging (one route
succeeding is enough), and the outline is honest that step 2(a) — making the "extends" relation
static despite its window depending on $n$ — may not even be formalizable, in which case that
should be reported as a clean negative rather than quietly folded into the charging argument. Base
case sanity check ($\omega(a_1)=1\Rightarrow B=1$) is a reasonable non-vacuity check, keep it.
Sanity note: this approach replaces the previously-registered, never-built
`covering-construction-induction` (elo 1502, expanded=0) — I left that slug untouched in the
population rather than deleting it, per the "cut approaches are never registered, but nothing else
is force-deleted" convention; it will simply be down-sampled over time.

### growth-bound-density — no action (correct call)

Agree with the outliner: building it this round alongside `antichain-signature-closure` would be
two approaches chasing the identical target claim with the identical unclosed gap — the exact
single-gap trap CLAUDE.md warns against. Its certified lemmas remain reusable; left unbuilt this
round is correct.

### monovariant-telescoping — no action (correct call)

`|Q|<∞` is proved false (round 1, reviewer-confirmed); RETHINK stands. Its certified Q-cover/density
lemmas remain background facts. Do not revive as framed.

### Diversity verdict for the orchestrator

Field this round: `antichain-signature-closure` and `dilworth-antichain-bound` are a technique
pair sharing one wall (Antichain Stabilization / chain-covering bound); `dense-signature-vanishing`
is the one approach that is structurally independent of that wall. That is 1 genuinely different
framing out of 3 built this round, not the full 3-way diversity the outline's prose claims. If both
antichain-family approaches (charging and Dilworth) stall again next round on the same lemma, that
is the 3-round-shared-wall signal CLAUDE.md flags — next round's outliner should be told explicitly
to bench the whole antichain family and seek a second genuinely independent mechanism alongside
`dense-signature-vanishing`, rather than trying a third technique for the same lemma.

### Ranking

Registered new slugs `antichain-signature-closure`, `dense-signature-vanishing`,
`dilworth-antichain-bound` at cold-start 1500, then ran `update_ranking` anchoring each to the
established population: `antichain-signature-closure` beats `core-signature-pigeonhole` and
`growth-bound-density` (subsumes their gap with a strictly cleaner reduction) and beats
`monovariant-telescoping` (dead-end); `dense-signature-vanishing` beats `monovariant-telescoping`
and draws with `core-signature-pigeonhole` (both unresolved, genuinely different mechanisms,
comparable promise); `dilworth-antichain-bound` beats the empty `covering-construction-induction`
it replaces and beats `monovariant-telescoping`; `core-signature-pigeonhole` and
`growth-bound-density` (real partial progress) both beat `covering-construction-induction` (never
built). Post-update standings: `antichain-signature-closure` 1546, `dilworth-antichain-bound` 1528,
`growth-bound-density` 1527, `core-signature-pigeonhole` 1515, `dense-signature-vanishing` 1510,
`covering-construction-induction` 1457, `monovariant-telescoping` 1416.

build set: antichain-signature-closure, dense-signature-vanishing, dilworth-antichain-bound
