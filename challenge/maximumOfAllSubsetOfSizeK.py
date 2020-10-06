"""
maximumOfAllSubsetOfSizeK
https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k/0
arr={1 2 3 1 4 5 2 3 6}
K=3
output: 3 3 4 5 5 5 6
"""
import heapq

def maximumOfAllSubsetOfSizeK(arr,n,k):
	if arr is None or k is None:
		return None
	if n<k:
		return max(arr)
	else:
		res=[]
		for i in range(n-k+1):
			#print(i,i+k)
			res.append(max(arr[i:i+k]))
	return res
	#print(" ".join(map(str,res)))

def maximumOfAllSubsetOfSizeK2(arr,n,k):
	if arr is None or k is None:
		return None
	res=[]
	for i in range(n-k+1):
		tmp=[j for j in arr[i:i+k]]
		#print(i,i+k,tmp)
		heapq._heapify_max(tmp)
		res.append(tmp[0])
	return res
	#print(" ".join(map(str,res)))


arr=list(map(int,"1 2 3 1 4 5 2 3 6".split()))
k=3
n=len(arr)
print(arr)
print(maximumOfAllSubsetOfSizeK(arr,n,k))
print(maximumOfAllSubsetOfSizeK2(arr,n,k))
arr=list(map(int,"8 5 10 7 9 4 15 12 90 13".split()))
k=4
n=len(arr)
print(arr)
print(maximumOfAllSubsetOfSizeK(arr,n,k))
print(maximumOfAllSubsetOfSizeK2(arr,n,k))