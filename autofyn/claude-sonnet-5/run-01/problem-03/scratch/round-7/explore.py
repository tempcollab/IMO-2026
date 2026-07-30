import numpy as np
from scipy.optimize import differential_evolution, minimize
from itertools import combinations_with_replacement, product
import json, random

def oddrank(lst):
    s = sorted(lst, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def c_of_n(n):
    return 2**n / (2**(n+1) - 1)

# ---------- ground-truth global search over Xiang Yu's response space ----------

def build_response(p, alloc, params):
    # p: sorted desc tuple, alloc: tuple of nonneg ints (marks per piece), sum(alloc)=budget
    # params: flat array, len = sum(alloc); for piece i, alloc[i] numbers in [0,1] -> sorted -> cuts
    out = []
    idx = 0
    for i, pi in enumerate(p):
        c = alloc[i]
        if c == 0:
            out.append(pi)
        else:
            rs = sorted(params[idx:idx+c])
            idx += c
            prev = 0.0
            cuts = [r*pi for r in rs]
            prevv = 0.0
            for cutv in cuts:
                out.append(cutv - prevv)
                prevv = cutv
            out.append(pi - prevv)
    return out

def allocations(m, budget, maxper=None):
    if maxper is None:
        maxper = budget
    # compositions of budget into m parts each in [0,maxper]
    res = []
    def rec(i, remaining, cur):
        if i == m:
            if remaining == 0:
                res.append(tuple(cur))
            return
        for v in range(0, min(maxper, remaining)+1):
            cur.append(v)
            rec(i+1, remaining-v, cur)
            cur.pop()
    rec(0, budget, [])
    return res

def true_optimum(p, budget, maxper=None, popsize=15, maxiter=60, seed=0):
    best = oddrank(list(p))  # do-nothing baseline
    best_alloc = None
    for alloc in allocations(len(p), budget, maxper=maxper):
        k = sum(alloc)
        if k == 0:
            continue
        def obj(x, alloc=alloc):
            return oddrank(build_response(p, alloc, x))
        bounds = [(0,1)]*k
        if k <= 3:
            # dense grid + local polish is fine, but DE is robust too
            res = differential_evolution(obj, bounds, popsize=popsize, maxiter=maxiter,
                                          tol=1e-10, seed=seed, polish=True, mutation=(0.3,1.7))
        else:
            res = differential_evolution(obj, bounds, popsize=popsize, maxiter=maxiter,
                                          tol=1e-10, seed=seed, polish=True, mutation=(0.3,1.7))
        if res.fun < best:
            best = res.fun
            best_alloc = (alloc, res.x.copy())
    return best, best_alloc

# ---------- existing certified menu ----------

def dom_value(p):
    # p sorted desc tuple/list
    if len(p) < 2: return None, None
    S = sum(p[1:])
    if p[0] >= S - 1e-15:
        return p[0], len(p)-1
    return None, None

def halve_menu(p, budget, depth=0):
    # returns best value achievable using HALVE possibly recursively + fallback to full menu on tail
    if budget <= 0 or len(p) < 2:
        return oddrank(list(p))
    if p[0] >= 2*p[1] - 1e-15:
        tail_best = menu_best(p[1:], budget-1, depth+1)
        return p[0]/2 + tail_best
    return None

def tail_snip_value(p):
    if len(p) < 1: return None
    m = len(p)
    if m % 2 == 1:
        return oddrank(list(p)) - p[-1]/2
    return None

def sandwich_value(p):
    m = len(p)
    if m < 3 or m % 2 == 0:
        return None
    p1,p2,p3,pm = p[0],p[1],p[2],p[-1]
    if p1 < p2 + pm - 1e-15:
        # value = p2 + p3 + p5 + ... + pm  = oddrank(p) - (p1-p2)
        return oddrank(list(p)) - (p1 - p2)
    return None

def partial_dom_values(p, budget):
    # try all j from 0..min(budget, m-1), maximal-j semantics relaxed: just try every j with p1>=S_j
    m = len(p)
    vals = []
    for j in range(0, min(budget, m-1)+1):
        Sj = sum(p[1:1+j])
        if p[0] >= Sj - 1e-15:
            # construct directly: split p1 into p[1..j] plus r=p1-Sj, merge with FULL tail p[1:]
            r = p[0] - Sj
            frags = list(p[1:1+j]) + [r] + list(p[1:])
            vals.append((j, oddrank(frags)))
    return vals

def menu_best(p, budget, depth=0):
    p = tuple(sorted(p, reverse=True))
    candidates = [oddrank(list(p))]
    dv, dk = dom_value(p)
    if dv is not None and dk <= budget:
        candidates.append(dv)
    if budget >= 1 and len(p) >= 2:
        hv = halve_menu(p, budget, depth)
        if hv is not None:
            candidates.append(hv)
    if budget >= 1:
        tv = tail_snip_value(p)
        if tv is not None:
            candidates.append(tv)
        sv = sandwich_value(p)
        if sv is not None:
            candidates.append(sv)
    for j, v in partial_dom_values(p, budget):
        candidates.append(v)
    return min(candidates)

# ---------- extended candidate: independent single-piece "tie to untouched value" moves ----------

def extended_tie_search(p, budget):
    m = len(p)
    best = oddrank(list(p))
    best_desc = None
    idxs = list(range(m))
    for k in range(1, budget+1):
        for S in combinations_with_replacement(idxs, k):
            if len(set(S)) != k:
                continue
            S = list(S)
            others = [i for i in idxs if i not in S]
            if not others:
                continue
            # each split piece i in S ties to some other piece's value (by index into 'others' + also could tie to another split-piece's own value)
            for targets in product(others, repeat=k):
                tie_list = []
                ok = True
                for i, tgt in zip(S, targets):
                    tv = p[tgt]
                    if not (0 < tv < p[i] - 1e-15):
                        ok = False
                        break
                    tie_list.append((i, tv))
                if not ok:
                    continue
                pieces = []
                tie_map = dict(tie_list)
                for i, val in enumerate(p):
                    if i in tie_map:
                        t = tie_map[i]
                        pieces.append(t)
                        pieces.append(val - t)
                    else:
                        pieces.append(val)
                v = oddrank(pieces)
                if v < best - 1e-12:
                    best = v
                    best_desc = (list(S), list(targets))
    return best, best_desc

# ---------- sampling ----------

def random_config(m, seed):
    rng = np.random.default_rng(seed)
    x = rng.dirichlet(np.ones(m))
    return tuple(sorted(x.tolist(), reverse=True))

def run_sweep(m, n_samples, seed0=0, maxper=2):
    budget = m - 1
    n = budget
    target = c_of_n(n)
    results = []
    for s in range(n_samples):
        p = random_config(m, seed0+s)
        mb = menu_best(p, budget)
        ext_best, ext_desc = extended_tie_search(p, budget)
        combined_menu = min(mb, ext_best)
        covered_old = mb <= target + 1e-9
        covered_ext = combined_menu <= target + 1e-9
        results.append(dict(p=p, menu=mb, ext=ext_best, target=target,
                             covered_old=covered_old, covered_ext=covered_ext,
                             ext_desc=ext_desc))
    return results

if __name__ == "__main__":
    import sys
    for m in [3,4,5]:
        res = run_sweep(m, 60, seed0=1000*m, maxper=2)
        n_old = sum(r['covered_old'] for r in res)
        n_ext = sum(r['covered_ext'] for r in res)
        print(f"m={m} n={m-1} target={c_of_n(m-1):.6f}  old-menu covered {n_old}/{len(res)}  old+ext-ties covered {n_ext}/{len(res)}")
        uncovered_by_ext = [r for r in res if not r['covered_ext']]
        print(f"  still uncovered after adding extended tie search: {len(uncovered_by_ext)}")
        for r in uncovered_by_ext[:5]:
            print("   p=", [round(x,4) for x in r['p']], "menu=",round(r['menu'],5),"ext=",round(r['ext'],5),"target=",round(r['target'],5))
