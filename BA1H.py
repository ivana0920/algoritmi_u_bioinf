# BA1H
# Find All Approximate Occurrences of a Pattern in a String
# https://rosalind.info/problems/ba1h/

def HammingDistance(p,q):
  if len(p)!=len(q):
    return "Greška!"
  else:
    rez=0
    for i in range(0,len(p)):
      if p[i]!=q[i]:
        rez+=1
    return rez 

def approximate(pattern,text,d):
  rez=list()
  for i in range (0,len(text)-len(pattern)+1):
    if HammingDistance(pattern,text[i:i+len(pattern)])<=d:
      rez.append(str(i))
  return rez


x="""ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
3"""
inlines=x.split()
pattern=inlines[0]
text=inlines[1]
d=int(inlines[2])
rez=approximate(pattern,text,d)
print(" ".join(rez))
