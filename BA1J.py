# BA1J
# Find Frequent Words with Mismatches and Reverse Complements
# https://rosalind.info/problems/ba1j/

from itertools import product

def HemmingDistance(p,q):
  br=0
  for i in range (0,len(p)):
    if p[i]!=q[i]:
      br+=1
  return br

def sviKmeri(k):
  rez=list()
  nukleotidi={"A","T","C","G"}
  for x in product(nukleotidi,repeat=k):
    temp=""
    for y in x:
      temp+=y
    rez.append(temp)
  return rez

def approximatrCount(pattern,text,d):
  count=0
  for i in range (0,len(text)-len(pattern)+1):
    if HemmingDistance(pattern,text[i:i+len(pattern)])<=d:
      count+=1
  return count

def komplement(symbol):
  if symbol=="A":
    return "T"  
  if symbol=="C":
    return "G" 
  if symbol=="G":
    return "C"  
  else:
    return "A"

def reverse(pattern):
  rez=""
  for x in pattern:
    rez+=komplement(x)
  return rez[::-1]

def FrequentWordsWithMismatchesAndReverse(text,k,d):
  max=0
  rez=list()
  for x in sviKmeri(k):
    if approximatrCount(x,text,d)+approximatrCount(reverse(x),text,d)>max:
      max=approximatrCount(x,text,d)+approximatrCount(reverse(x),text,d)
  for x in sviKmeri(k):
    if approximatrCount(x,text,d)+approximatrCount(reverse(x),text,d)==max:
      rez.append(x)
  return rez


x="""ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1"""
inlines=x.split()
text=inlines[0]
k=int(inlines[1])
d=int(inlines[2])
rez=FrequentWordsWithMismatchesAndReverse(text,k,d)
print(" ".join(rez))
