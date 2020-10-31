"""
KruskalAlgo
used for undirected edged graph
"""
class Graph:
	def __init__(self,V):
		self.V=V
		self.graph=[]
	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])
	def find(self,parent,i):
		if parent[i]==i:
			return i
		return self.find(parent,parent[i])
	def union(self,parent,rank,x,y):
		xroot=self.find(parent,x)
		yroot=self.find(parent,y)
		if rank[xroot]<rank[yroot]:
			parent[xroot]=yroot
		elif rank[xroot]>rank[yroot]:
			parent[yroot]=xroot
		else:
			parent[yroot]=xroot
			rank[xroot]+=1
		print("Parent:",parent,"\nRank:",rank)
	def Kruskal(self):
		result=[]
		i=e=0
		self.graph=sorted(self.graph,key=lambda x:x[2])
		parent=[i for i in range(self.V)]
		rank=[0 for i in range(self.V)]
		while e<self.V-1:
			u,v,w=self.graph[i]
			i+=1
			x=self.find(parent,u)
			y=self.find(parent,v)
			print("U,V,X,Y:",u,v,x,y)
			if x!=y:
				e+=1
				result.append([u,v,w])
				self.union(parent,rank,x,y)
		minimumCost=0
		print("Edges in the constructed MST")
		for u,v,w in result:
			minimumCost+=w
			print(f"({u},{v},{w})")
		print("Minimum Spanning Tree:",minimumCost)

g=Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.Kruskal()

g=Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 7, 11)
g.addEdge(1, 2, 8)
g.addEdge(7, 8, 7)
g.addEdge(7, 6, 1)
g.addEdge(8, 6, 6)
g.addEdge(6, 5, 2)
g.addEdge(2, 8, 2)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)
g.addEdge(3, 5, 14)
g.addEdge(3, 4, 9)
g.addEdge(5, 4, 10)
g.Kruskal()