# BA3C
# Construct the Overlap Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3c/

def Prefix(pattern):
  return pattern[:len(pattern)-1]

def Sufix(pattern):
  return pattern[1:]

def Overlap(patterns):
  rez=list()
  for pattern1 in patterns:
    for pattern2 in patterns:
      if Sufix(pattern1)==Prefix(pattern2):
        rez.append(pattern1+" -> "+pattern2)
  return rez

x="""
ATGCG
GCATG
CATGC
AGGCA
GGCAT
"""
patterns=x.split()
for pattern in Overlap(patterns):
  print(pattern)
