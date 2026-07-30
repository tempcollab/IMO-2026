# Lemma 15 — Hub abundance under ¬(FIN-Q)

Source: `approaches/covering-small-part-descent.md` (round 10). Reviewer-certified round 10 (gap-free;
imports the certified (★) membership dichotomy from `finite-connector-pool-periodicity.md`).

Notation: L_0=∏_{p≤P_max}p; for a residue r∈ℤ/L_0ℤ, S(r) its small part, R'_bad={r : S(r) non-covering,
E_∞ meets class r}, W(r)={i : primes(a_i)∩S(r)=∅}, Q_i=primes(a_i)∩(P_max,∞), Q(r)=⋃_{i∈W(r)}Q_i. The
certified dichotomy: for r∈R'_bad and m≡r (mod L_0), **m∈E_∞ ⟺ ∀i∈W(r) ∃q∈Q_i: q∣m** (★).

**Statement.** Assume ¬(FIN-Q): some r_0∈R'_bad has Q(r_0) infinite. Let
H={m≥a_1 : m≡r_0 (mod L_0), m∈E_∞}. Then
(a) a finite transversal D of {Q_i : i∈W(r_0)} exists;
(b) H is infinite;
(c) every m∈H is a bad term with S(m)=S(r_0) and Q(m) a finite transversal of {Q_i}.

**Proof.** (a) Fix m_1∈E_∞ in class r_0; (★) forward gives, for each i∈W(r_0), some q∈Q_i with q∣m_1, so
D:=Q(m_1) (finite) meets every Q_i. (b) gcd(L_0,∏D)=1 (D large primes ∤ L_0); by CRT the system m≡r_0
(mod L_0), m≡0 (mod ∏D) has infinitely many solutions m≥a_1; each satisfies (★) (q∈D∩Q_i divides m), so
m∈E_∞, hence (ENUM) a term, and m∈H. (c) m∈H ⟹ term; S(m)=S(m mod L_0)=S(r_0) non-covering ⟹ bad; (★)
⟹ Q(m) meets every Q_i. ∎

Reusable structural fact about a ¬(FIN-Q) configuration (an infinite family of bad hubs of fixed small
part and residue). Pruning note (verified): a single finite transversal already produces the whole family,
and any value-shed changes m mod L_0 — so the residue-class pigeonhole and value descent are orthogonal
(the round-10 iterated-hub-value-walk closer cannot descend). Superseded as a closing route by the
round-10 solve (`smallest-essential-prime-descent`), but the lemma itself is correct and reusable.
