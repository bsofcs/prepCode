"""
reverseLinkListPerKNodes
For example:
Input: 2->3->4->6->1->9->3->8->5->2->Null
K=4
Output: 6->4->3->2->8->3->9->1->2->5->Null
"""
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

def makeLinkList(arr):
	if arr is None:
		return None
	n=len(arr)
	prev=Node(arr[0])
	head=prev
	for i in range(1,n):
		tmp=Node(arr[i])
		prev.next=tmp
		prev=tmp
	return head

def printLL(head):
	if head is None:
		return None
	tmp=head
	while tmp!=None:
		print(tmp.data,end="->")
		tmp=tmp.next
	print("Null")

def reverse(head, k):
	if head is None or k is None:
		return None
	tmp=head
	prev=None
	stck=[]
	while tmp is not None:
		i=0
		while i<k and tmp is not None:
			stck.append(tmp.data)
			tmp=tmp.next
			i+=1
		while stck:
			if prev is None:
				prev=Node(stck.pop())
				head=prev
			else:
				prev.next=Node(stck.pop())
				prev=prev.next
	prev.next=None
	return head
			

arr=[2,3,4,6,1,9,3,8,5,12]
head=makeLinkList(arr)
print(arr)
printLL(head)
head=reverse(head, 4)
printLL(head)