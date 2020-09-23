"""
allSubsequencePalindromes

Approaches:
1. Recursive: allSubsequencePalindromes
2. DP: allSubsequencePalindromesDP
"""
def aSPUtil(arr,i,j):
	if i>j:
		return 0
	if i==j:
		return 1
	if arr[i]==arr[j]:
		return 1+aSPUtil(arr,i+1,j)+aSPUtil(arr,i,j-1)
	else:
		return aSPUtil(arr,i+1,j)+aSPUtil(arr,i,j-1)-aSPUtil(arr,i+1,j-1)

def allSubsequencePalindromes(arr):
	if arr is None:
		return None
	n=len(arr)
	return aSPUtil(arr,0,n-1)

def allSubsequencePalindromesDP(arr):
	if arr is None:
		return None
	n=len(arr)
	m=[[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		m[i][i]=1
	for l in range(2,n+1):
		for i in range(n-l+1):
			j=i+l-1
			if arr[i]==arr[j]:
				m[i][j]=m[i][j-1]+m[i+1][j]+1
			else:
				m[i][j]=m[i+1][j]+m[i][j-1]-m[i+1][j-1]
	return m[0][n-1]

a=["geeksforgeeks","Bhanu Saurabh","aaetaiaampampuri","aaaa","asd"]
for arr in a:
	print(arr)
	print(allSubsequencePalindromes(arr))
	print(allSubsequencePalindromesDP(arr))