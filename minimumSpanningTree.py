"""
minimumSpanningTree

Given a weighted, undirected and connected graph. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.


V: nodes in graph

E: number of edges in graph

graph: adjacency matrix, graph[i][j]=weight, if edge exits , else float("inf").

"""

def findNext(graph,visited,V,key):

	minVal=float("INF")

	minIndex=-1

	for i in range(V):
		if key[i]<minVal and i not in visited:
			minIndex=i

			minVal=key[i]

	return minIndex



def spanningTree(V, E, graph):

	if V is None or E is None or graph is None:

		return

	visited=set()

	key=[float("INF")]*V

	key[0]=0
	result=0

	for i in range(V):

		u=findNext(graph,visited,V,key)

		visited.add(u)
		for v in range(V):

		    if graph[u][v]>0 and v not in visited and key[v]>graph[u][v]:

		        key[v]=graph[u][v]

	result=sum(key)
	return result

V=2
E=1
graph=[[0,5],[5,0]]
print(spanningTree(V, E, graph))

V=3
E=3
graph=[[0,5,1],[5,0,3],[1,3,0]]
print(spanningTree(V, E, graph))