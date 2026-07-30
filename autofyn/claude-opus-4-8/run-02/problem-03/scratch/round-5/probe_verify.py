import random
exec(open('/tmp/round-5/probe_runcase.py').read().split("rng = random.Random(1)")[0])

def altsum_direct(parts):
    # D via level measure: integrate 1[N(t) odd] over t
    # equivalent to altsum of sorted descending list
    s=sorted(parts, reverse=True)
    tot=0; sign=1
    for v in s:
        tot+=sign*v; sign=-sign
    return tot

rng=random.Random(7)
n=5
worst=None
for trial in range(30000):
    a = rng.randint(1, n-1)
    b = rng.randint(0, n-a)
    Y = gen_Y(n, a, rng)
    Z, anchors, cutcounts = gen_Z(n, b, rng)
    F = Y+Z
    Ddirect = altsum_direct(F)
    maxc, deficit, surplus, Dtilde_formula = compute_run_stats(Y,Z)
    diff = abs(Ddirect - Dtilde_formula)
    if worst is None or Ddirect < worst[0]:
        worst = (Ddirect, Dtilde_formula, maxc, a, b, sum(Y), sum(Z))
print("min Ddirect over trials:", worst)
