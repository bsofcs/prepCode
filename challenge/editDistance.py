"""
editDistance
"""
def editDistanceRec(str1,str2):
	if str1 is None or str2 is None:
		return None
	if str1==str2:
		return 0
	return Util(str1,str2,len(str1),len(str2))

def Util(str1,str2,m,n):
	if m==n:
		return 0
	if n==0:
		return m
	if m==0:
		return n
	if str1[m-1]==str2[n-1]:
		return Util(str1,str2,m-1,n-1)
	return 1+min(Util(str1,str2,m-1,n),Util(str1,str2,m,n-1),Util(str1,str2,m-1,n-1))

def editDistance(str1,str2):
	if str1 is None and str2 is None:
		return
	m=len(str1)
	n=len(str2)
	if n==0:
		return m
	if m==0:
		return n
	dp=[[0 for i in range(m+1)] for i in range(n+1)]
	for i in range(m+1):
		dp[0][i]=i
	for i in range(n+1):
		dp[i][0]=i
	for i in range(1,n+1):
		for j in range(1,m+1):
			if str2[i-1]==str1[j-1]:
				dp[i][j]=dp[i-1][j-1]
			else:
				dp[i][j]=1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
	return dp[n][m]

str1="geek"
str2="gesek"
print(editDistanceRec(str1,str2))
print(editDistance(str1,str2))