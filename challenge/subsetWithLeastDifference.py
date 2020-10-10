"""
subsetWithLeastDifference
"""
def subsetWithLeastDifferenceRec(arr):
	if arr is None:
		return None
	n=len(arr)
	s=sum(arr)
	return(Util(arr,n,0,s))

def Util(arr,n,sTN,sT):
	if n==0:
		return abs((sT-sTN)-sTN)
	return min(Util(arr,n-1,sTN+arr[n-1],sT),Util(arr,n-1,sTN,sT))
def subsetWithLeastDifference(arr):
	if arr is None:
		return None
	n=len(arr)
	s=sum(arr)
	dp=[[0 for i in range(s+1)] for i in range(n+1)]
	for i in range(n+1):
		dp[i][0]=1
	for i in range(1,n+1):
		for j in range(1,s+1):
			if j>=arr[i-1]:
				dp[i][j]=(dp[i-1][j-1] or dp[i-1][j-arr[i-1]])
	for i in range(s//2,-1,-1):
		if dp[n][i]==1:
			diff=s-(2*i)
			sub=i
			break
	i=n;j=diff+sub
	a=[]
	while i>0 and j>0:
		if dp[i][j]==1 and dp[i-1][j-arr[i-1]]==1:
			a.append(i-1)
			j-=arr[i-1]
		else:
			j-=1
		i-=1
	print([arr[i] for i in a],"\n",[arr[i] for i in range(len(arr)) if i not in a])
	return diff
arr=[2,5,0,9,6,3,3,5]
print(sum(arr))
print("Diff:",subsetWithLeastDifference(arr))
print(subsetWithLeastDifferenceRec(arr))