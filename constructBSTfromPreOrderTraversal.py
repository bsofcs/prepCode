# constructBSTfromPreOrderTraversal

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstFromPreorderTree(self, preorder):
        if preorder is None:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        if len(preorder)==2 and preorder[0]>preorder[1]:
            root=TreeNode(preorder[0])
            root.left=TreeNode(preorder[1])
            return root
        if len(preorder)==2 and preorder[1]>preorder[0]:
            root=TreeNode(preorder[0])
            root.right=TreeNode(preorder[1])
            return root
        root=TreeNode(preorder[0])
        print("Start:",preorder)            
        for i in range(1,len(preorder)):
            if preorder[0]<preorder[i]:
                print(preorder[0],preorder[i],i,preorder[1:i])
                if i>1:
                    root.left=self.bstFromPreorderTree(preorder[1:i])
                if i<len(preorder):
                    root.right=self.bstFromPreorderTree(preorder[i:])
                break
        if root.left is None and root.right is None:
            root.left=self.bstFromPreorderTree(preorder[1:])
        return root
        
    def bstFromPreorder(self, preorder):
        if preorder is None:
            return None
        root=self.bstFromPreorderTree(preorder)
        if root is None:
            return None
        que=[root]
        result=[]
        while que:
            if que[0] is None:
                result.append(None)
                que.pop(0)
                continue
            if que[0].left is not None or que[0].right is not None:
                que.append(que[0].left)
                que.append(que[0].right)
            tmp=que.pop(0)
            result.append(tmp.val)
        return result
            


if __name__=='__main__':
    preorder=[4,2]
    s=Solution()
    print("RESULT:",s.bstFromPreorder(preorder))
    preorder=[8,5,1,7,10,12]
    s=Solution()
    print("RESULT:",s.bstFromPreorder(preorder))
    preorder=[1,2,3]
    s=Solution()
    print("RESULT:",s.bstFromPreorder(preorder))