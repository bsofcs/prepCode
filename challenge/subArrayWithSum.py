"""
subArrayWithSum
"""
def subArrayWithSum(arr,s):
	if arr is None or s is None:
		return None,None
	n=len(arr)
	m={}
	curr=0
	for i in range(n):
		curr+=arr[i]
		if curr==s:
			return 0,i
		if (curr-s) in m:
			return m[curr-s]+1,i
		m[curr]=i
	return None,None

arr=[1,2,3,7,5]
s=12
print(subArrayWithSum(arr,s))