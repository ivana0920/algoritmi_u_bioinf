# BA4A
# Translate an RNA String into an Amino Acid String
# https://rosalind.info/problems/ba4a/

tablica={"CAU":"H","CAC":"H","CAA":"Q","CAG":"Q", "CCU":"P","CCC":"P","CCA":"P","CCG":"P","CGU":"R", "CGC":"R","CGA":"R", "CGG":"R","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
         "GAU":"D","GAC":"D","GAA":"E","GAG":"E","GCU":"A","GCC":"A","GCA":"A","GCG":"A","GGU":"G","GGC":"G","GGA":"G","GGG":"G","GUU":"V","GUC":"V","GUA":"V","GUG":"V","UAU":"Y",
         "UAC":"Y","UAA":"*","UAG":"*","UCG":"S", "UCA":"S","UCC":"S", "UCU":"S","UGU":"C","UGC":"C","UGA":"*","UGG":"W","UUU":"F", "UUC":"F","UUA":"L","UUG":"L", "AAU":"N",
         "AAC":"N","AAA":"K","AAG":"K", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T","AGU":"S", "AGC":"S","AGA":"R","AGG":"R","AUU":"I","AUC":"I","AUA":"I","AUG":"M"}

def AminoAcidString(rna):
  rez=""
  for i in range(0,len(rna)-3,3):
    rez+=tablica[rna[i:i+3]]
  return rez    


print(AminoAcidString("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))
