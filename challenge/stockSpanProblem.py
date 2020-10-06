"""
stockSpanProblem
https://practice.geeksforgeeks.org/problems/stock-span-problem/0
"""
def stockSpanProblem(arr):
	if arr is None:
		return None
	n=len(arr)
	res=[0]*n
	for i in range(n-1,-1,-1):
		j=i-1
		currSpan=1
		while arr[j]<=arr[i] and j>=0:
			currSpan+=1
			j-=1
		res[i]=currSpan
	return res

arr=list(map(int,"100 80 60 70 60 75 85".split()))
print("Input:",arr)
print("Output:",stockSpanProblem(arr))