"""
alienDict
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
		return(stack[::-1])
def alienDict(words,alpha):
	if None in (words,alpha):
		return
	g=Graph(alpha)
	n=len(words)
	for i in range(n-1):
		word1,word2=words[i],words[i+1]
		len_w1,len_w2=len(word1),len(word2)
		for j in range(min(len_w1,len_w2)):
			if word1[j]!=word2[j]:
				g.addEdge(ord(word1[j])-ord('a'),ord(word2[j])-ord('a'))
				break
	print(g.graph)
	res=g.topologicalSort()
	for i in res:
		print(chr(i+ord('a')),end="->")
	print("End")


words=["baa", "abcd", "abca", "cab", "cad"]
alpha=4
alienDict(words,alpha)