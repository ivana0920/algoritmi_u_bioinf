# BA4D
# Compute the Number of Peptides of Given Total Mass
# https://rosalind.info/problems/ba4d/

tablica=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def RekMasa(masa,rez):
  if masa in rez:
    return rez[masa]
  if masa<0:
    return 0
  if masa==0:
      return 1
  
  rez[masa]=0
  for x in tablica:
    rez[masa]+=RekMasa(masa-x,rez)        
  return rez[masa]

def CountingPeptides(masa):
  rez=dict()
  return RekMasa(masa,rez)


print(CountingPeptides(1024))
