"""
maximumIncreasingPathInMatrix

You are allowed to move over a 2D matrix in one of the 4 ways: Up, Down, Right and Left
with a condition that:
	--- move from cell A to B iff B=A+1
Find the longest path in the matrix possible
"""
def findTheLongestFromCell(arr,i,j,dp):
	if arr is None or dp is None or i is None or j is None:
		return None
	n=len(arr)
	m=len(arr[0])
	if i<0 or i>=n or j<0 or j>=m:
		return 0
	if dp[i][j]!=-1:
		return dp[i][j]
	up=down=right=left=-1
	#up
	if i>0 and (arr[i][j]+1==arr[i-1][j]):
		up=1+findTheLongestFromCell(arr,i-1,j,dp)
	#down
	if i<n-1 and (arr[i][j]+1==arr[i+1][j]):
		down=1+findTheLongestFromCell(arr,i+1,j,dp)
	#left
	if j>0 and (arr[i][j]+1==arr[i][j-1]):
		left=1+findTheLongestFromCell(arr,i,j-1,dp)
	#right
	if j<m-1 and (arr[i][j]+1==arr[i][j+1]):
		right=1+findTheLongestFromCell(arr,i,j+1,dp)
	dp[i][j]=max(up,down,right,left,1)
	return dp[i][j]

def maximumIncreasingPathInMatrix(arr):
	if arr is None:
		return None
	n=len(arr)
	m=len(arr[0])
	dp=[[-1 for i in range(m)]for i in range(n)]
	result=1
	for i in range(n):
		for j in range(m):
			if dp[i][j]==-1:
				dp[i][j]=findTheLongestFromCell(arr,i,j,dp)
			result=max(result,dp[i][j])
	return result	

arr=[[1, 2, 9],  
    [5, 3, 8], 
    [4, 6, 7]]
print(maximumIncreasingPathInMatrix(arr))