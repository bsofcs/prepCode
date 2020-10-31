"""
printBTinWeirdPattern
Print nodes of a Binary Search Tree in Top Level Order and Reversed Bottom Level Order alternately.
Given a BT
InOrder: 5,10,12,20,22,25,28,30,36,38,40,48
PreOrder: 25,20,10,5,12,22,36,30,28,40,38,48

Output: 25 48 38 28 12 5 20 36 40 30 22 10
"""
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def formTreeFromInorderPreorder(InO,PreO):
	if 0 in (len(InO),len(PreO)):
		return None
	#print(InO,PreO)
	rPre=PreO[0]
	indexInO=InO.index(rPre)
	root=Node(rPre)
	#print("Left:",InO[:indexInO],[i for i in InO[:indexInO] if i in PreO])
	#print("Right:",InO[indexInO+1:],[i for i in InO[indexInO+1:] if i in PreO])
	root.left=formTreeFromInorderPreorder(InO[:indexInO],[i for i in PreO if i in InO[:indexInO]])
	root.right=formTreeFromInorderPreorder(InO[indexInO+1:],[i for i in PreO if i in InO[indexInO+1:]])
	return root

def InOrder(root):
	if root is None:
		return
	InOrder(root.left)
	print(root.data,end=" ")
	InOrder(root.right)

def PreOrder(root):
	if root is None:
		return
	print(root.data,end=" ")
	PreOrder(root.left)
	PreOrder(root.right)

def PostOrder(root):
	if root is None:
		return
	PostOrder(root.left)
	PostOrder(root.right)
	print(root.data,end=" ")

def printBTinWeirdPattern(root):
	
"""
	while queue:
		tmp=queue.pop(0) if flag=="Left" else queue.pop(len(queue)-1)
		if tmp=="|":
			flag="Right" if flag=="Left" else "Left"
		else:
			print(tmp,end=" ")
			queue.
"""	

InO=[5,10,12,20,22,25,28,30,36,38,40,48]
PreO=[25,20,10,5,12,22,36,30,28,40,38,48]
print("In:",InO,"\nPre:",PreO)
root=formTreeFromInorderPreorder(InO,PreO)
printBTinWeirdPattern(root)
"""
print("In:[",end="")
InOrder(root)
print("]\nPre:[",end="")
PreOrder(root)
print("]\nPost:[",end="")
PostOrder(root)
print("]")
"""