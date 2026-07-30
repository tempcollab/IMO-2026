from fractions import Fraction as F
import itertools, random

def oddrank(lst):
    s = sorted(lst, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def find_tied_run(A):
    # A sorted descending; find a maximal run of equal values with even length -> Move 0
    n = len(A)
    i = 0
    while i < n:
        j = i
        while j < n and A[j] == A[i]:
            j += 1
        runlen = j - i
        if runlen >= 2 and runlen % 2 == 0:
            return i, j
        i = j
    return None

memo = {}
def solve2(A, marks):
    A = tuple(sorted(A, reverse=True))
    key = (A, marks)
    if key in memo:
        return memo[key]
    if len(A) == 0 or marks == 0:
        memo[key] = oddrank(A)
        return memo[key]
    candidates = [oddrank(A)]  # stop
    # Move 0: remove tied even run (free)
    run = find_tied_run(A)
    if run is not None:
        i, j = run
        runlen = j - i
        val = A[i]
        contrib = (runlen // 2) * val
        rest = A[:i] + A[j:]
        candidates.append(contrib + solve2(rest, marks))
    # Move 1: halve the top piece p_1
    if marks >= 1 and len(A) >= 1:
        p1 = A[0]
        rest = list(A[1:]) + [p1/2, p1/2]
        candidates.append(solve2(rest, marks-1))
    # Move 2: contiguous prefix match: match p1 against tail prefix t_1..t_j (j=0..len(tail))
    if len(A) >= 1:
        p1 = A[0]
        tail = list(A[1:])
        cum = F(0)
        for j in range(1, len(tail)+1):
            cum += tail[j-1]
            s_sum = cum
            if s_sum > p1:
                break
            r = p1 - s_sum
            if r > 0:
                cost = j  # need j parts matching + 1 residual = j+1 parts => cost j
                if cost <= marks:
                    leftover = tail[j:] + [r]
                    candidates.append(cum + solve2(leftover, marks-cost))
            else:
                # r == 0 exact tie, cost = j-1
                cost = j-1
                if j>=1 and cost <= marks and cost>=0:
                    leftover = tail[j:]
                    candidates.append(cum + solve2(leftover, marks-cost))
    # Move 3: tail-snip - split smallest element in half
    if marks >= 1 and len(A) >= 1:
        pm = A[-1]
        rest = list(A[:-1]) + [pm/2, pm/2]
        candidates.append(solve2(rest, marks-1))
    val = min(candidates)
    memo[key] = val
    return val

def c(k):
    return F(2**k, 2**(k+1)-1)

if __name__ == "__main__":
    # verify extremal witness A=(6,5,4,2)/17
    A = [F(6,17), F(5,17), F(4,17), F(2,17)]
    v = solve2(A, 3)
    target = c(3)*sum(A)
    print("A=(6,5,4,2)/17: solve2=", v, "target=", target, "margin=", target-v)
