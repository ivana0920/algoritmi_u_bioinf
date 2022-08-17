# BA3A
# Generate the k-mer Composition of a String
# https://rosalind.info/problems/ba3a/

def StringCompositionProblem(k,text):
  rez=list()
  for i in range(0,len(text)-k+1):
    rez.append(text[i:i+k])
  return sorted(rez) 


x="""
5
CAATCCAAC
"""
inlines=x.split()
k=int(inlines[0])
text=inlines[1]
for kmer in StringCompositionProblem(k,text):
  print(kmer)
