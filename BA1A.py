#PODSTRING OD STRINGA TEXT OD I-TE DO I+K-TE POZICIJE
def kmer(text, i, k):
    return text[i:(i+k)]
#KOLIKO PUTA SE PATTERN POJAVIO U TEXT
def patterncount(text, pattern):
    count = 0
    np = len(pattern)
    for i in range(0, len(text) - np + 1):
        if kmer(text, i, np) == pattern:
            count = count + 1
    return count

print(patterncount('GCGCG','GCG'))

