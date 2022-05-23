#sortInMemoryLinkList
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.merge(*map(self.sortList, (head, slow)))
    
    def makeLL(self,arr):
        if arr is None:
            return None
        head=tmp=None
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
            return
        tmp=head
        while tmp:
            print(tmp.val,end="->")
            tmp=tmp.next
        print("None")

s=Solution()
arr=[4,2,1,3]
head=s.makeLL(arr)
s.printLL(head)
head=s.sortList(head)
s.printLL(head)