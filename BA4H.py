# BA4H
# Generate the Convolution of a Spectrum
# https://rosalind.info/problems/ba4h/

def SpectralConvolution(spectrum):
  rez=list()
  for x in spectrum:
    for y in spectrum:
      if int(x)>int(y):
        rez.append(int(x)-int(y))
  rez2=[str(x) for x in rez]
  return sorted(rez2)


x="0 137 186 323"
rez=""
for x in SpectralConvolution(x.split()):
  rez+=" "+x
print(rez.strip())
