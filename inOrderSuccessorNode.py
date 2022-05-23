#inOrder Successor of the Node Given
#wwwwwwwwwwwwwooooooooooooooooooooowwwwwwwwwwwwwwwww answer

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        if root is None or p is None:
            return None
        self.inOrder=[]
        self.buildInOrder(root)
        n=len(self.inOrder)
        ip=self.inOrder.index(p)
        if ip is None or ip==n-1:
            return None
        else:
            return self.inOrder[ip+1]
    
    def buildInOrder(self,root):
        if root is None:
            return
        if root.left:
            self.buildInOrder(root.left)
        self.inOrder.append(root)
        if root.right:
            self.buildInOrder(root.right)
            
    def inorderSuccessor2(self, root,p):
        successor = None
        
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
def findNode(root,i):
    if root is None:
        return None
    if root.val==i:
        return root
    l=findNode(root.left,i)
    r=findNode(root.right,i)
    return l if l else r
    
if __name__=="__main__":
    root=TreeNode(5)
    root.left=TreeNode(4)
    root.left.left=TreeNode(1)
    root.left.left.right=TreeNode(3)
    root.left.left.right.left=TreeNode(2)
    root.right=TreeNode(7)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(9)
    root.right.right.left=TreeNode(8)
    s=Solution()
    for i in range(1,10):
        ir=findNode(root,i)
        print(ir.val)
        result=s.inorderSuccessor2(root,ir)
        if result is None:
            result=None
        else:
            result=result.val
        print("Node: ",i," and it's successor:",result)