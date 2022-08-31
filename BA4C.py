# BA4C
# Generate the Theoretical Spectrum of a Cyclic Peptide
# https://rosalind.info/problems/ba4c/

tablica={"G":57, "A":71, "S":87, "P":97,"V":99, "T":101,"C":103,"I":113,"L":113, "N":114,"D":115, "K":128,"Q":128,"E":129, "M":131,"H":137,"F":147, "R":156, "Y":163,"W":186}

def Masa(peptide):
  rez=0
  for x in peptide:
    rez+=tablica[x]
  return rez

def CyclicTheoreticalSpectrum(peptide):
  subpeptides=list()
  rez=list()
  var=peptide+peptide
  for i in range(1,len(peptide)):
    for j in range(0,len(peptide)):
      subpeptides.append(var[j:j+i])
  for x in subpeptides:
    rez.append(Masa(x))
  rez.append(0)
  rez.append(Masa(peptide))
  return sorted(rez)

rez=CyclicTheoreticalSpectrum("LEQN")
for i in range(0,len(rez)):
  rez[i]=str(rez[i])
print(" ".join(rez))
