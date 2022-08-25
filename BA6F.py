# BA6F
# Implement ChromosomeToCycle
# https://rosalind.info/problems/ba6f/

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


x="(+1 -2 -3 +4)"
tmp=x[1:-1].split()
chromosome=list()
for x in tmp:
  chromosome.append(int(x))
rez=ChromosomeToCycle(chromosome)
for i in range(0,len(rez)):
  rez[i] = str(rez[i])
rez=" ".join(rez)
rez= "(" + rez + ")"
print(rez)
