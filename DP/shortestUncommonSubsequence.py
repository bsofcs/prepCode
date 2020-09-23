"""
shortestUncommonSubsequence
Given two strings S and T, find length of the shortest subsequence in S which is not a subsequence in T. If no such subsequence is possible, return -1. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. A string of length n has 2^n different possible subsequences.
For example:
str1="babab"
str2="babba"
so the subsequence "aab" from str1 is not present in str2
Output: 3

str1="abb"
str2="abab"
Output: -1
as there is no subsequence present in str1 that is not present in str2

Approach:
1. Recursive: shortestUncommonSubsequence
2. DP: shortestUncommonSubsequenceDP
"""
def sunsUtil(str1,str2,m,n):
	print(m,n,str1,str2)
	if m==0:
		return float("INF")
	if n<=0:
		return 1
	for i in range(n):
		if str1[0]==str2[i]:
			break
	if i==n:
		return 1
	tmp=sunsUtil(str1[1:],str2[i+1:],m-1,n-i-1)
	tmp1=sunsUtil(str1[1:],str2,m-1,n)
	return min(1+tmp,tmp1)

def shortestUncommonSubsequence(str1,str2):
	if str1 is None or str2 is None or str1==str2 or str1 in str2:
		return -1
	m=len(str1)
	n=len(str2)
	return sunsUtil(str1,str2,m,n)

def shortestUncommonSubsequenceDP(str1,str2):
	if str1 is None or str2 is None or str1==str2 or str1 in str2:
		return -1
	n=len(str1)
	m=len(str2)
	dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
	for i in range(n+1):
		dp[i][0]=1
	for i in range(m+1):
		dp[0][i]=float("INF")
	for i in range(1,n+1):
		for j in range(1,m+1):
			ch=str1[i-1]
			k=j-1
			while k>=0:
				if ch==str2[k]:
					break
				k-=1
			if k==-1:
				dp[i][j]=1
			else:
				dp[i][j]=min(dp[i-1][k]+1,dp[i-1][j])
	str=" "+str2
	print(" ",list(str))
	for i in range(n+1):
		c=" " if i==0 else str1[i-1]
		print(c,dp[i])
	return dp[n][m] if dp[n][m]<float("INF") else -1

str1="babab"
str2="babba"
print(shortestUncommonSubsequence(str1,str2))
print(shortestUncommonSubsequenceDP(str1,str2))