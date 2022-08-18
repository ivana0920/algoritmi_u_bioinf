# BA3E
# Construct the De Bruijn Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3e/

def Prefix(kmer):
  return kmer[:len(kmer)-1]

def Sufix(kmer):
  return kmer[1:]

def DeBruijn(patterns):
  rez=dict()
  patterns=sorted(patterns)
  for pattern in patterns:
    try:
      rez[Prefix(pattern)].append(Sufix(pattern))
    except KeyError:
      rez[Prefix(pattern)]=[Sufix(pattern)]
  return rez


x="""
GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG
"""
patterns=x.split()
rez=DeBruijn(patterns)
for x in rez.keys():
  print(x+" -> "+",".join(rez[x]))
