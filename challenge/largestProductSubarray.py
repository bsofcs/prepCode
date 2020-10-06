"""
largestProductSubarray

Input : arr[] = {-2, -3, 0, -2, -40}
Output : 80
Subarray : arr[3..4] i.e.{-2, -40}

Input : arr[] = {0, -4, 0, -2}
Output : 0
"""
def largestProductSubarray(arr):
	if arr is None:
		return None
	n=len(arr)
	s=float("-INF")
	for i in range(n):
		for j in range(i+1):
			tmp=1
			#print(arr[j:i+1],s)
			for k in range(j,i+1):
				tmp*=arr[k]
				if tmp>s:
					s=tmp
	return s

def maxSubarrayProduct(arr):
	if arr is None:
		return None
	n=len(arr)
	if n==1 and arr[0]==0: return 0
	max_ending_here=1
	min_ending_here=1
	max_so_far=float("-INF")
	for i in range(n):
		if arr[i]==0:
			max_ending_here=1
			min_ending_here=0
		else:
			max_ending_here=max_ending_here*arr[i]
		max_so_far=max(max_ending_here,max_so_far)
	return max_so_far
			
	

a=[[6, -3, -10, 0, 2],[-1, -3, -10, 0, 60],[-2, -3, 0, -2, -40],[-1],[1, -2, -3, 0, 7, -8, -2],[0],[1] ]
for arr in a:
	print(arr)
	print(largestProductSubarray(arr))
	print(maxSubarrayProduct(arr))


"""
Note if both max and min is needed
		if arr[i]>0:
			max_ending_here*=arr[i]
			min_ending_here=min(min_ending_here*arr[i],1)
		elif arr[i]==0:
			max_ending_here=1
			min_ending_here=0
		else:
			temp=max_ending_here
			max_ending_here=max_ending_here*arr[i]
			min_ending_here=temp*arr[i]
"""