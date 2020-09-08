"""
subsetSumToValProblem
Let us assume that "arr" is an array of interger and "T" is an natural number.
Check if there is a subset of the array which sums up to the value T.
Return Number of such subset if we have any.
"""

def subsetUtil(arr,n,T):
	if T==0:
		print()
		return True
	if n==0:
		return False
	if arr[n-1]>T:
		return subsetUtil(arr,n-1,T)
	tmp=subsetUtil(arr,n-1,T) 
	tmp1=subsetUtil(arr,n-1,T-arr[n-1])
	if tmp1:
		print(arr[n-1],end=",")
	return tmp or tmp1

def subsetSumToValBT(arr,T):
	if arr is None or T is None:
		return None
	n=len(arr)
	return subsetUtil(arr,n,T)

def subsetSumToVal(arr,T):
	if arr is None or T is None:
		return None
	n=len(arr)
	m=[[0 for i in range(T+1)] for j in range(n+1)]
	for i in range(T+1):
		m[0][i]=0
	for i in range(n+1):
		m[i][0]=1
	for i in range(1,n+1):
		for j in range(1,T+1):
			m[i][j]=(m[i-1][j] or m[i-1][j-arr[i-1]])
	print(" ",[i for i in range(T+1)])
	for i in range(n+1):
		if i:
			print(arr[i-1], m[i])
		else:
			print("0",m[i])
	return True if m[n][T] else False


def countSubsetSumToVal(arr,T):
	if arr is None or T is None:
		return None
	n=len(arr)
	m=[[0 for i in range(T+1)] for j in range(n+1)]
	for i in range(n+1):
		m[i][0]=1
	for i in range(1,n+1):
		for j in range(1,T+1):
			if arr[i-1]<=j:
				m[i][j]=m[i-1][j]+m[i-1][j-arr[i-1]]
			else:
				m[i][j]=m[i-1][j]
	for i in range(n+1):
		print(m[i])
	return m[n][T]

arr=[1,1,3,2,6]
T=5
print(subsetSumToValBT(arr,T))
print(subsetSumToVal(arr,T))
print("Count:",countSubsetSumToVal(arr,T))


arr=[3,3,3,3]
T=6
print(subsetSumToValBT(arr,T))
print(subsetSumToVal(arr,T))
print("Count:",countSubsetSumToVal(arr,T))