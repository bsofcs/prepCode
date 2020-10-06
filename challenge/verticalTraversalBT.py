"""
verticalTraversalBT

for example if the Tree is as:
		5
	       / \
	      2   4
	     / \   \
	    1   3   6
So the output will be 1,2,5,3,4,6
"""
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def verticalTraversalBT(root):
	if root is None:
		return None
	treeMap=dict()
	pillar=0
	Util(root,pillar,treeMap)
	res=[]
	for index in sorted(treeMap):
		res.extend(treeMap[index])
	return res

def Util(root,pillar,treeMap):
	if root is None:
		return None
	if pillar in treeMap:
		treeMap[pillar].append(root.data)
	else:
		treeMap[pillar]=[root.data]
	Util(root.left,pillar-1,treeMap)
	Util(root.right,pillar+1,treeMap)

root=Node(5)
root.left=Node(2)
root.left.left=Node(1)
root.left.right=Node(3)
root.right=Node(4)
root.right.right=Node(6)
res=verticalTraversalBT(root)
for i in res:
	print(i,end=" ")
print()