# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        if head is None or k is None or k==0:
            return None
        tmp=head
        prev=None
        while tmp:
            i=0
            stk=[]
            while i<k and tmp:
                stk.append(tmp)
                i+=1
                tmp=tmp.next
            while stk:
                if tmp or i==k:
                    if prev is None:
                        prev=stk.pop()
                        head=prev
                    else:
                        prev.next=stk.pop()
                        prev=prev.next
                else:
                    if prev is None:
                        prev=stk.pop(0)
                        head=prev
                    else:
                        prev.next=stk.pop(0)
                        prev=prev.next
        prev.next=None
        return head

def printLL(head):
    if head is None:
        return
    tmp=head
    while tmp:
        print(tmp.val,end="->")
        tmp=tmp.next
    print("None")
    
def makeLL(n):
    if n is None:
        return None
    prev=None
    head=None
    for i in range(n):
        if prev is None:
            prev=ListNode(i+1)
            head=prev
        else:
            prev.next=ListNode(i+1)
            prev=prev.next
    return head
    
# 1->2->3->.....->25->None

if __name__=="__main__":
    l,k=25,3
    s=Solution()
    head=makeLL(25)
    printLL(head)
    head=s.reverseKGroup(head,k)
    printLL(head)
    head=s.reverseKGroup(head,k)
    printLL(head)