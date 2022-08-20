# BA4B
# Find Substrings of a Genome Encoding a Given Amino Acid String
# https://rosalind.info/problems/ba4b/

tablica={"CAU":"H","CAC":"H","CAA":"Q","CAG":"Q", "CCU":"P","CCC":"P","CCA":"P","CCG":"P","CGU":"R", "CGC":"R","CGA":"R", "CGG":"R","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
         "GAU":"D","GAC":"D","GAA":"E","GAG":"E","GCU":"A","GCC":"A","GCA":"A","GCG":"A","GGU":"G","GGC":"G","GGA":"G","GGG":"G","GUU":"V","GUC":"V","GUA":"V","GUG":"V","UAU":"Y",
         "UAC":"Y","UAA":"*","UAG":"*","UCG":"S", "UCA":"S","UCC":"S", "UCU":"S","UGU":"C","UGC":"C","UGA":"*","UGG":"W","UUU":"F", "UUC":"F","UUA":"L","UUG":"L", "AAU":"N",
         "AAC":"N","AAA":"K","AAG":"K", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T","AGU":"S", "AGC":"S","AGA":"R","AGG":"R","AUU":"I","AUC":"I","AUA":"I","AUG":"M"}

def Zamjena(text):
  return text.replace("T","U")

def KomplementarnaNit(text):
  rez=""
  for x in text:
    if x=="C":
      rez+="G"
    elif x=="G":
      rez+="C"
    elif x=="T":
      rez+="A"
    else:
      rez+="T"
  return rez[::-1]

def ProteinTranslation(text):
  rez=""
  for i in range(0,len(text),3):
    rez+=tablica[text[i:i+3]]
  return rez

def PeptideEncoding(dna,amino):
  n=3*len(amino)
  res=list()
  for i in range(0, len(dna)-n):
    kmer=dna[i:i+n]
    pep=ProteinTranslation(Zamjena(kmer))
    pep2=ProteinTranslation(Zamjena(KomplementarnaNit(kmer)))
    if pep==amino:
      res.append(kmer)
    if pep2==amino:
      res.append(kmer)
  return res


x="""
ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
MA
"""
inlines=x.split()
dna=inlines[0]
amino=inlines[1]
for i in PeptideEncoding(dna,amino):
  print(i)
