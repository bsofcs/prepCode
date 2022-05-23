#verticaltraversalTree.py
class Solution:
    def __init__(self):
        self.d=dict()
    
    def verticalOrderList(self,root,mx,mi):
        if root is None:
            return mx,mi
        lmx,lmi,rmx,rmi=float("-INF"),float("INF"),float("-INF"),float("INF")
        if root.left is not None:
            if mi-1 in self.d:
                self.d[mi-1].append(root.left.val)
            else:
                self.d[mi-1]=[root.left.val]
            mi=mi-1
            lmx,lmi=self.verticalOrderList(root.left,mx,mi)
        if root.right is not None:
            if mx+1 in self.d:
                self.d[mx+1].append(root.right.val)
            else:
                self.d[mx+1]=[root.right.val]
            mx+=1
            rmx,rmi=self.verticalOrderList(root.left,mx,mi)
        return max(rmx,lmx),min(rmi,lmi)
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        mx,mi=self.verticalOrderList(root,0,0)
        result=[]
        for i in range(mi,mx+1):
            result.append[self.d[i]]
        return result