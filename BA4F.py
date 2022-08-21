# BA4F
# Compute the Score of a Cyclic Peptide Against a Spectrum
# https://rosalind.info/problems/ba4f/

tablica={"G":57, "A":71, "S":87, "P":97,"V":99, "T":101,"C":103,"I":113,"L":113, "N":114,"D":115, "K":128,"Q":128,"E":129, "M":131,"H":137,"F":147, "R":156, "Y":163,"W":186}

def Masa(peptide):
  rez=0
  for x in peptide:
    rez+=tablica[x]
  return rez

def EsperimentalniSpektar(peptide):
  subPeptides=["",peptide]
  var=peptide+peptide
  for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subPeptides.append(var[j:j+i])
    
  spectrum=[]
  for x in subPeptides:
    spectrum.append(Masa(x))    
  return sorted(spectrum)

def Score(peptide,spectrum):
  kopijaTeorSpetar=[int(x) for x in spectrum]
  br=0
  for value in EsperimentalniSpektar(peptide):
    if value in kopijaTeorSpetar:
      br+=1
      kopijaTeorSpetar.remove(value)
  return br


x="""NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484"""
inlines=x.split("\n")
peptide=inlines[0]
spectrum=inlines[1].split()
print(Score(peptide,spectrum))
