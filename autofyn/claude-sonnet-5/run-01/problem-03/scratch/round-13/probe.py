from fractions import Fraction as F
import itertools, random

def solve(A, budget, memo=None):
    # A: tuple sorted descending, Fractions
    if len(A) <= 1:
        return sum(A)
    p1 = A[0]
    tail = A[1:]
    # Move 1: halve
    best = p1/2 + solve(tail, budget)
    # Move 2: partial-dom
    S = 0
    jstar = 0
    prefsum = []
    s = F(0)
    for x in tail:
        s += x
        prefsum.append(s)
    for j in range(1, len(tail)+1):
        if prefsum[j-1] <= p1:
            jstar = j
        else:
            break
    if jstar >= 1:
        Sj = prefsum[jstar-1]
        leftover = list(tail[jstar:])
        r = p1 - Sj
        if r > 0:
            leftover.append(r)
        leftover = tuple(sorted(leftover, reverse=True))
        val2 = Sj + solve(leftover, max(budget-1,0))
        best = min(best, val2)
    # Move 3: tail-snip, only if |A| odd, |A|>=3, budget>0
    if len(A) % 2 == 1 and len(A) >= 3 and budget > 0:
        smallest = A[-1]
        newA = list(A[:-1]) + [smallest/2, smallest/2]
        newA = tuple(sorted(newA, reverse=True))
        val3 = solve(newA, budget-1)
        best = min(best, val3)
    return best

def solve_full(A):
    A = tuple(sorted(A, reverse=True))
    return solve(A, 1)

# witness
A = tuple(F(x) for x in [45,40,6,5,4])
Sig = sum(A)
val = solve_full(A)
print("witness value:", val, float(val), "Sigma/2:", Sig/2)

# pure move1 halving chain
def pure_halve(A):
    A = sorted(A, reverse=True)
    if len(A) <= 1:
        return sum(A)
    return A[0]/2 + pure_halve(A[1:])

print("pure move1 chain:", pure_halve(list(A)), float(pure_halve(list(A))))

print()
print("=== characterize local dominance ===")
def remaining_sums(A):
    A = sorted(A, reverse=True)
    R = []
    s = sum(A)
    for x in A:
        R.append(s)
        s -= x
    return R  # R[i] = sum from i to end

def local_dom_indices(A):
    A = sorted(A, reverse=True)
    R = remaining_sums(A)
    doms = []
    for i in range(len(A)-1):
        # is p_i > (R[i]-p_i)/2 i.e. dominant relative to remaining tail after it
        tailsum = R[i]-A[i]
        if tailsum>0 and A[i] > tailsum/2:
            doms.append(i)
    return doms

print("witness dom indices:", local_dom_indices(A))

# random search for violations of HALF-BOUND under Case C, focusing on cascading local dominance
random.seed(1)
worst = None
for trial in range(3000):
    m = random.randint(4,9)
    # build cascading dominant structure: start with total 1, p1 in (something< 1/2)
    vals = []
    remaining = F(1)
    for i in range(m-1):
        # pick p_i as random fraction in (0, remaining) biased toward > remaining/2 sometimes
        num = random.randint(1,999)
        den = 1000
        frac = F(num,den)
        p = frac*remaining
        vals.append(p)
        remaining -= p
        if remaining <= 0:
            break
    vals.append(remaining)
    vals = [v for v in vals if v>0]
    if len(vals) < 4:
        continue
    A = tuple(sorted(vals, reverse=True))
    Sig = sum(A)
    p1 = A[0]
    if p1 >= Sig/2:
        continue  # need Case C
    val = solve_full(A)
    margin = Sig/2 - val
    if worst is None or margin < worst[0]:
        worst = (margin, A, val, Sig)

print("worst margin found (Sigma/2 - solve_full), want >=0:", worst[0] if worst else None)
if worst:
    print(worst)
