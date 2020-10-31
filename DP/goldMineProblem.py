"""
goldMineProblem
A 2D matrix represnts a gold mine and the value in it represents the gold at that place.
you are allowed to move right, right-up or right-down
Initial place: In first column but not in any specific row
Get max gold
"""
def goldMineProblem(arr):
	if arr is None:
		return 0
	n=len(arr)
	m=len(arr[0])
	dp=[[0 for _ in range(m)] for _ in range(n)]
	for i in range(n):
		dp[i][m-1]=arr[i][m-1]
	for j in range(m-2,-1,-1):
		for i in range(n):
			right=right_up=right_down=0
			right=dp[i][j+1]
			right_up=0 if i-1<0 else dp[i-1][j+1]
			right_down=0 if i+1>=n else dp[i+1][j+1]
			#print(arr[i][j],right,right_up,right_down)
			dp[i][j]=arr[i][j]+max(right,right_up,right_down)
	#for i in range(n):
	#	print(dp[i])
	print(max([dp[i][0] for i in range(n)]))

arr=[[1, 3, 3],[2, 1, 4],[0, 6, 4]]
goldMineProblem(arr)
arr=[[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]]
goldMineProblem(arr)
arr=[[10, 33, 13, 15],[22, 21, 4, 1],[5, 0, 2, 3],[0, 6, 14, 2]]
goldMineProblem(arr)