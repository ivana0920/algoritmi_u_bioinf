# BA1B
# http://rosalind.info/problems/ba1b/
# Find the Most Frequent Words in a String

def FrequentWords(text,k):
  rez=dict()
  for i in range(0,len(text)-k+1):
    try:
      rez[text[i:i+k]]+=1
    except KeyError:
      rez[text[i:i+k]]=1
  return [x[0] for x in rez.items() if x[1]==max(rez.values())]

x="""ACGTTGCATGTCGCATGATGCATGAGAGCT
4"""
inlines=x.split()
text=inlines[0]
k=int(inlines[1])
rez=FrequentWords(text,k)
print(" ".join(rez))
