"""
subsetWithSumVal
Print the subset from a non-negative array, that adds upto a value given.
"""

def subsetWithSumVal(arr,K):
	if arr is None or K is None:
		return None
	n=len(arr)
	subsetUtil(arr,K,n-1)
	print()

def subsetUtil(arr,K,n):
	if K==0:
		print()
		return True
	if n==0:
		return False
	if arr[n]>K:
		return subsetUtil(arr,K,n-1)
	else:
		tmp=subsetUtil(arr,K,n-1) 
		tmp1=subsetUtil(arr,K-arr[n],n-1)
		if tmp1:
			print(arr[n],end=" ")
		return tmp or tmp1


def subsetWithSumValDP(arr,K):
	if arr is None or K is None:
		return None
	n=len(arr)
	m=[[0 for _ in range(K+1)] for _ in range(n+1)]
	for i in range(n+1):
		m[i][0]=1
	for i in range(1,n+1):
		for j in range(1,K+1):
			if arr[i-1]<=j:
				m[i][j]=(m[i-1][j] or m[i-1][j-arr[i-1]])
	for i in range(n+1):
		print(m[i])
	print(m[n][K])

arr=[10, 7, 5, 18, 12, 20, 15]
K=35
subsetWithSumVal(arr,K)
subsetWithSumValDP(arr,K)