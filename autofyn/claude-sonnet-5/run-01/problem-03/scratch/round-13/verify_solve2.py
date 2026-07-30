from fractions import Fraction as F
import sys
sys.setrecursionlimit(10000)
memo={}
def solve2(A, marks):
    A = tuple(A); key=(A,marks)
    if key in memo: return memo[key]
    if len(A)<=1 or marks==0:
        v = sum(A)  # oddrank of remaining pieces = alternating sum, but with <=1 no choice; with marks==0, must use oddrank of A as-is
        # Actually for marks==0 and len(A)>1, value = oddrank(A) as-is (no more splits)
        if len(A)<=1:
            v = sum(A)
        else:
            s=sorted(A,reverse=True)
            v=sum(s[i] for i in range(0,len(s),2))
        memo[key]=v; return v
    p1=A[0]; tail=A[1:]
    best=None
    # move1
    if marks>=1:
        v1=solve2(tail, marks-1)
        val1 = p1/F(2) + v1
        best = val1 if best is None else min(best,val1)
    # move2: contiguous prefix match only, try ALL j (not just j*) to respect budget properly
    Spref=F(0)
    for j in range(1, len(tail)+1):
        Spref += tail[j-1]
        if Spref > p1:
            break
        r = p1 - Spref
        cost = j if r>0 else j-1
        if cost<0: cost=0
        if marks>=cost:
            leftover=list(tail[j:])
            if r>0: leftover=leftover+[r]
            leftover=tuple(sorted(leftover,reverse=True))
            newmarks=marks-cost
            if len(leftover)==0:
                v2=F(0)
            else:
                v2=solve2(leftover,newmarks)
            val2=Spref+v2
            best = val2 if best is None else min(best,val2)
    # move3: tail-snip
    if len(A)%2==1 and len(A)>=3 and marks>=1:
        smallest=A[-1]
        Aprime=tuple(sorted(list(A[:-1])+[smallest/F(2),smallest/F(2)],reverse=True))
        v3=solve2(Aprime, marks-1)
        best = v3 if best is None else min(best,v3)
    memo[key]=best
    return best

T=tuple(sorted([F(20),F(15),F(12),F(8)],reverse=True))
val = solve2(T,3)
print("solve2(T,3) =", val, float(val))
print("Sigma(T)/2 =", F(55,2), float(F(55,2)))
