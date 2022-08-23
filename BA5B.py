# BA5B
# Find the Length of a Longest Path in a Manhattan-like Grid
# https://rosalind.info/problems/ba5b/

def ManhattanTourist(n,m,down,right):
  s=list()
  for i in range(0,n+1):
    s.append([0]*(m+1))

  for i in range(1,n+1):
    s[i][0]=s[i-1][0]+int(down[i-1][0])

  for j in range(1,m+1):
    s[0][j]=s[0][j-1]+int(right[0][j-1])

  for i in range(1,n+1):
    for j in range(1,m+1):
      s[i][j]=max(s[i-1][j]+int(down[i-1][j]),s[i][j-1]+int(right[i][j-1]))
  return s[n][m]

x="""4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2"""
inlines=x.split("\n")
n=int(inlines[0].split()[0])
m=int(inlines[0].split()[1])
down=list()
right=list()
for i in range(1,n+1):
  down.append(inlines[i].split())
for i in range(n+2,len(inlines)):
  right.append(inlines[i].split())
print(ManhattanTourist(n,m,down,right))
