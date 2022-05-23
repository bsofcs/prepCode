def clonning2D(arr):
 len_r=len(arr)
 len_c=len(arr[0])
 new_arr=[[arr[i][j] for j in range(len_c)] for i in range(len_r)]
 return new_arr

class Graph:
 def __init__(self,vertices):
  self.vertices=vertices
  self.adjMatrix=[[0 for i in range(vertices)] for j in range(vertices)]

 def addEdge(self,from_node,to_node):
  self.adjMatrix[from_node][to_node]=1

 def print_edges(self,lst_a):
  for i in range(self.vertices):
   for j in range(self.vertices):
    if self.adjMatrix[i][j]!=0:
     print(f"Path from {lst_a[i]} to {lst_a[j]} is {self.adjMatrix[i][j]}")

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

 def semesterListSubWise(self):
  visited=[False]*self.vertices
  stack=[]
  for i in range(self.vertices):
   if visited[i]==False:
    self.topologicalSort(i,visited,stack)
  return(stack[::-1])

 def topologicalSort(self,v,visited,stack):
  visited[v]=True
  for i in self.adjMatrix[v]:
   if visited[i]==False and self.adjMatrix[v][i]==1:
    self.topologicalSort(i,visited,stack)
  stack.insert(0,v)


lst_a=['C','DS','OS','CO','Algo','Design','Programming']
lst_b=[['C','CO'],['OS','CO'],['DS','Algo'],['Design','Programming']]
print(lst_a,lst_b)

