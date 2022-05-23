# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
#sumOfNodesWithEvenValuedGrandParent
# Definition for a binary tree node.

#
#
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def nvl(self,a,b):
        if a is None:
            return b
        #print(a.val)
        return a.val
        
    def sumEvenGrandparent(self, root):
        if root is None:
            return 0
        result=0
        if root.val%2==0:
            if root.left is not None:
                result+=self.nvl(root.left.left,0)+self.nvl(root.left.right,0)
            if root.right is not None:
                result+=self.nvl(root.right.left,0)+self.nvl(root.right.right,0)
        return result+self.sumEvenGrandparent(root.left)+self.sumEvenGrandparent(root.right)
        
if __name__=='__main__':
    root=TreeNode(6)
    root.left=TreeNode(7)
    root.left.left=TreeNode(2)
    root.left.left.left=TreeNode(9)
    root.left.right=TreeNode(7)
    root.left.right.left=TreeNode(1)
    root.left.right.right=TreeNode(4)
    root.right=TreeNode(8)
    root.right.left=TreeNode(1)
    root.right.right=TreeNode(3)
    root.right.right.right=TreeNode(5)
    s=Solution()
    print(s.sumEvenGrandparent(root))
