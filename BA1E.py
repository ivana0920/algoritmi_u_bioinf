# BA1E
# Find Patterns Forming Clumps in a String
# https://rosalind.info/problems/ba1e/

def FrequentWords(text,k):
  rez=dict()
  for i in range(0,len(text)-k+1):
    try:
      rez[text[i:i+k]]+=1
    except KeyError:
      rez[text[i:i+k]]=1  
  return rez

def Clump(text,k,l,t):
  rez=set()
  for i in range(0,len(text)-l):
    rijecnik=FrequentWords(text[i:i+l],k)
    for x in rijecnik.items():
      if x[1]>=t:
        rez.add(x[0])
  return rez

x="""CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
5 75 4"""
inlines=x.split()
text=inlines[0]
k=int(inlines[1])
l=int(inlines[2])
t=int(inlines[3])
rez=Clump(text,k,l,t)
print(" ".join(rez))
