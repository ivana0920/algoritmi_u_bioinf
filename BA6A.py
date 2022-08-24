# BA6A
# Implement GreedySorting to Sort a Permutation by Reversals
# https://rosalind.info/problems/ba6a/

def kSortingReversal(P,k):
  j=k
  while P[j]!=k+1 and P[j]!=-(k+1):
    j+=1
  P[k:j+1]=map(lambda x:-x, P[k:j+1][::-1])
  return P

def GreedySorting(P):
  for k in range(0,len(P)):
    if P[k]!=k+1:
      P=kSortingReversal(P,k)
      print("("+" ".join(["+"+str(x) if x>0 else str(x) for x in P])+")")
      if P[k]==-(k+1):
        P=kSortingReversal(P,k)
        print("("+" ".join(["+"+str(x) if x>0 else str(x) for x in P])+")")

        
x="(-3 +4 +1 +5 -2)"
tmp=x[1:len(x)-1].split()
P=list()
for x in tmp:
  P.append(int(x))
rez=GreedySorting(P)
