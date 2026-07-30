import numpy as np
from scipy.optimize import minimize
from fractions import Fraction as F

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

A = [26.0, 21.0, 10.0]

# Pattern (b): two different pieces each split once. Choose which 2 of the 3 pieces to split,
# and split ratio x in (0,1) for each -> piece*x, piece*(1-x)
best = None
import itertools
for pair in itertools.combinations(range(3), 2):
    def negval(xs, pair=pair):
        pieces = list(A)
        x1, x2 = xs
        i, j = pair
        # replace piece i with two parts, piece j with two parts
        vals = []
        for k in range(3):
            if k == i:
                vals += [A[k]*x1, A[k]*(1-x1)]
            elif k == j:
                vals += [A[k]*x2, A[k]*(1-x2)]
            else:
                vals += [A[k]]
        return oddrank(vals)
    # grid search + refine
    best_local = None
    for x1 in np.linspace(0.001,0.999,60):
        for x2 in np.linspace(0.001,0.999,60):
            v = negval([x1,x2])
            if best_local is None or v < best_local[0]:
                best_local = (v, x1, x2)
    # refine with Nelder-Mead
    res = minimize(negval, [best_local[1], best_local[2]], method='Nelder-Mead')
    v2 = negval(res.x)
    if best is None or min(best_local[0], v2) < best[0]:
        best = (min(best_local[0], v2), pair, best_local, res.x)
    print("pair", pair, "grid best", best_local[0], "refined", v2)

print("Pattern (b) overall best:", best[0])

# Pattern (a): one piece split into 3 parts (2 cuts on same piece)
best_a = None
for idx in range(3):
    def negval(xs, idx=idx):
        x1, x2 = xs  # split piece into x1, x2, 1-x1-x2 fractions (must be positive)
        if x1<=0 or x2<=0 or x1+x2>=1:
            return 1e9
        vals = []
        for k in range(3):
            if k == idx:
                vals += [A[k]*x1, A[k]*x2, A[k]*(1-x1-x2)]
            else:
                vals += [A[k]]
        return oddrank(vals)
    best_local=None
    for x1 in np.linspace(0.01,0.98,40):
        for x2 in np.linspace(0.01,0.98,40):
            if x1+x2>=1: continue
            v=negval([x1,x2])
            if best_local is None or v<best_local[0]:
                best_local=(v,x1,x2)
    res=minimize(negval,[best_local[1],best_local[2]],method='Nelder-Mead')
    v2=negval(res.x)
    print("piece",idx,"grid best",best_local[0],"refined",v2)
    if best_a is None or min(best_local[0],v2)<best_a[0]:
        best_a=(min(best_local[0],v2), idx, res.x)

print("Pattern (a) overall best:", best_a[0])
print()
print("TRUE 2-mark optimum (min over both patterns):", min(best[0], best_a[0]))
print("Sigma/2 =", 28.5, " Round-12 recursion claims:", 28.5)
print("Exact-tie builder claims true 2-mark value = 31")
