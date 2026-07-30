## imo-2026-06

### Scope note
The even-$a_1$ case is fully solved (`absorption-recurrence-even-case.md`, certified
`lemmas/even-persistence.md`). The **entire** remaining open content is odd $a_1$, currently
reduced (two independent, reviewer-verified routes) to one static combinatorial target —
"Antichain Stabilization" / equivalently "P-Confinement (PC)": the antichain $\mathcal A_n$ of
inclusion-minimal prime-sets $D_i=\mathrm{primes}(a_i)$ eventually stabilizes / has every generator
prime $\le L_0=\mathrm{rad}(a_1)$. Four rounds (six built approaches on this wall, one honest
per-prime negative result this round) have not proved this. My mandate: find an opening that does
**not** route through the antichain-of-minimal-prime-sets object. Honest verdict up front: I could
not find a framing that is *fully* orthogonal to PC — every genuinely different top-level target I
tried reduces, on inspection, to a restatement of PC or something at least as hard. But I found three
distinct **new tool-families** (not variants of charging/Dilworth/vanishing-identity, all already
dead per current.md) that attack PC itself from angles nobody in the population has used, plus one
useful negative computational finding. I report these honestly, flagging which are genuinely new vs.
which just reformulate the known wall.

### Distinct openings

**1. Covering-system / fixed-modulus congruence reformation (via the already-certified LCR lemma).**
`lemmas/local-congruence-reduction.md` (round 4, certified) shows: *if* PC holds up to index $i-1$,
then $a_i$ is exactly the smallest integer $>a_{i-1}$ lying in a fixed union of residue classes mod
$L_P=\prod_{p\le L_0}p$ — i.e. a purely arithmetic "smallest integer in a union of congruence classes"
process on a *fixed* finite modulus, no antichain bookkeeping needed once PC is assumed at that step.
This suggests attacking PC by strong induction on the generator index using classical covering-system
/ Beatty-sequence machinery (Erdős-style covering systems, density of arithmetic progressions,
inclusion–exclusion on residues mod $L_P$) rather than prime-set bookkeeping. **Honest assessment:**
this is a genuine reformulation that changes the toolbox (sieve/covering-system theory instead of
antichain combinatorics), but it does not escape PC itself — proving the induction step still needs
"the minimal congruence solution is always $L_0$-smooth," which is PC in disguise for the *next* step.
Promise: medium — worth trying because it opens sieve-theoretic tools (Buchstab-type smooth number
density, inclusion-exclusion residue counting) that the antichain framing has not used at all, but it
is not a bypass of the wall.

**2. Growth-rate / smooth-number contradiction framing (proof by contradiction on non-stabilization,
not induction building the antichain up).** All built approaches attack PC/Antichain Stabilization
*positively* (try to construct/derive that it holds). An unexplored architecture: assume for
contradiction that $\mathcal A_n$ never stabilizes (infinitely many genuinely new generators are
recruited forever), and derive a contradiction against the **already-proved, certified linear growth
bound** $a_n\le a_1+(n-1)L_0$ (`lemmas/gap-bound.md`) using a counting/density argument in the style
of `aimo-0009`'s crux move (bound a monotone sequence by double-counting a nested-value constraint) or
the smooth-number-counting technique already proved from scratch this round-cycle (round 4's
`self-closing-pair-density-odd-case.md` "infinitude of $\Pi$" argument — the $O_M((\log x)^{\pi(M)})$
vs. $\Theta(x)$ mismatch). Concretely: each new generator recruitment event requires a *specific* term
$a_j=O(j)$ whose factorization is incomparable to all existing generators; if recruitment happened
infinitely often with growing minimal generator size, one might be able to show the "smoothness debt"
required of infinitely many $a_j=O(j)$ grows faster than the smooth-number density permits — a genuine
counting contradiction, structurally different from the refuted "per-step $O(\log a_n)$ charging"
mechanism (that failed because the *budget* was $n$-dependent; this framing instead bounds a *global*
density of smooth vs. non-smooth integers in the range $[1,a_1+NL_0]$, not a per-step local budget).
**Honest assessment:** I did not carry this further (outside explorer scope) and it is speculative —
I do not have a candidate inequality that actually closes it — but it is a genuinely different proof
*architecture* (contradiction + global density, not induction + local structure) built from two tools
already independently certified/proved in this project (gap-bound, smooth-number counting), so it is
cheap to attempt. Promise: medium-low, but architecturally novel and reuses proven lemmas.

**3. Sperner/LYM-type weighted-sum monovariant on the (automatically pairwise-intersecting) antichain.**
Note (verified, not previously stated as such in the population): since the problem's own hypothesis
gives $\gcd(a_j,a_i)>1$ for **every** $i<j$, we have $D_i\cap D_j\neq\emptyset$ for every $i<j$
automatically — so $\{D_1,\dots,D_n\}$, and hence $\mathcal A_n$, is always a genuinely **pairwise-
intersecting family**, not merely an antichain. (This is a trivial restatement of the hypothesis, not
a new discovery, but it has not been exploited as a *quantitative* tool.) Classical extremal set
theory has sharp bounds for intersecting antichains via the LYM/Bollobás set-pair inequality:
$\sum_{F\in\mathcal A_n}\binom{m}{|F|}^{-1}\le1$ for an antichain on a ground set of size $m$ (LYM), and
intersecting antichains satisfy stronger Hilton–Milner/EKR-type bounds. **Unexplored candidate
monovariant**: $\Phi_n:=\sum_{F\in\mathcal A_n}L_0^{-|F|}$ (or $\binom{L_0}{|F|}^{-1}$-weighted), tried
against the empirical observation below (finding 4) that the "risk ratio" (max generator prime /
$L_0$) can climb close to 1 before a rescuing Absorption event — a weighted-sum monovariant might
capture exactly this "the antichain is allowed to sprawl, but a self-closing/absorption event must
occur before some LYM-type budget is exhausted" mechanism, which no per-prime or per-step candidate
tried so far (Round 4's $\sigma_p$/$\tau_p$, refuted) captures, since $\Phi_n$ is inherently a
*joint*, not per-prime, statistic (directly addressing the Round-4 Diagnosis that joint co-occurrence,
not per-prime history, drives antichain evolution). **Honest assessment:** genuinely new tool, not
tried by any approach in the population; I have not verified $\Phi_n$ is monotone or bounded — this is
a candidate to hand to the outliner/builder to test computationally before building on it. Promise:
medium (novel, targets the joint-co-occurrence structure correctly per Round 4's own diagnosis, but
unverified).

**4. (Explicitly reject, already tried) The `aimo-0030` "Ana & Banana" game transplant.** Memory rules
(round 5, rules 12–14) already record this was tried and its literal Claim-1/2/3 construction was
found NOT to transplant (threshold double-duty mismatch; boring-multiple-is-smooth claim falsified by
explicit counterexample $a_1=15$, $M=255=3\cdot5\cdot17$). I re-read the crux record directly: `aimo-
0030` is a *different* combinatorial object (a two-player decreasing coprime-move game, "good"/"bad"
positions), not the same recursion as our problem — its relevance is thematic (pairwise-non-coprime
structure among extremal positions) not structural identity. Do not re-attempt a literal transplant of
its Claims; if revisited, only the qualitative idea "characterize a set via closure under multiples/
prime-multiplication rules" (Claims 1–3 there) might inspire a genuinely reworked argument, but this
is speculative and not a new opening per se.

### Candidate technique(s)
- Covering-system / sieve theory (density of unions of residue classes mod a fixed modulus, once PC
  is locally assumed) — opening 1.
- Global smooth-number density / counting contradiction (reusing the certified $M$-smooth counting
  bound and gap-bound.md) — opening 2.
- LYM / Bollobás set-pair inequality for intersecting antichains, as a joint (not per-prime) weighted
  monovariant candidate — opening 3.

### Cheap-kill candidates
None found that bypass PC outright. One useful negative/diagnostic computation (below) shows PC is
empirically "tight" for some $a_1$ (ratio climbs toward but not past 1 before a rescuing Absorption
event) — this is evidence PC is a real theorem needing a real argument, not a triviality, and also
evidence against hoping for an easy uniform bound like "generator primes $\le 2\cdot\text{(smallest
prime of }a_1)$" or similar naive closed forms.

### Knowledge-base entries to use
- Number Theory: Modular arithmetic/CRT (for opening 1's induction step), Dirichlet's theorem (primes
  in AP — possibly relevant if a construction/counterexample-search direction is later needed),
  Bertrand's postulate (possible source of an explicit smooth/non-smooth threshold).
- Combinatorics: none of the existing named entries (Pigeonhole, Hall, Dilworth via "Monotone
  Subsequences" section) are new here — Dilworth was already tried (`dilworth-antichain-bound.md`).
  The LYM/Sperner idea (opening 3) is **not** explicitly named in `knowledge_base.md` as an entry;
  flagging it as a technique to add if it proves useful (currently absent from the KB).

### Analogous past problems (cruxes)
- `aimo-0648` (`sequences-and-recurrences`): "Show an order statistic (max/min) of the terms is
  preserved by the recurrence to confine the sequence to a bounded interval, forcing eventual
  periodicity of an integer sequence" — a floor-average recurrence over a bounded window of
  predecessors is eventually constant because the *state* (window of predecessor values) is literally
  finite. Structurally close in spirit (finite-state $\Rightarrow$ eventual periodicity) but the
  disanalogy is exactly our obstruction: our recursion's dependence on ALL prior terms (not a bounded
  window) is why the antichain compression is needed and why it's hard — this crux confirms the
  *shape* of argument we want but doesn't supply the missing compression step.
- `aimo-0009` (`sequences-and-recurrences`/`telescoping-and-summation`, ISL-style): "bound a sum of
  monotone terms by double-counting, pairing each below-threshold index against a nested-value
  nested-value constraint" — cited as the template for opening 2's proof-by-contradiction/counting
  architecture, not a direct transplant.
- `aimo-0678` (`divisibility-and-gcd`): already on record (round 1) as the closest transplantable
  analog for the overall eventual-periodicity target; its "isolate a regime where the recurrence
  simplifies so a sum invariant is exactly conserved" move is a reusable template if a genuinely new
  regime-decomposition is found for our sequence (not attempted this round).
- `aimo-0030` (`games-and-strategy`): thematically adjacent (pairwise-non-coprimality forced among
  extremal objects) but a **different problem** (a game, not our greedy sequence); literal transplant
  already refuted per memory rules 12–14 — do not re-attempt as stated.

### Prior progress
Best available (imported, unchanged this round): two equivalent-strength reductions, both fully
rigorous down to the single open target (Antichain Stabilization / PC):
1. `antichain-signature-closure.md`: gap-bound $\to$ Constraint Domination $\to$ (if Antichain
   Stabilization holds) theorem, plus the unconditional sufficient special case Absorption
   (`lemmas/absorption-lemma.md`).
2. `dilworth-antichain-bound.md` + `lemmas/local-congruence-reduction.md` (round 4): gap-bound $\to$
   signature-stabilization/CRT $\to$ (if P-Confinement holds) theorem with zero secondary gap; LCR
   gives the clean per-step congruence reformulation used in opening 1 above.
`self-closing-pair-density-odd-case.md` (round 4) additionally certifies the trivial-but-clean
Validity Monotonicity fact ($V_{n+1}\subseteq V_n$) and a fully proved negative result (the total prime
pool $\Pi$ is provably infinite under eventual periodicity, via smooth-number counting) — this exact
smooth-number-counting technique is the one I'm proposing to redeploy, in the opposite direction, for
opening 2.

### Dead ends (do not retry)
- Per-step $O(\log a_n)$ "witness-debt" charging (budget is $n$-dependent, proven not to sum finite) —
  refuted 3 times (rounds 2 and 4).
- Literal `aimo-0680` bounded-difference-quotient transplant (`dense-signature-vanishing`) — refuted
  computationally (1510/1770 violating pairs, $a_1=15$).
- Per-prime candidates $\sigma_p(n)$, $\tau_p(n)$, and the `aimo-0477` $v_p$-monotonicity transplant —
  all refuted this round (`per-prime-divisor-chain-decomposition.md`), with the useful diagnosis that
  per-prime history discards the joint co-occurrence information that actually drives antichain
  evolution (motivating opening 3's joint/weighted-sum candidate instead of a per-prime one).
- "Prove the total prime pool $\Pi$ finite, then finite-Boolean-lattice pigeonhole" — refuted with a
  full elementary proof that $\Pi$ is infinite under eventual periodicity (round 4).
- Literal `aimo-0030` Claim-1/2/3 construction transplant — refuted (threshold double-duty mismatch;
  "boring multiple is $L_0$-smooth" falsified by explicit counterexample).

### Small-case / intuition notes (this round's computation)
All labeled conjecture/empirical, not proof.
- **PC holds in every case tested** (9 odd $a_1$ values, up to 4–5 prime factors, up to 2500 terms):
  the max prime appearing in any live antichain generator never exceeded $L_0=\mathrm{rad}(a_1)$.
- **New finding: the "risk ratio" (max generator prime)/$L_0$ can climb close to 1 before a rescuing
  Absorption event, then crash to near 0.** For $a_1=3003=3\cdot7\cdot11\cdot13$: ratio grew
  monotonically from $0.37$ (at $n=100$) to $0.70$ (at $n=1100$), antichain size growing from 39 to
  247 generators over that window, then at $n\approx1150$ an Absorption event (a term became $3^k$)
  collapsed the antichain instantly to $\{\{3\}\}$ (ratio $\approx0.001$), which then persisted through
  $n=1400$. This is the sharpest empirical evidence yet that PC is a genuine, non-trivial theorem (not
  a loose inequality with huge slack) — the process appears to "just barely" stay under the $L_0$
  ceiling, rescued by Absorption before it could fail, in at least one example, over the observed
  range. This motivates opening 3 (a weighted budget that must be exhausted before a rescue is forced)
  over openings that assume large uniform slack.
- For $a_1\in\{7429,\,2431,\,4199,\,715,\,17017\}$ (products of larger primes, chosen to plausibly
  delay Absorption) the ratio stayed small (max observed $\approx0.02$) over 2000 terms — no
  counterexample to PC found, but also no case pushed the ratio as high as $a_1=3003$ did; a systematic
  search for a case where the ratio might reach/exceed 1 before any Absorption event would be a
  valuable next computational step (I did not have budget to do a wide randomized search this round).
