#Find All Occurrences of a Pattern in a String
#http://rosalind.info/problems/ba1d/

def kmer(text, i, k):
    return text[i:(i+k)]

def possition(pattern,text):
    niz=[]
    for i in range(0,len(text)-len(pattern)-1):
        if(kmer(text,i,len(pattern))==pattern):
            niz.append(i)
    return niz

print(possition('ATAT','GATATATGCATATACTT'))
