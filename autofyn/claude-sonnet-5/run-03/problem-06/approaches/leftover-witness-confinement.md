## Status
partial

## Approaches tried
- **Round 6 (this round, revise): attempted a "Coincidence Lemma" to close Step 6 directly, found the
  proposed mechanism invalid, searched for a repair, found none, and instead produced a rigorous
  negative result showing that *no* argument of the proposed shape (witness $H$ hits/doesn't-contain
  $\Rightarrow$ $H$ equals an earlier block $D_j$) can work in general.** Details below under "Step 6";
  summary: (a) confirmed the outline's stated justification ("$m<a_1$ means $m$ was tested as a
  recursion candidate") is false, for a *stronger* reason than the outline-reviewer's own flag — $a_1$
  is a free starting parameter of the problem, not itself produced by the recursion, so *no* integer is
  ever "tested as a candidate at step 2" except integers $>a_1$, and moreover Step 2 above **already
  proves** $m$ is never literally equal to any earlier term $a_k$ (Case B is impossible), which is
  exactly the one mechanism that would make $\pi(m)=D_j$ a *forced* coincidence rather than a
  coincidence at all; (b) built an explicit combinatorial counterexample (two blocks $\{2,3\},\{2,5\}$,
  witness $H=\{2\}$) showing that a valid hitting/not-containing witness can have strictly smaller
  cardinality than every block of a no-singleton antichain, hence *cannot* equal any block on
  cardinality grounds alone — so the Coincidence Lemma's conclusion does not follow from the
  hit/not-contain properties by any purely combinatorial argument; a proof, if one exists, would need
  genuinely new information tying $\pi(m)$'s specific value to the recursion's history, which was not
  found this round. **Verdict: this specific mechanism is refuted; Step 6 remains open, no new positive
  progress toward closing it this round** (a negative result, reported honestly per CLAUDE.md). Also
  fixed the file's own previously-flagged cosmetic error ($k\ge2\to k\ge3$ in the complete-graph special
  case).
- **Round 5 (new slug, revise of `dilworth-antichain-bound`):** Built out the round-5
  explorer's Leftover-Witness Lemma into a fully rigorous, certified pair of lemmas
  (`lemmas/leftover-witness.md`: the size-unrestricted LCR corollary, the Leftover-Witness Dichotomy,
  and the Case-B-impossible corollary), improving on the explorer's sketch by closing two soft spots
  the outline-reviewer did not flag but that needed care: (a) a clean, self-contained proof that
  $m\le a_{n-1}$ directly from $a_n$'s own minimality (avoiding an awkward "rule out $k=n$" detour),
  and (b) an explicit non-redundancy convention for "generator index" that makes the Case-B domination
  argument airtight even when $m$ equals an *earlier, possibly non-generator* term exactly. Proved in
  full: Case B is always impossible (immediate domination contradiction); the singleton-block
  sub-case is impossible by **two independent arguments** (a direct one via `lemmas/absorption-lemma.md`
  showing no fresh generator can appear at all once absorption has occurred, and the outline's
  hit/contain argument); reduced the entire remaining gap to the single precisely-stated combinatorial
  question of Step 6 below. **Attempted but did not close** Step 6 (the core open target): found by
  direct combinatorial construction that the naive hope "no antichain of blocks of size $\ge2$ admits
  a hitting-but-not-containing set of bounded size" is **false for arbitrary antichains** (confirming
  the outline's own warning), and — new this round — found that the most natural extra structural
  handle (ruling out "star" antichains, where all live blocks share one common prime, as a route to
  closing Step 6) does **not** obviously work either: analysis of the LCR consequences of a star
  configuration shows a star does not obviously prevent a large-prime intrusion, and a direct
  small-witness construction in the star case does not yield a contradiction. Verified computationally
  (fresh code, this round) that stars with $\ge3$ live blocks essentially never arise in the actual
  recursion's data (0 occurrences among hundreds of snapshots for $a_1\in\{15,105,385\}$, vs. exactly
  1 occurrence per run at the trivial $|\mathcal A|=2$ stage, which is a star automatically). This is
  suggestive but not a proof. **Verdict: genuine further narrowing of the gap (Step 6 is a strictly
  smaller, more specific target than raw PC), but the gap is not closed.**

- (Carried over from `dilworth-antichain-bound`, rounds 2 and 4, summarized — full history there.)
  Round 2: proved PC $\Rightarrow$ theorem with zero secondary gap (`lemmas/pc-implies-theorem.md`).
  Round 4: derived Local Congruence Reduction (`lemmas/local-congruence-reduction.md`), reducing PC's
  inductive step to a single congruence-avoiding-large-primes question; ruled out two odd-case
  simplification candidates by explicit counterexample (absorption-always false; "every new generator
  contains 2" false). PC itself was left fully open there.

## Current best

### Setup (imported, not re-derived)
Fix $a_1$ odd (the only remaining case; the even case is fully closed,
`approaches/absorption-recurrence-even-case.md`). $D_i:=\mathrm{primes}(a_i)$, $S:=D_1$,
$L_0:=\mathrm{rad}(a_1)$, $P:=\{\text{primes}\le L_0\}\supseteq S$, $L_P:=\prod_{p\in P}p$, and for
$x\in\mathbb Z$, $\pi(x):=P\cap\mathrm{primes}(x)$. $\mathcal A_n$ is the antichain of live generator
indices at time $n$ (definitions and Convention below). All of the following are cited, not
re-derived: `lemmas/gap-bound.md`, `lemmas/constraint-domination.md`,
`lemmas/signature-stabilization-and-crt-sufficiency.md`, `lemmas/periodicity-given-no-escape.md`,
`lemmas/pc-implies-theorem.md` (PC $\Rightarrow$ the full theorem, proved with zero secondary gap),
`lemmas/local-congruence-reduction.md` (LCR), `lemmas/absorption-lemma.md`.

**Target.** By `lemmas/pc-implies-theorem.md`, it suffices to prove **P-Confinement (PC)**: every
generator index $i$ has $D_i\subseteq P$.

**Convention (non-redundancy of generator indices).** "Index $i$ is a generator" means $D_i$ is not a
superset of, and not equal to, any $D_j$ for $j<i$ — i.e. $D_i$ is a genuinely new element of the
antichain of distinct minimal prime-sets seen so far. (Stated and justified in
`lemmas/leftover-witness.md`; consistent with, and a harmless refinement of,
`lemmas/constraint-domination.md`'s literal "inclusion-minimal index" phrasing.)

### Step 1 — Minimal-counterexample setup

Suppose PC fails. Let $n$ be **minimal** such that generator index $n$ has $D_n\not\subseteq P$, i.e.
some prime $q\mid a_n$ has $q>L_0$. Since $D_1=S\subseteq P$ trivially, $n\ge2$. By minimality of $n$,
PC holds for every generator index $<n$, so LCR (`lemmas/local-congruence-reduction.md`) applies with
$i=n$: for every $x>a_{n-1}$, $x$ is valid for step $n$ iff $x\bmod L_P\in G_{n-1}$.

Fix $q\mid a_n$ with $q>L_0$, $e:=v_q(a_n)\ge1$, $m:=a_n/q^e$.

### Step 2 — Leftover-Witness Dichotomy and Case B is impossible

By `lemmas/leftover-witness.md` (Leftover-Witness Dichotomy, proved there in full, citing the LCR
Global Validity Corollary — the observation, verified directly from the LCR proof text, that its
($\Leftarrow$) direction never uses $x>a_{i-1}$): exactly one of

- **Case A**: $m<a_1$;
- **Case B**: $m=a_k$ for a unique $k\in\{1,\dots,n-1\}$.

holds. By the Corollary in the same file (Case B is impossible for a genuine new generator): if
$m=a_k$ ($k<n$), then $D_k\subseteq D_n$ (since $a_n=q^e a_k$), contradicting $n$ being a generator
(Convention above: $D_n$ cannot be a superset of, or equal to, any earlier $D_k$). So **Case B is
impossible**, and Case A holds: $m<a_1$, a bound independent of $n$.

### Step 3 — Case A forces a specific forbidden witness $H=\pi(m)$

We show directly (not assuming Case A a priori, so this also re-derives why Case B fails) that
$H:=\pi(m)\subseteq P$ satisfies:

**(i) $H$ hits every block of $\mathcal A_{n-1}$.** For $j\in\mathcal A_{n-1}$: $\gcd(a_n,a_j)>1$
(validity of $a_n$ at its own step) gives a common prime $p\mid a_n,a_j$; by PC for the generator
$j<n$ (induction hypothesis), $D_j\subseteq P$, so $p\in D_j\subseteq P$, i.e. $p\in\pi(a_n)$. Since
$q\notin P$, $\pi(m)=\pi(a_n)$ (removing copies of $q$, a prime outside $P$, changes no $P$-prime
divisibility), so $p\in\pi(m)\cap D_j=H\cap D_j\ne\emptyset$.

**(ii) $H$ contains no block of $\mathcal A_{n-1}$ in full.** Suppose $D_j\subseteq H=\pi(m)\subseteq
\mathrm{primes}(m)$ for some $j\in\mathcal A_{n-1}$ ($j<n$). Then every prime of $D_j$ divides $m$,
hence divides $a_n=q^e m$, so $D_j\subseteq D_n$. Since $j<n$, this contradicts $n$ being a generator
(same Convention as Step 2), regardless of whether the containment is proper.

So, **if PC fails**, Case A holds ($m<a_1$) and $H:=\pi(m)$ is a subset of $P$ with:
$$|H|\le\omega(m)\le\log_2(a_1)\quad\text{(fixed, independent of }n\text{, since }m<a_1\text{ is a
positive integer, a product of }\omega(m)\text{ distinct primes each}\ge2\text{)},$$
which hits every block of $\mathcal A_{n-1}$ but contains no block of $\mathcal A_{n-1}$ in full.

### Step 4 — Singleton-block case is impossible (two independent proofs)

If $\mathcal A_{n-1}$ contains a singleton block $\{p\}$ (i.e. some generator index $j\le n-1$ has
$D_j=\{p\}$, i.e. $a_j$ is a pure $p$-power):

**Proof 1 (direct, via Absorption Lemma — the cleanest route).** By `lemmas/absorption-lemma.md`
part (a), $p\mid a_k$ for **every** $k\ge1$ (not just $k\ge j$), and part (b), $\mathcal
A_k=\{\{p\}\}$ for every $k\ge j$ — in particular $\mathcal A_{n-1}=\{\{p\}\}$ (a single block; recall
$n-1\ge j$ since $j\le n-1$). Now consider $D_n$: since $p\mid a_k$ for every $k$, in particular
$p\mid a_n$, so $\{p\}\subseteq D_n$. If $D_n\ne\{p\}$, then $D_n$ is a proper superset of $\{p\}=D_j$
with $j\le n-1<n$, contradicting $n$ being a generator (Convention). If $D_n=\{p\}$, then $D_n$ equals
the earlier $D_j$, again contradicting the Convention (no generator may equal an earlier $D_j$). Either
way, $n$ cannot be a generator at all — contradicting the very setup of Step 1. So **the
minimal-counterexample scenario cannot occur when $\mathcal A_{n-1}$ has a singleton block**: this
rules out the singleton case *before* even invoking Step 3.

**Proof 2 (via the hit/contain conditions, cross-check).** By Step 3(i), $p\in H$ (since $\{p\}\cap
H\ne\emptyset$ forces $p\in H$). But then $\{p\}\subseteq H$, i.e. $H$ contains the block $\{p\}$ in
full — contradicting Step 3(ii). Same conclusion, independent route.

Both proofs agree, and Proof 1 is in fact stronger: it shows that **once a singleton generator has
ever appeared** (at any index $j$, whether or not $j<n$), no further generator can ever appear, so the
whole theorem already follows for that $a_1$ directly via `lemmas/absorption-lemma.md` +
`lemmas/pc-implies-theorem.md` (the antichain permanently equals $\{\{p\}\}$, trivially $\subseteq
P$, so PC holds vacuously from index $j$ on, and holds for all generator indices $<j$ too since those
are unaffected). In particular, **if $\omega(a_1)=1$** (so $D_1=S=\{p\}$ is itself a singleton), PC
holds for that $a_1$ **immediately and unconditionally**, with $j=1$: no further case analysis is
needed for that sub-family of $a_1$ at all.

### Step 5 — The residual case and the core open target

Combining Steps 1–4: **if PC fails, then at the minimal violating index $n$, $\mathcal A_{n-1}$ has no
singleton block** (every live block has size $\ge2$; in particular $\omega(a_1)\ge2$), and there
exists $H\subseteq P$ with $|H|\le\log_2(a_1)$ hitting every block of $\mathcal A_{n-1}$ while
containing no block in full.

**Core open target (Step 6, unresolved).** Show that no such $H$ can arise from an antichain
$\mathcal A_{n-1}$ that is actually realized by this specific recursion (all blocks pairwise
intersecting — since $\gcd(a_i,a_j)>1$ for *every* pair $i,j$, not just adjacent ones, forces
$D_i\cap D_j\ne\emptyset$ for all $i,j\in\{1,\dots,n-1\}$, in particular for $i,j\in\mathcal A_{n-1}$
— and every block of size $\ge2$, and each block traced back to an actually-realized, previously
minimal term).

**What this round established about Step 6 (narrowing, not closing):**

1. **The claim is false for arbitrary abstract antichains.** E.g. $\{1,2\},\{1,3\},\{1,4\}$ is an
   antichain of pairwise-intersecting sets of size $2$, and $H=\{1\}$ hits every block without
   containing any — so any proof of Step 6 must use structure beyond "pairwise-intersecting antichain,
   blocks of size $\ge2$." This confirms and sharpens the outline's own warning.

2. **The "star" sub-case (all blocks of $\mathcal A_{n-1}$ share one common prime $p^*$) is the natural
   suspect and this round's attempted closure of it did not succeed.** If $\mathcal A_{n-1}$ is a star
   through $p^*$, then (by the same domination argument as Step 3's proof, applied to the whole prefix,
   as in `lemmas/pc-implies-theorem.md` Step A) $p^*$ divides $a_k$ for **every** $k=1,\dots,n-1$ (every
   term's prime set is a superset of some generator's, and every generator contains $p^*$). One might
   hope this forces the next term's minimal valid candidate to avoid large primes (by analogy with
   Absorption), but this is **not established**: LCR shows the true valid-residue set $G_{n-1}$ is, in
   general, a proper superset of "$\{x:p^*\mid x\}$" (validity can be achieved by hitting each block via
   a *different* prime, not only via $p^*$), so the minimal valid $x>a_{n-1}$ is not forced to be a
   multiple of $p^*$, and no contradiction was found. **Computational check (this round, fresh code):**
   among $\ge1000$ tracked antichain snapshots across $a_1\in\{15,105,385\}$, a star with $\ge3$ live
   blocks (the only case not automatically forced — any $2$-block antichain is trivially a star, since
   pairwise intersection alone forces the two blocks to share an element) **never occurred** — strong
   supporting evidence that this recursion's antichains do not become stars once they grow past $2$
   blocks, but this is an empirical observation, not a proof, and no structural reason for it was found
   this round.

3. **A special case does close cleanly, as a sanity check, not a general proof — corrected this round.**
   If $\mathcal A_{n-1}$ consists of *all* $2$-element subsets of some $k$-element prime set
   $\{p_1,\dots,p_k\}$ (the "complete-graph" antichain, generalizing the observed $a_1=15$ triangle
   $\{2,3\},\{2,5\},\{3,5\}$, $k=3$), then no valid $H$ exists **for $k\ge3$** — this is a correction of
   a previously-stated "$k\ge2$" claim, which is **false**: the round-6 proof-reviewer brute-forced
   $k=2,3,4,5$ and found $k=2$ (a single block $\{p_1,p_2\}$) admits the counterexample $H=\{p_1\}$
   (hits the sole block, does not contain it). For $k\ge3$: hitting every $2$-subset means $H$ is a
   vertex cover of the complete graph $K_k$ on $\{p_1,\dots,p_k\}$, whose minimum size is $k-1\ge2$ (any
   2 vertices outside a size-$\le k-2$ subset would form an uncovered edge); but any vertex cover of
   size $\ge2$ contains at least two vertices of $\{p_1,\dots,p_k\}$, which form an edge of $K_k$, i.e.
   a block — so every vertex cover of $K_k$ (for $k\ge3$) already contains some block in full, violating
   (ii). Hence Step 6 holds unconditionally for complete-graph antichains **with $k\ge3$**. This matches
   the observed $a_1=15$ terminal configuration exactly, but general live antichains in this recursion
   are **not** always of this complete-graph shape (blocks can have size $>2$, and need not be all pairs
   of a common ground set), so this does not close the general case — and, as the $k=2$ correction shows,
   does not even close the smallest complete-graph instance.

4. **This round's attempt: a "Coincidence Lemma," and why it does not work.** The idea (proposed by the
   round-6 outliner, adapting crux `aimo-0030`'s purification technique): show that the specific witness
   $H:=\pi(m)$ constructed in Step 3 is not just an abstract hitting-not-containing set, but is *forced*
   to equal $D_j$ for some earlier generator $j<n-1$ — because then $H=D_j\subseteq H$ trivially
   contains the block $D_j\in\mathcal A_{n-1}$, contradicting condition (ii) directly, closing Step 6
   without any further combinatorics.

   **The proposed justification is false, for a sharper reason than the outline-reviewer's flag.** The
   outline's justification was: "$m<a_1$ means $m$ was already tested as a candidate at some earlier
   step of the recursion (every positive integer $<a_1$ is $<a_2<\cdots$, so $m$ was tested for validity
   at step 2 and rejected...)." This is not merely imprecise but categorically wrong: $a_1$ is a **free
   starting parameter** of the problem statement (any positive integer $>1$, arbitrary, not itself
   produced by the recursion), and the recursion's candidates at every step $n\ge2$ are, by definition,
   restricted to integers strictly greater than the current term $a_n\ge a_1$. So no integer $m<a_1$ is
   ever, at any point, a candidate the recursion evaluates — $m$ was **never tested**, at step 2 or any
   other step. This confirms the outline-reviewer's flag exactly (not just imprecisely worded, but false
   as a factual claim about the recursion).

   **A repaired justification was sought and not found; moreover, the natural candidate repair is
   already ruled out by Step 2 above.** The one way "$m$ was already present in the recursion's history"
   *could* have been made literally true is if $m$ turned out to equal some earlier term $a_k$ ($k<n$)
   outright — that would make $\pi(m)=D_k$ a genuine, forced coincidence with an earlier block, with no
   further argument needed. But this is **exactly Case B**, and Step 2 above already proves Case B is
   impossible for a genuine new generator $n$ (it would force $D_k\subseteq D_n$, contradicting $n$
   being a generator by the non-redundancy Convention). So the single natural mechanism that would make
   the Coincidence Lemma true by construction is unavailable *by the very setup that produces $H$ in the
   first place* — $m$ is provably never an earlier term, only possibly sharing its earlier term's
   small-prime signature $\pi$, a strictly weaker and unforced relationship.

   **An explicit counterexample shows the Coincidence Lemma's conclusion does not follow from the
   hit/not-contain properties by any purely combinatorial argument either** (ruling out a
   structure-free repair, not just the specific "$m$ was tested" mechanism). Take a two-block antichain
   $\mathcal A_{n-1}=\{D_1,D_2\}$ with $D_1=\{2,3\}$, $D_2=\{2,5\}$ — pairwise-intersecting (share the
   prime $2$), both size $2$ (so this is a legitimate instance of the Step 6 residual case, "no
   singleton block"). The set $H=\{2\}$ hits both blocks ($2\in D_1\cap D_2$) and contains neither in
   full (both $D_1,D_2$ have cardinality $2>|H|=1$, so $D_i\not\subseteq H$ for $i=1,2$). This $H$ is a
   perfectly valid witness of Step 6's type, and by a pure cardinality argument it **cannot equal either
   block**: $|H|=1<2=|D_1|=|D_2|$. So even granting that *some* valid witness $H$ exists (which Step 3
   already establishes when PC fails), there is no reason internal to the hitting/not-containing
   definition forcing $H$ to have full block size, let alone forcing it to coincide with a specific
   earlier block. Any correct proof of Step 6 (or a repaired Coincidence Lemma) must therefore use
   information beyond "$H$ hits every block and contains none" — e.g. the actual numerical identity of
   $m$, or realizability constraints on which antichains this specific greedy recursion can produce
   (the still-open "no star" empirical fact from item 2 above is one candidate source of such extra
   information, but remains unproved).

   **Conclusion of this round's attempt.** The Coincidence Lemma as proposed is **refuted**: its stated
   justification is false, the one mechanism that would make it true by construction is already
   precluded by Step 2, and a concrete counterexample shows no purely combinatorial repair can work
   either. This is a genuine negative result (not merely an unattempted idea) — recorded per CLAUDE.md's
   "record everything" rule — but it does **not** close or further narrow Step 6 beyond where the file
   already stood; Step 6 remains exactly as open as before this round's attempt.

**Honest assessment.** Step 6 is now the *entire* remaining content of PC (hence of the whole odd-case
theorem): a single, precisely-stated, self-contained combinatorial question about hitting-versus-containing
sets for pairwise-intersecting antichains with blocks of size $\ge2$ that are realized by this specific
recursion. It is strictly narrower than raw PC (all of Steps 1–5 are fully proved, removing all
antichain/domination bookkeeping and the entire singleton-generator branch from the open question), but
it is **not resolved**: neither a general disproof-of-existence-of-$H$ argument, nor a reduction to the
"no star" fact (which itself is unproved, only empirically supported), nor (this round) the proposed
Coincidence Lemma route (now refuted, item 4 above) has closed it. The negative result on the
Coincidence Lemma is informative: it shows that any future attempt on Step 6 must use either (a) the
actual numerical/recursive identity of $m$ (not just its signature $\pi(m)$), since Step 2 already shows
$m$ is never literally an earlier term, or (b) a realizability constraint on the antichain itself (such
as the still-open "no star" fact), since pure hit/not-contain combinatorics alone is provably too weak
(the two-block counterexample above).

## Full proof
(Not applicable — Status is `partial`. Steps 1–5 above constitute a complete, rigorous proof that PC's
failure would force the single combinatorial configuration of Step 6 to exist; Step 6 itself — ruling
out that configuration — is open.)

## Promotable lemmas

**LCR Global Validity Corollary.** *Statement and proof:* see `lemmas/leftover-witness.md` (top
section). Already written to that file this round.

**Leftover-Witness Dichotomy + Case-B-impossible Corollary.** *Statement and proof:* see
`lemmas/leftover-witness.md` (main sections). Already written to that file this round. Improves on the
round-5 explorer's sketch by (a) a direct, self-contained proof that $m\le a_{n-1}$ using $a_n$'s own
minimality (no need to separately exclude $k=n$), and (b) an explicit non-redundancy convention for
"generator index" making the domination arguments airtight, including a clean resolution of the
$m=a_1$ boundary case (folded into Case B, $k=1$).

**Singleton-generator permanence fact.** *Statement:* if any generator index $j$ ever has $D_j=\{p\}$
(a singleton), then no generator index $n>j$ can exist at all — the antichain is permanently
$\{\{p\}\}$ from $j$ onward — and in particular if $\omega(a_1)=1$, PC holds for that $a_1$
unconditionally. *Proof:* given in full above (Step 4, Proof 1), a direct two-line consequence of
`lemmas/absorption-lemma.md` parts (a) and (b) plus the generator Convention; strictly sharper than
merely citing Absorption's own stated consequence, since it additionally shows *no new generator can
ever appear* (not just that the antichain stabilizes as a set). Recommend certifying to
`results/imo-2026-06/lemmas/singleton-generator-permanence.md` if a future approach wants to cite the
"$\omega(a_1)=1$ is trivial" fact or the "no fresh generator after absorption" fact directly.
