#mergeKSortedLists
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
#Merge all the linked-lists into one sorted linked-list and return it.
# lists: List[Optional[ListNode]]
#Example 1:
#
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6
#Example 2:
#
#Input: lists = []
#Output: []
#Example 3:
#
#Input: lists = [[]]
#Output: []

# Definition for singly-linked list.

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self,b):
        return self.val<b.val

class HeapNode:
    def __init__(self,listNode:ListNode,idx):
        self.listNode=listNode
        self.idx=idx

class Solution:
    def heapify(self,heapA):
        if heapA is None:
            return
        n=len(heapA)
        for i in range(n):
            smaller=i
            if 2*i+1<n and self.isSmallHeapNode(heapA[2*i+1],heapA[smaller]):
                smaller=2*i+1
            if 2*i+2<n and self.isSmallHeapNode(heapA[2*i+2],heapA[smaller]):
                smaller=2*i+2
            if smaller!=i:
                heapA[smaller],heapA[i]=heapA[i],heapA[smaller]
        print("\nHeap:")
        for i in heapA:
            print(i.listNode.val, end=" ")
        return heapA

    def popHeap(self,heapA): #returns Node and Index
        if len(heapA)<=0:
            return None,None
        n=len(heapA)
        #print("n",n)
        heapA[0],heapA[n-1]=heapA[n-1],heapA[0]
        result=heapA.pop(n-1)
        print("\n POP:",result.listNode.val,result.idx,end="")
        heapA=self.heapify(heapA) 
        print("POPPED")        
        return result.listNode,result.idx
        
    def pushHeap(self,heapA,listNode,idx):
        if None in (idx,listNode):
            return None
        print("\n PUSH:",listNode.val,end="")
        heapA.insert(0,HeapNode(listNode,idx))
        heapA=self.heapify(heapA)
        return heapA
        
    def isSmallHeapNode(self,heapNode1,heapNode2):
        if None in (heapNode1,heapNode2):
            return None
        return True if heapNode1.listNode.val<heapNode2.listNode.val else False
        
    def hasItem(self,lists):
        if lists is None:
            return False
        for i in lists:
            if i is not None:
                print("Has Elements:",i.val)
                return True
        return False
        
    def mergeKLists(self, lists):
        #create min heap
        heapA=[]
        result=None
        tmp=None
        if all(v is None for v in lists):
            return None
        n=len(lists)
        l=[i for i in lists if i is not None]
        lists=l
        if len(lists)<=0:
            return
        if len(lists)==1:
            return lists[0]
        for i in range(len(lists)):
            heapA.insert(0,HeapNode(lists[i],i))
            lists[i]=lists[i].next
            heapA=self.heapify(heapA)
        while self.hasItem(lists):
            tmpPop,idx=self.popHeap(heapA)
            if result is None:
                result=tmpPop
                tmp=tmpPop
            else:
                tmp.next=tmpPop
                tmp=tmp.next
            if tmpPop.next is not None and idx<len(lists):
                heapA=self.pushHeap(heapA,lists[idx],idx)
                lists[idx]=lists[idx].next
        while heapA:
            tmpPop,idx=self.popHeap(heapA)
            if result is None:
                result=tmpPop
                tmp=tmpPop
            else:
                tmp.next=tmpPop
                tmp=tmp.next
        return result

class Solution1:    
    def hasItem(self,lists):
        if lists is None:
            return None
        return False if all(i is None for i in lists) else True

    def mergeKLists(self, lists):
        l=[i for i in lists if i is not None]
        lists=l
        n=len(lists)
        if lists is None or n==0: return None
        if n==1: return lists[0]
        heapA=[]
        for i in range(n):
            heapA.append((lists[i],i))
            lists[i]=lists[i].next
        heapq.heapify(heapA)
        result=None
        tmpN=None
        while self.hasItem(lists):
            tmp,idx=heapq.heappop(heapA)
            if lists[idx] is not None:
                heapq.heappush(heapA,(lists[idx],idx))
                lists[idx]=lists[idx].next
            if result is None:
                result=tmp
                tmpN=tmp
            else:
                tmpN.next=tmp
                tmpN=tmpN.next
        while heapA:
            tmp,idx=heapq.heappop(heapA)
            if result is None:
                result=tmp
                tmpN=tmp
            else:
                tmpN.next=tmp
                tmpN=tmpN.next
        return result


class Solution2:    #using Merge sort
    def mergeKLists(self, lists):
        l=[i for i in lists if i is not None]
        lists=l
        n=len(lists)
        if lists is None or n==0: return None
        if n==1: return lists[0]
        return self.mergeKListsUtil(lists)
        
    def mergeKListsUtil(self,lists):
        if lists is None:
            return None
        n=len(lists)
        if n==1:
            return lists[0]
        mid=n//2
        left=self.mergeKListsUtil(lists[:mid])
        right=self.mergeKListsUtil(lists[mid:])
        result,prev=None,None
        while left is not None and right is not None:
            if left.val<right.val:
                tmp=left
                left=left.next
            else:
                tmp=right
                right=right.next
            if result is None:
                result=tmp
                prev=tmp
            else:
                prev.next=tmp
                prev=prev.next
        if left:
            prev.next=left
        if right:
            prev.next=right
        return result

def converArrayToLists(arr):
    if arr is None:
        return None
    head=None
    tmp=None
    for i in arr:
        if head is None:
            head = ListNode(i)
            tmp=head
        else:
            tmp.next=ListNode(i)
            tmp=tmp.next
    return head


s=Solution2()
if __name__=="__main__":
    lists_arr = [[-5,-4,-3,-1,0,3,3],[3,4],[-5,-3,-1,3],[-8,-6]]
    lists=[]
    for i in lists_arr:
        lists.append(converArrayToLists(i))
    head=s.mergeKLists(lists)
    while head is not None:
        print(head.val,end="=>")
        head=head.next
    print("NULL")
    
    