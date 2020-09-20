"""
LongestPalindrome
Given a subsequence find the length of the longest palindromic subsequence in it.
For Example:
Input: GEEKSFORGEEKS
Soln: EEFEE, EEOEE, EEKEE,..
Output: 5
"""
def LongestPalindrome(arr):
	if arr is None:
		return None
	n=len(arr)
	return lpUtil(arr,0,n-1)

def lpUtil(arr,i,j):
	if i>j:
		return 0
	if i==j:
		return 1
	if arr[i]==arr[j]:
		return 2+lpUtil(arr,i+1,j-1)
	else:
		return max(lpUtil(arr,i+1,j),lpUtil(arr,i,j-1))

def LongestPalindromeDP(arr):
	if arr is None:
		return None
	n=len(arr)
	dp=[[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		dp[i][i]=1
	for cl in range(2,n+1):
		for i in range(n-cl+1):
			j=i+cl-1
			if arr[i]==arr[j] and cl==2:
				dp[i][j]=2
			elif arr[i]==arr[j]:
				dp[i][j]=dp[i+1][j-1]+2
			else:
				dp[i][j]=max(dp[i+1][j],dp[i][j-1])
	return dp[0][n-1]

arr="aaetarchickentaeampampuri"
print(LongestPalindrome(arr))
print(LongestPalindromeDP(arr))
arr="GEEKSFORGEEKS"
print(LongestPalindrome(arr))
print(LongestPalindromeDP(arr))