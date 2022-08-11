# BA1F
# Find a Position in a Genome Minimizing the Skew
# https://rosalind.info/problems/ba1f/

def skew(genome):
  rez=[0]*len(genome)
  for i in range(0,len(genome)-1):
    if genome[i]=="G":
      rez[i+1]=rez[i]+1
    elif genome[i]=="C":
      rez[i+1]=rez[i]-1
    else:
      rez[i+1]=rez[i]
  return rez

def minskew(genome):
  rez=list()
  s=skew(genome)
  minimum=min(s)
  for i in range(0,len(s)):
    if s[i]==minimum:
      rez.append(i)
  return rez

print(skew("CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"))
