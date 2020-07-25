"""
allLongestSubsequenceInTwoString
"""
#maximum string length
N=10000
L=[[0 for _ in range(N)] for _ in range(N)]

def findLCS(x,y,m,n):
	s=set()
	if m==0 or n==0:
		s.add("")
		return s
	if x[m-1]==y[n-1]:
		tmp=findLCS(x,y,m-1,n-1)
		for string in tmp:
			s.add(string+x[m-1])
	else:
		if L[m-1][n]>=L[m][n-1]:
			tmp=findLCS(x,y,m-1,n)
			for i in tmp:
				s.add(i)
		if L[m][n-1]>=L[m-1][n]:
			tmp=findLCS(x,y,m,n-1)
			for i in tmp:
				s.add(i)
	return s

def LCS(x,y,m,n):
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				L[i][j]=0
			elif x[i-1]==y[j-1]:
				L[i][j]=L[i-1][j-1]+1
			else:
				L[i][j]=max(L[i-1][j],L[i][j-1])
	return L[m][n]

if __name__=='__main__':
	x=input("Enter the value of x(first string):")
	y=input("Enter the value of y(second string):")
	m=len(x)
	n=len(y)
	print("LCS length is:",LCS(x,y,m,n))
	s=findLCS(x,y,m,n)
	for i in s:
		print(i)