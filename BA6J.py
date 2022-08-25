# BA6J
# Implement 2-BreakOnGenomeGraph
# https://rosalind.info/problems/ba6j/

def TwoBreakOnGenomeGraph(g,i1,i2,j1,j2):
  if (i1,i2) in g:
    g.remove((i1,i2))
  else:
    if (i2,i1) in g:
      g.remove((i2,i1))
  if (j1,j2) in g:
      g.remove((j1,j2))
  else:
    if (j2,j1) in g:
      g.remove((j2, j1))
  g.append((int(i1),int(j1)))
  g.append((int(i2),int(j2)))
  return g


x="""(2, 4), (3, 8), (7, 5), (6, 1)
1, 6, 3, 8"""
inlines=x.split(("\n"))
i1,i2,j1,j2=inlines[1].split(", ")
g=inlines[0]
g=g[1:-1].split("), (")
for i in range(len(g)):
  a=g[i].split(", ")
  g[i]=(int(a[0]), int(a[1]))
rez=TwoBreakOnGenomeGraph(g,i1,i2,j1,j2)
for i in range(0,len(rez)):
  rez[i]=str(rez[i])
rez=", ".join(rez)
print(rez)
