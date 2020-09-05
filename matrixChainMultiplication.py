"""
matrixChainMultiplication

"""
def printParenthesis(m,j,i):
	if j==i:
		print(chr(65+j),end="")
		return
	else:
		print("(",end="")
		printParenthesis(m,m[j][i]-1,i)
		printParenthesis(m,j,m[j][i])
		print(")",end="")

def matrixChainMultiplication(arr):
	if arr is None:
		return None
	n=len(arr)
	noOfMatrix=(n-1)
	m=[[0 for i in range(noOfMatrix)] for j in range(noOfMatrix)]
	s=[[0 for i in range(noOfMatrix)] for j in range(noOfMatrix)]
	for l in range(2,noOfMatrix+1):
		for i in range(noOfMatrix-l+1):
			j=i+l-1
			m[i][j]=float("INF")
			for k in range(i,j):
				#print("l,i,j,k,m[i][k],m[k+1][j],arr[i],arr[k+1],arr[j+1]:\n",l,i,j,k,m[i][k],m[k+1][j],arr[i],arr[k+1],arr[j+1])
				q=(m[i][k]+m[k+1][j]+(arr[i]*arr[k+1]*arr[j+1]))
				#print("m[i][j],q:",m[i][j],q)
				if q<m[i][j]:
					m[i][j]=q
					m[j][i]=k+1
	printParenthesis(m, noOfMatrix - 1, 0) 
	print("\nOptimal Cost is :", m[0][noOfMatrix - 1]) 

arr=[2,3,4,5,3]
matrixChainMultiplication(arr)
arr=[40, 20, 30, 10, 30]
matrixChainMultiplication(arr)