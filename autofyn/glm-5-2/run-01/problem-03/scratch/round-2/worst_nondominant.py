import numpy as np
from itertools import product
from fractions import Fraction

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

# ---------------------------------------------------------------
# PART 3: Worst NON-DOMINANT config (L < 2*a_2) for small n.
# Two notions of "non-dominant":
#   (ND-parity) L < 2*a_2  =>  halving L does NOT give a clean parity cancellation
#   (ND-arith)  L < 2^n/D_n =>  the arithmetic factorization R/D_{n-1} > 1/D_n
# We want the config maximizing D (the UNMARKED alternating sum, i.e. Xiang marks nothing)
# subject to the non-dominant constraint, and see if Xiang can cap it with marks.
# Note: D is what Xiang wants to MINIMIZE. "Worst" = hardest for Xiang = largest D that
#   forces Xiang to act.
# But really we want: for configs in the non-dominant zone, can Xiang (with n marks)
# force D <= 1/D_n? And what's the worst starting D?
# ---------------------------------------------------------------

# First: relationship between the two thresholds.
# ND-arith: L < 2^n/D_n.
# For the parity split to fail we need L < 2*a_2.
# If L >= 2*a_2 AND L >= 2^n/D_n: full dominant (clean).
# If L >= 2*a_2 but L < 2^n/D_n: parity clean but arithmetic fails (R too big).
#   => halving gives D(rest), but rest total R > (2^n-1)/D_n, induction overshoots.
#   This is a SEPARATE sub-case! Let's call it "parity-clean-but-R-too-big".
# If L < 2*a_2: parity fails regardless of L vs 2^n/D_n. Pure non-dominant.

# The orchestrator conflates these. Let's separate.

# Sub-case X: L >= 2*a_2 (parity clean) but L < 2^n/D_n (arithmetic fails).
# Then D(total after halving) = D(rest) <= R/D_{n-1}, R = 1-L > (2^n-1)/D_n.
# So D(rest) <= R/D_{n-1} but R/D_{n-1} > 1/D_n. Induction alone overshoots.
# Need: either a sharper induction, or use the parity structure of THIS rest.
# Question: in this sub-case, is the rest itself "dominant" (its own largest piece small)?
# The rest's largest = a_2 <= L/2 < 2^n/(2*D_n) = 2^{n-1}/D_n.
# Rest has <= n pieces, total R. For the (n-1)-game target is R/D_{n-1}.
# We need to beat the induction: force D(rest) < R/D_{n-1} down to 1/D_n.
# Since R < 1 (always) and D_{n-1} = 2^n-1, R/D_{n-1} vs 1/D_n:
#   need D(rest) <= 1/D_n but induction gives <= R/D_{n-1} > 1/D_n. GAP = R/D_{n-1} - 1/D_n.
# Compute the gap size: R/D_{n-1} - 1/D_n = (R*D_n - D_{n-1})/(D_{n-1}*D_n).
# At R = (2^n-1)/D_n + eps (just above the threshold), gap = (R*D_n - (2^n-1))/(D_{n-1}*D_n)
#   = (R*D_n - D_{n-1})/(D_{n-1}*D_n). Small near threshold.

# Let's find the worst UNMARKED D in the non-dominant (parity) zone L < 2*a_2.
# Worst unmarked D = config maximizing D(a) subject to a_1 < 2*a_2, sum=1, <= n+1 pieces.
# For m pieces all nearly equal to 1/m: D = a_1 - a_2 + a_3 - ... 
# If all equal: D=0 (even m) or D=1/m (odd m).
# To MAXIMIZE D with a_1 < 2*a_2: want a_1 large, a_2 >= a_1/2, and alternating sum large.
# Conjecture worst: "two big equal + tail" = (L, L, small...) i.e. a_1=a_2=L, tail=1-2L.
# Then D = L - L + tail_stuff... = D(tail) + 0. Hmm if tail is tiny that's small.
# Actually: D = a_1 - a_2 + a_3 - ... If a_1 = a_2 = L, those cancel. Then D = a_3 - a_4 +...
# To maximize D overall with a_1<2*a_2: make a_1 big, a_2 = a_1/2 (boundary), maximize a_1.
# Then a_3,... contribute. With a_1 = 2*a_2, a_2 = a_1/2: D = a_1 - a_1/2 + (a_3 - ...) = a_1/2 + D(tail).
# Sum constraint: a_1 + a_1/2 + tail = 1 => tail = 1 - 3a_1/2.
# To maximize a_1 (and hence a_1/2 term) we minimize tail => tail -> 0 => a_1 -> 2/3.
# At a_1 = 2/3, a_2 = 1/3, tail=0: config (2/3, 1/3), D = 2/3 - 1/3 = 1/3.
# But a_1 = 2/3 = 2*a_2 => this is the BOUNDARY (dominant, equality). 
# So approaching the boundary from the non-dominant side: D -> 1/3 = 1/D_1.
# For general n, target 1/D_n. The unmarked D can be as large as ~1/3 >> 1/D_n for n>=2.
# So "mark nothing" is WAY too weak in the non-dominant zone for n>=2. Confirmed.

# Let's compute: for n=2,3,4, the worst unmarked D with L < 2*a_2 (and <= n+1 pieces).
# We'll grid-search over configs.
def worst_unmarked_D(n, grid=200, num_pieces_options=None):
    """Maximize D(a) s.t. sum=1, len(a)<=n+1, a sorted desc, a_1 < 2*a_2."""
    if num_pieces_options is None:
        num_pieces_options = list(range(2, n+2))  # 2..n+1 pieces
    best_D = -1
    best_config = None
    Dn = 2**(n+1)-1
    target = 1.0/Dn
    for m in num_pieces_options:
        # grid search m pieces on simplex, sorted desc
        # use random sampling for speed
        rng = np.random.default_rng(7)
        for _ in range(50000):
            a = np.sort(rng.dirichlet(np.ones(m)))[::-1]
            if a[0] >= 2*a[1]:
                continue  # dominant, skip
            d = D_alt(a)
            if d > best_D:
                best_D = d
                best_config = a.copy()
    return best_D, best_config, target

for n in [2,3,4]:
    bd, bc, tgt = worst_unmarked_D(n)
    Dn = 2**(n+1)-1
    print(f"n={n}: worst unmarked D (L<2a2) = {bd:.6f}, target 1/D_n = {tgt:.6f}, ratio={bd/tgt:.2f}x, config={np.round(bc,4)}")
