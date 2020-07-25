"""
maximumValueContiguousSubsequence
"""
def maxValSubArrayDP(arr):
	if arr is None:
		return


def kadaneAlgo(arr):
	if arr is None:
		return
	max_so_far=float("-INF")
	max_till_now=0
	start=end=0
	n=len(arr)
	for i in range(n):
		max_till_now+=arr[i]
		if max_till_now>max_so_far:
			max_so_far=max_till_now
			end=i
		if max_till_now<0:
			max_till_now=0
			start=i+1
	return [arr[start],arr[end],start,end,max_so_far]

if __name__=='__main__':
	arr=[-2,11,-4,13,-5,2]
	print("Kadane:",arr,kadaneAlgo(arr))
	arr=[1,-3,4,-2,-1,6]
	print("Kadane:",arr,kadaneAlgo(arr))
	arr=[i for i in range(10,0,-2)]
	print("Kadane:",arr,kadaneAlgo(arr))
	arr=[i for i in range(1,101)]
	print("Kadane:",arr,kadaneAlgo(arr))