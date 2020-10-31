"""
snakeSequence
A Snake Sequence is made up of adjacent numbers in the grid such that for each number, the number on the right or the number below is either (+/-)1.
ex:
9,6,5,2		9
8,7,6,5		8,7,6,5
7,3,1,6		      6
1,1,1,7		      7

The answer is 9->8->7->6->5->6->7
reason the movement is either:
Right (i,j+1) and Below (i+1,j)
"""

def snakeSequence(arr):
	if arr is None:
		return None
	n=len(arr)
	m=len(arr[0])
	result=0
	dp=[[1 for _ in range(m)] for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if i==0 and j==0:
				continue
			left=top=0
			if j>=0:
				left=dp[i][j-1]+1 if arr[i][j-1]==arr[i][j]-1 or arr[i][j-1]==arr[i][j]+1 else 0
			if i>=0:
				top=dp[i-1][j]+1 if arr[i-1][j]==arr[i][j]-1 or arr[i-1][j]==arr[i][j]+1 else 0
			dp[i][j]=max(dp[i][j],left,top)
			result=max(result,dp[i][j])
	for i in range(n):
		print(dp[i])
	return result

arr=[[9,6,5,2],
[8,7,6,5],
[7,3,1,6],
[1,1,1,7]]
print(snakeSequence(arr))