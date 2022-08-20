# BA3L
# Construct a String Spelled by a Gapped Genome Path
# https://rosalind.info/problems/ba3l/

def stringSpelledByPatterns(patterns):
    string=patterns[0]
    for x in patterns[1:]:
        string=string+x[-1]  
    return string

def GappedGenomePath(k,d,sequence):
    first=[x[0] for x in sequence]
    second=[x[1] for x in sequence]    

    prefix=stringSpelledByPatterns(first)
    sufix=stringSpelledByPatterns(second)
    
    for i in range(k+d+1,len(prefix)):
        if prefix[i]!=sufix[i-k-d]:
            return "there is no string spalled by the gapped patterns"
    return prefix+sufix[(len(sufix)-k-d):]
            return "nema takvog niza"
    return prefix+sufix[(len(sufix)-k-d):]
  
  
x="""
4 2
GACC|GCGC
ACCG|CGCC
CCGA|GCCG
CGAG|CCGG
GAGC|CGGA
"""
inlines=x.split()
k=int(inlines[0])
d=int(inlines[1])
temp1=[i.split("|") for i in inlines[2:]]
sequence=dict()
for i in range(0,len(temp1)):
  sequence[temp1[i][0]]=temp1[i][1]
print(GappedGenomePath(k,d,temp1))
sequence=dict()
for i in range(0,len(temp1)):
  sequence[temp1[i][0]]=temp1[i][1]
print(GappedGenomePath(k,d,sequence))
