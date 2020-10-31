"""
minimumDistanceBw2NodeInBT

Distance(n1,n2)=Distance(root,n1)+Distance(root,n2)-2*Distance(root,lca)
"""
class Node:
	def __init__(self,val):
		self.data=val
		self.left=None
		self.right=None

def lca(root,p,q):
	if None in (root,p,q):
		return
	if root.data==p or root.data==q:
		return root
	left=lca(root.left,p,q)
	right=lca(root.right,p,q)
	if left and right:
		return root
	return left if left else right

def pathFromRoot(root,a):
	if None in (root,a):
		return 0
	if root.data==a:
		return 1
	left=pathFromRoot(root.left,a)
	right=pathFromRoot(root.right,a)
	tmp=max(left,right) 
	return 1+tmp if tmp!=0 else 0

def minimumDistanceBw2NodeInBT(root,a,b):
	if None in (root,a,b):
		return
	pathA=pathFromRoot(root,a)
	pathB=pathFromRoot(root,b)	
	l=lca(root,a,b)
	pathLCA=pathFromRoot(root,l.data)
	#print(pathA,pathB,pathLCA)
	return (pathA+pathB-2*pathLCA)

root=Node(2)
root.left=Node(1)
root.right=Node(3)
print("1,3:",minimumDistanceBw2NodeInBT(root,1,3))
root.left.left=Node(4)
root.right.right=Node(6)
root.right.left=Node(7)
root.right.left.right=Node(8)
root.right.left.right.left=Node(9)
print("1,9:",minimumDistanceBw2NodeInBT(root,1,9))