"""
longestRepeatingSubseq
Input: AABEBCDD
Output: ABD
"""
def longestRepeatingSubseq(str):
	if str is None:
		return
	l1=len(str)
	dp=[[0 for i in range(l1+1)] for i in range(l1+1)]
	for i in range(1,l1+1):
		for j in range(1,l1+1):
			if str[i-1]==str[j-1] and i!=j:
				dp[i][j]=dp[i-1][j-1]+1
			else:
				dp[i][j]=max(dp[i-1][j],dp[i][j-1])
	#for i in range(l1+1):
	#	print(dp[i])
	i,j=l1,l1
	res=[]
	while i>0 and j>0:
		#print(i,j)
		if dp[i][j]==1+dp[i-1][j-1]:
			res.insert(0,str[i-1])
			i-=1
			j-=1
		elif dp[i][j]==max(dp[i-1][j],dp[i][j-1]):
			if dp[i][j]==dp[i-1][j]:
				i-=1
			else:
				j-=1
	print("".join(res))
	return dp[l1][l1]

str="bhanusaurabhra"
print(longestRepeatingSubseq(str))
str="AABEBCDD"
print(longestRepeatingSubseq(str))