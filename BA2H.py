# BA2H
# Implement DistanceBetweenPatternAndStrings
# https://rosalind.info/problems/ba2h/

import math

def HammingDistance(p,q):
  br=0
  for i in range(0,len(p)):
    if p[i]!=q[i]:
      br+=1
  return br

def DistanceBetweenPatternString(pattern,dna):
  k=len(pattern)
  distance=0
  for linija in dna:
    hd=math.inf
    for i in range(0,len(linija)-len(pattern)+1):
      if HammingDistance(pattern,linija[i:i+len(pattern)])<hd:
        hd=HammingDistance(pattern,linija[i:i+len(pattern)])
    distance+=hd
  return distance


x="""
AAA
TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT
"""
inlines=x.split()
pattern=inlines[0]
dna=list()
for i in range(1,len(inlines)):
  dna.append(inlines[i])
print(DistanceBetweenPatternString(pattern,dna))
