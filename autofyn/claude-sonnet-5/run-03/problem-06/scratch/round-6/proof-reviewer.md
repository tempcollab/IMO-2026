# Proof review — round 6 (reviewing round 5's build output, unreviewed due to interruption)

Problem: imo-2026-06. Even $a_1$ is fully closed (round 4, `absorption-recurrence-even-case.md` +
`lemmas/even-persistence.md`, not re-litigated this round). All remaining content is $a_1$ odd,
where the field's shared target is Antichain Stabilization / P-Confinement (PC).

Reviewed three round-5-built approach files in full, cross-checked every cited lemma's actual proof
body (not just its stated hypothesis list), independently re-derived the load-bearing steps, and ran
one brute-force computational check.

---

## 1. `leftover-witness-confinement.md`

**What it does.** Minimal-counterexample descent on PC: assume $n$ minimal with $D_n\not\subseteq
P$; write $a_n=q^e m$ for the offending large prime $q$; shows (Leftover-Witness Dichotomy, in
`lemmas/leftover-witness.md`) $m<a_1$ (Case A) is forced, since $m=a_k$ for $k<n$ (Case B) would
contradict $n$ being a genuine new generator; then $H:=\pi(m)$ hits every block of $\mathcal A_{n-1}$
without containing any, and is a fixed-size ($\le\log_2 a_1$) witness. Rules out the case where
$\mathcal A_{n-1}$ has a singleton block (two independent proofs, one via Absorption). Leaves "Step
6" — no such $H$ can arise from a *realized*, pairwise-intersecting antichain with all blocks size
$\ge2$ — as the sole open target.

**Verification performed.**
- Re-derived `lemmas/local-congruence-reduction.md`'s proof by hand: confirmed the ($\Leftarrow$)
  direction genuinely never uses $x>a_{i-1}$ (only Constraint Domination and $D_j\subseteq P$ for
  $j<i$), so the "LCR Global Validity Corollary" in `lemmas/leftover-witness.md` is legitimate, not a
  leap.
- Re-derived the Leftover-Witness Dichotomy proof (Steps 1–3 of `lemmas/leftover-witness.md`) line by
  line: Step 1 (global validity of $m$) is a correct chain through Constraint Domination and PC for
  smaller generators; Step 2 ($m\le a_{n-1}$ from $a_n$'s own minimality, avoiding a separate "rule
  out $k=n$" case) is correct and actually cleaner than the round-5 explorer's original sketch; Step 3
  (dichotomy via the standard "find $k$" argument, with the $m=a_1$ boundary folded cleanly into Case
  B $k=1$) is correct.
- Re-derived the "Case B impossible" corollary and Step 4's two proofs (singleton-block case): both
  correct, non-circular (Case B's contradiction uses only $D_k\subseteq D_n$, $k<n$, vs. the
  non-redundancy convention on generators — not the conclusion being sought).
- Re-checked `lemmas/absorption-lemma.md` (already certified round 2) and confirmed Step 4's use of it
  is valid: part (a)'s "$q\mid a_i$ for every $i\ge1$" genuinely applies to $a_n$ even though $j\le
  n-1<n$.
- **Found an error, brute-forced it in Python:** Step 6's discussion point 3 claims the "complete-graph
  antichain" special case (all 2-subsets of a $k$-set) has no valid witness $H$ "for any $k\ge2$." I
  wrote a brute-force search over all hitting-but-not-containing sets for $K_k$, $k=2,\dots,5$: at
  $k=2$ (a single 2-element block $\{p_1,p_2\}$), $H=\{p_1\}$ (and $\{p_2\}$) is a genuine
  counterexample — hits the sole block, does not contain it. For $k\ge3$ the claim holds (minimum
  vertex cover size $k-1\ge2$ forces containment of an edge). So the claim is correct only for
  $k\ge3$, not $k\ge2$ as stated. This is **not load-bearing** — the file already, correctly, states
  Step 6 remains open overall and this special case is presented only as a "sanity check, not a
  general proof" — but it is a genuine, previously-unflagged computational/logic error that should be
  fixed (the $k\ge2$ wording is simply wrong).
- Steps 1–5 do not overclaim: the file's own "Honest assessment" correctly states Step 6 is open, and
  the self-reported Status (`partial`) matches reality.

**Verdict: CHANGES REQUESTED.** True Status: **partial**. Real, verified narrowing of PC into one
crisp combinatorial target; certify `lemmas/leftover-witness.md` and
`lemmas/singleton-generator-permanence.md` (done, see below). Gap to close: Step 6 itself, plus the
cosmetic $k\ge2\to k\ge3$ fix in the file's own text.

---

## 2. `antichain-signature-closure.md`

**What it does this round.** Closes the round-2-flagged citation-hygiene gap: Lemma 3 previously
instantiated `lemmas/periodicity-given-no-escape.md` with $P^*$ built from the eventual generator set
without verifying $\mathrm{primes}(a_1)\subseteq P^*$. This round re-reads that lemma's proof body
directly and shows the hypothesis is never used.

**Verification performed.** Read `lemmas/periodicity-given-no-escape.md`'s proof in full (lines
10–37): confirmed it consumes only "$P$ finite, $G$ nonempty $\subseteq\mathbb Z/L_P\mathbb Z$,
$a_{n+1}=y_{n+1}$ for $n\ge N_1$" — the pigeonhole/periodicity/re-indexing argument never touches
$\mathrm{primes}(a_1)$ or any relation between $P$ and $a_1$. So the claimed fix is **correct**: the
citation is now genuinely valid, not merely re-asserted. Also re-verified $G^*\ne\emptyset$ ($0\in
G^*$ since $\pi(0)=P^*\supseteq$ every $\mathrm{primes}(a_{i_j})$, each nonempty). Lemma 2's
two-directional iff and Lemma 5 (self-closing $\Rightarrow$ permanent stabilization) re-derived and
confirmed correct — no gap in steps 4–6 given Antichain Stabilization. Cross-check with
`leftover-witness-confinement`'s "no singleton block" residual case is a legitimate, correctly-stated
consistency observation (both independently converge on the same open scope).

No overclaiming: file states clearly the core target (self-closing reachability) is still open.

**Verdict: CHANGES REQUESTED.** True Status: **partial**. The specific claimed fix (citation-hygiene)
is correct and closes real technical debt flagged two rounds ago. No new gap introduced.

---

## 3. `global-smooth-density-contradiction.md`

**What it does.** New, genuinely different (global counting/contradiction, not local
minimal-counterexample) architecture, dispatched as this round's diversity requirement. Proves: (1)
Growth-Event Update Lemma + Corollary restating Antichain Stabilization as "finitely many growth
events"; (2) Type A (unconditionally finite, elementary pigeonhole) vs. Type B (open, exactly the
PC-violating events) decomposition; (3) a "$P'$-enlargement Master Lemma" showing Antichain
Stabilization alone (not P-Confinement relative to the fixed $P$) suffices for the theorem — this
independently repairs the same citation-hygiene issue `antichain-signature-closure` fixed, via a
cleaner explicit construction ($P':=P\cup\bigcup\mathcal A^\infty$, automatically $\supseteq S$); (4) a
rigorous negative result refuting the dispatched global smooth-number-density mechanism.

**Verification performed.**
- Re-derived Lemma 1 (Growth-Event Update) and Corollary 1 from the finite-poset argument by hand:
  correct, standard, no gap.
- Re-derived Propositions 2–3 (Type A bound $\le 2^{|P|}-2$; Type B $\Rightarrow$ not $L_0$-smooth):
  correct, elementary.
- Re-derived the Master Lemma step by step against `lemmas/pc-implies-theorem.md` (confirmed that
  lemma's Steps A–D are genuinely generic in the finite prime set — re-read the proof text, confirmed
  it uses only "PC relative to $P_0$" and "$N_1$-stabilization relative to $P_0$," nothing tied to the
  specific fixed $P=\{p\le L_0\}$) and against `lemmas/signature-stabilization-and-crt-sufficiency.md`
  (confirmed genuinely generic in any finite $P_0\supseteq S$, with $0\in G$ always). The
  reinstantiation with $P':=P\cup\bigcup\mathcal A^\infty$ is valid: finite, $\supseteq S$
  automatically. No gap found.
- Re-derived Propositions 4–5 (smooth-number counting bound $O((\log x)^{\pi(M)})$, hence density
  $\to0$; so non-smooth density $\to1$): standard, correct, elementary, and correctly used to refute
  (not merely fail to find) the specific dispatched mechanism — the required scarcity runs the wrong
  direction.
- Section 5's honest convergence note (residual target = same event set as
  `leftover-witness-confinement`'s Step 6) is an accurate, useful cross-check, not an overclaim.

No overclaiming: Status `partial` is correct; the file is explicit that (4) is a negative result, not
a proof, for the specific tool it was asked to try.

**Verdict: CHANGES REQUESTED.** True Status: **partial**. Genuine new architecture, two new certified
lemmas, one rigorous, checked negative result (documented dead end for the "smooth-density scarcity"
mechanism specifically). Core gap (Type B finiteness) remains open, and is now known — via three
independently-built, independently-verified routes — to be one single combinatorial fact.

---

## Cross-cutting note

All three approaches converge, via independent constructions, on an equivalent open target:
"leftover-witness-confinement's Step 6" = "antichain-signature-closure's self-closing reachability
restricted to no-singleton-block antichains" = "global-smooth-density-contradiction's Type B
finiteness." This convergence across three independently built and independently reviewed routes is
strong evidence the population has correctly isolated the problem's true remaining difficulty, not an
artifact of one framing. None of the three routes closes it this round. Per the orchestrator's
plateau-breaking rule, this is a legitimate multi-round wall (now round 5/6 in this exact combinatorial
form); the next round should either attack "Step 6" head-on with new combinatorial machinery (e.g. a
structural classification of which antichains are actually realizable by this specific greedy
recursion — the abstract counterexample $\{1,2\},\{1,3\},\{1,4\}$ shows realizability constraints
beyond "pairwise-intersecting, blocks $\ge2$" are essential) or open a genuinely new top-level framing
that avoids the antichain-of-prime-sets object entirely, per the round-5 outline-reviewer's own
diagnosis.

## Lemmas certified this round

- `results/imo-2026-06/lemmas/leftover-witness.md` — already present, independently re-verified,
  **certified** (LCR Global Validity Corollary; Leftover-Witness Dichotomy; Case-B-impossible
  Corollary).
- `results/imo-2026-06/lemmas/singleton-generator-permanence.md` — already present, independently
  re-verified, **certified**.
- `results/imo-2026-06/lemmas/antichain-stabilization-implies-theorem.md` — newly written this round
  by the reviewer from `global-smooth-density-contradiction.md`'s Master Lemma, independently
  re-derived and **certified**.
- `results/imo-2026-06/lemmas/growth-event-decomposition.md` — newly written this round by the
  reviewer from `global-smooth-density-contradiction.md`'s §1/§3 (Growth-Event Update Lemma,
  Corollary 1, Type A/B Propositions 2–3), independently re-derived and **certified**.

## `current.md`

Updated: added a "Round 5 update" summary paragraph, added three "Approaches tried" entries for
`leftover-witness-confinement`, `antichain-signature-closure` (round 5 advance), and
`global-smooth-density-contradiction`, all marked CHANGES REQUESTED / partial. Overall `## Status`
**stays `partial`** — no approach reached `solved`; the odd-$a_1$ case remains open, now reduced
(three independently-verified ways) to a single precise combinatorial claim about realizable
antichains.

---

## Per-slug verdicts

- `leftover-witness-confinement`: **CHANGES REQUESTED** (Status: partial). Gap: Step 6 (no
  hitting-but-not-containing witness for realized, pairwise-intersecting, no-singleton-block
  antichains) is open; fix the false $k\ge2$ claim (should be $k\ge3$) in the complete-graph
  discussion.
- `antichain-signature-closure`: **CHANGES REQUESTED** (Status: partial). Citation-hygiene fix
  verified correct and complete; core target (Antichain Stabilization / self-closing reachability)
  remains open.
- `global-smooth-density-contradiction`: **CHANGES REQUESTED** (Status: partial). New architecture and
  two new lemmas verified correct; dispatched mechanism (smooth density) rigorously and correctly
  refuted as a documented dead end; core target (Type B finiteness) remains open.

**Overall recommendation for `current.md` `## Status`: partial** (unchanged from before this review;
even case solved, odd case narrowed further but not closed).
