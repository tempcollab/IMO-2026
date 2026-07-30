## Status
unsolved

## Approaches tried

- **Relax-the-game-then-transfer-down** (`aimo-0560` surrogate/relaxed-adversary
  pattern, `games-and-strategy`), attacking the upper bound
  `max_A min_B oddrank(B) ≤ c(n)` over **arbitrary** Liu Bang configurations
  `A` (not just the geometric `A_n`). Distinguishing mechanism from every
  other live upper-bound approach (`universal-adversary-strategy`,
  `minimax-mixed-duality`, `geometric-dominance-construction`): those all
  enumerate Liu Bang's tie/vertex structure and exhibit a matching named move
  (DOM/HALVE/TAIL-SNIP/SANDWICH/PARTIAL-DOM/MULTI-HALVE); this approach
  instead relaxes Xiang Yu's mark budget to unlimited, solves the relaxed
  game in closed form, and attempts to transfer the relaxed optimum down to
  the real `≤n`-mark game.

  **Mandatory cheap gate (run before any truncation-lemma attempt, per the
  outline-reviewer): result — the gate FAILS, and fails in the sharpest
  possible way (total degeneracy, not partial loss). Verdict: dead end,
  reported honestly below, not forced into a proof.**

  — **RETHINK: the relaxed (`∞`-mark) game is completely degenerate.** Its
  optimal value `V_∞(A) = 1/2` for *every* configuration `A` and *every*
  `n` (Theorem V-INF below, proved exactly, not just checked numerically).
  This value (a) does not depend on `A` at all, so it carries zero
  information to transfer about *which* configuration is hardest for
  Xiang Yu — the entire content of the problem (why `c(n) > 1/2` and how
  the gap shrinks with `n`) is invisible to the relaxation; (b) is achieved
  using exactly `n+1` marks (one per piece of `A`), i.e. **one mark more**
  than Xiang Yu's actual budget `n` — the relaxation doesn't even
  approximate the real game asymptotically, it requires a budget increment
  of exactly 1 to reach its optimum, and that "one extra mark" is precisely
  the missing resource that makes the real game's answer `c(n) > 1/2`
  instead of `1/2`; (c) sits on the **wrong side** of the inequality needed:
  since `∞`-mark Xiang Yu is only *more* powerful than `n`-mark Xiang Yu,
  `V_∞(A) ≤ min_{B: ≤n marks} oddrank(B)` for every `A` — i.e. `V_∞` is a
  **lower** bound on the real `n`-mark value, not an upper-bound template
  that could be "rounded down" to give a valid `n`-mark response. A
  genuine transfer lemma would need to run in the opposite direction from
  what a surrogate-adversary argument produces (a *harder* surrogate gives
  a valid strategy for the *real, easier* problem only when the real
  problem is a **restriction** of the surrogate in the direction that
  preserves the guarantee; here the real Xiang Yu is *weaker* than the
  relaxed Xiang Yu, and weakening the adversary makes life better for Liu
  Bang, not worse — so an upper bound on the value against the strong
  adversary is *not* automatically an upper bound against the weak one).
  These three facts together (config-independence, wrong-side budget gap,
  wrong-direction inequality) show the relaxation is not merely lossy but
  structurally the wrong tool for this target. Explicitly checked against
  the outline-reviewer's caveat: **this does not converge with
  `universal-adversary-strategy`'s or `minimax-mixed-duality`'s target.**
  The relaxed optimum is *not* achieved at a configuration-dependent
  finite tie-structure of the kind Lemma TIE-NECESSARY's discrete search
  produces — it is achieved by a single universal move (halve every piece)
  that ignores `A` entirely and is one mark over budget. So there is no
  load-bearing overlap to flag; the two other approaches' target (which
  tie-structure, using exactly `≤n` marks, is globally optimal for a given
  `A`) is untouched by this finding.

  — A follow-up experiment (not part of the gate, done to see whether the
  degenerate relaxed solution could still be salvaged by truncating it, i.e.
  "halve `n` of the `n+1` pieces, leave one whole") confirms the salvage
  fails too: this specific truncated construction reproduces `c(n)` exactly
  on the geometric configuration `A_n` (skipping the smallest piece) — a
  cute coincidence, not a new proof, since Proposition 4 already gives an
  exact-equality construction for `A_n` — but on generic (non-geometric)
  configurations, exhaustive random search finds it **badly violates** the
  bound: e.g. `n=1`, `A=(4/7,3/7)`, the best "halve one piece, leave the
  other whole" response gives `oddrank=5/7`, far above `c(1)=2/3`. So even
  the natural finite truncation of the degenerate relaxed strategy is not a
  valid general-purpose response; recovering a good response for such
  configurations requires exactly the case-by-case reasoning (which piece
  to touch, at what ratio) that `universal-adversary-strategy` /
  `minimax-mixed-duality` are already doing. There is no shortcut hiding
  inside this construction.

  **Conclusion:** the relax-then-transfer mechanism, as concretely
  instantiated here (unlimited splits = relax the *mark budget*), cannot
  give a useful bound for this problem, because the natural relaxation
  collapses to a constant (`1/2`) that (i) ignores `A`, (ii) needs a budget
  of `n+1` not `n`, and (iii) bounds the real value from the wrong side.
  This is a genuine dead end for the surrogate/relaxed-adversary proof
  shape as applied to the mark-budget axis of this game. (A different
  relaxation — e.g. relaxing something other than the mark count, such as
  allowing Xiang Yu to see Liu Bang's marks *before* committing to how many
  he'll use, which is already true, or relaxing to a continuous "mixing
  weight" version — is not what was tested here and is not ruled out by
  this finding; but per the outline-reviewer's explicit instruction not to
  re-open plain mixing-over-the-named-menu, and since no alternative
  relaxation was identified this round, this slug is retired rather than
  continued into an unmotivated new relaxation.)

## Current best

No positive progress toward the target theorem (upper bound over arbitrary
configurations). The one substantive output of this round's work is a
**correctly proved, general, negative result** ruling out this entire proof
shape (see Theorem V-INF and the pairing lemma below), together with the
concrete numerical evidence that pins down *why* it fails (config-blindness,
off-by-one budget mismatch, wrong-direction inequality). No lemma from this
file is imported by, or overlaps with, the live lower-bound or upper-bound
work of the other approaches.

### Theorem V-INF (the `∞`-mark relaxed game is degenerate)

**Setup.** Fix any Liu Bang configuration `A = {a_1 ≥ ... ≥ a_r}` (`r ≥ 1`
pieces, `Σ a_i = 1`; no constraint on `r` needed for this theorem — it holds
for *every* finite composition of `1`, in particular every `A` reachable
with `≤ n` marks, `r ≤ n+1`). Define the **relaxed value**
`V_∞(A) := inf { oddrank(B) : B a refinement of A into finitely many pieces,
each original piece split into arbitrarily many further pieces at
arbitrary positive ratios, no limit on the number of splits }`, where
`oddrank(S) = f(S)` is the claiming-phase value from Lemma
`claiming-phase-value.md` (sum of the odd-ranked elements of `S` sorted
descending).

**Claim.** `V_∞(A) = 1/2` for every `A`, and the value `1/2` is **achieved**
(not merely approached) by refining every piece of `A` into exactly two
equal halves — a finite construction using exactly `r` marks (one per
piece of `A`).

**Proof.**

*Lower bound `oddrank(B) ≥ Σ(B)/2` for every finite multiset `B`, by a
direct pairing argument (Lemma PAIR-LB).* Let `B` sorted descending be
`b_1 ≥ b_2 ≥ ... ≥ b_N`. Group consecutive pairs
`(b_1,b_2), (b_3,b_4), ...`; if `N` is odd, the last group `(b_N)` is a
singleton. In each pair `(b_{2i-1}, b_{2i})`, sortedness gives
`b_{2i-1} ≥ b_{2i} ≥ 0`, so `b_{2i-1} - b_{2i} ≥ 0`. Summing over all
complete pairs, and adding `b_N ≥ 0` if `N` is odd,
```
oddrank(B) - evenrank(B) = Σ_i (b_{2i-1} - b_{2i}) [+ b_N if N odd] ≥ 0,
```
where `evenrank(B) := b_2+b_4+⋯`. Since `oddrank(B)+evenrank(B)=Σ(B)`, this
gives `oddrank(B) ≥ Σ(B)/2`. Applied to any refinement `B` of `A`
(`Σ(B)=Σ(A)=1`), this gives `oddrank(B) ≥ 1/2` for *every* refinement `B`,
with **arbitrarily many marks**, hence `V_∞(A) ≥ 1/2` for every `A`. ∎ (Lemma
PAIR-LB)

*Upper bound / achievability: `V_∞(A) ≤ 1/2`, attained at `r` marks.*
Refine `A` by splitting each piece `a_i` into two equal halves `a_i/2, a_i/2`
(one mark per piece, `r` marks total, all `2r` resulting pieces distinct in
value across different original pieces generically, or tied — doesn't
matter, see below). Sort the resulting multiset `B` descending: because
`a_1 ≥ a_2 ≥ ... ≥ a_r`, the `2` copies of `a_i/2` occupy a contiguous block
of `2` consecutive ranks in the sorted order of `B` (all copies of `a_i/2`
are `≥` all copies of `a_j/2` for `j>i`, and `≤` all copies of `a_j/2` for
`j<i`; ties between blocks, if any, can be broken arbitrarily without
affecting the computation below since tied elements contribute identically
regardless of which copy is assigned which rank). Within any block of
**exactly 2** equal values occupying two consecutive ranks `(s, s+1)` of the
global sorted order, exactly one of `s, s+1` is odd and the other is even,
**regardless of the parity of `s`** (any two consecutive integers contain
exactly one odd and one even). Hence each block of `2` contributes exactly
one copy of `a_i/2` to `oddrank(B)` and exactly one copy to `evenrank(B)`.
Summing over all `r` blocks,
```
oddrank(B) = Σ_{i=1}^r (a_i/2) = Σ(A)/2 = 1/2.
```
This exhibits a refinement achieving `oddrank(B) = 1/2` exactly, so
`V_∞(A) ≤ 1/2`. Combined with Lemma PAIR-LB, `V_∞(A) = 1/2`, attained (not
just approached), using exactly `r` marks (`r` = number of pieces of `A`,
`r ≤ n+1` when `A` comes from `≤n` Liu Bang marks). ∎ (Theorem V-INF)

**Reviewer-facing verification (exact `Fraction` arithmetic, reproduced in
this round's build):** confirmed `oddrank(halve-every-piece(A)) = 1/2`
exactly for the geometric configurations `A_1=(2/3,1/3)`,
`A_2=(4/7,2/7,1/7)`, `A_3=(8/15,4/15,2/15,1/15)`, and two non-geometric
configurations `(1/2,3/10,1/5)` and `(1/2,1/5,1/5,1/10)` — matches the
closed form in every case.

### Why this kills the transfer step (the gate's honest-stop condition)

Per the outline's mandated gate: "if the relaxed optimum is numerically
clean [...] attempt the truncation lemma; if the relaxation is degenerate
[...] report that honestly." Theorem V-INF shows the relaxation *is*
numerically clean (a closed form!) but **also degenerate** in exactly the
sense the gate warned about: `V_∞` carries no dependence on `A`, so there is
no configuration-specific information in the relaxed optimum to transfer
down — every configuration relaxes to the *same* value `1/2`, and the real
target `c(n) = 2^n/(2^{n+1}-1)` is strictly bigger than `1/2` for every
finite `n` (with gap `c(n)-1/2 = 1/(2(2^{n+1}-1)) → 0` as `n→∞`, but
strictly positive and configuration-independent for fixed `n`). Since
`c(n)` is a max over `A` of a genuinely `A`-dependent quantity
(`min_B oddrank(B)`), and the relaxed value has already thrown away all of
that `A`-dependence, no truncation/rounding lemma applied *after* the
relaxation step can recover the needed `A`-dependent bound — the
information loss happens at the relaxation step itself, not at the
transfer step, so there is nothing left to transfer. This is a structural
diagnosis, not merely "we couldn't find the lemma": the relaxed problem is
provably a different (strictly easier, and direction-reversed, see above)
problem from the one that needs solving.

Numeric follow-up (the "halve all but one piece" truncation, using exactly
`n` marks) was tested as the most natural candidate salvage and **fails
badly** on non-geometric configurations (e.g. `n=1`, `A=(4/7,3/7)` gives
`5/7 > c(1)=2/3`; systematic random search over `n=1,...,4` found many such
violations), confirming there is no easy fix within this mechanism.

## Full proof
(Not present — Status is `unsolved`. This approach's deliverable this round
is a rigorous negative result, Theorem V-INF, ruling out the relax-the-
mark-budget mechanism for the upper bound; it does not itself make progress
toward `c(n)`.)
