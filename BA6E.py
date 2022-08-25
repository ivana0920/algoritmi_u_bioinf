# BA6E
# Find All Shared k-mers of a Pair of Strings
# https://rosalind.info/problems/ba6e/

def ReverseComplement(text):
  rez=""
  for x in text:
    if x=="A":
      rez+="T"
    if x=="T":
      rez+="A"
    if x=="G":
      rez+="C"
    if x=="C":
      rez+="G"         
  return rez[::-1]

def shared(k,dna1,dna2):
  rez=list()  
  for i in range(0,len(dna1)-k+1):
    for j in range (0,len(dna2)-k+1):
      if dna1[i:i+k]==dna2[j:j+k] or dna1[i:i+k]==ReverseComplement(dna2[j:j+k]):
        rez.append([i,j])
  return rez


x="""
3
AAACTCATC
TTTCAAATC
"""
inlines=x.split()
k=int(inlines[0])
dna1=inlines[1]
dna2=inlines[2]
rez=shared(k,dna1,dna2)
for x in rez:
  print("("+str(x[0])+", "+str(x[1])+")")
