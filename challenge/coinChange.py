"""
coinChange
"""
def coinChange(coins,val):
	if None in (coins,val):
		return
	n=len(coins)
	dp=[[float("INF") for i in range(val+1)] for i in range(n+1)]
	for i in range(val+1):
		dp[0][i]=0
	for i in range(1,n+1):
		for j in range(val+1):
			if j>=coins[i-1]:
				dp[i][j]=max(dp[i-1][j],1+dp[i][j-coins[i-1]])
			else:
				dp[i][j]=dp[i-1][j]
	return dp[n][val]

coins=[2, 5, 3, 6]
val=10
print(coinChange(coins,val))