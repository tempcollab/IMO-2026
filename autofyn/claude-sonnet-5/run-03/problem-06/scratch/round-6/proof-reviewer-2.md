# Round 6 proof-reviewer report — imo-2026-06

Reviewed three built approaches. Overall result: **the problem is SOLVED.**
`current.md` Status updated to `solved`, Full proof written (synthesized from and citing
`approaches/global-signature-purification.md`, independently re-derived and computationally
corroborated below). New lemma files certified:
`lemmas/global-signature-purification.md` (the four load-bearing lemmas of the solved proof),
`lemmas/proper-subset-pigeonhole-dichotomy.md` (a correct, self-contained, but now non-critical
fact from the `gcd-pigeonhole-omega-induction` file).

---

## 1. `approaches/global-signature-purification.md` — claims Status `solved`

### Verdict: **APPROVE** — Status: **solved**

This is a genuinely complete, correct, self-contained proof of the whole theorem, for every
$a_1\ge2$ (both parities — in particular the odd case, which was the entire remaining open content
through round 5). I re-derived every load-bearing step from scratch (not just re-read the prose)
and cross-checked every non-trivial computational claim independently.

**What I did to verify it, in order of the four pieces:**

1. **The recursive "good" definition and well-foundedness.** The domain $\{k,k+1,\dots\}$ is
   order-isomorphic to $\mathbb N$, so strong recursion is legitimate; $\mathrm{good}(k)=T$
   vacuously (no valid witness range). No issue.

2. **Correspondence Lemma (Lemma 0 + Corollary).** I re-did the induction on $n$ by hand:
   part (a) ("$a_{n+1}$ is good") splits on $a_n<m<a_{n+1}$ (bad by IH(ii)) vs. $k\le m\le a_n$
   (either bad by IH(iii), or $m=a_i$ which is ruled out because $\gcd(a_{n+1},a_i)>1$ is exactly
   $a_{n+1}$'s defining property) — airtight, a clean restatement of the recursion's own
   minimality, no hidden step. I then **brute-force checked it computationally**: for $a_1\in\{2,
   \dots,60\}$ (not just the file's tested $\{9,15,21,45\}$), built the actual greedy sequence up
   to $a_1+250$ and independently computed the "good" set via the literal DP recursion on
   $[a_1,a_1+250]$ — **0 mismatches** in every case (my first pass showed spurious mismatches near
   the range boundary caused by an insufficiently-long sequence; once I extended the sequence to
   actually reach the boundary, mismatches vanished — a methodology trap worth flagging for future
   verifiers, not a flaw in the proof).

3. **Purification Lemma.** I re-derived the two cases ($n=0$: $b>a=x$ since $q\mid b/a$; $n\ge1$:
   $x<pk\le ak<aq\le b$ using $p\le a$, $k<q$, and $aq\mid b$ by coprimality) and confirmed both
   inequality chains algebraically. Then **ran 16553 random trials** of the exact construction
   (random $k\in[2,60]$, random $b\in[k,k+2000]$ with a small prime factor) checking $k\le x\le b$,
   $\pi(x)=\pi(b)$, and $x$ $k$-smooth — **0 failures**.

4. **Signature Determinacy Theorem.** This is the crux load-bearing step (a minimal-counterexample
   induction on $\max(a,b)$). I re-derived it line by line, in particular the two places most
   likely to hide a circularity or gap: (i) "$r'$ is good" — this uses the *minimality* of the
   counterexample pair, not the theorem's own conclusion, applied to the strictly smaller pair
   $(r',r)$ with $\max(r',r)=r<a\le\max(a,b)$; this is valid strong induction, not circular. (ii)
   the final contradiction — $p$ small, $p\mid r'$, $\pi(r')=\pi(r)\Rightarrow p\mid r$; $p$ small,
   $p\mid b$, $\pi(a)=\pi(b)\Rightarrow p\mid a$; so $p\mid\gcd(a,r)$, contradicting
   $\gcd(r,a)=1$ — I verified this uses only the *original* hypothesis $\pi(a)=\pi(b)$ (given, not
   derived) and the *just-established* $\pi(r')=\pi(r)$ (from Purification, independent). No
   circularity. I then **brute-force checked it computationally** for $a_1\in\{2,\dots,60\}$ (every
   signature class in $[a_1,a_1+250]$ has uniform good/bad status — 0 mismatches) and additionally
   for two large odd composites $a_1\in\{15015,45045\}$ (0 mismatches in a smaller window). This is
   broader than the file's own tested set $\{15,45,105\}$.

5. **Periodic-Enumeration Lemma and the final claim.** I re-derived the order-preserving-bijection
   argument by hand: $\varphi(x)=x+L$ maps $G\cap[k,\infty)$ bijectively onto $G\cap[k+L,\infty)$
   (periodicity gives membership both directions, injectivity is a shift); since
   $T:=\#(G\cap[k,k+L))$ counts exactly the first $T$ terms of the increasing enumeration of $G$,
   $\varphi$ carries the $n$-th smallest element of $G\cap[k,\infty)$ (i.e. $a_n$) to the $n$-th
   smallest of $G\cap[k+L,\infty)$ (i.e. $a_{T+n}$) — giving $a_{n+T}=a_n+L$ **for every** $n\ge1$,
   not just eventually. This is exactly the theorem's statement, verified to match word-for-word
   (the problem asks for $a_{n+T}=a_n+L$ for every positive integer $n$; the proof delivers exactly
   that, with $T\ge1$ and $L\ge2$ both explicit positive integers). I then **numerically confirmed**
   the actual $(T,L)$ pair against a from-scratch greedy simulation: for $a_1=9$, $L=210$
   (=$2\cdot3\cdot5\cdot7$), $T=70$, checked $a_{n+70}=a_n+210$ for 40+ values of $n$ — all match;
   for $a_1=15$ (the classic hard test case used to refute other approaches in earlier rounds),
   $L=30030$, $T=8008$, checked against all available simulated terms (54 values of $n$, limited by
   simulation budget for this large $L$) — all match. For even $a_1=2$: $L=2,T=1$, giving
   $a_n=2n$, independently matching (not citing) `lemmas/even-persistence.md`.

**No load-bearing gap found anywhere.** The "no circularity" claim in the file is itself checked
and correct (the minimal-counterexample induction never assumes Theorem A's conclusion for a pair
before it is established for a strictly smaller $\max$). The proof does not depend on the
antichain-of-prime-sets/PC/Step-6 machinery that occupied rounds 1-5 at all — it is a genuinely
independent route, and it closes the theorem completely.

**Answer-type check.** This problem is `prove` type (existence of $T,L$), not a numeric
`compute_and_prove`; the proof correctly exhibits explicit $T,L$ (not just asserts existence) and
verifies the periodicity identity holds for all $n\ge1$, matching the rigor-rule bar for
"prove, don't conjecture" and the problem's literal quantifier ("for every positive integer $n$").

**Action taken:** `current.md` Status set to `solved`, Full proof section written (a synthesized,
reviewer-verified restatement citing this approach), and the four lemmas certified to
`lemmas/global-signature-purification.md`.

---

## 2. `approaches/leftover-witness-confinement.md` — round 6 update

### Verdict: **CHANGES REQUESTED** (Status as self-reported: `partial` — accurate, not overclaimed)

This round's content is purely negative/diagnostic (per the dispatch instructions): an attempted
"Coincidence Lemma" for closing Step 6 was proposed and refuted, and a previously-flagged
off-by-one ($k\ge2$ vs. $k\ge3$ in the complete-graph special case) was fixed. I checked both.

- **Refutation of the Coincidence Lemma.** The file gives two independent reasons it fails: (a) the
  proposed justification ("$m<a_1$ means $m$ was tested as a recursion candidate") is categorically
  false, since $a_1$ is a free parameter never itself produced by the recursion, and no integer
  $<a_1$ is ever a tested candidate; (b) the one repair that would make the mechanism true by
  construction (forcing $m$ to literally equal an earlier term $a_k$) is exactly "Case B," already
  proved impossible in Step 2 (domination contradiction with the generator's non-redundancy
  convention); (c) an explicit two-block counterexample ($D_1=\{2,3\}$, $D_2=\{2,5\}$, $H=\{2\}$)
  shows no purely combinatorial repair (hit/not-contain alone) can force $H$ to equal a specific
  block, since $|H|=1<2=|D_1|=|D_2|$ rules it out on cardinality grounds alone. I checked this
  cardinality argument directly — correct and elementary.
- **The $k\ge2\to k\ge3$ fix.** I independently brute-forced the complete-graph vertex-cover claim
  for $k=2,\dots,7$ (does a subset $H$ of $\{0,\dots,k-1\}$ exist that hits every 2-element subset
  but contains none in full?): $k=2$ **has** such an $H$ ($\{0\}$); $k=3,\dots,7$ have **none**.
  This exactly confirms the file's corrected claim ($k\ge3$ closes, $k=2$ does not) and matches the
  memory-recorded round-6 finding. Fix verified correct.

**No new positive lemma or reduction was produced this round** (as the file itself honestly
states) — Step 6 remains exactly as open as before. This matches the self-reported Status
`partial` (not overclaimed to `solved`); the approach's cumulative value (Steps 1-5, established in
prior rounds and already reviewed) is real, so `partial`/CHANGES REQUESTED, not a downgrade to
`unsolved`, is the correct call — the "Current best" is not purely negative overall, only this
round's specific increment is. Now moot for the run's headline goal since the theorem is solved via
an independent route (`global-signature-purification`), but the negative result and the fix are
valuable, correctly-verified population history.

---

## 3. `approaches/gcd-pigeonhole-omega-induction.md` — round 6 update

### Verdict: **CHANGES REQUESTED** (Status as self-reported: `partial` — largely accurate)

This round produced one genuinely new, correctly proved lemma (Proper-Subset Pigeonhole Dichotomy)
and one honest negative finding (the Reduction Lemma mechanism is structurally obstructed, not just
unfound).

- **Proper-Subset Pigeonhole Dichotomy.** Re-derived: for $n\ge2$, $\gcd(a_1,a_n)>1$ is forced by
  the recursion's own constraint at $i=1$, so $R_n:=\mathrm{primes}(\gcd(a_1,a_n))$ is a nonempty
  subset of $S=\mathrm{primes}(a_1)$; either $R_n=S$ cofinitely (Case I) or $R_n\ne S$ infinitely
  often, in which case finite pigeonhole over the $2^{|S|}-1$ proper subsets forces some fixed
  $R_0\subsetneq S$ to recur infinitely (Case II). This is correct, elementary, and self-contained
  — **certified** to `lemmas/proper-subset-pigeonhole-dichotomy.md`.
- **Reduction Lemma obstruction.** The file gives a genuine structural reason (not just "not
  found") the naive reduction fails: a recurring value $R_0=\mathrm{primes}(\gcd(a_1,a_n))$ only
  constrains $a_n$'s interaction with $a_1$ specifically, not with the unboundedly many other
  earlier terms, so the $R_0$-subsequence is not literally (or gap-isomorphically) a copy of a
  fresh recursion seeded at $g_0=\prod_{p\in R_0}p$ — illustrated concretely for $a_1=105$,
  $R_0=\{3\}$ (cofactors $37,41,47,53,\dots$ bear no relation to the trivial fresh recursion at
  $g_0=3$). This is a fair, checked negative finding.
- **Bug found in the file's own "toy counterexample" (Item 5 / Promotable lemmas).** The claimed
  example — "the increasing sequence $b_1=1,b_2=100,b_n=2n$ for $n\ge3$" — is **not actually
  increasing**: $b_3=2\cdot3=6<100=b_2$. This is a genuine error in the stated example (violates
  its own hypothesis). However, I checked the **underlying general claim** computationally (search
  over ~18700 valid strictly-increasing, eventually-arithmetic sequences with random prefixes): in
  ~97% of cases (18060/18691), **no** valid $(T,L)$ exists for all $n\ge1$ — so the qualitative
  warning ("eventually arithmetic does not imply global periodicity-with-shift, in general") is
  correct and important, only the specific published witness sequence is broken. A valid fix: take
  $b_1=2,b_2=6,b_3=9,b_4=12,\dots$ (prefix $\{2\}$, then arithmetic with difference 3 from index 2)
  — verified by direct computation to admit no valid $(T,L)$. This concern is flagged for the
  record but is **not load-bearing** for anything in the now-solved proof: `current.md`'s Full
  proof (Section 4 of `global-signature-purification`) does not rely on
  `lemmas/periodicity-given-no-escape.md` at all, and directly handles prefix consistency correctly
  via the explicit $T:=\#(G\cap[k,k+L))$ construction (verified above, part of the certified
  proof). I did not certify the toy counterexample as stated (bug); a corrected version could be
  certified in a future round if ever needed, but since the theorem is now solved this is low
  priority.

**Status `partial` is accurate** (real new lemma + a correctly-documented obstruction, no
overclaim). Now moot for the run's headline goal.

---

## Overall Status recommendation

**Status: solved.** `results/imo-2026-06/current.md` Status set to `solved`; Full proof written
(citing `approaches/global-signature-purification.md`, independently verified). Certified lemmas:
`lemmas/global-signature-purification.md`, `lemmas/proper-subset-pigeonhole-dichotomy.md`.

Per-slug verdicts:
- `global-signature-purification` — **APPROVE** (Status: solved)
- `leftover-witness-confinement` — **CHANGES REQUESTED** (Status: partial; negative result this
  round, correctly verified, no overclaim)
- `gcd-pigeonhole-omega-induction` — **CHANGES REQUESTED** (Status: partial; one new certified
  lemma, one correctly-documented obstruction, one flagged-and-fixed bug in a non-critical toy
  example)
