"""
LongestPalindrome
Given a subsequence find the length of the longest palindromic subsequence in it.
For Example:
Input: GEEKSFORGEEKS
Soln: EEFEE, EEOEE, EEKEE,..
Output: 5

Approach:
1. Recursion: LongestPalindrome
2. DP: LongestPalindromeDP
3. DP in O(n) space: LongestPalindromeDPOn
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
	#for i in range(n):
	#	print(dp[i])
	index=dp[0][n-1]
	i,j=0,n-1
	l,r=[],[]
	while dp[i][j]!=0:
		if dp[i+1][j-1]==0:
			l.append(arr[i])
			break
		elif dp[i][j]==dp[i+1][j-1]+2 and dp[i][j]!=max(dp[i+1][j],dp[i][j-1]):
			l.append(arr[i])
			r.append(arr[j])
			i+=1
			j-=1
		elif dp[i][j]==max(dp[i+1][j],dp[i][j-1]) and dp[i][j]==dp[i+1][j]:
			i+=1
		else:
			j-=1
	l.extend(r[::-1])
	return "".join(l)

def LongestPalindromeDPOn(arr):
	if arr is None:
		return None
	n=len(arr)
	a=[0]*n
	for i in range(n-1,-1,-1):
		back_up=0
		for j in range(i,n):
			if i==j:
				a[j]=1
			elif arr[i]==arr[j]:
				a[j],back_up=back_up+2,a[j]
			else:
				back_up,a[j]=a[j],max(a[j],a[j-1])
	print(a)
	return a[n-1]

arr="aaetarchickentaeampampuri"
print(arr)
print(LongestPalindrome(arr))
print(LongestPalindromeDP(arr))
print(LongestPalindromeDPOn(arr))
arr="GEEKSFORGEEKS"
print(arr)
print(LongestPalindrome(arr))
print(LongestPalindromeDP(arr))
print(LongestPalindromeDPOn(arr))
arr="Bhanu Saurabh"
print(arr)
print(LongestPalindrome(arr))
print(LongestPalindromeDP(arr))
print(LongestPalindromeDPOn(arr))