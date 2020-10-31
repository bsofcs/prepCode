"""
countAllPossiblePaths
Find the count of all possible paths between any two nodes in a graph
"""
class Graph:
	def __init__(self,V):
		self.V=V
		self.adj=[[] for i in range(V)]
	def addEdge(self, u, v):
		self.adj[u].append(v)
	def countPaths(self, s, d):
		visited=[False]*self.V
		pathCount=[0]
		path=[]
		self.Util(s,d,visited,pathCount)
		visited=[False]*self.V
		self.UtilPath(s,d,visited,path)
		return pathCount[0]
	def Util(self,u,d,visited,pathCount):
		visited[u]=True
		if u==d:
			pathCount[0]+=1
		else:
			i=0
			while i<len(self.adj[u]):
				if not visited[self.adj[u][i]]:
					self.Util(self.adj[u][i],d,visited,pathCount)
				i+=1
		visited[u]=False
	def UtilPath(self,u,d,visited,path):
		visited[u]=True
		path.append(u)
		if u==d:
			print(path)
		else:
			i=0
			while i<len(self.adj[u]):
				if not visited[self.adj[u][i]]:
					self.UtilPath(self.adj[u][i],d,visited,path)
					path.pop(len(path)-1)
				i+=1
		visited[u]=False
g=Graph(4)
g.addEdge(0,1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)
s,d=2,3
print(g.countPaths(s, d))