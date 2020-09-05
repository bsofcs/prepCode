"""
arrayIntoTwoSubsetWithMinimumSumDifference
Given an array, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
"""
def arrayIntoTwoSubsetWithMinimumSumDifference(arr):
	if arr is None:
		return None
	#with recursion
	n=len(arr)
	print(recursiveUtil(arr,n,0,sum(arr)))
	print(usingDP(arr))

def recursiveUtil(arr,n,sumTillNow,sumTotal):
	if n==0:
		return abs((sumTotal-sumTillNow)-sumTillNow)
	return min(recursiveUtil(arr,n-1,sumTillNow+arr[n-1],sumTotal),recursiveUtil(arr,n-1,sumTillNow,sumTotal))

def usingDP(arr):
	s=sum(arr)
	n=len(arr)
	m=[[0 for i in range(s+1)] for j in range(n+1)]
	for i in range(n+1):
		m[i][0]=1
	for i in range(1,n+1):
		for j in range(1,s+1):
			m[i][j]=(m[i-1][j] or m[i-1][j-arr[i-1]])
	diff=float("INF")
	"""
	for i in range(n+1):
		a=arr[i-1] if i!=0 else " "
		print(a,m[i])
	"""
	for i in range(s//2,-1,-1):
		if m[n][i]==1:
			#print("i:",i,s,s//2)
			diff=s-(2*i)
			break
	return diff

arr=[1,6,1,3]
arrayIntoTwoSubsetWithMinimumSumDifference(arr)