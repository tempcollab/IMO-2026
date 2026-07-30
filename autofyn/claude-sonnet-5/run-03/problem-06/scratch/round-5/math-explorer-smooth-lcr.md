## imo-2026-06 — lens: structural mechanism for smoothness in the LCR/PC gap

### Key finding: the problem is essentially "prove periodicity" for the ISL-2013-N5 (Ana/Banana) good-number sequence, and that periodicity is *exactly* the direction the official committee dropped as too hard

The crux corpus entry **`aimo-0030`** (ISL 2013 N5 — the "Ana and Banana" coprime-move game, domain
number_theory) is not just analogous, it is **the same recursion**. Its official solution's
"Comment 2" defines, for a fixed threshold $k$, the sequence of *good numbers* by exactly:
$b_0=k$, $b_{n+1}=$ the smallest $b>b_n$ that is coprime to none of $b_0,\dots,b_n$ — this is
**literally** the imo-2026-06 recursion with $a_1\leftrightarrow k=b_0$. Comment 4 of that official
solution explicitly states: *"The original proposal contained two questions ... (b) to show that the
word $W_k$ [good/bad pattern] is indeed periodic. The Problem Selection Committee thinks that the
[weaker] version is somewhat easier, even though it demands to prove a stronger result [about
signature-invariance]."* I.e. **full periodicity of exactly this greedy sequence was proposed to the
2013 committee and deliberately excluded from the shortlist as (relatively) too hard**, in favor of
the weaker "signature-invariance" statement (any two integers with the same small-prime divisibility
pattern are both good or both bad) that the published solution actually proves. imo-2026-06 is asking
for the harder, dropped direction. This is strong outside evidence that PC / periodicity needs a
genuinely new idea beyond the ISL-2013-N5 machinery, not a routine transplant — but the ISL-2013-N5
machinery is still the best available toolkit to try to adapt.

### The transplantable mechanism, and exactly where it breaks for us

ISL-2013-N5's **Claim 4** (Solution 2) is precisely a "produce a smooth number with the same
small-prime signature" construction: given $b$ with a small prime $p\mid b$ and a big prime $q\mid b$
($q>k$), let $a=$ product of $b$'s small prime factors, and $x=p^n a$ for the least $n\ge0$ with
$x\ge k$. Then $x$ is *similar* to $b$ (same small primes) and $x\le b$. The proof of $x<b$ uses: (i)
minimality of $n$ gives $x<pk$; (ii) $p\le a$ (as $p\mid a$); (iii) **crucially, $k<q$** (true by
definition, since $q$ is "big" iff $q>k$ — the *same* threshold $k$ is both the game's move-floor and
the small/big split point); combining, $x<pk<aq\le b$ (the last step using $aq\mid b$ since
$\gcd(a,q)=1$ and both divide $b$).

**I attempted the direct transplant of this construction to PC** (strong induction on the generator
index $i$, using LCR): suppose the putative bad generator $a_i$ has a large prime $q>L_0$; let
$a:=\mathrm{rad}(D_i^P)$ (product of $a_i$'s small primes) and $x=p^n a$ for least $n$ with
$x>a_{i-1}$. By LCR (already certified, `lemmas/local-congruence-reduction.md`), $\pi(x)=D_i^P=
\pi(a_i)$, so $x$ satisfies exactly the same covering condition as $a_i$ and is **also a valid
candidate** whenever $x>a_{i-1}$ — this half of the transplant works cleanly. The construction gives
$aq\mid a_i$ (since $\gcd(a,q)=1$, both divide $a_i$), so $aq\le a_i$, exactly as in ISL-2013-N5. But
the bound $x<pk<aq$ **requires $a_{i-1}<q$** (their "$k<q$"), and **this fails here**: our threshold
for "small vs. big" ($L_0$, fixed, depending only on $a_1$) is *decoupled* from the sequence's actual
floor $a_{i-1}$ (which grows without bound as $i\to\infty$), whereas in ISL-2013-N5 the same constant
$k$ plays both roles simultaneously. I verified concretely this mismatch is real and not merely
formal: for $a_1=15$ ($L_0=15$), the term after $a_{n}=1009$ has "boring" multiple-of-$L_0$ candidate
$M=1020=2^2\cdot3\cdot5\cdot17$, i.e. **the big prime $q=17$ satisfies $q<a_{i-1}=1009$**, so
$a_{i-1}<q$ is false — the transplant's key inequality has no reason to hold once $i$ is even
moderately large. **This is a genuine, checked negative result** for the literal transplant of
Claim 4/ISL-2013-N5's mechanism, and it independently confirms (from a totally different angle) round
4's own diagnosis that a naive density/threshold argument points the wrong way. Do not retry the
literal transplant; any adaptation needs a substitute for the "$k<q$" step that doesn't rely on
comparing $a_{i-1}$ to $L_0$ directly.

### Correction to round 4's diagnosis paragraph (small but worth flagging)

The `dilworth-antichain-bound.md` "Diagnosis" paragraph asserts the gap-bound's boring candidate $M$
(next multiple of $L_0$ after $a_{i-1}$) is "always-smooth ... (all prime factors in $S\subseteq P$)".
**This is false as stated** — $M$ is only guaranteed to be a multiple of $L_0$; nothing forces
$M/L_0$'s cofactor to avoid large primes. Direct computation ($a_1=15$, $L_0=15$): for
$a_{n}\in\{241,\dots,246\}$, $M=255=3\cdot5\cdot17$, and $17>L_0=15$, so $M$ is **not** $L_0$-smooth.
(It happens to still lie in $P=\{$primes$\le15\}$'s reach only if the extra prime is $\le L_0$; here
it isn't.) This doesn't kill anything load-bearing (the boring candidate's role is only to prove
$a_i\le M$, which doesn't need $M$ itself smooth), but the outliner should not lean on "$M$ is smooth"
as a fact — it is not proved and is false in general.

### Distinct openings for a genuine structural mechanism

1. **Fixed-window vs. growing-floor reframing (the real obstruction, stated cleanly).** By LCR +
   the already-certified window bound ($a_i\in(a_{i-1},a_{i-1}+L_P]$, `signature-stabilization...`),
   PC is exactly: "in a window of *fixed* length $L_P$ (constant, depending only on $a_1$) sliding
   along the integers as $a_{i-1}\to\infty$, is the first integer hitting a fixed union of residue
   classes mod $L_P$ always $L_0$-smooth?" Any structural argument must explain why the *residue
   condition itself* (built from previously realized, already-confined generator primes) biases the
   minimal solution toward smoothness, since raw smooth-number density in a fixed window shrinks to 0
   as the window's location $\to\infty$ (Dickman $\rho$). This reframing is not new content beyond
   round 4's own diagnosis, but stating it via the *fixed* $L_P$ window (not "$a_{i-1}$-dependent
   window of length $L_0$") sharpens it: the window length truly does NOT grow, only its location does
   — worth the outliner knowing precisely which certified lemma supplies this ($y_{n+1}-a_n\le L_P$ in
   `lemmas/signature-stabilization-and-crt-sufficiency.md`, tighter than the informal "$\le L_0$"
   language used in round 4's diagnosis text, though gap-bound's own $\le L_0$ bound is in fact
   tighter still and should probably be the one actually used — the two bounds are not the same and
   the outliner should pick the tightest applicable one explicitly).

2. **Attack via ISL-2013-N5's Claim 5 analogue instead of Claim 4.** Claim 5 there ("any two good
   numbers share a common *small* prime") is proved by minimal-counterexample descent using Claim 4,
   but its *statement* is different from — and possibly more tractable than — PC. A genuinely
   different top-level target to try: prove directly (not via PC) that **any two antichain generators
   $D_i,D_j$ ($i\ne j\in\bigcup_n\mathcal A_n$) share a common prime $\le L_0$** (this is automatic
   from Constraint Domination if $i<j$ and $D_i\subseteq P$ by PC, so it's implied by PC, but might be
   provable *without* first establishing full smoothness of each individual $D_i$ — worth checking
   whether this weaker "pairwise small intersection" statement is enough to run the periodicity
   argument, or whether it's strictly weaker than PC and insufficient). Not attempted; flagged as an
   opening only.

3. **Minimal-counterexample descent on PC itself, but manufacturing the smaller valid candidate from
   the *generator that supplied $a_i$'s validity* rather than from $a_i$'s own factorization.** Since
   by LCR $a_i$'s validity is witnessed purely through $\pi(a_i)=D_i^P$ against each $D_j$,
   $j\in\mathcal A_{i-1}$, and each $D_j\subseteq P$ (by strong induction), the "useful" part of $a_i$
   is exactly $D_i^P$ — a subset of the *finite* lattice $2^P$. Instead of constructing $x=p^n\cdot
   \mathrm{rad}(D_i^P)$ (which is what failed above), consider constructing $x$ as the **smallest
   integer with $\pi(x)=D_i^P$ exceeding $a_{i-1}$ realized as $\mathrm{rad}(D_i^P)$ raised through
   *all* its prime powers jointly via CRT** (i.e. literally $y_{i}$ from the certified sufficiency
   lemma, restricted to residues realizing exactly $D_i^P$) — this is really just re-deriving that
   $a_i\le y_i$, already known; the open content is still whether $a_i=y_i$ *and* $y_i$ (or whatever
   the true minimal solution is) is smooth. This opening doesn't obviously go further than what's
   already certified; flagged as likely redundant with LCR, not a new mechanism — recorded so it is
   not re-tried as if new.

4. **Give up on proving PC for every generator; look for a *different* sufficient condition weaker
   than PC that still closes the theorem via `periodicity-given-no-escape.md`.** E.g. instead of "every
   generator's full prime set $\subseteq P$", try "every generator's full prime set, *intersected with
   its role in $G_{i-1}$*, is eventually periodic as a function of $i$" — i.e. attack Antichain
   Stabilization (the sibling target) directly via a *periodicity-of-the-generator-sequence-itself*
   argument (not smoothness), possibly by showing the sequence of $(D_i^P)_i$ for consecutive new
   generators is eventually periodic as a walk on the finite lattice $2^P$ even if individual $D_i$
   are not smooth — since only $D_i^P$ (not the full $D_i$) is what LCR's $G_{i-1}$ actually depends
   on. This reopens exactly the "Antichain Stabilization without PC" question that
   `self-closing-pair-density-odd-case.md` already tried and found no shortcut for (their Attempt 4);
   flagged as a known-hard alternative, not a fresh mechanism, but worth the outliner knowing it's the
   same target as PC's "byproduct" relationship noted in `dilworth-antichain-bound.md`.

### Cheap-kill candidates
- None obvious for PC itself (it's empirically true in all 24+13 tested cases; no small
  counterexample to search for). The one genuine "cheap kill" found this round is the correction above
  (M is not always smooth) — already folded in; it doesn't kill PC but removes a false intermediate
  claim from the population's record.
- A cheap sanity check for any future mechanism: test it against $a_1=385$ and $a_1=429$
  (`self-closing-pair-density-odd-case.md`'s richest examples, generators using primes outside
  $S\cup\{2\}$, e.g. $19$ for $a_1=385$, and both $2,5\notin S$ for $a_1=429$) — any proposed
  structural argument must produce exactly these primes as the "allowed" outcome and no others; a
  mechanism that can't reconstruct these known generator sets by hand is not yet right.

### Candidate technique(s)
- ISL-2013-N5 (`aimo-0030`)'s three claims (esp. Claim 4's "manufacture smooth similar number", Claim
  5's minimal-counterexample descent) — best available structural toolkit, but the direct transplant
  is refuted (see above); a *modified* version that avoids comparing $a_{i-1}$ to $L_0$ would be needed.
- `modular-arithmetic-and-CRT` + `size-bounding-and-descent` (subtopics) generically fit LCR's
  congruence-minimization framing.
- No sieve/probabilistic-method technique in the corpus looks likely to help (the round-4 diagnosis
  already shows density arguments point the wrong way; `probabilistic-method` subtopic not recommended
  here).

### Knowledge-base entries to use
Read `knowledge_base.md` fully; nothing beyond generic CRT/pigeonhole/induction entries (already cited
by the certified lemmas) looked specific enough to name — no entry addresses smooth-number-in-a-window
questions directly. (If the outliner wants a citation for "count of $M$-smooth numbers up to $x$ is
$O_M((\log x)^{\pi(M)})$", that fact is already used and justified inline in
`self-closing-pair-density-odd-case.md`'s Attempt 3 — cite that derivation, not a KB entry.)

### Analogous past problems (cruxes)
- **`aimo-0030` (ISL 2013 N5, "Ana and Banana")** — the closest possible analogue; same recursion
  (Comment 2), and the exact target (periodicity of the good/bad word) is the officially-acknowledged
  harder direction the shortlist dropped. Crux move: "manufacture a smooth number sharing the same
  small-prime signature, then use it in a minimal-counterexample descent." Transplant attempted this
  round and found to break on the threshold mismatch described above — a real, checked negative
  result, not a guess.
- No other corpus entry found that is genuinely analogous (several matched keyword-level on "prime
  factor" / "smallest integer" / "gcd" but on inspection concern unrelated problem shapes — e.g.
  `aimo-0682`, `aimo-0727`, `aimo-0421`, `aimo-0628` — recorded as checked, not analogous, not
  recommended).

### Prior progress
Current best is `dilworth-antichain-bound.md`'s **PC $\Rightarrow$ theorem** reduction (fully proved,
certifiable) plus **LCR** (fully proved, certified in `lemmas/local-congruence-reduction.md`), reducing
the entire remaining problem (odd $a_1$ only; even case fully solved) to proving PC. PC itself remains
open. This round did not close PC but (a) found and refuted a concrete transplant candidate with a
precise, checked reason, (b) identified the problem's exact relationship to ISL-2013-N5 and the
official acknowledgment that this direction is hard, (c) corrected a false auxiliary claim in the
round-4 diagnosis (M is not always smooth).

### Dead ends (do not retry)
- Literal transplant of ISL-2013-N5 Claim 4's smooth-manufacturing bound to PC's inductive step: fails
  because it needs $a_{i-1}<q$ (previous term less than the offending large prime), which is false in
  general once $i$ is large (checked example: $a_1=15$, $a_{i-1}=1009$, candidate large prime $17$,
  $1009\gg17$). See "The transplantable mechanism" section above for the full argument and why it
  breaks specifically (not just "didn't work" — the exact inequality that fails is identified).
- All previously-recorded dead ends from `dilworth-antichain-bound.md` round 4 (Attempt 1: $\nu_n$
  repackaging; Attempt 3: "every odd-case generator beyond $D_1$ contains 2", refuted by $a_1=21,33,35,
  385,7429$) and `self-closing-pair-density-odd-case.md` round 4 (finite-total-prime-pool route,
  refuted via smooth-number counting; odd-specific PC shortcut, none found) — all confirmed still valid
  on inspection, not retried.

### Small-case / intuition notes (conjecture, not proof)
- Verified computationally (fresh, independent of prior rounds' code) that $M$ (next multiple of
  $L_0$) is genuinely not always $L_0$-smooth: for $a_1=15$, $M=255=3\cdot5\cdot17$ at
  $a_{n}\in\{241,\dots,246\}$.
- The ISL-2013-N5 analogy (same recursion, dropped-as-hard target) is strong intuition that PC is a
  "real" theorem requiring a genuinely new idea, not a folklore fact with a one-page transplantable
  proof — consistent with round 4's own assessment ("apparently of comparable difficulty to Antichain
  Stabilization").
