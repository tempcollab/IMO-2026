from explore import *
from scipy.optimize import differential_evolution

def multi_halve_value(p, budget, depth=0):
    # try halving the first K pieces simultaneously, K=1..len(p)
    m = len(p)
    best = None
    for K in range(1, min(m, budget)+1):
        if K < m and p[K-1] < 2*p[K] - 1e-15:
            continue
        cost = K
        if cost > budget:
            continue
        halved_sum = sum(p[i]/2 for i in range(K))
        tail = p[K:]
        leftover = budget - cost
        if len(tail) == 0:
            tail_val = 0.0
        else:
            tail_val = menu_best(tail, leftover, depth+1) if leftover > 0 else oddrank(list(tail))
        val = halved_sum + tail_val
        if best is None or val < best:
            best = val
    return best

def residual_refine_value(fixed_list, r, extra_marks, seed=0):
    # fixed_list: list of floats (already-fixed pieces), r: value to be split into extra_marks+1 parts
    # search over cut positions in [0,r] to minimize oddrank(fixed_list + fragments)
    if extra_marks == 0:
        return oddrank(fixed_list + [r])
    def obj(x):
        rs = sorted(x)
        prev = 0.0
        frags = []
        for cv in rs:
            v = cv*r
            frags.append(v - prev)
            prev = v
        frags.append(r - prev)
        return oddrank(fixed_list + frags)
    bounds = [(0,1)]*extra_marks
    res = differential_evolution(obj, bounds, popsize=20, maxiter=80, tol=1e-11, seed=seed, polish=True)
    return res.fun

def partial_dom_residual_menu(p, budget):
    m = len(p)
    best = None
    for j in range(0, min(budget, m-1)+1):
        Sj = sum(p[1:1+j])
        if p[0] < Sj - 1e-15:
            continue
        r = p[0] - Sj
        extra = budget - j
        fixed = list(p[1:1+j]) + list(p[1:])  # duplicated prefix + full untouched tail
        if extra == 0:
            val = oddrank(fixed + [r])
        else:
            val = residual_refine_value(fixed, r, min(extra, 3))
        if best is None or val < best:
            best = val
    return best

def full_menu_best(p, budget):
    p = tuple(sorted(p, reverse=True))
    vals = [menu_best(p, budget)]
    mh = multi_halve_value(p, budget)
    if mh is not None: vals.append(mh)
    pdr = partial_dom_residual_menu(p, budget)
    if pdr is not None: vals.append(pdr)
    ext_best, _ = extended_tie_search(p, budget)
    vals.append(ext_best)
    return min(vals)

def run_sweep2(m, n_samples, seed0=0):
    budget = m - 1
    target = c_of_n(budget)
    results = []
    for s in range(n_samples):
        p = random_config(m, seed0+s)
        fm = full_menu_best(p, budget)
        results.append((p, fm, target, fm <= target + 1e-7))
    return results

if __name__ == "__main__":
    for m in [3,4,5]:
        res = run_sweep2(m, 40, seed0=2000*m)
        n_ok = sum(r[3] for r in res)
        print(f"m={m} budget={m-1} target={c_of_n(m-1):.6f}  full-extended-menu covered {n_ok}/{len(res)}")
        bad = [r for r in res if not r[3]]
        for r in bad[:6]:
            print("   p=",[round(x,4) for x in r[0]], "full_menu=",round(r[1],5),"target=",round(r[2],5))
