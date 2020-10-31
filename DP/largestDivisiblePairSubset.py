"""
largestDivisiblePairSubset
Given an array of n distinct elements, find length of the largest subset such that every pair in the subset is such that the larger element of the pair is divisible by smaller element
"""
def largestDivisiblePairSubset(arr):
	if arr is None:
		return None
	arr.sort()
	n=len(arr)
	dp=[1]*n
	i=0
	while i<n:
		j=0
		while j<i:
			if arr[i]%arr[j]==0 and dp[i]<dp[j]+1:
				dp[i]=dp[j]+1
			j+=1
		i+=1
	print(dp)
	print(max(dp))

arr=[10, 5, 3, 15, 20]
largestDivisiblePairSubset(arr)
arr=[18, 1, 3, 6, 13, 17]
largestDivisiblePairSubset(arr)