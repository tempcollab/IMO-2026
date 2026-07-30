# Round 11 — proof-builder report (`universal-adversary-strategy`)

## Status
partial (unchanged: Case C for general `m\ge4` still open)

## What was done

Per the round-11 outliner/reviewer's assignment, checked Route A first
(cheap reuse of `recursive-embedding-induction`'s certified Lemma
TREE-BOUND-MULTICLUSTER for Case C's existence question), then attempted
Route B properly generalized to matching `\ge2` simultaneous top-level
pairs before invoking the induction hypothesis (the outline-reviewer's
mandated fallback, since Route B as literally written was already caught
as an IH-strength error).

## Route A: ruled out, with a structural argument (not just a numeric check)

Read `lemmas/tree-bound-multicluster.md` in full. Its statement is a
**universal-over-responses** bound (`D(B)\ge\tau_m` for *every* forest
Xiang Yu can build) against **one fixed, highly special configuration**
(the geometric `A_n`, anchors `\tau_l=2^{m-l}`). Case C needs the opposite
shape: an **exists-a-response** statement, true for **every** (arbitrary,
non-geometric) configuration. Two independent reasons the mechanism does
not transfer:

1. **Quantifier direction is reversed** — literally invoking the lemma's
   conclusion would say "no match/self-halve response beats `\tau_m`
   against `A_n`," which (if it said anything about Case C at all) argues
   *against* match/self-halve constructions being powerful, not for it.
2. **No discrete anchor lattice in Case C.** The lemma's actual technical
   engine — Reduction R1 (a depth-`2` impurity is indistinguishable from a
   pure split), Reduction R2 (pairwise cancellation of impurities tied at
   the *same integer depth*, via the newly-checked Fact PAIR-CANCEL), and
   the Step-2 telescoping identity `\tau_1-\tau_j=\tau_2+\cdots+\tau_j` —
   all depend on every reachable value being exactly one of finitely many
   powers of `2`. Case C's residual values (e.g. `r_1=p_1-p_2`) are generic
   reals with no reason to coincide with anything, so there is no discrete
   "depth" for R1/R2 to act on and no telescoping identity to invoke.

Conclusion: the resemblance is real at the level of move *vocabulary*
("tie an existing value" / "split into two equal halves") but not at the
level of the mechanism that makes the bound provable. Route A closed, no
partial transfer found. This is reported as a structural dead end, not
revisited without a genuinely new bridging idea.

## Route B generalized (exactly 2 simultaneous top-level pairs): refuted by an exact witness

Constructed the honest, index-correct generalization: match `p_1\to p_2`
and (independently) `p_3\to p_4`, reattach both residuals into a
size-`(m-2)` tail, and legitimately invoke the strong-induction hypothesis
at size `m-2` (target `c(m-3)`, not an overclaimed stronger bound — checked
the indexing carefully against Claim PTBI's own statement).

- **Works on the known hard `m=5` witness**
  (`A=(1826,1563,1520,1514,765)/7188`): exact value
  `\approx0.51028 < c(4)\approx0.51613`, margin `\approx0.0059` (script
  `/tmp/route_b2_check.py`).
- **Fails as a universal construction.** Using that `c(k)` is strictly
  decreasing (`c(0)=1>c(1)=2/3>c(2)=4/7>\cdots\to1/2`, verified exactly),
  the construction's value is provably hardest to satisfy when `p_2+p_4` is
  smallest relative to `\Sigma`, i.e. on a near-uniform tail. Built the
  explicit family `p_1=0.499`, `p_2=\cdots=p_m=(1-p_1)/(m-1)` and found
  exact `Fraction` violations for **every** `m` tested from `4` to `100`
  (e.g. `m=6`: target `0.50794` vs. construction value `0.51997`, margin
  `-0.01204`; `m=20`: margin `-1.2\times10^{-6}$, still strictly negative).
- **Honesty check.** This witness is not a new hard case for Case C in
  general — it sits close to Lemma DOM's boundary (`p_1<S` only barely),
  and a direct optimizer search (`/tmp/true_opt_check2.py`) shows the
  already-certified Lemma PARTIAL-DOM (an *adaptive-length* chain, not a
  fixed pair count — here essentially spending nearly the whole budget
  subdividing `p_1` alone to duplicate the near-uniform tail) closes it
  easily, true optimum `\approx0.5$, comfortably under target. So the
  refutation is specifically of the *fixed two-pair template*, not of
  Case C's solvability at this witness.

## Sharpened diagnosis (recorded in the approach file)

Combining: (a) the `m=5` witness genuinely needs exactly 2 disjoint
top-level pairs plus a self-halve; (b) the uniform-tail witness needs a
long, adaptive-length PARTIAL-DOM-style chain instead; (c) Route A's
transfer fails structurally — **no fixed integer number of top-level pairs
is a universal construction for Case C.** The correct `MATCH-HALVE-EXISTS`
claim, if true, requires a config-dependent selection rule (variable chain
length plus a decision of how much budget to reserve for a terminal
self-halve), not a single small fixed-shape template. This rules out (with
proof) two more concrete candidate constructions and narrows what a
working proof must look like for next round.

## Honest assessment

Case C for general `m\ge4` is **still open**. This round's value is
negative-but-precise: two more plausible routes (a cheap lower-bound reuse,
and the natural fix to the round-10/11 IH-bookkeeping error) are now ruled
out with proof rather than left as untested hopes, and the two contrasting
witnesses (2-pair-plus-halve vs. long-adaptive-chain) give a concrete
constraint any future fixed-template attempt must satisfy simultaneously.
No false progress claimed; Status remains `partial`.

## Files
- `/tmp/route_b2_check.py` — exact-`Fraction` verification of the
  generalized 2-pair construction on the `m=5` witness and the
  uniform-tail refuting family (`m=4..100`).
- `/tmp/true_opt_check2.py` — Nelder-Mead allocation search confirming the
  uniform-tail witness's true optimum (`\approx0.5`) is achieved by
  subdividing `p_1` alone (PARTIAL-DOM-style), not by fixed pair matching.
- `/tmp/route_a_sanity.py` — confirms `c(k)` strictly decreasing (used in
  the Route B refutation's monotonicity argument).

Approach file updated:
`results/imo-2026-03/approaches/universal-adversary-strategy.md` (new
"Round 11 build" section, plus the top-of-file "Approaches tried" summary
entry).
