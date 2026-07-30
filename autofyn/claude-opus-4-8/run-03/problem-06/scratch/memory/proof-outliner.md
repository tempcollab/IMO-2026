# proof-outliner role memory

ALWAYS: for greedy-gcd-sequence problems, first check whether the sequence equals the increasing
enumeration of the "compatible set" {m : gcd(m,a_i)>1 ∀i} — the inclusion E_∞ ⊆ E_n (finite-step
eligible sets shrink) makes "greedy min never skips a compatible element" a clean rigorous reduction
that kills the transient and gives the "for every n" (not just eventual) periodicity for free. Found on
imo-2026-06, round 1.

NEVER: trust an explorer's clean modular predicate ("eligible ⟺ divisible by ≥2 of core primes") without
a numeric exact-set check — it was FALSE for imo-2026-06 a_1=35 (34 residues mod 210, not the 70 the
predicate gives). Verify residue-set equality, not just cardinality, before committing an approach to it.
(round 1)

ALWAYS: run a quick sympy simulation to (a) confirm the target identity holds from n=1 vs only
eventually, and (b) locate the single isolated gap, before writing approach files — it turned a vague
"prove periodicity" into "prove one finiteness lemma" on imo-2026-06. (round 1)

ALWAYS: when a field has collapsed to ONE certified crux (imo-2026-06 Lemma A), give each new
slug a genuinely different ATTACK SURFACE (static set-identity induction / dynamic recruitment
monovariant / global capacity count) and state honestly that they share the crux — do not pretend
they are independent proofs. Reviewer wants diversity of surface + explicit gap, not fake closure.
(round 2)
NEVER: propose the "peel the large prime off the cofactor" route on greedy-gcd problems — it is
CIRCULAR (the peeled cofactor's compatibility is a corollary of the very crux). Flagged by explorer
on imo-2026-06 round 2. (round 2)
ALWAYS: reformulate a "share a small prime" crux as "every element's small part is itself a
covering set" (CSP) — the implication (CSP)⇒(SL) is a free two-liner (two covering sets pairwise
intersect in a small prime), which cleanly re-targets the whole field. Found on imo-2026-06 r3. (round 3)
ALWAYS: when window-minimality/smaller-competitor is proven dead (empty window), pivot to a global
well-ordering on VALUE — the "smallest bad term's large-partner is a strictly LARGER bad term"
ascent gave a genuinely new proven opening on imo-2026-06 r3 (larger known terms may be used as
upper-bound competitors; smaller ones are forbidden). (round 3)
NEVER: target "witness term is P_max-smooth" — literally FALSE (a1=231 has term 237=3·79). The true
crux is REDUNDANCY: large primes divide terms freely, they are just never the SOLE bridge. (round 3)
ALWAYS: to escape a SYMMETRIC well-order trap (imo-2026-06 mutual bad-pair, ascent folds back), move the
extremal object OFF the terms — order a residue class / a linking PRIME / a window index instead. The
per-class witness-index-set W(r) (fixed by r mod L_0) and q*=min large sole-link prime are genuinely
non-symmetric handles the term-value well-order cannot supply. (round 5)
NEVER: propose any window-CRT / "length-a_1 window holds a full residue system mod L_0" step on
imo-2026-06 — VERIFIED FALSE (a_1<L_0 for a_1∈{15,35,231}); a_1 can be ≪ L_0 (a_1 prime ⇒ L_0=primorial).
Any residue-pigeonhole must avoid needing a_1 ≥ L_0. (round 5)
ALWAYS: on imo-2026-06 the GREEDY-DYNAMICS surface is best entered via "Window Purity" — ENUM makes the
terms = E_∞ enumerated, so the open gap (a_n,a_{n+1}) contains NO E_∞-element, hence every interior integer
is non-covering. Cheap certifiable lemma, per-window, avoids the dead global count. The genuine wall behind
the star is MUTUAL/CYCLIC infinite witnessing (single-sided witness folds harmlessly into finite Q_rel of
the certified Reduction Lemma) — a strictly narrower target than "star exists". (round 7)
NEVER: assume "one hub blocks the whole rejection window (a_n,a_{n+1})" on imo-2026-06 — REFUTED numerically
r7 (only ~45–100% of windows depending on a_1, never universal); multi-hub joint rejection is the norm. (round 7)

ALWAYS: when the field has collapsed to one wall 3x, keep the same-wall approaches on DIFFERENT targets (imo-2026-06 round 8: ℰ-small-only [set-only] vs crisp-value-inequality [value] attack the same crux but avoid the single-gap trap by not sharing a gap). (round 8)
NEVER: merge a new pure-mechanism approach into an advancing one just because the reformulation is "cleaner" — that recreates the shared-gap collapse the mandate forbids. (round 8)

ALWAYS: on imo-2026-06 the OPEN crux (no large prime is an essential connector) is LITERALLY aimo-0030 (IMO "Ana-Banana") Claim 3 under the dictionary k↔P_max, "n bad"↔non-covering set, "good"↔covering; Claim 1↔support-monotonicity(certified), Claim 2↔Lemma 6(certified). So aimo-0030's minimal-counterexample value-descent (manufacture a smaller coprime witness y^α via the cofactor, floor/power chain) is the natural transplant — its inequality y^α<ky<py=x/p^{r-1}<n/p^{r-1} is the crux-equivalent gap. Fielded round 10 as smallest-essential-prime-descent. (round 10)
NEVER: field the "recruitment costs one slot per window" counting mechanism on imo-2026-06 — recruitment-counting explorer self-certified it decomposes into Lemma B (bounds a RATE not a total) + (R2') (confinement ⟺ Q(r_0) finite = the conclusion). Only the greedy per-STEP existence constraint (successor must exist in the a_1-window) escapes, not occupancy statistics. (round 10)
