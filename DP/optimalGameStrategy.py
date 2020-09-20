"""
optimalGameStrategy
You are given an array A of size N. The array contains integers and is of even length. The elements of the array represent N coin of values V1, V2, ....Vn. You play against an opponent in an alternating way.

In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin.

You need to determine the maximum possible amouint of money you can win if you go first.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains N denoting the size of the array. The second line contains N elements of the array.

Output:
For each testcase, in a new line, print the maximum amout.
"""
def optimalGameUtil(arr,i,j):
	if j<0 or i>j:
		return 0
	if i==j:
		return arr[i]
	return max(arr[i]+min(optimalGameUtil(arr,i+2,j),optimalGameUtil(arr,i+1,j-1)),
		arr[j]+min(optimalGameUtil(arr,i,j-2),optimalGameUtil(arr,i+1,j-1)))

def optimalGame(arr):
	if arr is None:
		return None
	n=len(arr)
	print(optimalGameUtil(arr,0,n-1))

def optimalGameDP(arr):
	if arr is None:
		return None
	n=len(arr)
	m=[[0 for i in range(n)] for i in range(n)]
	for k in range(n):
		for j in range(k,n):
			i=j-k
			x=m[i+2][j] if (i+2)<=j else 0
			y=m[i+1][j-1] if (i+1)<=(j-1) else 0
			z=m[i][j-2] if i<=(j-2) else 0
			m[i][j]=max(arr[i]+min(x,y),arr[j]+min(y,z))	
			print(k,j,i,x,y,z,arr[i]+min(x,y),arr[j]+min(y,z),m[i][j])		
	for i in range(n):
		print(m[i])
			

arr=[3,1,9,4,5,2]
optimalGame(arr)
optimalGameDP(arr)
"""
arr=[4,7,2,6,2,8,3,4]
optimalGame(arr)
optimalGameDP(arr)
arr=[2,2,2,2]
optimalGame(arr)
optimalGameDP(arr)
"""