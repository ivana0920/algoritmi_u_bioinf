# BA1B
# http://rosalind.info/problems/ba1b/
# Find the Most Frequent Words in a String

def kmer(text, i, k):
    return text[i:(i+k)]

def kmersfrequency(text, k):
    D = dict()     
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] += 1
        except KeyError:
            D[tmp] = 1
    return(D)

def mostfrequentkmers(text, k):
    D = kmersfrequency(text, k)
    return dict.fromkeys([x[0] for x in D.items() if x[1] == max(D.values())],max(D.values()))

print(mostfrequentkmers("ACGTTGCATGTCGCATGATGCATGAGAGCT",4))
