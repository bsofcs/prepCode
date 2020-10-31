"""
zigZagTraversal
"""
def zigZagTraversal(arr):
	n=len(arr)
	dp=[[1,1] for i in range(n)]
	mx=0
	for i in range(1,n):
		for j in range(i):
			if arr[i]<arr[j] and dp[i][0]<dp[j][1]+1:
				dp[i][0]=dp[j][1]+1
			if arr[i]>arr[j] and dp[i][1]<dp[j][0]+1:
				dp[i][1]=dp[j][0]+1
			mx=max(mx,max(dp[i]))
	print("\n",arr)
	for i in dp:
		print(i)
	print(mx)

arr=[1,5,4]
zigZagTraversal(arr)
arr=[10, 22, 9, 33, 49, 50, 31, 60]
zigZagTraversal(arr)