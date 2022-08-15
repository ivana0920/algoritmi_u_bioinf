# BA2A
# Implement MotifEnumeration
# https://rosalind.info/problems/ba2a/

from itertools import product

def HemmingDistance(p,q):
  br=0
  for i in range (0,len(p)):
    if p[i]!=q[i]:
      br+=1
  return br

def sviKmeri(k):
  rez=list()
  nukleotidi={"A","C","G","T"}
  for x in product(nukleotidi, repeat=k):
    tmp=""
    for y in x:
      tmp+=y
    rez.append(tmp)
  return rez

def approximateCount(pattern,text,d):
  count=0
  for i in range(0,len(text)-len(pattern)+1):
    pattern2=text[i:i+len(pattern)]
    if HemmingDistance(pattern,pattern2)<=d:
      count+=1
  return count

def MotifEnumeration(dna,k,d):
  rez=set()
  SviKmeri=sviKmeri(k)
  for linija in dna:
    for i in range (0,len(linija)-k+1):
      pattern=linija[i:i+k]
      for j in range (0,len(SviKmeri)):
        pattern2=SviKmeri[j]
        if HemmingDistance(pattern,pattern2)<=d:
          a=0
          for l in range (0,len(dna)):
            a+=approximateCount(pattern2,dna[l],d)
          if a>=len(dna):
              rez.add(pattern)
  return rez
  
  
x="""
3 1
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT
"""
inlines=x.split()
k=int(inlines[0])
d=int(inlines[1])
dna=list()
for i in range(2,len(inlines)):
  dna.append(inlines[i])
print(MotifEnumeration(dna,k,d))
