#addTwoNumbers.py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        head1=l1
        head2=l2
        carry=0
        resulthead=None
        resulttmp=None
        resultPre=None
        while(head1 is not None and head2 is not None):
            resultPre=resulttmp
            result=head1.val+head2.val+carry
            carry=result//10
            result=result%10
            resulttmp=ListNode(result)
            if resulthead is None:
                resulthead=resulttmp
            else:
                resultPre.next=resulttmp
            head1=head1.next
            head2=head2.next
        while head1 is not None:
            resultPre=resulttmp
            result=head1.val+carry
            carry=result//10
            result=result%10
            resulttmp=ListNode(result)
            resultPre.next=resulttmp
            head1=head1.next
        while head2 is not None:
            resultPre=resulttmp
            result=head2.val+carry
            carry=result//10
            result=result%10
            resulttmp=ListNode(result)
            resultPre.next=resulttmp
            head2=head2.next
        if carry>0:
            if resultPre is not None:
                resultPre.next.next=ListNode(carry)
            else:
                resulthead.next=ListNode(carry)
        tmp=resulthead
        return resulthead
        