## Status
unsolved (R15 GATED PROBE — GATE RETURNED **NO**, decisively. The two-band Z-transform recursion
does NOT exist: it reduces to a clean recursion in $Z_{n-1}(-1)$ only when there is no $F$-fragment
inside the bottom band, i.e. essentially the already-closed $|F|=2$ case; on the OPEN $|F|\ge3$
domain the deviation from a clean recursion is EXACTLY the certified dead SPLIT cross-term
$\mu(O_F\cap O_B)$ that Lemma MID was built to eliminate. This is a **7th dead lower lever** — the
transform object. No fake proof. Retire the recursion mechanism.)

## Approach: gen-func-transform (framing G — a global Z-transform of the parity-measure, evaluated at z = −1)

Target (the whole claim): for every positive integer $n$, the largest $c$ Liu can guarantee is
$$c(n)=\frac{2^n}{2^{n+1}-1},\qquad\text{equivalently minimax }D=u_n=\frac1{2^{n+1}-1}.$$
This slug attacked the LOWER wall (Liu plays the ladder $C_n$; every Xiang $\le n$-cut refinement has
$D\ge1$ ⟺ GAP MID-core $\mu\{g\text{ odd}\}\ge1$), which after R14 had NO live vehicle.

### The transform (certified-fact restatement — NOT new content)

Certified MID setting (`lemmas/mass-difference-reduction.md`): $g=N_F-N_B$ on $(0,L)$, $L=2^{n-1}$,
integer step function with $\int_0^L g=1$ (MID b) and $D(S)=\mu\{g\text{ odd}\}$ (MID a). Define
$$Z(z):=\int_0^L z^{\,g(t)}\,dt.$$
Direct evaluation gives $Z(1)=L$, $Z'(1)=\int g=1$, and — via the character
$\mathbf1[g\text{ odd}]=(1-(-1)^g)/2$ — $Z(-1)=L-2\mu\{g\text{ odd}\}$. So GAP MID-core is EXACTLY
$$Z(-1)\le L-2.$$
(Roots-of-unity/character filter, crux analogue aimo-0155.) **Confirmed exactly** (`sympy`/`Fraction`)
on all witnesses: $Z(-1)=L-2\mu\{g\text{ odd}\}$ and $\int g=1$ hold identically. **But this identity
is Lemma MID rewritten — by itself it closes nothing.** The entire value of the slug rested on the
gate below.

### THE GATE — result: **NO** (decisive refutation, exact arithmetic)

By certified ONE-REC/TB, $B=F_B\sqcup B_B$: $F_B$ = fragments of the top piece $2^{n-1}$ of $C_{n-1}$
($\Sigma F_B=L$), $B_B$ a refinement of $C_{n-2}$ confined to $(0,L/2)$. Two-band structure: on
$(L/2,L)$, $g=N_F-N_{F_B}$; on $(0,L/2)$, $g=(N_F-N_{F_B})-N_{B_B}$.

**Exact two-band decomposition (VERIFIED identity, holds always).** Writing the level-$(n-1)$
sub-instance transform $Z_{n-1}(-1):=\int_0^{L/2}(-1)^{g'}$ with $g'=N_{F_B}-N_{B_B}$, one has on the
bottom band $(-1)^{g}=(-1)^{N_F}\,(-1)^{g'}$ (since $g-g'=N_F-2N_{F_B}\equiv N_F\pmod2$). Hence
$$Z_n(-1)=\underbrace{\int_{L/2}^{L}(-1)^{N_F-N_{F_B}}}_{\text{TopBand}(F,F_B)}
+\underbrace{\int_0^{L/2}(-1)^{N_F(t)}\,(-1)^{g'(t)}\,dt}_{\text{BottomBand}}.$$
Verified exactly at $n=3,4$ on $F=\{8,5,3\},\{6,6,4\},\{8,8\},\{4,3,1\}$: LHS $=$ TopBand $+$
BottomBand every time.

**The obstruction (this is the whole refutation).** BottomBand carries the weight
$w(t)=(-1)^{N_F(t)}$ INSIDE the sub-instance domain $(0,L/2)$. Subtracting the clean sub-value,
$$\boxed{\,Z_n(-1)-\big[\text{TopBand}+Z_{n-1}(-1)\big]
=\int_0^{L/2}\!\big[(-1)^{N_F}-1\big](-1)^{g'}
=-2\!\!\int_{O_F\cap(0,L/2)}\!\!(-1)^{g'}\,dt\,,}$$
where $O_F=\{t:N_F(t)\text{ odd}\}$. This deviation is EXACTLY $-2$ times the signed overlap of $O_F$
with the sub-configuration on the bottom band — i.e. the **certified SPLIT cross-term
$\mu(O_F\cap O_B)$** (`lemmas/split-cross-term.md`) that Lemma MID was constructed to ELIMINATE.
**Verified exactly**: for $F=\{8,5,3\}$ the deviation is $-2$; $F=\{6,6,4\}$: $-4$; tight
$\{8,8,4,4,3,2,1,1\}$: $0$; $n=3\ F=\{4,3,1\}$: $-2$ — each equalling $-2\int_{O_F}(-1)^{g'}$ on the
nose.

**When (and only when) is the recursion clean?** $w(t)$ is constant on $(0,L/2)$ **iff $F$ has no
fragment strictly below $L/2=2^{n-2}$** (then $N_F\equiv|F|$ there, so $w\equiv(-1)^{|F|}$ and
$Z_n(-1)=\text{TopBand}+(-1)^{|F|}Z_{n-1}(-1)$, a genuine recursion). Verified: $\{8,8\}$, $\{6,6,4\}$
have constant weight; $\{8,5,3\}$, $\{5,5,4,2\}$ (an $F$-fragment $<L/2$) do NOT. The "no small
fragment" case is essentially the $|F|=2$ case already closed inside MID; the OPEN residual is
$|F|\ge3$ WITH an interior fragment, and there the weight flips.

**Decisive collision (exact, cut-budget-respecting, $n=4$, $B$ uses $\le n-1=3$ cuts).** Fix the
top-level data $F=\{8,5,3\}$, $F_B=\{4,4\}$ (so TopBand $=-2$ is fixed). Three admissible $B_B$
(refinements of $C_2=\{1,2,4\}$) all give the SAME sub-value $Z_{n-1}(-1)=0$ but DIFFERENT $Z_4(-1)$:

| $B_B$ (by provenance $4\!\to,\ 2\!\to,\ 1\!\to$) | $B$ cuts | BottomBand | $Z_4(-1)$ |
|---|---|---|---|
| $4;\ 2;\ \tfrac12,\tfrac12$ | 2 | $-2$ | $-4$ |
| $\tfrac12,\tfrac72;\ 2;\ \tfrac12,\tfrac12$ | 3 | $0$ | $-2$ |
| $\tfrac12,\tfrac12,3;\ 2;\ 1$ | 3 | $+2$ | $0$ |

Identical $(F,F_B,Z_{n-1}(-1))$ produce three distinct $Z_n(-1)$. Therefore $Z_n(-1)$ is **not a
function of the top-level data together with $Z_{n-1}(-1)$**: no clean recursion carrying the scalar
IH $Z_{n-1}(-1)\le L/2-2$ exists. $\blacksquare$(gate)

**Diagnosis (why it collapses to repackaging).** To bound $Z_n(-1)$ from a two-band split one must
control the deviation $-2\int_{O_F\cap(0,L/2)}(-1)^{g'}$, whose value depends on the DETAILED
placement of the sub-instance's odd-set relative to $O_F$ — precisely the SPLIT cross-term. The
Z-transform does NOT linearize this term; evaluating at $z=-1$ reintroduces exactly the object
$\mu(O_F\cap O_B)$ that MID removed. This is the same "reframing, not reduction" fate as the
vertex-polytope (R14) and LP-dual reframings: the transform is a new NOTATION for MID, not a new
reduction. It matches the R15 genfunc explorer's own prediction and the outline-reviewer's
independent prediction (bottom-band integrand factors cleanly only if $h=N_F-N_{F_B}$ is trivial on
the bottom band, which it generically is not).

## Approaches tried
- (round 15, registered) gen-func-transform: opened as a gated escalation probe. Z-transform
  $Z(z)=\int z^{g}$, $Z(-1)=L-2\mu\{g\text{ odd}\}$ makes MID-core the single evaluation
  $Z(-1)\le L-2$ (roots-of-unity filter, aimo-0155). Core identity certified-MID repackaging.
- (round 15, GATE RUN) Two-band recursion for $Z_n(-1)$ via ONE-REC/TB: **REFUTED, decisive.**
  Exact `sympy`/`Fraction` at $n=3,4$ (incl. mandated tight $\{8,8,4,4,3,2,1,1\}$ and cross-group
  $F=\{6,6,4\}$). The bottom band carries the weight $(-1)^{N_F(t)}$; the deviation from a clean
  recursion equals $-2\int_{O_F\cap(0,L/2)}(-1)^{g'}$ = the certified dead SPLIT cross-term
  $\mu(O_F\cap O_B)$. Cut-budget-respecting collision: identical $(F=\{8,5,3\},F_B=\{4,4\},
  Z_{n-1}(-1)=0)$ yield three distinct $Z_4(-1)\in\{-4,-2,0\}$ ⇒ $Z_n(-1)$ is not a function of
  top-level data $+$ $Z_{n-1}(-1)$; no IH-carrying recursion exists. Clean recursion holds ONLY when
  $F$ has no fragment $<L/2$ (essentially the closed $|F|=2$ case), never on the open $|F|\ge3$
  interior. Outcome: **7th dead lower lever (the transform object)**; the transform is a repackaging
  of certified MID, not a reduction. Retire the recursion mechanism.

## Current best
No new progress toward GAP MID-core. The transform identity $Z(-1)=L-2\mu\{g\text{ odd}\}$ (⟺
MID-core is $Z(-1)\le L-2$) is an exact restatement of certified Lemmas M + MID and closes nothing.
The two-band recursion — the slug's entire non-repackaging content — is REFUTED: $Z_n(-1)$ is not
determined by $(F,F_B,Z_{n-1}(-1))$; the obstruction is precisely the certified dead SPLIT cross-term
$\mu(O_F\cap O_B)$, so the Z-transform re-imports the very term MID was built to remove. The LOWER
wall remains without a live vehicle; the transform object joins the six exhausted lower families
(scalar-reserve, structured-matching, prefix/termwise monovariant, f-partition, vertex-polytope/LP-dual,
merge/budget-domination). A correct lower argument must control the $O_F$-vs-sub-configuration overlap
GLOBALLY (the shared Gap-Interleaving exchange, same DNA as the upper $L^\star$/GAP-U wall) — no
scalar transform of the static parity-measure can do it.

## Full proof
Not present — Status is unsolved (gate returned NO; no proof).

## Promotable lemmas
None. The only exact identity established this round — the two-band decomposition
$Z_n(-1)=\text{TopBand}+\int_0^{L/2}(-1)^{N_F}(-1)^{g'}$ with deviation
$-2\int_{O_F\cap(0,L/2)}(-1)^{g'}$ — is a straightforward re-expression of certified TB + split-cross-term
and is not reusable as new content. Its value is entirely diagnostic: it is the explicit obstruction
proving the transform recursion is a repackaging of the dead cross-term, recorded so no agent retries
a Z-transform / generating-function recursion on the LOWER wall.
