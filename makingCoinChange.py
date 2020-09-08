"""
makingCoinChange
Given n types of coin denominations of values v1<v2<..<vn (natural numbers).
Assume v1=1, so that we can always make change for any amount of money C. Give an algorithm which makes change for an amount of money C with as few coins as possible.

Approach 1: Back Tracking
Here every coin is taken, then the value of the coin is reduced. Then every other coin is taken in count, to form a n-nary tree. while back tracking we take the length of the shorter branch at every node.
code: coinMakerBT

Approach 2: Dynamic Programming
We create an array "m" of the length (value+1) [i.e. 0,values]. For each element in "m", we calculate the minimum coins needed to reach this number.
For every coin, we calculate the optimal value to every element in "m".
code: coinMakerDP

Approach 3: Dynamic Programming with Coins Values
Here we make take the same approach as that of the Knapsack problem.
But with a twist, i.e. since all the coins are available in huge number and a same coin can be picked again and again.
So while including the same the coin, we take the leftover value from the same row, i.e. making the scope of the same coin be picked again.
code: minimumCoins
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
	print(m)
	return m[value]

def minimumCoins(arr,K):
	if arr is None or K is None:
		return None
	n=len(arr)
	m=[[0 for i in range(K+1)] for i in range(n+1)]
	for i in range(n+1):
		m[i][0]=0
	for i in range(K+1):
		m[0][i]=float("INF")
	for i in range(1,n+1):
		for j in range(1,K+1):
			if arr[i-1]<=j:
				m[i][j]=min(m[i-1][j],m[i][j-arr[i-1]]+1)
			else:
				m[i][j]=m[i-1][j]
	for i in range(n+1):
		print(m[i])
	i=n
	val=K
	s=[]
	while i>0 and val>0:
		if m[i][val]!=m[i-1][val]:
			print(i,val,arr[i-1],"Accept")
			s.append(arr[i-1])
			val-=arr[i-1]
		else:
			i-=1
	print(s)
	return(m[n][K])


coins=[9,5,5,1]
value=11
print(coinMakerBT(coins,value))
print(coinMakerDP(coins,value))
print(minimumCoins(coins,value))