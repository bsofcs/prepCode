"""
addTwoNumbersRepresentedInLinkLists

Example: Given are two lists:
l1=4->5->Null
l2=3->4->5->Null
output: 3->9->0->Null
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def makeLL(arr):
	if arr is None:
		return None
	prev=None
	n=len(arr)
	for i in range(n):
		if prev is None:
			head=Node(arr[i])
			prev=head
		else:
			prev.next=Node(arr[i])
			prev=prev.next
	return head

def printLL(head):
	if head is None:
		return None
	tmp=head
	while tmp is not None:
		print(tmp.data,end="->")
		tmp=tmp.next
	print("Null")


def invertLL(head):
	if head is None:
		return None
	prev=None
	stk=[]
	tmp=head
	while tmp:
		stk.append(tmp.data)
		tmp=tmp.next
	while stk:
		if prev is None:
			head=Node(stk.pop())
			prev=head
		else:
			prev.next=Node(stk.pop())
			prev=prev.next
	return head


def addTwoLL(ll1,ll2):
	if ll1 is None or ll2 is None:
		return None
	ll1=invertLL(ll1)
	ll2=invertLL(ll2)
	head=None
	prev=None
	carry=0
	while ll1 and ll2:
		s=ll1.data+ll2.data+carry
		carry=s//10
		if prev is None:
			head=Node(s%10)
			prev=head
		else:
			prev.next=Node(s%10)
			prev=prev.next
		ll1=ll1.next
		ll2=ll2.next
	prev.next=ll1 if ll1 else ll2
	return invertLL(head)

ll1=makeLL([4,5])
ll2=makeLL([3,4,5])
print("LL1:",end="")
printLL(ll1)
print("LL2:",end="")
printLL(ll2)
ans=addTwoLL(ll1,ll2)
printLL(ans)