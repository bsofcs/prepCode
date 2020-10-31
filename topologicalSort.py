"""
topologicalSort
"""
from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.graph=[[] for _ in range(vertices)]
		self.V=vertices
	def addEdge(self,u,v):
		self.graph[u].append(v)
	def topoligicalSortUtil(self,v,visited,stack):
		visited[v]=True
		for i in self.graph[v]:
			if visited[i]==False:
				self.topoligicalSortUtil(i,visited,stack)
		stack.append(v)
	def topologicalSort(self):
		visited=[False]*self.V
		stack=[]
		for i in range(self.V):
			if visited[i]==False:
				self.topoligicalSortUtil(i,visited,stack)
		print(stack[::-1])

g=Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,0)
g.addEdge(1,3)
g.addEdge(3,0)
g.addEdge(2,1)
g.topologicalSort()