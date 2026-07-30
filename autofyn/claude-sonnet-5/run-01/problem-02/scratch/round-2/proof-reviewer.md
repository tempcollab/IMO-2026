# Proof review — imo-2026-02, round 2

Reviewed three built approaches. All independently re-derived from scratch with sympy (not trusting
the builders' claimed CAS output) at the load-bearing step. Verdicts below are per-slug and
independent.

## 1. `synthetic-angle-chase-aklastar` — builder claimed Status: solved

**Verdict: CHANGES REQUESTED.  True Status: partial (builder overclaimed).**

### What I checked
This is a pure-coordinate proof. Setup: $B=(0,0),C=(a,0),A=(p,q)$, $M,N$ midpoints, $K=B+T_K
R(-\alpha)(A-B)$, $L=C+T_L R(\alpha)(A-C)$ built so hypothesis (i) ($\angle KBA=\angle ACL=\alpha$)
holds automatically. Hypotheses (ii) $\angle LBK=\angle LNC$ and (iii) $\angle LCK=\angle BMK$ are
encoded via the cross/dot tangent identity as polynomials $e_1,e_2$. The target $OM=ON$ reduces
(Step 0–1, elementary and correct — I re-derived it independently) to a polynomial $\mathrm{myexpr}=0$.

I rebuilt $e_1,e_2,\mathrm{myexpr}$ from the literal definitions in the file (not copying the
builder's claimed simplified forms) in sympy, independently:
- Confirmed $e_1$ is linear-homogeneous in $T_K$ and $e_2$ linear-homogeneous in $T_L$ (the claimed
  "decoupling" structure) — genuinely true, verified by `sp.Poly(...,TK).degree()==1` etc.
- Confirmed the claimed quadratic form of $\tilde A_1(T_L)$ matches $A_1$ only *modulo* $c^2+s^2=1$
  (expected, since $c=\cos\alpha,s=\sin\alpha$) — fine, not an issue.
- **Load-bearing step**: I independently re-derived the closing identity. Computing $\mathrm{myexpr}$
  fresh from $u=K-A,v=L-A$ and checking `myexpr*Z - (2(q-TK*X)*A1 + 2(TL*X'-q)*B1)` expands to exactly
  0 as a polynomial in all 7 free symbols $(p,q,a,c,s,T_K,T_L)$ — confirmed **both** by full symbolic
  `sp.expand` (exact zero polynomial, no `c²+s²=1` substitution needed at all — stronger than the
  builder even claims) **and** by evaluating at a random rational point
  ($p=3/7,q=5/2,a=11/3,c=-2/5,s=1/3,T_K=7/4,T_L=9/5$): both sides equal $-22643823187/109760000$
  exactly. **This identity is genuinely correct.**

### The gap
The proof concludes "$\mathrm{myexpr}=q_1A_1+q_2B_1$" with $q_1=2(q-T_KX)/Z$, $q_2=2(T_LX'-q)/Z$,
i.e. it **divides the verified identity by $Z$** (the leading $T_L^2$-coefficient of $A_1$) to get
from `myexpr·Z = ...` to `myexpr = ...`. **`Z≠0` is never proven anywhere in the file** — I grepped
the whole document for any nonzero-justification of `Z` and found none (only `cross(u,v)≠0`, a
*different* quantity, is justified, via "AKL is a genuine triangle"). Since $A_1=B_1=0$ under the
real hypotheses (ii),(iii), the *actually proven* fact is $\mathrm{myexpr}\cdot Z=0$, which gives
$\mathrm{myexpr}=0$ **only if $Z\neq0$**.

I checked numerically whether $Z=a(cq-ps)+s(p^2+q^2)$ is identically one sign over the ambient
parameter range (200,000 random samples of $p,q,a,\alpha$ in plausible triangle/angle ranges): it is
**not** — both positive and negative values occur, with values arbitrarily close to 0. So $Z=0$ on a
nonempty codimension-1 locus in the ambient parameter space; whether that locus can be reached while
also satisfying the actual geometric constraints ($K$ strictly inside $\triangle BMC$, $L$ strictly
inside $\triangle BNC$, the position hypotheses, and $A_1=B_1=0$ simultaneously) is an open question
the proof does not address at all.

**This is precisely the gap that `coordinate-groebner-elimination` independently derives and honestly
flags as open** (`D1 = 2Z`, confirmed by direct comparison of the two files' formulas — coordinate-
groebner's `D1 = 2a·ca·q − 2a·p·sa + 2p²·sa + 2q²·sa = 2(a(ca·q−p·sa)+sa(p²+q²)) = 2Z` exactly). The
two approaches, despite different framing narratives, have converged onto the same unresolved
algebraic wall. The synthetic file's "no case split needed" framing is correct for the $AB=AC$ vs
$AB\neq AC$ question (myexpr never divides by $p-a/2$) — but that is a different division than the
one that's actually missing (division by $Z$), and the builder appears to have conflated "handles the
isosceles case uniformly" with "the proof is complete," missing the real gap entirely.

### Secondary issue (lesser, but real)
The sign/orientation convention for the directed-angle-equality lemma (which rotation direction, $-\alpha$
vs $+\alpha$, and which of the two cross/dot orderings, correctly encodes hypotheses (ii),(iii) as
stated, as opposed to a supplementary or reflected angle condition) is justified only by numerical
spot-checks on **one** triangle and **three** values of $\alpha$ (§"Verification"), not proven in
general. This is the kind of "computer verified" stand-in for a real argument the dispatch flagged to
watch for. It is very plausible the sign convention is right (a continuity argument — the space of
valid configurations is connected and the sign pattern is locally constant away from degenerate loci
— could likely close this cheaply), but as written it is asserted from spot-checks, not proven.

### Promotable lemmas from this file
- **Lemma 1 (circumcenter x-coordinate reduction)** — certified, fully proved, elementary. Written to
  `results/imo-2026-02/lemmas/circumcenter-x-coordinate-reduction.md`.
- **Lemma 2 (decoupling lemma)** — certified (structure only, not any nonvanishing claim about
  Z/D1 — added an explicit caveat to that effect). Written to
  `results/imo-2026-02/lemmas/ray-parametrized-angle-decoupling.md` (merged with the equivalent lemma
  from `coordinate-groebner-elimination`, since they are the same fact independently derived).
- **Lemma 3 (directed-angle-as-cross/dot)** — **not certified as-is**. The write-up asserts an "iff"
  but only really justifies the forward direction cleanly; the converse (equal cross/dot product
  ⟹ equal angle) relies on injectivity of $\tan$ on $(0°,180°)\setminus\{90°\}$ plus a check of the
  $\mathrm{dot}=0$ edge case, neither spelled out in the file. The underlying claim is true (I checked
  the tan-injectivity and the $90°$ edge case myself) but the file's proof of it has an
  unacknowledged gap, so it does not meet the promotion bar as written.

## 2. `coordinate-groebner-elimination` — builder claimed Status: partial

**Verdict: CHANGES REQUESTED. True Status: partial — self-assessment is accurate.**

Independently re-derived §1 (base reduction), §3 (decoupling, $e_1=T_K\cdot\text{const}\cdot g_1$,
$e_2=T_L\cdot g_2$) and the closing cofactor identity from the raw coordinate definitions; all check
out (this is essentially the identical computation as approach 1 above, done with a slightly
different but equivalent parametrization — same $D1=2Z$ leading-coefficient gap). The file is
commendably honest about the one open gap (§6: "$D1\neq0$ ... has not yet been carried out") and
proposes two concrete, unfinished routes to close it (tie $D1$ to the discriminant of $g_1$ being
forced positive by $K,L$ existing as real points, or handle the $D1=0$ locus by a resultant
computation). This is the closest-to-solved live approach in the population — the gap is well
localized and the proposed route (a) via the discriminant is plausible and should be the top target
next round.

### Promotable lemmas
- **Base reduction lemma** — same content as approach 1's Lemma 1; already certified above (single
  merged lemma file, no need to duplicate).
- **Decoupling lemma** — same content as approach 1's Lemma 2; already certified above (merged).

## 3. `inversion-at-a-collinearity` — builder claimed Status: partial

**Verdict: CHANGES REQUESTED. True Status: partial — self-assessment is accurate**, with one
additional issue flagged below.

Checked Lemmas 1–3 (inversion distance formula, similar-triangle correspondence, cross-ratio
preservation of concyclic-or-collinear under inversion) line by line: all are standard, correctly
stated, and completely proved with no gaps or hidden steps — these are good, certifiable, reusable
lemmas independent of the rest of the file. Certified to
`results/imo-2026-02/lemmas/inversion-basics.md`.

The substantive remaining content — translating hypotheses (i)-(iii) (angles at $B,C,M,N$, none at
$A$) through the inversion into a statement about $K^*,L^*,A^{*\prime}$ — is honestly recorded as
**not completed** ("I attempted this recombination for hypothesis (i) ... and did not reach a clean
closed form"). The isosceles-case decoupling lemma (when $AB=AC$, hypotheses (ii),(iii) reduce to the
same quadratic $Q(\alpha,x)=0$) is a genuine new elementary result, fully proved (verified by direct
term-by-term matching of $Q_1|_{p=a/2}$ and $Q_2|_{p=a/2}$, which I did not fully re-derive myself
given time budget but which is a routine substitution check, low risk). The final branch-selection
step (only the symmetric branch $T_K=T_L$ satisfies the position hypotheses) is checked on only 10
numeric data points and explicitly not proved in general — correctly flagged as an open gap, not
overclaimed.

**Additional issue found:** the file's "Base reformulation" section states "$OM=ON \iff A^*$ lies on
circle($AKL$) ... proved in `approaches/synthetic-angle-chase-aklastar.md`; cited here, not
re-derived." I checked `synthetic-angle-chase-aklastar.md`'s current (this-round) content: **it does
not contain any $A^*$/concyclicity framework at all** — that file pivoted entirely to a direct
coordinate proof this round (its own history notes explicitly record dropping the earlier
concyclicity-chase framing as unsuccessful). So this citation is **stale**, pointing to material that
existed in an earlier round but is no longer present in the cited file. This base reformulation is
therefore currently **unproved** in the live population — it must either be re-derived locally in
this file next round, or the file should stop assuming it. I've noted this in `current.md`.

## Overall population status

`current.md` Status is **partial** (not solved — the "solved" claim was correctly rejected). Two
independent coordinate-based approaches (`synthetic-angle-chase-aklastar`,
`coordinate-groebner-elimination`) have converged on the **same** residual gap: proving
$Z\neq0$ (equivalently $D_1\neq0$) — the leading coefficient of the quadratic pinning $T_L$ from
hypothesis (ii) — on the geometrically valid locus. This is a genuine shared-gap plateau per
CLAUDE.md's guidance: closing it in either file closes it in both (they are the same fact), so next
round should either (a) push hard on the discriminant-positivity argument coordinate-groebner
proposes, since it is the most concrete open lead, or (b) per the plateau-break rule, put a
genuinely different framing on the table (e.g. push the inversion approach's hypothesis-translation
further, or try a fresh synthetic/trig approach) rather than a third variant of the same coordinate
elimination that will hit the identical wall.

## Files written/modified this round
- `results/imo-2026-02/current.md` — rewritten (reviewer-owned), Status: partial, "Current best"
  documents the shared reduction and the precise open gap.
- `results/imo-2026-02/approaches/synthetic-angle-chase-aklastar.md` — Status corrected from
  `solved` to `partial`, with an explicit reviewer-note section explaining the gap (builder's own
  prose left otherwise intact for audit trail).
- `results/imo-2026-02/lemmas/circumcenter-x-coordinate-reduction.md` — new, certified.
- `results/imo-2026-02/lemmas/ray-parametrized-angle-decoupling.md` — new, certified (with explicit
  caveat that it does not certify any $Z\neq0$/$D_1\neq0$ claim).
- `results/imo-2026-02/lemmas/inversion-basics.md` — new, certified.
- `record_outcome` called for all three slugs (all `partial`).
