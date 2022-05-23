#rotateList
#Given the head of a linked list, rotate the list to the right by k places.
#
#Example 1:
#
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]
#Example 2:
#
#
#Input: head = [0,1,2], k = 4
#Output: [2,0,1]
# 
#
#Constraints:
#
#The number of nodes in the list is in the range [0, 500].
#-100 <= Node.val <= 100
#0 <= k <= 2 * 109

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if None in (head,k):
            return None
        tmp,q=head,[]
        while tmp:
            q.append(tmp)
            tmp=tmp.next
        n=len(q)
        k=k%n
        if k==0:
            return head
        else:
            head=q[n-k]
            q[n-k-1].next=None
            return head
        