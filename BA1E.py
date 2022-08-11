# BA1B
# Find Patterns Forming Clumps in a String
# https://rosalind.info/problems/ba1e/

def kmer(text,i,k):
  return text[i:(i+k)]

def kmersfrequency(text,k):
  D=dict()
  for i in range(0, len(text) - k + 1):
    temp=kmer(text,i,k)
    try:
      D[temp]= D[temp]+1
    except KeyError:
      D[temp]=1
  return D

def clumps(text,k,L,t):
  lista=[]
  for i in range (0,len(text)-L+1):
    D=kmersfrequency(text[i:(i+L)],k)
    for j in D:
      if (D[j]>=t):
        if j not in lista:
          lista.append(j)
  return lista
  
  print(clumps("CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC",5,75,4))
