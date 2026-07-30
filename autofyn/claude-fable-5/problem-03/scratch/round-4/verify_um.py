import random, itertools
from fractions import Fraction as F

# ---------- Independent implementation of the U(m) strategy per the proof ----------
# Moves operate on an active list; we track retired pieces to reconstruct final multiset S.

def delta(ms):
    s = sorted(ms, reverse=True)
    return sum(v if i % 2 == 0 else -v for i, v in enumerate(s))

def lemmaB_split(a, beta):
    """Exhaustive search: disjoint nonempty P,N with |sum P - sum N| <= beta.
    Returns (P_idx, N_idx) or None."""
    m = len(a)
    best = None
    for assign in itertools.product((0, 1, -1), repeat=m):
        P = [i for i in range(m) if assign[i] == 1]
        N = [i for i in range(m) if assign[i] == -1]
        if not P or not N:
            continue
        d = sum(a[i] for i in P) - sum(a[i] for i in N)
        if abs(d) <= beta:
            return P, N
    return None

def run_U(a):
    """Execute the proof's strategy on multiset a. Returns (delta_final, cuts_used).
    Asserts every move legality and the invariants."""
    m = len(a)
    T = sum(a)
    beta = F(T, 2**m - 1) if T != 0 else F(0)
    if T == 0:
        return delta(a), 0

    active = list(a)   # active pieces
    retired = []       # retired pieces (must come in exactly tied pairs)
    cuts = 0

    def bisect(x):
        nonlocal cuts
        assert x > 0 and x in active
        active.remove(x)
        retired.extend([x / 2, x / 2])
        cuts += 1

    def match(L, S):
        # cut L at distance S: retire {S(sub), S(old)}, active gains L-S
        nonlocal cuts
        assert L > S > 0 and L in active and S in active
        active.remove(L); active.remove(S)
        retired.extend([S, S])
        active.append(L - S)
        cuts += 1
        return L - S

    def freeretire(x):
        assert active.count(x) >= 2 and x > 0
        active.remove(x); active.remove(x)
        retired.extend([x, x])

    # Branch 1
    small = [x for x in a if x <= beta]
    if small:
        keep = min(a)
        removed_keep = False
        for x in list(active):
            if x == keep and not removed_keep:
                removed_keep = True
                continue
            if x > 0:
                bisect(x)
        A_end = active
    else:
        # Branch 2: all > beta
        split = lemmaB_split(a, beta)
        assert split is not None, f"Lemma B FAILS on {a}"
        Pi, Ni = split
        P = [a[i] for i in Pi]; N = [a[i] for i in Ni]
        if sum(P) < sum(N):
            P, N = N, P
        s = sum(P) - sum(N)
        assert 0 <= s <= beta
        Pp, Np = list(P), list(N)
        consumed = 0
        q = F(0)
        carrier = None  # length must equal |q| when q != 0
        while True:
            if q == 0:
                if not Pp:
                    assert not Np, f"state2 reached: {a}"
                    break
                x = Pp.pop()
                carrier = x  # designation, 0 cuts
                q = x
                consumed += 1
                continue
            if q > 0:
                if not Np:
                    # state 3 stop
                    assert (Pp and 0 < q < s) or (not Pp and q == s)
                    assert q <= beta
                    break
                y = Np.pop()
                consumed += 1
                assert carrier == q
                if y < q:
                    carrier = match(carrier, y)
                    q = q - y
                elif y > q:
                    carrier = match(y, carrier)
                    q = q - y
                    assert carrier == -q
                else:
                    freeretire(carrier)
                    carrier = None
                    q = F(0)
            else:  # q < 0
                assert Pp, f"state1 reached: {a}"
                x = Pp.pop()
                consumed += 1
                assert carrier == -q
                if x < -q:
                    carrier = match(carrier, x)
                    q = q + x
                elif x > -q:
                    carrier = match(x, carrier)
                    q = q + x
                    assert carrier == q
                else:
                    freeretire(carrier)
                    carrier = None
                    q = F(0)
        # endgame: bisect all unconsumed (Pp and Z)
        for x in Pp + [a[i] for i in range(m) if i not in Pi and i not in Ni]:
            bisect(x)
        A_end = active
        assert len(A_end) <= 1

    d_end = delta(A_end)
    # sanity: final multiset S = retired + A_end must satisfy Delta(S) == Delta(A_end)
    S = retired + A_end
    assert delta(S) == d_end, (a, S, A_end)
    # retired pieces pair up exactly
    rs = sorted(retired)
    assert len(rs) % 2 == 0 and all(rs[2*i] == rs[2*i+1] for i in range(len(rs)//2))
    return d_end, cuts

def rand_instance(m, style):
    if style == 0:
        return [F(random.randint(1, 50)) for _ in range(m)]
    if style == 1:  # with ties
        vals = [F(random.randint(1, 8)) for _ in range(m)]
        return vals
    if style == 2:  # with zeros
        return [F(random.randint(0, 20)) for _ in range(m)]
    if style == 3:  # ladder-like
        return sorted([F(2**k) + F(random.randint(-1,1), 7) for k in range(m)], reverse=True)
    if style == 4:  # rationals
        return [F(random.randint(1, 40), random.randint(1, 9)) for _ in range(m)]
    if style == 5:  # near-equal (all > beta regime, forces Branch 2)
        base = random.randint(10, 30)
        return [F(base + random.randint(0, 3)) for _ in range(m)]

random.seed(20260728)
fails = 0
tested = 0
branch2 = 0
for m in range(1, 9):
    for trial in range(600):
        a = rand_instance(m, trial % 6)
        T = sum(a)
        beta = F(T, 2**m - 1) if T else F(0)
        if T > 0 and all(x > beta for x in a):
            branch2 += 1
        d, c = run_U(a)
        tested += 1
        if not (d <= beta and c <= m - 1):
            fails += 1
            print("FAIL", m, a, d, beta, c)
print(f"tested={tested} branch2_instances={branch2} fails={fails}")

# tight ladder check
for m in range(1, 8):
    a = [F(2**k) for k in range(m)]
    T = sum(a); beta = F(T, 2**m-1)
    d, c = run_U(a)
    assert d <= beta and c <= m-1
    print(f"ladder m={m}: delta={d} beta={beta} cuts={c} (tight iff equal: {d==beta})")

# greedy-killer
a = [F(5), F(3), F(3), F(2)]
d, c = run_U(a)
print("greedy-killer (5,3,3,2): delta =", d, "beta =", F(13, 15), "cuts =", c)
