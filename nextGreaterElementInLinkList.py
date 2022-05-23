#nextGreaterElementInLinkList
class LinkListNode:
    def __init__(self,val):
        self.val=val
        self.next=None


class nextGreaterElementInLinkList:
    def revLinkList(self,head):
        if head is None:
            return None
        pre=None
        curr=head
        nxt=curr.next
        while(curr):
            curr.next=pre
            pre=curr
            curr=nxt
            nxt=None if nxt is None else nxt.next
        head=pre
        return head
        
    def printList(self,head):
        if head is None:
            return None
        tmp=head
        print()
        while(tmp):
            print(tmp.val,end="->")
            tmp=tmp.next
        print("None")
            
    def nextGreaterElement(self,head):
        if head is None:
            return None
        revHead=self.revLinkList(head)
        st,result=[],[]
        tmp=revHead
        while(tmp):
            if len(st)==0:
                result=[0]
                st.append(tmp.val)
            else:
                while(len(st)!=0 and st[-1]<=tmp.val):
                    st.pop()
                if len(st)==0:
                    st=[tmp.val]
                    result.append(tmp.val)
                else:
                    result.append(st[-1])
                    st.append(tmp.val)
            tmp=tmp.next
        return result[::-1]

#2->1->3->0->5 
head=LinkListNode(2)
head.next=LinkListNode(1)
head.next.next=LinkListNode(3)
head.next.next.next=LinkListNode(0)
head.next.next.next.next=LinkListNode(5)
s=nextGreaterElementInLinkList()
s.printList(head)
print(s.nextGreaterElement(head))

#4->3->1->5->7->9
head=LinkListNode(4)
head.next=LinkListNode(3)
head.next.next=LinkListNode(1)
head.next.next.next=LinkListNode(5)
head.next.next.next.next=LinkListNode(7)
head.next.next.next.next.next=LinkListNode(9)
s.printList(head)
print(s.nextGreaterElement(head))
