#removeDuplicatesFromSortedList2
#Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
#
#Example 1:
#
#Input: head = [1,2,3,3,4,4,5]
#Output: [1,2,5]
#Example 2:
#
#Input: head = [1,1,1,2,3]
#Output: [2,3]
#
#Constraints:
#
#The number of nodes in the list is in the range [0, 300].
#-100 <= Node.val <= 100
#The list is guaranteed to be sorted in ascending order.

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        tmp=head
        q,flag=[],1
        while tmp:
            #print([i.val for i in q],tmp.val)
            if not q:
                q.append(tmp)
            else:
                while tmp and tmp.val==q[-1].val:
                    flag=0
                    tmp=tmp.next
                if not flag:
                    q.pop(-1)
                    flag=1
                if q:
                    q[-1].next=tmp
                    q.append(tmp)
                else:
                    q=[tmp]
            tmp=tmp.next if tmp else None
        return q[0] if q else None
        
    def deleteDuplicates1(self, head):
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next   