# BA2C
# Find a Profile-most Probable k-mer in a String
# https://rosalind.info/problems/ba2c/

def Profile(k,text,profile):
  rez=dict()
  retci={"A":0,"C":1,"G":2,"T":3}
  for i in range(0,len(text)-k+1):
    pattern=text[i:i+k]
    stupac=0
    for slovo in pattern:
      try:
        rez[pattern]*=float(profile[retci[slovo]][stupac])
      except KeyError:
        rez[pattern]=float(profile[retci[slovo]][stupac])
      stupac+=1
  return [x[0] for x in rez.items() if x[1]==max(rez.values())]


x="""ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
5
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2"""
inlines=x.split("\n")
text=inlines[0]
k=int(inlines[1])
profile=list()
for i in range(2,len(inlines)):
  profile.append(inlines[i].split())
rez=Profile(k,text,profile)
for x in rez:
  print(x)
