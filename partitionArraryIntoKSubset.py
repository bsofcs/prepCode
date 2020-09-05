"""
partitionArraryIntoKSubset
"""

def partitionArraryIntoKSubset(arr,k):
	if arr is None or k is None or k==0:
		return None
	s=sum(arr)
	n=len(arr)
	if s%k!=0 or n<k:
		return False
	if k==1:
		return True
	taken=[False]*n
	return partArrInKSubset(arr,0,k,s//k,taken,0)

def partArrInKSubset(arr,currIndex,k,TotSum,taken,sumTillNow):
	n=len(arr)
	if k==1:
		return True
	if sumTillNow==TotSum:
		return partArrInKSubset(arr,0,k-1,TotSum,taken,0)
	if currIndex>=n or sumTillNow>TotSum:
		return False
	for i in range(currIndex,n):
		if taken[i]==False:
			taken[i]=True
			return partArrInKSubset(arr,i+1,k-1,TotSum,taken,sumTillNow-arr[i])
		taken[i]=False
	return False

arr=[1,2,3,4,3,5]
k=5
print(partitionArraryIntoKSubset(arr,k))
dp = [i for i in range(1 << 4)] 
print(dp)
"""
https://www.geeksforgeeks.org/partition-of-a-set-into-k-subsets-with-equal-sum-using-bitmask-and-dp/?ref=rp
"""