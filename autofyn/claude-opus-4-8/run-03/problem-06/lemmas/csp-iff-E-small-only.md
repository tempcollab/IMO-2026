# Lemma (Crux-equivalence: (CSP) ⟺ ℰ-small-only)

**Certified** (proof-reviewer, round 9). Independently proved in TWO approaches this round —
`covering-small-part-descent` (Lemma 10) and `minimal-cover-small-only` (Lemma D) — the cross-check
raises confidence; certified once, crediting both.

Notation: greedy sequence a_1<a_2<…; a **term** = element of E_∞∩[a_1,∞) (ENUM); P:=primes(a_1);
P_max:=max P; small ≤P_max, large >P_max; S(m):=primes(m)∩[2,P_max]. A finite prime set is **covering**
iff it meets primes(a_i) for every term. 𝒞=covering sets, 𝒯={primes(term)}; by certified
`realizability-and-self-dual-clutter.md` (Lemma 1) 𝒞=𝒯 with clause (c): every integer ≥a_1 whose prime
set ⊇ a covering set is a term; ℰ = minimal covering sets (edges). A term m is **bad** iff S(m) is
non-covering. **(CSP)** = no term is bad. **ℰ-small-only** = every edge C∈ℰ satisfies C⊆[2,P_max].

## Statement
(CSP) ⟺ ℰ-small-only.

## Proof
Elementary monotonicity used throughout: covering sets are up-closed under ⊆ (a superset of a covering
set meets every color the subset meets); equivalently, a subset of a non-covering set is non-covering.

**(⇐) ℰ-small-only ⟹ (CSP).** Let m be a term and C:=primes(m)∈𝒯=𝒞 (covering). 𝒞 is an up-set of finite
sets, so C contains an edge C'∈ℰ. By hypothesis C'⊆[2,P_max], and C'⊆C, so C'⊆C∩[2,P_max]=S(m). C' is
covering, hence its superset S(m) is covering: m is not bad. As m was arbitrary, (CSP) holds.

**(⇒) (CSP) ⟹ ℰ-small-only.** Suppose some edge C∈ℰ contains a large prime q. Fix p_1∈C and let k≥0 be
least with N:=(∏_{p∈C}p)·p_1^{k}≥a_1. Then primes(N)=C exactly (the power of p_1∈C adds/drops no prime).
Since primes(N)=C is covering and N≥a_1, clause (c) makes N a term. Its small part
S(N)=C∩[2,P_max]⊆C∖{q} (q large, q∉[2,P_max]). Because C is a minimal cover and q∈C, the proper subset
C∖{q} is non-covering, hence its subset S(N) is non-covering: N is a bad term, contradicting (CSP). So no
edge carries a large prime; ℰ-small-only holds. ∎

## Reusability
Pins the standing crux (CSP) at the transversal level: it is *literally* the statement that no large
prime is load-bearing in any minimal covering set — not weaker, not stronger. Bridges the value language
of (CSP) and the set-system (edge) language of ℰ. Any approach may target either face. Gap-free; no
stronger than proved (a biconditional).
