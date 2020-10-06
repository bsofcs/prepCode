"""
convertBT2DLL
"""
class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

class LLNode:
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None

def PreOrder(root):
	if root is None:
		return None
	print(root.data,end=" ")
	PreOrder(root.left)
	PreOrder(root.right)

def InOrder(root):
	if root is None:
		return None
	InOrder(root.left)
	print(root.data,end=" ")
	InOrder(root.right)

def printDLLfromL2R(head):
	if head is None:
		return None
	tmp=head
	print("Null<=>",end="")
	while tmp:
		print(tmp.data,end="<=>")
		tmp=tmp.next
	print("Null")

def printDLLfromR2L(head):
	if head is None:
		return None
	tmp=head
	while tmp.next:
		tmp=tmp.next
	print("Null<=>",end="")
	while tmp:
		print(tmp.data,end="<=>")
		tmp=tmp.prev
	print("Null")

def makeDLLfromBT(root):
	if root is None:
		return None
	head=makeDLLfromBT(root.left)
	left=head
	if left:
		while left.next:
			left=left.next
	right=makeDLLfromBT(root.right)
	if head:
		tmp=LLNode(root.data)
		left.next=tmp
		tmp.prev=left
		tmp.next=right
		if right: 
			right.prev=tmp
	else:
		head=LLNode(root.data)
		head.next=right
		if right:
			right.prev=head
	return head
	

root=TreeNode(5)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.right=TreeNode(3)
root.left.left=TreeNode(1)
root.right.right=TreeNode(6)
print("InOrder:",end="")
InOrder(root)
print("\nPreOrder:",end="")
PreOrder(root)
head=makeDLLfromBT(root)
print("\nLink List:")
printDLLfromL2R(head)
printDLLfromR2L(head)





