"""
maximumIndexDiff
"""

def maximumIndexDiff(arr,n):
	if arr is None or n is None:
		return None
	Lmin=[0]*n
	Rmax=[0]*n
	Lmin[0]=arr[0]
	for i in range(1,n):
		Lmin[i]=min(arr[i],Lmin[i-1])
	Rmax[n-1]=arr[n-1]
	for j in range(n-2,-1,-1):
		Rmax[j]=max(arr[j],Rmax[j+1])
	print(Lmin,"\n",Rmax)
	i,j=0,0
	maxDiff=-1
	while i<n and j<n:
		if Lmin[i]<=Rmax[j]:
			maxDiff=max(maxDiff,j-i)
			j+=1
		else:
			i+=1
	return maxDiff

arr=[34, 8, 10, 3, 2, 80, 30, 33, 1]
n=len(arr)
print(maximumIndexDiff(arr,n))