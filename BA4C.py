# BA4C
# Generate the Theoretical Spectrum of a Cyclic Peptide
# https://rosalind.info/problems/ba4c/

tablica=mase={"G":57, "A":71, "S":87, "P":97,"V":99, "T":101,"C":103,"I":113,"L":113, "N":114,"D":115, "K":128,"Q":128,"E":129, "M":131,"H":137,"F":147, "R":156, "Y":163,"W":186}

def Masa(peptide):
  rez=0
  for x in peptide:
    rez+=tablica[x]
  return rez

def Ciklicki(text,k):
  rez=text
  for i in range(0,k-1):
    rez+=text[i]
  if k==1:
    return text
  else:
    return rez

def Cyclospectrum(peptide):
  rez=list()
  for i in range(1,len(peptide)):
    temp=Ciklicki(peptide,i)
    for j in range(0,len(temp)):
      kmer=temp[j:j+i]
      if len(kmer)==i:
        rez.append(Masa(kmer))
  rez.append(0)
  rez.append(Masa(peptide))
  return sorted(rez)

rez=""
for x in Cyclospectrum("LEQN"):
  rez=rez+" "+str(x)
print(rez.strip())
