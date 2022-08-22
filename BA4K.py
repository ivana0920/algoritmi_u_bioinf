# BA4K
# Compute the Score of a Linear Peptide
# https://rosalind.info/problems/ba4k/

tablica={"G":57, "A":71, "S":87, "P":97,"V":99, "T":101,"C":103,"I":113,"L":113, "N":114,"D":115, "K":128,"Q":128,"E":129, "M":131,"H":137,"F":147, "R":156, "Y":163,"W":186}
 
def Masa(peptide):
  rez=0
  for x in peptide:
    rez+=tablica[x]
  return rez

def TeoreticalSpectrum(peptide):
  rez=list()
  for i in range(1,len(peptide)):
    for j in range(0,len(peptide)-i+1):
      rez.append(peptide[j:j+i])
  rez2=list()
  for x in rez:
    rez2.append(Masa(x))
  rez2.append(0)
  rez2.append(Masa(peptide))
  return sorted(rez2)

def LinearScore(peptide, spectrum):
  spectrumInt=[int(x) for x in spectrum]
  rez=0
  for value in TeoreticalSpectrum(peptide):
    if value in spectrumInt:
      rez+=1
      spectrumInt.remove(value)
  return(rez)


x="""NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484"""
inlines=x.split("\n")
peptide=inlines[0]
spectrum=inlines[1].split()
LinearScore(peptide, spectrum)
