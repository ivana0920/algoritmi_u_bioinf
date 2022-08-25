# BA6C
# Compute the 2-Break Distance Between a Pair of Genomes
# https://rosalind.info/problems/ba6c/

def blocks(p):
  elements=0
  for c in p:
    elements=elements+len(c)
  return elements

def ChromosomeToCycle(Chromosome):
  Nodes=[]
  for j in range(0,len(Chromosome)):
    i=Chromosome[j]
    if i > 0:
      Nodes.append(2*i-1)
      Nodes.append(2*i)
    else:
      Nodes.append(-2*i) #minus because i is negative
      Nodes.append(-2*i-1)
  return Nodes

def ColoredEdges(P):
  Edges = []
  for Chromosome in P:
    Nodes = ChromosomeToCycle(Chromosome)
    for j in range(len(Chromosome)):
      Edges.append((Nodes[2 * j + 1], Nodes[(2 * j + 2) % len(Nodes)]))
  return Edges

def cycles(p,q):
  e=ColoredEdges(p)
  e.extend(ColoredEdges(q))
  c=0
  nodes=[]
  for i in range (2*blocks(p)):
    nodes.append(i)
  while len(e)>0:
    first=e[0][0]
    second=e[0][1]
    e.remove(e[0])
    while second!=first:
      for edge in e:
        if edge[0]==second:
          second=edge[1]
          e.remove(edge)
          break
        if edge[1]==second:
          second = edge[0]
          e.remove(edge)
          break
    c=c+1
  return c


x="""(+1 +2 +3 +4 +5 +6)
(+1 -3 -6 -5)(+2 -4)"""
inlines=x.split("\n")
p=inlines[0]
q=inlines[1]
P=p[1:-1].split(")(")
Q=q[1:-1].split(")(")
for i in range(len(P)):
  P[i]=[int(el) for el in P[i].split(" ")]
for i in range(len(Q)):
  Q[i]=[int(el) for el in Q[i].split(" ")]
print(blocks(P)-cycles(P,Q))
