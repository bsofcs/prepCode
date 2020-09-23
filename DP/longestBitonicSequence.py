"""
longestBitonicSequence

A Bitonic Sequence has number which increases to pick and then decreases to bottom. But there are catches:
	1. a single element is also a bitonic sequence
	2. a ascending array is also a bitonic array
	3. so is a descending array

Question: we need to find the longest bitonic subsequence in a given series of numbers:
Example:
I/p: 1, 11, 2, 10, 4, 5, 2, 1
O/p: 6 (1, 2, 10, 4, 2, 1)
I/p: 12, 11, 40, 5, 3, 1
O/p: 5 (12, 11, 5, 3, 1)
I/p: 80, 60, 30, 40, 20, 10
O/p: 5 (80, 60, 30, 20, 10)
"""

def longestBitonicSequence(arr):
	if arr is None:
		return None
	n=len(arr)
	l2ris=[1 for i in range(n)]
	r2lis=[1 for i in range(n)]
	for i in range(1,n):
		for j in range(0,i):
			if arr[j]<arr[i]:
				l2ris[i]=max(l2ris[i],l2ris[j]+1)
	for i in range(n-1,-1,-1):
		for j in range(n-1,i,-1):
			if arr[j]<arr[i]:
				r2lis[i]=max(r2lis[i],r2lis[j]+1)
	res=[l2ris[i]+r2lis[i]-1 for i in range(n)]
	return max(res)

a=[[80, 60, 30, 40, 20, 10],[12, 11, 40, 5, 3, 1],[1, 11, 2, 10, 4, 5, 2, 1],[1,3,5,6,7,8,9,10],[1]]
for arr in a:
	print(arr)
	print(longestBitonicSequence(arr))