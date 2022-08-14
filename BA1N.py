# BA1N
# Generate the d-Neighborhood of a String
# https://rosalind.info/problems/ba1n/

def HemmingDistance(p,q):
  br=0
  for i in range(0,len(p)):
    if p[i]!=q[i]:
      br+=1
  return br

def Neighbors(pattern,d):
  neighbours=set()
  nukleotidi={"A","C","G","T"}
  if d==0:
    return {pattern}
  if len(pattern)==1:
    return nukleotidi
  suffix=Neighbors(pattern[1:],d)
  for text in suffix:
    if HemmingDistance(pattern[1:],text)<d:
      for x in nukleotidi:
        s=x+text
        neighbours.add(s)
    else:
      s=pattern[0]+text
      neighbours.add(s)
  return neighbours     
  
  
print(Neighbors("ACG",1))
