# BA6G
# Implement CycleToChromosome
# https://rosalind.info/problems/ba6g/

def CycleToChromosome(cvorovi):
  chromosome=list()
  for j in range(0,int(len(cvorovi)/2)):
    if cvorovi[2*j]<cvorovi[2*j+1]:
      chromosome.append(int(cvorovi[2*j+1]/2))
    else:
      chromosome.append(int(-cvorovi[2*j]/2))
  return chromosome   


x="(1 2 4 3 6 5 7 8)"
tmp=x[1:-1].split()
cvorovi=list()
for x in tmp:
  cvorovi.append(int(x))
len(cvorovi)
rez=CycleToChromosome(cvorovi)
rez=["+"+str(x) if x>0 else str(x) for x in rez]
rez="("+" ".join(rez)+")"
print(rez)
