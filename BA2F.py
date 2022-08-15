# BA2F
# Implement RandomizedMotifSearch
# https://rosalind.info/problems/ba2f/

import random

def HammingDistance(p,q):
  br=0
  for i in range(0,len(p)):
    if p[i]!=q[i]:
      br+=1
  return br


x="""
8 5
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA
"""
inlines=x.split()
k=int(inlines[0])
t=int(inlines[0])
dna=list()
for i in range(2,len(inlines)):
  dna.append(inlines[i])
rez=RandomizedMotifSearch2(dna,k,t)
for j in range(0,len(rez)):
  print(rez[j])
