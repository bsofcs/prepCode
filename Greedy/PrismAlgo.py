"""
PrismAlgo
"""
class Graph:
	def __init__(self,V):
		self.V=V
		self.graph=[[0 for _ in range(V)] for _ in range(V)]
	def printMST(self,parent):
		print("Edge\tWeight")
		for i in range(1,self.V):
			print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
	def minKey(self, key, mstSet):
		mn=float("INF")
		for v in range(self.V):
			if key[v]<mn and mstSet[v]==False:
				mn=key[v]
				min_index=v
		return min_index
	def prismAlgo(self):
		key=[float("INF")]*self.V
		parent=[None]*self.V
		key[0]=0
		mstSet=[False]*self.V
		parent[0]=-1
		for cout in range(self.V):
			u=self.minKey(key,mstSet)
			mstSet[u]=True
			for v in range(self.V):
				if self.graph[u][v]>0 and mstSet[v]==False and key[v]>self.graph[u][v]:
					key[v]=self.graph[u][v]
					parent[v]=u
					print(u,v,key,parent)
		self.printMST(parent)

g=Graph(5)
g.graph=[ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
g.prismAlgo()
g=Graph(9)
g.graph=[[0,4,0,0,0,0,0,8,0],
	[4,0,8,0,0,0,0,11,0],
	[0,8,0,7,0,4,0,0,2],
	[0,0,7,0,9,14,0,0,0],
	[0,0,0,9,0,10,0,0,0],
	[0,0,4,14,10,0,2,0,0],
	[0,0,0,0,0,2,0,0,6],
	[8,11,0,0,0,0,0,0,7],
	[0,0,2,0,0,0,6,7,0]
	]
g.prismAlgo()


