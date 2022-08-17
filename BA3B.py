# BA3B
# Reconstruct a String from its Genome Path
# https://rosalind.info/problems/ba3b/

def StringSpelledGenomePathProblem(kmers):
  rez=kmers[0]
  for i in range(0,len(kmers)):
    rez+=kmers[i][-1]
  return rez


x="""
ACCGA
CCGAA
CGAAG
GAAGC
AAGCT
"""
kmers=x.split()
print(StringSpelledGenomePathProblem(kmers))
