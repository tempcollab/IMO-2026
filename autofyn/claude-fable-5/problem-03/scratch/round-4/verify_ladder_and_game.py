import numpy as np, itertools, random
from scipy.optimize import minimize
from fractions import Fraction as F

def delta_np(pieces):
    s = np.sort(pieces)[::-1]
    signs = np.array([1 if i % 2 == 0 else -1 for i in range(len(s))])
    return float(np.dot(s, signs))

# ---- attack the ladder lower bound: min over ALL Xiang cut allocations, n=1..3 ----
for n in (1, 2, 3):
    u = 1.0 / (2**(n+1) - 1)
    rungs = [2**k * u for k in range(n, -1, -1)]
    best = np.inf
    # allocate c_k cuts to rung k, sum <= n
    for alloc in itertools.product(range(n+1), repeat=n+1):
        C = sum(alloc)
        if C > n:
            continue
        # variables: for rung k with c cuts, c interior positions -> fragments
        def frags(x):
            out = []
            idx = 0
            for k, c in enumerate(alloc):
                L = rungs[k]
                if c == 0:
                    out.append(L)
                else:
                    cuts = np.sort(np.clip(x[idx:idx+c], 1e-9, L-1e-9)) * 0 + np.sort(L * (1/(1+np.exp(-x[idx:idx+c]))))
                    idx += c
                    prev = 0.0
                    for t in cuts:
                        out.append(t - prev); prev = t
                    out.append(L - prev)
            return np.array(out)
        nv = C
        if nv == 0:
            val = delta_np(np.array(rungs))
            best = min(best, val)
            continue
        for seed in range(12):
            rng = np.random.default_rng(1000*seed + C)
            x0 = rng.normal(size=nv)
            r = minimize(lambda x: delta_np(frags(x)), x0, method='Nelder-Mead',
                         options={'maxiter': 4000, 'xatol': 1e-12, 'fatol': 1e-14})
            best = min(best, r.fun)
    print(f"n={n}: min Delta over Xiang replies = {best:.10f}  (u = {u:.10f})  ok={best >= u - 1e-7}")

# ---- end-to-end upper bound spot check: random Liu partitions, n up to 5,
#      Xiang uses the U(n+1) strategy (independent implementation in verify_um) ----
import importlib.util
spec = importlib.util.spec_from_file_location("vu", "/tmp/round-4/verify_um.py.mod")
# instead re-import by exec of the functions only
src = open("/tmp/round-4/verify_um.py").read().split("random.seed")[0]
ns = {}
exec(src, ns)
run_U = ns['run_U']

random.seed(7)
worst = F(0)
for trial in range(400):
    n = random.randint(1, 5)
    k = random.randint(1, n+1)
    parts = [F(random.randint(1, 60)) for _ in range(k)]
    T = sum(parts)
    a = [p / T for p in parts] + [F(0)] * (n + 1 - k)  # padded to n+1, total 1
    u = F(1, 2**(n+1) - 1)
    d, c = run_U(a)
    assert c <= n, (n, a, c)
    assert d <= u, (n, a, d, u)
print("end-to-end: 400 random Liu partitions, n=1..5: all replies legal (cuts<=n) and Delta<=u. OK")

# claiming game brute force vs odd(S), small random multisets (re-check Lemma G)
import functools
def game_value(ms):
    ms = tuple(sorted(ms, reverse=True))
    @functools.lru_cache(maxsize=None)
    def rec(rem):
        if not rem:
            return F(0)
        best = None
        for i in range(len(rem)):
            nxt = rem[:i] + rem[i+1:]
            v = rem[i] + (sum(nxt) - rec(nxt))
            if best is None or v > best:
                best = v
        return best
    return rec(ms)

random.seed(99)
for _ in range(60):
    m = random.randint(1, 7)
    ms = [F(random.randint(0, 6)) for _ in range(m)]
    s = sorted(ms, reverse=True)
    odd = sum(s[0::2])
    assert game_value(ms) == odd, (ms, game_value(ms), odd)
print("Lemma G re-check: 60 random multisets, game value == odd(S). OK")
