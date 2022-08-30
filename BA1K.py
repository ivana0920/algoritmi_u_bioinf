# BA1K
# Generate the Frequency Array of a String
# https://rosalind.info/problems/ba1k/

def SimbolToNumber(symbol):
  if symbol=="A":
    return 0
  elif symbol=="C":
    return 1
  elif symbol=="G":
    return 2
  else:
    return 3  

def PatternToNumber(pattern):
  if pattern=="":
    return 0
  symbol=pattern[-1]
  prefix=pattern[:-1]
  return 4*PatternToNumber(prefix)+SimbolToNumber(symbol)

def FrequencyArray(text,k):
  FArray=[0]*(4**k)
  for i in range(0,len(text)-k+1):
    pattern=text[i:i+k]
    j=PatternToNumber(pattern)
    FArray[j]=FArray[j]+1
  return FArray  


x="""ACGCGGCTCTGAAA
2"""
inlines=x.split()
text=inlines[0]
k=int(inlines[1])
rez=FrequencyArray(text,k)
for i in range(0,len(rez)):
  rez[i]=str(rez[i])
print(" ".join(rez))
