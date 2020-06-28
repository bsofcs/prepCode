class Graph:
 def __init__(self,vertices):
  self.vertices=vertices
  self.adjMatrix=[[-1 for i in range(vertices)] for j in range(vertices)]

 def addEdge(self,from_node,to_node,weight):
  self.adjMatrix[from_node][to_node]=weight

 def print_edges(self):
  for i in range(self.vertices):
   for j in range(self.vertices):
    if self.adjMatrix[i][j]!=-1:
     print(f"Path from {i} to {j} is {self.adjMatrix[i][j]}")

 def check_cycle(self):
  grey=[]
  black=[]
  for currentNode in range(self.vertices):
   if currentNode not in black:
    if self.dfs(currentNode,grey,black)==True:
      return True
  return False

 def dfs(self,currentNode,grey,black):
  grey.append(currentNode)
  for n_node in self.adjMatrix[currentNode]:
   if n_node==-1:
    print("Continue for :",n_node)
    continue
   if n_node in black:
    continue
   if n_node in grey:
    return True
   if self.dfs(n_node,grey,black)==True:
    return True
  black.append(currentNode)
  grey.remove(currentNode)
  return False

g = Graph(4) 
g.addEdge(0,1,1) 
g.addEdge(0,2,1) 
g.addEdge(1,2,1) 
g.addEdge(2,0,1) 
g.addEdge(2,3,1) 
g.addEdge(3,3,1)
g.print_edges()
has_cycle="Has Cycle" if(g.check_cycle()) else "No Cycle"
print(has_cycle)


h=Graph(3)
h.addEdge(0,1,1) 
h.addEdge(0,2,1) 
h.addEdge(2,1,1) 
h.print_edges()
print(h.adjMatrix)
has_cycle="Has Cycle" if(h.check_cycle()) else "No Cycle"
print(has_cycle)