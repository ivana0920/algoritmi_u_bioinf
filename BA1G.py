# BA1G.py
# Compute the Hamming Distance Between Two Strings
# https://rosalind.info/problems/ba1g/

def HammingDistance(p,q):
  if len(p)!=len(q):
    return "Greška!"
  else:
    rez=0
    for i in range(0,len(p)):
      if p[i]!=q[i]:
        rez+=1
    return rez 
  
  
print(HammingDistance("GGGCCGTTGGT","GGACCGTTGAC"))
