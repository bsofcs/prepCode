"""
KthMinInSorted2DArray
"""
import heapq
def KthMinInSorted2DArray(arr,K):
	if None in (arr,K):
		return 
	print(arr,K)
	n,m=len(arr),len(arr[0])
	h=arr[0]
	heapq.heapify(h)
	for i in range(1,n):
		for j in range(m):
			heapq.heappush(h,arr[i][j])
	for i in range(K):
		t=heapq.heappop(h)
	print(t)

arr=[
[16, 28, 60, 64],
[22, 41, 63, 91],
[27, 50, 87, 93],
[36, 78, 87, 94]
]
K=7
KthMinInSorted2DArray(arr,K)