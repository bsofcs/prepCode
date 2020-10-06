"""
copyLLwithRND
You are given a Singly Linked List with N nodes where each node next pointing to its next node. You are also given M random pointers , where you will be given M number of pairs denoting two nodes a and b  i.e. a->arb = b
"""
class Node:
	def __init__(self,val):
		self.data=val
		self.next=None
		self.abr=None

def printLL(head):
	if head is None:
		return
	tmp=head
	while tmp:
		print("{",tmp.data,":{",end="")
		if tmp.abr:
			print(tmp.abr.data,end="")
		print("}}->",end="")
		tmp=tmp.next
	print("None")

def cloneLL(head):
	if head is None:
		return
	tmp=head
	prev=None
	prev1=None
	while tmp:
		prev=tmp
		tmp1=Node(tmp.data)
		if prev1 is not None:
			prev1.next=tmp1
		prev1=tmp1	
		tmp=tmp.next
		prev.next=tmp1
		tmp1.abr=prev
	head1=head.next
	tmp=head
	tmp1=head1
	while tmp:
		if tmp.abr is not None:
			tmp.next=tmp1.next.abr
			tmp1.abr=tmp.abr.next
			tmp1=tmp1.next
			tmp=tmp.next
			continue
		if tmp1.next is None:
			tmp.next=None
			break
		tmp.next=tmp1.next.abr
		tmp=tmp.next
		tmp1=tmp1.next
	tmp1=head1
	prev=None
	while tmp1:
		if tmp1.abr.data==tmp1.data:
			tmp1.abr=None
		tmp1=tmp1.next
	return head1
			
def cloneLLTry1(head):
	if head is None:
		return None
	di=dict()
	tmp=head
	prev=None
	while tmp:
		copy=Node(tmp.data)
		di[tmp]=copy
		if prev is not None:
			prev.next=copy
		prev=copy
		tmp=tmp.next
	head1=di[head]
	tmp=head
	tmp1=None
	while tmp:
		tmp1=di[tmp]
		if tmp.abr:
			tmp1.abr=di[tmp.abr]
		tmp=tmp.next
	return head1
root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)
root.abr=root.next.next
root.next.abr=root.next.next.next
printLL(root)
root1=cloneLL(root)
print("Cloned")
printLL(root1)
printLL(root)
root1=cloneLLTry1(root)
printLL(root1)
