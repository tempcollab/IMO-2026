from fractions import Fraction as F

def solve_trace(A, budget, depth=0):
    A = tuple(sorted(A, reverse=True))
    if len(A) == 1:
        return A[0], ("base", A[0])
    p1 = A[0]
    tail = A[1:]
    v1_tail, trace1 = solve_trace(tail, budget, depth+1)
    v1 = p1/2 + v1_tail
    S = F(0); jstar = 0
    for j in range(1, len(tail)+1):
        Snew = S + tail[j-1]
        if p1 >= Snew:
            jstar = j; S = Snew
        else: break
    r = p1 - S
    leftover = list(tail[jstar:])
    if r > 0: leftover.append(r)
    leftover = tuple(leftover)
    if len(leftover) == 0:
        v2 = S; trace2 = ("dom-full", S)
    else:
        v2_left, trace2sub = solve_trace(leftover, max(budget-1,0), depth+1)
        v2 = S + v2_left
        trace2 = ("dom", S, jstar, leftover, trace2sub)
    cands = [("halve", v1, trace1), ("partial-dom", v2, trace2)]
    if len(A)%2==1 and len(A)>=3 and budget>0:
        last = A[-1]
        Aprime = tuple(sorted(list(A[:-1])+[last/2,last/2], reverse=True))
        v3, trace3 = solve_trace(Aprime, budget-1, depth+1)
        cands.append(("tail-snip", v3, trace3))
    best = min(cands, key=lambda c: c[1])
    return best[1], best

A = [F(45,100), F(40,100), F(6,100), F(5,100), F(4,100)]
val, trace = solve_trace(A, 1)
Sigma = sum(A)
print("Sigma/2 =", Sigma/2, float(Sigma/2))
print("solve_full =", val, float(val))
print("trace:", trace)
