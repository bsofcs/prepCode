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

def partitionArrayIntoKSubsetDP(arr,K):
	if None in (arr,K):
		return
	N=len(arr)
	Sum=sum(arr)
	if Sum%K!=0 or N<K:
		return False
	target=Sum/K
	dp=[0 for i in range(1<<15)]
	for i in range((1<<15)):
		dp[i]=-1
	dp[0]=0
	for mask in range((1<<15)):
		if dp[mask]==-1:
			continue
		for i in range(N):
			if (mask & (1<<i)==0) and dp[mask]+arr[i]<=target:
				dp[mask|(1<<i)]=((dp[mask]+arr[i])%target)
	if (dp[(1<<N)-1]==0):
		return True
	else:
		return False
	

arr=[1,2,3,4,3,5]
k=2
print(partitionArraryIntoKSubset(arr,k))
print(partitionArrayIntoKSubsetDP(arr,k))
"""
https://www.geeksforgeeks.org/partition-of-a-set-into-k-subsets-with-equal-sum-using-bitmask-and-dp/?ref=rp
"""