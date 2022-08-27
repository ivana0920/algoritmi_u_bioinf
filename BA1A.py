# BA1A
# http://rosalind.info/problems/ba1a/
# Compute the Number of Times a Pattern Appears in a Text

def Count(text, pattern):
  rez=0
  for i in range(0,len(text)-len(pattern)+1):
    if text[i:i+len(pattern)]==pattern:
      rez+=1
  return rez

x="""GCGCG
GCG"""
inlines=x.split()
text=inlines[0]
pattern=inlines[1]
print(Count(text, pattern))
