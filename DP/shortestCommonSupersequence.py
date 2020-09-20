"""
shortestCommonSupersequence
Given two strings str1 and str2, find the length of the smallest string which has both, str1 and str2 as its sub-sequences.
Note: str1 and str2 can have both uppercase and lowercase letters.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two space-separated strings.

Output:
For each testcase, in a new line, output the length of the required string.
"""
def shortestCommonSupersequence(str1,str2):
	n1,n2=len(str1),len(str2)
	if n1==0 or n2==0:
		return max(n1,n2)
	m=[[0 for i in range(n2+1)] for i in range(n1+1)]
	for i in range(1,n1+1):
		for j in range(1,n2+1):
			if str1[i-1]==str2[j-1]:
				m[i][j]=m[i-1][j-1]+1
			else:
				m[i][j]=max(m[i-1][j],m[i][j-1])
	return(n1+n2-m[n1][n2])

str1="BhanuSaurabh"
str2="BhaSaurh"
print(shortestCommonSupersequence(str1,str2))