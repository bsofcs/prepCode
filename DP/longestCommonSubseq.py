"""
longestCommonSubseq
"""
def longestCommonSubseq(str1,str2):
	if None in (str1,str2):
		return
	l1=len(str1)
	l2=len(str2)
	dp=[[0 for i in range(l1+1)] for i in range(l2+1)]
	for i in range(1,l2+1):
		for j in range(1,l1+1):
			if str2[i-1]==str1[j-1]:
				dp[i][j]=dp[i-1][j-1]+1
			else:
				dp[i][j]=max(dp[i-1][j],dp[i][j-1])
	for i in range(l2+1):
		print(dp[i])
	return dp[l2][l1]

str1="bhanu"
str2="saurabhbhanu"
print(longestCommonSubseq(str1,str2))