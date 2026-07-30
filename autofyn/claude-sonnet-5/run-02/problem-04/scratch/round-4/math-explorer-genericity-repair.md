## imo-2026-04 (lens: repair the necessity/genericity bound with shift added)

- Distinct openings:
  1. **Direct repair of `corrected-genericity-bound`'s closure**, adding shift as a
     third generator, but *simplified*: drop the paper's awkward recursive
     "target-doubling" scaffolding (§2/§3 there, which tracks $V_i=2^i\theta$ and
     reflect-relative-to-$V_i$) in favor of the much more direct route that the
     *actual* sufficiency construction (`binary-word-invariant` §4) uses: one
     transfer with target $\theta$ itself (seeding the junk-free constant
     $180°-\theta$), then a chain of **shift-by-$\theta$** steps ($a\mapsto a-\theta$,
     valid while $a>\theta$) optionally interleaved with **halve** steps
     ($a\mapsto a/2$), until the junk-free lineage hits exactly $2\theta$ (triggering
     the D1 bisection double-hit) or exactly $90°$ (D2) or exactly $\theta$ itself
     (only possible as the degenerate case where a shift step coincides with $p=2\theta$,
     which is again D1). This reframes the whole "closure" as: $C^*:=$ closure of
     $\{180°-\theta\}$ under (halve) and (shift-by-$\theta$), and asks when $2\theta\in
     C^*$. This is a strictly smaller, more tractable object than the paper's 3-generator
     $C(V)$-over-doubling-targets scheme, and it is the object that actually matches
     the constructive proof, so it is the right thing to characterize.
  2. **Number-theoretic sub-lemma**: characterize exactly which $\theta$ admit
     $2\theta\in C^*$ (equivalently which $n=180/\theta$ arise). I ran a symbolic/
     numeric check (below) strongly suggesting the closed form is simply "$\theta =
     180°/n$ for integer $n\ge2$" — i.e. shift+halve, run to a hit at $2\theta$, never
     produces anything outside the already-known sufficiency family. If provable, this
     closes necessity for the *"pure shift/halve/transfer-once" strategy class*
     exactly matching sufficiency — a genuine route to a complete solve of imo-2026-04,
     not just a partial repair.
  3. **Junk-coefficient invariant, reused as-is.** The propagation analysis in
     `corrected-genericity-bound` §5 (nonzero junk never cancels: halve negates/halves
     it, "reflect"/transfer erases it only by literally discarding the junk-carrying
     angle and injecting a fresh junk-free constant, and — critically — shift is
     *already one of the enumerated "messy single-hit" cases* there, §5 bullet 3: "$B=
     \{r,p-V,q+V\}$: ... no cancellation of a nonzero $(C,D)$ ever occurs") is
     independently correct and does NOT need to be redone; it already covers shift.
     So the fix is purely combinatorial/closure-theoretic (item 1/2), not a fix to the
     algebraic-independence argument itself.
  4. **Alternative framing if 1–2 fail**: even if the exact closed form of $C^*$ isn't
     provably $\{180/n\}$ on the nose, a weaker but still useful goal is an *upper
     bound* on $C^*$ (e.g. "every element of $C^*$ has the form $180\cdot(\text{dyadic
     rational})/(\text{integer})$" or similar), which combined with case-by-case
     exclusion could still shrink the necessity gap without fully closing it — report
     this as fallback so the outliner isn't forced into all-or-nothing.

- Candidate technique(s): closure-operator / numerical-semigroup analysis of a
  2-generator (halve, shift-by-fixed-constant) affine recursion in $\theta$ (this is a
  "binary word" / continued-fraction-flavored combinatorial number theory tool — matches
  the abandoned approach's own working title `binary-word-invariant`); reuse of the
  already-certified junk-coefficient algebraic-independence invariant for the outer
  necessity wrapper.

- Cheap-kill candidates: **I ran the concrete numeric/symbolic check** — represent every
  reachable value from seed $180-\theta$ under sequences of (halve: $a\mapsto a/2$) and
  (shift: $a\mapsto a-\theta$) as $A+B\theta$ ($A,B\in\mathbb Q$), solve $A+B\theta=2\theta$
  for $\theta=A/(2-B)$, and check whether $n:=180/\theta$ is always a positive integer
  $\ge2$. Tested 20,000 random sequences of length up to 8 (Python, exact `Fraction`
  arithmetic): **zero counterexamples** — every hit gives an integer $n\ge2$. This is
  strong evidence (conjecture, not proof) that the pure (halve, shift) closure, run to a
  $2\theta$-hit, produces *exactly* $\{180/n:n\ge2\}$, no more and no less. This is the
  single most important scouting fact for the outliner: **the repair looks not just
  plausible but likely to close the whole problem**, provided the closed form can be
  proven rigorously (a manageable induction/binary-representation argument, not
  case-search). The natural proof strategy: show by strong induction on sequence length
  that at every point the reachable value is $180\cdot\frac{2^h - \text{(odd
  correction)}}{2^h\cdot(\text{denominator})}$... concretely, track $(A,B)$ as a pair of
  dyadic rationals and show $A/(2-B)$ has the required integrality by clearing
  denominators — should reduce to elementary number theory once someone sets up the
  right induction, but is not yet done here (scouting only).

- Knowledge-base entries to use: no specific dedicated KB entry found for "closure of an
  affine recursion" — check `knowledge_base.md`'s "Invariants & monovariants" entry
  (line ~117, ~191) as the general framing for why an invariant/closed-form argument is
  the right kind of tool here; otherwise this repair is closer to raw combinatorial
  number theory than a named KB technique.

- Analogous past problems (cruxes): I did not have time this pass to query the crux
  corpus directly (dispatch focus was the closure repair, and the numeric check
  consumed the budget); the outliner/next explorer should query subtopic
  "combinatorial game theory" / "invariants" / "number theory — Diophantine
  characterization of closures" per `crux_moves_documentation.md`'s exact field names,
  looking for problems of the form "characterize exactly which values are reachable
  under a fixed pair of affine moves" (e.g. Euclidean-algorithm-flavored or
  binary-representation cruxes) — flagging this as unexplored rather than claiming
  "none".

- Prior progress: **{180°/n : n≥2} ⊆ S ⊆ (0°,90°]** is the certified state (see
  `current.md`). The dead approach `corrected-genericity-bound` claimed a *smaller*
  necessity bound $F=\{180/((2^k+1)2^j)\}$ that is refuted (its closure omitted shift).
  The certified lemma `transfer-and-shift-moves.md` and `double-hit-primitives.md`
  are reusable as-is.

- Dead ends (do not retry): the *original* `corrected-genericity-bound` closure
  $C(V):=$ closure of $\{180-V\}$ under (halve) and (reflect $a\mapsto V-a$) ONLY —
  refuted, gives $\{180/(2^m+1)\}$, too small, contradicted by the certified 180°/7°
  witness. Do not resubmit this exact closure; it must be replaced (per opening 1/2
  above), not patched by re-adding reflect alongside shift in the *same* overcomplicated
  doubling-target scaffolding — that scaffolding is unnecessary machinery inherited from
  a different (and, per my analysis, non-matching) decomposition of the win condition
  than the one the actual sufficiency proof uses; recommend rebuilding the closure from
  scratch around the simpler (halve, shift) pair matching `binary-word-invariant` §4's
  real construction, rather than trying to retrofit `corrected-genericity-bound`'s
  existing §3 machinery.

- Small-case / intuition notes (all conjectural, backed by hand + numeric checks, not
  proofs):
  - Hand-verified: mixed halve/shift chains reaching $2\theta$ always give integer
    $n=180/\theta\ge2$ for several explicit short sequences (e.g. halve→shift gives
    $n=7$; shift→shift→halve→shift gives $n=9$; halve→shift→shift→shift gives $n=11$),
    matching the 20,000-trial randomized sweep above.
  - The actual $n=7$ witness in `binary-word-invariant` §4, re-examined: its 5th
    "shift" move is literally the D1 double-hit bisection in disguise, since the
    pre-shift value there equals exactly $2\theta$ ($360/7=2\cdot180/7$) — confirms
    that shift chains always terminate a win via D1, consistent with the framing in
    opening 1.
  - Conjecture (not proved): $S=\{180°/n:n\ge2\}$ exactly, i.e. the necessity gap is
    real but closable, and the true answer to the problem coincides with the already-
    proven lower bound. If the outliner can rigorously prove the (halve,shift)-closure
    claim above (item 2), combined with the untouched junk-coefficient wrapper (item 3)
    and the already-certified non-obtuse bound, the problem **solves completely**.
