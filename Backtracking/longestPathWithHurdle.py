"""
longestPathWithHurdle
Find the longest path in 2D matrix having 1's and 0's where 1 is pass and 0 is stop.
The path cannot move in any diagonal path i.e. only left, right, top and bottom
"""
def longestPathWithHurdle(arr):
	if arr is None:
		return
	n=len(arr)
	m=len(arr[0])
	print(n,m)
	visited=[[False for _ in range(m)] for _ in range(n)]
	count=longestPathUtil(arr,visited,0,0,n,m)
	print(count)

def longestPathUtil(arr,visited,x,y,n,m):
	if None in (arr,visited,x,y,n,m):
		return
	if x==n-1 and y==m-1:
		return(True,1)
	visited[x][y]=True
	left=right=top=bottom=float("-INF")
	result,sol=float("-INF"),False
	if y-1>=0 and arr[x][y-1]!=0 and visited[x][y-1]==False:
		sol,left=longestPathUtil(arr,visited,x,y-1,n,m)
		result=max(result,left) if sol else result
	if y+1<m and arr[x][y+1]!=0 and visited[x][y+1]==False:
		sol,right=longestPathUtil(arr,visited,x,y+1,n,m)
		result=max(result,right) if sol else result
	if x-1>=0 and arr[x-1][y]!=0 and visited[x-1][y]==False:
		sol,top=longestPathUtil(arr,visited,x-1,y,n,m)
		result=max(result,top) if sol else result
	if x+1<n and arr[x+1][y]!=0 and visited[x+1][y]==False:
		sol,bottom=longestPathUtil(arr,visited,x+1,y,n,m)
		result=max(result,bottom) if sol else result
	if left==-1 and right==-1 and top==-1 and bottom==-1:
		return 1
	visited[x][y]=False
	if result==float("-INF"):
		return(False,float("INF"))
	return(True,1+result)

arr=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
longestPathWithHurdle(arr)