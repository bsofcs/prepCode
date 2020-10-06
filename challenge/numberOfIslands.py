"""
numberOfIslands
Given a Matrix consisting of 0s and 1s. Find the number of islands of connected 1s present in the matrix
https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1

Your task is to return the count of number
 of islands in the given boolean grid.

Function Arguments: A (boolean grid), N -> no of rows, M -> no of columns.
Return Type: Integer denoting the number of islands
"""

def numberOfIslands(arr,n,m):
	if arr is None or n is None or m is None or n==0 or m==0:
		return None
	count=0
	i=j=0
	for i in range(n):
		for j in range(m):
			if arr[i][j]==1:
				count+=1
				#print(count,i,j)
				arr=submergeIsland(arr,n,m,i,j)
	return count

def submergeIsland(arr,n,m,x,y):
	move_x=[-1,-1,0,1,1, 1, 0,-1]
	move_y=[ 0, 1,1,1,0,-1,-1,-1]
	if x<0 or x>=n or y<0 or y>=m or arr[x][y]==0:
		return arr
	arr[x][y]=0
	for i in range(8):
		new_x=x+move_x[i]
		new_y=y+move_y[i]
		if new_x in range(0,n) and new_y in range(0,m):
			if arr[new_x][new_y]==1:
				arr=submergeIsland(arr,n,m,new_x,new_y)
	return arr


arr=[[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]]
n,m=len(arr),len(arr[0])
print("numberOfIslands",numberOfIslands(arr,n,m))
arr=[[1,1,0],[0,0,1],[1,0,1]]
n,m=len(arr),len(arr[0])
print("numberOfIslands",numberOfIslands(arr,n,m))
arr=[[1,1,0,0],
[0,0,1,0],
[0,0,0,1],
[0,1,0,0]]
n,m=len(arr),len(arr[0])
print("numberOfIslands",numberOfIslands(arr,n,m))