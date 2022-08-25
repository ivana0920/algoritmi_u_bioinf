# BA6H
# Implement ColoredEdges
# https://rosalind.info/problems/ba6h/

def ChromosomeToCycle(chromosome):
  cvorovi=list()
  for j in range(0,len(chromosome)):
      i=chromosome[j]
      if i>0:
        cvorovi.append(2*i-1)
        cvorovi.append(2*i)
      else:
        cvorovi.append(-2*i) 
        cvorovi.append(-2*i-1)
  return cvorovi

def ColoredEdges(P):
  bridovi=list()
  for chromosome in P:
    cvorovi=ChromosomeToCycle(chromosome)
    for j in range(0,len(chromosome)):
      bridovi.append((cvorovi[2*j+1], cvorovi[(2*j+2)%len(cvorovi)]))
  return bridovi


x="(+1 -2 -3)(+4 +5 -6)"
P=x[1:-1].split(")(")
for i in range(0,len(P)):
  P[i]=[int(x) for x in P[i].split()]
rez=ColoredEdges(P)
for i in range(0,len(rez)):
  rez[i]=str(rez[i])
rez=", ".join(rez)
print(rez)
