"""
searchNumberInSorted2Darray
Find a number X in a NXN matrix, where every row and column is arranged in sorted increasing order
"""
def searchNumberInSorted2Darray(mat,x):
	if mat is None or x is None:
		return None
	n=len(mat)
	i,j=0,n-1
	while(i<n and j>=0):
		print(mat[i][j])
		if mat[i][j]==x:
			print(f"Found at [{i}][{j}]")
			return
		elif mat[i][j]>x:
			j-=1
		else:
			i+=1
	print("Not present")
mat=[[10, 20, 30, 40],[15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
x=[29,100,11]

for i in range(len(mat)):
	print(mat[i])

for i in x:
	searchNumberInSorted2Darray(mat,i)