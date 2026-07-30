# Outline review — round 16 v2 (imo-2026-03)

## universal-adversary-strategy (revise): 5-strategy closure of m=4 Case C, incl. new tail-internal-tie Strategy C

**Verdict: APPROVE.**

This is a genuine repair of the flaw I found earlier this round (RETHINK
of `proof-outliner.md`), not a relabeling of the same failed plan. I
independently re-verified every load-bearing numeric and structural claim
from scratch (fresh Python, exact `fractions.Fraction`, my own recursive
`V_3`/`V_4` implementations, not reusing the outliner's script) and found
no error. Scripts: `/tmp/round-16/verify_v2.py`, `/tmp/round-16/adv_search_v2.py`,
`/tmp/round-16/edge_check.py`, `/tmp/round-16/local_perturb.py`.

### 1. Citation fix is correct

Checked `lemmas/double-insert.md` directly: DOUBLE-INSERT is indeed
hypothesis-free (`oddrank(\{v,v\}\cup T)=oddrank(T)+v` for *any* list `T`
and any `v`), unlike `lemmas/block-recurse.md`'s stated hypothesis
(`r:=p_1-S_j<t_j`), which Case C alone does not guarantee. Every one of
the outline's 5 constructions (Strategy A: split `p_1\to(t_1,r)`; Strategy
B: split `p_1\to(p_1/2,p_1/2)`; Strategy C_{ij}: split `\max(t_i,t_j)\to
(\min(t_i,t_j),r)`) is exactly of the form "split one value, and the
result duplicates an existing list element" — DOUBLE-INSERT applies
unconditionally to each. This is the right citation; I found no case where
it's actually needed to invoke the stricter BLOCK-RECURSE hypothesis.

### 2. `V_3`'s 3-case closed form matches the certified round-9 theorem

Re-read `lemmas/ptbi-threshold-reduction.md` (Cases A/B, general `m`) and
`current.md`'s round-9 entry ("m=3's general upper bound is now solved in
full, unconditionally over every configuration," `min(TAIL-SNIP,
BLOCK-RECURSE_1)\le4/7` throughout Case C). The outline's `V_3` pseudocode
(Case A: peel-half+`L_2` IH; Case B: DOM; Case C: `min(x_1+x_3/2,
x_2+L_2(x_1-x_2,x_3))`) is a faithful transcription of that certified
theorem. This is the fix that mattered: I independently confirmed on the
exact witness that using the incomplete 2-branch `V_3` (the round-16-draft
bug) gives `V_3(1859,931,8)=1859` (spurious, DOM-only), while the correct
3-case `V_3` gives `1403` (Case A fires) — a `456`-unit difference that
is exactly why Strategy C now succeeds.

### 3. Independent re-verification of the headline witness — exact match

Reproduced `A=(1859,931,619,611)` (`\Sigma=4020`, target `2144`) with my
own implementation:
```
StratA = 2161,  StratB = 4319/2 = 2159.5,
StratC_{01} = 4319/2 = 2159.5,  StratC_{02} = 4319/2 = 2159.5,
StratC_{12} = 2014   <- winner, exactly matches the outliner's number
min = 2014 <= target = 2144   [PASS]
```
Exact `Fraction` arithmetic throughout, no floating point.

### 4. Independent adversarial search — found and confirms an EXACT tight point

I ran two independently-parametrized `scipy.optimize.differential_evolution`
searches (sigmoid-squashed and direct-ratio simplex parametrizations, 5+4
seeds, `popsize` 60-80) over the continuous Case-C 4-parameter space,
minimizing `target - min(5 strategies)`. **Both converge to the same
global point, margin exactly 0 to machine precision**, which I then pinned
down exactly: `A=(6,4,3,2)` (any positive scaling), `\Sigma=15`,
`target=c(3)\cdot15=8`. Exact `Fraction` check:
```
StratA = StratB = StratC_{01} = StratC_{02} = StratC_{12} = 8 = target, EXACTLY.
```
All five candidates tie the target simultaneously at this one point — a
striking and useful fact for the builder (see below). I additionally ran
30,000 random Case-C `m=4` integer trials (zero violations, worst margin
`83/15`) and 20,000 trials concentrated near the `p_1\to\Sigma(tail)`
boundary and near `t_3\to0$ (zero violations, worst margin `\approx0.0098`),
plus 50,000 local perturbations around the exact tight point `(6,4,3,2)`
(zero negative margins, smallest found `1/1875`). This is strong,
independently-reproduced evidence the bound holds everywhere in Case C for
`m=4`, with the extremal boundary now pinned to an exact rational point
rather than merely "found numerically."

### 5. Mark-budget bookkeeping checked

Each strategy costs exactly `1` (the split/tie) `+ \le2` (`V_3`'s own
budget) `\le3=m-1` — verified this is consistent for all 5 candidates
against the stated recursive triples (`Strategy A` recurses on
`(t_2,t_3,r)`; `Strategy B` on `(t_1,t_2,t_3)`; `Strategy C_{ij}` on
`(p_1,t_k,r)`), matching the outline exactly.

### 6. What remains open (correctly flagged, not fatal)

The `\le15`-way algebraic case split (Step 4) is genuinely not yet written
— correctly reported as an open item, not overclaimed. **Builder guidance**
(new, from this review's independent search): the exact tight point
`A=(6,4,3,2)` is a genuine simultaneous 5-way tie — this is a strong hint
that the algebraic case split's hardest boundary sits exactly here, and
that a slicker argument (e.g. showing all 5 candidates coincide on a
codimension-2 locus and are individually monotana away from it) may be
available instead of 15 raw sub-cases. Flag this concretely to the
builder as a shortcut to try before grinding through all 15 cases by
brute force.

No fatal flaw found. Approve to build.

## recursive-embedding-induction (advance, no new work)

**Verdict: APPROVE** (trivial, no-op nomination). Fully proved lower
bound (`lemmas/tree-bound-multicluster.md`, certified round 10), out of
scope for this round's Case C work, no regression risk, nothing to verify
that hasn't already been independently re-verified in prior rounds. No
build needed.

## Diversity note

Still a single active line on the open gap (`universal-adversary-strategy`),
but this round is real, verified, non-trivial progress on that line — not
a repeat of a previously-refuted framing. The `m=4`-specific "bounded tail
tie" content is a genuinely new, smaller-scope tool (not general
SLACK-COVER) and the numerics now support it strongly, including
identifying the exact extremal point. If the case-split write-up stalls
for 2+ more rounds, the diversity mandate should still be invoked (per
CLAUDE.md), but this round does not yet call for it — real forward motion
was made, with a genuinely new mechanism (Strategy C) rather than a
re-derivation of the already-refuted peel-vs-halve-only menu.

## Ranking

Ranked `universal-adversary-strategy` above every currently-dead-end
sibling (`case-c-secondary-extremality`, `case-c-slack-covering`,
`defect-hall-deficiency`, `minimax-mixed-duality`,
`majorization-smoothing`, `relaxed-adversary-transfer`), above the two
weaker-`partial` approaches (`equalization-potential-bound`,
`potential-averaging-bound`), and above its own narrower-scoped twin
`universal-adversary-strategy-exact-tie` (whose "advanced" outcome was a
negative/diagnostic result, smaller in scope than this round's positive
construction). Compared as a draw against `recursive-embedding-induction`
(both are currently the strongest live approaches in their respective,
non-overlapping scopes — lower bound fully closed vs. upper bound real
progress this round — no direct head-to-head signal to break the tie).
This also clears the stale flag on `defect-hall-deficiency` from last
round.

## build set: universal-adversary-strategy
