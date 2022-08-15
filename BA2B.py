# BA2B
# Find a Median String
# https://rosalind.info/problems/ba2b/

from itertools import product

def HammingDistance(p,q):
  br=0
  for i in range(0,len(p)):
    if p[i]!=q[i]:
      br+=1
  return br

def SviKmeri(k):
  nukleotidi={"A","C","G","T"}
  rez=list()
  for x in product(nukleotidi,repeat=k):
    tmp=""
    for y in x:
      tmp+=y
    rez.append(tmp)
  return rez

def d(pattern,text):
  rez=list()
  for i in range(0,len(text)-len(pattern)+1):
    pattern2=text[i:i+len(pattern)]
    rez.append(HammingDistance(pattern,pattern2))
  return min(rez)

def MedianString(dna,k):
  svikmeri=SviKmeri(k)
  rez=dict()
  for x in svikmeri:
    for linija in dna:
      try:
        rez[x]+=d(x,linija)
      except KeyError:
        rez[x]=d(x,linija)
  return [x for x in rez.keys() if rez[x]==min(rez.values())]


x="""
3
AAATTGACGCAT
GACGACCACGTT
CGTCAGCGCCTG
GCTGAGCACCGG
AGTACGGGACAG
"""
inlines=x.split()
k=int(inlines[0])
dna=list()
for i in range(1,len(inlines)):
  dna.append(inlines[i])
print(MedianString(dna,k))
