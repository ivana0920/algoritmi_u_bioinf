# BA2C
# Find a Profile-most Probable k-mer in a String
# https://rosalind.info/problems/ba2c/

def mostProbkmerinText(text,k,profile):
  rez=dict()
  D={"A":0,"C":1,"G":2,"T":3}
  for i in range(0,len(text)-k+1): 
    pattern=text[i:i+k] 
    br=0
    for j in pattern:
      try:
        rez[pattern]*=profile[D[j]][br]
      except KeyError:
         rez[pattern]=profile[D[j]][br]
      br+=1
  return [x for x in rez.keys() if rez[x]==max(rez.values())]


x="""
ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
5
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2
"""
inlines=x.split("\n")
text=inlines[0]
k=int(inlines[1])
profile=list()
for i in range(2,len(inlines)):
  profile.append(inlines[i].split())
  for j in range(0,k):
    profile[i-2][j]=float(profile[i-2][j])
print(mostProbkmerinText(text,k,profile))
