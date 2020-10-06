"""
duplicateSubTreeWthHeight2
"""

def dupSub(root):

    # Code here

    if root is None:

        return None

    stk=[root]

    res=[]

    d=dict()

    while stk:

        t=stk.pop()

        if t=="NA":

            res.append("NA")

            continue

        res.append(t.data)

        if not t.right and t.left:

            stk.append("NA")

        if t.right:

            stk.append(t.right)

        if not t.left and t.right:

            stk.append("NA")

        if t.left:

            stk.append(t.left)

    n=len(res)

    mx=-1

    m=[[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1,n+1):

        for j in range(1,n+1):

            if res[i-1]==res[j-1] and i<j:

                m[i][j]=m[i-1][j-1]+1
                mx=max(mx,m[i][j])

    return 0 if mx<2 else 1