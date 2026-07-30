# Proof-builder report — imo-2026-06 / minimal-cover-small-only (round 9)

**Status: partial** (advanced). Gap (step 4, ℰ-small-only for |P|≥2) NOT closed — honestly open.

## What I did
Filled the round-8 skeleton and added one gap-free new lemma. The approach targets the whole P6
claim via (CSP), through **ℰ-small-only** ("every minimal covering set / edge of the self-dual clutter ℰ
lies in [2,P_max]"), by a **pure-transversal** mechanism (no value induction). Steps 1,2,3,5 remain
gap-free from certified lemmas; the base case |P|=1 is complete.

## New rigorous result this round — Lemma D (promotable)
**ℰ-small-only ⟺ (CSP), both directions, gap-free.** The reviewer flagged the target as
"crux-equivalent-or-stronger" and asked to resolve it. I proved the missing converse:
(CSP) ⟹ ℰ-small-only, by realizing any hypothetical large-prime edge C as an explicit **bad term**
m=(∏_{p∈C}p)·q^k ≥ a_1 (a term by certified Realizability clause (c), with small part S(m)⊆C∖{q}
non-covering because C is a minimal covering set). Combined with the endgame (I)⟹(II), this shows the
pure-transversal target is **literally equivalent** to the standing crux (CSP) — not weaker, and not
strictly stronger. Imports only `realizability-and-self-dual-clutter.md`. Proposed for certification.

## On the reviewer's specific ask (downward well-founded monovariant)
I could NOT produce one, and Lemma D now explains why rigorously: the essential-witness partner map
C↦C' (Lemma C4) is **horizontal** — C∩C'={q} keeps the same large prime q (q∈C'), and C''s other large
primes are unconstrained by C — so max-large-prime, |Q_C|, ∏Q_C, min/max large prime are none forced to
decrease. Since ℰ-small-only IS (CSP), whose only surviving obstruction is the a_1 *value* inequality,
no purely transversal (prime/edge) quantity can carry the closing pressure. I recorded this as an honest
obstruction, NOT as a theorem: (CSP) holds on every numeric seed, so no configuration exhibits an
increase, hence I do not claim "no downward monovariant exists" — only that this construction yields none.

I respected every barred closure (global Σ1/p², pure covering/Helly per Prop D, symmetric ascent,
aimo-0016, direct (q*,k) rewrite) and did NOT reintroduce value-descent (Lemma D uses value only via
"a_1 is a term"/Realizability, staying set-theoretic in mechanism).

## Honest gap
ℰ-small-only for |P|≥2 = (CSP) = the crisp value inequality. Not closed. The base-case contradiction
(|P|=1) dissolves for |P|≥2 because C∩C'={q} only forces disjoint non-empty P-parts, bounding the
partner family by |P| with no contradiction.

## Files
- Approach: `/home/agentuser/repo/results/imo-2026-06/approaches/minimal-cover-small-only.md`
- Promotable: Lemmas A, B, C (from round 8) and **NEW Lemma D (ℰ-small-only ⟺ (CSP))**.

## Note for the orchestrator
Lemma D formally confirms the "3rd collapse to one wall": this transversal reformulation equals (CSP)
exactly. The pure-transversal route has no independent closing mechanism (its natural map is horizontal).
Keep the approach live as the clean transversal statement of the crux, but the field's closing pressure
must come from the value lane (covering-small-part-descent / a growth-rate–recruitment framing), as the
round-8 diversity note anticipated.
