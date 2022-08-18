# BA3F
# Find an Eulerian Cycle in a Graph
# https://rosalind.info/problems/ba3f/

def EulerianCycle(putovi):
  pocetni_cvor=list(putovi.keys())[0]
  trenutni_cvor=pocetni_cvor
  konacni_put=[trenutni_cvor]

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


x="""0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6"""
inlines=x.split("\n")
temp=[y.strip().split(" -> ") for y in inlines]
putovi=dict()
for i in range (len(temp)):
  putovi[temp[i][0]]=temp[i][1].split(",")
rez=EulerianCycle(putovi)
ispis=rez[0]
for i in range (1,len(rez)):
  ispis+=" -> "+ rez[i]
print(ispis)
