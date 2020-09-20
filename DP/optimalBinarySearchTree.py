"""
optimalBinarySearchTree

Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the number of searches to keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.

"""

def optimalBinarySearchTree(keys,freq):
	if keys is None or freq is None or len(keys)!=len(freq):
		return None
	n=len(keys)
	m=[[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		m[i][i]=freq[i]
	for k in range(2,n+1):
		for i in range(n-k+2):
			j=i+k-1
			if i>=n or j>=n:
				break
			m[i][j]=float("INF")
			for head in range(i,j+1):
				leftTree=m[i][head-1] if head>i else 0
				rightTree=m[head+1][j] if head<j else 0
				print(k,i,j,head,leftTree,rightTree,m[i][j])
				m[i][j]=min(m[i][j],leftTree+rightTree+sum(freq[i:j+1]))
	for i in range(n):
		print(m[i])

keys = [10, 12, 16,21] 
freq = [4,2,6,3]
optimalBinarySearchTree(keys,freq)