from fractions import Fraction as F
import random

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def rand_sorted(m, denom=10000):
    vals = sorted((random.randint(1, denom) for _ in range(m)), reverse=True)
    # ensure strictly decreasing (resample on collision, small chance)
    while len(set(vals)) < m:
        vals = sorted((random.randint(1, denom) for _ in range(m)), reverse=True)
    return [F(v, 1) for v in vals]  # keep as raw ints scaled by 1 (sum not normalized, fine for identity check)

def test_sandwich(trials=20000):
    random.seed(1)
    fails = 0
    checked = 0
    for _ in range(trials):
        m = random.choice([3,5,7])
        tail = rand_sorted(m-1)  # p2..pm as fractions, strictly decreasing
        p2 = tail[0]; pm = tail[-1]
        # choose p1 with p1 < p2 + pm  and p1 >= p2 (p1 must be the max)
        # also need p1 > pm (obviously, plus need feasibility interval nonempty:
        # max(p3, p1-pm) < p2  <=> p1 < p2+pm (since p3<p2 always true here)
        lo = p2
        hi = p2 + pm
        if hi <= lo:
            continue
        # sample p1 in (lo, hi) strictly, as a fraction
        # pick random rational strictly between lo and hi
        t = F(random.randint(1, 999), 1000)
        p1 = lo + t*(hi-lo)
        if p1 <= lo or p1 >= hi:
            continue
        A = [p1] + tail
        assert all(A[i] >= A[i+1] for i in range(len(A)-1)), (A,)
        # feasibility x range: (max(p3, p1-pm), p2)
        p3 = tail[1]
        xlo = max(p3, p1-pm)
        xhi = p2
        if xhi <= xlo:
            continue
        # pick x strictly inside
        s = F(random.randint(1,999),1000)
        x = xlo + s*(xhi-xlo)
        y = p1 - x
        # sanity: verify order p2 > x > p3 > ... > pm > y > 0
        newlist = [p2, x] + tail[1:] + [y]
        assert newlist[0] > newlist[1] > newlist[2], (newlist,)
        for i in range(len(newlist)-1):
            if not (newlist[i] >= newlist[i+1]):
                # allow equality only among tail internal (shouldn't happen, strictly decreasing sampled)
                raise AssertionError((newlist,i))
        B = [x, y] + tail  # full multiset after split (p1 replaced by x,y; tail p2..pm unchanged)
        got = oddrank(B)
        m_full = len(tail)+1  # = m
        OS = sum(tail[i] for i in range(1, len(tail), 2))  # tail indices: tail[0]=p2,...; want p3,p5,... i.e. tail[1],tail[3],...
        expected = p2 + OS
        checked += 1
        if got != expected:
            fails += 1
            print("MISMATCH", A, x, y, got, expected)
    print(f"checked={checked} fails={fails}")

test_sandwich(30000)
