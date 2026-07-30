import numpy as np
from search import compositions, best_for_alloc, reconstruct_leaves, oddrank
from fractions import Fraction

def run(A, budget, label, popsize=20, maxiter=150, polish_iters=4):
    print(f"=== {label}: A={A} budget={budget} ===")
    m = len(A)
    best_overall = None
    best_alloc = None
    best_sol = None
    for ks in compositions(budget, m):
        val, sol = best_for_alloc(A, ks, seed=hash(ks)%1000, popsize=popsize, maxiter=maxiter, polish_iters=polish_iters)
        if best_overall is None or val < best_overall - 1e-10:
            best_overall = val
            best_alloc = ks
            best_sol = sol
    print("BEST:", best_overall, "alloc:", best_alloc)
    leaves, origin = reconstruct_leaves(A, best_sol)
    order = sorted(zip(leaves, origin), key=lambda t: -t[0])
    for r,(v,o) in enumerate(order,1):
        print(f"  rank {r}: value={v:.8f} from piece {o+1} {'ODD' if r%2==1 else 'even'}")
    return best_overall, best_alloc, best_sol

if __name__ == "__main__":
    import sys
    # m=4 case-C example
    A4 = [0.35,0.30,0.20,0.15]
    run(A4, 3, "m=4 test1")

    # m=4 second example, closer to boundary p1~Sigma/2
    A4b = [0.49,0.30,0.12,0.09]
    run(A4b, 3, "m=4 test2")
