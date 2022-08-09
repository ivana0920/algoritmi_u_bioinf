# BA1A
# http://rosalind.info/problems/ba1a/
# Compute the Number of Times a Pattern Appears in a Text

def PatternCount(text,pattern):
  count=0
  for i in range(0,len(text)-len(pattern)+1):
    if text[i:i+len(pattern)]==pattern:
      count+=1
  return count

print(PatternCount("GCGCG","GCG"))
