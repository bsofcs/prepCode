class Graph:
 def __init__(self,graph_dict={}):
  self.graphDict=graph_dict
 def vertices(self):
  return(list(self.graphDict.keys()))
 def edges(self):
  for node in list(self.graphDict.keys()):
   for target in self.graphDict[node]:
    print("Edge from {} to {}".format(node,target))
 def add_vertex(self,vertex):
  if vertex not in self.graphDict:
   self.graphDict[vertex]=[]
 def add_edges(self,edge):
  edge=set(edge)
  (vertex1,vertex2)=tuple(edge)
  if vertex1 in self.graphDict:
   self.graphDict[vertex1].append(vertex2)
  else:
   self.graphDict[vertex1]=[vertex2]
 def check_for_path(self,source,destination,path=[]):
  graph=self.graphDict
  path=path+[source]
  if source==destination:
   return path
  for vertex in graph[source]:
   if vertex not in path:
    extendedPath=self.check_for_path(vertex,destination,path)
    if extendedPath:
     return extendedPath
  return None

g_dict={"a":["b","c"],"b":["d","e"],"c":["d","e"],"d":["e"],"e":["a"]}
g=Graph(g_dict)
print("Vertices:")
print(g.vertices())
print("Edges:")
g.edges()
print("Path between ""a"" and ""e"":")
print(g.check_for_path("a","e"))
print("Path between ""a"" and ""d"":")
print(g.check_for_path("a","d"))
print("Path between ""d"" and ""a"":")
print(g.check_for_path("d","a"))