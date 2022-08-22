# BA4J
# Generate the Theoretical Spectrum of a Linear Peptide
# https://rosalind.info/problems/ba4j/

def LinearSpectrum(peptide,aminoAcid,aminoAcidMass):
  prefixMass=list()
  prefixMass.append(0)
  for i in range(0,len(peptide)):
    for j in range(0,20):
      if aminoAcid[j]==peptide[i]:
        prefixMass.append(prefixMass[i] + aminoAcidMass[j])
  linearSpectrum=[0]
  for i in range(0,len(peptide)):
    for j in range(i+1,len(peptide)+1):
      linearSpectrum.append(prefixMass[j]-prefixMass[i])
  linearSpectrum=sorted(linearSpectrum)
  return(linearSpectrum)

rez=LinearSpectrum("NQEL", 
                  ["G", "A", "S", "P", "V", "T", "C", "I", "L", "N", "D", "K", "Q", "E", "M", "H", "F", "R", "Y","W"],
                  [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163,186])
rez2=""
for i in rez:
  rez2+=str(i)+" "
print(rez2.strip())
