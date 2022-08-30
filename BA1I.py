# BA1I
# Find the Most Frequent Words with Mismatches in a String
# https://rosalind.info/problems/ba1i/

from itertools import product

def HemmingDistance(p,q):
  br=0
  for i in range (0,len(p)):
    if p[i]!=q[i]:
      br+=1
  return br

def sviKmeri(k):
  rezultat=list()
  nukleotidi={"A","T","G","C"}
  for x in product(nukleotidi,repeat=k):
    temp=""
    for y in x:
      temp+=y
    rezultat.append(temp)
  return rezultat

def appriximateCount(pattern,text,d):
  count=0
  for i in range (0,len(text)-len(pattern)+1):
    pattern2=text[i:i+len(text)]
    if HemmingDistance(pattern,pattern2)<=d:
      count+=1
  return count

def MostFrequentWordsWithMismatches(text,k,d):
  max=0
  rezultat=list()
  for x in sviKmeri(k):
    if appriximateCount(x,text,d)>max:
      max=appriximateCount(x,text,d)
  for x in sviKmeri(k):
    if appriximateCount(x,text,d)==max:
      rezultat.append(x)
  return rezultat


x="""ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1"""
inlines=x.split()
text=inlines[0]
k=int(inlines[1])
d=int(inlines[2])
rez=MostFrequentWordsWithMismatches(text,k,d)
print(" ".join(rez))
