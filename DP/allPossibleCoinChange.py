"""
allPossibleCoinChange
Given the unlimited supply of coin of the denominations given in an array
It is similar to the Coin change problem where we have to make the minimum number of coins needed to make the value.

Code: minimumCoins to find the minimum coins needed to reach the value
Here we take the min(the value without the new coin, new coin included + values reduces by the new coin but including the new coin)

Code: allPossibleChanges to find the all the ways to make a chage for the value:
Here we add the two values i.e.(the value without the new coin, values reduces by the new coin but including the new coin) 
"""

def minimumCoins(arr,K):
	n=len(arr)
	m=[[float("INF") for i in range(K+1)] for j in range(n+1)]
	for i in range(n+1):
		m[i][0]=0
	for i in range(1,n+1):
		for j in range(1,K+1):
			if j>=arr[i-1]:
				m[i][j]=min(m[i-1][j],1+m[i][j-arr[i-1]])
			else:
				m[i][j]=m[i-1][j]
	for i in range(n+1):
		print(m[i])
	return m[n][K]

def allPossibleChanges(arr,K):
	n=len(arr)
	m=[[0 for i in range(K+1)] for j in range(n+1)]
	for i in range(n+1):
		m[i][0]=1
	for i in range(1,n+1):
		for j in range(1,K+1):
			if j>=arr[i-1]:
				m[i][j]=m[i-1][j]+m[i][j-arr[i-1]]
			else:
				m[i][j]=m[i-1][j]
	for i in range(n+1):
		print(m[i])
	return m[n][K]


arr=[1,2,5]
K=5
print(minimumCoins(arr,K))
print(allPossibleChanges(arr,K))