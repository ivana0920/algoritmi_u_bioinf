# BA6B
# Compute the Number of Breakpoints in a Permutation
# https://rosalind.info/problems/ba6b/

def Breakpoints(P):
  rez=0
  for i in range(0,len(P)-1):
    if P[i+1]-P[i]!=1:
      rez+=1
  return rez


x="(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)"
tmp=x[1:len(x)-1].split()
P=list()
P.append(0)
for x in tmp:
  P.append(int(x))
P.append(len(P))
print(Breakpoints(P))
