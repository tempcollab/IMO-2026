## Status
solved

**Round 6 (this round): SOLVED.** `approaches/global-signature-purification.md` gives a complete,
independent proof of the whole theorem, for every $a_1\ge2$ (both parities, in particular the odd
case that was the entire remaining open content through round 5). The proof-reviewer independently
re-derived every step from scratch and ran extensive computational corroboration (see "Full proof"
below and the reviewer's round-6 report); no gap was found. The proof does **not** depend on the
antichain/PC/Step-6 machinery at all — it is a self-contained "good-number" purification argument
(structurally related to, but not citing, crux `aimo-0030`). Certified as
`lemmas/global-signature-purification.md`. All other approaches in the population (antichain
family, gcd-pigeonhole family) remain historically valuable partial-progress records but are
superseded; the theorem is proved.

**Round 4 major update:** the theorem is now **fully proved and reviewer-verified for every even
$a_1$** (`approaches/absorption-recurrence-even-case.md`, certified `lemmas/even-persistence.md`):
if $2\mid a_1$ then $a_n=a_1+2(n-1)$ for all $n$, an elementary two-lemma induction with no
dependence on the antichain machinery. The **entire remaining content of the theorem is now the
case $a_1$ odd**, for which Antichain Stabilization / P-Confinement (equivalent-strength open
targets, PC $\Rightarrow$ Antichain Stabilization $\Rightarrow$ theorem) remain open. Status stays
`partial` overall only because of the odd case.

**Round 5 update (reviewed round 6, after an interrupted round 5 session):** three approaches built
this round, all independently reviewed and verified correct as far as they go; none closes the odd
case. Net effect: (1) the round-2-flagged citation-hygiene gap in `antichain-signature-closure.md`
is now **fully and correctly closed**, independently, by **two different repair routes**
(`antichain-signature-closure`'s own direct re-verification, and `global-smooth-density-contradiction`'s
cleaner "$P'$-enlargement Master Lemma," now certified as
`lemmas/antichain-stabilization-implies-theorem.md` — this shows **Antichain Stabilization alone**,
with no reference to the fixed truncation $P=\{p\le L_0\}$, already suffices for the full theorem,
strictly subsuming `lemmas/pc-implies-theorem.md`'s PC hypothesis); (2) `leftover-witness-confinement`
narrows PC to a single, precisely-stated residual combinatorial question (its "Step 6": no
hitting-but-not-containing witness set exists for realized, pairwise-intersecting antichains with no
singleton block), proving away every other case (singleton-block case fully closed two independent
ways, now certified as `lemmas/singleton-generator-permanence.md` and the Leftover-Witness Dichotomy,
`lemmas/leftover-witness.md`); (3) `global-smooth-density-contradiction` independently derives an
equivalent restatement ("only finitely many Type B growth events," `lemmas/growth-event-decomposition.md`)
via a genuinely different, global counting architecture, and **rigorously refutes** the specific
global smooth-number-density mechanism it was dispatched to try (Type-B-eligible integers have
density $\to1$, not $\to0$ — the wrong shape for a scarcity argument). **All three approaches'
residual open targets are now cross-checked and shown equivalent** by three independent constructions
— strong evidence the field has correctly identified the problem's true remaining content, not an
artifact of any one framing. **One error found and flagged** (not load-bearing, does not affect the
overall gap): `leftover-witness-confinement.md`'s Step 6 discussion, point 3, claims the
"complete-graph antichain" special case closes "for any $k\ge2$" — this is **false at $k=2$**
(verified by brute force: a single 2-element block $\{p_1,p_2\}$ admits the valid witness
$H=\{p_1\}$, hitting without containing); the claim is correct for $k\ge3$ only. Status remains
`partial`; the odd case remains open, now reduced (via three independently-verified equivalent
routes) to one precise combinatorial claim.

## Approaches tried
- `growth-bound-density` (round 1): Proved the unconditional gap bound $a_{n+1}-a_n\le L_0:=
  \mathrm{rad}(a_1)$ and a Constraint Domination lemma. Remaining gap: whether the inclusion-minimal
  antichain of signatures stabilizes finitely. **Verdict: CHANGES REQUESTED (partial).**
- `core-signature-pigeonhole` (round 1): Repaired the S-too-coarse bug using $P=\{\text{primes}\le
  L_0\}$. Built the CRT machine (signature stabilization $\to$ sufficient residue set $G$ $\to$
  one-directional $a_{n+1}\le y_{n+1}$), isolating the single remaining gap as "No-Escape."
  **Verdict: CHANGES REQUESTED (partial).**
- `monovariant-telescoping` (round 1): $Q$-cover/density lemmas proved, but the headline target
  $|Q|<\infty$ is **false** (proved false by the reviewer: once the theorem's conclusion holds, $Q$
  is cofinite). **Verdict: RETHINK (dead-end for the $|Q|<\infty$ target); lemmas kept as background
  facts.**
- `antichain-signature-closure` (round 2, revise of `core-signature-pigeonhole`): Re-targeted the
  closing mechanism to use the exact, untruncated antichain of live minimal prime-sets, collapsing
  the old two-part sufficiency/No-Escape gap into one target, **Antichain Stabilization**. Proved two
  new, fully rigorous lemmas — **Absorption** (a prime-power term forces permanent antichain collapse
  to a singleton; certified as `lemmas/absorption-lemma.md`) and **self-closing sufficiency** (a
  self-closing antichain configuration, once reached, persists forever; certified as
  `lemmas/self-closing-antichain-sufficiency.md`) — plus a precise negative diagnosis of the
  outline's "witness-debt charging" argument (the per-step budget $O(\log a_n)$ is not fixed, grows
  with $n$, so cannot give a finite total bound; confirmed by the reviewer's own re-derivation, not
  just asserted). All numerical claims (antichain size 268 at $n=893$ for $a_1=2310$, collapse to size
  1 at $n=894$ with $a_{894}=2^{12}$, 353 growth events in the first 893 terms, all-even prefix)
  independently reproduced by the reviewer from scratch and matched exactly. **One rigor gap found by
  the reviewer, not previously flagged**: Lemma 3 (periodicity via `lemmas/periodicity-given-no-escape.md`)
  is invoked with $P^*$ built from the *eventual* generator set, but that lemma's literal hypothesis
  is $\mathrm{primes}(a_1)\subseteq P$, and $P^*\supseteq\mathrm{primes}(a_1)$ is **not** guaranteed
  (if $\mathrm{primes}(a_1)$ itself gets dominated by a strictly smaller later generator, $P^*$ can
  fail to contain some prime of $a_1$). The cited lemma's proof does not actually use this hypothesis
  anywhere in its body, so the result likely still holds, but as written the citation is not literally
  valid and needs either (a) a direct check that $P^*\supseteq\mathrm{primes}(a_1)$ always holds, or
  (b) a re-proof of the periodicity step generic in $P$ (dropping the unused hypothesis explicitly).
  This does not affect the paper's true open gap (Antichain Stabilization itself), but the "zero
  residual gap in steps 4–6" claim is not fully established as stated. **Verdict: CHANGES REQUESTED
  (partial)** — real progress (two new certified lemmas, a checked negative diagnosis, a cleaner
  target restated as "self-closing reachability"), but Antichain Stabilization / self-closing
  reachability remains open for general $a_1$, plus the citation gap above should be patched.
- `dense-signature-vanishing` (round 2, new): Attempted to transplant crux `aimo-0680`'s
  bounded-difference-quotient pigeonhole + growing-divisor-vanishing mechanism. Proved two cheap
  pigeonhole facts (Propositions 1–2, trivial corollaries of already-certified lemmas). **Refuted the
  literal transplant by explicit, reviewer-reproduced counterexample**: for $a_1=15$, of the 1770
  pairs $(i,j)$ among the first 60 terms, 1510 violate $(j-i)\mid a_j-a_i$ (reviewer independently
  recomputed this exact count and confirms it). Argued (Proposition 4, a reasoned but not fully
  formalized diagnostic, honestly hedged as such) that any repaired/localized version of the identity
  would already be at least as strong as the No-Escape/Antichain-Stabilization property the rest of
  the population is attacking directly, so this specific mechanism cannot bypass the shared wall.
  **True Status: unsolved** (no positive lemma or reduction toward the theorem was produced; the
  file's self-reported "partial" overclaims — Propositions 1–2 carry no independent content beyond
  already-certified facts, and Propositions 3–4 are negative/diagnostic only). **Verdict: RETHINK**
  (the literal-transplant approach cannot itself become a proof; recorded as a documented dead end
  per CLAUDE.md's "record everything" rule, exactly parallel to round 1's `monovariant-telescoping`
  call). No lemmas promoted from this file (correctly, the builder itself did not propose any).
- `dilworth-antichain-bound` (round 2, revise of `covering-construction-induction`): The originally
  assigned Dilworth/chain-covering-by-window-size mechanism was found (correctly) not to close, for
  the same reason the "witness-debt charging" argument fails elsewhere (the per-window prime budget
  $O(\log a_n)$ is not $n$-independent) — a real, reported negative finding for that specific
  technique. Recovered with a **new, fully rigorous reduction**: **P-Confinement (PC)** $\Rightarrow$
  full theorem, with **zero secondary gap** (Steps A–D, reviewed and re-derived step by step by the
  reviewer with no gap found; unlike `antichain-signature-closure`, this uses the fixed
  $P=\{\text{primes}\le L_0\}\supseteq\mathrm{primes}(a_1)$ throughout, so the citation of
  `periodicity-given-no-escape.md` is fully valid with no hypothesis mismatch). PC verified
  computationally (zero violations across 5 values of $a_1$, reviewer-reproduced up to 400 terms
  each) but not proved for general $a_1$; the builder honestly assesses it as likely comparable in
  difficulty to Antichain Stabilization (and shows PC $\Rightarrow$ Antichain Stabilization, so PC is
  the stronger, not easier, claim), not a shortcut around the shared wall. **Verdict: CHANGES
  REQUESTED (partial)** — genuinely new, certified reduction (`lemmas/pc-implies-theorem.md`); PC
  itself remains the open gap, essentially the same wall in a cleaner, single-hypothesis form.
- `leftover-witness-confinement` (round 5, revise of `dilworth-antichain-bound`, reviewed round 6):
  Built the round-5 explorer's Leftover-Witness Lemma into two certified lemmas
  (`lemmas/leftover-witness.md`, `lemmas/singleton-generator-permanence.md`), fully closing every
  case of PC's minimal-counterexample descent except one: "Step 6," a single precise combinatorial
  question (no hitting-but-not-containing witness set for a realized, pairwise-intersecting
  antichain with no singleton block). Reviewer independently re-derived Steps 1–5 line by line; no
  gap found there. **One error found in Step 6's discussion** (non-load-bearing): the claim that the
  "complete-graph antichain" special case closes "for any $k\ge2$" is **false at $k=2$** (brute-force
  counterexample: $H=\{p_1\}$ hits the single block $\{p_1,p_2\}$ without containing it); true only
  for $k\ge3$. Does not affect the file's honest admission that Step 6 remains open. **Verdict:
  CHANGES REQUESTED (partial)** — the strongest narrowing of PC in the population; fix the $k\ge2$
  vs. $k\ge3$ error before further reliance on that sub-claim.
- `antichain-signature-closure` (round 5, advance, reviewed round 6): Closed the round-2-flagged
  citation-hygiene gap (Lemma 3's use of `lemmas/periodicity-given-no-escape.md` with $P^*$ built
  from the eventual generator set) by re-reading the cited lemma's proof body and confirming
  $\mathrm{primes}(a_1)\subseteq P$ is never used. **Independently verified correct** by the reviewer
  (re-read the cited proof body directly). Cross-checked scope with `leftover-witness-confinement`'s
  Step 6 — both converge on the same residual "no singleton block" case. **Verdict: CHANGES REQUESTED
  (partial)** — real, correct hygiene fix; core target (Antichain Stabilization / self-closing
  reachability) still open.
- `global-smooth-density-contradiction` (round 5, new, reviewed round 6): The round's required
  diversity opening — global counting/contradiction architecture, not local minimal-counterexample
  induction. Proved, unconditionally and reviewer-verified: (1) the Growth-Event Update Lemma +
  Corollary (Antichain Stabilization $\Leftrightarrow$ finitely many growth events) and a Type A
  (unconditionally finite, $\le2^{|P|}-2$) / Type B (open, PC-violating) decomposition of growth
  events, certified as `lemmas/growth-event-decomposition.md`; (2) a "$P'$-enlargement Master Lemma"
  showing Antichain Stabilization *alone* (not P-Confinement) already implies the full theorem, with
  a cleaner, independently-verified fix for the same citation-hygiene issue flagged in
  `antichain-signature-closure`, certified as `lemmas/antichain-stabilization-implies-theorem.md`;
  (3) a rigorous negative result refuting the specific dispatched mechanism (global smooth-number
  density): the property "has a prime factor $>L_0$" has density $\to1$, not $\to0$, among integers,
  so no scarcity-based counting contradiction of this shape can bound Type B events — reviewer
  re-derived the smooth-number counting bound from scratch and confirmed it. Honestly documents that
  its residual target (Type B finiteness) is equivalent to `leftover-witness-confinement`'s Step 6 and
  `antichain-signature-closure`'s self-closing reachability. **Verdict: CHANGES REQUESTED (partial)**
  — genuine new architecture and two new certified lemmas; the specific tool dispatched (smooth
  density) is now a documented, checked dead end for this target, and the core gap remains open.

## Cross-cutting diagnosis (updated round 2)
Two of round 2's three built approaches (`antichain-signature-closure`, `dilworth-antichain-bound`)
both reduce the entire theorem to a single, checkable, static combinatorial hypothesis about the
prime sets used by antichain generators — "Antichain Stabilization" / its equivalent "self-closing
reachability," and "P-Confinement" respectively — with **PC $\Rightarrow$ Antichain Stabilization**
proved (so PC is the stronger of the two, not an easier alternate route). This is still the *same*
underlying obstruction identified in round 1 (does a fixed finite covering pattern eventually
suffice), now stated in its cleanest forms yet, with two independently reviewer-verified certified
lemmas (`absorption-lemma.md`, `self-closing-antichain-sufficiency.md`) showing exactly how
stabilization occurs in the two known example families (prime-power absorption for $a_1=2310$;
non-absorption self-closing triple for $a_1=15$). The `dense-signature-vanishing` attempt to find a
genuinely independent route (transplanting `aimo-0680`) is now a reviewer-confirmed dead end, and its
own diagnosis (Proposition 4) argues, plausibly but only semi-formally, that identity-based
approaches of this shape cannot bypass the wall either. **No approach has yet proved that Antichain
Stabilization / self-closing reachability / PC actually holds for every $a_1$.** Per the orchestrator
rule on breaking shared-gap plateaus: this is round 2 of the antichain-family wall (round 1 called it
"No-Escape"/growth-bound gap, essentially the same claim); next round should prioritize either (a) a
genuinely new proof technique for self-closing reachability specifically (e.g. a direct argument
about which pairs of primes must eventually co-occur in a generator, using density/pigeonhole on
*pairs* rather than on individual growth events — the per-event charging approach is now
reviewer-confirmed dead twice, in two different technique dressings), or (b) a wholly different
top-level framing not going through antichains/signatures at all, since `dense-signature-vanishing`'s
attempt at (b) this round also failed and its own diagnosis suggests any successor needs a genuinely
new source for a growing-divisor-type identity, not a variant of the greedy recursion's own
step-by-step definition.

## Current best
Best available rigorous chain (either of two equally strong, reviewer-verified reductions):

**Route 1 (`antichain-signature-closure`):**
1. Gap bound: $a_{n+1}-a_n\le L_0=\mathrm{rad}(a_1)$ (`lemmas/gap-bound.md`).
2. Constraint Domination (`lemmas/constraint-domination.md`).
3. If the untruncated antichain $\mathcal A_n$ of inclusion-minimal prime-sets stabilizes (Antichain
   Stabilization) — equivalently, if some $\mathcal A_N$ is *self-closing*
   (`lemmas/self-closing-antichain-sufficiency.md`) — the theorem follows with no further gap (the
   file's Lemma 2/Corollary/Lemma 3, modulo the citation-hygiene point noted above under "Approaches
   tried," which is very likely a one-line fix).
4. **Sufficient special case, fully proved unconditionally**: if any term of the sequence is ever a
   prime power, Antichain Stabilization holds automatically (`lemmas/absorption-lemma.md`).

**Route 2 (`dilworth-antichain-bound`):**
1–2. Same as above, plus signature-stabilization/CRT-sufficiency machinery for the fixed
   $P=\{\text{primes}\le L_0\}$ (`lemmas/signature-stabilization-and-crt-sufficiency.md`).
3. If **P-Confinement** holds (every antichain generator's untruncated prime set stays within $P$),
   the theorem follows with zero secondary gap, fully and rigorously proved with no hypothesis
   mismatch (`lemmas/pc-implies-theorem.md`).

Nothing in the population yet proves Antichain Stabilization / self-closing reachability / PC for
general $a_1$. Status remains `partial`.

## Full proof

(From `approaches/global-signature-purification.md`, verified line-by-line and computationally
corroborated by the round-6 proof-reviewer; certified as `lemmas/global-signature-purification.md`.)

Fix $a_1=:k\ge2$. Write $(a_n)_{n\ge1}$ for the sequence: $a_1=k$, and for $n\ge1$, $a_{n+1}$ is the
smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for all $i\le n$ (given by the problem to be a
well-defined, strictly increasing, unbounded infinite sequence).

**0. Good integers.** Call a prime $p$ *small* if $p\le k$, *big* if $p>k$. For $x\ge k$, let
$\pi(x):=\{p\text{ prime}\le k: p\mid x\}$; call $x,x'\ge k$ *similar* if $\pi(x)=\pi(x')$. Define
$\mathrm{good}:\{k,k+1,\dots\}\to\{T,F\}$ by well-founded recursion:
$$\mathrm{good}(x):=\big[\text{every }m\text{ with }k\le m<x,\ \gcd(m,x)=1\text{ has }\mathrm{good}(m)=F\big],$$
so $\mathrm{good}(k)=T$ vacuously. $x$ is *bad* iff there is $m\in[k,x)$, $\gcd(m,x)=1$, $m$ good.

**Fact 1.** Distinct good $g,g'\ge k$ have $\gcd(g,g')>1$. (If $\gcd(g,g')=1$ with $g<g'$, then
$m=g$ witnesses $g'$ bad, contradiction.)

**1. Correspondence Lemma.** $\{x\ge k:x\text{ good}\}=\{a_1,a_2,\dots\}$.

*Proof.* By induction on $n$: (i) $a_n$ good; (ii) every $x\in(a_n,a_{n+1})$ bad; (iii)
$\{x\in[k,a_n]:x\text{ good}\}=\{a_1,\dots,a_n\}$. Base $n=1$ immediate. Step: for (a), any
$m\in[k,a_{n+1})$ coprime to $a_{n+1}$ is bad — if $a_n<m<a_{n+1}$ by (ii); if $m\le a_n$, by (iii)
either $m$ is bad or $m=a_i$ ($i\le n$), but the latter forces $\gcd(a_{n+1},a_i)>1$ by
$a_{n+1}$'s defining property, contradicting $\gcd(m,a_{n+1})=1$ — so $a_{n+1}$ is good. (b)/(c)
follow by direct set-bookkeeping and the minimality defining $a_{n+2}$. Taking $n\to\infty$
(sequence unbounded) gives the Corollary. $\square$

**2. Purification Lemma.** If $b\ge k$ has a small prime factor, there is $x$ with $k\le x\le b$,
$\pi(x)=\pi(b)$, $x$ $k$-smooth.

*Proof.* If $b$ is already $k$-smooth take $x=b$. Else fix small $p\mid b$, big $q\mid b$. Let
$a:=\prod\{p'\le k: p'\mid b\}$ (squarefree, $\pi(a)=\pi(b)$, $a\mid b$, $a\ge p$). Let $n\ge0$ be
minimal with $x:=p^na\ge k$. If $n=0$: $x=a$, and since $q\mid b/a$, $b>a=x$. If $n\ge1$: minimality
gives $p^{n-1}a<k$, so $x<pk\le ak<aq$; and $\gcd(a,q)=1$, $a\mid b$, $q\mid b$ give $aq\mid b$, so
$x<aq\le b$. Either way $x\le b$. $\square$

**3. Signature Determinacy Theorem.** Similar $a,b\ge k$ satisfy $\mathrm{good}(a)=\mathrm{good}(b)$.

*Proof.* Suppose not; take a counterexample pair $(a,b)$, $\pi(a)=\pi(b)$, minimizing $\max(a,b)$;
WLOG $a$ bad, $b$ good. Bad $a$ gives $r\in[k,a)$, $\gcd(r,a)=1$, $r$ good. $r$ has a small prime
factor (via $\gcd(r,k)>1$: Fact 1 if $r\ne k$, trivial if $r=k$). Apply Purification to $r$: get
$r'\in[k,r]$, $\pi(r')=\pi(r)$, $r'$ $k$-smooth. If $r'$ were bad, $(r',r)$ would be a smaller
($\max=r<a\le\max(a,b)$) counterexample — impossible by minimality — so $r'$ is good. Then $r',b$
both good give (Fact 1, or trivially if $r'=b$) a common prime $p\mid\gcd(r',b)$, necessarily small
($r'$ $k$-smooth). Small $p\mid r'$, $\pi(r')=\pi(r)$ give $p\mid r$; small $p\mid b$,
$\pi(a)=\pi(b)$ give $p\mid a$. So $p\mid\gcd(a,r)$, contradicting $\gcd(r,a)=1$. $\square$

**4. Periodicity.** Let $L:=\prod_{p\le k\text{ prime}}p\ge2$. For $x,x'\ge k$, $x\equiv x'\pmod L$
$\Rightarrow\pi(x)=\pi(x')$ (each small $p\mid L$). Hence by Theorem A, for $x\ge k$: $x$ good
$\iff$ $x+L$ good. Let $G:=\{x\ge k:x\text{ good}\}=\{a_1,a_2,\dots\}$ (Correspondence Lemma), and
$T:=\#(G\cap[k,k+L))\ge1$ (as $a_1=k\in G\cap[k,k+L)$). The shift $\varphi(x)=x+L$ is an
order-preserving bijection $G\cap[k,\infty)\to G\cap[k+L,\infty)$ (periodicity gives membership
both ways; injectivity is clear). Since $a_1,\dots,a_T$ enumerate $G\cap[k,k+L)$ exactly (the $T$
smallest elements of $G$), $a_{T+1},a_{T+2},\dots$ enumerate $G\cap[k+L,\infty)$ increasingly, so
$\varphi$ carries the $n$-th smallest element of $G\cap[k,\infty)$ (namely $a_n$) to the $n$-th
smallest of $G\cap[k+L,\infty)$ (namely $a_{T+n}$): $a_{n+T}=a_n+L$ for every $n\ge1$. $\blacksquare$

**Conclusion.** With $T,L$ as constructed (positive integers, $T\ge1$, $L\ge2$),
$a_{n+T}=a_n+L$ for every positive integer $n$ — exactly the theorem, for every $a_1\ge2$.

**Verification notes (reviewer, round 6, not part of the proof itself but corroborating it):**
Correspondence Lemma checked by direct DP brute force for $a_1\in\{2,\dots,60\}$ (0 mismatches,
correcting for sequence-length truncation artifacts); Purification Lemma's construction checked
over 16553 random $(k,b)$ pairs (0 failures); Signature Determinacy checked by exhaustive
same-signature-status comparison for $a_1\in\{2,\dots,60\}$ and $a_1\in\{15015,45045\}$ (0
mismatches); the $(T,L)$ pair was directly computed and confirmed against a from-scratch greedy
simulation for $a_1=9$ ($T=70,L=210$, checked for 40+ shifted pairs) and $a_1=15$ ($T=8008,
L=30030$, checked against all available simulated terms). For even $a_1=2$: $L=2$, $T=1$, giving
$a_n=2n$, matching `lemmas/even-persistence.md` (obtained independently, not cited).
