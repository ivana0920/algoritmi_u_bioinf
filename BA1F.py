# BA1F
# Find a Position in a Genome Minimizing the Skew
# https://rosalind.info/problems/ba1f/

def difference(genome,l):
  brC=0
  brG=0
  for i in range (0,l+1):
    if (genome[i]=="C"):
      brC+=1
    if (genome[i]=="G"):
      brG+=1
  return (brG-brC)

def skew(genome):
  rez=dict()
  rez[0]=0
  for i in range (0,len(genome)):
    if (i==0):
      if (genome[i]=="C"):
        rez[0]=-1
      if (genome[i]=="G"):
        rez[0]=1
    else:
      rez[i]=difference(genome,i)
  return [k for k in range (0,len(rez)) if rez[k]==min(rez.values())]


print(skew("CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"))
