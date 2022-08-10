# BA1D
# http://rosalind.info/problems/ba1d/
# Find All Occurrences of a Pattern in a String

def kmer(text,i,k):
  return text[i:(i+k)]

def possition(pattern,text):
  rez=""
  for i in range(0,len(text)-len(pattern)+1):
    if(kmer(text,i,len(pattern))==pattern):
      rez= rez + str(i) +" "
  return rez

print(possition("ATAT","GATATATGCATATACTT"))
