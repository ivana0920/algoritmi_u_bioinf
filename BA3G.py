# BA3G
# Find an Eulerian Path in a Graph
# https://rosalind.info/problems/ba3g/

from collections import Counter

def EulerianCycle(putovi,start):
  pocetni_cvor=start
  trenutni_cvor=pocetni_cvor
  konacni_put=[pocetni_cvor]

  while putovi:
    if trenutni_cvor in putovi:
      konacni_put.append(putovi[trenutni_cvor][0])
      if len(putovi[trenutni_cvor])==1:
        del putovi[trenutni_cvor]
      else:
        del putovi[trenutni_cvor][0]
      trenutni_cvor=konacni_put[-1]
    else:
      for i,elem in enumerate(konacni_put):
        if elem in putovi:
          novi_ciklus=konacni_put[i:-1]+konacni_put[:i+1]
          konacni_put=novi_ciklus
          trenutni_cvor=elem
          break
  return konacni_put 

def AddImaginaryEdge(putovi):
  br_ulaznih_bridova=Counter()
  br_izlaznih_bridova=Counter()

  for key,value in putovi.items():
    br_izlaznih_bridova[key]+=len(value)
    for v in value:
      br_ulaznih_bridova[v]+=1
  start=list(br_ulaznih_bridova-br_izlaznih_bridova)[0]
  end=list(br_izlaznih_bridova-br_ulaznih_bridova)[0]
  putovi[start]=[end]
  return start,end

def EulerianPath(putovi):
  start,end=AddImaginaryEdge(putovi)
  ciklus=EulerianCycle(putovi,end)[1:]
  print(ciklus)
  for i in range (0,len(ciklus)):
    if ciklus[i]==start and ciklus[i+1]==end:
      return ciklus[i+1:]+ciklus[:i+1]
    
    

x="""0 -> 2
1 -> 3
2 -> 1
3 -> 0,4
6 -> 3,7
7 -> 8
8 -> 9
9 -> 6"""
inlines=x.split("\n")
temp=[y.strip().split(" -> ") for y in inlines]
putovi=dict()
for i in range(0,len(temp)):
  putovi[temp[i][0]]=temp[i][1].split(",")
rez=EulerianPath(putovi)
ispis=rez[0]
for i in range(1,len(rez)):
  ispis+="->"+rez[i]
print(ispis)
