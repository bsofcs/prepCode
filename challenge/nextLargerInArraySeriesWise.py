"""
nextLargerInArraySeriesWise

https://practice.geeksforgeeks.org/problems/next-larger-element/0
"""

def nextLargerInArraySeriesWise(arr):
	if arr is None:
		return None
	n=len(arr)
	res=[-1]*n
	for i in range(n):
		for j in range(i+1,n):
			if arr[i]<arr[j]:
				res[i]=arr[j]
				break
	return res

#with better Execution Time
def nextLargerInArraySeriesWise2(arr):
	if arr is None:
		return None
	n=len(arr)
	res=[-1]*n
	st=[arr[n-1]]
	for i in range(n-2,-1,-1):
		if arr[i]<=st[-1]:
			res[i]=st[-1]
		else:
			while st[-1]<arr[i]:
				st.pop()
				if not st: break
			if st:
				res[i]=st[-1]
		st.append(arr[i])
	return res

arr=[4,3,2,1]
print(nextLargerInArraySeriesWise(arr))
print(nextLargerInArraySeriesWise2(arr))