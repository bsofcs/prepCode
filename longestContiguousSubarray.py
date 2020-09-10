"""
longestContiguousSubarray
"""

def longestContiguousSubarray(X,Y):
	if X is None or Y is None:
		return None
	x=len(X)
	y=len(Y)
	m=0
	for i in range(x):
		for j in range(i,x):
			if X[i:j+1] in Y:
				m=(j+1-i) if m<(j+1-i) else m
#				print(i,j,j+1-i,m)
	return m


def longestContiguousSubarrayDP(X,Y):
"""
Only difference it has from longest common subsequence is that here we consider continuous strings.
Thus we do not keep the last best result in case of mismatch.
i.e. instead of m[i][j]=m[i-1][j] for else part we keep 0 there
"""
	if X is None or Y is None:
		return None
	x=len(X)
	y=len(Y)
	m=[[0 for i in range(y+1)] for j in range(x+1)]
	result=0
	for i in range(1,x+1):
		for j in range(1,y+1):
			if X[i-1]==Y[j-1]:
				m[i][j]=m[i-1][j-1]+1
				result=max(m[i][j],result)
	for i in range(x+1):
		print(m[i])
	return result
X=input("Enter the first string:")
Y=input("Enter the second string:")
print(longestContiguousSubarray(X,Y))
print(longestContiguousSubarrayDP(X,Y))