"""
maxDiffNodeToAncestor
"""
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def maxDiff(root,res=float("-INF")):
	if root is None:

		return float("INF"),res
	if root.left is None and root.right is None:
		return root.data,res
	l,res=maxDiff(root.left,res)
	r,res=maxDiff(root.right,res)
	minChild=min(l,r)
	res=max(res,root.data-minChild)
	return minChild,res


root=Node(8)
root.left=Node(3)
root.left.left=Node(1)
root.left.right=Node(6)
root.left.right.left=Node(4)
root.left.right.right=Node(7)
root.right=Node(10)
root.right.right=Node(14)
root.right.right.left=Node(13)
print(maxDiff(root))

root=Node(7)
root.right=Node(23)
root.right.right=Node(13)
root.right.right.right=Node(13)
print(maxDiff(root))

root=Node(7)
root.left=Node(23)
root.left.left=Node(13)
root.left.left.left=Node(0)
print(maxDiff(root))