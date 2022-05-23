# Definition for a binary tree node.
#constructBTfromInorderPostorder
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        rootVal=postorder[len(postorder)-1]
        root=TreeNode(rootVal)
        leftInOrder=inorder[:inorder.index(rootVal)]
        rightInOrder=inorder[inorder.index(rootVal)+1:]
        leftPostOrder,rightPostOrder=[],[]
        for i in postorder:
            if i in leftInOrder:
                leftPostOrder.append(i)
            if i in rightInOrder:
                rightPostOrder.append(i)
        if len(leftInOrder)>0:
            leftChild=self.buildTree(leftInOrder,leftPostOrder)
            root.left=leftChild
        if len(rightInOrder)>0:
            rightChild=self.buildTree(rightInOrder,rightPostOrder)
            root.right=rightChild
        return root
    def buildTree1(self,inorder,postorder):
        if not inorder or not postorder:
            return None
        root=TreeNode(postorder[-1])
        idx=inorder.index(postorder[-1])
        root.left=self.buildTree1(inorder[:idx],postorder[:idx])
        root.right=self.buildTree1(inorder[idx+1:],postorder[idx:len(postorder)-1])
        return root
        
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.val,end=" ")
    printInorder(root.right)
    
def printPostOrder(root):
    if root is None:
        return
    printPostOrder(root.left)
    printPostOrder(root.right)
    print(root.val,end=" ")
        
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
s=Solution()
root=s.buildTree(inorder,postorder)
printInorder(root)
print()
printPostOrder(root)