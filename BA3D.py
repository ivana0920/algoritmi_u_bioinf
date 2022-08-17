# BA3D
# Construct the De Bruijn Graph of a String
# https://rosalind.info/problems/ba3d/

def Sufix(Pattern):
  return Pattern[1:len(Pattern)]

def Prefix(Pattern):
  return Pattern[0:len(Pattern)-1]

def SviKmeri(k,tetx):
  rez=list()
  for i in range(0,len(text)-k+1):
    rez.append(text[i:i+k])
  return rez

def DeBruijnk(k,text):
  rez=dict()
  svikmeri=sorted(SviKmeri(k,text))
  for kmer in svikmeri:
    try:
      rez[Prefix(kmer)].append(Sufix(kmer))
    except KeyError:
      rez[Prefix(kmer)]=[Sufix(kmer)]
  return rez


x="""
4
AAGATTCTCTAC
"""
inlines=x.split()
k=int(inlines[0])
text=inlines[1]
rez=DeBruijnk(k,text)
for key in rez.keys():
  print(key+" -> "+",".join(rez[key]))
