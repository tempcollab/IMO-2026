# proof-builder report — `universal-adversary-strategy`, round 15

## Task
Per the approach file's "Round 15 plan" (approved by the round-15
outline-reviewer): (1) prove Lemma MARKS-MONO; (2) use it to decouple
Lemma SLACK-COVER's joint covering+value statement and attempt the
`aimo-0292`-style scalar peel-induction targeted at the `m=4`
`T=(0.20,0.15,0.12,0.08)` family; (3) assemble a full proof if steps 1-2
close; (4) report honestly if a genuine gap remains.

## Result: real, verified progress; gap sharpened, NOT closed

**Status remains `partial`.** No claim of `solved`.

### Closed this round (fully proved)

- **Lemma MARKS-MONO** (`solve2(A,k)` non-increasing in mark budget `k`):
  proved in full by strong induction on the well-founded order `(k,|A|)`
  lexicographic (`k` primary). Required two harmless clarifications to
  `solve2`'s operational definition, both recorded explicitly: (1) the
  "do nothing further" option must be an unconditional candidate in the
  `min` at every recursion, not only a fallback when no move fires; (2)
  fixed a genuine latent bug where the recursion wrongly forbade
  splitting a lone remaining piece (`|A|=1`) — this move is legal and
  sometimes beneficial. Neither clarification changes any previously
  certified numeric value (checked against all four previously-reported
  witnesses).
- **Lemma EXACT-TIE-SLACK**: re-derived from the elementary "splitting
  into `j` parts costs `j-1` cuts" counting fact (not from re-running
  code): confirms 2-mark slack at the exact-tie (`r=0`) boundary, and
  exactly zero slack at `r>0`, for an *arbitrary* subset match `S` (not
  just a full-tail or contiguous-prefix match).
- Both lemmas combine into a clean **decoupling corollary**: proving
  Lemma SLACK-COVER reduces to a pure scalar covering inequality
  `Σ(S)+c(m'-1)Σ(L) ≤ c(m-1)Σ(A)`, exactly as the plan anticipated.

### Attempted but not closed: Lemma SLACK-COVER / the `m=4` family

The scalar covering induction did not close in general. Instead it
produced a genuinely new, exact-`Fraction`-verified finding that re-maps
the gap:

1. **The round-13/14 "counterexample" doesn't actually threaten Claim
   PTBI.** It refutes the auxiliary, stronger Lemma HALF-BOUND
   (`≤Σ/2`), not the real target `c(m-1)Σ`. Exactly verified:
   `T=(0.20,0.15,0.12,0.08)`, contiguous-only value `7/25=0.28`, real
   target `c(3)Σ(T)=22/75≈0.2933`, margin `1/75>0` — the actual theorem
   holds on this witness via the **already fully certified**
   contiguous-only menu (BLOCK-RECURSE/Move1/Move3/Move0), no
   non-contiguous matching needed.
2. **`m=4` evidence, not a full proof.** Extensive search (400 random
   Case-C `m=4` trials + 23 `differential_evolution` restarts +
   Nelder-Mead polish) found no violation of `c(3)Σ` under the
   contiguous-only menu; found and exactly verified the extremal
   configuration `A=(6,5,4,2)/17`: contiguous-only value `9/17`, target
   `8/15`, margin exactly `1/255>0`. Traced one natural sub-strategy by
   hand (peel `t_1`, bound leftover by the already-certified general
   `m=3` theorem) and found it is *not* by itself sufficient everywhere
   in its own sub-case (a limiting near-uniform-tail config breaks its
   closed-form condition `t_1≥(4/15)Σ`), though the *full* recursive
   minimum still succeeds there via a different branch. **A complete
   case-exhaustive hand proof for general `m=4` was not finished** —
   honestly left open, not hand-waved.
3. **Proved the bypass does NOT generalize.** Exact counterexample:
   `A=(14,12,10,9,8,4)` (`m=6`, `Σ=57`, Case C). Contiguous-only menu:
   `29`, exceeding target `c(5)Σ=608/21≈28.952` by exactly `1/21` — a
   genuine, exact failure. The full non-contiguous subset-match menu
   (independently implemented) achieves `57/2=28.5≤608/21` on the same
   instance. This proves Lemma SLACK-COVER's non-contiguous existence
   question is genuinely necessary in general, even though it may be
   avoidable at `m=4,5`.

### Net effect
Case C for general `m≥4` remains the sole open gap for the whole
problem. This round narrows it precisely: (a) two new certified lemmas
(MARKS-MONO, EXACT-TIE-SLACK) correctly decouple any future SLACK-COVER
attempt; (b) the target that actually needs proving is confirmed weaker
than the abandoned HALF-BOUND, and evidence (not proof) suggests `m=4,5`
may be closeable with already-certified machinery alone; (c) `m=6` is now
a *proved* hard case requiring genuine non-contiguous matching — a
sharper, exact replacement for the previous `m=8` test case (which the
round-15 explorer showed was never load-bearing).

## Files touched
- `/home/agentuser/repo/results/imo-2026-03/approaches/universal-adversary-strategy.md`
  — added round-15 bullet to "Approaches tried" and a full "Round 15
  build" section with both proofs and the exact witnesses.
- `current.md` not touched (reviewer-owned).

## Recommendation for next round
1. Finish the `m=4` case-exhaustive proof (case tree mapped in the
   write-up: `j*=1` vs `j*=2` top-level branches, each further branching
   on the leftover's own best move) using only already-certified
   machinery — no open existence question needed if this closes.
2. Separately, attack the now precisely-isolated `m=6` (and presumably
   larger) non-contiguous existence question directly (Lemma PAIR-VALUE
   + Hall-type argument), using `A=(14,12,10,9,8,4)` as the canonical
   hard test case going forward instead of the `m=8` witness or the
   `T=(0.20,0.15,0.12,0.08)` witness (shown this round to not actually
   require non-contiguous matching for the real theorem).
