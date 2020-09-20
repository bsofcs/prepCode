"""
editDistance

Method 1: editDistanceRecursive
Here we recur till both the length of the strings are used up.
For the last element of the both the strings are same then we proceed to the strings reduced length
Otherwise take the minimum of the following:
	1. Insertion
	2. Deletion
	3. Replacement
and add 1 to the value
"""
def editDistanceRecursive(str1,str2,m,n):
	if str1 is None or str2 is None or m is None or n is None:
		return None
	if m==0:
		return n
	if n==0:
		return m
	if str1[m-1]==str2[n-1]:
		return editDistanceRecursive(str1,str2,m-1,n-1)
	return (1+min(editDistanceRecursive(str1,str2,m,n-1),	#Insert
		editDistanceRecursive(str1,str2,m-1,n),		#Deletion
		editDistanceRecursive(str1,str2,m-1,n-1)	#Replacement
		))

def editDistanceDP(str1,str2,m,n):
	if str1 is None or str2 is None or m is None or n is None:
		return None
	dp=[[0 for i in range(n+1)] for j in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i==0:
				dp[i][j]=j
			elif j==0:
				dp[i][j]=i
			elif str1[i-1]==str2[j-1]:
				dp[i][j]=dp[i-1][j-1]
			else:
				dp[i][j]=1+min(dp[i][j-1],	#Insert
						dp[i-1][j],	#Delete
						dp[i-1][j-1]	#Replacement
				)
	for i in range(m+1):
		print(dp[i])
	return dp[m][n]

str1="Geek"
str2="Geeking"
m=len(str1)
n=len(str2)
print(editDistanceRecursive(str1,str2,m,n))
print(editDistanceDP(str1,str2,m,n))