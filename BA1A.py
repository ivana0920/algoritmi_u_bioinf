# BA1A
# http://rosalind.info/problems/ba1a/
# Compute the Number of Times a Pattern Appears in a Text

def kmer(text, i, k):
    return text[i:(i+k)]

def patterncount(text, pattern):
    count = 0
    np = len(pattern)
    for i in range(0, len(text) - np + 1):
        if kmer(text, i, np) == pattern:
            count = count + 1
    return count

print(patterncount('GCGCG','GCG'))
