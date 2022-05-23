#findLeavesOfBinaryTree.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        result=[]
        self.temp_result=[]
        while root.left is not None or root.right is not None:
            self.deleteLeaves(root)
            result.append(self.temp_result)
            self.temp_result=[]
        result.append([root.val])
        return result
            
    def deleteLeaves(self, root):
        if root is None:
            return
        if root.left is not None and self.isLeaf(root.left):
            self.temp_result.append(root.left.val)
            root.left=None
        if root.right is not None and self.isLeaf(root.right):
            self.temp_result.append(root.right.val)
            root.right=None
        self.deleteLeaves(root.left)
        self.deleteLeaves(root.right)
        
    def isLeaf(self,root):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True
        return False

root=TreeNode(1)
root.right=TreeNode(3)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
s=Solution()
print(s.findLeaves(root))