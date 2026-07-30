# proof-builder report — inversion-at-a-collinearity (round 4)

File updated: `/home/agentuser/repo/results/imo-2026-02/approaches/inversion-at-a-collinearity.md`
Status: **partial** (unchanged — genuine gaps remain, honestly recorded).

## What was done this round

1. **Fixed the stale cross-reference.** The file previously cited
   `synthetic-angle-chase-aklastar.md` for "OM=ON ⟺ A,K,L,A* concyclic (AB≠AC)", but that file
   dropped its A* framework this round. Re-derived this base reformulation **locally, from scratch**
   (new "Lemma 0"): with `A*=(a/2,q)` in the standard `B=(0,0),C=(a,0),A=(p,q)` coordinates, proved
   `OM=ON ⟺ A* on circumcircle(AKL)` for `AB≠AC`, via a clean argument that segment `AA*` is
   horizontal (both endpoints have y-coordinate q) so its perpendicular bisector is the same
   vertical line `x=(2p+a)/4` as the perpendicular bisector of `M,N`. Checked with sympy for safety;
   the proof itself is elementary coordinate geometry, fully self-contained. Made this a promotable
   lemma.

2. **Sharpened the hypothesis-translation gap from "not completed" to a precise structural
   diagnosis.** Lemma 2 (similar triangles under inversion, already certified) only transforms an
   angle at vertex Y≠A if one of its two legs passes through A. Checking the three hypotheses
   against this criterion: hypothesis (i) (∠KBA=∠ACL) has this form (leg BA, leg CA both pass
   through A) and *does* translate cleanly — worked out the full translation, hypothesis (i)
   becomes ∠AK*B* = ∠AL*C* (an angle equality between K* and L*, each also involving B*/C*).
   Hypotheses (ii) (∠LBK=∠LNC) and (iii) (∠LCK=∠BMK) do *not* have this form — neither leg of any of
   these four angles passes through A in general — so Lemma 2 gives no information about them
   directly. This is recorded as a genuine structural obstruction of the single-inversion-at-A
   framing, not merely unfinished computation: two of three hypotheses are, by their form, invisible
   to the tool. Attempting a workaround (e.g. inverting at a different center to make (ii)/(iii)
   accessible) would require recomputing the entire target-point machinery (A*, A*') for that new
   center, which was not attempted this round due to time.

3. **Resolved the isosceles branch-selection question as a non-issue for the overall problem**
   (though it remains open for this specific route). Noted that the sibling coordinate approach's
   `myexpr·Z = 2(q−T_KX)A_1 + 2(T_LX'−q)B_1` identity is unconditional (holds for any T_K,T_L,α, not
   just the branch selected by position hypotheses), and never divides by p−a/2. So whenever
   A_1=B_1=0 (hypotheses (ii),(iii) hold) on *any* root/branch, myexpr=0 follows automatically given
   Z≠0 on that branch — meaning there is no need to single out "the" geometric branch among the
   quadratic's roots in the isosceles case either. This means my own decoupling-lemma +
   branch-selection sub-project (real, correctly proved decoupling to a shared quadratic Q(α,x), but
   only numerically checked branch-selection on 10 samples) is not actually load-bearing for the
   problem's proof — the sibling approach already handles AB=AC uniformly. This is recorded
   honestly: it doesn't resolve the branch-selection question, it explains why this approach doesn't
   need to resolve it to matter for the overall population, while noting this specific approach's
   A*-based route still can't give an *independent* proof of the isosceles case (A* degenerates when
   p=a/2).

## Remaining gaps (honest)

- Hypotheses (ii),(iii) do not translate through Lemma 2 (inversion centered at A); a genuinely
  different mechanism would be needed to complete the collinearity chase for K*,L*,A*'. Not closed
  this round.
- The isosceles-case branch-selection (ruling out asymmetric/large-root branches beyond the 10
  numeric samples) is still open for this approach's own machinery, though shown not to matter for
  the overall problem given the sibling approach's uniform-in-p argument.

## Promotable lemmas (new this round)

- **Lemma 0 (Base reformulation, local, no external citation):** for AB≠AC, OM=ON ⟺ A,K,L,A*
  concyclic, with A*=(a/2,q). Proved in full, self-contained. Ready for reviewer certification.

Status stays `partial` — real progress (Lemma 0, the structural diagnosis, the meta-observation) but
the two headline gaps (hypothesis translation for (ii)/(iii); general isosceles branch-selection)
remain open, exactly as expected given this approach's lower priority this round.
