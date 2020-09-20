"""
makingPiecesOfRodFromGivenSet

Given an integer N denoting the Length of a line segment. you need to cut the line segment in such a way that the cut length of a line segment each time is integer either x , y or z. and after performing all cutting operation the total number of cutted segments must be maximum. 


Input
First line of input contains of an integer 'T' denoting number of test cases. First line of each testcase contains N . Second line of each testcase contains 3 space separated integers x , y and z.
"""
def makePiecesTry1(arr,N):
	if arr is None or N is None:
		return None
	n=len(arr)
	m=[[0 for i in range(N+1)] for j in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,N+1):
			if arr[i-1]<=j:
				m[i][j]=max(m[i-1][j],1+m[i][j-arr[i-1]])
			else:
				m[i][j]=m[i-1][j]
	for i in range(n+1):
		print(m[i])
	return m[n][N]

def makePiece(arr,N):
	if arr is None or N is None:
		return None
	n=len(arr)
	m=[0]*(N+1)
	for i in range(min(arr),N+1):
		for j in range(n):
			if arr[j]==i and m[i]==0:
				print(m[i],m[i-arr[j]]+1)
				m[i]=1
			if arr[j]<=i and m[i-arr[j]]!=0:
				print(m[i],m[i-arr[j]]+1)
				m[i]=max(m[i],1+m[i-arr[j]])
		print(m)
	return m[N]

arr=[2,1,3]
N=4
print(makePiece(arr,N))	
print(makePiecesTry1(arr,N))

arr=[2,1,1]
N=5
print(makePiece(arr,N))	
print(makePiecesTry1(arr,N))