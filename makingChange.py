"""
makingChange
Given n types of coin denominations of values v1<v2<..<vn (natural numbers).
Assume v1=1, so that we can always make change for any amount of money C. Give an algorithm which makes change for an amount of money C with as few coins as possible.

Approach 1: Back Tracking
Here every coin is taken, then the value of the coin is reduced. Then every other coin is taken in count, to form a n-nary tree. while back tracking we take the length of the shorter branch at every node.
code: coinMakerBT

Approach 2: Dynamic Programming
We create an array "m" of the length (value+1) [i.e. 0,values]. For each element in "m", we calculate the minimum coins needed to reach this number.
For every coin, we calculate the optimal value to every element in "m".
code: coinMakerDP
"""

def coinMakerBT(coins,value):
	if coins is None or value is None:
		return
	n=len(coins)
	if value==0:
		return 0
	res=float("INF")
	for i in range(n):
		if coins[i]<=value:
			sub_res=coinMakerBT(coins,value-coins[i])
			if sub_res!=float("INF") and sub_res+1<res:
				res=sub_res+1
	return res

def coinMakerDP(coins,value):
	if coins is None or value is None:
		return
	n=len(coins)
	if value==0:
		return 0
	m=[float("INF")]*(value+1)
	m[0]=0
	for i in range(1,value+1):
		for j in range(len(coins)):
			if coins[j]<=i:
				sub_res=m[i-coins[j]]
				if sub_res+1<m[i] and sub_res!=float("INF"):
					m[i]=sub_res+1
	return m[value]

coins=[9,6,5,1]
value=11
print(coinMakerBT(coins,value))
print(coinMakerDP(coins,value))