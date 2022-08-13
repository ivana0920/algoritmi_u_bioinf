# BA1L
# Implement PatternToNumber
# https://rosalind.info/problems/ba1l/

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


print(FrequencyArray("ACGCGGCTCTGAAA",2))
