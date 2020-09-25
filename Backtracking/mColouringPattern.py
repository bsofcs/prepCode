"""
mColouringPattern
Given an undirected graph and a number m, determine if the graph can be coloured with at most m colours such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices.

Input:
1. A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is adjacency matrix representation of the graph. A value graph[i][j] is 1 if there is a direct edge from i to j, otherwise graph[i][j] is 0
2. An integer m which is the maximum number of colors that can be used
"""
def mColouringPattern(graph,m):
	if m is None or graph is None:
		return None
	n=len(graph)
	colour=[0 for i in range(n)]
	if graphColouring(graph,m,0,colour)==False:
		return False
def graphColouring(graph,m,i,colour):
	n=len(colour)
	if i==n:
		if isSafe(graph,colour):
			print(colour)
			return True
		return False
	for k in range(m):
		colour[i]=k+1
		if graphColouring(graph,m,i+1,colour):
			return True
		colour[i]=0
	return False

def isSafe(graph,colour):
	n=len(colour)
	for i in range(n):
		for j in range(n):
			if graph[i][j] and colour[i]==colour[j]:
				return False
	return True
graph=[[0, 1, 1, 1],
	[1, 0, 1, 0],
	[1, 1, 0, 1],
	[1, 0, 1, 0]]
m=3
mColouringPattern(graph,m)