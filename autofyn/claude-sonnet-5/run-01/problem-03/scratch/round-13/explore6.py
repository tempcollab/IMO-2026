from fractions import Fraction as F

def solve(A, budget):
    A = tuple(sorted(A, reverse=True))
    if len(A) == 1:
        return A[0]
    p1 = A[0]; tail = A[1:]
    v1 = p1/2 + solve(tail, budget)
    S = F(0); jstar=0
    for j in range(1,len(tail)+1):
        Snew = S+tail[j-1]
        if p1>=Snew:
            jstar=j; S=Snew
        else: break
    r = p1-S
    leftover = list(tail[jstar:])
    if r>0: leftover.append(r)
    leftover = tuple(leftover)
    v2 = S if len(leftover)==0 else S+solve(leftover, max(budget-1,0))
    cands=[v1,v2]
    if len(A)%2==1 and len(A)>=3 and budget>0:
        last=A[-1]
        Aprime=tuple(sorted(list(A[:-1])+[last/2,last/2],reverse=True))
        cands.append(solve(Aprime,budget-1))
    return min(cands)

def excess(A,budget):
    return solve(A,budget) - sum(A)/2

# verify excess identity: excess(A,budget) = min(excess(tail,budget), excess(leftover,budget-1)[if nonempty else 0], excess(A',budget-1)[if applicable])
def check_identity(A,budget):
    A = tuple(sorted(A, reverse=True))
    if len(A)==1:
        return True
    p1=A[0]; tail=A[1:]
    e1 = excess(tail,budget)
    S=F(0);jstar=0
    for j in range(1,len(tail)+1):
        Snew=S+tail[j-1]
        if p1>=Snew: jstar=j;S=Snew
        else: break
    r=p1-S
    leftover=list(tail[jstar:])
    if r>0: leftover.append(r)
    leftover=tuple(leftover)
    e2 = F(0) if len(leftover)==0 else excess(leftover,max(budget-1,0))
    es=[e1,e2]
    if len(A)%2==1 and len(A)>=3 and budget>0:
        last=A[-1]
        Aprime=tuple(sorted(list(A[:-1])+[last/2,last/2],reverse=True))
        e3=excess(Aprime,budget-1)
        es.append(e3)
    lhs = excess(A,budget)
    rhs = min(es)
    return lhs==rhs, lhs, rhs

# test on several examples
tests = [
 [F(45,100),F(40,100),F(6,100),F(5,100),F(4,100)],
 [F(1,3),F(1,3),F(1,3)],
 [F(1826,7188),F(1563,7188),F(1520,7188),F(1514,7188),F(765,7188)],
]
for A in tests:
    ok, lhs, rhs = check_identity(A,1)
    print(A, "identity holds:", ok, lhs, rhs, float(lhs))

# Now specifically check the tail-snip "self-tie" mechanism: after tail-snip, do the two new halves ever get matched to each other exactly?
def trace_tailsnip_selftie(A, budget, depth=0):
    A = tuple(sorted(A, reverse=True))
    if len(A)==1: return
    p1=A[0]; tail=A[1:]
    if len(A)%2==1 and len(A)>=3 and budget>0:
        last=A[-1]
        newhalf = last/2
        Aprime=tuple(sorted(list(A[:-1])+[newhalf,newhalf],reverse=True))
        # check partial-dom match on Aprime: does p1 exactly match some prefix ending EXACTLY at newhalf, i.e. self tie?
        p1p = Aprime[0]; tailp = Aprime[1:]
        S=F(0)
        matched_selftie = False
        count_newhalf_seen = 0
        for j in range(len(tailp)):
            v = tailp[j]
            Snew = S+v
            if p1p>=Snew:
                S=Snew
                if v==newhalf:
                    count_newhalf_seen+=1
            else:
                break
        print("  "*depth,"tail-snip at depth",depth,"newhalf=",float(newhalf),"S(jstar)=",float(S),"p1'=",float(p1p),"exact match(r=0)?",S==p1p)

for A in tests:
    print("---", A)
    trace_tailsnip_selftie(A,1)
