## Status
partial

## Approaches tried
- **lex-rewrite-descent** (round 7, NEW) — Foreign-technique transplant (aimo-0960-style ACTIVE local
  rewrite/exchange operator on the lex-minimal bad configuration ordered by (q*, window-index)), meant to
  break the proven-symmetric bad-partner trap with a *designed asymmetric* operator that strictly lowers a
  well-order. **Outcome: the operator does NOT exist as designed — its success condition is logically
  equivalent to the theorem itself (proved circular below), and the a_1-floor blocks the value-descent
  variant.** Reported honestly per the reviewer's mandate (search first, do not hand-wave an operator into
  being). SALVAGE = one new fully-proved, promotable structural constraint on the minimal bad realizer
  (**Lemma X, minimal-bad-term floor-tightness**), a genuine "lower-pressure" fact the field wanted. No
  solve; the route as framed (constructive local descent) is pruned. Reviewer: expected partial.

## Current best

### 0. Mandated computational search (report first, honestly)

The reviewer required a small-case operator search on real bad configurations *before* asserting any
operator. I ran it (sympy, a_1 ∈ {15, 35, 99, 231, 1155}, 300 terms each): **there are ZERO bad terms in
any real greedy sequence** — CSP holds empirically (0 small-disjoint term pairs; F1 pairwise-sharing
confirmed on the first 60 terms of each). This is consistent with every prior round.

Consequence for this approach: **a bad configuration never occurs in an actual sequence**, so the rewrite
operator *cannot be tested or pattern-matched on real data* — it must act on the *hypothetical*
lex-minimal bad configuration assumed to exist for contradiction. The operator therefore cannot be
"found by search"; it must be *proved* to exist purely from the certified structure. I attacked that
proof directly and found the two natural descent targets are both blocked, for reasons I now make
rigorous (this is the honest core deliverable).

Shared notation (all certified): greedy sequence a_1<a_2<…; term = element of E_∞∩[a_1,∞) (ENUM);
P:=primes(a_1); P_max:=max P; S(m):=primes(m)∩[2,P_max]; a prime is *large* iff >P_max. A prime set is
**covering** iff it meets primes(a_i) for every i; **(REAL)** 𝒞=𝒯 (realizability): covering sets are
exactly the prime sets of terms, and every integer ≥a_1 whose prime set contains a covering set is a
term (clause (c)). A term m is **bad** iff S(m) is non-covering (some term B, a *witness*, has
primes(B)∩S(m)=∅). q* := the minimal large linking prime (Lemma A, certified).

### 1. The two designed descent targets are both blocked (rigorous)

The outline offers the operator two ways to strictly lower the order on the lex-minimal bad configuration:
(iii) drop the linking prime below q*, or (i)/(value) shrink the smaller member A. Both fail:

**(a) "Lower the linking prime below q*" is circular — equivalent in strength to the theorem.**
By the certified **Lemma A** (`minimal-linking-prime-and-window-cap.md`): q* is the minimum, over *all*
small-disjoint term pairs, of the (necessarily large) primes they share; every small-disjoint term pair
shares only primes ≥ q*. The operator's success condition (iii) is: produce two terms {A′,B′} that are
small-disjoint (S(A′)∩S(B′)=∅) and share a prime q′ with P_max < q′ < q*. But **the mere existence of
any such pair is, verbatim, "q* is not the minimum large linking prime"** — i.e. the negation of Lemma A's
extremal choice. Exhibiting it is therefore not a *reduction* of the crux; it is a restatement of the
crux (indeed it immediately gives a *smaller* q*, and iterating well-orders the large primes down to a
contradiction only *after* the pair is produced). No certified fact produces such a pair, and producing
one "by an explicit rewrite" is exactly the construction that is equal in strength to the whole theorem.
This confirms and sharpens the standing caveat (`minimal-linking-prime-and-window-cap.md` Scope, and
round-5 memory): *producing a link in (P_max, q*) needs a construction equal in strength to the theorem.*
The (q*)-descent is not an available descent; it is the wall.

**(b) The exchange operator's covering-preservation is a global obstruction (Prop D barrier, re-encountered).**
The remaining hope is an exchange A → A·s/q (q large, q‖A, s a small prime, s<q): primes become
primes(A)\{q}∪{s}. For A′:=A·s/q to be a *term* we need primes(A′) covering (REAL), i.e. the new small
prime s must cover **every** term that q was the sole cover of in A. For A′ to remain *bad* (else no
contradiction — a good term is harmless) we additionally need s to miss the witness B (s∤B), so that
S(A′)=S(A)∪{s} stays non-covering. So the operator needs a single small prime s that (α) covers exactly
the witness set of q and (β) misses B. Whether such an s exists is a **global covering question about the
family {primes(a_i)}**, and at the abstract covering level it can FAIL: the certified **Prop D barrier**
(round 2) states an intersecting covering family CAN have a minimal covering set that genuinely requires
a large prime with no small substitute (e.g. the a_1=15 self-dual triangle {2,3},{3,5},{2,5} has no
centre — `realizability-and-self-dual-clutter.md` Lemma 2 Reusability note). Hence no *local* (rewrite)
operator preserves covering in general; a valid operator would have to be driven by the greedy *value/
window* structure that forces CSP — which is the crux itself. The exchange operator does not exist as a
covering-combinatorial object.

**Conclusion of §1 (honest):** the aimo-0960 transplant, as designed, has no order-lowering
covering-preserving operator. Both descent targets collapse onto the standing wall (they are
equivalent-strength, not reductions). I did not hand-wave one into being. The route as framed is pruned;
recorded so no future round re-attempts the *direct* (q*,k) rewrite.

### 2. Salvage — a NEW, fully-proved structural constraint on the minimal bad realizer

The value-descent variant (shrink A by dividing out a prime) *does* run — it is only stopped by the
a_1-floor — and it yields a genuinely new, certifiable constraint on the smallest bad term. This is the
"lower pressure" the field has wanted (a value fact a minimal bad realizer must satisfy).

**Lemma X (minimal-bad-term floor-tightness).** *Suppose a bad term exists; let m_0 be the smallest one
(well-ordering). Then exactly one of:*
  *(A) m_0 is squarefree and primes(m_0) is a **minimal** covering set (an edge of the clutter ℰ) that
      contains a large prime; or*
  *(B) there is a prime p — either with p^2 ∣ m_0 (a **repeated** prime) or with primes(m_0)\{p} still
      covering (a **cover-redundant** prime) — and for the smallest such p one has m_0 < a_1·p.*

*Proof.* Every term is bad-or-good; m_0 is a term (bad ⇒ term), so m_0 ≥ a_1 and primes(m_0) is covering
(REAL, 𝒯⊆𝒞). Call a prime p **sheddable** if either p^2∣m_0, or (p‖m_0 and primes(m_0)\{p} is covering).
Claim: for every sheddable p, the integer n := m_0/p satisfies n < a_1.

Fix a sheddable p and n=m_0/p (a positive integer > 1, as m_0 has ≥ 2 prime factors: primes(m_0) is
covering hence meets P and, m_0 being bad, S(m_0) is non-covering so primes(m_0) ⊄ [2,P_max], giving a
large prime too). Two cases for its prime set:
 • If p^2∣m_0: primes(n)=primes(m_0), which is covering.
 • If p is cover-redundant (p‖m_0, primes(m_0)\{p} covering): primes(n)=primes(m_0)\{p}, which is
   covering by hypothesis.
In both cases **primes(n) is covering**, so n ∈ E_∞ (n shares a prime with every a_i via the covering
set primes(n)).

Next, **n is bad if it is a term.** Its small part: S(n)=primes(n)∩[2,P_max]. In case p^2∣m_0,
S(n)=S(m_0). In the cover-redundant case, S(n)=S(m_0)\{p} (equality when p>P_max, i.e. S unchanged, or
removal of the one small prime p). Either way S(n) ⊆ S(m_0). Let B be a witness of m_0
(primes(B)∩S(m_0)=∅). Then primes(B)∩S(n) ⊆ primes(B)∩S(m_0)=∅, so **B witnesses S(n) non-covering** —
n is bad whenever n is a term.

Now suppose, for contradiction, n ≥ a_1. Then n ∈ E_∞ and n ≥ a_1, so by ENUM (equivalently REAL
clause (c), primes(n) ⊇ the covering set primes(n)) **n is a term**; by the previous paragraph n is a
**bad** term; and n = m_0/p < m_0 (p ≥ 2). This contradicts the minimality of m_0. Hence n < a_1, i.e.
m_0 < a_1·p, proving the Claim.

If m_0 has NO sheddable prime, then m_0 is squarefree (no repeated prime) and primes(m_0) has no
cover-redundant prime, i.e. primes(m_0) is a **minimal** covering set; since m_0 is bad, S(m_0) is
non-covering so primes(m_0) is not contained in [2,P_max], i.e. it contains a large prime — this is case
(A). Otherwise a sheddable prime exists; taking the smallest one p gives m_0 < a_1·p by the Claim — case
(B). The two cases are mutually exclusive (A has no sheddable prime; B exhibits one). ∎

**What Lemma X buys (and why it does not yet close the crux).** It pins the smallest bad realizer to a
narrow value band: either it is *exactly* the radical of a minimal covering set that genuinely needs a
large prime (case A), or its value is floor-tight, m_0 < a_1·p for its smallest sheddable prime p (case
B). This is a real downward constraint absent from the certified upward tools (bad-partner ascent is
symmetric; the Lemma-6 family multiplies *up*). It does not close the crux because in case (B) the prime
p can itself be large, so the bound a_1·p is weak, and in case (A) m_0 is a genuine minimal-covering
radical whose large prime is *essential* — which the Prop D barrier says the abstract covering level
permits. The missing ingredient remains the greedy value/window fact ruling out case (A) entirely (that
essential-large-prime minimal covering sets never actually arise), which is CSP itself.

### 3. Fallback (aimo-0009 shift-and-overshoot) — not closable this round, recorded

The aimo-0009 "exclude a whole residue block for the minimal witness's class" mechanism was the sanctioned
fallback. As the round-7 explorer already reported, the source proof leans on a *linear inequality chain*
(a_i ≤ n+i−1) with no literal analogue for our covering/divisibility object; the over-exclusion
inequality does not transplant mechanically. I attempted to run several shifted GPC/F1 instances against
the certified mod-L_0 periodicity of S(·) to exclude a residue block for m_0's witness class; this
reduces, again, to producing a covering set disjoint from a whole block of classes, which is the same
global covering question blocked in §1(b). No overshoot inequality found. Recorded honestly as not
closing; not a proven dead end at the mechanism level, but no progress extracted here.

### Standing crux (unchanged, one wall)
No bad term exists (CSP). Equivalently no essential-large-prime minimal covering set is realized. Lemma X
confines the minimal counterexample; the wall is that the *abstract* covering level permits case (A)
(Prop D), so only the greedy value dynamics can rule it out — the surface this route (a static local
rewrite) does not touch. Live carriers of the closure remain window-purity-class-cycle (dynamics/FIN-W)
and covering-small-part-descent (value/local-capacity); this slug contributes the pruning of the direct
rewrite + Lemma X.

## Promotable lemmas

**Lemma X (minimal-bad-term floor-tightness).** *Suppose a bad term exists; let m_0 be the smallest.
Then either (A) m_0 is squarefree and primes(m_0) is a minimal covering set containing a large prime, or
(B) there is a prime p with p^2∣m_0 or with primes(m_0)\{p} covering, and for the smallest such p,
m_0 < a_1·p.* Proved in full in §2 above (imports only certified REAL/ENUM and the definition of bad;
gap-free). Reusable as a value-level constraint on the minimal bad realizer for any descent/minimality
framing (the downward dual of the certified bad-signature geometric family, which only goes up).

**Negative certification (route pruning, for the outliner — not a cache lemma).** The direct
(q*,k)-lowering active rewrite of aimo-0960 flavour has no valid operator: (i) lowering the linking prime
below q* is logically equivalent to negating Lemma A's minimality (equal in strength to the theorem, not
a reduction); (ii) the covering-preserving exchange A→A·s/q requires a single small prime covering q's
entire witness set, which the certified Prop D barrier permits to be impossible at the covering level.
Future rounds should not re-field the *direct* constructive rewrite in the (q*,k) order.
