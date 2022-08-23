# BA5A
# Find the Minimum Number of Coins Needed to Make Change
# https://rosalind.info/problems/ba5a/

import math

def DPChange(money,strCoins):
  coins=[int(x) for x in strCoins]
  minCoins=[0]*(money+1)
  for m in range(1,money+1):
    minCoins[m]=math.inf
    for i in range(1,len(coins)):
      if m>=coins[i]:
        if minCoins[m-coins[i]]+1<minCoins[m]:
          minCoins[m]=minCoins[m-coins[i]]+1
  return minCoins[money]


x="""40
1,5,10,20,25,50"""
inlines=x.split("\n")
money=int(inlines[0])
coins=inlines[1].split(",")
print(DPChange(money,coins))
