#swapNodesInK
#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
#Example 1: here k=2
#
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]
#Example 2:
#
#Input: head = []
#Output: []
#Example 3:
#
#Input: head = [1]
#Output: [1]
#
#Constraints:
#
#The number of nodes in the list is in the range [0, 100].
#0 <= Node.val <= 100

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution1:    # when k is always 2: which is faster but very specific to k value
    def swapPairs(self, head):
        if not head or not head.next: return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head
        
class Solution:
    def swapPairs(self, head):
        if head is None:
            return None
        k=2
        if k<=1:
            return head
        tmp=head
        prev=None
        count=0
        stk=[]
        while True:
            if tmp is None and count!=k:
                print("Count:",count)
                break
            elif count<k:
                stk.insert(0,tmp)
                print([i.val for i in stk])
                tmp=tmp.next
                count+=1
            else:
                print("OUT:",[i.val for i in stk])
                if stk:
                    stk[-1].next=None
                tmp1=prev
                print("PREV","None" if prev is None else tmp1.val)
                while stk:
                    if prev is None:
                        prev=stk[-1]
                        head = stk.pop(0)
                        print("Head",head.val)
                        tmp1=head
                    else:
                        print(tmp1.val,[i.val for i in stk])
                        tmp1.next=stk.pop(0)
                        print("tmp1",tmp1.next.val)
                        tmp1=tmp1.next
                    count-=1
                prev=tmp1
        if stk and prev is not None:
            prev.next=stk[-1]
        return head
                
            
    def createLL(self,arr):
        head=None
        tmp=None
        for i in arr:
            if head is None:
                head=ListNode(i)
                tmp=head
            else:
                tmp.next=ListNode(i)
                tmp=tmp.next
        return head
        
    def printLL(self,head):
        if head is None:
            return None
        tmp=head
        while tmp:
            print(tmp.val,end="->")
            tmp=tmp.next
        print("NULL")

s=Solution()        
head = [1,2,3,4,5]
head = s.createLL(head)
print("INPUT:")
s.printLL(head)
print("OUTPUT:")
s.printLL(s.swapPairs(head))