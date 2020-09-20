"""
minimumCostPathInMatrixFromSourceToTarget

One is allowed to move right or down only. Source is the first cell of the first row.
Target is the last cell of the last row. 
"""

def minimumCostPathInMatrixFromSourceToTarget(arr):
	if arr is None:
		return None
	n=len(arr)
	m=len(arr[0])
	dp=[[-1 for i in range(m)] for i in range(n)]
	dp[0][0]=arr[0][0]
	for i in range(n):
		for j in range(m):
			if dp[i][j]==-1:
				fromRight=fromTop=float("INF")
				#fromTop
				if i-1>=0:
					fromTop=dp[i-1][j]+arr[i][j]
				#fromRight
				if j-1>=0:
					fromRight=dp[i][j-1]+arr[i][j]
				dp[i][j]=min(fromRight,fromTop)
	return(dp[n-1][m-1])

arr=[[1, 2, 9],  
    [5, 3, 8], 
    [4, 6, 7]]
print(minimumCostPathInMatrixFromSourceToTarget(arr))
arr=[[1,3,5,8],[4,2,1,7],[4,3,2,3]]
print(minimumCostPathInMatrixFromSourceToTarget(arr))