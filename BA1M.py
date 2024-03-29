# BA1M.py
# Implement NumberToPattern
# https://rosalind.info/problems/ba1m/

def NumberToSimbol(br):
  if br==0:
    return "A"
  elif br==1:
    return "C"
  elif br==2:
    return "G"
  else:
    return "T"  

def NumberToPattern(index,k):
  if k==1:
    return NumberToSimbol(index)
  prefixInd=index//4
  ostatak=index%4
  symbol=NumberToSimbol(ostatak)
  prefixPattern=NumberToPattern(prefixInd,k-1)
  return prefixPattern+symbol


x="""45
4"""
inlines=x.split()
index=int(inlines[0])
k=int(inlines[1])
print(NumbertoPattern(index,k))
