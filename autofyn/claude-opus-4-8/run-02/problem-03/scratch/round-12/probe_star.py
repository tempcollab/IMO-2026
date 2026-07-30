from fractions import Fraction as Fr
from itertools import product

def ladder(n):
    return [2**(n-1-i) for i in range(n)]  # descending: 2^{n-1},...,1

def partitions_of(total, maxparts):
    # integer partitions of total into at most maxparts parts (descending)
    res=[]
    def rec(remain, maxp, cap, cur):
        if remain==0:
            res.append(list(cur)); return
        if maxp==0: return
        for v in range(min(cap,remain),0,-1):
            cur.append(v); rec(remain-v, maxp-1, v, cur); cur.pop()
    rec(total, maxparts, total, [])
    return res

def Dtilde_from_merge(reds, blues):
    # merge descending, colour, compute D~ and blue_odd, red_even
    elems = [(v,'r') for v in reds]+[(v,'b') for v in blues]
    # sort descending by value; tie-break arbitrary (blue before red say)
    elems.sort(key=lambda x:(-x[0], x[1]))
    D=Fr(0); blue_odd=Fr(0); red_even=Fr(0)
    for j,(v,c) in enumerate(elems):
        rank=j+1
        s=1 if rank%2==1 else -1
        D+=s*v
        if c=='b' and rank%2==1: blue_odd+=v
        if c=='r' and rank%2==0: red_even+=v
    return D, blue_odd, red_even

if __name__=='__main__':
  for n in range(1,8):
      L=ladder(n); tot=2**n
      worst=None
      cnt=0; ties=0
      for pi in partitions_of(tot, n+1):
          D,bo,re=Dtilde_from_merge(pi,L)
          cnt+=1
          assert D==1+2*(bo-re), (pi,D,bo,re)
          if bo<re: worst=(pi,bo,re,D)
          if bo==re: ties+=1
      print(f"n={n}: #partitions={cnt}, ties(D=1)={ties}, violation={worst}")
