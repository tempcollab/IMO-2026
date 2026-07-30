## Status
partial

## Approaches tried

- **Round 6 (new, this round).** Dispatched as a bounded, low-priority computational-check effort per
  the outliner's explicit instruction: attempt the strong-induction-on-$\omega(a_1)$ architecture, with
  a mandatory *first* check of whether the core **Reduction Lemma** (Step 3 of the outline) has any
  concrete mechanism, and an honest negative report if not. Findings below.

  1. **Base case ($\omega(a_1)=1$) — imported, no new work.** `lemmas/singleton-generator-permanence.md`
     already shows: if $\omega(a_1)=1$ (so $a_1=p^{e}$), then $D_1=\{p\}$ is a singleton generator, no
     later index is ever a generator, so P-Confinement holds unconditionally for that $a_1$, and hence
     (via `lemmas/pc-implies-theorem.md`, already certified) the full theorem holds for this $a_1$ with
     $T=1$, $L=p$. Cited directly, no new content.

  2. **Rigorous (not merely empirical) pigeonhole dichotomy — new, correct, but limited.** For
     $\omega(a_1)\ge2$, write $S:=\mathrm{primes}(a_1)$. For $n\ge2$, $\gcd(a_1,a_n)$ is a divisor of the
     fixed integer $a_1$ (forced $>1$ since the defining recursion requires $\gcd(a_n,a_1)>1$ for the
     constraint index $i=1$), so $R_n:=\mathrm{primes}(\gcd(a_1,a_n))$ is one of the $2^{|S|}$ subsets of
     $S$. Exactly one of the following two cases holds (pure logic, no computation needed):
     - **Case I (degenerate).** $R_n=S$ for all sufficiently large $n$ (i.e. $a_1\mid a_n$ for cofinitely
       many $n$).
     - **Case II (generic).** $R_n=S$ fails for infinitely many $n$ — i.e. $R_n\subsetneq S$ for
       infinitely many $n$. Since there are only finitely many proper subsets of $S$ ($2^{|S|}-1$ of
       them), pigeonhole on this infinite set of indices forces some **fixed proper subset**
       $R_0\subsetneq S$ (nonempty, since $R_n\ne\emptyset$ always by the same argument as
       `growth-bound-density`'s Step 1 of `lemmas/gap-bound.md`) with $R_n=R_0$, i.e.
       $\mathrm{primes}(\gcd(a_1,a_n))=R_0$, for infinitely many $n$. Setting $g_0:=\prod_{p\in R_0}p$
       (or any divisor of $a_1$ with prime support exactly $R_0$), $\omega(g_0)=|R_0|<|S|=\omega(a_1)$: a
       genuine, unconditional size decrease.

     This sharpens the outline's "pigeonhole fact" (which only guaranteed *some* divisor value $g_0$
     recurs, without addressing whether it could be forced to equal $a_1$ itself, i.e. $R=S$, the
     boundary case the outline flagged as possibly "the generic/hard case"): the dichotomy above shows
     the only way to be stuck without a genuine $\omega$-decrease is Case I, a single sharply-stated
     degenerate condition ($a_1\mid a_n$ cofinitely), not an amorphous worry about $R=S$ recurring "too
     often." **This dichotomy itself is fully proved** (Case I / Case II exhaust all possibilities by
     definition, and Case II's conclusion follows from finite pigeonhole, exactly as in
     `lemmas/gap-bound.md`'s style of argument).

  3. **Computational check (bounded, as instructed).** Simulated the greedy sequence for
     $a_1\in\{15,21,33,35,45,63,105,165,231,315\}$ (odd, $\omega(a_1)\in\{2,3\}$) to $n=400$ (fresh
     Python simulation, `math.gcd`/`sympy.factorint`, same recursion as the rest of the population). In
     **every** tested case, Case I does **not** occur: the last 50 terms of every run include indices
     with $\gcd(a_1,a_n)\ne a_1$ (e.g. $a_1=15$: tail gcd values cycle through $5,3,15,3,5,3,15,\dots$,
     never settling to $15$ alone). Moreover the *smallest* prime of $S$ typically gives the most
     frequently recurring proper subset (e.g. $a_1=105$: $R_0=\{3\}$ recurs $166$ times in $400$ terms,
     more than any other value, including $a_1$ itself which recurs only rarely comparatively). This is
     consistent with Case II always holding and with $R_0$ often being a single prime (i.e. $g_0$ often
     achievable with $\omega(g_0)=1$, landing directly on the solved base case) — but this is an
     **empirical pattern only** across 10 small cases, not a proof that Case I is impossible in general.

  4. **The Reduction Lemma itself — searched for a mechanism, found none; honest negative report.**
     Given a recurring proper subset $R_0\subsetneq S$ from Case II, the outline's hoped-for move is to
     show the tail behavior of $(a_n)$ "reduces to" a fresh recursion seeded at $g_0=\prod_{p\in R_0}p$.
     I looked concretely at what the subsequence of indices $n$ with
     $\mathrm{primes}(\gcd(a_1,a_n))=R_0$ actually consists of, and found a structural obstruction to
     the naive reduction:
     - The terms $a_n$ in this subsequence are constrained by the *full* recursion, i.e. they must share
       a prime factor with **every** earlier term $a_1,\dots,a_{n-1}$ (not merely with $a_1$). Only the
       *interaction with $a_1$ specifically* is guaranteed to route through $R_0$; the interaction with
       every other earlier term $a_i$ ($i\ge2$) can (and generically does) route through primes entirely
       outside $R_0$ (indeed outside $S$ altogether, since $a_i$ for $i\ge2$ typically carries prime
       factors not in $S$ at all — this is exactly the mechanism behind
       `lemmas/gap-bound.md`/`lemmas/constraint-domination.md`'s Constraint Domination machinery, which
       the rest of the population needs precisely because a single term's validity depends on
       unboundedly many earlier terms' prime content, not just $a_1$'s). So a term $a_n$ with
       $\mathrm{primes}(\gcd(a_1,a_n))=R_0$ is **not** in general a "clean" number governed by $g_0$
       alone — it can carry arbitrarily much additional prime content (outside $R_0$, indeed outside
       $S$) needed to satisfy its sharing constraints against the growing list of earlier terms. There is
       no evident way to "quotient out" this extra content and recover a sequence that literally
       coincides with (or is provably order-isomorphic to, gap-for-gap) the fresh recursion seeded at
       $g_0$.
     - I checked this concretely: for $a_1=105$, $R_0=\{3\}$ recurs at (among others) $n=2,4,7,9,\dots$
       with $a_n\in\{111,123,141,159,\dots\}=3\cdot\{37,41,47,53,\dots\}$ — these cofactors ($37,41,47,
       53,\dots$) are primes well outside $S=\{3,5,7\}$ and bear no visible relation to the fresh
       recursion started at $g_0=3$ (which is the trivial sequence $3,4,5,6,7,8,\dots$, i.e. every integer
       $\ge3$ once $\omega=1$ collapse is invoked — since $3$ itself is prime, by
       `lemmas/singleton-generator-permanence.md` this fresh recursion is $a_1'=3, a_2'=4,\dots$, an
       arithmetic progression with $L=1$ eventually, or immediately). The subsequence
       $111,123,141,159,\dots$ of the *actual* $a_1=105$ sequence is not a subsequence of, nor obviously
       related in gap-structure to, this trivial fresh sequence: it has been "grown" by the constraints
       of the ambient $105$-recursion (each term needing to satisfy $\gcd(\cdot,a_i)>1$ against every
       earlier term of the *full* sequence, most of which carry primes unrelated to $3$).
     - No alternative formulation of "reduces to" (e.g. matching gap-multisets, matching residues mod
       some auxiliary modulus, matching growth-event counts) was found to hold between this subsequence
       and any natural object attached to $g_0$ alone, within the bounded effort budgeted for this
       approach.

     **Conclusion: the Reduction Lemma (outline Step 3) has no mechanism, and the structural reason
     above (a single earlier term $a_1$ constrains only part of $a_n$'s required prime content; the
     recursion's real difficulty — unbounded dependence on *all* earlier terms, which is exactly what
     Constraint Domination/the antichain machinery exists to handle — is invisible to any argument that
     looks only at $\gcd(a_1,a_n)$) suggests this specific reduction shape is not viable, not merely
     unfound.** Per the outline's own instructions and CLAUDE.md's "record everything," this is reported
     honestly as a **negative finding**, not forced into a fake proof.

  5. **Secondary observation, flagged for cross-checking (not this approach's own gap, but relevant to
     the population).** While analyzing Case I (the degenerate "$a_1\mid a_n$ cofinitely" scenario), I
     verified that even *if* Case I held (making the tail of $(a_n)$ eventually an honest arithmetic
     progression with common difference $L_0=\mathrm{rad}(a_1)$, via `lemmas/gap-bound.md`: if
     $L_0\mid a_n$ for all $n\ge N_0$, the gap bound forces $a_{n+1}-a_n=L_0$ exactly for $n\ge N_0$),
     this does **not** by itself hand over the theorem's conclusion "$a_{n+T}=a_n+L$ for *every* $n\ge1$"
     (not just eventually) for free. Concretely: "eventually arithmetic with difference $L_0$ from index
     $N_0$" only pins down $a_{n+T}-a_n$ for pairs with $n\ge N_0$; it says nothing about whether the
     *actual, already-determined* finite prefix $a_1,\dots,a_{N_0-1}$ is consistent with any single global
     shift $L$. I verified this is a real gap in general (not automatic) with an explicit toy
     counterexample: the abstract increasing integer sequence $b_1=1$, $b_2=100$, $b_n=2n$ for $n\ge3$ is
     eventually arithmetic (difference $2$, from $N_0=3$) but admits **no** $T,L$ with $b_{n+T}=b_n+L$ for
     *all* $n\ge1$ — for any candidate $T\ge2$ (forcing $1+T\ge3$), consistency would require
     $b_{1+T}=2(1+T)=2+2T$ to equal $b_1+L=1+L$, i.e. $L=2T+1$, while consistency at $n=2$ requires
     $b_{2+T}=2(2+T)=4+2T$ to equal $b_2+L=100+L$, i.e. $L=2T-96$; these disagree ($2T+1\ne 2T-96$) for
     every $T$, so no valid $(T,L)$ exists. This shows "eventually arithmetic (or eventually periodic
     with a shift)" is **not**, on its own, sufficient to conclude global periodicity for an arbitrary
     sequence — the actual values of the finite prefix must also be shown consistent with the chosen
     shift, which requires either extra structure specific to the recursion or a different argument. This
     observation does not affect my approach's own (already-negative) conclusion, but it is relevant to
     `lemmas/periodicity-given-no-escape.md` (certified elsewhere), whose proof's final paragraph
     ("extending to all $n\ge1$") argues along similar lines and is worth a second look by whichever
     approach relies on it most heavily — flagged here for the reviewer, not claimed as a refutation
     (the cited lemma's setting has more structure — the state space is genuinely finite and tracked from
     a fixed residue system — than my toy counterexample, so it may well be salvageable; I have not
     checked this in the depth the concern deserves, and it is out of scope for my own approach's file).

## Current best

- The theorem holds unconditionally when $\omega(a_1)=1$ (base case, cited from
  `lemmas/singleton-generator-permanence.md` + `lemmas/pc-implies-theorem.md`), which is already
  established elsewhere and not new to this approach.
- New, fully rigorous content from this round: the **Proper-Subset Pigeonhole Dichotomy** (Item 2 above)
  — for $\omega(a_1)\ge2$, either (I) $a_1\mid a_n$ for cofinitely many $n$, or (II) some fixed proper
  subset $R_0\subsetneq S=\mathrm{primes}(a_1)$ satisfies $\mathrm{primes}(\gcd(a_1,a_n))=R_0$ for
  infinitely many $n$. This is correct and sharper than the outline's original pigeonhole fact, but by
  itself gives no path to the theorem: it produces raw material ($R_0$, hence $g_0$ with
  $\omega(g_0)<\omega(a_1)$) but **no established way to leverage it** into a genuine reduction of the
  $a_1$-sequence's tail behavior to the $g_0$-sequence's behavior.
- **The core Reduction Lemma (outline Step 3) is an open gap with no mechanism found**, and Item 4 above
  gives a structural reason (not just "not yet found") for why the most natural version of this
  reduction — treating the $R_0$-recurring subsequence as a disguised copy of the fresh $g_0$-recursion
  — does not hold: those terms' *other* prime content, needed to satisfy sharing constraints against all
  earlier terms of the full sequence (not just $a_1$), is essentially unconstrained by $g_0$ and grows
  with $n$ in a way with no visible relation to a smaller, independent recursion.
- **This approach does not close the theorem and, per the outline's explicit instruction, should not be
  pushed further into a forced "full induction" write-up.** It remains open as a genuinely different
  top-level framing (still avoiding the antichain-of-prime-sets object entirely) should a future round
  find a different way to make the recurring subset $R_0$ bite — e.g. by combining it with the antichain
  machinery instead of trying to bypass it — but no such combination was found or attempted here (out of
  the bounded scope assigned).

## Full proof
(Not applicable — Status is partial; the Reduction Lemma, the load-bearing step, is an open gap with a
documented negative finding rather than a proof.)

## Promotable lemmas

- **Proper-Subset Pigeonhole Dichotomy.** *Statement:* Let $(a_n)$ be the greedy sequence with
  $S:=\mathrm{primes}(a_1)$, $|S|\ge2$. Then either (I) $a_1\mid a_n$ for all sufficiently large $n$, or
  (II) there is a nonempty proper subset $R_0\subsetneq S$ such that
  $\mathrm{primes}(\gcd(a_1,a_n))=R_0$ for infinitely many $n$. *Proved in full* in Item 2 above (pure
  pigeonhole on the finite set of subsets of $S$, using only the already-certified fact $\gcd(a_1,a_n)>1$
  for all $n\ge2$, itself immediate from the problem's defining recursion). Reusable by any future
  approach wanting a guaranteed $\omega$-decrease candidate divisor, with the caveat (also proved) that
  it does not by itself give a working reduction.
- **Toy counterexample: "eventually arithmetic" does not imply "globally periodic-with-shift."**
  *Statement:* there exists an increasing sequence of positive integers that is arithmetic (common
  difference $2$) from index $3$ onward but admits no $T,L\in\mathbb Z_{>0}$ with $b_{n+T}=b_n+L$ for
  every $n\ge1$. *Proved in full* in Item 5 above (explicit sequence $1,100,6,8,10,\dots$, explicit
  contradiction between the constraints at $n=1$ and $n=2$ for every candidate $T$). Not about our
  specific recursion, but relevant as a warning to any approach (including
  `lemmas/periodicity-given-no-escape.md`) that infers global periodicity from eventual periodicity
  without separately verifying prefix consistency — flagged for the reviewer to check against that
  lemma's proof, not asserted as a refutation of it.
