"""
twoSubsetWithSameSum
Given a set of numbers, check whether it can be partitioned into two subsets such that the sum of elements in both subsets is same or not.

Basically we need to find one subset having sum = TotalSumOfArray/2
"""

def canExist2Sub(arr):
	if arr is None:
		return None
	s=sum(arr)
	if s%2!=0:
		return False
	print(canExistUtil2Sub(arr,s/2))
	print(subsetWithGivenSum(arr,s//2))

def canExistUtil2Sub(arr,totSum):
	if totSum==0:
		return True
	n=len(arr)
	if n==0 or totSum<=0:
		return False
	return(canExistUtil2Sub(arr[:n-1],totSum) or canExistUtil2Sub(arr[:n-1],totSum-arr[n-1]))

def subsetWithGivenSum(arr,totSum):
	n=len(arr)
	m=[[False for i in range(totSum+1)] for j in range(n+1)]
	for i in range(totSum+1):
		m[0][i]=False
	for i in range(n+1):
		m[i][0]=True
	for i in range(1,n+1):
		for j in range(1,totSum+1):
			if arr[i-1]>j:
				m[i][j]=False
			else:
				m[i][j]=m[i-1][j] or m[i-1][j-arr[i-1]]
	return m[n][totSum]
	
arr=[0,2,4,6]
canExist2Sub(arr)